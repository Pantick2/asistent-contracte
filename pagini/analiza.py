# =====================================================================
# 🔒 SISTEMUL DE BIFARE MUTAT DUPĂ RECLAMELE DE SIDEBAR
# =====================================================================
accepta_termeni = st.checkbox(L["bifa_text"], value=st.session_state.termeni_acceptati, key="chk_termeni_obligatoriu")
st.session_state.termeni_acceptati = accepta_termeni

if not st.session_state.termeni_acceptati:
    st.warning(L["blocat_text"])
    if "rezultat_analiza" not in st.session_state:
        st.info(L["ghid"])
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
        with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
        with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)
    st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
    st.stop()

# INTERFATA DE INPUT (APARE DUPĂ BIFA ACTIVĂ)
api_cheie_utilizator = st.sidebar.text_input("Gemini API Key:", type="password")
foloseste_mod_demo = True
cheie_finala = None

if api_cheie_utilizator.strip():
    cheie_finala = api_cheie_utilizator
    foloseste_mod_demo = False
    st.sidebar.success(L["side_s"])
else:
    cheie_finala = CHEIE_API_DEMO
    st.sidebar.info(f"{L['side_d']} ({st.session_state['numar_utilizari']}/{LIMITA_UTILIZARI_GRATUITE} analize).")

client = genai.Client(api_key=cheie_finala) if cheie_finala else None

if "rezultat_analiza" not in st.session_state:
    st.info(L["ghid"])
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
    with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
    with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(L["up_t"], type=["pdf", "docx", "txt"])
text_manual = st.text_area(L["tx_t"], height=150)

contract_final_text = ""
if uploaded_file is not None:
    nm_f = uploaded_file.name.lower()
    if ".pdf" in nm_f:
        try: contract_final_text = "".join([p.extract_text() for p in pypdf.PdfReader(uploaded_file).pages])
        except Exception: pass
    if ".docx" in nm_f:
        try: contract_final_text = "\n".join([pr.text for pr in docx.Document(uploaded_file).paragraphs])
        except Exception: pass
    if ".txt" in nm_f:
        try: contract_final_text = uploaded_file.read().decode("utf-8")
        except Exception: pass

if text_manual.strip(): contract_final_text = text_manual

st.markdown("---")
st.caption(L["disc"])
st.markdown("---")

if st.button(L["b_start"], type="primary"):
    if foloseste_mod_demo and st.session_state["numar_utilizari"] >= LIMITA_UTILIZARI_GRATUITE:
        st.error(L["e_limita"])
    elif not contract_final_text.strip():
        st.error(L["e_text"])
    elif client is None:
        st.error(L["e_config"])
    else:
        with st.spinner(L["spinner"]):
            try:
                response = client.models.generate_content(model='gemini-2.5-flash', contents=f"Contract:\n\n{contract_final_text}", config=types.GenerateContentConfig(system_instruction=L["prompt"], temperature=0.2))
                if foloseste_mod_demo: st.session_state["numar_utilizari"] += 1
                st.session_state["rezultat_analiza"] = response.text
                st.success(L["succes"])
                st.rerun()
            except Exception as e: st.error(f"Eroare: {str(e)}")

# =====================================================================
# 📊 APELARE BANNER 2 (MĂRIT PENTRU A LĂSA LOC POPUP-ULUI SĂ APARĂ)
# =====================================================================
if "rezultat_analiza" in st.session_state:
    st.markdown(L["rap_t"])
    st.markdown(st.session_state["rezultat_analiza"])
    st.download_button(label=L["b_down"], data=st.session_state["rezultat_analiza"], file_name="analiza.txt", mime="text/plain")
    
    st.markdown("---")
    html_final_ad = ads_config.genereaza_html_banner(ads_config.ID_BANNER_FINAL, latime="100%", inaltime="90px")
    # Schimbăm height de la 110 la 400 pentru ca fereastra de cookie-uri să aibă loc fizic să se deschidă pe ecran
    components.html(html_final_ad, height=400)

st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
