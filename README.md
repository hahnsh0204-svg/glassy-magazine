# Glassy — four magazine concepts

One idea — a **premium, multi-market (US / 日本 / 中文) online magazine for Korean beauty & dermatology *trends***, curated with taste and sourced from Seoul, with a light MD trust layer — built **four ways**. Each concept clones the design language **and** the business model of a different, genuinely successful business.

| Concept | Reverse-engineered from | Business model |
|---|---|---|
| **v1 · The Edit** | Soko Glam / The Klog | commerce-led editorial (curated shop + affiliate) |
| **v2 · The Radar** | Hypebae / Hypebeast | fast trend media + brand studio (labeled native) + commerce |
| **v3 · The Dispatch** | Air Mail | premium membership + luxury advertising + shop-as-editorial |
| **v4 · The Panel** | Allure (Condé Nast) | testing authority + awards entry fees & seal licensing + box waitlist |

A gallery at the root lets you compare the four and pick.

## Build

```bash
pip install markdown
python build.py     # renders index.html (gallery) + v1/ v2/ v3/ v4/ (home + articles each)
```

Shared content = `content/*.md`. Each version renders the same stories in its own skin and revenue engine.

## Positioning

Not the medical-evidence journal (that was an earlier direction) — this is the **trend magazine**: *what's blowing up in Korean skin, beauty & derm right now, and whether you should care* — fast, tasteful, multi-market, sanity-checked by a doctor. Market & business research in `RESEARCH_BRIEF.md` (cited).

## Status

Prototype. Subscribe / member buttons capture intent locally (fake-door). Shop / sponsored / membership modules are illustrative. Educational information, not medical advice; no specific clinic promotion; prices indicative as of Jul 2026.
