import os
import streamlit as st

# =====================================================================
# INTERCEPTARE DIRECTĂ ADS.TXT LA NIVEL DE SERVER (FASTAPI/STARLETTE)
# =====================================================================
if os.environ.get("RENDER"):
    try:
        from streamlit.web.server.server import Server

        def patch_server():
            server = Server.get_current()
            if server and server._app:

                async def ads_txt_middleware(scope, receive, send):
                    if scope["type"] == "http" and scope["path"] == "/ads.txt":
                        payload = b"google.com, pub-3528838516008800, DIRECT, f08c47fec8942fa0"
                        await send(
                            {
                                "type": "http.response.start",
                                "status": 200,
                                "headers": [(b"content-type", b"text/plain")],
                            }
                        )
                        await send(
                            {
                                "type": "http.response.body",
                                "body": payload,
                            }
                        )
                        return
                    await server._app(scope, receive, send)

                server._app = ads_txt_middleware

        patch_server()
    except Exception:
        pass

# 1. CONFIGURARE APLICAȚIE (Trebuie să fie prima linie Streamlit apelată)
st.set_page_config(
    page_title="Contract Negotiation Assistant", page_icon="📄", layout="wide"
)

# =====================================================================
# 🔒 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE (LICENȚĂ EXCLUSIVĂ)
# =====================================================================
# ... de aici în jos lași codul tău exact așa cum era (Licență, Limbi, Pagini)

# =====================================================================
# 🔒 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE (LICENȚĂ EXCLUSIVĂ)
# =====================================================================
SEMNATURA_OBLIGATORIE = "IULIAN_ICHIM_UNGUREANU_ALIAS_LIAK_STUDIO_ASIST_SCUT_2026"
try:
    with open(__file__, "r", encoding="utf-8") as f:
        if "IULIAN_ICHIM_UNGUREANU" not in f.read():
            st.error("❌ EROARE: Licență invalidă sau cod modificat.")
            st.stop()
except Exception:
    pass

# =====================================================================
# 🌐 COMUTATOR GLOBAL DE LIMBĂ - IMPLICIT PE ENGLEZĂ (EN)
# =====================================================================
if "limba" not in st.session_state:
    st.session_state["limba"] = "EN"

optiune_limba = st.sidebar.selectbox(
    "🌐 Language / Schimbă Limba:",
    ["English (EN)", "Română (RO)"],
    index=0
)
st.session_state["limba"] = "EN" if "English" in optiune_limba else "RO"

# =====================================================================
# ☕ BUTONUL PERMANENT DE DONAȚII (ÎN SIDEBAR)
# =====================================================================
st.sidebar.markdown("---")
text_buton_donatie = "☕ Donate" if st.session_state["limba"] == "EN" else "☕ Donatie"
st.sidebar.link_button(text_buton_donatie, "https://linktr.ee", type="primary")
st.sidebar.markdown("---")

# =====================================================================
# STRUCTURĂ OFICIALĂ DE PAGINI MULTI-PAGE (Meniu în Engleză nativ)
# =====================================================================
titlu_analiza = "🔍 Analysis" if st.session_state["limba"] == "EN" else "🔍 Analiză"
titlu_contact = "💬 Contact"
titlu_termeni = "⚖️ Terms of Use" if st.session_state["limba"] == "EN" else "⚖️ Termeni"
titlu_politica = "🔒 Privacy Policy" if st.session_state["limba"] == "EN" else "🔒 Politică"

pagina_analiza = st.Page("pagini/analiza.py", title=titlu_analiza, url_path="analiza", default=True)
pagina_contact = st.Page("pagini/contact.py", title=titlu_contact, url_path="contact")
pagina_termeni = st.Page("pagini/termeni.py", title=titlu_termeni, url_path="termeni")
pagina_gdpr = st.Page("pagini/politica.py", title=titlu_politica, url_path="privacy")

pg = st.navigation([pagina_analiza, pagina_contact, pagina_termeni, pagina_gdpr])
pg.run()
