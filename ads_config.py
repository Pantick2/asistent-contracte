# =====================================================================
# ⚙️ FIȘIER CENTRALIZAT PENTRU MONETIZARE (DOAR BANNERE)
# =====================================================================

COD_CLIENT_ADSENSE = "ca-pub-3528838516008000"
ID_BANNER_SIDEBAR = "9294641909"
ID_BANNER_FINAL = "2371850766"  

def genereaza_html_banner(slot_id, latime="auto", inaltime="auto"):
    return f"""
    <div style="text-align: center; margin: 10px 0;">
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
