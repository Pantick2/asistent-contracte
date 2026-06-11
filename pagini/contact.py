import streamlit as st

st.title("💬 Feedback & Support")
st.markdown("Părerea ta contează! Trimite-ne idei de îmbunătățire sau raportează o problemă întâmpinată.")

form_html = """<form action="https://formsubmit.co" method="POST" style="background:#f8fafc; padding:25px; border-radius:12px;">
    <input type="text" name="name" placeholder="Nume" required style="width:100%; padding:10px; margin-bottom:15px; border-radius:6px; border:1px solid #ccc;"><br>
    <input type="email" name="email" placeholder="Email" required style="width:100%; padding:10px; margin-bottom:15px; border-radius:6px; border:1px solid #ccc;"><br>
    <textarea name="message" placeholder="Mesaj" required style="width:100%; height:150px; padding:10px; margin-bottom:15px; border-radius:6px; border:1px solid #ccc;"></textarea><br>
    <button type="submit" style="background:#0284c7; color:white; border:none; padding:12px 24px; border-radius:6px; font-weight:600; cursor:pointer;">Trimite Mesajul</button>
</form>"""
st.markdown(form_html, unsafe_allow_html=True)
