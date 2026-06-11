import streamlit as st
import urllib.parse

st.title("💬 Feedback & Contact")
st.write("Ai întâmpinat o echipă, o problemă sau vrei să trimiți un feedback? Completează câmpurile de mai jos.")

st.markdown("---")

# ⚠️ EMAIL-UL TĂU REAL:
ADRESA_TA_DE_EMAIL = "ichim.i1991@outlook.com"

# Câmpurile formularului (fără st.form pentru a evita eroarea de duplicat)
nume = st.text_input("Numele tău sau Alias (Freelancer / Firmă):", key="txt_nume_contact")
email_utilizator = st.text_input("Adresa ta de email (pentru a-ți putea răspunde):", key="txt_email_contact")
tip_mesaj = st.selectbox("Tipul mesajului:", ["Feedback / Sugestie", "Raportare Eroare (Bug)", "Întrebare Generală"], key="sb_tip_contact")
mesaj = st.text_area("Mesajul tău:", height=150, key="ta_mesaj_contact")

st.markdown("---")

# Validare și generare link securizat
if nume.strip() and email_utilizator.strip() and mesaj.strip():
    if "@" in email_utilizator:
        # Codificăm textul pentru a fi trimis în siguranță prin URL direct către FormSubmit
        subiect_mail = f"[Asistent Contracte] Mesaj Nou: {tip_mesaj}"
        text_complet = f"Nume: {nume}\nEmail: {email_utilizator}\nTip: {tip_mesaj}\n\nMesaj:\n{mesaj}"
        
        params = urllib.parse.urlencode({
            "_subject": subiect_mail,
            "Mesaj Complet": text_complet,
            "_captcha": "false"
        })
        
        url_trimitere = f"https://formsubmit.co{ADRESA_TA_DE_EMAIL}?{params}"
        
        st.success("✅ Formularul este completat corect!")
        st.link_button("🚀 Trimite Mesajul prin FormSubmit", url_trimitere, type="primary")
    else:
        st.warning("⚠️ Adresa de email nu este validă (lipsește caracterul @).")
else:
    st.info("💡 Completează Numele, Email-ul și Mesajul pentru a activa butonul de trimitere.")

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
