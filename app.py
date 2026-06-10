import streamlit as st
from google import genai
from google.genai import types
import docx  # Pentru citirea fișierelor Word (pip install python-docx)
import pypdf  # Pentru citirea fișierelor PDF (pip install pypdf)

# =====================================================================
# 🔒 SISTEM ANTIFURT ȘI VERIFICARE INTEGRITATE (LICENȚĂ EXCLUSIVĂ)
# =====================================================================
SEMNATURA_OBLIGATORIE = "PROPRIETATE_INTELECTUALA_IULIAN_ICHIM_UNGUREANU_ALIAS_PANTICK_ASIST_SCUT_2026"

def verifica_integritate_cod():
    try:
        cale_fisier = __file__
        with open(cale_fisier, "r", encoding="utf-8") as f:
            continut_cod = f.read()
        
        if continut_cod.count(SEMNATURA_OBLIGATORIE) < 2:
            st.error("❌ EROARE CRITICĂ: Licență invalidă sau cod modificat neautorizat.")
            st.warning("Această aplicație aparține de drept lui IULIAN ICHIM-UNGUREANU (Pantick). Accesul este blocat.")
            st.stop()
    except Exception:
        st.error("❌ Eroare de sistem la verificarea licenței de autor.")
        st.stop()

# Declanșăm verificarea automată la fiecare rulare
verifica_integritate_cod()
# =====================================================================

# =====================================================================
# CONFIGURARE PAGINĂ ȘI DESIGN PREMIUM (Cromatica Slate & Blue)
# =====================================================================
st.set_page_config(
    page_title="Asistent Contracte Freelanceri", 
    page_icon="📄", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injectare CSS personalizat pentru aspect profesional și carduri responsive
st.markdown("""
    <style>
        html, body, [data-testid="stSidebarView"] {
            font-family: 'Inter', sans-serif;
        }
        .feature-card {
            background-color: #f8fafc;
            padding: 20px;
            border-radius: 12px;
            border-left: 5px solid #0284c7;
            margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .feature-title {
            color: #0f172a;
            font-weight: 600;
            margin-bottom: 5px;
            font-size: 16px;
        }
        .feature-desc {
            color: #475569;
            font-size: 14px;
            line-height: 1.5;
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# CONFIGURARE LOGICĂ DE MONETIZARE ȘI CONTORIZARE DEMO
# =====================================================================
CHEIE_API_DEMO = "gen-lang-client-0040445167" 
LIMITA_UTILIZARI_GRATUITE = 2

if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

# =====================================================================
# DICȚIONARUL DE LIMBI (INTERFAȚĂ ȘI INSTRUCȚIUNI AI)
# =====================================================================
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
        "welcome_disclaimer": (
            "💡 **Cum folosim acest instrument:** Acest site funcționează ca un **copilot de negociere** pentru a te ajuta să înțelegi jargonul comercial. "
            "Informațiile generate sunt **strict orientative și de îndrumare**. Acest instrument NU oferă asistență juridică sau consultanță de avocat. "
            "Aplicația aplică o politică de **zero stocare**: textul tău este procesat instant și se șterge automat când închizi pagina. "
            "📋 *Vă rugăm să verificați „Termenii și Condițiile” și „Politica de Confidențialitate” din meniul lateral pentru mai multe detalii.*"
        ),
        "gdpr_text": "🔒 **Securitate & Disclaimer:** Conținutul documentelor nu este stocat sau folosit pentru antrenarea modelelor publice. Această analiză automată are rol informativ și nu înlocuiește sfatul unui avocat.",
        "gdpr_checkbox": "Am citit, înțeleg și sunt de acord cu Termenii, Condițiile și procesarea datelor în conformitate cu GDPR.",
        "card1_title": "💡 Ghid de Îndrumare",
        "card1_desc": "Traduce clauzele contractuale încâlcite în idei simple, ca să înțelegi exact ce ți se cere.",
        "card2_title": "🚩 Alertă Clauze Ascunse",
        "card2_desc": "Semnalează penalitățile disproporționate sau termenele de plată care te-ar putea dezavantaja.",
        "card3_title": "🗣️ Idei de Renegociere",
        "card3_desc": "Îți oferă argumente și formulări politicoase pentru a propune modificări de la egal la egal.",
        "prompt_instruction": (
            "Ești un expert juridic specializat în protecția freelancerilor. "
            "Analizează textul contractului oferit și identifică riscurile majore (penalități disproporționate, "
            "proprietate intelectuală abuzivă, termene de plată nerealiste, clauze de exclusivitate ascunse, reziliere unilaterală defavorabilă). "
            "Răspunde STRICT în limba ROMÂNĂ. "
            "Returnează rezultatul în format Markdown, cu următoarea structură pentru fiecare problemă găsită:\n"
            "### 🚩 [Numele Riscului]\n"
            "- **Clauza originală:** [Textul din contract]\n"
            "- **Traducere pe înțelesul tuturor:** [Ce înseamnă de fapt în limbaj simplu]\n"
            "- **De ce este periculoasă:** [Riscul real pentru freelancer]\n"
            "- **Sugestie de renegociere:** [Cum să reformuleze sau ce contra-argument să folosească]"
        )
    },
    "en": {
        "title": "📄 Freelancer Contract Negotiation Assistant",
        "subtitle": "Protect your business. Spot hidden unfair clauses and negotiate like a pro.",
        "sidebar_lang": "Language / Limba interfeței:",
        "sidebar_api": "Personal Gemini API Key:",
        "api_info": f"DEMO mode active ({LIMITA_UTILIZARI_GRATUITE} free analyses).",
        "limit_reached_msg": "⚠️ Demo limit reached!",
        "limit_instructions": "To keep using this tool for free, generate your own API key in Google AI Studio. It takes under a minute.",
        "btn_get_key": "🚀 Get your free key here",
        "file_label": "Drag and drop your contract (PDF, DOCX, TXT):",
        "text_label": "Or paste the suspicious clauses here:",
        "btn_analyze": "Start Smart Analysis",
        "err_no_text": "Please upload a file or paste contract text.",
        "spinner": "AI is auditing the text for legal risks...",
        "success": "Analysis completed successfully!",
        "result_header": "🔍 Contract Audit Report & Counter-arguments",
        "btn_download": "Download Negotiation Report (.txt)",
        "welcome_disclaimer": (
            "💡 **How to use this tool:** This site acts as a **negotiation copilot** to help you understand business jargon. "
            "The generated insights are **strictly for guidance and educational purposes**. This tool DOES NOT provide legal advice or attorney services. "
            "The app enforces a **zero-storage policy**: your text is processed instantly and deleted automatically when you close the page. "
            "📋 *Please review the \"Terms and Conditions\" and \"Privacy Policy\" in the sidebar for more details.*"
        ),
        "gdpr_text": "🔒 **Security & Disclaimer:** Document contents are not stored or used to train public models. This automated analysis is informative and does not replace the advice of a lawyer.",
        "gdpr_checkbox": "I have read, understood, and agree to the Terms, Conditions, and data processing in accordance with GDPR.",
        "card1_title": "💡 Guidance Guide",
        "card1_desc": "Translates tangled legal clauses into simple ideas, so you understand exactly what is asked of you.",
        "card2_title": "🚩 Hidden Clauses Alert",
        "card2_desc": "Flags disproportionate penalties or payment terms that could put you at a disadvantage.",
        "card3_title": "🗣️ Negotiation Ideas",
        "card3_desc": "Gives you polite yet firm arguments and scripts to propose contract changes as an equal partner.",
        "prompt_instruction": (
            "You are a legal expert specialized in protecting freelancers. "
            "Analyze the provided contract text and identify major risks (disproportionate penalties, "
            "unfair intellectual property clauses, unrealistic payment terms, hidden exclusivity clauses, unfavorable unilateral termination). "
            "Respond STRICTLY in ENGLISH. "
            "Return the result in Markdown format, with the following structure for each problem found:\n"
            "### 🚩 [Risk Name]\n"
            "- **Original Clause:** [Text from the contract]\n"
            "- **Plain English Translation:** [What it actually means in simple terms]\n"
