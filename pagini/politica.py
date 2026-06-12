import streamlit as st

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

if st.session_state["limba"] == "RO":
    st.title("🔒 Politica de Confidențialitate")
    st.caption("Ultima actualizare: Iunie 2026 | Conformitate cu UK-GDPR & GDPR (UE)")
    st.markdown("---")
    
    st.markdown("### 1. PRINCIPIUL DE BAZĂ: ZERO STOCARE DATE CONTRACTUALE")
    st.markdown("Confidențialitatea documentelor dumneavoastră comerciale este prioritatea absolută a acestei Platforme:")
    st.markdown("* **Fără baze de date:** Platforma funcționează fără un modul de stocare de tip bază de date. Niciun server nu colectează, nu salvează și nu arhivează textul contractelor încărcate sau introduse manual.")
    st.markdown("* **Procesare volatilă in-memory:** Documentele sunt procesate exclusiv în memoria temporară a browserului (sesiune) pe durata rulării analizei. În secunda în care închideți tab-ul sau fereastra de browser, toate textele sunt șterse definitiv, instantaneu și irevocabil.")

    st.markdown("### 2. DATE COLECTATE ȘI SCOPUL PROCESĂRII")
    st.markdown("Platforma nu solicită crearea unui cont de utilizator și nu colectează date de identificare directă (nume, prenume, adrese de email, numere de telefon) pentru utilizarea instrumentului AI.")
    st.markdown("* **Chei API Personale:** Dacă alegeți să introduceți cheia dumneavoastră personală (Google Gemini API Key), aceasta este utilizată exclusiv local pentru a autoriza cererile directe către infrastructura Google. Cheia nu este trimisă către administrator și nu este stocată.")
    st.markdown("* **Date tehnice de sesiune:** Pe durata vizitei, pot fi procesate date tehnice temporare (cum ar fi adresa IP anonimizată, tipul browserului sau logurile de eroare de pe server) cu unicul scop de a asigura stabilitatea tehnică și securitatea platformei împotriva atacurilor cibernetice.")

    st.markdown("### 3. SERVICII FURNIZATE DE TERȚI ȘI PUBLICITATE (GOOGLE ADMOB)")
    st.markdown("Pentru a asigura auto-susținerea financiară, mentenanță tehnică și viitoarele actualizări, Platforma poate afișa reclame prin intermediul serviciului Google AdMob.")
    st.markdown("* **Module cookie de publicitate:** Google AdMob poate utiliza module cookie sau identificatori unici de publicitate pentru a difuza reclame bazate pe vizitele anterioare ale utilizatorilor pe acest website sau pe alte site-uri de pe internet.")
    st.markdown("* **Controlul utilizatorului:** Puteți opta pentru dezactivarea publicității personalizate accesând setările Google Ads sau modificând setările de confidențialitate și cookie-uri ale browserului dumneavoastră.")

    st.markdown("### 4. DONAȚII ȘI LINK-URI EXTERNE (LINKTREE)")
    st.markdown("Platforma integrează link-uri către servicii terțe externe (cum ar fi Linktree) pentru facilitarea donațiilor opționale sau interacțiunea pe rețelele sociale.")
    st.markdown("* Administratorul acestei Platforme nu colectează și nu controlează datele financiare sau personale introduse de dumneavoastră pe platformele terțe (PayPal, Stripe etc.). Vă recomandăm să consultați politicile de confidențialitate ale acelor servicii externe.")

    st.markdown("### 5. DREPTURILE DUMNEAVOASTRĂ CONFORM GDPR / UK-GDPR")
    st.markdown("Conform legislației privind protecția datelor, beneficiați de dreptul de acces, rectificare, ștergere sau restricționare a procesării. Cu toate acestea, având în vedere că Platforma aplică o politică strictă de zero stocare, administratorul nu deține înregistrări istorice și nu poate identifica sau extrage date referitoare la contractele analizate în sesiunile anterioare.")

    st.markdown("### 6. LEGEA APLICABILĂ ȘI JURISDICȚIA")
    st.markdown("Orice solicitare sau litigiu legat de prezenții termeni de confidențialitate va fi guvernat de legile din Anglia și Țara Galilor și va fi trimis spre soluționare exclusivă instanțelor competente din Milton Keynes, Regatul Unit.")
    
    st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)

else:
    st.title("🔒 Privacy Policy")
    st.caption("Last Updated: June 2026 | UK-GDPR & EU-GDPR Compliance")
    st.markdown("---")
    
    st.markdown("### 1. CORE PRINCIPLE: ZERO CONTRACTUAL DATA STORAGE")
    st.markdown("The confidentiality of your commercial documents is the absolute priority of this Platform:")
    st.markdown("* **No Databases:** The Platform operates without any database storage module. No server collects, saves, or archives the text of uploaded or manually entered contracts.")
    st.markdown("* **Volatile In-Memory Processing:** Your documents are processed exclusively within the temporary memory (session) of your browser during the live analysis. The exact second you close the browser tab or window, all texts are permanently, instantly, and irrevocably deleted.")

    st.markdown("### 2. DATA COLLECTED AND PURPOSE OF PROCESSING")
    st.markdown("The Platform does not require user accounts and does not collect direct identification data (first name, last name, email addresses, phone numbers) to use the AI tool.")
    st.markdown("* **Personal API Keys:** If you choose to enter your personal Google Gemini API Key, it is used exclusively to authorize direct requests to Google's infrastructure. The key is not transmitted to the administrator and is not stored.")
    st.markdown("* **Technical Session Data:** During your visit, temporary technical data (such as anonymized IP addresses, browser type, or server error logs) may be processed solely to ensure technical stability and security against cyber attacks.")

    st.markdown("### 3. THIRD-PARTY SERVICES AND ADVERTISING (GOOGLE ADMOB)")
    st.markdown("To ensure financial self-sustainment, technical maintenance, and future updates, the Platform may display advertisements through the Google AdMob service.")
    st.markdown("* **Advertising Cookies:** Google AdMob may use cookies or unique advertising identifiers to serve ads based on users' prior visits to this website or other sites on the internet.")
    st.markdown("* **User Control:** You can opt-out of personalized advertising by visiting Google Ads Settings or by adjusting your browser's cookie and privacy settings.")

    st.markdown("### 4. DONATIONS AND EXTERNAL LINKS (LINKTREE)")
    st.markdown("The Platform integrates links to external third-party services (such as Linktree) to facilitate optional donations or social media interaction.")
    st.markdown("* The administrator of this Platform does not collect or control financial or personal data entered by you on third-party payment platforms (PayPal, Stripe, etc.). We recommend reviewing the privacy policies of those external services.")

    st.markdown("### 5. YOUR RIGHTS UNDER GDPR / UK-GDPR")
    st.markdown("Under data protection laws, you possess the right to access, rectify, erase, or restrict processing. However, since the Platform enforces a strict zero data storage policy, the administrator holds no historical records and cannot identify or retrieve data regarding contracts analyzed in past sessions.")

    st.markdown("### 6. GOVERNING LAW AND JURISDICTION")
    st.markdown("Any inquiry or dispute related to these privacy terms shall be governed by the laws of England and Wales and submitted to the exclusive jurisdiction of the competent courts in Milton Keynes, United Kingdom.")
    
    st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Freelancer Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
