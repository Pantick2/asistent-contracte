import os
import streamlit as st

streamlit_path = os.path.dirname(st.__file__)
index_path = os.path.join(streamlit_path, "static", "index.html")
meta_tag = (
    '<meta name="google-adsense-account" content="ca-pub-3528838516008000">'
)

if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()
    if meta_tag not in html:
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html.replace("<head>", f"<head>{meta_tag}"))
        print("✅ AdSense injectat cu succes!")
