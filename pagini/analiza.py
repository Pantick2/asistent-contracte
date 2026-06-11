import streamlit as st
from google import genai
from google.genai import types
import docx
import pypdf

# 1. Gestionare Limbă (Implicit Română)
if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

if "termeni_acceptati" not in st.session_state:
    st.session_state.termeni_acceptati = False

if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

# 2. ANTET: Limba (Stânga) și Donații (Dreapta Sus)
col_stanga, col_dreapta = st.columns([8, 2])

with col_stanga:
    if st.button("🌐 Schimbă Limba / Switch Language (RO / EN)"):
        st.session_state["limba"] = "EN" if st.session_state["limba"] == "RO" else "RO"
        st.rerun()

with col_dreapta:
    st.link_button("☕ Buy me a coffee / Donează", "https://linktr.ee/safescanallergyscan", type="secondary")

# Dicționar de traduceri pentru Interfață
t = {
    "RO": {
        "titlu": "📄 Asistent de Negociere pentru Freelanceri",
        "subtitlu": "Protejează-ți business-ul. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "avertisment_b2b": "⚠️ **Utilizare B2B Exclusivă:** Această platformă este un instrument experimental destinat exclusiv profesioniștilor (freelanceri/firme).",
        "bifa_text": "Am citit, înțeleg și sunt de acord în mod expres cu Termenii, Condițiile (inclusiv Guvernanța Legii Engleze, Jurisdicția Exclusivă a Instanțelor din Milton Keynes, UK și Clauza Penală de Non-Defăimare) și Politica de Confidențialitate (GDPR).",
        "blocat_text": "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        "ghid_utilizare": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un **copilot de negociere**. Informațiile generate sunt **strict orientative**. Acest instrument NU oferă asistență juridică sau consultanță de avocat. Aplicația aplică o politică de **zero stocare**.",
        "card1": "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale încâlcite în idei simple.",
        "card2": "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele de plată.",
        "card3": "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        "sidebar_titlu": "Cheie Gemini API personală:",
        "sidebar_succes": "Cheie personală activă.",
        "sidebar_demo": "Modul DEMO activ",
        "upload_titlu": "Trage sau încarcă contractul (PDF, DOCX, TXT):",
        "text_titlu": "Sau introdu textul clauzelor suspecte manual:",
        "disclaimer_mic": "🔒 **Securitate & Disclaimer:** Conținutul documentelor nu este stocat sau folosit pentru antrenarea modelelor publice. Această analiză automată are rol informativ și nu înlocuiește sfatul unui avocat public din UK sau țara de origine.",
        "buton_start": "Pornește Analiza Inteligentă",
        "eroare_limita": "⚠️ Limita demo a fost atinsă!",
        "eroare_text": "Te rugăm să introduci text sau să încarci un document.",
        "eroare_config": "Sistemul Demo nu este configurat!",
        "spinner_text": "AI-ul scanează textul pentru riscuri legale...",
        "succes_analiza": "Analiză finalizată cu succes!",
        "raport_titlu": "## 🔍 Raport de Audit Contractual",
        "descarca_buton": "Descarcă Raportul (.txt)",
        "prompt": "Ești un expert juridic specializat în protecția freelancerilor. Analizează textul contractului oferit și identifică riscurile majore. Răspunde STRICT în limba ROMÂNĂ. Returnează rezultatul în format Markdown, cu structura: ### 🚩 [Nume Risc], Clauză originală, Traducere, De ce e periculoasă, Sugestie renegociere.",
        "subsol": "🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)"
    },
    "EN": {
        "titlu": "📄 Negotiation Assistant for Freelancers",
        "subtitlu": "Protect your business. Identify hidden unfair clauses and renegotiate on equal terms.",
        "avertisment_b2b": "⚠️ **B2B Exclusive Use:** This platform is an experimental tool intended exclusively for professionals (freelancers/businesses).",
        "bifa_text": "I have read, understand, and expressly agree to the Terms, Conditions (including English Law Governance, Exclusive Jurisdiction of the Courts in Milton Keynes, UK, and the Non-Disparagement Liquidated Damages Clause) and the Privacy Policy (GDPR).",
        "blocat_text": "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        "ghid_utilizare": "💡 **How to use this tool:** This site acts as a **negotiation copilot**. Generated information is **strictly indicative**. This tool DOES NOT provide legal assistance or solicitor advice. The app enforces a **zero data storage** policy.",
        "card1": "<b>💡 Guidance Guide</b><br>Translates tangled contract clauses into simple ideas.",
        "card2": "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or payment terms.",
        "card3": "<b>🗣️ Renegotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        "sidebar_titlu": "Personal Gemini API Key:",
        "sidebar_succes": "Personal key active.",
        "sidebar_demo": "DEMO mode active",
        "upload_titlu": "Drag or upload contract (PDF, DOCX, TXT):",
        "text_titlu": "Or enter the text of suspicious clauses manually:",
        "disclaimer_mic": "🔒 **Security & Disclaimer:** Document content is not stored or used to train public models. This automated analysis is for informational purposes and does not replace the advice of a qualified lawyer in the UK or country of origin.",
        "buton_start": "Start Intelligent Analysis",
        "eroare_limita": "⚠️ Demo limit reached!",
        "eroare_text": "Please enter text or upload a document.",
        "eroare_config": "Demo System is not configured!",
        "spinner_text": "AI is scanning text for legal risks...",
        "succes_analiza": "Analysis completed successfully!",
        "raport_titlu": "## 🔍 Contractual Audit Report",
        "descarca_buton": "Download Report (.txt)",
        "prompt": "You are a legal expert specializing in freelancer protection. Analyze the provided contract text and identify major risks. Respond STRICTLY in ENGLISH. Return the result in Markdown format with the structure: ### 🚩 [Risk Name], Original Clause, Translation, Why it is dangerous, Renegotiation suggestion.",
        "subsol": "🛡️ Freelancer Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)"
    }
}

L = t[st.session_state["limba"]]

st.markdown("""<style>
.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }
</style>""", unsafe_allow_html=True)

# ⚠️ CHEIA TA DEMO:
CHEIE_API_DEMO = "gen-lang-client-0040445167" 
LIMITA_UTILIZARI_GRATUITE = 2

st.title(L["titlu"])
st.markdown(f"<p style='font-size:18px; color:#475569;'>{L['subtitlu']}</p>", unsafe_allow_html=True)

# =====================================================================
# 🔒 ZIDUL JURIDIC OBLIGATORIU
# =====================================================================
st.info(L["avertisment_b2b"])

accepta_termeni = st.checkbox(L["bifa_text"], value=st.session_state.termeni_acceptati)
st.session_state.termeni_acceptati = accepta_termeni

if not st.session_state.termeni_acceptati:
    st.warning(L["blocat_text"])
    st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
    st.stop()

# =====================================================================
# CODUL APLICAȚIEI (Apare doar după bife)
# =====================================================================
if "rezultat_analiza" not in st.session_state:
    st.info(L["ghid_utilizare"])
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f"<div class='feature-card'>{L['card1']}</div>", unsafe_allow_html=True)
    with col2: st.markdown(f"<div class='feature-card'>{L['card2']}</div>", unsafe_allow_html=True)
    with col3: st.markdown(f"<div class='feature-card'>{L['card3']}</div>", unsafe_allow_html=True)

api_cheie_utilizator = st.sidebar.text_input(L["sidebar_titlu"], type="password")
foloseste_mod_demo = True
cheie_finala = None

if api_cheie_utilizator.strip():
    cheie_finala = api_cheie_utilizator
    foloseste_mod_demo = False
    st.sidebar.success(L["sidebar_succes"])
else:
    cheie_finala = CHEIE_API_DEMO
    st.sidebar.info(f"{L['sidebar_demo']} ({st.session_state['numar_utilizari']}/{LIMITA_UTILIZARI_GRATUITE}).")

client = None
if cheie_finala and cheie_finala != "AICI_PUI_CHEIA_TA_GEMINI":
    client = genai.Client(api_key=cheie_finala)

uploaded_file = st.file_uploader(L["upload_titlu"], type=["pdf", "docx", "txt"])
text_manual = st.text_area(L["text_titlu"], height=150)

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
st.caption(L["disclaimer_mic"])

if st.button(L["buton_start"], type="primary"):
    if foloseste_mod_demo and st.session_state["numar_utilizari"] >= LIMITA_UTILIZARI_GRATUITE:
        st.error(L["eroare_limita"])
        st.link_button("🚀 API Key", "https://google.com")
    elif not contract_final_text.strip():
        st.error(L["eroare_text"])
    elif client is None:
        st.error(L["eroare_config"])
    else:
        with st.spinner(L["spinner_text"]):
            try:
