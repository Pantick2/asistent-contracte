import streamlit as st
from google import genai
from google.genai import types
import docx
import pypdf

st.markdown("""<style>
.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }
</style>""", unsafe_allow_html=True)

# ⚠️ PUNE CHEIA TA REALĂ ÎNTRE GHILIMELELE DE MAI JOS:
CHEIE_API_DEMO = "gen-lang-client-0040445167" 
LIMITA_UTILIZARI_GRATUITE = 2

if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

st.title("📄 Asistent de Negociere pentru Freelanceri")
st.markdown("<p style='font-size:18px; color:#475569;'>Protejează-ți business-ul. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.</p>", unsafe_allow_html=True)

if "rezultat_analiza" not in st.session_state:
    st.info("💡 **Cum folosim acest instrument:** Acest site funcționează ca un **copilot de negociere**. Informațiile generate sunt **strict orientative**. Acest instrument NU oferă asistență juridică sau consultanță de avocat. Aplicația aplică o politică de **zero stocare**.")
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown("<div class='feature-card'><b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale încâlcite în idei simple.</div>", unsafe_allow_html=True)
    with col2: st.markdown("<div class='feature-card'><b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele de plată.</div>", unsafe_allow_html=True)
    with col3: st.markdown("<div class='feature-card'><b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.</div>", unsafe_allow_html=True)

api_cheie_utilizator = st.sidebar.text_input("Cheie Gemini API personală:", type="password")
foloseste_mod_demo = True
cheie_finala = None

if api_cheie_utilizator.strip():
    cheie_finala = api_cheie_utilizator
    foloseste_mod_demo = False
    st.sidebar.success("Cheie personală activă.")
else:
    cheie_finala = CHEIE_API_DEMO
    st.sidebar.info(f"Modul DEMO activ ({st.session_state['numar_utilizari']}/{LIMITA_UTILIZARI_GRATUITE} analize).")

client = None
if cheie_finala and cheie_finala != "AICI_PUI_CHEIA_TA_GEMINI":
    client = genai.Client(api_key=cheie_finala)

uploaded_file = st.file_uploader("Trage sau încarcă contractul (PDF, DOCX, TXT):", type=["pdf", "docx", "txt"])
text_manual = st.text_area("Sau introdu textul clauzelor suspecte manual:", height=150)

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

if text_manual.strip():
    contract_final_text = text_manual

st.markdown("---")
st.caption("🔒 **Securitate & Disclaimer:** Conținutul documentelor nu este stocat sau folosit pentru antrenarea modelelor publice. Această analiză automată are rol informativ și nu înlocuiește sfatul unui avocat.")
accepta_gdpr = st.checkbox("Am citit, înțeleg și sunt de acord cu Termenii, Condițiile și procesarea datelor în conformitate cu GDPR.")
st.markdown("---")

if st.button("Pornește Analiza Inteligentă", type="primary", disabled=not accepta_gdpr):
    if foloseste_mod_demo and st.session_state["numar_utilizari"] >= LIMITA_UTILIZARI_GRATUITE:
        st.error("⚠️ Limita demo a fost atinsă!")
        st.link_button("🚀 Obține cheia ta gratuită", "https://google.com")
    elif not contract_final_text.strip():
        st.error("Te rugăm să introduci text sau să încarci un document.")
    elif client is None:
        st.error("Sistemul Demo nu este configurat!")
    else:
        with st.spinner("AI-ul scanează textul pentru riscuri legale..."):
            try:
                prompt_instruction = "Ești un expert juridic specializat în protecția freelancerilor. Analizează textul contractului oferit și identifică riscurile majore. Răspunde STRICT în limba ROMÂNĂ. Returnează rezultatul în format Markdown, cu structura: ### 🚩 [Nume Risc], Clauză originală, Traducere, De ce e periculoasă, Sugestie renegociere."
                response = client.models.generate_content(model='gemini-2.5-flash', contents=f"Contract:\n\n{contract_final_text}", config=types.GenerateContentConfig(system_instruction=prompt_instruction, temperature=0.2))
                if foloseste_mod_demo: st.session_state["numar_utilizari"] += 1
                st.session_state["rezultat_analiza"] = response.text
                st.success("Analiză finalizată cu succes!")
                st.rerun()
            except Exception as e: st.error(f"Eroare: {str(e)}")

if "rezultat_analiza" in st.session_state:
    st.markdown("## 🔍 Raport de Audit Contractual")
    st.markdown(st.session_state["rezultat_analiza"])
    st.download_button(label="Descarcă Raportul (.txt)", data=st.session_state["rezultat_analiza"], file_name="analiza.txt", mime="text/plain")
    
st.markdown("<br><hr><center style='color:#94a3b8; font-size:12px;'>🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)</center>", unsafe_allow_html=True)
