# Ch 1 working notes — display audit of ten landing states

*Full audit return, 16 August 2026. Method: WebFetch of live pages (server-rendered HTML).
JS-rendered defaults (Power BI, Grapher, Gapminder) observed via config files or documentation
where possible; inference is marked. Summarised in Ch 1; this is the complete record.*

## Per-instrument notes

**1. OECD Better Life Index** — oecdbetterlifeindex.org
(a) First screen: headline **"How's life?"**, explanatory paragraphs, a carousel image. The
famous flower is not the entry state of the current page. Opening framing verbatim: *"There is
more to life than the cold numbers of GDP and economic statistics."* (b) Answers the OECD's own
question at supranational geography; no place preselected. (c) Words carry everything — the
message is an argument against GDP, in prose; graphics decorative. (d) First invited actions:
"Download executive summary", "Download the index data", "Learn more about the Better Life
Initiative" — document downloads, not weighting. No weighting sliders pushed at arrival.
(e) Provenance partial: "The 2020 How's Life? report", "over 80 indicators" — a dated report
title, not a freshness stamp. INFERRED: this appears to be a rebuilt/simplified site versus the
earlier interactive flower-first version.

**2. ONS Explore Local Statistics** — ons.gov.uk/explore-local-statistics/
(a) Headline **"Explore local statistics"**, subhead **"Find, compare and visualise statistics
about places in the United Kingdom."** Search box primary: *"Search for a postcode, local
authority, region, parliamentary constituency or other named area."* (b) Answers the visitor's
question about *their* place — but only after they supply the place. Nation links offer a browse
path. (c) Words carry a capability statement; no graphics carry the message. (d) First act: type
a postcode or "Explore indicators" (108 of them). Entry move is unambiguously **search**.
(e) No date or freshness on the first screen.

**3. Thriving Places Index** — centreforthrivingplaces.org
(a) Org homepage: "Building Pathways to a Thriving Future", three CTA boxes. Index dashboard
page: headline **"Thriving Places Dashboard"**, subhead **"Does your place support people and
planet to thrive?"**, then an embedded Power BI dashboard requiring interaction — fetched
instructions say **"Select the name of the local authority using the drop-down in the top
corner."** A place score does *not* appear on arrival. (b) Answers a policy-maker's question at
England local-authority geography, after selection. (c) Scoring language via documented colour
scale: 0–10, *"<3.5 = very low compared to the England average"* through *">6.5 = very high"*,
organised by domains (Local Conditions, Equality, Sustainability). (d) First act: choose an
authority from a dropdown. (e) Provenance good: page modified 2025-12-16; 2024 Indicator List
and 2024 Methodology linked. Map page embed could not be observed. INFERRED: map likely loads
all authorities coloured.

**4. Our World in Data** — ourworldindata.org + /grapher/life-expectancy
(a) Homepage headline **"Research and data to make progress against the world's largest
problems."** First screen: inventory (14,071 charts, 126 topic pages, 29 explorers, 501
articles), featured articles, topics. (b) OWID's own mission question at global geography.
(c) Words carry mission + scale; the stat block is the graphic. (d) First act: browse/search/
read. (e) Freshness conspicuous: relative dates ("Yesterday," "13 days ago") as homepage
furniture.
Grapher page (defaults recovered from **config.json**, not the rendered page): title "Life
expectancy", subtitle "over the long-run" — a noun phrase, not a sentence. Default entities:
**World, Americas, Europe, Africa, Asia, Oceania** — continents, never a random country; default
tab "map". Source line: "Riley (2005); Zijdeman et al. (2015); HMD (2025); UN WPP (2024) – with
major processing by Our World in Data," last updated 2025-10-22 — provenance is first-screen
furniture on every chart.

**5. The Pudding, "This is a teenager"** — pudding.cool/2024/03/teenagers/
(a) Scroll position zero: headline **"This is a teenager"**, byline, an interactive timeline
(1997–2021) with slider "Avg age 13", narrative beginning **"This is a teenager. We'll call him
Alex. It's 1997…"** Prompts: "(Click a kid to see details)", "Keep scrolling ↓". (b) The reader
is handed one *exemplar person*, not a geography; unit is a human. (c) Words carry a story; the
graphic carries the population the story is one instance of. (d) First act: scroll, or click a
kid. (e) No publication date visible at top — provenance deferred to footer. Weakest freshness
signal in the set.

**6. Creative Footprint** — creative-footprint.org
(a) First screen: logo, strapline **"The Creative Footprint is a non-profit initiative that
measures and indexes live music space"**, three verbs "Monitor / Engage / Reclaim", button "Read
the CFP Reports", hero image. Cities listed: Copenhagen, Rotterdam, Sydney, Montréal, Stockholm,
Tokyo, New York, Berlin. **No scores or visualisations on the landing page.** (b) The
organisation's advocacy question at city level; no city's result shown on arrival. (c) Words
carry mission verbs; graphics carry atmosphere. (d) First act: request a report via a form (a
gated PDF), or newsletter. A city's result on arrival is **a story behind a form**. (e)
Provenance thin: "(c) 2023," "Since its founding in 2017." No data dates.

**7. London Night Time Data Observatory** — data.london.gov.uk/night-time-observatory/
(a) Headline "Night Time Observatory"; intro verbatim: *"This webpage contains a range of
research and data on London at night. The first iteration of the Observatory contains links to
over 30 data sources split across four themes…"* Four theme cards: Vibrancy, Vitality, Safety,
Livability, each defined in a sentence. (b) A researcher's question ("where is the data?") at
London-wide geography; no place, no number, no picture of the night. (c) Words carry a taxonomy.
(d) First act: pick a theme, then leave for someone else's dataset. (e) Freshness: none beyond a
2018 report reference; the intro's own "first iteration… plans to build on this in the future"
is the page admitting its landing state is a promise.

**8. Gapminder Tools** — **FAILED TO FETCH** (repeated redirects, two variants). Marketing
homepage did fetch: "You are probably wrong about" + rotating topics; tools under "Free tools
for a fact-based worldview"; first invited act is a quiz. INFERRED, not observed: the tools app
conventionally opens on income-vs-life-expectancy bubbles, latest year, all countries plotted,
none selected, play button (not autoplay). Treat as prior knowledge, not audit evidence.

**9. GLA Cultural Infrastructure Map** — dataset page + apps.london.gov.uk/cim/
(a) Dataset landing: description verbatim: *"London's first Cultural Infrastructure Map brings
together new research and information that has previously not existed in one place."* Map
linked, not embedded. The map tool fetched only partially (JS app): role selection ("A Public
User" / "Venue Operator"), borough/ward filters, travel-time tools; default pin state
unconfirmed. INFERRED: category layers, many pins on load. (b) The GLA's planning question at
borough/venue geography. (c) Institutional first-ness claim in words. (d) First act: click
through to the tool. (e) Provenance unusually honest: "Data captured between January 2018 and
June 2019," 2023 revision, "Last Update over 2 years ago" — a staleness confession, but on the
dataset page, not the map. Note: mylocalculture.org.uk failed (likely dead domain).

**10. BBC postcode interactive** — "NHS tracker – are hospital waiting times improving near
you?" (fetched via feeds.bbci.co.uk mirror; direct bbc.co.uk 403 from proxy)
(a) Headline verbatim **"NHS tracker - are hospital waiting times improving near you?"** — the
headline *is* a question addressed to the reader. Four paragraphs of national context, ending
"Use your postcode to find out whether waiting lists are getting better near you", then the
input, then "About the data." (b) The default answers the *national* question in prose; the
personal answer withheld until you type. (c) Words carry the news line and the instruction; the
result chart doesn't exist until you act. (d) First act: read, then type a postcode.
(e) "Published" notation and methodology section adjacent.

## Pattern synthesis — six landing patterns

**1. Message-first (prose argument, data deferred).** OECD BLI, Creative Footprint, OWID
homepage, Gapminder homepage. Assumes a visitor who needs persuading the question matters. Does
well: framing, mission clarity. Fails: the data can recede entirely — OECD's landing now offers
PDFs where the flower once bloomed; Creative Footprint gates its only results behind a form.
Message-first with no exemplar risks becoming brochure-first.

**2. Input-first (blank until you identify yourself).** ONS ELS; BBC pieces are the hybrid
(message-*then*-input). Assumes the visitor arrives with a place in mind. Does well: instant
personal relevance. Fails: the empty state shows nothing — no proof the answer is worth typing
for. The BBC hybrid fixes this with four paragraphs of stakes; pure search spends zero.

**3. Select-first (dashboard awaiting a dropdown).** TPI. Structurally input-first but
tool-shaped: you arrive at an instrument panel, not a question. Assumes a professional who knows
which authority they manage. Does well: rich comparable scoring once selected. Fails: a citizen
arriving cold sees controls, not meaning; Power BI embeds are opaque to search, sharing, and
fetching.

**4. Exemplar-first (one concrete instance carries the dataset).** The Pudding ("Alex"); OWID
Grapher defaults (World + continents is choosing an exemplar aggregation rather than an empty
chart). Assumes a visitor with no prior question who must be given a protagonist. Does well:
zero-effort meaning at scroll position zero; the default already says something true. Fails: the
exemplar's framing is authorial and sticky; provenance can slip to the footer.

**5. Links-hub (taxonomy of elsewhere).** Observatory; the GLA dataset page as a one-item
variant. Assumes a researcher-librarian. Does well: honest scoping, low maintenance, good theme
vocabulary. Fails: communicates nothing about the subject itself on arrival; freshness rots
visibly. A hub's landing state is a promissory note.

**6. Map/field-first (everything plotted, filter to focus).** GLA CIM tool (partially INFERRED);
Gapminder tools (INFERRED); the Pudding's clickable field borrows this. Assumes a browsing
visitor who reads density before value. Does well: an all-pins map's first message is abundance
and coverage. Fails: answers "how much, where" but not "so what"; every pin equal means no pin
argued for; staleness invisible on a pin.

**Cross-cutting.** (i) Provenance on the first screen splits the field: OWID and TPI treat
freshness as display content; The Pudding, Creative Footprint, ONS and the Observatory defer or
omit it. (ii) The strongest openings put a *question in the visitor's voice* in the headline
(BBC, TPI); the weakest lead with the institution's self-description ("London's first…",
"non-profit initiative that measures…"). (iii) None of the ten pushes weighting or configuration
at arrival; the slider-first era appears over.

**Failed/degraded fetches:** gapminder.org/tools (redirect loop — inference only);
mylocalculture.org.uk (dead); bbc.co.uk direct (403 — content via feeds mirror); OWID Grapher
and both Power BI embeds render via JS — defaults from config.json (OWID) and on-page
documentation (TPI).
