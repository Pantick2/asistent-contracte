import streamlit as st

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

if st.session_state["limba"] == "RO":
    st.title("🔒 Politica de Confidențialitate")
    st.caption("Ultima actualizare: Iunie 2026 | Conformitate cu GDPR")
    st.markdown("---")
    st.markdown("### 1. PRINCIPIUL DE BAZĂ: ZERO STOCARE")
    st.markdown("Prioritatea absolută a acestei Platforme este confidențialitatea totală. Nu deținem și nu operăm baze de date pentru stocarea documentelor sau a textelor introduse. Totul se șterge instant la închiderea ferestrei.")
    st.markdown("### 2. DATE PROCESATE DE TERȚI")
    st.markdown("Platforma funcționează exclusiv prin apelarea securizată a API-ului oficial Google Gemini. Cheia API personală introdusă rulează local și nu este interceptată de administrator.")
    st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
else:
    st.title("🔒 Privacy Policy")
    st.caption("Last Updated: June 2026 | GDPR Compliance")
    st.markdown("---")
    st.markdown("### 1. CORE PRINCIPLE: ZERO STORAGE")
    st.markdown("The absolute priority of this Platform is total confidentiality. We do not own or operate databases to store documents or entered text. Everything is deleted instantly when the window is closed.")
    st.markdown("### 2. DATA PROCESSED BY THIRD PARTIES")
    st.markdown("The Platform works exclusively by calling the official Google Gemini API securely. Your personal API key runs locally and is not intercepted by the administrator.")
    st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Freelancer Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
