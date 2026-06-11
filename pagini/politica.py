import streamlit as st

st.title("🔒 Politica de Confidențialitate (GDPR)")
st.write("Ultima actualizare: Iunie 2026")

st.markdown("""
### 1. ANGAJAMENTUL PRIVIND PROTECȚIA DATELOR
Respectăm confidențialitatea și securitatea datelor cu caracter personal în conformitate cu Regulamentul (UE) 2016/679 (Regulamentul general privind protecția datelor - GDPR). Acest document explică în mod transparent modul în care datele transmise prin intermediul Platformei noastre sunt gestionate.

### 2. DATELE COLECTATE ȘI PROCESATE
Aplicația noastră aplică o politică fundamentală de **ZERO STOCARE (No Data Retention)**:
* **FĂRĂ COLECTARE DE IDENTITATE:** Platforma în varianta sa actuală nu colectează adrese de e-mail (cu excepția paginii de Feedback unde utilizatorul le introduce voluntar), nume, prenume, numere de telefon sau date bancare.
* **CONȚINUTUL CONTRACTELOR:** Atunci când încărcați un fișier de tip PDF, Word (.docx) sau text, conținutul documentului este citit digital și trimis exclusiv pe o linie securizată către analiza AI. Acest text nu este copiat pe serverele noastre, nu este salvat în fișiere jurnal (logs) și nu este vizualizat de nicio persoană fizică.

### 3. TRANSMITEREA DATELOR CĂTRE TERȚE PĂRȚI (GOOGLE GEMINI API)
Pentru a vă pune la dispoziție funcția de analiză automată, textul extras din contract este transmis prin intermediul unei conexiuni securizate criptate (HTTPS) către serverele Google Gemini API.
* **POLITICA GOOGLE PRIVIND DATELE:** Conform termenilor oficiali de utilizare ai Google pentru API-urile dedicate dezvoltatorilor (Google AI Studio Enterprise/Developer Terms), datele transmise prin apeluri API **NU sunt utilizate de Google pentru a antrena sau îmbunătăți modelele lor de inteligență artificială publice**. Datele dumneavoastră rămân izolate în acea sesiune de procesare.

### 4. DREPTURILE DUMNEAVOASTRĂ CONFORM GDPR
Regulamentul GDPR oferă persoanelor vizate o serie de drepturi, printre care: dreptul de acces la date, dreptul de rectificare, dreptul la ștergerea datelor („dreptul de a fi uitat”) și dreptul de restricționare.
* **CUM SE APLICĂ AICI:** Deoarece aplicația noastră nu stochează absolut nicio dată personală și nu deține o bază de date, **nu colectăm informații pe care să le putem extrage, modifica sau șterge la cerere**. Datele dumneavoastră se șterg singure în momentul în care părăsiți website-ul sau închideți browserul.

### 5. SECURITATEA DATELOR
Deși datele sunt volatile și nu sunt păstrate pe server, transmisiunea dintre dispozitivul dumneavoastră (telefon sau calculator) și cloud este securizată prin protocoale de criptare SSL/TLS de ultimă generație furnizate automat prin infrastructura securizată a serverelor Streamlit Cloud.

### 6. FORMULARUL DE FEEDBACK ȘI CONTACT
Dacă decideți să folosiți pagina „Feedback & Contact”, datele introduse (Nume, Email, Mesaj) sunt transmise securizat prin intermediul serviciului terț FormSubmit direct către adresa de e-mail a administratorului (`leaiichim@gmail.com`). Aceste date sunt folosite exclusiv pentru a vă răspunde la solicitări și nu vor fi vândute, închiriate sau distribuite către nicio altă companie de marketing.
""")
