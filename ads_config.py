# =====================================================================
# ⚙️ FIȘIER CENTRALIZAT PENTRU MONETIZARE (COOKIES + ADSENSE)
# =====================================================================

COD_CLIENT_ADSENSE = "ca-pub-3528838516008000"
LINK_SCRIPT_COOKIE = "https://cookie-script.com"

# ID-urile unice ale unităților tale publicitare Display Ads
ID_BANNER_SIDEBAR = "AICI_PUI_ID_SLOT_PENTRU_SIDEBAR"  # Pune cele 10 cifre din AdSense
ID_BANNER_FINAL = "AICI_PUI_ID_SLOT_PENTRU_BANNER_JOS"  # Pune cele 10 cifre de la celălalt banner

def genereaza_html_banner(slot_id, latime="auto", inaltime="auto"):
    # Acest container încarcă simultan și popup-ul de cookie-uri și codul AdSense de fiecare dată când este apelat
    return f"""
    <div style="text-align: center; margin: 10px 0;">
        <!-- Scriptul de Cookie-uri certificat Google -->
        <script type="text/javascript" charset="UTF-8" src="{LINK_SCRIPT_COOKIE}"></script>
        
        <!-- Scriptul general de reclame Google -->
        <script async src="https://googlesyndication.com{COD_CLIENT_ADSENSE}" crossorigin="anonymous"></script>
        
        <!-- Unitatea publicitară efectivă -->
        <ins class="adsbygoogle"
             style="display:block; width:{latime}; height:{inaltime};"
             data-ad-client="{COD_CLIENT_ADSENSE}"
             data-ad-slot="{slot_id}"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>
             (adsbygoogle = window.adsbygoogle || []).push({{}});
        </script>
    </div>
    """
