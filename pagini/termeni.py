
```python
import streamlit as st

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

# Antet cu buton de donație Linktree
col_st, col_dr = st.columns([8, 2])
with col_dr:
    st.link_button("☕ Buy me a coffee", "https://linktr.ee/safescanallergyscan")

if st.session_state["limba"] == "RO":
    st.title("⚖️ Termeni și Condiții de Utilizare")
    st.caption("Ultima actualizare: Iunie 2026 | Locație legală: Milton Keynes, UK")
    st.markdown("""
    ### 1. ACCEPTAREA TERMENILOR ȘI NATURA DIGITALĂ A ACORDULUI
    Prin accesarea, vizitarea sau utilizarea acestui website („Platforma”), sunteți de acord în mod expres și necondiționat să respectați prezenții Termeni și Condiții, precum și legislația aplicabilă din Anglia și Țara Galilor. 
    * **FĂRĂ CONTURI DE UTILIZATOR:** Platforma funcționează ca un instrument de tip „utilizare directă”, fără un sistem de autentificare.
    * **SEMNĂTURĂ DIGITALĂ:** Acordul de utilizare se consideră semnat digital în momentul în care bifați activ căsuța de confirmare înainte de inițierea analizei contractuale.

    ### 2. NATURA SERVICIULUI ȘI MODELUL DE UTILIZARE (API KEY)
    Acest website este o interfață experimentală bazată pe algoritmi de Inteligență Artificială (Google Gemini API), administrată și deținută în totalitate de **IULIAN ICHIM-UNGUREANU (Alias Pantick)**, operând din **Milton Keynes, Regatul Unit (United Kingdom)**.
    * **LIMITA DE UTILIZARE ȘI COSTA-SHARING (BYO-API-KEY):** Platforma oferă un număr limitat de 2 încercări gratuite. Pentru utilizarea continuă, Platforma solicită introducerea propriei chei API personale (Google Gemini API Key).
    * **RESPONSABILITATEA CHEII API:** Utilizatorul poartă întreaga răspundere legală și financiară pentru propria cheie API introdusă. Administratorul nu stochează cheia.
    * **FĂRĂ CONSULTANȚĂ JURIDICĂ B2B:** Destinat exclusiv profesioniștilor (freelanceri). Conținutul generat NU constituie consultanță juridică autorizată.

    ### 3. FINANȚARE, MONETIZARE ȘI DONAȚII (LINKTREE)
    * **SCOPUL MONETIZĂRII:** Veniturile din reclame (ex. Google AdMob) sunt destinate strict acoperirii costurilor de mentenanță și servere.
    * **DONAȚII PRIN PĂRȚI TERȚE:** Opțiunea de donație prin Linktree este complet voluntară. Fondurile pot fi redirecționate către entități terțe sau cauze caritabile.
    * **FĂRĂ SERVICII PREMIUM SAU UPGRADE-URI:** Efectuarea unei donații nu deblochează funcționalități suplimentare, beneficii sau upgrade-uri pe Platformă.

    ### 4. GARANȚIA STRICTĂ DE NON-STOCARE A DATELOR CONTRACTUALE
    * **PROCESARE VOLATILĂ IN-MEMORY:** Documentele și cheile API sunt procesate exclusiv în memoria temporară a browserului (sesiune) și sunt șterse definitiv și irevocabil instantaneu la închiderea tab-ului.

    ### 5. LIMITAREA TOTALĂ A RĂSPUNDERII (DAMAGE CAP)
    * **PLAFONUL DE RĂSPUNDERE ZERO (£0):** Răspunderea totală cumulată a administratorului este limitată strict la **£0 GBP**.
    * **PLAFON REZIDUAL DE SIGURANȚĂ:** Dacă o instanță anulează plafonul de £0 din cauza prezenței reclamelor, răspunderea maximă absolută este limitată la o sumă fixă de **£10 GBP**.

    ### 6. INDEMNIZARE, ANTI-HĂRȚUIRE ȘI CHELTUIELI DE JUDECATĂ
    * **6.1. Procese nefondate:** Dacă utilizatorul deschide un proces care este respins, acesta se obligă să achite integral toate cheltuielile de judecată ale administratorului (onorarii avocați din UK/solicitors, taxe de curte).
    * **6.2. Clauză Penală pentru hărțuire online:** Se interzic campaniile de denigrare sau defăimare (rețele sociale, Linktree etc.). În caz de încălcare, utilizatorul se obligă irevocabil să achite daune-interese în cuantum fix de **£1.000 GBP pentru fiecare postare hărțuitoare distinctă**.

    ### 7. RENUNȚAREA LA PROCESE COLECTIVE (CLASS ACTION WAIVER)
    Orice procedură se va desfășura strict pe bază individuală. Utilizatorul renunță la dreptul de a participa în procese colective.

    ### 8. LEGEA APLICABILĂ ȘI JURISDICȚIA EXCLUSIVĂ
    Prezenții Termeni sunt guvernați de **legile din Anglia și Țara Galilor (English Law)**. Orice dispută va fi trimisă spre soluționare exclusivă **instanțelor din Milton Keynes, Regatul Unit**.
    """)
else:
    st.title("⚖️ Terms and Conditions of Use")
    st.caption("Last Updated: June 2026 | Legal Venue: Milton Keynes, UK")
    st.markdown("""
    ### 1. ACCEPTANCE OF TERMS AND DIGITAL NATURE OF THE AGREEMENT
    By accessing, browsing, or using this website ("the Platform"), you expressly and unconditionally agree to comply with these Terms and Conditions and the applicable laws of England and Wales.
    * **NO USER ACCOUNTS:** The Platform operates as a "direct-use" tool, without any authentication system.
    * **DIGITAL SIGNATURE:** This agreement is deemed digitally signed the moment you actively check the confirmation box before initiating the contract analysis.

    ### 2. NATURE OF THE SERVICE AND OPERATING MODEL (API KEY)
    This website is an experimental interface based on Artificial Intelligence algorithms (Google Gemini API), fully owned and administered by **IULIAN ICHIM-UNGUREANU (Alias Pantick)**, operating from **Milton Keynes, United Kingdom**.
    * **USAGE LIMITS AND COST-SHARING (BYO-API-KEY):** The Platform offers a strict limit of 2 free analyses. For continuous use, it requires users to input their own personal Google Gemini API Key.
    * **API KEY RESPONSIBILITY:** The user bears sole legal and financial responsibility for their API key. The administrator does not store or intercept it.
    * **NO B2B LEGAL ADVICE:** Intended exclusively for professionals (freelancers). Generated content DOES NOT constitute authorized legal advice.

    ### 3. FINANCING, MONETIZATION, AND DONATIONS (LINKTREE)
    * **MONETIZATION PURPOSE:** Any revenue generated from ads (e.g., Google AdMob) is strictly used to cover maintenance and server costs.
    * **THIRD-PARTY DONATIONS:** Any donation option via external platforms (e.g., Linktree) is entirely voluntary. Funds may be redirected to third parties or charitable causes.
    * **NO PREMIUM SERVICES OR UPGRADES:** Making a donation does not unlock additional features, performance upgrades, or priority services on the Platform.

    ### 4. STRICT CONTRACTUAL DATA NON-STORAGE GUARANTEE
    * **VOLATILE IN-MEMORY PROCESSING:** Uploaded documents and API keys are processed exclusively within the browser's temporary memory (session) and are permanently, instantly, and irrevocably deleted when the browser tab is closed.

    ### 5. TOTAL LIMITATION OF LIABILITY (DAMAGE CAP)
    * **ZERO LIABILITY CAP (£0):** The administrator's total cumulative liability for any claim is strictly limited to **£0 GBP**.
    * **RESIDUAL SAFETY CAP:** If a court invalidates the £0 cap due to the presence of ads, the absolute maximum liability is limited to a fixed sum of **£10 GBP**.

    ### 6. INDEMNIFICATION, ANTI-HARASSMENT, AND LEGAL COSTS
    * **6.1. Frivolous Lawsuits:** If a user initiates court action that is dismissed, they unconditionally agree to fully reimburse all legal costs incurred by the administrator (UK solicitors' fees, court fees, travel).
    * **6.2. Liquidated Damages for Online Harassment:** Public campaigns of harassment or defamation are strictly prohibited (social media, Linktree, etc.). In case of breach, the user irrevocably agrees to pay fixed liquidated damages of **£1,000 GBP per distinct defamatory post**.

    ### 7. CLASS ACTION WAIVER
    Proceedings will be conducted solely on an individual basis. The user waives the right to participate as a plaintiff or class member in any class action.

    ### 8. GOVERNING LAW AND EXCLUSIVE JURISDICTION
    These Terms are governed by and construed in accordance with the **laws of England and Wales (English Law)**. Any dispute shall be submitted to the **exclusive jurisdiction of the courts in Milton Keynes, United Kingdom**.
    """)

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
