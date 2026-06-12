import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURARE APLICAȚIE (Trebuie să fie prima linie absolută)
st.set_page_config(page_title="Asistent Contracte Freelanceri", page_icon="📄", layout="wide")

# =====================================================================
# 🍪 INJECTARE PRIN COMPONENTĂ HTML (OBLIGATORIU PENTRU PYTHON 3.14)
# =====================================================================
LINK_SCRIPT_COOKIE = "https://cookie-script.com"
COD_CLIENT_ADSENSE = "ca-pub-3528838516008000"

html_antet = f"""
<script type="text/javascript" charset="UTF-8" src="{LINK_SCRIPT_COOKIE}"></script>
<script async src="https://googlesyndication.com{COD_CLIENT_ADSENSE}" crossorigin="anonymous"></script>
"""

# Forțăm randarea scripturilor printr-o componentă nativă Streamlit
components.html(html_antet, height=0)

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
st.sidebar.link_button(text_buton_donatie, "https://linktr.ee", type="primary")
st.sidebar.markdown("---")

# =====================================================================
# STRUCTURĂ OFICIALĂ DE PAGINI MULTI-PAGE (URL-URI ULTRA-SCURTE)
# =====================================================================
pagina_analiza = st.Page("pagini/analiza.py", title="🔍 Analiză", url_path="analiza", default=True)
pagina_contact = st.Page("pagini/contact.py", title="💬 Contact", url_path="contact")
pagina_termeni = st.Page("pagini/termeni.py", title="⚖️ Termeni", url_path="termeni")
pagina_gdpr = st.Page("pagini/politica.py", title="🔒 Politică", url_path="privacy")

# Generăm automat meniul din stânga securizat
pg = st.navigation([pagina_analiza, pagina_contact, pagina_termeni, pagina_gdpr])
pg.run()
