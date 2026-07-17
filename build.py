#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glassy v3 — four reverse-engineered magazine concepts for a premium, multi-market
(US/JP/CN) Korean beauty & dermatology TREND magazine. Each concept clones the design
language AND the business model of a different, genuinely successful business:

  V1 · "The Edit"      ← Soko Glam / The Klog   — commerce-led editorial (curated shop)
  V2 · "The Radar"     ← Hypebae / Hypebeast     — trend media + brand studio + commerce
  V3 · "The Dispatch"  ← Air Mail                — premium membership + luxury advertising
  V4 · "The Panel"     ← Allure (Condé Nast)     — testing authority + awards & seal licensing

Shared content lives in ./content/*.md ; a gallery at root lets you compare and pick.
Run: pip install markdown ; python build.py
"""
import html, pathlib, re
import markdown

ROOT = pathlib.Path(__file__).parent
CONTENT = ROOT / "content"
MD_EXT = ["tables", "sane_lists", "attr_list"]
def md(t): return markdown.markdown(t, extensions=MD_EXT, output_format="html5")
def esc(s): return html.escape(str(s))

# ------------------------------------------------------------------ content
def read_article(p):
    raw = p.read_text(encoding="utf-8")
    fm = {}
    body = raw
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        body = m.group(2).strip()
    fm["slug"] = p.stem
    fm["body_html"] = md(body)
    fm["body_md"] = body
    return fm

ORDER = ["glass-skin-stack", "exosome-vs-rejuran", "hifu-seoul", "seoul-dispatch"]
ARTS = {a["slug"]: a for a in (read_article(CONTENT / f"{s}.md") for s in ORDER)}
ARTICLES = [ARTS[s] for s in ORDER]
FEATURED = ARTS["glass-skin-stack"]
REST = [a for a in ARTICLES if a["slug"] != FEATURED["slug"]]

# illustrative "Shop the Edit" picks (category-level, indicative — prototype fake-door)
SHOP = [
    ("PDRN Overnight Booster", "Barrier & bounce", "$—"),
    ("Ceramide Barrier Cream", "The base layer", "$—"),
    ("Mineral SPF Fluid", "Non-negotiable", "$—"),
    ("Snail Mucin Essence", "The glow step", "$—"),
]
DISC = "Educational information, not medical advice. No specific clinic promotion. Prices indicative as of Jul 2026."

# functional email capture (validation + success), theme-neutral markup
def capture(list_name, cta, ph="you@email.com"):
    return (f'<form class="cap" data-list="{esc(list_name)}"><input type="email" required placeholder="{esc(ph)}" aria-label="Email">'
            f'<button type="submit">{esc(cta)}</button>'
            f'<div class="cap-ok" role="status" hidden>You’re in — watch your inbox.</div></form>')
SCRIPT = """<script>document.querySelectorAll('form.cap').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var i=f.querySelector('input');if(!i.checkValidity()){i.reportValidity();return;}try{var k='glassy:'+(f.dataset.list||'x'),a=JSON.parse(localStorage.getItem(k)||'[]');a.push({e:i.value.trim(),t:Date.now()});localStorage.setItem(k,JSON.stringify(a));}catch(_){}f.querySelectorAll('input,button').forEach(function(el){el.style.display='none';});var ok=f.querySelector('.cap-ok');if(ok)ok.hidden=false;});});</script>"""

MARKETS = ['EN', '日本', '中文']

def shell(title, desc, fonts, css, body, rel="."):
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<style>{css}</style></head><body>{body}
<div class="cbar">Concept prototype · reverse-engineered design & business model · <a href="{rel}/index.html">← compare all four</a></div>
{SCRIPT}</body></html>"""

# ==================================================================
# V1 — "The Edit"  (Soko Glam / The Klog : commerce-led editorial)
# ==================================================================
FONTS1 = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">'
CSS1 = """
:root{--ink:#3b4256;--soft:#6b7189;--navy:#363c73;--pink:#e8388a;--bg:#fff;--wash:#f6f4fb;--line:#ece9f3;--r:16px}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Nunito Sans",sans-serif;font-size:16px;line-height:1.6}
a{color:inherit;text-decoration:none}.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
h1,h2,h3,h4,.brand,.btn,.eyebrow{font-family:"Poppins",sans-serif}
.promo{background:var(--navy);color:#fff;text-align:center;font-weight:700;font-size:13px;letter-spacing:.03em;padding:9px}
.top{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:18px;height:70px}
.brand{font-weight:800;font-size:26px;letter-spacing:-.02em;color:var(--navy)}.brand b{color:var(--pink)}
.mkt{margin-left:auto;display:flex;gap:8px}.mkt a{font-weight:700;font-size:12px;color:var(--soft);padding:4px 8px;border-radius:8px}.mkt a.on{background:var(--pink);color:#fff}
.nav{display:flex;gap:20px;flex-wrap:wrap;padding:12px 0;border-bottom:1px solid var(--line);font-family:"Poppins";font-weight:600;font-size:14px;color:var(--soft)}
.nav a:hover{color:var(--pink)}
.btn{display:inline-block;font-weight:700;font-size:14px;background:var(--pink);color:#fff;padding:12px 20px;border-radius:999px}
.btn.ghost{background:transparent;color:var(--navy);border:2px solid var(--line)}
.hero{display:grid;grid-template-columns:1.55fr 1fr;gap:22px;margin:26px 0}
.hero .big{border-radius:var(--r);overflow:hidden;position:relative;min-height:430px;display:flex;align-items:flex-end;padding:30px;color:#fff;background:linear-gradient(150deg,#c9b8ff,#ffb0d6 55%,#ffd9a8)}
.hero .big::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(40,20,50,.55),transparent 60%)}
.hero .big>div{position:relative;z-index:1;max-width:30ch}
.tag{display:inline-block;background:#fff;color:var(--pink);font-family:"Poppins";font-weight:700;font-size:12px;padding:6px 12px;border-radius:999px;margin-bottom:12px}
.hero .big h1{font-size:38px;line-height:1.08;margin:0 0 10px;font-weight:800}
.hero .big p{margin:0 0 16px;font-size:15px;opacity:.95}
.hero .side{display:flex;flex-direction:column;gap:16px}
.scard{background:var(--wash);border-radius:var(--r);padding:18px;flex:1;display:flex;flex-direction:column;justify-content:center}
.scard .k{font-family:"Poppins";font-weight:700;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--pink)}
.scard h3{font-size:20px;margin:6px 0 6px;line-height:1.18;color:var(--navy)}
.scard p{margin:0;font-size:13.5px;color:var(--soft)}
.sec{padding:36px 0;border-top:1px solid var(--line)}
.sec-h{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px}
.sec-h h2{font-size:24px;color:var(--navy);margin:0}.sec-h a{font-weight:700;color:var(--pink);font-size:14px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:.15s}
.card:hover{box-shadow:0 12px 30px rgba(54,60,115,.10);transform:translateY(-3px)}
.card .im{height:150px;background:linear-gradient(135deg,#ffe0ee,#e9ddff 60%,#dff5f0)}
.card .bd{padding:16px}.card .cat{font-family:"Poppins";font-weight:700;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--pink)}
.card h3{font-size:17px;line-height:1.25;margin:7px 0 6px;color:var(--navy)}.card p{margin:0;font-size:13.5px;color:var(--soft)}
.shelf{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.prod{background:var(--wash);border-radius:14px;padding:16px;text-align:center}
.prod .im{height:120px;border-radius:10px;background:linear-gradient(135deg,#fff,#ffe9f3);margin-bottom:12px;border:1px solid var(--line)}
.prod .nm{font-family:"Poppins";font-weight:700;font-size:14px;color:var(--navy)}.prod .no{font-size:12.5px;color:var(--soft);margin:3px 0 10px}
.prod .sh{display:block;background:var(--navy);color:#fff;font-family:"Poppins";font-weight:700;font-size:13px;padding:9px;border-radius:999px}
.news{background:linear-gradient(135deg,#fff0f7,#f3ecff);border-radius:20px;padding:34px;text-align:center;margin:30px 0}
.news h2{font-size:26px;color:var(--navy);margin:0 0 8px}.news p{color:var(--soft);margin:0 auto 18px;max-width:52ch}
.cap{display:flex;gap:10px;max-width:440px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.cap input{flex:1;min-width:200px;padding:13px 16px;border-radius:999px;border:1px solid var(--line);font:inherit}
.cap button{font-family:"Poppins";font-weight:700;background:var(--pink);color:#fff;border:0;padding:13px 22px;border-radius:999px;cursor:pointer}
.cap-ok{flex-basis:100%;font-family:"Poppins";font-weight:700;color:var(--pink);margin-top:8px}
.foot{background:var(--navy);color:#dfe0f0;margin-top:20px}.foot .wrap{padding:34px 22px;font-size:13px;line-height:1.7}
.foot .brand{color:#fff;font-size:22px;display:block;margin-bottom:10px}
.cbar{background:#151422;color:#8a8ca8;font-size:12px;text-align:center;padding:9px}.cbar a{color:var(--pink);font-weight:700}
/* article */
.art{max-width:760px;margin:30px auto;padding:0 22px}
.art .cat{font-family:"Poppins";font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--pink)}
.art h1{font-size:40px;line-height:1.08;color:var(--navy);margin:10px 0 12px}
.art .dek{font-size:20px;color:var(--soft);margin:0 0 18px}
.art .meta{font-family:"Poppins";font-weight:600;font-size:13px;color:var(--soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:12px 0;margin-bottom:24px}
.prose{font-size:17px;line-height:1.75}.prose h2{font-family:"Poppins";color:var(--navy);font-size:24px;margin:32px 0 10px}
.prose h3{font-family:"Poppins";color:var(--navy);font-size:19px;margin:24px 0 8px}.prose strong{color:var(--navy)}
.prose table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14.5px}
.prose th{background:var(--wash);text-align:left}.prose th,.prose td{border:1px solid var(--line);padding:9px 12px}
.disc{max-width:760px;margin:20px auto;padding:0 22px;color:var(--soft);font-size:12.5px}
@media(max-width:820px){.hero,.grid,.shelf{grid-template-columns:1fr}.hero .side{flex-direction:row}}
"""

def v1_card(a, rel="."):
    return (f'<a class="card" href="{rel}/{a["slug"]}.html"><div class="im"></div><div class="bd">'
            f'<div class="cat">{esc(a.get("category",""))}</div><h3>{esc(a["title"])}</h3>'
            f'<p>{esc(a.get("dek","")[:110])}</p></div></a>')

def v1_home():
    side = "".join(f'<a class="scard" href="./{a["slug"]}.html"><div class="k">{esc(a.get("category",""))}</div>'
                   f'<h3>{esc(a["title"])}</h3><p>{esc(a.get("readtime",""))}</p></a>' for a in REST[:2])
    grid = "".join(v1_card(a) for a in REST)
    shelf = "".join(f'<div class="prod"><div class="im"></div><div class="nm">{esc(n)}</div><div class="no">{esc(no)}</div>'
                    f'<a class="sh" href="#shop">Shop · {esc(pr)}</a></div>' for n,no,pr in SHOP)
    mkt = "".join(f'<a class="{"on" if m=="EN" else ""}" href="#">{esc(m)}</a>' for m in MARKETS)
    body = f"""
<div class="promo">Seoul’s beauty shelf, curated for you — free shipping on the Edit over $50</div>
<header class="top"><div class="wrap"><span class="brand">Glassy<b>.</b></span>
<nav class="mkt">{mkt}</nav></div>
<div class="wrap"><nav class="nav"><a>Trend Radar</a><a>The Treatment</a><a>The Shelf</a><a>Seoul Dispatch</a><a>Shop the Edit</a><a href="#news">Newsletter</a></nav></div></header>
<main class="wrap">
<section class="hero"><a class="big" href="./{FEATURED['slug']}.html"><div><span class="tag">{esc(FEATURED.get('hero_tag',''))}</span>
<h1>{esc(FEATURED['title'])}</h1><p>{esc(FEATURED.get('dek','')[:120])}</p><span class="btn">Read the edit</span></div></a>
<div class="side">{side}</div></section>

<section class="sec"><div class="sec-h"><h2>The latest from Seoul</h2><a href="#">All stories →</a></div><div class="grid">{grid}</div></section>

<section class="sec" id="shop"><div class="sec-h"><h2>Shop the Edit</h2><a href="#">The full shelf →</a></div>
<div class="shelf">{shelf}</div>
<p class="disc" style="margin-top:14px">Curated picks are category-level and indicative — a prototype. {esc(DISC)}</p></section>

<section class="news" id="news"><h2>The Seoul shelf, in your inbox</h2>
<p>New K-beauty and derm trends, the honest picks, and where to shop them — weekly.</p>{capture('edit','Get the Edit')}</section>
</main>
<footer class="foot"><div class="wrap"><span class="brand">Glassy<b style="color:var(--pink)">.</b></span>
Concept 1 of 4 — modeled on the Soko Glam / The Klog playbook: editorial that curates the shelf, monetized by curated commerce & affiliate. {esc(DISC)}</div></footer>
"""
    return shell("Glassy · The Edit — curated K-beauty from Seoul", "Curated Korean beauty & derm trends, and where to shop them.", FONTS1, CSS1, body)

def v1_article(a):
    body = f"""
<div class="promo">Seoul’s beauty shelf, curated for you</div>
<header class="top"><div class="wrap"><a class="brand" href="./index.html">Glassy<b>.</b></a></div></header>
<article class="art"><div class="cat">{esc(a.get('category',''))}</div><h1>{esc(a['title'])}</h1>
<p class="dek">{esc(a.get('dek',''))}</p><div class="meta">Glassy Edit · {esc(a.get('readtime',''))} · {esc(a.get('date',''))}</div>
<div class="prose">{a['body_html']}</div></article>
<section class="news" id="news" style="max-width:760px;margin:30px auto"><h2>Get the weekly Edit</h2>
<p>The honest picks from Seoul, in your inbox.</p>{capture('edit','Subscribe')}</section>
<p class="disc"><a href="./index.html" style="color:var(--pink);font-weight:700">← All stories</a> &nbsp;·&nbsp; {esc(DISC)}</p>
<footer class="foot"><div class="wrap">{esc(DISC)}</div></footer>
"""
    return shell(a['title'] + " — Glassy", a.get('dek','')[:150], FONTS1, CSS1, body)

# ==================================================================
# V2 — "The Radar"  (Hypebae / Hypebeast : trend media + brand studio)
# ==================================================================
FONTS2 = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS2 = """
:root{--ink:#151515;--soft:#6a6a6a;--bg:#fff;--grid:#f2f2f2;--line:#e4e4e4;--hot:#ff4d2e;--spon:#eef3ee;--sponink:#2f7d4f}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Inter",sans-serif;font-size:15px;line-height:1.55}
a{color:inherit;text-decoration:none}.wrap{max-width:1240px;margin:0 auto;padding:0 20px}
h1,h2,h3,.brand,.hd{font-family:"Archivo",sans-serif;letter-spacing:-.01em}
.util{background:#111;color:#cfcfcf;font-size:12px}.util .wrap{display:flex;align-items:center;gap:18px;height:38px}
.util a{color:#cfcfcf;font-weight:600}.util .sp{flex:1}.util .lang{display:flex;gap:8px}.util .lang a.on{color:#fff}
.promo{background:var(--grid);text-align:center;font-weight:700;font-size:12.5px;letter-spacing:.03em;padding:8px;text-transform:uppercase}
.top{position:sticky;top:0;z-index:20;background:#fff;border-bottom:2px solid #111}
.top .wrap{display:flex;flex-direction:column;align-items:center;gap:8px;padding:14px 20px}
.brand{font-weight:900;font-size:30px;letter-spacing:.02em;text-transform:lowercase;border-bottom:3px solid #111;line-height:.9;padding-bottom:3px}
.nav{display:flex;gap:22px;flex-wrap:wrap;justify-content:center;font-family:"Archivo";font-weight:800;font-size:13px;text-transform:uppercase}
.nav a:hover{color:var(--hot)}.nav .store{background:#111;color:#fff;padding:4px 10px}
.heroimg{height:360px;margin:0;background:linear-gradient(120deg,#111,#3a2a2a 60%,#c99);display:flex;align-items:center;justify-content:center;position:relative}
.heroimg .lbl{position:absolute;left:20px;top:16px;background:var(--hot);color:#fff;font-family:"Archivo";font-weight:900;font-size:11px;text-transform:uppercase;letter-spacing:.08em;padding:5px 9px}
.heroimg h1{color:#fff;font-size:clamp(30px,5vw,56px);font-weight:900;text-transform:uppercase;text-align:center;max-width:22ch;margin:0;line-height:1}
.section{padding:26px 0;border-bottom:1px solid var(--line)}
.rowh{display:flex;align-items:center;gap:10px;margin-bottom:16px}
.rowh h2{font-size:15px;text-transform:uppercase;font-weight:900;margin:0}.rowh .ln{flex:1;height:2px;background:#111}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.card .im{height:180px;background:var(--grid);margin-bottom:10px;position:relative;overflow:hidden}
.card .im .t{position:absolute;left:8px;top:8px;background:#111;color:#fff;font-family:"Archivo";font-weight:800;font-size:10px;text-transform:uppercase;padding:3px 7px}
.card h3{font-size:16px;font-weight:800;text-transform:uppercase;line-height:1.06;margin:0 0 6px}
.card:hover h3{color:var(--hot)}.card p{margin:0 0 8px;color:var(--soft);font-size:13px}
.card .m{display:flex;gap:12px;align-items:center;font-size:12px;color:var(--soft);font-weight:600}
.card .m .fire{color:var(--hot)}
.spon{grid-column:span 2;background:var(--spon);border:1px solid #d6e4d9;padding:16px;display:flex;gap:16px}
.spon .im{width:150px;flex:0 0 150px;height:140px;background:linear-gradient(135deg,#dfeee2,#c7e6cf);border-radius:6px}
.spon .pb{font-family:"Archivo";font-weight:800;font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:var(--sponink)}
.spon h3{font-size:19px;font-weight:900;margin:6px 0 6px;text-transform:none}.spon p{font-size:13px;color:#4a5a4d;margin:0 0 10px}
.spon .sh{background:var(--sponink);color:#fff;font-family:"Archivo";font-weight:800;font-size:12px;text-transform:uppercase;padding:8px 14px;display:inline-block}
.strip{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px}
.chip{flex:0 0 auto;background:var(--grid);font-family:"Archivo";font-weight:800;font-size:12px;text-transform:uppercase;padding:8px 14px}
.news{background:#111;color:#fff;padding:34px 0;text-align:center}.news h2{font-size:26px;text-transform:uppercase;font-weight:900;margin:0 0 8px}
.news p{color:#bdbdbd;margin:0 auto 18px;max-width:52ch}
.cap{display:flex;gap:0;max-width:440px;margin:0 auto;border:2px solid #fff}
.cap input{flex:1;min-width:160px;padding:13px 16px;border:0;font:inherit;background:#111;color:#fff}.cap input::placeholder{color:#888}
.cap button{font-family:"Archivo";font-weight:900;text-transform:uppercase;background:var(--hot);color:#fff;border:0;padding:13px 22px;cursor:pointer}
.cap-ok{flex-basis:100%;color:var(--hot);font-family:"Archivo";font-weight:800;padding:12px}
.foot{background:#fff;border-top:2px solid #111}.foot .wrap{padding:30px 20px;font-size:12.5px;color:var(--soft);line-height:1.7}
.foot .brand{color:#111;font-size:22px;display:inline-block;border-bottom:3px solid #111;margin-bottom:10px}
.cbar{background:#111;color:#888;font-size:12px;text-align:center;padding:9px}.cbar a{color:var(--hot);font-weight:800}
.art{max-width:720px;margin:26px auto;padding:0 20px}
.art .k{font-family:"Archivo";font-weight:900;font-size:12px;text-transform:uppercase;color:var(--hot)}
.art h1{font-size:clamp(30px,5vw,46px);font-weight:900;text-transform:uppercase;line-height:1.02;margin:8px 0 12px}
.art .dek{font-size:19px;color:var(--soft);margin:0 0 16px}.art .meta{font-family:"Archivo";font-weight:700;font-size:12px;text-transform:uppercase;color:var(--soft);border-top:2px solid #111;border-bottom:1px solid var(--line);padding:10px 0;margin-bottom:22px}
.prose{font-size:17px;line-height:1.75}.prose h2{font-family:"Archivo";font-weight:900;text-transform:uppercase;font-size:22px;margin:30px 0 10px}
.prose h3{font-family:"Archivo";font-weight:800;font-size:18px;margin:22px 0 8px}.prose strong{color:#111}
.prose table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}.prose th{background:var(--grid);text-align:left}.prose th,.prose td{border:1px solid var(--line);padding:9px 12px}
.disc{max-width:720px;margin:18px auto;padding:0 20px;color:var(--soft);font-size:12.5px}
@media(max-width:900px){.grid{grid-template-columns:repeat(2,1fr)}.spon{grid-column:span 2}}
@media(max-width:560px){.grid{grid-template-columns:1fr}.spon{grid-column:span 1;flex-direction:column}}
"""

def v2_card(a, tag=None):
    fires = 100 + len(a['title'])*7
    return (f'<a class="card" href="./{a["slug"]}.html"><div class="im"><span class="t">{esc(a.get("category",""))}</span></div>'
            f'<h3>{esc(a["title"])}</h3><p>{esc(a.get("dek","")[:80])}</p>'
            f'<div class="m"><span class="fire">\U0001f525 {fires}</span><span>{esc(a.get("readtime",""))}</span></div></a>')

def v2_home():
    lang = "".join(f'<a class="{"on" if m=="EN" else ""}" href="#">{esc(m)}</a>' for m in MARKETS)
    cards = v2_card(REST[0]) + f"""<div class="spon"><div class="im"></div><div>
<div class="pb">Presented by — a partner brand</div><h3>Inside the lab behind Seoul’s barrier boom</h3>
<p>A brand-studio story, clearly labeled and editorially walled. This is how the Radar monetizes without selling the verdict.</p>
<a class="sh" href="#">Read the partner story</a></div></div>""" + "".join(v2_card(a) for a in REST[1:])
    chips = "".join(f'<span class="chip">{esc(c)}</span>' for c in ["#GlassSkin","#Exosomes","#Rejuran","#HIFU","#OliveYoung","#Xiaohongshu","#Gangnam","#SPF"])
    body = f"""
<div class="util"><div class="wrap"><a>Glassy</a><a>The Radar</a><a>Shop</a><span class="sp"></span><span>Newsletter</span><span class="lang">{lang}</span></div></div>
<div class="promo">Trending now in Seoul — the week’s biggest moves in K-beauty & derm</div>
<header class="top"><div class="wrap"><span class="brand">glassy</span>
<nav class="nav"><a>Trend Radar</a><a>The Treatment</a><a>The Shelf</a><a>Seoul Dispatch</a><a>Beauty</a><a class="store">Store</a></nav></div></header>
<a class="heroimg" href="./{FEATURED['slug']}.html"><span class="lbl">{esc(FEATURED.get('hero_tag',''))}</span><h1>{esc(FEATURED['title'])}</h1></a>
<main class="wrap">
<section class="section"><div class="rowh"><h2>Trend Radar</h2><div class="ln"></div></div><div class="grid">{cards}</div></section>
<section class="section"><div class="rowh"><h2>Trending tags</h2><div class="ln"></div></div><div class="strip">{chips}</div></section>
</main>
<section class="news" id="news"><h2>Don’t miss the drop</h2><p>The week’s biggest K-beauty & derm trends from Seoul, first.</p>{capture('radar','Subscribe')}</section>
<footer class="foot"><div class="wrap"><span class="brand">glassy</span><br>
Concept 2 of 4 — modeled on the Hypebae / Hypebeast playbook: fast trend media monetized by a brand studio (labeled native), commerce, and scale. {esc(DISC)}</div></footer>
"""
    return shell("Glassy · The Radar — what’s trending in Seoul", "The week’s biggest K-beauty & derm trends from Seoul.", FONTS2, CSS2, body)

def v2_article(a):
    body = f"""
<div class="promo">Trending now in Seoul</div>
<header class="top"><div class="wrap"><a class="brand" href="./index.html">glassy</a>
<nav class="nav"><a href="./index.html">Trend Radar</a><a href="./index.html">The Treatment</a><a href="./index.html">The Shelf</a><a class="store">Store</a></nav></div></header>
<article class="art"><div class="k">{esc(a.get('category',''))}</div><h1>{esc(a['title'])}</h1>
<p class="dek">{esc(a.get('dek',''))}</p><div class="meta">Glassy Radar — {esc(a.get('readtime',''))} — {esc(a.get('date',''))}</div>
<div class="prose">{a['body_html']}</div></article>
<section class="news" id="news"><h2>Get the Radar</h2><p>Seoul’s trends, first.</p>{capture('radar','Subscribe')}</section>
<p class="disc"><a href="./index.html" style="color:var(--hot);font-weight:800">← ALL STORIES</a> &nbsp;·&nbsp; {esc(DISC)}</p>
<footer class="foot"><div class="wrap">{esc(DISC)}</div></footer>
"""
    return shell(a['title'] + " — Glassy", a.get('dek','')[:150], FONTS2, CSS2, body)

# ==================================================================
# V3 — "The Dispatch"  (Air Mail : premium membership + luxury ads)
# ==================================================================
FONTS3 = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Libre+Caslon+Text:ital,wght@0,400;1,400&family=Marcellus&display=swap" rel="stylesheet">'
CSS3 = """
:root{--cream:#faf6f0;--ink:#262635;--soft:#5a5a6a;--red:#c22e28;--navy:#2b3a67;--line:#e4ddd0;--r:4px}
*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font-family:"Libre Caslon Text",Georgia,serif;font-size:17px;line-height:1.6}
a{color:inherit;text-decoration:none}.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
h1,h2,h3,.disp{font-family:"Playfair Display",Georgia,serif}
.lbl,.nav a,.util a,.brandsub{font-family:"Marcellus",serif;letter-spacing:.14em;text-transform:uppercase}
.util{border-bottom:1px solid var(--line)}.util .wrap{display:flex;align-items:center;gap:22px;height:46px;font-size:12px}
.util a{color:var(--ink)}.util a.sub{color:var(--red)}.util .sp{flex:1}
.mast{text-align:center;padding:22px 0 10px}
.badge{display:inline-block;background:var(--red);color:var(--cream);font-family:"Marcellus";letter-spacing:.12em;text-transform:uppercase;font-size:22px;padding:12px 22px;border-radius:6px;position:relative}
.nav2{display:flex;gap:26px;justify-content:center;padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);font-size:12px}
.nav2 a:hover{color:var(--red)}
.stripe{height:8px;background:repeating-linear-gradient(135deg,var(--red) 0 14px,#fff 14px 28px,var(--navy) 28px 42px,#fff 42px 56px)}
.hero{display:grid;grid-template-columns:1.1fr 1fr;gap:36px;padding:34px 0;align-items:center}
.ribbon{display:inline-block;background:var(--red);color:#fff;font-family:"Marcellus";letter-spacing:.12em;text-transform:uppercase;font-size:12px;padding:7px 26px;clip-path:polygon(8% 0,92% 0,100% 50%,92% 100%,8% 100%,0 50%);margin-bottom:16px}
.hero h1{font-size:46px;line-height:1.06;font-weight:600;margin:0 0 14px}
.hero .dek{font-size:19px;color:var(--soft);margin:0 0 16px;font-style:italic}
.hero .by{font-family:"Marcellus";letter-spacing:.1em;text-transform:uppercase;font-size:12px;color:var(--soft)}
.hero .im{height:400px;background:radial-gradient(circle at 40% 35%,#f0e6d6,#d8c8b0);border:1px solid var(--line)}
.issue{font-family:"Marcellus";letter-spacing:.14em;text-transform:uppercase;font-size:12px;color:var(--red);text-align:right;margin-top:8px}
.sec{padding:30px 0;border-top:1px solid var(--line)}
.sh{font-family:"Marcellus";letter-spacing:.14em;text-transform:uppercase;font-size:13px;color:var(--navy);margin:0 0 18px;text-align:center;position:relative}
.sh span{background:var(--cream);padding:0 16px;position:relative;z-index:1}.sh::before{content:"";position:absolute;left:0;right:0;top:50%;height:1px;background:var(--line)}
.list{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}
.it .cat{font-family:"Marcellus";letter-spacing:.1em;text-transform:uppercase;font-size:11px;color:var(--red)}
.it h3{font-size:22px;font-weight:600;line-height:1.15;margin:6px 0 8px}.it:hover h3{color:var(--red)}
.it p{margin:0;font-size:14.5px;color:var(--soft)}
.ad{border:1px solid var(--line);background:#fff;text-align:center;padding:26px;margin:26px 0}
.ad .t{font-family:"Marcellus";letter-spacing:.2em;text-transform:uppercase;font-size:10px;color:var(--soft)}
.ad .b{font-family:"Playfair Display";font-size:24px;margin:8px 0 4px}.ad .s{font-size:13px;color:var(--soft)}
.member{background:var(--navy);color:#f2ede2;border-radius:6px;padding:40px;text-align:center;margin:30px 0}
.member .rib{font-family:"Marcellus";letter-spacing:.16em;text-transform:uppercase;font-size:12px;color:#e9b949}
.member h2{font-family:"Playfair Display";font-size:32px;margin:10px 0 8px;color:#fff}
.member p{max-width:52ch;margin:0 auto 20px;color:#cdd3e0}
.member .price{font-family:"Marcellus";letter-spacing:.1em;font-size:14px;margin-bottom:16px}
.cap{display:flex;gap:10px;max-width:440px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.cap input{flex:1;min-width:200px;padding:13px 16px;border:1px solid #4a5680;background:#233156;color:#fff;font:inherit;border-radius:3px}
.cap input::placeholder{color:#9aa6c4}
.cap button{font-family:"Marcellus";letter-spacing:.1em;text-transform:uppercase;background:#e9b949;color:#23305a;border:0;padding:13px 24px;cursor:pointer;border-radius:3px;font-size:13px}
.cap-ok{flex-basis:100%;color:#e9b949;font-family:"Marcellus";letter-spacing:.06em}
.foot{border-top:8px solid;border-image:repeating-linear-gradient(135deg,var(--red) 0 14px,#fff 14px 28px,var(--navy) 28px 42px,#fff 42px 56px) 8;margin-top:20px}
.foot .wrap{padding:30px 24px;font-size:13px;color:var(--soft);line-height:1.7}.foot .b{font-family:"Playfair Display";font-size:22px;color:var(--ink);display:block;margin-bottom:8px}
.cbar{background:#23305a;color:#9aa6c4;font-size:12px;text-align:center;padding:9px}.cbar a{color:#e9b949}
.art{max-width:720px;margin:30px auto;padding:0 24px}
.art .cat{font-family:"Marcellus";letter-spacing:.14em;text-transform:uppercase;font-size:12px;color:var(--red)}
.art h1{font-size:44px;font-weight:600;line-height:1.08;margin:12px 0 14px}
.art .dek{font-size:20px;color:var(--soft);font-style:italic;margin:0 0 18px}
.art .meta{font-family:"Marcellus";letter-spacing:.1em;text-transform:uppercase;font-size:12px;color:var(--soft);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:12px 0;margin-bottom:24px}
.prose{font-size:18px;line-height:1.8}.prose h2{font-family:"Playfair Display";font-size:27px;font-weight:600;margin:32px 0 10px}
.prose h3{font-family:"Marcellus";letter-spacing:.06em;font-size:18px;margin:24px 0 8px}.prose strong{color:var(--ink)}
.prose table{width:100%;border-collapse:collapse;margin:20px 0;font-size:15px}.prose th{background:#fff;text-align:left;font-family:"Marcellus";letter-spacing:.06em;font-size:12px;text-transform:uppercase}
.prose th,.prose td{border:1px solid var(--line);padding:10px 12px}
.disc{max-width:720px;margin:20px auto;padding:0 24px;color:var(--soft);font-size:12.5px}
@media(max-width:820px){.hero,.list{grid-template-columns:1fr}}
"""

def v3_home():
    items = "".join(f'<a class="it" href="./{a["slug"]}.html"><div class="cat">{esc(a.get("category",""))}</div>'
                    f'<h3>{esc(a["title"])}</h3><p>{esc(a.get("dek","")[:100])}</p></a>' for a in REST)
    body = f"""
<div class="util"><div class="wrap"><a class="sub">Subscribe</a><a>The Treatment</a><a>Shop</a><a>Seoul</a><span class="sp"></span><a>Sign In</a><a>EN / 日本 / 中文</a></div></div>
<div class="mast"><a class="badge" href="./index.html">Glassy</a></div>
<nav class="nav2"><a>Trend Radar</a><a>The Treatment</a><a>The Shelf</a><a>Seoul Dispatch</a><a>The Verdict</a><a>City Guides</a></nav>
<div class="stripe"></div>
<main class="wrap">
<div class="issue">The Weekly Dispatch · {esc(FEATURED.get('date','Jul 2026'))}</div>
<section class="hero"><div><span class="ribbon">{esc(FEATURED.get('hero_tag',''))}</span>
<h1><a href="./{FEATURED['slug']}.html">{esc(FEATURED['title'])}</a></h1>
<p class="dek">{esc(FEATURED.get('dek',''))}</p><div class="by">By the Glassy Seoul desk · {esc(FEATURED.get('readtime',''))}</div></div>
<a class="im" href="./{FEATURED['slug']}.html"></a></section>

<section class="sec"><div class="sh"><span>From this week’s issue</span></div><div class="list">{items}</div></section>

<div class="ad"><div class="t">Advertisement</div><div class="b">A house of quiet luxury</div><div class="s">Your brand, in refined company. — Glassy partner placement</div></div>

<section class="member"><div class="rib">Membership</div><h2>Join the Glassy Circle</h2>
<p>The full weekly Dispatch, the MD-checked Verdict archive, and the Seoul City Guides — with a members’ concierge for planning a trip.</p>
<div class="price">$8 / month · $70 / year · Circle $300</div>{capture('circle','Become a member')}</section>
</main>
<footer class="foot"><div class="wrap"><span class="b">Glassy</span>
Concept 3 of 4 — modeled on the Air Mail playbook: a premium curated weekly monetized by membership and luxury advertising, with a shop-as-editorial and a medical-tourism concierge. {esc(DISC)}</div></footer>
"""
    return shell("Glassy · The Dispatch — a premium weekly from Seoul", "A premium curated weekly on Korean beauty & dermatology, for the world.", FONTS3, CSS3, body)

def v3_article(a):
    body = f"""
<div class="util"><div class="wrap"><a class="sub" href="#member">Subscribe</a><span class="sp"></span><a>Sign In</a></div></div>
<div class="mast"><a class="badge" href="./index.html">Glassy</a></div>
<div class="stripe"></div>
<article class="art"><div class="cat">{esc(a.get('category',''))}</div><h1>{esc(a['title'])}</h1>
<p class="dek">{esc(a.get('dek',''))}</p><div class="meta">The Glassy Seoul desk · {esc(a.get('readtime',''))} · {esc(a.get('date',''))}</div>
<div class="prose">{a['body_html']}</div></article>
<section class="member" id="member" style="max-width:720px;margin:30px auto"><div class="rib">Membership</div>
<h2>Read the full Dispatch</h2><p>Members get the weekly issue, the Verdict archive, and the Seoul City Guides.</p>
<div class="price">$8 / month · $70 / year</div>{capture('circle','Become a member')}</section>
<p class="disc"><a href="./index.html" style="color:var(--red)">← The current issue</a> &nbsp;·&nbsp; {esc(DISC)}</p>
<footer class="foot"><div class="wrap">{esc(DISC)}</div></footer>
"""
    return shell(a['title'] + " — Glassy", a.get('dek','')[:150], FONTS3, CSS3, body)

# ==================================================================
# V4 — "The Panel"  (Allure / Condé Nast : testing authority + awards & seal licensing)
# ==================================================================
FONTS4 = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Work+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
CSS4 = """
:root{--ink:#111114;--soft:#55555e;--bg:#fff;--red:#e4002b;--redd:#b80022;--wash:#f7f7f8;--line:#e6e6e9;--r:12px}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:"Work Sans",sans-serif;font-size:15.5px;line-height:1.6}
a{color:inherit;text-decoration:none}.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
h1,h2,.brand,.num{font-family:"Fraunces",Georgia,serif;font-weight:600}
.promo{background:var(--red);color:#fff;text-align:center;font-weight:600;font-size:12.5px;letter-spacing:.04em;padding:9px}
.promo a{text-decoration:underline;font-weight:700}
.top{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.97);backdrop-filter:blur(8px);border-bottom:1px solid var(--ink)}
.m1{display:flex;align-items:center;gap:18px;padding:12px 0 4px}
.brand{font-size:30px;letter-spacing:-.01em;line-height:1;display:inline-block}
.tagline{font-size:9.5px;font-weight:800;letter-spacing:.24em;text-transform:uppercase;color:var(--soft);margin-top:4px}
.mkt{margin-left:auto;display:flex;gap:8px}.mkt a{font-weight:600;font-size:11.5px;color:var(--soft);padding:3px 8px;border:1px solid transparent;border-radius:3px}.mkt a.on{color:var(--red);border-color:var(--red)}
.nav{display:flex;gap:20px;flex-wrap:wrap;padding:9px 0 12px;font-weight:700;font-size:11px;letter-spacing:.14em;text-transform:uppercase}
.nav a:hover{color:var(--red)}
.btn{display:inline-block;background:var(--red);color:#fff;font-weight:700;font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;padding:12px 22px;border-radius:3px}
.btn:hover{background:var(--redd)}.btn.ghost{background:transparent;color:var(--ink);border:1.5px solid var(--ink)}
.eyebrow{font-weight:800;font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--red)}
.seal{width:128px;aspect-ratio:1;border-radius:50%;background:var(--red);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;text-align:center;border:3px solid var(--red);box-shadow:inset 0 0 0 2px #fff;text-transform:uppercase;flex:0 0 auto}
.seal .b{font-family:"Fraunces",serif;font-size:15px;letter-spacing:.06em}
.seal .t{font-weight:700;font-size:9px;letter-spacing:.09em;line-height:1.4}
.seal .y{font-size:8.5px;letter-spacing:.3em;text-indent:.3em}
.seal.sm{width:72px;border-width:2px;box-shadow:inset 0 0 0 1.5px #fff}
.seal.sm .b{font-size:9px}.seal.sm .t{font-size:5.5px}.seal.sm .y{font-size:5px;letter-spacing:.22em}
.seal.outline{background:transparent;border-color:#fff;box-shadow:none}
.hero{display:grid;grid-template-columns:1.15fr 1fr;gap:36px;padding:38px 0 30px;align-items:center}
.hero .l{display:flex;gap:26px;align-items:flex-start}
.hero h1{font-size:50px;line-height:1.02;margin:8px 0 14px}
.hero .sub{font-size:16px;color:var(--soft);margin:0 0 20px;max-width:52ch}
.cta{display:flex;gap:12px;flex-wrap:wrap}
.spot{background:var(--wash);border:1px solid var(--line);border-radius:var(--r);padding:26px;display:flex;gap:20px;align-items:center;transition:.15s}
.spot:hover{border-color:var(--red)}
.spot h3{font-family:"Fraunces",serif;font-size:23px;line-height:1.15;margin:6px 0 8px;font-weight:600}
.spot p{margin:0 0 10px;font-size:13.5px;color:var(--soft)}
.spot .rd{font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--red)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:2px solid var(--ink);border-bottom:1px solid var(--line)}
.st{padding:18px 18px 16px}.st+.st{border-left:1px solid var(--line)}
.num{font-size:34px;color:var(--red);line-height:1}
.st .lb{font-size:10.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--soft);margin-top:7px}
.sec{padding:34px 0;border-top:1px solid var(--line)}
.sh{display:flex;align-items:center;gap:10px;margin:0 0 20px;font-weight:800;font-size:12px;letter-spacing:.18em;text-transform:uppercase}
.sh::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--red);flex:0 0 auto}
.method{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
.step{border:1px solid var(--line);border-radius:var(--r);padding:16px}
.step .n{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--red);color:var(--red);font-family:"Fraunces",serif;font-size:13px;display:flex;align-items:center;justify-content:center;margin-bottom:10px}
.step h3{font-size:13.5px;margin:0 0 6px}
.step p{margin:0;font-size:12.5px;color:var(--soft);line-height:1.5}
.fine{font-size:12px;color:var(--soft);margin-top:14px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.card{border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:.15s;background:#fff}
.card:hover{border-color:var(--red);transform:translateY(-3px)}
.card .im{height:150px;background:linear-gradient(135deg,#fafafa,#f0f0f3);position:relative}
.card .im::after{content:"";position:absolute;inset:0;margin:auto;width:72px;height:72px;border:1.5px solid rgba(228,0,43,.18);border-radius:50%}
.card .bd{padding:16px}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:9px}
.chip{border:1px solid var(--line);border-radius:3px;font-size:9.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;padding:3px 7px;color:var(--soft)}
.chip.red{border-color:var(--red);color:var(--red)}
.card .cat{font-weight:800;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--red)}
.card h3{font-size:17px;line-height:1.25;margin:6px 0 6px}
.card p{margin:0;font-size:13px;color:var(--soft)}
.vote{background:var(--wash);border-top:1px solid var(--line);padding:42px 0;text-align:center}
.vote h2{font-size:32px;margin:8px 0 10px}
.vote p{color:var(--soft);max-width:56ch;margin:0 auto 20px}
.shelf{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.prod{border:1px solid var(--line);border-radius:var(--r);padding:14px;text-align:center;position:relative}
.prod .sl{position:absolute;top:10px;left:10px;z-index:1}
.prod .im{height:120px;border-radius:8px;background:linear-gradient(135deg,#fff,#f4f4f6);border:1px solid var(--line);margin-bottom:12px}
.prod .nm{font-weight:700;font-size:13.5px}
.prod .no{font-size:12px;color:var(--soft);margin:3px 0 10px}
.prod .shp{display:block;background:var(--red);color:#fff;font-weight:700;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;padding:9px;border-radius:3px}
.box{display:grid;grid-template-columns:1.2fr 1fr;gap:30px;align-items:center;border:1.5px solid var(--ink);border-radius:var(--r);padding:34px;margin:34px 0}
.box h2{font-size:30px;margin:8px 0 10px}
.box p{color:var(--soft);margin:0 0 18px}
.box .cap{margin:0;justify-content:flex-start}
.box .ill{height:220px;border:1px solid var(--line);border-radius:var(--r);background:var(--wash);display:flex;align-items:center;justify-content:center}
.brands{background:#111114;color:#fff;padding:46px 0}
.brands .row{display:flex;gap:28px;align-items:center;margin-bottom:26px;flex-wrap:wrap}
.brands .eyebrow{color:#ff5d75}
.brands h2{font-size:32px;margin:6px 0 0}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:18px}
.bstep{border:1px solid #2c2c33;border-radius:var(--r);padding:18px}
.bstep .t{color:#ff5d75;font-weight:800;font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:8px}
.bstep p{margin:0;font-size:13px;color:#b9b9c2;line-height:1.55}
.brands .fine{color:#8a8a94;margin:0 0 20px}
.clinic{border:1px dashed #c9c9d0;border-radius:var(--r);padding:20px 22px;margin:30px 0;font-size:13.5px;color:var(--soft);line-height:1.6}
.clinic b{color:var(--ink)}
.news{background:var(--wash);border-top:2px solid var(--ink);padding:42px 0;text-align:center}
.news h2{font-size:30px;margin:0 0 8px}
.news p{color:var(--soft);margin:0 auto 18px;max-width:54ch}
.cap{display:flex;gap:10px;max-width:440px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.cap input{flex:1;min-width:200px;padding:12px 15px;border:1.5px solid var(--ink);border-radius:3px;font:inherit;background:#fff}
.cap button{font-family:"Work Sans",sans-serif;font-weight:700;font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;background:var(--red);color:#fff;border:0;padding:12px 22px;border-radius:3px;cursor:pointer}
.cap button:hover{background:var(--redd)}
.cap-ok{flex-basis:100%;font-weight:700;color:var(--red);margin-top:8px}
.foot{border-top:3px solid var(--red);margin-top:10px}
.foot .wrap{padding:30px 22px;font-size:13px;color:var(--soft);line-height:1.7}
.foot .brand{font-size:22px;color:var(--ink);display:block;margin-bottom:8px}
.cbar{background:#16161a;color:#8a8a94;font-size:12px;text-align:center;padding:9px}.cbar a{color:#ff5d75;font-weight:700}
.art{max-width:740px;margin:30px auto;padding:0 22px}
.art .cat{font-weight:800;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.art h1{font-size:42px;line-height:1.06;margin:10px 0 12px}
.art .dek{font-size:19px;color:var(--soft);margin:0 0 16px}
.badges{display:flex;gap:10px;align-items:center;margin:0 0 18px;flex-wrap:wrap}
.art .meta{font-weight:600;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);border-top:2px solid var(--ink);border-bottom:1px solid var(--line);padding:11px 0;margin-bottom:24px}
.prose{font-size:16.5px;line-height:1.75}
.prose h2{font-family:"Fraunces",serif;font-size:26px;margin:32px 0 10px;font-weight:600}
.prose h3{font-size:18px;font-weight:700;margin:24px 0 8px}
.prose strong{color:var(--ink)}
.prose table{width:100%;border-collapse:collapse;margin:20px 0;font-size:14px}
.prose th{text-align:left;border-bottom:2px solid var(--red);font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;padding:9px 10px}
.prose td{border-bottom:1px solid var(--line);padding:9px 10px}
.verdict{display:flex;gap:18px;align-items:center;border:1px solid var(--line);border-left:3px solid var(--red);border-radius:var(--r);padding:18px 20px;margin:28px 0;font-size:13.5px;color:var(--soft);line-height:1.6}
.verdict b{color:var(--ink)}.verdict a{color:var(--red);font-weight:700}
.shelf.s2{grid-template-columns:repeat(2,1fr)}
.disc{max-width:740px;margin:20px auto;padding:0 22px;color:var(--soft);font-size:12.5px}
@media(max-width:900px){.hero{grid-template-columns:1fr}.hero .l{flex-direction:column}.method{grid-template-columns:repeat(2,1fr)}.grid{grid-template-columns:1fr}.shelf{grid-template-columns:repeat(2,1fr)}.stats{grid-template-columns:repeat(2,1fr)}.stats .st:nth-child(odd){border-left:0}.stats .st:nth-child(n+3){border-top:1px solid var(--line)}.box{grid-template-columns:1fr}.steps{grid-template-columns:1fr}}
"""

def seal(year="2026", size=""):
    cls = ("seal " + size).strip()
    return (f'<div class="{cls}"><span class="b">Glassy</span>'
            f'<span class="t">Best of<br>Seoul Beauty</span><span class="y">{esc(year)}</span></div>')

def v4_chips(a):
    cat = a.get("category", "")
    if cat == "The Treatment":
        return '<span class="chip red">Panel tested</span><span class="chip">MD-reviewed ✓</span>'
    if cat == "Seoul Dispatch":
        return '<span class="chip">Field notes · Gangnam</span>'
    return '<span class="chip red">Panel tested</span>'

def v4_card(a):
    return (f'<a class="card" href="./{a["slug"]}.html"><div class="im"></div><div class="bd">'
            f'<div class="chips">{v4_chips(a)}</div><div class="cat">{esc(a.get("category",""))}</div>'
            f'<h3>{esc(a["title"])}</h3><p>{esc(a.get("dek","")[:110])}</p></div></a>')

def v4_home():
    sl, big, out = seal("2026", "sm"), seal(), seal("2026", "outline")
    mkt = "".join(f'<a class="{"on" if m=="EN" else ""}" href="#">{esc(m)}</a>' for m in MARKETS)
    steps_data = [
        ("Panels, not opinions.", "Every entry goes to three or more testers across skin tones, ages, and concerns."),
        ("Tested where the trend starts.", "Products and protocols run in Seoul, at a real cadence, for six months."),
        ("MD-reviewed.", "A Korean MD on the Panel reads every claim against the published evidence. Education, not medical advice."),
        ("Data over hype.", "Higher entry tiers fund independent ingredient and clinical-data review — never better odds."),
        ("The verdict is not for sale.", "Entry fees cover the cost of testing. Winning is free, and it cannot be bought."),
    ]
    steps = "".join(f'<div class="step"><div class="n">{i}</div><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
                    for i, (h, p) in enumerate(steps_data, 1))
    stats = "".join(f'<div class="st"><div class="num">{esc(n)}</div><div class="lb">{esc(l)}</div></div>'
                    for n, l in [("212", "SKUs tested this cycle"), ("3+", "testers per entry, every skin tone"),
                                 ("6 mo", "of wear per verdict"), ("0", "paid placements, ever")])
    grid = "".join(v4_card(a) for a in REST)
    shelf = "".join(f'<div class="prod"><span class="sl">{sl}</span><div class="im"></div>'
                    f'<div class="nm">{esc(n)}</div><div class="no">{esc(no)}</div>'
                    f'<a class="shp" href="#shop">Shop · {esc(pr)}</a></div>' for n, no, pr in SHOP)
    spot = (f'<a class="spot" href="./{FEATURED["slug"]}.html">{sl}<div>'
            f'<div class="eyebrow">Protocol of the Year</div><h3>{esc(FEATURED["title"])}</h3>'
            f'<p>{esc(FEATURED.get("dek","")[:130])}</p><span class="rd">Read the verdict →</span></div></a>')
    body = f"""
<div class="promo">The 2026 Glassy Awards are live — every winner, tested. <a href="#winners">See the list</a></div>
<header class="top"><div class="wrap m1"><div><span class="brand">Glassy</span><div class="tagline">The K-Beauty Authority</div></div><nav class="mkt">{mkt}</nav></div>
<div class="wrap"><nav class="nav"><a href="#awards">Awards</a><a>Trend Radar</a><a>The Treatment</a><a>Seoul Dispatch</a><a href="#vote">Readers’ Choice</a><a href="#box">Glassy Box</a><a href="#brands">For Brands</a></nav></div></header>
<main class="wrap">
<section class="hero" id="awards"><div class="l">{big}<div><div class="eyebrow">The Glassy Awards · 2026</div>
<h1>Best of Seoul Beauty</h1>
<p class="sub">Six months of testing. Panels across every skin tone. A Korean MD reading every claim against the evidence. No seal is ever for sale — it can only be earned.</p>
<div class="cta"><a class="btn" href="#winners">See the 2026 winners</a><a class="btn ghost" href="#method">How we test</a></div></div></div>
{spot}</section>
<div class="stats">{stats}</div>
<section class="sec" id="method"><div class="sh">How we test</div><div class="method">{steps}</div>
<p class="fine">Entry fees fund testing. They never buy a verdict.</p></section>
<section class="sec" id="winners"><div class="sh">From the Panel’s desk</div><div class="grid">{grid}</div></section>
</main>
<section class="vote" id="vote"><div class="wrap"><div class="eyebrow">Readers’ Choice 2026</div><h2>Your turn to judge.</h2>
<p>Our editors shortlist 500+ products across skin, device and clinic-grade care. Readers crown the winners over five weeks — one ballot, no brand submissions.</p>{capture('vote','Register to vote')}</div></section>
<main class="wrap">
<section class="sec" id="shop"><div class="sh">Shop the winners</div><div class="shelf">{shelf}</div>
<p class="fine">We may earn commission on purchases. Winners are chosen months before commerce is attached. {esc(DISC)}</p></section>
<section class="box" id="box"><div><div class="eyebrow">The Glassy Box</div><h2>The winners, boxed.</h2>
<p>Four times a year, the Panel packs its award winners and Seoul discoveries. $29 a month, $130+ of tested beauty inside.</p>
{capture('box','Join the waitlist')}<p class="fine">Waitlist only, for now — we’d rather test longer than ship sooner.</p></div>
<div class="ill">{big}</div></section>
</main>
<section class="brands" id="brands"><div class="wrap"><div class="row">{out}<div><div class="eyebrow">For Brands</div><h2>Earn the seal. Then put it to work.</h2></div></div>
<div class="steps"><div class="bstep"><div class="t">Enter</div><p>First 8 SKUs free; $95 standard, $295 Clean, $695 Breakthrough per additional SKU. Higher tiers fund independent ingredient and clinical-data review.</p></div>
<div class="bstep"><div class="t">Win</div><p>Winning is free, and it cannot be bought. The Panel’s verdict is the only way onto the list.</p></div>
<div class="bstep"><div class="t">License</div><p>Winners license the seal for packaging, retail and campaigns. Annual, tiered — the shelf becomes the ad.</p></div></div>
<p class="fine">The model: a seal 82% of shoppers recognize turned its winners into $82M of sales. That is the asset this masthead builds.</p>
<a class="btn" href="#brands">Request the entry kit →</a></div></section>
<main class="wrap"><div class="clinic"><span class="eyebrow">2027 · The Clinic Panel</span><br>
<b>The first MD-audited methodology for judging Seoul clinics — methodology first.</b> No clinic is named until it survives review, and we never take referral fees for a verdict. Educational only — never a booking service.</div></main>
<section class="news" id="news"><div class="wrap"><h2>What survived testing this week</h2>
<p>One email a week: the verdicts, the winners, and what Seoul is actually booking — before it trends.</p>{capture('panel','Get the Verdict')}</div></section>
<footer class="foot"><div class="wrap"><span class="brand">Glassy</span>
Concept 4 of 4 — modeled on the Allure playbook: an independent testing-and-awards authority monetized by award entry fees, seal licensing, reader-vote engagement, a subscription-box waitlist, and affiliate commerce on winners. {esc(DISC)}</div></footer>
"""
    return shell("Glassy · The Panel — the K-beauty authority", "Tested in Seoul: the awards, verdicts and winners of Korean beauty & dermatology.", FONTS4, CSS4, body)

def v4_article(a):
    sl = seal("2026", "sm")
    cat = a.get("category", "")
    if cat == "The Treatment":
        badges = f'<div class="badges">{sl}<span class="chip red">Panel tested</span><span class="chip">MD-reviewed ✓</span></div>'
    elif cat == "Seoul Dispatch":
        badges = '<div class="badges"><span class="chip">Field notes · Gangnam</span></div>'
    else:
        badges = f'<div class="badges">{sl}<span class="chip red">Protocol of the Year</span></div>'
    shelf2 = "".join(f'<div class="prod"><span class="sl">{sl}</span><div class="im"></div>'
                     f'<div class="nm">{esc(n)}</div><div class="no">{esc(no)}</div>'
                     f'<a class="shp" href="./index.html#shop">Shop · {esc(pr)}</a></div>' for n, no, pr in SHOP[:2])
    body = f"""
<div class="promo">The 2026 Glassy Awards — every winner, tested</div>
<header class="top"><div class="wrap m1"><div><a class="brand" href="./index.html">Glassy</a><div class="tagline">The K-Beauty Authority</div></div>
<nav class="mkt"><a href="./index.html#awards">Awards</a><a href="./index.html#method">How we test</a><a class="on" href="./index.html#news">Newsletter</a></nav></div></header>
<article class="art"><div class="cat">{esc(cat)}</div><h1>{esc(a['title'])}</h1>
<p class="dek">{esc(a.get('dek',''))}</p>{badges}<div class="meta">By the Glassy Panel · {esc(a.get('readtime',''))} · {esc(a.get('date',''))}</div>
<div class="prose">{a['body_html']}</div>
<div class="verdict">{sl}<div><b>This verdict follows the Panel’s methodology</b> — three or more testers, a Korean MD reading the claims against published evidence, six months in Seoul. Educational, not medical advice. <a href="./index.html#method">How we test →</a></div></div></article>
<div class="art"><div class="sh">Shop the winners</div><div class="shelf s2">{shelf2}</div>
<p class="fine">We may earn commission on purchases. Winners are chosen months before commerce is attached.</p></div>
<section class="news"><div class="wrap"><h2>Get the Verdict, weekly</h2><p>The winners, the verdicts, and what Seoul books next — before it trends.</p>{capture('panel','Subscribe')}</div></section>
<p class="disc"><a href="./index.html" style="color:var(--red);font-weight:700">← All verdicts</a> &nbsp;·&nbsp; {esc(DISC)}</p>
<footer class="foot"><div class="wrap">{esc(DISC)}</div></footer>
"""
    return shell(a['title'] + " — Glassy", a.get('dek','')[:150], FONTS4, CSS4, body)

# ==================================================================
# gallery (root)
# ==================================================================
GAL_CSS = """
*{box-sizing:border-box}body{margin:0;background:#0f0f14;color:#eee;font-family:"Inter",-apple-system,sans-serif;line-height:1.6}
a{color:inherit;text-decoration:none}
.wrap{max-width:1240px;margin:0 auto;padding:56px 24px}
h1{font-size:clamp(30px,5vw,46px);letter-spacing:-.02em;margin:0 0 12px}.lede{color:#9a9aa6;font-size:18px;max-width:70ch;margin:0 0 8px}
.small{color:#6a6a76;font-size:13px;margin:0 0 36px}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.c{display:block;background:#1a1a22;border:1px solid #2a2a34;border-radius:14px;overflow:hidden;transition:.15s;color:#eee}
.c:hover{transform:translateY(-4px);border-color:#4a4a58}
.c .sw{height:140px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px}
.c1 .sw{background:linear-gradient(135deg,#ffe0ee,#e9ddff);color:#363c73}
.c2 .sw{background:#f2f2f2;color:#111;text-transform:lowercase;font-size:26px}
.c3 .sw{background:#faf6f0;color:#c22e28;font-family:Georgia,serif;letter-spacing:.1em}
.c4 .sw{background:#e4002b;color:#fff;font-family:Georgia,serif;letter-spacing:.02em}
.c .bd{padding:20px}.c .n{font-weight:800;font-size:19px;margin:0 0 4px}.c .ref{font-size:12px;color:#8a8a96;text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.c .d{color:#9a9aa6;font-size:14px;margin:0 0 12px}.c .go{font-weight:700;font-size:13px}
.c1 .go{color:#e8388a}.c2 .go{color:#ff4d2e}.c3 .go{color:#c22e28}.c4 .go{color:#ff5d75}
@media(max-width:1080px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.cards{grid-template-columns:1fr}}
"""
def gallery():
    def card(cls, slug, name, ref, model, desc, go):
        return (f'<a class="c {cls}" href="./{slug}/index.html"><div class="sw">{name}</div><div class="bd">'
                f'<div class="ref">{esc(ref)} · {esc(model)}</div><div class="n">{esc(name)} — {esc(desc)}</div>'
                f'<div class="d">Reverse-engineered site + business model.</div><div class="go">{esc(go)} →</div></div></a>')
    cards = (card("c1","v1","Glassy · The Edit","Soko Glam / The Klog","commerce-led editorial","curated shop","Open The Edit")
             + card("c2","v2","glassy · The Radar","Hypebae / Hypebeast","trend media + brand studio","fast trends","Open The Radar")
             + card("c3","v3","Glassy · The Dispatch","Air Mail","membership + luxury ads","premium weekly","Open The Dispatch")
             + card("c4","v4","Glassy · The Panel","Allure (Condé Nast)","awards + seal licensing + box","the testing authority","Open The Panel"))
    body = f"""<main class="wrap"><h1>Glassy — four ways to build it</h1>
<p class="lede">One idea — a premium, multi-market (US / 日本 / 中文) magazine for Korean beauty & dermatology <em>trends</em> — built four ways. Each concept clones the design language <b>and</b> the business model of a different, genuinely successful business. Open each, then pick.</p>
<p class="small">Working prototypes · shared content, different skins & revenue engines · subscribe buttons capture intent locally (fake-door). {esc(DISC)}</p>
<div class="cards">{cards}</div></main>"""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Glassy — four concepts</title><meta name="description" content="Four reverse-engineered magazine concepts for a K-beauty trend publication.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
<style>{GAL_CSS}</style></head><body>{body}</body></html>"""

# ------------------------------------------------------------------ main
def main():
    (ROOT / "index.html").write_text(gallery(), encoding="utf-8")
    versions = [("v1", v1_home, v1_article), ("v2", v2_home, v2_article), ("v3", v3_home, v3_article), ("v4", v4_home, v4_article)]
    for slug, home, art in versions:
        d = ROOT / slug; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(home(), encoding="utf-8")
        for a in ARTICLES:
            (d / f"{a['slug']}.html").write_text(art(a), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("built glassy-v3: gallery + v1/v2/v3/v4 (home +", len(ARTICLES), "articles each)")

if __name__ == "__main__":
    main()
