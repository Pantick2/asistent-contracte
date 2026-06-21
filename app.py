import inject_adsense  # <--- ACEASTA TREBUIE SĂ FIE PRIMA LINIE!
import streamlit as st
import os

# --- INJECTARE COD DE VERIFICARE GOOGLE ADSENSE ---
st.components.v1.html(
    """
    <script async src="https://googlesyndication.com"
     crossorigin="anonymous"></script>
    """,
    height=0,
    width=0
)
# -------------------------------------------------------------
# RESTUL APLICAȚIEI TALE CONTINUĂ DE AICI ÎN JOS (de la vechea linie 34)
# -------------------------------------------------------------


    # Rulăm injectarea rutei imediat ce serverul devine disponibil
    import threading

    def pornire_intarziata():
        import time

        time.sleep(2)
        try:
            from streamlit.runtime import runtime

            if runtime.exists():
                st.sdk.main.get_instance()._run_on_server(
                    adauga_ruta_ads
                )  # Alternativă sigură de execuție pe buclă
        except:
            try:
                adauga_ruta_ads()
            except:
                pass


    threading.Thread(target=pornire_intarziata, daemon=True).start()
except:
    pass

# 1. CONFIGURARE APLICAȚIE (Trebuie să rămână prima linie activă din Streamlit)
st.set_page_config(
    page_title="Contract Negotiation Assistant", page_icon="📄", layout="wide"
)

# =====================================================================
# 🔒 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE (LICENȚĂ EXCLUSIVELY)
# =====================================================================
# ... restul codului tău cu licența și meniurile din screenshot continuă neschimbat aici ...


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
