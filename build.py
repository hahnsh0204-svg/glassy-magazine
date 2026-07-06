#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Glassy v3 — three reverse-engineered magazine concepts for a premium, multi-market
(US/JP/CN) Korean beauty & dermatology TREND magazine. Each concept clones the design
language AND the business model of a different, genuinely successful business:

  V1 · "The Edit"      ← Soko Glam / The Klog   — commerce-led editorial (curated shop)
  V2 · "The Radar"     ← Hypebae / Hypebeast     — trend media + brand studio + commerce
  V3 · "The Dispatch"  ← Air Mail                — premium membership + luxury advertising

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
<div class="cbar">Concept prototype · reverse-engineered design & business model · <a href="{rel}/index.html">← compare all three</a></div>
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
Concept 1 of 3 — modeled on the Soko Glam / The Klog playbook: editorial that curates the shelf, monetized by curated commerce & affiliate. {esc(DISC)}</div></footer>
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
Concept 2 of 3 — modeled on the Hypebae / Hypebeast playbook: fast trend media monetized by a brand studio (labeled native), commerce, and scale. {esc(DISC)}</div></footer>
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
Concept 3 of 3 — modeled on the Air Mail playbook: a premium curated weekly monetized by membership and luxury advertising, with a shop-as-editorial and a medical-tourism concierge. {esc(DISC)}</div></footer>
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
# gallery (root)
# ==================================================================
GAL_CSS = """
*{box-sizing:border-box}body{margin:0;background:#0f0f14;color:#eee;font-family:"Inter",-apple-system,sans-serif;line-height:1.6}
.wrap{max-width:1080px;margin:0 auto;padding:56px 24px}
h1{font-size:clamp(30px,5vw,46px);letter-spacing:-.02em;margin:0 0 12px}.lede{color:#9a9aa6;font-size:18px;max-width:70ch;margin:0 0 8px}
.small{color:#6a6a76;font-size:13px;margin:0 0 36px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.c{display:block;background:#1a1a22;border:1px solid #2a2a34;border-radius:14px;overflow:hidden;transition:.15s;color:#eee}
.c:hover{transform:translateY(-4px);border-color:#4a4a58}
.c .sw{height:140px;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px}
.c1 .sw{background:linear-gradient(135deg,#ffe0ee,#e9ddff);color:#363c73}
.c2 .sw{background:#f2f2f2;color:#111;text-transform:lowercase;font-size:26px}
.c3 .sw{background:#faf6f0;color:#c22e28;font-family:Georgia,serif;letter-spacing:.1em}
.c .bd{padding:20px}.c .n{font-weight:800;font-size:19px;margin:0 0 4px}.c .ref{font-size:12px;color:#8a8a96;text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.c .d{color:#9a9aa6;font-size:14px;margin:0 0 12px}.c .go{font-weight:700;font-size:13px}
.c1 .go{color:#e8388a}.c2 .go{color:#ff4d2e}.c3 .go{color:#c22e28}
@media(max-width:820px){.cards{grid-template-columns:1fr}}
"""
def gallery():
    def card(cls, slug, name, ref, model, desc, go):
        return (f'<a class="c {cls}" href="./{slug}/index.html"><div class="sw">{name}</div><div class="bd">'
                f'<div class="ref">{esc(ref)} · {esc(model)}</div><div class="n">{esc(name)} — {esc(desc)}</div>'
                f'<div class="d">Reverse-engineered site + business model.</div><div class="go">{esc(go)} →</div></div></a>')
    cards = (card("c1","v1","Glassy · The Edit","Soko Glam / The Klog","commerce-led editorial","curated shop","Open The Edit")
             + card("c2","v2","glassy · The Radar","Hypebae / Hypebeast","trend media + brand studio","fast trends","Open The Radar")
             + card("c3","v3","Glassy · The Dispatch","Air Mail","membership + luxury ads","premium weekly","Open The Dispatch"))
    body = f"""<main class="wrap"><h1>Glassy — three ways to build it</h1>
<p class="lede">One idea — a premium, multi-market (US / 日本 / 中文) magazine for Korean beauty & dermatology <em>trends</em> — built three ways. Each concept clones the design language <b>and</b> the business model of a different, genuinely successful business. Open each, then pick.</p>
<p class="small">Working prototypes · shared content, different skins & revenue engines · subscribe buttons capture intent locally (fake-door). {esc(DISC)}</p>
<div class="cards">{cards}</div></main>"""
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Glassy — three concepts</title><meta name="description" content="Three reverse-engineered magazine concepts for a K-beauty trend publication.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
<style>{GAL_CSS}</style></head><body>{body}</body></html>"""

# ------------------------------------------------------------------ main
def main():
    (ROOT / "index.html").write_text(gallery(), encoding="utf-8")
    versions = [("v1", v1_home, v1_article), ("v2", v2_home, v2_article), ("v3", v3_home, v3_article)]
    for slug, home, art in versions:
        d = ROOT / slug; d.mkdir(exist_ok=True)
        (d / "index.html").write_text(home(), encoding="utf-8")
        for a in ARTICLES:
            (d / f"{a['slug']}.html").write_text(art(a), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("built glassy-v3: gallery + v1/v2/v3 (home +", len(ARTICLES), "articles each)")

if __name__ == "__main__":
    main()
