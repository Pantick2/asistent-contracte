import streamlit as st
import streamlit.components.v1 as components
import google.generativeai as genai
import docx
import pypdf
import ads_config

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

if "termeni_acceptati" not in st.session_state:
    st.session_state.termeni_acceptati = False

if "rezultat_analiza" not in st.session_state:
    st.session_state["rezultat_analiza"] = None

# Dicționarul de traduceri
t = {
    "RO": {
        "titlu": "📄 Asistent de Negociere Contractuală",
        "subtitlu": "Protejează-ți drepturile. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "avertisment_b2b": "⚠️ **Disclaimer Legal:** Această platformă este un instrument experimental bazat pe AI, destinat informării generale și educației contractuale.",
        "bifa_text": "Am citit, înțeleg și accept în mod exprimat Termenii de Utilizare și Politica de Confidențialitate (GDPR).",
        "blocat_text": "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        "ghid": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un copilot informativ. Rezultatele generate sunt strict orientative.",
        "c1": "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale complicate în cuvinte simple.",
        "c2": "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele abuzive.",
        "c3": "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        "side_s": "🚀 Cheie personală activată cu succes!",
        "side_d": "🔑 Introduceți cheia dvs. Gemini API Key în căsuța de mai jos pentru a debloca analiza.",
        "up_t": "Încarcă documentul (PDF, DOCX, TXT):",
        "tx_t": "Sau introdu textul clauzelor suspecte manual:",
        "disc": "🔒 Securitate & Siguranță: Conținutul documentelor este procesat volatil. Analiză informativă.",
        "b_start": "Pornește Analiza Inteligentă",
        "e_text": "Te rugăm să introduci text sau să încarci un document.",
        "e_config": "❌ Eroare: Trebuie să introduceți o cheie Gemini API validă în bara laterală pentru a putea porni analiza.",
        "spinner": "AI-ul scanează textul pentru riscuri contractuale...",
        "succes": "Analiză finalizată cu succes!",
        "rap_t": "## 🔍 Raport de Audit Contractual",
        "b_down": "Descarcă Raportul (.txt)",
        "prompt": "Ești un expert juridic în audit contractual. Analizează contractul în ROMÂNĂ: Nume Risc, Clauză originală, Traducere, De ce e periculoasă, Sugestie renegociere.",
        "subsol": "🛡️ Asistent Contracte | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)"
    },
    "EN": {
        "titlu": "📄 Contract Negotiation Assistant",
        "subtitlu": "Protect your business. Identify hidden clauses, contractual risks, and renegotiate with confidence.",
        "avertisment_b2b": "⚠️ **Legal Disclaimer:** This platform is an experimental AI-based tool intended strictly for general informational purposes.",
        "bifa_text": "I have read, understand, and agree to the Terms of Use and Privacy Policy (GDPR).",
        "blocat_text": "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        "ghid": "💡 **How to use this tool:** This site acts as an informational copilot. Generated results are strictly indicative.",
        "c1": "<b>💡 Guidance Guide</b><br>Translates complicated contractual clauses into simple terms.",
        "c2": "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or unfair terms.",
        "c3": "<b>🗣️ Negotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        "side_s": "🚀 Personal key activated successfully!",
        "side_d": "🔑 Please enter your Gemini API Key in the box below to unlock the analysis.",
        "up_t": "Upload document (PDF, DOCX, TXT):",
        "tx_t": "Or enter text manually:",
        "disc": "🔒 Security & Safety: Document processed dynamically and not stored. Educational purposes only.",
        "b_start": "Start Intelligent Analysis",
        "e_text": "Please enter text or upload a document.",
        "e_config": "❌ Error: You must enter a valid Gemini API Key in the sidebar to run the analysis.",
        "spinner": "AI is scanning text for contractual risks...",
        "succes": "Analysis completed successfully!",
        "rap_t": "## 🔍 Contractual Audit Report",
        "b_down": "Download Report (.txt)",
        "prompt": "You are a legal expert in contract auditing. Analyze the contract and identify risks in ENGLISH: Risk Name, Original Clause, Translation, Why it is dangerous, Renegotiation suggestion.",
        "subsol": "🛡️ Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)"
    }
}

L = t[st.session_state["limba"]]
st.markdown("<style>.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }</style>", unsafe_allow_html=True)

st.title(L["titlu"])
st.markdown(f"<p style='font-size:18px; color:#475569;'>{L['subtitlu']}</p>", unsafe_allow_html=True)

html_ad_config = f"""
<div style="display:none;">
    <script type="text/javascript" charset="UTF-8" src="https://cookie-script.com"></script>
</div>
"""
components.html(html_ad_config, height=0)

st.info(L["avertisment_b2b"])

st.sidebar.markdown("---")
st.sidebar.caption("Advertisement")
try:
    html_sidebar_ad = ads_config.genereaza_html_banner(ads_config.ID_BANNER_SIDEBAR, latime="100%", inaltime="250px")
    components.html(html_sidebar_ad, height=270)
except Exception:
    pass

accepta_termeni = st.checkbox(L["bifa_text"], value=st.session_state.termeni_acceptati, key="chk_termeni_obligatoriu")
st.session_state.termeni_acceptati = accepta_termeni

if not st.session_state.termeni_acceptati:
    st.warning(L["blocat_text"])
    if "rezultat_analiza" not in st.session_state:
        st.info(L["ghid"])
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
        with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
        with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)
    st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
    st.stop()

# =====================================================================
# INTERFATA DE INPUT - EXCLUSIV PE CHEIA UTILIZATORULUI
# =====================================================================
api_cheie_utilizator = st.sidebar.text_input("Gemini API Key:", type="password", key="cheie_utilizator_curata")
cheie_finala = None

if api_cheie_utilizator.strip():
    cheie_finala = api_cheie_utilizator.strip()
    st.sidebar.success(L["side_s"])
else:
    st.sidebar.info(L["side_d"])

if "rezultat_analiza" not in st.session_state:
    st.info(L["ghid"])
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
    with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
    with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(L["up_t"], type=["pdf", "docx", "txt"])
text_manual = st.text_area(L["tx_t"], height=150)

contract_final_text = ""
if uploaded_file is not None:
    nm_f = uploaded_file.name.lower()
    if ".pdf" in nm_f:
        try: contract_final_text = "".join([p.extract_text() for p in pypdf.PdfReader(uploaded_file).pages])
        except Exception: pass
    elif ".docx" in nm_f:
        try: contract_final_text = "\n".join([pr.text for pr in docx.Document(uploaded_file).paragraphs])
        except Exception: pass
    elif ".txt" in nm_f:
        try: contract_final_text = uploaded_file.read().decode("utf-8")
        except Exception: pass

if text_manual.strip(): 
    contract_final_text = text_manual

st.markdown("---")
st.caption(L["disc"])
st.markdown("---")

if st.button(L["b_start"], type="primary"):
    if not cheie_finala:
        st.error(L["e_config"])
    elif not contract_final_text.strip():
        st.error(L["e_text"])
    else:
        with st.spinner(L["spinner"]):
            try:
                        try:
                # Configurează cheia utilizatorului direct în sistemul de operare înainte de apel
                import os
                os.environ["GEMINI_API_KEY"] = cheie_finala
                
                # Forțează utilizarea serverului stabil v1 de producție la configurare
                genai.configure(client_options={"api_version": "v1"})
                
                prompt_complet = f"{L['prompt']}\n\n{contract_final_text}"
                model = genai.GenerativeModel("models/gemini-1.5-flash")
                response = model.generate_content(prompt_complet)
                
                st.session_state["rezultat_analiza"] = response.text
                st.success(L["succes"])
                st.rerun()
            except Exception as e:
                st.error(f"Eroare AI: {str(e)}")

if "rezultat_analiza" in st.session_state and st.session_state["rezultat_analiza"]:
    st.markdown(L["rap_t"])
    st.markdown(st.session_state["rezultat_analiza"])
    st.download_button(label=L["b_down"], data=st.session_state["rezultat_analiza"], file_name="analiza.txt", mime="text/plain")
    
    st.markdown("---")
    try:
        html_final_ad = ads_config.genereaza_html_banner(ads_config.ID_BANNER_FINAL, latime="100%", inaltime="90px")
        components.html(html_final_ad, height=400)
    except Exception:
        pass

st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
