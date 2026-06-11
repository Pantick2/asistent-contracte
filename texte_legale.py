import streamlit as st

def afiseaza_termeni_si_conditii():
    st.title("⚖️ Termeni și Condiții de Utilizare")
    st.write("Ultima actualizare: Iunie 2026")
    st.markdown("""
    ### 1. Cum funcționează aplicația
    Acest instrument este un asistent digital bazat pe inteligență artificială orientativă administrat de IULIAN ICHIM-UNGUREANU (Pantick).
    * Utilizatorul încarcă un contract sau introduce un text juridic în interfață.
    * Textul este transmis securizat și criptat direct către algoritmul AI (Google Gemini).

    ### 2. Garanția de Non-Stocare a Datelor (Confidențialitate Totală)
    Confidențialitatea contractelor tale este prioritatea noastră absolută.
    * **Fără baze de date:** Aplicația **NU stochează, nu colectează și nu salvează** pe niciun server textul contractelor.
    * **Procesare volatilă:** Datele introduse există doar în memoria temporară a sesiunii tale de browser și dispar definitiv la închiderea ferestrei.

    ### 3. Exonerare Totală de Răspundere (Disclaimer)
    Informațiile, traducerile și sugestiile de contra-argumente generate au un scop **strict informativ și educațional**.
    * Acest instrument **NU oferă consultanță juridică** și nu înlocuiește un avocat.
    * Dezvoltatorul nu își asumă nicio răspundere legală sau financiară pentru eventualele pierderi sau contracte semnate dezavantajos.

    ### 4. Suportarea Cheltuielilor de Judecată (Abuz de Drept)
    În cazul în care utilizatorul inițiază o acțiune în instanță împotriva dezvoltatorului, încălcând clauzele din prezentul document, și acțiunea este respinsă, **utilizatorul se obligă în mod necondiționat să achite integral toate cheltuielile de judecată efectuate de dezvoltator** (onorariile avocaților, taxele, costurile logistice).

    ### 5. Jurisdicție și Litigii
    Prezentul acord este guvernat de legislația din România. Litigiile vor fi trimise spre soluționare instanțelor judecătorești competente de la sediul/domiciliul dezvoltatorului.
    """)

def afiseaza_politica_confidentialitate():
    st.title("🔒 Politica de Confidențialitate (GDPR)")
    st.write("Ultima actualizare: Iunie 2026")
    st.markdown("""
    ### 1. Datele procesate
    Aplicația noastră aplică o politică strictă de **non-stocare**. Noi nu colectăm adrese de email, nume, adrese IP sau fișiere pe serverele noastre.
    
    ### 2. Procesarea prin Terțe Părți (Google Gemini API)
    Atunci când apeși pe butonul de analiză, textul contractului este trimis criptat (prin conexiune securizată HTTPS) către API-ul oficial Google Gemini pentru a fi procesat în timp real.
    * Google declară în politicile sale comerciale că datele transmise prin intermediul API-urilor de dezvoltare nu sunt folosite pentru antrenarea modelelor publice AI.

    ### 3. Drepturile tale (GDPR)
    Deoarece nu deținem o bază de date cu caracter personal, nu stocăm informații pe care să le putem extrage sau șterge la cerere. Datele tale dispar definitiv din memoria sesiunii în momentul în care ai închis această fereastră de browser.
    """)
