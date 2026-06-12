# =====================================================================
# ⚙️ FIȘIER CENTRALIZAT PENTRU MONETIZARE (COMPATIBIL PYTHON 3.14)
# =====================================================================

COD_CLIENT_ADSENSE = "ca-pub-3528838516008000"
LINK_SCRIPT_COOKIE = "https://cookie-script.com"

# ⚠️ Înlocuiește cu cele 10 cifre reale din panoul tău Google AdSense:
ID_BANNER_SIDEBAR = "9294641909"  
ID_BANNER_FINAL = "2371850766"  

def genereaza_html_banner(slot_id, latime="auto", inaltime="auto"):
    # Închidem scripturile într-o structură protejată care forțează browserul să le execute
    return f"""
    <div style="text-align: center; margin: 10px 0;">
        <script type="text/javascript" charset="UTF-8" src="{LINK_SCRIPT_COOKIE}"></script>
        <script async src="https://googlesyndication.com{COD_CLIENT_ADSENSE}" crossorigin="anonymous"></script>
        
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
