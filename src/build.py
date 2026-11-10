"""Build the slide deck (with the dashboard embedded) into ../public/index.html.
Usage: python3 src/build.py   (standard library only)"""
import json
from pathlib import Path

SRC = Path(__file__).parent
OUT = SRC.parent / "public"
OUT.mkdir(exist_ok=True)

data = (SRC / "data.json").read_text()
dash_tpl = (SRC / "dashboard_template.html").read_text()
slides_tpl = (SRC / "slides_template.html").read_text()
city = (SRC / "city.svg").read_text()

# dashboard (embedded inside the slides; wider frame so it fills the slide)
dashboard = dash_tpl.replace("__DATA__", data)
embedded = dashboard.replace(".frame{max-width:1280px;margin:24px auto;", ".frame{max-width:1780px;margin:10px auto;")
assert "max-width:1780px" in embedded, "dashboard frame rule changed; update build.py"
slides = slides_tpl.replace("__CITY__", city).replace("__DASH__", json.dumps(embedded).replace("</", "<\\/"))
(OUT / "index.html").write_text(slides)
print("built:", *(f"{p.name} ({p.stat().st_size//1024} KB)" for p in sorted(OUT.glob("*.html"))))
