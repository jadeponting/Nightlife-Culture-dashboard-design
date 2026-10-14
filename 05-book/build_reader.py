#!/usr/bin/env python3
"""Build the Dashboard Design reader (05-book/reader.html) from the chapters in 04-chapters/.

Nightlife Culture Style Guide v1.5. Fonts and the design system's stylesheet are inlined from the
nightlife-culture-design skill assets; no style of our own sets type. Modelled on the dashboard
book's 05-book/build_reader.py. Run from the repo root:

    python3 05-book/build_reader.py --assets <folder holding fonts.css, nc.css, nightlife-culture-wordmark.svg>

Repo paths are the default; pass --chapters DIR --root DIR --out FILE to override.
The reference section (rule register, glossary, decision log) is added after the chapters as appendices A to C.
"""
import argparse, re, html, datetime
from pathlib import Path
import markdown
from bs4 import BeautifulSoup, NavigableString

# Titles and one-line claims are the README's chapter table.
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

# The reference section, as appendices after the chapters (EDIT-PLAN stage 6). Paths are from the repo root.
APPENDICES = [
    ("06-register/rule-register.md", "A", "The rule register",
     "All 377 rules in one table: tier, kind, source, chapter rows, test, record and status"),
    ("00-plan/DECISIONS.md", "B", "The decision log",
     "Every open choice in one place, with the book's steer and the moment the build will raise it"),
    ("06-register/deviation-log.md", "C", "The deviation log",
     "The nine-line entry every departure from a rule is written to, and the entries so far"),
    ("03-tests/PROBES.md", "D", "The probe candidates",
     "Seventy-five small tests the chapters proposed; none has been run"),
]

# Sections open on arrival; the rest are folded. Matched against the heading with its "n · " prefix removed.
OPEN_SECTIONS = re.compile(r"^(the question|the 60-second version|the rules|at a glance|every rule|what this book is for|the nine-line spine|how to read this)$", re.I)

# Decision numbers in the appendices become links to their entries in the decision log.
DREF = re.compile(r"\bDB-(\d{2})\b")
RREF = re.compile(r"\bDD-(\d{3})\b")
MARK_SPAN = '<span class="nc-small mark">[{}]</span>'

# Cross-references in running text become links: "Chapter 7", "Ch 7", "Chapters 1 to 4", "rule 7.3".
XREF = re.compile(r"\b(Chapters?|Ch)\s+(\d{1,2})\b|\b([Rr]ules?)\s+(\d{1,2})\.(\d{1,2})\b")


def sec_label(num):
    return f"Appendix {num}" if num.isalpha() else f"Chapter {int(num)}"


def strip_num(t):
    return re.sub(r"^\s*\d+\s*·\s*", "", t).strip()


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60]


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
    for pre in soup.find_all("pre"):
        pre["class"] = ["nc-pre"]
        for code in pre.find_all("code"):
            code["class"] = ["nc-code"]
    for code in soup.find_all("code"):
        if not code.find_parent("pre"):
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
    for li in soup.find_all("li"):
        first = li.contents[0] if li.contents else None
        if isinstance(first, NavigableString) and str(first).startswith("[ ]"):
            first.replace_with(NavigableString(str(first)[3:].lstrip()))
    return soup


def anchor_rules(soup, num):
    """Give each rule paragraph or row an id (#rule-7-3) so cross-references land on it."""
    seen = set()
    pat = re.compile(r"^\s*(?:Rule\s+)?(\d{1,2})\.(\d{1,2})\b")
    # the rules section first, so a numbered sub-heading elsewhere never takes a rule's anchor
    rules_sec = [d for d in soup.find_all("details") if d.summary and strip_num(d.summary.get_text(strip=True)).lower() == "the rules"]
    candidates = [el for d in rules_sec for el in d.find_all(["p", "li", "tr"])]
    candidates += [el for el in soup.find_all(["p", "li", "tr"]) if el not in candidates]
    for el in candidates:
        txt = el.get_text(" ", strip=True)
        m = pat.match(txt)
        if not m or int(m.group(1)) != int(num):
            continue
        rid = f"rule-{int(m.group(1))}-{int(m.group(2))}"
        if rid in seen:
            continue
        seen.add(rid)
        el["id"] = rid
    return seen


def link_xrefs(soup, known_chapters, known_rules):
    """Turn chapter and rule references in running text into links. Never inside headings, links or code."""
    for node in list(soup.find_all(string=XREF)):
        if node.find_parent(["a", "code", "summary", "h2", "h3", "h4", "script", "style"]):
            continue
        text = str(node); out = []; last = 0
        for m in XREF.finditer(text):
            out.append(html.escape(text[last:m.start()]))
            if m.group(2):
                n = int(m.group(2)); href = f"#ch{n:02d}" if f"{n:02d}" in known_chapters else None
            else:
                rid = f"rule-{int(m.group(4))}-{int(m.group(5))}"
                href = f"#{rid}" if rid in known_rules else None
            out.append(f'<a class="nc-link" href="{href}">{html.escape(m.group(0))}</a>' if href else html.escape(m.group(0)))
            last = m.end()
        out.append(html.escape(text[last:]))
        node.replace_with(BeautifulSoup("".join(out), "html.parser"))


def link_drefs(soup):
    for node in list(soup.find_all(string=re.compile(r"\bD[BD]-\d{2,3}\b"))):
        if node.find_parent(["a", "code", "summary", "h2", "h3", "h4", "script", "style"]):
            continue
        text = html.escape(str(node))
        text = DREF.sub(lambda m: f'<a class="nc-link" href="#db-{m.group(1)}">DB-{m.group(1)}</a>', text)
        text = RREF.sub(lambda m: f'<a class="nc-link" href="#dd-{m.group(1)}">DD-{m.group(1)}</a>', text)
        node.replace_with(BeautifulSoup(text, "html.parser"))


def render_marks(md_text):
    """Chapter 0's rule: the manuscript's marks are rendered as bracketed words, because screen readers find the dagger hard."""
    def dag(m):
        a, b = m.group(1), m.group(2)
        q, f = ("'", '"'), ("`", "*")
        if (a in q and b in q) or a in f or b in f or (a == "(" and b == ")"):
            return m.group(0)
        return a + MARK_SPAN.format("abstract or summary only") + b
    md_text = re.sub(r"(.?)†(.?)", dag, md_text)
    md_text = re.sub(r'(?<!["\'`])\((read once|two passes|three passes)\)', lambda m: MARK_SPAN.format(m.group(1)), md_text)
    return md_text


def build_chapter(md_text, num, title, claim, out):
    # the status line under the title is a note, not a subtitle
    status = None
    m = re.match(r"^# .+\n\n\*(.+?)\*\n", md_text)
    if m:
        status = m.group(1); md_text = md_text[:m.start(1) - 1] + md_text[m.end():]
    if not num.isalpha() and num != "00":
        md_text = render_marks(md_text)
    body_html = markdown.markdown(md_text, extensions=["tables", "sane_lists", "fenced_code"])
    soup = BeautifulSoup(body_html, "html.parser")
    h1 = soup.find("h1")
    if h1:
        h1.decompose()
    classify(soup)
    if num.isalpha():
        # an appendix with no sections of its own is one section, so search and the rail can reach it
        if not soup.find("h2"):
            h = soup.new_tag("h2", attrs={"class": "nc-heading-2"}); h.string = title
            soup.insert(0, h)
        # a table that comes before any section gets one of its own, so the opening panel holds only the introduction
        first_h2 = soup.find("h2"); first_tab = soup.find("div", class_="nc-table-scroll")
        if first_tab is not None and first_tab.find_previous("h2") is None and first_tab.find_parent("div", class_="nc-table-scroll") is None:
            h = soup.new_tag("h2", attrs={"class": "nc-heading-2"}); h.string = "Every rule"
            first_tab.insert_before(h)
        for h3 in soup.find_all("h3"):
            m = re.match(r"^(DB-\d{2})\b", h3.get_text(strip=True))
            if m:
                h3["id"] = m.group(1).lower()
        for tr in soup.find_all("tr"):
            first = tr.find(["td", "th"])
            if first is not None:
                m = re.match(r"^(DD-\d{3})$", first.get_text(strip=True))
                if m:
                    tr["id"] = m.group(1).lower()

    sec = out.new_tag("section", id=f"ch{num}")
    sec["class"] = ["chapter"]
    head = out.new_tag("h2", attrs={"class": "nc-section-head nc-heading-1"})
    slot = out.new_tag("span", attrs={"class": "nc-number-slot"})
    n = out.new_tag("span", attrs={"class": "nc-number nc-number-box"}); n.string = num
    slot.append(n); head.append(slot)
    t = out.new_tag("span", attrs={"class": "nc-section-title"}); t.string = title
    head.append(t); sec.append(head)
    sub = out.new_tag("p", attrs={"class": "nc-subtitle"}); sub.string = claim; sec.append(sub)
    if status:
        st = out.new_tag("p", attrs={"class": "nc-small status"})
        frag = BeautifulSoup(markdown.markdown(status), "html.parser")
        for c in list(frag.p.contents):
            st.append(c)
        for code in st.find_all("code"):
            code["class"] = ["nc-file-reference"]
        sec.append(st)
    actions = out.new_tag("div", attrs={"class": "nc-action-row"})
    b1 = out.new_tag("button", attrs={"type": "button", "class": "nc-text-action", "data-expand": f"ch{num}"}); b1.string = "Expand all"
    b2 = out.new_tag("button", attrs={"type": "button", "class": "nc-text-action", "data-collapse": f"ch{num}"}); b2.string = "Collapse all"
    actions.append(b1); actions.append(b2); sec.append(actions)

    # sections by h2; anything before the first h2 (the tiers-and-flags box) becomes a panel
    current = None; lead = None; toc = []
    for node in list(soup.contents):
        if isinstance(node, NavigableString) and not str(node).strip():
            continue
        if getattr(node, "name", None) == "h2":
            stitle = node.get_text(" ", strip=True)
            current = out.new_tag("details", attrs={"class": "nc-collapsible"})
            if OPEN_SECTIONS.search(strip_num(stitle)):
                current["open"] = ""
            sid = f"ch{num}-" + slug(stitle)
            current["id"] = sid; toc.append((sid, stitle))
            summ = out.new_tag("summary")
            node["class"] = ["nc-heading-2"]
            summ.append(node.extract()); current.append(summ)
            sec.append(current)
        elif current is None:
            if lead is None:
                lead = out.new_tag("div", attrs={"class": "nc-panel nc-panel--left acc-teal"}); sec.append(lead)
            lead.append(node.extract())
        else:
            current.append(node.extract())

    # the 60-second version reads as a panel: the part to read first
    sv = sec.find("details", id=re.compile(r"-the-60-second-version$"))
    if sv:
        panel = out.new_tag("div", attrs={"class": "nc-panel nc-panel--left acc-teal sixty"})
        for c in [c for c in list(sv.contents) if getattr(c, "name", None) != "summary"]:
            panel.append(c.extract())
        sv.append(panel)

    # the question becomes the key statement
    q = sec.find("details", id=re.compile(r"-the-question$"))
    if q:
        p = q.find("p")
        if p:
            panel = out.new_tag("div", attrs={"class": "nc-key-statement-panel"})
            ks = out.new_tag("p", attrs={"class": "nc-key-statement"}); ks.string = re.sub(r"\s+", " ", p.get_text(" ", strip=True))
            panel.append(ks); p.replace_with(panel)

    # in-chapter contents, after the action row
    nav = out.new_tag("nav", attrs={"class": "chapter-toc", "aria-label": f"{sec_label(num)} sections"})
    sec["data-toc"] = "|".join(f"{sid}\t{stitle}" for sid, stitle in toc)
    lab = out.new_tag("p", attrs={"class": "nc-label"}); lab.string = "In this appendix" if num.isalpha() else "In this chapter"; nav.append(lab)
    ul = out.new_tag("ul", attrs={"class": "nc-list"})
    for sid, stitle in toc:
        li = out.new_tag("li", attrs={"class": "nc-list-item"})
        a = out.new_tag("a", attrs={"class": "nc-link", "href": f"#{sid}"}); a.string = stitle
        li.append(a); ul.append(li)
    nav.append(ul); actions.insert_after(nav)
    return sec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", default="04-chapters")
    ap.add_argument("--root", default=".", help="repo root, for the appendices")
    ap.add_argument("--assets", default=None, help="folder holding fonts.css, nc.css, nightlife-culture-wordmark.svg")
    ap.add_argument("--out", default="05-book/reader.html")
    ap.add_argument("--kick", default=None, help="masthead line under the wordmark")
    ap.add_argument("--note", default=None, help="Claude note text (HTML); omit for none")
    a = ap.parse_args()
    chapters = Path(a.chapters)
    assets = Path(a.assets) if a.assets else None
    fonts = (assets / "fonts.css").read_text() if assets else "/* fonts.css not found at build time */"
    nc = (assets / "nc.css").read_text() if assets else "/* nc.css not found at build time */"
    wordmark = (assets / "nightlife-culture-wordmark.svg").read_text() if assets else ""
    wordmark = re.sub(r"<\?xml[^>]*>|<!--.*?-->", "", wordmark, flags=re.S).strip()

    today = datetime.date.today().strftime("%-d %B %Y")
    doc = BeautifulSoup("<!DOCTYPE html><html lang='en-GB'><head></head><body class='nc-doc'></body></html>", "html.parser")
    sections = []
    for fn, num, title, claim in CHAPTERS:
        path = chapters / fn
        if not path.exists():
            continue
        sections.append([num, title, claim, build_chapter(path.read_text(), num, title, claim, doc)])

    n_chapters = len(sections)
    for fn, num, title, claim in APPENDICES:
        path = Path(a.root) / fn
        if path.exists():
            sections.append([num, title, claim, build_chapter(path.read_text(), num, title, claim, doc)])

    known_chapters = {s[0] for s in sections}
    known_rules = set()
    for num, _, _, sec in sections:
        if not num.isalpha():
            known_rules |= anchor_rules(sec, num)
    for num, _, _, sec in sections:
        link_xrefs(sec, known_chapters, known_rules)
        link_drefs(sec)

    # running foot with previous, contents and next
    for i, (num, title, claim, sec) in enumerate(sections):
        foot = doc.new_tag("div", attrs={"class": "nc-foot"})
        f1 = doc.new_tag("span", attrs={"class": "nc-running-foot"}); f1.string = f"Nightlife Culture · Dashboard Design · {sec_label(num)} · {title}"
        f2 = doc.new_tag("span", attrs={"class": "nc-running-foot"})
        links = []
        if i > 0:
            links.append((f"#ch{sections[i-1][0]}", f"Previous: {sections[i-1][0].lstrip('0') or '0'}"))
        links.append(("#contents", "Contents"))
        if i < len(sections) - 1:
            links.append((f"#ch{sections[i+1][0]}", f"Next: {sections[i+1][0].lstrip('0') or '0'}"))
        for j, (href, label) in enumerate(links):
            if j:
                f2.append(" · ")
            lk = doc.new_tag("a", attrs={"class": "nc-link", "href": href}); lk.string = label; f2.append(lk)
        foot.append(f1); foot.append(f2); sec.append(foot)

    def contents_item(num, title, claim):
        return f'<a href="#ch{num}"><span class="nc-contents-title"><span class="nc-number-slot"><span class="nc-number nc-number-box">{num}</span></span><span>{html.escape(title)}</span></span><span class="nc-small">{html.escape(claim)}</span></a>'
    contents = "".join(contents_item(n_, t_, c_) for n_, t_, c_, _ in sections[:n_chapters])
    if len(sections) > n_chapters:
        contents += '</nav><h3 class="nc-heading-3" id="appendices">The reference section</h3><p class="nc-body">Behind the book: what an agent or a build checks against, and the choices the book leaves open.</p><nav class="nc-contents" aria-label="Appendices">' + "".join(contents_item(n_, t_, c_) for n_, t_, c_, _ in sections[n_chapters:])
    rail_items = []
    for i, (num, title, claim, sec) in enumerate(sections):
        if i == n_chapters:
            rail_items.append('<p class="nc-label rail-label rail-appx">The reference section</p>')
        subs = "".join(f'<a class="rail-sub-link nc-small" href="#{t.split(chr(9))[0]}">{html.escape(t.split(chr(9))[1])}</a>' for t in sec.get("data-toc", "").split("|") if t)
        del sec["data-toc"]
        rail_items.append(f'<a class="rail-ch" href="#ch{num}" data-ch="ch{num}"><span class="nc-contents-title"><span class="nc-number-slot"><span class="nc-number nc-number-box">{num}</span></span><span>{html.escape(title)}</span></span></a><div class="rail-sub" data-for="ch{num}" hidden>{subs}</div>')
    rail = '<nav class="nc-contents nc-contents--rail rail" aria-label="Chapters"><p class="nc-label rail-label"><a class="nc-link" href="#top">Dashboard Design</a></p>' + "".join(rail_items) + '</nav>'
    kick = a.kick or f"Nightlife Culture · Dashboard Design · {today}"
    note = f'<div class="nc-claude-note"><p class="nc-label">Claude note · not for publication</p><p class="nc-small">{a.note}</p></div>' if a.note else ""

    head = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dashboard Design</title>
<meta name="nc-source" content="Nightlife Culture Style Guide v1.5; built from dashboard-design/04-chapters by 05-book/build_reader.py, {today}">
<style>
{fonts}
{nc}
html,body{{margin:0;background:var(--nc-chalk)}}
.nc-mast .nc-wordmark{{width:11rem;color:var(--nc-white);margin-bottom:var(--nc-sp5)}}
.nc-mast .nc-wordmark svg{{width:100%;height:auto;display:block}}
section.chapter{{margin-top:var(--nc-sp8);scroll-margin-top:var(--nc-sp5)}}
section.chapter p.status{{color:var(--nc-charcoal);margin-top:var(--nc-sp2)}}
.chapter-toc{{margin:var(--nc-sp4) 0}}
details[id],[id^="rule-"],[id^="d-"]{{scroll-margin-top:var(--nc-sp5)}}
:target{{background:var(--nc-white)}}
pre.nc-pre{{overflow-x:auto;max-width:100%;background:var(--nc-white);padding:var(--nc-sp3);box-sizing:border-box}}
#search-results:empty{{display:none}}
.layout{{max-width:86rem;margin:0 auto;padding:0 var(--nc-sp5) var(--nc-sp9);display:grid;grid-template-columns:16rem minmax(0,1fr);gap:var(--nc-sp7)}}
.layout>main{{min-width:0}}
.rail{{position:sticky;top:0;align-self:start;max-height:100vh;overflow-y:auto;margin:0;padding:var(--nc-sp5) 0 var(--nc-sp6)}}
.rail .rail-label{{margin:0 0 var(--nc-sp3);padding-left:var(--nc-sp3)}}
.rail a.rail-ch{{display:block;padding-top:var(--nc-sp2);padding-bottom:var(--nc-sp2)}}
.rail .rail-sub{{padding:0 0 var(--nc-sp2) var(--nc-sp6)}}
.rail .rail-sub-link{{display:block;padding:var(--nc-sp1) 0;color:var(--nc-charcoal);text-decoration:none}}
.rail .rail-sub-link:hover,.rail .rail-sub-link:focus{{text-decoration:underline;color:var(--nc-ink)}}
.sixty>p:first-child{{margin-top:0}}
.rail .rail-appx{{margin-top:var(--nc-sp5)}}
.nc-table a[href^="#d-"],.nc-table th[scope=row]{{white-space:nowrap}}
@media (min-width:60.01rem){{.chapter-toc{{display:none}}}}
@media (max-width:60rem){{.layout{{display:block}}.rail{{display:none}}}}
</style>"""
    mast = f"""<header class="nc-mast" id="top"><div class="nc-wrap">
<div class="nc-wordmark" aria-label="Nightlife Culture">{wordmark}</div>
<p class="nc-kick">{html.escape(kick)}</p>
<h1 class="nc-display">Dashboard<br>Design</h1>
<p class="stand">How dashboards work, and why: the methodological and theoretical foundation behind the Vibe Map's evidence displays, written for someone meeting the subject for the first time.</p>
</div></header>"""
    intro = f"""<div class="layout">
{rail}
<main id="main">
<div class="nc-search"><label class="nc-label" for="q">Search the whole book</label><div class="nc-search-row"><input class="nc-body" id="q" type="search" placeholder="e.g. denominator, league table, recognition" autocomplete="off"></div></div>
<div id="search-results"></div>
<h2 class="nc-section-head nc-heading-2" id="contents"><span class="nc-section-title">Contents</span></h2>
<nav class="nc-contents" aria-label="Contents">{contents}</nav>
{note}
"""
    script = """<script>
(function(){
  document.querySelectorAll('[data-expand]').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#'+b.dataset.expand+' details').forEach(function(d){d.open=true;});});});
  document.querySelectorAll('[data-collapse]').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('#'+b.dataset.collapse+' details').forEach(function(d){d.open=false;});});});
  var q=document.getElementById('q'), out=document.getElementById('search-results');
  var all=Array.prototype.slice.call(document.querySelectorAll('section.chapter details'));
  var cache=all.map(function(d){return {el:d, text:d.textContent.toLowerCase(), title:(d.querySelector('summary')||{}).textContent||'', chapter:d.closest('section').querySelector('.nc-section-title').textContent};});
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;');}
  function run(){
    var term=q.value.trim().toLowerCase(); out.innerHTML='';
    if(term.length<3){return;}
    var hits=cache.filter(function(c){return c.text.indexOf(term)>-1;});
    var h='<p class="nc-small">'+hits.length+' section'+(hits.length===1?'':'s')+' mention “'+esc(term)+'”</p>';
    if(hits.length){h+='<ul class="nc-list">'+hits.slice(0,60).map(function(c){c.el.open=true;return '<li class="nc-list-item"><a class="nc-link" href="#'+c.el.id+'">'+esc(c.chapter)+' · '+esc(c.title)+'</a></li>';}).join('')+'</ul>';}
    out.innerHTML=h;
  }
  q.addEventListener('input',run);
  function openTarget(){if(!location.hash)return; var t=document.getElementById(decodeURIComponent(location.hash.slice(1))); if(!t)return; var d=t.closest('details'); while(d){d.open=true; d=d.parentElement&&d.parentElement.closest('details');} if(t.tagName==='DETAILS'){t.open=true;} t.scrollIntoView({block:'start',inline:'nearest'});}
  window.addEventListener('hashchange',openTarget); openTarget();
  var links=Array.prototype.slice.call(document.querySelectorAll('.rail a.rail-ch'));
  function mark(id){links.forEach(function(l){var on=l.dataset.ch===id; if(on){l.setAttribute('aria-current','true');}else{l.removeAttribute('aria-current');} var sub=document.querySelector('.rail-sub[data-for="'+l.dataset.ch+'"]'); if(sub){sub.hidden=!on;}}); var rail=document.querySelector('.rail'), cur=document.querySelector('.rail a[aria-current]'); if(rail&&cur){var r=rail.getBoundingClientRect(), c=cur.getBoundingClientRect(); if(c.top<r.top||c.bottom>r.bottom){rail.scrollTop+=c.top-r.top-r.height/3;}}}
  var chapters=Array.prototype.slice.call(document.querySelectorAll('section.chapter'));
  function onScroll(){var y=window.innerHeight*0.25, id=null; chapters.forEach(function(c){if(c.getBoundingClientRect().top<=y){id=c.id;}}); mark(id);}
  window.addEventListener('scroll',onScroll,{passive:true}); onScroll();
})();
</script>"""
    parts = [f"<!DOCTYPE html>\n<html lang=\"en-GB\">\n<head>\n{head}\n</head>\n<body class=\"nc-doc\">\n{mast}\n{intro}"]
    for num, title, claim, sec in sections:
        parts.append(str(sec))
    parts.append(f'<div class="nc-foot"><span class="nc-running-foot">Nightlife Culture · Dashboard Design · the reader</span><span class="nc-running-foot">{today}</span></div>\n</main>\n</div>\n{script}\n</body>\n</html>\n')
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text("\n".join(parts))
    print("wrote", a.out, Path(a.out).stat().st_size, "bytes;", n_chapters, "chapters;", len(sections) - n_chapters, "appendices;", len(known_rules), "rule anchors")


if __name__ == "__main__":
    main()
