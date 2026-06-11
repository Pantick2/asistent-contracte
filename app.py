import streamlit as st

# Configurare aplicație (Trebuie să fie prima linie absolută)
st.set_page_config(page_title="Asistent Contracte Freelanceri", page_icon="📄", layout="wide")

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
# 🌐 COMUTATOR GLOBAL DE LIMBĂ (ÎN SIDEBAR)
# =====================================================================
if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"

optiune_limba = st.sidebar.selectbox(
    "🌐 Schimbă Limba / Language:",
    ["Română (RO)", "English (EN)"],
    index=0 if st.session_state["limba"] == "RO" else 1
)

st.session_state["limba"] = "RO" if "Română" in optiune_limba else "EN"

# =====================================================================
# ☕ BUTONUL DEFINITIV ȘI PERMANENT DE DONAȚII (ÎN SIDEBAR, SUB MENIU)
# =====================================================================
st.sidebar.markdown("---")
# Textul butonului se schimbă automat în funcție de limba selectată mai sus
text_buton_donatie = "☕ Donate" if st.session_state["limba"] == "EN" else "☕ Donatie"
st.sidebar.link_button(text_buton_donatie, "https://linktr.ee", type="primary")
st.sidebar.markdown("---")

# =====================================================================
# STRUCTURĂ OFICIALĂ DE PAGINI MULTI-PAGE (MAPPED DIRECT PE FIȘIERE)
# =====================================================================
pagina_analiza = st.Page("pagini/analiza.py", title="🔍 Aplicație Analiză", default=True)
pagina_contact = st.Page("pagini/contact.py", title="💬 Feedback & Contact")
pagina_termeni = st.Page("pagini/termeni.py", title="⚖️ Termeni și Condiții")
pagina_gdpr = st.Page("pagini/politica.py", title="🔒 Politica de Confidențialitate")

# Generăm automat meniul din stânga securizat
pg = st.navigation([pagina_analiza, pagina_contact, pagina_termeni, pagina_gdpr])
pg.run()
