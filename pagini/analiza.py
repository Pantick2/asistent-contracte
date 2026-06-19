import streamlit as st
import streamlit.components.v1 as components
from google import genai
import docx
import pypdf
import openpyxl
import ads_config

if "limba" not in st.session_state:
    st.session_state["limba"] = "EN"

if "termeni_acceptati" not in st.session_state:
    st.session_state.termeni_acceptati = False

if "rezultat_analiza" not in st.session_state:
    st.session_state["rezultat_analiza"] = None

# Dicționarul de traduceri
t = {
    "RO": {
        "titlu": "📄 Asistent de Negociere Contractuală",
        "subtitlu": "Protejează-ți drepturile. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "avertisment_b2b": "⚠️ **Disclaimer Legal:** Această platformă este un instrument experimental bazat pe AI, destinat informării generale și educației contractuale.",
        "bifa_text": "Am citit, înțeleg și accept în mod exprimat Termenii de Utilizare și Politica de Confidențialitate (GDPR).",
        "blocat_text": "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        "ghid": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un copilot informativ. Rezultatele generate sunt strict orientative.",
        "c1": "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale complicate în cuvinte simple.",
        "c2": "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele abuzive.",
        "c3": "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        "side_s": "🚀 Cheie personală activată cu succes!",
        "side_d": "🔑 Introduceți cheia dvs. Gemini API Key în căsuța de mai jos pentru a debloca analiza.",
        "up_t": "Încarcă documentul (PDF, DOCX, XLSX, TXT):",
        "tx_t": "Sau introdu textul clauzelor suspecte manual:",
        "disc": "🔒 Securitate & Siguranta: Conținutul documentelor este procesat volatil. Analiză informativă.",
        "b_start": "Pornește Analiza Inteligentă",
        "e_text": "Te rugăm să introduci text sau să încarci un document.",
        "e_config": "❌ Eroare: Trebuie să introduceți o cheie Gemini API validă în bara laterală pentru a putea pornii analiza.",
        "spinner": "AI-ul scanează textul pentru riscuri contractuale...",
        "coada_msg": "⏳ Serverul procesează un alt document în acest moment. Sunteți în lista de așteptare, analiza dvs. va începe automat imediat...",
        "succes": "Analiză finalizată cu succes!",
        "rap_t": "## 🔍 Raport de Audit Contractual",
        "b_down": "Descarcă Raportul (.txt)",
        "prompt": "Ești un algoritm automat de scanare textuală și un asistent digital de tip scut contractual pentru business. NU ești avocat și NU oferi consultanță juridică. Analizează textul primit și identifică riscurile comerciale evidente. Structurează rezultatul în ROMÂNĂ: 1. Nume Risc Comercial, 2. Clauză originală, 3. Traducere pe înțelesul tuturor, 4. De ce poate fi o capcană de business, 5. Idee orientativă de renegociere.",
        "subsol": "🛡️ Asistent Contracte | Deținut de IULIAN ICHIM-UNGUREANU (Liak Studio)",
        "b_ghid": "📖 Ghid de Utilizare & Obținere Cheie API"
    },
    "EN": {
        "titlu": "📄 Contract Negotiation Assistant",
        "subtitlu": "Protect your business. Identify hidden clauses, contractual risks, and renegotiate with confidence.",
        "avertisment_b2b": "⚠️ **Legal Disclaimer:** This platform is an experimental AI-based tool intended strictly for general informational purposes.",
        "bifa_text": "I have read, understand, and agree to the Terms of Use and Privacy Policy (GDPR).",
        "blocat_text": "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        "ghid": "💡 **How to use this tool:** This site acts as an informational copilot. Generated results are strictly indicative.",
        "c1": "<b>💡 Guidance Guide</b><br>Translates complicated contractual clauses into simple terms.",
        "c2": "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or unfair terms.",
        "c3": "<b>🗣️ Negotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        "side_s": "🚀 Personal key activated successfully!",
        "side_d": "🔑 Please enter your Gemini API Key in the box below to unlock the analysis.",
        "up_t": "Upload document (PDF, DOCX, XLSX, TXT):",
        "tx_t": "Or enter text manually:",
        "disc": "🔒 Security & Safety: Document processed dynamically and not stored. Educational purposes only.",
        "b_start": "Start Intelligent Analysis",
        "e_text": "Please enter text or upload a document.",
        "e_config": "❌ Error: You must enter a valid Gemini API Key in the sidebar to run the analysis.",
        "spinner": "AI is scanning text for contractual risks...",
        "coada_msg": "⏳ The server is currently processing another document. You are in the waiting queue, your analysis will start automatically in a moment...",
        "succes": "Analysis completed successfully!",
        "rap_t": "## 🔍 Contractual Audit Report",
        "b_down": "Download Report (.txt)",
        "prompt": "You are an automated text scanning algorithm and a digital contract shield assistant for business. You are NOT a lawyer and you DO NOT provide legal advice. Analyze the text and identify obvious commercial risks. Structure the report in ENGLISH: 1. Commercial Risk Name, 2. Original Clause, 3. Plain English Translation, 4. Why it can be a business trap, 5. Tentative renegotiation suggestion.",
        "subsol": "🛡️ Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Liak Studio)",
        "b_ghid": "📖 User Guide & How to get API Key"
    }
}

L = t[st.session_state["limba"]]
st.markdown("<style>.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }</style>", unsafe_allow_html=True)

st.title(L["titlu"])
st.markdown(f"<p style='font-size:18px; color:#475569;'>{L['subtitlu']}</p>", unsafe_allow_html=True)

html_ad_config = f"""
<div style="display:none;">
    <script type="text/javascript" charset="UTF-8" src="https://cookie-script.com"></script>
</div>
"""
components.html(html_ad_config, height=0)

st.info(L["avertisment_b2b"])

# =====================================================================
# 📊 APELARE BANNER 1 (SIDEBAR)
# =====================================================================
st.sidebar.markdown("---")
st.sidebar.caption("Advertisement")
try:
    html_sidebar_ad = ads_config.genereaza_html_banner(ads_config.ID_BANNER_SIDEBAR, latime="100%", inaltime="250px")
    components.html(html_sidebar_ad, height=270)
except Exception:
    pass
# =====================================================================
# 🪟 POPUP MODAL CU INSTRUCȚIUNI DETALIATE ȘI GHID CHEIE API
# =====================================================================
if st.button(L["b_ghid"]):
    @st.dialog("User Guide & API Key Setup / Ghid de Utilizare", width="large")
    def afiseaza_ghid_modal():
        if st.session_state["limba"] == "RO":
            st.markdown("""
            ### 🛠️ Cum funcționează și cum se folosește aplicația:
            1. **Acceptarea Termenilor (Obligatoriu):** Bifează căsuța de confirmare GDPR de pe ecran. Aceasta deblochează formularele. Aplicația procesează datele volatil (în memorie), fără a stoca permanent documentele tale.
            2. **Introducerea Cheii API:** Mergi în bara laterală din stânga (Sidebar) și introdu cheia ta personală **Gemini API Key**. Aceasta asigură resursele de calcul dedicate pentru analiza ta.
            3. **Încărcarea Contractului:** Poți proceda în două moduri:
               * **Prin Document:** Încarcă un fișier în format **PDF, Word (.docx), Excel (.xlsx) sau Text (.txt)** utilizând zona de upload.
               * **Manual:** Dă copy-paste direct la paragrafele, clauzele sau textul suspect în căsuța mare de text.
            4. **Generarea Scutului:** Apasă pe butonul albastru **"Pornește Analiza Inteligentă"**. Algoritmul va rula documentul prin sistemul de coadă și va genera raportul în câteva secunde.
            
            ---
            
            ### 🔑 Ghid Pas cu Pas pentru Obținerea Cheii Gemini (100% Gratuit):
            Pentru a rula analize nelimitate pe contul tău, ai nevoie de o cheie gratuită de la Google. Urmează acești pași simpli de pe telefon sau PC:
            
            1. **Accesează Platforma:** Intră pe site-ul oficial Google pentru dezvoltatori: [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key).
            2. **Autentificare Securizată:** Conectează-te folosind contul tău obișnuit și personal de **Gmail / Google**.
            3. **Generarea Cheii:** 
               * În colțul din stânga sus, apasă pe butonul albastru mare pe care scrie **"Get API key"**.
               * În pagina următoare, apasă pe butonul **"Create API key"**.
               * Selectează proiectul tău (creat automat în mod gratuit de Google).
            4. **Copierea Codului:** Pe ecran va apărea o fereastră cu un cod lung (textul va începe cu literele `AIzaSy` sau formatul modern `AQ.`). Apasă pe butonul **"Copy"** pentru a-l salva în memoria dispozitivului tău.
            5. **Activarea Aplicației:** Întoarce-te pe acest site, inserează codul copiat în căsuța din stânga și ești gata! 
            
            ⚠️ *Notă de Siguranță:* Cheia ta este trimisă direct către serverele securizate ale Google prin conexiune criptată. Platforma noastră nu îți stochează, nu îți vede și nu îți salvează cheia sau conținutul contractelor.
            """)
        else:
            st.markdown("""
            ### 🛠️ How it works and how to use the application:
            1. **Accept Terms (Mandatory):** Check the GDPR confirmation box on the screen. This unlocks the interface. The application processes data dynamically in memory without storing your files permanently.
            2. **Enter your API Key:** Go to the left sidebar and paste your personal **Gemini API Key**. This provides the necessary computing power for your dedicated audit.
            3. **Upload the Contract:** You can choose between two methods:
               * **Via Document:** Upload a file in **PDF, Word (.docx), Excel (.xlsx), or Text (.txt)** format using the drag-and-drop area.
               * **Manually:** Copy and paste the specific paragraphs or suspicious clauses directly into the text area.
            4. **Run the Shield:** Click the blue button **"Start Intelligent Analysis"**. The algorithm will put the document in the processing queue and generate your report in a few seconds.
            
            ---
            
            ### 🔑 Step-by-Step Guide to Get a Gemini API Key (100% Free):
            To run unlimited contractual scans on your own account, you need a free key from Google. Follow these simple steps from your phone or PC:
            
            1. **Access the Platform:** Go to the official Google developer portal: [Google AI Studio](https://google.com).
            2. **Secure Login:** Sign in using your regular, personal **Gmail / Google** account.
            3. **Generate the Key:**
               * In the top-left corner, click the large blue button labeled **"Get API key"**.
               * On the next screen, click the **"Create API key"** button.
               * Select your project (automatically generated for free by Google).
            4. **Copy the Code:** A popup will display a long text string (starting with `AIzaSy` or the modern `AQ.`). Click the **"Copy"** button to save it to your clipboard.
            5. **Activate the Site:** Return to this website, paste the copied code into the sidebar input field, and you are ready!
            
            ⚠️ *Security Note:* Your key is transmitted directly to Google's secure servers via an encrypted connection. Our platform does not store, see, or save your API key or your contract's content.
            """)
    afiseaza_ghid_modal()

# =====================================================================
# 🔒 SISTEMUL DE BIFARE CONTRACTUAL
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

api_cheie_utilizator = st.sidebar.text_input("Gemini API Key:", type="password", key="cheie_utilizator_curata")
cheie_finala = None

if api_cheie_utilizator.strip():
    cheie_finala = api_cheie_utilizator.strip()
    st.sidebar.success(L["side_s"])
else:
    st.sidebar.info(L["side_d"])

if "rezultat_analiza" not in st.session_state:
    st.info(L["ghid"])
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
    with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
    with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(L["up_t"], type=["pdf", "docx", "xlsx", "txt"])
text_manual = st.text_area(L["tx_t"], height=150)
# Sistem de coadă sigur prin stocare cache nativă Streamlit
@st.cache_resource
def obtine_coada_globala():
    import threading
    return threading.Lock()

coada_globala = obtine_coada_globala()

contract_final_text = ""
if uploaded_file is not None:
    nm_f = uploaded_file.name.lower()
    if ".pdf" in nm_f:
        try: contract_final_text = "".join([p.extract_text() for p in pypdf.PdfReader(uploaded_file).pages])
        except Exception: pass
    elif ".docx" in nm_f:
        try: contract_final_text = "\n".join([pr.text for pr in docx.Document(uploaded_file).paragraphs])
        except Exception: pass
    elif ".xlsx" in nm_f:
        try:
            wb = openpyxl.load_workbook(uploaded_file, data_only=True)
            linii_excel = []
            for sheet in wb.worksheets:
                for row in sheet.iter_rows(values_only=True):
                    rand_text = " | ".join([str(cell) for cell in row if cell is not None])
                    if rand_text.strip(): linii_excel.append(rand_text)
            contract_final_text = "\n".join(linii_excel)
        except Exception: pass
    elif ".txt" in nm_f:
        try: contract_final_text = uploaded_file.read().decode("utf-8")
        except Exception: pass

if text_manual.strip(): 
    contract_final_text = text_manual

st.markdown("---")
st.caption(L["disc"])
st.markdown("---")

if st.button(L["b_start"], type="primary"):
    if not cheie_finala:
        st.error(L["e_config"])
    elif not contract_final_text.strip():
        st.error(L["e_text"])
    else:
        este_blocat = coada_globala.locked()
        
        with st.spinner(L["coada_msg"] if este_blocat else L["spinner"]):
            with coada_globala:
                try:
                    client = genai.Client(api_key=cheie_finala)
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=f"{L['prompt']}\n\n{contract_final_text}"
                    )
                    
                    if st.session_state["limba"] == "RO":
                        text_disclaimer_protectie = (
                            "⚠️ **NOTĂ IMPORTANTĂ DE SIGURANȚĂ JURIDICĂ:**\n"
                            "Acest raport este generat în mod automat de un algoritm bazat pe inteligență artificială și are un scop pur educativ, informativ și de orientare comercială generală. "
                            "Prezentele puncte reprezintă o opinie algoritmică strict orientativă și NU constituie consultanță juridică autorizată. Această platformă nu înlocuiește sub nicio formă un specialist în drept.\n\n"
                            "**Pentru decizii contractuale oficiale, sfaturi de specialitate și o expertiză legală autorizată, vă rugăm și vă recomandăm insistent să consultați o casă de avocatură autorizată sau un cabinet de avocatură înscris în Barou.**\n"
                            "--- \n\n"
                        )
                    else:
                        text_disclaimer_protectie = (
                            "⚠️ **IMPORTANT LEGAL DISCLAIMER:**\n"
                            "This report is automatically generated by an AI algorithm and is intended strictly for educational, informational, and general business guidance purposes. "
                            "These points represent a strictly indicative algorithmic opinion and DO NOT constitute authorized legal advice. This platform does not replace a legal professional.\n\n"
                            "**For official contractual decisions, professional advice, and authorized legal expertise, please and strongly we advise you to consult an authorized law firm or a licensed attorney.**\n"
                            "--- \n\n"
                        )
                    
                    st.session_state["rezultat_analiza"] = text_disclaimer_protectie + response.text
                    st.success(L["succes"])
                    st.rerun()
                except Exception as e:
                    st.error(f"Eroare AI: {str(e)}")

if "rezultat_analiza" in st.session_state and st.session_state["rezultat_analiza"]:
    st.markdown(L["rap_t"])
    st.markdown(st.session_state["rezultat_analiza"])
    st.download_button(label=L["b_down"], data=st.session_state["rezultat_analiza"], file_name="analiza.txt", mime="text/plain")
    
    st.markdown("---")
    try:
        html_final_ad = ads_config.genereaza_html_banner(ads_config.ID_BANNER_FINAL, latime="100%", inaltime="90px")
        components.html(html_final_ad, height=400)
    except Exception:
        pass

st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
