import streamlit as st

st.title("💬 Feedback & Contact")
st.write("Ai întâmpinat o problemă sau vrei să trimiți un feedback? Completează formularul de mai jos.")

st.markdown("---")

# ⚠️ ÎNLOCUIEȘTE EMAIL-UL DE MAI JOS CU ADRESA TA REALĂ UNDE VREI SĂ PRIMEȘTI MESAJELE:
ADRESA_TA_DE_EMAIL = "ichim.i1991@outlook.com"
import streamlit as st

st.title("💬 Feedback & Contact")
st.write("Ai întâmpinat o problemă sau vrei să trimiți un feedback? Completează formularul de mai jos.")

st.markdown("---")

# ⚠️ ÎNLOCUIEȘTE EMAIL-UL DE MAI JOS CU ADRESA TA REALĂ UNDE VREI SĂ PRIMEȘTI MESAJELE:
ADRESA_TA_DE_EMAIL = "iulianichim96@gmail.com"

# Construim formularul în Streamlit
with st.form("formular_contact", clear_on_submit=True):
    nume = st.text_input("Numele tău sau Alias (Freelancer / Firmă):")
    email_utilizator = st.text_input("Adresa ta de email (pentru a-ți putea răspunde):")
    tip_mesaj = st.selectbox("Tipul mesajului:", ["Feedback / Sugestie", "Raportare Eroare (Bug)", "Întrebare Generală"])
    mesaj = st.text_area("Mesajul tău:", height=150)
    
    # Butonul de trimitere din interiorul formularului
    buton_trimite = st.form_submit_button("Trimite Mesajul", type="primary")

# Logica de expediere prin FormSubmit (HTML integrat)
if buton_trimite:
    if not nume.strip() or not email_utilizator.strip() or not mesaj.strip():
        st.error("❌ Te rugăm să completezi toate câmpurile obligatorii (Nume, Email și Mesaj).")
    elif "@" not in email_utilizator:
        st.error("❌ Te rugăm să introduci o adresă de email validă.")
    else:
        # Codul HTML ascuns care trimite datele automat către email-ul tău
        form_html = f"""
        <form action="https://formsubmit.co{ADRESA_TA_DE_EMAIL}" method="POST" id="hidden_form" style="display:none;">
            <input type="text" name="Nume" value="{nume}">
            <input type="email" name="Email" value="{email_utilizator}">
            <input type="text" name="Tip Mesaj" value="{tip_mesaj}">
            <textarea name="Mesaj">{mesaj}</textarea>
            <input type="hidden" name="_next" value="https://google.com">
            <input type="hidden" name="_subject" value="[Asistent Contracte] Mesaj Nou: {tip_mesaj}">
            <input type="hidden" name="_captcha" value="false">
        </form>
        <script>
            document.getElementById('hidden_form').submit();
        </script>
        """
        # Executăm trimiterea în fundal
        st.components.v1.html(form_html, height=0)
        st.success("✅ Mesajul tău a fost procesat! Vei fi redirecționat pentru confirmarea finală.")

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)

# Construim formularul în Streamlit
with st.form("formular_contact", clear_on_submit=True):
    nume = st.text_input("Numele tău sau Alias (Freelancer / Firmă):")
    email_utilizator = st.text_input("Adresa ta de email (pentru a-ți putea răspunde):")
    tip_mesaj = st.selectbox("Tipul mesajului:", ["Feedback / Sugestie", "Raportare Eroare (Bug)", "Întrebare Generală"])
    mesaj = st.text_area("Mesajul tău:", height=150)
    
    # Butonul de trimitere din interiorul formularului
    buton_trimite = st.form_submit_button("Trimite Mesajul", type="primary")

# Logica de expediere prin FormSubmit (HTML integrat)
if buton_trimite:
    if not nume.strip() or not email_utilizator.strip() or not mesaj.strip():
        st.error("❌ Te rugăm să completezi toate câmpurile obligatorii (Nume, Email și Mesaj).")
    elif "@" not in email_utilizator:
        st.error("❌ Te rugăm să introduci o adresă de email validă.")
    else:
        # Codul HTML ascuns care trimite datele automat către email-ul tău
        form_html = f"""
        <form action="https://formsubmit.co{ADRESA_TA_DE_EMAIL}" method="POST" id="hidden_form" style="display:none;">
            <input type="text" name="Nume" value="{nume}">
            <input type="email" name="Email" value="{email_utilizator}">
            <input type="text" name="Tip Mesaj" value="{tip_mesaj}">
            <textarea name="Mesaj">{mesaj}</textarea>
            <input type="hidden" name="_next" value="https://google.com">
            <input type="hidden" name="_subject" value="[Asistent Contracte] Mesaj Nou: {tip_mesaj}">
            <input type="hidden" name="_captcha" value="false">
        </form>
        <script>
            document.getElementById('hidden_form').submit();
        </script>
        """
        # Executăm trimiterea în fundal
        st.components.v1.html(form_html, height=0)
        st.success("✅ Mesajul tău a fost procesat! Vei fi redirecționat pentru confirmarea finală.")

st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
