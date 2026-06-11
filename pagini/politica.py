import streamlit as st

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

col_st, col_dr = st.columns([8, 2])
with col_dr:
    st.link_button("☕ Buy me a coffee", "https://linktr.ee")

if st.session_state["limba"] == "RO":
    st.title("🔒 Politica de Confidențialitate")
    st.caption("Ultima actualizare: Iunie 2026 | Conformitate cu UK-GDPR")
    
    st.markdown("### 1. PRINCIPIUL DE BAZĂ: ZERO STOCARE DATE CONTRACTUALE")
    st.markdown("Prioritatea absolută a acestei Platforme este confidențialitatea totală.")
    st.markdown("* **Fișiere și texte:** Nu deținem baze de date pentru stocarea documentelor comerciale sau a textelor analizate.")
    st.markdown("* **Chei API:** Cheia Gemini API introdusă personal de utilizator rulează exclusiv în memoria volatilă a sesiunii și dispare irevocabil la închiderea ferestrei.")

    st.markdown("### 2. DATE COLECTATE DE PĂRȚI TERȚE (GOOGLE ADMOB)")
    st.markdown("Deoarece Platforma afișează reclame pentru auto-susținere, servicii terțe (Google AdMob) pot colecta date tehnice:")
    st.markdown("* **Cookie-uri și Identificatori:** Google poate utiliza module cookie sau identificatori publicitari pentru a afișa reclame relevante.")
    st.markdown("* **Controlul utilizatorului:** Puteți reseta sau bloca acești identificatori din setările browserului dumneavoastră.")

    st.markdown("### 3. DONAȚII ȘI REȚELE EXTERNE (LINKTREE)")
    st.markdown("Platforma folosește servicii externe precum Linktree pentru donații voluntare. Interacțiunea cu aceste link-uri se supune politicilor de confidențialitate ale platformelor respective (Linktree, PayPal etc.).")

    st.markdown("### 4. JURISDICȚIE")
    st.markdown("Orice solicitare legată de datele tehnice procesate va fi guvernată de legea din Anglia și Țara Galilor, sub autoritatea exclusivă a instanțelor din Milton Keynes, Regatul Unit.")
else:
    st.title("🔒 Privacy Policy")
    st.caption("Last Updated: June 2026 | UK-GDPR Compliance")
    
    st.markdown("### 1. CORE PRINCIPLE: ZERO CONTRACTUAL DATA STORAGE")
    st.markdown("The absolute priority of this Platform is total confidentiality.")
    st.markdown("* **Files and Texts:** We do not own or maintain databases to store uploaded commercial documents or analyzed texts.")
    st.markdown("* **API Keys:** The Gemini API key entered by the user runs exclusively within volatile session memory and is irrevocably destroyed upon closing the browser tab.")

    st.markdown("### 2. DATA COLLECTED BY THIRD PARTIES (GOOGLE ADMOB)")
    st.markdown("As the Platform displays advertisements for technical self-sustainment, third-party services (Google AdMob) may collect technical data:")
    st.markdown("* **Cookies and Identifiers:** Google may use cookies or advertising identifiers to serve relevant ads based on user visits.")
    st.markdown("* **User Control:** You can reset or disable these identifiers directly via your browser settings.")

    st.markdown("### 3. DONATIONS AND EXTERNAL NETWORKS (LINKTREE)")
    st.markdown("The Platform uses external services like Linktree to redirect users to voluntary donation options. Interactions with these links are subject to the privacy policies of the respective platforms (Linktree, PayPal, etc.).")

    st.markdown("### 4. JURISDICTION")
    st.markdown("Any request or dispute regarding the technical session data processed on this site shall be governed by the laws of England and Wales, under the exclusive authority of the courts in Milton Keynes, United Kingdom.")

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
