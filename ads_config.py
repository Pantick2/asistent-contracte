# =====================================================================
# ⚙️ FIȘIER CENTRALIZAT PENTRU MONETIZARE (GOOGLE ADSENSE / ADMOB)
# =====================================================================

# Codul tău de client Google Publisher (Schimbă-l când primești codul real)
COD_CLIENT_ADSENSE = "ca-pub-XXXXXXXXXXXXXXXX"

# ID-urile unice pentru fiecare spațiu publicitar de pe site
ID_BANNER_SIDEBAR = "XXXXXXXXXX"  # Bannerul din meniul din stânga
ID_BANNER_FINAL = "YYYYYYYYYY"    # Bannerul de jos, de sub raport

# Funcție care generează automat codul securizat cerut de Google
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
