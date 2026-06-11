import streamlit as st
from google import genai
from google.genai import types
import docx
import pypdf

# =====================================================================
# 🔒 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE (LICENȚĂ EXCLUSIVĂ)
# =====================================================================
SEMNATURA_OBLIGATORIE = "IULIAN_ICHIM_UNGUREANU_ALIAS_PANTICK_ASIST_SCUT_2026"

def verifica_integritate_cod():
    try:
        with open(__file__, "r", encoding="utf-8") as f:
            if f.read().count("IULIAN_ICHIM_UNGUREANU") < 1:
                st.error("❌ EROARE: Licență invalidă sau cod modificat.")
                st.stop()
    except Exception:
        pass

verifica_integritate_cod()

# =====================================================================
# CONFIGURARE PAGINĂ ȘI VARIABILE GLOBALE
# =====================================================================
st.set_page_config(page_title="Asistent Contracte Freelanceri", page_icon="📄", layout="wide")

st.markdown("""<style>html, body, [data-testid="stSidebarView"] { font-family: 'Inter', sans-serif; }
.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }</style>""", unsafe_allow_html=True)

CHEIE_API_DEMO = "gen-lang-client-0040445167" 
LIMITA_UTILIZARI_GRATUITE = 2

if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

TEXTS = {
    "ro": {
        "title": "📄 Asistent de Negociere pentru Freelanceri",
        "subtitle": "Protejează-ți business-ul. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "sidebar_lang": "Limba interfeței / Language:",
        "sidebar_api": "Cheie Gemini API personală:",
        "api_info": f"Modul DEMO activ ({LIMITA_UTILIZARI_GRATUITE} analize gratuite).",
        "limit_reached_msg": "⚠️ Limita demo a fost atinsă!",
        "limit_instructions": "Pentru a continua să folosești instrumentul gratuit, generează o cheie API proprie din Google AI Studio. Este gratuit și durează un minut.",
        "btn_get_key": "🚀 Obține cheia ta gratuită",
        "file_label": "Trage sau încarcă contractul (PDF, DOCX, TXT):",
        "text_label": "Sau introdu textul clauzelor suspecte manual:",
        "btn_analyze": "Pornește Analiza Inteligentă",
        "err_no_text": "Te rugăm să introduci text sau să încarci un document.",
        "spinner": "AI-ul scanează textul pentru riscuri legale...",
        "success": "Analiză finalizată cu succes!",
        "result_header": "🔍 Raport de Audit Contractual și Contra-argumente",
        "btn_download": "Descarcă Raportul de Negociere (.txt)",
        "welcome_disclaimer": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un **copilot de negociere**. Informațiile generate sunt **strict orientative**. Acest instrument NU oferă asistență juridică sau consultanță de avocat. Aplicația aplică o politică de **zero stocare**. 📋 *Vă rugăm să verificați „Termenii și Condițiile” și „Politica de Confidențialitate” din meniul lateral pentru mai multe detalii.*",
        "gdpr_text": "🔒 **Securitate & Disclaimer:** Conținutul documentelor nu este stocat sau folosit pentru antrenarea modelelor publice. Această analiză automată are rol informativ și nu înlocuiește sfatul unui avocat.",
        "gdpr_checkbox": "Am citit, înțeleg și sunt de acord cu Termenii, Condițiile și procesarea datelor în conformitate cu GDPR.",
        "card1_title": "💡 Ghid de Îndrumare", "card1_desc": "Traduce clauzele contractuale încâlcite în idei simple, ca să înțelegi exact ce ți se cere.",
        "card2_title": "🚩 Alertă Clauze Ascunse", "card2_desc": "Semnalează penalitățile disproporționate sau termenele de plată care te-ar putea dezavantaja.",
        "card3_title": "🗣️ Idei de Renegociere", "card3_desc": "Îți oferă argumente și formulări politicoase pentru a propune modificări de la egal la egal.",
        "prompt_instruction": "Ești un expert juridic specializat în protecția freelancerilor. Analizează textul contractului oferit și identifică riscurile majore (penalități disproporționate, proprietate intelectuală abuzivă, termene de plată nerealiste, clauze de exclusivitate ascunse, reziliere unilaterală defavorabilă). Răspunde STRICT în limba ROMÂNĂ. Returnează rezultatul în format Markdown, cu următoarea structură pentru fiecare problemă găsită:\n### 🚩 [Numele Riscului]\n- **Clauza originală:** [Textul din contract]\n- **Traducere pe înțelesul tuturor:** [Ce înseamnă de fapt în limbaj simplu]\n- **De ce este periculoasă:** [Riscul real pentru freelancer]\n- **Sugestie de renegociere:** [Cum să reformuleze sau ce contra-argument să folosească]"
    },
    "en": {
        "title": "📄 Freelancer Contract Assistant",
        "subtitle": "Protect your business. Spot hidden unfair clauses and negotiate like a pro.",
        "sidebar_lang": "Language / Limba interfeței:",
        "sidebar_api": "Personal Gemini API Key:",
        "api_info": f"DEMO mode active ({LIMITA_UTILIZARI_GRATUITE} free analyses).",
        "limit_reached_msg": "⚠️ Demo limit reached!",
        "limit_instructions": "To keep using this tool for free, generate your own API key in Google AI Studio.",
        "btn_get_key": "🚀 Get your free key here",
        "file_label": "Upload your contract (PDF, DOCX, TXT):",
        "text_label": "Or paste the suspicious clauses here:",
        "btn_analyze": "Start Smart Analysis",
        "err_no_text": "Please upload a file or paste contract text.",
        "spinner": "AI is auditing the text for legal risks...",
        "success": "Analysis completed successfully!",
        "result_header": "🔍 Contract Audit Report & Counter-arguments",
        "btn_download": "Download Negotiation Report (.txt)",
        "welcome_disclaimer": "💡 **How to use this tool:** This site acts as a **negotiation copilot**. The insights are **strictly for guidance**. This tool DOES NOT provide legal advice. The app enforces a **zero-storage policy**. 📋 *Please review the \"Terms and Conditions\" and \"Privacy Policy\" in the sidebar.*",
        "gdpr_text": "🔒 **Security & Disclaimer:** Document contents are not stored or used to train public models. This automated analysis is informative and does not replace the advice of a lawyer.",
        "gdpr_checkbox": "I have read, understood, and agree to the Terms, Conditions, and data processing in accordance with GDPR.",
        "card1_title": "💡 Guidance Guide", "card1_desc": "Translates tangled legal clauses into simple ideas.",
        "card2_title": "🚩 Hidden Clauses Alert", "card2_desc": "Flags disproportionate penalties or payment terms.",
        "card3_title": "🗣️ Negotiation Ideas", "card3_desc": "Gives you polite yet firm arguments and scripts to propose contract changes.",
        "prompt_instruction": "You are a legal expert specialized in pointing out high-risk contract terms for freelance professionals. Analyze the contract and outline responses in English. Return Markdown."
    }
}

# =====================================================================
# BARA LATERALĂ DE NAVIGARE (SIDEBAR)
# =====================================================================
st.sidebar.markdown("<h2 style='text-align: center; color: #0284c7;'>🛡️ Asistent Scut</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Meniu de navigare cu denumiri fixe
pagina_curenta = st.sidebar.radio("Navigare pagini:", ["Aplicație Analiză", "Feedback & Contact", "Termeni și Condiții", "Politică de Confidențialitate"])

st.sidebar.markdown("---")
lang = st.sidebar.selectbox(TEXTS["ro"]["sidebar_lang"], options=["ro", "en"], format_func=lambda x: "🇷🇴 Română" if x == "ro" else "🇺🇸 English")
t = TEXTS[lang]

# =====================================================================
# FUNCȚII EXTRAGERE TEXT LINIARĂ
# =====================================================================
def citeste_contract_pdf(file_obj):
    txt_acumulat = ""
    try:
        pdf_rd = pypdf.PdfReader(file_obj)
        for p in pdf_rd.pages:
            txt_acumulat += p.extract_text() or ""
    except Exception: pass
    return txt_acumulat

def citeste_contract_docx(file_obj):
    txt_acumulat = ""
    try:
        doc_rd = docx.Document(file_obj)
        for pr in doc_rd.paragraphs:
            txt_acumulat += pr.text + "\n"
    except Exception: pass
    return txt_acumulat

# =====================================================================
# BLOC LOGIC DE RULARE STRUCTURAT (IF - ELIF - ELSE LEGATE STRÂNS)
# =====================================================================
if pagina_curenta == "Aplicație Analiză":
    st.title(t["title"])
    st.markdown(f"<p style='font-size:18px; color:#475569;'>{t['subtitle']}</p>", unsafe_allow_html=True)
    
    if "rezultat_analiza" not in st.session_state:
        st.info(t["welcome_disclaimer"])
        col1, col2, col3 = st.columns(3)
        with col1: st.markdown(f"<div class='feature-card'><b>{t['card1_title']}</b><br>{t['card1_desc']}</div>", unsafe_allow_html=True)
        with col2: st.markdown(f"<div class='feature-card'><b>{t['card2_title']}</b><br>{t['card2_desc']}</div>", unsafe_allow_html=True)
        with col3: st.markdown(f"<div class='feature-card'><b>{t['card3_title']}</b><br>{t['card3_desc']}</div>", unsafe_allow_html=True)

    api_cheie_utilizator = st.sidebar.text_input(t["sidebar_api"], type="password")
    foloseste_mod_demo = True
    cheie_finala = None

    if api_cheie_utilizator.strip():
        cheie_finala = api_cheie_utilizator
        foloseste_mod_demo = False
        st.sidebar.success("Cheie personală activă.")
    else:
        cheie_finala = CHEIE_API_DEMO
        st.sidebar.info(f"{t['api_info']} ({st.session_state['numar_utilizari']}/{LIMITA_UTILIZARI_GRATUITE})")

    client = None
    if cheie_finala and cheie_finala != "AICI_PUI_CHEIA_TA_GEMINI":
        client = genai.Client(api_key=cheie_finala)

