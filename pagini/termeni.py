import streamlit as st

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

col_st, col_dr = st.columns([8, 2])
with col_dr:
    st.link_button("☕ Buy me a coffee", "https://linktr.ee")

if st.session_state["limba"] == "RO":
    st.title("⚖️ Termeni și Condiții de Utilizare")
    st.caption("Ultima actualizare: Iunie 2026 | Locație legală: Milton Keynes, UK")
    
    st.markdown("### 1. ACCEPTAREA TERMENILOR ȘI NATURA DIGITALĂ A ACORDULUI")
    st.markdown("Prin accesarea, vizitarea sau utilizarea acestui website, sunteți de acord în mod expres și necondiționat să respectați prezenții Termeni și Condiții, precum și legislația aplicabilă din Anglia și Țara Galilor.")
    st.markdown("* **FĂRĂ CONTURI DE UTILIZATOR:** Platforma funcționează ca un instrument de tip utilizare directă, fără un sistem de autentificare.")
    st.markdown("* **SEMNĂTURĂ DIGITALĂ:** Acordul de utilizare se consideră semnat digital în momentul în care bifați activ căsuța de confirmare înainte de inițierea analizei contractuale.")

    st.markdown("### 2. NATURA SERVICIULUI ȘI MODELUL DE UTILIZARE (API KEY)")
    st.markdown("Acest website este o interfață experimentală bazată pe algoritmi de Inteligență Artificială (Google Gemini API), administrată și deținută în totalitate de IULIAN ICHIM-UNGUREANU (Alias Pantick), operând din Milton Keynes, Regatul Unit (United Kingdom).")
    st.markdown("* **LIMITA DE UTILIZARE ȘI COSTA-SHARING:** Platforma oferă un număr limitat de 2 încercări gratuite. Pentru utilizarea continuă, Platforma solicită introducerea propriei chei API personale (Google Gemini API Key).")
    st.markdown("* **RESPONSABILITATEA CHEII API:** Utilizatorul poartă întreaga răspundere legală și financiară pentru propria cheie API introdusă. Administratorul nu stochează cheia.")
    st.markdown("* **FĂRĂ CONSULTANȚĂ JURIDICĂ B2B:** Destinat exclusiv profesioniștilor (freelanceri). Conținutul generat NU constituie consultanță juridică autorizată.")

    st.markdown("### 3. FINANȚARE, MONETIZARE ȘI DONAȚII (LINKTREE)")
    st.markdown("* **SCOPUL MONETIZĂRII:** Veniturile din reclame (ex. Google AdMob) sunt destinate strict acoperirii costurilor de mentenanță și servere.")
    st.markdown("* **DONAȚII PRIN PĂRȚI TERȚE:** Opțiunea de donație prin Linktree este complet voluntară. Fondurile pot fi redirecționate către entități terțe sau cauze caritabile.")
    st.markdown("* **FĂRĂ SERVICII PREMIUM:** Efectuarea unei donații nu deblochează funcționalități suplimentare, beneficii sau upgrade-uri pe Platformă.")

    st.markdown("### 4. GARANȚIA STRICTĂ DE NON-STOCARE A DATELOR CONTRACTUALE")
    st.markdown("* **PROCESARE VOLATILĂ IN-MEMORY:** Documentele și cheile API sunt procesate exclusiv în memoria temporară a browserului (sesiune) și sunt șterse definitiv și irevocabil instantaneu la închiderea tab-ului.")

    st.markdown("### 5. LIMITAREA TOTALĂ A RĂSPUNDERII (DAMAGE CAP)")
    st.markdown("* **PLAFONUL DE RĂSPUNDERE ZERO:** Răspunderea totală cumulată a administratorului este limitată strict la £0 GBP.")
    st.markdown("* **PLAFON REZIDUAL DE SIGURANȚĂ:** Dacă o instanță anulează plafonul de £0 din cauza prezenței reclamelor, răspunderea maximă absolută este limitată la o sumă fixă de £10 GBP.")

    st.markdown("### 6. INDEMNIZARE, ANTI-HĂRȚUIRE ȘI CHELTUIELI DE JUDECATĂ")
    st.markdown("* **6.1. Procese nefondate:** Dacă utilizatorul deschide un proces care este respins, acesta se obligă să achite integral toate cheltuielile de judecată ale administratorului (onorarii avocați din UK/solicitors, taxe de curte).")
    st.markdown("* **6.2. Clauză Penală pentru hărțuire online:** Se interzic campaniile de denigrare sau defăimare (rețele sociale, Linktree etc.). În caz de încălcare, utilizatorul se obligă irevocabil să achite daune-interese în cuantum fix de £1.000 GBP pentru fiecare postare hărțuitoare distinctă.")

    st.markdown("### 7. RENUNȚAREA LA PROCESE COLECTIVE (CLASS ACTION WAIVER)")
    st.markdown("Orice procedură se va desfășura strict pe bază individuală. Utilizatorul renunță la dreptul de a participa în procese colective.")

    st.markdown("### 8. LEGEA APLICABILĂ ȘI JURISDICȚIA EXCLUSIVĂ")
    st.markdown("Prezenții Termeni sunt guvernați de legile din Anglia și Țara Galilor (English Law). Orice dispută va fi trimisă spre soluționare exclusivă instanțelor din Milton Keynes, Regatul Unit.")
else:
    st.title("⚖️ Terms and Conditions of Use")
    st.caption("Last Updated: June 2026 | Legal Venue: Milton Keynes, UK")
    
    st.markdown("### 1. ACCEPTANCE OF TERMS AND DIGITAL NATURE OF THE AGREEMENT")
    st.markdown("By accessing, browsing, or using this website, you expressly and unconditionally agree to comply with these Terms and Conditions and the applicable laws of England and Wales.")
    st.markdown("* **NO USER ACCOUNTS:** The Platform operates as a direct-use tool, without any authentication system.")
    st.markdown("* **DIGITAL SIGNATURE:** This agreement is deemed digitally signed the moment you actively check the confirmation box before initiating the contract analysis.")

    st.markdown("### 2. NATURE OF THE SERVICE AND OPERATING MODEL (API KEY)")
    st.markdown("This website is an experimental interface based on Artificial Intelligence algorithms (Google Gemini API), fully owned and administered by IULIAN ICHIM-UNGUREANU (Alias Pantick), operating from Milton Keynes, United Kingdom.")
    st.markdown("* **USAGE LIMITS AND COST-SHARING:** The Platform offers a strict limit of 2 free analyses. For continuous use, it requires users to input their own personal Google Gemini API Key.")
    st.markdown("* **API KEY RESPONSIBILITY:** The user bears sole legal and financial responsibility for their API key. The administrator does not store or intercept it.")
    st.markdown("* **NO B2B LEGAL ADVICE:** Intended exclusively for professionals (freelancers). Generated content DOES NOT constitute authorized legal advice.")

    st.markdown("### 3. FINANCING, MONETIZATION, AND DONATIONS (LINKTREE)")
    st.markdown("* **MONETIZATION PURPOSE:** Any revenue generated from ads (e.g., Google AdMob) is strictly used to cover maintenance and server costs.")
    st.markdown("* **THIRD-PARTY DONATIONS:** Any donation option via external platforms (e.g., Linktree) is entirely voluntary. Funds may be redirected to third parties or charitable causes.")
    st.markdown("* **NO PREMIUM SERVICES:** Making a donation does not unlock additional features, performance upgrades, or priority services on the Platform.")

    st.markdown("### 4. STRICT CONTRACTUAL DATA NON-STORAGE GUARANTEE")
    st.markdown("* **VOLATILE IN-MEMORY PROCESSING:** Uploaded documents and API keys are processed exclusively within the browser temporary memory (session) and are permanently, instantly, and irrevocably deleted when the browser tab is closed.")

    st.markdown("### 5. TOTAL LIMITATION OF LIABILITY (DAMAGE CAP)")
    st.markdown("* **ZERO LIABILITY CAP:** The administrator's total cumulative liability for any claim is strictly limited to £0 GBP.")
    st.markdown("* **RESIDUAL SAFETY CAP:** If a court invalidates the £0 cap due to the presence of ads, the absolute maximum liability is limited to a fixed sum of £10 GBP.")

    st.markdown("### 6. INDEMNIFICATION, ANTI-HARASSMENT, AND LEGAL COSTS")
    st.markdown("* **6.1. Frivolous Lawsuits:** If a user initiates court action that is dismissed, they unconditionally agree to fully reimburse all legal costs incurred by the administrator (UK solicitors fees, court fees, travel).")
    st.markdown("* **6.2. Liquidated Damages for Online Harassment:** Public campaigns of harassment or defamation are strictly prohibited (social media, Linktree, etc.). In case of breach, the user irrevocably agrees to pay fixed liquidated damages of £1,000 GBP per distinct defamatory post.")

    st.markdown("### 7. CLASS ACTION WAIVER")
    st.markdown("Proceedings will be conducted solely on an individual basis. The user waives the right to participate as a plaintiff or class member in any class action.")

    st.markdown("### 8. GOVERNING LAW AND EXCLUSIVE JURISDICTION")
    st.markdown("These Terms are governed by and construed in accordance with the laws of England and Wales (English Law). Any dispute shall be submitted to the exclusive jurisdiction of the courts in Milton Keynes, United Kingdom.")

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
