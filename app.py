import streamlit as st

# 1. CONFIGURARE APLICAȚIE (Trebuie să fie prima linie absolută)
st.set_page_config(page_title="Asistent Contracte Freelanceri", page_icon="📄", layout="wide")

# 🔍 INTERCEPTARE ȘI AFIȘARE DIRECTĂ ADS.TXT PENTRU GOOGLE
if "X-Recompute-For" in st.context.headers or "ads.txt" in st.query_params:
    st.text("google.com, pub-3528838516008000, DIRECT, f08c47fec0942fa0")
    st.stop()

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
# ☕ BUTONUL PERMANENT DE DONAȚII (ÎN SIDEBAR)
# =====================================================================
st.sidebar.markdown("---")
text_buton_donatie = "☕ Donate" if st.session_state["limba"] == "EN" else "☕ Donatie"
st.sidebar.link_button(text_buton_donatie, "https://linktr.ee/safescanallergyscan", type="primary")
st.sidebar.markdown("---")

# =====================================================================
# STRUCTURĂ OFICIALĂ DE PAGINI MULTI-PAGE
# =====================================================================
pagina_analiza = st.Page("pagini/analiza.py", title="🔍 Analiză", url_path="analiza", default=True)
pagina_contact = st.Page("pagini/contact.py", title="💬 Contact", url_path="contact")
pagina_termeni = st.Page("pagini/termeni.py", title="⚖️ Termeni", url_path="termeni")
pagina_gdpr = st.Page("pagini/politica.py", title="🔒 Politică", url_path="privacy")

pg = st.navigation([pagina_analiza, pagina_contact, pagina_termeni, pagina_gdpr])
pg.run()
