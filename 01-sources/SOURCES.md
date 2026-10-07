# Sources ledger — dashboard-design

*The durable record of what the chapters cite, where each thing lives, and how far it was
verified. Updated at the end of every chapter sprint. Started 16 August 2026, covering
Chapters 1–4.*


> **Version 2 note, 6 October 2026.** The citation marks in §1 below were version 1's. Version 2 replaces them with the legend in `04-chapters/ch00-how-to-read-this-book.md`: every source is one of **Standard · Evidence · Reading · Nightlife Culture** (with *practitioner* noted where a Reading source is a practitioner's account), and every entry says how it was read — *at source* (link opened, quotation taken, date), *spot-checked* (the orchestrator re-opened it), *verified* (an independent agent re-traced it), *abstract* (authors' summary only; marked † where it supports a Fixed rule), *secondary* (quoted through a named intermediary), *(confidential)*. Version 1's chapters are archived; their entries below stand as the record of what they cited. Version 2 entries begin at §5.

---

## 1 · How to read a citation in the chapters

| Mark | Meaning |
|---|---|
| **[Axiom]** | A decision Carly has already made, in a house document listed in §2. Cited, never re-argued |
| **[House steer]** | Given by Carly directly in the working session, on the date stated |
| **[Measured]** | A number from a study — the study is in §3 with its link |
| **[Evaluated]** | Assessed systematically but not quantified |
| **[Practice-lore]** | Repeated professional guidance with no primary study behind it — used only when marked |
| **verified** | I fetched the source myself and checked the quoted words against it, on the date stated |
| **agent-fetched** | A research assistant fetched it and extracted the quotes; URL recorded; not independently re-checked unless also marked verified |
| **second-hand** | The original was unreachable; the claim comes via the listed intermediary and says so in the chapter |
| **(confidential)** | Unpublished house material — cited, never reproduced at length; do not quote externally until released |

**"§12" and friends** refer to sections of the Nightlife Culture Style Guide v1.4 — contents:
00 how to use · 01 brand foundation · 02 the method + decision hierarchy · 03 voice and tone ·
04 language and editorial rules · 05 audiences · **06 evidence standard** · 07 colour ·
08 typography · 09 layout · 10 slides · 11 logo · **12 data and charts** · **13 accessibility**
· 14 documents · **15 known gaps** · **16 the seven tests** · 17 do and do not · 18 versions.

---

## 2 · The house corpus — where everything lives on your machine

| Document | Location | Status |
|---|---|---|
| **Nightlife Culture Style Guide v1.4** | `NC_Brand/Style Guide/` (working folder: `Nightlife Culture Design System - Working/`); HTML copy in the Design Standards claude.ai project | Current. The § references above |
| **The Decision Book** — 18 chapters, 347 rules | `~/Documents/GitHub/decision-book/chapters/` | Frozen. Chapters cited so far: 1, 6, 7, 8, 10, 15, 16, 18 |
| **Comparative Place-Based Research Methodology v1.0** + Workbook v2.0 | `Nightlife Culture/Business planning/Competitor analysis /` | Governs where it touches the guide (§06's own precedence rule) |
| **Trusted partner deck** (Aug 2026) | uploaded to session; house copy with NC_Brand materials | The two-columns problem definition (slides 7–8); partnership principles (slide 14); definitions (slide 5) |
| **A Ticket to the Future — feasibility study** (2024) | `A Ticket To The Future - Refresh/` | **Published.** £42m ticket sales; council-approved roadmap |
| **ATTTF Vibe Setting Framework** | `A Ticket To The Future - Refresh/` | **Unpublished — confidential.** Workshops 1–4; *Seeing the System* design questions (pp 31–32); belonging cues and design principles (pp 43–51); 78%/32% appears in its published-facing foreword |
| **ATTTF New 2026 Data draft v2** | `A Ticket To The Future - Refresh/` | **Unpublished — confidential.** £510.9m economic contribution, ~£214m GVA, 3,086 jobs (also stated in VSF foreword) |
| **"On the essence of vibe"** | Obsidian: `Nightlife Culture Biz/Thoughts and ramblings/On the essence of vibe..md` | The co-production theory of vibe; Ch 4's spine |
| **Research questions and ponderings** | Obsidian: `…/Research and project thinkings/Research Questions and ponderings.md` | Lifetime value of a resident DJ; who owns your city's sound |
| **Ticket Atlas** | `~/Documents/GitHub/ticket-atlas-review-2026` | Candidate dataset (fitness unassessed — plan §2b) |
| **Research plan + brief** | this repo, `00-plan/` | BRIEF-v1 governs |

---

## 3 · External sources by chapter

*Every load-bearing external claim in Chapters 1–4. URL, what it supports, and verification
status. Anything used from `raw/RAW-desk-research-notes.md` beyond this list is unverified notes
and is not citable until it graduates to this table.*

### Chapter 1 — The default view

| Source | Supports | Status |
|---|---|---|
| [Aisch, *In defense of interactive graphics*](http://www.vis4.net/blog/in-defense-of-interactive-graphics/) | 10–15% interaction; the 85% misreading; "don't make the user click or hover" | agent-fetched, quotes extracted |
| [Jachimowicz et al. 2019, defaults meta-analysis (PDF)](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/67AF6972CFB52698A60B6BD94B70C2C0/S2398063X1800043Xa.pdf/when-and-why-defaults-influence-decisions-a-meta-analysis-of-default-effects.pdf) | d = 0.68 [0.53–0.83]; 27.24pp; endorsement mechanism | **verified 16 Aug 2026** |
| [Craft & Cairns 2005 (PDF)](https://faculty.cc.gatech.edu/~john.stasko/8001/craft05.pdf) | 52 citations, zero validations of the Mantra; "inspiration and guideline" | **verified 16 Aug 2026** |
| [Shneiderman 1996, *The Eyes Have It* (PDF)](https://hci.stanford.edu/courses/cs448b/papers/shneiderman96eyes.pdf) | mantra wording; "wrote it down as a reminder" | agent-fetched |
| [Hornbæk & Hertzum 2011 (PDF)](http://mortenhertzum.dk/publ/IJHCS2011.pdf) | overviews please reliably, help unreliably; 2/17 error comparisons | agent-fetched |
| [van Ham & Perer 2009 (PDF)](https://perer.org/papers/adamPerer-DOIGraphs-InfoVis2009.pdf) | "search, show context, expand on demand"; case-study evidence only | agent-fetched |
| [Cho et al. 2017, anchoring in visual analytics (PDF)](https://webpages.charlotte.edu/~wdou1/publications/2017/Anchoring_bias_VAST17.pdf) | first-shown view biases exploration and outcomes | agent-fetched |
| [Borkin et al. 2015, *Beyond Memorability*](https://vcg.seas.harvard.edu/publications/20150101-beyond-memorability-visualization-recognition-and-recall) | titles and text carry the message | agent-fetched |
| [ONS, *Say what you see* 2019](https://digitalblog.ons.gov.uk/2019/01/28/say-what-you-see-the-way-we-write-chart-titles-is-changing) | 10-word titles; 9.5× telemetry | agent-fetched |
| [Lindgaard et al. 2006](https://www.tandfonline.com/doi/abs/10.1080/01449290500330448) | appeal stabilises at 50ms (scope: appeal only) | agent-fetched, abstract |
| [Tuch et al. 2012 (PDF)](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38315.pdf) | simplicity + prototypicality drive the snap judgment | agent-fetched |
| [Blascheck et al. 2018 (PDF)](https://www.microsoft.com/en-us/research/wp-content/uploads/2018/08/GlanceableVis-InfoVis2018.pdf) | glance cost varies ~8× by chart form | agent-fetched |
| [Hullman & Diakopoulos 2011 (PDF)](https://users.eecs.northwestern.edu/~jhullman/vis_rhetoric.pdf) | default views as anchored interpretation | agent-fetched |
| [NN/g, empty states](https://www.nngroup.com/articles/empty-state-interface-design/) | craft guidance only; no studies | agent-fetched; practice-lore |
| Display audit, 10 landing pages, 16 Aug 2026 | the six landing patterns | agent-fetched, live pages; Gapminder tools **inferred** (unfetchable); full notes in `02-research-notes/` |

### Chapter 2 — The two columns

| Source | Supports | Status |
|---|---|---|
| Decision Book Ch 16 | "invulnerable to facts…"; never repeat the opposing frame | **house, read directly** |
| Decision Book Ch 6, Ch 7 | gaps as findings; precision as claim; deliberate incompleteness; neutral-to-positive ramp | **house, read directly** |
| [Urban Institute, *Do No Harm Guide*](https://www.urban.org/research/publication/do-no-harm-guide-applying-equity-awareness-in-data-visualization) | reference categories; ordering; deficit framing | agent-fetched; practitioner consensus |
| [Ge, Cui & Kay, *CALVI* (PDF)](https://mucollective.northwestern.edu/files/2023-CALVI.pdf) | 0.39 baseline on misleading items; missing data/normalisation hardest to detect | agent-fetched |

### Chapter 3 — The map

| Source | Supports | Status |
|---|---|---|
| [Ericson, *When Maps Shouldn't Be Maps*](https://www.ericson.net/content/2011/10/when-maps-shouldnt-be-maps/) | "CAN be mapped ≠ MUST be a map" | agent-fetched |
| [Axis Maps, choropleth guide](https://www.axismaps.com/guide/choropleth) | never choropleth counts; enumeration-units rule | agent-fetched |
| [Datawrapper Academy, choropleths](https://academy.datawrapper.de/article/134-what-to-consider-when-creating-choropleth-maps) | normalisation; table instead | agent-fetched |
| [Openshaw 1984, MAUP (PDF)](https://www.uio.no/studier/emner/sv/iss/SGO9010/openshaw1983.pdf) | boundaries change the pattern | agent-fetched |
| [Schiewe 2019](https://link.springer.com/article/10.1007/s42489-019-00026-y) ([open PDF](https://d-nb.info/1208303082/34)) | acreage bias 30–40%/90%; dark-is-more ~90%; legends ignored | agent-fetched |
| [xkcd 1138](https://xkcd.com/1138/) | the population-map trap | agent-fetched |
| [Google Maps Platform, clustering](https://mapsplatform.google.com/resources/blog/how-cluster-map-markers/) | pin cloud and its fix | agent-fetched; vendor practice-lore |
| [LCR venues map](https://lcrmusicboard.co.uk/venues-map/) + [UoL announcement](https://news.liverpool.ac.uk/2022/10/06/were-working-with-liverpool-city-region-to-map-local-music-venues/) | Liverpool audit | **second-hand** — app robots-blocked; audited from host pages |
| [Toronto music map](https://www.toronto.ca/business-economy/industry-sector-support/music/music-directories/music-venues-spaces-studios-stores-map/) | directory pin-map pattern | agent-fetched; widget unrendered |
| Decision Book Ch 10 | the six diagram jobs; Systems Map as containment | **house, read directly** |
| Doughnut Economics (Raworth) | non-geographic map carrying an economic argument | **house reference frame** — named on steer; not independently fetched |

### Chapter 4 — The felt layer

| Source | Supports | Status |
|---|---|---|
| "On the essence of vibe" | co-production theory; arena critique; belonging cues | **house, read directly 16 Aug 2026** |
| Vibe Setting Framework, Workshops 2 & 4 | extraction finding; design questions; belonging definition; cue list; spectrum exercise; design principles 3 & 9 | **house, read directly (confidential)** |
| [Böhme 1993 (PDF)](https://phc.hse.ru/data/2013/12/09/1339377124/Boehme_atmosphere.pdf) | atmospheres are made | agent-fetched |
| [Michels 2015 (open access)](https://gh.copernicus.org/articles/70/255/2015/gh-70-255-2015.pdf) | the three empirical layers | agent-fetched |
| [ISO 12913-1 (sample)](https://cdn.standards.iteh.ai/samples/52161/a6f7669ea47c440593644e959eb4bbe7/ISO-12913-1-2014.pdf) + [ISO/TS 12913-3 (draft sample)](https://cdn.standards.iteh.ai/samples/86955/869167dd32c943e3aca1c73ba5606004/ISO-DTS-12913-3.pdf) | soundscape definition; the circumplex incl. *vibrant*; medians/IQRs | agent-fetched — **note: sample/draft pages, not the purchased standards; buy before publication-grade citation** |
| [Anderson 2009 (PDF)](https://archandphil.wordpress.com/wp-content/uploads/2012/08/andersonbenaffectiveatmospheres.pdf) | singular excess; no method | agent-fetched |
| [Garcia-Mispireta, *Together, Somehow*](https://www.dukeupress.edu/together-somehow) | stranger-intimacy; "vague, fluid, may hide exclusions" | agent-fetched, publisher page |
| [Fetters, Curry & Creswell 2013 (PDF)](https://bpb-us-w2.wpmucdn.com/campuspress.yale.edu/dist/3/2905/files/2022/04/Fetters-Curry-Creswell-Integration-MM-HSR-2013.pdf) | confirmation / expansion / discordance | agent-fetched |
| [Reed et al. 2025](https://journals.sagepub.com/doi/10.1177/13634607231221993) | participatory mapping at n=12; the safety paradox | agent-fetched |
| [Queering the Map (overview)](https://en.wikipedia.org/wiki/Queering_the_Map) | brigaded before moderation existed | agent-fetched, tertiary — primary account not retrieved |
| [Fan-Led Review of Live and Electronic Music](https://publications.parliament.uk/pa/cm5901/cmselect/cmcumeds/1628/report.html) | fan voice as recognised evidence channel; Bristol Nights named | via VSF footnote 8; **link not yet independently fetched — verify before external use** |

---

### Chapter 5 — Comparison without a league table

| Source | Supports | Status |
|---|---|---|
| [Espeland & Sauder 2007, *Rankings and Reactivity* (AJS)](https://www.journals.uchicago.edu/doi/10.1086/517897) | reactivity; mission drift; "devastating" one-tier drop; reverse engineering | agent-fetched (superseded-phase sweep) |
| [CEPR/VoxEU, *The demise of Doing Business*](https://cepr.org/voxeu/columns/demise-doing-business-goodharts-law-action) | improvement can register as failure under relative rank; keep the data, drop the ranking | agent-fetched |
| [JRC statistical audit of the 2025 Global Innovation Index](https://www.wipo.int/web-publications/global-innovation-index-2025/en/appendix-ii-joint-research-centre-jrc-statistical-audit-of-the-2025-global-innovation-index.html) | rank confidence intervals; <10 positions treated as reliable; 21–33-position intervals exist | agent-fetched |
| [EU Cultural & Creative Cities Monitor, Annex A (PDF)](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC117336/citiesmonitor_annexa.pdf) | "for about 80% of the cities… ranks are the result of the underlying data" — one in five are artefacts | agent-fetched |
| [Fattore, Maggino & Colombo, partial orders](https://link.springer.com/chapter/10.1007/978-94-007-3898-0_4) | evaluation without aggregation; preserved incomparability | agent-fetched |
| [Campbell's law](https://en.wikipedia.org/wiki/Campbell%27s_law) · [Goodhart / Strathern](https://en.wikipedia.org/wiki/Goodhart%27s_law) | indicator corruption; note: the famous phrasing is Strathern 1997, not Goodhart | agent-fetched, tertiary |
| [Better Life Index design account](https://truth-and-beauty.net/projects/oecd-better-life-index) — published by the Organisation for Economic Co-operation and Development (OECD) | reader weighting as a collection channel | agent-fetched |
| ONS Explore Local Statistics ([case study](https://analysisfunction.civilservice.gov.uk/case-studies/case-study-launching-explore-local-statistics-service-ons)) | similar-authority clusters; spread displays | agent-fetched (Ch 1 audit) |
| Decision Book Ch 6 | breakout statistics travel furthest → the crop test | **house, read directly** |
| Style Guide §12 + Comparative Methodology v1.0 | the comparability gate, verbatim | **axiom** |
| Vibe Setting Framework | "not about smoothing out the scene, homogenising music experiences" | **house, confidential** |
| House steer 17 Aug 2026 | hyperlocal London point (Croydon/Hackney/Romford vs Farringdon/Enfield); transferable-metric purpose | **house steer** |

### Chapter 6 — The measure on screen

| Source | Supports | Status |
|---|---|---|
| [OECD/JRC Handbook on Constructing Composite Indicators (PDF)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf) | compensability; weights as trade-offs; the (21,1,1,1)=(6,6,6,6) illustration | agent-fetched (superseded-phase sweep) |
| [Ravallion, *Troubling tradeoffs in the Human Development Index*](https://www.sciencedirect.com/science/article/abs/pii/S0304387812000053) | implicit exchange rates — a year of life valued orders of magnitude apart | agent-fetched |
| [Paruolo, Saisana & Saltelli, *Ratings and rankings: voodoo or science?* (JRSS-A)](https://academic.oup.com/jrsssa/article/176/3/609/7075546) | effective vs nominal weights; "little more than cosmetic"; 20%→21% vs 40%→81% | agent-fetched |
| [Creative Footprint — Rotterdam report](https://www.creative-footprint.org/) | part scores 8.58/5.90/5.41 vs 6.10 headline; weights undisclosed | agent-fetched; arithmetic checkable from published numbers |
| [AHRC Cultural Value Project report (PDF)](https://www.ukri.org/wp-content/uploads/2021/11/AHRC-291121-UnderstandingTheValueOfArts-CulturalValueProjectReport.pdf) | "a framework within which sits a variety of components…" — against the single metric | agent-fetched |
| [UNECE work on measuring well-being (dashboards vs composites)](https://unece.org/statistics) | the profile/indicator-set form's standing | agent-fetched, general reference — pin the specific paper before publication-grade citation |
| Raworth, *Doughnut Economics* | the boundary form; non-compensatory display | house reference frame; not independently fetched |
| Decision Book Ch 6 | breakout-statistic discipline | **house, read directly** |
| "Artists Make Great Places" framework | "may also be a decision that a scored index is not useful" | **axiom** |
| House steers 17 Aug 2026 | attribution flip; dynamic census; joy-metric-alongside; university story | **house steer** — see `02-research-notes/use-case-register.md` |

### Chapter 7 — Discovery: finding your tribe

| Source | Supports | Status |
|---|---|---|
| [Every Noise at Once (overview)](https://en.wikipedia.org/wiki/Every_Noise_at_Once) · [McDonald in Significance](https://www.significancemagazine.com/culture/93-every-noise-at-once-using-big-data-to-explore-new-music) | position-as-sound similarity map; Sound of the City; frozen after Dec 2023 layoff — the platform-dependency lesson | agent-fetched |
| [Herlocker, Konstan & Riedl 2000 (PDF)](https://grouplens.org/site-content/uploads/explain-CSCW-20001.pdf) | explanations improve acceptance; histogram winner; 86% wanted them | agent-fetched; measured |
| [Tintarev & Masthoff 2012](https://link.springer.com/article/10.1007/s11257-011-9117-5) | seven explanation aims; personalised explanations liked more, less effective | agent-fetched; measured |
| [Kotkov et al., serendipity survey](https://www.sciencedirect.com/science/article/abs/pii/S0950705116302763) | serendipity evaluation immature | agent-fetched |
| [Reuters Institute filter-bubble review](https://reutersinstitute.politics.ox.ac.uk/echo-chambers-filter-bubbles-and-polarisation-literature-review) | "no support for the filter bubble hypothesis"; news-domain caveat | agent-fetched |
| [Spotify Engineering, algotorial playlists](https://engineering.atspotify.com/2023/04/humans-machines-a-look-behind-spotifys-algotorial-playlists) | human-curated pool, machine-matched delivery | agent-fetched; first-party |
| [Teleport via Smithsonian](https://www.smithsonianmag.com/innovation/where-should-you-live-app-will-tell-you-180962588/) | personal weights, decomposed score, no global rank | agent-fetched; tool defunct |
| [Discover Uni](https://discoveruni.gov.uk/) | state precedent for choice-without-ranking; silent on scene | agent-fetched |
| [360Giving funder guidance](https://www.360giving.org/explore/using-360giving-data-as-a-funder/) | absence-made-visible as underinvestment display | agent-fetched; verbatim |
| [Fairbnb](https://www.positive.news/lifestyle/the-ethical-alternative-to-airbnb-fairbnb/) | discovery revenue returning to the discovered | agent-fetched |
| [Everywhere Is Queer](https://www.goodgoodgood.co/articles/everywhere-is-queer-app) | opt-in self-declaration as consent precedent | agent-fetched |
| House steers 17 Aug (use-case register); community register (confidential); Form 696 sector memory | the kid/jungle/Bristol case; Business Improvement Districts; redistribute question; findability risks | **house** |

### Chapter 8 — Gaps, uncertainty and freshness

| Source | Supports | Status |
|---|---|---|
| [Kay et al., quantile dotplots for transit decisions, CHI 2018 (PDF)](https://www.mjskay.com/papers/chi2018-uncertain-bus-decisions.pdf) | 50-dot quantile dotplots at 97% of optimal (n=408); text intervals unstable | agent-fetched (raw phase); measured |
| [Hullman, Resnick & Adar, hypothetical outcome plots (PDF)](https://idl.cs.washington.edu/files/2015-HOPs-PLOS.pdf) | animated draws beat static forms for multi-variable, lose for single-value on volatile data | agent-fetched; measured |
| [Padilla, Kay & Hullman, uncertainty visualization review (PDF)](http://space.ucmerced.edu/Downloads/publications/Uncertainty_Visualization_Padilla_Kay_Hullman_2022.pdf) | deterministic construal from hard boundaries "persists even with extensive instructions"; no one-size-fits-all | agent-fetched; measured/evaluated |
| [Correll, Moritz & Heer, value-suppressing uncertainty palettes (PDF)](https://www.domoritz.de/papers/2018-VSUPs-CHI.pdf) | behaviour shift, not accuracy; n=24 caveat | agent-fetched; measured, small-n |
| ONS Census 2021 flexible table builder (SDC methodology) | fixed classifications prevent differencing; cell-key perturbation; declared no-cumulative-tracking trade-off | agent-fetched (raw phase) — pin the specific ONS methodology page before publication-grade citation |
| Decision Book Ch 6, 8, 15 | gaps as findings; query-time thresholds; uncertainty through filtering; explained empty states | **house, read directly; axioms** |
| Style Guide §12, §13 | `[c]` marker; range as headline; threshold three; secondary suppression; fixed categories | **axioms** |
| Observatory case (Ch 1) | heartbeat; container vs contents | verified on live pages, 16 Aug 2026 |

### Chapters 9–14 — the overnight run (17 Aug 2026)

*No new external sources were introduced in Chapters 9–14: all claims trace to entries already
in this ledger (Chapters 1–8 sections), to the raw-phase sweeps (marked agent-fetched
throughout), or to house material. New additions for completeness:*

| Source | Supports | Status |
|---|---|---|
| [Boy, Détienne & Fekete, storytelling in information visualisation (preprint PDF)](https://scispace.com/pdf/storytelling-in-information-visualizations-does-it-engage-uf9ih4u2zg.pdf) | the null: no-story explored ~2× longer; 35.4% followed sequence | agent-fetched (raw phase); measured — now load-bearing in Ch 9/10 |
| [Kim, Reinecke & Hullman, *Explaining the Gap* (PDF)](https://users.eecs.northwestern.edu/~jhullman/explaining_the_gap.pdf) | prediction-before-reveal: ~4pp, visual only, unfamiliar only | agent-fetched; measured — Ch 9 |
| [Heer & Robertson, animated transitions (PDF)](https://idl.cs.washington.edu/files/2007-AnimatedTransitions-InfoVis.pdf) | staging helps; over-staging hurts | agent-fetched; measured small-n — Ch 9 |
| [Heer & Shneiderman, interactive dynamics (PDF)](https://idl.cs.washington.edu/files/2012-InteractiveDynamics-CACM.pdf) | the 12-task coverage audit; self-declared unvalidated | agent-fetched — Ch 9 |
| [Segel & Heer, narrative visualisation (PDF)](http://vis.stanford.edu/files/2010-Narrative-InfoVis.pdf) | genres and patterns; no user study | agent-fetched — Ch 10 |
| [Victor, *Explorable Explanations*](http://worrydream.com/ExplorableExplanations/) | interactivity optional | agent-fetched — Ch 10 |
| [ONS Digital, 331 local stories](https://digitalblog.ons.gov.uk/2023/01/27/semi-automation-and-census-2021-how-we-told-331-local-stories-in-one-go/) | semi-automated written narrative at scale | agent-fetched — Ch 10 |
| [Chartability](https://chartability.fizz.studio/) + [EuroVis paper (PDF)](https://www.domoritz.de/papers/2022-Chartability.pdf) | 50 heuristics, 10 critical, 2–8h | agent-fetched — Ch 11 |
| [Zong et al., rich screen-reader experiences](https://vis.csail.mit.edu/pubs/rich-screen-reader-vis-experiences/) + Olli tooling | structure/navigation/description; 13 blind participants | agent-fetched; measured small-n — Ch 11 |
| [Umwelt (MIT News)](https://news.mit.edu/2024/umwelt-enables-interactive-accessible-charts-creation-blind-low-vision-users-0327) | multimodal authoring; 5 participants | agent-fetched — Ch 11, priced as promising |
| [Bateman et al., *Useful Junk?*](https://dl.acm.org/doi/10.1145/1753326.1753716) · [Borkin et al. 2015](https://vcg.seas.harvard.edu/publications/20150101-beyond-memorability-visualization-recognition-and-recall) · [Alebri et al. 2024](https://discovery-pp.ucl.ac.uk/id/eprint/10174581) | the embellishment line | agent-fetched — Ch 13 |
| [Fragapane, *Noise Pollution*, MoMA](https://www.moma.org/collection/works/447623) | the institutional proof | agent-fetched — Ch 13 |
| Gallery entries (Ch 12) | statuses marked per entry in the chapter; re-verify before handbook build | mixed — see chapter |

## 4 · What "truncation" means here, honestly

The chapters compress by design — the Decision Book's template is built on the 60-second version
and rules tables, not literature review. What gets cut is the *narrative of the search*: the
dead ends, the full quotes, the per-study caveats. Three places hold what the chapters don't:

1. **This ledger** — every load-bearing claim, its link, its status. The citable record.
2. **`raw/RAW-desk-research-notes.md`** — the full desk-research returns from the superseded
   phase. Rich, but **unverified**: nothing graduates from there into a chapter without landing
   in this ledger first.
3. **`02-research-notes/`** — per-chapter working notes (the display audit's full per-instrument
   notes should land there; currently summarised in Ch 1 only — logged as a gap).

Rule going forward, added to the working method: **a chapter sprint is not done until its
sources are in this ledger.**


---

## 5 · Version 2 — Chapter 1: What a dashboard is for (5–6 October 2026)

*Full agent returns with every quotation at `02-research-notes/ch01-agent-returns.md`; the sprint record in `RESEARCH-LOG.md`, Entry 1. The chapter's own Sources section carries the grouped list with how each was read; this table is the ledger view. † = abstract only, supports a Fixed rule, on the verification list.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Few 2004, *Dashboard Confusion* (perceptualedge.com PDF) | Reading (practitioner) | At source; spot-checked | The canonical definition; "not a specific type of information or technology" |
| Few 2006 *Common Pitfalls*; 2007 *Confusion Revisited*, *Why Most Dashboards Fail*; 2010 blog | Reading (practitioner) | At source | "say too little"; monitoring vs analysis; situation awareness as Few's own criterion |
| Sarikaya, Correll, Bartram, Tory & Fisher 2019, IEEE TVCG 25(1) | Evidence (corpus, 83) | At source (preprint); verified | Definition in flux; visual vs functional genre; seven clusters; the O'Connell asset→deficit case |
| Bach et al. 2023, IEEE TVCG 29(1) (WRAP open copy) | Evidence (144 dashboards; workshop 23) | At source; verified | Static 21% / analytic 73%; the four-way trade-off |
| Purich et al. 2023, arXiv 2306.16513 | Evidence (25,620 dashboards; preprint) | At source (agent) | Median 8 panels; cross-filter 75%; bar 60% |
| Eckerson 2011, *Performance Dashboards* 2nd ed. | Reading (practitioner) | At source (publisher sample ch. 1) | Layered-system definition; three types; EIS history |
| Velcu-Laitinen & Yigitbasioglu 2012, IJDAR 12 | Evidence (survey, n=145/36) | At source; verified | Dashboards used to communicate more than monitor |
| Yigitbasioglu & Velcu 2012, IJAIS 13(1) | Evidence (review) | Abstract | "little is known about … effectiveness" |
| Kaplan & Norton 1992, HBR | Reading (practitioner) | Secondary — not checked against HBR | The cockpit metaphor |
| Watson, Rainer & Koh 1991, MISQ 15(1) | Evidence (survey, 50 firms) | At source | EIS definition and use |
| Mattern 2015, *Places Journal* | Reading (cultural history) | At source; verified | Etymology; "all the mud" |
| Endsley 1995, Human Factors 37(1); Endsley 2015 restatement | Evidence (theory) | Abstract; definition via 2015 | Three levels of situation awareness |
| Dowding et al. 2015, IJMI 84(2) | Evidence (systematic review, 11) | At source (author MS) | Screen-saver finding; non-use |
| Khairat et al. 2018, JMIR Hum Factors 5(2) | Evidence (integrative review, 17) | PMC full text | Supporting |
| Coiera et al. 2025, JAMIA Open 8(4) | Evidence (systematic review, 70) | PMC full text; verified | Counts for mortality/LOS/harms; "quasi-experimental, mostly before/after" (corrected) |
| Rossi et al. 2025, Implementation Science 20:16 | Reading (position paper) | At source | "28% used it at least once" — one study |
| Verbert et al. 2014, PUC 18 | Evidence (overview) | Abstract; verified | The field's stated promise |
| Jivet et al. 2017 (EC-TEL); 2018 (LAK, preprint) | Evidence (26 dashboards) | 2017 abstract; 2018 at source; verified | Evaluated for satisfaction not purpose; 1 of 13 measured SRL; peer-comparison harm |
| Kaliisa et al. 2024, LAK | Evidence (38 studies) | Author summary † | Achievement negligible; participation moves |
| Matheus, Janssen & Maheshwari 2020, GIQ 37(3) | Evidence (two cases) | Abstract † | Necessary not sufficient; "imposing a pre-defined view" |
| Behn 2007; 2008 (IBM Center; HKS) | Reading (practitioner) | At source | CitiStat: causation unprovable; the meeting |
| Gerrish 2016, PAR 76(1) | Evidence (meta-analysis, 49 studies) | Abstract †; verified | Small average effect; depends on practice |
| Bevan & Hood 2006, Public Administration 84(3) | Evidence | Abstract only | "targets and terror" — typology unread `[Further research]` |
| Barbazza et al. 2022, Digital Health (medRxiv) | Evidence (33 teams) | At source | No public contact; no analytics |
| Sense about Science 2022, *What Counts?* | Evidence (survey) | At source | Dashboard reach 35% |
| Gartner 2023 release; BARC BI Survey 19 | Vendor/analyst | At source | Cited only to show no independent figure exists |
| Dong et al. 2022, Lancet ID 22(12) | Evidence (builders' account) | Full text; verified | Scale; anomaly detection; BI front-ends as obstacle |
| Ivanković et al. 2021, JMIR 23(2) | Evidence (158 dashboards) | Abstract †; spot-checked | 12.7%; seven features |
| UKHSA blogs 2020–2022 (Flowers; Griffiths) | Reading (team account) | At source; spot-checked | 17,000 responses; 90.3%; Downing Street; API; postcode |
| OSR 2021 *State of the Statistical System*; OSR/RSS award 2022 | Standard-setter | At source | API "an exemplar" |
| UKSA *Code of Practice for Statistics* 2.0 (2018), 3.0 (2025) | Standard (binding on official statistics; adopted here) | At source | Trustworthiness · Quality · Value |
| O'Neill 2002, Reith Lectures 3 & 4 (BBC transcripts) | Reading (philosophy) | At source | Transparency ≠ trust; intelligent accountability |
| OSR blog 2021; Spiegelhalter OSR blog 2026 | Standard-setter | At source | "demonstrating trustworthiness" |
| Tennison 2020, ODI | Reading | At source | Trust hierarchy |
| van der Bles et al. 2020, PNAS 117(14) | Evidence (5 experiments, n=5,780) | Abstract †; verified (Cambridge repository) | Numeric uncertainty barely dents trust |
| NatCen/UKSA 2024 *Public Confidence in Official Statistics 2023*; 2015 (2014 wave) | Evidence (national surveys) | At source; verified | 85%/72%/32%; 2014 like-for-like 81%/28% (corrected) |
| Openshaw 1984, CATMOG 38 (Oslo mirror) | Evidence (primary) | At source; verified | MAUP; Iowa 0.34 → ±0.99 |
| Lee, Rogers & Soifer 2025, Political Analysis 33 | Evidence | At source | "wildly unpredictable" |
| Robinson 1950, ASR 15(3) | Evidence (primary) | At source (JSTOR scan); verified | Ecological fallacy; −.619/.118 |
| Subramanian et al. 2009, IJE 38(2) | Evidence | Abstract + summary † | Atomistic fallacy; multilevel |
| Simpson 1951; Julious & Mullee 1994 BMJ; Bickel et al. 1975 Science | Evidence (primary) | At source; Bickel verified | Simpson's paradox; one percentage discrepancy noted |
| OECD/JRC 2008 Handbook (JRC PDF) | Standard | At source; verified | Scale by size; weights are trade-offs; compensability |
| CWTS Leiden *Responsible use* | Standard-setter practice | At source | Size-dependent vs independent |
| Wainer 2007, American Scientist 95(3) | Evidence | At source; spot-checked | De Moivre's equation; both ends of rankings |
| Gelman & Price 1999, Stat Med 18 | Evidence | At source; verified | Shrinkage's opposite bias |
| Goldstein & Spiegelhalter 1996, JRSS A 159(3) | Evidence | At source; verified | Two-thirds inseparable; screening not verdict; CHF gaming |
| ONS Census 2021 SDC; ONS 2024 post-tabular SDC; ONS small-area income 2023; CDC suppression | Standard | At source | 10-5 rule; 14% perturbed; counts below 16; shrinkage toward average |
| Jiang & Rao 2020, ARSIA 7 | Evidence | Abstract | Small-area definition |
| Hawkins 1980 | Evidence (definition) | Secondary | Outlier as different mechanism |
| Tukey 1977 | Reading | Preface verified at two copies | "notice what we never expected" |
| Chandola, Banerjee & Kumar 2009, ACM CSUR 41(3) | Evidence (survey) | Abstract | Anomalies as actionable |
| Pascale & Sternin 2005 HBR; Singhal, Sternin & Durá 2009 | Reading (practitioner) | At source | Positive deviance; 85% self-reported |
| Kitchin, Lauriault & McArdle 2015, RSRS 2(1) (Maynooth MS) | Reading + Evidence | At source; spot-checked | Engine not camera; the design-brief conclusion |
| Kitchin & McArdle 2017; Kitchin, Maalsen & McArdle 2016 | Reading | Preprints at source | Translator not mirror; "dupe them" |
| Porter 1995, *Trust in Numbers* | Reading | Secondary (excerpt compilation) | Technology of distance; weak experts |
| Scott 1998, *Seeing Like a State* | Reading | Introduction at source; verified | Abridged maps; mētis; parasitic on informal |
| Espeland & Stevens 2008, EJS 49(3) | Reading | At source; verified | Commensuration; reactivity |
| Strathern 1997, European Review 5(3) | Reading | At source; spot-checked p. 308 | "measure becomes a target" |
| Goodhart 1975; Campbell 1979 | Reading | Secondary (two sources agree) | Original wordings |
| Muller 2018 (book; Chronicle essay) | Reading | Essay at source; book secondary | Metric fixation |
| Merry 2016, *Seductions of Quantification* | Reading | Introduction at source | Data inertia; expertise inertia |
| Star & Griesemer 1989, SSS 19(3) (uniud.it open copy) | Reading | Original reached; verified pp. 393, 410 | Boundary objects; ideal type |
| Turnhout 2009, Science and Public Policy 36(5) | Evidence | Abstract † | Social achievement, not property |
| D'Ignazio & Klein 2020 *Data Feminism*; D'Ignazio 2024 *Counting Feminicide* | Reading | At source (open access); verified | What gets counted counts; paradox of exposure; counterdata |
| Crossick & Kaszynska 2016 (AHRC); Belfiore 2015, AHHE 14(1) | Reading | At source | Measurement one component of evaluation; "bogus numbers" |
| *Artists Make Great Places* v2.1; BRIEF-v2 | Nightlife Culture | — | The Vibe Map description; the failure register |


## 6 · Version 2 — Chapter 2: Who reads it, and what turns their decision (5–6 October 2026)

*Legend as §5. "At source" — a research agent opened the link on 5 October; "spot-checked" — the orchestrator re-opened it; "verified" — the independent verification pass re-traced it on 5–6 October (fifty-eight items; mismatches corrected in draft 2 and recorded in the research log, Entry 2). † abstract-only. "Secondary" — reached through another named document. A fifth kind, Practice, is used for practitioner frameworks not tested as research; Chapter 0 carries it from its next revision.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| HM Treasury 2026, *The Green Book* (5 Feb 2026; gov.uk HTML + PDF) | Standard | At source; spot-checked; verified | Appraisal; social value; five cases; monetise→quantify→describe; BCR not the decision; distributional analysis; no WELLBY |
| HM Treasury 2022, *The Green Book* (withdrawn; OHE mirror, chs 1–5) | Standard | At source (partial) | The five cases as questions |
| HM Treasury 2021, *Wellbeing Guidance for Appraisal* | Standard | At source; verified | WELLBY; £13,000 [£10k–£16k]; evidence graded by causal design |
| HM Treasury 2025, *Green Book Review 2025* | Standard | At source; verified | BCR < 1 not automatically poor VfM; place-based business cases |
| HM Treasury 2026, *The Magenta Book* (May 2026) | Standard | At source; spot-checked; verified | Monitoring v evaluation (Fig 1.1); counterfactual; four quality criteria; no single hierarchy |
| WWC Local Economic Growth, Maryland SMS page + 2016 scoring guide | Standard | At source; verified | Levels 1–5; SMS 3 minimum |
| Puttick & Ludlow 2013, Nesta *Standards of Evidence* | Standard | At source (two agents); verified | Five levels; L1 a convincing account; L2 change without cause |
| EEF 2023, *Toolkit Guide* v3.0.0 | Standard | At source; verified | Padlocks; cost/strength/size side by side; threats to security |
| Nutley, Powell & Davies 2013, *What counts as good evidence?* | Evidence (review) | At source; spot-checked; verified | Hierarchies critique; Box 6 (Phil Davies 2007) |
| Oliver et al. 2014, BMC HSR 14:2 | Evidence (systematic review, 145) | At source; spot-checked; verified incl. Table 1 | Barriers/facilitators; self-report caveat; "over two thirds" |
| Cairney & Oliver 2017; Cairney & Kwiatkowski 2017; Cairney 2017 ORE | Reading | At source; verified | Two shortcuts; framing; timing; "should not be exaggerated" |
| Weiss 1979, PAR 39(5) | Evidence/Reading | **Secondary** (AcaWiki; NRC 2012) | Enlightenment; political model — flagged |
| Nutley, Walter & Davies 2007, *Using Evidence* | Reading | Abstract + deck † | Research use is meandering; typology flagged |
| Parkhurst 2017, *The Politics of Evidence* | Reading | Partial (T&F page; LSE review); verified | Technical v issue bias; good governance of evidence |
| Kneale et al. 2017, Implementation Science 12:53 | Evidence (scoping review, 21) | At source; verified | Primacy of local evidence; HWB member quotation |
| Kelly et al. 2017, J Public Health 39(4) | Evidence (31 interviews) | At source; spot-checked; verified | "Welcome to democracy"; wards; 95%; 75–85% |
| Woodall et al. 2024, Perspectives in Public Health 146(3) | Evidence (single site) | At source | Four-year cycles |
| Kenny et al. 2017, POST *Role of Research in the UK Parliament* | Evidence (n = 157) | At source; verified | Source credibility first; no sorting by method; charities and timing; 78% |
| Geddes 2018, Parliamentary Affairs 71(2) | Evidence | Abstract † | Who gives evidence |
| IfG 2015 *Evidence Transparency Framework*; Sense about Science 2024 | Practice + Evidence | At source; verified (scale paraphrased) | Four stages; three of six; 74% |
| Kingdon 1984/1995 | Reading | **Secondary** via Mintrom & True 2022 (verified) | Policy window; "special problem well-documented" |
| Sabatier 1988; Jenkins-Smith & Sabatier 1993 | Reading | **Secondary** via Cairney 2015 handbook ch. 33 (verified) | Coalitions; secondary aspects; "learn on their own terms" |
| IfG/Imperial 2020 roundtable | Practice | At source; verified | Relationships; ministerial tone |
| Pandey et al. 2014, IEEE TVCG 20(12) | Evidence (n = 720) | At source; spot-checked; verified | Charts v tables; the reversal |
| Tal & Wansink 2016, PUS 25(1) | Evidence (contested) | Abstract † | "Blinded with science" claim |
| Dragicevic & Jansen 2018, IEEE TVCG 24(1) | Evidence (N = 623) | Project page †; verified | Non-replication; charts aid understanding |
| Markant et al. 2023, CHI | Evidence | Abstract † | Strong priors; belief moves, attitude does not |
| Small, Loewenstein & Slovic 2007, OBHDP 102(2) | Evidence (contested) | At source | $2.83 v $1.17; statistics dampen |
| Jenni & Loewenstein 1997, JRU 14(3) | Evidence | At source | Proportion of reference group |
| Lee & Feeley 2016, Social Influence 11(3) | Evidence (meta-analysis, 41) | Abstract † | r = .05 |
| Maier, Wong & Feldman 2023, Collabra 9(1) | Evidence (preregistered, n = 1,004) | At source; verified | No IVE; publication bias; scope insensitivity |
| Zebregs et al. 2015, Health Communication 30(3) | Evidence (meta-analysis, k = 15) | At source; verified | Statistics→belief; narrative→intention |
| Jones & McBeth 2010; Shanahan et al. 2011, PSJ | Reading (theory) | At source (open copies); verified | Policy narrative definition; "more persuasive than science" thinly sourced |
| Liem, Perin & Wood 2020, CGF 39(3) | Evidence (2 × 300) | At source; verified | < 2% attitude; structure raised threat |
| Boy, Détienne & Fekete 2015, CHI | Evidence | **Secondary** (via Liem; Shao) | Narrative lead-in did not increase exploration — flagged |
| Shao et al. 2024, CHI (arXiv) | Evidence (n = 103) | At source; verified | Storytelling aids comprehension |
| Espeland & Sauder 2007, AJS 113(1) | Evidence (136 interviews) | At source; verified | Reactivity; "artificial lines" (faculty member) |
| Marshall et al. 2000, JAMA 283(14) | Evidence (review) | Abstract † (verification could not re-open) | Consumers rarely use; hospitals respond |
| Metcalfe et al. 2018, Cochrane CD004538 | Evidence (12 studies) | Plain-language summary; verified | Little or no difference to choice |
| Hastings & Weinstein 2008, QJE / NBER 13623 | Evidence (field RCT) | At source; spot-checked; verified | 5–7 points; format added little; timing |
| Engel, Rodden & Tabellini 2022, Science Advances 8(11) | Evidence (n = 1,751) | At source; verified (name and pooled figure corrected) | Count v rate maps |
| Thorpe et al. 2021, JAMA Network Open | Evidence (n = 2,676) | At source; verified | Maps did not improve knowledge; more optimistic |
| van der Bles et al. 2019, RSOS 6 | Evidence | At source (mirror) | Direct v indirect uncertainty; trust |
| Kerr et al. 2023, RSOS 10(11) | Evidence (n = 10,519; 12 countries) | At source; verified | Numeric ranges cheap; vague hedges costly |
| Hullman 2020, IEEE TVCG 26(1) | Evidence (n = 90 + 13) | At source; verified | Why authors omit uncertainty; rhetorical model |
| Joslyn & LeClerc 2012, JEP Applied 18(1) | Evidence | Abstract † | Uncertainty improved decisions |
| Peters et al. 2006, Psych Science 17(5); Kahan et al. 2017, BPP 1(1) | Evidence | Abstract † | Numeracy; motivated numeracy |
| van der Linden, Leiserowitz & Maibach 2019, JEP 62 | Evidence (n = 6,301) | At source; verified | Gateway belief; d = 0.88 → 0.09 |
| Ipsos MORI June 2016; UKSA Norgrove letter 17 Sept 2017 | Evidence; Standard | At source; verified | £350m reach; "clear misuse" |
| Allcott 2011, J Public Econ 95 | Evidence (field RCT, ~600k) | At source; verified | 2%; top decile 6.3% |
| James & Moseley 2014, Public Administration 92(2) | Evidence (field) | Abstract † | Negativity bias; no voice effect |
| Dowding et al. 2015, IJMI 84(2) | Evidence (review) | At source (also Ch 1) | Screen-saver accessibility |
| Centre for Cities 2024, *Cities Outlook*; ONS Subnational Indicators Explorer 2024 | Practice; Standard | At source; verified (counts); pride-in-place grouping unverified | 17 and 38 indicators; nothing cultural |
| MHCLG PPG *Viability*; Social Value Act 2012 s.1; PPN 003 (2025) | Standard | At source; verified | Residual arithmetic; 15–20%; duty to consider |
| National TOMs 2021; HACT Social Value Bank + Fujiwara methodology paper | Practice | At source; verified | Price lists; 88 outcomes |
| Thriving Places Index 2018/2024 | Practice | At source; verified | Refuses the league table |
| Markusen & Gadwa 2010, NEA | Practice/Reading | At source | Definition; attribution caveat p. 16 |
| Markusen 2012/2013, Createquity / IJUS 17(3) | Evidence/Reading | Open copy at source; spot-checked; verified | Fuzzy concepts; proxy data; rewards the successful; live music |
| Gadwa Nicodemus 2013, Cultural Trends 22(3–4) | Evidence | At source (MS); verified | The vibrancy indicators list |
| Moss 2012, Createquity; ArtPlace/Forecast "10 Years" 2014 | Practice | At source; verified | Outcomes problem; the shift away from indicators |
| Jackson, Kabwasa-Green & Herranz 2006, Urban Institute | Evidence/Practice | At source; verified | Cultural vitality; define the construct first |
| Fujiwara, Kudrna & Dolan 2014 (two DCMS reports) | Evidence | At source; verified | Wellbeing valuation; £1,084 etc.; caveats |
| Fields in Trust 2018, *Revaluing Parks* | Evidence/Practice | At source; spot-checked; verified | £974 v £30.24; £34.2bn; not cashable |
| SIRC/Sport England 2020; Sport England release 27 Feb 2025 | Evidence; Practice | At source; verified | 3.28:1; 58% wellbeing; "£4.20 per £1" without caveats |
| BOP Consulting 2014, ACE libraries review | Evidence (review) | At source; verified | "holy grail" |
| Carter / WWC Growth 2014; WWC public realm 2014 | Evidence (review) | At source; verified | "often zero"; property prices; lack of evidence |
| Corry 2018, WWC Wellbeing; Schoemaker 2023, Sustainability 15(6) | Reading; Evidence (review) | At source; verified (Schoemaker framing corrected) | Critique of monetised wellbeing; range across activities |
| DCMS 2021 CHC framework; DCMS 2024/2025 CHC pages | Standard | At source; verified | "implicitly valued at zero"; stock→flow→benefit |
| ACE / Counting What Counts, Impact & Insight; Centre for Cultural Value principles | Practice | At source | Self-defined success; learning over monitoring |
| Gehl Institute 2017 Public Life Data Protocol; PPS Place Diagram | Practice | At source | Counting as evidence; heuristic |
| Impact Frontiers five dimensions; GIIN IRIS+ | Practice | At source; verified | The investor grammar; "importance to people experiencing it" |
| NPC 2013 theory of change; TNLCF evidence principles; Esmée reporting; Inspiring Impact Code 2022 | Practice | At source; verified ("If appropriate" restored) | Funders' asks; the conversation |
| NPC 2012 *Making an impact*; NPC 2013 *Funding impact*; CEP Bolduc 2021 | Evidence (surveys) | At source; spot-checked; verified | 75%; 38%; 42%; 88/89%; ~60% |
| Ebrahim & Rangan 2014, CMR 56(3) | Reading/Evidence | At source; spot-checked; verified | Impact at the level that sees the system |
| Lowe 2013, PMM 33(3); Lowe, Wilson & Boobis 2016 | Reading; Evidence | Abstract †; at source (verified) | Paradox of outcomes; "everybody manipulates" |
| Arvidson et al. 2013, VSR 4(1) | Evidence/Reading | At source (open copy); verified | SROI as credibility device |
| ACE 2023, equality analysis 2023–26 | Standard/Practice | At source; verified | Score then balance portfolio |
| Peters & Roose 2022, Poetics 92; Hug & Aeschbach 2020 | Evidence | Abstract †; at source (verified) | Matthew effect; applicant criteria |
| Impact Investing Institute PBII hub; Better Society Capital | Practice | At source; verified | Narrative first; stakeholder voice |
| Smith-Merry 2020, Evidence & Policy 16(2) | Reading | Abstract + opening † | Validity from context |
| Hill O'Connor & Bennett 2026, Policy & Politics 54(2) | Evidence (three cases) | Authors' summary; verified | Admitted, then re-filed |
| ALLIANCE 2022; Geddes fellowship page 2022 | Practice; Evidence | At source | Lived experience wanted, purpose undefined |
| McIntosh & Wright 2019, JSP 48(3); McLaughlin 2009, BJSW 39(6) | Reading | Abstract † | Assumed authenticity |
| Cousins & Whitmore 1998; Fetterman 1994/2005 | Reading | **Secondary** (BetterEvaluation) | Participatory and empowerment evaluation |
| Charlton 1998, *Nothing About Us Without Us* | Reading | At source; verified | Provenance; control and voice |
| Mahajan et al. 2022, HSSC 9 | Evidence | At source; verified | Co-agree standards and route first |
| Lincoln & Guba 1985 | Reading | **Secondary** (Roller 2021; verified as secondary) | Member checking p. 314 — flagged |
| Birt et al. 2016, QHR 26(13) | Evidence/Reading | Abstract † | "merely a nod"; synthesised member checking |
| BRIEF-v2; *Artists Make Great Places* v2.1 | Nightlife Culture | — | The failure register; the readers; the three groups |


## 7 · Version 2 — Chapter 3: The canonical truths of showing data (6 October 2026)

*Legend as §5. "At source" — a research agent opened the link on 6 October; "spot-checked" — the orchestrator re-opened it; "verified" — the independent verification pass re-traced it on 6 October (fifty-eight items; mismatches corrected in draft 2 and recorded in the research log, Entry 3). † abstract-only. "Secondary" — reached through another named document. "Adjacent domain" — evidence from policy, websites, news articles or health communication rather than dashboards, marked so in the chapter's rules table.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Franconeri, Padilla, Shah, Zacks & Hullman 2021, PSPI 22(3) | Evidence (review) | At source (first two-thirds); publisher summary for the rest; verified | The spine: accurate, efficient, understandable; statistics fast, comparisons slow; schemas; direct labels; 37% (Pew) |
| Cleveland & McGill 1984 JASA; 1985 Science | Evidence (primary) | At source (course copies); verified | The hierarchy as hypothesis; "partly conjectural"; tables if accuracy were all |
| Heer & Bostock 2010 CHI | Evidence (n = 186) | At source; verified | Replication; rectangles ≈ circles; squares worst |
| Talbot, Setlur & Anand 2014 TVCG | Evidence (4 × 50) | At source; verified (7.38 corrected to absolute error) | Why bar types differ; readers round to 10s and 5s |
| Kosara & Skau 2016; Skau & Kosara 2016; Kosara 2019 | Evidence (~100 each) | At source; verified | Pies read by area, not angle; donuts no worse |
| Davis et al. 2022 TVCG | Evidence (109; 130,800 judgements) | At source; verified | Individual differences exceed chart-type gaps; ~22% share the canonical order |
| Healey & Enns 2012 TVCG; Healey web overview; Treisman & Gelade 1980 | Evidence | At source; verified | Preattentive 200–250 ms; conjunctions; feature hierarchies; hue masks shape |
| Wagemans et al. 2012 Psych Bull | Evidence (review) | At source (author MS copy) | Gestalt vocabulary |
| ColorBrewer schemes page; Harrower & Brewer 2003 | Practice | At source; abstract † | Sequential / diverging / qualitative |
| Borland & Taylor 2007 via Moreland 2016 | Reading | Secondary (Moreland at source) | The rainbow objections |
| Liu & Heer 2018 CHI | Evidence (166) | At source; verified | Jet worst; viridis family best; naming + perceptual space |
| Reda, Nalawade & Ansah-Koi 2018 CHI | Evidence (381) | At source; verified | Rainbow best for reading a value; diverging for pattern |
| Birch 2012 JOSA A | Evidence | Abstract † | 8% men / 0.4% women (European descent) |
| Healey 1996 | Evidence (38) | At source; verified | Seven colours for rapid search |
| Szafir 2018 TVCG | Evidence (461) | At source; verified (draft 1 figure and direction corrected) | Small marks need bigger colour differences; lines more discriminable than points |
| Lin et al. 2013 CGF | Evidence (144) | At source | Semantic colours ~10% faster |
| WCAG 2.2 (Rec. 12 Dec 2024) SC 1.1.1, 1.3.1, 1.4.1, 1.4.3, 1.4.4, 1.4.10, 1.4.11, 2.1.1, 2.5.8, 3.1.5; Understanding pages | Standard | At source; verified | The hard lines; 1.4.11's chart examples; AAA note |
| Government Analysis Function — charts (2022), checklist (2023), colours; ONS Service Manual — chart text, colours | Standard (voluntary) | At source; verified (colour wording corrected; checklist's truncation line found) | No legends; four lines; pies ≤5; bars from zero; data download; 5/9 colours; 15-word titles |
| Borkin et al. 2016 TVCG (Beyond Memorability) | Evidence (33; 393) | At source; verified | Title first and longest; 46% recall the title; message redundancy |
| Matzen et al. 2017 (Sandia/HCII) | Evidence | At source; verified | 87.8% title in first three fixations; text 60% of fixations in memory task |
| Yang, Hou, Li, Chang & Zeng 2025 TVCG (Dashboard Vision) | Evidence (60; 1,216 dashboards) | At source; spot-checked; verified | Text attention out of proportion to area; numbers most looked-at; subtitles > titles; upper-left |
| Sultanum & Setlur 2026 arXiv | Evidence (preprint; self-report) | At source | Colour only — reading flows start at the title |
| Kong, Liu & Karahalios 2018 CHI; 2019 CHI | Evidence (111/104; 200; nationally representative) | At source; spot-checked; verified | Title decides the message; 80% "neutral"; trust data > chart > title |
| Kim, Setlur & Agrawala 2021 CHI | Evidence (2,168) | At source; verified | Captions redirect only to salient features |
| Stokes et al. 2023 TVCG; Stokes & Hearst 2021 | Evidence (302); Reading | At source; spot-checked; verified ("sizable" restored) | More text preferred; title-only lowest; trend in title |
| ONS Digital blog 2019 "Say what you see"; ONS Service Manual chart text | Practice | At source; verified | Message titles; 9.5× line; no study named |
| Huestegge & Philipp 2011 AP&P | Evidence (small lab) | At source; verified | Legend round trips 4.37 v 3.63 |
| Ginns 2006 Learning and Instruction | Evidence (meta-analysis, 50) | At source; verified (0.78 clause removed) | Spatial contiguity d = 0.72 |
| Few (Perceptual Edge pages); EU data-visualisation guide | Practice | At source | Direct labelling as craft |
| Lindgaard et al. 2006 BIT; 2011 TOCHI | Evidence (22/31/40; adjacent domain) | At source (mirror); abstract † | 50 ms appeal |
| Tuch et al. 2012 IJHCS | Evidence (59; 82; adjacent domain) | At source; verified (120 sites) | Complexity and prototypicality |
| Blascheck et al. 2019 TVCG | Evidence (36; smartwatch) | At source; verified | Bar/donut ~250 ms; radial ~1,600 ms |
| Bera 2016 CACM | Evidence (30) | At source | Colour misuse slows decisions |
| Nielsen Norman Group — Pernice 2017; Nielsen 2008; Kendrick 2019 | Practice | At source; verified (F-pattern wording restored) | The F is a failure mode; 20–28% read |
| Tufte 1983/2001 | Practice | Secondary (standard reproductions) | Data-ink; chartjunk |
| Bateman et al. 2010 CHI | Evidence (20; 10) | At source; verified | The study that started the argument |
| Few 2011 "The Chartjunk Debate" | Practice | At source; verified | "plain ugly" |
| Borkin et al. 2013 TVCG | Evidence (261; 2,070) | At source; verified | Memorability ≠ comprehension; common charts least memorable |
| Haroz, Kosara & Franconeri 2015 CHI | Evidence (5 experiments) | At source; verified | Pictographs as data free; background images distract |
| Skau, Harrison & Kosara 2015 CGF | Evidence (~94) | At source; verified (quotation restored) | Styled bars raise error |
| Borgo et al. 2012 TVCG; Inbar et al. 2007 | Evidence | Abstract † | Memory up, search slower; people prefer chartjunk |
| Ajani et al. 2022 TVCG | Evidence (24; unreplicated) | At source; verified | Declutter → professional; focus → recall; trust unmoved |
| Correll, Bertini & Franconeri 2020 CHI | Evidence (40/32/25) | At source (arXiv); spot-checked; verified (Exp 2 p = 0.05 added) | Truncation exaggerates; label does not help |
| Yang, B.W. et al. 2021 JARMAC | Evidence (5 studies) | Abstract † | Persisted after teaching; 83.5% |
| Long & Kay 2024 CHI | Evidence (122) | At source; verified | Objective accuracy often unaffected |
| Isenberg et al. 2011 TVCG | Evidence (15) — dual-scale | At source; verified | Not about dual-axis charts |
| ONS 2019 "Dueling with axis"; Brath, Hagerman & Sorenson 2022 | Practice | At source; abstract | Dual axes untested; 19% of 944 |
| Zacks, Levy, Tversky & Schiano 1998 JEP:A | Evidence (200) | At source; verified | 3D cost small; neighbours ten times larger |
| Romano et al. 2020 Health Economics | Evidence (~2,000) | Abstract + authors' LSE post † | Log 40.66% v linear 83.79% |
| Reinholtz, Maglio & Spiller 2021 JEP:A | Evidence (596; preregistered) | At source; verified | Stock v flow d = 0.74 |
| Heer & Agrawala 2006 TVCG | Reading | At source | Colour only — banking to 45° |
| Vessey 1991; Vessey & Galletta 1991 via Braithwaite & Goldstone 2013 | Reading; Evidence | Abstract †; secondary (Frontiers at source) | Cognitive fit |
| Ehrenberg 1977 JRSS A; Kozak et al. 2011; UW-Madison tables bibliography; Cole 2015 ADC | Practice | Abstract †; secondary; at source | Two or three effective digits; "asserted without experimental results" |
| Jerez-Fernandez et al. 2014; Zhang & Schwarz 2012; Xie & Kronrod 2012 | Evidence | Secondary / abstract † | Precision as confidence cue |
| Gigerenzer & Hoffrage 1995; McDowell & Jacobs 2017 via Weber et al. 2018; Gigerenzer 2011 BMJ; Gigerenzer et al. 2007 PSPI | Evidence | At source; abstract †; at source; at source; verified | Natural frequencies; 24% v 4%; 21% → 87% |
| Javed, McDonnel & Elmqvist 2010 TVCG | Evidence (16) | At source; verified | Overlay for local, split for dispersed |
| Tse 2016 Malofiej slides; Nieman Lab 2016 | Practice | At source (PDF extracted); verified — no percentage | The three rules |
| Aisch 2017 vis4.net; Baur 2017; Hohman et al. 2020 Distill | Practice | At source; verified | The footnote; 85% was a button |
| Conlen, Kale & Heer 2019 CGF | Evidence (tens of thousands of sessions; adjacent domain) | At source; verified (reach-to-end corrected) | 85%/54%/median zero; mobile |
| Boy et al. 2015 CHI; Boy et al. 2016 TVCG | Evidence | Secondary (Tong et al.); abstract † | No extra exploration; cues mostly fail |
| Feng et al. 2017 HindSight; Feng et al. 2019 | Evidence (>400) | At source | 5.4 of 20; 20.7 of 255 |
| Dimara & Perin 2020 TVCG; Dimara et al. 2020 TVCG | Reading | At source | Definition; bias taxonomy |
| Jachimowicz, Duncan, Weber & Johnson 2019 BPP | Evidence (58 datasets, 55 studies, 73,675; adjacent domain) | At source (both copies); spot-checked; verified — sentence present | Default d = 0.68; 27.24; endorsement |
| Cho et al. 2017 VAST | Evidence (81) | At source; verified | Visual and numeric anchors |
| Valdez, Ziefle & Sedlmair 2018 TVCG | Evidence (726) | At source; verified | Priming |
| Xiong, van Weelden & Franconeri 2020 TVCG | Evidence (small) | At source; verified | Curse of knowledge |
| Hullman & Diakopoulos 2011 TVCG | Reading | At source; verified | Default views anchor interpretation |
| Shneiderman 1996 | Practice/Reading | At source; verified | "a reminder"; "a starting point" |
| Craft & Cairns 2005 IV | Evidence (citation audit) | At source; verified | 52 citations, no validations |
| Hornbæk & Hertzum 2011 IJHCS | Evidence (review, 60 papers) | At source; spot-checked; verified | 23 comparisons; 2 of 17 |
| van Ham & Perer 2009 TVCG | Reading (case studies) | At source; verified | The counter-mantra |
| Tversky, Morrison & Bétrancourt 2002 IJHCS | Evidence (review) | At source; verified | Apprehension principle |
| Robertson et al. 2008 TVCG | Evidence (36) | At source; verified | Animation enjoyed, inaccurate; small multiples |
| Heer & Robertson 2007 TVCG | Evidence (24) | At source; verified | Transitions help |
| Brehmer, Lee, Isenberg & Choe 2019 TVCG | Evidence (96) | At source (arXiv); verified | Small multiples faster on phones |
| McKenna et al. 2017 CGF | Evidence (240) | At source; verified | Engagement up; comprehension flat |
| Gapminder pages | Practice | At source (tool itself unreachable) | Default bubble chart described |
| Padilla, Kay & Hullman 2021 (Wiley StatsRef) | Evidence (review) | At source (author preprint); verified (frequency sentence re-attributed) | Taxonomy; the named misreadings |
| Hullman, Resnick & Adar 2015 PLOS ONE | Evidence (288) | At source; verified | HOPs |
| Kay, Kola, Hullman & Munson 2016 CHI | Evidence (~540) | At source; verified | Quantile dotplots ~1.15× |
| Correll & Gleicher 2014 TVCG | Evidence | At source; verified | Within-the-bar bias |
| Hofman, Goldstein & Hullman 2020 CHI | Evidence (1,743; 1,830; adjacent domain) | At source; spot-checked; verified | CI v PI: 86/67/57 |
| Padilla, Ruginski & Creem-Regehr 2017 CRPI | Evidence | At source; verified (cone wording restored) | Boundaries as categories and size |
| Belia, Fidler, Williams & Cumming 2005 Psych Methods | Evidence (473) | At source; verified | Researchers misread error bars |
| Budescu et al. 2014 NCC; 2012 Climatic Change | Evidence (24 countries) | At source; abstract † | "Likely" read toward 50% |
| Wintle et al. 2019 PLOS ONE | Evidence (924) | At source; verified | 32% → 66% with the number bracketed |
| Spiegelhalter 2017 ARSIA | Evidence (review) | At source; verified | The recommendations |
| Markant et al. 2023 CHI (arXiv) | Evidence (331) | At source; verified | Uncertainty may harden the opposed; authors' caveat |
| MacEachren et al. 2012 TVCG; Kinkeldey et al. 2014; 2017 | Evidence (experts) | At source; abstract †; secondary | Fuzziness/value/location read as uncertain |
| Akl et al. 2011 Cochrane | Evidence (35 studies) | At source (summary); verified | RRR persuades without informing |
| Pighin et al. 2011 MDM | Evidence (7 experiments) | Abstract † | 1-in-X; icon array cures it |
| Garcia-Retamero & Cokely 2017 Human Factors; 2013 CDPS; Okan et al. 2012; Galesic et al. 2009 | Evidence (36 studies; 27,885) | At source; abstract †; abstract †; secondary | Icon arrays; heuristics; who they help |
| Fagerlin, Zikmund-Fisher & Ubel 2011 JNCI | Evidence (consensus) | At source (PMC); partly verified (headings) | Ten steps |
| Galesic & Garcia-Retamero 2011 MDM | Evidence (495; 492) | Abstract † | ~9 of 13; one third both low |
| Börner et al. 2016 Information Visualization | Evidence (273) | At source; verified | 14% technical label; <50% partially accurate |
| Lee, Kim & Kwon 2017 TVCG (VLAT) | Evidence (191) | At source; verified | About half of 53 items |
| DfE PIAAC 2023 National Report for England; OECD GPS | Standard (official) | At source; verified | 21% Level 1 or below; 268 v 263 |
| National Numeracy page; OSR *Statistical literacy research* p. 4 | Standard (official) | At source; verified — draft 1 quotation did not exist, corrected | 49.1% Entry Level 3 or below (2011); no survey captures statistical literacy |
| Shah & Hoeffner 2002 EPR | Evidence (review) | Abstract † | Colour only |
| WAI-ARIA 1.2; Graphics-ARIA 1.0; W3C wiki chart roles 2015; Accessible Infographics CG | Standard (spec) / abandoned proposal | At source; verified | No chart role; graphics-document |
| WAI Tutorials — Complex Images | Guidance | At source; verified | Two-part text alternative |
| COGA Working Group Note 2021 | Guidance | At source; verified | "not required for conformance"; numerical patterns |
| EU WAD FAQ on EN 301 549 | Standard (European) | At source | Relationship to WCAG |
| PSBAR 2018 regs 4, 6; GOV.UK accessibility requirements; Service Manual | Standard (law; guidance) | At source; verified (exemption wording attributed correctly) | Who is bound |
| Equality Act 2010 s.20; Explanatory Notes Sch 2 | Standard (law) | At source; verified | Anticipatory duty; accessible format |
| The Decision Book Ch 6, Ch 7; Style Guide v1.5 | Nightlife Culture | Read directly (skill) | The axioms tested in Looking back |
| BRIEF-v2; version 1 Chapter 1 (archived) | Nightlife Culture | — | The failure register; defaults/glance evidence re-verified |


## 8 · Version 2 — Chapter 4: From data to evidence (6 October 2026)

*Legend as §5. "At source" — a research agent opened the link on 6 October; "spot-checked" — the orchestrator re-opened it (thirteen items, all held); "verified" — the independent verification pass re-traced it on 6 October (ninety-five items; mismatches corrected in draft 2 and recorded in the research log, Entry 4). † abstract-only. "Secondary" — reached through another named document. "Adjacent domain" — evidence or standards from medicine, psychology, price indices or financial reporting rather than public displays, marked so in the chapter's rules table. "Colour" — illustration only, carrying no rule.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| OSR 2023, *Quality and statistics: an OSR perspective* | Standard (regulator) | At source; verified (one paraphrase restored to source wording) | "bear the weight of the decisions"; quality definition; users' testimony on prominent, succinct quality information |
| HM Treasury 2015, *The Aqua Book* (archived PDF) | Standard | At source; verified | Verification v validation (§6.3); four principles; RIGOUR |
| Analysis Function et al. 2025, *The AQuA Book* (GOV.UK, 30 July 2025) | Standard | At source; verified | Four roles; proportionality; assumptions log; black boxes |
| HM Treasury 2013, Macpherson review (final; interim) | Standard | At source; verified (parenthetical restored) | Single SRO; inputs, methodology and outputs; business-critical test |
| NAO 2012, *Lessons from cancelling the InterCity West Coast franchise competition* | Evidence (audit) | At source; verified | Purpose drift: "received no extra quality assurance once the Department decided to use it" |
| Wang & Strong 1996 JMIS 12(4) | Evidence (two surveys, n = 137 and 355) | At source (MIT copy); verified (survey stages corrected) | "fit for use by data consumers"; twenty dimensions; believability and reputation as intrinsic |
| Pipino, Lee & Wang 2002 CACM; Batini et al. 2009 ACM CSUR | Evidence | At source | Colour: subjective v objective assessment; currency/volatility/timeliness |
| Government Data Quality Framework 2020 | Standard | At source | Six DAMA dimensions; five principles; timeliness relative to the period represented |
| Regulation (EC) No 223/2009, Art. 12 | Standard (law) | At source; verified | Accuracy, timeliness, comparability (three axes), coherence definitions |
| European Statistics Code of Practice 2017, P12–P15 | Standard | At source; verified (14.2–14.4) | Comparability indicators; metadata |
| Eurostat 2020 *ESS handbook for quality and metadata reports* | Standard | At source | Reliability filed under data revision |
| GSS 2019 *Quality statistics in government* | Standard | At source; verified | Reliability = "closeness of early estimates to subsequent estimated values"; UK dimension wording |
| Code of Practice for Statistics 3.0 (3 Nov 2025) — pages 1, 3–7; transition guidance; summary of changes | Standard | At source; spot-checked (Std 6, 7; 3.9, 4.5, 6.6, 6.7, 7.2, 7.4, 7.5); verified (all quoted practices; Standards for Public Use; date) | Standards 3, 4, 6, 7, 9, 10; Standards for Public Use; the provenance list |
| Code of Practice 2.0/2.1 (2018/2022), Q1–Q3 | Standard (historical) | Secondary (Analysis Function and OSR pages reproduce the text) | Chapter 1's citation mapped to Standards 6 and 7 |
| OSR 2025, TQV Voluntary Application guidance; Voluntary Application page | Standard | At source; verified (on the guidance page) | Self-published TQV statement; "no formal role"; "informal and advisory" |
| ONS, *Guide to statistical revisions*; *Revisions policies for economic statistics* | Standard | At source; verified | Revisions v corrections |
| ONS 2025, *GDP revisions in Blue Book 2025* | Evidence (official) | At source; verified (0.66pp caveat restored) | MAR 0.2pp (t+3), 0.5pp (t+36); 0.7 from 2020; the trade-off sentence |
| OSR 2023, *Revisions of estimates of UK GDP* | Standard (regulator) | At source; verified (truncation restored) | "normal and unavoidable"; "in a central place" |
| MHCLG statistics revisions policy | Standard | At source | Colour: scheduled v unscheduled |
| Federal Reserve Bank of St. Louis, ALFRED; Philadelphia Fed real-time dataset | Practice | At source; verified (ALFRED) | Vintages |
| W3C PROV-DM 2013 | Standard | At source; verified | Entity / activity / agent; derivation; attribution |
| W3C DCAT 3 (22 Aug 2024) | Standard | At source; verified except *dct:temporal* (paraphrased; absent-value note restored to source) | Three dates; closed interval; versioning |
| Wilkinson et al. 2016 *Sci Data*; GO FAIR principles | Standard (community) | At source; verified | R1.2; A2 |
| schema.org Dataset | Standard | At source | Colour |
| Analysis Function 2018, *Communicating quality, uncertainty and change* | Standard | At source; verified | Adjustments incl. imputation; imputation rates; "not hidden away in … footnotes" |
| Rubin 1976 *Biometrika* | Evidence (foundational) | Abstract † (DASH) | "ignore the process that causes missing data" |
| Schafer & Graham 2002 *Psych Methods* | Evidence (review; adjacent domain) | At source (ETH copy); verified | Case deletion the default; ad hoc edits; MI |
| Sterne et al. 2009 *BMJ* | Evidence (adjacent domain) | At source; verified | Plain MCAR/MAR/MNAR; untestable; report differences |
| NRC 2010, ch. 4 | Standard/Evidence (adjacent domain) | At source; verified | Unverifiable mechanism; sensitivity analysis |
| Bell et al. 2014 *BMC Med Res Methodol* | Evidence (one review; adjacent domain) | At source; verified | 45% complete-case; 8% MI; 35% sensitivity |
| Hand 2020 *Dark Data* ch. 1 (publisher sample); Hand 2020 *Significance* 17(3) | Evidence/Practice | At source; verified (Sandy truncation restored) | Fifteen DD-Types; definition; potholes; Sandy; Challenger's missing zeros |
| Codd 1986 *SIGMOD Record* 15(4) | Evidence/Standard (foundational) | At source; spot-checked | A-mark / I-mark; marks not values; zero "far too valuable" |
| Console, Guagliardo & Libkin 2019 IJCAI | Evidence (history) | At source | Colour: Kleene logic; Codd 1987 4VL |
| Darwen 2012, CS319 slides | Practice | At source; verified | SUM(X)+SUM(Y) ≠ SUM(X+Y); one table per meaning |
| SQL-92 draft §3.1.3, §4.1 | Standard | At source; verified | "effectively only one null value" |
| PostgreSQL 18 docs (comparison; aggregate) | Standard (manual) | At source; verified | NULL semantics; aggregates skip nulls; `coalesce(sum(x),0)` |
| R base docs, *NA* | Standard (manual) | At source | Colour |
| Analysis Function 2022, *Using symbols and shorthand in tables* | Standard | At source; spot-checked; verified | The codes; true-zero rule; No to NA; no symbols |
| Analysis Function 2021, *Releasing statistics in spreadsheets* — "Cells with no data" | Standard | At source; spot-checked; verified | The one-reason blank rule |
| Analysis Function 2022, *Data visualisation: charts* — "Breaks in time series" | Standard | At source; spot-checked | "do not join the points … even if the line is dotted or dashed" |
| Analysis Function 2026, *An introduction to SDC* | Standard | At source; verified | Primary and secondary suppression; "c" |
| SDMX CL_OBS_STATUS 2.2; CL_CONF_STATUS 1.4 (registry JSON) | Standard | At source; verified | O/M/L/Q/H/N/K/W/E/I; confidentiality reasons |
| Eurostat database flags page; Statistics Explained *Tutorial: Symbols and abbreviations* | Standard | At source; verified | 0 / 0n / : / - / c; "Never use NA or ND"; never blank; don't overload |
| ABS 2005, *Australian Social Trends* symbols | Standard (historical) | At source | Colour: one dash for three kinds; "n.y.a." |
| CDC NNDSS weekly data legend; MMWR 64(22) 2015 | Standard | At source; verified (N truncation restored) | U / - / N / NN / NP / NC; the dash is not zero |
| Understanding Society, *Missing values* | Standard (survey documentation) | At source; verified (chapter's label unquoted) | Nine negative codes |
| CMU 36-402 note, "Fixed and Random Zeroes" | Practice (teaching note) | At source | Structural v sampling zero |
| ONS 2026, *Special case aggregates in consumer prices* | Standard (adjacent domain — price indices) | At source; spot-checked | Free = "zero price but with non-zero quantity" |
| Brynjolfsson et al. 2019 NBER 25695 | Evidence | Abstract † | Colour: GDP-B |
| NCES 2002 Standard 4-1 | Standard | At source; verified | Imputed values flagged with method; weighted proportion |
| ASA 2022 *Ethical Guidelines* | Standard (professional) | At source; verified | "including missing data handling" |
| PHE 2020 statement on delayed reporting | Evidence (official statement) | At source; verified | 15,841; file-size limit (not "Excel") |
| CDC NCHS provisional death counts, technical notes | Standard | At source; verified | 65/85/95% completeness |
| ONS 2023, *Protecting personal data in Census 2021 results* | Standard | At source; verified | Swapping; perturbation; "cell count of one" |
| Wickham 2014 *JSS* 59(10) | Evidence/Practice (canonical) | At source; spot-checked | Three rules; "surprisingly difficult" |
| Eurostat glossary: statistical / observation / reporting unit; enterprise; reference period; calendar adjustment | Standard | At source; verified | Three units; reference v publication time; calendar effect |
| Council Regulation (EEC) 696/93, Annex | Standard (law) | At source; verified (eight units) | Enterprise, local unit, group; preamble on comparability |
| Bhattacherjee, *Social Science Research* §2.1 | Practice (textbook) | At source | Unit of analysis v unit of collection |
| GSS 2017, *Survey reference period* v5.6 | Standard | At source | Financial-year harmonisation |
| NHS England KH03 definitions (2020; 2023); NHS Data Dictionary 2015 | Standard | At source; verified | Midnight occupancy; day-ward cap |
| Pierce et al. 2024 *J Hosp Med* (online Nov 2023) | Evidence (adjacent domain) | Secondary (Today's Hospitalist Jan 2024; The Hospitalist Aug 2024); verified at the trade-press source | Midnight understates; 11 a.m. peak; 9.1 patients, 5.5% |
| Simon et al. 2011 *IJNS* 48(1) | Evidence (adjacent domain) | Abstract † | Two of five methods underestimate; up to 7.6% |
| FINRA, settlement cycles (2026); SEC T+3 (historic) | Standard/Practice | At source; verified | Trade v settlement date; T+1 |
| GOV.UK, *Date-times and time stamps standard* (2026 update); ISO 8601 page | Standard | At source; verified | Descending order; sort by filename; UTC offset; 01/05/22 |
| ONS 2023, *The night-time economy, UK: 2022* | Standard (definition only) | At source; verified | 6pm–6am window — no further use |
| Datta, Knox & Bronnenberg 2018 *Marketing Science* | Evidence | Abstract † | Individual-grain diversification |
| CDC, *Principles of Epidemiology* 3rd ed., Lesson 3 §1–2 | Standard (teaching text) | At source; verified | Ratio / proportion / rate; population at risk; person-time |
| Tufte 1997 *Visual Explanations* ch. 2 | Practice + documentary cases | At source (library copy); verified; one near-verbatim sentence not used | Snow's unpopulated areas; Challenger's 92% missing |
| Hájek 2007 *Synthese* | Reading (philosophy) | Abstract † | The reference class problem |
| Tesco PLC, Preliminary Results 2025/26, fn 3 | Practice (corporate reporting; adjacent domain) | At source; verified | LFL definition; 52 weeks "to aid comparability" |
| Gelman & Price 1999 *Stat Med* | Evidence | At source; spot-checked | Both tails; shrinkage flips the artefact |
| Spiegelhalter 2005 *Stat Med* | Evidence | Abstract fragments † | Funnel plots v league tables |
| PHE Fingertips, confidence intervals guidance | Standard | At source; verified | Intervals "particularly important … when numbers are small" |
| SDMX Glossary v2.1 (2020), citing SIMS 2014 | Standard | At source; verified | Comparability = attributable to true values |
| Eurostat SIMS 2.0 (2015); Quality Grading System | Standard | At source; verified (grading) | CC1/CC2; data points since last break |
| OSR 2025, *Adequacy of UK-wide comparable statistics* §3 | Standard (regulator) | At source; verified (wording restored) | "meaningful comparability" |
| Eurostat, LFS correction for breaks | Standard | At source; verified (wording restored) | Break-free series or correction factors; "h" |
| GSS Geography Policy — best-fit; names and codes (NRS copies); ONS CHD page; ONS geospatial training; ONS administrative geography | Standard | At source; verified (one CHD sentence unlocated and unquoted) | Building blocks; best-fit; codes not re-used; "use the correct year"; reorganisation years |
| Analysis Function, GSS harmonisation pages | Standard | At source; verified | "users may come to incorrect conclusions"; harmonised topics |
| ESMA 2015/1415, APM guidelines ¶20, 26, 37, 41 | Standard (financial regulation; adjacent domain) | At source; verified | Define; reconcile; comparators; constant; restate |
| CIPFA Nearest Neighbours page | Practice | At source; verified | "40 metrics"; "results and common sense"; "relies on the indicators" |
| PHE 2016, *Comparators Briefing — technical* | Practice/Standard | At source; verified | Euclidean distance; IMD 22.5% circularity; region/national "may not indicate performance" |
| DfE 2025, children's services statistical neighbour technical report | Practice (published method) | At source; verified | 23 variables; weighted Euclidean; ten neighbours |
| ONS 2011 Area Classifications methodology | Practice/Standard | At source; verified | K-means; 60 variables; 8/24 |
| LG Inform comparison groups | Practice | At source | Colour |
| Lorenz 1905 *PASA* 9(70) | Evidence (foundational) | At source (Internet Archive OCR); verified | The curve; "average income is no safe criterion" |
| World Bank WDI metadata: Gini; top-decile share | Standard | At source; verified | Definitions |
| US DoJ, Herfindahl-Hirschman Index (2024) | Standard | At source; verified | Formula; 2,600; 1,800 |
| NIST/SEMATECH e-Handbook §1.3.5.1 | Standard | At source; verified | Mean distorted, median not |
| ONS 2017, ASHE interpretation guide §4 | Standard | At source; verified | Why the median |
| Juran 1975 "The Non-Pareto Principle; Mea Culpa" | Practice (historical) | Secondary (blog reproduction) | Misnamed; curves belong to Lorenz |
| Juran Institute 2019/2024, Pareto guide | Practice | At source; verified | Pareto 1895; "vital few" |
| Rosen 1981 *AER* 71(5) | Evidence (theory) | At source (scholar-hosted scan); verified | Imperfect substitution; joint consumption |
| Salganik, Dodds & Watts 2006 *Science* 311 | Evidence (n = 14,341) | At source (co-author copy); spot-checked | Social influence → inequality and unpredictability; Gini |
| Anderson 2004/2006 *The Long Tail* | — | Not read; not quoted | — |
| Elberse 2008 *HBR* | Evidence (industry data) | Secondary (reprint); spot-checked against the reprint | 78%/32%; 24% one copy; 91% under 100; "A few winners" |
| Coelho & Mendes 2019 *JBR* | — | Abstract † (result not stated) | Not used for any figure |
| Aguiar & Waldfogel 2015 NBER 21653 | Evidence | Abstract at source | "top 50 songs" coverage caveat |
| Nightlife Culture ticketing analysis — 78%/32% | Nightlife Culture | Not researched | The worked case; now stated as undefined until unit, period and base are supplied |
| Meng 2018 *AoAS* 12(2) | Evidence | At source (Harvard copy); spot-checked | Quality × quantity × difficulty; 2.3m ≈ 400; "the more the data" |
| Lazer, Kennedy, King & Vespignani 2014 *Science* 343 | Evidence | Abstract at source (DASH); body secondary (two agreeing teaching copies) | Big data hubris; algorithm dynamics; "not the output of instruments designed…" |
| Salganik 2018 *Bit by Bit* §2.3 (open edition) | Practice (textbook) + cited Evidence | At source; verified (grouping labels restored) | Ten characteristics; 20 friends; the pager |
| Kitchin & McArdle 2016 *BD&S* | Evidence | At source; verified (probable) | Velocity and exhaustivity |
| boyd & Crawford 2012 *ICS* (author draft) | Reading (critical) | At source; verified | "Big data and whole data are also not the same"; Twitter |
| ADR UK, *What is administrative data?* | Standard (institutional) | At source; verified | Definition; not collected for research |
| ONS 2023 working paper, *Cataloguing errors in administrative and alternative data sources* | Standard/Evidence | At source; verified (live URL under /onsworkingpaperseries/) | Measurement / representation / processing errors |
| Connelly, Playford, Gayle & Dibben 2016 *SSR* 59 | Evidence (review) | At source (Warwick); verified | Undocumented; uncover the data-generation process |
| Bean 2016, *Independent Review of UK Economic Statistics* | Standard | At source | Colour: VAT returns; "improved business register" |
| Hawkins 1980 | — | Secondary (Aggarwal 2017; Osborne & Overbay 2004 — one-word difference) | "a different mechanism" |
| Aggarwal 2017 *Outlier Analysis* ch. 1 | Practice/Evidence (textbook) | At source; spot-checked | The Hawkins quotation; "normal model" |
| Barnett & Lewis 1994; Grubbs 1969 | — | Secondary (Hodge & Austin 2004; Osborne & Overbay) | Definitions; "not all outliers are illegitimate contaminants" |
| Hodge & Austin 2004 *AI Review* 22 | Evidence (survey) | At source; verified | B&L and Grubbs as quoted; causes |
| NIST/SEMATECH e-Handbook §1.3.5.17; §7.1.6 | Standard | At source; verified | Grubbs' assumptions; "prescence"; fences; "investigated carefully" |
| Lin, Zhang & Tong 2025 arXiv:2506.06491 | Evidence (preprint) | At source; verified | Tukey's "outside" and "far out"; 0.7% |
| Dawson 2011 *JSE* 19(2) | Evidence (simulation) | At source; spot-checked | ≥30% of normal samples flagged |
| Chandola, Banerjee & Kumar 2009 *ACM CSUR* 41(3) | Evidence (survey) | At source; verified | Anomaly v noise; point / contextual / collective |
| Osborne & Overbay 2004 *PARE* 9(6) | Evidence | At source (ResearchGate author copy); verified | Seven causes; z = 3 screen; fringeliers |
| Leys et al. 2013 *JESP* 49(4) | Evidence (adjacent domain) | At source (postprint mirror); verified (survey gloss softened) | Three problems; MAD; 1.4826; thresholds; "justified" |
| Simmons, Nelson & Simonsohn 2011 *Psych Sci* | Evidence (adjacent domain) | At source; verified | Flexibilities; 61%; report with exclusions included |
| Bakker & Wicherts 2014 *PLOS ONE* 9(7) | Evidence (adjacent domain; 153 articles) | At source; spot-checked; verified | 41% df/N discrepancy; protocol in advance |
| Hampel 2001, ETH Research Report 94 | Evidence/Practice | At source (mirror); verified | Breakdown points; 1–10% gross errors |
| Huber 1981 | — | Not verified; not quoted | — |
| Marsh et al. 2004 *BMJ* 329 | Evidence/Practice | Partial (public extract); verified | Positive deviance definition |
| Singhal, Sternin & Durá 2010, PD Initiative case study | Practice (advocacy) | At source | Colour: Vietnam; 85% (the movement's own) |
| Bradley et al. 2009 *Implementation Science* 4:25 | Evidence/Practice | At source; verified | Four steps; hypothesis-generating |
| Baxter et al. 2016 *BMJ Qual Saf* 25 | Evidence (systematic review) | At source; verified | "arbitrary"; "must always be stated" |
| Pascale & Sternin 2005 *HBR* | — | Teaser only | Colour; not quoted |
| Decision Book (design-decisions skill) Ch 6, 8, 9; rule register (DAT-14, DTA-19, COL-17) | Nightlife Culture | At source | Agrees / conflicts / silent-on log |
| Style Guide v1.5 (nightlife-culture-design skill) | Nightlife Culture | At source | Conflict log |
| Version 1 Ch 3 *The map*; Ch 8 *Gaps, uncertainty, freshness* (archived) | Nightlife Culture (prior position) | At source | Backward look |
| Prototype data contract | Nightlife Culture | Not re-read this sprint | Flagged |


## 9 · Version 2 — Chapter 5: Building a measure (6 October 2026)

*Legend as §5. "At source" — a research agent opened the link on 6 October; "spot-checked" — the orchestrator re-opened it (twelve items; eleven held, one unreachable); "verified" — the independent verification pass re-traced it on 6 October (eighty-two items; mismatches corrected in draft 2 and recorded in the research log, Entry 5). † abstract-only. "Secondary" — reached through another named document. "Reconstructed" — an abstract rebuilt from an index and therefore weaker than secondary. "Adjacent domain" — evidence or standards from education, health, development economics, environmental management or machine learning. "Method only" — a sector instrument read for its published method and never for its findings.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| OECD/JRC 2008, *Handbook on Constructing Composite Indicators* | Standard | Part I at source (JRC PDF); Part II via the JRC web guide's reproduction; spot-checked; verified | Definition; craftsmanship; pros and cons; equal weights; "value judgements"; compensability; sensitivity; presentation |
| JRC Competence Centre on Composite Indicators, *10 step guide* (steps 5–8, 10); *About* | Standard | At source; verified (live URLs under /composite-indicators/10-step-guide/) | Revised ten steps; normalisation and weighting sentences; the (21,1,1,1) example; sensitivity questions; "over 100 statistical audits" |
| Ravallion 2010/2012, "Mashup Indices of Development", WPS 5432 / WBRO 27(1) | Evidence | At source (working paper); verified | Definition of a mashup; "free to set"; the dashboard alternative |
| Crossick & Kaszynska 2016, AHRC Cultural Value Project report | Standard/Evidence | At source (first four chapters); verified | "evaluation, of which measurement is but one component"; non-commensurability; components framework |
| Paruolo, Saisana & Saltelli 2013, JRSS A 176(3) (arXiv 1104.3009v2) | Evidence | At source (author preprint); spot-checked; verified | Main effect; "little more than cosmetic"; THES 0.40/0.81 and 0.20/0.21; ARWU; HDI; four conclusions |
| Becker, Saisana, Paruolo & Vandecasteele 2017, *Ecological Indicators* 80 | Evidence | Abstract † (JRC repository); verified | Fitting weights to intended importance |
| Greco, Ishizaka, Tasiou & Torrisi 2019, *Social Indicators Research* 141 | Evidence (review) | At source (abstract and weighting section); verified | Equal weights commonest; five reasons; "miss the point" |
| JRC 2025, Statistical Audit of the Global Innovation Index (Appendix II) | Practice + Evidence | At source; verified ("Seven economies" ellipsis added) | "scaling coefficients and not importance coefficients"; 5,000 runs; rank intervals; reading instruction |
| Social Progress Imperative, methodology page; 2015 Methodological Report | Practice | Page at source; report secondary copy; verified (52 indicators in 2015) | Equal weights as a declared null; PCA within components |
| Munda & Nardo 2005, JRC EUR 21834 EN | Evidence | At source; verified | Compensability definition; substitution rates; non-compensatory "compulsory" |
| Munda & Nardo 2009, *Applied Economics* 41(12); Munda 2005, *Env Dev Sust* 7 | Evidence | Abstracts † | Colour |
| Ravallion 2010/2012, "Troubling Tradeoffs in the HDI", WPS 5484 / JDE 99(2) | Evidence | At source (CORE copy); spot-checked; verified | $0.51; $9,000; "transparency about the implicit tradeoffs"; the reform moved the price |
| UNDP, HDR 2010 Box 1.2; Technical Note 1 | Standard | At source; verified | Geometric mean; "imperfect substitutability" |
| Klugman, Rodríguez & Choi 2011, HDRO RP 2011/01 | Evidence (rejoinder) | At source; verified | "inappropriate to label the trade-offs … as 'values'" |
| García Aguña & Kovacevic 2010, HDRO RP 2010/47 | Evidence | At source; verified | HDI rank shifts "relatively minor"; weights the main driver |
| Legatum Institute, Prosperity Index methodology | Practice | At source; verified | Power means; "poor substitutes"; "punish weakness"; p = −1 |
| MHCLG 2019, *English Indices of Deprivation 2019: Technical Report* | Standard | At source (to §4.6); verified (39 indicators; weights; 2000 derivation inherited) | Domain weights; ranks; exponential transformation; "deprivation and not affluence"; sensitivity |
| Böhringer & Jochem 2007, *Ecological Economics* 63(1); ZEW DP 06-073 | Evidence (review) | Abstract † plus working paper at source; verified (eleven indices) | "rather useless if not misleading" |
| Saisana, Saltelli & Tarantola 2005, JRSS A 168(2) | Evidence | At source (author copy); verified | TAI audit; the Netherlands; "no longer a magic number" |
| ONS *Content style guide — Rounding*; Analysis Function *Data visualisation: tables*; *Communicating quality, uncertainty and change* | Standard | At source; verified | Two effective digits; rounding reduces precision; the range sentence |
| Goodhart 1975 (RBA; reprinted 1984) | Evidence (original) | **Secondary** — Chrystal & Mizen 2003 (third-party copy; verified), Thornton 2007, Manheim & Garrabrant 2018 agree; pages unverified | "Ignoring Goodhart's law, that any observed statistical regularity will tend to collapse…" |
| Strathern 1997, *European Review* 5(3) | Evidence/Reading | At source (mirrored PDF); spot-checked; verified (p. 308; abstract p. 305) | The aphorism; the 2.1 sentence; Hoskin attribution; "a life of its own" |
| Hoskin 1996, in Munro & Mouritsen (eds) | — | Not reachable; cited as Strathern cites it | — |
| Campbell 1976, Dartmouth Occasional Paper 8 (EPP 2(1) 1979) | Evidence | At source; spot-checked; verified (pp. 49–53) | The law; crime statistics; achievement tests; multiple indicators |
| Kerr 1975, AMJ 18(4); Kerr 1995 retrospective | Evidence/Reading | 1975 at source (institutional copy); verified ("Nonetheless," restored); 1995 secondary — colour | "rewarded … pretend to do"; "Fascination with an 'Objective' Criterion" |
| Bevan & Hood 2006, *Public Administration* 84(3) | Evidence | At source (third-party PDF; LSE record); spot-checked; verified | Gaming; ratchet/threshold/distortion; synecdoche; CHI third; the spike; NAO nine trusts; 23%/5.3%; 10/16/22; "we do not know" |
| Hood 2006, PAR 66(4) | Evidence | At source (third-party PDF); verified | Central non-verification as gaming |
| PASC 2003, *On Target?* HC 62-I | Standard (parliamentary) | At source; verified (80% restored to full form) | Massaged times; Bristol Eye Hospital; 80% misstated or undisclosed |
| NAO 2001, *Inappropriate adjustments to NHS waiting lists* HC 452 | Standard | Report page at source | Nine trusts |
| Bevan & Hamblin 2009, JRSS A 172(1) | Evidence | Abstract †; verified | "only in England has this target been met" |
| Kelman & Friedman 2009, JPART 19(4) | Evidence (adjacent domain) | Abstract †; verified | "no evidence for any of the dysfunctional effects" |
| Propper et al. 2008 (BEJEAP 8(2)); 2010 (JPubE 94) | Evidence (adjacent domain) | Abstracts † (RePEc); verified | England–Scotland; no diversion, no health loss |
| Besley, Bevan & Burchardi 2009, CEPR DP 7306 | Evidence | Abstract †; verified | England–Wales; "some shuffling" |
| Burgess, Wilson & Worth 2013, JPubE 106 | Evidence (adjacent domain) | Abstract †; verified | Wales league tables abolished; effectiveness fell |
| Bevan & Wilson 2013; Dixon, Hood & Wilson | Evidence | Abstract †; author site | Colour |
| Koretz 2005, CSE Report 655; Klein et al. 2000, RAND IP-202 | Evidence (adjacent domain) | At source; verified | Score inflation; sawtooth; "3 to 5 times" |
| Nichols & Berliner 2005, EPSL | Evidence/Reading | At source | Colour |
| Espeland & Sauder 2007, AJS 113(1) | Evidence | Abstract at source; verified | "reactivity"; two mechanisms named |
| Muller 2018, *The Tyranny of Metrics*, introduction | Reading | At source (publisher excerpt); verified | "metric fixation"; "not measurement, but excessive measurement" |
| Manheim & Garrabrant 2018, arXiv 1803.04585 | Reading (taxonomy) | At source; verified | Four variants |
| Belfiore & Bennett 2007, IJCP 13(2) | Reading | At source (Warwick author copy); verified | Advocacy agenda; "policy-based evidence-making" |
| Holden 2004, *Capturing Cultural Value*; 2006, *Cultural Value and the Crisis of Legitimacy* | Reading | At source; verified ("easy to measure" is Holden quoting Kelly, Mulgan & Muers 2002) | Tail wagging the dog; the triad; "Money thus flows into measurement" |
| Centre for Cultural Value 2021, *Evaluation Principles*; launch essay | Practice/Standard (sector) | At source; verified (essay attribution corrected) | Learning over monitoring; "low-value monitoring and reporting" |
| Cronbach & Meehl 1955, *Psychological Bulletin* 52 | Evidence (foundational) | At source; verified | Construct validity; nomological net; "explicit, public steps of inference" |
| Messick 1995, *American Psychologist* 50(9) (ETS RR-94-45) | Evidence (foundational) | At source (ETS report); verified (one sentence removed; one restored) | Unified definition; six aspects; two failures; consequential aspect |
| AERA/APA/NCME 2014, *Standards for Educational and Psychological Testing* | Standard | At source (open PDF); verified | Definition; unitary; five sources; consequences boundary; reliability; no face validity |
| Borsboom, Mellenbergh & van Heerden 2004, *Psych Review* 111(4) | Evidence/Reading | **Secondary** (Hathcoat 2013; Ramminger & Jacobs 2024); verified against Hathcoat | The iff definition; ontology/epistemology |
| Campbell & Fiske 1959, *Psych Bulletin* 56 | Evidence (foundational) | **Secondary** (one fragment via Rönkkö & Cho 2022; definitions from the Standards and Trochim) | Convergent and discriminant |
| McHugh 2012, *Biochemia Medica* 22(3); Koo & Li 2016 | Practice/Evidence | McHugh at source, verified; Koo & Li record only † | Inter-rater reliability; kappa |
| Trochim, *Research Methods Knowledge Base* | Practice (methods text) | At source; verified ("in reality" restored; face-validity wording replaced) | Convergent/discriminant; face validity; "consistent but wrong" |
| ONS, *Personal well-being in the UK QMI*; *survey user guide* | Standard | At source; spot-checked; verified | The ONS4; cognitive testing; "not appropriate to combine" |
| Dolan, Layard & Metcalfe 2011, CEP SP23 | Evidence/Standard | At source; verified | Three categories; "stable and reliable patterns"; "the time has certainly come" |
| OECD 2013, *Guidelines on Measuring Subjective Well-being* | Standard | Landing page only | Not quoted |
| Lincoln & Guba 1985, *Naturalistic Inquiry* p. 314 | Practice (foundational) | **Secondary** (Roller 2021; Dahal 2025 agree) | "most crucial technique"; member check defined |
| Birt et al. 2016, QHR 26(13) | Evidence/Reading | Abstract at source, verified; body partial, unverified | Nod to validation; synthesised member checking |
| Thomas 2017, QRP 14(1) | Evidence (review) | **Reconstructed** abstract; summarised in Lloyd et al. 2024 (at source) | Little evidence member checks improve findings |
| Morse et al. 2002, IJQM 1(2); Morse 2015 QHR 25(9) | Reading | 2002 at source, spot-checked, verified; 2015 abstract † | "may actually invalidate"; "not a verification strategy" |
| Lloyd, Hyett & Kenny 2024, IJQM | Evidence (small) | At source; verified | 11 of 13; nine unchanged; grammar edits |
| Fraser, Dougill, Mabee, Reed & McAlpine 2006, J Env Mgmt 78(2) | Evidence (adjacent domain) | At source (author copy; string-verified by agent); verifier could not reach | Empowerment; "apparently simply job"; must feed decisions |
| Reed, Fraser & Dougill 2006, *Ecological Economics* 59(4) | Evidence | Abstract at source | Top-down v bottom-up |
| Reed 2008, *Biological Conservation* 141 | Evidence (review; adjacent domain) | At source (author copy; string-verified by agent); verifier could not reach (no OA copy) | Claims "rarely been tested"; "little empirical evidence" |
| de Vente, Reed, Stringer, Valente & Newig 2016, *Ecology and Society* 21(2) | Evidence (24 cases) | At source; verified | Design over context; trust and learning; government-run trade-off |
| Reed, Dougill & Baker 2008, *Ecological Applications* 18(5) | Evidence (adjacent domain) | **Reconstructed** abstract † | Pastoralist indicators mostly valid, not always reliable |
| Bell & Morse 1999/2008 | Practice | Not reachable; a reviewer's characterisation | Colour |
| Sen 2005, *Journal of Human Development* 6(2) | Reading (philosophy) | At source (UNICEF copy; string-verified); verified | Public reasoning; no fixed list |
| Alkire 2008, MPRA 8862 | — | At source; **no quotation used** (fetch tool fabricated sentences; caught by string search) | — |
| Charlton 1998 (UC Press page); UN DESA 2004 | Practice | At source; verified | "Nothing About Us Without Us" |
| DCMS 2021, *Valuing culture and heritage capital*; CHC Portal 2025 | Standard | At source; verified | Definition; Green Book appraisal; alongside qualitative |
| Knell & Whitaker 2016, *Quality Metrics National Test: Final Report* | Practice (delivery team) | At source; spot-checked; verified (triangulation ellipsis added) | Twelve statements; slider; medians and IQRs; "clapometer"; "apples, pears and pineapples" |
| Impact & Insight Toolkit — dimensions; glossary; history; ACE page | Practice | At source; verified | Six domains; outcomes v qualities; lineage |
| UNESCO 2019, *Culture\|2030 Indicators* | Standard | Institutional copy (ITI); verified | Same-place change, not ranking; four dimensions, 22 indicators |
| Centre for Thriving Places — methodology appendix; FAQ | Practice | At source; verified | 48 indicators; z-scores; equal weights; no overall score, no stated reason |
| OECD Better Life Index — OECD landing text; Wikipedia | Practice | Landing at source; mechanics **secondary** | User-set weights |
| ONS, *UK Measures of National Well-being* dashboard; 2023 review; user guide | Standard | At source; verified | 60 measures; per-measure change; no rationale stated |
| Creative Footprint — methodology page; early overview PDF; 2024 Rotterdam report methodology and scores | Practice (sector instrument — **method only**) | At source; spot-checked; verified (harmonic mean corrected; inference withdrawn) | 15 criteria; "proprietary algorithms"; Likert; 8.58/5.90/5.41 v 6.10; undisclosed weights and aggregation |
| Stiglitz, Sen & Fitoussi 2009 | Standard | Institutional copy (Eurostat), executive summary and early chapters; verified | Rec. 11; the car; "no single measure"; Rec. 9; health indices |
| UNECE 2025, *Guidelines on measurement of well-being*, Ch. 4 | Standard | At source; spot-checked; verified | Dashboard defined; onus; side by side; compensability; "accompanied by dashboards"; Box 4.1 |
| UNECE/Eurostat/OECD 2014, CES Recommendations | Standard | Not reachable (403) | — |
| Saltelli 2007, *Social Indicators Research* 81(1) | Reading (commentary) | Abstract †; verified | "mostly advocacy-driven" |
| Gebru et al. 2021 (arXiv 1803.09010v8); Mitchell et al. 2019 (arXiv 1810.03993); Holland et al. 2018 (arXiv 1805.03677) | Practice (adjacent domain — machine learning) | At source; verified | Datasheets; model cards; nutrition label |
| Decision Book Ch 6, 8, 9; rule register | Nightlife Culture | At source | Silent on composites |
| Style Guide v1.5 — evidence components | Nightlife Culture | At source | Conflict log |
| Version 1 Ch 6 *The measure on screen* (archived) | Nightlife Culture (prior position) | At source | Recipe on the face; refusal test; (21,1,1,1); the sector composite's figures; intensity not volume |
| *Artists Make Great Places* v2.1 — the open form question | Nightlife Culture | As version 1 cites it; not re-read | The form left open |

## 10 · Version 2 — Chapter 6: Finding value in the data (6 October 2026)

*Legend as §5. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string (the presence-check method; see Research Log Entry 6, method notes); "spot-checked" — the orchestrator re-opened it (twelve items; all held); "verified" — the independent verification pass re-traced it on 6 October (about 250 items; mismatches corrected in draft 2). No web search was available for this sprint; every source was reached by direct address. "Reconstructed" — an abstract rebuilt from the OpenAlex index, not checked against the publisher. "Unreached" — named in the chapter, nothing quoted.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Fayyad, Piatetsky-Shapiro & Smyth 1996, *AI Magazine* 17(3) | Evidence | At source (AAAI PDF); verified | KDD definition; four tests; steps one and nine; "data dredging … dangerous" |
| Pearl 2018, UCLA Tech Report R-481 | Evidence | At source; spot-checked; verified | Three rungs; "Interventional questions cannot be answered…" |
| Hernán 2018, *AJPH* 108(5) | Evidence | Reconstructed abstract †; verified against the index | The "c-word" argument |
| Hill 1965, *Proc R Soc Med* 58(5), in the JRSM 2015 open reprint | Evidence (adjacent domain) | At source; spot-checked; verified | Nine viewpoints; "none … sine qua non"; "glitter of the t table"; the licence to act |
| HM Treasury, *Magenta Book*, May 2026 edition (at the 2020 address; pp. 1–72) | Standard | At source; verified (incl. the "particularly suited" conditions) | Impact; counterfactual; attribution; experimental "most defendable"; theory-based conditions; "Ruling out of alternative causes" |
| Mayne 2008, ILAC Brief 16 | Evidence/Practice | At source; verified | Contribution analysis; six steps; "stronger and more credible" |
| Scholarpedia, "Granger causality" (incl. Granger's personal account) | Evidence | At source; verified | Predictor not cause; "it is only Granger causality" |
| OECD, Composite leading indicator page | Standard | At source (definition only); verified | "early signals of turning points"; methodology unreached |
| HCA 2014, *Additionality Guide* 4th ed. (withdrawn 24 May 2022) | Standard | At source; verified ("first sentence" corrected to opening definition; "longer-term") | Additionality; reference case; deadweight; leakage; displacement; substitution; multipliers; figure 2.3; ready reckoners; "Not adequate" |
| HM Treasury, *Green Book*, February 2026 edition, ch. 7 | Standard | At source; verified (publication 5 Feb 2026; 2022 withdrawn) | Distributional analysis; welfare-weight formula; 1.3; weighted alongside unweighted |
| Ricardo 1817/1821, *Principles*, ch. II (Econlib) | Evidence (classical) | At source; verified | Rent; "a rent is paid because corn is high" |
| Mazzucato 2018, *The Value of Everything* — publisher blurb; Mazzucato & Ryan-Collins 2022 (UCL Discovery) | Evidence | Blurb at source (secondary to the book); 2022 paper at source; verified | Taking against making; rents as unearned income |
| SROI Network / Cabinet Office 2012, *A Guide to SROI*; Social Value International, Principles | Standard (the method's own) | At source; verified (principle wordings are the site's; Guide spells "over-claim") | Definition; "about value, rather than money"; deadweight; attribution; displacement; "not appropriate to compare the social return ratios alone"; seven then eight principles |
| Arvidson, Lyon, McKay & Moro 2013, *Voluntary Sector Review* 4(1) | Evidence (critique) | Abstract † (Lund record); verified (wording corrected) | Participatory design against use for competition |
| Easton, Lees, Hubbard & Tate 2020, *Urban Studies* 57(2) | Evidence (systematic review) | At source; spot-checked; verified (one sentence is their quotation of Baeten et al. 2017 — secondary) | Measurement failures; the tripartite confound; Freeman's method |
| Freeman 2005, *Urban Affairs Review* 40(4); Ding, Hwang & Divringi 2016 | Evidence | Freeman: reconstructed abstract †, method via Easton; Ding: metadata only | First large-N operationalisation; not paraphrased |
| US EPA 2010/2014, *Guidelines for Preparing Economic Analyses*, ch. 7 §7.3.1.2 | Standard (adjacent domain) | At source; verified | Travel cost; single purpose; time; substitutes |
| Fujiwara & Campbell 2011, HM Treasury Green Book supplementary guidance | Standard | At source; verified | Revealed preference; use-value only; the demand relation; time at one-third to full wage |
| ecosystemvaluation.org, "Travel Cost Method" | Practice | At source; verified | "the 'price' of access to the site" |
| Hotelling 1947 (letter); Clawson 1959; Clawson & Knetsch 1966; Reilly 1931 | Evidence | Unreached; attribution secondary (Wikipedia) | Colour only |
| Tobler 1970, *Economic Geography* 46 | Evidence | Metadata (Crossref); first law secondary (Wikipedia) | Epigraph only |
| Huff 1964, *Journal of Marketing* 28(3); ESRI Huff model page | Evidence/Practice | Abstract †; ESRI single pass | Colour only |
| ONS 2015, Travel to Work Areas 2001–2011 | Standard | At source; verified | 75% / 66.7% / 3,500 / 25,000 |
| Clark, Bradburn, Love & Altman 2003, *BJC* 89 | Evidence (adjacent domain) | At source (Nature); verified | Censoring; Kaplan–Meier; rates mislead |
| ONS 2016, Methodology Working Paper 8 (mobile phone data) | Standard | At source; verified | MNO share; no constant proportional relationship; usage heterogeneity |
| ONS 2026, real-time indicators methodology and 17 Sept 2026 bulletin | Standard | At source; verified | EE 24m devices; residents and workers excluded; Revolut caveat; "statistics in development" |
| Wesolowski et al. 2012, *PLoS ONE* 7(4) | Evidence (adjacent domain; Kenya 2009) | At source; verified | Heterogeneous ownership skews estimates |
| Poor & Smith 2004, *J Cultural Economics* 28(3); Bedate et al. 2004 | Evidence | Poor & Smith abstract † (RePEc); verified ("average annual individual consumer surplus"); Bedate metadata | $8.00–$19.26 by functional form |
| Stirling 2007, *J R Soc Interface* 4(15) (SPRU WP 156; PMC2373389) | Evidence | At source in two copies; verified (first quotation follows the working paper's "mentioned above") | Variety, balance, disparity; every index a weighting |
| Jost 2006, *Oikos* 113(2); Hill 1973, *Ecology* 54(2) | Evidence | Abstracts † via Crossref/OpenAlex metadata | Effective numbers |
| Benhamou & Peltier 2007, *J Cultural Economics* 31(2) | Evidence | Abstract † (RePEc); verified | Supplied against consumed diversity; verdict depends on property |
| Geurs & van Wee 2004, *J Transport Geography* 12(2) | Evidence | Abstract † only; four components not quoted | Named only |
| TfL 2015, *Assessing transport connectivity in London* | Practice/Standard | At source; verified (reliability factor in Table 2.1) | PTAL; "does not take into account…" |
| Martin 2002, *Cultural Trends* 12(47); Ipsos MORI 2003 page | Evidence | Reconstructed abstract †; Ipsos at source; verified | 62%; the research question |
| The Audience Agency — Audience Spectrum pages; liquidation notice 11 Sept 2026 | Practice | At source; verified | Segmentation; liquidation 10 Sept 2026 |
| McMillan & Chavis 1986 (author's site); Peterson, Speer & McMillan 2008 (PDF on author's site) | Evidence (adjacent domain) | At source; verified (n = 293; eight items) | Four elements; the Brief Sense of Community Scale |
| DCMS, Taking Part guidance and Year 11 questionnaire; Participation Survey 2023–24 main and technical reports | Standard | At source; verified | 12-month reference; 91%; 25% response; "weighting only corrects for observed bias" |
| Warwick Commission 2015 | Evidence | Unreached (PDF 404) | The 8% not used |
| ONS 2025, Business demography UK 2024 §8; Business demography QMI | Standard | At source; verified | Survival definition; reactivations; "not final until the third year"; size invisible; IDBR unit; geography caution |
| Eurostat, Glossary: Enterprise survival | Standard | At source; verified | Register-identity continuity |
| Holling 1973, *Annu Rev Ecol Syst* 4 | Evidence | Unreached | Named only |
| Walker, Holling, Carpenter & Kinzig 2004, *Ecology and Society* 9(2) | Evidence (adjacent domain) | At source; verified | Resilience, adaptability, transformability |
| Martin & Sunley 2013/2015, PEEG 13.20 / *J Econ Geog* 15(1) | Evidence | At source (working paper); verified; one table cell failed its check and is unused | Three interpretations; "bounce forward"; their definition |
| Kaminsky, Lizondo & Reinhart 1998, *IMF Staff Papers* 45(1) | Evidence (adjacent domain) | Abstract † (MPRA); verified | Signals; threshold; 24 months |
| Berg & Pattillo 1999, *IMF Staff Papers* 46(2) | Evidence (adjacent domain) | Abstract † (IMF eLibrary); verified (mitigating sentence restored in draft 2) | Out-of-sample verdict |
| Tuckman & Chang 1991, *NVSQ* 20(4) | Evidence | Abstract †; verified; criteria not named | Vulnerability as behaviour |
| Scott 1998, *Seeing Like a State* (libcom OCR copy); Scott 2010, Cato Unbound | Evidence/Reading | At source; spot-checked; verified (forester's name not confirmed) | Legibility; abridged maps; fiscal forestry; the second generation |
| FDA 2018, Surrogate Endpoint Resources; FDA-NIH BEST glossary | Standard (adjacent domain) | At source; verified | Surrogate definition; validated / reasonably likely |
| Fleming & DeMets 1996, *Ann Intern Med* 125(7) | Evidence (adjacent domain) | Abstract page at source; verified | "In practice, this requirement frequently fails" |
| Tukey 1962, 1977, 1980 | Evidence | Unreached | Named only |
| Center for Open Science, Preregistration page; Nosek et al. 2018 | Practice/Standard; Evidence | COS at source, verified; Nosek unreached | Exploratory/confirmatory; "same data cannot be used to generate and test" |
| Gelman & Loken 2013 (working paper); 2014, *American Scientist* 102(6) | Evidence | At source (both); verified | The garden; "even with just one analysis" |
| Benjamini & Hochberg 1995, *JRSS B* 57(1) | Evidence | Abstract at source (OUP); verified | FWER; FDR |
| ASA 2016, press release (Wasserstein & Lazar journal text walled) | Standard (professional) | At source; verified (all six) | Six principles |
| Vigen, *Spurious Correlations* (main page; item 1433); Yule 1926; Granger & Newbold 1974 | Colour; Evidence | Vigen at source, verified (count is the main page's); Yule and G&N metadata | r = 0.967; "Observations not independent" |
| Goodfellow, Bengio & Courville 2016, ch. 5 §5.3; Google MLCC "Dividing the original dataset" (2025) | Evidence; Practice | At source; verified | Holdout discipline; "wear out" |
| Ioannidis 2005, *PLoS Medicine* 2(8) | Evidence | At source; verified | Corollaries 3 and 4 |
| Box 1976, *JASA* 71(356); Box 1979, MRC TSR 1954 / Launer & Wilkinson p. 202 | Evidence | 1976 at source, verified; 1979 heading at source, body from the published chapter as the verifier read it | "importantly wrong"; the aphorism's home |
| Breiman 2001, *Statistical Science* 16(3) (course mirror) | Evidence | At source; verified | Two cultures; 98% / 2% |
| Hand 2006, *Statistical Science* 21(1) (arXiv math/0606441) | Evidence | At source; verified | 85–90%; nonstationarity; "illusory" |
| Open Science Collaboration 2015, *Science* 349 | Evidence | Crossref editor's summary only | Not used for figures |
| AQuA Book 2025 (updated July 2026), §2, §5.3, §9.5; Glover 2014, DSTL/TR81015 | Standard | At source; verified (negative finding qualified by §5.3 and §9.5; "it specified" is the page's) | Verification; validation; no outturn instruction; "agreement of those judged competent" |
| NHS Improvement 2019, *Making Data Count* (getting started; strengthening your decisions) | Practice (NHS guidance) | At source; spot-checked; verified | Two points; common/special cause; limits; 99%; rules; "seven to nine"; "wild goose chases" |
| NIST/SEMATECH e-Handbook §6.3.1, §6.3.2.1 | Standard (adjacent domain) | At source; verified | 3σ; 0.0027; ARL ≈ 371; the two questions |
| Spiegelhalter, Grigg, Kinsman & Treasure 2003, *IJQHC* 15(1) | Evidence (adjacent domain) | Abstract † at source; verified | "could have … depending on the data source and the comparator" |
| Salmon, Schumacher & Höhle 2016, *JSS* 70(10) (arXiv 1411.1292); Farrington et al. 1996 | Evidence (implementation) | At source; verified; Farrington unreached | Seasonal reference window; EARS baseline |
| Wainer 2007, *American Scientist* 95(3), verified in *Picturing the Uncertain World* (2009) ch. 1 | Evidence | At source (2009 chapter); verified; magazine 503 | De Moivre's equation; both tails; $1.7bn to education projects |
| Tversky & Kahneman 1971, *Psychological Bulletin* 76(2) | Evidence | Unreached | Named only |
| Eurostat 2019, *Guidelines on small area estimation*, KS-GQ-19-011 | Standard | At source; verified | Small area by precision; indirect estimators; Fay–Herriot as weighted average |
| Rao & Molina 2015; Fay & Herriot 1979; Gelman & Hill 2007 | Evidence | Unreached; named via Eurostat / Gelman 2006 | — |
| ONS 2025, Income estimates for small areas QMI; ONS 2019, fuel poverty small-area research | Standard | At source; spot-checked; verified | 25,000; 40% of MSOAs; 7,264; multilevel; "should not be used to measure change"; "borrowing strength" |
| US Census Bureau, SAIPE county-level estimation details | Standard | At source; spot-checked; verified | Shrinkage weight in one sentence |
| Efron & Morris 1975, *JASA* 70(350) (McGill copy); Efron & Morris 1977, *Scientific American* (standfirst only) | Evidence | 1975 at source, verified; 1977 unreached beyond standfirst | 18 players; 45 at-bats; Clemente; shrinking toward X̄; efficiency 3.50 |
| Gelman 2006, *Technometrics* 48(3) (author's PDF) | Evidence | At source; spot-checked; verified (Minnesota confirmed; draft 1 glosses cut) | Lac Qui Parle County; shrinking toward the complete-pooling estimate |
| NHS England Digital 2023, HES/ECDS disclosure control | Standard | At source; verified | 1–7 as "*"; rounding to 5; rates |
| Government Analysis Function 2026, SDC for tables from surveys | Standard | At source; verified | 2 / 3 / statutory 5; risk rises as population falls |
| ONS 2025, OPN QMI; ONS 2018, ASHE low pay/pension QMI | Standard | At source; verified | Base > 10; CV bands; dark green for both reasons |
| Decision Book Ch 5, 6, 8, 10, 15 | Nightlife Culture | At source (repo) | Conflict log; the two reasons operated unnamed |
| Style Guide v1.5 — evidence components | Nightlife Culture | At source | Conflict log |
| Version 1 Ch 6 *The measure on screen* (archived) | Nightlife Culture (prior position) | At source; verified against reader.html ("what the night didn't originate") | Claim ladder; ledger strip; dynamic census |
| BRIEF-v2 §2 (failure register) | Nightlife Culture | At source | "do not recognise their place within the front-end interface" |

## 11 · Version 2 — Chapter 7: Comparison, time and intervention (6 October 2026)

*Legend as §5 and §10. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (eleven sources, thirty-six sentences; all held); "verified" — the independent verification pass re-traced it (about three hundred items; fourteen mismatches corrected in draft 2). No web search was available. "(read once)" sentences were all confirmed by the verifier.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Espeland & Sauder 2007, *AJS* 113(1); Espeland & Sauder, *Engines of Anxiety* ch. 1 (Russell Sage open chapter); Espeland & Stevens 1998, *Annu Rev Sociol* 24; Sauder & Espeland 2009, *ASR* 74(1) | Evidence | 2007 abstract †; book chapter at source, verified; 1998 abstract †; 2009 abstract † (Crossref) | Reactivity; two mechanisms; "play a crucial role in creating this hierarchy"; commensuration; internalisation |
| World Bank statement 16 Sept 2021; External Panel Review 1 Sept 2021 (Alfaro, Auerbach, Cárdenas, Ito, Kalemli-Özcan, Sandefur); Sandefur & Wadhwa, CGD blog 18 Jan 2018; B-READY FAQ and About | Standard / Evidence | At source; spot-checked; verified (eleven recommendations; "small changes" summarises 2008 and 2013 reviews; two blog authors) | "Remove the aggregate index and country rankings"; arbitrary weights; interference; Chile; no aggregate score; quintiles |
| MHCLG 2019, *IoD2019 FAQs* Q22 | Standard | At source; verified | Relative rank; "overtaken" |
| Goldstein & Spiegelhalter 1996, *JRSS A* 159(3) (Bristol CMM typescript) | Evidence | At source; spot-checked; verified; published text and discussion unreached | Intervals on ranks; two-thirds not separable; "misplaced"; health warning; extrinsic factors |
| Marshall & Spiegelhalter 1998, *BMJ* 316 (with commentary by Sanderson & McKee) | Evidence | At source; spot-checked; verified (authorship corrected) | IVF clinic ranks unreliable, "particularly for smaller institutions" |
| Leckie & Goldstein 2009, CMPO WP 09/208 | Evidence | At source; verified | Future cohort; "very little to offer as guides to school choice" |
| Mogstad, Romano, Shaikh & Wilhelm 2024, *REStud* 91(1) | Evidence | Abstract † (Crossref); verified | Confidence sets for ranks; robust for countries, uninformative for neighbourhoods |
| JRC, Cultural and Creative Cities Monitor 2019 (JRC117336) and 2017 Annex B (JRC107331) | Practice + Evidence | At source; verified (2,000 simulations) | ±3 positions for ~80%; 81% within two of median; ±25% weights |
| Bird et al. 2005, *JRSS A* 168(1) (RSS working party) | Standard | Summary †; body unreached | "screening devices"; "harmful and indeed destructive" |
| NHS England Digital, SHMI page | Standard | At source; verified | "It is inappropriate to rank trusts according to their SHMI" |
| UKSA Board minutes 30 Oct 2025, item 9.3 | — (a minute) | At source; verified | "should not be reduced to league tables" |
| Government Analysis Function 2022, *Data visualisation: charts*; 2018, *Communicating quality, uncertainty and change* | Standard | At source; verified | "Always rank bars by value"; describing change; empty caveats |
| APHO 2008, Technical Briefing 3; ONS 2025, *User guide to mortality statistics* §7; PHE 2017, directly standardised rates guide | Standard (adjacent domain) | At source; verified (APHO truncation corrected) | Direct and indirect standardisation; observed/expected; the two conditions; 1976/2013 ESP; the under-10 floor |
| CIPFA Nearest Neighbours page; Oflog 2023 | Practice / Standard | At source; verified | "a subjective process"; 40 metrics; adoption |
| ONS 2024, clustering methodology; ONS 2025/2026, clustering and statistical nearest neighbours; ONS 2025, Explore Local Statistics QMI | Standard | At source; verified (nearest neighbours added 14 Feb 2025) | k-means; 34 metrics; not a judgement; 20 by Euclidean distance; snapshot; three words by MAD; fewer than 10 areas |
| DfE 2025, Children's services statistical neighbour benchmarking model technical report | Standard | At source; verified | 10 neighbours; weighted Euclidean distance; stated assumption; closeness bands |
| Faulkender & Yang 2010, *JFE* 96(2); Bizjak, Lemmon & Nguyen 2011, *JFE* 100(3) | Evidence (adjacent domain) | Abstracts † (RePEc); verified (Bizjak truncation corrected) | Self-chosen comparators flatter; disclosure "preliminary" |
| Bruggemann & Carlsen 2014, *MATCH* 71; Carlsen & Bruggemann 2022, *Standards* 2(3); Fattore 2016, *Soc Indic Res* 128 | Evidence | At source; at source; abstract † | Incomparability as information; "smashed out by aggregation"; the method's limit |
| Spiegelhalter 2005, *Stat Med* 24; Spiegelhalter 2005, *QSHC* 14 | Evidence (adjacent domain) | Abstracts † (Crossref; BMJ); bodies unreached | Funnel definition; "avoid spurious ranking"; over-dispersion |
| APHO 2007 (Flowers), Technical Briefing 2; PHE 2017, Funnel Plots guide; HQIP Oct 2025, NCAPOP Outlier Guidance | Standard (practitioner) | At source; spot-checked (APHO); verified (HQIP truncation corrected) | Ranking's flaws; common and special cause; funnel mechanics; 2 in 1,000; alert and alarm; case-mix |
| Hyndman & Athanasopoulos, *FPP3* §§2.3, 3.2–3.6, 13.7; Hyndman & Kostenko 2007, *Foresight* 6 | Practice (textbook) | At source; verified | Components; smoothing choices; STL windows; "misleading and unsubstantiated"; minimum observations |
| Cleveland et al. 1990, *JOS* 6(1) | Evidence | Unreached (image scan) | — |
| ONS seasonal adjustment page; RSI QMI 2025; Retail sales Aug 2026 bulletin | Standard | At source; verified | Purpose; calendar effects; irregular; monthly review; unconstrained revisions; weather as commentary; three-month rate |
| Eurostat 2015, *ESS guidelines on seasonal adjustment* (KS-GQ-15-001) | Standard | At source; spot-checked; verified | 3 and 7 years; one observation revises years; which growth rate; end-point; turning points |
| US Census Bureau, Seasonal Adjustment Q&A; ABS 2023, *Time Series Analysis: The Basics* | Standard | At source; spot-checked (ABS); verified | Factors are estimates; same period last year; artificial seasonality |
| ECB Monthly Bulletin Jan 2005 and Jan 2007, boxes on base effects | Standard | At source; verified | Base effect |
| ONS style guide (percentages; statistical language); Eurostat Statistics Explained (percentage points; index and base year) | Standard | At source; verified | Percentage points; "significant"; index definition |
| ONS CPI Technical Manual 2019 (rev. 2025); ONS CPI brief guide 2026; ILO et al. 2020 CPI Manual ch. 1; US BLS, calculating percent changes; HMT 2014, GDP deflators guide; Commons Library SN04944 | Standard | At source; verified ("measures" corrected) | Chain-linking; "arbitrary"; five-year weights; index points; real terms |
| Barnett, van der Pols & Dobson 2005, *IJE* 34(1); Bland & Altman 1994, *BMJ* 309; Morton & Torgerson 2003, *BMJ* 326 | Evidence | Abstract †; at source; opening at source; verified | Regression to the mean |
| Code of Practice for Statistics 3.0 (OSR, 2025); ONS revisions policy 2024; Eurostat 2013 revision guidelines; Philadelphia Fed real-time data set; ONS crime QMI 2026; ONS TCSEW comparability 2021 | Standard | At source; verified | Breaks; back series; revisions; vintages; mode change |
| Columbia Mailman, Age-Period-Cohort primer | Practice | At source; verified | APC identification |
| Campbell & Stanley 1963 (SFU scan, OCR to c. p. 26) | Evidence | At source; spot-checked; verified | Internal validity; eight threats; "bad example" |
| Bernal, Cummins & Gasparrini 2017, *IJE* 46(1); Lopez Bernal et al. 2018, *IJE* 47(6); Cochrane EPOC 2017 | Evidence / Standard | At source; verified | ITS; impact model a priori; no fixed limits; co-interventions; controls; three points each side |
| Card & Krueger 1994, *AER* 84(4) | Evidence | At source (author's copy); verified | The canonical DiD |
| World Bank DIME Wiki (DiD; PSM; MDE); Huntington-Klein, *The Effect* ch. 18; Cunningham, *Mixtape* chs. 4, 9, 10 | Practice (textbook / wiki) | At source; verified | Equal trends; untestable; pre-trend checks; SUTVA; matching limits |
| Goodman-Bacon 2021, *J Econometrics* 225(2) (NBER WP 25018); Callaway & Sant'Anna 2021 (arXiv); Roth 2022, *AER: Insights* 4(3); Roth et al. 2023 (arXiv) | Evidence | At source; abstract †; at source; read not cited | Staggered adoption; negative weights; pre-test caution |
| Abadie, Diamond & Hainmueller 2010, *JASA* 105(490); 2015, *AJPS* 59(2); Abadie 2021, *JEL* 59(2) (June 2020 manuscript) | Evidence | At source; spot-checked (2021); verified; typeset JEL unreached | Synthetic control; weights; contextual requirements; placebos |
| Lee & Lemieux 2010, *JEL* 48(2) (NBER WP 14723) | Evidence | At source; verified | RD; "overly simplistic and pessimistic" |
| HM Treasury, *Magenta Book* May 2026 (pp. 56–57, 64–65) and Annex A (May 2026, at the 2020 path) | Standard | At source; spot-checked; verified | Counterfactual; feasibility table; spillovers and displacement; synthetic control area; design annex |
| What Works Centre for Local Economic Growth: SMS page 2015; scoring guide 2016; Brett-Harding 2022, 2023 | Standard / Practice | At source; verified | Five levels; Level 3 floor; DiD max 3; displacement |
| J-PAL 2021, Power calculations; EEF 2019, security of findings; Nesta 2013, Standards of Evidence | Practice / Standard | At source; verified | Power; MDE; padlocks; "will not evidence direct causality" |
| HM Treasury, *Green Book* Feb 2026 ch. 6 and uncertainty passages; HMT optimism-bias supplementary guidance (Mott MacDonald 2002) | Standard | At source; spot-checked; verified | Optimism bias; own record; switching value; range; scenarios; risk and uncertainty; the table |
| OBR, FER June 2026 and July 2025; EFO March 2026 | Practice / Evidence | At source; verified | Forecast against outturn; 0.4/0.7 pp; fan chart caveat |
| Britton, Fisher & Whitley 1998, *BoE QB*; BoE MPR May 2024 and July 2026; Bernanke 2024 review | Practice / Evidence | At source; spot-checked (Bernanke); verified (fan published to Feb 2026; absent from April 2026) | Fan chart's aim and bands; "on 100 occasions"; "They should be eliminated"; scenarios |
| van der Bles et al. 2019, *RSOS* 6; van der Bles et al. 2020, *PNAS* 117(14); Spiegelhalter 2017 | Evidence | At source; abstract †; abstract †, not cited | Framework; small decrease in stated trust, mostly verbal |
| Mastrandrea et al. 2010, IPCC guidance note; Budescu, Broomell & Por 2009; Wintle et al. 2019, *PLoS ONE*; MoD 2023 | Standard / Evidence | At source; reconstructed †; at source; at source | Likelihood and confidence scales; readers deviate; 66% vs 32%; yardstick with gaps |
| Gneiting, Balabdaoui & Raftery 2007, *JRSS B* 69; Good Judgment Open FAQ; WWRP/WGNE verification page; Wikipedia (calibration; Brier) | Evidence / Practice / secondary | Summary †; at source; at source; secondary | Calibration and sharpness; Brier |
| GO-Science 2024, *Futures Toolkit*; Uncertainty Toolkit for Analysts ch. 6; ONS 2025, National population projections | Standard / Practice | At source; verified | "Scenarios are not predictions"; even number; front-load caveats; "Projections are not forecasts" |
| Choi & Varian 2012 (2011 PDF); Lazer et al. 2014 (DASH record); ONS Data Science Campus 2019 | Evidence / Practice | At source; abstract †; at source | Predicting the present; "more than double" (reporting *Nature*); not predictions of GDP |
| The Conference Board, Description of Components; BCI Handbook 2001 (incl. Beckman) | Standard / Practice | At source; verified (inserted word removed) | "Historically"; conformity and timing; real-time record |
| US DOJ/FTC 2023 Merger Guidelines; CMA129 (rev. 3 Sept 2026); ONS Business demography 2024 | Standard | At source; verified | HHI and thresholds; no UK thresholds; births and deaths; no "churn" |
| Wikipedia, "Survivorship bias" | secondary | At source, marked | Plain statement |
| Version 1 Ch 5 *Comparing places and scenes without a league table* (archived); Style Guide v1.5 §12; Decision Book Ch 6, 8, 10, 15, 16 | Nightlife Culture | At source (repo); not re-traced by the verifier | Identity/conditions; place-centred default; cropping rule; "beats"; the gate; conflict log |

## 12 · Version 2 — Chapter 8: Automation without admin (6 October 2026)

*Legend as §5 and §10. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (twelve sources; one reshaped sentence corrected); "verified" — the independent verification pass re-traced it (about 400 strings on some 125 pages; ten wrong, ten truncated, five numbers restated, all corrected in draft 2). No web search was available to any agent. "(read once)" — single pass, so marked in the chapter (four remain after the verifier's pass). "Secondary" — reached through a named reproduction. "Unreached" — sought, not opened; nothing quoted. Developer documentation rarely carries a date; every limit, price and term is as read on 6 October 2026.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Government Analysis Function, *Data visualisation: building and managing dashboards* (GSS Presentation Champions, 6 Feb 2026) | Standard | At source; spot-checked; verified | "is a digital service"; "not an appropriate project for a single person or for temporary staff"; "Always make it clear which dates or period"; change notes; six-month retirement banner; archive incl. code |
| GOV.UK publishing guidance: *Write change notes*; *Withdraw and unpublish*; *Statistics* content type; withdrawn-page furniture (COVID-19 stay-at-home guidance) | Standard / Practice | At source | "Do not say the page has been updated without saying what has changed"; withdrawal banner keeps the address; four weeks' notice |
| Eurostat, *Glossary: Timeliness*; European Statistics Code of Practice 2017 Principle 13 | Standard | At source; title only (alt text) | Timeliness vs punctuality |
| UK Statistics Authority, *Code of Practice for Statistics* 3.0 (Autumn 2025), practices 2.4, 3.1, 3.5, 3.6, 3.9, 8.4, 9.7, 10.7 | Standard | At source; verified (3.5 and 9.7 tails restored) | Release calendar; revisions; advance notice of removals; continued availability |
| data.gov.uk / National Data Library: *Managing published data*; *About*; *API documentation*; *Accepted DCAT and data.json fields* | Standard | At source; verified | "a single dataset and add new data"; "should not delete"; no key/no limits; "now known as the National Data Library"; UK frequency field |
| W3C *Data on the Web Best Practices* (Rec. 31 Jan 2017; FPWD 24 Feb 2015; Implementation Report 2016) | Standard / Evidence | At source (BP5, 7, 8, 11; versioning intro); BP21/22/27/28 unreached (truncation); draft marked as draft | Version indicator; series URIs; "none of the data catalog solutions implement" BP27 |
| W3C *Data Quality Vocabulary* (WG Note, 15 Dec 2016) | Standard (non-normative) | At source; ISO 25012 original unreached | Currentness and timeliness relative to a use |
| W3C *DCAT 3* (Rec. 22 Aug 2024) §5.1, §6.4; DCAT 3 RDF; SEMIC *DCAT-AP 3.0.0* (14 Jun 2024); DCMI *accrualPeriodicity* (2020); DCAT-US v1.1 (2014) | Standard | At source; DCAT 3 verified; `accrualPeriodicity`, §6.7, §11–12 unreached (truncation) | Issued/modified; three-way absent-value note; three meanings of "frequency"; repeating interval as "modified" |
| ONS *National Accounts Revisions Policy* (updated Jan 2026; notice 31 Mar 2026); ONS time series ABMI page; ONS release calendar | Standard | At source; verified ("Provisional" label removed) | Revision vs correction; "back to 1997"; "Next release" furniture |
| FRB St. Louis *ALFRED*; Bank of England real-time database | Practice | At source; unreached (robots) | Vintages |
| Bowers, Stanton & Zittrain, *CJR* 21 May 2021; Klein et al. 2014 *PLoS ONE* 9(12); Lawrence et al. 2001 *Computer* 34(2); Pew, *When Online Content Disappears* (17 May 2024) | Evidence | At source (CJR is the authors' account; report unreached); verified (Pew "as of October 2023" restored); spot-checked (Pew) | Link and reference rot base rates; 21% of government pages; "one out of five" |
| Open Data Barometer 4th ed. (2017/18); Global Open Data Index methodology (archived); Harvard LIL *Data.gov Archive* (6 Feb 2025) | Evidence / Practice | At source | 74% up to date; the instruments stopped; third-party archive |
| Google Search Central, *Byline date* (10 Dec 2025); Fogg 2002 guideline 8; Nielsen 1996 item 9; Nielsen heuristic 1 (1994/2024) | Practice / Evidence (perception) | At source | Thin evidence that stale costs trust; "web gardener" |
| Ivanković et al. 2021 *JMIR* 23(2) | Evidence | Unreached (three routes) | — |
| GDS *API technical and data standards* (2018; upd. 19 Jul 2024); *Managing your live API* (2020; upd. 9 Sep 2026); *Setting API service levels* (2019; upd. 9 Sep 2026); API design collection; api.gov.uk; Technology Code of Practice | Standard | At source; verified | "try to give users 6 months notice"; beta needs less; "even if you have spare capacity"; "1 in 20 … 2 hours a day" |
| RFC 6585 (2012) §4; IETF draft-ietf-httpapi-ratelimit-headers-11 (23 May 2026); RFC 9110 §10.2.3; MDN *Retry-After* | Standard / secondary | At source; verified; RFC 9110 unreached (truncation); MDN marked secondary | 429; Retry-After MAY; counting undefined; no standard quota header |
| Open Government Licence v3.0 (via SPDX); TfL Transport Data Service terms (OGL v2.0 basis) | Standard (licence) | Secondary (SPDX; National Archives page loops), spot-checked, verified; TfL at source, verified | "does not guarantee the continued supply"; "as is"; "revise this Licence without notice" |
| TfL Unified API FAQ and Products; Companies House rate limiting; ONS developer hub, bots guide, retirement guide; Nomis API help; data.police.uk call limits and About; OS rate limiting policy, Zoomstack, Maps API, Vector Tile API, API branding; FSA FHRS API help and open data; EA flood-monitoring API reference | Standard (platform) | At source; ONS bots spot-checked; verified | The table of limits; idle-account deletion; "ban without notice"; beta and breaking changes; Deprecation/Sunset/Link and 404; "rolling blackouts"; 25,000 cells; snap points; 600/50 per minute; one "depreciated" version; "no guarantee of service level" |
| OSMF Nominatim Usage Policy; OSMF Tile Usage Policy | Standard (operator policy) | At source; tile policy spot-checked; verified | 1/s and 4/min for scheduled scripts; "no SLA or guarantee"; 7-day cache; no bulk, no offline; "Our tile servers are not" |
| Skiddle API page; GitHub Skiddle/web-api (archived 30 Apr 2024) | Standard (platform) | At source; verified | Beta; "continually changed"; "non-commercial use only"; listings only |
| Ticketmaster Getting started; Discovery API v2; Terms of Use (27 Jun 2023) | Standard (platform) | At source; terms spot-checked; verified ("Further, we reserve" restored) | 5000/day, 5/s; "reasonable periods"; "a large number of calls … not primarily in response to direct user actions"; "at any time" |
| Eventbrite developer site; DICE; Resident Advisor; See Tickets; Fatsoma | — | Unreached (script-only; 401/404/403/shell) | No public terms to read |
| Spotify: rate limits; quota modes; blog 27 Nov 2024; blog 15 Apr 2025; February 2026 migration guide; Developer Terms v10 (15 May 2025); Developer Policy (15 May 2025) | Standard (platform) | At source; III.13/III.5 spot-checked; verified (non-commercial clause is Policy §IV.2) | Rolling 30 s; 5 users; "Effective today" list; organisations only, 250k MAUs; dev-mode narrowing; III.13 derived metrics; III.5; no store/aggregate; "without notice"; "no obligation to maintain" |
| YouTube Data API Getting started (14 Sep 2026), Quota cost (15 Sep 2026), Revision history (1 Jun 2026 entry) | Standard (platform) | At source; verified (strings re-pointed to their pages) | "A search query costs 1 unit"; search.list bucket of 100/day |
| MusicBrainz rate limiting ("As of 2012-01-08"); Last.fm API ToS; SoundCloud guide and rate limits; Bandcamp developer | Standard (platform) | At source; SoundCloud read once | 1/s and 503; 100 MB cap, non-commercial; 15,000 stream calls; labels only |
| Schroepfer, Facebook Newsroom 4 Apr 2018; TechCrunch 29 Mar 2023 (Mehta); docs.x.com pricing; Reddit Data API Wiki (11 May 2026) | Standard (announcement) / secondary / Standard (platform) | At source; verified ("So starting today"); TechCrunch secondary; Reddit 2023 post unreached | "Starting today"; "effective today"; 2023 tiers; pay-per-usage, 3M reads; 100 QPM |
| Google Maps Platform Terms (26 Aug 2026) §1.3(c), §3.2.3 | Standard (contract) | At source; verified | 12 months with exceptions; no caching; no non-Google map nearby |
| Treynor Sloss, Dahlin, Rau & Beyer, *ACM Queue* 15(2), 2017 | Practice (adjacent domain) | At source; spot-checked; verified; product arithmetic the chapter's | Intersection rule; "extra 9"; "design for graceful degradation" |
| Google SRE Book ch. 1, 3, 4, 5, 6, 22, 24, App. A (sre.google; year not on pages) | Practice (adjacent domain) | At source; verified | 100% wrong target; SLI/SLO/SLA; error budget; Chubby outage; alerts/tickets/logging; golden signals; "HTTP 200 … wrong content"; toil; Geisser; backoff; "code path you never use"; cron; availability table |
| Google SRE Workbook ch. 2 (Table 2-1), ch. 13 (Sodt, Maravić et al.) | Practice | At source; spot-checked; verified (idempotent mutation re-attributed here) | Freshness SLO forms; "Stale data is almost always better than incorrect data"; idempotency |
| cronie crontab(5) (2012-11-22) and cron(8) (2013-09-26; man7 copy 3 Aug 2026) | Standard (reference) | At source; verified; inference from silence marked | Mail is the only channel; DST missing hours; no notion of failure |
| GitHub Docs: schedule event; Pages limits; Actions billing; Online Services SLA | Standard (platform) | At source; spot-checked; verified; SLA unreached (HTTP 500) | 5 min; "may be dropped"; start of hour; 60 days; last-modifier notifications; IANA timezone; 1 GB/100 GB; commercial clause; free for public repos |
| Healthchecks.io docs; Cronitor heartbeat docs; Monte Carlo *What is data observability?* (31 Jul 2025, mod. 25 Sep 2026) | Practice (vendor) | At source | Dead man's switch; pillars renamed |
| RFC 9111 (STD 98, 2022) §1, 4.2, 4.2.4, 4.3, 4.3.3, 5.1, 5.2.2; RFC 5861 (Informational, 2010); MDN Cache-Control and ETag | Standard / secondary | At source; verified (§4.3.3 tail restored); RFC 9110 §8.8.3/§13 unreached | Fresh/stale/lifetime/Age/max-age; MUST NOT serve stale unless; stale-while-revalidate; stale-if-error |
| Fowler, *CircuitBreaker* (6 Mar 2014); Nygard, *Release It!* 2nd ed. excerpts ch. 1, 4 (2018); Azure *Bulkhead* (19 Mar 2026); AWS Well-Architected REL05-BP01 | Practice | At source; verified; Nygard ch. 5 unreached | Breaker definition and fallback; "Integration points are the number-one killer"; bulkhead; "Invalidating or emptying local state as a result of a failed refresh" |
| Willison, *Git scraping* (9 Oct 2020); *Baked Data* (28 Jul 2021); Datasette publish docs | Practice | At source; verified (splice corrected) | Definition; benefits; "at most a few times a day"; 6,26,46 cron and his reason |
| Protomaps *PMTiles* docs and basemap downloads; DuckDB-Wasm overview | Practice | At source; verified | Single-file archive; range requests; read-only; 120 GB planet; 4 GB |
| Cloudflare Pages limits (5 Sep 2026) and Functions pricing (8 Sep 2026); Netlify pricing (plan note 4 Sep 2025); Mapbox pricing and map-loads glossary; MapTiler Cloud pricing | Standard (platform / price list) | At source; verified (12-hour session re-pointed to glossary) | 25 MiB; "free and unlimited"; 300 credits, paused; 50,000 loads, $5/1,000, 12 hours; 100k requests, pause, $30 |
| GAO-19-471 (11 Jun 2019); Winters, Manshreck & Wright, *SWE at Google* ch. 1; Eghbal, *Roads and Bridges* (14 Jul 2016); Avelino et al. 2016 (arXiv:1604.06766); Wikipedia *Software maintenance*, *Bus factor*; Tidelift 2024; xkcd 2347 | Evidence / Practice / secondary | At source; verified; Avelino abstract †; Tidelift unreached; xkcd not quoted | 80% of $90bn on O&M; "programming integrated over time"; Hyrum's Law; unpaid maintainers; 65% at TF ≤ 2 |
| web.dev *Web Vitals* (31 Oct 2024); *How the thresholds were defined* (McQuade & Pollard, 7 May 2025) | Practice (platform) | At source; verified | 2.5 s / 200 ms / 0.1; 75th percentile; 10% of origins; 3.5% and 42% |
| HTTP Archive *Web Almanac 2024* Page Weight and Performance; *Web Almanac 2025* Page Weight and Performance (15 Jan 2026) | Evidence | At source; page weight spot-checked (one reshaped sentence corrected); verified (one sentence re-attributed to 2024) | 2,311 KB; 558 KB JS; 43%/44%/48%; "devices and networks people can afford" |
| Russell, *The Performance Inequality Gap, 2024* | Practice (reasoned model) | At source; verified ("~" and "Conservatively" restored); later edition unreached | ~$350–375 device; 7.2 Mbps/94 ms; ~1.3 MiB/650 KiB; 2.5 MiB/100 KiB; "15-25% as fast" |
| Google/DoubleClick, *The need for mobile speed* (8 Sep 2016) | Evidence (vendor; weak) | At source; verified | "53% of visits are likely to be abandoned"; n=3.7K footnote |
| GOV.UK Service Manual, *Building a robust frontend using progressive enhancement* (upd. 27 Sep 2024); *Designing for different browsers and devices* (upd. 30 Jan 2026); Herlihy, GDS blog 21 Oct 2013 | Standard / Evidence | At source; Herlihy spot-checked; verified (title corrected) | "functional using only HTML"; no SPA; failure list; "1.1% of people … (1 in 93)"; 0.2/0.9 |
| Ofcom *Connected Nations 2025* (19 Nov 2025) and *2024*; *Adults' Media Use and Attitudes 2025* (7 May 2025) | Evidence (regulator) | At source; verified | 96%/88%; 18% smartphone-only; 30% DE vs 9% AB; 49%/35%/74%; 6% |
| Mapbox Vector Tile Specification 2.1 (2016; via raw file); Mapbox *Vector tiles introduction*; MapLibre README and site | Standard (open spec) / Practice | At source; verified (processing-power sentence confirmed with decoy) | Encoding; styled at runtime; more processing power on device; BSD fork |
| ONS *Digital boundaries* (4 Oct 2023); Open Geography Portal records BFC and BSC (Dec 2024 LADs; WFS and Feature Layer sizes); ONS administrative geography; Census 2021 geographies | Standard | At source; verified (like-for-like sizes; BGC/BUC unreached, rate-limited) | BFC/BFE/BGC/BUC/BSC; 127,631,360 vs 1,671,168; "first Thursday in May"; two-owner licence |
| Mapshaper reference and simplification guide; TopoJSON README; Leaflet homepage; Bundlephobia (leaflet 1.9.4, maplibre-gl 6.12.0); Tippecanoe README; OSM wiki *Tile disk usage* (22 Sep 2026); Protomaps cost calculator | Practice / secondary / Evidence (community) | At source; verified; Bundlephobia version unmatched; calculator not quoted | Visvalingam default; "small polygons can disappear"; 80% reduction; 42 KB vs ~287 KB; 500K tile ceiling; 1.7 PB/135 bn |
| W3C WAI *Complex Images* (8 Apr 2026); WCAG 2.2 Understanding SC 2.5.1, 2.5.7, 2.1.1, 1.4.1; WAI RDWG *Accessible Maps* (2012); Analysis Function *Data visualisation: colours* (upd. 12 Feb 2026); GOV.UK Design System patterns and components; IBM Carbon; PatternFly; Google *Data Studio — data freshness* (5 Oct 2026) | Standard / Practice | At source; verified (2.5.1 and 2.5.7 tails restored); design-system negatives read once | Two-part alternative; map examples for drag and pinch; "downloadable data table"; five blues; no freshness pattern; "bottom left corner" |
| Nightlife Culture: *Vibe Setting Framework — Seeing the System* (confidential); Decision Book ch. 8, 15, rule register; Style Guide v1.5; version 1 Ch 1 and 8 (archived) | Nightlife Culture | At source (repo); not re-traced by the verifier | "maintained … or extractive" (cited as in Ch 1); DTA-05/06, BRF-15, BRK-18, DSH-01–21; seven tests; founding failure |

## 13 · Version 2 — Chapter 9: Measuring a vibe (6 October 2026)

*Legend as §5 and §10. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (fourteen sources; forty strings; all held); "verified" — the independent verification pass re-traced it (about 150 fetches across some 115 sources; nine wrong, fourteen truncated or over-glossed, all corrected in draft 2). No web search was available to any agent. This chapter's literature was the least open so far: † marks an abstract; "secondary" a quotation reached through a named reproduction; "reconstructed" an abstract rebuilt from an index record; "(read once)" a single pass (five remain). "Unreached" — sought, not opened; nothing quoted.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Böhme 1993 *Thesis Eleven* 36; Anderson 2009 *Emotion, Space and Society* 2(2) | Critical scholarship | Unreached; fragments secondary via Michels 2015 | The made and excess registers' founding texts |
| Michels 2015, *Geographica Helvetica* 70 | Evidence (methods essay) | At source (open); verified | "aesthetic work"; three steps; "extremely difficult to be analytically precise" |
| Sumartojo & Pink 2018 (Routledge); Edensor 2012 *EPD* 30(6) | Critical scholarship / Evidence | Publisher description; abstract † (method only); verified | No "measure" claim; atmospheres "coproduced by visitors" |
| Garcia-Mispireta 2023, *Together, Somehow* (Duke) | Evidence (ethnography) | Publisher description only; verified (a reviewer's blurb on the page not quoted as the description's) | "may hide exclusions and injustices" |
| ISO 12913-1:2014; ISO/TS 12913-2:2018; ISO/TS 12913-3:2019 (withdrawn 8 May 2025); ISO/TS 12913-3:2025 | Standard | Catalogue pages at source; texts unreached; definition, methods and attributes secondary via Mitchell et al. 2020; formulae secondary via the Soundscapy tutorial; verified | The perceived register's standard; "vibrant" as a derived diagonal |
| Axelsson, Nilsson & Berglund 2010 *JASA* 128(5); Russell 1980 *JPSP* 39(6); Russell, Ward & Pratt 1981 *E&B* 13(3); Russell & Pratt 1980 | Evidence | Abstract † (Europe PMC); at source (archive PDF); abstract †; unreached | 100 listeners, 50 excerpts, 116 scales, 50/18/6%; the circle; 105 adjectives, 323 subjects |
| Mitchell, Oberman, Aletta et al. 2020, SSID Protocol, *Applied Sciences* 10(7); Mitchell, Aletta & Kang, Soundscapy tutorial (2022 JASA-EL unreached) | Evidence (protocol) / Practice | At source; spot-checked; verified | 100 responses per location; 4000/59/10; per-respondent coordinates; "percent of people likely to perceive" |
| Lionello, Aletta, Mitrovic & Kang 2021 *Frontiers in Psychology*; SATP (Zenodo v1.2; Lam et al.; Watcharasupat et al.) | Evidence | At source; spot-checked; verified; abstracts † | Non-equidistant scales "particularly on the vibrant-monotonous direction"; translation validity |
| Aletta, Kang & Axelsson 2016 *LUP* 149 | Evidence (review) | Accepted manuscript at source (White Rose); verified | Descriptor / indicator; sources over levels (reporting Axelsson); 52% v 21% (Ricciardi) |
| Scannell & Gifford 2010; Williams & Vaske 2003 *Forest Science* 49(6); Stedman 2002; Lewicka 2011; Jorgensen & Stedman 2001 | Evidence | At source; at source, spot-checked, verified; abstract †; unreached; unreached | Framework; 12 items, alphas 0.81–0.94, four items, the ceiling |
| DCMS/Verian, Community Life Survey 2024/25 (questionnaire; technical report; release) | Standard | At source; verified | Belonging item; "a few minutes walking distance"; 62%; 177,749; ABOS; 19.86% |
| Sung, Lee & Cheon 2015; Delclòs-Alió & Miralles-Guasch 2018; Jacobs 1961 | Evidence | Abstracts †; unreached (secondary) | Jacobs's four conditions operationalised |
| Kotler 1973; Bitner 1992; Echtner & Ritchie 1993; Uhrich & Benkenstein 2010; Turley & Milliman 2000 | Evidence | Unreached (tertiary, not quoted); abstract †; abstract †; unreached; unreached | Atmospherics; servicescape; structured + unstructured |
| Frank 2012 *The Baffler*; Markusen 2012 *Createquity* | Critical journalism / scholarship | At source; verified | "no one seems to be exactly sure what vibrancy is"; ArtPlace "not able to measure vibrancy directly" (with its continuation); "fuzzy concept" |
| ONS 2017 *Public perceptions of crime*; ONS 2022 *Perceptions of personal safety*; Farrall et al. 1997 †; Gray, Jackson & Farrall 2008 †; CSEW questionnaires | Standard / Evidence | At source; at source; abstracts; unreached (HTTP 400) | The contrast case: "magnify"; questions dropped 2017–18 |
| Brown 2017 *Transactions in GIS* 21(1); Brown & Kyttä 2018; Brown & Fagerholm 2015; Kahila-Tani et al. 2019; Brown & Kyttä 2014 | Evidence | Abstracts † (Crossref/Aalto); 2014 unreached; verified | Who marks, how much, where; "small-group elitist activity"; "little evidence … used" |
| Reed, Paddon, Wilkinson & MacLeod 2025 *Sexualities* 28(3) | Evidence | At source (open; method only); verified | n = 12; "We make no claim"; "always partial" |
| Kosmala et al. 2016; Haklay 2010; Haklay 2016; Nielsen 2006 | Evidence / Practice | Published abstract † (preprint differs); abstract †; abstract †; at source; verified | Volunteer accuracy presupposes ground truth; "can be fairly accurate"; 90-9-1 |
| Chambers 2007 IDS WP 296; Holland (ed.) 2013; Davies & Dart 2005 MSC Guide; Wang & Burris 1997 | Practice / Evidence | At source (full); publisher page; at source (full; ch. 6 unreached), spot-checked, verified; abstract † | Participatory numbers and their conditions; MSC's "less time-consuming ways" list; photovoice goals |
| Schilling, Watkins & Watkins 2002; Aspiration Tech; Seeds for Change; NN/g dot voting 2019; Reips & Funke 2008 †; Diamantopoulos et al. 2012; Bowling 2005; Allen et al. 2022 | Evidence / Practice | At source; at source; at source; at source; abstract; at source (open); extract only; unreached; verified | The living histogram's artefact; spectrum lines as conversation; VAS; single items |
| Lorenz et al. 2011 *PNAS* †; Muchnik, Aral & Taylor 2013 *Science* † (editor's summary) | Evidence | Crossref abstracts; verified | Social influence narrows without improving |
| Bethlehem 2010 †; Couper 2000; BIS/NERC 2016 press release; TIME 2009; Stanford Deliberative Democracy Lab; Fung 2006 | Evidence / Standard / Practice | Abstract (RePEc); unreached; at source; at source; at source; at source (author PDF); verified | Self-selection; Boaty McBoatface; "this is an Internet poll"; sample first; "frequently quite unrepresentative" |
| Orstad et al. 2017 *E&B* 49(8) †; Solymosi et al. 2021 † | Evidence (systematic reviews) | Abstracts; spot-checked; verified | Perceived and objective place "related but distinct"; 8.2% |
| Arnstein 1969; Cabinet Office *Consultation principles* (2012; 2018); LGA Gunning guide 2019; Moseley [2014] UKSC 56 | Evidence / Standard / secondary | At source (reproduction); at source; at source; unreached; verified | Consultation rung; "Explain the responses … and how these have informed the policy"; "conscientious consideration" |
| Sjoberg, Mellon & Peixoto 2017 *PAR* 77(3) †; Fumagalli, Laurie & Lynn 2010 †; Cleary & Balmer 2015 †; van der Wal et al. 2016 † | Evidence | Abstracts; Sjoberg spot-checked; verified | 57% at n = 399,364; tailored report-back; feedback and retention |
| Feedback Labs; Keystone Accountability; Boyle & Harris 2009 (nef/NESTA); Ostrom 1996; Parks et al. 1981 | Practice | At source; at source; at source (full), verified; unreached; unreached (footnoted by Boyle & Harris) | Loop stages; "Constituent Voice"; co-production's boundaries |
| GIDA 2019 CARE one-pager; Carroll et al. 2020 *Data Science Journal* 19 | Standard (principles) | At source; verified | Responsibility; "openly available evidence" |
| Breiger 1974 †; Freeman 2003 (NAP); Génois & Barrat 2018 *EPJ Data Science*; Eagle, Pentland & Lazer 2009 *PNAS*; Crandall et al. 2010 †; Neal et al. 2021; McPherson et al. 2001; Feld 1981 †; Kossinets & Watts 2009 †; Kossinets 2006 †; Marsden 1990 †; Borgatti & Halgin 2011; Borgatti, Carley & Krackhardt 2006 | Evidence | Abstract; at source by the agent (verifier unreached); at source, spot-checked, verified; at source (PMC), verified; abstract; at source; at source, verified; abstract; abstract; abstract; abstract; unreached; unreached | Duality; co-presence v contact; 95% off-campus; null model; baseline v inbreeding; boundary specification |
| Silver, Clark & Navarro 2010 *Social Forces* 88(5); Silver & Clark 2014 *Cultural Studies*; Silver & Clark 2016 *Scenescapes*; Borer, *AJS* review; Rindzeviciute 2019 | Evidence / Reading | At source (authors' PDFs), spot-checked, verified; publisher blurb; at source (authors' site); read once | Coders 1–5; r = .8; face validity; performance score (2014); fifteen pole-pairs (2014); "organizational directories" (Silver & Clark, via Borer) |
| McKercher & Tse 2012 †; Dick & Basu 1994 †; Oppermann 2000; Zeithaml et al. 1996; Falk | Evidence | Abstracts; read once; unreached | Intention ≠ return; loyalty = attitude + patronage |
| Oldenburg 1989 (via Steinkuehler & Williams 2006 *JCMC* and Project for Public Spaces); Jeffres et al. 2009 †; Finlay et al. 2019 †; Rhubart et al. 2022 *Socius* | Evidence / secondary | Secondary; abstracts; at source (open); verified | The regulars; "availability does not necessarily mean access" |
| TfL 2017 *Review of the TfL WiFi pilot*; Geographic Data Service SmartStreetSensor record; Martin et al. 2017 | Practice | At source; at source; abstract (read once); verified | Device counts, Wi-Fi-off loss, MAC randomisation |
| Lizardo 2014 †; The Audience Agency; Sun et al. 2013 †; Peterson & Kern 1996 | Evidence / Practice | Abstract; at source; abstract; unreached | Read; not cited in the body |
| De Nadai et al. 2016 (arXiv 1603.04012); De Nadai et al. 2016b (arXiv 1608.00462) | Evidence | At source (full); verified; one sentence | "assumed" proxy; 34%; OLS; 77%; day and night |
| Cranshaw, Schwartz, Hong & Sadeh 2012 (ICWSM) | Evidence | At source (full); verified | 27 residents; the five biases; the missing district |
| Sulis, Manley, Zhong & Batty 2018 *JOSIS* 16; Sobolevsky et al. 2015 (arXiv) | Evidence | At source (open); verified; at source | r = 0.43 "incongruous"; card-spending normalisation |
| Hecht & Stephens 2014 (ICWSM); Malik et al. 2015 † | Evidence | At source; abstract; verified | 24.4×; geotag users predicted by income, urbanity, age, ethnicity |
| Salganik, *Bit by Bit* §2.3, §2.4.2 | Practice (open textbook) | At source (each sub-page); verified | The ten characteristics; construct validity |
| Meng 2018 *AoAS* (via Bradley et al. 2021 *Nature* 600); Lazer et al. 2014 *Science* † (DASH) | Evidence | Unreached at source; secondary at source, verified; abstract | Big Data Paradox; Google Flu |
| Dodds et al. 2011 *PLoS ONE*; Mitchell et al. 2013 *PLoS ONE* (+ arXiv preprint); Schwartz et al. 2013 | Evidence | At source; verified; coefficients from preprint | Three limits; "how people appear to others"; Spearman 0.328 |
| Jaidka et al. 2020 *PNAS* 117(19) | Evidence | Reconstructed abstract (OpenAlex); full text unreached; verified by position | Dictionaries "inconsistent"; supervised up to r = 0.64 |
| Eichstaedt et al. 2015 †; Brown & Coyne 2018 *PeerJ* | Evidence | Abstract; at source (open); verified | The sign flip |
| Blodgett, Green & O'Connor 2016 (EMNLP; arXiv); Mislove et al. 2011 †; Pew 2019 *Sizing Up Twitter Users*; Ofcom *Online Nation 2025*; Olteanu et al. 2019 *Frontiers in Big Data* | Evidence / Critical scholarship | At source; abstract; at source; at source; at source; verified | 64.0 v 80.4 recall; 10%/80%; 39%; bias definitions |
| Salesses, Schechtner & Hidalgo 2013 *PLoS ONE*; Naik et al. 2014 †; Dubey et al. 2016 †; Quercia et al. 2014/2015/2016 †; Quintana et al. 2025 † | Evidence | At source; abstracts; verified | Place Pulse raters (76% male, median 28, 91 countries); "lively"; models predict raters' judgements |
| Barrett, Adolphs, Marsella, Martinez & Pollak 2019 *PSPI* 20(1); Mohammad 2022 *Computational Linguistics* 48(2) (arXiv) | Evidence / Practice | At source (truncated ~100k; closing sections unreached), spot-checked, verified; at source (preprint), verified | Three shortcomings; "what one is trying to convey or what is perceived" |
| Regulation (EU) 2024/1689 — recitals 18, 44; Articles 3(39), 5(1)(f), 113 | Standard (law) | At source (EUR-Lex; Commission Service Desk consolidated text); verified | The biometric emotion-inference prohibition and its stated reasons |
| Mitchell et al. 2021 *JASA* 150(6) †; Spotify Web API reference (audio features); Park et al. 2019 *NHB* †; Edmans et al. 2021 (SSRN) | Evidence / Standard (platform) | Abstract; at source; abstract, verified (referent corrected); abstract | Prediction from recordings; valence defined not derived; song positivity as proxy |
| Csikszentmihalyi & Larson 1987 (reconstructed); Kahneman et al. 2004 *Science* †; Kahneman & Riis 2005; NRC 2013 *Subjective Well-Being* Summary; MacKerron & Mourato 2013 †; Seresinhe et al. 2019 *Sci Rep*; Bakolis et al. 2018 *BioScience* | Evidence / Standard | Reconstructed; abstract; truncated (not used); at source, verified; abstract; at source, verified; at source, verified | ESM/DRM; "often regarded as the gold standard"; Mappiness; Urban Mind |
| ONS *Personal well-being user guidance* (14 Jan 2025); *FAQ* (26 Sep 2018); *QMI* (14 Jan 2025); *UK Measures of National Well-being user guide* (18 Sep 2026); *Review … 2022–23* (5 Jul 2023); ONS 2011–12 testing reports | Standard | At source; spot-checked; verified (stems with anchors; review and guide separated); unreached (web archive) | The four questions; cognitive testing; context and mode; bands and why; floor 50/5; CV bands; 34,000; 118; 44→60 |
| Dolan, Layard & Metcalfe 2011 (CEP SP23); OECD 2013 *Guidelines* (NCBI Bookshelf; Ch. 1 unreached); OECD 2025 *Update* †; What Works Wellbeing 2017; Krueger & Schkade 2007 † | Practice / Standard / Evidence | At source, verified; at source, verified; landing-page abstract; at source; abstract | Three accounts; scale, labels, order, context, mode; shortened core module; local indicators; test–retest |
| AERA/APA/NCME 2014 *Standards*, ch. 1; Cronbach & Meehl 1955; DeVellis & Thorpe 2021 (5th ed.); Willis 2004; Beatty & Willis 2007 †; Boateng et al. 2018; Nevo 1985 (reconstructed); Price, Jhangiani & Chiang 2015; Jarvis et al. 2003 †; Diamantopoulos & Winklhofer 2001 †; Kelley 1927; Messick | Standard / Evidence / Practice | At source (open PDF), spot-checked, verified; at source, verified; publisher page, verified; publisher page; abstract; at source, verified; reconstructed; at source, verified; abstracts; unreached | Validity for a use; five sources; nine steps; conventions; face validity "at best a very weak kind"; formative v reflective |
| Birt et al. 2016 †; Lincoln & Guba 1985 (via qualres.org); Tracy 2010 †; Candela 2019 † | Evidence / secondary | Abstract; secondary, verified; abstract; abstract | Member checking and its cautions |
| Fetters, Curry & Creswell 2013 *HSR*; O'Cathain, Murphy & Nicholl 2010 *BMJ* | Standard (method) | At source (repository), spot-checked, verified; at source, verified | Fit; confirmation / expansion / discordance; the four cells with silence |
| Nightlife Culture: Vibe Setting Framework (confidential); Decision Book ch. 6, 8, 10, 15 and rule list; Style Guide v1.5; version 1 Ch 4 *The felt layer* (archived) | Nightlife Culture | At source (repo); not re-traced by the verifier | Three registers; human dot plot; "what this changed"; co-production rule; discordance as finding; "extractive" |

## 14 · Version 2 — Chapter 10: Safety, ethics and consent (6 October 2026)

*Legend as §5 and §10. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (seventeen sources; about a hundred strings with controls; every quoted string found); "verified" — the independent verification pass re-traced it (about two hundred fetches; some six hundred strings, figures, dates and section numbers confirmed; five wrong, five misattributed, a dozen reshaped, all corrected in draft 2). Statute read at legislation.gov.uk in the version current on 6 October 2026; regulator pages carry the date shown on the page. Nothing in this ledger is legal advice. "Unreached" — sought and not opened; nothing quoted. No web search was available to any agent.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| UK GDPR Arts 4 (incl. new (2)–(7)), 5 (incl. (3)), 6(1)(a),(ea),(f), 6(5), 6(11), 7, 8A, 9, 13(5)–(6), 14, 17, 21, 25 (incl. (1A)–(1B)), 35, 36, 83, 84A–84D, Annex 1; Recital 26 | Standard (law) | At source; Arts 4 and 84C spot-checked; all verified | Personal data; identifiability; statistical and research purposes; consent and withdrawal; bases; RAS purposes and the two exclusions; special category; transparency for data not from the subject; objection and erasure; by design; DPIA; prior consultation; penalties |
| Data Protection Act 2018 s.19 (omitted 5.2.2026), s.123, Sch 1 Pt 1 para 4 | Standard (law) | At source; verified | The former research safeguards; the Children's Code's statutory footing; the special-category research condition's public-interest limb |
| S.I. 2026/82 (Commencement No. 6, 5 Feb 2026); S.I. 2026/1015 (Commencement No. 9; Information Commission from 30 Sept 2026); S.I. 2026/386 (consequential) | Standard (law) | At source (the third via F-notes); verified | The in-force dates; the regulator's change of identity |
| PECR (S.I. 2003/2426) reg 6 as substituted; Sch A1 (esp. para 5) | Standard (law) | At source; verified | The statistics exception for a site's own analytics |
| ICO anonymisation guidance (published 28 March 2025; under review): about; introduction (1 Apr 2025); "How do we ensure anonymisation is effective?" (page 10 Oct 2025); pseudonymisation | Standard (regulator, non-statutory) | At source; spot-checked; verified | Effective anonymisation; spectrum; singling out and linkability; motivated intruder; release model; "lose control"; NHS k = 5; k-anonymity's limits; educated guesses; the review example | 
| ICO "What is personal data?" (7 Sept 2026); identifiers page (19 Nov 2024) | Standard (regulator) | At source; verified | Pseudonymised data is personal data; context decides identifiers |
| ICO "What is special category data?" (22 Sept 2025; under review) | Standard (regulator) | At source; spot-checked; verified | The intention test; "regardless of how confident"; onlookers "(rightly or wrongly)" to fairness |
| ICO consent: "When is consent appropriate?"; "What is valid consent?" (both 4 Aug 2026); at-a-glance (19 Aug 2026) | Standard (regulator) | At source; both main pages spot-checked; verified | Imbalance of power; "misleading and inherently unfair"; the research withdrawal sentence; "no such thing as 'evolving' consent" |
| ICO legitimate interests (23 Mar 2026, updated for the Act); recognised legitimate interest (23 Mar 2026) | Standard (regulator) | At source; verified | The three-part test and LIA; five pre-approved purposes, none for research |
| ICO the research provisions (landing 3 Mar 2026; safeguards 9 Oct 2025; pre-Act, under review) | Standard (regulator) | At source; verified | Indicative criteria; "to inform the services you provide to them"; still cites Article 89 |
| ICO right to object (25 Mar 2025); right to erasure (10 Jan 2025) | Standard (regulator) | At source; verified | Objection restricted for research; erasure's limits; inform other controllers |
| ICO right to be informed — exceptions (22 Sept 2025); what to provide (15 Jan 2026) | Standard (regulator) | At source; verified | "no automatic exception … public domain"; publish anyway; say the source |
| ICO DPIA: examples of high-risk processing (19 Nov 2024); how do we do a DPIA (18 Feb 2026); when do we need one | Standard (regulator) | At source; verified | The high-risk list and its "when combined" qualifier; seven steps; step 3 consultation; publish; the individual harm list |
| ICO storage and access technologies guidance, "What are the exceptions?" (finalised 29 Apr 2026) | Standard (regulator) | At source; verified | "how your service is used, not about who uses it"; demographic segmentation fails; wifi probes excluded |
| ICO Children's Code: services covered (5 Dec 2024); standards (2 Dec 2024) | Standard (regulator; statutory code under DPA s.123) | At source; verified | "more probable than not"; not-for-profit ISS; standards 10 and 12 |
| ICO Data (Use and Access) Act pages (12 Feb 2026; 19 Jun 2026); gov.uk commencement plans (updated 5 Feb 2026, stale on the Commission) | Standard (regulator; government) | At source; verified | All provisions in force; broad consent and commercial research summarised |
| ICO joint statement on scraping, Bonner (24 Aug 2023); gen-AI consultation response, executive summary (page 13 Oct 2025) | Standard (regulator statements) | At source; verified | "lawful reason … even when it is publicly available"; "invisible processing" |
| ICO Home Office GPS monitoring notice (1 Mar 2024); 23andMe penalty (17 Jun 2025) | Standard (regulator enforcement) | At source; verified; read for the legal point only | Location reveals special categories by inference; postcode with ethnicity as a vector; £2.31m; 155,592 |
| ICO "Crime-mapping and geo-spatial crime data" v3.5 (2014) | Standard (regulator, 2014) | At source; verified | Household pins unfair; heat maps and blocks; "not 'fair game'"; secondary uses; upload frequency |
| ICO "Overview of Data Protection Harms and the ICO's Taxonomy" v1 (Apr 2022) | Standard (regulator framework) | At source; verified | Individual and societal tiers; no harm to place |
| Equality Act 2010 ss.4, 19, 20, 26, 29, 31, 149, 158; Schs 2, 25; Explanatory Notes to s.29 | Standard (law) | At source; s.29 spot-checked; verified | "for payment or not"; indirect discrimination; harassment and s.29(8); reasonable adjustments and accessible format; PSED's reach; positive action; hosting |
| S.I. 2018/952 regs 3–4; GDS/CDDO accessibility guidance (updated 30 Sept 2024) | Standard (law); government guidance | At source; verified | Scope; "bodies governed by public law"; maps and third-party content excluded; WCAG 2.2 AA named by the guidance |
| EHRC Services Code of Practice | Standard (statutory code) | Unreached (403) | — |
| Online Safety Act 2023 ss.3, 4, 9, 10 (incl. (3A)), 12, 20, 21, 23, 35, 55; Schs 1, 13; Crime and Policing Act 2026 (c. 20) noted | Standard (law) | At source; Sch 1 spot-checked; verified (the verifier found 10(3A)) | User-to-user definition; limited-functionality exemption; duties; 48-hour limit for intimate-image reports; children's access assessment; penalties |
| Ofcom: overview of regulated services; "Time for tech firms to act" (16 Dec 2024); illegal-harms statement (upd. 25 Jun 2026); important dates (upd. 24 Aug 2026); children's access duties (upd. 29 Jun 2026); illegal content duties (18 Feb 2026, upd. 25 Jun 2026); U2U Codes (24 Feb 2025); protection of children duties (upd. 1 Apr 2026); compliance guide (upd. 21 May 2025) | Standard (regulator) | At source; the overview, illegal-content duties and Codes verified; the rest agent-only | "services of all sizes"; three months from launch; tiers; 7 million; measures for all; "highly effective age assurance"; £18m / 10% |
| DSIT Online Safety Act explainer (upd. 24 Apr 2025) | Standard (government) | At source; verified | Proportionality; no small-service exemption |
| Sweeney 2002 *IJUFKS* 10(5); Sweeney 2000 CMU Working Paper 3 | Evidence (foundational; working paper) | At source; verified | k-anonymity; Weld; 87% as a 1990 summary-table estimate |
| Machanavajjhala et al., ℓ-diversity (TKDD preprint); Li, Li & Venkatasubramanian 2007, t-closeness | Evidence | At source; verified | Two attacks; "so Alice concludes"; skewness and similarity; "does not deal with identity disclosure" |
| Taylor, Floridi & van der Sloot (eds) 2017 *Group Privacy*; Mittelstadt 2017 *Phil & Tech* 30(4); Floridi 2014 | Critical scholarship | Abstract †, verified; at source (open), verified; unreached | "types, not tokens"; ad hoc groups; group privacy as a third interest |
| Narayanan & Shmatikov 2008; de Montjoye et al. 2013 *Sci Rep*; de Montjoye et al. 2015 *Science*; Rocher, Hendrickx & de Montjoye 2019 *Nat Commun*; Culnane, Rubinstein & Teague 2017; Pandurangan 2014; Strava Engineering 2017 ("Building the Global Heatmap"); DoD memo 3 Aug 2018; Wikipedia "AOL search log release" | Evidence; practitioner; policy; tertiary | At source, verified; at source, verified; abstract †, verified; at source, spot-checked, verified; abstract †, verified; at source, verified; at source, verified; at source, verified; tertiary (NYT unreached) | Re-identification: 8 ratings/99%; four points/95%; four purchases/90%, +22%; 99.98% model estimate; 10% sample; 22M hashes in two minutes; 700 million activities; operational-area prohibition; the case recorded, not relied on |
| Dinur & Nissim 2003; Garfinkel & Abowd 2018 *ACM Queue*; Hawes *HDSR* (title unconfirmed at source); Abowd et al. 2023 arXiv 2312.11283; Abowd & Hawes 2022 arXiv 2206.03524 | Evidence (official accounts; theory) | At source, verified; at source, verified; at source for the figures, verified; abstract †, verified; at source, verified | Ω(√n); 7.7 billion; 219 million / 52 million; 97 million / 3.4 million; 44%; "suppression rules disproportionately impact small population groups" |
| Dwork 2006; Dwork & Roth 2014 | Evidence (foundational; textbook) | At source, verified; at source, spot-checked, verified ("weakens" is not the book's word; "deteriorates" is) | The definition; the promise; the smoker; "a definition, not an algorithm"; kε; "overly accurate answers" |
| US Census Bureau: Abowd blog 17 Aug 2018; press release CB21-CN.42 (9 Jun 2021); "Developing the DAS" (rev. 6 Aug 2026); Abowd et al. TopDown (arXiv 2204.08986 / HDSR; PDF §5.3) | Standard (official); Evidence | At source; verified | ε = 19.61; "exponentially higher"; "aggregate small populations"; noisy measurements; sparse geographies "not reliable" |
| Ruggles et al. 2019 *AEA P&P*; Kenny et al. 2021 *Sci Adv* 7(41); Santos-Lozada et al. 2020 *PNAS*; boyd & Sarathy 2022 *HDSR* | Critical scholarship; Evidence | At source, verified; at source, spot-checked, verified; abstract †, verified; at source, verified | The quarrel: law and precedent; mixed-race precincts undercounted yet predictable; mortality estimates; "epistemic" |
| ONS "Policy on protecting confidentiality in tables of birth and death statistics" (no page date; 2018 revision) | Standard (official statistics policy) | At source; spot-checked; verified | 0/1/2 risky; judgement scaled to sensitivity; secondary suppression; "usually numbers less than three"; rounding to three or five; standard classifications; §4.4 online tools (five; registration; log; legal-obligations statement; "If possible" a limit); Annex B.2 differencing |
| ONS "Protecting personal data in Census 2021 results" (last revised 9 Mar 2023); EAP168 (Aug 2021); Census 2021 QMI (rev. 23 Nov 2023) | Standard (official statistics methodology) | At source; the first spot-checked; all verified | Swapping 7–10%; ~14% perturbed; same cell same key; "high chance" a count of one is swapped/perturbed/imputed; 4/5 variable caps; "will not provide details of which rule"; parameters kept private; "perception of disclosure" (EAP168) |
| Hundepool et al., *Handbook on Statistical Disclosure Control*, 2nd ed. (sdctools.github.io; June 2026), ch. 5 | Standard (method) | At source; verified | Differencing; protection in all linked tables; cell key; rounding bases 3 and 5 |
| OSR *Code of Practice for Statistics* Edition 3.0 ("Autumn 2025"; web "Published: 3 November 2025"), Standard 4 and principles; OSR 2020 "The Public Good of Statistics" | Standard | At source; verified (PDF pp. 1, 3) | 4.3–4.6; "individual and business information"; "Everyone can apply or draw on the Code"; "harm" absent from the principles page |
| ONS "Guidance on intruder testing"; ONS Working Paper 16 (synthetic data pilot); ONS Data Science Campus & Turing (30 Nov 2023) | Standard (official statistics) | At source; verified | "friendly intruders"; half a day; confidence per claim; six levels; "real or perceived risk"; ε = 1; "not an absolute guarantee" |
| GSS/GSR tables guidance (2014; under review) | Standard | Landing page only; PDFs unreached | — |
| Elliot, Mackey & O'Hara, *Anonymisation Decision-Making Framework*, 2nd ed. (UKAN 2020) | Practice | At source; spot-checked; verified | "not a property of the data"; functional anonymisation; data environment; data situation; ten components |
| Hoang, Asano & Yoshikawa 2016 arXiv 1604.08235 | Evidence (read as technology only) | At source; verified | Trilateration; hidden distance defeated; "up to the victim's building"; 2014 report and the hide-distance option |
| Belmont Report (1979); ESRC Framework for Research Ethics — core principles (12 May 2025), consent (7 May 2026), terms (7 May 2026), ethics reviews (12 May 2025); AoIR Ethical Guidelines 3.0 (2019) | Standard (ethics; funder; association) | At source; verified | Individualist baseline; groups as rights-holders without mechanism; cut-off and "cannot then be excluded"; "may be useful to other research-related audiences"; "guidelines, not recipes"; consent from communities; "manifestly impracticable" |
| Dickert & Sugarman 2005 *AJPH* 95(7); UNESCO Declaration 2005 Art 6(3); CIOMS 2016 Guidelines 7 and 9; Regulation (EU) 2022/868 Recital 31, Art 2(15) | Evidence (ethics); Standard (international); Standard (EU law, not UK) | At source, spot-checked, verified; at source, verified; at source, verified; at source, verified | Consultation is not consent; "legitimate political system"; never a substitute; rights personal and not waivable |
| CSJCA & NCCPE 2012 CBPR ethics guide; Garrison 2013 *STHV* 38(2); Weijer & Emanuel 2000; Banks et al. 2013; ICPHR Position Paper 2 | Practice; Evidence | At source, verified; abstract †, verified; unreached; unreached; unreached | Collective consent and renegotiation; Havasupai: no precedent, avoidance |
| Carroll et al. 2020 *Data Science Journal* 19:43; FNIGC OCAP®; Te Mana Raraunga 2018; Kukutai & Taylor (eds) 2016 ch. 1; Local Contexts TK Labels; Walter & Suina 2019 | Practice (frameworks; rights-holders' statements); Critical scholarship | At source, verified; at source, verified; at source (single pass; verifier blocked by robots); at source, verified; at source, verified; unreached | CARE's scope and "normative foundation"; "specifically First Nations—not Indigenous"; 3.1, 5.2, 6.3; "sovereign entities"; the labels |
| Rambaldi, Chambers, McCall & Fox 2006 (IIED G02957); Ada Lovelace Institute 2021; ODI data trusts 2018 and 2019 report; ODI Data Ethics Canvas (lang file); MIDATA; Camden Data Charter; McAreavey & Das 2013 *IJQM* 12(1); Cornwall 2008 *CDJ* 43(3); Cooke & Kothari 2001; Young 2000/2002 (OUP page); Charlton (UC Press page); Costanza-Chock 2020 *Design Justice* (MIT open) | Practice; Evidence; Critical scholarship | At source, verified; at source, spot-checked, verified; at source, verified (the six-part list unverified, not used); at source; at source, verified; at source, verified; at source, verified; abstract †, verified; unreached; publisher page, verified; publisher page, verified; at source, verified | "Who? and Whose?"; five levels and legitimacy; definitions changed 2018→2019; fifteen headings, none on consent; cooperative withdrawal; a council charter; gatekeepers; "who is participating, in what and for whose benefit"; the slogan's origin |
| UK Data Service consent page; UK Biobank privacy notice (15 May 2025); Zenodo policies; TNA takedown policy; Internet Archive help; *Pro Git* 2nd ed. §1.3; GitHub Docs (removing sensitive data); Mayer-Schönberger *Delete* (PUP page) | Practice; policy; technical | At source; UK Biobank, Zenodo, TNA, IA, Pro Git, GitHub verified | Graded withdrawal; "would not be possible to remove data from research that had already taken place"; tombstone; temporary removal; "no guarantees"; "only add data"; clones |
| eBird sensitive species (mod. 15 May 2026); iNaturalist geoprivacy; NBN Atlas sensitive species (mod. 13 May 2026); Treasure Act 1996 Code of Practice 3rd rev. (2023); PAS policy; EIR 2004 reg 12; Redfin 13 Dec 2021 | Practice; Standard (code); Standard (law, by analogy); company statement | At source, spot-checked, verified; at source, verified; at source, verified; at source, verified; unreached (403); at source, verified; at source, verified | 400 km²; hidden from site-level output; 0.2° cells; statutory-body lists; 10 m square; presumption, named harm, weighing; a decision not to publish |
| Citron & Solove 2022 *BU L Rev* 102; Shelby et al. 2023 arXiv 2210.05791 | Legal scholarship (US); Evidence (review) | At source, verified; abstract †, verified | The typology; "no cognizable harm"; five themes |
| UKSA geospatial ethics (18 May 2021) pp. 3, 5, 6; UKSA public good guidance (22 Jul 2021); NSDEC ethical principles (page 11 Aug 2026); MHCLG IoD 2025 FAQ (upd. 17 Nov 2025) | Standard (official statistics ethics; official) | At source; geospatial spot-checked; all verified | "blight"; "redlined"; ecological fallacy; colour; missing ≠ zero; "stigmatisation"; "not a suitable tool for targeting individuals" |
| Robinson 1950/2009 *IJE*; Wacquant 2007; Wacquant, Slater & Pereira 2014; Sampson & Raudenbush 2004; Sampson 2012 (UCP page) | Evidence; Critical scholarship | Opening only; abstract †; abstract †, verified; abstract †, verified; publisher page | The fallacy's definition; stigma as "action through collective representation"; perceived disorder tracks race and poverty |
| Aaronson, Hartley & Mazumder 2021 *AEJ:EP* 13(4) and Chicago Fed WP 2017-12; Fishback et al. NBER 28146 / *JEH* 83(4); Nelson et al. *Mapping Inequality* | Evidence | Abstract † + WP at source, verified; abstract †, verified; unreached | Effects on ownership, values, rents, segregation; 15–30% / 40%; "at most 4 to 20 percent" (a different quantity) |
| Chainey & Tompson 2012 *Policing* 6(3); Braakmann 2017 *Urban Studies* 54(8); Glaeser, Kim & Luca 2018 *AEA P&P* and 2017 NBER 24010; Barron, Kung & Proserpio 2021 *Marketing Science* 40(1); Cortright 2009 | Evidence | Abstracts †, verified; unreached | police.uk since Dec 2008, "poor cartographic discipline"; 0.6–1.6% price effects of risk; "leading indicator for housing price changes"; 29.2% (nowcasting paper); 0.018% / 0.026% |
| Norwegian Consumer Council *Out of Control* (14 Jan 2020); Forbrukerrådet 15 Dec 2021 and 21 Oct 2025; Datatilsynet decision; Jernigan & Mistree 2009 *First Monday*; Kosinski et al. 2013; Ruberg & Ruelos 2020 *BD&S* 7(1) | Evidence (NGO); secondary; Evidence; Critical scholarship | At source, verified; secondary (complainant), verified; unreached; at source (open), verified; unreached; at source, verified | 135 third parties; 65m NOK upheld; association reveals; "who is or is not 'counted'" |
| Grimmelmann 2015 *Yale JL&T* 17; Discourse trust levels (2018); Pew "State of Online Harassment" (13 Jan 2021); Amnesty release (Nov 2017); eSafety Safety by Design; Gillespie 2018 | Legal scholarship; Practice; Evidence (surveys); regulator framework | At source, verified; at source, verified; at source, verified; at source, verified; at source, verified; unreached | Verbs and adverbs; sandboxing; 41%, seven-in-ten, 51%; 23%, 76%, 32%; three principles |
| Taylor 2017 *BD&S* 4(2); Dencik, Hintz & Cable 2016 *BD&S* 3(2); D'Ignazio & Klein 2020 (MIT open); Design Justice Network principles; The Engine Room / responsibledata.io; Oxfam 2015 (landing); Nissenbaum 2004 *Wash L Rev* 79(1); boyd & Crawford 2012 *ICS* 15(5); Zimmer 2010; Metcalf & Crawford 2016 *BD&S* 3(1); MRS Code of Conduct 2023 | Critical scholarship; Practice; Standard (professional) | At source, verified (all but Zimmer, abstract †, and Oxfam's PDF, unreached) | Three pillars; group level; seven principles; "impact on the community over the intentions"; "unintended consequences"; five rights; two norms; "in public" v "being public"; T3; public data's secondary uses; rules 23, 31, 34, 49 |
| Nightlife Culture: version 1 Chs 4, 7, 8 (archived); Decision Book Chs 8, 10, 15 and rule register; Style Guide v1.5; the brief; Vibe Setting Framework (confidential); Form 696 history (Carly's knowledge; frame only) | Nightlife Culture | At source (repo); not re-traced by the verifier | Threshold three; secondary suppression; fixed categories; "with the reason"; the filter walk; "consent to be found"; "only consented scenes"; community-held; the failure register |

## 15 · Version 2 — Chapter 11: The first screen and the path through it (6 October 2026)

*Legend as §5 and §10. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (sixteen sources; about ninety strings with controls; all held); "verified" — the independent verification pass re-traced it (about 600 strings and figures across about 125 pages; seven wrong, five truncated, three misattributed, all corrected in draft 2). "Unreached" — sought and not opened; nothing quoted. No web search was available to any agent.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Few 2004 "Dashboard Confusion"; Few 2007 "Revisited" | Practice | At source (author PDFs); verified | The single-screen definition; monitoring v analysis |
| Sarikaya, Correll, Bartram, Tory & Fisher 2019 *TVCG* 25(1) | Evidence (survey; 83 dashboards) | At source (preprint); spot-checked; verified | Two genres; "rarely given dashboards their due consideration"; no users consulted |
| Bach et al. 2022/23 *TVCG* "Dashboard Design Patterns" (arXiv 2205.00757; site) | Evidence (pattern catalogue; 144; 42 patterns) | At source; spot-checked; verified | "purely descriptive"; "beyond the scope"; the parameters law; structure and screen-space patterns; 23 workshop participants |
| Srinivasan et al. 2024 *TVCG* (Tableau Public census) | Evidence (25,620) | At source; verified | 75% interactive; median 8 blocks; 21% text; "far simpler" |
| Sultanum & Setlur 2024 (VIS) "From Instruction to Insight"; Sultanum & Setlur 2026 (TVCG/VIS) "Not Always Top-Left" | Evidence (190 dashboards; 18 authors + 16 users) | At source; the 2026 preprint spot-checked; both verified | 92% titled; experts split; titles first 65.6%; "consistently visited first"; self-report limit |
| Tory, Bartram, Fiore-Gartland & Crisan 2021 *CG&A*; Dimara, Zhang, Tory & Franconeri 2021 *TVCG* | Evidence (interviews n = 20; survey 177/164 + 9 interviews) | At source; verified | "data dump"; "jumping off point"; non-users absent; "Only one participant" used a dashboard in the meeting |
| ONS Service Manual: dashboards; interactive charts and animations; annotations; chart text; titles and headings; main points; structuring content; how people read online; choropleth maps; line-chart component; component index | Standard (design system) | At source; dashboards and interactive charts spot-checked; all verified | Justify the dashboard; burden on the user; not one screen; start from the main message; tooltip exemption; 15 words; 60 characters; 28%; "Over half"; "80% … first quarter"; rates not counts; Jenks; keyboard-reachable tooltips; downloads below |
| Analysis Function: building and managing dashboards; testing dashboards; examples (6 Feb 2026); charts (19 May 2022) | Standard (design system) | At source; building/managing spot-checked; verified | Conditions; lifecycle with retirement; inverted pyramid; "Two-thirds"; "rarely meet full accessibility"; breaks in time series |
| GOV.UK Design System: start page; details; accordion; tabs; summary list; structuring forms. GOV.UK publishing guidance: clear structure; titles; summaries; retire outdated content; a withdrawn page | Standard (design system); case | At source; details spot-checked; verified | "just enough information"; hidden-content evidence; "most important information first"; 65 characters; withdrawn banner and history |
| NHS Service Manual: expander; know that a page is up to date; do and don't lists | Standard (design system) | At source; verified | Hiding tested well when overwhelmed; review dates unnoticed near the footer |
| Feng, Deng, Peck & Harrison 2018 CHI | Evidence (n = 830) | At source; verified | Search adopted 66.7–80.6%; "deeply personal" |
| Kim, Reinecke & Hullman 2017 CHI | Evidence (n = 378) | At source; verified (the 4.08 re-attributed) | Predict-and-explain −4.08 on moderately familiar data; predict alone −2.30; 1.27–1.78 on unfamiliar with explanation; nothing on familiar |
| OECD Better Life Index landing; OECD responses page; OECD Statistics WP 2018/03; Stefaner project page; NN/g "Login Walls" 2014 | Case; practitioner; abstract † | At source; verified | Configuration uptake (six million visitors; 60,000 / 130,000 indexes — unreconciled); reciprocity |
| ONS "Explore local statistics" landing; UKHSA data dashboard "What's new" and landing (6 Oct 2026) | Cases (structure only) | At source; verified | Input-first; a landing redesigned twice with notes; stamps beside figures |
| StatCounter UK platform share (Sept 2026); Ofcom *Online Nation 2025* p. 12 | Practitioner data; Standard (regulator research) | At source; verified | 53.56% phones; 77% of time online |
| Segel & Heer 2010 *TVCG* 16(6) | Evidence (design space; 58) | At source; spot-checked; verified | Genres; martini glass; "most common"; "interesting default view"; no reader study |
| Hullman & Diakopoulos 2011 *TVCG* 17(12) | Evidence (framework; 51) | At source; verified | Rhetoric; four layers; provenance rhetoric; default views anchor |
| Hullman et al. 2013 *TVCG* (sequence); Riche et al. 2018; Stolper et al. 2016 | Evidence | Reconstructed abstract; publisher page; unreached | — |
| Boy, Détienne & Fekete 2015 CHI | Evidence (three field experiments) | Abstract † via index; secondary via Conlen 2019, McKenna 2017, Schröder 2023 (verified); full text unreached; version 1's figures withdrawn | "does not seem to increase user-engagement in exploration" |
| Zhi, Ottley & Metoyer 2019 *CGF* | Evidence (n = 180) | Abstract † (EG Digital Library); verified | Slideshow better for comprehension; linking raised engagement; recall interaction |
| Kong, Liu & Karahalios 2018 and 2019 CHI | Evidence (104; 200) | At source; verified | Slant and perceived message; title remembered over chart (133/398; 68; about half neither); credibility falls; 72–87% neutral |
| Kim, Setlur & Agrawala 2021 CHI | Evidence (219; 2,168) | At source; verified | Caption v chart prominence |
| Stokes, Setlur, Cogley, Satyanarayan & Hearst 2023 *TVCG* | Evidence (512; 302) | At source; spot-checked; verified | "not penalized"; preference; L2/L4 steer; guidelines |
| Ajani et al. 2022 *TVCG* | Evidence (n = 24) | At source; verified | Declutter v focus; "pushy" |
| McKenna et al. 2017 *CGF* | Evidence (n = 240) | At source; verified | No scroller/stepper difference; comprehension flat (Chapter 3 corrected) |
| Schneiders 2020 *Media and Communication* 8(1) | Evidence (n = 381) | At source; verified | Scrollytelling recall v efficiency |
| Hohman, Conlen, Heer & Chau 2020 *Distill*; The Pudding 2017; Schröder et al. 2023 (arXiv 2312.01164); Victor 2011 | Evidence (review); Practice; Evidence (review of 184); Practice (essay) | At source; verified | Thin evidence; publishers' metrics; "doesn't hide content"; "not forced to interact" |
| Wainwright 2023 (ONS Digital blog); ONS "About these articles"; ONSvisual robo-utils and robo-article | Practice (official method) | At source; blog spot-checked; verified | 331 pages; "not a labour-saving tool"; checked; labelled; templates |
| Graefe 2016 Tow/CJR; Graefe & Bohlken 2020 *Media and Communication* 8(3) | Evidence (report; meta-analysis of 12, n = 4,473) | At source; verified | The four steps; 3,000 v 300; 7% → 1% (an executive's claim); the stock-split error; d = 0.0 / 0.5 / 2.8; told-human effect |
| Our World in Data FAQs; redesign post (2023); The Markup About; ONS QMI page; ProPublica strapline; Dörk et al. 2013 | Practice; Standard; Critical scholarship | At source; verified (strapline read once) | Precedents for stating method; disclosure principle |
| Heer & Shneiderman 2012 *CACM*; Yi, Kang, Stasko & Jacko 2007 *TVCG*; Dimara & Perin 2020 *TVCG* | Practice (framework); Evidence (review); abstract † | At source; verified; abstract | Twelve task types, "a community project"; seven intents, "relatively low level of attention"; "a thinking tool" |
| Lam 2008 *TVCG* | Evidence (synthesis of 32 studies) | Abstract † (index) | Seven costs |
| Mosca, Ottley & Chang 2021 CHI | Evidence (472 + 1,980 analysed) | At source; spot-checked; verified | Static ≥ interactive; 43–44% used the filter; 70/40 confounded |
| Zikmund-Fisher, Dickson & Witteman 2011 *JMIR* 13(3) | Evidence (n = 3,371) | Abstract † (index; control failed on that pass) | Completion 79.3 → 65.5; choice 73.8 → 61.6 (strong dominance) |
| Nielsen 2006 (NN/g); Springer & Whittaker 2019 IUI | Practice; Evidence (74; 12) | At source; verified | The two conditions; detail raised expectation not trust |
| Stoiber et al. 2022 *Visual Informatics* 6(4); Dhanoa et al. 2022 *CGF*; Dhanoa et al. 2025 *TVCG* (D-Tour) | Evidence (596 across three studies); Practice (model); Evidence (qualitative, six users) | At source; verified | No correctness gain except one unfamiliar form (abstract and body disagree); no baseline for tours |
| W3C *Understanding WCAG 2.2*: 1.4.13; 2.1.1; 2.5.1; 2.5.7; 2.5.8; 2.5.5. W3C ARIA APG tooltip pattern | Standard (W3C) | At source; 2.5.8 spot-checked; verified | Hover conditions and reasons; keyboard; gestures; dragging; 24 px and the dense-visualisation exception; 44 px |
| NN/g "Tooltip Guidelines" 2019; Parhi, Karlson & Bederson 2006; Apple "Dos and Don'ts"; Google Android touch targets; Chartability | Practice; Evidence (n = 20); Practice | At source; verified (Chartability read once) | Touch has no hover; 9.2/9.6 mm; 44 pt; 48 dp |
| Hoffswell, Li & Liu 2020 CHI; Kim, Moritz & Hullman 2021 EuroVis; Kim, Rossi, Sarma, Moritz & Hullman 2021 *TVCG*; Brehmer et al. 2019 and 2020 *TVCG* | Evidence (231 examples; 378 pairs; modelling; 87; 96) | At source; verified | Phones remove content and interactivity; density-message trade-off; linear and small multiples faster |
| Berners-Lee 1998; RFC 7089; Zittrain, Albert & Lessig 2014; Klein et al. 2014; Jones et al. 2016; Pew 2024; UK Government Web Archive (About; How to use) | Standard; Standard (IETF); Evidence; Standard (archive) | At source; Jones spot-checked; all verified | Cool URIs; Memento; 49.9%; one in five; 76.35% drift; 38%/21%; "Interactive content usually cannot be archived" |
| FORCE11 2014; DataCite versioning; RDA WGDC 2015 (Rauber et al.); DCC Ball & Duke 2015 | Standard (community); Practice | At source; RDA spot-checked; verified | Eight principles (P7); DOI versioning; R1–R14; three approaches |
| Our World in Data grapher page and archive twin; Gerber & Giattino 2025; OWID FAQ; chart API docs | Practice (case) | At source; the 2025 post spot-checked; verified | State in URL; archived citations; previous/next/live; the selection gap |
| ONS dataset versions page; ONS Revisions Policy and Correction of Errors Policy; GOV.UK "Retire outdated content"; UKHSA "Access our data" and topic page | Standard (official; design system); case | At source; verified (the "history mode" sentence read in context and not used) | Versions; corrections banner "when and why"; withdrawn banner; area in URL |
| Heer, Viégas & Wattenberg 2007 CHI; Shiny "Bookmarking state" | Evidence (system); Practice | At source; verified | State as URL; many URLs one view; 2,000 characters |
| Wilkinson 2012 (handbook chapter); Wickham 2010 *JCGS*; Satyanarayan et al. 2017 *TVCG*; Bostock et al. 2011 *TVCG* | Standard (method) | Abstract †; at source; at source; at source; verified | Data independent of the specification; unit := (data, transforms, mark, encodings); selections; the data join |
| Burns et al. c. 2022; Peck, Ayuso & El-Etr 2019 CHI; Xiong et al. 2019 TrustVis; Elhamdadi et al. 2022 BELIV; Mayr et al. 2019 TrustVis; Kennedy et al. 2016 *ICS*; Lin & Thornton 2021 (PsyArXiv) | Evidence; Evidence (42 interviews); Evidence (77); Position; Position; Critical scholarship; Evidence (preprint; 3,405) | At source; at source; at source (corrected wording); abstract; at source; at source (accepted manuscript); abstract †; verified | Metadata → thoroughness not accuracy; 17/42 moved; disclosure predicted choice; trust factors; source line as rhetoric; beauty → trust via competence |
| Sarma et al. 2022 *TVCG*; Song & Szafir 2019 *TVCG*; Andreasson & Riveiro 2014 iV | Evidence (202); Evidence; Evidence | At source, verified; abstract †; abstract † (index) | Dropped gap most biased; explained emptiness beat blurring, raised risk-taking |
| Monmonier 2018 (UCP page); ColorBrewer; Brewer & Pickle 2002 *Annals AAG* 92(4); Esri Insights docs; Axis Maps guide | Practice; Practice; Evidence (56) †; vendor; practice | Publisher page; at source; abstract †; at source; at source; verified | Scheme types; quantiles; matched legends +28%; rates not counts |
| Schiewe 2019 *KN* 69(3); Nusrat, Alam & Kobourov 2018 *TVCG*; Nusrat & Kobourov 2016 (arXiv) | Evidence (260); Evidence (33); survey | At source; spot-checked; verified (the 93.1 sentence corrected); at source, verified; at source (Kaspar et al. secondary) | Area-size bias; dark-is-more; cartogram ranking; choropleth + circles beat cartograms |
| Bartram, Patra & Stone 2017 CHI; Schloss et al. 2018 *CRPI* | Evidence | Abstract †; at source (not a map study) | — |
| data.gov.uk Historical Performance Platform; CDDO blog 18 Feb 2021; NAO 2017 HC 1059; GDS blogs June 2016; UKHSA "What's new" 12 Mar 2024 and archive page; US Federal IT Dashboard letter; Johns Hopkins CRC notice; COVID Tracking Project 1 Feb 2021 | Standard (official); Evidence (audit); Practice (cases) | At source; verified | 802/118; "lack of clarity about the purpose"; "all things to all people"; supply-side reasons; 1.4 GB archive with caveat |
| Nightlife Culture: version 1 Chs 1, 9, 10 (archived); Decision Book Chs 7, 15 and rule register; Style Guide v1.5 DSH-01–21; the brief | Nightlife Culture | At source (repo); not re-traced by the verifier | The sentence first; the six patterns; the purchase table; the crop test; "how this argues"; the poster beside the open door |

## 16 · Version 2 — Chapter 12: Recognising your place (6 October 2026)

*Legend as §5, §10 and §15. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (three sources: Peck et al.; Flowerdew; the verifier's Lisnic correction); "verified" — the independent verification pass re-traced it (about 700 checks across about 480 items and about 128 pages; three substantive errors found and corrected — Lisnic's corpus, Kotkov's 8.5 per cent, the Community Life Survey's "local area"; Flowerdew's remainder counts not reconciled; 29 "(read once)" marks lifted). "†" — abstract, secondary or press summary only. "Unreached" — sought and not opened; nothing quoted. The four research agents worked without web search this sprint.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| Lynch 1960 *The Image of the City* | Practice (method) | Unreached; instruction secondary via Wikipedia "Mental mapping"; verified | "a rapid description of the city to a stranger"; "just a rough sketch" |
| Wang & Schwering 2015 *JOSIS* 11; Gieseking 2013 *Qualitative Inquiry* 19(9) | Evidence (21 participants; 45 maps); Evidence of method | At source; †; verified | Seven invariant sketch aspects, distances distorted; "ad hoc and piecemeal" |
| Coulton, Korbin, Chan & Su 2001 *AJCP* 29(2); Coulton, Chan & Mikelbank 2010 (Urban Institute) | Evidence (pilot); Evidence (7,498 households; ten cities) | †; At source; verified | Resident maps differ from census units; median 0.35 against 2.23 sq mi; 83% drew; 33% consensus rule |
| Lupton 2003 CASEpaper 73 (LSE) | Reading (policy review) | At source (Kearns & Parkinson, Dietz, McCulloch & Joshi secondary); verified | Three scales (home area, locality, district); "defined by the limitations of an available data set" |
| Understanding Society, variable scopngbha (and the Community Life Survey's frames, Ch 9) | Standard (official statistics) | At source; verified (the Community Life Survey "local area" wording corrected) | "I feel like I belong to this neighbourhood", no spatial definition; two walking-distance frames |
| Montello, Goodchild, Gottsegen & Fohl 2003 *Spatial Cognition and Computation* 3(2–3) | Evidence (36 pedestrians) | At source; verified | 100% and 50% confidence regions; 33 of 36; core about 300 m from centroid; "vague region" |
| Hollenstein & Purves 2010 *JOSIS* 1; Woodruff 2012 (Bostonography); Aadland, Farah & Magee 2016 *JOSIS* 12 | Evidence (8 million photographs); Practice; Evidence of method | At source; At source; †; verified | "0.5–2% of tags"; 25/50/75% contours; core and boundary zone |
| ONS: Statistical geographies; Census 2021 area types; Census geography; Administrative geography (England); Postal geography; Postcode products; Towns and cities (2 Aug 2023) | Standard (ONS) | At source; verified | OA design "similar population sizes… socially homogenous"; LSOA/MSOA sizes; 8,483 wards; BUAs; postcode best-fit |
| MHCLG: English Indices of Deprivation 2019 Technical Report and Release; 2025 Release and FAQ (30 Oct 2025) | Standard (official statistics) | At source; verified | "LSOAs are also referred to as 'neighbourhoods'"; no "definitive threshold" for deprived; rank 1,000 not half as deprived as 500 |
| House of Commons Library, MSOA Names v2.3 (13 Feb 2026) | Practice | At source; verified | 7,264 names; "aren't 'official' names"; publish, invite correction, errors channel |
| ONS Digital, Build a custom area profile (17 Jan 2023; May 2025) | Practice (official method) | At source; verified | "simply select an area on a map"; population-weighted centroid |
| Openshaw & Taylor 1979 (via Jelinski & Wu 1996 *Landscape Ecology* 11(3)); Fotheringham & Wong 1991 *Environment and Planning A* 23(7) | Evidence (method) | Unreached; secondary, at source; †; verified | Scale and zoning problems; Iowa +0.979 to −0.811; "essentially unpredictable" |
| Flowerdew 2011 *Population Trends* 145 | Evidence (2001 English census; 153 correlations at three scales) | At source; spot-checked by the orchestrator; verifier refused the PDF | 68 negative / 60 positive at all scales; "about 60 per cent of cases"; "Most of the time, not very"; remainder counts not printed |
| Straw 1991 *Cultural Studies* 5(3); Straw 2014 postface; Bennett & Peterson 2004 *Music Scenes* | Reading (conceptual text) | At source (author copy); verified; Bennett & Peterson unreached, named only | Scene against community; "hiding" cultural productivity |
| Silver, Clark & Navarro 2010 *Social Forces* 88(5); Silver, Clark & Rothfield, working paper | Evidence of method | †; At source; verified | Amenity scoring by zip code; "rankings and maps of the U.S." |
| Peck, Ayuso & El-Etr 2019 CHI | Evidence (42 interviews) | At source; spot-checked; verified | "find their home state"; "decisions framed or driven by personal experience"; replication request |
| Kennedy, Hill, Allen & Kirk 2016 *First Monday* 21(11); Kennedy & Hill 2018 *Sociology* 52(4) | Evidence (nine focus groups; 46 participants); Evidence | At source; †; verified | Subject matter as one of six engagement factors; feeling of numbers (abstract only) |
| Kim, Hullman & Agrawala 2016 CHI | Evidence (40 crowd-workers) | At source; verified | Personalised analogies rated 1.9 points higher; self-rated helpfulness |
| Wainwright 2023, ONS Digital "Semi-automation and Census 2021" | Practice (official method) | At source; verified | 331 stories; "really valued being able to read all about the place they call home"; "every individual area's page had been read" |
| Taylor 1994; Fraser & Honneth 2003 (via Internet Encyclopedia of Philosophy); Fraser 2000 *NLR* 3; Fraser 1995 *NLR* I/212 | Reading (political theory) | Secondary, at source; At source (openings only); verified | Taylor on misrecognition; Fraser's displacement and reification hazards |
| Lewandowsky et al. 2020 *The Debunking Handbook 2020* | Evidence (field review) | At source; verified | "come up empty"; "Repeat the misinformation, only once"; "repetition makes information appear true" |
| Swire-Thompson, DeGutis & Lazer 2020 *JARMAC* 9(3); Wood & Porter 2019 *Political Behavior* 41; Skurnik, Yoon, Park & Schwarz 2005 *JCR* 31(4) | Evidence (review); Evidence (10,100 subjects; 52 issues); Evidence | At source; †; †; verified | "not a robust empirical phenomenon"; no worldview backfire; older adults after 3 days |
| Lakoff 2016; 2023 (george-lakoff.com) | Practice (blog) | At source; verified | "negating a frame just activates the frame"; no study cited |
| Chong & Druckman 2007 *Annual Review of Political Science* 10; 2007 *APSR* 101(4) | Evidence (869; 1,277) | At source; verified | "qualities of frames than… frequency of dissemination"; weak frame never prevails |
| FrameWorks UK 2018 (JRF) *How to talk about poverty in the UK* | Evidence (practitioner experiments; 12,448) | At source; verified | "leading with prevalence data had no significant effect on issue salience" |
| McKnight & Kretzmann 1990 (Northwestern); Kretzmann & McKnight 1993 | Practice (framework) | At source; Kretzmann & McKnight unreached; verified | "a map of riches, assets, and capacities"; needs map and assets map |
| O'Connell et al. 2016 (arXiv:1609.09756); Sarikaya et al. 2019 *TVCG* 25(1) (Ch 11) | Practice (design case) | At source; verified | "largely negative" data; "do not yet know how effective"; Ch 1 gloss corrected |
| Holder & Xiong 2022 *TVCG* (arXiv:2208.04440); Quinn 2020 *Educational Researcher* 49(7) | Evidence (four experiments; 329, 434, 281, 266); Evidence (three randomised experiments) | At source; †; verified | "bar charts may encourage deficit thinking"; "Hiding variability tends to increase stereotyping"; gap news and stereotypes (0.30, 0.38 SD), faded after 2 weeks |
| Schwabish & Feng 2021 *Do No Harm Guide* (Urban Institute) | Practice | At source; verified | "who is and is not included"; calling out the absence; message over the chart |
| Glasgow Centre for Population Health 2011, 2012 (briefings 9, 10); Fogarty et al. 2018 (Lowitja Institute) | Practice (reviews) | At source; verified | Assets not a replacement for structural investment; "almost a complete lack of evaluation"; "defining my cultural identity" |
| Zhang & Schwarz 2012 *JCR* 39(2); Thomas, Simon & Kadiyali 2010 *Marketing Science* 29(1) | Evidence | †; †; verified | Granularity read as precision; price-precision effect kept separate |
| van der Bles et al. 2020 *PNAS* 117(14) | Evidence (five experiments; n = 5,780) | At source; verified | Verbal hedge d = 0.75; numeric range d = 0.17, not significant |
| Gustafson & Rice 2020 *Public Understanding of Science* 29(6); Dries et al. 2024 *PUS* | Evidence (review of 48 experiments); Evidence | †; †; verified | "only positive or null effects"; uncertainty "buffers against a loss of trust" |
| Hullman 2019 "Why authors don't visualize uncertainty" (arXiv:1908.01697) | Evidence (survey; 90, 85 answering) | At source; verified | 53/85 "confuse or overwhelm"; 15/85 "seem questionable" |
| Ge, Cui & Kay 2023 CHI (CALVI) | Evidence (n = 497) | At source; verified | 15 trick items, M = 0.39 against 0.80; "Missing Data" means a mark where nothing was measured |
| Analysis Function: symbols and shorthand in tables (11 Jan 2022); charts (dual axis; titles; source); communicating quality, uncertainty and change | Standard (Analysis Function) | At source; verified | [x] [z] [c] [u] [w] [low]; "do not recommend using dual axis charts" |
| Few 2008 "Dual-scaled axes in graphs" | Practice | At source; verified | "Magnitude comparisons between values with different units… not appropriate" |
| L'Yi, Jo & Seo 2020 IEEE VIS (arXiv:2009.00192); Ondov, Jardine, Elmqvist & Franconeri 2019 *TVCG* 25(1) | Evidence (review of 127 papers; 15 user studies); Evidence (four experiments; 189 of 200) | At source; verified | Juxtaposition "almost never outperformed"; overlay and mirror performance |
| Wood et al. 2012 *TVCG* "Sketchy rendering" | Evidence | At source; verified | Area judgement compromised; engagement raised; belief unmeasured |
| OCSI 2019 *Community Needs Index* | Practice (official method) | At source; verified | Assets counted and published as need |
| ONS service manual, "Writing main points and analysis"; ONS Explore Local Statistics QMI (25 Apr 2025) | Standard (ONS) | At source; verified | "one trend or point per bullet"; "higher" / "similar" at one median absolute deviation; separate indicators; beeswarm |
| Stevens 1946 *Science* 103; Velleman & Wilkinson 1993 *The American Statistician* 47(1) | Evidence of method | Stevens unreached; Velleman & Wilkinson at source (author copy; Hand & Keynes secondary); verified | "Scale type… depends upon the questions we intend to ask of the data"; Stevens via their rendering only |
| Albo, Lanir, Bak & Rafaeli 2016 *TVCG* 22(1); Feldman 2013 *Social Indicators Research* 111(3) | Evidence | †; †; verified | Radar "least effective and least liked"; filled-radar area not invariant to axis order |
| Waldner et al. 2019 *TVCG* 26(1); Javed, McDonnel & Elmqvist 2010 *TVCG* 16(6); Borgo et al. 2013 (Eurographics STAR) | Evidence (92 crowd-workers); Evidence; Evidence (survey) | At source; †; At source; verified | Linear bars over radial rose; small multiples and wide spans; glyph axis order |
| Gale, Singleton, Bates & Longley 2016 *JOSIS* 12 | Evidence of method | At source (two agents independently); verified | OAC naming rule: "pejorative were not used"; "consequences of factors that have happened to areas" |
| ONS area classifications; 2021 and 2022 residential-based classifications; Geographic Data Service OAC 2021; Wyszomierski et al. 2024 *Geographical Journal* 190(2) | Standard (ONS); Evidence | At source; †; verified | "Hard-Pressed Living"; pen-portrait hedge; 2021 names not printed |
| Understanding Scottish Places (methodology; about; town page); OECD Regional Well-Being (guide, FAQ, Oct 2025); CHE (Germany) ranking methodology | Practice | At source; verified | 508 towns; "no single ranking"; three ranking groups, "no overall value" |
| European Statistics Code of Practice 2017, Principle 14; Regulation (EC) 223/2009 Art. 12(1); Eurostat SIMS manual; OSR Code of Practice 3.0 (3 Nov 2025; modified 11 Aug 2026) | Standard (law); Standard (regulator) | At source; verified | Comparability definition; 6.6, 6.7, 7.4, 9.3 |
| Fattore 2016 *Social Indicators Research* 128(2); Annoni & Brüggemann 2009 *SIR* 92(3); Fattore, Maggino & Colombo 2012 | Evidence of method | †; †; Fattore et al. unreached; verified | Profile comparison without aggregation; "rather troublesome" |
| Herlocker, Konstan & Riedl 2000 CSCW | Evidence (78 users, 210 users; 97 exit survey) | At source; verified | 5.25 against 4.53; "no statistically significant difference"; the "86%" corrected |
| Bilgic & Mooney (author copy) | Evidence (34 subjects; 53 recommendations) | At source; verified | Neighbour style "overestimate… by 0.74"; promotion against satisfaction |
| Tintarev & Masthoff 2007 ICDE workshop; 2012 *UMUAI* 22(4–5); Nunes & Jannach 2017 *UMUAI* 27 | Evidence (survey); Evidence (review of 217) | At source; †; At source (arXiv); verified | Seven aims; personalisation "detrimental to effectiveness"; 21.5% evaluated |
| Singh & Joachims 2018 KDD (arXiv:1802.07281) | Evidence of method | At source; verified | Exposure "determined by position"; 0.03 gap, "30% less exposure" |
| Abdollahpouri, Mansoury, Burke & Mobasher 2019 (arXiv:1907.13286); Ekstrand, Das, Burke & Diaz 2022 (arXiv:2105.05779) | Evidence; Evidence (review) | At source (Ekstrand: first part only); verified | Niche users see largest discrepancy; "rich-get-richer" |
| Salganik, Dodds & Watts 2006 *Science* 311 | Evidence (14,341; 48 songs) | At source (author copy); verified | Social influence raised "inequality and unpredictability of success" |
| Fleder & Hosanagar 2009 *Management Science* 55(5) | Evidence (model) | † (abstract read by an agent; not re-reached by the verifier) | Rich-get-richer; individual up, aggregate down |
| Arguedas, Robertson, Fletcher & Nielsen 2022 (Reuters Institute); Zuiderveen Borgesius et al. 2016 *Internet Policy Review* 5(1); Bruns 2019 *IPR* 8(4) | Evidence (review) | At source; verified | "opposite of what the 'filter bubble' hypothesis posits"; "vague and founded in anecdotes" |
| Kotkov 2018 dissertation (Jyväskylä); Kotkov, Wang & Veijalainen 2016 | Evidence (302 of 2,146 items) | At source; Kotkov et al. unreached; verified (the 8.5 per cent corrected) | "There is no consensus on definition"; 14% serendipitous |
| Ekstrand, Harper, Willemsen & Konstan 2014 RecSys | Evidence (582 users; 81 days) | At source; verified | Satisfaction against novelty; "Too many unfamiliar recommendations" |
| Teleport (surviving page); Discover Uni (how-to; data; comparing; rankings); Numbeo indices | Practice | At source; verified | "sorted by how well they match"; "up to seven"; fixed-weight global ordering |
| 360Giving (funder guide; 360Insights); Arts Council England 2021 *Methodology for identifying priority places*; Levelling Up for Culture Places | Practice; Standard (method) | At source; verified | "Find gaps, overlaps"; seven weighted indicators; 54 places; no "cold spots" |
| Everywhere Is Queer; Safe Space Alliance; Ask for Angela (listing mechanism) | Practice | At source; verified | Self-listing by the owner; verification; no stated safety rationale |
| Ask for Angela pledge page | Practice | At source; not re-reached | Signed pledge, business added to a map |
| Lisnic, Polychronis, Lex & Kogan 2023 CHI | Evidence (9,958 posts coded) | At source; verifier's corpus correction spot-checked; verified | "only 12%"; "the majority (55.3%)" screenshots; "more than 40%" of sceptic charts |
| Lisnic, Cutler, Kogan & Lex 2025 CHI | Evidence (three experiments; 130, 160, 675) | At source; verified | "Juxtaposed approaches are croppable"; 38% did not notice |
| Lee, Yang, Inchoco, Jones & Satyanarayan 2021 CHI (arXiv:2101.07993); Lo, Gupta, Shigyo, Wu, Bertini & Qu 2022 EuroVis (arXiv:2204.09548) | Evidence (about 500,000 tweets; 41,000 images); Evidence (1,143 images) | At source (Lee verifier re-traced); At source; verified | "anti-mask groups practice… data literacy"; 74 issue types, no issue for cropping |
| Analysis Function, charts (titles; placement; source); GOV.UK publishing guidance, Images; ONS service manual, Chart text | Standard (Analysis Function; design system; ONS) | At source; verified | "can be taken out of context if it is copied and pasted"; "Avoid using images with text"; source "directly after the chart" |
| Our World in Data: FAQ; a chart page; chart API documentation | Practice | At source; verified | Live or archived embed; source line and licence; "uncaptioned" preset |
| Scottish Government: SIMD 2020 collection page; "How can I use SIMD?" | Standard (official statistics) | At source; verified | Rank is ordinal; not "how much more deprived" |
| Scottish Government: SIMD "Do not use SIMD for" page | Standard (official statistics) | At source by an agent; not re-reached by the verifier | "Identifying affluent areas"; no cross-time rank comparison |
| ONS, Personal well-being in the UK QMI (14 Jan 2025) | Standard (ONS) | At source; verified | "simply ranking local authorities… can be misleading" |
| Wacquant 2007 *Thesis Eleven* 91; Wacquant, Slater & Pereira 2014 *Environment and Planning A* 46(6) | Reading (theory) | At source (author copy); †; verified | "A blemish of place"; "People there commonly hide their address" |
| Tunstall, Green, Lupton, Watmough & Bates 2014 *Urban Studies* 51(4) | Evidence (2,001 applications; 667 jobs) | At source; verified | Net preference 2.6 points, p = 0.1170; "small and… not statistically significant" |
| Permentier, Bolt & van Ham 2011 *Urban Studies* 48(5); Permentier, van Ham & Bolt 2008; Kearns, Kearns & Lawson 2013; Slater 2018 *Sociological Review* | Evidence; Reading | †; Permentier 2008 and Kearns unreached; † | Perceived reputation; "sink estate" invented by journalists |
| Local Trust / OCSI 2019 *Left behind?* | Practice | At source; verified | "controversial and contentious"; "ward-level data can mask variations" |
| Qualitative Research Guidelines Project "Member checks" (Lincoln & Guba 1985); Candela 2019 *TQR* 24(3); Carlson 2010 *TQR* 15(5); Birt et al. 2016; Motulsky 2021 | Reading; Practice (case) | Secondary, at source; At source; At source; Lincoln & Guba, Birt and Motulsky unreached; verified | Member-check definition; "I may have caused harm"; forms of return |
| Murray, Falkenburger & Saxena 2015 *Data Walks* (Urban Institute) | Practice | At source; verified | Five stations, six minutes each; "leave titles at the door" |
| Detroit Urban Research Center 2011; Gaddy & Scott 2020 (Urban Institute); Rambaldi, Chambers, McCall & Fox 2006 *PLA* 54; Sieber 2006; Elwood 2006; Peluso 1995 | Standard (community); Practice | At source; Sieber, Elwood and Peluso unreached; verified | CBPR principle 7; "Return data and research results"; "The maps are never final" |
| Version 1, Chs 2, 5, 7 (archived); Decision Book ARG-12, DAT-18, DAT-21, TBL-17, LAY-08, geography rules (boundary vintage; best-fit lookup), Ch 16 (framing), Ch 6 (breakouts); Style Guide v1.5 (comparability flag; voice rules; slides); Comparative Methodology v1.0 (via Style Guide §12); the trusted-partner deck, slides 7–8 | Nightlife Culture | Read directly (repo); version 1 positions tested, not sources; not re-traced by the verifier | The two columns; "Never repeat the opposing frame"; "Space is read as importance"; "The source travels with the figure"; the eight-criterion gate; "Does it paint a recognisable picture?" |

## 17 · Version 2 — Chapter 13: Accessible as the good version (6 October 2026)

*Legend as §5, §10, §15 and §16. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (three pages: Understanding Conformance; Understanding 1.4.5; the Analysis Function dashboards page); "verified" — the independent verification pass re-traced it (about 430 items across about 171 pages; thirteen wrong, all corrected — among them Lundgard's 63 per cent quotation, the WebAIM "every count" claim, two Analysis Function wordings, the Chartability confidence quotation, Kuster's sample; 26 "(read once)" marks lifted). "†" — abstract or secondary only. "Unreached" — nothing quoted. The four research agents had web search rationed to thirty calls each.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| WCAG 2.2 (W3C Recommendation, 12 Dec 2024); Understanding Conformance | Standard (W3C) | At source; Conformance spot-checked; verified | "a fallback option for conformance"; "cannot be achieved if part of a web page is excluded"; "should be deprecated" |
| Understanding 1.4.5 Images of Text | Standard (W3C) | At source; spot-checked; verified | "where both are presented to the user, this success criterion is met" |
| Understanding 1.1.1; Technique G92 | Standard (W3C) | At source; verified | Chart example in four sentences; short and long alternative; "Where possible and practical… a table" |
| Understanding 1.4.11 (contrast of graphics) | Standard (W3C) | At source; verified | "each line in a graph"; labels or a table lift the 3:1 requirement |
| Understanding 1.4.4, 1.4.10, 1.4.12, 1.3.2, 1.3.3 | Standard (W3C) | At source; verified | "canvas implementations of text are considered to be images of text"; 1.5 / 2 / 0.12 / 0.16 spacing |
| Understanding 2.1.2, 2.4.3, 2.4.7, 2.4.11, 2.4.13, 2.5.2, 2.5.7, 2.5.8 | Standard (W3C) | At source; verified | "custom components and widgets are not implemented with keyboard users in mind"; "2 CSS pixel thick perimeter"; sticky filter bar |
| Understanding 2.2.2, 2.3.1, 2.3.3; Technique C39 | Standard (W3C) | At source; verified | Auto-updating pause or frequency control; "quite severe" for vestibular disorders; reduced-motion technique |
| Understanding 3.2.1, 3.2.2, 3.3.2 | Standard (W3C) | At source; verified | A change of content is not a change of context; "Too much information… as harmful as too little" |
| Understanding 4.1.2, 4.1.3; Technique ARIA22 | Standard (W3C) | At source; verified | "'18 results returned'" as a status message, not the results; role=status; "too 'chatty'" |
| WAI-ARIA 1.2 (Rec 6 Jun 2023); WAI-ARIA 1.3 (WD 4 Jun 2026) | Standard (W3C) | At source; verified | No chart role; status, table, grid, figure definitions |
| WAI-ARIA Graphics Module 1.0 (Rec 2 Oct 2018) | Standard (W3C) | At source; verified | graphics-document; "Future work will expand on this framework… charts or maps" |
| ARIA Authoring Practices Guide (Read Me First; Table; Grid; Alert; Names and Descriptions) | Standard (W3C) | At source; verified | "No ARIA is better than Bad ARIA"; "A role is a promise"; native table preferred |
| Chart-roles wiki (2015); ARIA Working Group charter | Standard (W3C) | At source; verified | "last edited on 11 September 2015"; charter has no "chart" |
| WAI Tutorials: Complex Images (8 Apr 2026) and its long-description example; Images of Text | Standard (W3C) | At source; verified | "scales, values, relationships and trends"; three approaches, no longdesc; aria-describedby "one continuous paragraph" |
| COGA, Making Content Usable… (Working Group Note, 29 Apr 2021); WAI supplemental-guidance pattern pages | Standard (W3C) | At source; verified | "Reinforce numbers with non-numerical concepts"; "most common 1500 words"; "lower secondary"; "contextually-relevant graphs" |
| WCAG 3.0 Working Draft (10 Sep 2026); WAI "WCAG 3 Introduction" (25 Sep 2026); W3C press release on ISO/IEC 40500:2025 (21 Oct 2025) | Standard (W3C) | At source; verified | "inappropriate to cite this document as other than a work in progress"; "meet WCAG 2.2 success criteria now"; ISO status |
| Media Queries Level 5 (WD 19 Feb 2026) — reduced-motion definition; csswg-drafts issue thread | Standard (W3C) | Unreached; thread read as secondary | Definition sentence not quoted; C39 intent used instead |
| Accessible Infographics Community Group; Data Visualization Community Group | Standard (W3C) | At source; verified | Closed 7 Apr 2023 and 7 Dec 2023, no published report |
| EN 301 549 v3.2.1 (2021-03), ETSI and Canadian HTML; AccessibleEU notice (7 Sep 2026); v4.1.1 (2026-09) ETSI PDF | Standard (EU law) | At source; verified | v3.2.1 incorporates WCAG 2.1 AA; v4.1.1 "is not yet the legal reference standard" |
| EN 301 549 v4.1.1, clause 9 | Standard (EU law) | Unreached | Not quoted |
| S.I. 2018/952 regs 1, 3–14 as revised; 2018 Explanatory Memorandum (legislation.gov.uk) | Standard (law) | At source; verified | Reg 3 definitions; reg 4(1) NGOs; reg 4(2)(d) maps, (e) third-party content; regs 6–8 |
| S.I. 2022/1097 (reg 9 substituted); S.I. 2025/557 (annotations) | Standard (law) | At source; verified | WCAG A and AA presumption, "as amended from time to time", no version number; EN 301 549 dropped |
| Directive (EU) 2016/2102, recital 30 and Article 1(4)(e) | Standard (EU law) | At source; verified | Origin of reg 4(2)(e); content "should be excluded"; not to be used "if it hinders" |
| GOV.UK: Understanding accessibility requirements for public sector bodies (30 Sep 2024); Sample accessibility statement (30 Sep 2024) | Standard (regulator) | At source; verified | "WCAG version 2.2"; "lack of time or knowledge" not a burden; statement form |
| GOV.UK: Public sector website and mobile application accessibility monitoring (30 Sep 2024) | Standard (regulator) | At source; verified | "monitoring for this standard since October 2024"; "responsibility to make sure that it is accessible"; Axe; manual tests |
| GOV.UK: Accessibility monitoring of public sector websites and mobile apps 2022 to 2024 (17 Dec 2024) | Evidence (monitoring data; 1,203 websites; 21 apps) | At source; verified | "nearly all"; ten clean; 29,787 issues; focus 13.3%, contrast 13.0%; "30-40%"; 66 of 93 EHRC letters; "out-of-date" statements |
| GOV.UK: Technology Code of Practice point 2 (5 Oct 2023); Guidance: Technical Specifications (13 Jul 2026); GDS accessibility blog (9 Dec 2022) | Standard (regulator) | At source; verified | "You must meet the WCAG 2.2 AA standard as a minimum" |
| Equality Act 2010 ss. 6, 20, 21, 29, 212; Sch 2 para 2; Sch 25; Explanatory Notes para 676 (legislation.gov.uk) | Standard (law) | At source; verified | "(for payment or not)"; 20(6) "accessible format"; "disabled persons generally"; "an anticipatory duty" |
| EHRC / OEO Code of Practice for services, public functions and associations, 2026: paras 1.5, 1.6, 3.6, Chapter 11 | Standard (regulator) | At source; verified | In force 5 Aug 2026; "whether in the private, public or voluntary sectors"; "free of charge"; no "WCAG" |
| EHRC 2026 Code, Chapter 7 (anticipatory duty) via stammeringlaw.org.uk | Standard (regulator) | Secondary; unreached at source | "The duty is anticipatory"; flagged [Further research] |
| EHRC, "Websites and Internet services" (19 Feb 2019); "General web accessibility guidance" (2014) | Standard (regulator) | At source; verified | "think in advance"; "a website must be accessible to all users" |
| Analysis Function, "Accessibility legislation: what you need to know" (29 Oct 2020); Civil Society (2012) on the airline proceedings | Evidence (public record) | At source; verified | £3,000 (2023) and £5,000 (2021) settlements; 2012 airline proceedings; no UK judgment found |
| Directive (EU) 2019/882 Arts 2, 3, 4, 31; recitals 43, 70 | Standard (EU law) | At source; verified | Service categories; maps and third-party carve-outs; "Microenterprises… exempt" |
| Written Question UIN 6505 (answered 10 Oct 2024) | Standard (regulator) | At source; verified | EAA "will not directly apply to the UK" |
| BSI Knowledge pages: BS 8878:2010; BS ISO/IEC 30071-1:2019; ISO page for ISO/IEC 30071-1:2019 | Standard (regulator) | At source; verified | BS 8878 still "Current"; 30071-1 "confirmed" in 2024 |
| Procurement Act 2023 s.56; Public Contracts Regulations 2015 (revoked) | Standard (law) | At source; verified | No accessibility wording in technical specifications |
| US Department of Justice, ADA Title II web rule fact sheet (8 Apr 2024) | Standard (law) | At source (United States law, for its wording); verified | "should not have a main web page that is inaccessible and a separate accessible version" |
| Sharif, Chintalapati, Wobbrock & Reinecke 2021 ASSETS | Evidence (36 against 36) | At source; verified | "61.48% less accurately and spend 210.96% more time"; "entirely indetectable" |
| Sharif, Wang, Muongchan, Reinecke & Wobbrock 2022 CHI (VoxLens) | Evidence (21 screen-reader users) | At source; verified | Accuracy 34 to 75%; time 84.6 to 54.1 s; baseline from prior work |
| Sharif, Krishnaswamy, Aitharaju & Wobbrock 2025 W4A | Evidence (survey; 106) | At source; verified | "63% (N=67)" never met sonification; "limited value" for complex visualisations |
| Fan, Siu, Rao, Kim, Vazquez, Greco, O'Modhrain & Follmer 2023 *ACM TACCESS* | Evidence (87 visualisations audited; 127 users) | At source; verified | Tables 7/13; maps 1/15; 50 named tactile graphics; 73% not typically accessible; 94% concerned |
| Lundgard & Satyanarayan 2022 *IEEE TVCG* | Evidence (30 blind, 90 sighted; 2,147 sentences) | At source; verified (the 63 per cent quotation corrected) | Four-level model; "63%, n=19" against editorialising; Levels 2 and 3 |
| Jung, Mehta, Kulkarni, Zhao & Kim 2022 *IEEE TVCG* | Evidence (22 interviews; 7,493 figures) | At source; verified | "reference the underlying data"; 2 to 8 sentences; 40% had alt text |
| Zong, Lee, Lundgard, Jang, Hajas & Satyanarayan 2022 *CGF*; Blanco, Zong & Satyanarayan 2022 Olli (IEEE VIS posters; README) | Evidence (13 blind and low-vision readers); Practice | At source; verified | Friedman test: table easier than multi-view (p<0.01); Olli "accessible tree view" |
| Kim, Joyner, Riegelhuth & Kim 2021 *CGF* 40(3); Marriott et al. 2021 *ACM Interactions* 28(3) | Evidence (review of 56 papers); Reading | At source; verified | "did not consider various types of visual impairment"; "largely heuristic" |
| Siu et al. 2022 CHI (audio data narratives); Thompson, Martinez, Sarikaya, Cutrell & Lee 2023 CHI (Chart Reader) | Evidence (16 users); Evidence (10 users over five months) | At source; verified | Narratives 15.4 against 12.4 insights; "a lossy exchange" |
| Chintalapati, Bragg & Wang 2022 ASSETS; Mack, Cutrell, Lee & Morris 2021 ASSETS | Evidence (547 alt texts); Evidence (12 authors) | At source; verified | "only 50%… extrema or outliers"; "only 31%… trends"; blank box 2.96 against 2.38 |
| Elavsky, Bennett & Moritz 2022 *CGF* and Chartability site (v2); Elavsky, Nadolskis & Moritz 2023 Data Navigator | Evidence (19 participants); Evidence of method | At source; verified (the confidence quotation corrected) | 7 principles, 50 heuristics, 14 critical; 2 to 8 hours; auditors' confidence; no user study |
| Walker & Nees 2011, *The Sonification Handbook* | Evidence (review) | At source (author copy); verified | "around 20 min) can reduce performance error by 50%" |
| Chundury, Jordan, Reyazuddin, Elmqvist & Lazar 2026 *ACM TACCESS* 19(1) | Evidence (10 blind participants) | †; not re-reached by the verifier | "task accuracy did not differ significantly across systems" |
| Apple, Audio Graphs developer documentation; Highcharts sonification documentation and accessibility page | Practice (vendor documentation) | At source; verified | "audio graph represents the x-axis as time… y-axis as pitch"; overview claim without a study |
| Froehlich et al. 2019 *Interactions* | Evidence (review) | At source; verified | Digital maps "inherently graphical"; no choropleths |
| Biggs, Toth, Stockman, Coughlan & Walker 2022 ICAD; Biggs, Toth, Coughlan & Walker 2026 (arXiv:2605.07849) | Evidence (13 blind participants); Evidence (20 sighted, 20 blind) | †; At source (preprint; first author leads the vendor); verified | Geographic questions M = 0.44 text map against 0.23 table; workload lower on table |
| Schmutz, Sonderegger & Sauer 2016 *Human Factors* 58(4) | Evidence (61 non-disabled users) | †; not re-reached by the verifier | High WCAG conformance gave better performance and ratings |
| Schmutz, Sonderegger & Sauer 2017 *Human Factors* 59(6) | Evidence (55 visually impaired, 55 non-impaired) | †; verified | Higher conformance helped both groups |
| Schmutz et al. 2018 *Ergonomics* 61(5) | Evidence | Unreached | Not quoted |
| Schmutz et al. 2019 *Applied Ergonomics* 74 | Evidence | Secondary, via González-Sordé (2024); verified | Easy-to-read cost non-disabled users reading time and liking |
| Ofcom 2006 *Television Access Services* para 1.9; Stagetext 2023 | Evidence (4,365 adults); Evidence (survey) | At source; verified | 7.5 million "had used" subtitles, about 6 million not hearing-impaired; 80% of 18–24s |
| Gernsbacher 2015 *Policy Insights from the Behavioral and Brain Sciences* 2(1) | Evidence (review) | †; verified | "More than 100 empirical studies document that captioning…" |
| Rello & Baeza-Yates 2013 ASSETS; Rello & Baeza-Yates 2016 *ACM TACCESS* 8(4) | Evidence (48 dyslexic readers; 97 readers) | At source; verified | Sans serif improved; "OpenDys… neither better nor worse"; "also beneficial for those without dyslexia" |
| Rello, Pielot & Marcos 2016 CHI | Evidence (104 readers; 28 dyslexic) | At source; verified | "at least 18-point font size" |
| Kuster, van Weerdenburg, Gompel & Bosman 2018 *Annals of Dyslexia* | Evidence (170 children; 102 and 45) | †; not re-reached by the verifier | "Dyslexie font neither benefits nor impedes" |
| Wery & Diliberto 2017 *Annals of Dyslexia* 67(2) | Evidence (single-subject design) | †; verified | "no improvement in reading rate or accuracy" |
| British Dyslexia Association, Dyslexia Style Guide 2023 | Practice | At source; verified | "12-14 point"; 1.5 spacing; the convergence closing line |
| WebAIM Screen Reader User Survey #10 (2024) | Evidence (1,539 respondents) | At source; verified | JAWS 40.5, NVDA 37.7; 91.3% mobile; 71.6% by headings |
| WebAIM Survey of Web Accessibility Practitioners #3 (2021); "Text-only versions" (2020) | Evidence (758 practitioners); Practice | At source; verified (the "every count" claim corrected) | Overlays: 67% not effective, 72% of those with disabilities; text-only "neglect other types" |
| The WebAIM Million (February 2025; February 2026) | Evidence (one million home pages) | At source; verified | 95.9% with failures; 56.1 errors; ARIA pages 59.1 against 42 |
| Family Resources Survey 2023/24 (DWP; updated 15 Jan 2026); House of Commons Library CDP-2022-0238 | Evidence (official statistics) | At source; verified | "16.8 million (25%)" disabled; "more than 2 million" with sight loss |
| Colour Blind Awareness; British Dyslexia Association (prevalence); NIDCD; Vestibular Disorders Association | Evidence (charity and US figures marked) | At source; verified | 1 in 12 men; "Ten percent… believed"; "About 15 percent of American adults" |
| GOV.UK writing guidelines, "Use clear language"; GDS guest post (17 Feb 2014); Trudeau 2011–12 (SSRN abstract) | Standard (design system); Evidence | At source; †; verified | "80% of people preferred sentences written in clear English"; 376 legal-writing responses (†) |
| National Literacy Trust adult literacy page (Survey of Adult Skills 2023); Surrey County Council reading-levels page | Evidence (official statistics); Practice | At source; verified | "1 in 6 (18% / 6.6 million)"; "reading age of 9" |
| NHS "6 in 10" figure's source | Evidence | Unreached; source not named on the page | "more than 6 in 10 adults struggle" — provenance unstated |
| ONS service manual: Dashboards; Interactive charts and animations; Chart text; Bar chart component | Standard (official statistics) | At source; verified | "between 100 and 200 characters"; "A [chart type] showing that [chart title]"; dashboards "difficult to make accessible" |
| ONS accessibility statement (reviewed Dec 2025) | Practice | At source; verified | "partially compliant"; "underlying data are accessible through other formats" |
| Analysis Function: Data visualisation: building and managing dashboards; dashboard software (both 6 Feb 2026) | Standard (official statistics) | At source; "rarely" sentence spot-checked; verified (two wordings corrected) | "Dashboards rarely meet full accessibility requirements"; "greater control" in R and Python |
| Analysis Function: Making charts accessible, DataConnect22 Q&A (2022); Making analytical publications accessible (29 Oct 2020); Data visualisation: charts (19 May 2022); Releasing statistics in spreadsheets (30 Jun 2021) | Standard (official statistics) | At source; verified | "I am yet to find a fully accessible dashboard"; "never be in both the alt attribute and the body text"; SVG |
| Accessibility statements: UKHSA data dashboard (19 Dec 2023); OHID Fingertips | Practice | At source; verified | "partially compliant"; colour alone fails 1.4.1; "not keyboard operable" |
| Accessibility statements: Public Health Scotland (18 May 2026); Scottish Borders Council (29 May 2025); Kingston Data (18 Feb 2026) | Practice | At source; verified | "Title of the graph… is an image of text"; Power BI keyboard and colour failures |
| Accessibility statements: Manchester City Council (25 Mar 2026); Kent County Council (9 Jun 2026); Eurostat (12 Feb 2026) | Practice | At source; verified | Three third-party handlings; "do not always have text alternatives" |
| GOV.UK Design System: accessibility strategy; accessibility statement (18 Dec 2024); Service Manual: Service Standard point 5; Understanding WCAG 2.2; Making your service accessible | Standard (design system) | At source; verified | "does not immediately make that service accessible"; "Inclusive, accessible services are better for everyone" |
| NHS digital service manual: accessibility content and design (Feb 2025); How we write (2019); Health literacy (2023) | Standard (design system) | At source; verified | "reading age of 9 to 11" unsourced; "ideally under 125 characters"; no raster text |
| BBC GEL technical guide, Infographics (2021) | Practice | At source; verified | Alt text "a literal interpretation"; caption "an editorial summary"; "avoid creating interactive visualisations" |
| BBC Mobile Accessibility Guidelines; BBC R&D | Practice | Unreached (domain blocked) | Not quoted |
| Datawrapper; Flourish; Highcharts; Vega-Lite; Tableau; Power BI accessibility documentation | Practice (vendor documentation) | At source; verified | Keyboard navigation claims; Power BI 250-character alt text; "a few known problems" |
| Overlay Fact Sheet; FTC press releases (3 Jan and 22 Apr 2025) | Practice | At source; verified | "full compliance cannot be achieved with an overlay"; $1 million consent order |
| GDS blog comment (23 Jul 2013) | Practice | At source; verified | "I'd rather we didn't build a separate 'accessible' site" |
| Nightlife Culture: Style Guide v1.5 §13 (the floor), §02 (hierarchy), §04 (register), LNG and DSH rules | Nightlife Culture | Read directly | The floor mapped to criteria; brand-against-access hierarchy; register meets COGA |
| Nightlife Culture: The Decision Book, Chapter 15 (dashboards) and the rule register | Nightlife Culture | Read directly | "nothing load-bearing in a tooltip"; non-interactive route |
| Nightlife Culture: the Vibe Setting Framework's phone-read test | Nightlife Culture | House, confidential; cited, not reproduced | Community's reading-level standard |
| Version 1, Chapter 11 (archived) | Nightlife Culture | Positions tested, not sources | No parallel version; "keep turning out to be the same build"; distribution argument |


## 18 · Version 2 — Chapter 14: Where evidence meets expression (6 October 2026)

*Legend as §5, §10, §15, §16 and §17. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (four pages: MoMA record 163892; the anthropographics Experiment 2 analysis page; the Nature Figure 1 caption; Understanding 1.1.1); "verified" — the independent verification pass re-traced it against the agents' returns (about 850 quoted strings, all matching; about twenty marks added; one count corrected — Kineticharts asks three comprehension questions — and eight items confirmed at source, two unreachable). "Read once" means a single fetch with no presence check; "abstract" means only the abstract was reachable; "secondary" means read through another source; "not read" means unreachable and nothing quoted.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| **Theory and method** | | | |
| Mackinlay 1986, Automating the Design of Graphical Presentations, *ACM TOG* 5(2) | Standard (method) | Verified; bar example read once; Figures 14/15 not machine-readable | "encodes all the facts in the set"; "encodes only the facts in the set" (the removal test) |
| Munzner 2009, A Nested Model for Visualization Design and Validation, *IEEE TVCG*; 2015 slides; textbook principles | Standard (method) | Verified; two sentences read once; 2015 slides verified; textbook via two course pages, secondary | Nested model places the boundary at the encoding level |
| Kosara 2007, Visualization Criticism, *IV 2007* | Standard (method) | Verified; three sentences read once | "on opposite ends of the sublimity scale"; "a third way" |
| Viégas & Wattenberg 2007, Artistic Data Visualization, *HCII 2007* | Standard (method) | Verified; one sentence read once | "visualizations of data done by artists with the intent of making art" |
| Lau & Vande Moere 2007, Towards a Model of Information Aesthetics, *IV 2007* | Standard (method) | Abstract (via mirror); axes secondary (Roberts 2024) | "proposes a model of information aesthetics in the context of information visualization" |
| Vande Moere & Purchase 2011, On the role of design in information visualization, *Information Visualization* 10(4) | Standard (method) | Abstract; one sentence secondary (Quispel et al. 2018) | "balancing the three requirements of utility, soundness and attractiveness" |
| Pousman, Stasko & Mateas 2007, Casual Information Visualization, *IEEE TVCG* 13(6) | Standard (method) | Verified | Frame for a public display read by non-analysts; social and reflective insight |
| Dörk, Feng, Collins & Carpendale 2013, Critical InfoVis, *CHI 2013 EA* | Standard (method) | Verified; three sentences read once | Four principles as a check on the house's own position |
| D'Ignazio & Klein 2020, *Data Feminism* ch. 3, MIT Press | Standard (method) | Verified; four sentences read once | The argument against plainness: its principle on emotion and its concession |
| Correll 2019, Ethical Dimensions of Visualization Research, *CHI 2019* | Standard (method) | Verified; one sentence read once | "All visualizations are rhetorical, and have the power to potentially persuade" |
| Correll & Heer 2017, Black Hat Visualization, DECISIVe | Standard (method) | Verified | "visualizations which have fidelity to the underlying data" — faithful, and still harmful |
| Kostelnick 2008, The Visual Rhetoric of Data Displays, *IEEE TPC* 51(1) | Standard (method) | Not read; characterised only via Prantl, Möller & Koesten | Not quoted; listed among full texts to obtain |
| Hullman, Adar & Shah 2011, Benefitting InfoVis with Visual Difficulties, *IEEE TVCG* | Standard (method) | Verified; "desirable difficulties" read once | "non-efficient visual elements may benefit comprehension and recall" |
| Chevalier et al. 2016, Animations 25 years later, *AVI 2016* | Standard (method) | Abstract | Roles of animation; full role list left to further research |
| Tufte 2006, Analytical design and human factors (forum post); Tufte's books | Standard (method) | Forum post verified; books not read; rules secondary (Wikipedia, InfoVis-Wiki, Stasko slides, Boxes and Arrows, data.europa.eu) | "spare, straightforward, conventional, and self-effacing" |
| **Conventions of objectivity** | | | |
| Kennedy, Hill, Aiello & Allen 2016, The work that visualisation conventions do, *Information, Communication & Society* 19(6) | Evidence of method | Verified; three sentences read once | "objectivity, transparency and facticity"; four conventions |
| Kennedy, Hill, Allen & Kirk 2016, Engaging with (big) data visualizations, *First Monday* 21(11) | Evidence | Verified (n, ages, effectiveness sentences); factors abstract; "did not like it" read once | Participant n and ages; effectiveness findings; the "did not like it" response |
| Quispel, Maes & Schilperoord 2018, Aesthetics and Clarity in Information Visualization, *Arts* 7(4) | Evidence | Read once | Ten designers, 26 handbooks; clarity and aesthetics |
| Arunkumar, Padilla, Bae & Bryan 2023, Image or Information?, *IEEE TVCG* | Evidence | Verified | 500 annotated visualisations; image-rated displays convey less |
| Sunlight Foundation, Cesal 2014, data visualization style guide launch post | Evidence of method | Verified | Polished charts "taken more seriously" for attention to detail |
| **Affect and persuasion** | | | |
| Boy et al. 2017, Showing People Behind Data, *CHI 2017* | Evidence | Verified; measures read once | "very similar effects on empathy and prosocial behavior" |
| Morais, Jansen, Andrade & Dragicevic 2020, Showing Data about People, *IEEE TVCG* | Evidence | Not read; dimensions via Sorapure 2022 and the authors' catalogue, secondary | Anthropographics design-space dimensions, second-hand |
| Morais et al. 2021, Can Anthropographics Promote Prosociality?, *CHI 2021* | Evidence | Paper not read; abstract read once; analysis pages verified, re-checked at source; standardised effect read once | Effect 3.4 [0.021, 6.8]; n 786 |
| Campbell & Offenhuber 2019, Feeling numbers, *Information Design Journal* 25(1) | Evidence | Abstract | "appeals to emotion through proximity techniques" |
| Lan, Shi, Wu, Jiao & Cao 2021, Smile or Scowl?, *IEEE TVCG* | Evidence | Verified; several sentences read once | 976 infographics; 490 participants; 117,120 ratings |
| Lan, Shi, Zhang & Cao 2021, Kineticharts, *IEEE VIS/TVCG* | Evidence | Verified; comprehension sentence read once | "60 animated charts for the five affects"; comprehension similar to baseline |
| Lan, Wu & Cao 2023, Affective Visualization Design, *IEEE TVCG* | Evidence | Verified; design-space sentence, task list and "not at odds" sentence read once | "kept 109 papers"; "identified 61 projects"; "not at odds" |
| Lan, Wu, Chen & Cao 2023, The Chart Excites Me!, *IEEE TVCG* | Evidence | Verified | 265 visualisations, 184 participants; design features that carry feeling |
| Lee-Robbins & Adar 2022, Affective Learning Objectives for Communicative Visualizations, *IEEE TVCG* | Evidence of method | Verified; template and abstract sentences read once | Twelve interviews; template for writing an affective intent down |
| Bartram, Patra & Stone 2017, Affective Color in Visualization, *CHI 2017* | Evidence | Verified; several sentences read once | 8608 images; 76 persons; "Trustworthy showed very little structure" |
| Anderson & Robinson 2022, Affective Congruence in Visualization Design, *IEEE TVCG* 28(8) | Evidence | Abstract | "affectively congruent colors" on maps; no accuracy gain claimed |
| Blair, Wang & Perin 2024, Quantifying Emotional Responses, *IEEE TVCG* | Evidence | Read once | "certain data characteristics influence the emotion of viewers even when the data has no meaning" |
| **Perception, polarity, redundancy, difficulty, glance, distance** | | | |
| Piepenbrock, Mayr, Mund & Buchner 2013, Positive display polarity, *Ergonomics* 56(7) | Evidence | Verified | 85 older and 84 younger adults; positive polarity; d = 2.17 and 0.58 |
| Buchner & Baumgartner 2007, Text–background polarity, *Ergonomics* 50(7) | Evidence | Abstract | "proofreading performance was consistently better with positive polarity" |
| Dobres, Chahine & Reimer 2017, Ambient illumination, contrast polarity, letter size, *Applied Ergonomics* 60 | Evidence | Abstract, read once | Legibility thresholds highest for negative polarity in dark ambient light |
| While & Sarvghad 2024, Dark mode or light mode?, *IEEE VIS short papers* | Evidence | Verified; abstract count discrepancy noted | "did not always match their preferred polarity"; both polarities available |
| Budiu 2020, Dark Mode vs. Light Mode, Nielsen Norman Group | Evidence | Read once | Performance "tends to be better with light mode" |
| Nothelfer, Gleicher & Franconeri 2017, Redundant Encoding, *JEP: HPP* 43(9) | Evidence | Verified; boundary sentence and most n values read once | Redundant encoding measured in small lab experiments |
| Ottley, Kaszowska, Crouser & Peck 2019, Combining Text and Visualization, *EuroVis short papers* | Evidence | Verified; integration sentence read once | 32 participants; "no significant effect"; a twin beside a form is not thereby read |
| Stokes, Setlur, Cogley, Satyanarayan & Hearst 2022, Striking a Balance, *IEEE TVCG* | Evidence | Abstract | 302 participants; text on the chart not penalised |
| Xie, Zhou & Liu 2018, Null Effects of Perceptual Disfluency, *Educational Psychology Review* 30(3) | Evidence | Verified | 25 articles, 3135 participants; no effect of disfluency on recall |
| Weissgerber, Terhorst & Rummer 2024, *Metacognition and Learning* 19 | Evidence | Abstract | "null results for disfluency, WMC, and their interaction for all learning outcomes" |
| Few 2011, Benefitting InfoVis with Visual Difficulties? Provocation Without a Cause, perceptualedge.com | Evidence | Read once | "unnecessary cognitive effort, without benefit" (practitioner rebuttal) |
| Jansen, Dragicevic & Fekete 2013, Physical Visualizations, *CHI 2013*; Dragicevic & Jansen 2018 re-analysis | Evidence | Abstract, strings verified there; n via re-analysis, verified | "the first infovis study comparing physical to on-screen visualizations" |
| Blascheck et al. 2019, Glanceable Visualization, *IEEE TVCG* 25(1) | Evidence | Verified; n and task read once | Watch-sized chart; eighteen participants in each of two studies |
| Garvey, Pietrucha & Meeker 1997, Font and Capitalization on Guide Signs, *TRR* 1605 | Evidence | Abstract (a Clearview study; silent on case) | Clearview font study, 48 older drivers; not a mixed-case study |
| Garvey, Eie & Klena 2016, *Interdisciplinary Journal of Signage and Wayfinding* 1(1) | Evidence | Verified; reconciliation read once | "Sixty-four subjects from 19-87 years of age viewed 64 displays using 33 fonts" |
| Tejero, Royo & Roca 2024, *Human Factors* | Evidence | Secondary (ResearchGate rendering), read once | "No support for differences in the legibility distance" between title and upper case |
| Bertucci & Crawford 2015, Best Practice Standards for On-Premise Signs (USSC Foundation 2018) | Evidence | Verified | The legibility index: letter height from reading distance |
| Bullough 2017, Factors Affecting Sign Visibility, Conspicuity and Legibility, *IJSW* 1(2) | Evidence | Verified (Forbes et al. 1965 sentence is Bullough's) | "Only 3-4 short, familiar words can be read in a single glance at a sign" |
| Traffic Signs Manual, Chapter 7 (TSO) | Standard (regulator) | Verified; x-height table not extracted | "The size of an alphabet is specified in terms of its x-height" |
| Lamar; Clear Channel Outdoor design-tips pages | Practice | Read once; no source cited on either | "say it in seven words or less"; the rule with no study behind it |
| Bitgood 2000, The Role of Attention in Designing Effective Interpretive Labels, *J. Interpretation Research* 5(2) | Evidence | Verified for Borun & Miller 18% and Serrell median 8 minutes; others read once | "three principles of attention"; label reading times |
| Boukhelifa, Bezerianos, Isenberg & Fekete 2012, Sketchiness as a Visual Variable, *IEEE TVCG* 18(12) | Evidence | Abstract, read once | "sketchiness is a viable alternative for the visualization of uncertainty in lines" |
| Lazard & Atkinson 2015, *Science Communication* 37(1) | Evidence | Abstract (measures elaboration, not credibility) | Cited in the log only |
| Li & Moacdieh 2014, *Proceedings of the HFES Annual Meeting* 58(1) | Evidence | Abstract | Cited in the log only |
| **Official, regulatory and standards** | | | |
| Government Analysis Function, Data visualisation: infographics (17 Aug 2022) | Standard (official statistics) | Verified; negative findings checked | "provide a plain text alternative explaining all the information within the infographic" |
| Government Analysis Function, Charts; Charts: a checklist; Colours in charts; Accessible publications; Advice for policy professionals §10 | Standard (official statistics) | All verified; sentences marked read once where so | List to avoid: "shaded backgrounds", "unnecessary borders", "3D shapes" |
| GOV.UK content guidance, Images; GOV.UK Design System, Images; Design System backlog issue #177 (Dark Mode) | Standard (design system) | Guidance and Design System verified; issue #177 read once | "provide a plain text version of the content"; open dark-mode issue since December 2018 |
| NHS digital service manual, Icons (June 2026) and Images (January 2025) | Standard (design system) | Verified | "Use icons sparingly, and not for decoration." |
| ONS service manual: Data visualisation principles; Chart elements; Colours; Interactive charts and animations; Dashboards; Chart text; Design System Image; Brand guidelines | Standard (official statistics) | Verified; sentences marked read once where so | "never make an animation the only way to get the information"; "backgrounds" as decoration |
| W3C, WCAG 2.2 Understanding 1.1.1, 1.2.1, 1.2.2, 1.2.3, 1.2.5, 1.4.2; WAI Images Tutorial (8 Apr 2026) | Standard (W3C) | Verified; sensory-experience definition and decoration note re-checked at source; intent sentences read once where so | "specific sensory experience"; "words cannot fully capture"; decoration as a removal test |
| Material Design (archived v1), Accessibility; Carbon Design System: Motion, Pictograms, Accessibility | Standard (design system) | Verified; Material sound sentence and one Carbon sentence read once | "Give visual alternatives to sound, and vice versa."; Carbon productive and expressive motion |
| Office for Statistics Regulation: Code of Practice 3.0; letter 27 Feb 2023; political support statement; two blogs (24 May, 30 Aug 2024) | Standard (regulator) | All verified; one sentence read once in the statement and each blog | "cannot be dismissed as just a matter of opinion"; "the y-axis beginning at 8%" |
| Greater London Authority, City Intelligence Data Design guidelines v2.0 (May 2019) | Standard (design system) | Two passes agree; dark-ground lines read once | "All colours work on a dark background"; dark-ground palettes |
| data.europa.eu Data Visualisation Guide, Chart junk and data ink pages (2023) | Standard (official statistics) | Verified; two sentences read once | "a lot of chart junk is actually harmless"; "harmfull junk" |
| **Newsrooms and platforms** | | | |
| The Pudding: about; pitch; This is a teenager (March 2024); Is the love song dying? | Practice | Verified; pitch "no-go" sentence read once; Is the love song dying? not read beyond title | "Is it an argument, or just a topic?"; first screen is a written sentence |
| Our World in Data, life-expectancy grapher | Practice | Verified fragments; source line and headings read once | Source and date block before the chart; "Next expected update" |
| ONS, Explore Local Statistics; Census area changes template and one area page | Practice | Verified; dates and method sentences read once | "Find an area"; input before any chart, map or statistic |
| BBC (blocked); Leimdorfer, Data Journalism at the BBC; Applied Works (Medium, 11 Apr 2023); BBC-Data-Unit GitHub | Practice | BBC not read (blocked); Handbook and Applied Works verified; GitHub read once | "the most shared BBC page ever"; BBC audit not determinable |
| Gapminder: home; Upgrader; Dollar Street; Ignorance Project; 2017 and 2019 studies | Practice | Verified; 2019 n read once | "You are probably wrong about"; "photos as data to kill country stereotypes" |
| MoMA records 163892, 447623, 447622, 215813, 216726, 216731, 110268; artist pages 136154, 67122; records 447620, 110269; press release 14 Feb 2013; V&A O1247173; Art Institute of Chicago 213139 | Practice | Records verified at the record (163892 spot-checked); 447620, 110269, press release read once; V&A date field read once; Art Institute verified | Museum records of data works; "an expressive interpretation of reality"; a record's date is the version's |
| Pulitzer Prizes, Mona Chalabi 2023; Dezeen (16 Nov 2023); It's Nice That (8 Mar 2018); Nightingale (1 Nov 2019); monachalabi.com | Practice | Verified; monachalabi.com read once ("Under construction") | "computer-generated images overstate certainty"; "You'll never see decimal places on my illustrations" |
| Halloran, N., The Fallen of World War II (neilfilms.com/ww2) | Practice | Verified; first elements read once | Mode choice leads, with no data input |
| Raworth, kateraworth.com/doughnut and doughnuteconomics.org; Fanning & Raworth 2025, Doughnut monitors, *Nature* 646, 47–56 | Practice | Verified; both Figure 1 caption sentences re-checked at source (spot-checked) | Caption prints its own defect: "a quadratic scaling of wedge area"; 35 indicators |
| Pomerance, Boyd & Dörk 2026, Navigating and Narrating Interactive Flowcharts, *J. Visualization and Interaction* 1(1); OSF 5usfm | Practice | Verified; several figures read once; OSF not read | 177 survey responses, 23,346 logged sessions; the evaluated exception |
| Data Visualization Society, IIB Awards status and FAQ; informationisbeautifulawards.com about and 2024 winners | Practice | Verified | Eight IIB criteria, none on accuracy |
| Centre for Thriving Places, dashboard and about pages; GLA Night Time Data Observatory landing and theme pages | Practice | Verified; methodology PDF not read (image only); counts read once | "Welcome to the Night Time Data Observatory."; "over 30 data sources"; 24 entries |
| ABC News (Australia), What's driving up burger prices? (5 Aug 2024) | Practice | Verified | Leads with a written sentence, no input; sources once at the end |
| Financial Times, Visual Vocabulary README; Datawrapper blog (24 Jul 2023; 29 May 2018); The Economist, Leo 2019, Mistakes, we've drawn a few; Urban Institute style guide; ProPublica news-apps guide | Practice | Verified; Economist headings read once | "Avoid 3-D charts at all costs."; "Stay away from 3-D."; "crimes against data visualisation" |
| Lupi 2017, Data Humanism (PrintMag; giorgialupi.com); dear-data.com/theproject; stefanieposavec.com/dear-data-about | Practice | Verified | Four headings, e.g. "Embrace Complexity"; "a slower, more analogue way" |
| **House** | | | |
| Nightlife Culture Style Guide v1.5 §06 evidence standard; Decision Book Ch 7, Ch 10, Ch 18 (tier test; BRK-07; override log); rule register; Version 1 Chapters 12 and 13 (archived) | Nightlife Culture | House documents; no status given | "Strong design must never make weak evidence look stronger than it is" |


## 19 · Version 2 — Chapter 15: Learning from the best (6 October 2026)

*Legend as §5, §10 and §15–§18. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (five pages: the PHE RAG guide; the OECD Regional Well-Being user guide; NatCen's PCOS 2023 page; the English Indices of Deprivation 2025 FAQ; the UKHSA dashboard's Compliance page); "verified" — the independent verification pass re-traced it against the agents' returns (about 800 quoted strings, none differing in wording; about twenty marks added; several counts and attributions corrected — among them the measles chart's four-week window, the Fingertips amber rule, the pre-release Order's wording, the "interesting rather than useful" scope — and six targets confirmed at source). "Read once" means a single fetch with no presence check; "two passes" means returned identically twice without a presence check; "abstract" means only the abstract was reachable; "secondary" means read through another source; "not read" means unreachable and nothing quoted.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| **Public health** | | | |
| UKHSA data dashboard: Compliance page (9 Jul 2024); metrics documentation index and cases page (12 Feb 2025); What's new; Access our data; COVID-19 archive data download (1 May 2025) | Practice; Standard (official statistics) | At source; verified; items read once where so; Compliance page spot-checked (presence check, false control rejected) | "it is not possible for the dashboard to be classed as official statistics"; "so we commit to update the data at 4pm every Thursday"; five-heading metric page; labelled change log |
| PHE/UKHSA blogs: Using data to track the virus (23 Apr 2020); The COVID-19 dashboard (4 Sep 2020); Behind the scenes (22 Mar 2021); UKHSA data dashboard takes over (21 Dec 2023) | Practice; Evidence (self-reported) | At source; verified; sentences read once where so | "over 300,000 unique users every day"; trust "90.3%", up from "73.4%", with no n or wording |
| OSR, State of the UK's statistical system 2020/21, Case Study 6 (14 Jul 2021) | Standard (regulator) | At source; verified | "one of strongest examples of open data and statistics being used by a huge number of individuals" |
| PublicTechnology (19 Jul 2022) on the RSS/OSR award | Practice | Secondary | Award for voluntary adoption of the Code of Practice for Statistics |
| GDS/UKHSA, Winter Viruses Dashboard Alpha Assessment (14 Feb 2025) | Practice | At source; verified; two sentences read once | "create a measurement framework that demonstrates how metrics map to key performance indicators (KPIs) and goals" |
| PHE, Technical Guide: RAG Rating Indicator Values (20 Jun 2017); Spine Charts (2017); Funnel Plots (13 Dec 2017) | Standard (official statistics) | At source; verified; spot-checked (the rule and the one-in-twenty sentence); Spine Charts and Funnel Plots read once | "indicator values should only be given red or green RAG ratings if they are statistically significantly higher or lower than the comparator"; "one in twenty red or green ratings could be expected" |
| OHID, Public health technical guidance: Confidence intervals; Proportions; Trend markers; Fingertips API (comparator methods, comparators, significances, recent trends; indicator metadata CSV, indicator 90366); Geography change log; New Service Updates | Standard (official statistics); Practice | At source; verified; items read once where so (header row as a whole read once; twelve header fields and method names verified); Geography change log and New Service Updates read once; "Find public health data" verified | "There must be at least five points in the series"; "χ² > 9.5495"; "The preferred OHID method is the Wilson Score method"; thirty-two-field metadata record |
| Public Health Scotland, Toolkit README | Practice | Read once; chart and dashboard guidance not read (site retired) | Not quoted in the chapter body |
| JHU CSSE: Gardner, Mapping COVID-19 (blog, 2020); Dong, Du & Gardner 2020, *Lancet Infect Dis* 20(5); Dong et al. 2022, *Lancet Infect Dis* 22(12), e370–e376; CSSE repository README; JHU Hub retirement notice (10 Feb 2023); CSSE project page | Practice; Evidence (†) | Blog and retirement notice at source; verified (reason and dates read once); Dong 2020 not read; Dong 2022 abstract; README read once (banner and licence verified); project page verified for the requests figure, qualifier read once | "launched the first global real-time coronavirus surveillance system" (†); errata.csv for own errors, dated list for source revisions; notice, final update 10 March 2023 |
| Hasell et al. 2020, A cross-country database of COVID-19 testing, *Scientific Data* 7:345 | Evidence of method | At source; verified; unit labels and the corrections sentence's first clause read once | "a URL at which the specific observation of the corresponding raw data can be found"; unit labels per series |
| Mathieu et al. 2021, A global database of COVID-19 vaccinations, *Nature Human Behaviour* 5:947–953 | Evidence of method | At source; verified; one sentence read once | "regularly audited for accuracy against the original official sources"; "We do not audit official reports beyond technical validation" |
| OWID, covid-jhu-who (28 Feb 2023); Future updates of our data on COVID-19 (15 Nov 2024); covid-19-data README | Practice | At source; verified; items read once where so | "The URL of all our charts and the variable names in our dataset will remain the same"; dataset-by-dataset sunset note |
| WHO COVID-19 dashboard, About | Practice | At source; verified | "Caution must be taken when interpreting all data presented"; the aggregator's standing disclaimer |
| Ivanković et al. 2021, *J Med Internet Res* 23(2):e25682 | Evidence of method | At source; verified; several figures read once; the 93/158 slip noted | "158 dashboards from 53 countries"; "Only 20 of the 158 dashboards (12.7%) stated both their primary purpose and intended audience"; seven features of actionability |
| Barbazza et al. 2021, medRxiv preprint (published *Digital Health* 2022, not read) | Evidence of method | At source; verified; items read once where so | "the importance of disclosing errors as they happen"; "monitoring user analytics was not pursued" |
| Ismail et al. 2022, *BMC Public Health* 22:2453 | Evidence | At source; verified (n; views; 76.4%); design and limits read once | "76.4% of respondents reported that the dashboard influenced their personal planning and behaviour" |
| Padilla et al. 2022, *Scientific Reports* 12:2014 | Evidence | At source; verified (N; 34 techniques); findings read once | "cumulative y-axis can show only an upward or flat trend"; y-axis alone shifts perceived risk |
| Crepaz & Arikan 2021, LSE blog (article in *J Elections, Public Opinion and Parties*, not read) | Evidence | At source; verified; two sentences read once; secondary (authors' blog) | "information disclosure has no direct effects on willingness to trust"; "a 6% drop in political trust" |
| Clarkson 2023; Bos et al. 2021; Human Behavior and Emerging Technologies 2021 | Evidence | Read once / abstract (entry does not say which); cited in the log only | Cited in the research log only; not quoted in the chapter body |
| OSR, Regulatory guidance: Dashboards (21 Aug 2025; last modified 15 Jun 2026) | Standard (regulator) | At source; verified; minimum list read once except the retirement bullet | "come with a plan for maintaining, updating and retiring the dashboard"; the minimum list for an official dashboard |
| Arleo et al. 2025, arXiv 2503.15529 | Evidence | Read once; cited in the log only | Cited in the research log only; not quoted in the chapter body |
| **Finance and risk** | | | |
| Haldane & McMahon 2018, *AEA Papers and Proceedings* 108:578–83 (authors' manuscript) | Evidence | At source; verified; several figures read once | "the new layered content is easier to read and understand"; 285 members of the public; Flesch-Kincaid 7.8 against 13.4 |
| Bholat, Broughton, Parker, Ter Meer & Walczak 2018, Bank of England SWP 750 (JME version) | Evidence | At source; verified; arms, scales and the 2.85/2.02 sentence read once; JME abstract: abstract (†) | "improved the average comprehension score by 25% (0.5 points)"; "42% (0.8 points)"; "the simplification of language increases public comprehension more than the inclusion of visuals" (†) |
| Haldane 2018, Climbing the Public Engagement Ladder (speech) | Practice | At source; verified | "around 95% of all the words central banks utter are inaccessible to around 95% of the population"; "a one-sentence, one-graphic version for the time-poor" |
| Haldane, Macaulay & McMahon 2020, Bank of England SWP 847 | Evidence | At source; verified | Layered communication; the Bank's reasons for layering |
| McMahon & Naylor 2023, Bank of England SWP 1,047 | Evidence | Abstract (†) | "conceptual complexity has actually increased" while sentences shortened (†) |
| Bank of England, Quarterly Bulletin (17 Oct 2025) | Practice | At source; verified; one sentence read once | "A new Monetary Policy Overview will set out how the analytical inputs have informed the MPC's collective policy decision."; fan charts continued "For now" |
| Britton, Fisher & Whitley 1998, Bank of England Quarterly Bulletin Q1 | Standard (method) | At source; verified; two sentences read once | The 1998 fan-chart band rule: 10 per cent of the distribution per pair of bands; "without claiming a spuriously high degree of precision" |
| Bank of England, Monetary Policy Report November 2025, Chart 3.1 footnote | Standard (method) | At source; verified in part (second clause of the band sentence; pandemic exclusion; skew sentence); the rest two passes | The 30-occasion band rule; "exclude errors during the pandemic given its exceptional nature" |
| Bernanke review, 12 Apr 2024 | Standard (method) | At source; verified; two sentences read once | "They should be eliminated."; "little attention from the public" with no survey cited |
| McMahon, Naylor, Rholes & Rickards 2026, Bank of England SWP 1,196 | Evidence | At source; verified; Part II n: abstract (†) | "fan charts are well understood and perform best at jointly conveying both expectations and uncertainty"; 300 public and 75 experts |
| Tak, Toet & van Erp 2014, *IEEE TVCG* 20(6) | Evidence | Abstract (†) | "perceived certainty is affected by its visual representation"; "Participants (n = 140)" |
| OBR Briefing Paper 4 (2012); EFO October 2021 box; FER October 2024 Box 2.1 | Standard (method); Practice | At source; verified; one sentence read once | "10 per cent probability bands"; bands "show the outcomes that someone might anticipate if they believed that forecast errors in the past 20 years offered a reasonable guide" |
| BIS Quarterly Review (16 Mar 2026) | Evidence | At source; verified | "Fan charts are the most common tool, published by almost 75% of the 25 central banks in our sample in 2025" |
| ESRB Risk Dashboard, Issue 56 (2 Jul 2026) and Annex I | Standard (regulator) | At source; verified; threshold sentence read once | "The risk dashboard should not be considered to be a policy statement on systemic risks"; data cut-off date on the face |
| EBA Risk Dashboard Q4 2024 and Q4 2023 | Standard (regulator) | At source; colour rule verified; two threshold rows returned identically twice (not string-verified); others not printed | "Traffic lights provide the trend of the RI risk indicator"; fixed thresholds applied to shares of banks' assets |
| Aikman et al. 2015, FEDS Notes | Practice | At source; verified; colour and caveat sentences read once | Heat map standardised against history; "the arrival of additional data can change the standardized and rescaled values" |
| ECB Financial Stability Review, December 2011 | Practice | Read once | An aggregate that "did not reflect the crisis in certain euro area countries" |
| Bank of England FPC, CCyB policy statement (12 Jul 2023) | Standard (regulator) | At source; verified | Decisions "are not mechanically tied to any level or rate of change for an individual or specific combination of indicators" |
| ALFRED (St Louis Fed), about and home | Practice | At source; verified | "Economic data time travel since 2006."; "a collection of vintage versions of U.S. economic data" |
| Croushore & Stark 2001, *Journal of Econometrics* 105(1):111–130 (Philadelphia Fed WP 99-4) | Evidence | At source; verified; one sentence read once | "the coefficients change dramatically" on later vintages; results "generally robust" for many studies |
| ONS: National Accounts Revisions Policy (Jan 2026); GDP first quarterly estimate April–June 2026 (13 Aug 2026); GDP QMI (8 Apr 2022); revisions triangles dataset | Standard (official statistics) | At source; verified; definitions read once | "A revision is a scheduled change"; "A correction is an unplanned revision"; "The mean absolute revision between the first and final estimates is 0.27 percentage points" |
| ONS pre-release access statement | Standard (official statistics) | At source; verified | "pre-release access to Office for National Statistics (ONS) statistics was removed in all but exceptional circumstances" |
| Pre-release Access to Official Statistics Order 2008, SI 2008/2998 | Standard (law) | At source; verified (paras 3, 4); paras 5 and 9 read once | 24-hour limit on pre-release access; published list of persons given early access |
| IMF SDDS Guide 2013; IMF factsheet 2023 | Standard (method) | At source; verified; one sentence read once | Advance release calendar; "simultaneous release to all interested parties" |
| van der Bles, van der Linden, Freeman & Spiegelhalter 2020, *PNAS* (Europe PMC full text) | Evidence | At source; verified; arm sizes read once | "only a small decrease in trust in numbers and trustworthiness of the source, and mostly for verbal uncertainty communication"; "total n = 5,780" |
| Galvão & Mitchell 2021, ESCoE DP 2021-06 / Cleveland Fed WP 21-28 | Evidence | At source; verified; wave-one n read once | "improves the public's understanding of data uncertainty, but does not reduce its trust in the statistical office" |
| Runge 2021; Runge & Hudson-Sharp 2020 | Evidence | Read once / abstract (entry does not say which); cited in the log only | Cited in the research log only; not quoted in the chapter body |
| OSR, Revisions of estimates of UK GDP (29 Nov 2023); Approaches to presenting uncertainty (21 Sep 2022) | Standard (regulator) | At source; verified | "the uncertainty surrounding these statistics is in itself a key message"; uncertainty "better depicted and described in statistical bulletins" than in dashboards |
| Cox 2008, *Risk Analysis* 28(2):497–512 | Evidence of method | Abstract (†); two sentences read once | "Typical risk matrices can correctly and unambiguously compare only a small fraction (e.g., less than 10%) of randomly selected pairs of hazards." |
| Eurostat, Flags and special values | Standard (official statistics) | At source; verified; list partly read once | Status flags "p = provisional", "e = estimated", "b = break in time series" |
| Analysis Function, Using symbols and shorthand (11 Jan 2022) | Standard (official statistics) | At source; verified; one sentence read once | "[p] = provisional", "[r] = revised", "[f] = forecast" in square brackets |
| **Economic development and place** | | | |
| ONS: Explore Local Statistics service QMI (25 Apr 2025); Clustering similar local authorities and statistical nearest neighbours (18 Mar 2026); an indicator page; Analysis Function case study and blog (13 Jun 2025); National Statistical blog (26 Mar 2024); GSS subnational data strategy | Standard (official statistics); Practice | At source; verified; metadata list and reach percentages' context read once | "K-means clustering"; "ordered list of the 20 most similar areas"; "93% of users found it easy to use" with no n |
| Nomis: About; First-time visitors; a dataset page; release calendar; 2004 update note | Practice | At source; verified; items read once where so | "First launched in 1981"; "Revisions and corrections" per dataset; release calendar with "Confirmed" or "Provisional" status |
| MHCLG: English Indices of Deprivation 2025 (FAQ; Research Report; Technical Report, 30 Oct 2025); IoD 2019 FAQ; Indices Futures consultation response (22 Dec 2022) | Standard (official statistics) | At source; verified; FAQ rank sentence returned identically three times by the agent and confirmed at source (spot-checked) | "a small area with a rank of 1,000 is not half as deprived as a place with a rank of 500"; "should not be viewed or construed as a time-series" |
| ONS Health Index: Health in England 2015 to 2021 (16 Jun 2023); methods and development; 2015–2018 methods; ONS blog (3 Dec 2020) | Standard (official statistics); Practice | At source; verified; structure and weighting details read once | "comparisons can be made between scores over time"; "Next release: To be announced" |
| Scottish Government, National Performance Framework: performance overview; indicator performance page; gov.scot collection; Cabinet Secretary letter (15 Sep 2026) | Standard (official statistics); Practice | At source; verified; category labels read once; per-indicator pages not read (redirect) | "improving, maintaining or worsening based on the change between the last two data points of an indicator"; thresholds not retrievable |
| Welsh Government, Quality information for the Wellbeing of Wales report 2026 (1 Oct 2026) | Standard (official statistics) | At source; verified; two sentences read once | "We assign each measure as either improved, deteriorated, no change or not assessed"; significance test or data-expert judgement |
| OECD Regional Well-Being: landing page; User Guide (Oct 2025) | Standard (method); Practice | At source; verified; spot-checked (no-composite, ±5 per cent and Manhattan-distance sentences); method details read once | "The web tool does not include a regional composite well-being index"; ±5 per cent arrow rule |
| Centre for Cities: data tool; Cities Outlook 2026 (26 Jan 2026) | Practice | At source; verified; purpose sentence read once | Ranked tables ("10 cities with the highest") with no intervals, as contrast |
| What Works Growth: Scientific Maryland Scale page; Scoring Guide (Jun 2016); Enterprise Zones rapid evidence review (May 2025) | Standard (method); Practice | At source; verified | "We define SMS 3 methods to be the minimum standard for our reviews"; before-and-after excluded as unattributable |
| Levelling Up White Paper technical annex (Feb 2022); Statement of Levelling Up Missions (25 Jan 2024); Levelling-up Missions Annual Reports 2024–25 (May 2025) and 2025–26 (Jul 2026) | Standard (official statistics); Practice | At source; verified; geography sentences read once | "this is an important data gap"; "Social Fabric Index: not implemented"; "has moved away from the levelling up programme" |
| Scottish Government, Near time data service: dashboard user engagement (13 Aug 2024) | Evidence of method | Read once (figures returned on verification pass) | "41 users completed the survey in Microsoft Forms. This equates to a 5% response rate."; whether data informed "their decisions or conclusions as part of their role" |
| JRC statistical audit of the Global Innovation Index 2024 | Evidence of method | At source; verified | "All published GII 2024 ranks lie within the simulated 90 percent confidence intervals"; 5,000 Monte Carlo simulations |
| County Health Rankings & Roadmaps, methods page | Practice | At source; verified | "Beginning in 2024, Health Groups are displayed"; ten unequal groups replace ranks |
| Arndt 2015, *Health Services Research* (PMC) | Evidence of method | At source; verified | "rankings can be too unreliable to be helpful"; "Rankings are driven, in part, by random noise" |
| GSS, Communicating quality, uncertainty and change (2018; under review) | Standard (official statistics) | At source; verified; one sentence read once | "Describe the direction of change, its absolute size and its relative size over time" |
| ONS, Small area GVA estimates 1998 to 2022 (21 Aug 2024) | Standard (official statistics) | At source; verified | "We advise a degree of caution when making comparisons between data at the most granular (building block) level" |
| **Culture and charity** | | | |
| Nordicity 2016, Evaluation of Participants' Experience of the Quality Metrics National Test Phase (6 Sep 2016) | Evidence of method | At source; verified; several figures read once | "interesting" rather than "useful"; 63 per cent agreed the framework was useful; 66 per cent response rate |
| Knell & Whitaker 2016 | Evidence of method | Cited only (Chapter 5) | Not quoted in the chapter body |
| Impact & Insight Toolkit: History; FAQs; Knell, A Decade of Solving the Evaluation Puzzle (4 Nov 2025) | Practice | At source; verified; history sentence read once | "it is not mandatory to sign up"; "Culture Counts is a data processor."; "over 800 organisations registered" |
| Arts Council England: Impact and Insight Toolkit page; Illuminate page and FAQ | Practice | At source; verified; purpose and FAQ sentences read once | "It is not owned by Arts Council England."; Illuminate mandatory for funded organisations, live 1 June 2023 |
| Arts Professional: 13 Sep 2023; 27 Aug 2024; 16 Dec 2025; 10 Mar 2026; 18 Sep 2026 | Practice | 13 Sep 2023 and 10 Mar 2026 read once; 27 Aug 2024 verified; 16 Dec 2025 verified, secondary for the Hodge review; 18 Sep 2026 verified in fragments, secondary for ACE's words | "The present reporting requirements are not fit for purpose." (Hodge review); survey requirement suspended "by an additional year" |
| Selwood 2019, *Cultural Trends* 28(2–3):177–197 (mirror) | Evidence of method | At source; verified | "NPOs are potentially compromised by their dual role as data providers and grant recipients" |
| Gilmore, Glow & Johanson 2017, *Cultural Trends* | Evidence of method | Abstract (†) | Named among academic critiques; no finding quoted |
| Phiddian et al. 2017 | Evidence of method | Not read | Named among academic critiques; nothing quoted |
| The Audience Agency, liquidation notice (11 Sep 2026); audiencespectrum.org; audienceanswers.org | Practice | Notice at source; verified; the two sites read once | "was placed into Liquidation on 10 September 2026"; notice names no successor for Audience Spectrum or Audience Finder |
| DCMS, Participation Survey 2024–25 annual technical report; Community and Engagement Survey guidance (updated 12 Aug 2026); 2025/26 methodology note; January–March 2026 technical report | Standard (official statistics) | At source; verified | "A vertical dotted line is included in charts to indicate the change in survey name and structure, although estimates can still be compared." |
| DCMS, Embedding a Culture and Heritage Capital Approach (17 Dec 2024) | Standard (official statistics) | At source; verified; two sentences read once | "One limitation that is important to be aware of is double counting between methods" |
| Inspiring Impact, Code of Good Impact Practice (2022 hosting) | Standard (method) | At source; verified; contribution sentence read once | "Be honest and open"; changes "may have occurred without your involvement" |
| NPC, Four pillar approach (4 Jun 2014) | Standard (method) | At source; verified | "Map your theory of change"; "Choose your level of evidence" |
| Social Value International, Principles | Standard (method) | At source; verified; one principle read once | "Only claim the value that activities are responsible for creating." |
| Impact Frontiers, Five dimensions of impact | Standard (method) | At source; verified; two read once | "Contribution tells us whether an enterprise's efforts resulted in outcomes that were likely better than what likely would have occurred otherwise." |
| Charities SORP 2026 via ICAEW summary | Standard (method) | Secondary | 2026 edition asks the smallest charities to "consider how their work made a difference" |
| NPC, Making an Impact (16 Oct 2012, summary page) | Evidence | At source; verified | "Only 5% of charities say that wanting to improve services is a primary motivation" |
| NPC, Money for Good UK (Mar 2013) | Evidence | At source; verified | "60% of donors say they care about impact, 10% look mainly for information on impact and ultimately just 2% use an informed assessment" |
| Charity Commission, Accounts Monitoring Review (2018) | Evidence | At source; verified | "52% of the trustees' annual reports demonstrated a clear understanding of the public benefit reporting requirement" |
| Hyndman & McConville 2016, *NVSQ* 45(4):844–865 (accepted manuscript) | Evidence | At source; verified | "the vast majority (94 per cent) of charities fail to report a single efficiency measure" |
| Karlan & Wood 2014, NBER WP 20047 | Evidence | Abstract (†) | Study of "how donors respond to new information about a charity's effectiveness"; no finding quoted |
| Charity Commission / BMG, Public trust in charities 2026 and 2025 | Evidence | At source; verified; series and question wording read once | One fixed 0–10 question in waves; mean 6.5; "Most of the money raised is spent directly on the causes the charity supports" 55 per cent |
| **The great public data projects** | | | |
| Our World in Data: organization; easier-to-reuse-our-data (21 Nov 2024); FAQs; funding; Global Change Data Lab Trustees' Annual Report 2022 (23 Sep 2023); ETL metadata reference; 2020 audience survey post | Practice | At source; verified; funding, processing-level rule and survey figures read once | "nearly 100 million page views this year"; `origin.date_published` fields; "1.6% of sessions have a CSV download" |
| NatCen for UKSA, Public Confidence in Official Statistics 2023 (14 May 2024) and 2021 (25 Apr 2022) | Evidence | At source; verified; 2023 87 per cent sentence and sample spot-checked; 2014 and 2018 figures read once | "87% of respondents who gave an opinion indicating that they tend to trust it (71%) or trust it a great deal (16%)"; government presents statistics honestly "(32%, compared to 35% in 2021)" |
| Human Mortality Database, Project overview and Methods Protocol v6 (5 Aug 2025) | Practice | At source; verified | "comparability, flexibility, accessibility, reproducibility"; "we have not attempted to correct the data for systematic age misstatement" |
| UK Data Service: About; DOI blog (2020); citation guidance | Practice | Read once | "Using the study's DOI will always bring the user back to this edition of this dataset" |
| COVID Tracking Project, It's Time (1 Feb 2021) | Practice | At source; verified; final-update sentence read once | "gap analyses noting where replacement data still doesn't exist"; five weeks' notice of the end |
| **House** | | | |
| BRIEF-v2 §6 and §7 | Nightlife Culture | House document; no status given | Chapter 15's definition and the fold note |
| Version 1, Chapter 12 (archived) | Nightlife Culture | House document; no status given | Nearest predecessor; its sector claims tested in section 11 |
| Chapters 2, 5, 6, 7, 8, 11, 12, 14 | Nightlife Culture | House documents; no status given | Earlier findings leaned on, as cited |


## 20 · Version 2 — Chapter 16: Breaking these rules well (6 October 2026)

*Legend as §5, §10 and §15–§19. "At source" — a research agent opened the link on 6 October and a second fetch confirmed the exact string; "spot-checked" — the orchestrator re-opened it (five pages: the FRC 2021 "Improving the quality of 'comply or explain' reporting"; the Claesen et al. 2021 abstract; Nygard 2011; Ancker et al. 2017; the Tetlock, Skitka & Boettger 1989 PubMed abstract — all holding); "verified" — the independent verification pass re-traced it against the agents' returns (42 items re-traced; nine wording or count corrections — two FRC sentences closed early; "create"/"creating" in the SIMS manual; "most"/"many" statements; the planning memorandum's attribution; the flag-line count; two internal tallies; the Revisit-at-end breakdown — and the Tetlock authorship confirmed through Crossref). "Read once" means a single fetch with no presence check; "two passes" means returned identically twice without a presence check; "abstract" means only the abstract was reachable, and a dagger (†) marks a figure or quotation taken from an abstract or a secondary account; "secondary" means read through another source; "not read" means unreachable and nothing quoted.*

| Source | Kind | How read | Used for |
|---|---|---|---|
| **The house and the book** | | | |
| Decision Book, `design-decisions/SKILL.md` L19–33, L37–56, L87, L215–225 | Nightlife Culture; Standard (design system) | Read directly | The tier test table ("Uncertainty — there is a right answer"; "Ambiguity — no single correct answer"); the override log's four lines; the gap register's four fields |
| Decision Book, `references/breaking-rules.md` L1–20, L22–51, L71, L77, L86–90 | Nightlife Culture; Standard (design system) | Read directly | "the taxonomy of deviation" promised in the subtitle; the three borrowed lines (L28–29); the override log's printings (L33, L89); "Deviation classified honestly: ignorant, lazy, expedient or earned" (L88) |
| Decision Book, `references/rule-register.md` L1–20, L71, L363 and the 26 BRK rows | Nightlife Culture; Standard (design system) | Read directly; 347 rows counted | The 347-row register (74.4 per cent Fixed); BRK-04 "Name what the break buys: attention, retention, comprehension, context, register or fit"; BRK-07 (L71); BRK-08 (L363); BRK-11 "State every value in the design system once; other mentions point to it" |
| Decision Book, `references/gap-register.md` L1–35, L131–144; `references/found-a-gap.md` L40–72 | Nightlife Culture; Standard (design system) | Read directly | The gap register's fields; "Attach an interim rule to every known gap" |
| Decision Book, `references/override-log-template.md` L1–15 | Nightlife Culture; Standard (design system) | Read directly | A five-column table under the words "Four lines per departure" |
| Decision Book, `references/checklists.md` L358–362 | Nightlife Culture; Standard (design system) | Read directly | "Override logged: trigger, rule and tier, alternative, evidence"; the deviation classes' checklist line (L360) |
| Decision Book, `references/layout-and-type.md` L52, L69; `references/choose-format.md` L88; `references/colour.md` L30 | Nightlife Culture; Standard (design system) | Read directly | House rules read by line for the register and the conflict log |
| Style Guide (v1.5), `nightlife-culture-design/references/voice.md` L77–100 | Nightlife Culture | Read directly | The evidence standard (voice.md L89), which stands; Chapter 14's two companions remain a candidate |
| **The three borrowed sentences** | | | |
| *Navigating Ambiguity*, Small, Schmutte & Stanford d.school (Ten Speed Press, 19 April 2022): Educators' Guide, https://images.penguinrandomhouse.com/promo_image/9781984857965_10268.pdf; publisher's page https://www.penguinrandomhouse.com/books/623448/ | Practice; Standard (method) | At source; verified, consecutive; publisher's page read once | "Uncertainty implies that there is something to be certain about. An absolute truth or fact exists. With ambiguity there's no singular, correct answer." |
| *Drawing on Courage*, Goel & Stanford d.school (Ten Speed Press, 19 April 2022): Educator Guide, https://dschool.sfo3.digitaloceanspaces.com/documents/Drawing-on-Courage-Educator-Guide.pdf; publisher's page https://www.penguinrandomhouse.com/books/623449/drawing-on-courage-by-ashish-goel-and-stanford-dschool/ | Practice; Standard (method) | At source; verified; publisher's page verified for the date | "fear enlists its good friends reason and comfort"; the house's 2021 is 2022 at publisher and copyright line |
| *This Is a Prototype*, Witthoft & Stanford d.school (Ten Speed Press, 4 October 2022): Educators' Guide, https://images.penguinrandomhouse.com/promo_image/9781984858047_10270.pdf; publisher's page https://www.penguinrandomhouse.com/books/623452/this-is-a-prototype-by-scott-witthoft-and-stanford-dschool/ | Practice; Standard (method) | At source; verified; publisher's page read once | "How do you close the gap between I wonder and I know?" — a question at source, not the house's instruction |
| **Tier vocabularies** | | | |
| RFC 2119, Bradner, March 1997 (BCP 14), https://www.rfc-editor.org/rfc/rfc2119.txt | Standard (method) | At source; verified | MUST, SHOULD, MAY; "Imperatives of the type defined in this memo must be used with care and sparingly." |
| RFC 8174, Leiba, May 2017, https://www.rfc-editor.org/rfc/rfc8174.txt | Standard (method) | At source; verified | The words carry their meanings "when, and only when, they appear in all capitals"; "a lot of normative text does not use them and is still normative" |
| ISO/IEC Directives Part 2, ninth edition (2021), https://www.iso.org/sites/directives/current/part2/index.xhtml | Standard (method) | At source; definitions verified; clause 7 read once | Requirement: "from which no deviation is permitted if conformance with the document is to be claimed"; recommendation; permission |
| WCAG 2.2, W3C Recommendation, 12 December 2024, https://www.w3.org/TR/WCAG22/: Conformance section | Standard (W3C) | Date verified; conformance section not read (unreachable; the reader never reached it) | Named for the check against the dated Recommendation; nothing quoted from it |
| WCAG 2.2 editors' source file, https://raw.githubusercontent.com/w3c/wcag/main/guidelines/index.html | Standard (W3C) | At source; verified (conformance sentences, in the source file and not the dated Recommendation) | "Conformance claims are not required."; "A 'statement of partial conformance' may be made that the page does not conform, but could conform if certain parts were removed." |
| W3C, Understanding Conformance, https://www.w3.org/WAI/WCAG22/Understanding/conformance | Standard (W3C) | At source; verified | "It is important to recognize that this is a statement of non-conformance" |
| National Highways, DMRB GG 101, version 0.1.0, 29 September 2021, https://www.standardsforhighways.co.uk/tses/attachments/25cefcd4-3464-4e41-8e4f-fffc155723ea | Standard (method) | At source; verbs verified; departure and justification clauses read once | "Requirements with this verb form cannot be varied."; departures approved "before the design is finalised"; "Justifications to support all design decisions shall be recorded" |
| MISRA Compliance:2020 (February 2020), https://misra.org.uk/app/uploads/2021/06/MISRA-Compliance-2020.pdf | Standard (method) | Two passes | Mandatory, required, advisory; "A violation which has been formally accepted and approved"; "Simply to satisfy the convenience of the developer" |
| Hale & Borys 2013, Working to rule, or working safely? *Safety Science* 55, Part 1 (https://research.tudelft.nl/en/publications/working-to-rule-or-working-safely-part-1-a-state-of-the-art-revie) and Part 2 (abstract on a third-party mirror, https://vnniosh.vn/?p=18481) | Evidence of method | Abstract (†); Part 2 secondary | Two models of a rule; the framework "places the monitoring and adaptation of rules central to its management process" |
| **Deviation regimes** | | | |
| FRC, UK Corporate Governance Code 2024 (January 2024), https://media.frc.org.uk/documents/UK_Corporate_Governance_Code_2024_a2hmQmY.pdf | Standard (regulator) | At source; verified in fragments; read once where marked | "The Code does not set out a rigid set of rules; instead, it offers flexibility through 'comply or explain' reporting against the Provisions."; explanations "should indicate when the company expects to conform" |
| FRC, "What constitutes an explanation under 'comply or explain'?", February 2012 (IoD-hosted copy, https://www.iod.com/app/uploads/2022/02/What-constitutes-an-explanation-under-Comply-or-Explain-2012-guidance-ea5e769fb43d52439ef542c7ab9a3d47.pdf); FRC news page, 15 February 2012, https://www.frc.org.uk/news-and-events/news/2012/02/frc-publishes-paper-on-its-comply-or-explain-approach-to-corporate-governance/ | Standard (regulator) | Paper two passes, fragments verified; news page verified | "it is up to them to decide whether to accept or reject explanations"; "a large majority of companies who do not comply with one or more provisions of the Code provide a full explanation of their reasons" |
| FRC, "Improving the quality of 'comply or explain' reporting", 26 February 2021, https://www.frc.org.uk/docs/1892/html/ | Standard (regulator); Evidence | At source; verified; elements read once; spot-checked | "Our sample identified 74 cases of non-compliance with the Code, but we found only four explanations that we considered high quality"; "tick-box compliance"; the four-part template |
| FRC, Annual Review of Corporate Governance Reporting, November 2025, https://media.frc.org.uk/documents/Annual_Review_of_Corporate_Governance_Reporting_2025.pdf | Standard (regulator); Evidence | At source; verified; chart values three passes | Companies disclosing any departure, 73 (2022) to 25 (2025); no proportion judged adequate (two passes) |
| Seidl, Sanderson & Roberts 2013, *Journal of Management & Governance* 17:791–826 (https://link.springer.com/article/10.1007/s10997-011-9209-y); CBR Working Paper 389 (2009), https://jbs.cam.ac.uk/cbrwp389 | Evidence | Published article: abstract (†); working paper: at source; verified | "almost 25% of UK deviations, and almost 50% of German deviations were not properly justified" (working paper); "some 715 records of deviation" (abstract) |
| Arcot, Bruno & Faure-Grimaud 2010, *International Review of Law and Economics* 30(2):193–201; discussion paper FMG DP581 (2005), https://www.fmg.ac.uk/sites/default/files/publications/DP581.pdf | Evidence | Journal: abstract; discussion paper: at source; verified; read once where marked | "Almost one in five instances of non-compliances (on average 17%) are not explained"; good explanations "roughly about 20%" |
| Shrives & Brennan 2015, *British Accounting Review* 47(1):85–99, https://nrl.northumbria.ac.uk/id/eprint/18021/ | Evidence | Abstract (†) | Read; not used in the body |
| MacNeil & Li 2006, *Corporate Governance: An International Review* 14(5):486–496 | Evidence | Abstract (†) | Read; not used in the body |
| Keay 2014, *Legal Studies* 34(2):279–304 | Evidence | Abstract (†) | "There is no provision in the UK for any statements by companies to be assessed by any regulatory body." |
| Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018, SI 2018/952, regs 7 and 8, https://www.legislation.gov.uk/uksi/2018/952/regulation/7 and https://www.legislation.gov.uk/uksi/2018/952/regulation/8 | Standard (law) | At source; verified (reg 7(2)–(4)); read once (reg 7(1), reg 8) | "A public sector body must perform an assessment of the extent to which compliance with the accessibility requirement imposes a disproportionate burden." |
| GDS accessibility pages: "Understanding accessibility requirements for public sector bodies" (updated 30 September 2024), https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps; sample accessibility statement (updated 30 September 2024), https://www.gov.uk/government/publications/sample-accessibility-statement/sample-accessibility-statement-for-a-fictional-public-sector-website; "Accessibility monitoring of public sector websites and mobile apps from 2022 to 2024" (17 December 2024), https://www.gov.uk/government/publications/accessibility-monitoring-of-public-sector-websites-and-mobile-apps-from-2022-to-2024/accessibility-monitoring-of-public-sector-websites-and-mobile-apps-from-2022-to-2024; monitoring guidance page | Standard (government guidance); Evidence | At source; verified; monitoring guidance page read once | "You cannot take things like lack of time or knowledge into account in your assessment"; "We will make another assessment when the supplier contract is up for renewal"; claims at closure 17, 37 and 57 per cent; "many accessibility statements are now out-of-date" |
| GOV.UK Service Manual, "How service assessments work" (updated 7 September 2026), https://www.gov.uk/service-manual/service-assessments/how-service-assessments-work, and "Check if you need a service assessment" (3 September 2024), https://www.gov.uk/service-manual/service-assessments/check-if-you-need-a-service-assessment; GDS blog, 23 October 2020 | Standard (government guidance) | At source; verified where quoted; read once where marked; blog read once | "You need to fix amber issues within a reasonable period of time, usually up to 3 months."; the live "tracking amber evidence" document |
| OSR guidance: "TQV Voluntary Application" (15 October 2025), https://osr.statisticsauthority.gov.uk/guidance/tqv-voluntary-application-showing-trustworthiness-quality-and-value-when-working-with-data-and-statistics/; "Exemptions to the specific practices of the Code of Practice for Statistics", https://osr.statisticsauthority.gov.uk/our-regulatory-work/assessment/exemptions-to-the-specific-practices-of-code-of-practice-for-statistics | Standard (regulator) | At source; verified; exemption tables read once | "we encourage it to publish a TQV statement"; "Exemptions are rare."; the temporary table's "Duration" column |
| OSR, Code of Practice for Statistics 3.0 (published 3 November 2025; PDF path /2026/08/), https://osr.statisticsauthority.gov.uk/wp-content/uploads/sites/3/2026/08/Code-of-Practice-for-Statistics-3.0.pdf and https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/5/ | Standard (official statistics) | At source; verified where quoted; practices 6.7, 2.5 and 2.10 read once | "Explain reasons for deviations from these standards and any related implications for use." (practice 6.7); "Be open about your decisions and reasons for change." |
| Financial Services and Markets Act 2000 ss.138A and 138B, https://www.legislation.gov.uk/ukpga/2000/8/section/138A and https://www.legislation.gov.uk/ukpga/2000/8/section/138B | Standard (law) | At source; verified (138A, 6 October 2026); read once (138B) | The two-limb test: "unduly burdensome or would not achieve the purpose for which the rules were made" |
| FCA waivers: "How to apply" (updated 27 March 2026), https://www.fca.org.uk/firms/waivers-modifications/apply; main waivers page (6 August 2026); Handbook SUP 8.3, https://www.handbook.fca.org.uk/handbook/SUP/8/3.html | Standard (regulator) | At source; verified | "Most waivers and modifications are granted for a set period and then cease to apply."; "A waiver or modification will not apply retrospectively." |
| ISO 9001:2015 page (withdrawn 16 September 2026), https://www.iso.org/standard/62085.html; ISO 9001:2026 page, https://www.iso.org/standard/9001 | Standard (method) | 2015 page: at source; verified; 2026 page: read once | Withdrawn and replaced by ISO 9001:2026, three weeks before the chapter |
| ISO 9001:2015 clause 10.2 (nonconformity and corrective action); two secondary renderings (a Philippine Department of Energy training module; an auditor-training blog) | Standard (method) | Secondary (withdrawn edition; the clause text itself not reached) | "retain documented information as evidence of: a) the nature of the nonconformities and any subsequent actions taken; b) the results of any corrective action." |
| ISO 9000:2015 definitions, read in the European Union Agency for Railways terminology collection, https://www.era.europa.eu/era-railway-terminology-collection/concession/term/sms_safety_culture_human_and_organisational_factor | Standard (method) | Secondary (the standard itself not open); concession verified; deviation permit read once | Concession ("Permission to use or release a product or service that does not conform to specified requirements"); deviation permit ("prior to its realization") |
| NHS England Digital, Quality and Outcomes Framework 2024-25 (28 August 2025), https://digital.nhs.uk/data-and-information/publications/statistical/quality-and-outcomes-framework-achievement-prevalence-and-exceptions-data/2024-25, and technical annex | Standard (regulator); Evidence | At source; verified | "As of 1 April 2019, exception reporting is being replaced with a Personalised Care Adjustment (PCA)."; adjustment rates 1.8 per cent (smoking) to 29.9 per cent (COPD) |
| Doran, Fullwood, Reeves, Gravelle & Roland 2008, *NEJM* 359:274–84 | Evidence | Not read (unreachable: nejm.org 403; PubMed 429) | Nothing quoted; reached only through Roland 2016 and Kontopantelis et al. 2016 |
| Doran, Kontopantelis, Fullwood, Lester, Valderas & Campbell 2012, *BMJ* 344:e2405, https://pmc.ncbi.nlm.nih.gov/articles/PMC3328418 | Evidence | At source; verified; the gaming sentence read once | "The median rate of exception reporting was 2.7% (interquartile range 1.9-3.9%) overall"; £0.58 per patient; "our findings raise the possibility of gaming" |
| Kontopantelis et al. 2016, *BMJ Quality & Safety* 25(9):657–670, https://pmc.ncbi.nlm.nih.gov/articles/PMC5013124 | Evidence | At source; verified | "Exempted patients had a higher adjusted risk of death in the following year than non-exempted patients" (hazard ratio 1.37; 1.20) |
| Roland 2016, Should doctors be able to exclude patients from pay-for-performance schemes? *BMJ Quality & Safety* 25(9):653, https://qualitysafety.bmj.com/content/25/9/653 | Evidence | At source; verified | "we still do not know whether the ability of doctors to exclude patients from the P4P scheme has been in the interests of patients or not"; median 5.3 to 4.5 per cent |
| HM Treasury, ministerial directions collection (23 February 2026), https://www.gov.uk/government/collections/ministerial-directions | Standard (government guidance) | At source; verified | "the accounting officer should ask for a formal written direction to proceed."; published by presumption since 2011 |
| Institute for Government, ministerial directions explainer (17 February 2026) | Practice | Two passes | The route to the auditor and the committee; 107 known since 1990 |
| Columbia Accident Investigation Board report, via globalsecurity.org | Practice | Secondary, verified on the secondary (the Board's report not read: NASA-hosted PDFs unreachable) | "36 percent of these waivers have not been reviewed in 10 years" |
| Space.com, 2005 | Practice | Tertiary; read once | The Board's recommendation that "an independent group rather than shuttle program managers be given sole authority to grant waivers" |
| **Records of decisions** | | | |
| Nygard, "Documenting Architecture Decisions", Cognitect blog, 15 November 2011, https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | Practice | At source; verified; spot-checked; "Blindly accept the decision." read once | "Large documents are never kept up to date."; "Nobody ever reads large documents, either."; the five-part form; immutability not in the post |
| adr.github.io, https://adr.github.io/ | Practice | At source; verified | The form's definitions (an architecture decision record; a decision log) |
| AWS Prescriptive Guidance, "Architectural decision record process", https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html | Practice | At source; verified | "When the team accepts an ADR, it becomes immutable." |
| Thoughtworks Technology Radar, "Lightweight Architecture Decision Records" (2016–18), https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records | Practice | At source; verified | "storing these details in source control, instead of a wiki or website, as then they can provide a record that remains in sync with the code itself" |
| Buchgeher, Schöberl, Geist, Dorninger, Haindl & Weinreich 2023, Using Architecture Decision Records in Open Source Projects, *IEEE Access* 11:63725–63740, https://research.jku.at/en/publications/using-architecture-decision-records-in-open-source-projects-an-ms/ | Evidence | Abstract (†) | Adoption "is still low"; "About 50% of all repositories with ADRs contain just one to five ADRs" |
| Santana Junior et al. 2026, Architecture Decision Records: Adoption, Impact, and Developer Engagement in Open-Source Software, ICSA 2026 (26 June 2026), https://conf.researchr.org/details/icsa-2026/icsa-2026-papers/34/Architecture-Decision-Records-Adoption-Impact-and-Developer-Engagement-in-Open-Sou | Evidence | Abstract (†) | 63 per cent of 5,800 records "opened directly with a status of "accepted" or equivalent" |
| Nogueira, Silva & Conte 2026, One Size Fits All? An Empirical Comparison of ADR Templates, EASE '26 (arXiv 2604.27333) | Evidence | At source; verified; scores read once | The short founding template beat the longer one, 0.8 against 0.7, with 33 students |
| Claesen, Gomes, Tuerlinckx & Vanpaemel 2021, Comparing dream to reality, *Royal Society Open Science* 8:211037, https://royalsocietypublishing.org/doi/10.1098/rsos.211037 | Evidence | At source; verified; spot-checked (abstract) | "Two out of 27 preregistered studies contained no deviations from the preregistration plan."; "One study (4%) reported all the deviations." |
| Willroth & Atherton 2024, Best Laid Plans: A Guide to Reporting Preregistration Deviations, *AMPPS* 7(1), https://journals.sagepub.com/doi/full/10.1177/25152459231213802 | Evidence of method | At source; verified; table headings two passes | The deviation definition; the table's columns; the editor survey (n = 34 of 170; M = 3.3, M = 1.3) |
| APS Observer, 7 February 2024, https://www.psychologicalscience.org/observer/methods-preregistration-deviations | Practice | At source; verified | Unsigned summary of the editor survey in Willroth & Atherton |
| Field, Wagenmakers, Kiers, Hoekstra, Ernst & van Ravenzwaaij 2020, The effect of preregistration on trust in empirical research findings, *Royal Society Open Science* 7:181351, https://pmc.ncbi.nlm.nih.gov/articles/PMC7211853 | Evidence | At source; verified | "we report ambiguous Bayes factors and conclude that we do not have strong evidence towards answering our research questions." |
| Lakens 2024, When and How to Deviate From a Preregistration, *Collabra: Psychology* 10(1):117094, https://online.ucpress.edu/collabra/article/10/1/117094/200749/When-and-How-to-Deviate-From-a-Preregistration | Evidence of method | At source; verified; one sentence read once in full | "One justifiable reason to deviate from a preregistered statistical analysis plan is to increase the validity of the scientific claim – even if doing so comes at the expense of the severity of the test." |
| Center for Open Science, preregistration page, https://www.cos.io/initiatives/prereg; OSF Support, "Advanced Actions on Registrations", https://help.osf.io/article/113-advanced-actions-registrations; DeHaven, COS blog, 23 May 2017, https://www.cos.io/blog/preregistration-plan-not-prison | Practice | At source; verified; read once where marked | "You will be prompted to enter a justification for the update."; "Start a Transparent Changes document now" |
| Keep a Changelog 1.1.0, https://keepachangelog.com/en/1.1.0/ | Practice | At source; verified | "Changelogs are for humans, not machines."; "A changelog which only mentions some of the changes can be as dangerous as not having a changelog." |
| Semantic Versioning 2.0.0, https://semver.org/ | Standard (community) | At source; verified | "Once a versioned package has been released, the contents of that version MUST NOT be modified." |
| Gebru, Morgenstern, Vecchione, Wortman Vaughan, Wallach, Daumé III & Crawford 2021, Datasheets for Datasets, arXiv 1803.09010v8 (https://arxiv.org/pdf/1803.09010v8) and *Communications of the ACM*, December 2021 (https://cacm.acm.org/research/datasheets-for-datasets/) | Standard (method) | At source; verified; sections and cost read once | "We emphasize that the process of creating a datasheet is not intended to be automated."; the maintenance questions |
| Mitchell et al. 2019, Model Cards for Model Reporting, FAT* '19, arXiv 1810.03993v2, https://arxiv.org/pdf/1810.03993v2 | Standard (method) | At source; verified; "short (one to two page)" read once | "the usefulness and accuracy of a model card relies on the integrity of the creator(s) of the card itself" |
| Liang et al. 2024, *Nature Machine Intelligence* 6:744–753 (arXiv 2402.05160) | Evidence | At source; verified | Training section filled in 74.3 per cent of 32,111 cards, Limitations 17.4 per cent |
| Yang, Liang & Zou 2024, Navigating Dataset Documentations in AI, ICLR 2024 (arXiv 2401.13822) | Evidence | Abstract (†) | Read; not used in the body |
| Holland, Hosny, Newman, Joseph & Chmielinski 2018, The Dataset Nutrition Label, arXiv 1805.03677, https://arxiv.org/abs/1805.03677 | Standard (method) | Abstract (†) | Read; not used in the body |
| The GDS Way, "Documenting architecture decisions" (reviewed 5 March 2026), https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html | Standard (government guidance) | At source; verified | "Architecture decisions should be stored in version control so there is a record of what was changed, who by, and when." |
| DSIT & GDS, "Architectural Decision Record Framework", 4 November 2025, https://www.gov.uk/government/publications/architectural-decision-record-framework/architectural-decision-record-framework | Standard (government guidance) | At source; verified; fields two passes | The fields: title, date, status, context, decision, consequences, stakeholders consulted, links |
| HM Treasury, The Green Book 2026 (5 February 2026), chapter 5, https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026 | Standard (government guidance) | At source; verified | "Practitioners must record the reason for each rating in a brief paragraph, explaining the underlying evidence, assumptions and sources." |
| NAO, "Investigation into government procurement during the COVID-19 pandemic", 26 November 2020, https://www.nao.org.uk/reports/government-procurement-during-the-covid-19-pandemic/ | Practice | At source; verified | "insufficient documentation on key decisions"; "it remains essential that decisions are properly documented" |
| Eurostat, Technical Manual of the Single Integrated Metadata Structure (SIMS) (2014), https://ec.europa.eu/eurostat/documents/64157/4373903/03-Single-Integrated-Metadata-Structure-and-its-Technical-Manual.pdf; Eurostat, "Reference metadata reporting standards", https://ec.europa.eu/eurostat/web/metadata/reference-metadata-reporting-standards | Standard (official statistics) | At source; SIMS manual: key clause verified, the rest read once; reporting-standards page verified | "each concept is only reported upon once"; two reports drawn for two readers (ESMS, ESQRS) |
| ONS Service Manual, Methodology (QMI), https://service-manual.ons.gov.uk/content/content-types/methodology | Standard (official statistics) | At source; verified | "All regular, established bulletins must have a quality and methodology information (QMI) report published alongside them." |
| Government Analysis Function, "Quality statistics in government" (2019; under review), https://analysisfunction.civilservice.gov.uk/policy-store/quality-statistics-in-government/ | Standard (official statistics) | At source; verified | The two-tier rule: caveats beside the figure, detail in Background Quality Reports |
| UK Data Service, study-level documentation, https://ukdataservice.ac.uk/learning-hub/research-data-management/document-your-data/study-level-documentation/ | Practice | At source; verified; read once where marked | Many records bound "into a bookmarked PDF/a user guide" |
| Cornell Data Services, Writing READMEs for Research Data, https://data.research.cornell.edu/data-management/sharing/readme/ | Practice | At source; verified | Read; not used in the body |
| Lethbridge, Singer & Forward 2003, How Software Engineers Use Documentation, *IEEE Software* (Nov/Dec), https://courses.cs.duke.edu//cps196.1/fall11/classwork/Lethbridge-Singer-Forward-2003.pdf | Evidence | At source (course copy); verified | "SEs were likely to update documentation continually only when it was attached to the process for completing a change request" |
| Harrison, Avgeriou & Zdun 2007, Using Patterns to Capture Architectural Decisions, *IEEE Software* (Jul/Aug), https://pure.rug.nl/ws/files/2815284/2007IEEESoftwHarrison.pdf | Evidence | At source; verified | "at that point, they've often forgotten many decisions and the rationale behind them" |
| Aghajani et al. 2020, Software Documentation: The Practitioners' Perspective, ICSE '20, https://www.inf.usi.ch/faculty/lanza/PUBS/P/Agha2020a.pdf | Evidence | Read once | Read; not used in the body |
| Norris & Sasse 2019, Moving on: The cost of high staff turnover in the civil service, Institute for Government (15 January 2019), https://www.instituteforgovernment.org.uk/publication/staff-turnover-civil-service | Evidence | At source; verified | "Several departments, including the Treasury and the Cabinet Office, lose a quarter of their staff each year" |
| Allan 2015, Review of Government Digital Records, Cabinet Office (17 December 2015), https://assets.publishing.service.gov.uk/media/5a756530e5274a1baf95e3cd/Report_-_Digital_Records_Review.pdf | Practice | At source; verified in fragments | "The processes have been burdensome and compliance poor."; "poorly organised and indexed" |
| Klein, Van de Sompel, Sanderson, Shankar, Balakireva, Zhou & Tobin 2014, Scholarly Context Not Found, *PLOS ONE* (26 December 2014), https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253 | Evidence | At source; verified | "one out of five STM articles suffering from reference rot" |
| New Zealand Controller and Auditor-General, "Making infrastructure investment decisions quickly", Part 6 (13 December 2023), https://ao.parliament.nz/2023/infrastructure-decisions/part6.htm; Northern Ireland Audit Office blog (13 February 2019), https://www.niauditoffice.gov.uk/blog-importance-good-record-keeping-audit-perspective-0 | Practice | Read | Read; not used in the body |
| Government Analysis Function, The AQuA Book (HTML edition 30 July 2025, updated 20 July 2026), https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government | Standard (government guidance) | At source; assumptions log verified; decisions log read once | "explain who made the decision and who signed it off" |
| **Overrides, checklists and written reasons** | | | |
| van der Sijs, Aarts, Vulto & Berg 2006, *JAMIA* 13(2):138–147, https://academic.oup.com/jamia/article/13/2/138/729061 | Evidence | Abstract (†) | "Drug safety alerts are overridden by clinicians in 49% to 96% of cases." |
| Ancker et al. 2017, *BMC Medical Informatics and Decision Making* 17:36, https://link.springer.com/article/10.1186/s12911-017-0430-8 | Evidence | At source; verified; spot-checked | "Likelihood of reminder acceptance dropped by 30% for each additional reminder received per encounter"; 112 clinicians; 1.27 million advisories |
| Nanji et al. 2014, *JAMIA* 21(3):487–491, https://academic.oup.com/jamia/article-abstract/21/3/487/872274 | Evidence | Abstract (†) | "An average of 53% of overrides were classified as appropriate", from 12% to 92% by rule |
| Poly, Islam, Yang & Li 2020, *JMIR Medical Informatics* 8(7):e15653, https://medinform.jmir.org/2020/7/e15653/ | Evidence | At source; verified | "The range of average override alerts was 46.2%-96.2%." |
| Felisberto et al. 2024, *Health Informatics Journal* 30(2), https://journals.sagepub.com/doi/10.1177/14604582241263242 | Evidence | At source; verified | "the overall prevalence of alert override by physicians was 90% (CI95% 85–95%)" |
| AHRQ PSNet, "Alert Fatigue" (15 December 2024), https://psnet.ahrq.gov/primer/alert-fatigue | Practice | At source; verified | Clinicians "ignore both the bothersome, clinically meaningless alarms and the critical alerts that warn of impending serious patient harm" |
| Haynes et al. 2009, *NEJM* 360(5):491–9, https://pubmed.ncbi.nlm.nih.gov/19144931/ | Evidence | Abstract (†) | "The rate of death was 1.5% before the checklist was introduced and declined to 0.8% afterward (P=0.003)." |
| Urbach, Govindarajan, Saskin, Wilton & Baxter 2014, *NEJM* 370(11):1029–38, abstract on the authors' institute's site, https://www.ices.on.ca/publications/journal-articles/introduction-of-surgical-safety-checklists-in-ontario-canada/ | Evidence | Abstract (†) | "not associated with significant reductions in operative mortality or complications"; 101 hospitals |
| Leape 2014, *NEJM* editorial, quoted by The Incidental Economist, 14 March 2014, https://theincidentaleconomist.com/wordpress/?p=54007 | Evidence | Secondary (quoted on a third party's page); the last sentence read once | "it is not the act of ticking off a checklist that reduces complications, but performance of the actions it calls for" |
| Russ et al. 2015, *Journal of the American College of Surgeons* 220, abstract on an Oxford page, https://www.psy.ox.ac.uk/publication/492123 | Evidence | Abstract (†) | "On average, two-thirds of the items were checked ... they failed to pause or focus on the checks in more than 70% of cases." |
| Bergs et al. 2014, *British Journal of Surgery* 101(3):150–158, https://documentserver.uhasselt.be/handle/1942/16492?mode=full | Evidence | Abstract (†) | "a strong correlation between a significant decrease in postoperative complications and adherence to aspects of care embedded in the checklist" |
| De Jager et al. 2016, systematic review of 25 studies, https://researchonline.jcu.edu.au/45374/1/45374%20De%20Jager%20et%20al%202016.pdf | Evidence | At source (PDF); verified; journal attribution unverified | "Postoperative mortality rates were not significantly decreased in any studies in developed nations" |
| Lerner & Tetlock 1999, *Psychological Bulletin* 125(2):255–275, https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:10087938&resultType=core&format=json | Evidence | Abstract (†); the body not read (unreachable) | "Under what conditions will accountability attenuate, have no effect on, or amplify cognitive biases?" |
| Tetlock, Skitka & Boettger 1989, *Journal of Personality and Social Psychology* 57(4):632–640, https://pubmed.ncbi.nlm.nih.gov/2795435/ | Evidence | Abstract (†); spot-checked (PubMed abstract); authorship confirmed through Crossref | "preemptive self-criticism"; "defensive bolstering"; "The experiment yielded results supportive of these 3 predictions." |
| Vieider 2008, Separating Real Incentives and Accountability, Tinbergen Institute DP 08-055, https://papers.tinbergen.nl/08055.pdf | Evidence | Secondary; verified | "Accountability in front of an audience with unknown views generally results in more cognitive effort." |
| Hoffmann, Gaissmaier & von Helversen 2017, *Judgment and Decision Making* 12(6):627–641, https://dlab.sauder.ubc.ca/sjdm/journal/17/17411/jdm17411.html | Evidence | At source; verified | "Process accountability neither changed how accurately people made a judgment, nor the judgment strategies." |
| Chang, Atanasov, Patil, Mellers & Tetlock 2017, *Judgment and Decision Making* 12(6), https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A16B2380B817354B0F39A392BFD1FD5C/S1930297500006732a.pdf/accountability-and-adaptive-performance-under-uncertainty-a-long-term-view.pdf | Evidence | Abstract (†) | "Process accountability promoted more effective knowledge sharing, improving accuracy among observers." |
| NAO, Evaluation of Regulatory Impact Assessments 2006-07 (HC 606, July 2007), https://www.nao.org.uk/reports/evaluation-of-regulatory-impact-assessments-2006-07/ | Practice | At source; verified | "A predetermined policy agenda can have a far greater influence on government action than the outcome or findings of the impact assessment." |
| NAO, Delivering High Quality Impact Assessments (HC 128, 30 January 2009), https://www.nao.org.uk/wp-content/uploads/2009/01/0809128es.pdf | Practice | At source; verified | "only 20 per cent presented the results of an evaluation of a range of options" |
| Explanatory Memorandum to SI 2013/1238 (Town and Country Planning (Development Management Procedure) (England) (Amendment) Order 2013), https://www.legislation.gov.uk/uksi/2013/1238/pdfs/uksiem_20131238_en.pdf | Standard (law) | At source; verified | A reason-giving duty repealed: "both burdensome and unnecessary because it duplicates material documented elsewhere" |
| Wright et al. 2019, *JAMIA* 26(10):934–942, https://academic.oup.com/jamia/article/26/10/934/5480565 | Evidence | At source; verified | "users often enter a space or random characters to move past the screen" |
| Haggerty 2004, Ethics Creep, *Qualitative Sociology* 27(4):391–414, https://link.springer.com/article/10.1023/B:QUAS.0000049239.15922.a3 | Evidence | Abstract (†) | "rupture the relationship between following the rules and acting ethically" |
| Degani & Wiener 1990, Human factors of flight-deck checklists, NASA CR 177549, https://ntrs.nasa.gov/api/citations/19910017830/downloads/19910017830.pdf | Evidence | At source; verified | "a long and detailed checklist is no guarantee of absolute safety" |
| Paterno et al. 2009, *JAMIA* 16(1):40–46, https://academic.oup.com/jamia/article/16/1/40/865495 | Evidence | Abstract (†); the hard-stop caveat read once | "Compliance with DDI alerts was significantly higher at the site with tiered DDI alerts compared to the non-tiered site (29% vs. 10%, p < 0.001)." |
| Shah et al. 2006, *JAMIA* 13(1):5–11, via the AHRQ summary page, https://digital.ahrq.gov/health-it-tools-and-resources/workflow-assessment-health-it-toolkit/research/shah-nr-et-al-2006 | Evidence | Secondary | Interrupting alerts accepted 67 per cent of the time; no control group |
| Powers, Shiffman, Melnick, Hickner & Sharifi 2018, *JAMIA* 25(11):1556–1566, abstract on a Weill Cornell record, https://vivo.weill.cornell.edu/display/pubid30239810 | Evidence | Abstract (†) | "Hard stops were superior to soft stops in 3 of 4 studies." |
| Australian Office of Parliamentary Counsel, "Sunsetting of legislative instruments" (22 October 2025), https://www.opc.gov.au/sites/default/files/2025-11/Sunsetting%20of%20legislative%20instruments.pdf | Standard (government guidance) | At source; fragments verified; full sentences read once | "Sunsetting ensures that legislative instruments are kept up-to-date and only remain in force for as long as they are needed." |
| Government Analysis Function, Using symbols and shorthand (January 2022) | Standard (official statistics) | Read once, via Chapter 15 | "We do not recommend using symbols such as '. :', '*' or '†' anymore"; "[p] = provisional" |
| **This book's own files** | | | |
| Chapters 0–15, version 2, by file line as the compilation cites them | Nightlife Culture | The compilation | The rules tables counted (486 rows; 433 carrying Fixed); the records, tests, flags, gaps and conflict logs assembled |
| The compilation, `02-research-notes/ch16-assembly.md` | Nightlife Culture | By script; every row re-checked against its source line (the gap and conflict rows of Chapters 14–15 not put through the verbatim re-check) | 486 rule rows, 129 record lines, 19 test paragraphs naming 55 tests, 66 flag lines, 207 gap rows, 57 conflict-log rows |
| Agent returns, `02-research-notes/ch16-agent-returns.md` | Nightlife Culture | Read directly | The four reports: the URLs, dates, kinds and verification marks above |
| Version 1, Chapter 14, `ch14-breaking-these-rules-well.md` (17 August 2026; archived) | Nightlife Culture | Read directly | "circa 150 Fixed-tier rules"; "only the record separates expedient from earned"; tested in section 10 |
| BRIEF-v2, `00-plan/BRIEF-v2.md` | Nightlife Culture | House document; no status given | "Tiers, deviation, the override log, the assembled removal tests, the gap register, the rule register for the build." |
