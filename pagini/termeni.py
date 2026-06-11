```python
import streamlit as st

def run_termeni():
    if "limba" not in st.session_state:
        st.session_state["limba"] = "RO"

    if st.session_state["limba"] == "RO":
        st.title("⚖️ Termeni și Condiții de Utilizare")
        st.caption("Ultima actualizare: Iunie 2026 | Locație legală: Milton Keynes, UK")
        st.markdown("""
        ### 1. ACCEPTAREA TERMENILOR ȘI NATURA DIGITALĂ A ACORDULUI
        Prin accesarea, vizitarea sau utilizarea acestui website („Platforma”), sunteți de acord în mod expres și necondiționat să respectați prezenții Termeni și Condiții, precum și legislația aplicabilă din Anglia și Țara Galilor.
        * **FĂRĂ CONTURI DE UTILIZATOR:** Platforma funcționează ca un instrument de tip „utilizare directă”, fără un sistem de autentificare, creare de conturi sau colectare de credențiale.
        * **SEMNĂTURĂ DIGITALĂ:** Acordul de utilizare se consideră semnat digital în momentul în care bifați activ căsuța de confirmare de pe pagina principală. Dacă nu sunteți de acord, aveți obligația de a părăsi imediat site-ul.

        ### 2. NATURA SERVICIULUI ȘI MODELUL DE UTILIZARE (API KEY)
        Acest website este o interfață experimentală bazată pe algoritmi de Inteligență Artificială (Google Gemini API), administrată și deținută în totalitate de **IULIAN ICHIM-UNGUREANU (Alias Pantick)**, operând din **Milton Keynes, Regatul Unit (United Kingdom)**.
        * **LIMITA DE UTILIZARE ȘI COSTA-SHARING (BYO-API-KEY):** Platforma oferă un număr strict limitat de 2 (două) încercări gratuite bazate pe resursele administratorului. Pentru utilizarea continuă, Platforma solicită utilizatorului să își introducă propria cheie API personală (Google Gemini API Key).
        * **RESPONSABILITATEA CHEII API:** Utilizatorul poartă întreaga răspundere legală și financiară pentru generarea, utilizarea și securitatea propriei chei API introduse. Administratorul nu are acces și nu stochează cheia API introdusă.
        * **FĂRĂ CONSULTANȚĂ JURIDICĂ B2B:** Platforma este un instrument strict orientativ și educațional destinat exclusiv profesioniștilor (freelanceri/firme). Conținutul generat NU constituie consultanță juridică autorizată.

        ### 3. FINANȚARE, MONETIZARE ȘI DONAȚII (LINKTREE)
        * **SCOPUL MONETIZĂRII:** Eventualele venituri realizate din reclame afișate (ex. Google AdMob) sunt destinate strict acoperirii costurilor de mentenanță și servere necesare funcționării Platformei.
        * **DONAȚII PRIN PĂRȚI TERȚE:** Orice opțiune de donație accesibilă prin platforme externe (ex. Linktree) este complet voluntară. Fondurile pot fi redirecționate către entități terțe, fără ca acest lucru să confere utilizatorului statutul de client plătitor.
        * **FĂRĂ SERVICII PREMIUM SAU UPGRADE-URI:** Efectuarea unei donații nu deblochează funcționalități suplimentare, beneficii sau upgrade-uri de performanță pe Platformă. Toți utilizatorii au acces la exact aceeași interfață.

        ### 4. GARANȚIA STRICTĂ DE NON-STOCARE A DATELOR CONTRACTUALE
        * **PROCESARE VOLATILĂ IN-MEMORY:** Documentele introduse și cheile API sunt procesate exclusiv în memoria temporară a browserului (sesiune). În momentul în care închideți tab-ul sau fereastra de browser, toate datele sunt șterse definitiv, instantaneu și irevocabil. Platforma nu deține baze de date pentru stocarea acestora.

        ### 5. LIMITAREA TOTALĂ A RĂSPUNDERII (DAMAGE CAP)
        În măsura maximă permisă de legislația aplicabilă în Anglia și Țara Galilor (English Law):
        * **PLAFONUL DE RĂSPUNDERE ZERO (£0):** Având în vedere caracterul gratuit al interfeței, administratorul nu este răspunzător pentru nicio daună directă sau indirectă. Răspunderea totală cumulată este limitată strict la **£0 GBP**.
        * **PLAFON REZIDUAL DE SIGURANȚĂ:** Dacă o instanță competentă anulează plafonul de £0 din cauza prezenței reclamelor, răspunderea maximă absolută a administratorului este limited la o sumă fixă de **£10 GBP**, sumă recunoscută de utilizator ca fiind echitabilă.

        ### 6. INDEMNIZARE, ANTI-HĂRȚUIRE ȘI CHELTUIELI DE JUDECATĂ
        * **6.1. OBLIGAȚIA ÎN CAZ DE PROCESE NEFONDATE:** Dacă un utilizator inițiază o acțiune în instanță împotriva administratorului încălcând clauzele asumate, iar acțiunea este respinsă sau anulată, utilizatorul se obligă necondiționat să achite integral toate cheltuielile de judecată efectuate de administrator (onorariile avocaților/solicitors din UK implicați în apărare, taxele de curte, costurile de transport).
        * **6.2. CLAUZĂ PENALĂ PENTRU CAMPANII DE DENIGRARE:** Utilizatorul se obligă să nu inițieze și să nu participe la nicio campanie publică de hărțuire, denigrare sau defăimare împotriva Platformei sau a administratorului (pe rețele sociale, forumuri sau Linktree). În caz de încălcare, în baza principiului daunelor pre-evaluate (Liquidated Damages), utilizatorul se obligă irevocabil să achite administratorului daune-interese în cuantum fix de **£1.000 GBP pentru fiecare postare hărțuitoare distinctă**.

        ### 7. RENUNȚAREA LA PROCESE COLECTIVE (CLASS ACTION WAIVER)
        Orice procedură se va desfășura strict pe bază individuală. Utilizatorul renunță în mod expres la dreptul de a participa ca reclamant sau membru într-un proces colectiv (Class Action) în fața oricărei instanțe din lume.

        ### 8. LEGEA APLICABILĂ ȘI JURISDICTIA EXCLUSIVĂ
        Prezenții Termeni sunt guvernați și interpretați în conformitate cu **legile din Anglia și Țara Galilor (English Law)**. Orice dispută va fi trimisă spre soluționare exclusivă **instanțelor de judecată competente din Milton Keynes, Regatul Unit (United Kingdom)**.
        """)
    else:
        st.title("⚖️ Terms and Conditions of Use")
        st.caption("Last Updated: June 2026 | Legal Venue: Milton Keynes, UK")
        st.markdown("""
        ### 1. ACCEPTANCE OF TERMS AND DIGITAL NATURE OF THE AGREEMENT
        By accessing, browsing, or using this website ("the Platform"), you expressly and unconditionally agree to comply with these Terms and Conditions and the applicable laws of England and Wales.
        * **NO USER ACCOUNTS:** The Platform operates as a "direct-use" tool, without an authentication or registration system.
        * **DIGITAL SIGNATURE:** This agreement is deemed digitally signed and executed the moment you actively check the confirmation box on the homepage.

        ### 2. NATURE OF THE SERVICE AND OPERATING MODEL (API KEY)
        This website is an experimental interface based on Artificial Intelligence algorithms (Google Gemini API), fully owned and administered by **IULIAN ICHIM-UNGUREANU (Alias Pantick)**, operating from **Milton Keynes, United Kingdom**.
        * **USAGE LIMITS AND COST-SHARING (BYO-API-KEY):** The Platform offers a strict limit of 2 free analyses. For continuous use, it requires users to input their own personal Google Gemini API Key.
        * **API KEY RESPONSIBILITY:** The user bears sole legal and financial responsibility for their API key. The administrator does not store or intercept it.
        * **NO B2B LEGAL ADVICE:** Intended exclusively for professionals (freelancers/businesses). Generated content DOES NOT constitute authorized legal advice.

        ### 3. FINANCING, MONETIZATION, AND DONATIONS (LINKTREE)
        * **MONETIZATION PURPOSE:** Any revenue generated from ads (e.g., Google AdMob) is strictly used to cover maintenance and server costs.
        * **THIRD-PARTY DONATIONS:** Any donation option via external platforms (e.g., Linktree) is entirely voluntary. Funds may be redirected to third parties or charitable causes.
        * **NO PREMIUM SERVICES OR UPGRADES:** Making a donation does not unlock additional features, performance upgrades, or priority services on the Platform. All users access the exact same interface.

        ### 4. STRICT CONTRACTUAL DATA NON-STORAGE GUARANTEE
        * **VOLATILE IN-MEMORY PROCESSING:** Uploaded documents and API keys are processed exclusively within the browser's temporary memory (session) and are permanently, instantly, and irrevocably deleted when the browser tab is closed.

        ### 5. TOTAL LIMITATION OF LIABILITY (DAMAGE CAP)
        To the maximum extent permitted by applicable laws of England and Wales:
        * **ZERO LIABILITY CAP (£0):** Given the free-of-charge nature of the interface, the administrator's total cumulative liability for any claim is strictly limited to **£0 GBP**.
        * **RESIDUAL SAFETY CAP:** If a court invalidates the £0 cap due to the presence of ads, the absolute maximum liability is limited to a fixed sum of **£10 GBP**.

        ### 6. INDEMNIFICATION, ANTI-HARASSMENT, AND LEGAL COSTS
        * **6.1. REIMBURSEMENT FOR FRIVOLOUS LAWSUITS:** If a user initiates court action in breach of these waivers and the action is dismissed, they unconditionally agree to fully reimburse all legal costs incurred by the administrator (UK solicitors' fees, court fees, travel).
        * **6.2. LIQUIDATED DAMAGES FOR ONLINE HARASSMENT:** Public campaigns of harassment, defamation, or disparagement against the Platform or the administrator (on social media, forums, or Linktree) are strictly prohibited. In case of breach, the user irrevocably agrees to pay fixed liquidated damages of **£1,000 GBP per distinct defamatory post**.

        ### 7. CLASS ACTION WAIVER
        Proceedings will be conducted solely on an individual basis. The user waives the right to participate as a plaintiff or class member in any class action worldwide.

        ### 8. GOVERNING LAW AND EXCLUSIVE JURISDICTION
        These Terms are governed by and construed in accordance with the **laws of England and Wales (English Law)**. Any dispute shall be submitted to the **exclusive jurisdiction of the courts in Milton Keynes, United Kingdom**.
        """)
