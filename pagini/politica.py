```python
import streamlit st

# Verificăm limba setată global
if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

# Antet pe două coloane pentru a pune butonul de donație în dreapta sus
col_stanga, col_dreapta = st.columns([8, 2])

with col_dreapta:
    text_btn = "Donate" if st.session_state["limba"] == "EN" else "Donatie"
    st.link_button(text_btn, "https://linktr.ee", type="primary")

if st.session_state["limba"] == "RO":
    st.title("🔒 Politica de Confidențialitate")
    st.caption("Ultima actualizare: Iunie 2026 | Conformitate cu UK-GDPR")
    
    st.markdown("""
    ### 1. PRINCIPIUL DE BAZĂ: ZERO STOCARE DATE CONTRACTUALE
    Prioritatea absolută a acestei Platforme este confidențialitatea totală. 
    * **Fișiere și texte:** Nu deținem și nu operăm baze de date pentru stocarea documentelor comerciale sau a textelor analizate de dumneavoastră.
    * **Chei API:** Cheia Gemini API introdusă personal de utilizator rulează exclusiv în memoria volatilă a sesiunii browserului și dispare irevocabil în secunda în care închideți fereastra.

    ### 2. DATE COLECTATE DE PĂRȚI TERȚE (GOOGLE ADMOB)
    Deoarece Platforma afișează reclame pentru auto-susținere și mentenanță, servicii terțe (Google AdMob) pot colecta date tehnice de navigare:
    * **Cookie-uri și Identificatori:** Google poate utiliza module cookie sau identificatori publicitari pentru a afișa reclame relevante în funcție de interesele utilizatorilor.
    * **Controlul utilizatorului:** Puteți reseta, bloca sau gestiona acești identificatori din setările browserului dumneavoastră sau prin bannerul de consimțământ.

    ### 3. DONAȚII ȘI REȚELE EXTERNE (LINKTREE)
    Platforma folosește servicii externe precum Linktree pentru gestionarea donațiilor voluntare. Interacțiunea cu aceste link-uri se supune politicilor de confidențialitate ale platformelor respective (Linktree, PayPal, Stripe), administratorul nefiind responsabil de datele introduse de dumneavoastră pe acele site-uri.

    ### 4. JURISDICȚIE ȘI LEGE APLICABILĂ
    Orice solicitare, investigație sau litigiu legat de datele tehnice procesate de modulele de publicitate pe acest site va fi guvernat de legea din Anglia și Țara Galilor, sub autoritatea exclusivă a instanțelor din **Milton Keynes, Regatul Unit**.
    """)
else:
    st.title("🔒 Privacy Policy")
    st.caption("Last Updated: June 2026 | UK-GDPR Compliance")
    
    st.markdown("""
    ### 1. CORE PRINCIPLE: ZERO CONTRACTUAL DATA STORAGE
    The absolute priority of this Platform is total confidentiality.
    * **Files and Texts:** We do not own, maintain, or operate databases to store uploaded commercial documents or analyzed texts.
    * **API Keys:** The Gemini API key entered by the user runs exclusively within volatile session memory and is irrevocably destroyed the exact moment you close the browser tab.

    ### 2. DATA COLLECTED BY THIRD PARTIES (GOOGLE ADMOB)
    As the Platform displays advertisements for technical self-sustainment and server maintenance, third-party services (Google AdMob) may collect technical data:
    * **Cookies and Identifiers:** Google may use cookies or mobile advertising identifiers to serve relevant ads based on user visits and interests.
    * **User Control:** You can reset, disable, or manage these identifiers directly via your browser settings or the cookie consent banner.

    ### 3. DONATIONS AND EXTERNAL NETWORKS (LINKTREE)
    The Platform uses external services like Linktree to redirect users to voluntary donation options. Interactions with these links are subject to the privacy policies of the respective platforms (Linktree, PayPal, etc.), and the administrator is not responsible for any data you provide on those external sites.

    ### 4. GOVERNING LAW AND JURISDICTION
    Any request, inquiry, or dispute regarding the technical session data processed on this site shall be governed by the laws of England and Wales, under the exclusive authority of the courts in **Milton Keynes, United Kingdom**.
    """)

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
