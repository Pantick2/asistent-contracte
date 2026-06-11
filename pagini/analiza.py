import streamlit as st
from google import genai
from google.genai import types
import docx
import pypdf

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

# Initializam starea acceptului in sesiune
if "termeni_acceptati" not in st.session_state:
    st.session_state.termeni_acceptati = False

# Dicționar de traduceri pentru interfața de analiză și sistemul de bifare
t = {
    "RO": {
        "titlu": "📄 Asistent de Negociere pentru Freelanceri",
        "subtitlu": "Protejează-ți business-ul. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "avertisment_b2b": "⚠️ **Utilizare B2B Exclusivă:** Această platformă este un instrument experimental destinat exclusiv profesioniștilor (freelanceri/firme).",
        "bifa_text": "Am citit, înțeleg și sunt de acord în mod expres cu Termenii, Condițiile de Utilizare și Politica de Confidențialitate (GDPR).",
        "blocat_text": "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        "ghid": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un **copilot de negociere**. Informațiile generate sunt **strict orientative**. Acest instrument NU oferă asistență juridică sau consultanță de avocat. Aplicația aplică o politică de **zero stocare**.",
        "c1": "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale încâlcite în idei simple.",
        "c2": "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele de plată.",
        "c3": "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        "side_s": "Cheie personală activă.",
        "side_d": "Modul DEMO activ",
        "up_t": "Trage sau încarcă contractul (PDF, DOCX, TXT):",
        "tx_t": "Sau introdu textul clauzelor suspecte manual:",
        "disc": "🔒 **Securitate & Disclaimer:** Conținutul documentelor nu este stocat sau folosit pentru antrenarea modelelor publice. Această analiză automată are rol informativ și nu înlocuiește sfatul unui avocat.",
        "b_start": "Pornește Analiza Inteligentă",
        "e_limita": "⚠️ Limita demo a fost atinsă!",
        "e_text": "Te rugăm să introduci text sau să încarci un document.",
        "e_config": "Sistemul Demo nu este configurat!",
        "spinner": "AI-ul scanează textul pentru riscuri legale...",
        "succes": "Analiză finalizată cu succes!",
        "rap_t": "## 🔍 Raport de Audit Contractual",
        "b_down": "Descarcă Raportul (.txt)",
        "prompt": "Ești un expert juridic specializat în protecția freelancerilor. Analizează textul contractului oferit și identifică riscurile majore. Răspunde STRICT în limba ROMÂNĂ. Returnează rezultatul în format Markdown, cu structura: ### 🚩 [Nume Risc], Clauză originală, Traducere, De ce e periculoasă, Sugestie renegociere.",
        "subsol": "🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)"
    },
    "EN": {
        "titlu": "📄 Negotiation Assistant for Freelancers",
        "subtitlu": "Protect your business. Identify hidden unfair clauses and renegotiate on equal terms.",
        "avertisment_b2b": "⚠️ **B2B Exclusive Use:** This platform is an experimental tool intended exclusively for professionals (freelancers/businesses).",
        "bifa_text": "I have read, understand and expressly agree to the Terms, Conditions of Use and the Privacy Policy (GDPR).",
        "blocat_text": "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        "ghid": "💡 **How to use this tool:** This site acts as a **negotiation copilot**. Generated information is **strictly indicative**. This tool DOES NOT provide legal advice or solicitor assistance. The app enforces a **zero data storage** policy.",
        "c1": "<b>💡 Guidance Guide</b><br>Translates tangled contract clauses into simple ideas.",
        "c2": "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or payment terms.",
        "c3": "<b>🗣️ Renegotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        "side_s": "Personal key active.",
        "side_d": "DEMO mode active",
        "up_t": "Drag or upload contract (PDF, DOCX, TXT):",
        "tx_t": "Or enter the text of suspicious clauses manually:",
        "disc": "🔒 **Security & Disclaimer:** Document content is not stored or used to train public models. This automated analysis is for informational purposes and does not replace the advice of a lawyer.",
        "b_start": "Start Intelligent Analysis",
        "e_limita": "⚠️ Demo limit reached!",
        "e_text": "Please enter text or upload a document.",
        "e_config": "Demo System is not configured!",
        "spinner": "AI is scanning text for legal risks...",
        "succes": "Analysis completed successfully!",
        "rap_t": "## 🔍 Contractual Audit Report",
        "b_down": "Download Report (.txt)",
        "prompt": "You are a legal expert specializing in freelancer protection. Analyze the provided contract text and identify major risks. Respond STRICTLY in ENGLISH. Return the result in Markdown format with the structure: ### 🚩 [Risk Name], Original Clause, Translation, Why it is dangerous, Renegotiation suggestion.",
        "subsol": "🛡️ Freelancer Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)"
    }
}

L = t[st.session_state["limba"]]

st.markdown("""<style>
.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }
</style>""", unsafe_allow_html=True)

CHEIE_API_DEMO = "gen-lang-client-0040445167" 
LIMITA_UTILIZARI_GRATUITE = 2

if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

# Titlul și subtitlul sunt vizibile mereu pentru design profesional
st.title(L["titlu"])
st.markdown(f"<p style='font-size:18px; color:#475569;'>{L['subtitlu']}</p>", unsafe_allow_html=True)

# =====================================================================
# 🔒 ZIDUL JURIDIC DE BLOCARE (CHECKBOX OBLIGATORIU)
# =====================================================================
st.info(L["avertisment_b2b"])

# Forțăm bifa direct în calea utilizatorului
accepta_termeni = st.checkbox(L["bifa_text"], value=st.session_state.termeni_acceptati, key="chk_termeni_obligatoriu")
st.session_state.termeni_acceptati = accepta_termeni

# Dacă utilizatorul NU a bifat căsuța, oprim execuția fișierului AICI
if not st.session_state.termeni_acceptati:
    st.warning(L["blocat_text"])
    st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
    st.stop()

# =====================================================================
# INTERFAȚA DE UPLOAD ȘI ANALIZĂ (RULEAZĂ DOAR DUPĂ CE SE BIFAZĂ)
# =====================================================================
if "rezultat_analiza" not in st.session_state:
    st.info(L["ghid"])
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
    with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
    with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)

api_cheie_utilizator = st.sidebar.text_input("Gemini API Key:", type="password")
foloseste_mod_demo = True
cheie_finala = None

if api_cheie_utilizator.strip():
    cheie_finala = api_cheie_utilizator
    foloseste_mod_demo = False
    st.sidebar.success(L["side_s"])
else:
    cheie_finala = CHEIE_API_DEMO
    st.sidebar.info(f"{L['side_d']} ({st.session_state['numar_utilizari']}/{LIMITA_UTILIZARI_GRATUITE} analize).")

client = None
if cheie_finala and cheie_finala != "AICI_PUI_CHEIA_TA_GEMINI":
    client = genai.Client(api_key=cheie_finala)

uploaded_file = st.file_uploader(L["up_t"], type=["pdf", "docx", "txt"])
text_manual = st.text_area(L["tx_t"], height=150)

contract_final_text = ""
if uploaded_file is not None:
    nm_f = uploaded_file.name.lower()
    if ".pdf" in nm_f:
        try: contract_final_text = "".join([p.extract_text() for p in pypdf.PdfReader(uploaded_file).pages])
        except Exception: pass
    if ".docx" in nm_f:
        try: contract_final_text = "\n".join([pr.text for pr in docx.Document(uploaded_file).paragraphs])
        except Exception: pass
    if ".txt" in nm_f:
        try: contract_final_text = uploaded_file.read().decode("utf-8")
        except Exception: pass

if text_manual.strip():
    contract_final_text = text_manual

st.markdown("---")
st.caption(L["disc"])
st.markdown("---")

if st.button(L["b_start"], type="primary"):
    if foloseste_mod_demo and st.session_state["numar_utilizari"] >= LIMITA_UTILIZARI_GRATUITE:
        st.error(L["e_limita"])
    elif not contract_final_text.strip():
        st.error(L["e_text"])
    elif client is None:
        st.error(L["e_config"])
    else:
        with st.spinner(L["spinner"]):
            try:
                response = client.models.generate_content(model='gemini-2.5-flash', contents=f"Contract:\n\n{contract_final_text}", config=types.GenerateContentConfig(system_instruction=L["prompt"], temperature=0.2))
                if foloseste_mod_demo: st.session_state["numar_utilizari"] += 1
                st.session_state["rezultat_analiza"] = response.text
                st.success(L["succes"])
                st.rerun()
            except Exception as e: st.error(f"Eroare: {str(e)}")

if "rezultat_analiza" in st.session_state:
    st.markdown(L["rap_t"])
    st.markdown(st.session_state["rezultat_analiza"])
    st.download_button(label=L["b_down"], data=st.session_state["rezultat_analiza"], file_name="analiza.txt", mime="text/plain")
    
st.markdown(f"{L['subsol']}", unsafe_allow_html=True)
