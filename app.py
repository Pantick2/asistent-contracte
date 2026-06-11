import streamlit as st
from google import genai
from google.genai import types
import docx
import pypdf

# 1. CONFIGURARE APLICAȚIE (Trebuie să fie prima linie absolută)
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

# 2. GESTIONARE STĂRI GLOBALE (IN-MEMORY)
if "limba" not in st.session_state:
    st.session_state["limba"] = "RO"
if "termeni_acceptati" not in st.session_state:
    st.session_state.termeni_acceptati = False
if "numar_utilizari" not in st.session_state:
    st.session_state["numar_utilizari"] = 0

# =====================================================================
# ☕ ANTETUL GLOBAL FIX (Buton permanent de donație + Schimbare limbă)
# =====================================================================
col_stanga_btn, col_spatiu, col_dreapta_btn = st.columns([2.5, 6.0, 1.5])

with col_stanga_btn:
    if st.button("🌐 Schimbă Limba / Switch Language"):
        st.session_state["limba"] = "EN" if st.session_state["limba"] == "RO" else "RO"
        st.rerun()

with col_dreapta_btn:
    text_global_donatie = "Donate" if st.session_state["limba"] == "EN" else "Donatie"
    st.link_button(text_global_donatie, "https://linktr.ee", type="primary")
# 3. DICȚIONAR DE TRADUCERI PENTRU INTERFAȚĂ ȘI TEXTE LEGALE
t = {
    "RO": {
        "titlu": "📄 Asistent de Negociere pentru Freelanceri",
        "subtitlu": "Protejează-ți business-ul. Identifică clauzele abuzive ascunse și renegociază de la egal la egal.",
        "avertisment_b2b": "⚠️ **Utilizare B2B Exclusivă:** Această platformă este un instrument experimental destinat exclusiv profesioniștilor (freelanceri/firme).",
        "bifa_text": "Am citit, înțeleg și sunt de acord în mod expres cu Termenii, Condițiile (inclusiv Guvernanța Legii Engleze, Jurisdicția Exclusivă a Instanțelor din Milton Keynes, UK și Clauza Penală de Non-Defăimare) și Politica de Confidențialitate (GDPR).",
        "blocat_text": "🔒 Pentru a accesa funcțiile de upload și analiza AI, trebuie mai întâi să bifați căsuța de acceptare a Termenilor de mai sus.",
        "ghid": "💡 **Cum folosim acest instrument:** Acest site funcționează ca un copilot de negociere. Informațiile generate sunt strict orientative. Acest instrument NU oferă asistență juridică sau consultanță de avocat. Aplicația aplică o politică de zero stocare.",
        "c1": "<b>💡 Ghid de Îndrumare</b><br>Traduce clauzele contractuale încâlcite în idei simple.",
        "c2": "<b>🚩 Alertă Clauze Ascunse</b><br>Semnalează penalitățile disproporționate sau termenele de plată.",
        "c3": "<b>🗣️ Idei de Renegociere</b><br>Îți oferă argumente și formulări politicoase.",
        "side_t": "Cheie Gemini API personală:",
        "side_s": "Cheie personală activă.",
        "side_d": "Modul DEMO activ",
        "up_t": "Trage sau încarcă contractul (PDF, DOCX, TXT):",
        "tx_t": "Sau introdu textul clauzelor suspecte manual:",
        "disc": "🔒 Securitate & Disclaimer: Conținutul documentelor nu este stocat sau folosit pentru antrenarea modelelor publice. Această analiză automată are rol informativ și nu înlocuiește sfatul unui avocat public din UK sau țara de origine.",
        "b_start": "Pornește Analiza Inteligentă",
        "e_limita": "⚠️ Limita demo a fost atinsă!",
        "e_text": "Te rugăm să introduci text sau să încarci un document.",
        "e_config": "Sistemul Demo nu este configurat!",
        "spinner": "AI-ul scanează textul pentru riscuri legale...",
        "s_analiza": "Analiză finalizată cu succes!",
        "r_titlu": "## 🔍 Raport de Audit Contractual",
        "b_down": "Descarcă Raportul (.txt)",
        "prompt": "Ești un expert juridic specializat în protecția freelancerilor. Analizează textul contractului oferit și identifică riscurile majore. Răspunde STRICT în limba ROMÂNĂ. Returnează rezultatul în format Markdown, cu structura exactă: Nume Risc, Clauză originală, Traducere, De ce e periculoasă, Sugestie renegociere.",
        "subsol": "🛡️ Asistent Contracte Freelanceri | Deținut de IULIAN ICHIM-UNGUREANU (Pantick)"
    },
    "EN": {
        "titlu": "📄 Negotiation Assistant for Freelancers",
        "subtitlu": "Protect your business. Identify hidden unfair clauses and renegotiate on equal terms.",
        "avertisment_b2b": "⚠️ **B2B Exclusive Use:** This platform is an experimental tool intended exclusively for professionals (freelancers/businesses).",
        "bifa_text": "I have read, understand, and expressly agree to the Terms, Conditions (including English Law Governance, Exclusive Jurisdiction of the Courts in Milton Keynes, UK, and the Non-Disparagement Liquidated Damages Clause) and the Privacy Policy (GDPR).",
        "blocat_text": "🔒 To access upload functions and AI analysis, you must first check the box to accept the Terms above.",
        "ghid": "💡 **How to use this tool:** This site acts as a negotiation copilot. Generated information is strictly indicative. This tool DOES NOT provide legal assistance or solicitor advice. The app enforces a zero data storage policy.",
        "c1": "<b>💡 Guidance Guide</b><br>Translates tangled contract clauses into simple ideas.",
        "c2": "<b>🚩 Hidden Clauses Alert</b><br>Flags disproportionate penalties or payment terms.",
        "c3": "<b>🗣️ Renegotiation Ideas</b><br>Provides you with polite arguments and wordings.",
        "side_t": "Personal Gemini API Key:",
        "side_s": "Personal key active.",
        "side_d": "DEMO mode active",
        "up_t": "Drag or upload contract (PDF, DOCX, TXT):",
        "tx_t": "Or enter the text of suspicious clauses manually:",
        "disc": "🔒 Security & Disclaimer: Document content is not stored or used to train public models. This automated analysis is for informational purposes and does not replace the advice of a qualified lawyer in the UK or country of origin.",
        "b_start": "Start Intelligent Analysis",
        "e_limita": "⚠️ Demo limit reached!",
        "e_text": "Please enter text or upload a document.",
        "e_config": "Demo System is not configured!",
        "spinner": "AI is scanning text for legal risks...",
        "s_analiza": "Analysis completed successfully!",
        "r_titlu": "## 🔍 Contractual Audit Report",
        "b_down": "Download Report (.txt)",
        "prompt": "You are a legal expert specializing in freelancer protection. Analyze the provided contract text and identify major risks. Respond STRICTLY in ENGLISH. Return the result in Markdown format with the exact structure: Risk Name, Original Clause, Translation, Why it is dangerous, Renegotiation suggestion.",
        "subsol": "🛡️ Freelancer Contract Assistant | Owned by IULIAN ICHIM-UNGUREANU (Pantick)"
    }
}

L = t[st.session_state["limba"]]
st.markdown("<style>.feature-card { background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0284c7; margin-bottom: 15px; }</style>", unsafe_allow_html=True)

# CREARE FILTRE DE NAVIGARE STRUCTURATĂ PRIN TAB-URI INTERNE
opțiuni_tab = ["🔍 Aplicație Analiză / Analysis", "⚖️ Termeni și Condiții / Terms", "🔒 Confidențialitate / Privacy"]
tab_analiza, tab_termeni, tab_politica = st.tabs(opțiuni_tab)
# =====================================================================
# 📂 TAB 1: INTERFAȚA DE ANALIZĂ JURIDICĂ
# =====================================================================
with tab_analiza:
    st.title(L["titlu"])
    st.markdown(f"<p style='font-size:18px; color:#475569;'>{L['subtitlu']}</p>", unsafe_allow_html=True)
    st.info(L["avertisment_b2b"])

    accepta_termeni = st.checkbox(L["bifa_text"], value=st.session_state.termeni_acceptati, key="chk_analiza")
    st.session_state.termeni_acceptati = accepta_termeni

    if not st.session_state.termeni_acceptati:
        st.warning(L["blocat_text"])
    else:
        if "rezultat_analiza" not in st.session_state:
            st.info(L["ghid"])
            col1, col2, col3 = st.columns(3)
            with col1: st.markdown(f"<div class='feature-card'>{L['c1']}</div>", unsafe_allow_html=True)
            with col2: st.markdown(f"<div class='feature-card'>{L['c2']}</div>", unsafe_allow_html=True)
            with col3: st.markdown(f"<div class='feature-card'>{L['c3']}</div>", unsafe_allow_html=True)

        api_cheie_utilizator = st.sidebar.text_input(L["side_t"], type="password", key="pwd_api")
        foloseste_mod_demo = True
        cheie_finala = None

        if api_cheie_utilizator.strip():
            cheie_finala = api_cheie_utilizator
            foloseste_mod_demo = False
            st.sidebar.success(L["side_s"])
        else:
            cheie_finala = "gen-lang-client-0040445167"
            st.sidebar.info(f"{L['side_d']} ({st.session_state['numar_utilizari']}/2).")

        client = genai.Client(api_key=cheie_finala) if cheie_finala else None
        uploaded_file = st.file_uploader(L["up_t"], type=["pdf", "docx", "txt"], key="f_up")
        text_manual = st.text_area(L["tx_t"], height=150, key="txt_man")

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
        st.caption(L["disc"])

        if st.button(L["b_start"], type="primary", key="btn_run"):
            if foloseste_mod_demo and st.session_state["numar_utilizari"] >= 2:
                st.error(L["e_limita"])
            elif not contract_final_text.strip():
                st.error(L["e_text"])
            elif client is None:
                st.error(L["e_config"])
            else:
                with st.spinner(L["spinner"]):
                    try:
                        response = client.models.generate_content(
                            model='gemini-2.5-flash', 
                            contents=f"Contract:\n\n{contract_final_text}", 
                            config=types.GenerateContentConfig(system_instruction=L["prompt"], temperature=0.2)
                        )
                        st.session_state["numar_utilizari"] += 1
                        st.session_state["rezultat_analiza"] = response.text
                        st.success(L["s_analiza"])
                        st.rerun()
                    except Exception as e: 
                        st.error(f"Eroare: {str(e)}")

        if "rezultat_analiza" in st.session_state:
            st.markdown(L["r_titlu"])
            st.markdown(st.session_state["rezultat_analiza"])
            st.download_button(label=L["b_down"], data=st.session_state["rezultat_analiza"], file_name="analiza.txt", mime="text/plain", key="btn_down")
# =====================================================================
# ⚖️ TAB 2: TEXTUL INTEGRAL DE TERMENI ȘI CONDIȚII
# =====================================================================
with tab_termeni:
    if st.session_state["limba"] == "RO":
        st.title("⚖️ Termeni și Condiții de Utilizare")
        st.caption("Ultima actualizare: Iunie 2026 | Locație legală: Milton Keynes, UK")
        st.markdown("### 1. ACCEPTAREA TERMENILOR ȘI NATURA DIGITALĂ A ACORDULUI\nPrin accesarea acestui website, sunteți de acord să respectați prezenții Termeni și legislația din Anglia și Țara Galilor. Acordul se consideră semnat digital în momentul în care bifați activ căsuța de confirmare.")
        st.markdown("### 2. NATURA SERVICIULUI ȘI MODELUL DE UTILIZARE (API KEY)\nAcest website este o interfață experimentală administrată în totalitate de IULIAN ICHIM-UNGUREANU (Alias Pantick), operând din Milton Keynes, UK. Instrumentul oferă 2 analize gratuite, după care solicită introducerea propriei chei API personală (Google Gemini API Key). Conținutul generat NU constituie consultanță juridică autorizată, fiind un instrument strict educativ B2B.")
        st.markdown("### 3. FINANȚARE, MONETIZARE ȘI DONAȚII (LINKTREE)\nVeniturile realizate din reclame (ex. Google AdMob) sunt destinate exclusiv acoperirii costurilor de mentenanță. Opțiunea de donație prin Linktree este complet voluntară și nu deblochează funcționalități sau upgrade-uri suplimentare.")
        st.markdown("### 4. GARANȚIA STRICTĂ DE NON-STOCARE\nDocumentele introduse manual sau încărcate sunt procesate exclusiv în memoria temporară a browserului (sesiune) și sunt șterse definitiv și irevocabil instantaneu la închiderea tab-ului.")
        st.markdown("### 5. LIMITAREA TOTALĂ A RĂSPUNDERII (DAMAGE CAP)\nÎn măsura maximă permisă de English Law, răspunderea totală cumulată a administratorului pentru orice pretenție este limitată strict la £0 GBP. Dacă o instanță anulează acest plafon din cauza prezenței reclamelor, răspunderea maximă absolută este limitată la o sumă fixă de £10 GBP.")
        st.markdown("### 6. INDEMNIZARE ȘI CLAUZĂ PENALĂ PENTRU HĂRȚUIRE ONLINE\n6.1. În caz de procese nefondate respinse de magistrați, utilizatorul se obligă să achite integral toate cheltuielile de judecată efectuate de administrator (onorarii avocați solicitors din UK).\n6.2. Se interzic campaniile de denigrare sau defăimare împotriva Platformei (pe rețele sociale sau Linktree). În caz de încălcare, utilizatorul se obligă irevocabil să achite daune-interese în cuantum fix de £1.000 GBP pentru fiecare postare hărțuitoare distinctă.")
        st.markdown("### 7. RENUNȚAREA LA PROCESE COLECTIVE\nOrice procedură se va desfășura strict pe bază individuală. Utilizatorul renunță la dreptul de a participa într-un proces colectiv (Class Action) la nivel mondial.")
        st.markdown("### 8. LEGEA APLICABILĂ ȘI JURISDICTIA EXCLUSIVĂ\nPrezenții Termeni sunt guvernați de legile din Anglia și Țara Galilor (English Law). Orice dispută va fi trimisă spre soluționare exclusivă instanțelor de judecată competente din Milton Keynes, Regatul Unit (United Kingdom).")
    else:
        st.title("⚖️ Terms and Conditions of Use")
        st.caption("Last Updated: June 2026 | Legal Venue: Milton Keynes, UK")
        st.markdown("### 1. ACCEPTANCE OF TERMS AND DIGITAL NATURE\nBy accessing this website, you agree to comply with these Terms and the laws of England and Wales. This agreement is deemed digitally executed when you check the confirmation box.")
        st.markdown("### 2. NATURE OF SERVICE AND OPERATING MODEL (API KEY)\nThis website is an experimental interface owned by IULIAN ICHIM-UNGUREANU (Alias Pantick), operating from Milton Keynes, UK. The tool offers 2 free analyses, after which it requires your personal Google Gemini API Key. Generated content DOES NOT constitute authorized legal advice; it is a B2B educational tool.")
        st.markdown("### 3. FINANCING, MONETIZATION, AND DONATIONS\nAny ad revenue (Google AdMob) is used strictly for technical maintenance. Donations via Linktree are voluntary and do not unlock premium features or upgrades.")
        st.markdown("### 4. STRICT DATA NON-STORAGE GUARANTEE\nUploaded documents and API keys are processed exclusively in volatile browser memory (session) and are instantly and permanently deleted upon closing the browser tab.")
        st.markdown("### 5. TOTAL LIMITATION OF LIABILITY (DAMAGE CAP)\nTo the maximum extent permitted by English Law, the administrator's liability is strictly capped at £0 GBP. If a court invalidates this due to ads, the absolute maximum liability is limited to a fixed sum of £10 GBP.")
        st.markdown("### 6. INDEMNIFICATION AND LIQUIDATED DAMAGES FOR HARASSMENT\n6.1. In case of frivolous lawsuits, the user agrees to fully reimburse all UK solicitors' fees and legal costs incurred by the administrator.\n6.2. Public campaigns of harassment or defamation on social media or Linktree are strictly prohibited. In case of breach, the user agrees to pay fixed liquidated damages of £1,000 GBP per distinct defamatory post.")
        st.markdown("### 7. CLASS ACTION WAIVER\nProceedings will be conducted solely on an individual basis. The user waives the right to participate in any class action worldwide.")
        st.markdown("### 8. GOVERNING LAW AND EXCLUSIVE JURISDICTION\nThese Terms are governed by and construed in accordance with the laws of England and Wales (English Law). Any dispute shall be submitted to the exclusive jurisdiction of the courts in Milton Keynes, United Kingdom.")

# =====================================================================
# 🔒 TAB 3: POLITICA DE CONFIDENȚIALITATE (UK-GDPR)
# =====================================================================
with tab_politica:
    if st.session_state["limba"] == "RO":
        st.title("🔒 Politica de Confidențialitate")
        st.caption("Ultima actualizare: Iunie 2026 | Conformitate cu UK-GDPR")
        st.markdown("### 1. ZERO STOCARE DATE CONTRACTUALE\nNu deținem baze de date pentru stocarea documentelor sau a textelor analizate. Cheia API personală rulează exclusiv în sesiunea volatilă a browserului și dispare irevocabil la închidere.")
        st.markdown("### 2. DATE COLECTATE DE PĂRȚI TERȚE (GOOGLE ADMOB)\nPlatforma afișează reclame pentru auto-susținere. Serviciul Google AdMob poate colecta module cookie sau identificatori publicitari pentru a afișa reclame relevante. Puteți gestiona sau bloca acești identificatori din setările browserului.")
        st.markdown("### 3. DONAȚII ȘI REȚELE EXTERNE\nPlatforma folosește servicii externe precum Linktree pentru donații voluntare. Interacțiunea cu aceste link-uri se supune politicilor de confidențialitate ale platformelor respective (Linktree, PayPal, Stripe).")
        st.markdown("### 4. JURISDICȚIE\nOrice solicitare sau litigiu legat de datele tehnice procesate va fi guvernat de legea din Anglia și Țara Galilor, sub autoritatea exclusivă a instanțelor din Milton Keynes, Regatul Unit.")
    else:
        st.title("🔒 Privacy Policy")
        st.caption("Last Updated: June 2026 | UK-GDPR Compliance")
        st.markdown("### 1. ZERO CONTRACTUAL DATA STORAGE\nWe do not operate databases to store uploaded commercial documents. Personal API keys run exclusively within volatile session memory and are destroyed upon closing the browser tab.")
        st.markdown("### 2. THIRD-PARTY DATA (GOOGLE ADMOB)\nThis site displays ads for maintenance. Google AdMob may collect cookies or advertising identifiers to serve relevant ads. You can manage or disable these identifiers directly via your browser settings.")
        st.markdown("### 3. DONATIONS AND EXTERNAL NETWORKS\nWe use Linktree for voluntary donations. Interactions with these links are subject to the privacy policies of the respective external platforms (Linktree, PayPal, Stripe).")
        st.markdown("### 4. JURISDICTION\nAny data-related dispute is governed exclusively by the laws of England and Wales, under the authority of the courts in Milton Keynes, United Kingdom.")

st.markdown(f"<br><hr><center style='color:#94a3b8; font-size:12px;'>{L['subsol']}</center>", unsafe_allow_html=True)
