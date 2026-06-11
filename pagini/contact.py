import streamlit as st
import urllib.parse

if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

ADRESA_TA_DE_EMAIL = "ichim.i1991@outlook.com"

if st.session_state["limba"] == "RO":
    st.title("💬 Feedback & Contact")
    st.write("Ai întâmpinat o problemă sau vrei să trimiți un feedback? Completează câmpurile de mai jos.")
    nume = st.text_input("Numele tău sau Alias (Freelancer / Firmă):", key="txt_nume_ro")
    email_utilizator = st.text_input("Adresa ta de email (pentru a-ți putea răspunde):", key="txt_email_ro")
    tip_mesaj = st.selectbox("Tipul mesajului:", ["Feedback / Sugestie", "Raportare Eroare (Bug)", "Întrebare Generală"], key="sb_tip_ro")
    mesaj = st.text_area("Mesajul tău:", height=150, key="ta_mesaj_ro")
    
    if nume.strip() and email_utilizator.strip() and mesaj.strip():
        if "@" in email_utilizator:
            params = urllib.parse.urlencode({"_subject": f"[Asistent Contracte] Mesaj Nou: {tip_mesaj}", "Mesaj Complet": f"Nume: {nume}\nEmail: {email_utilizator}\nTip: {tip_mesaj}\n\nMensaj:\n{mesaj}", "_captcha": "false"})
            st.success("✅ Formularul este completat corect!")
            st.link_button("🚀 Trimite Mesajul", f"https://formsubmit.co{ADRESA_TA_DE_EMAIL}?{params}", type="primary")
        else:
            st.warning("⚠️ Adresa de email nu este validă.")
    else:
        st.info("💡 Completează toate câmpurile pentru a activa butonul.")
    st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)

else:
    st.title("💬 Feedback & Contact")
    st.write("Encountered an issue or want to send feedback? Please fill out the fields below.")
    nume = st.text_input("Your Name or Alias (Freelancer / Company):", key="txt_nume_en")
    email_utilizator = st.text_input("Your email address (to reply back to you):", key="txt_email_en")
    tip_mesaj = st.selectbox("Message Type:", ["Feedback / Suggestion", "Bug Report", "General Question"], key="sb_tip_en")
    mesaj = st.text_area("Your Message:", height=150, key="ta_mesaj_en")
    
    if nume.strip() and email_utilizator.strip() and mesaj.strip():
        if "@" in email_utilizator:
            params = urllib.parse.urlencode({"_subject": f"[Contract Assistant] New Message: {tip_mesaj}", "Full Message": f"Name: {nume}\nEmail: {email_utilizator}\nType: {tip_mesaj}\n\nMessage:\n{mesaj}", "_captcha": "false"})
            st.success("✅ Form it completed correctly!")
            st.link_button("🚀 Send Message", f"https://formsubmit.co{ADRESA_TA_DE_EMAIL}?{params}", type="primary")
        else:
            st.warning("⚠️ The email address is not valid.")
    else:
        st.info("💡 Complete all fields to activate the send button.")
    st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Freelancer Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
