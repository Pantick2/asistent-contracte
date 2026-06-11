import streamlit as st

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

col_st, col_dr = st.columns([8, 2])
with col_dr:
    st.link_button("☕ Buy me a coffee", "https://linktr.ee/safescanallergyscan")

if st.session_state["limba"] == "RO":
    st.title("🔒 Politica de Confidențialitate")
    st.caption("Ultima actualizare: Iunie 2026 | Conformitate cu UK-GDPR")
    st.markdown("""
    ### 1. PRINCIPIUL DE BAZĂ: ZERO STOCARE DATE CONTRACTUALE
    Prioritatea absolută a acestei Platforme este confidențialitatea totală. 
    * **Fișiere și texte:** Nu deținem baze de date pentru stocarea documentelor comerciale sau a textelor analizate.
    * **Chei API:** Cheia Gemini API introdusă personal de utilizator rulează exclusiv în memoria volatilă a sesiunii și dispare irevocabil la închiderea ferestrei.

    ### 2. DATE COLECTATE DE PĂRȚI TERȚE (GOOGLE ADMOB)
    Deoarece Platforma afișează reclame pentru auto-susținere, servicii terțe (Google AdMob) pot colecta date tehnice:
    * **Cookie-uri și Identificatori:** Google poate utiliza module cookie sau identificatori publicitari pentru a afișa reclame relevante.
    * **Controlul utilizatorului:** Puteți reseta sau bloca acești identificatori din setările browserului dumneavoastră.

    ### 3. DONAȚII ȘI REȚELE EXTERNE (LINKTREE)
    Platforma folosește servicii externe precum Linktree pentru donații voluntare. Interacțiunea cu aceste link-uri se supune politicilor de confidențialitate ale platformelor respective (Linktree, PayPal etc.).

    ### 4. JURISDICȚIE
    Orice solicitare legată de datele tehnice procesate va fi guvernată de legea din Anglia și Țara Galilor, sub autoritatea exclusivă a instanțelor din **Milton Keynes, Regatul Unit**.
    """)
else:
    st.title("🔒 Privacy Policy")
    st.caption("Last Updated: June 2026 | UK-GDPR Compliance")
    st.markdown("""
    ### 1. CORE PRINCIPLE: ZERO CONTRACTUAL DATA STORAGE
    The absolute priority of this Platform is total confidentiality.
    * **Files and Texts:** We do not own or maintain databases to store uploaded commercial documents or analyzed texts.
    * **API Keys:** The Gemini API key entered by the user runs exclusively within volatile session memory and is irrevocably destroyed upon closing the browser tab.

    ### 2. DATA COLLECTED BY THIRD PARTIES (GOOGLE ADMOB)
    As the Platform displays advertisements for technical self-sustainment, third-party services (Google AdMob) may collect technical data:
    * **Cookies and Identifiers:** Google may use cookies or advertising identifiers to serve relevant ads based on user visits.
    * **User Control:** You can reset or disable these identifiers directly via your browser settings.

    ### 3. DONATIONS AND EXTERNAL NETWORKS (LINKTREE)
    The Platform uses external services like Linktree to redirect users to voluntary donation options. Interactions with these links are subject to the privacy policies of the respective platforms (Linktree, PayPal, etc.).

    ### 4. JURISDICTION
    Any request or dispute regarding the technical session data processed on this site shall be governed by the laws of England and Wales, under the exclusive authority of the courts in **Milton Keynes, United Kingdom**.
    """)

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
