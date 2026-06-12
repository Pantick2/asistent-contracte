# =====================================================================
# ⚙️ FIȘIER CENTRALIZAT PENTRU MONETIZARE UNIFICATĂ (PC + MOBIL)
# =====================================================================

COD_CLIENT_ADSENSE = "ca-pub-3528838516008000"
LINK_SCRIPT_COOKIE = "https://cookie-script.com"

# ID-urile unităților tale publicitare Display Ads (Responsive)
ID_BANNER_SIDEBAR = "9294641909"  
ID_BANNER_FINAL = "2371850766"  

def genereaza_html_banner(slot_id, latime="auto", inaltime="auto"):
    # Forțăm injectarea scriptului cu prioritate maximă pentru ecranele mobile
    return f"""
    <div style="text-align: center; margin: 10px 0;">
        <!-- Înrcărcăm scriptul de cookie-uri cu atribute de forțare mobilă -->
        <script type="text/javascript" charset="UTF-8" src="{LINK_SCRIPT_COOKIE}" data-cs-viewport="true"></script>
        
        <!-- Scriptul general de reclame Google AdSense (Valabil PC + Telefon) -->
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
