#!/usr/bin/env python3
"""Build the Dashboard Design reader (05-book/reader.html) from the version 2 chapters.

Nightlife Culture Style Guide v1.5. Fonts and the design system's stylesheet are inlined from the
nightlife-culture-design skill assets; no style of our own sets type. Run from the repo root:

    python3 05-book/build_reader.py

Repo paths are the default; pass --chapters DIR --assets DIR --out FILE to override.
"""
import argparse, re, html, datetime
from pathlib import Path
import markdown
from bs4 import BeautifulSoup, NavigableString

CHAPTERS = [
    ("ch00-how-to-read-this-book.md", "00", "How to read this book",
     "The legend: five kinds of claim, three tiers, the flags — and what the book never does."),
    ("ch01-what-a-dashboard-is-for.md", "01", "What a dashboard is for",
     "A display that turns data into a decision for a named reader. An argument, not a window."),
    ("ch02-who-reads-it-and-what-turns-their-decision.md", "02", "Who reads it, and what turns their decision",
     "There is no reader in general. Access, timing and relationships move decisions more than charts do."),
    ("ch03-the-canonical-truths-of-showing-data.md", "03", "The canonical truths of showing data",
     "Seven rules that survived testing, and the record beneath them."),
    ("ch04-from-data-to-evidence.md", "04", "From data to evidence",
     "A number is undefined until its unit, period and base are stated. Nothing is never one thing."),
    ("ch05-building-a-measure.md", "05", "Building a measure",
     "A composite is a model; weights are judgements; a rank carries its interval; the recipe goes on the face."),
    ("ch06-finding-value-in-the-data.md", "06", "Finding value in the data",
     "Behaviour is evidence of value and every record names who is in it. A dashboard speaks from the first rung and says so."),
    ("ch07-comparison-time-and-intervention.md", "07", "Comparison, time and intervention",
     "A comparison declares what it holds equal and who chose the comparators. After is not because."),
    ("ch08-automation-without-admin.md", "08", "Automation without admin",
     "Freshness is a declared lifetime; a dashboard is a service; the phone sets the budget; a map is a licence, a supply and a vintage."),
    ("ch09-measuring-a-vibe.md", "09", "Measuring a vibe",
     "A vibe is three constructs, never one number; a felt measure is a distribution with its sample; who was asked is part of the measure."),
    ("ch10-safety-ethics-and-consent.md", "10", "Safety, ethics and consent",
     "Anonymity is a property of data in its environment; the house does not publish on consent; a community is consulted, governs and agrees."),
    ("ch11-the-first-screen-and-the-path-through-it.md", "11", "The first screen and the path through it",
     "The first screen is a sentence to a named reader; every landing is an endorsement; interaction is paid for; a citable state is an address and a dated snapshot."),
    ("ch12-recognising-your-place.md", "12", "Recognising your place",
     "A figure about a place is a figure about a unit; identity is never ranked; the two columns side by side; discovery is matching; a crop carries its provenance."),
    ("ch13-accessible-as-the-good-version.md", "13", "Accessible as the good version",
     "The accessible version is the version; a chart meets the standard by its description, its table and its status; the statement is a public record."),
    ("ch14-where-evidence-meets-expression.md", "14", "Where evidence meets expression",
     "Expression is tested by what remains when it is removed, and it buys engagement, mood and recognition — not accuracy."),
    ("ch15-learning-from-the-best.md", "15", "Learning from the best",
     "Trust is measured as producers measure theirs, or not claimed; no arrow without a printed rule; every public data project ends, and the plan is written first."),
    ("ch16-breaking-these-rules-well.md", "16", "Breaking these rules well",
     "Fixed in three senses; a short Fixed register the build enforces; one deviation log with nine lines; the twelve records as one."),
]

OPEN_SECTIONS = re.compile(r"(the question|60-second|holds true|the truths|^the rules|what holds|^postscript)", re.I)


def classify(soup):
    """Apply the design system's roles to generic markdown output."""
    for h in soup.find_all("h2"):
        h["class"] = ["nc-heading-2"]
    for h in soup.find_all("h3"):
        h["class"] = ["nc-heading-3"]
    for h in soup.find_all("h4"):
        h["class"] = ["nc-heading-4"]
    for h in soup.find_all(["h5", "h6"]):
        h.name = "h4"; h["class"] = ["nc-heading-4"]
    for p in soup.find_all("p"):
        p["class"] = p.get("class", []) + ["nc-body"]
    for ul in soup.find_all("ul"):
        ul["class"] = ["nc-list"]
    for ol in soup.find_all("ol"):
        ol["class"] = ["nc-list", "nc-list--num"]
    for li in soup.find_all("li"):
        li["class"] = ["nc-list-item"]
    for a in soup.find_all("a"):
        a["class"] = ["nc-link"]
    for hr in soup.find_all("hr"):
        hr.decompose()
    for code in soup.find_all("code"):
        txt = code.get_text()
        if txt.startswith("["):
            code.name = "span"; code["class"] = ["nc-evidence-mark"]
        else:
            code["class"] = ["nc-file-reference"]
    for bq in soup.find_all("blockquote"):
        bq.name = "div"; bq["class"] = ["nc-panel", "nc-panel--left", "acc-violet"]
    for t in soup.find_all("table"):
        t["class"] = ["nc-table"]
        for th in t.find_all("th"):
            th["scope"] = "col"
        body = t.find("tbody")
        if body:
            for tr in body.find_all("tr"):
                first = tr.find(["td", "th"])
                if first is not None and first.name == "td":
                    first.name = "th"; first["scope"] = "row"
        wrap = soup.new_tag("div", attrs={"class": "nc-table-scroll"})
        t.wrap(wrap)
    # checklist items: the list bullet is the box; drop the raw brackets
    for li in soup.find_all("li"):
        first = li.contents[0] if li.contents else None
        if isinstance(first, NavigableString) and str(first).startswith("[ ]"):
            first.replace_with(NavigableString(str(first)[3:].lstrip()))
    return soup


MARK_SPAN = '<span class="nc-evidence-mark">[{}]</span>'


def render_marks(md_text):
    """Chapter 0's rule: the manuscript's marks are rendered as bracketed words in the reader."""
    def dag(m):
        a, b = m.group(1), m.group(2)
        q, f = ("'", '"'), ("`", "*")
        if (a in q and b in q) or a in f or b in f:
            return m.group(0)  # a quoted or formatted dagger is text about the mark, not a mark
        return a + MARK_SPAN.format("abstract or secondary") + b
    md_text = re.sub(r"(.?)†(.?)", dag, md_text)
    md_text = re.sub(r"\((read once|two passes|three passes)\)", lambda m: MARK_SPAN.format(m.group(1)), md_text)
    return md_text


def build_chapter(md_text, num, title, soup_factory):
    if num != "00":
        md_text = render_marks(md_text)
    # the two italic lines under the chapter title become one subtitle line
    md_text = re.sub(r"(^# .+\n\n)\*(.+?)\*\n\*(.+?)\*\n", lambda m: f"{m.group(1)}*{m.group(2)} · {m.group(3)}*\n", md_text, count=1, flags=re.M)
    body_html = markdown.markdown(md_text, extensions=["tables", "sane_lists"])
    soup = BeautifulSoup(body_html, "html.parser")
    # drop the markdown h1; the reader sets its own chapter heading
    h1 = soup.find("h1")
    if h1:
        h1.decompose()
    classify(soup)
    # the first italic paragraphs after the title are the chapter's subtitle lines
    subs = []
    for p in list(soup.find_all("p", recursive=False))[:3]:
        if p.find("em") and len(p.get_text()) < 220 and p.get_text().strip().startswith(p.find("em").get_text().strip()[:10]):
            p["class"] = ["nc-subtitle"]; subs.append(p)
        else:
            break
    # group into sections by h2
    out = soup_factory()
    sec = out.new_tag("section", id=f"ch{num}")
    sec["class"] = ["chapter"]
    head = out.new_tag("h2", attrs={"class": "nc-section-head nc-heading-1"})
    slot = out.new_tag("span", attrs={"class": "nc-number-slot"})
    n = out.new_tag("span", attrs={"class": "nc-number nc-number-box"}); n.string = num
    slot.append(n); head.append(slot)
    t = out.new_tag("span", attrs={"class": "nc-section-title"}); t.string = title
    head.append(t); sec.append(head)
    for p in subs:
        sec.append(p.extract())
    actions = out.new_tag("div", attrs={"class": "nc-action-row"})
    b1 = out.new_tag("button", attrs={"type": "button", "class": "nc-text-action", "data-expand": f"ch{num}"}); b1.string = "Expand all"
    b2 = out.new_tag("button", attrs={"type": "button", "class": "nc-text-action", "data-collapse": f"ch{num}"}); b2.string = "Collapse all"
    actions.append(b1); actions.append(b2); sec.append(actions)

    current = None
    for node in list(soup.contents):
        if isinstance(node, NavigableString) and not str(node).strip():
            continue
        if getattr(node, "name", None) == "h2":
            current = out.new_tag("details", attrs={"class": "nc-collapsible"})
            stitle = node.get_text(" ", strip=True)
            if OPEN_SECTIONS.search(stitle):
                current["open"] = ""
            sid = f"ch{num}-" + re.sub(r"[^a-z0-9]+", "-", stitle.lower()).strip("-")[:60]
            current["id"] = sid
            summ = out.new_tag("summary")
            node["class"] = ["nc-heading-2"]
            summ.append(node.extract()); current.append(summ)
            sec.append(current)
        else:
            if current is None:
                sec.append(node.extract())
            else:
                current.append(node.extract())
    # the question: a bold paragraph becomes the key statement
    q = sec.find("details", id=re.compile(r"the-question"))
    if q:
        for p in q.find_all("p"):
            if p.find("strong") and len(p.get_text()) < 400:
                panel = out.new_tag("div", attrs={"class": "nc-key-statement-panel"})
                ks = out.new_tag("p", attrs={"class": "nc-key-statement"}); ks.string = p.get_text(strip=True)
                panel.append(ks); p.replace_with(panel); break
    foot = out.new_tag("div", attrs={"class": "nc-foot"})
    f1 = out.new_tag("span", attrs={"class": "nc-running-foot"}); f1.string = f"Nightlife Culture · Dashboard Design · Chapter {int(num)} — {title}"
    f2 = out.new_tag("span", attrs={"class": "nc-running-foot"})
    back = out.new_tag("a", attrs={"class": "nc-link", "href": "#contents"}); back.string = "Back to contents"
    f2.append(back); foot.append(f1); foot.append(f2); sec.append(foot)
    return sec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", default="04-chapters")
    ap.add_argument("--assets", default=None, help="folder holding fonts.css, nc.css, nightlife-culture-wordmark.svg")
    ap.add_argument("--out", default="05-book/reader.html")
    a = ap.parse_args()
    chapters = Path(a.chapters)
    assets = Path(a.assets) if a.assets else None
    fonts = (assets / "fonts.css").read_text() if assets else "/* fonts.css not found at build time */"
    nc = (assets / "nc.css").read_text() if assets else "/* nc.css not found at build time */"
    wordmark = (assets / "nightlife-culture-wordmark.svg").read_text() if assets else ""
    wordmark = re.sub(r"<\?xml[^>]*>|<!--.*?-->", "", wordmark, flags=re.S).strip()

    today = datetime.date.today().strftime("%-d %B %Y")
    doc = BeautifulSoup("<!DOCTYPE html><html lang='en-GB'><head></head><body class='nc-doc'></body></html>", "html.parser")
    sf = lambda: doc
    sections = []
    for fn, num, title, claim in CHAPTERS:
        path = chapters / fn
        if not path.exists():
            continue
        sections.append((num, title, claim, build_chapter(path.read_text(), num, title, sf)))

    contents = "".join(
        f'<a href="#ch{num}"><span class="nc-contents-title"><span class="nc-number-slot"><span class="nc-number nc-number-box">{num}</span></span><span>{html.escape(title)}</span></span><span class="nc-small">{html.escape(claim)}</span></a>'
        for num, title, claim, _ in sections)

    head = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Design — the reader — Nightlife Culture</title>
<meta name="nc-source" content="Nightlife Culture Style Guide v1.5; built from dashboard-design/04-chapters by 05-book/build_reader.py, {today}">
<style>
{fonts}
{nc}
html,body{{margin:0;background:var(--nc-chalk)}}
.nc-mast .nc-wordmark{{width:11rem;color:var(--nc-white);margin-bottom:var(--nc-sp5)}}
.nc-mast .nc-wordmark svg{{width:100%;height:auto;display:block}}
section.chapter{{margin-top:var(--nc-sp8)}}
#search-results:empty{{display:none}}
</style>"""
    mast = f"""<header class="nc-mast"><div class="nc-wrap">
<div class="nc-wordmark" aria-label="Nightlife Culture">{wordmark}</div>
<p class="nc-kick">Nightlife Culture · Dashboard Design · Research book, version 2 · {today}</p>
<h1 class="nc-display">Dashboard<br>Design</h1>
<p class="stand">How dashboards work and why — the methodological foundation for the Vibe Map's evidence displays, written for a reader meeting the subject for the first time. All four parts: Foundations (0–3), the analytical foundation (4–8), the felt layer (9–10), the reading experience (11–13), the boundary and the practice (14–16).</p>
</div></header>"""
    intro = f"""<div class="nc-wrap">
<div class="nc-panel nc-panel--left acc-teal"><p class="nc-label">How to use this reader</p><p class="nc-body">Each chapter opens with its question and its 60-second version; the rest is folded. Open a section by clicking its heading, or use <em>Expand all</em>. The search opens every section that contains the words you type. Every rule carries a kind — Standard, Evidence, Reading, Practice or Nightlife Culture — and a tier — Fixed (as a requirement, a sequence or a statement of the record), Adaptable or Decorative; Chapter 0 explains both, and Chapter 16 re-bases the tiers for the build. Flags in square brackets mark loose ends. This page is generated from the chapter files in <code class="nc-file-reference">04-chapters/</code>; the files are the record and the research log is the journey.</p></div>
<div class="nc-search"><label class="nc-label" for="q">Search the whole book</label><div class="nc-search-row"><input class="nc-body" id="q" type="search" placeholder="e.g. denominator, Code of Practice, suppression" autocomplete="off"></div></div>
<div id="search-results"></div>
<h2 class="nc-section-head nc-heading-2" id="contents"><span class="nc-section-title">Contents</span></h2>
<nav class="nc-contents" aria-label="Contents">{contents}</nav>
<div class="nc-claude-note"><p class="nc-label">Claude note · not for publication</p><p class="nc-small">Draft reader. Chapters 1–16 are at draft 2 and have not yet been read by Carly; Chapter 0 was revised on 7 October 2026. Before relying on a claim: the library pass (<code class="nc-file-reference">01-sources/LIBRARY-PASS.md</code>) proposes ten corrections that have not been applied to these chapters; the rule register (<code class="nc-file-reference">06-register/</code>) is the current statement of each rule\'s tier where it differs from a chapter\'s table; and Chapter 16 ends with a postscript. The manuscript\'s marks (†, "(read once)", "(two passes)") are rendered here as bracketed words. The chapter files in the repository are the source of truth; regenerate this page with <code class="nc-file-reference">05-book/build_reader.py</code> after any edit.</p></div>
"""
    script = """<script>
(function(){
  document.querySelectorAll('[data-expand]').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#'+b.dataset.expand+' details').forEach(function(d){d.open=true;});});});
  document.querySelectorAll('[data-collapse]').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#'+b.dataset.collapse+' details').forEach(function(d){d.open=false;});});});
  var q=document.getElementById('q'), out=document.getElementById('search-results');
  var all=Array.prototype.slice.call(document.querySelectorAll('section.chapter details'));
  var cache=all.map(function(d){return {el:d, text:d.textContent.toLowerCase(), title:(d.querySelector('summary')||{}).textContent||'', chapter:d.closest('section').querySelector('.nc-section-title').textContent};});
  function run(){
    var term=q.value.trim().toLowerCase(); out.innerHTML='';
    if(term.length<3){return;}
    var hits=cache.filter(function(c){return c.text.indexOf(term)>-1;});
    var h='<p class="nc-small">'+hits.length+' section'+(hits.length===1?'':'s')+' mention “'+term.replace(/</g,'&lt;')+'”</p>';
    if(hits.length){h+='<ul class="nc-list">'+hits.slice(0,40).map(function(c){c.el.open=true;return '<li class="nc-list-item"><a class="nc-link" href="#'+c.el.id+'">'+c.chapter.replace(/</g,'&lt;')+' · '+c.title.replace(/</g,'&lt;')+'</a></li>';}).join('')+'</ul>';}
    out.innerHTML=h;
  }
  q.addEventListener('input',run);
  // open a folded section when its anchor is the target
  function openTarget(){var t=location.hash&&document.querySelector(location.hash); if(t){var d=t.closest('details'); if(d){d.open=true;} if(t.tagName==='DETAILS'){t.open=true;}}}
  window.addEventListener('hashchange',openTarget); openTarget();
})();
</script>"""
    parts = [f"<!DOCTYPE html>\n<html lang=\"en-GB\">\n<head>\n{head}\n</head>\n<body class=\"nc-doc\">\n{mast}\n{intro}"]
    for num, title, claim, sec in sections:
        parts.append(str(sec))
    parts.append(f'<div class="nc-foot"><span class="nc-running-foot">Nightlife Culture · Dashboard Design · the reader</span><span class="nc-running-foot">Version 2 · {today}</span></div>\n</div>\n{script}\n</body>\n</html>\n')
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text("\n".join(parts))
    print("wrote", a.out, Path(a.out).stat().st_size, "bytes;", len(sections), "chapters")


if __name__ == "__main__":
    main()
