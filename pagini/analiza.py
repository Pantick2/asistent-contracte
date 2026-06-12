import streamlit as st
import streamlit.components.v1 as components
from google import genai
from google.genai import types
import docx
import pypdf
import ads_config

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

if "termeni_acceptati" not in st.session_state:
    st.session_state.termeni_acceptati = False

if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

# Dicționarul tău complet de traduceri
t = {
    "RO": {
        "titlu": "📄 Asistent de Negociere Contractuală",
        "subtitlu": "Protejează-ți drepturile. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "avertisment_b2b": "⚠️ **Disclaimer Legal:** Această platformă este un instrument experimental bazat pe AI, destinat informării generale și educației contractuale.",
        "bifa_text": "Am citit, înțeleg și accept în mod expres Termenii de Utilizare (Limitare Răspunderii la £10, Jurisdicția Milton Keynes, UK și Clauza de Non-Defăimare) și Politica de Confidențialitate (GDPR).",
        "blocat_text": "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        "ghid": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un copilot informativ. Rezultatele generate sunt strict orientative.",
        "c1": "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale complicate în cuvinte simple.",
        "c2": "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele abuzive.",
        "c3": "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        "side_s": "Cheie personală activă.",
        "side_d": "Modul DEMO activ",
        "up_t": "Încarcă documentul (PDF, DOCX, TXT):",
        "tx_t": "Sau introdu textul clauzelor suspecte manual:",
        "disc": "🔒 Securitate & Siguranță: Conținutul documentelor este procesat volatil. Analiză informativă.",
        "b_start": "Pornește Analiza Inteligentă",
        "e_limita": "⚠️ Limita demo a fost atinsă!",
        "e_text": "Te rugăm să introduci text sau să încarci un document.",
        "e_config": "Sistemul Demo nu este configurat!",
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
        "bifa_text": "I have read, understand, and agree to the Terms of Use (£10 Liability Cap, Milton Keynes, UK Jurisdiction) and Privacy Policy (GDPR).",
        "blocat_text": "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        "ghid": "💡 **How to use this tool:** This site acts as an informational copilot. Generated results are strictly indicative.",
        "c1": "<b>💡 Guidance Guide</b><br>Translates complicated contractual clauses into simple terms.",
        "c2": "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or unfair terms.",
        "c3": "<b>🗣️ Negotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        "side_s": "Personal key active.",
        "side_d": "DEMO mode active",
        "up_t": "Upload document (PDF, DOCX, TXT):",
        "tx_t": "Or enter text manually:",
        "disc": "🔒 Security & Safety: Document processed dynamically and not stored. Educational purposes only.",
        "b_start": "Start Intelligent Analysis",
        "e_limita": "⚠️ Demo limit reached!",
        "e_text": "Please enter text or upload a document.",
        "e_config": "Demo System is not configured!",
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

# =====================================================================
# 🍪 CONSOLE POPUP COOKIE-SCRIPT GENERAT VIZIBIL LA INTRAREA ÎN SITE
# =====================================================================
LINK_SCRIPT_COOKIE = "https://cookie-script.com"
COD_CLIENT_ADSENSE = "ca-pub-3528838516008000"

html_fortat_intrare = f"""
<div style="text-align: center;">
    <script type="text/javascript" charset="UTF-8" src="{LINK_SCRIPT_COOKIE}"></script>
    <script async src="https://googlesyndication.com{COD_CLIENT_ADSENSE}" crossorigin="anonymous"></script>
</div>
"""
# Alocăm un spațiu fizic de 350px sus pe pagină. Popup-ul este obligat să apară vizual în el instant!
components.html(html_fortat_intrare, height=350)

st.info(L["avertisment_b2b"])
