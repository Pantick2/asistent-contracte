import streamlit as st

# 1. Configurare aplicație (Trebuie să fie prima linie absolută)
st.set_page_config(page_title="Asistent Contracte Freelanceri", page_icon="📄", layout="wide")

# 2. Gestionare implicită a limbii (pentru a ști ce scrie pe butonul global)
if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

# =====================================================================
# ☕ ANTETUL GLOBAL FIX (Apare pe toate paginile, sus în colț)
# =====================================================================
col_spatiu, col_buton = st.columns([8.5, 1.5])

with col_buton:
    # Textul butonului se schimbă dinamic dacă utilizatorul schimbă limba în aplicație
    text_global_donatie = "Donate" if st.session_state["limba"] == "EN" else "Donatie"
    st.link_button(text_global_donatie, "https://linktr.ee", type="primary")

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
# STRUCTURĂ OFICIALĂ DE PAGINI MULTI-PAGE
# =====================================================================
pagina_analiza = st.Page("pagini/analiza.py", title="🔍 Aplicație Analiză", default=True)
pagina_contact = st.Page("pagini/contact.py", title="💬 Feedback & Contact")
pagina_termeni = st.Page("pagini/termeni.py", title="⚖️ Termeni și Condiții")
pagina_gdpr = st.Page("pagini/politica.py", title="🔒 Politica de Confidențialitate")

# Lansarea meniului și randarea paginii curente sub butonul global
pg = st.navigation([pagina_analiza, pagina_contact, pagina_termeni, pagina_gdpr])
pg.run()
