import streamlit as st

# Configurare aplicație (Trebuie să fie prima linie)
st.set_page_config(page_title="Asistent Contracte Freelanceri", page_icon="📄", layout="wide")

# =====================================================================
# ☕ ANTET GLOBAL PERMANENT (Butonul fix de donație în dreapta sus)
# =====================================================================
col_spatiu, col_buton = st.columns([8.5, 1.5])
with col_buton:
    st.link_button("Donatie / Donate", "https://linktr.ee", type="primary")

# =====================================================================
# 🔒 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE (LICENȚĂ EXCLUSIVĂ)
# =====================================================================
SEMNATURA_OBLIGATORIE = "IULIAN_ICHIM_UNGUREANU_ALIAS_PANTICK_ASIST_SCUT_2026"

try:
    with open(__file__, "r", encoding="utf-8") as f:
        if "IULIAN_ICHIM_UNGUREANU" not in f.read():
            st.error("❌ EROARE: Licență invalidă sau cod modificat.")
            st.stop()
except Exception:
    pass

# =====================================================================
# STRUCTURĂ OFICIALĂ DE PAGINI MULTI-PAGE (IMUNĂ LA ERORI)
# =====================================================================
pagina_analiza = st.Page("pagini/analiza.py", title="🔍 Aplicație Analiză", default=True)
pagina_contact = st.Page("pagini/contact.py", title="💬 Feedback & Contact")
pagina_termeni = st.Page("pagini/termeni.py", title="⚖️ Termeni și Condiții")
pagina_gdpr = st.Page("pagini/politica.py", title="🔒 Politica de Confidențialitate")

# Generăm automat meniul din stânga securizat
pg = st.navigation([pagina_analiza, pagina_contact, pagina_termeni, pagina_gdpr])
pg.run()
