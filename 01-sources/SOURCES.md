# Sources ledger — dashboard-design

*The durable record of what the chapters cite, where each thing lives, and how far it was
verified. Updated at the end of every chapter sprint. Started 16 August 2026, covering
Chapters 1–4.*

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
