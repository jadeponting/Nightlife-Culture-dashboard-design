# Chapter 16 — the book's own machinery, assembled

*Compiled 6 October 2026 by Agent C from the sixteen version 2 chapter files in `/home/claude/ncvi-research/` (ch00 … ch15) and the house documents in the synced skills folder. No web research. No rule is reworded: every rule, record line, test, flag, gap row and conflict-log row is copied from its file by script, and file line numbers ("L") are given so each can be checked. `ch01-the-default-view.md` and the `*-agent-returns.md` files were not read.*

**How to read the IDs.** `7.12` = Chapter 7, row 12 of its `## The rules` table. `G-7.12` = Chapter 7, row 12 of its gaps table. "ch07 L554" = line 554 of the Chapter 7 file. Columns or notes marked **[added]** are mine; everything else in a table is as printed.

**What is mine and what is the book's.** Counts come from scripts run over the files. Four things are judgement and are labelled where they occur: the grouping of near-duplicate rules (1.3), the form given to each test (3.16), the group given to each gap row (5.3), and the list of what is still open (6.3). Part 8 is observation.

## Summary of counts

| Part | What was compiled | Count |
|---|---|---|
| 1 | Rule rows, Chapters 1–15 (Chapter 0 has no rules table) | **486** rows in 15 tables |
| 1 | Distinct Tier wordings | **53** |
| 1 | Rows with Fixed in the tier / Adaptable only / Decorative | **433** (405 Fixed only + 28 mixed Fixed-and-Adaptable) / **45** / **8** |
| 1 | Fixed rows by the sense the cell states | unmarked **212**; procedure **102**; stance **90**; sequence **2**; statement of the record **0**; other qualifier **31** (a cell can carry two) |
| 1 | Groups of duplicate or near-duplicate rules | **42** |
| 2 | Records beneath the dashboard (Chapters 4–15) | **12** documents, **129** lines (10, 9, 10, 10, 10, 12, 14, 12, 10, 12, 11, 9); 4 printed as lists, 8 as tables |
| 3 | `## What proves a break works` sections | **15** sections, 19 paragraphs, 3060 words; **55** separate tests named: reader test 27, removal 10, record check 7, recomputation 6, adversarial walk 4, none of the five 1 |
| 4 | Lines with `[Revisit → Ch 16]` | **6** (Chs 11 ×2, 12, 13, 14, 15) |
| 4 | Lines with `[Revisit at end]` | **60** (44 uses + 16 legend listings) |
| 4 | Lines with "Awaiting Carly" / "Carly's call" | **3** / **2** |
| 4 | Supplement: other lines naming this book's Chapter 16 / leaving something to Carly | 27 / 35 |
| 5 | Gap rows, Chapters 0–15 | **207** in 16 tables: (a) no study 23 + (a*) no official rule or source 25 = 48; (b) unreachable 32; (c) awaiting Carly 4; (d) house systems 38; (e) none of these 85 |
| 6 | Conflict-log rows | **57** (35 paragraphs in Chs 1–13 + 22 table rows in Chs 14–15); still open, de-duplicated: **37 items** (5 direct conflicts, 15 tensions, 12 candidates, 4 carried to Chapter 16, 1 more awaiting Carly) |
| 7 | House documents quoted | tier test (SKILL.md L37–56); Chapter 18 rules table (26 rows); override log (5 printings); deviation taxonomy (one checklist line); gap register (31 entries); rule register (347 rows, BRK-07 at L71); evidence standard (voice.md L89) |
| 8 | Observations | **10** |

**Where the files did not match the brief for this compilation** (detail in the part named):

1. Chapter 0 has no rules table (Part 1).
2. The Tier wordings asked about as "(procedure)" and "(stance)" are the form used only in Chapters 14–15; Chapters 3–13 write "as a procedure" and "as a stance" (Part 1.2).
3. "Beneath the dashboard" is the heading in five chapters only (8, 10, 13, 14, 15); the records of Chapters 4–7 are lists, not tables; Chapter 5 never uses the words "recipe card" (Part 2).
4. Conflict logs are prose in Chapters 1–13 and tables only in Chapters 14–15 (Part 6).
5. Gap tables in Chapters 14–15 have different columns from the other fourteen (Part 5).
6. `gap-register.md` does not print the four fields as a header; they are in `SKILL.md` and `found-a-gap.md` (Part 7.5).
7. The deviation taxonomy is named in a subtitle and printed only as one checklist line (Part 7.4).

**Contents.** Part 1 The rule register (1.1 register · 1.2 counts · 1.3 duplicates · 1.4–1.5 senses of Fixed) — Part 2 The records beneath the dashboard — Part 3 The assembled tests — Part 4 The flags to Chapter 16 and to the end — Part 5 The gaps — Part 6 The conflict logs — Part 7 The house's machinery as printed — Part 8 What I noticed.

---

## PART 1 — THE RULE REGISTER

**What has a rules table.** Chapters 1–15 each have one section headed `## The rules` holding exactly one table with the same five printed columns: `Rule | Why | Kind | Tier | Source`. Chapter 0 has **no** `## The rules` section and no rules table. What Chapter 0 has instead is a different form: the template table "How a chapter teaches" (ch00 L48–65, `Section | What it does`), the two legend tables "Kind — where the claim comes from" (L75–81, `Kind | Meaning | What you may do with it`, 5 rows) and "Tier — how firm it is" (L89–93, `Tier | Plain meaning | Breaking it is`, 3 rows), and the flags table (L107–115, `Flag | Means`, 7 rows). None of these is a register of rules with a why, kind, tier and source.

**The line printed under each `## The rules` heading** (verbatim; Chapters 12–15 print none — the table follows the heading directly):

- **Ch 1** (L300): *Kind and tier as in Chapter 0. † marks a source read at the authors' abstract only; the full text is on the verification list before this version closes (`[Further research]`).*
- **Ch 2** (L441): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only; the full text is on the verification list (`[Further research]`).*
- **Ch 3** (L429): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only (`[Further research]`).*
- **Ch 4** (L532): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only (`[Further research]`). "Secondary" marks a quotation that reached the chapter through a named reproduction.*
- **Ch 5** (L405): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only (`[Further research]`). "Secondary" marks a quotation that reached the chapter through a named reproduction. "Adjacent domain" marks evidence or standards from education, health, development economics, environmental management or machine learning rather than cultural display.*
- **Ch 6** (L487): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only (`[Further research]`). "Secondary" marks a quotation that reached the chapter through a named reproduction; "reconstructed" marks an abstract rebuilt from an index. "Adjacent domain" marks evidence or standards from environmental economics, ecology, epidemiology, clinical trials, industrial quality control, public-health surveillance, machine learning or official statistics rather than cultural display.*
- **Ch 7** (L435): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only (`[Further research]`). "Secondary" marks a quotation that reached the chapter through a named reproduction; "reconstructed" marks an abstract rebuilt from an index. "Adjacent domain" marks evidence or standards from public health, education, economics, central banking, climate science, intelligence analysis or official statistics rather than cultural display.*
- **Ch 8** (L599): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research; "Standard" includes protocol specifications, licences and published platform terms, which bind in the way a standard does. "Secondary" marks a quotation that reached the chapter through a named reproduction. "Adjacent domain" here means reliability engineering, web standards and performance research rather than cultural display. Every limit, price and term in this table is as read on 6 October 2026 and carries that date.*
- **Ch 9** (L541): *Kind and tier as in Chapter 0; Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only; "secondary" a quotation reached through a named reproduction; "reconstructed" an abstract rebuilt from an index record. "Adjacent domain" here means soundscape acoustics, environmental psychology, survey methodology, network science, computational social science and official statistics rather than cultural display.*
- **Ch 10** (L689): *Kind and tier as in Chapter 0; Standard (law) is the text of a statute or regulation as read on 6 October 2026; Standard (regulator) is guidance from the data-protection, online-safety or statistics regulators, non-statutory unless marked a code; Standard (method) is a methods handbook; Standard (international) an international instrument; "by analogy" marks a statute that binds public bodies and not the studio, used for its structure. Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only; "secondary" a quotation reached through a named reproduction. Nothing in this table is legal advice.*
- **Ch 11** (L459): *Kind and tier as in Chapter 0; Standard (design system) is a public design system's published guidance, backed by stated research only where it says so; Standard (W3C) is a WCAG 2.2 success criterion at the level named; Standard (community) a community-endorsed declaration or recommendation; Standard (method) a published grammar or method; Standard (regulator) and (law) as in Chapter 10. Practice marks a practitioner's framework not tested as research. † marks a source read at the authors' abstract only; "secondary" a quotation reached through a named reproduction. "Adjacent domain" here means news graphics, business dashboards, health risk communication, scholarly publishing and cartography rather than cultural display.*
- **Ch 12** (heading at L442): *(no line printed between the heading and the table)*
- **Ch 13** (heading at L405): *(no line printed between the heading and the table)*
- **Ch 14** (heading at L488): *(no line printed between the heading and the table)*
- **Ch 15** (heading at L490): *(no line printed between the heading and the table)*

### 1.1 The register — every row, as printed

Columns `Rule | Why | Kind | Tier | Source` are reproduced exactly as printed, cell for cell (extracted by script, not retyped). Added columns: **Ch** (chapter), **#** (row number within that chapter's table, used as the ID `Ch.#` everywhere below), **L** (line number in the chapter file) and, last, **Sense [added]** — my reading of which sense of Fixed the Tier cell's own wording indicates (see 1.5; blank for rows with no Fixed in the tier).

| Ch | # | L | Rule | Why | Kind | Tier | Source | Sense [added] |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 304 | Name the reader and the decision before any display is designed | A display for nobody serves nobody; the first feature of an actionable dashboard | Evidence | **Fixed** | Ivanković et al. 2021†; Jivet et al. 2018 | unmarked |
| 1 | 2 | 305 | State the dashboard's job — monitor, analyse or communicate — in writing, and design for it | The three jobs need different displays; most are used to communicate | Reading | **Fixed** | Few 2007; Eckerson 2011; Velcu-Laitinen & Yigitbasioglu 2012 | unmarked |
| 1 | 3 | 306 | Document provenance, method, positionality and uncertainty on the face of the display | A dashboard is a translator; its readers must be able to check it | Reading + Standard | **Fixed** | Kitchin et al. 2015; O'Neill 2002; Code of Practice | unmarked |
| 1 | 4 | 307 | Release the data with the display, through a documented route | A dashboard without a data release is a wall downstream | Evidence + Standard | **Fixed** | Dong et al. 2022; OSR 2021 | unmarked |
| 1 | 5 | 308 | Show uncertainty as a numeric range, never as a vague hedge or a hidden point | Numeric uncertainty costs almost no trust; verbal hedging does | Evidence | **Fixed** | van der Bles et al. 2020† | unmarked |
| 1 | 6 | 309 | Design and measure use from the first day | Non-use is the dominant failure mode and is almost never measured | Evidence | **Fixed** | Dowding et al. 2015; Rossi et al. 2025 | unmarked |
| 1 | 7 | 310 | Watch for the proxy moving without the goal; measure the goal where it can be measured | Dashboards move the countable before the intended | Evidence | **Fixed** | Jivet et al. 2018; Kaliisa et al. 2024†; Gerrish 2016† | unmarked |
| 1 | 8 | 311 | Treat every published measure as reactive; audit for gaming | A measure that becomes a target ceases to be a good measure | Evidence + Reading | **Fixed** | Strathern 1997; Campbell 1979; Goldstein & Spiegelhalter 1996 | unmarked |
| 1 | 9 | 312 | Show and justify the unit of aggregation; test sensitivity to it | The same numbers regrouped can give any answer | Evidence | **Fixed** | Openshaw 1984; Lee et al. 2025 | unmarked |
| 1 | 10 | 313 | Scale size-dependent measures by an appropriate denominator, and say which | Unscaled sums are won by the big | Standard | **Fixed** | OECD/JRC 2008 | unmarked |
| 1 | 11 | 314 | Rankings by rate are screening instruments, never verdicts; show intervals | Two-thirds of comparisons in a typical league table cannot be separated; small units sit at both ends | Evidence | **Fixed** | Goldstein & Spiegelhalter 1996; Wainer 2007; Gelman & Price 1999 | unmarked |
| 1 | 12 | 315 | Where official statistics suppress or perturb, show that fact, never a blank | Suppression removes exactly the small cells a local reader needs | Standard | **Fixed** | ONS; CDC | unmarked |
| 1 | 13 | 316 | Investigate an outlier as a mechanism before treating it as noise; use positive deviance as a method | A favourable outlier is the object of study, not the thing to trim | Reading | Adaptable | Hawkins 1980; Tukey 1977; Pascale & Sternin 2005 |  |
| 1 | 14 | 317 | Treat trust as earned by conduct — trustworthiness, quality, value — not sought from the display | Trust attaches to the producer and detaches from the presenter | Standard + Evidence | **Fixed** (adopted voluntarily) | Code of Practice; Public Confidence in Official Statistics 2023 | other qualifier |
| 1 | 15 | 318 | Build the common ground before the screen; test recognition with each community | A boundary object is a social achievement, not a design feature | Reading | Adaptable in method; Fixed as sequence | Star & Griesemer 1989; Turnhout 2009† | Adaptable part + sequence |
| 1 | 16 | 319 | Where the measure is of a place, think multilevel: the place is information, not only an average | Both the ecological and the atomistic fallacy are real | Evidence | **Fixed** | Robinson 1950; Subramanian et al. 2009† | unmarked |
| 1 | 17 | 320 | Never print an unsourced adoption or failure percentage for dashboards | None exists that is independent | Reading | **Fixed** | This chapter's search | unmarked |
| 1 | 18 | 321 | The job, the layering, the degree of framing, the order of failures to prevent, the amount of mud | Open choices with named trade-offs | — | Adaptable | Section 10 |  |
| 1 | 19 | 322 | Register, imagery, metaphor | Free, within the design system | — | *Decorative* | — |  |
| 2 | 1 | 445 | Name each reader, the decision they make, the evidence they are obliged to accept and the clock they keep, before design; declare whose grammar the first screen speaks | Readers grade by contradictory rules; the first screen is always in somebody's grammar; a display built for a reader in general is graded by none | Reading | **Fixed** | Section 1; Oliver 2014; Kelly 2017; Parkhurst 2017 | unmarked |
| 2 | 2 | 446 | Label every panel as monitoring or as evaluation; never imply a counterfactual the display does not have | The official reader's grammar makes the distinction and discounts the breach | Standard | **Fixed** | Magenta Book 2026 | unmarked |
| 2 | 3 | 447 | State where a claim stands on the evidence ladder when it will be read by a funder or a What Works body | A before-and-after is Maryland Level 1; data showing change is Nesta Level 2; the reader will score it so | Standard | **Fixed** | WWC Growth SMS; Nesta 2013 | unmarked |
| 2 | 4 | 448 | Follow the Treasury's order — monetise, quantify, describe — and label which is which; never present a benefit-cost ratio as the decision | The order is mandatory guidance; the ratio is not the decision | Standard | **Fixed** | Green Book 2026; Green Book Review 2025 | unmarked |
| 2 | 5 | 449 | Any wellbeing value carries its design grade and its range (£10,000–£16,000 per WELLBY) | The Treasury grades wellbeing evidence by causal design | Standard | **Fixed** | Wellbeing Guidance 2021 | unmarked |
| 2 | 6 | 450 | Show "who benefits" — distribution across groups and places — as a panel, not a footnote | Distributional analysis is now a required question | Standard | **Fixed** | Green Book 2026 ch. 7 | unmarked |
| 2 | 7 | 451 | Show the reader's own geography — the ward, the patch — at the scale they plan at | Local beats rigorous; the member's evidence is their ward | Evidence | **Fixed** | Kneale 2017; Kelly 2017 | unmarked |
| 2 | 8 | 452 | Make the source checkable before making the chart persuasive | Readers triage by source credibility first and do not sort by method | Evidence | **Fixed** | Kenny et al. 2017; IfG 2020 | unmarked |
| 2 | 9 | 453 | Design release to the reader's calendar; keep the problem documented between windows | Timing is the most prominent barrier and a strategy, not a circumstance | Evidence + Reading | Adaptable | Oliver 2014; Cairney & Kwiatkowski 2017; Kingdon via Mintrom & True |  |
| 2 | 10 | 454 | Offer a plain-table view as a first-class route for the reader already opposed | In one study, tables out-persuaded charts among the hostile in all three topics; the authors call the result uncertain | Evidence | Adaptable (a hypothesis to test) | Pandey et al. 2014 |  |
| 2 | 11 | 455 | Never add a chart for its air of science; add it for the information it carries | The trivial-graph effect did not replicate; and the design system's own rule that strong design must never make weak evidence look stronger | Evidence† + Nightlife Culture | **Fixed** (adopted) | Dragicevic & Jansen 2018†; Style Guide v1.5 | other qualifier |
| 2 | 12 | 456 | Name the denominator on every map and comparison, and show the alternative | Count versus rate moved perception by nine points; the fraction of a group is the persuasive unit | Evidence | **Fixed** | Engel et al. 2022; Jenni & Loewenstein 1997 | unmarked |
| 2 | 13 | 457 | Treat a league table as acting on the ranked; never present one as a reader's decision aid without intervals | Public performance data barely moves consumer choice and reorganises the ranked | Evidence | **Fixed** | Cochrane 2018; Marshall et al. 2000†; Espeland & Sauder 2007; Ch 1 | unmarked |
| 2 | 14 | 458 | Show uncertainty as a numeric range; never as a verbal hedge; never omit it to protect the signal | Numeric ranges cost almost nothing at n = 10,519; omission is an editorial choice | Evidence | **Fixed** | Kerr et al. 2023; Hullman 2020 | unmarked |
| 2 | 15 | 459 | Never let a place indicator be read as evidence of an intervention; mark descriptions as descriptions | Fuzzy concept, proxy data, rewards the already-successful | Reading | **Fixed** | Markusen 2013; ArtPlace 2014 | unmarked |
| 2 | 16 | 460 | Define the construct before choosing the proxy | Or the proxy defines it | Reading | **Fixed** | Jackson et al. 2006 | unmarked |
| 2 | 17 | 461 | Carry every valuation's caveats on the face of the display | The next release will drop them; this is the last place they survive | Reading | **Fixed** | Fields in Trust 2018; Sport England 2020/2025 | unmarked |
| 2 | 18 | 462 | Decide openly whose reading a property-value or footfall figure serves, and show the choice | Success to the investor; displacement to the resident | Reading | **Fixed** (show the decision) | Markusen 2013; WWC Growth 2014 | other qualifier |
| 2 | 19 | 463 | Claim outputs and outcomes for organisations; claim impact only at the level that can see the system | Impact belongs to funders, coalitions and places | Reading | Adaptable | Ebrahim & Rangan 2014 |  |
| 2 | 20 | 464 | Release numbers with their data and caveats so an opposing coalition's analyst can check them | Cross-coalition learning needs shared, checkable figures | Reading + Standard | **Fixed** | Sabatier via Cairney; Code of Practice (Ch 1) | unmarked |
| 2 | 21 | 465 | Agree data standards and the route to decision with the scene before collecting | Community data earns standing when both are co-agreed first | Evidence | **Fixed** | Mahajan et al. 2022 | unmarked |
| 2 | 22 | 466 | Do not place lived experience in a panel beside the numbers as a supplement | That is the re-filing three Scottish cases describe | Evidence (three cases) + Reading | Adaptable in form; Fixed as a prohibition on the supplement pattern | Hill O'Connor & Bennett 2026 | Adaptable part + other qualifier |
| 2 | 23 | 467 | Recognition is checked before release, as a dialogue that can change the next release | Member checking is a credibility test only when it can alter the account | Reading | **Fixed** as sequence | Lincoln & Guba (secondary); Birt et al. 2016† | sequence |
| 2 | 24 | 468 | Numbers for understanding, not numbers for advocacy: produce with caveats, release with data | A sector's dashboard is read by the people advocacy numbers are used against | Nightlife Culture | **Fixed** (adopted) | Section 8; UKSA 2017 | other qualifier |
| 2 | 25 | 469 | Which reader comes first (declared); monetise/quantify/describe; the plain-table view; where lived experience sits; which numbers the investor sees; documenting between windows | Open choices with named trade-offs | — | Adaptable | Section 11 |  |
| 2 | 26 | 470 | Register, imagery, metaphor | Free, within the design system | — | *Decorative* | — |  |
| 3 | 1 | 433 | Name the comparison the reader is to make before choosing a form; design the display to make that comparison first | Statistics are fast, comparisons slow and serial; design works by choosing the comparison | Evidence | **Fixed** | Franconeri et al. 2021; Ajani et al. 2022 (n = 24) | unmarked |
| 3 | 2 | 434 | For a precise ratio comparison, use position on a common scale, then length; do not ask for a precise reading from area or colour | Replicated top of the hierarchy | Evidence | **Fixed** for precise comparison; Adaptable as a general form rule | Cleveland & McGill 1984; Heer & Bostock 2010 | other qualifier + Adaptable part |
| 3 | 3 | 435 | Never let colour be the only means of distinguishing or conveying anything | Level A success criterion; 8% of men | Standard | **Fixed** | WCAG 2.2 SC 1.4.1; Birch 2012† | unmarked |
| 3 | 4 | 436 | Text at 4.5:1; parts of graphics needed to understand the content at 3:1 against adjacent colours | Level AA | Standard | **Fixed** | WCAG 2.2 SC 1.4.3, 1.4.11 | unmarked |
| 3 | 5 | 437 | Lightness for order, hue for category; no rainbow for ordered data on a pattern map | Lightness is read as order; the rainbow bins and exaggerates | Evidence | **Fixed** (pattern maps); Adaptable where the task is reading a value | Liu & Heer 2018; Franconeri 2021; Reda et al. 2018 | other qualifier + Adaptable part |
| 3 | 6 | 438 | Limit categorical colours — seven is the experimental ceiling for search, four or five the house limit; give small marks bigger colour steps | Search degrades beyond seven; small marks need bigger differences than large ones | Evidence + Standard (voluntary) | Adaptable within the ceiling | Healey 1996; Szafir 2018; Analysis Function; ONS |  |
| 3 | 7 | 439 | Put the message in the title, in words; put statistics and context beside the marks; never title-only, never no-text | Title first, longest, remembered, decisive; readers prefer the most-annotated chart; placement follows meaning | Evidence | **Fixed** | Borkin et al. 2016; Kong et al. 2018; Stokes et al. 2023 | unmarked |
| 3 | 8 | 440 | Title and chart point at the same salient thing | A caption cannot redirect to a faint feature; a contradicting title is believed and unnoticed | Evidence | **Fixed** | Kim, Setlur & Agrawala 2021; Kong et al. 2019 | unmarked |
| 3 | 9 | 441 | Label at the mark; legends only where labels cannot fit, and then ordered to match the data | Working-memory round trip; spatial contiguity d = 0.72; the compliance route for 1.4.1 | Practice + analogous Evidence + Standard | **Fixed** (evidential status stated) | Huestegge & Philipp 2011; Ginns 2006; WCAG 1.4.1 | other qualifier |
| 3 | 10 | 442 | Build first screens from fast-glance forms; avoid radial bars for comparison | Six-fold glance penalty for the decorative form — from 36 people on a smartwatch | Evidence (small; adjacent device) | Adaptable (strong default) | Blascheck et al. 2019 |  |
| 3 | 11 | 443 | Design the first glance for simplicity and for looking like what the display claims to be | Appeal forms in 50 ms on complexity and prototypicality — websites, small student samples | Evidence (adjacent domain) | Adaptable (what it claims to be is Carly's) | Lindgaard et al. 2006; Tuch et al. 2012 |  |
| 3 | 12 | 444 | Pictograms that are the data are permitted; nothing decorative behind the data; no styled bars (rounded, capped, triangular) | Free or helpful; distracting; inaccurate, respectively | Evidence | **Fixed** | Haroz et al. 2015; Skau et al. 2015 | unmarked |
| 3 | 13 | 445 | Declutter for professionalism; add a headline, one highlight and one sentence for recall | 2.5–3× recall of the intended conclusion in one study of 24; consistent with the title and text evidence; trust unmoved by either | Evidence (small, unreplicated) + the title evidence | Adaptable (strong default); the headline itself is Fixed under the words rule | Ajani et al. 2022; Borkin et al. 2016; Stokes et al. 2023 | Adaptable part + other qualifier |
| 3 | 14 | 446 | Bar axes start at zero; a broken line axis is declared and the effect size it implies is chosen deliberately | Truncation exaggerates even when labelled and taught | Evidence | **Fixed** | Correll et al. 2020; Yang et al. 2021†; Long & Kay 2024 | unmarked |
| 3 | 15 | 447 | Do not compare non-baseline segments of a stacked bar; use grouped or dot charts | Length judgement plus part-of-whole bias | Evidence | **Fixed** | Cleveland & McGill; Talbot et al. 2014 | unmarked |
| 3 | 16 | 448 | Public defaults: linear scale, daily flow with the cumulative available, absolute risk with a fixed denominator and a stated interval | Log halved correct reading of one question; cumulative raises perceived risk; relative risk persuades without informing; 1-in-X alarms (health domain) | Evidence (part adjacent domain) | **Fixed** as defaults | Romano et al. 2020†; Reinholtz et al. 2021; Akl et al. 2011; Pighin et al. 2011† | other qualifier |
| 3 | 17 | 449 | Show a value the reader wants to know as a number or a table, not a chart; show a trend or comparison as a chart | Cognitive fit | Evidence† + Reading | Adaptable | Vessey & Galletta 1991†; Cleveland & McGill |  |
| 3 | 18 | 450 | Two or three significant figures; never more precision than the data has; frequencies ("9 in 100") where chance is involved | Readers round anyway; precision reads as confidence; frequencies are reasoned about better | Practice + Evidence | **Fixed** (ceiling); Adaptable (digits) | Ehrenberg 1977; Cole 2015; Gigerenzer & Hoffrage 1995; McDowell & Jacobs 2017 | other qualifier + Adaptable part |
| 3 | 19 | 451 | Nothing crucial behind a click, a hover or a tooltip; everything crucial reachable by keyboard and on a phone | Median use of optional controls is zero (interactive articles, not dashboards); hover does not exist on touch; SC 2.1.1 | Evidence (adjacent domain) + Standard | **Fixed** | Conlen et al. 2019; Tse 2016; WCAG 2.1.1 | unmarked |
| 3 | 20 | 452 | Every default — place, measure, period, sort, extent — is chosen, written down and shown as a choice | Defaults shift choices (d = 0.68, policy and consumer domains), partly by being read as advice; the opening view anchors the session | Evidence (adjacent domain + visualisation) | **Fixed** as a stance | Jachimowicz et al. 2019; Cho et al. 2017; Hullman & Diakopoulos 2011 | stance |
| 3 | 21 | 453 | Treat "overview first" as a satisfaction preference; let the reader's arriving question decide | 52 citations, no validations; 2 of 17 comparisons more accurate | Evidence | Adaptable | Craft & Cairns 2005; Hornbæk & Hertzum 2011 |  |
| 3 | 22 | 454 | Small multiples for analysis; animation only for transitions between states of the same chart, or for presentation with the static version available | Animation enjoyed, slower, less accurate; transitions preserve identity | Evidence | **Fixed** | Robertson et al. 2008; Heer & Robertson 2007; Brehmer et al. 2019 | unmarked |
| 3 | 23 | 455 | Never a bare interval or a hard boundary for uncertainty; prefer countable dots, gradients, violins or animated draws; show outcome spread, not only estimate uncertainty, where individuals are the subject | Within-the-bar bias; containment; CI overstates individual effect (a treatment-effect game, n > 3,500) | Evidence (part adjacent domain) | **Fixed** | Correll & Gleicher 2014; Padilla et al. 2017; Hofman et al. 2020; Kay et al. 2016 | unmarked |
| 3 | 24 | 456 | A word for probability carries its number in brackets beside it | 32% → 66% agreement; a glossary does not help | Evidence | **Fixed** | Wintle et al. 2019; Budescu et al. 2014 | unmarked |
| 3 | 25 | 457 | Test uncertainty displays with sceptical readers before release | One study: uncertainty may amplify discounting among the strongly opposed | Evidence (one study) | Adaptable | Markant et al. 2023 |  |
| 3 | 26 | 458 | Plan for a reader at PIAAC Level 1 and with low graph literacy; test with them | A fifth of adults in England; a third with both deficits in Germany and the US | Evidence | **Fixed** as the planning assumption | PIAAC 2023; Galesic & Garcia-Retamero 2011† | other qualifier |
| 3 | 27 | 459 | Meet WCAG 2.2 AA as the yardstick of reasonable adjustment; two-part text alternatives for every chart; `role="img"` or `graphics-document` on every SVG chart | Equality Act anticipatory duty; WAI complex-images guidance; no chart role exists | Standard + guidance | **Fixed** | Equality Act 2010 s.20; WCAG 2.2; WAI tutorials; WAI-ARIA 1.2 | unmarked |
| 3 | 28 | 460 | Which chart below the top of the hierarchy; how many colours; how much text; convention or novelty at first glance; which uncertainty form; line-axis breaks; overview or search; animation or multiples; rounding | Open choices with named trade-offs | — | Adaptable | Section 14 |  |
| 3 | 29 | 461 | Register, imagery, metaphor, texture around the chart | Free, within the design system and provided nothing that carries meaning lives only there | — | *Decorative* | Decision Book Ch 7 |  |
| 4 | 1 | 536 | State the unit of observation (what one row is) and the count of rows beneath every figure | The grain is a choice that changes the count; three units (reporting, observation, statistical) are routinely conflated; the row count is our reading of what the figure needs to bear weight | Standard + Reading | **Fixed** (unit); **Fixed** as a stance (count) | Wickham 2014; Eurostat glossary; Regulation 696/93; section 3 | other qualifier + stance |
| 4 | 2 | 537 | State the reference period as a closed interval, separately from the date issued and the date last modified | A number has three dates; the stamp usually gives the least useful | Standard | **Fixed** | Eurostat; DCAT 3; ALFRED | unmarked |
| 4 | 3 | 538 | Write down the rule by which an activity that crosses a boundary (midnight; month end; clock change) is assigned to a period; never change it without a [b] | The boundary is a measurement rule and decides how much is counted | Standard + Evidence (adjacent domain) | **Fixed** as a stance; the rule itself Adaptable | KH03; Pierce et al. 2024 (secondary); Eurostat calendar adjustment | stance + Adaptable part |
| 4 | 4 | 539 | ISO 8601 with UTC offset in data; natural dates in display | Sorts correctly as text; removes ambiguity; a day across a clock change is not 24 hours | Standard | **Fixed** | GOV.UK open standard | unmarked |
| 4 | 5 | 540 | Name the denominator of every rate and make the alternatives reachable; use time-in-observation (person-time, venue-nights) where units are observed for unequal spans | A rate exists to compare unequal populations; the reference class is a choice | Standard (epidemiological) + Reading | **Fixed** | CDC Principles of Epidemiology; Hájek 2007† | unmarked |
| 4 | 6 | 541 | Rates on small bases carry intervals and are shown in a funnel, never ranked raw or ranked adjusted | Small units fill both tails; shrinkage flips the artefact | Evidence | **Fixed** | Gelman & Price 1999; Spiegelhalter 2005†; PHE Fingertips | unmarked |
| 4 | 7 | 542 | Ship the provenance set with every figure: responsible party; source and why; method and deviations; period; issued and modified; status; quality with error; what was withheld; what it may be compared with | The regulator's list, the European dimensions and three machine standards converge on it | Standard | **Fixed** | Code of Practice 3.0 Std 6, 7, 3.9, 3.10, 4.5, 9.3, 9.5, 10.5; Reg. 223/2009; PROV-DM; DCAT 3; FAIR R1.2 | unmarked |
| 4 | 8 | 543 | Keep the record when the number changes: a figure's description and its previous values outlive its current value | Metadata "accessible, even when the data are no longer available"; revisions are normal and should be visible in one place | Standard | **Fixed** | FAIR A2; OSR 2023 on GDP revisions | unmarked |
| 4 | 9 | 544 | Use "reliable" in the official sense (closeness of early to later estimates) or not at all; show provisional figures as [p] and revised as [r] | The ordinary and official senses diverge | Standard | **Fixed** | GSS quality dimensions; Analysis Function | unmarked |
| 4 | 10 | 545 | Name who owns the display's figures and who assured them; assure in proportion to the weight of the decision | Four roles; a single responsible owner; fit for *this* purpose | Standard (government guidance) | **Fixed** (adopted) | AQuA Book 2025; Macpherson 2013 | other qualifier |
| 4 | 11 | 546 | Zero only for a true zero; never for missing, rounded-to-zero or not-applicable | The data-standard, the statistical standard and the relational model agree | Standard | **Fixed** | Analysis Function; Eurostat "0n"; SDMX N; Codd 1986 | unmarked |
| 4 | 12 | 547 | Every empty cell states its kind; a blank is permitted only where there is exactly one reason for blanks and it is stated above the table | More than one kind of nothing forces a label on every nothing | Standard | **Fixed** | Analysis Function "Releasing statistics in spreadsheets" | unmarked |
| 4 | 13 | 548 | Never "NA", "N/A" or a bare symbol as the label for a nothing; letters in square brackets, or words | Ambiguous between not applicable and not available; symbols defeat screen readers | Standard | **Fixed** | Analysis Function; Eurostat | unmarked |
| 4 | 14 | 549 | Distinguish *not applicable* (the value cannot exist) from *not asked* (it could, and nobody did) | Every official scheme makes the split; the studio's six do not | Standard + Reading | Adaptable (how to name it) — flagged for Carly | SDMX M/L; [z]/[x]; Codd I/A-mark; Understanding Society −8 |  |
| 4 | 15 | 550 | Treat "free" as a value — zero price with a quantity — and never as a nothing; make the quantity visible where the price is zero | The national statistician's price-index method; no scheme codes it as missing | Standard (adjacent domain — price indices) + Nightlife Culture | **Fixed** | ONS special-case aggregates | unmarked |
| 4 | 16 | 551 | Never join a line across a missing point, dotted or dashed; highlight the gap and say why | "Joining points implies we know something about the data" | Standard | **Fixed** | Analysis Function "Data visualisation: charts" | unmarked |
| 4 | 17 | 552 | Flag every imputed or estimated value as such, with the method and who estimated; show imputation rates | Filled values carry uncertainty measured values do not | Standard | **Fixed** | NCES 4-1-7; SDMX E/I; Analysis Function 2018 | unmarked |
| 4 | 18 | 553 | A suppressed cell is marked, never blanked; secondary suppression applied; the display states whether its protection is suppression or perturbation | A blank is six things; a perturbed table is quietly [e] | Standard | **Fixed** | Analysis Function SDC; Code 4.5; ONS Census 2021 | unmarked |
| 4 | 19 | 554 | Where the mechanism of missingness may be correlated with the measure, show what would change if the nothing were something | MAR cannot be verified from data; sensitivity analysis is the remedy | Evidence (adjacent domain) | **Fixed** as a procedure | Sterne et al. 2009; NRC 2010 | procedure |
| 4 | 20 | 555 | Every comparison carries the ten-line declaration (definition; period; geography and vintage; method; disclosure; breaks; revisions; comparator and method; precision; outlier handling) | Valid "to the extent that differences … can be attributed to differences between the true values" | Standard | **Fixed** | SIMS/SDMX glossary; Reg. 223/2009; European Code P14; Code 3.0; ESMA 2015 | unmarked |
| 4 | 21 | 556 | Mark a change of definition or method with [b]; provide a back series or correction factors where possible | Before and after "cannot be directly compared" | Standard | **Fixed** | Analysis Function; Code 7.5; Eurostat LFS | unmarked |
| 4 | 22 | 557 | Use area codes with their vintage; declare the lookup for any best-fit aggregation; never compare across a boundary change without it | Codes change only with boundaries and are never re-used; best-fit carries stated error | Standard | **Fixed** | GSS geography policy; ONS CHD | unmarked |
| 4 | 23 | 558 | A like-for-like or defined measure is defined, reconciled to an audited total, shown with comparators, held constant, and restated if redefined | The finance rule, resembling the statistical one | Standard (adjacent domain — financial reporting) | **Fixed** (adopted) | ESMA 2015 ¶20, 26, 37, 41 | other qualifier |
| 4 | 24 | 559 | Name the comparator group and publish its variables, standardisation, distance and count; the comparator model must not contain the outcome | "The outcome ultimately relies on the indicators and mathematical procedures used"; IMD contains employment at 22.5% | Practice + Standard | **Fixed** | PHE Comparators Briefing; DfE 2025; CIPFA | unmarked |
| 4 | 25 | 560 | Beside any sum or mean of a skewed quantity, show the median and a concentration measure (top-share, Lorenz curve, Gini or HHI) | A total is a weighted statement about its largest terms | Evidence | **Fixed** (that one is shown); Adaptable (which) | Lorenz 1905; NIST; ONS ASHE; World Bank; DoJ | other qualifier + Adaptable part |
| 4 | 26 | 561 | Do not assume 80/20; measure the bow | Misnamed by its populariser; the shape varies and is more extreme in cultural markets | Evidence + Practice | **Fixed** | Juran 1975 (secondary); Elberse 2008 (secondary); Rosen 1981 | unmarked |
| 4 | 27 | 562 | Where a display ranks by popularity, say so and show the distribution: visible popularity increases concentration and unpredictability | Experimental; n = 14,341 | Evidence | **Fixed** as disclosure | Salganik, Dodds & Watts 2006 | other qualifier |
| 4 | 28 | 563 | Report platform and transactional feeds as within-sample comparisons unless the selection has been measured against a benchmark; state coverage | Quality × quantity × difficulty; 2.3 million ≈ 400 at ρ ≈ −0.005 | Evidence | **Fixed** as a stance | Meng 2018; Salganik 2018 | stance |
| 4 | 29 | 564 | Audit every feed against the ten characteristics and publish the audit with the feed's provenance | A ready-made checklist; algorithmic confounding and drift are invisible in the data | Practice (textbook) | Adaptable (strong default; the audit itself is a Nightlife Culture choice) | Salganik 2018 §2.3 |  |
| 4 | 30 | 565 | Never claim what a head-only feed cannot see | Top-50 data say nothing about the tail | Reading | **Fixed** as a stance | Aguiar & Waldfogel 2015 (abstract) | stance |
| 4 | 31 | 566 | For administrative sources, state why the organisation recorded it and who is not in it | Not collected for research; undocumented for analysis; coverage and unit errors | Standard + Evidence | **Fixed** | ONS 2023 error catalogue; Connelly et al. 2016 | unmarked |
| 4 | 32 | 567 | Write the outlier rule and threshold before the data arrives; prefer the median absolute deviation to mean-and-SD; justify the threshold | Mean-and-SD is self-defeating; 41% silent-exclusion signal | Evidence (adjacent domain) | **Fixed** as a procedure; Adaptable (rule and threshold) | Leys et al. 2013; Bakker & Wicherts 2014 | procedure + Adaptable part |
| 4 | 33 | 568 | Investigate a flagged point against the six artefact causes before treating it as a finding; remove only a confirmed artefact, and declare the removal | The definition is "a different mechanism"; the seventh cause is the finding | Evidence + Practice | **Fixed** | Hawkins via Aggarwal; Osborne & Overbay 2004; NIST | unmarked |
| 4 | 34 | 569 | Any figure shown with a point removed is shown with it included, one tap away | "Report what the statistical results are if those observations are included" | Evidence (adjacent domain) | **Fixed** | Simmons, Nelson & Simonsohn 2011 | unmarked |
| 4 | 35 | 570 | Do not run automated outlier alerts on box-plot fences or normal-theory tests for skewed data without stating the false-flag rate | ≥30% of normal samples flagged; non-normality read as outliers | Evidence | **Fixed** | Dawson 2011; NIST (Grubbs) | unmarked |
| 4 | 36 | 571 | Treat a good-end outlier as a hypothesis about mechanism; state the criteria, threshold and comparison group; show its base | Positive deviance's second step; its systematic review | Evidence + Practice | **Fixed** | Bradley et al. 2009; Baxter et al. 2016; Gelman & Price | unmarked |
| 4 | 37 | 572 | Contextual anomalies (unusual for this place at this time) need a model of normal that includes the context; a global threshold cannot find them | Point, contextual and collective anomalies | Evidence (survey) | Adaptable | Chandola, Banerjee & Kumar 2009 |  |
| 4 | 38 | 573 | Which grain, which day boundary, which denominator, which concentration instrument, whether a seventh kind of nothing, how a nothing looks, how much provenance on the face, suppress or perturb, which outlier rule, which neighbours | Open choices with named trade-offs | — | Adaptable | Section 12 |  |
| 4 | 39 | 574 | How the labels, codes, gaps and provenance panels are styled | Free within the design system and Chapter 3's rules on colour and words | — | *Decorative* | Design system |  |
| 5 | 1 | 409 | Write the construct and the theoretical framework before choosing parts; a composite without one is not built | The handbook's first step; a "mashup index" is one whose producer "is essentially free to set" its parts | Standard + Evidence | **Fixed** | OECD/JRC 2008; Ravallion 2012 | unmarked |
| 5 | 2 | 410 | Every part of a composite carries Chapter 4's provenance set | A composite inherits every defect of its parts and hides them | Standard | **Fixed** | Chapter 4; Code of Practice 3.0 | unmarked |
| 5 | 3 | 411 | State the normalisation and note that it sets exchange rates; prefer the method that matches the data's shape and the measure's purpose | Z-scores let extremes dominate; min-max lets outliers set the range; the trade-off changes with the unit | Standard + Evidence | **Fixed** (stated); Adaptable (which) | Handbook §1.5; Munda & Nardo 2005 | other qualifier + Adaptable part |
| 5 | 4 | 412 | Declare who set the weights and how; treat equal weights as a declared judgement, never a default; check for the uneven-group trap | "Weights are essentially value judgements"; "equal weighting does not mean 'no weights'" | Standard | **Fixed** | Handbook §1.6; Greco et al. 2019; SPI methodology | unmarked |
| 5 | 5 | 413 | Show the effective importance of each part beside its nominal weight | Nominal weights "are hardly ever found to match" main effects; 20% can explain 21% and 40% can explain 81% | Evidence | **Fixed** | Paruolo, Saisana & Saltelli 2013; Becker et al. 2017† | unmarked |
| 5 | 6 | 414 | Choose the aggregation as a judgement about which parts may compensate which, and say so | Addition is fully compensatory; (21,1,1,1) = (6,6,6,6); the HDI, Legatum and the IMD all changed their arithmetic to stop good parts hiding bad ones | Standard + Evidence | **Fixed** | Handbook §1.6 and toolbox (via JRC web reproduction); HDR 2010; Legatum; IoD 2019 | unmarked |
| 5 | 7 | 415 | Publish the price list of any additive or partly compensatory index — the rate at which each part exchanges for each other, in the parts' own units — and answer the refusal test | The exchange rate exists whether or not it is shown ($0.51 against $9,000); "how many new venues compensate for one forty-year-old institution?" | Evidence + Nightlife Culture | **Fixed** | Ravallion 2010/2012; version 1 Ch 6 | unmarked |
| 5 | 8 | 416 | Decide and declare whether the instrument is one-tailed (built to find shortfall, or thriving) or two-tailed | The IMD is "specifically constructed to identify deprivation and not affluence"; the arithmetic differs | Standard (adjacent domain) + Reading | **Fixed** (declared); Adaptable (which) | IoD 2019 Technical Report | other qualifier + Adaptable part |
| 5 | 9 | 417 | Run an uncertainty and sensitivity analysis over the defensible alternatives and publish the rank with its interval | "No longer a magic number"; ranks read "not only at face value, but also within the 90 percent confidence intervals" | Evidence + Practice (JRC audit) | **Fixed** | Saisana, Saltelli & Tarantola 2005; JRC GII 2025 audit | unmarked |
| 5 | 10 | 418 | Report composite scores to two effective digits unless the inputs justify more; never imply a resolution the inputs lack | Official rounding guidance; decimal places are a claim | Standard | **Fixed** | ONS style guide; Analysis Function tables guidance; Ehrenberg (Ch 3) | unmarked |
| 5 | 11 | 419 | Say a rank as a range with a most-likely value | The official form for an uncertain figure | Standard | **Fixed** | Analysis Function 2018 | unmarked |
| 5 | 12 | 420 | Design the independent audit with the measure: name the check that is not on the dashboard, its frequency and owner, and the response to gaming | Measures change what they measure; the improvements were real and remain unverifiable because no independent check was built | Evidence (adjacent domain) | **Fixed** as a procedure | Campbell 1976; Bevan & Hood 2006; Hood 2006; PASC 2003 | procedure |
| 5 | 13 | 421 | Expect ratchet, threshold and output-distortion effects and the three non-adversarial failures of a proxy; monitor the distribution near any threshold | The eight-minute "spike"; regressional, extremal and causal failure need no cheat | Evidence (adjacent domain) | **Fixed** as a procedure | Bevan & Hood 2006; Manheim & Garrabrant 2018 | procedure |
| 5 | 14 | 422 | Use "multiple indicators, all recognized as imperfect" and never a single target with sanctions attached | Campbell's remedy, with his own doubt; the target was met only where it carried sanction, and gamed there | Evidence (adjacent domain) | Adaptable (strong default) | Campbell 1976; Bevan & Hamblin 2009† |  |
| 5 | 15 | 423 | Validate a reading for a use, under the five sources of evidence; state reliability first, including inter-rater reliability for any judged score | "It is the interpretations of test scores for proposed uses that are evaluated, not the test itself" | Standard (adjacent domain — psychometrics) | **Fixed** | AERA/APA/NCME 2014; Messick 1995; McHugh 2012 | unmarked |
| 5 | 16 | 424 | Test discriminant validity against size and against platform coverage | A measure that moves with the platform measures the platform | Standard + Reading | **Fixed** | Standards 2014; Chapter 4 | unmarked |
| 5 | 17 | 425 | Count a consequence against validity when it traces to construct underrepresentation or irrelevant variance; otherwise record it as a consequence | The *Standards'* boundary; Messick's two failures | Standard (adjacent domain) | **Fixed** | Standards 2014 p. 20; Messick 1995 | unmarked |
| 5 | 18 | 426 | Cognitively test any felt-quality question before use; present felt qualities as a small panel unless a combination is separately validated | The ONS's four questions; "It is not appropriate to combine these questions" | Standard | **Fixed** (test); Adaptable (combine) | ONS QMI and user guide; Dolan, Layard & Metcalfe 2011 | other qualifier + Adaptable part |
| 5 | 19 | 427 | Gather recognition from the people measured, record what it corrected, and mark it on the card as face validity and credibility — not as evidence of the construct | Member checks correct fact and confirm resonance; evidence that they improve findings is thin; the *Standards* do not count face validity | Evidence (adjacent domain) + Nightlife Culture | **Fixed** as a stance | Lincoln & Guba — secondary; Birt et al. 2016; Thomas 2017 — secondary; Morse et al. 2002; Reed 2008 | stance |
| 5 | 20 | 428 | Give the people measured the first claim on which parts count and how they are weighted, through a facilitated process with real decision power | The studio's own position, with Sen's argument from public reasoning; the evidence on process design is from environmental management and says how, not whether | Nightlife Culture + Reading; Evidence (adjacent domain) for the how | **Fixed** as a stance (the studio's) | Sen 2005; de Vente et al. 2016; Charlton 1998 | stance |
| 5 | 21 | 429 | Combine community-chosen indicators with field measurement; accept neither unquestioningly | Mostly valid, "not always sufficiently accurate or reliable" | Evidence (adjacent domain; one study) | Adaptable | Reed, Dougill & Baker 2008† |  |
| 5 | 22 | 430 | Whatever the form, the components travel with it: a composite is accompanied by its dashboard | UNECE 2025 recommendation; Stiglitz–Sen–Fitoussi; Paruolo's second option (do not aggregate pillars with important trade-offs) | Standard | **Fixed** | UNECE 2025 §4.25; SSF 2009 Rec. 9 and 11 | unmarked |
| 5 | 23 | 431 | Publish the recipe as a standard card, one tap from any composed number, with the fact of composition visible beside the number | Three of the handbook's six cons are conditional on transparency; "explicit, public steps of inference" | Nightlife Culture + Standard; Practice for the form | **Fixed** | Version 1 Ch 6; Handbook; Cronbach & Meehl 1955; Gebru et al.; Mitchell et al.; Holland et al. | unmarked |
| 5 | 24 | 432 | No composite cultural-value score without an adopted method: the ten steps written, judgements declared, sensitivity run, validity evidence gathered, recognition recorded, card published | A score before that is a mashup | Nightlife Culture (with Standard behind it) | **Fixed** | Version 1; Handbook; Ravallion | unmarked |
| 5 | 25 | 433 | Treat the belief that decision-makers prefer a composite as Practice until evidence is found | No study found either way; the one commentary read calls the spread "mostly advocacy-driven" | Reading | Adaptable | Saltelli 2007† |  |
| 5 | 26 | 434 | Which form; which construct and parts; who weights; which aggregation and tail; how much of the card on the face; how recognition is gathered; how the audit runs | Open choices with named trade-offs | — | Adaptable | Section 14 |  |
| 5 | 27 | 435 | How the card, the sliders, the profile shape and the interval are styled | Free within the design system and Chapter 3's rules | — | *Decorative* | Design system |  |
| 6 | 1 | 491 | Before any behavioural figure is read, name the population the record observes and who it cannot see | Revealed-preference methods "only measure use-value"; footfall is one network's 24m devices with residents and workers excluded; card data skews "younger and more metropolitan" | Standard + Evidence | **Fixed** | Fujiwara & Campbell 2011; ONS RTI methodology 2026; ONS 2016; Wesolowski et al. 2012 | unmarked |
| 6 | 2 | 492 | Treat distance as a price only with the method's assumptions stated: single purpose, a declared value of time, substitutes considered | "If a trip has more than one purpose, it almost certainly violates the travel cost model's central assumption"; time valued at "one-third to the full wage", neither bound firm | Standard (adjacent domain) | **Fixed** (stated); Adaptable (values) | US EPA 2010; Fujiwara & Campbell 2011; Poor & Smith 2004† | other qualifier + Adaptable part |
| 6 | 3 | 493 | Define a catchment by a self-containment threshold on observed flows, and state the threshold | TTWAs: 75% both ways, 66.7% for large areas — the catchment is a rule, not a radius | Standard | **Fixed** as a procedure | ONS TTWA 2015 | procedure |
| 6 | 4 | 494 | Measure return as survival with censoring; a visitor who has not yet returned is censored, not lost | Simple rates "ignore the duration spent"; censoring "(a) a patient has not (yet) experienced the relevant outcome" | Evidence (adjacent domain) + Reading | **Fixed** as a procedure | Clark et al. 2003 | procedure |
| 6 | 5 | 495 | Report diversity as variety, balance and disparity, and declare which the index weights; count supplied and consumed diversity separately | "Each is a necessary but insufficient property"; "diversity increases when variety is the sole consideration, whereas taking balance or disparity into account leads to the opposite conclusion" | Evidence | **Fixed** | Stirling 2007; Benhamou & Peltier 2007† ; Jost 2006† | unmarked |
| 6 | 6 | 496 | Any access score names what it leaves out | PTAL "does not take into account the destinations you can travel to from each location or the ease of interchange" | Standard + Practice | **Fixed** as a stance | TfL 2015 | stance |
| 6 | 7 | 497 | Measure welcome with an instrument validated for belonging, re-tested in the scene's own wording, rather than with a proxy | Four elements; eight items; confirmed by factor analysis on n = 293 residents of neighbourhoods | Evidence (adjacent domain — community psychology) | **Fixed** (instrument); Adaptable (wording) | McMillan & Chavis 1986; Peterson, Speer & McMillan 2008 | other qualifier + Adaptable part |
| 6 | 8 | 498 | When comparing an audience with "the public", state the national yardstick's definition and reference period | 91% engage in 12 months when reading counts; response rate 25% | Standard | **Fixed** | DCMS Participation Survey 2023–24 | unmarked |
| 6 | 9 | 499 | State survival as a cohort figure with its definition, and mark closures provisional for two years | "A business is deemed to have survived if it was born in year t … and it is active … in any part of t plus 1"; deaths "not final until the third year" | Standard | **Fixed** | ONS Business Demography 2025; QMI | unmarked |
| 6 | 10 | 500 | Name the sense of "resilience" before measuring it: bounce back, absorb, or adapt | Three interpretations in one word; the authors favour the third | Reading (Evidence for the taxonomy) | **Fixed** as a stance | Martin & Sunley 2013/2015; Walker et al. 2004 | stance |
| 6 | 11 | 501 | Any early-warning indicator states its window, its threshold, and its out-of-sample record | 24-month window; "the predictive power of even the best of them may be limited" | Evidence (adjacent domain) | **Fixed** as a procedure | Kaminsky, Lizondo & Reinhart 1998†; Berg & Pattillo 1999† | procedure |
| 6 | 12 | 502 | Grade every proxy for value as validated, reasonably likely, or neither, on the card | A surrogate "is expected to predict that clinical benefit"; "In practice, this requirement frequently fails" | Standard (adjacent domain) + Reading | **Fixed** as a stance | FDA 2018; Fleming & DeMets 1996 | stance |
| 6 | 13 | 503 | Keep a measure that is not the proxy beside the proxy, and watch for them parting | The forest "grew excellently in the first generation" | Evidence + Reading | **Fixed** as a stance | Scott 1998; Plochmann via Scott | stance |
| 6 | 14 | 504 | Label every activity figure gross until the deductions are shown; name which of deadweight, displacement, leakage and substitution were applied and from where | "Additionality is the extent to which something happens as a result of an intervention that would not have occurred in the absence of the intervention"; "significant care needs to be taken in using default or ready reckoner values" | Standard | **Fixed** | HCA Additionality Guide 2014 (withdrawn 2022) | unmarked |
| 6 | 15 | 505 | Ask of any price-based indicator whether it measures a product or a rent | "a rent is paid because corn is high" | Evidence (classical economics) + Reading | **Fixed** as a stance | Ricardo 1817; Mazzucato 2018 (blurb, secondary) | stance |
| 6 | 16 | 506 | Show distributional figures weighted beside unweighted, with the weight and its source | "Practitioners must present weighted estimates alongside unweighted estimates" | Standard | **Fixed** | HM Treasury Green Book 2026 ch. 7 | unmarked |
| 6 | 17 | 507 | Never place a social-return ratio in a league table; show it with its story | "it is not appropriate to compare the social return ratios alone" | Standard (the method's own) | **Fixed** | SROI Guide 2012; Social Value International | unmarked |
| 6 | 18 | 508 | Keep economic displacement (a deduction) and residential displacement (people moved out) apart; show who left, and call it displacement only with the comparison the literature requires and the three readings named | Proxies "cannot be relied upon to distinguish between involuntary displacement, voluntary outmigration or incumbent socio-economic uplift" | Standard + Evidence | **Fixed** | HCA 2014; Easton et al. 2020 | unmarked |
| 6 | 19 | 509 | Label every claim of cause with the rung its evidence reaches; from observational data alone the verbs are "alongside", "after" and "where"; "contributed to" only with a theory of change whose alternatives have been tested | "Interventional questions cannot be answered from purely observational information"; "Ruling out of alternative causes in order to claim impact" | Evidence + Standard | **Fixed** | Pearl 2018; Magenta Book 2026; Mayne 2008 | unmarked |
| 6 | 20 | 510 | Where the question behind a chart is causal, state the question and the rung rather than letting "associated with" stand in for an answer | The euphemism hides the question (reconstructed abstract) | Reading | Adaptable (strong default) | Hernán 2018† |  |
| 6 | 21 | 511 | Where a causal reading is wanted, show Hill's viewpoints the data can show — gradient, consistency, sequence — and the alternatives considered | "is there any other way of explaining the set of facts before us" | Evidence (adjacent domain) | **Fixed** as a procedure | Hill 1965 | procedure |
| 6 | 22 | 512 | A theory-of-change claim names its alternative explanations and the evidence against each | "Ruling out of alternative causes in order to claim impact"; a story "stronger and more credible", never "foolproof" | Standard | **Fixed** | Magenta Book 2026; Mayne 2008 | unmarked |
| 6 | 23 | 513 | "Leading" is shown only when a lead has been measured against a named reference series; until then two series are two series | "it is only Granger causality"; a CLI is built by turning-point comparison | Evidence + Standard | **Fixed** | Granger (Scholarpedia); OECD CLI | unmarked |
| 6 | 24 | 514 | The studio's claim ladder puts the observed fact on top, the anchor claim beneath it marked as contribution, a deadweight line marked as stated preference, and counter-flows | Version 1's form, amended by Pearl, Hill and the Additionality Guide | Nightlife Culture (tested) | **Fixed** as a stance | Version 1 Ch 6; this chapter §8 | stance |
| 6 | 25 | 515 | Treat every dashboard view as exploratory; a pattern is a hypothesis with a date until tested outside the data that produced it | "the same data cannot be used to generate and test a hypothesis"; holdouts "wear out" | Evidence (adjacent domain) | **Fixed** | COS; Goodfellow et al. 2016; Google MLCC | unmarked |
| 6 | 26 | 516 | Judge the surprise of a found comparison against the number of comparisons the view allowed | "multiple comparisons can be a problem, even when there is no 'fishing expedition'" | Evidence | **Fixed** | Gelman & Loken 2013/2014 | unmarked |
| 6 | 27 | 517 | Choose family-wise or false-discovery control for any highlighting rule, and say which | The two error rates; neither makes every highlight real | Standard (adjacent domain) | **Fixed** (declared); Adaptable (which) | Benjamini & Hochberg 1995 | other qualifier + Adaptable part |
| 6 | 28 | 518 | No "significant" badge standing alone as the reason for a highlight or a decision; an error-controlled highlighting rule is not a badge | "decisions should not be based only on whether a p-value passes a specific threshold"; "the glitter of the t table" | Standard (professional) | **Fixed** | ASA 2016; Hill 1965 | unmarked |
| 6 | 29 | 519 | Treat two trending series as one comparison; do not report their correlation as a finding | "sequential years are not independent of each other" | Evidence (Yule by citation; Vigen as plain statement) | **Fixed** | Vigen; Yule 1926 (metadata) | unmarked |
| 6 | 30 | 520 | Any model on the display states what it is importantly wrong about, which culture it was built in, and the date and population of its last validation | "the scientist must be alert to what is importantly wrong"; "population distributions are nonstationary" | Evidence | **Fixed** as a procedure | Box 1976; Breiman 2001; Hand 2006 | procedure |
| 6 | 31 | 521 | A pattern becomes a canonical truth by two tests, out-of-sample and the agreement of the competent; the described are among the competent | "Validation literally means to make valid, through the agreement of those judged competent"; KDD step one is "from the customer's viewpoint" | Evidence + Standard for the two tests; Nightlife Culture for who is competent | **Fixed** (two tests); **Fixed** as a stance (the described) | Glover 2014; AQuA Book 2025; Fayyad et al. 1996; Chapter 5 (Sen) | other qualifier + stance |
| 6 | 32 | 522 | Never read two points as a trend; show a measure against its own history with limits the data set | "tells you nothing about trends and how much the data varies naturally"; "You don't set the limits" | Practice (NHS guidance) + Evidence (adjacent domain) | **Fixed** | NHS Making Data Count 2019; NIST/SEMATECH | unmarked |
| 6 | 33 | 523 | Distinguish common-cause from special-cause variation on the face, and say which action each calls for | "wild goose chases" | Practice (NHS guidance) | **Fixed** as a stance | NHS Making Data Count 2019 | stance |
| 6 | 34 | 524 | Every alert states its false-alarm rate and its detection delay, worked out for the measure's own distribution and agreed with the people who answer it | ARL ≈ 371 for one rule of a correct 3σ chart on a long stable series; run-length "between seven and nine … you should decide" | Standard (adjacent domain) + Practice | **Fixed** (stated); Adaptable (values) | NIST/SEMATECH; NHS 2019 | other qualifier + Adaptable part |
| 6 | 35 | 525 | Judge an anomaly against the same season in previous years, not the previous period | "data from the less recent past often encompass relevant information about e.g., seasonality" | Evidence (adjacent domain) | **Fixed** as a procedure | Salmon, Schumacher & Höhle 2016 | procedure |
| 6 | 36 | 526 | Surveillance claims state their comparator and their boundary | "could have indicated an 'alarm' … depending on the data source and the comparator" | Evidence (adjacent domain) | **Fixed** | Spiegelhalter et al. 2003† | unmarked |
| 6 | 37 | 527 | Never rank places of different sizes by a raw rate; show the interval or do not rank | "Small schools are overrepresented at both tails, exactly as expected" | Evidence | **Fixed** | Wainer 2007/2009 | unmarked |
| 6 | 38 | 528 | Define "small" by precision needed, not by geography | "the sample size is not large enough for a direct design-based estimation of sufficient precision" | Standard | **Fixed** | Eurostat 2019 | unmarked |
| 6 | 39 | 529 | Show the direct figure with its interval and the shrunk figure with its weight, side by side; mark modelled figures modelled with their covariates named; label a complete count's interval as drawn from its history, a sample's from its sampling | Weight on the model = sampling variance ÷ total variance; two observations gave "an implausibly high estimate" | Standard + Evidence | **Fixed** | SAIPE; Gelman 2006; Efron & Morris 1975; Eurostat 2019 | unmarked |
| 6 | 40 | 530 | No trend arrow on a modelled small-area figure | Its intervals "should not be used to measure change" | Standard | **Fixed** | ONS income QMI 2025 | unmarked |
| 6 | 41 | 531 | Say whether a withheld figure is withheld for confidentiality or for precision, and never let the same mark mean both | NHS 1–7 as "*"; Analysis Function 2/3/5; OPN base > 10; ASHE's dark green means both | Standard + Reading | **Fixed** as a stance | NHS England 2023; Analysis Function 2026; ONS OPN 2025; ONS ASHE 2018 | stance |
| 6 | 42 | 532 | Set the identifying threshold by the scene's knowability, above the national rule where local knowledge would name the units | The national rules assume an intruder without local knowledge | Nightlife Culture + Standard behind it | **Fixed** as a stance | This chapter; Decision Book Ch 8/15 | stance |
| 6 | 43 | 533 | Record the ten-line claim record beneath every statement of value; "not done" is written, not hidden | A visible boundary is a boundary; a hidden one is an overclaim | Nightlife Culture (with Standard behind each line) | **Fixed** as a stance | This chapter §12 | stance |
| 7 | 1 | 439 | Every comparison carries the comparison record: what is held equal, who chose the comparators, the standardisation, the order, the interval, the season, the base month, the design, the ripple, the future's terms; a line that cannot be filled says "not done" | A comparison is a claim that two things are alike in all but one respect; the claim is shown or it is assumed | Standard behind each line; Nightlife Culture for the record as a whole | **Fixed** as a stance | This chapter §12; Chapter 4 | stance |
| 7 | 2 | 440 | No league table of places on any measure, and no bands of position (quintiles and the like); position is shown within a distribution with its interval, in categories of statistical separation from an expectation if categories are needed | Rankings "play a crucial role in creating this hierarchy"; "about two thirds of all possible comparisons do not allow separation"; "Remove the aggregate index and country rankings"; ranks of many small units do not survive their intervals | Evidence + Standard; the extension to every measure on a dashboard of small places is a Reading | **Fixed** as a stance | Espeland & Sauder†; Goldstein & Spiegelhalter 1996; Marshall & Spiegelhalter 1998; Mogstad et al.†; EPR 2021; SHMI; RSS 2005† | stance |
| 7 | 3 | 441 | Where a single place's rank must be stated (a reader asks "where do we stand?"), it is given as a range, and a small unit's rank on a rate is not stated at all | "ranks are extremely unreliable statistical summaries … particularly for smaller institutions"; about one city in five has a rank interval of ±3 or more under modelling choices alone | Evidence | **Fixed** | Marshall & Spiegelhalter; JRC C3 2017/2019; Chapter 5; Chapter 6 | unmarked |
| 7 | 4 | 442 | Compare places on a funnel or against a declared expectation, never by sorted value alone; where a display is sorted, the sort is a reading aid and the finding is position against limits | "avoid spurious ranking of institutions into 'league tables'"; "Always rank bars by value" is a readability rule | Evidence + Standard (adjacent domain); Practice | **Fixed** (the principle); Adaptable (the form) | Spiegelhalter 2005†; APHO 2007; PHE 2017; Analysis Function 2022 | other qualifier + Adaptable part |
| 7 | 5 | 443 | State and handle over-dispersion before reading points outside a funnel | "could lead to a large number of institutions being inappropriately classified as 'abnormal'" | Evidence (adjacent domain) | **Fixed** as a procedure | Spiegelhalter 2005b†; APHO 2007 | procedure |
| 7 | 6 | 444 | Standardise for the drivers of a rate before comparing places, or state that the rate is crude and why | Equal crude rates in populations of different structure mean unequal performance | Standard (adjacent domain) | **Fixed** (declared); Adaptable (whether) | APHO 2008; ONS mortality guide | other qualifier + Adaptable part |
| 7 | 7 | 445 | An observed-to-expected ratio is compared with the expectation, and with other ratios only under the two conditions the method names; it is not ranked | "should only be directly compared to each other if the age structures … are similar to the standard, or if the ratio of their age-specific … rates to that of the standard is consistent across the age groups"; "It is inappropriate to rank trusts according to their SHMI" | Standard (adjacent domain) | **Fixed** | APHO 2008; NHS England SHMI | unmarked |
| 7 | 8 | 446 | Peers are chosen by a published method with a stated distance, a fixed number appropriate to the field, and a stated assumption, applied to every place alike before any comparison; each carries a label for how like it is | ONS 20 by Euclidean distance; DfE 10 with closeness bands; "It was assumed that local authorities with similar characteristics would perform or progress at a similar rate" | Standard + Practice (CIPFA) | **Fixed** as a procedure | ONS 2025/2026; DfE 2025; CIPFA | procedure |
| 7 | 9 | 447 | Self-chosen comparators are shown beside the published set, labelled as chosen, and the choice is kept as data; they never define the comparison alone | "peer groups are constructed in a manner that biases compensation upward, particularly in firms outside the … S&P 500"; "Preliminary evidence suggests that increased disclosure has reduced the biases" | Evidence (adjacent domain, abstract)† + Nightlife Culture | **Fixed** as a stance | Faulkender & Yang 2010†; Bizjak et al. 2011†; version 1 Ch 5 | stance |
| 7 | 10 | 448 | Where each of two places exceeds the other on different measures, say they cannot be ordered | "The evidence of conflicts is smashed out by aggregation methods to obtain a single quantity, which allows a ranking" | Evidence + Reading | **Fixed** as a stance | Carlsen & Bruggemann 2022; Fattore 2016† | stance |
| 7 | 11 | 449 | Identity measures — those the studio designates nominal, and says so — are never on an ordered axis; condition measures are compared through the gate, which now includes interval, standardisation and order | Version 1's split, extended and its examples corrected by this chapter | Nightlife Culture (tested) | **Fixed** as a stance | Version 1 Ch 5; this chapter §11 | stance |
| 7 | 12 | 450 | Name every trend line's method and window; show no end-point of a trend-cycle without a warning | "The smoothness of the trend-cycle can also be controlled by the user"; "the most recent values should not be shown because of the end-point problem" | Practice (textbook) + Standard | **Fixed** | FPP3 §3; Eurostat 2015 §7.2 | unmarked |
| 7 | 13 | 451 | Mark seasonally adjusted figures as estimates subject to revision, name the method, and adjust no series under three years | "seasonal factors are estimates based on present and past experience"; "just one additional observation results in revisions … for several years"; "Very short series (less than 3 years) cannot be seasonally adjusted" | Standard | **Fixed** | US Census Bureau; Eurostat 2015 §4.1, §6.1; ONS | unmarked |
| 7 | 14 | 452 | Do not seasonally adjust a series that is not seasonal | "will often introduce an artificial seasonal element" | Standard (adjacent domain) | **Fixed** | ABS 2023; Eurostat 2015 | unmarked |
| 7 | 15 | 453 | A year-on-year figure shows both ends; a period-on-period figure uses the adjusted series; the display says which growth rate it leads with and why | "does not completely remove all seasonal effects"; the base effect; "Monthly growth should therefore be used with caution and alongside other measures" | Standard | **Fixed** (both ends; say which); Adaptable (which leads) | ABS; Eurostat §7.2; ECB 2007; ONS retail bulletin | other qualifier + Adaptable part |
| 7 | 16 | 454 | Percentage points are not per cent; index points are not per cent; cash is not volume; an index names its base | "A fall of 1% would result in a value of 9.9%"; "index value changes are affected by the level of the index in relation to its base period"; "value data are deflated to produce … volume measures" | Standard | **Fixed** | ONS style guide; BLS; ONS RSI QMI; HMT deflators guide | unmarked |
| 7 | 17 | 455 | Before any change in a place selected for being extreme is read, regression to the mean is named as the first explanation | "should always be considered as a possible cause of an observed change"; "Even if subjects are not treated the mean … will go down" | Evidence (adjacent domain) | **Fixed** | Barnett et al. 2005†; Bland & Altman 1994 | unmarked |
| 7 | 18 | 456 | Every series carries its breaks and its revision status; a consistent back series is provided or its absence stated | "Explain the nature and extent of the change, and provide a consistent back series where possible" | Standard | **Fixed** | Code of Practice 3.0 §7.5, §3.9; ONS revisions policy | unmarked |
| 7 | 19 | 457 | Describe a change by direction, absolute size and relative size; call a change within random variation indicative, not definitive; never caveat with "care must be taken" alone | The Analysis Function's own rules | Standard | **Fixed** | Analysis Function 2018 | unmarked |
| 7 | 20 | 458 | Do not use "significant" of a change unless making a point about statistical significance | ONS style | Standard | **Fixed** | ONS style guide; Chapter 6 | unmarked |
| 7 | 21 | 459 | No fixed number of observations is claimed as enough for a trend; the series' length and noise are stated and what they support | "These are misleading and unsubstantiated in theory or practice" | Practice (textbook) | **Fixed** as a stance | FPP3 §13.7; Hyndman & Kostenko 2007 | stance |
| 7 | 22 | 460 | A before-and-after display lists its eight rivals and uses no verb stronger than "after"; an interrupted series with its impact model declared may say "departed from its trend" | Design 2 is "a 'bad example'"; history, maturation, testing, instrumentation, regression, selection, mortality, interaction | Evidence; the verbs are a Nightlife Culture reading | **Fixed** | Campbell & Stanley 1963; Bernal et al. 2017 | unmarked |
| 7 | 23 | 461 | An interrupted-series claim records its impact model before the after-data are examined, lists co-interventions, handles season and autocorrelation, and carries a control where one exists | "the essential, yet often omitted, step of proposing the impact model a priori"; "cannot exclude confounding due to co-interventions" | Evidence (adjacent domain) | **Fixed** as a procedure | Bernal et al. 2017; Lopez Bernal et al. 2018; Magenta Annex A | procedure |
| 7 | 24 | 462 | A difference-in-differences claim names its comparison group, shows its pre-trend check as a check and not a proof, and reports effects by adoption group when adoption is staggered | "cannot be tested because it involves a non-existent counterfactual"; "'Passing' these tests does not mean that parallel trends is true"; already-treated units "can serve as controls" | Evidence | **Fixed** as a procedure | Cunningham; Huntington-Klein; Roth 2022; Goodman-Bacon 2021; Callaway & Sant'Anna | procedure |
| 7 | 25 | 463 | A synthetic-control claim shows its weights, its pre-period fit, and its placebos in time and in space, and checks the six contextual requirements and the pre-period | "preclude extrapolation"; "make explicit the contribution of each comparison unit"; "small effects will be indistinguishable from other shocks" | Evidence | **Fixed** as a procedure | Abadie, Diamond & Hainmueller 2010, 2015; Abadie 2021 | procedure |
| 7 | 26 | 464 | A cut-off claim speaks for those near the cut-off, and a matched claim for what was recorded | "local average treatment effect"; "only as good as the characteristics used for matching" | Standard + Evidence | **Fixed** | Magenta Annex A; Lee & Lemieux 2010; DIME | unmarked |
| 7 | 27 | 465 | Every intervention claim states whether spillover and displacement were considered, and whether the comparison place was reached by the ripple | "Assuming that such spillover effects do not exist is a strong restriction"; "tells us very little if that activity is simply displaced from elsewhere" | Standard + Evidence | **Fixed** | Magenta Book 2026 §2.3.2; Abadie 2021; What Works Growth | unmarked |
| 7 | 28 | 466 | Before an effect is called absent, the minimum detectable effect for the series and the number of places is stated, by a power calculation whose inputs are declared | "the effect size below which we may not be able to distinguish that the effect is different from zero, even if it is"; "Sample sizes are too small" | Practice (J-PAL; DIME) + Standard (EEF; Magenta Book) | **Fixed** as a procedure | J-PAL; DIME; EEF 2019; Magenta Book 2026 | procedure |
| 7 | 29 | 467 | Every intervention claim states its rung on the What Works scale, with any other ladder's differing placement beside it, and the verb that rung earns; plain before/after and place-against-place are the bottom | "We define SMS 3 methods to be the minimum standard"; "No comparator" scores zero; "it will not evidence direct causality" | Standard (SMS; EEF) + Practice (Nesta) | **Fixed** | What Works Growth SMS; EEF 2019; Nesta 2013 | unmarked |
| 7 | 30 | 468 | A projection is labelled a projection, states its assumptions first, gives a central estimate with a range, states its switching value, and has been adjusted for optimism bias by the maker's own record or the generic uplift | "Projections are not forecasts"; "Practitioners must account for optimism bias"; "A switching value is the value that a key variable would need to change to such that an option stops representing value for money" | Standard | **Fixed** | ONS NPP 2025; Green Book 2026; HMT optimism-bias guidance | unmarked |
| 7 | 31 | 469 | Scenarios say what they do not cover, and a single future figure is not shown; the default is an even number of scenarios, taken from the cross-government toolkit over the Bank's baseline-plus-two | "Try to include an even number of scenarios"; "Presenting a single figure is best avoided"; "neither all-encompassing nor do they reflect the full distribution of risks" | Standard + Practice | **Fixed** (no single figure; say what is omitted); **Fixed** as a stance (even number) | Uncertainty Toolkit; Bank of England 2026; Futures Toolkit | other qualifier + stance |
| 7 | 32 | 470 | Keep and show the record of projections against outturn | "examines how our forecasts compare to subsequent outturn data"; the Green Book's own-record adjustment | Standard + Practice | **Fixed** as a procedure | OBR FER; Green Book 2026 | procedure |
| 7 | 33 | 471 | Words for likelihood carry their numbers in the sentence; no verbal likelihood term stands without one | "substantially improved only when numerical guidelines are bracketed in text"; "only a small decrease in trust … mostly for verbal uncertainty communication" | Evidence | **Fixed** | Wintle et al. 2019; van der Bles et al. 2020†; IPCC 2010 | unmarked |
| 7 | 34 | 472 | A fast or nowcast series is labelled an early sighting of the present, never a forecast | "predicting the present"; "none should be used to predict GDP on their own" | Evidence + Standard | **Fixed** | Choi & Varian; ONS Data Science Campus; Lazer et al.† | unmarked |
| 7 | 35 | 473 | "Leading" is used only of a series with a measured record of turning points against a named reference series — the Conference Board's tests of conformity and consistent timing, or an equivalent stated one — and the record's real-time weakness is noted | "Historically, the cyclical turning points in the leading index have occurred before"; "rarely provided adequate signals" in real time | Standard + Evidence | **Fixed** as a procedure | Conference Board; Chapter 6 | procedure |
| 7 | 36 | 474 | A borrowed concentration threshold names its jurisdiction; a churn figure publishes its recipe; an average over survivors says who left | HHI thresholds are American and the CMA applies none; no official churn; survivorship | Standard + Reading | **Fixed** as a stance | DOJ/FTC 2023; CMA 2026; ONS business demography | stance |
| 8 | 1 | 603 | Every dashboard that intends to be read next year carries, published beside it, the service record: freshness promise, dependencies, refresh, watch and alarm, availability and degraded mode, budget and device, map supply, retirement, owner, not-done | A dashboard is "a digital service" to be "continually" managed; the promise its first screen makes has to be kept by something | Standard + Nightlife Culture for the record as a whole | **Fixed** as a stance | Analysis Function 2026; this chapter §12 | stance |
| 8 | 2 | 604 | Each series states the period it describes, the date published, the date last revised and its declared frequency; "last updated" alone is never shown | "Always make it clear which dates or period"; the catalogue standards separate the dates and the frequency; a date without a frequency does not say whether the figure is late; an absent date means one of three things | Standard (the period); Nightlife Culture (the four parts) | **Fixed** (period); **Fixed** as a stance (four parts) | Analysis Function 2026; DCAT 3; DCAT-AP 3; DCMI; ONS revisions policy | other qualifier + stance |
| 8 | 3 | 605 | The page's freshness lifetime is declared in days, compared against the data's date on the page itself, and shown in words a reader can read | "A 'stale' response is one where" its age has exceeded its lifetime; "The oldest data is no older than Y" is a checkable sentence | Standard + Practice (adjacent domain) | **Fixed** as a procedure | RFC 9111 §4.2; SRE workbook | procedure |
| 8 | 4 | 606 | A change to the data carries a change note saying what changed and when; the page is never marked updated without saying what | "Do not say the page has been updated without saying what has changed" | Standard | **Fixed** | GOV.UK change notes; Analysis Function 2026 | unmarked |
| 8 | 5 | 607 | Revisions and corrections are distinguished and dated; a figure open to revision says until when | "A revision is a scheduled change"; "A correction is an unplanned revision … because of the identification of an error" | Standard | **Fixed** | ONS revisions policy; Code of Practice 3.0 §3.9 | unmarked |
| 8 | 6 | 608 | Every dependency is recorded with its stated limit, its terms, the notice it has promised, and the date its page was read; it is marked as needed at build time or at read time, and as a dependency on *supply* or on *terms* | The open licence "does not guarantee the continued supply"; the platform terms address storing, deriving, combining and scheduled calling clause by clause | Standard | **Fixed** as a procedure | OGL v3.0; the platform terms §6 | procedure |
| 8 | 7 | 609 | The stated rate limit is the real limit; the refresh job never relies on capacity beyond it, respects `Retry-After`, keeps a clock per interface, and backs off with jitter | "you should not let your users go over the limits you set even if you have spare capacity"; "Always use randomized exponential backoff" | Standard + Practice | **Fixed** | GDS service levels; RFC 6585; ONS bots; SRE ch. 22 | unmarked |
| 8 | 8 | 610 | A beta-labelled or no-service-level interface is treated as able to change without notice, whatever its publisher | "there may occasionally be breaking changes"; beta "where your users are expecting breaking changes" need not be given the six months | Standard | **Fixed** as a stance | ONS developer hub; GDS live API guidance | stance |
| 8 | 9 | 611 | Response headers announcing deprecation and sunset are read by the refresh job and raise a ticket | The statistics office signals retirement by `Deprecation`, `Sunset` and `Link` headers, then 404; a client reading only the body cannot see it coming | Standard + Practice | Adaptable (which interfaces signal); **Fixed** (that the job reads them) | ONS retirement guide | Adaptable part + other qualifier |
| 8 | 10 | 612 | Platform interfaces are used only within their written terms; a series derived from a platform whose terms forbid deriving it is not built | III.13: "Do not analyze … creating new or derived listenership metrics"; "non-commercial use only" | Standard | **Fixed** | Spotify Developer Policy; Skiddle; Last.fm; Ticketmaster | unmarked |
| 8 | 11 | 613 | Whether to call a platform at all is a recorded decision made with its terms open, not a default | A dependency on terms is theirs to withdraw | Nightlife Culture | Adaptable | This chapter §6, §13; `[Prototype flag]` |  |
| 8 | 12 | 614 | Fetch at build time, not at read time; the reader's page depends on its host alone, and every other dependency is the night's job's | "A service cannot be more available than the intersection of all its critical dependencies"; ten at 99.9% is 3.65 days a year | Practice (adjacent domain) + chapter's arithmetic | **Fixed** as a stance; Adaptable for a declared live element | Treynor et al. 2017; SRE availability table; Willison 2021 | stance + Adaptable part |
| 8 | 13 | 615 | On a failed fetch the last good copy is kept and shown with its age; the page is never blanked | "Invalidating or emptying local state as a result of a failed refresh" is a named anti-pattern; `stale-if-error`; "Stale data is almost always better than incorrect data" | Standard + Practice | **Fixed** | AWS REL05-BP01; RFC 5861; SRE workbook | unmarked |
| 8 | 14 | 616 | Each series is its own compartment; a closed source empties one panel and not the page | "if one element fails, the others continue to function"; "Integration points are the number-one killer of systems" | Practice (adjacent domain) | **Fixed** as a procedure | Azure bulkhead; Nygard; Fowler | procedure |
| 8 | 15 | 617 | The degraded mode is exercised before launch and on a schedule, and the date recorded | "the code path you never use is the code path that (often) doesn't work" | Practice (adjacent domain) | **Fixed** as a procedure | SRE ch. 22 | procedure |
| 8 | 16 | 618 | The availability objective is set in the data's terms, written before launch, and not higher than readers can tell | "100% is the wrong reliability target"; "Users build on the reality of what you offer, rather than what you say you'll supply" | Practice (adjacent domain) | **Fixed** as a stance; Adaptable in value | SRE ch. 1, 3, 4 | stance + Adaptable part |
| 8 | 17 | 619 | A page that loads with the wrong or stale content is counted as an error, so the watch checks the data's date and not the status code | Errors include "an HTTP 200 success response, but coupled with the wrong content" | Practice (adjacent domain) | **Fixed** | SRE ch. 6 | unmarked |
| 8 | 18 | 620 | The watch is independent of the job and the scheduler, pinged by the job after the effect is confirmed, recorded as a dependency in its own right, and its ticket goes to a role with a named second | Schedules are delayed, "may be dropped", are disabled after 60 quiet days and notify "the user who last modified the cron syntax"; "monitoring of the effect of cron jobs" | Standard (platform) + Practice | **Fixed** as a procedure | GitHub docs; SRE ch. 24; Healthchecks.io | procedure |
| 8 | 19 | 621 | Signals are sorted into alerts, tickets and logs; a failed refresh is a ticket; the one alert is the page lying about its date | "Every page should be actionable" (a page being a pager alert); "humans should be notified only when they need to take action" | Practice (adjacent domain) | **Fixed** | SRE ch. 1, 6 | unmarked |
| 8 | 20 | 622 | The refresh job is idempotent and, in doubt, skipped rather than doubled; scheduled off the hour | "we favor skipping launches rather than risking double launches"; "High load times include the start of every hour" | Practice + Standard (platform) | **Fixed** as a procedure | SRE ch. 24; SRE workbook; GitHub docs | procedure |
| 8 | 21 | 623 | Every fetch is committed to a version history so that any figure's vintage is recoverable by date | "records changes to that resource over time in the commit history"; a living series owes its archive | Practice | **Fixed** as a stance | Willison 2020; Chapter 4 | stance |
| 8 | 22 | 624 | The free tier's limits are recorded in the service record as design constraints with a date, and no availability is assumed of it | 25 MiB per asset; 1 GB per site; paused at the credit cap; no commitment could be established | Standard (platform) | **Fixed** as a procedure | Cloudflare; GitHub Pages; Netlify | procedure |
| 8 | 23 | 625 | The cost of a live element is computed with the studio's own expected numbers before it is chosen | Billing is per initialisation; "A map load is counted every time Mapbox GL JS initializes" | Standard (price list) | Adaptable | Mapbox pricing; this chapter's arithmetic |  |
| 8 | 24 | 626 | The page is budgeted for the seventy-fifth-percentile phone and network, not the builder's, and tested on one | "15-25% as fast as those carried by programmers and their bosses"; "a good threshold to measure is the 75th percentile" | Practice (a reasoned model) + Evidence (the Almanac's medians) | **Fixed** as a stance | Russell 2024; web.dev; Web Almanac | stance |
| 8 | 25 | 627 | Figures and the table are in the HTML and shown before any script runs; the page is not a single-page application | "Government services should be functional using only HTML" (a standard for government services, adopted here); "1.1% of people aren't getting JavaScript enhancements (1 in 93)", four-fifths involuntarily | Standard (adopted) + Evidence (one measurement) | **Fixed** as a stance | GOV.UK Service Manual; Herlihy 2013 | stance |
| 8 | 26 | 628 | Total weight is held within Russell's five-second budget for the baseline phone — about 1.3 MiB with half script, 2.5 MiB with almost none — and the vector renderer is counted against the script line before it is chosen | "650KiB of JavaScript" or "100KiB of JavaScript" at five seconds; the renderer is about 287 KB gzipped | Practice (a reasoned model) | **Fixed** as a stance; Adaptable in figure | Russell 2024; Bundlephobia (secondary) | stance + Adaptable part |
| 8 | 27 | 629 | The "53% abandon" figure is not used without its date, source and wording, and preferably not at all | Vendor research, 2016, n=3.7K opt-in sites, "likely to be abandoned" | Reading | **Fixed** | Google 2016 | unmarked |
| 8 | 28 | 630 | The map's tile supply is one of four named kinds, recorded with what was agreed to: cache, attribution, logo, offline, non-commercial, pause | "Our tile servers are not [free]"; "no SLA or guarantee"; "service will pause"; "Offline use is not permitted" | Standard (policy) | **Fixed** as a procedure | OSMF; OS; MapTiler; Mapbox; Protomaps | procedure |
| 8 | 29 | 631 | Boundary files are the generalised product appropriate to the scale, cut to the area shown, with their date and two-owner attribution; a boundary vintage is pinned and stated | BFC about 128 MB against BSC about 1.7 MB in the same record; "as at December 2024"; "Contains both Ordnance Survey and ONS Intellectual Property Rights" | Standard | **Fixed** | ONS digital boundaries; Open Geography Portal; Decision Book DTA-05/06 | unmarked |
| 8 | 30 | 632 | Simplification is checked for vanished small polygons before publication | "At high simplification, small polygons can disappear entirely" | Practice | **Fixed** as a procedure | Mapshaper | procedure |
| 8 | 31 | 633 | Every map has a non-map twin — the same figures by the same places as a table — reachable before the script; pan and zoom have buttons; the sequential ramp is short | "make sure the data is available in another format such as a downloadable data table"; WCAG 2.5.1 and 2.5.7 examples; five blues | Standard | **Fixed** | Analysis Function colours; WCAG 2.2; WAI complex images | unmarked |
| 8 | 32 | 634 | The notice the studio gives when retiring a series, and the archive address, are written before the first series needs them; a retired series stays reachable | "Do this at least six months before retirement"; "keeping data and metadata available, with a clear note that it is no longer updated"; "This publication was withdrawn on" | Standard | **Fixed** as a procedure; Adaptable in period | Analysis Function 2026; GOV.UK withdrawal; Code of Practice 3.0 §10.7 | procedure + Adaptable part |
| 8 | 33 | 635 | The owner of the ticket is a role with a successor, and the record says where it lives | "not an appropriate project for a single person"; 65% of projects at truck factor ≤ 2 | Standard + Evidence † | **Fixed** as a stance | Analysis Function 2026; Avelino et al. 2016 † | stance |
| 8 | 34 | 636 | The record's last line states what the dashboard does not promise | "Users build on the reality of what you offer, rather than what you say you'll supply" | Practice (adjacent domain) | **Fixed** as a stance | SRE ch. 4 | stance |
| 9 | 1 | 545 | Every felt measure carries the measure record: construct and register, items, who chose, who was asked, who answered, the spread, the five sources of validity evidence, recognition, discordance, what this changed | A measure is validated by accumulated evidence for a use; without the record nothing accumulates | Standard + Nightlife Culture for the record as a whole | **Fixed** as a stance | AERA/APA/NCME 2014; this chapter §15 | stance |
| 9 | 2 | 546 | The construct is named in words, and its register (made / perceived / excess), before any item is written; the three registers are never collapsed into one number | "define the construct before the proxy"; a "fuzzy concept … flourishes precisely because of its imprecision"; no literature proposes a blended score | Evidence + Reading | **Fixed** as a stance | Chapter 5; Markusen 2012; §1, §4 | stance |
| 9 | 3 | 547 | A measure says whether it is reflective or formative and is validated accordingly | "few studies use formative indicator measurement models, even though they should"; the two are misspecified for each other | Evidence (adjacent domain) † | **Fixed** as a procedure | Jarvis et al. 2003 †; Diamantopoulos & Winklhofer 2001 † | procedure |
| 9 | 4 | 548 | A felt result is reported as a distribution with bands, never as a point alone; coordinates or scores are computed per respondent, not from the room's median | "relying only on average ratings might mask important differences"; "percent of people likely to perceive" | Standard + Practice (adjacent domain) | **Fixed** | ONS FAQ; Mitchell, Aletta & Kang | unmarked |
| 9 | 5 | 549 | Bands' cut-points are chosen by a stated method — the respondents' own turning point, or an adopted official set — and the method is on the record | "the mid-point of the scale (5) acts as an important cut-off for respondents" | Standard | **Fixed** as a procedure; Adaptable in value | ONS FAQ 35 | procedure + Adaptable part |
| 9 | 6 | 550 | A borrowed attribute word is checked for how it is read before it is used; "vibrant" in particular is a derived diagonal and the least evenly read axis of the standard instrument | "a general non-equidistant interpretation of the scales, particularly on the vibrant-monotonous direction" | Evidence (adjacent domain) | **Fixed** as a procedure | Lionello et al. 2021; ISO/TS 12913-3 formulae (secondary) | procedure |
| 9 | 7 | 551 | The place is defined to the respondent in the question, at a stated scale | "By neighbourhood we mean a few minutes walking distance from your home" | Standard | **Fixed** | Community Life Survey questionnaire | unmarked |
| 9 | 8 | 552 | In situ and retrospective answers are different measures (experienced; evaluative) and are not pooled or compared as one | Experienced wellbeing "is concerned with people's emotional states"; evaluative "refers to judgments" | Standard (adjacent domain) | **Fixed** | National Research Council 2013; ONS4 | unmarked |
| 9 | 9 | 553 | Every felt measure states its recruitment route, response, known gaps and the share contributed by its most active contributors | "Mapping effort was highest in sampling groups whose livelihoods were closely related to the purpose"; "90-9-1"; "those who choose to participate are frequently quite unrepresentative" | Evidence † + Practice | **Fixed** | Brown 2017 †; Haklay 2016 †; Nielsen 2006; Fung 2006 | unmarked |
| 9 | 10 | 554 | The ceiling is named: a felt measure taken only among those present is a measure of those who chose to be there | "relatively low variance and high scores observed on attachment" | Evidence (adjacent domain) | **Fixed** as a stance | Williams & Vaske 2003 | stance |
| 9 | 11 | 555 | No felt estimate is published below the official floor (fewer than 50 answers or a numerator under 5), and its precision band is stated | "not published if the sample size they are based on is fewer than 50"; CV bands | Standard | **Fixed** | ONS QMI | unmarked |
| 9 | 12 | 556 | A felt measure for a place is compared with its own history or with declared peers, and Chapter 7's rule against ranking applies | "progress over time within the same local authority, or across local authorities that share a similar demographic composition" | Standard | **Fixed** | ONS QMI; Chapter 7 | unmarked |
| 9 | 13 | 557 | Self-placement used as a measure is private before it is public, is one item among several, and its visible form is labelled a conversation, not a measure | "even mild social influence can undermine the wisdom of crowd effect"; a single item of a non-concrete construct; the living histogram's artefact | Evidence (adjacent domain) † | **Fixed** as a stance | Lorenz et al. 2011 †; Diamantopoulos et al. 2012; Schilling et al. 2002 | stance |
| 9 | 14 | 558 | An open, repeatable vote is never presented as a measure of the place | "Boaty McBoatface topped the list with over 124,000 votes"; "this is an Internet poll" | Evidence (case) | **Fixed** | BIS/NERC 2016; TIME 2009 | unmarked |
| 9 | 15 | 559 | Where representativeness is claimed, recruitment is by sample first; where it is not, the claim is bounded to the participants | "Randomly selecting participants from among the general population is the best guarantee of descriptive representativeness"; "We make no claim that the maps produced represent a coherent and fixed" community | Evidence + Practice | **Fixed** as a stance | Fung 2006; Deliberative Democracy Lab; Reed et al. 2025 | stance |
| 9 | 16 | 560 | A story-of-change method is used for the significant, not the average, and is not relied on as the accountability case | its own manual lists "understand the average experience of participants" and accountability reporting among the things other methods do more efficiently | Practice | **Fixed** as a procedure | Davies & Dart 2005 | procedure |
| 9 | 17 | 561 | "What this changed" is a line on every felt measure: how many answered, what they said, how it informed the decision, within a stated time, told to the people who answered | "Explain the responses that have been received from consultees and how these have informed the policy"; responsiveness "associated with a 57 percent increase" in taking part again | Standard + Evidence † | **Fixed** | Cabinet Office 2018; Sjoberg et al. 2017 †; Arnstein 1969 | unmarked |
| 9 | 18 | 562 | Report-back is tailored to those who answered, not generic | "the tailored newsletter, or sending no newsletter at all, were equally effective … and significantly better than the general newsletter" | Evidence † | Adaptable | Cleary & Balmer 2015 †; Fumagalli et al. 2010 † |  |
| 9 | 19 | 563 | "Co-produced" is used only where the people who gave the data share in what is done with it; otherwise "participatory" | "Co-design and other forms of asking the advice of users … can lack any continuing involvement in delivery" | Practice | **Fixed** as a stance | Boyle & Harris 2009; Chambers 2007 | stance |
| 9 | 20 | 564 | Co-presence is shown as *who was there together*; it is called a tie only after the co-occurrence count has been tested against opportunity, and centrality computed from co-presence is not shown as a measure of anyone's importance | "not easily usable to build in a reliable and systematic fashion surrogate contact data"; "whether an observed number of co-occurrences … is significant"; baseline v inbreeding homophily | Evidence (adjacent domain) | **Fixed** | Génois & Barrat 2018; Neal et al. 2021; McPherson et al. 2001 | unmarked |
| 9 | 21 | 565 | A two-mode network states its boundary — which events and people are in it — because omitting contexts inflates clustering | "network boundary specification and fixed choice designs can dramatically alter estimates of network-level statistics" | Evidence (adjacent domain) † | **Fixed** as a procedure | Kossinets 2006 † | procedure |
| 9 | 22 | 566 | Return is shown as return; stated intention to return is not a measure of it, and return alone is not attachment | "no statistically significant correlation exists between intention and actual repeat visitation rates"; loyalty is attitude *and* patronage | Evidence † | **Fixed** | McKercher & Tse 2012 †; Dick & Basu 1994 † | unmarked |
| 9 | 23 | 567 | An amenity or premises count is labelled an indicator coded by outsiders, never a descriptor | "Can what are in the end organizational directories really get at … the experiential meaning of place?"; "availability does not necessarily mean access" | Evidence + Reading | **Fixed** | Silver, Clark & Navarro 2010; Rhubart et al. 2022 | unmarked |
| 9 | 24 | 568 | A trace is labelled for the population it records and used within-sample; its skew is stated | "Nonrepresentative data are bad for out-of-sample generalizations, but can be quite useful for within-sample comparisons"; "24.4 times the number of Foursquare users per capita" | Evidence + Practice | **Fixed** | Salganik; Hecht & Stephens 2014; Malik et al. 2015; Chapter 4 | unmarked |
| 9 | 25 | 569 | A trace or signal is shown as an indicator of a vibe only after it has been validated against a descriptor in the place and population concerned; until then it is labelled an unvalidated indicator | 77% of an "assumed" proxy; dictionaries "inconsistent"; a signal that flipped sign; "related but distinct constructs" | Evidence | **Fixed** | De Nadai et al. 2016; Jaidka et al. 2020 (reconstructed); Brown & Coyne 2018; Orstad et al. 2017 † | unmarked |
| 9 | 26 | 570 | Text sentiment is labelled as "how people appear to others", with its platform's reach and the tools' known error by speaker stated | "we quantify only how people appear to others"; parser recall "64.0%" against "80.4%" | Evidence | **Fixed** | Dodds et al. 2011; Blodgett et al. 2016 | unmarked |
| 9 | 27 | 571 | No inference of feeling from faces is built, and none from gait or voice without the evidence the face lacks | "no unique mapping between a configuration of facial movements and instances of an emotion category"; the field's own ethics sheet on "utterance, facial expression, gait, etc."; Article 5(1)(f) for biometric inference at work and in education | Evidence + Practice + Standard (law) | **Fixed** as a stance | Barrett et al. 2019; Mohammad 2022; Regulation (EU) 2024/1689 | stance |
| 9 | 28 | 572 | Crowdsourced perception of images is labelled as the judgement of the raters, with who they were | "76.0% identified themselves as male"; predicts "human judgments of pairwise image comparisons" | Evidence | **Fixed** | Salesses et al. 2013; Dubey et al. 2016 | unmarked |
| 9 | 29 | 573 | A sound measure uses what is heard and by whom before how loud; a song-feature proxy is labelled defined-not-derived and supply-withdrawn | the review's report of Axelsson et al.: "perceived sound sources are more important as indicators … than sound levels"; valence defined, derivation unpublished; endpoint withdrawn Nov 2024 | Evidence + Standard (platform) | **Fixed** | Aletta, Kang & Axelsson 2016; Spotify reference; Chapter 8 | unmarked |
| 9 | 30 | 574 | Experience sampling, where used, is within-person, its sample described, and its respondents' burden counted as a cost | "using only the within-individual variation"; "all Apple iOS users"; "difficult to scale up" | Evidence † + Standard | **Fixed** as a procedure | MacKerron & Mourato 2013 †; Seresinhe et al. 2019; NRC 2013 | procedure |
| 9 | 31 | 575 | A new felt item is cognitively tested before it is asked, placed with known context effects, and administered in a stated mode | "Cognitive testing was undertaken to understand how respondents chose their score"; "strongly affected by question structure and context"; mode effects | Standard | **Fixed** as a procedure | ONS user guidance; OECD 2013 | procedure |
| 9 | 32 | 576 | Validity is claimed for an interpretation and a use, argued from the five sources; the record says which have evidence and which say "not yet" | "It is the interpretations of test scores for proposed uses that are evaluated, not the test itself" | Standard | **Fixed** | AERA/APA/NCME 2014 | unmarked |
| 9 | 33 | 577 | Recognition is gathered as member checking — who was shown what, what they said, what changed — and recorded as content and response-process evidence plus legitimacy; it is never presented as validation complete | "Face validity is at best a very weak kind of evidence"; member checking "often mentioned as one in a list" | Evidence + Reading | **Fixed** as a stance | Price et al. 2015; Birt et al. 2016 †; Chapter 5 | stance |
| 9 | 34 | 578 | Reliability is reported where measured and marked "not yet" where not; a 0.70 floor is named as the common minimum and 0.90 as the recommended one | "a reliability coefficient of 0.70 has often been accepted as satisfactory"; "0.90 is the minimum recommended threshold" | Practice (primer) | Adaptable | Boateng et al. 2018 |  |
| 9 | 35 | 579 | Felt and counted layers are integrated by a declared protocol with four cells — agreement, partial agreement, silence, dissonance — and discordance is reported, not resolved by preferring the number | "Discordance occurs if …"; "the only one to include silence" | Standard (method) | **Fixed** as a procedure | Fetters, Curry & Creswell 2013; O'Cathain, Murphy & Nicholl 2010 | procedure |
| 9 | 36 | 580 | The discordant cell is pre-committed before the dashboard is built | Pre-registration of the integration; version 1's rule | Practice + Nightlife Culture | **Fixed** as a stance | Version 1 Ch 4; this chapter §13 | stance |
| 9 | 37 | 581 | The measure's effect on the measured is gathered as consequences evidence after launch, including the extraction question | Consequences are a source of validity evidence; "the mix and balance of extraction and empowerment" | Standard + Nightlife Culture | **Fixed** as a procedure | AERA/APA/NCME 2014; Chambers 2007; house framework (confidential) | procedure |
| 10 | 1 | 693 | Every dashboard that shows people carries the safeguards record: what is held and about whom, the basis, the release model, the method per view, the query-time controls, the walk, who was consulted, who governs and who stood at the door, the held layer, withdrawal, harm, regimes, moderation, review and what this changed | Anonymisation "is a process of risk management but it is also a dynamic decision-making process"; the statute requires "appropriate safeguards" | Standard (law) + Practice + Nightlife Culture for the record as a whole | **Fixed** as a stance | UK GDPR Art 84B; Elliot, Mackey & O'Hara; this chapter §19 | stance |
| 10 | 2 | 694 | The first line of the record is written before the first row is collected, is dated, and names a person | By design and by default; the regulator's step 1 | Standard (law) + Standard (regulator) | **Fixed** as a procedure | UK GDPR Art 25; ICO DPIA steps | procedure |
| 10 | 3 | 695 | Anonymity is assessed in the data environment — what else is public, who is motivated, what tools exist — and reassessed on a stated schedule | "not a property of the data"; "periodically review the decisions you take" | Practice + Standard (regulator) | **Fixed** as a procedure | Elliot, Mackey & O'Hara; ICO anonymisation guidance | procedure |
| 10 | 4 | 696 | The identifiability test is the motivated intruder, and for a scene the intruder is modelled as a regular with local knowledge | "reasonably competent"; "curiosity (eg a local person's desire …)"; "one person or group knows a great deal about another person" | Standard (regulator) + Nightlife Culture | **Fixed** as a stance | ICO anonymisation guidance; Chapter 6 | stance |
| 10 | 5 | 697 | The disclosure floor is set per view, above the national rule where the scene can name the units, and stated; its value is a judgement scaled to sensitivity | "make a judgement call for other low counts, depending on the sensitivity"; online tools "stricter"; "A minimum cell count equal to five is suggested" | Standard (regulator) + Nightlife Culture | **Fixed** as a procedure; Adaptable in value | ONS births and deaths policy §4.2.2, §4.4; Chapter 6 | procedure + Adaptable part |
| 10 | 6 | 698 | The precision floor and the disclosure floor are two numbers for two objects, both stated; a count above the disclosure floor whose mean is below the precision floor is shown as a count, not a score | Fifty is a reliability rule; two, three, five and seven are identification rules | Standard + Reading | **Fixed** | ONS QMI; ONS births and deaths policy; this chapter §5 | unmarked |
| 10 | 7 | 699 | Suppression is primary and secondary, across every linked view; or a consistent cell key is used so the same cell shows the same way everywhere; the choice is declared | "additional cells will have to be suppressed (secondary suppression)"; "If a cell requires protection in one table then it will require protection in all tables"; "the same cell value and cell key" | Standard (regulator) + Standard (method) | **Fixed** as a procedure | ONS policy; Handbook on SDC; ONS Census 2021 methodology | procedure |
| 10 | 8 | 700 | Every floor is paired with a form that keeps the small present — a band, a presence mark, a held status — and a withheld cell is marked, never blank | "suppression rules disproportionately impact small population groups and small areas"; "Missing data is not the same as a zero value"; the brief's "aggregation of 'the biggest'" | Evidence + Standard + Nightlife Culture | **Fixed** | Abowd & Hawes; UKSA geospatial ethics; Chapter 4; the brief | unmarked |
| 10 | 9 | 701 | A rate or share whose underlying counts are small is treated as disclosive even if the counts are not published | "A rate or other statistic may be disclosive if it is possible to infer that the underlying counts contain small numbers" | Standard (regulator) | **Fixed** | ONS births and deaths policy | unmarked |
| 10 | 10 | 702 | Classifications readers may filter by are fixed; a reader-drawn boundary, reader-defined category or free time window is treated as a table builder and protected as one | "a set of standard classifications"; differencing "two or more overlapping tables and subtraction"; variable caps | Standard (regulator) | **Fixed** as a procedure | ONS policy; ONS Census 2021 table builder | procedure |
| 10 | 11 | 703 | An interactive view is protected as an online tool: either a limit on overlapping views with a request log (per user where readers register, per session where they do not) audited by a named person, or a consistent cell key with capped combinations; registration for deeper views where the studio chooses; controls "kept under review" | "generate multiple tables and potentially to attempt to breach confidentiality"; registration, log, "If possible, … a limit on the number of similar tables" | Standard (regulator) | **Fixed** as a procedure; Adaptable in parts | ONS births and deaths policy §4.4 | procedure + Adaptable part |
| 10 | 12 | 704 | Before release and at each data release, a friendly intruder who knows the scene walks the views for a bounded time; claims and confidences are recorded; a small number of low-confidence correct claims is the standard, not zero | "friendly intruders"; "around a half day"; "Each identification claim is given a percentage of confidence"; "a small number of correct claims with low confidence" | Standard (regulator) + Nightlife Culture | **Fixed** as a procedure | ONS intruder testing; version 1's filter walk | procedure |
| 10 | 13 | 705 | Hiding one field is not relied on as protection against repeated queries; the walk tests chosen positions, not single views | Trilateration succeeded with distance hidden: "up to the victim's building" | Evidence | **Fixed** | Hoang, Asano & Yoshikawa | unmarked |
| 10 | 14 | 706 | Differential privacy, if used, is used for what it protects — a person's participation — and never presented as protecting a group; its budget and its small-area cost are published | "It is the conclusions reached in the study that affect the smoker"; (kε, 0) for groups of size k; "systematically undercounts … mixed-race"; "aggregate small populations" | Evidence + Standard | **Fixed** as a stance | Dwork & Roth; Kenny et al.; US Census Bureau | stance |
| 10 | 15 | 707 | Synthetic data is for demonstration, test and download, never the face, and is released only where no "real or perceived risk of disclosure" remains | "it is not acceptable to release a synthetic dataset that could lead to a real or perceived risk of disclosure" | Standard (regulator) | **Fixed** | ONS synthetic data pilot | unmarked |
| 10 | 16 | 708 | Pseudonymised rows are treated as personal data; a hash is not anonymisation | "Pseudonymised personal data remains personal data"; "computing the 22M hashes took less than 2 minutes" | Standard (regulator) + Evidence (case) | **Fixed** | ICO; Pandurangan | unmarked |
| 10 | 17 | 709 | Every statutory citation in the record carries the date read and the version; the record is re-read against the current text on a stated schedule | Article 89 and s.19 omitted 5 February 2026; the regulator renamed 30 September 2026; guidance "under review" | Standard (law) + Practice | **Fixed** as a procedure | legislation.gov.uk; S.I. 2026/82; S.I. 2026/1015 | procedure |
| 10 | 18 | 710 | A lawful basis is recorded per purpose before collection; the house does not use consent as the basis for anything it will publish, taking as its reason the regulator's sentence on research — a stance, since the regulator's sentence is narrower and a consent basis with a declared cut-off is the funder's own practice | "If you would not be able to fully action a withdrawal of consent … you should not use consent as your lawful basis"; "no exemption to this for scientific research"; Art 8A(4) | Standard (regulator) + Standard (law) + Nightlife Culture | **Fixed** as a stance | ICO valid consent; UK GDPR Arts 7(3), 8A(4) | stance |
| 10 | 19 | 711 | Where legitimate interests is the basis, the three-part test is run and the assessment kept | "identify a legitimate interest; show … necessary; and balance it" | Standard (regulator) | **Fixed** as a procedure | ICO legitimate interests | procedure |
| 10 | 20 | 712 | Whether the research and statistics provisions fit is a question put to counsel and recorded as open until answered; the two exclusions are checked in terms | "substantial damage or substantial distress"; "measures or decisions with respect to a particular data subject"; "aggregate data that is not personal data" | Standard (law) | **Fixed** as a procedure | UK GDPR Arts 4(5), 84B, 84C | procedure |
| 10 | 21 | 713 | No panel infers a special-category characteristic about the people in a place unless an Article 9 condition, a DPIA and consultation are on the record; an onlooker's likely inference is written into the harm assessment as a fairness question | "regardless of how confident you are that the inference is correct"; "other people could (rightly or wrongly) infer" | Standard (regulator) | **Fixed** | ICO special category data | unmarked |
| 10 | 22 | 714 | Data about identifiable people taken from a platform or a public source carries Article 14's notice or a published reason, and the record says where it came from | "no automatic exception … just because the personal data is in the public domain"; "must take appropriate measures … including by making the information available publicly"; "lawful reason … even when it is publicly available" | Standard (law) + Standard (regulator) | **Fixed** | UK GDPR Art 14(5)–(7); ICO; ICO/Bonner 2023 | unmarked |
| 10 | 23 | 715 | The house does a DPIA for any dashboard that combines sources, re-uses public data, tracks location or behaviour, or profiles — the regulator requires one for the first and, combined with another criterion, for the others; it seeks the views of those affected or their representatives; it is published unless there is a stated reason | The regulator's high-risk list; "Where appropriate, the controller shall seek the views of data subjects or their representatives"; "good practice to publish" | Standard (law) + Standard (regulator) + Nightlife Culture | **Fixed** as a procedure | UK GDPR Art 35; ICO DPIA guidance | procedure |
| 10 | 24 | 716 | The site's own analytics count how the service is used, never who uses it, or run on consent | "It is about how your service is used, not about who uses it"; demographic segmentation "cannot rely on the statistical purposes exception" | Standard (law) + Standard (regulator) | **Fixed** | PECR Sch A1 para 5; ICO storage and access guidance | unmarked |
| 10 | 25 | 717 | The children's tests are applied and the evidence kept: more probable than not, and who actually uses the service | "more probable than not"; "based on evidence about who actually uses a service" | Standard (regulator, code) + Standard (law) | **Fixed** as a procedure | ICO Children's Code; UK GDPR Art 25(1A); OSA s.35 | procedure |
| 10 | 26 | 718 | A free dashboard is a service to the public under the Equality Act; every map has an accessible twin; a panel's rules are checked for particular disadvantage to a protected group | "for payment or not"; "provided in an accessible format"; "a particular disadvantage" | Standard (law) | **Fixed** | Equality Act 2010 ss.19, 20, 29 | unmarked |
| 10 | 27 | 719 | If the public can write what the public sees, the dashboard is run as a regulated service: a named accountable individual, a risk assessment within three months of launch, moderation, reporting and complaints routes, a written record | s.3(1); "services of all sizes"; "three months to complete a risk assessment"; the measures for all services | Standard (law) + Standard (regulator) | **Fixed** | Online Safety Act 2023; Ofcom | unmarked |
| 10 | 28 | 720 | A community is consulted, governs and agrees; it is never asked to consent, and no agreement by a community or its leaders is recorded as a person's consent | "should not be mistaken for community consent"; "In no case should a collective community agreement … substitute" | Standard (international) + Evidence | **Fixed** as a stance | UNESCO 2005 Art 6(3); CIOMS 2016; Dickert & Sugarman | stance |
| 10 | 29 | 721 | Consultation is tailored to the community and recorded with what it changed; the record names who it was reached through | "must be tailored to the communities"; gatekeepers "may also have other interests" | Evidence + Practice | **Fixed** as a procedure | Dickert & Sugarman; McAreavey & Das | procedure |
| 10 | 30 | 722 | Indigenous data-sovereignty frameworks are cited for their questions and structure and never adopted as the authority for a non-Indigenous community's claim; the house's layer carries the house's name | "specifically First Nations—not Indigenous"; "inherent rights to self-determination as sovereign entities"; "a normative foundation" | Practice + Reading | **Fixed** as a stance | FNIGC; Kukutai & Taylor; Carroll et al. | stance |
| 10 | 31 | 723 | "Less defined types of consent shall be balanced by stronger governance arrangements": a held layer is at the collaborate or empower level of the spectrum or it is not called community-held | "Less defined types of consent shall be balanced by stronger governance arrangements"; the five levels | Practice | **Fixed** as a stance | Te Mana Raraunga 5.2; Ada Lovelace Institute | stance |
| 10 | 32 | 724 | Withdrawal tiers, the cut-off and what cannot be undone are written before the first contribution and told at it | "cannot then be excluded"; "it would not be possible to remove data from research that had already taken place"; "as easy to withdraw as to give" | Standard + Practice + Standard (law) | **Fixed** as a procedure | ESRC; UK Biobank; UK GDPR Art 7(3) | procedure |
| 10 | 33 | 725 | A withdrawn item leaves a tombstone: identifier kept, content removed, reason stated; copies are not promised back | "the reason for the withdrawal will be indicated on a tombstone page"; "You cannot remove sensitive data from other users' clones" | Practice | **Fixed** as a procedure | Zenodo; GitHub Docs; Pro Git | procedure |
| 10 | 34 | 726 | The held layer is a declared status for a category, never a marker on a unit: present in a coarser count, decided by a named process, reason public, review date set, tested by the walk against public lists; it is drawn as held and never as empty | eBird, iNaturalist, NBN Atlas; "presumption in favour of disclosure" with a named harm; "Missing data is not the same as a zero value" | Practice + Standard (law, by analogy) + Nightlife Culture | **Fixed** as a stance | eBird; NBN Atlas; EIR 2004 reg 12; UKSA | stance |
| 10 | 35 | 727 | Holding is a decision and not a default: local and small-area data are not avoided because they carry risk | "should not necessarily be used as a rationale for avoiding local or small area data altogether" | Standard (regulator) | **Fixed** | UKSA geospatial ethics | unmarked |
| 10 | 36 | 728 | The harm assessment has three columns — persons, groups, places — and the place column asks about stigma, speculation, findability and the ecological fallacy for every panel | The regulator's list is individual; "blight a geographic area or community"; "stigmatisation"; "a leading indicator for housing price changes" | Standard (regulator) + Evidence + Nightlife Culture | **Fixed** as a procedure | ICO DPIA; UKSA; Aaronson et al.; Glaeser et al. † | procedure |
| 10 | 37 | 729 | No panel grades or ranks places, and where a value is drawn by colour the scale is checked for stigma; a money view is lit for a scene only after its governance has agreed, the speculation reading has been assessed, and both are on the record | The lending maps "led to reduced home ownership rates"; "impact on the community over the intentions of the designer" | Evidence + Practice + Nightlife Culture | **Fixed** as a stance | Aaronson et al.; Design Justice Network; Chapter 7 | stance |
| 10 | 38 | 730 | Colour and area are checked for stigma: no red or dark for low, no dominance of large empty areas, and "fewer" never drawn as "nothing" | "Red traditionally spells danger"; "Large areas … tend to dominate visually"; "Missing data is not the same as a zero value" | Standard (regulator) | **Fixed** | UKSA geospatial ethics; Chapter 3 | unmarked |
| 10 | 39 | 731 | Moderation is designed as verbs and adverbs before contributions open, with gating that prices rather than excludes where it can, and its uneven cost on who contributes is counted in the measure record | "excluding, pricing, organizing, and norm-setting"; "seven-in-ten"; "76% … made changes to the way they use the platforms" | Evidence + Practice | **Fixed** as a procedure | Grimmelmann; Pew 2021; Amnesty 2017 | procedure |
| 10 | 40 | 732 | The safety burden is designed in, not left to the user | "The burden of safety should never fall solely upon the user" | Practice (regulator framework) | **Fixed** as a stance | eSafety Commissioner | stance |
| 10 | 41 | 733 | A breach or a failure of protection is stated in public and addressed in public | "Be transparent about breaches of privacy and act publicly in addressing weaknesses" | Standard | **Fixed** | Code of Practice for Statistics 3.0, 4.4 | unmarked |
| 10 | 42 | 734 | The quotation rule applies to the dashboard as to the book: institutions are quoted; private persons are not identified by it or through it | The chapter's own method; the case reached only through a tertiary source | Nightlife Culture | **Fixed** as a stance | This chapter §18 | stance |
| 10 | 43 | 735 | After launch, the record's last line asks who benefited from being made visible and who paid, and answers with evidence | "unintended consequences"; "the mix and balance of extraction and empowerment"; consequences as validity evidence | Practice + Standard + Nightlife Culture | **Fixed** as a procedure | The Engine Room; Chambers (Chapter 9); AERA/APA/NCME (Chapter 9) | procedure |
| 11 | 1 | 463 | Every view carries a face sheet: the sentence, the pattern and first state, what of each record sits on the face, the nothings, the interactions and their costs, hover and pointer routes, the small-screen form, the state and its address, the snapshot and citation, words, map and colour, tests and review | The field describes dashboards and does not evaluate them; the surface must account for itself | Nightlife Culture + Practice | **Fixed** as a stance | This chapter §11; Sarikaya et al.; Bach et al. | stance |
| 11 | 2 | 464 | The first screen's sentence is written before the screen is designed; it answers the named reader's question and works with no interaction | Titles are visited first by two-thirds of readers in the one study; a title is remembered over its chart; most readers touch nothing optional | Evidence + Standard (design system) | **Fixed** | Sultanum & Setlur 2026; Kong, Liu & Karahalios 2019; ONS interactive charts; Chapters 1, 3 | unmarked |
| 11 | 3 | 465 | A dashboard is justified before it is built: a named reader, data updated often enough to revisit, a need for combination, and the resource to maintain it; otherwise charts with specific insights | "Only use a dashboard if you have clear justification"; "put the burden of interpreting and understanding data onto the user" | Standard (design system) | **Fixed** as a procedure | ONS dashboards; Analysis Function 2026 | procedure |
| 11 | 4 | 466 | The most important information comes first on every page, section and chart; chart titles state the trend; headings and titles within the official lengths, and within the house's shorter one where it applies | Inverted pyramid; "around 28% of content"; "15 words or fewer"; "fewer than 60 characters"; "65 characters or less" | Standard (design system) + Nightlife Culture | **Fixed**; the house limit Fixed as a stance | ONS content; GOV.UK content; Chapter 1 | unmarked + stance |
| 11 | 5 | 467 | The landing pattern is chosen from the six, named in writing, and the exemplar (if any) is declared an endorsement | No study compares the patterns; the first-shown view anchors | Reading + Evidence | **Fixed** as a procedure | Version 1 audit; Cho et al. (Chapter 3) | procedure |
| 11 | 6 | 468 | Nothing is asked of the reader before something is given: no configuration, registration or weighting before the sentence and a figure; a skippable guess offered after the sentence is not a toll | "shows the main message without needing any interaction"; a start point gives "just enough information" first; configuration-first taken up by one or two in a hundred | Standard (design system) + Evidence (case) | **Fixed** | ONS; GOV.UK start page; OECD BLI figures | unmarked |
| 11 | 7 | 469 | A search or place input sits beside content that already says something, never instead of it | Search adopted by two-thirds to four-fifths when offered beside a display; "deeply personal"; no evidence for a blank screen | Evidence (adjacent domain) | **Fixed** as a stance | Feng et al. 2018 | stance |
| 11 | 8 | 470 | The small screen is designed first; what is removed for it is recorded as not the message; no hover content is load-bearing | "Over half" (ONS) to "Two-thirds" (Analysis Function) arrive on a phone or tablet; "80% … do not scroll past the first quarter"; phone versions "remove content" and "removed the interactivity completely" | Standard (design system) + Evidence | **Fixed** | ONS; Analysis Function; Hoffswell, Li & Liu 2020; Kim, Moritz & Hullman 2021 | unmarked |
| 11 | 9 | 471 | On a phone, linear layouts and small multiples are the defaults over radial forms and animation | 2.8–5.4 s against 3.3–6.9 s; small multiples "consistently completed tasks in less time" | Evidence (adjacent domain) | Adaptable | Brehmer et al. 2019, 2020 |  |
| 11 | 10 | 472 | The authored account and exploration are both reachable from the first screen; neither is a toll on the other | "The reader is not forced to interact in order to learn"; the taxonomy's commonest structure may open on a default view; the null (secondary) | Practice + Evidence + Reading | **Fixed** as a stance | Victor 2011; Segel & Heer 2010; Boy et al. 2015 (secondary) | stance |
| 11 | 11 | 473 | Every written line links to the view that shows it, and every view to its line | Linking "significantly increased user engagement" and improved recall with the slideshow layout | Evidence (adjacent domain) † | **Fixed** as a procedure | Zhi, Ottley & Metoyer 2019 † | procedure |
| 11 | 12 | 474 | Text on the face is not treated as clutter: the title carries the trend, statistics and context sit by the point, and whatever an annotation carries is also in the text, because annotations may vanish on a phone | "heavily annotated charts were not penalized"; "Perceptual content … should be positioned in the title"; "Annotations may not display on mobile devices" | Evidence + Standard (design system) | **Fixed** | Stokes et al. 2023; Ajani et al.; ONS annotations | unmarked |
| 11 | 13 | 475 | A title never says what the chart does not show; where they would disagree, the chart is redrawn or the title rewritten | Readers recall the title's message and call the result neutral; the chart wins when the caption names a weak feature | Evidence | **Fixed** | Kong, Liu & Karahalios 2018, 2019; Kim, Setlur & Agrawala 2021 | unmarked |
| 11 | 14 | 476 | Generated sentences are built by rule from checked data, their topics ranked per place, checked by a person, labelled as generated, written in the house's voice, and aware of every series break they speak across | "not a labour-saving tool"; "all data are checked before publishing"; readability d = 2.8 against; the stock-split error | Practice (official) + Evidence | **Fixed** as a procedure | ONS 2023; Graefe 2016; Graefe & Bohlken 2020 | procedure |
| 11 | 15 | 477 | The "how this argues" page states the display's rhetorical positions — defaults, orderings, denominators, what is held — and is linked from every view; it is written for the reader who checks | Four editorial layers; "provenance rhetoric"; "Disclosing some of these decisions is a way to establish trust"; metadata changed thoroughness, not accuracy | Evidence + Reading + Practice | **Fixed** as a stance | Hullman & Diakopoulos 2011; Dörk et al. 2013; Burns et al. | stance |
| 11 | 16 | 478 | Every interaction names its purchase from the table and its costs from the seven, or is cut; the static reading works before it is added | "does not improve participants' accuracy … can significantly detract"; a required interaction cut completion and correct choice; seven costs | Evidence + Practice | **Fixed** as a procedure | Mosca, Ottley & Chang 2021; Zikmund-Fisher et al. 2011 †; Lam 2008 †; Decision Book Ch 7 | procedure |
| 11 | 17 | 479 | Guided tours and onboarding are not relied on to fix a first screen; a familiar form and a sentence are | No correctness difference with or without onboarding; readers skim the guide; "only useful once" | Evidence | **Fixed** as a stance | Stoiber et al. 2022; Sultanum & Setlur 2024 | stance |
| 11 | 18 | 480 | Nothing the majority of readers need is one step away; nothing one step away is hidden behind a control readers think will take them off the page; detail on request is two levels at most, with an obvious route | "some users avoid clicking the link"; "Do not use the details component to hide information that the majority of your users will need"; "beyond 2 disclosure levels typically have low usability" | Standard (design system) + Practice | **Fixed** | GOV.UK details, accordion, tabs; Nielsen 2006 | unmarked |
| 11 | 19 | 481 | Content on hover meets the three conditions (dismissible, hoverable, persistent) and is also reachable by keyboard focus; nothing is only on hover, because touch has no hover | SC 1.4.13 and its reasons; "not normally available on touchscreens"; "people using a touchscreen device may not use a physical keyboard" | Standard (W3C, AA) + Practice | **Fixed** | WCAG 2.2 1.4.13, 2.5.7; NN/g 2019; Decision Book Ch 15 | unmarked |
| 11 | 20 | 482 | Every control works by keyboard and by a single pointer without a path or a drag; maps have buttons for zoom and pan | SC 2.1.1 (A), 2.5.1 (A), 2.5.7 (AA) | Standard (W3C) | **Fixed** | WCAG 2.2 | unmarked |
| 11 | 21 | 483 | Targets are at least 24 by 24 CSS pixels, or have an equivalent control that is; dense data marks that must be smaller get an equivalent route — the table twin | SC 2.5.8 and its "interactive data visualization where targets are necessarily dense" exception, with "equivalent functionality through alternative means" | Standard (W3C, AA) | **Fixed** | WCAG 2.2 2.5.8; Chapter 8 | unmarked |
| 11 | 22 | 484 | A tooltip, where used, repeats what is at the mark or in the table, is spoken and keyboard-reachable, and is never the only place a value lives | The ONS's components; the ONS's exemption; no public design system has a tooltip component | Standard (design system) | **Fixed** | ONS chart components; ONS interactive charts | unmarked |
| 11 | 23 | 485 | Every reachable state has one canonical address that encodes the selection in a fixed order | "a URL that links to the current state"; "different parameter settings result in different URLs, and yet provide exactly the same visualization view"; 2,000 characters | Evidence + Practice | **Fixed** as a procedure | Heer, Viégas & Wattenberg 2007; Shiny docs | procedure |
| 11 | 24 | 486 | Every state can be frozen as a dated, unchanging snapshot of its data and text — at each release at least, and on request or on share — findable from the live view and linking previous, next and live; the citation is generated and carries the address with its selection, the snapshot date, the data version and the retrieval date | Links rot; content drifts; "Interactive content usually cannot be archived"; "timeslice, version and/or granular portion"; R1–R14; OWID's archived citations | Standard (community) + Evidence + Practice | **Fixed** as a procedure | FORCE11 2014; RDA WGDC 2015; Jones et al. 2016; The National Archives; Our World in Data 2025 | procedure |
| 11 | 25 | 487 | Data are versioned and timestamped; a correction is announced at the top of the affected view with when and why; a retired view keeps its address under a dated banner; statistics are never silently replaced | ONS versions and corrections policy; "Correction of errors are reported at the top of the affected release"; "withdraw the content - this keeps the content on the site" | Standard (regulator; design system) | **Fixed** | ONS revisions policy; GOV.UK publisher guidance | unmarked |
| 11 | 26 | 488 | A cropped or shared copy carries the stamp, the floor note, the unit and the snapshot date | The share is the state's afterlife; the data dump is the commonest use | Nightlife Culture + Evidence | **Fixed** | Version 1 crop test; Tory et al. 2021 | unmarked |
| 11 | 27 | 489 | Every view declares the data version, the specification version and the selection it was built from, and a degraded state is a state with an aged data version | "independent from the other components"; "unit := (data, transforms, mark-type, encodings)"; "re-evaluated as selections change" | Standard (method) + Reading | **Fixed** as a procedure | Wickham 2010; Satyanarayan et al. 2017; Chapter 8 | procedure |
| 11 | 28 | 490 | The records' kinds sit on the face as statuses in text that open the record; a source line is followable, not only present | Metadata read as "more thorough" without accuracy; a source line "suggests that there may be no need for the user to check"; beauty trusted via inferred competence | Evidence + Reading | **Fixed** as a stance | Burns et al.; Kennedy et al. 2016; Lin & Thornton †; Chapter 4 | stance |
| 11 | 29 | 491 | A cell not shown is marked, explained by kind, and never blank; nothing is imputed into a withheld cell; a series is never joined across a gap; the maker expects, and does not design away, the lower confidence a shown gap produces against a dropped one | Dropping the gap was the most biased and the most confident; an explained empty cell beat a blurred one for confidence and raised risk-taking; "Do not join the points" | Evidence + Standard | **Fixed** | Sarma et al. 2022; Andreasson & Riveiro 2014 †; Analysis Function; Chapters 4, 10 | unmarked |
| 11 | 30 | 492 | A felt distribution and a funnel carry their reading in their title and their band and n in words beside the shape | The public has no schema for either; a distribution is a slow glance | Reading | **Fixed** as a stance | Chapters 3, 7, 9 | stance |
| 11 | 31 | 493 | A choropleth shows rates, never counts; its breaks are declared and, "when possible", held constant across every view of the same measure; its legend is matched | "standardised rates, not absolute values"; "matched legends across series … increased map-comparison accuracy by approximately 28 percent" | Standard (design system) + Evidence † | **Fixed** | ONS choropleth maps; Brewer & Pickle 2002 † | unmarked |
| 11 | 32 | 494 | Breaks by quantile unless a declared reason; five bands | Quantiles best in the one controlled test; the design system's default is natural breaks | Evidence † + Standard (design system) | Adaptable | Brewer & Pickle 2002 †; ONS |  |
| 11 | 33 | 495 | Small areas are given size — an inset, a tile form or a second view — and the map's sentence says what the darkest shape means | "small areas were missed by approximately 30–40% of map users"; 93 per cent chose the darker map without a legend and about half with one; the remedy is the chapter's, since the study endorses none | Evidence + Reading | **Fixed** as a stance | Schiewe 2019 | stance |
| 11 | 34 | 496 | Cartograms are used knowingly: contiguous over rectangular, and never as the only map, since a choropleth with circles beat them in the one head-to-head | "Rectangular cartograms are a clear outlier"; "choropleth/graduated circles are more effective" (secondary) | Evidence + secondary | Adaptable | Nusrat, Alam & Kobourov 2018; Nusrat & Kobourov 2016 |  |
| 11 | 35 | 497 | The stigma check runs on every map before publication: no red or dark for low; large empty areas do not dominate; missing is not zero; the held category is coarsened | Chapter 10's rules; dark-is-more measured | Standard (regulator) + Evidence | **Fixed** | UKSA (Chapter 10); Schiewe 2019 | unmarked |
| 11 | 36 | 498 | Two tests are run on every first screen. The two-readers test: one reader given the authored account alone and one the views alone, each asked what the place is like. The three-phones test: a reader of each user group asked, on their own phone, what the dashboard says, which figure it rests on and what they would do next | The field's test gap; the design systems' "test with users" | Nightlife Culture + Standard (design system) | **Fixed** as a procedure | Version 1 Ch 10; DSH-12 | procedure |
| 11 | 37 | 499 | The dashboard measures its own use as how, not who; publishes it aggregate and dated; and reads "those who interacted did better" with the confound named | "not about who uses it"; publishers "unwilling to share internal metrics"; "an artifact of participant engagement, or an effect of interacting" | Standard (law) + Evidence + Nightlife Culture | **Fixed** as a stance | Chapter 10; Hohman et al. 2020; Mosca et al. 2021 | stance |
| 11 | 38 | 500 | A dashboard has a retirement plan: a banner six months ahead, the state preserved, data and metadata kept and marked, code archived in public | The lifecycle's fifth stage; every stated cause of a retirement read was supply-side | Standard (design system) + Evidence (cases) | **Fixed** as a procedure | Analysis Function 2026; Chapter 8 | procedure |
| 11 | 39 | 501 | Scrollytelling and other editorial forms sit above the dashboard, carry its states and snapshots, and are priced as unevaluated for comprehension | Recall equal to video and worse than text per second; scroller v stepper no difference; "it doesn't hide content" | Evidence + Practice | Adaptable | Schneiders 2020; McKenna et al. 2017; The Pudding 2017 |  |
| 12 | 1 | 446 | Every figure about a place states its unit, the unit's vintage, and what the unit hides | No official unit was designed around recognition; the unit can change the finding | Standard (ONS) + Evidence | **Fixed** | ONS geography pages; Flowerdew; Decision Book geography rules | unmarked |
| 12 | 2 | 447 | The landing unit is a declared choice; the administrative unit is shown beside it | The reader's officer, funder and councillor live in the administrative unit | Reading | **Fixed** as a stance | Section 3; Chapter 11 | stance |
| 12 | 3 | 448 | A place with no administrative edge is shown as a core and bands of agreement, with the number of people whose agreement it is | People judge membership of a vague region and disagree about its edge | Evidence + Practice | **Fixed** as a procedure | Montello et al.; Bostonography | procedure |
| 12 | 4 | 449 | Where residents' or a scene's own units are gathered, the prompt, the sample and the consensus rule are published | The drawn unit was a sixth of the programme's target area and varied by place | Evidence | **Fixed** as a procedure | Coulton, Chan & Mikelbank | procedure |
| 12 | 5 | 450 | A reader may draw their own unit, subject to the query-time walk | The official body already allows it | Practice + Chapter 10 | Adaptable | ONS custom area profile |  |
| 12 | 6 | 451 | Comparisons across boundary vintages carry an explicit lookup | Best-fit carries error | Standard (design system) | **Fixed** | Decision Book; ONS best-fit | unmarked |
| 12 | 7 | 452 | The reader's place is found first and by a name people use | Readers judge a chart by whether they find home in it | Evidence (interviews) | **Fixed** as a stance | Peck, Ayuso & El-Etr; ONS 331 | stance |
| 12 | 8 | 453 | The missed column is shown first, as a declared endorsement, and never alone | The first thing shown is read as an endorsement; no evidence speaks to the order of two true columns; assets sit beside needs, never instead | Reading + Nightlife Culture | **Fixed** as a stance | Chapter 11; GCPH; house principle | stance |
| 12 | 9 | 454 | "Never repeat the opposing frame" is not a reason for any layout | The familiarity backfire effect is not robust; frame strength decides, not count; the corrections literature tests belief, not frames, so the mechanism is weakened rather than refuted | Evidence | **Fixed** | Lewandowsky et al.; Swire-Thompson et al.; Chong & Druckman | unmarked |
| 12 | 10 | 455 | Both columns get the same type scale, chart quality and space | Space and finish are read as importance | Reading | **Fixed** as a stance | Decision Book LAY-08; Wood et al. | stance |
| 12 | 11 | 456 | Every hole in either column is rendered at full size with its kind named by symbol and in words | A gap drawn over reads as data; the shorthand exists; whether an unlabelled gap reads as less value is a reading | Evidence + Standard (Analysis Function) + Reading | **Fixed** | CALVI; Analysis Function symbols; Chapter 11 | unmarked |
| 12 | 12 | 457 | The missed column shows its intervals, samples and bands | Quantified uncertainty has only positive or null effects on credibility | Evidence | **Fixed** | Gustafson & Rice; van der Bles et al.; Chapter 9 | unmarked |
| 12 | 13 | 458 | Two unlike measures never share an axis, and the cost of separate panels is accepted | The standard does not recommend dual axes; the house makes that a bar; juxtaposition almost never wins for precise comparison | Standard (Analysis Function) + Reading | **Fixed** as a stance | Analysis Function; Few; L'Yi, Jo & Seo | stance |
| 12 | 14 | 459 | The bridging sentence says one thing from each column and no relation the data do not hold | No guidance exists; the worded-comparison rule is the model | Reading | **Fixed** as a procedure | ELS QMI; poster rule | procedure |
| 12 | 15 | 460 | Identity fields are never ranked, and the data contract records which fields are identity | Scale type follows the question; the house declares its question | Evidence of method + Nightlife Culture | **Fixed** as a stance | Velleman & Wilkinson; house axiom | stance |
| 12 | 16 | 461 | A profile is small multiples of linear marks in a fixed, stated axis order, never a filled area; the form is held open to test | Radar read worst and the flower chart was preferred, in abstracts; filled area is a ranking by an arbitrary order; linear read best in the one full study, on one series | Evidence † | **Fixed** as a stance, form Adaptable | Albo et al. †; Feldman †; Waldner et al.; Javed et al. † | stance + Adaptable part |
| 12 | 17 | 462 | Any label for a place or type is written without blame — literal, not pejorative, neither negative nor positive, naming what happened to an area — and carries the per-place hedge | The classifier's published naming rule, and its own output's limit | Standard (official statistics) + Evidence of method | **Fixed** as a procedure | Gale et al.; ONS classification pages | procedure |
| 12 | 18 | 463 | Conditions are shown as conditions with numbers, never folded into a type's name | A label for a condition cannot be neutral | Reading | **Fixed** as a stance | Section 6 | stance |
| 12 | 19 | 464 | Every cross-place condition chart carries the gate's status, the harmonised criteria and the wording rule inside its frame | Comparability is a quality dimension producers must state; the frame is what travels | Standard (law) + Standard (regulator) + Standard (design system) | **Fixed** | ESS Code P14; Code 3.0 6.6–9.3; Style Guide §12 | unmarked |
| 12 | 20 | 465 | Each condition on its own spread, the place marked, the comparison worded by a published threshold | The official service's form | Practice (official) | **Fixed** as a procedure | ELS QMI; Chapter 7 | procedure |
| 12 | 21 | 466 | Incomparable conditions are not added; the sentence says ahead-on-this, behind-on-that | Adding them is Chapter 5's composite by another name; the diagrams that show partial orders are hard to read | Reading + Evidence † | **Fixed** as a stance | Chapter 5; Fattore †; Annoni & Brüggemann † | stance |
| 12 | 22 | 467 | The advocacy sentence passes through the gate and names its peer by method | Its first half is a comparison | Reading | **Fixed** | Section 6; Chapter 7 | unmarked |
| 12 | 23 | 468 | No ordering the house makes in discovery is by size or popularity | A sorted list concentrates exposure and changes what it sorts | Evidence | **Fixed** | Singh & Joachims; Salganik, Dodds & Watts; Abdollahpouri et al. | unmarked |
| 12 | 24 | 469 | A match is made from the reader's weights or nearness, shows the weights, and exists only on request | The careful tools show only the reader's own ordering, behind the reader's choice | Practice + Reading | **Fixed** as a stance | ELS; Discover Uni | stance |
| 12 | 25 | 470 | Every match shows its why as content cues, never as social proof | Content cues enable accurate assessment; neighbour cues inflate by 0.74 | Evidence | **Fixed** | Bilgic & Mooney; Tintarev & Masthoff | unmarked |
| 12 | 26 | 471 | Explanations are tested for decision quality, not liking | Personalisation raised satisfaction and hurt effectiveness; the founding study found no decision gain | Evidence | **Fixed** | Tintarev & Masthoff †; Herlocker et al. | unmarked |
| 12 | 27 | 472 | An adjacency row is a probe, not a rule, and is measured | Novelty lowered satisfaction; the filter bubble is unsupported | Evidence | Adaptable | Ekstrand et al. 2014; Arguedas et al. |  |
| 12 | 28 | 473 | Whether a kind of place is findable is a status of the category, set with the forum, recorded in the safeguards record, never a marker on a named room or business | Chapter 10 retired consent to be found | Reading (Chapter 10) | **Fixed** | Chapter 10; opt-in directories as precedent only | unmarked |
| 12 | 29 | 474 | The Form 696 test is run with the walk before any category is made findable | Findable to audiences is findable to enforcement | Nightlife Culture (Carly's frame) + Chapter 10 | **Fixed** as a procedure | Version 1; Chapter 10 | procedure |
| 12 | 30 | 475 | The money view says that a gap in grants data is also a gap in publishing | The data are what was published | Reading | **Fixed** | 360Giving pages; Section 7 | unmarked |
| 12 | 31 | 476 | Any "absence made visible" method publishes its weights, its standardisation and its judgement steps | The official method is a composite with staff scoring inside | Standard (method) | **Fixed** | Arts Council England 2021; Chapter 5 | unmarked |
| 12 | 32 | 477 | Every chart carries, inside its frame, title, unit, source, base, address and snapshot date, for comparisons the gate and wording, and for either column the bridging sentence; the page text repeats them | Charts travel as screenshots; context beside the frame is cropped; a cropped counted panel must still say what sat beside it | Evidence + Reading | **Fixed** as a stance | Lisnic et al. 2023, 2025; Decision Book DAT-18, DAT-21, TBL-17; Chapter 11 | stance |
| 12 | 33 | 478 | The departure from official practice on text in images is made in addition to page text, never instead | The standard's reason is accessibility; the house keeps the accessible route and adds the frame | Standard (Analysis Function) + Reading | **Fixed** as a procedure | Analysis Function; GOV.UK; Chapter 13 | procedure |
| 12 | 34 | 479 | No screen carries an ordered all-places list | The thing most easily cropped into a verdict | Reading | **Fixed** as a stance | Version 1; Chapter 7 | stance |
| 12 | 35 | 480 | Any rank the house ever lets out carries the official wording: ordinal, relative, no distance | The bodies that publish ranks say so | Standard (official statistics) | **Fixed** | IoD2025; SIMD; ONS well-being QMI | unmarked |
| 12 | 36 | 481 | Every place-page is shown to people from the scene before publication, in a form chosen with them; what was said and what changed is recorded by role, never by name; the page says it was reviewed | The house's own test; the one recorded harm of member checking is the unanswered portrait | Nightlife Culture + Practice | **Fixed** as a procedure | Style Guide slides; Candela; Data Walks; CBPR principle 7 | procedure |
| 12 | 37 | 482 | Every place-page keeps a standing errors channel and dates its corrections | The nearest UK case of a statistical unit made recognisable did it this way | Practice | **Fixed** as a procedure | MSOA Names; Chapter 11 | procedure |
| 12 | 38 | 483 | Harm through a place's representation is assessed as Chapter 10 requires, in proportion, with the measured size of the penalty stated beside the theory | The one field experiment reached found a small, non-significant penalty against a large theoretical literature | Evidence | **Fixed** | Tunstall et al.; Wacquant; Chapter 10 | unmarked |
| 12 | 39 | 484 | The recognition record, ten lines, sits beneath every place-page | Nine records now; whether one document is for the end | Reading | **Fixed** as a procedure | This chapter | procedure |
| 12 | 40 | 485 | How the holes are drawn; how the columns are composed; the profile's visual language | Open, within the rules above | — | *Decorative* | Chapter 14 of this book |  |
| 13 | 1 | 409 | One page per layout; the accessible routes are supplementary content on it; no parallel accessible version | A page conforms whole or not; an alternate version is the standard's fallback | Standard (W3C) | **Fixed** | Understanding Conformance | unmarked |
| 13 | 2 | 410 | The phone layout conforms as a page in its own right | "A full page includes each variation … for various screen sizes" | Standard (W3C) | **Fixed** | Conformance requirement 2 | unmarked |
| 13 | 3 | 411 | Every chart has a short description that identifies it and a long description, in body text, carrying its statistics and trend, with the data in a table where practical | 1.1.1's own chart example; G92; what blind readers rank most useful | Standard (W3C) + Evidence | **Fixed** | Understanding 1.1.1; G92; Lundgard & Satyanarayan | unmarked |
| 13 | 4 | 412 | The long description is two to eight plain sentences generated from the current state by a published rule and read by a person against the figures; it is never duplicated in an alt attribute | Interviews; audit of alt texts; the anchoring finding; "auditory clutter" | Evidence + Standard (official statistics) | **Fixed** as a procedure | Jung et al.; Chintalapati et al.; Mack et al.; Analysis Function | procedure |
| 13 | 5 | 413 | The chart's description carries the chart and not the author's interpretation; interpretation lives in the authored account on the page, read by everyone | Blind readers emphatic against interpretation in the description; sighted readers rank it highly; both read the account | Evidence + Reading | **Fixed** as a stance | Lundgard & Satyanarayan; Chapter 11 | stance |
| 13 | 6 | 414 | Every view has a native HTML table twin with header cells, paginated and keyboard-sortable, the figures reachable before any script | The type most often rated accessible; the official fallback; the APG prefers native tables | Evidence + Standard (W3C) + Chapter 8 | **Fixed** | Fan et al.; APG; Analysis Function | unmarked |
| 13 | 7 | 415 | A map's twin is joined by a sentence for the shape and the statement says the twin does not carry geography | Tables lost to a text map on geographic questions | Evidence (one preprint) | **Fixed** as a procedure | Biggs et al.; Chapter 11 | procedure |
| 13 | 8 | 416 | A navigable structure is built on graphics-document and native roles, never invented ARIA; tested with named screen readers before release | "A role is a promise"; "No ARIA is better than Bad ARIA"; ARIA pages carry more errors | Standard (W3C) + Evidence | **Fixed** | APG; Graphics Module; WebAIM Million | unmarked |
| 13 | 9 | 417 | The structure is built after the description and the table, and tested against them | The one study's table was easier than its richest prototype | Evidence | Adaptable | Zong et al. |  |
| 13 | 10 | 418 | Each line, slice or mark that carries meaning has 3:1 contrast unless labels carry the same information | 1.4.11's chart cases | Standard (W3C) | **Fixed** | Understanding 1.4.11 | unmarked |
| 13 | 11 | 419 | Colour is never the only carrier; legends match by more than colour | 1.4.1; declared in most of the dashboard statements read | Standard (W3C) + Practice | **Fixed** | Chapter 3; UKHSA; PHS; Analysis Function | unmarked |
| 13 | 12 | 420 | Chart text is text: SVG or HTML, never canvas; resizable to 200 per cent and respaceable | 1.4.4; 1.4.12 "canvas implementations of text are considered to be images of text" | Standard (W3C) | **Fixed** | Understanding 1.4.4, 1.4.12 | unmarked |
| 13 | 13 | 421 | The frame's identifying text (title, unit, source, base, address, date; gate and wording on comparisons) is drawn as SVG text on the page, repeated as HTML beside the chart, and baked into the export; never the image alone | 1.4.5 is met "where both are presented to the user"; the one declared failure was a title in the image only | Standard (W3C) + Practice | **Fixed** as a procedure | Understanding 1.4.5; PHS statement; Chapter 12 | procedure |
| 13 | 14 | 422 | Everything is operable by keyboard with no trap; focus visible, sized and contrasted to 2.4.13, and never covered by the filter bar | 2.1.1, 2.1.2, 2.4.7, 2.4.11, 2.4.13 (AAA, adopted); the first and third commonest public failures | Standard (W3C) + Evidence | **Fixed** (2.4.13 as a stance) | Understanding pages; GDS monitoring | stance |
| 13 | 15 | 423 | Nothing fires on mouse-down; every drag has a single-pointer alternative; targets 24 px or the table twin | 2.5.2, 2.5.7, 2.5.8 | Standard (W3C) | **Fixed** | Understanding pages; Chapter 11 | unmarked |
| 13 | 16 | 424 | Auto-updating views can be paused; moving content that lasts more than five seconds can be stopped | 2.2.2, which applies regardless of conformance | Standard (W3C) | **Fixed** | Understanding 2.2.2 | unmarked |
| 13 | 17 | 425 | The reduced-motion preference is honoured and motion from interaction can be disabled | 2.3.3's vestibular reason, adopted though AAA | Standard (W3C) | **Fixed** as a stance | Understanding 2.3.3; C39 | stance |
| 13 | 18 | 426 | Content reflows at 320 CSS pixels; only the map and the table are excepted, not their headings or controls | 1.4.10 and its limit | Standard (W3C) | **Fixed** | Understanding 1.4.10 | unmarked |
| 13 | 19 | 427 | A filter changes content, not context; one polite status message says what changed; the view is never announced | 3.2.2; 4.1.3; "too 'chatty'" | Standard (W3C) | **Fixed** | Understanding 3.2.2, 4.1.3; ARIA22 | unmarked |
| 13 | 20 | 428 | Numbers are reinforced with words; each step carries what the last knew; uncommon terms are explained within one click; the "how this argues" page has a lower-secondary summary | COGA's patterns, specific where WCAG is silent | Standard (W3C), informative | **Fixed** as a stance | COGA; Chapters 7, 9, 11, 12 | stance |
| 13 | 21 | 429 | Body type is a sans serif at a size between the two measured figures, the choice recorded; no font designed for dyslexia is relied on | Sans serif, monospaced and roman read better; the dyslexia fonts neither helped nor hindered in three studies; 18 point against 12–14 | Evidence | **Fixed** as a stance | Rello & Baeza-Yates; Rello, Pielot & Marcos; Kuster; Wery & Diliberto | stance |
| 13 | 22 | 430 | No overlay widget | Practitioners rate them ineffective; a regulator's order against one vendor's claims | Evidence + Practice | **Fixed** | WebAIM 2021; FTC 2025; Overlay Fact Sheet | unmarked |
| 13 | 23 | 431 | The house publishes an accessibility statement in the public sector's model form with the twelve lines, per view, dated within twelve months | It is the chapter's record and what a public body's own statement can point to; the model is the regulator's form, adopted | Standard (regulator) as a model | **Fixed** as a procedure | Reg 8; model statement; Section 11 | procedure |
| 13 | 24 | 432 | Non-compliances are declared by criterion in the public sector's form, with the route around each | The public sector's own practice; "statement of non-conformance" | Standard (W3C) + Practice | **Fixed** as a procedure | Understanding Conformance; PHS | procedure |
| 13 | 25 | 433 | The house claims no disproportionate burden, and never on time, knowledge or priority | The public sector's own exclusion, adopted as a house line | Standard (regulator), adopted | **Fixed** as a stance | GOV.UK | stance |
| 13 | 26 | 434 | Tooling is chosen against these rules in week one | Canvas and closed tools cannot be retrofitted; official statements name the tools | Reading + Practice | **Fixed** | Analysis Function software page; version 1 | unmarked |
| 13 | 27 | 435 | Chartability's critical heuristics before every release; a full pass per major release | Two to eight hours; evaluated on auditors' confidence, so not instead of the walks | Practice | **Fixed** as a procedure | Elavsky et al. | procedure |
| 13 | 28 | 436 | A scan, the three walks and the question before every release: scanner for contrast and the 30–40 per cent; keyboard; zoom on the phone layout; screen reader with pass criteria; a blind reader asked for the trend, the figures and, on a map, where | The failures found by hand and by scanner; what blind readers want asked | Evidence + Reading | **Fixed** as a procedure | GDS monitoring; Lundgard & Satyanarayan | procedure |
| 13 | 29 | 437 | Observed testing includes disabled readers of the real audience | "user research must include disabled people"; "User testing should be carried out" | Standard (design system) + Standard (W3C) | **Fixed** | GOV.UK Design System; Understanding 4.1.3 | unmarked |
| 13 | 30 | 438 | Audio is a labelled extra after the description and the table; recorded sound on a page, if any, is content and not a route to a figure | Point estimates with training; unfamiliar; of limited value for maps | Evidence | Adaptable | Walker & Nees; Sharif et al. 2025 |  |
| 13 | 31 | 439 | The distribution argument is recorded once, as funding and reputation | Reg 4(2)(e); the three statements | Reading of law | **Fixed** as a procedure | Section 4 | procedure |
| 13 | 32 | 440 | The law is cited by section with its date, and never as advice | The chapter's own rule | Nightlife Culture | **Fixed** | Section 4 | unmarked |
| 13 | 33 | 441 | How the routes look and sound; the reduced-motion page; the structure's narration style | Open, within the rules above | — | *Decorative* | Chapter 14 of this book |  |
| 14 | 1 | 492 | Sort every element into a layer, then run the removal test on every expressive one — mono, silent, still, undressed — and the fifth check: stripped and dressed say the same thing | Expressiveness is "all the facts" and "only the facts"; a lost fact is a wrong sort, an added fact is a false fact | Standard (method); Reading | **Fixed** (procedure) | Mackinlay 1986; Kosara 2007; W3C 1.1.1; AF infographics; ONS animations; AF §10 | procedure |
| 14 | 2 | 493 | Record each element in the boundary log, eleven lines, before it ships | An unlogged break is indistinguishable from negligence at the next audit | Nightlife Culture | **Fixed** (procedure) | Decision Book Ch 18; this chapter | procedure |
| 14 | 3 | 494 | Name the purchase in the affective-intent template, limited to what expression is measured to buy | Engagement, mood and recognition are measured, and memorability in Chapter 3; empathy, giving and accuracy are not | Evidence; Evidence of method | **Fixed** (stance) | Lee-Robbins & Adar 2022; Boy 2017; Morais 2021; Kineticharts; Arunkumar 2023 | stance |
| 14 | 4 | 495 | The precise twin is one step away and the form states its finding, and any distortion, in words on itself | A twin beside a form is not thereby read | Evidence; Practice | **Fixed** (procedure) | Ottley 2019; Decision Book Ch 7; Fanning & Raworth 2025 | procedure |
| 14 | 5 | 496 | Humanised marks are whole units and are never priced as buying empathy or action | A sliced person encodes a fraction the data does not say; the measured effect on a hypothetical allocation is at best about 3 in 100 | Evidence; Practice; Reading | **Fixed** | FT Visual Vocabulary; Boy 2017; Morais 2021; Correll 2019 | unmarked |
| 14 | 6 | 497 | A dark register ships with a light one and the reader's choice is honoured | Positive polarity advantage in both age groups at small sizes; chart polarity individual; the floor already carries user override | Evidence | **Fixed** (procedure) | Piepenbrock 2013; Dobres 2017 †; While & Sarvghad 2024; AF colours; Chapter 13's floor | procedure |
| 14 | 7 | 498 | A drawn or approximate register is worn only where the data is imprecise, and says so | Sketchiness works as an uncertainty cue | Evidence †; Practice | Adaptable | Boukhelifa 2012 †; Chalabi interviews |  |
| 14 | 8 | 499 | Mood is carried only in channels that encode nothing | Palette moved feeling more than the data's trend did | Evidence | **Fixed** | Blair 2024; Bartram 2017; Anderson & Robinson 2022 † | unmarked |
| 14 | 9 | 500 | Any sound that is content has a text document; captions include non-speech sound; nothing autoplays beyond three seconds without a stop | Level A | Standard (W3C) | **Fixed** | WCAG 1.2.1; 1.2.2; 1.4.2 | unmarked |
| 14 | 10 | 501 | A specific sensory experience is identified in words, never ignored | The standard's third category | Standard (W3C) | **Fixed** | WCAG 1.1.1 | unmarked |
| 14 | 11 | 502 | The conventions of objectivity are earned by the records beneath them; a source line points to a reachable source | The source line "performs the rhetorical, persuasive work of ascribing transparency" | Evidence of method; Reading | **Fixed** (stance) | Kennedy et al. 2016; Chapters 4–7 | stance |
| 14 | 12 | 503 | Never make the evidence layer harder to read on purpose | Disfluency: recall d = −0.01; slower; less confident | Evidence | **Fixed** | Xie et al. 2018; Weissgerber 2024 †; Hullman 2011 (the proposal) | unmarked |
| 14 | 13 | 504 | A headline read in passing has its letter height set from the distance it is read at, and its finding restated in the body text at arm's length | The legibility index; three or four words a glance | Standard (method); Evidence | **Fixed** (procedure) | USSC 2015; Bullough 2017; Garvey 2016 | procedure |
| 14 | 14 | 505 | Short headlines; the count is the house's | The mantra; the measured numbers are distance, seconds and glance | Nightlife Culture | Adaptable | Version 1 Ch 13; the sign literature |  |
| 14 | 15 | 506 | The display's genre is the house's to choose; the evidence layer passes the removal test in any genre | Prototypicality is about speed of judgement; unfamiliar forms cost glances and liking | Reading | Adaptable | Chapter 11; Kennedy focus groups; Blascheck 2019 |  |
| 14 | 16 | 507 | No form is invented without a glance-cost estimate and a plan to measure it | One radial form took about six times a bar's glance, in one study | Evidence | Adaptable | Blascheck 2019 |  |
| 14 | 17 | 508 | Audit accuracy, then the floor, then beauty; beauty is never a licence | The field's prize has no accuracy criterion; the regulator's casework is about encodings, sources and context | Practice; Standard (regulator) | **Fixed** (stance) | IIB FAQ; OSR casework; Code 3.0 9.2 | stance |
| 14 | 18 | 509 | Probes meet the evaluated exception's standard and add a comparison | Logs plus survey, open materials, behaviour against self-report; no control | Evidence of method | Adaptable | Pomerance, Boyd & Dörk 2026 |  |
| 14 | 19 | 510 | Everything else in the register — palette beyond the encoding, display type, illustration, pattern, imagery, pacing, the poster layer, stoppable sound, disableable motion | Free, under the rules above | — | *Decorative* | Decision Book Ch 18 |  |
| 15 | 1 | 494 | Measure trust, if at all, with a fixed question in waves, of those able to express a view; never report an on-site percentage as trust | Producers' trust is measured this way; displays' almost never; the self-selected figure has no n | Evidence; Reading | **Fixed** (procedure) | PCOS 2021, 2023; Charity Commission 2025, 2026; UKHSA blog 2021 | procedure |
| 15 | 2 | 495 | Every metric has a documentation page with fixed headings — definition, rationale, method, caveats, source, frequency, date — and, where it has them, numerator, denominator and polarity | A reader can check what a figure is before reading it; the regulator lists sources, status, limitations and update schedule as the minimum | Practice; Standard (regulator) | **Fixed** (procedure) | UKHSA; Fingertips; ELS QMI; OSR 2025 | procedure |
| 15 | 3 | 496 | Keep a dated, labelled change log apart from the refresh, with issue and resolved paired | A reader can see what changed when and why; the dashboard teams' lesson, under trust, was to disclose errors as they happen | Practice; Evidence of method | **Fixed** (procedure) | UKHSA "What's new"; Barbazza 2021 | procedure |
| 15 | 4 | 497 | Keep the house's own errors in a machine-readable errata file and its sources' revisions in a dated list with reasons | A reader can tell whose mistake moved a figure; no reader evidence, so a bet with a small cost | Practice | **Fixed** (procedure) | JHU README (read once) | procedure |
| 15 | 5 | 498 | A revision is a scheduled change; a correction is labelled as a correction; print the typical revision's size once it can be computed | The ONS's distinction and practice | Standard (official statistics) | **Fixed** (procedure) | ONS revisions policy; GDP first estimate 2026 | procedure |
| 15 | 6 | 499 | Keep every published data file as a dated vintage from the first release | Results change when figures do; it cannot be started later | Practice; Evidence | **Fixed** (procedure) | ALFRED; Croushore & Stark 2001 | procedure |
| 15 | 7 | 500 | Draw a late-returns series by event date; state the incompleteness window on the metric's page; mark it on the chart with the direction of bias; keep the by-publication series labelled as not a trend | The documented answer to the tail that looks like a fall | Practice | **Fixed** (procedure) | PHE 2020; UKHSA documentation and log | procedure |
| 15 | 8 | 501 | Colour a value as a judgement only when it is significantly different from a named comparator; a neutral colour by default; a neutral ramp where there is no good direction; print the one-in-twenty sentence | A colour is read as a verdict; the RAG guide's rule and its warning that one in twenty is chance | Standard (official statistics) | **Fixed** (procedure) | PHE RAG guide 2017; OHID technical guidance | procedure |
| 15 | 9 | 502 | Draw an arrow only under a printed rule — independent points, a stated test, a robustness check — dated where the arrow is; otherwise no arrow, with the reason | An arrow is a claim about a trend; rules that live elsewhere get lost | Standard (official statistics); Practice | **Fixed** (procedure) | Fingertips trend markers; OECD user guide; Wales 2026; Scotland's redirects | procedure |
| 15 | 10 | 503 | Show uncertainty as a range beside a point; never a verbal hedge alone | Ranges cost little or no trust; hedges did little for understanding | Evidence | **Fixed** (procedure) | van der Bles 2020; Galvão & Mitchell 2021 | procedure |
| 15 | 11 | 504 | Mark provisional, revised and forecast values in square brackets, not symbols | Screen readers find symbols hard; the UK standard | Standard (official statistics) | **Fixed** (procedure) | Analysis Function 2022; Eurostat flags | procedure |
| 15 | 12 | 505 | Any ordering of places ships with a question-and-answer text saying what it can and cannot be used to say, with worked examples and the reason comparability is lost between editions | A rank implies a distance the data do not measure; the deprivation indices say so | Standard (official statistics) | **Fixed** (stance) | IoD 2025 FAQ and research report | stance |
| 15 | 13 | 506 | Where no composite is made, print the refusal and its reason; where one is made, its rank carries an interval | The OECD's sentence; the JRC's audit | Standard (method); Evidence of method | **Fixed** (stance) | OECD RWB user guide; JRC/GII 2024; Chapter 5 | stance |
| 15 | 14 | 507 | A base-year index freezes its standardisation, prints the count of indicators whose change could not be measured, and carries a status notice when it stalls | The Health Index's method, and the notice it lacks | Standard (official statistics); Reading | Adaptable | ONS Health Index 2023 |  |
| 15 | 15 | 508 | Label every "what difference did it make" claim with its evidence level, with a declared minimum | Before-and-after is description | Standard (method) | Adaptable | What Works Growth SMS; Chapter 7 |  |
| 15 | 16 | 509 | Print, on any indicator display, what it is not, that no mechanical inference may be drawn from it, and the data cut-off date | The systemic-risk board prints all three; the other regulator displays read print the first | Standard (regulator) | Adaptable | ESRB; FPC 2023 |  |
| 15 | 17 | 510 | Publish a release calendar at least a quarter ahead; release at one moment; list anyone who sees a figure early | The statutory test is trust | Standard (law); Standard (method) | Adaptable | Pre-release Order 2008; IMF SDDS; ONS 2017 |  |
| 15 | 18 | 511 | Count reach in the unit counted and name it, never as "readers"; measure use only by asking, and print the response rate | The units do not convert; the two evaluations that asked had a 5 per cent response and a sample of survivors | Reading; Evidence of method | **Fixed** (procedure) | JHU, UKHSA, OWID figures; Scottish Government 2024 (read once); Ismail 2022 | procedure |
| 15 | 19 | 512 | Write the retirement plan before launch: notice, reason, archive, licence, stable URLs, successor, gap analysis | Four documented endings and one undocumented; the regulator lists the plan among the minimum and asks for archiving processes "from the start" | Standard (regulator); Practice | **Fixed** (procedure) | OSR 2025; JHU; OWID; UKHSA; CTP; TAA | procedure |
| 15 | 20 | 513 | Evaluate a pilot independently before roll-out, with N, n and response rate printed, and read the result before making the thing piloted a condition | The culture sector's own evidence: a pilot whose data were "interesting" rather than "useful" and whose benchmarking most doubted was made a condition anyway | Evidence of method | Adaptable | Nordicity 2016; Selwood 2019; Hodge review (secondary) |  |
| 15 | 21 | 514 | Record every borrowed mechanism in the precedent record, nine lines, with its status, before it ships | A rule with no stated reason is a habit; one with no evidence or named cost is a bet | Nightlife Culture | **Fixed** (procedure) | This chapter | procedure |
| 15 | 22 | 515 | Which of section 9's mechanisms beyond the above to adopt, and when their conditions are met | The offer, with terms | — | Adaptable | Section 9 |  |

### 1.2 Counts

**Rows per chapter** (data rows; header and rule lines excluded).

| Ch | Rows | Tier cell contains "Fixed" | of which exactly `**Fixed**` | Adaptable only (no "Fixed" in cell) | *Decorative* |
|---|---|---|---|---|---|
| 1 | 19 | 16 | 14 | 2 | 1 |
| 2 | 26 | 21 | 16 | 4 | 1 |
| 3 | 29 | 21 | 13 | 7 | 1 |
| 4 | 39 | 34 | 24 | 4 | 1 |
| 5 | 27 | 22 | 15 | 4 | 1 |
| 6 | 43 | 42 | 21 | 1 | 0 |
| 7 | 36 | 36 | 17 | 0 | 0 |
| 8 | 34 | 32 | 10 | 2 | 0 |
| 9 | 37 | 35 | 17 | 2 | 0 |
| 10 | 43 | 43 | 14 | 0 | 0 |
| 11 | 39 | 35 | 15 | 4 | 0 |
| 12 | 40 | 37 | 15 | 2 | 1 |
| 13 | 33 | 30 | 16 | 2 | 1 |
| 14 | 19 | 13 | 5 | 5 | 1 |
| 15 | 22 | 16 | 0 | 6 | 0 |
| **Total** | **486** | **433** | **212** | **45** | **8** |

Chapter 0: 0 rows (no rules table).

**Totals by tier — every distinct wording counted separately** (53 distinct wordings across 486 rows). The IDs are given for every wording used fewer than six times.

| Count | Tier cell, exactly as printed | Rows (Ch.#) |
|---|---|---|
| 212 | **Fixed** | by chapter: Ch 1: 14, Ch 2: 16, Ch 3: 13, Ch 4: 24, Ch 5: 15, Ch 6: 21, Ch 7: 17, Ch 8: 10, Ch 9: 17, Ch 10: 14, Ch 11: 15, Ch 12: 15, Ch 13: 16, Ch 14: 5 |
| 78 | **Fixed** as a procedure | by chapter: Ch 4: 1, Ch 5: 2, Ch 6: 6, Ch 7: 8, Ch 8: 9, Ch 9: 8, Ch 10: 16, Ch 11: 10, Ch 12: 10, Ch 13: 8 |
| 73 | **Fixed** as a stance | by chapter: Ch 3: 1, Ch 4: 2, Ch 5: 1, Ch 6: 10, Ch 7: 7, Ch 8: 7, Ch 9: 9, Ch 10: 11, Ch 11: 9, Ch 12: 11, Ch 13: 5 |
| 37 | Adaptable | by chapter: Ch 1: 2, Ch 2: 3, Ch 3: 4, Ch 4: 2, Ch 5: 3, Ch 8: 2, Ch 9: 2, Ch 11: 4, Ch 12: 2, Ch 13: 2, Ch 14: 5, Ch 15: 6 |
| 19 | **Fixed** (procedure) | by chapter: Ch 14: 5, Ch 15: 14 |
| 8 | *Decorative* | by chapter: Ch 1: 1, Ch 2: 1, Ch 3: 1, Ch 4: 1, Ch 5: 1, Ch 12: 1, Ch 13: 1, Ch 14: 1 |
| 5 | **Fixed** (stance) | 14.3, 14.11, 14.17, 15.12, 15.13 |
| 4 | **Fixed** (adopted) | 2.11, 2.24, 4.10, 4.23 |
| 3 | Adaptable (strong default) | 3.10, 5.14, 6.20 |
| 2 | **Fixed** (declared); Adaptable (which) | 5.8, 6.27 |
| 2 | **Fixed** (stated); Adaptable (values) | 6.2, 6.34 |
| 2 | **Fixed** as a procedure; Adaptable in value | 9.5, 10.5 |
| 1 | **Fixed** (2.4.13 as a stance) | 13.14 |
| 1 | **Fixed** (adopted voluntarily) | 1.14 |
| 1 | **Fixed** (both ends; say which); Adaptable (which leads) | 7.15 |
| 1 | **Fixed** (ceiling); Adaptable (digits) | 3.18 |
| 1 | **Fixed** (declared); Adaptable (whether) | 7.6 |
| 1 | **Fixed** (evidential status stated) | 3.9 |
| 1 | **Fixed** (instrument); Adaptable (wording) | 6.7 |
| 1 | **Fixed** (no single figure; say what is omitted); **Fixed** as a stance (even number) | 7.31 |
| 1 | **Fixed** (pattern maps); Adaptable where the task is reading a value | 3.5 |
| 1 | **Fixed** (period); **Fixed** as a stance (four parts) | 8.2 |
| 1 | **Fixed** (show the decision) | 2.18 |
| 1 | **Fixed** (stated); Adaptable (which) | 5.3 |
| 1 | **Fixed** (test); Adaptable (combine) | 5.18 |
| 1 | **Fixed** (that one is shown); Adaptable (which) | 4.25 |
| 1 | **Fixed** (the principle); Adaptable (the form) | 7.4 |
| 1 | **Fixed** (two tests); **Fixed** as a stance (the described) | 6.31 |
| 1 | **Fixed** (unit); **Fixed** as a stance (count) | 4.1 |
| 1 | **Fixed** as a procedure; Adaptable (rule and threshold) | 4.32 |
| 1 | **Fixed** as a procedure; Adaptable in parts | 10.11 |
| 1 | **Fixed** as a procedure; Adaptable in period | 8.32 |
| 1 | **Fixed** as a stance (the studio's) | 5.20 |
| 1 | **Fixed** as a stance, form Adaptable | 12.16 |
| 1 | **Fixed** as a stance; Adaptable for a declared live element | 8.12 |
| 1 | **Fixed** as a stance; Adaptable in figure | 8.26 |
| 1 | **Fixed** as a stance; Adaptable in value | 8.16 |
| 1 | **Fixed** as a stance; the rule itself Adaptable | 4.3 |
| 1 | **Fixed** as defaults | 3.16 |
| 1 | **Fixed** as disclosure | 4.27 |
| 1 | **Fixed** as sequence | 2.23 |
| 1 | **Fixed** as the planning assumption | 3.26 |
| 1 | **Fixed** for precise comparison; Adaptable as a general form rule | 3.2 |
| 1 | **Fixed**; the house limit Fixed as a stance | 11.4 |
| 1 | Adaptable (a hypothesis to test) | 2.10 |
| 1 | Adaptable (how to name it) — flagged for Carly | 4.14 |
| 1 | Adaptable (strong default); the headline itself is Fixed under the words rule | 3.13 |
| 1 | Adaptable (strong default; the audit itself is a Nightlife Culture choice) | 4.29 |
| 1 | Adaptable (what it claims to be is Carly's) | 3.11 |
| 1 | Adaptable (which interfaces signal); **Fixed** (that the job reads them) | 8.9 |
| 1 | Adaptable in form; Fixed as a prohibition on the supplement pattern | 2.22 |
| 1 | Adaptable in method; Fixed as sequence | 1.15 |
| 1 | Adaptable within the ceiling | 3.6 |

**Grouped.**

| Group | Rows | Share of 486 | Distinct wordings |
|---|---|---|---|
| Fixed — all variants with no Adaptable part | 405 | 83.3% | 20 |
| Mixed — one cell says both Fixed and Adaptable | 28 | 5.8% | 25 |
| Adaptable — plain or qualified, no Fixed part | 45 | 9.3% | 7 |
| Decorative | 8 | 1.6% | 1 |
| other | 0 | 0.0% | 0 |
| **Total** | **486** | 100% | 53 |

Within "Fixed — all variants with no Adaptable part" (405 rows): exactly `**Fixed**` 212; wording contains "procedure" 97; contains "stance" (and not "procedure") 85; contains "sequence" 1; other qualifiers only 10.

Within "Adaptable" (45 rows): exactly `Adaptable` 37; qualified (strong default, a hypothesis to test, within the ceiling, flagged for Carly, etc.) 8.

Any row whose Tier cell contains the word "Fixed" at all: **433** (89.1%); contains "Adaptable" at all: **73**; Decorative: **8**. (The first two overlap in the 28 mixed cells.)

**The two spellings of the same qualifier.** "as a procedure" / "as a stance" (Chapters 4–13) and "(procedure)" / "(stance)" (Chapters 14–15) are the same qualifier in two forms:

| Wording family | Rows | Chapters where used |
|---|---|---|
| "as a procedure" (any cell containing it) | 83 | Ch 4: 2, Ch 5: 2, Ch 6: 6, Ch 7: 8, Ch 8: 10, Ch 9: 9, Ch 10: 18, Ch 11: 10, Ch 12: 10, Ch 13: 8 |
| "(procedure)" | 19 | Ch 14: 5, Ch 15: 14 |
| "as a stance" (any cell containing it) | 85 | Ch 3: 1, Ch 4: 4, Ch 5: 2, Ch 6: 11, Ch 7: 8, Ch 8: 11, Ch 9: 9, Ch 10: 11, Ch 11: 10, Ch 12: 12, Ch 13: 6 |
| "(stance)" | 5 | Ch 14: 3, Ch 15: 2 |
| "sequence" | 2 | Ch 1: 1, Ch 2: 1 |
| "statement of the record" | 0 | — none in any rules table |
| "(adopted)" / "(adopted voluntarily)" | 5 | Ch 1: 1, Ch 2: 2, Ch 4: 2 |

**Kind column, for reference.** 182 distinct Kind wordings across the 486 rows (Chapter 0 defines five kinds). The ten commonest: `Evidence` 62; `Standard` 59; `Reading` 25; `Evidence (adjacent domain)` 20; `—` 14; `Evidence + Reading` 12; `Evidence + Practice` 12; `Standard (W3C)` 12; `Standard + Evidence` 11; `Practice` 10. Rows whose Kind cell is a dash `—` (no kind given): 1.18, 1.19, 2.25, 2.26, 3.28, 3.29, 4.38, 4.39, 5.26, 5.27, 12.40, 13.33, 14.19, 15.22 (14 rows — every one is a residual "open choices" row or a Decorative row).

### 1.3 Duplicates and near-duplicates — the same rule stated in more than one chapter, in different words

Each group below sets the chapters' own wordings side by side, as printed, with the tier each chapter gave. The grouping is mine (made by reading all 486 rows); the wording is the chapters'. A row may appear in more than one group. "Tiers" at the foot of each group lists the distinct tier wordings in it — where there is more than one, the same rule carries different firmness in different chapters.

**D1 · The twin / the precise version**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 8.31 | Every map has a non-map twin — the same figures by the same places as a table — reachable before the script; pan and zoom have buttons; the sequential ramp is short | **Fixed** |
| 10.26 | A free dashboard is a service to the public under the Equality Act; every map has an accessible twin; a panel's rules are checked for particular disadvantage to a protected group | **Fixed** |
| 13.6 | Every view has a native HTML table twin with header cells, paginated and keyboard-sortable, the figures reachable before any script | **Fixed** |
| 13.7 | A map's twin is joined by a sentence for the shape and the statement says the twin does not carry geography | **Fixed** as a procedure |
| 14.4 | The precise twin is one step away and the form states its finding, and any distortion, in words on itself | **Fixed** (procedure) |

Chapters: 8, 10, 13, 14. Tiers (3 distinct): `**Fixed**` · `**Fixed** as a procedure` · `**Fixed** (procedure)`.

**D2 · The table route (a plain table as a route to the same figures)**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 2.10 | Offer a plain-table view as a first-class route for the reader already opposed | Adaptable (a hypothesis to test) |
| 3.17 | Show a value the reader wants to know as a number or a table, not a chart; show a trend or comparison as a chart | Adaptable |
| 8.25 | Figures and the table are in the HTML and shown before any script runs; the page is not a single-page application | **Fixed** as a stance |
| 11.21 | Targets are at least 24 by 24 CSS pixels, or have an equivalent control that is; dense data marks that must be smaller get an equivalent route — the table twin | **Fixed** |
| 11.22 | A tooltip, where used, repeats what is at the mark or in the table, is spoken and keyboard-reachable, and is never the only place a value lives | **Fixed** |
| 13.6 | Every view has a native HTML table twin with header cells, paginated and keyboard-sortable, the figures reachable before any script | **Fixed** |
| 13.15 | Nothing fires on mouse-down; every drag has a single-pointer alternative; targets 24 px or the table twin | **Fixed** |

Chapters: 2, 3, 8, 11, 13. Tiers (4 distinct): `Adaptable (a hypothesis to test)` · `Adaptable` · `**Fixed** as a stance` · `**Fixed**`.

**D3 · The sentence first / the title carries the message**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.7 | Put the message in the title, in words; put statistics and context beside the marks; never title-only, never no-text | **Fixed** |
| 3.8 | Title and chart point at the same salient thing | **Fixed** |
| 3.13 | Declutter for professionalism; add a headline, one highlight and one sentence for recall | Adaptable (strong default); the headline itself is Fixed under the words rule |
| 11.2 | The first screen's sentence is written before the screen is designed; it answers the named reader's question and works with no interaction | **Fixed** |
| 11.4 | The most important information comes first on every page, section and chart; chart titles state the trend; headings and titles within the official lengths, and within the house's shorter one where it applies | **Fixed**; the house limit Fixed as a stance |
| 11.12 | Text on the face is not treated as clutter: the title carries the trend, statistics and context sit by the point, and whatever an annotation carries is also in the text, because annotations may vanish on a phone | **Fixed** |
| 11.13 | A title never says what the chart does not show; where they would disagree, the chart is redrawn or the title rewritten | **Fixed** |
| 14.13 | A headline read in passing has its letter height set from the distance it is read at, and its finding restated in the body text at arm's length | **Fixed** (procedure) |
| 14.14 | Short headlines; the count is the house's | Adaptable |

Chapters: 3, 11, 14. Tiers (5 distinct): `**Fixed**` · `Adaptable (strong default); the headline itself is Fixed under the words rule` · `**Fixed**; the house limit Fixed as a stance` · `**Fixed** (procedure)` · `Adaptable`.

**D4 · The source line / provenance travels with the figure**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.3 | Document provenance, method, positionality and uncertainty on the face of the display | **Fixed** |
| 2.8 | Make the source checkable before making the chart persuasive | **Fixed** |
| 4.7 | Ship the provenance set with every figure: responsible party; source and why; method and deviations; period; issued and modified; status; quality with error; what was withheld; what it may be compared with | **Fixed** |
| 5.2 | Every part of a composite carries Chapter 4's provenance set | **Fixed** |
| 11.28 | The records' kinds sit on the face as statuses in text that open the record; a source line is followable, not only present | **Fixed** as a stance |
| 12.32 | Every chart carries, inside its frame, title, unit, source, base, address and snapshot date, for comparisons the gate and wording, and for either column the bridging sentence; the page text repeats them | **Fixed** as a stance |
| 13.13 | The frame's identifying text (title, unit, source, base, address, date; gate and wording on comparisons) is drawn as SVG text on the page, repeated as HTML beside the chart, and baked into the export; never the image alone | **Fixed** as a procedure |
| 14.11 | The conventions of objectivity are earned by the records beneath them; a source line points to a reachable source | **Fixed** (stance) |

Chapters: 1, 2, 4, 5, 11, 12, 13, 14. Tiers (4 distinct): `**Fixed**` · `**Fixed** as a stance` · `**Fixed** as a procedure` · `**Fixed** (stance)`.

**D5 · The dates: period, published, revised; the snapshot date; vintages kept**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 4.2 | State the reference period as a closed interval, separately from the date issued and the date last modified | **Fixed** |
| 4.8 | Keep the record when the number changes: a figure's description and its previous values outlive its current value | **Fixed** |
| 8.2 | Each series states the period it describes, the date published, the date last revised and its declared frequency; "last updated" alone is never shown | **Fixed** (period); **Fixed** as a stance (four parts) |
| 8.21 | Every fetch is committed to a version history so that any figure's vintage is recoverable by date | **Fixed** as a stance |
| 11.24 | Every state can be frozen as a dated, unchanging snapshot of its data and text — at each release at least, and on request or on share — findable from the live view and linking previous, next and live; the citation is generated and carries the address with its selection, the snapshot date, the data version and the retrieval date | **Fixed** as a procedure |
| 11.25 | Data are versioned and timestamped; a correction is announced at the top of the affected view with when and why; a retired view keeps its address under a dated banner; statistics are never silently replaced | **Fixed** |
| 11.26 | A cropped or shared copy carries the stamp, the floor note, the unit and the snapshot date | **Fixed** |
| 12.32 | Every chart carries, inside its frame, title, unit, source, base, address and snapshot date, for comparisons the gate and wording, and for either column the bridging sentence; the page text repeats them | **Fixed** as a stance |
| 15.6 | Keep every published data file as a dated vintage from the first release | **Fixed** (procedure) |
| 15.16 | Print, on any indicator display, what it is not, that no mechanical inference may be drawn from it, and the data cut-off date | Adaptable |

Chapters: 4, 8, 11, 12, 15. Tiers (6 distinct): `**Fixed**` · `**Fixed** (period); **Fixed** as a stance (four parts)` · `**Fixed** as a stance` · `**Fixed** as a procedure` · `**Fixed** (procedure)` · `Adaptable`.

**D6 · The gate / what a comparison must declare**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 2.12 | Name the denominator on every map and comparison, and show the alternative | **Fixed** |
| 4.20 | Every comparison carries the ten-line declaration (definition; period; geography and vintage; method; disclosure; breaks; revisions; comparator and method; precision; outlier handling) | **Fixed** |
| 7.1 | Every comparison carries the comparison record: what is held equal, who chose the comparators, the standardisation, the order, the interval, the season, the base month, the design, the ripple, the future's terms; a line that cannot be filled says "not done" | **Fixed** as a stance |
| 7.11 | Identity measures — those the studio designates nominal, and says so — are never on an ordered axis; condition measures are compared through the gate, which now includes interval, standardisation and order | **Fixed** as a stance |
| 12.19 | Every cross-place condition chart carries the gate's status, the harmonised criteria and the wording rule inside its frame | **Fixed** |
| 12.22 | The advocacy sentence passes through the gate and names its peer by method | **Fixed** |
| 12.32 | Every chart carries, inside its frame, title, unit, source, base, address and snapshot date, for comparisons the gate and wording, and for either column the bridging sentence; the page text repeats them | **Fixed** as a stance |
| 13.13 | The frame's identifying text (title, unit, source, base, address, date; gate and wording on comparisons) is drawn as SVG text on the page, repeated as HTML beside the chart, and baked into the export; never the image alone | **Fixed** as a procedure |

Chapters: 2, 4, 7, 12, 13. Tiers (3 distinct): `**Fixed**` · `**Fixed** as a stance` · `**Fixed** as a procedure`.

**D7 · Boundary vintage and the lookup**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 4.22 | Use area codes with their vintage; declare the lookup for any best-fit aggregation; never compare across a boundary change without it | **Fixed** |
| 8.29 | Boundary files are the generalised product appropriate to the scale, cut to the area shown, with their date and two-owner attribution; a boundary vintage is pinned and stated | **Fixed** |
| 12.1 | Every figure about a place states its unit, the unit's vintage, and what the unit hides | **Fixed** |
| 12.6 | Comparisons across boundary vintages carry an explicit lookup | **Fixed** |

Chapters: 4, 8, 12. Tiers (1 distinct): `**Fixed**`.

**D8 · Ranks, league tables and intervals**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.11 | Rankings by rate are screening instruments, never verdicts; show intervals | **Fixed** |
| 2.13 | Treat a league table as acting on the ranked; never present one as a reader's decision aid without intervals | **Fixed** |
| 4.6 | Rates on small bases carry intervals and are shown in a funnel, never ranked raw or ranked adjusted | **Fixed** |
| 5.9 | Run an uncertainty and sensitivity analysis over the defensible alternatives and publish the rank with its interval | **Fixed** |
| 5.11 | Say a rank as a range with a most-likely value | **Fixed** |
| 6.17 | Never place a social-return ratio in a league table; show it with its story | **Fixed** |
| 6.37 | Never rank places of different sizes by a raw rate; show the interval or do not rank | **Fixed** |
| 7.2 | No league table of places on any measure, and no bands of position (quintiles and the like); position is shown within a distribution with its interval, in categories of statistical separation from an expectation if categories are needed | **Fixed** as a stance |
| 7.3 | Where a single place's rank must be stated (a reader asks "where do we stand?"), it is given as a range, and a small unit's rank on a rate is not stated at all | **Fixed** |
| 7.4 | Compare places on a funnel or against a declared expectation, never by sorted value alone; where a display is sorted, the sort is a reading aid and the finding is position against limits | **Fixed** (the principle); Adaptable (the form) |
| 7.7 | An observed-to-expected ratio is compared with the expectation, and with other ratios only under the two conditions the method names; it is not ranked | **Fixed** |
| 9.12 | A felt measure for a place is compared with its own history or with declared peers, and Chapter 7's rule against ranking applies | **Fixed** |
| 10.37 | No panel grades or ranks places, and where a value is drawn by colour the scale is checked for stigma; a money view is lit for a scene only after its governance has agreed, the speculation reading has been assessed, and both are on the record | **Fixed** as a stance |
| 12.34 | No screen carries an ordered all-places list | **Fixed** as a stance |
| 12.35 | Any rank the house ever lets out carries the official wording: ordinal, relative, no distance | **Fixed** |
| 15.12 | Any ordering of places ships with a question-and-answer text saying what it can and cannot be used to say, with worked examples and the reason comparability is lost between editions | **Fixed** (stance) |
| 15.13 | Where no composite is made, print the refusal and its reason; where one is made, its rank carries an interval | **Fixed** (stance) |

Chapters: 1, 2, 4, 5, 6, 7, 9, 10, 12, 15. Tiers (4 distinct): `**Fixed**` · `**Fixed** as a stance` · `**Fixed** (the principle); Adaptable (the form)` · `**Fixed** (stance)`.

**D9 · Identity is never ranked**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 7.11 | Identity measures — those the studio designates nominal, and says so — are never on an ordered axis; condition measures are compared through the gate, which now includes interval, standardisation and order | **Fixed** as a stance |
| 12.15 | Identity fields are never ranked, and the data contract records which fields are identity | **Fixed** as a stance |

Chapters: 7, 12. Tiers (1 distinct): `**Fixed** as a stance`.

**D10 · Uncertainty as a numeric range; a word for likelihood carries its number**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.5 | Show uncertainty as a numeric range, never as a vague hedge or a hidden point | **Fixed** |
| 2.14 | Show uncertainty as a numeric range; never as a verbal hedge; never omit it to protect the signal | **Fixed** |
| 3.23 | Never a bare interval or a hard boundary for uncertainty; prefer countable dots, gradients, violins or animated draws; show outcome spread, not only estimate uncertainty, where individuals are the subject | **Fixed** |
| 12.12 | The missed column shows its intervals, samples and bands | **Fixed** |
| 15.10 | Show uncertainty as a range beside a point; never a verbal hedge alone | **Fixed** (procedure) |
| 3.24 | A word for probability carries its number in brackets beside it | **Fixed** |
| 7.33 | Words for likelihood carry their numbers in the sentence; no verbal likelihood term stands without one | **Fixed** |

Chapters: 1, 2, 3, 7, 12, 15. Tiers (2 distinct): `**Fixed**` · `**Fixed** (procedure)`.

**D11 · A cell not shown is marked, never blank; a line is never joined across a gap**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.12 | Where official statistics suppress or perturb, show that fact, never a blank | **Fixed** |
| 4.12 | Every empty cell states its kind; a blank is permitted only where there is exactly one reason for blanks and it is stated above the table | **Fixed** |
| 4.16 | Never join a line across a missing point, dotted or dashed; highlight the gap and say why | **Fixed** |
| 4.18 | A suppressed cell is marked, never blanked; secondary suppression applied; the display states whether its protection is suppression or perturbation | **Fixed** |
| 6.41 | Say whether a withheld figure is withheld for confidentiality or for precision, and never let the same mark mean both | **Fixed** as a stance |
| 10.7 | Suppression is primary and secondary, across every linked view; or a consistent cell key is used so the same cell shows the same way everywhere; the choice is declared | **Fixed** as a procedure |
| 10.8 | Every floor is paired with a form that keeps the small present — a band, a presence mark, a held status — and a withheld cell is marked, never blank | **Fixed** |
| 11.29 | A cell not shown is marked, explained by kind, and never blank; nothing is imputed into a withheld cell; a series is never joined across a gap; the maker expects, and does not design away, the lower confidence a shown gap produces against a dropped one | **Fixed** |
| 12.11 | Every hole in either column is rendered at full size with its kind named by symbol and in words | **Fixed** |

Chapters: 1, 4, 6, 10, 11, 12. Tiers (3 distinct): `**Fixed**` · `**Fixed** as a stance` · `**Fixed** as a procedure`.

**D12 · Nothing crucial behind a hover or a click; keyboard; pointer; target size**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.19 | Nothing crucial behind a click, a hover or a tooltip; everything crucial reachable by keyboard and on a phone | **Fixed** |
| 11.8 | The small screen is designed first; what is removed for it is recorded as not the message; no hover content is load-bearing | **Fixed** |
| 11.18 | Nothing the majority of readers need is one step away; nothing one step away is hidden behind a control readers think will take them off the page; detail on request is two levels at most, with an obvious route | **Fixed** |
| 11.19 | Content on hover meets the three conditions (dismissible, hoverable, persistent) and is also reachable by keyboard focus; nothing is only on hover, because touch has no hover | **Fixed** |
| 11.20 | Every control works by keyboard and by a single pointer without a path or a drag; maps have buttons for zoom and pan | **Fixed** |
| 11.21 | Targets are at least 24 by 24 CSS pixels, or have an equivalent control that is; dense data marks that must be smaller get an equivalent route — the table twin | **Fixed** |
| 11.22 | A tooltip, where used, repeats what is at the mark or in the table, is spoken and keyboard-reachable, and is never the only place a value lives | **Fixed** |
| 13.14 | Everything is operable by keyboard with no trap; focus visible, sized and contrasted to 2.4.13, and never covered by the filter bar | **Fixed** (2.4.13 as a stance) |
| 13.15 | Nothing fires on mouse-down; every drag has a single-pointer alternative; targets 24 px or the table twin | **Fixed** |

Chapters: 3, 11, 13. Tiers (2 distinct): `**Fixed**` · `**Fixed** (2.4.13 as a stance)`.

**D13 · Colour never the only carrier; contrast**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.3 | Never let colour be the only means of distinguishing or conveying anything | **Fixed** |
| 13.11 | Colour is never the only carrier; legends match by more than colour | **Fixed** |
| 3.4 | Text at 4.5:1; parts of graphics needed to understand the content at 3:1 against adjacent colours | **Fixed** |
| 13.10 | Each line, slice or mark that carries meaning has 3:1 contrast unless labels carry the same information | **Fixed** |

Chapters: 3, 13. Tiers (1 distinct): `**Fixed**`.

**D14 · Recognition / member checking before release**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.15 | Build the common ground before the screen; test recognition with each community | Adaptable in method; Fixed as sequence |
| 2.23 | Recognition is checked before release, as a dialogue that can change the next release | **Fixed** as sequence |
| 5.19 | Gather recognition from the people measured, record what it corrected, and mark it on the card as face validity and credibility — not as evidence of the construct | **Fixed** as a stance |
| 9.33 | Recognition is gathered as member checking — who was shown what, what they said, what changed — and recorded as content and response-process evidence plus legitimacy; it is never presented as validation complete | **Fixed** as a stance |
| 12.36 | Every place-page is shown to people from the scene before publication, in a form chosen with them; what was said and what changed is recorded by role, never by name; the page says it was reviewed | **Fixed** as a procedure |

Chapters: 1, 2, 5, 9, 12. Tiers (4 distinct): `Adaptable in method; Fixed as sequence` · `**Fixed** as sequence` · `**Fixed** as a stance` · `**Fixed** as a procedure`.

**D15 · The construct before the proxy, the parts or the items**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 2.16 | Define the construct before choosing the proxy | **Fixed** |
| 5.1 | Write the construct and the theoretical framework before choosing parts; a composite without one is not built | **Fixed** |
| 9.2 | The construct is named in words, and its register (made / perceived / excess), before any item is written; the three registers are never collapsed into one number | **Fixed** as a stance |

Chapters: 2, 5, 9. Tiers (2 distinct): `**Fixed**` · `**Fixed** as a stance`.

**D16 · The denominator; rates not counts**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.10 | Scale size-dependent measures by an appropriate denominator, and say which | **Fixed** |
| 2.12 | Name the denominator on every map and comparison, and show the alternative | **Fixed** |
| 4.5 | Name the denominator of every rate and make the alternatives reachable; use time-in-observation (person-time, venue-nights) where units are observed for unequal spans | **Fixed** |
| 11.31 | A choropleth shows rates, never counts; its breaks are declared and, "when possible", held constant across every view of the same measure; its legend is matched | **Fixed** |

Chapters: 1, 2, 4, 11. Tiers (1 distinct): `**Fixed**`.

**D17 · The unit declared**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.9 | Show and justify the unit of aggregation; test sensitivity to it | **Fixed** |
| 2.7 | Show the reader's own geography — the ward, the patch — at the scale they plan at | **Fixed** |
| 4.1 | State the unit of observation (what one row is) and the count of rows beneath every figure | **Fixed** (unit); **Fixed** as a stance (count) |
| 12.1 | Every figure about a place states its unit, the unit's vintage, and what the unit hides | **Fixed** |
| 12.2 | The landing unit is a declared choice; the administrative unit is shown beside it | **Fixed** as a stance |

Chapters: 1, 2, 4, 12. Tiers (3 distinct): `**Fixed**` · `**Fixed** (unit); **Fixed** as a stance (count)` · `**Fixed** as a stance`.

**D18 · Release the data with the display**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.4 | Release the data with the display, through a documented route | **Fixed** |
| 2.20 | Release numbers with their data and caveats so an opposing coalition's analyst can check them | **Fixed** |
| 2.24 | Numbers for understanding, not numbers for advocacy: produce with caveats, release with data | **Fixed** (adopted) |

Chapters: 1, 2. Tiers (2 distinct): `**Fixed**` · `**Fixed** (adopted)`.

**D19 · Defaults and first states are declared choices**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.20 | Every default — place, measure, period, sort, extent — is chosen, written down and shown as a choice | **Fixed** as a stance |
| 11.5 | The landing pattern is chosen from the six, named in writing, and the exemplar (if any) is declared an endorsement | **Fixed** as a procedure |
| 12.2 | The landing unit is a declared choice; the administrative unit is shown beside it | **Fixed** as a stance |
| 12.8 | The missed column is shown first, as a declared endorsement, and never alone | **Fixed** as a stance |

Chapters: 3, 11, 12. Tiers (2 distinct): `**Fixed** as a stance` · `**Fixed** as a procedure`.

**D20 · Monitoring is not evaluation; the rung and the verb**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 2.2 | Label every panel as monitoring or as evaluation; never imply a counterfactual the display does not have | **Fixed** |
| 2.3 | State where a claim stands on the evidence ladder when it will be read by a funder or a What Works body | **Fixed** |
| 2.15 | Never let a place indicator be read as evidence of an intervention; mark descriptions as descriptions | **Fixed** |
| 6.19 | Label every claim of cause with the rung its evidence reaches; from observational data alone the verbs are "alongside", "after" and "where"; "contributed to" only with a theory of change whose alternatives have been tested | **Fixed** |
| 7.22 | A before-and-after display lists its eight rivals and uses no verb stronger than "after"; an interrupted series with its impact model declared may say "departed from its trend" | **Fixed** |
| 7.29 | Every intervention claim states its rung on the What Works scale, with any other ladder's differing placement beside it, and the verb that rung earns; plain before/after and place-against-place are the bottom | **Fixed** |
| 15.15 | Label every "what difference did it make" claim with its evidence level, with a declared minimum | Adaptable |

Chapters: 2, 6, 7, 15. Tiers (2 distinct): `**Fixed**` · `Adaptable`.

**D21 · "Leading" only with a measured record**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 6.23 | "Leading" is shown only when a lead has been measured against a named reference series; until then two series are two series | **Fixed** |
| 7.35 | "Leading" is used only of a series with a measured record of turning points against a named reference series — the Conference Board's tests of conformity and consistent timing, or an equivalent stated one — and the record's real-time weakness is noted | **Fixed** as a procedure |

Chapters: 6, 7. Tiers (2 distinct): `**Fixed**` · `**Fixed** as a procedure`.

**D22 · The retirement plan**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 8.32 | The notice the studio gives when retiring a series, and the archive address, are written before the first series needs them; a retired series stays reachable | **Fixed** as a procedure; Adaptable in period |
| 11.25 | Data are versioned and timestamped; a correction is announced at the top of the affected view with when and why; a retired view keeps its address under a dated banner; statistics are never silently replaced | **Fixed** |
| 11.38 | A dashboard has a retirement plan: a banner six months ahead, the state preserved, data and metadata kept and marked, code archived in public | **Fixed** as a procedure |
| 15.19 | Write the retirement plan before launch: notice, reason, archive, licence, stable URLs, successor, gap analysis | **Fixed** (procedure) |

Chapters: 8, 11, 15. Tiers (4 distinct): `**Fixed** as a procedure; Adaptable in period` · `**Fixed**` · `**Fixed** as a procedure` · `**Fixed** (procedure)`.

**D23 · Revisions, corrections, change notes, status marks**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 4.9 | Use "reliable" in the official sense (closeness of early to later estimates) or not at all; show provisional figures as [p] and revised as [r] | **Fixed** |
| 4.21 | Mark a change of definition or method with [b]; provide a back series or correction factors where possible | **Fixed** |
| 7.18 | Every series carries its breaks and its revision status; a consistent back series is provided or its absence stated | **Fixed** |
| 8.4 | A change to the data carries a change note saying what changed and when; the page is never marked updated without saying what | **Fixed** |
| 8.5 | Revisions and corrections are distinguished and dated; a figure open to revision says until when | **Fixed** |
| 11.25 | Data are versioned and timestamped; a correction is announced at the top of the affected view with when and why; a retired view keeps its address under a dated banner; statistics are never silently replaced | **Fixed** |
| 15.3 | Keep a dated, labelled change log apart from the refresh, with issue and resolved paired | **Fixed** (procedure) |
| 15.5 | A revision is a scheduled change; a correction is labelled as a correction; print the typical revision's size once it can be computed | **Fixed** (procedure) |
| 15.11 | Mark provisional, revised and forecast values in square brackets, not symbols | **Fixed** (procedure) |

Chapters: 4, 7, 8, 11, 15. Tiers (2 distinct): `**Fixed**` · `**Fixed** (procedure)`.

**D24 · Reactivity, gaming and the independent audit**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.7 | Watch for the proxy moving without the goal; measure the goal where it can be measured | **Fixed** |
| 1.8 | Treat every published measure as reactive; audit for gaming | **Fixed** |
| 5.12 | Design the independent audit with the measure: name the check that is not on the dashboard, its frequency and owner, and the response to gaming | **Fixed** as a procedure |
| 5.13 | Expect ratchet, threshold and output-distortion effects and the three non-adversarial failures of a proxy; monitor the distribution near any threshold | **Fixed** as a procedure |
| 6.13 | Keep a measure that is not the proxy beside the proxy, and watch for them parting | **Fixed** as a stance |

Chapters: 1, 5, 6. Tiers (3 distinct): `**Fixed**` · `**Fixed** as a procedure` · `**Fixed** as a stance`.

**D25 · The disclosure floor set by the scene's knowability**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 6.42 | Set the identifying threshold by the scene's knowability, above the national rule where local knowledge would name the units | **Fixed** as a stance |
| 10.4 | The identifiability test is the motivated intruder, and for a scene the intruder is modelled as a regular with local knowledge | **Fixed** as a stance |
| 10.5 | The disclosure floor is set per view, above the national rule where the scene can name the units, and stated; its value is a judgement scaled to sensitivity | **Fixed** as a procedure; Adaptable in value |

Chapters: 6, 10. Tiers (2 distinct): `**Fixed** as a stance` · `**Fixed** as a procedure; Adaptable in value`.

**D26 · Outliers**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.13 | Investigate an outlier as a mechanism before treating it as noise; use positive deviance as a method | Adaptable |
| 4.33 | Investigate a flagged point against the six artefact causes before treating it as a finding; remove only a confirmed artefact, and declare the removal | **Fixed** |
| 4.36 | Treat a good-end outlier as a hypothesis about mechanism; state the criteria, threshold and comparison group; show its base | **Fixed** |

Chapters: 1, 4. Tiers (2 distinct): `Adaptable` · `**Fixed**`.

**D27 · Feeds and traces: who is in the record**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 4.28 | Report platform and transactional feeds as within-sample comparisons unless the selection has been measured against a benchmark; state coverage | **Fixed** as a stance |
| 4.31 | For administrative sources, state why the organisation recorded it and who is not in it | **Fixed** |
| 6.1 | Before any behavioural figure is read, name the population the record observes and who it cannot see | **Fixed** |
| 9.24 | A trace is labelled for the population it records and used within-sample; its skew is stated | **Fixed** |

Chapters: 4, 6, 9. Tiers (2 distinct): `**Fixed** as a stance` · `**Fixed**`.

**D28 · Measuring use; measuring trust**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.6 | Design and measure use from the first day | **Fixed** |
| 10.24 | The site's own analytics count how the service is used, never who uses it, or run on consent | **Fixed** |
| 11.37 | The dashboard measures its own use as how, not who; publishes it aggregate and dated; and reads "those who interacted did better" with the confound named | **Fixed** as a stance |
| 15.18 | Count reach in the unit counted and name it, never as "readers"; measure use only by asking, and print the response rate | **Fixed** (procedure) |
| 1.14 | Treat trust as earned by conduct — trustworthiness, quality, value — not sought from the display | **Fixed** (adopted voluntarily) |
| 15.1 | Measure trust, if at all, with a fixed question in waves, of those able to express a view; never report an on-site percentage as trust | **Fixed** (procedure) |

Chapters: 1, 10, 11, 15. Tiers (4 distinct): `**Fixed**` · `**Fixed** as a stance` · `**Fixed** (procedure)` · `**Fixed** (adopted voluntarily)`.

**D29 · The stigma check on colour and area**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 10.37 | No panel grades or ranks places, and where a value is drawn by colour the scale is checked for stigma; a money view is lit for a scene only after its governance has agreed, the speculation reading has been assessed, and both are on the record | **Fixed** as a stance |
| 10.38 | Colour and area are checked for stigma: no red or dark for low, no dominance of large empty areas, and "fewer" never drawn as "nothing" | **Fixed** |
| 11.35 | The stigma check runs on every map before publication: no red or dark for low; large empty areas do not dominate; missing is not zero; the held category is coarsened | **Fixed** |

Chapters: 10, 11. Tiers (2 distinct): `**Fixed** as a stance` · `**Fixed**`.

**D30 · Name the purchase**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 11.16 | Every interaction names its purchase from the table and its costs from the seven, or is cut; the static reading works before it is added | **Fixed** as a procedure |
| 14.3 | Name the purchase in the affective-intent template, limited to what expression is measured to buy | **Fixed** (stance) |

Chapters: 11, 14. Tiers (2 distinct): `**Fixed** as a procedure` · `**Fixed** (stance)`.

**D31 · Felt questions cognitively tested; validity argued from five sources**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 5.18 | Cognitively test any felt-quality question before use; present felt qualities as a small panel unless a combination is separately validated | **Fixed** (test); Adaptable (combine) |
| 9.31 | A new felt item is cognitively tested before it is asked, placed with known context effects, and administered in a stated mode | **Fixed** as a procedure |
| 5.15 | Validate a reading for a use, under the five sources of evidence; state reliability first, including inter-rater reliability for any judged score | **Fixed** |
| 9.32 | Validity is claimed for an interpretation and a use, argued from the five sources; the record says which have evidence and which say "not yet" | **Fixed** |

Chapters: 5, 9. Tiers (3 distinct): `**Fixed** (test); Adaptable (combine)` · `**Fixed** as a procedure` · `**Fixed**`.

**D32 · Precision and significant figures**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.18 | Two or three significant figures; never more precision than the data has; frequencies ("9 in 100") where chance is involved | **Fixed** (ceiling); Adaptable (digits) |
| 5.10 | Report composite scores to two effective digits unless the inputs justify more; never imply a resolution the inputs lack | **Fixed** |

Chapters: 3, 5. Tiers (2 distinct): `**Fixed** (ceiling); Adaptable (digits)` · `**Fixed**`.

**D33 · The word "significant"**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 6.28 | No "significant" badge standing alone as the reason for a highlight or a decision; an error-controlled highlighting rule is not a badge | **Fixed** |
| 7.20 | Do not use "significant" of a change unless making a point about statistical significance | **Fixed** |

Chapters: 6, 7. Tiers (1 distinct): `**Fixed**`.

**D34 · The phone / small screen first**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.19 | Nothing crucial behind a click, a hover or a tooltip; everything crucial reachable by keyboard and on a phone | **Fixed** |
| 3.26 | Plan for a reader at PIAAC Level 1 and with low graph literacy; test with them | **Fixed** as the planning assumption |
| 8.24 | The page is budgeted for the seventy-fifth-percentile phone and network, not the builder's, and tested on one | **Fixed** as a stance |
| 8.25 | Figures and the table are in the HTML and shown before any script runs; the page is not a single-page application | **Fixed** as a stance |
| 11.8 | The small screen is designed first; what is removed for it is recorded as not the message; no hover content is load-bearing | **Fixed** |
| 11.9 | On a phone, linear layouts and small multiples are the defaults over radial forms and animation | Adaptable |
| 13.2 | The phone layout conforms as a page in its own right | **Fixed** |

Chapters: 3, 8, 11, 13. Tiers (4 distinct): `**Fixed**` · `**Fixed** as the planning assumption` · `**Fixed** as a stance` · `Adaptable`.

**D35 · Name the reader and the decision first**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.1 | Name the reader and the decision before any display is designed | **Fixed** |
| 2.1 | Name each reader, the decision they make, the evidence they are obliged to accept and the clock they keep, before design; declare whose grammar the first screen speaks | **Fixed** |
| 11.3 | A dashboard is justified before it is built: a named reader, data updated often enough to revisit, a need for combination, and the resource to maintain it; otherwise charts with specific insights | **Fixed** as a procedure |

Chapters: 1, 2, 11. Tiers (2 distinct): `**Fixed**` · `**Fixed** as a procedure`.

**D36 · Who benefits — distribution shown**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 2.6 | Show "who benefits" — distribution across groups and places — as a panel, not a footnote | **Fixed** |
| 6.16 | Show distributional figures weighted beside unweighted, with the weight and its source | **Fixed** |

Chapters: 2, 6. Tiers (1 distinct): `**Fixed**`.

**D37 · "Not done" is written, not hidden**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 6.43 | Record the ten-line claim record beneath every statement of value; "not done" is written, not hidden | **Fixed** as a stance |
| 7.1 | Every comparison carries the comparison record: what is held equal, who chose the comparators, the standardisation, the order, the interval, the season, the base month, the design, the ripple, the future's terms; a line that cannot be filled says "not done" | **Fixed** as a stance |
| 8.34 | The record's last line states what the dashboard does not promise | **Fixed** as a stance |

Chapters: 6, 7, 8. Tiers (1 distinct): `**Fixed** as a stance`.

**D38 · Animation and motion**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.22 | Small multiples for analysis; animation only for transitions between states of the same chart, or for presentation with the static version available | **Fixed** |
| 13.16 | Auto-updating views can be paused; moving content that lasts more than five seconds can be stopped | **Fixed** |
| 13.17 | The reduced-motion preference is honoured and motion from interaction can be disabled | **Fixed** as a stance |

Chapters: 3, 13. Tiers (2 distinct): `**Fixed**` · `**Fixed** as a stance`.

**D39 · Map controls have buttons**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 8.31 | Every map has a non-map twin — the same figures by the same places as a table — reachable before the script; pan and zoom have buttons; the sequential ramp is short | **Fixed** |
| 11.20 | Every control works by keyboard and by a single pointer without a path or a drag; maps have buttons for zoom and pan | **Fixed** |

Chapters: 8, 11. Tiers (1 distinct): `**Fixed**`.

**D40 · Radial forms and filled profiles**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 3.10 | Build first screens from fast-glance forms; avoid radial bars for comparison | Adaptable (strong default) |
| 11.9 | On a phone, linear layouts and small multiples are the defaults over radial forms and animation | Adaptable |
| 12.16 | A profile is small multiples of linear marks in a fixed, stated axis order, never a filled area; the form is held open to test | **Fixed** as a stance, form Adaptable |

Chapters: 3, 11, 12. Tiers (3 distinct): `Adaptable (strong default)` · `Adaptable` · `**Fixed** as a stance, form Adaptable`.

**D41 · The rule that carries each record (one per chapter, 4–15)**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 4.7 | Ship the provenance set with every figure: responsible party; source and why; method and deviations; period; issued and modified; status; quality with error; what was withheld; what it may be compared with | **Fixed** |
| 5.23 | Publish the recipe as a standard card, one tap from any composed number, with the fact of composition visible beside the number | **Fixed** |
| 6.43 | Record the ten-line claim record beneath every statement of value; "not done" is written, not hidden | **Fixed** as a stance |
| 7.1 | Every comparison carries the comparison record: what is held equal, who chose the comparators, the standardisation, the order, the interval, the season, the base month, the design, the ripple, the future's terms; a line that cannot be filled says "not done" | **Fixed** as a stance |
| 8.1 | Every dashboard that intends to be read next year carries, published beside it, the service record: freshness promise, dependencies, refresh, watch and alarm, availability and degraded mode, budget and device, map supply, retirement, owner, not-done | **Fixed** as a stance |
| 9.1 | Every felt measure carries the measure record: construct and register, items, who chose, who was asked, who answered, the spread, the five sources of validity evidence, recognition, discordance, what this changed | **Fixed** as a stance |
| 10.1 | Every dashboard that shows people carries the safeguards record: what is held and about whom, the basis, the release model, the method per view, the query-time controls, the walk, who was consulted, who governs and who stood at the door, the held layer, withdrawal, harm, regimes, moderation, review and what this changed | **Fixed** as a stance |
| 11.1 | Every view carries a face sheet: the sentence, the pattern and first state, what of each record sits on the face, the nothings, the interactions and their costs, hover and pointer routes, the small-screen form, the state and its address, the snapshot and citation, words, map and colour, tests and review | **Fixed** as a stance |
| 12.39 | The recognition record, ten lines, sits beneath every place-page | **Fixed** as a procedure |
| 13.23 | The house publishes an accessibility statement in the public sector's model form with the twelve lines, per view, dated within twelve months | **Fixed** as a procedure |
| 14.2 | Record each element in the boundary log, eleven lines, before it ships | **Fixed** (procedure) |
| 15.21 | Record every borrowed mechanism in the precedent record, nine lines, with its status, before it ships | **Fixed** (procedure) |

Chapters: 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15. Tiers (4 distinct): `**Fixed**` · `**Fixed** as a stance` · `**Fixed** as a procedure` · `**Fixed** (procedure)`.

**D42 · The residual rows: "open choices" and Decorative (same row shape repeated chapter to chapter)**

| Ch.# | Rule, as printed | Tier, as printed |
|---|---|---|
| 1.18 | The job, the layering, the degree of framing, the order of failures to prevent, the amount of mud | Adaptable |
| 1.19 | Register, imagery, metaphor | *Decorative* |
| 2.25 | Which reader comes first (declared); monetise/quantify/describe; the plain-table view; where lived experience sits; which numbers the investor sees; documenting between windows | Adaptable |
| 2.26 | Register, imagery, metaphor | *Decorative* |
| 3.28 | Which chart below the top of the hierarchy; how many colours; how much text; convention or novelty at first glance; which uncertainty form; line-axis breaks; overview or search; animation or multiples; rounding | Adaptable |
| 3.29 | Register, imagery, metaphor, texture around the chart | *Decorative* |
| 4.38 | Which grain, which day boundary, which denominator, which concentration instrument, whether a seventh kind of nothing, how a nothing looks, how much provenance on the face, suppress or perturb, which outlier rule, which neighbours | Adaptable |
| 4.39 | How the labels, codes, gaps and provenance panels are styled | *Decorative* |
| 5.26 | Which form; which construct and parts; who weights; which aggregation and tail; how much of the card on the face; how recognition is gathered; how the audit runs | Adaptable |
| 5.27 | How the card, the sliders, the profile shape and the interval are styled | *Decorative* |
| 12.40 | How the holes are drawn; how the columns are composed; the profile's visual language | *Decorative* |
| 13.33 | How the routes look and sound; the reduced-motion page; the structure's narration style | *Decorative* |
| 14.19 | Everything else in the register — palette beyond the encoding, display type, illustration, pattern, imagery, pacing, the poster layer, stoppable sound, disableable motion | *Decorative* |
| 15.22 | Which of section 9's mechanisms beyond the above to adopt, and when their conditions are met | Adaptable |

Chapters: 1, 2, 3, 4, 5, 12, 13, 14, 15. Tiers (2 distinct): `Adaptable` · `*Decorative*`.

*42 groups; 204 distinct rows appear in at least one group.*

Rows in Chapters 6–11 have no residual "open choices" or Decorative row at all (see D42): those six tables end on a Fixed rule.

### 1.4 The senses of Fixed — what Chapter 0 says

Chapter 0, `ch00-how-to-read-this-book.md`, line 95, quoted in full:

> Two refinements the chapters use. A truth may be **Fixed as a statement of the record** — the evidence says this and the book will not pretend otherwise — without the design rule that follows from it being Fixed; the chapter says which. And a rule may be **Fixed as sequence**: the order of operations is the hard line (define the construct before the proxy; check recognition before release), while the form each step takes is Adaptable. Where you deviate from a Fixed or Adaptable rule, Chapter 16 gives the four-line record to keep and the test to run first.

The Tier table that this paragraph refines (ch00 L89–93), verbatim:

| Tier | Plain meaning | Breaking it is |
|---|---|---|
| **Fixed** | **A hard line.** There is a right answer and it can be checked: contrast, keyboard access, disclosure thresholds, provenance on every number, no league table of identities, no implied counterfactual. | Negligence. Do not do it for taste |
| **Adaptable** | **A default you may argue with.** There is no single right answer; the book states a position and the reasons. You may take a different one if you can defend it and you log it. | The job. Deviation is expected — with a record |
| **Decorative** | **Free.** Register, imagery, pacing, texture — provided nothing that carries meaning lives only there. | Expected |

The gap row that asks for the check (ch00 L197, "Gaps found while writing this chapter"), verbatim:

> | "Fixed" was being used for three things (a rule to obey; a fact the book is confident of; a sequence that is the hard line) and a cold reader of Chapter 2 could not tell which | Named the two refinements above — Fixed as a statement of the record; Fixed as sequence — so that chapters can say which they mean | Amber | Chapter 16's rule register should check every Fixed for which sense it carries |

So Chapter 0 names **three** uses of "Fixed" in its gap row ("a rule to obey; a fact the book is confident of; a sequence that is the hard line") and **two** named refinements in its legend ("**Fixed as a statement of the record**"; "**Fixed as sequence**"). The words "stance" and "procedure" do not occur anywhere in Chapter 0 (0 matches each for `stance` and `procedure` in the file).

Where "Fixed as a stance" and "Fixed as a procedure" are defined instead — in the chapters' own "Before you start" notes, in four different wordings:

- **Ch 5** (L12): "Fixed as a stance" marks a rule the studio adopts and will not reopen on a given display though its source is a reading or a practice; "Fixed as a procedure" fixes the steps and not the parameter.
- **Chs 6, 7, 8, 9, 10, 11** (L12 in each; identical wording): "Fixed as a stance" marks a rule the studio adopts whose source is a reading or a practice, and "Fixed as a procedure" fixes the steps and not the parameter.
- **Ch 12** (L12): "Fixed as a stance" means the house has decided it and the chapter gives the grounds; "Fixed as a procedure" means the rule is a thing to do, not a thing to believe.
- **Chs 13, 14, 15** (L12 in each; identical wording): "Fixed as a stance" means the house has decided it and the chapter gives the grounds; "Fixed as a procedure" means the rule is a thing to do.
- **Chs 1–4**: no definition of either qualifier in "Before you start" (Chapter 3 uses "as a stance" once and Chapter 4 uses both, undefined in the chapter's own note; Chapter 4's gap row G4.17 records this: "The Fixed tier was used with four qualifiers ("as a stance", "as a procedure", "adopted", "as disclosure") that Chapter 0 does not define").

### 1.5 The check — which sense each Fixed rule's Tier cell indicates

Method: the Tier cell is split at semicolons; each part containing "Fixed" is labelled by its own words — **procedure** (the part says "as a procedure" or "(procedure)"), **stance** ("as a stance" or "(stance)"), **sequence** ("as sequence"), **statement of the record**, **other qualifier** (a parenthesis or phrase that is none of these — e.g. "(adopted)", "(declared)", "(unit)", "as defaults", "as disclosure", "as the planning assumption"), or **unmarked** (the part is exactly `**Fixed**`). A part that says "Adaptable" is noted as an Adaptable part. The label for every row is in the last column of the register in 1.1. Nothing here judges which sense a rule *ought* to carry; it records only what the table says.

**Rows whose Tier cell contains "Fixed": 433.** By the combination of labels in the cell:

| Label(s) in the Tier cell | Rows |
|---|---|
| unmarked | 212 |
| procedure | 97 |
| stance | 80 |
| other qualifier + Adaptable part | 14 |
| other qualifier | 10 |
| stance + Adaptable part | 5 |
| procedure + Adaptable part | 5 |
| other qualifier + stance | 4 |
| Adaptable part + other qualifier | 3 |
| Adaptable part + sequence | 1 |
| sequence | 1 |
| unmarked + stance | 1 |
| **Total** | **433** |

**Rows carrying each label at least once** (a cell with two Fixed parts can carry two):

| Label | Rows | Share of the 433 |
|---|---|---|
| unmarked | 213 | 49.2% |
| procedure | 102 | 23.6% |
| stance | 90 | 20.8% |
| sequence | 2 | 0.5% |
| statement of the record | 0 | 0.0% |
| other qualifier | 31 | 7.2% |
| Adaptable part | 28 | 6.5% |

**The unmarked count.** **212** of the 433 Fixed-bearing rows (49.0%) say exactly `**Fixed**` and nothing more — the table does not say which sense is meant. One further row has an unmarked Fixed part beside a marked one (11.4: `**Fixed**; the house limit Fixed as a stance`).

| Ch | Fixed-bearing rows | unmarked (exactly `**Fixed**`) | procedure | stance | sequence | statement of the record | other qualifier | with an Adaptable part |
|---|---|---|---|---|---|---|---|---|
| 1 | 16 | 14 | 0 | 0 | 1 | 0 | 1 | 1 |
| 2 | 21 | 16 | 0 | 0 | 1 | 0 | 4 | 1 |
| 3 | 21 | 13 | 0 | 1 | 0 | 0 | 7 | 4 |
| 4 | 34 | 24 | 2 | 4 | 0 | 0 | 5 | 3 |
| 5 | 22 | 15 | 2 | 2 | 0 | 0 | 3 | 3 |
| 6 | 42 | 21 | 6 | 11 | 0 | 0 | 5 | 4 |
| 7 | 36 | 17 | 8 | 8 | 0 | 0 | 4 | 3 |
| 8 | 32 | 10 | 10 | 11 | 0 | 0 | 2 | 5 |
| 9 | 35 | 17 | 9 | 9 | 0 | 0 | 0 | 1 |
| 10 | 43 | 14 | 18 | 11 | 0 | 0 | 0 | 2 |
| 11 | 35 | 15 | 10 | 10 | 0 | 0 | 0 | 0 |
| 12 | 37 | 15 | 10 | 12 | 0 | 0 | 0 | 1 |
| 13 | 30 | 16 | 8 | 6 | 0 | 0 | 0 | 0 |
| 14 | 13 | 5 | 5 | 3 | 0 | 0 | 0 | 0 |
| 15 | 16 | 0 | 14 | 2 | 0 | 0 | 0 | 0 |
| **Total** | **433** | **212** | **102** | **90** | **2** | **0** | **31** | **28** |

**Rows marked "sequence" (the only two):** 1.15 — "Build the common ground before the screen; test recognition with each community" — `Adaptable in method; Fixed as sequence`; 2.23 — "Recognition is checked before release, as a dialogue that can change the next release" — `**Fixed** as sequence`.

**Rows marked "statement of the record": none.** The phrase is not in any rules table. It is printed in the "What holds true regardless" lists of Chapters 1 and 2 only — ch01 L249 (truth 3) and ch02 L385, L389, L393, L397 (four truths) — each ending "*Fixed as a statement of the record.*"

**Rows with an "other qualifier" (31), with the cell as printed:**

- 1.14 — `**Fixed** (adopted voluntarily)` — Treat trust as earned by conduct — trustworthiness, quality, value — not sought from the display
- 2.11 — `**Fixed** (adopted)` — Never add a chart for its air of science; add it for the information it carries
- 2.18 — `**Fixed** (show the decision)` — Decide openly whose reading a property-value or footfall figure serves, and show the choice
- 2.22 — `Adaptable in form; Fixed as a prohibition on the supplement pattern` — Do not place lived experience in a panel beside the numbers as a supplement
- 2.24 — `**Fixed** (adopted)` — Numbers for understanding, not numbers for advocacy: produce with caveats, release with data
- 3.2 — `**Fixed** for precise comparison; Adaptable as a general form rule` — For a precise ratio comparison, use position on a common scale, then length; do not ask for a precise reading from area or colour
- 3.5 — `**Fixed** (pattern maps); Adaptable where the task is reading a value` — Lightness for order, hue for category; no rainbow for ordered data on a pattern map
- 3.9 — `**Fixed** (evidential status stated)` — Label at the mark; legends only where labels cannot fit, and then ordered to match the data
- 3.13 — `Adaptable (strong default); the headline itself is Fixed under the words rule` — Declutter for professionalism; add a headline, one highlight and one sentence for recall
- 3.16 — `**Fixed** as defaults` — Public defaults: linear scale, daily flow with the cumulative available, absolute risk with a fixed denominator and a stated interval
- 3.18 — `**Fixed** (ceiling); Adaptable (digits)` — Two or three significant figures; never more precision than the data has; frequencies ("9 in 100") where chance is involved
- 3.26 — `**Fixed** as the planning assumption` — Plan for a reader at PIAAC Level 1 and with low graph literacy; test with them
- 4.1 — `**Fixed** (unit); **Fixed** as a stance (count)` — State the unit of observation (what one row is) and the count of rows beneath every figure
- 4.10 — `**Fixed** (adopted)` — Name who owns the display's figures and who assured them; assure in proportion to the weight of the decision
- 4.23 — `**Fixed** (adopted)` — A like-for-like or defined measure is defined, reconciled to an audited total, shown with comparators, held constant, and restated if redefined
- 4.25 — `**Fixed** (that one is shown); Adaptable (which)` — Beside any sum or mean of a skewed quantity, show the median and a concentration measure (top-share, Lorenz curve, Gini or HHI)
- 4.27 — `**Fixed** as disclosure` — Where a display ranks by popularity, say so and show the distribution: visible popularity increases concentration and unpredictability
- 5.3 — `**Fixed** (stated); Adaptable (which)` — State the normalisation and note that it sets exchange rates; prefer the method that matches the data's shape and the measure's purpose
- 5.8 — `**Fixed** (declared); Adaptable (which)` — Decide and declare whether the instrument is one-tailed (built to find shortfall, or thriving) or two-tailed
- 5.18 — `**Fixed** (test); Adaptable (combine)` — Cognitively test any felt-quality question before use; present felt qualities as a small panel unless a combination is separately validated
- 6.2 — `**Fixed** (stated); Adaptable (values)` — Treat distance as a price only with the method's assumptions stated: single purpose, a declared value of time, substitutes considered
- 6.7 — `**Fixed** (instrument); Adaptable (wording)` — Measure welcome with an instrument validated for belonging, re-tested in the scene's own wording, rather than with a proxy
- 6.27 — `**Fixed** (declared); Adaptable (which)` — Choose family-wise or false-discovery control for any highlighting rule, and say which
- 6.31 — `**Fixed** (two tests); **Fixed** as a stance (the described)` — A pattern becomes a canonical truth by two tests, out-of-sample and the agreement of the competent; the described are among the competent
- 6.34 — `**Fixed** (stated); Adaptable (values)` — Every alert states its false-alarm rate and its detection delay, worked out for the measure's own distribution and agreed with the people who answer it
- 7.4 — `**Fixed** (the principle); Adaptable (the form)` — Compare places on a funnel or against a declared expectation, never by sorted value alone; where a display is sorted, the sort is a reading aid and the finding is position against limits
- 7.6 — `**Fixed** (declared); Adaptable (whether)` — Standardise for the drivers of a rate before comparing places, or state that the rate is crude and why
- 7.15 — `**Fixed** (both ends; say which); Adaptable (which leads)` — A year-on-year figure shows both ends; a period-on-period figure uses the adjusted series; the display says which growth rate it leads with and why
- 7.31 — `**Fixed** (no single figure; say what is omitted); **Fixed** as a stance (even number)` — Scenarios say what they do not cover, and a single future figure is not shown; the default is an even number of scenarios, taken from the cross-government toolkit over the Bank's baseline-plus-two
- 8.2 — `**Fixed** (period); **Fixed** as a stance (four parts)` — Each series states the period it describes, the date published, the date last revised and its declared frequency; "last updated" alone is never shown
- 8.9 — `Adaptable (which interfaces signal); **Fixed** (that the job reads them)` — Response headers announcing deprecation and sunset are read by the refresh job and raise a ticket

**Chapter 0's own examples against the tables.** Chapter 0 L95 gives two examples of "Fixed as sequence": "define the construct before the proxy; check recognition before release". In the tables: the construct-before-proxy rule is 2.16 (`**Fixed**`), 5.1 (`**Fixed**`) and 9.2 (`**Fixed** as a stance`) — none marked as sequence; the recognition-before-release rule is 1.15 (`Adaptable in method; Fixed as sequence`), 2.23 (`**Fixed** as sequence`), then 5.19 and 9.33 (`**Fixed** as a stance`) and 12.36 (`**Fixed** as a procedure`).

---

## PART 2 — THE RECORDS BENEATH THE DASHBOARD

**What was expected and what is printed.** Twelve documents, one from each of Chapters 4–15, as expected. Three things differ from the expected description: (1) only **five** chapters use the words "Beneath the dashboard" in a heading (8, 10, 13, 14, 15); Chapters 9, 11 and 12 say "Beneath the measure", "Beneath the view" and "Beneath the page"; Chapters 6 and 7 put the document under `### The record beneath them`; Chapters 4 and 5 print theirs in the body of the chapter (under `### The minimal set` and `## 12 · The recipe on the face`) and use `### The record beneath them` for something else — a list of findings of record. (2) Only the eight records of Chapters 8–15 are printed as tables; those of Chapters 4–7 are lists. (3) Chapter 3 also has a `### The record beneath them` (L373) and leaves no document: like Chapters 4 and 5 it is the findings of record under "the seven". Chapters 0–3 leave no record. Chapter 0 names none of the twelve (0 matches for any of the twelve names).

| # | Ch | Name | Heading it sits under, as printed | Form | Lines | Unit it is kept per | Public / internal / log (as the chapter says) |
|---|---|---|---|---|---|---|---|
| 1 | 4 | the provenance set | `### The minimal set` (in §5) | bulleted list | 10 | every figure | not stated |
| 2 | 5 | "the recipe" / "the card" — called "the recipe card" only from Chapter 6 onward | `## 12 · The recipe on the face` | numbered list | 9 | every composed number / measure | published; one tap from the number |
| 3 | 6 | the claim record | `### The record beneath them` | numbered list | 10 | every statement of value | not stated |
| 4 | 7 | the comparison record | `### The record beneath them` | numbered list | 10 | every comparison | not stated |
| 5 | 8 | the service record | `### Beneath the dashboard: the service record` | table, 2 columns | 10 | the dashboard | public — "published beside the page" |
| 6 | 9 | the measure record | `### Beneath the measure: the measure record` | table, 2 columns | 12 | every felt measure | public — "published beside the panel" |
| 7 | 10 | the safeguards record | `### Beneath the dashboard: the safeguards record` | table, 2 columns | 14 | every dashboard that shows people | partly public, line by line ("published or not") |
| 8 | 11 | the face sheet | `### Beneath the view: the face sheet` | table, 2 columns | 12 | every view | not stated; "build artefact" |
| 9 | 12 | the recognition record | `### Beneath the page: the recognition record` | table, 3 columns | 10 | every place-page | not stated |
| 10 | 13 | the accessibility statement | `### Beneath the dashboard: the accessibility statement` | table, 3 columns | 12 | the dashboard, with lines per view | public — "also a public document" |
| 11 | 14 | the boundary log | `### Beneath the dashboard: the boundary log` | table, 3 columns | 11 | every expressive element (grows) | growing log; public or internal open |
| 12 | 15 | the precedent record | `### Beneath the dashboard: the precedent record` | table, 3 columns | 9 | every borrowed mechanism (grows) | growing list; "a working file" |
| | | **Twelve documents** | | 4 lists, 8 tables | **129** | | |

### 2.1 Chapter 4 — the provenance set

**Name and place, as printed.** Heading as printed: `### The minimal set` (L205), inside `## 5 · Provenance — what a number must carry`. The chapter's "What holds true regardless" has a subsection `### The record beneath them` (L460) but that subsection is a list of 21 findings of record, **not** this document. The name "provenance set" is the Decision Book's phrase, taken up by the chapter: rule 4.7 "Ship the provenance set with every figure…"; L653 "This chapter's provenance set is ten lines and its comparability declaration is ten more". There is no subsection headed "Beneath the dashboard" in Chapter 4.

**Lines.** 10 bullets (L209–218). Rule 4.7 restates nine of them in one cell; the tenth bullet ("the record must **outlive the number**") is rule 4.8. Chapter 4 also prints a second ten-line list, `### The declaration` (heading L328; items L332–341, the comparability declaration, numbered 1–10), which Chapter 7 makes line 1 of its comparison record. Form: a bulleted list of ten (not a table).

The lines, exactly as printed (file line in brackets; the line name is the bold text):

- [L209] - **who is responsible** for it (PROV agent; the Code's producer; the Macpherson review's single responsible owner);
- [L210] - **what source** it was derived from, and why that source was chosen (PROV derivation; Code 7.3);
- [L211] - **what method** generated it, and any deviation from a recognised standard (PROV activity; Code 6.7, 7.4);
- [L212] - **what period** it describes — the reference period, as a closed interval (DCAT temporal; Eurostat);
- [L213] - **when it was issued and when it last changed** — separately from the period (DCAT issued, modified; the vintage);
- [L214] - **what status** it has — provisional, revised, estimated, in development (Code 3.10, 7.6; the table shorthand);
- [L215] - **what quality** it claims, with error and confidence where they exist, in words, numbers or graphics (Code 7.2);
- [L216] - **what was withheld or altered** for confidentiality (Code 4.5; section 6);
- [L217] - **what it may be compared with** (Code 6.6, 9.3; section 7);
- [L218] - and the record must **outlive the number** (FAIR A2).

**Line names (first column / bold text), exactly:** `who is responsible` · `what source` · `what method` · `what period` · `when it was issued and when it last changed` · `what status` · `what quality` · `what was withheld or altered` · `what it may be compared with` · `outlive the number`

**Public, internal, or a growing log?** **Not stated as public or internal.** What the chapter says:

> (ch04 L504) Which lines are on the face (period, status, and the fact that caveats exist, at minimum) and which are one tap away is a layout decision for Chapter 11, bounded by the Code's "prominently" and the regulator's "succinct".

> (ch04 L653) This chapter's provenance set is ten lines and its comparability declaration is ten more; both cannot be on the face of every figure.

> (rule 4.7, L542, tier `**Fixed**`) Ship the provenance set with every figure: responsible party; source and why; method and deviations; period; issued and modified; status; quality with error; what was withheld; what it may be compared with

**Is it one document with the others?** Chapter 4 has no sentence asking whether the records are one document (there was only one record when it was written). The question is first put in Chapter 7 (L554, quoted under Chapter 7 below).

### 2.2 Chapter 5 — "the recipe" / "the card" — called "the recipe card" only from Chapter 6 onward

**Name and place, as printed.** Heading as printed: `## 12 · The recipe on the face` (L303); the lines are introduced by "The recipe has nine lines." (L307). The words "recipe card" do **not** occur in Chapter 5 (0 matches); Chapter 5 says "the recipe", "a card", "a standard card", "the card". The name "recipe card" is first printed in Chapter 6 L420 ("Chapter 5 for a recipe card beneath every measure"). `### The record beneath them` (L343) in Chapter 5 is, as in Chapter 4, a list of findings of record, not this document.

**Lines.** 9 numbered lines (L309–317). Form: a numbered list of nine (not a table).

The lines, exactly as printed (file line in brackets; the line name is the bold text):

- [L309] 1. **The construct, in a sentence**, and the theoretical framework that connects it to the parts — the handbook's first step; Cronbach and Meehl's net.
- [L310] 2. **The parts**: each indicator, with Chapter 4's provenance set for each (unit, period, base, source, status).
- [L311] 3. **The normalisation**, and the fact that it sets exchange rates (Munda and Nardo).
- [L312] 4. **The nominal weights and who set them** — statistics, experts, the public, the reader, or nobody ("equal weighting does not mean 'no weights'") — **and the effective importances beside them** (Paruolo; Becker).
- [L313] 5. **The aggregation rule and the price list it implies**: for an additive index, the rate at which each part exchanges for each other, in the parts' own units — the refusal test version 1 posed and this chapter keeps as a Nightlife Culture rule: *how many new venues does the measure say compensate for the loss of one forty-year-old institution?* If the display cannot answer, the measure is not ready. (The test is a values test, not a method test: method says the rate exists and must be shown; whether a given rate is acceptable is the studio's judgement, and the test makes the studio state it.)
- [L314] 6. **The rank with its interval**, from a published sensitivity analysis over the defensible alternatives (Saisana; the JRC audits), and the score at no more digits than the inputs support (two effective digits; the ONS).
- [L315] 7. **The validity evidence** under the five headings — content, response process, internal structure, relations to other variables (convergent and discriminant, including against platform coverage), consequences — with reliability stated, including inter-rater reliability wherever a judgement was scored.
- [L316] 8. **The recognition record**: who was asked whether they see themselves in it, what they corrected, and who chose the parts (Sen's public reasoning; the member-check literature's limits).
- [L317] 9. **The audit design**: how it will be known whether the measured thing moved and not only the measure — the independent check Hood found missing — and what the builder will do when the measure starts to be gamed (Campbell's "multiple indicators, all recognized as imperfect").

**Line names (first column / bold text), exactly:** `The construct, in a sentence` · `The parts` · `The normalisation` · `The nominal weights and who set them … and the effective importances beside them` · `The aggregation rule and the price list it implies` · `The rank with its interval` · `The validity evidence` · `The recognition record` · `The audit design`

**Public, internal, or a growing log?** **Published; one tap from the number.** What the chapter says:

> (ch05 L319) Nine lines cannot all sit beside every number, and Chapter 4 proposed the resolution: the *fact* that a number is composed, and that its recipe exists, is visible on the face; the recipe is one tap away, and it is a document, not a tooltip.

> (ch05 L319) The *dataset nutrition label*: "a distilled yet comprehensive overview of dataset 'ingredients'", which "creates an expectation of explanation, which will drive better data collection practices." A card — the recipe in nine lines, in a standard form, one tap from the score — is the dashboard's version of all three; its design is Chapter 11's and the design system's.

> (ch05 L321) This chapter can now say what "adopted" must mean, as a Nightlife Culture rule with the handbook behind it: the ten steps walked and written down; the weights and aggregation chosen as judgements and declared as such; the sensitivity analysis run; the validity evidence gathered under the five headings; the recognition recorded; and the card published.

> (rule 5.23, L431, tier `**Fixed**`) Publish the recipe as a standard card, one tap from any composed number, with the fact of composition visible beside the number

**Is it one document with the others?** No sentence in Chapter 5 asks whether the records are one document.

### 2.3 Chapter 6 — the claim record

**Name and place, as printed.** Heading as printed: `### The record beneath them` (L418) — here, unlike Chapters 3–5, the subsection *is* the document. Name printed in bold in L420: "a **claim record** beneath every statement of value".

**Lines.** 10 numbered lines (L422–431), "Ten lines, as a floor." Form: a numbered list of ten (not a table).

The lines, exactly as printed (file line in brackets; the line name is the bold text):

- [L422] 1. **What was observed** — the behaviour, count or price, in Chapter 4's terms: unit, period, base.
- [L423] 2. **Who is in the record** — the population the source observes, and who it cannot see.
- [L424] 3. **Gross or net** — and if net, which of deadweight, displacement, leakage, substitution and multipliers were applied, from what source, bespoke or borrowed.
- [L425] 4. **Created or captured** — whether the figure is a product or a price, and if a price, whose position it rewards.
- [L426] 5. **For whom** — the distributional reading, weighted beside unweighted, with the weight and its source.
- [L427] 6. **The rung** — observational; interventional with a named comparison; counterfactual by argument only — and the verb that matches it.
- [L428] 7. **The alternatives considered** — the other explanations, in Hill's sense, and what was found against each.
- [L429] 8. **Noticed on** — the date and view in which the pattern was first seen, and whether it has yet been tested outside them.
- [L430] 9. **The model's known wrongness** — what the baseline, forecast, score or shrinkage cannot see, and the date it was last validated and on what.
- [L431] 10. **The small-number treatment** — direct or modelled; the interval; the shrinkage weight; and, if withheld, whether for confidentiality or precision.

**Line names (first column / bold text), exactly:** `What was observed` · `Who is in the record` · `Gross or net` · `Created or captured` · `For whom` · `The rung` · `The alternatives considered` · `Noticed on` · `The model's known wrongness` · `The small-number treatment`

**Public, internal, or a growing log?** **Not stated as public or internal;** "beneath every statement of value", and a visible "not done". What the chapter says:

> (ch06 L420) This chapter asks for a **claim record** beneath every statement of value — the lines that let a reader see what kind of claim they are looking at.

> (ch06 L433) Most of these lines will say "not done" for most figures on most dashboards.

> (ch06 L433) A "not done" that is visible is a boundary; a "not done" that is hidden is an overclaim.

> (ch06 L616) - `[Revisit → Ch 11]` How much of the claim record sits on the face.

> (rule 6.43, L533, tier `**Fixed** as a stance`) Record the ten-line claim record beneath every statement of value; "not done" is written, not hidden

**Is it one document with the others?** No sentence in Chapter 6 asks whether the records are one document; L420 only lists the three ("Chapter 4 asked for a provenance set beneath every number and Chapter 5 for a recipe card beneath every measure.").

### 2.4 Chapter 7 — the comparison record

**Name and place, as printed.** Heading as printed: `### The record beneath them` (L376). Name printed in bold in L378: "a **comparison record** beneath every comparison".

**Lines.** 10 numbered lines (L380–389), "Ten lines, as a floor; the first is Chapter 4's declaration and the rest are this chapter's." Form: a numbered list of ten (not a table).

The lines, exactly as printed (file line in brackets; the line name is the bold text):

- [L380] 1. **What is held equal** — Chapter 4's ten-line comparability declaration for the indicator: same definition, unit, period, base, source, coverage, revision status; and, for a borrowed series, cash or real, who is still in it, and any breaks or vintages.
- [L381] 2. **The comparators, who chose them, and why this place** — the places or periods compared; the published method, its distance and its fixed number; or "chosen by the place", labelled; and whether the place was selected for the comparison because its figure was extreme.
- [L382] 3. **The standardisation** — what the figure has been adjusted for (size, age, mix), against what expectation; or "crude", stated.
- [L383] 4. **The order on the display** — whether the display sorts the places, by what, and whether the sort is a reading aid or the finding.
- [L384] 5. **The interval** — the uncertainty on each place's figure, and whether the places can be separated; the funnel's limits, if a funnel.
- [L385] 6. **The season and the smoothing** — raw, seasonally adjusted (by what method, revised when, series length) or trend-cycle (what window); and whether the latest point is an end-point estimate.
- [L386] 7. **The base month, and the record** — for any year-on-year figure, what happened twelve months earlier; for any series called "leading", its measured record of turning points against a named reference series.
- [L387] 8. **The design, and its assumption** — for any before/after: none (Design 2, with the eight rivals listed), interrupted series (impact model chosen when), difference-in-differences (comparison group; pre-trend check; adoption timing), synthetic control (weights; placebos run), cut-off, match; and the rung on the ladder.
- [L388] 9. **The ripple** — spillover and displacement considered; the neighbour used as a control, and whether it was reached.
- [L389] 10. **The future's terms** — for any projection: the label; the assumptions; the central estimate and range; the switching value; the number of scenarios; the optimism-bias adjustment and its source; the record of past projections against outturn.

**Line names (first column / bold text), exactly:** `What is held equal` · `The comparators, who chose them, and why this place` · `The standardisation` · `The order on the display` · `The interval` · `The season and the smoothing` · `The base month, and the record` · `The design, and its assumption` · `The ripple` · `The future's terms`

**Public, internal, or a growing log?** **Not stated as public or internal;** "beneath every comparison"; unfilled lines say "not done". What the chapter says:

> (ch07 L378) This chapter asks for a **comparison record** beneath every comparison — the lines that let a reader see what was held equal and by whom.

> (ch07 L550) - `[Revisit → Ch 11]` How much of the comparison record sits on the face; the funnel as a first-screen object.

> (ch07 L486) - [ ] The comparison record exists beneath every comparison; unfilled lines say "not done"

> (rule 7.1, L439, tier `**Fixed** as a stance`) Every comparison carries the comparison record: what is held equal, who chose the comparators, the standardisation, the order, the interval, the season, the base month, the design, the ripple, the future's terms; a line that cannot be filled says "not done"

**Is it one document with the others?** First chapter to ask the question:

> (ch07 L554) - `[Revisit at end]` **The comparison record and the three records before it.** Chapters 4, 5, 6 and 7 now ask for a provenance set, a recipe card, a claim record and a comparison record; the closing chapter should say whether they are one document with four parts.

> (ch07 L575) - **Opens a thread** for Chapter 0: four records now sit beneath a dashboard's numbers (provenance set, recipe card, claim record, comparison record); the legend should say whether they are one; and "Fixed as a procedure" has become the commonest tier in the book for rules whose steps are fixed and whose parameters are judgements.

> (ch07 L697) | Four records now sit beneath a dashboard's numbers across Chapters 4–7 | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

### 2.5 Chapter 8 — the service record

**Name and place, as printed.** Heading as printed: `### Beneath the dashboard: the service record` (L524) — the first use of "Beneath the dashboard" as a heading.

**Lines.** 10 table rows (L530–539), numbered "1 · … 10 ·". Form: a table, columns `Line | What it states`.

The table, exactly as printed (with the file line added):

| L | Line | What it states |
|---|---|---|
| 530 | 1 · Freshness promise | For each series: period described, published, last revised, declared frequency; the page's own freshness lifetime, in days, and where it is shown |
| 531 | 2 · Dependencies | Each interface, file and host the page needs — at build time and at read time, marked which — with its stated limit, its terms (supply or terms), the notice it has promised, and the date its page was read |
| 532 | 3 · Refresh mechanism | What runs, where, on what schedule, off the hour; what it fetches and what it commits; that it can be run twice safely |
| 533 | 4 · Watch and alarm | What checks that the data's date advanced, independent of the job; where the ticket goes — a role, not a person — and who is second |
| 534 | 5 · Availability target and degraded mode | The objective in the data's terms ("the oldest figure is never more than N days behind, 11 months in 12"); what the page shows when a fetch fails, series by series; when the degraded mode was last exercised |
| 535 | 6 · Budget and baseline device | The byte budget; the device and network it was tested on; what the page shows before any script runs |
| 536 | 7 · Map supply, licence and vintage | Which of the four supplies; what has been agreed to (cache, attribution, logo, offline, non-commercial); the boundary product and its date; the renderer and its weight; where the twin is |
| 537 | 8 · Retirement plan and archive | How a series ends when its source closes: the notice given, what is archived, where the last state stays reachable; how the whole page ends |
| 538 | 9 · Owner and successor | Whose job the ticket is; who takes it when they leave; where this record lives |
| 539 | 10 · Not done | What the record declines to promise, and why |

**Line names (first column / bold text), exactly:** `1 · Freshness promise` · `2 · Dependencies` · `3 · Refresh mechanism` · `4 · Watch and alarm` · `5 · Availability target and degraded mode` · `6 · Budget and baseline device` · `7 · Map supply, licence and vintage` · `8 · Retirement plan and archive` · `9 · Owner and successor` · `10 · Not done`

**Public, internal, or a growing log?** **Public — "published beside" the page.** What the chapter says:

> (ch08 L526) The *service record* is written before the dashboard launches, by the person who will keep it, and it answers ten questions.

> (ch08 L650) - [ ] The service record exists, is dated, and is published beside the page

> (rule 8.1, L603, tier `**Fixed** as a stance`) Every dashboard that intends to be read next year carries, published beside it, the service record: freshness promise, dependencies, refresh, watch and alarm, availability and degraded mode, budget and device, map supply, retirement, owner, not-done

**Is it one document with the others?** 

> (ch08 L526) The truths are kept by a record, as Chapters 4 to 7 each produced one — the provenance set, the recipe card, the claim record and the comparison record — and whether these five are one document is a question for the end of the book `[Revisit at end]`. The *service record* is written before the dashboard launches, by the person who will keep it, and it answers ten questions. Each line is short; the point is that each is answered, and that the last — what is not promised — is answered too, because section 7 showed that a year of silent reliability makes a promise whether or not one was written.

> (ch08 L695) - `[Revisit at end]` **Five records.** The provenance set (Ch 4), recipe card (Ch 5), claim record (Ch 6), comparison record (Ch 7) and service record (Ch 8) may be one document with five parts; the service record's line 2 overlaps the provenance set's source lines. Chapter 0 should say.

> (ch08 L892) | Five records now sit beneath a dashboard's numbers across Chapters 4–8 | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

### 2.6 Chapter 9 — the measure record

**Name and place, as printed.** Heading as printed: `### Beneath the measure: the measure record` (L466) — "Beneath the **measure**", not "Beneath the dashboard".

**Lines.** 12 table rows (L472–483), numbered "1 · … 12 ·". Form: a table, columns `Line | What it states`.

The table, exactly as printed (with the file line added):

| L | Line | What it states |
|---|---|---|
| 472 | 1 · Construct and register | What the measure is of, in words; which register (made / perceived / excess); reflective or formative; what it is not |
| 473 | 2 · Items and format | The questions as asked, their scale and anchors, the language(s), and where the words came from (standard, adapted, the scene's own) |
| 474 | 3 · Who chose what counts | How the items were arrived at and with whom; what was proposed and dropped |
| 475 | 4 · Who was asked, how, when, where | Recruitment route; in situ or later; mode; moment; the place as defined to the respondent |
| 476 | 5 · Who answered and who did not | n per place and period; response rate where known; the known gaps; the share contributed by the most active |
| 477 | 6 · The spread | The distribution and its bands; the cut-points and how they were chosen; the official floor applied |
| 478 | 7 · Response-process evidence | Cognitive interviews: how many, in what rounds, what changed |
| 479 | 8 · Internal structure and reliability | Do the items hang together (reflective) or build as intended (formative); reliability and test–retest where known |
| 480 | 9 · Relations to other variables | Known-groups and convergent tests run; what the measure moved with and did not; the trace or signal indicators checked against it |
| 481 | 10 · Recognition | Member checking: who was shown what, when, what they said, what changed; the legitimacy claim stated |
| 482 | 11 · Discordance | Where this measure disagrees with the counted layers; the matrix cell; what was done about it |
| 483 | 12 · What this changed | What the measure has been used for; what the people in it were told; the consequences evidence gathered since launch |

**Line names (first column / bold text), exactly:** `1 · Construct and register` · `2 · Items and format` · `3 · Who chose what counts` · `4 · Who was asked, how, when, where` · `5 · Who answered and who did not` · `6 · The spread` · `7 · Response-process evidence` · `8 · Internal structure and reliability` · `9 · Relations to other variables` · `10 · Recognition` · `11 · Discordance` · `12 · What this changed`

**Public, internal, or a growing log?** **Public — "published beside the panel"** (checklist); opened before the first person is asked. What the chapter says:

> (ch09 L468) The *measure record* has twelve lines; it is opened before the first person is asked and filled as the work proceeds.

> (ch09 L595) - [ ] The measure record exists, is dated, and is published beside the panel

> (ch09 L487) Several of its lines say "not yet", and a record whose lines say so is a record a sceptical reader can trust more than one that does not.

> (rule 9.1, L545, tier `**Fixed** as a stance`) Every felt measure carries the measure record: construct and register, items, who chose, who was asked, who answered, the spread, the five sources of validity evidence, recognition, discordance, what this changed

**Is it one document with the others?** 

> (ch09 L468) Chapters 4 to 8 each left a record beneath a dashboard's numbers — the provenance set, the recipe card, the claim record, the comparison record, the service record — and whether they are one document is for the end of the book `[Revisit at end]`. A felt measure needs its own, because none of the five says who was asked how they felt and how the asking was tested. The *measure record* has twelve lines; it is opened before the first person is asked and filled as the work proceeds.

> (ch09 L649) - `[Revisit at end]` **Six records.** The provenance set, recipe card, claim record, comparison record, service record and measure record; whether they are one document; whether the measure record's line 12 and the service record's "what this changed" are the same field.

> (ch09 L852) | Six records now sit beneath a dashboard's numbers | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

### 2.7 Chapter 10 — the safeguards record

**Name and place, as printed.** Heading as printed: `### Beneath the dashboard: the safeguards record` (L612).

**Lines.** 14 table rows (L618–631), numbered "1 · … 14 ·". Form: a table, columns `Line | What it states`.

The table, exactly as printed (with the file line added):

| L | Line | What it states |
|---|---|---|
| 618 | 1 · What is processed, about whom | The unit (person, venue, area, scene); whether each layer is personal, pseudonymised or anonymous information, and on what test; whether special-category data is present or inferable, and whether any inference is the studio's |
| 619 | 2 · Lawful basis and its test | The basis per purpose; the legitimate interests assessment or the consent record; whether the research and statistics provisions are relied on, and the counsel's view of the fit; the date the statute was read |
| 620 | 3 · Release model and environment | Public, registered, or not shown, per layer; what other data about the same people and places is already public; who else holds what |
| 621 | 4 · Disclosure method per view | The disclosure floor per view and how it was set against the scene's knowability; suppression (primary and secondary), rounding, banding or perturbation; fixed classifications or the cap on combinations; consistency across views; the precision floor, separately |
| 622 | 5 · Query-time controls | What a reader can combine, move or redefine; the limit on overlapping views; registration for deeper views, if any; the log and who audits it; what is not shown and whether the kind or the rule is stated |
| 623 | 6 · The intruder's walk | Who walked, when, for how long, knowing what; each claim and its confidence; what changed before release; the next walk's date |
| 624 | 7 · Who was consulted | The DPIA's step 3 and Article 35(9): who, how, when; what they said; what changed; whether the assessment is published |
| 625 | 8 · Who governs, and who stood at the door | The scene's body for the held layer and how it was constituted; the gatekeepers through whom it was reached; the form and renewal of its agreement, and what that agreement is understood to add |
| 626 | 9 · The held layer | What is held, as a category and never as a marked unit; at what coarser resolution it is shown, if at all; who decided and by what process; the reason, in public, for the category; the walk's test that the held units cannot be recovered from public lists; the review date |
| 627 | 10 · Withdrawal | The tiers available to a contributor; the cut-off; what cannot be undone and why; how and when the contributor was told |
| 628 | 11 · Harm assessment | Harms to persons (the regulator's list), to groups (inference, discrimination, findability), to places (stigma, speculation, the ecological fallacy); the panels that carry each; the mitigations and the residue; published or not |
| 629 | 12 · Regimes in scope | Equality Act (service to the public; accessible format; hosted content); Online Safety Act status, risk tier and the named accountable individual; the children's test applied and its evidence; PECR for the site's own analytics; the emotion-inference line |
| 630 | 13 · Moderation and audit | The verbs and adverbs chosen; the gating rules; the reporting and complaints routes; the audit's schedule and last date; what gaming was found |
| 631 | 14 · Review, incident, and what this changed | The record's review date against the current law; the plan if things go wrong and the commitment to be transparent about a breach; after launch, who benefited from being made visible and who paid — the extraction question, answered with evidence |

**Line names (first column / bold text), exactly:** `1 · What is processed, about whom` · `2 · Lawful basis and its test` · `3 · Release model and environment` · `4 · Disclosure method per view` · `5 · Query-time controls` · `6 · The intruder's walk` · `7 · Who was consulted` · `8 · Who governs, and who stood at the door` · `9 · The held layer` · `10 · Withdrawal` · `11 · Harm assessment` · `12 · Regimes in scope` · `13 · Moderation and audit` · `14 · Review, incident, and what this changed`

**Public, internal, or a growing log?** **Partly public, by line — the record itself says "published or not".** Lines 7 and 11 each record whether the assessment is published; the chapter speaks of the record "published beside a panel" only as a question handed to Chapter 11. What the chapter says:

> (ch10 L614) Its first line is written before the first row is collected; it is dated, it names a person, and it is re-read against the current law on a stated schedule.

> (ch10 L810) - `[Revisit → Ch 11]` The display of the three nothings; the status of a held layer on the first screen; colour and area rules against stigma; what a safeguards record looks like when it is published beside a panel.

> (ch10 L635) Several of its lines say "open" or "not yet", and a record whose lines say so is one a sceptical reader, a regulator or a scene can trust more than one that does not.

> (rule 10.1, L693, tier `**Fixed** as a stance`) Every dashboard that shows people carries the safeguards record: what is held and about whom, the basis, the release model, the method per view, the query-time controls, the walk, who was consulted, who governs and who stood at the door, the held layer, withdrawal, harm, regimes, moderation, review and what this changed

> (rule 10.2, L694, tier `**Fixed** as a procedure`) The first line of the record is written before the first row is collected, is dated, and names a person

> (rule 10.23, L715, tier `**Fixed** as a procedure`) The house does a DPIA for any dashboard that combines sources, re-uses public data, tracks location or behaviour, or profiles — the regulator requires one for the first and, combined with another criterion, for the others; it seeks the views of those affected or their representatives; it is published unless there is a stated reason

**Is it one document with the others?** 

> (ch10 L614) Chapters 4 to 9 each left a record — the provenance set, the recipe card, the claim record, the comparison record, the service record, the measure record — and whether they are one document is for the end of the book `[Revisit at end]`.

> (ch10 L812) - `[Revisit at end]` **Seven records.** Provenance set, recipe card, claim record, comparison record, service record, measure record, safeguards record — whether one document; whether the measure record's line 12, the service record's "what this changed" and this record's line 14 are one field.

> (ch10 L1064) | Seven records now sit beneath a dashboard's numbers | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

### 2.8 Chapter 11 — the face sheet

**Name and place, as printed.** Heading as printed: `### Beneath the view: the face sheet` (L388) — "Beneath the **view**". The chapter says it is "not an eighth record about the data but a sheet about the *surface*" (L390); Chapter 12 nonetheless counts its own as "a ninth" and Chapter 14 L16 lists "the face sheet (11)" among "the ten documents".

**Lines.** 12 table rows (L394–405), numbered "1 · … 12 ·"; one sheet per view. Form: a table, columns `Line | What it states`.

The table, exactly as printed (with the file line added):

| L | Line | What it states |
|---|---|---|
| 394 | 1 · The sentence | What this view says, in the house's words and limits, to which of the named readers; the question it answers; whether it is written or generated, and if generated, the template, the check and the label |
| 395 | 2 · The pattern and the first state | Which landing pattern (for a first screen) or which default state (for any view); why; declared as the endorsement it is; what the empty state shows, if there is one |
| 396 | 3 · What sits on the face | From each record — provenance set, recipe card, claim record, comparison record, service record, measure record, safeguards record — the status that is on the face in text, the record one step away, and what is on request; the stamp and the period beside the figure |
| 397 | 4 · The nothings on this view | Which cells are not shown, under which floor or hold; how each is marked and explained; the category-level form of any held layer |
| 398 | 5 · The interactions | Each control: its purchase (from the table), its costs (from the seven), what it changes, and the static reading that works without it; what is only here (nothing crucial) |
| 399 | 6 · Hover, keyboard, pointer, size | How content on hover meets the three conditions; keyboard and single-pointer routes for every control; targets under 24 CSS pixels and their equivalent route |
| 400 | 7 · The small-screen form | What is removed, kept and re-laid for the phone; what the message is and that it survives; figures before script; the table twin |
| 401 | 8 · The state and its address | The selection parameters and their canonical order; the data version and specification version the view was built from; the degraded state and how it reads |
| 402 | 9 · The snapshot and the citation | How this state is frozen (date, what it contains, where it lives, previous/next/live); the generated citation text; what a cropped or shared copy carries |
| 403 | 10 · Words and text | Title length; annotations and where their content is also carried; the chart's reading in its title; the generated label |
| 404 | 11 · Map and colour | For any map: rates not counts; the breaks and that they are held across views; the legend; the small-area form; the stigma check (no red or dark for low; large areas not dominating; missing not zero) |
| 405 | 12 · Tests and review | The two-readers test result; the walk (Chapter 10) for this view; the glance and small-screen checks; the review date |

**Line names (first column / bold text), exactly:** `1 · The sentence` · `2 · The pattern and the first state` · `3 · What sits on the face` · `4 · The nothings on this view` · `5 · The interactions` · `6 · Hover, keyboard, pointer, size` · `7 · The small-screen form` · `8 · The state and its address` · `9 · The snapshot and the citation` · `10 · Words and text` · `11 · Map and colour` · `12 · Tests and review`

**Public, internal, or a growing log?** **Not stated as public or internal; one per view; named a "build artefact" in Looking back.** What the chapter says:

> (ch11 L390) This chapter leaves something different in kind: not an eighth record about the data but a sheet about the *surface* — one per view, which says what of the seven records sits on this face, what the view says and to whom, what it costs to touch, and how it is cited.

> (ch11 L515) - [ ] Face sheet exists for every view; line 1 written before the view was drawn

> (ch11 L606) - **Opens threads** for Chapter 12 (the sentence per place as recognition; the two columns on a first screen), Chapter 13 (the criteria in full; the equivalent route), Chapter 14 (what a creative treatment may do to the sentence, the breaks and the stamp), Chapter 16 (the face sheet, the cut list and the retirement plan as build artefacts), and the end of the book (seven records and a face sheet; the 60-second version's length).

> (rule 11.1, L463, tier `**Fixed** as a stance`) Every view carries a face sheet: the sentence, the pattern and first state, what of each record sits on the face, the nothings, the interactions and their costs, hover and pointer routes, the small-screen form, the state and its address, the snapshot and citation, words, map and colour, tests and review

> (rule 11.28, L490, tier `**Fixed** as a stance`) The records' kinds sit on the face as statuses in text that open the record; a source line is followable, not only present

**Is it one document with the others?** 

> (ch11 L390) Chapters 4 to 10 each left a record beneath a dashboard's numbers, and whether the seven are one document is for the end of the book `[Revisit at end]`. This chapter leaves something different in kind: not an eighth record about the data but a sheet about the *surface* — one per view, which says what of the seven records sits on this face, what the view says and to whom, what it costs to touch, and how it is cited. It is called the *face sheet*, it has twelve lines, and its first line is written before the view is drawn.

> (ch11 L571) - `[Revisit at end]` **Seven records and a face sheet.** Whether the records are one document and the face sheet is its front page; whether the measure record's line 12, the service record's "what this changed", the safeguards record's line 14 and the face sheet's line 12 are one field.

> (ch11 L766) | Seven records and now a face sheet | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

### 2.9 Chapter 12 — the recognition record

**Name and place, as printed.** Heading as printed: `### Beneath the page: the recognition record` (L373) — "Beneath the **page**". Note the same two words are already the name of line 8 of Chapter 5's recipe ("**The recognition record**: who was asked whether they see themselves in it…", ch05 L316).

**Lines.** 10 table rows (L379–388), numbered "1 … 10" (no "·"); a third column, "From", appears for the first time. One per place-page. Form: a table, columns `Line | What it records | From`.

The table, exactly as printed (with the file line added):

| L | Line | What it records | From |
|---|---|---|---|
| 379 | 1 Unit | The unit the page's figures are for, its vintage, and what it hides (the units above and below it) | Section 3; Decision Book geography rules |
| 380 | 2 Residents' unit | Whether a drawn or named unit exists for this place, who drew it, how many, and the consensus rule | Section 3 |
| 381 | 3 Scale | Which unit the page lands on and why; the administrative unit shown beside it | Section 3; Chapter 11 |
| 382 | 4 Identity fields | Which fields are identity (never ranked) and which are conditions; the question the profile answers; the axis order | Section 6; data contract |
| 383 | 5 Labels | Every label the page gives the place or its type, the rule it was written by, the hedge, and who reviewed it | Sections 6, 9 |
| 384 | 6 Gates | For each condition compared: the gate's status, which criteria were harmonised, the wording rule | Section 6; Style Guide §12 |
| 385 | 7 Peers | The peer method, the peers, and who chose them | Chapter 7 |
| 386 | 8 Sentence | The bridging sentence and the advocacy sentence, each within the poster rule | Sections 5, 6 |
| 387 | 9 Review | Who from the scene saw the page before publication, in what form, what they said about unit, labels and what is missing, and what changed | Section 9; Chapter 9 |
| 388 | 10 Errors | The standing channel for correction, and the corrections made, dated | Section 3 (MSOA names); Chapter 11 |

**Line names (first column / bold text), exactly:** `1 Unit` · `2 Residents' unit` · `3 Scale` · `4 Identity fields` · `5 Labels` · `6 Gates` · `7 Peers` · `8 Sentence` · `9 Review` · `10 Errors`

**Public, internal, or a growing log?** **Not stated as public or internal;** "one per place-page", written before publication, updated at every review; the *page* says it was reviewed. What the chapter says:

> (ch12 L375) This chapter leaves a ninth, one per place-page, called the *recognition record*.

> (ch12 L375) Ten lines, written before the page is published and updated at every review.

> (rule 12.39, L484, tier `**Fixed** as a procedure`) The recognition record, ten lines, sits beneath every place-page

> (rule 12.36, L481, tier `**Fixed** as a procedure`) Every place-page is shown to people from the scene before publication, in a form chosen with them; what was said and what changed is recorded by role, never by name; the page says it was reviewed

**Is it one document with the others?** 

> (ch12 L375) Chapters 4 to 11 each left a record; whether they are one document is for the end of the book `[Revisit at end]`. This chapter leaves a ninth, one per place-page, called the *recognition record*. Ten lines, written before the page is published and updated at every review.

> (ch12 L545) - `[Revisit at end]` Nine records; whether one document. The 60-second version's length (raised an eighth time).

### 2.10 Chapter 13 — the accessibility statement

**Name and place, as printed.** Heading as printed: `### Beneath the dashboard: the accessibility statement` (L344).

**Lines.** 12 table rows (L350–361), numbered "1 … 12"; "a line per view for each route". Form: a table, columns `Line | What it records | From`.

The table, exactly as printed (with the file line added):

| L | Line | What it records | From |
|---|---|---|---|
| 350 | 1 Status | Fully, partially or not compliant with WCAG 2.2 AA, in the model's words, for each layout | Reg 8; model statement |
| 351 | 2 Per view: description | The short description's place and the long description's (body text); that it carries type, figures and trend and not interpretation; how it is generated and who read it against the data | Section 5; Analysis Function |
| 352 | 3 Per view: table | The table twin's location, its headers, pagination, and what it cannot carry (shape; geography) | Sections 5, 8 |
| 353 | 4 Per view: structure | Whether a navigable structure exists, on what roles, tested with which screen readers | Section 3; APG |
| 354 | 5 Per view: audio | Whether an audio graph or sonification exists, and that it is an extra | Section 5 |
| 355 | 6 Motion and updates | The reduced-motion behaviour; the pause control for auto-updating views | Section 3; 2.2.2, 2.3.3 |
| 356 | 7 Keyboard and focus | The walk's result per view: reached, operated, left; focus visible and unobscured | 2.1.1, 2.1.2, 2.4.7, 2.4.11 |
| 357 | 8 Zoom and reflow | 400 per cent result per layout; what is excepted (map, table) and what is not (their furniture) | 1.4.10, 1.4.4, 1.4.12 |
| 358 | 9 Non-compliances | Each failure by criterion, in the public sector's form, with the route around it | Reg 8(4)(a), (b); PHS as model |
| 359 | 10 Burden | Any claim and its assessment; the house's default is none | Reg 7 |
| 360 | 11 Tested | Date, technologies (named screen readers, browsers, platforms), and who tested, including disabled readers of the audience | Design System; Chartability |
| 361 | 12 Contact | The errors channel (Chapter 12) and the request route for information in another format | Reg 8(4)(c); reg 13 |

**Line names (first column / bold text), exactly:** `1 Status` · `2 Per view: description` · `3 Per view: table` · `4 Per view: structure` · `5 Per view: audio` · `6 Motion and updates` · `7 Keyboard and focus` · `8 Zoom and reflow` · `9 Non-compliances` · `10 Burden` · `11 Tested` · `12 Contact`

**Public, internal, or a growing log?** **Public — the only record the book calls "a public document".** What the chapter says:

> (ch13 L42) Beneath the dashboard the chapter leaves a tenth record, which is also a public document: the *accessibility statement*, in the model's form, with a line per view for each route — description, structure, table and what it cannot carry, audio, motion and update controls — and the declared non-compliances, the test date, the technology tested with, and the contact.

> (ch13 L346) This chapter's tenth is different in kind from the others and the same in kind as the public sector's: it is published, in the model statement's form, and it is the record.

> (ch13 L399) **The statement.** Linked from the footer; twelve lines per the record; the non-compliances in the public sector's form; the test date and the screen readers named; the errors channel.

> (rule 13.23, L431, tier `**Fixed** as a procedure`) The house publishes an accessibility statement in the public sector's model form with the twelve lines, per view, dated within twelve months

**Is it one document with the others?** 

> (ch13 L346) Chapters 4 to 12 each left a record; whether they are one document is for the end of the book `[Revisit at end]`. This chapter's tenth is different in kind from the others and the same in kind as the public sector's: it is published, in the model statement's form, and it is the record. Its lines — the model's own (status; non-accessible content and why; alternatives; contact; preparation and testing) with the house's per-view lines between them:

> (ch13 L496) - `[Revisit at end]` Ten records; the statement as the public one. The 60-second version's length (raised a ninth time).

### 2.11 Chapter 14 — the boundary log

**Name and place, as printed.** Heading as printed: `### Beneath the dashboard: the boundary log` (L430). The chapter also calls it "the register" (L446 "what a line in the register looks like"; break test L516 "write the register entry"; conflict log L728 "a ten-line register"; gap row L714 "Used in the register").

**Lines.** 11 table rows (L436–446), unnumbered; "eleven lines per element". (The chapter's own conflict log, L728, says "a ten-line register".) Form: a table, columns `Line | What it holds | Why`.

The table, exactly as printed (with the file line added):

| L | Line | What it holds | Why |
|---|---|---|---|
| 436 | Element | What the expressive element is, where it appears, and the version of the display it was added to | A register entry outlives the person who made the choice |
| 437 | Tier claimed | Decorative; specific sensory experience; or a named Adaptable choice at the encoding level | The tier is the argument's first move (Decision Book Ch 18) |
| 438 | Purchase | What it buys, in the affective-intent template — "The viewer will [observe / position / strengthen / connect / behave] [noun]" — limited to what expression is measured to buy | An unnamed break is a mistake made confidently; an over-claimed one is a false one |
| 439 | Touches | Which view, encoding or claim it sits on or near | Blair: palette moves feeling more than data; the register must say what it is next to |
| 440 | Mono | What the greyscale render lost or changed | Hue is the commonest leak |
| 441 | Silent | What muting lost; for sound-as-content, where the text document is | WCAG 1.2.1; 1.4.2 |
| 442 | Still | What disabling motion lost; where the pause control is | ONS; WCAG 2.2.2 (Chapter 13) |
| 443 | Undressed | What stripping the register lost or changed | Mackinlay's second clause |
| 444 | Stripped beside dressed | Whether the two versions say the same thing — no added size, order, brightness or cause — and, for a form, its estimated glance cost against a bar | The fifth check; the two-houses infographic; Blascheck |
| 445 | Twin and identification | Where the precise twin is, how many steps away, and the words that identify the element to a reader who cannot see or hear it | Ottley; WCAG's "descriptive identification" for a sensory experience |
| 446 | Tested, and status | Whether readers saw the stripped and dressed versions and what each took from the data — figures and trend agreeing is the pass; the sample is the three user groups' readers, as Chapter 13's test; two readers is the shape of the test, not its size — with date, who ran it, and the entry's status (open, closed, re-tiered, removed) and owner | The evaluated exception's standard, with the comparison it lacked |

**Line names (first column / bold text), exactly:** `Element` · `Tier claimed` · `Purchase` · `Touches` · `Mono` · `Silent` · `Still` · `Undressed` · `Stripped beside dressed` · `Twin and identification` · `Tested, and status`

**Public, internal, or a growing log?** **A growing log; public or internal left open.** What the chapter says:

> (ch14 L432) Each earlier chapter left a record beneath the display; this one leaves the eleventh, and it is a log rather than a sheet, because it grows by one line each time an expressive element is added.

> (ch14 L450) `[Revisit at end]` Whether the eleven records beneath the dashboard are one document is the standing question; this one is the first that is a log, and a log may want to live in the design repository rather than on the public page, with its existence declared on the page.

> (ch14 L464) **Open, and the house's to decide with a reason recorded.** Whether the boundary log is public or internal.

> (rule 14.2, L493, tier `**Fixed** (procedure)`) Record each element in the boundary log, eleven lines, before it ships

**Is it one document with the others?** 

> (ch14 L450) `[Revisit at end]` Whether the eleven records beneath the dashboard are one document is the standing question; this one is the first that is a log, and a log may want to live in the design repository rather than on the public page, with its existence declared on the page.

> (ch14 L562) `[Revisit at end]` Whether the eleven records are one document, and whether a log belongs on the page or in the repository with a declaration on the page.

### 2.12 Chapter 15 — the precedent record

**Name and place, as printed.** Heading as printed: `### Beneath the dashboard: the precedent record` (L434).

**Lines.** 9 table rows (L440–448), unnumbered; "Nine lines per entry." Form: a table, columns `Line | What it holds | Why`.

The table, exactly as printed (with the file line added):

| L | Line | What it holds | Why |
|---|---|---|---|
| 440 | Mechanism | What is borrowed, in one sentence, and the record it feeds (recipe card, service record, comparison record, face sheet, boundary log, …) | A borrowed rule lives in the record it serves, not in this one |
| 441 | Source | The project or body, the document, its version and date, and the date it was read | Rules change under the same name (the fan chart's bands; the Toolkit's status) |
| 442 | Rule as printed | The threshold, interval, colour, cadence or wording, quoted, from one named document | A paraphrased rule drifts (the "twice as deprived" this chapter expected and did not find) |
| 443 | Reason given | The source's own stated reason | The reason decides whether the rule transfers |
| 444 | Evidence | What was measured about it, by whom, on whom, with n; or "none found" | With a reason but no evidence or named cost, the entry is a bet, and says so |
| 445 | Condition or cost | What the mechanism needs (intervals; five annual points; a stable indicator set; storage), and what the display does while the need is unmet | A rule adopted without its condition fails silently |
| 446 | What the house changes | Any departure from the printed rule, and why | The departure is the house's, and is owned |
| 447 | Status | Adopted; adapted; declined, with the reason; or awaiting a condition | The record is a decision list |
| 448 | Review | When the source document is to be re-read for change, and who owns the entry | Sources retire (Scotland's pages; Fingertips itself) |

**Line names (first column / bold text), exactly:** `Mechanism` · `Source` · `Rule as printed` · `Reason given` · `Evidence` · `Condition or cost` · `What the house changes` · `Status` · `Review`

**Public, internal, or a growing log?** **A growing list; "a working file".** What the chapter says:

> (ch15 L436) Each earlier chapter left a record beneath the display; this one leaves the twelfth, and like the boundary log it grows by one entry each time something is adopted.

> (ch15 L558) `[Prototype flag]` The lag distribution of any late-returns series the house will publish, from which the window is set; the vintage naming rule, which must exist before the first release; the retirement plan; the precedent record as a working file.

> (ch15 L458) Everything else — which metadata fields beyond the minimum; whether to publish a compliance-style statement; whether to run a trust question at all, and in whose waves; which evidence scale to label contribution claims with — is the studio's, with the precedent record as the place the choice is written.

> (rule 15.21, L514, tier `**Fixed** (procedure)`) Record every borrowed mechanism in the precedent record, nine lines, with its status, before it ships

**Is it one document with the others?** 

> (ch15 L452) `[Revisit at end]` Whether the twelve records beneath the dashboard are one document; this one, like the boundary log, is a list that grows.

> (ch15 L562) `[Revisit → Ch 16]` The precedent record beside the boundary log and the override log; the status marks [p] [r] [f] against this book's own dagger; the twelve records as one document; the regulator's minimum list as a checklist the house can voluntarily meet; the retirement plan as a Fixed rule.

> (ch15 L564) `[Revisit at end]` The fold question (section 11); whether the twelve records are one document.

> (ch15 L682) | The precedent record's place among twelve records | §12 | A growing list, like the boundary log | Chapter 16; `[Revisit at end]` |

### 2.13 All line names across the twelve records

129 lines in all (10 + 9 + 10 + 10 + 10 + 12 + 14 + 12 + 10 + 12 + 11 + 9). Line names exactly as printed (for the four lists, the bold text). "Recurs" marks a concept word in the **name** that also appears in the name of a line in another record; the concept words are listed in 2.14.

| Ch | Record | Line | Line name, as printed | Recurs (concept words in the name shared with another record) |
|---|---|---|---|---|
| 4 | provenance set | 1 | who is responsible | owner / responsible / who governs; who (who was asked / consulted / answered / is in the record) |
| 4 | provenance set | 2 | what source | source |
| 4 | provenance set | 3 | what method | method |
| 4 | provenance set | 4 | what period | period / date / when |
| 4 | provenance set | 5 | when it was issued and when it last changed | period / date / when |
| 4 | provenance set | 6 | what status | status |
| 4 | provenance set | 7 | what quality |  |
| 4 | provenance set | 8 | what was withheld or altered | withheld / held / nothings |
| 4 | provenance set | 9 | what it may be compared with | gate / comparators / peers / compared |
| 4 | provenance set | 10 | outlive the number |  |
| 5 | recipe (card) | 1 | The construct, in a sentence | sentence / words |
| 5 | recipe (card) | 2 | The parts |  |
| 5 | recipe (card) | 3 | The normalisation |  |
| 5 | recipe (card) | 4 | The nominal weights and who set them … and the effective importances beside them | who chose / who set; who (who was asked / consulted / answered / is in the record) |
| 5 | recipe (card) | 5 | The aggregation rule and the price list it implies | rule |
| 5 | recipe (card) | 6 | The rank with its interval | interval |
| 5 | recipe (card) | 7 | The validity evidence | evidence |
| 5 | recipe (card) | 8 | The recognition record | recognition; record |
| 5 | recipe (card) | 9 | The audit design | the walk / audit |
| 6 | claim record | 1 | What was observed |  |
| 6 | claim record | 2 | Who is in the record | record; who (who was asked / consulted / answered / is in the record) |
| 6 | claim record | 3 | Gross or net |  |
| 6 | claim record | 4 | Created or captured |  |
| 6 | claim record | 5 | For whom |  |
| 6 | claim record | 6 | The rung |  |
| 6 | claim record | 7 | The alternatives considered |  |
| 6 | claim record | 8 | Noticed on |  |
| 6 | claim record | 9 | The model's known wrongness |  |
| 6 | claim record | 10 | The small-number treatment | small-number / spread |
| 7 | comparison record | 1 | What is held equal | withheld / held / nothings |
| 7 | comparison record | 2 | The comparators, who chose them, and why this place | who chose / who set; gate / comparators / peers / compared; who (who was asked / consulted / answered / is in the record) |
| 7 | comparison record | 3 | The standardisation |  |
| 7 | comparison record | 4 | The order on the display |  |
| 7 | comparison record | 5 | The interval | interval |
| 7 | comparison record | 6 | The season and the smoothing |  |
| 7 | comparison record | 7 | The base month, and the record | record |
| 7 | comparison record | 8 | The design, and its assumption |  |
| 7 | comparison record | 9 | The ripple |  |
| 7 | comparison record | 10 | The future's terms |  |
| 8 | service record | 1 | 1 · Freshness promise |  |
| 8 | service record | 2 | 2 · Dependencies |  |
| 8 | service record | 3 | 3 · Refresh mechanism |  |
| 8 | service record | 4 | 4 · Watch and alarm |  |
| 8 | service record | 5 | 5 · Availability target and degraded mode |  |
| 8 | service record | 6 | 6 · Budget and baseline device |  |
| 8 | service record | 7 | 7 · Map supply, licence and vintage | map |
| 8 | service record | 8 | 8 · Retirement plan and archive |  |
| 8 | service record | 9 | 9 · Owner and successor | owner / responsible / who governs |
| 8 | service record | 10 | 10 · Not done | not done / what it cannot / non-compliances |
| 9 | measure record | 1 | 1 · Construct and register |  |
| 9 | measure record | 2 | 2 · Items and format |  |
| 9 | measure record | 3 | 3 · Who chose what counts | who chose / who set; who (who was asked / consulted / answered / is in the record) |
| 9 | measure record | 4 | 4 · Who was asked, how, when, where | period / date / when; who (who was asked / consulted / answered / is in the record) |
| 9 | measure record | 5 | 5 · Who answered and who did not | who (who was asked / consulted / answered / is in the record) |
| 9 | measure record | 6 | 6 · The spread | small-number / spread |
| 9 | measure record | 7 | 7 · Response-process evidence | evidence |
| 9 | measure record | 8 | 8 · Internal structure and reliability |  |
| 9 | measure record | 9 | 9 · Relations to other variables |  |
| 9 | measure record | 10 | 10 · Recognition | recognition |
| 9 | measure record | 11 | 11 · Discordance |  |
| 9 | measure record | 12 | 12 · What this changed | what this changed |
| 10 | safeguards record | 1 | 1 · What is processed, about whom |  |
| 10 | safeguards record | 2 | 2 · Lawful basis and its test | test / tested |
| 10 | safeguards record | 3 | 3 · Release model and environment |  |
| 10 | safeguards record | 4 | 4 · Disclosure method per view | method |
| 10 | safeguards record | 5 | 5 · Query-time controls |  |
| 10 | safeguards record | 6 | 6 · The intruder's walk | the walk / audit |
| 10 | safeguards record | 7 | 7 · Who was consulted | who (who was asked / consulted / answered / is in the record) |
| 10 | safeguards record | 8 | 8 · Who governs, and who stood at the door | owner / responsible / who governs; who (who was asked / consulted / answered / is in the record) |
| 10 | safeguards record | 9 | 9 · The held layer | withheld / held / nothings |
| 10 | safeguards record | 10 | 10 · Withdrawal |  |
| 10 | safeguards record | 11 | 11 · Harm assessment |  |
| 10 | safeguards record | 12 | 12 · Regimes in scope |  |
| 10 | safeguards record | 13 | 13 · Moderation and audit | the walk / audit |
| 10 | safeguards record | 14 | 14 · Review, incident, and what this changed | review; what this changed |
| 11 | face sheet | 1 | 1 · The sentence | sentence / words |
| 11 | face sheet | 2 | 2 · The pattern and the first state |  |
| 11 | face sheet | 3 | 3 · What sits on the face |  |
| 11 | face sheet | 4 | 4 · The nothings on this view | withheld / held / nothings |
| 11 | face sheet | 5 | 5 · The interactions | purchase / interactions |
| 11 | face sheet | 6 | 6 · Hover, keyboard, pointer, size |  |
| 11 | face sheet | 7 | 7 · The small-screen form |  |
| 11 | face sheet | 8 | 8 · The state and its address |  |
| 11 | face sheet | 9 | 9 · The snapshot and the citation |  |
| 11 | face sheet | 10 | 10 · Words and text | sentence / words |
| 11 | face sheet | 11 | 11 · Map and colour | map |
| 11 | face sheet | 12 | 12 · Tests and review | review; test / tested |
| 12 | recognition record | 1 | 1 Unit |  |
| 12 | recognition record | 2 | 2 Residents' unit |  |
| 12 | recognition record | 3 | 3 Scale |  |
| 12 | recognition record | 4 | 4 Identity fields |  |
| 12 | recognition record | 5 | 5 Labels |  |
| 12 | recognition record | 6 | 6 Gates | gate / comparators / peers / compared |
| 12 | recognition record | 7 | 7 Peers | gate / comparators / peers / compared |
| 12 | recognition record | 8 | 8 Sentence | sentence / words |
| 12 | recognition record | 9 | 9 Review | review |
| 12 | recognition record | 10 | 10 Errors | errors / contact |
| 13 | accessibility statement | 1 | 1 Status | status |
| 13 | accessibility statement | 2 | 2 Per view: description |  |
| 13 | accessibility statement | 3 | 3 Per view: table | twin / table |
| 13 | accessibility statement | 4 | 4 Per view: structure |  |
| 13 | accessibility statement | 5 | 5 Per view: audio |  |
| 13 | accessibility statement | 6 | 6 Motion and updates |  |
| 13 | accessibility statement | 7 | 7 Keyboard and focus |  |
| 13 | accessibility statement | 8 | 8 Zoom and reflow |  |
| 13 | accessibility statement | 9 | 9 Non-compliances | not done / what it cannot / non-compliances |
| 13 | accessibility statement | 10 | 10 Burden |  |
| 13 | accessibility statement | 11 | 11 Tested | test / tested |
| 13 | accessibility statement | 12 | 12 Contact | errors / contact |
| 14 | boundary log | 1 | Element |  |
| 14 | boundary log | 2 | Tier claimed |  |
| 14 | boundary log | 3 | Purchase | purchase / interactions |
| 14 | boundary log | 4 | Touches |  |
| 14 | boundary log | 5 | Mono |  |
| 14 | boundary log | 6 | Silent |  |
| 14 | boundary log | 7 | Still |  |
| 14 | boundary log | 8 | Undressed |  |
| 14 | boundary log | 9 | Stripped beside dressed |  |
| 14 | boundary log | 10 | Twin and identification | twin / table |
| 14 | boundary log | 11 | Tested, and status | status; test / tested |
| 15 | precedent record | 1 | Mechanism |  |
| 15 | precedent record | 2 | Source | source |
| 15 | precedent record | 3 | Rule as printed | rule |
| 15 | precedent record | 4 | Reason given |  |
| 15 | precedent record | 5 | Evidence | evidence |
| 15 | precedent record | 6 | Condition or cost |  |
| 15 | precedent record | 7 | What the house changes |  |
| 15 | precedent record | 8 | Status | status |
| 15 | precedent record | 9 | Review | review |

### 2.14 Which line names recur

**Exact repeats of a whole line name** (ignoring the leading number and case):

- `Review` — Ch 12 recognition record, line 9; Ch 15 precedent record, line 9
- `Status` — Ch 13 accessibility statement, line 1; Ch 15 precedent record, line 8

**Concept words by record.** "N" = the word is in a line **name** in that record (line number in brackets); "t" = it is only in a line's descriptive text (for the four lists, the text of the item after the bold name); blank = absent. The word patterns are literal (e.g. "unit" matches unit/units only), so this is a count of the records' own vocabulary, not of the idea.

| Concept word(s) | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | Records with it in a line name | Records with it anywhere |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| unit |  | t(2,5) | t(1) | t(1) |  |  | t(1,9) |  | N(1,2) t(3,9) |  |  |  | 1 | 5 |
| base |  | t(2) | t(1) | N(7) t(1) |  |  |  |  |  |  |  |  | 1 | 3 |
| period / date / when | N(4,5) | t(2,9) | t(1,8,9) | t(1,6,8) | t(1,2,4,5,7,8,9) | N(4) t(5,10) | t(2,6,7,9,10,13,14) | t(3,9,12) | t(10) | t(11) | t(11) | t(2,9) | 2 | 12 |
| source | N(2) | t(2) | t(2,3,5) | t(1,10) | t(8) |  |  |  |  |  |  | N(2) t(4,9) | 2 | 6 |
| owner / responsible / who governs | N(1) |  |  |  | N(9) |  | N(8) |  |  |  | t(11) |  | 3 | 4 |
| review | t(1) |  |  |  |  |  | N(14) t(9) | N(12) | N(9) t(5) |  |  | N(9) | 4 | 5 |
| status | N(6) | t(2) |  | t(1) |  |  | t(12) | t(3) | t(6) | N(1) | N(11) | N(8) t(2) | 4 | 9 |
| not done / what it cannot / non-compliances |  |  |  |  | N(10) |  |  |  |  | N(9) |  |  | 2 | 2 |
| interval | t(4) | N(6) | t(10) | N(5) |  |  |  |  |  |  |  | t(3,6) | 2 | 5 |
| recognition |  | N(8) |  |  |  | N(10) |  |  |  |  |  |  | 2 | 2 |
| who chose / who set | t(2) | N(4) t(8) |  | N(2) t(8) |  | N(3) t(6) | t(13) |  | t(7) |  |  |  | 3 | 6 |
| method | N(3) | t(5) |  | t(2,6) |  |  | N(4) |  | t(7) |  |  |  | 2 | 5 |
| vintage / version | t(5) | t(5) |  | t(1) | N(7) |  |  | t(8) | t(1) |  | t(1,9,11) | t(2) | 1 | 8 |
| test / tested |  | t(5) | t(8) |  | t(6) | t(8,9) | N(2) t(1,9,12) | N(12) |  | N(11) t(4) | N(11) |  | 4 | 8 |
| what this changed |  |  |  |  |  | N(12) | N(14) |  |  |  |  |  | 2 | 2 |
| withheld / held / nothings | N(8) |  | t(10) | N(1) |  |  | N(9) t(8) | N(4) t(11) |  |  |  |  | 4 | 5 |
| twin / table | t(6) |  |  |  | t(7) |  |  | t(5,7) |  | N(3) t(8) | N(10) |  | 2 | 5 |
| map |  |  |  |  | N(7) |  |  | N(11) |  | t(8) |  |  | 2 | 3 |
| gate / comparators / peers / compared | N(9) |  |  | N(2) |  |  |  |  | N(6,7) |  |  |  | 3 | 3 |
| errors / contact | t(7) |  |  |  |  |  |  |  | N(10) | N(12) |  |  | 2 | 3 |
| retirement / archive |  |  |  |  | N(8) |  |  |  |  |  |  | t(9) | 1 | 2 |
| sentence / words | t(7) | N(1) |  |  |  | t(1,2) |  | N(1,10) | N(8) | t(1) | t(10) | t(1) | 3 | 8 |
| record | t(10) | N(8) | N(2) | N(7) t(10) | t(9,10) |  | t(2,14) | t(3) |  |  |  | t(1,8) | 3 | 8 |
| rule |  | N(5) |  |  |  |  | t(5) |  | t(2,5,6,8) |  |  | N(3) t(1,4,6,7) | 2 | 4 |
| evidence |  | N(7) |  |  |  | N(7) t(12) | t(12,14) |  |  |  |  | N(5) | 3 | 4 |
| register |  |  |  |  |  | N(1) |  |  |  |  | t(1,4,8) |  | 1 | 2 |
| who (who was asked / consulted / answered / is in the record) | N(1) | N(4) t(8) | N(2) | N(2) t(1) | t(4,9) | N(3,4,5) t(10) | N(7,8) t(3,5,6,9,14) |  | t(2,5,7,9) | t(2,11) | t(1,10,11) | t(9) | 6 | 11 |
| the walk / audit |  | N(9) |  |  |  |  | N(6,13) t(9) | t(12) |  | t(7) |  |  | 2 | 4 |
| harm |  |  |  |  |  |  | N(11) |  |  |  |  |  | 1 | 1 |
| purchase / interactions |  |  |  |  |  |  |  | N(5) |  |  | N(3) |  | 2 | 2 |
| the state / snapshot / citation |  | t(5) |  |  | t(8) |  |  | N(2,8,9) |  |  |  |  | 1 | 3 |
| rung |  |  | N(6) | t(8) |  |  |  |  |  |  |  |  | 1 | 2 |
| gross / net / created |  | t(1) | N(3,4) |  |  |  |  |  |  |  |  |  | 1 | 2 |
| small-number / spread |  |  | N(10) |  |  | N(6) |  |  |  |  |  |  | 2 | 2 |

Column heads 4–15 are the chapters: 4 provenance set · 5 recipe · 6 claim record · 7 comparison record · 8 service record · 9 measure record · 10 safeguards record · 11 face sheet · 12 recognition record · 13 accessibility statement · 14 boundary log · 15 precedent record.

**Reading the matrix — the seven words asked about.**

- **unit** — a line name only in the recognition record ("Unit", "Residents' unit"); in the text of the recipe (lines 2 and 5), the claim record (line 1), the comparison record (line 1) and the safeguards record (lines 1 and 9). The provenance set has no line for the unit: Chapter 4 makes the unit a rule (4.1) and not a line of the set.
- **base** — a line name only in the comparison record, and there it means the *base month* (line 7); as "the thing counted against" it is in the text of the recipe (line 2), the claim record (line 1) and the comparison record (line 1). No record has a line named for the base.
- **date / period / when** — the only concept present in the text of all twelve records, and a line name in two (provenance set: "what period", "when it was issued and when it last changed"; measure record: "Who was asked, how, when, where"). Each record dates something different: the figure (4), the validation (6), the read of a dependency's terms (8), the statute (10), the snapshot (11), the test (13), the source document (15).
- **source** — a line name in the provenance set ("what source") and the precedent record ("Source"); in the text of the recipe, the claim record, the comparison record and the service record. Chapter 8's flag (L695) says "the service record's line 2 overlaps the provenance set's source lines".
- **owner** — a line name in the provenance set ("who is responsible"), the service record ("Owner and successor") and the safeguards record ("Who governs, and who stood at the door" — a different owner: the scene's body); in the text of the boundary log (line 11, "and owner") and, as "who owns the entry", the precedent record (line 9).
- **review** — a line name in four: safeguards record ("Review, incident, and what this changed"), face sheet ("Tests and review"), recognition record ("Review" — here a review *by the scene*, not a re-reading date) and precedent record ("Review").
- **status** — a line name in four: provenance set ("what status" — of the figure), accessibility statement ("Status" — of compliance), boundary log ("Tested, and status" — of the entry), precedent record ("Status" — of the adoption). Four different things have a status.

**Three lines the chapters themselves say may be one field.** Chapter 9 L649: "whether the measure record's line 12 and the service record's "what this changed" are the same field" (the service record as printed has no line of that name; its ten lines are in 2.5). Chapter 10 L812 adds "this record's line 14"; Chapter 11 L571 adds "the face sheet's line 12". As printed: measure record line 12 "What this changed"; safeguards record line 14 "Review, incident, and what this changed"; face sheet line 12 "Tests and review".

**False friends in the matrix** (same word, different thing): "held" is *held equal* in the comparison record (line 1) and the *held layer* in the safeguards record (line 9) and face sheet (line 4); "record" in line names means three things (the recipe's "recognition record"; the claim record's "Who is in the record" — the data; the comparison record's "The base month, and the record" — a track record); "register" in the measure record (line 1) is the made/perceived/excess register, not a log; "review" in the provenance set (line 1) is "the Macpherson review", and "error" there (line 7) is statistical error, not the errors channel of the recognition record and the accessibility statement.

**"Not done".** Only the service record has a line for it (line 10, "Not done"). The claim record and the comparison record make it a rule about every line instead (6.43 ""not done" is written, not hidden"; 7.1 "a line that cannot be filled says "not done""); the measure and safeguards records' filled examples use "not yet" and "open"; the accessibility statement has "Non-compliances" (line 9).

---

## PART 3 — THE ASSEMBLED TESTS

Every `## What proves a break works` section, Chapters 1–15, in full and verbatim (Chapter 0 has none; it describes the section in its template table, L59: "**What proves a break works** | The test to run before deviating from a Fixed rule"). Eleven sections are one paragraph; those of Chapters 8, 9, 10 and 11 are two.

### 3.1 Chapter 1 (heading L326; 1 paragraph; 125 words)

> [L328] If you must build a dashboard that breaks one of the Fixed rules above — a ranking without intervals, a display without a data release, a measure that is not scaled — the test is the same in every case: **find the person the rule protects and show them.** Give the ranking to someone at the bottom of it and ask if it is fair. Give the display to someone who needs the data underneath and ask them to get it. Give the unscaled measure to the smallest unit in it and ask whether they can see themselves. If the break survives that, log it in the four-line record Chapter 16 describes. If it does not, it was not a break; it was a mistake.

### 3.2 Chapter 2 (heading L474; 1 paragraph; 155 words)

> [L476] If you must break a Fixed rule above — imply an effect without a comparison, show a monetised headline without its caveats, present a ranking as advice, show property value without saying whose reading it serves — the test is the same: **find the reader who grades by the opposite rule and show them.** Give the impact claim to a What Works analyst and ask what level it is. Give the £-headline to the person who wrote the report it came from and ask if they recognise their caveats. Give the property-value panel to a resident of the street and ask what it means to them. Give the "voices" panel to the people quoted in it and ask whether they could change it. If the break survives that, log it in the four-line record Chapter 16 describes (what rule, why, for whom, what proved it). If it does not, it was a reader you forgot.

### 3.3 Chapter 3 (heading L465; 1 paragraph; 155 words)

> [L467] If you must break a Fixed rule above — a legend instead of labels, a truncated bar, a rainbow, an error bar, a finding behind a hover — the test is the same: **give the display to the reader the rule protects, for the time the rule assumes, and ask them what it says.** Print the legend chart in greyscale and give it to someone with protanopia — the commonest red–green deficiency. Give the truncated bar to someone for five seconds and ask how big the difference is, then ask them to read the numbers, and notice that the two answers disagree. Give the error bar to a statistician and ask what it means for one person. Give the hover to someone on a phone. If the reading survives, log the break in the four-line record Chapter 16 describes (what rule, why, for whom, what proved it). If it does not, the rule was right.

### 3.4 Chapter 4 (heading L578; 1 paragraph; 169 words)

> [L580] The Fixed rules above are mostly standards, and breaking a standard is different from breaking an experimental finding: the test is not whether a reader misreads but whether the figure can be *checked*. If you must show a number without its unit, period or base; a blank without its kind; a line joined across a gap; a comparison without its declaration; a total without its shape; a platform figure as the city; or a trimmed series without the untrimmed one — the test is: **hand the display to someone who was not in the room, with the decision it is meant to bear, and ask them to reconstruct how the number was made and what would change it.** If they can, from what is on the face and one tap away, the break has cost nothing. If they cannot, the number cannot bear the weight, and the standard was right. Log the break in the four-line record Chapter 16 will describe (what rule, why, for whom, what proved it).

### 3.5 Chapter 5 (heading L439; 1 paragraph; 156 words)

> [L441] The Fixed rules above are mostly about what is declared, and the test for breaking one is the same as Chapter 4's: **hand the composed number and whatever accompanies it to someone who was not in the room, and ask them to reconstruct how it was made, what would change it, and what one part is worth in terms of another.** If they can — from the face and one tap — the break has cost nothing. If they cannot say what the weights did, what a strength paid for, or how far the rank could move, the number cannot bear the weight, and the rule was right. For the audit rule the test is harder and later: a year on, can anyone say whether the measured thing moved, from a source that is not the measure? Log the break in the four-line record Chapter 16 will describe (what rule, why, for whom, what proved it).

### 3.6 Chapter 6 (heading L537; 1 paragraph; 180 words)

> [L539] Most of the Fixed rules here are about what is declared beside a figure, and the test for breaking one is Chapter 4's and Chapter 5's: **give the figure and what accompanies it to someone who was not in the room, and ask them four questions — who is in this record, is this gross or net, what rung does the "because" reach, and could this number be noise?** If they can answer all four from the face and one tap, the break has cost nothing. If any answer is "I can't tell", the rule was carrying weight. For the alert rules the test is later and arithmetical: after a year, count the alarms that were answered and found to be nothing, and compare the count with the false-alarm rate the feature declared. For the small-number rules the test is adversarial: try, as someone who knows the scene, to name the venues behind a withheld count; if you can, the threshold was the national rule's and not the scene's. Log the break in the four-line record Chapter 16 will describe.

### 3.7 Chapter 7 (heading L478; 1 paragraph; 148 words)

> [L480] The test for breaking a comparison rule is the same as the earlier chapters': **give the comparison and what accompanies it to someone who was not in the room and ask four questions — what is being held equal, who chose the comparators, could these two be told apart, and what else could have moved the line?** If the answers come from the face and one tap, the break has cost nothing. For the ranking rule the test is adversarial: crop the display as a hostile reader would, and see whether what survives is a league table; if it is, the rule was carrying weight. For the projection rules the test is later and arithmetical: a year on, compare the projection with the outturn and see whether the range held and whether the switching value was crossed. Log the break in the four-line record Chapter 16 will describe.

### 3.8 Chapter 8 (heading L640; 2 paragraphs; 200 words)

> [L642] The test for whether a departure from one of this chapter's rules has cost anything is the same shape as the earlier chapters', with a different clock: **take one of the page's sources away, or stop its refresh, and open it on the baseline phone a week later.** If a reader who was not in the room can tell, from the face alone, how old each figure is, which series is missing and why, and that someone knows — the break has cost nothing. If the page is blank, or shows a date that is the page's rather than the data's, or shows last month's figures as this month's with no sign, the break has failed, however well the page loaded.

> [L644] For a departure that adds a live element, the test is the chain arithmetic done with real numbers and written in the record. For a vector map, it is the renderer's weight counted against the script budget on the baseline device, with the twin table present. For a platform dependency, it is the clause that permits what the dashboard does, quoted in the record beside the series. For a studio of one, it is the name of the second.

### 3.9 Chapter 9 (heading L585; 2 paragraphs; 244 words)

> [L587] The test for a departure from one of this chapter's rules is a conversation: **show the felt result, with its record, to someone who gave an answer and to someone who was not asked, and listen for three things.** Does the person who answered recognise the question they were asked and see what their answer changed? Does the person who was not asked see, from the face, that they were not — who was, how many, and what that means for the number? And can either of them tell, from the face alone, that the number is a spread and not a verdict? If all three, the break has cost nothing — this is a test of whether the face is legible, not a test of the measure's validity, which the record carries. If the person who answered does not recognise the question, the content and response-process evidence has failed; if the person not asked cannot see the gap, the selection has been hidden; if either reads the number as a verdict on the place, the register or the spread has been collapsed.

> [L589] For a trace or signal shown as an indicator, the test is the convergent one: the number beside the descriptor it is supposed to predict, in the same place, with the correlation stated. For a public self-placement, it is the private version run first and compared. For a departure from the floor, it is the interval shown and the reason given.

### 3.10 Chapter 10 (heading L739; 2 paragraphs; 320 words)

> [L741] The test for a departure from one of this chapter's rules has two halves, and both are conversations. **First, give the view and its record to someone who knows the scene and was not consulted, and ask them to find a person or a room in it in an hour.** If they cannot, or can only with low confidence about a unit the record already names as a residual risk, the disclosure half of the break has cost nothing. If they can, the floor, the classifications or the walk has failed, whatever the rule said. **Second, give the same view and the record to someone in the scene who was described by it and was not asked, and listen for three things.** Do they see, from the face, that the small rooms are present and not erased — and that the held ones were held at someone's request and not hidden by the studio? Do they see who was consulted and through whom, and would they have gone through the same door? And can they tell, from what the record says about harm, whether an investor reading the same view would learn where to buy? If all three, the voice half of the break has cost nothing — and this is a test of whether the face and the record are legible, not of whether the law was met, which the record and counsel carry.

> [L743] For a departure from the floor, the test is the intruder's hour, with the floor's new value. For a departure from the held layer's resolution, it is the scene's own reading of the coarser map. For a departure from the withdrawal tiers, it is a contributor asked, before contributing, to say back what they could and could not take back. For a departure from "no ranking", it is the money view shown to the scene with the speculation column of the harm assessment beside it.

### 3.11 Chapter 11 (heading L505; 2 paragraphs; 352 words)

> [L507] The test for a departure from one of this chapter's rules is two conversations and a phone. **First, give the first screen to one reader of each of the three user groups the studio tests with (Chapter 2), on their own phone, and ask three things: what the dashboard says, which figure it rests on, and what they would do next.** If each gives the sentence, points to the figure and names a next step, the first screen works whatever pattern it took — the second and third questions are there because the title evidence says a reader will repeat a sentence whether or not the view supports it; if any answers "what am I looking at", or repeats the sentence and cannot find its figure, the schema, the sentence or the device has failed and the break has cost the reader. **Second, give one reader the authored account alone — the sentence and the written lines, with the charts covered — and one the views alone with their titles but without the written account, and ask both what the place is like.** If they agree, the two layers are one dashboard and the sequencing break has cost nothing; if they diverge, the authored account says something the views do not show, and the "how this argues" page is where to look for the crack.

> [L509] For a break in the interaction rules, the test is the Bayesian study's: show the static reading working without the control, then watch one real reader meet the control cold, and if they do not use it, remember that most will not and the surface they saw was the product. For a break in the hover rule, the test is a touchscreen and a keyboard, in that order. For a break in the citation rule, the test is a year: cite the state, change the data, and see whether the citation still finds what was cited. For a break in the map rules, the test is the 260-person study's: ask a reader to point to the smallest area and the largest value, without the legend, and count.

### 3.12 Chapter 12 (heading L489; 1 paragraph; 209 words)

> [L491] Run the five tests of section 10 on the page as built, with the three user groups and a holder of the harm frame. Then the two that this chapter adds. The *crop test, measured*: screenshot each panel and hand it to someone who has not seen the page; they must be able to say what the panel is about, its unit, its source, its date, for a comparison whether the gate passed, and for either column what the other column holds — without the page, and without being told where to look. If they cannot, the context was beside the frame. This is a legibility test; the chapter's own evidence says that a third of readers do not notice in-frame context unprompted, so the pass rate is the measure, not a single reader's success. The *review test*: the recognition record's line 9 is read back to the people who were in the room; they confirm that what they said is what is recorded and that what changed is what they asked for. It is a check on the record, not a validation of the account, which Chapter 9 says member checking cannot supply alone. A break in any Fixed rule above is logged with these two results attached.

### 3.13 Chapter 13 (heading L445; 1 paragraph; 283 words)

> [L447] A scan, three walks and a question; each has a pass. The *scan*: an automated checker on every layout, for contrast and the rest of what it catches; a pass is zero detected failures. The *keyboard walk*: mouse unplugged, every view reached, every control used, every view left, with focus visible throughout, on the desktop layout and on the phone layout with an external keyboard; a pass is no failure. The *zoom walk*: the phone layout at 400 per cent, which is the 320-pixel width 1.4.10 names, every view read, no two-dimensional scrolling except inside the map and the table and never for their headings or controls; text respaced to 1.4.12's values with nothing lost; a pass is no failure. The *screen-reader read*: a screen-reader user who has not seen the page, with one of the two commonest desktop readers or VoiceOver on a phone, says the view's sentence, the figure it rests on and a next step, using the written route and the table together; a pass is all three; the time against a sighted reader's is recorded. The *question*: a blind reader is asked what the trend is, what the figures are and, on a map, which places sit beside the one named; a sighted reader is asked the same from the chart; a pass is agreement on the trend, the figures and the neighbours — the chapter's evidence says the groups differ on interpretation, which is why interpretation is not asked. The structure, where built, is tested by the screen-reader read with the table covered. A departure from any Fixed rule above is logged with the five results attached, and the statement's line 9 carries it until it is fixed.

### 3.14 Chapter 14 (heading L514; 1 paragraph; 191 words)

> [L516] Run the four removals and the fifth check, and write the register entry. If the stripped version states every figure with its unit, base, date and gate, and the dressed version says nothing the stripped one does not, the expressive layer was free and the entry closes. If the stripped version lost a fact, the sort was wrong: the element was encoding it and belongs in the evidence layer, to be judged as an encoding and to meet the floor, and the test runs again. If the dressed version added a fact — a size, an order, a brightness, a cause — the element has failed Mackinlay's second clause, and the fix is to scale it to the data, or to state the distortion in words on the form and ship the twin beside it as the Doughnut's authors did, or to re-tier it as Decorative and remove the scaling. Then the comparison: readers who saw the stripped view and readers who saw the dressed one, asked what the data said; the entry closes when the two groups agree on the figures and the trend and may differ on everything else.

### 3.15 Chapter 15 (heading L519; 1 paragraph; 173 words)

> [L521] A break here is a departure from one of this chapter's rules, or a borrowing from a sector on terms the chapter did not set. Take any rule the build uses for provenance, change over time, reach or an ending, and find its entry in the precedent record. If the entry's nine lines are filled — the rule as printed from a dated source, the reason, the evidence or "none found", the condition, the house's changes with their reasons, the status and the review — the rule was borrowed and the house owns its departures. If the entry is missing, the rule is unexamined; if its reason line is empty, it is a habit; if its evidence and cost lines are empty, it is a bet. Then the reader test from section 14 for any change-over-time device: a reader shown the most recent period says what the data say about it, and the pass is that the reader reports the direction the device states and does not read an artefact as a movement.

*15 sections, 19 paragraphs, 3060 words.*

### 3.16 Classification by form

The five forms asked for: **removal** (take something away and see what is left); **adversarial walk** (go to a state with bad intent — try to break, name, crop or misuse it); **reader test** (a reader is asked and the answer compared); **recomputation** (the number is rebuilt, recounted or re-measured from its parts, or checked later against what happened); **record check** (a document is inspected). The classification is mine. Two tables: the first gives one form per chapter — the test the section leads with (its bold sentence where it has one); the second lists every separate test the sections name, because most sections name several.

**A. The leading test of each chapter.**

| Ch | The leading test, as printed | Form | Note |
|---|---|---|---|
| 1 | "find the person the rule protects and show them." | reader test | Three instances given: the bottom of the ranking; someone who needs the data; the smallest unit. |
| 2 | "find the reader who grades by the opposite rule and show them." | reader test | Four instances: a What Works analyst; the report's author; a resident; the people quoted. |
| 3 | "give the display to the reader the rule protects, for the time the rule assumes, and ask them what it says." | reader test | Timed; one instance is also a removal (the chart printed in greyscale). |
| 4 | "hand the display to someone who was not in the room, with the decision it is meant to bear, and ask them to reconstruct how the number was made and what would change it." | reader test | The reader's task is a reconstruction — the nearest any leading test comes to recomputation; the chapter says "the test is not whether a reader misreads but whether the figure can be *checked*". |
| 5 | "hand the composed number and whatever accompanies it to someone who was not in the room, and ask them to reconstruct how it was made, what would change it, and what one part is worth in terms of another." | reader test | Reconstruction again ("the same as Chapter 4's"). |
| 6 | "give the figure and what accompanies it to someone who was not in the room, and ask them four questions…" | reader test | Four questions. |
| 7 | "give the comparison and what accompanies it to someone who was not in the room and ask four questions…" | reader test | Four questions. |
| 8 | "take one of the page's sources away, or stop its refresh, and open it on the baseline phone a week later." | removal | Followed by a reader ("a reader who was not in the room can tell, from the face alone…"). |
| 9 | "show the felt result, with its record, to someone who gave an answer and to someone who was not asked, and listen for three things." | reader test | "a conversation"; two readers. |
| 10 | "First, give the view and its record to someone who knows the scene and was not consulted, and ask them to find a person or a room in it in an hour." / "Second, give the same view and the record to someone in the scene who was described by it and was not asked, and listen for three things." | adversarial walk (first half) + reader test (second half) | The section says the test "has two halves, and both are conversations". Counted below as one adversarial walk and one reader test. |
| 11 | "First, give the first screen to one reader of each of the three user groups… on their own phone, and ask three things…" / "Second, give one reader the authored account alone… and one the views alone…" | reader test | Two reader tests (three-phones; two-readers); the second works by removal (each reader has one layer covered). |
| 12 | "Run the five tests of section 10 on the page as built, with the three user groups and a holder of the harm frame." | reader test | Section 10 calls them "read-aloud tests run in a room"; then the crop test and the review test are added. |
| 13 | "A scan, three walks and a question; each has a pass." | none of the five alone — a battery | An automated scan, two walks under a removed capability (mouse; screen width), and two reader tests. Counted below under "battery". |
| 14 | "Run the four removals and the fifth check, and write the register entry." | removal | Then a record check (the entry) and a reader comparison. |
| 15 | "Take any rule the build uses for provenance, change over time, reach or an ending, and find its entry in the precedent record." | record check | Then one reader test. |

Count of leading tests by form (15 chapters; Chapter 10 has two halves, so 16 entries): **reader test 11** (Chs 1, 2, 3, 4, 5, 6, 7, 9, 10 second half, 11, 12); **removal 2** (Chs 8, 14); **adversarial walk 1** (Ch 10 first half); **record check 1** (Ch 15); **recomputation 0**; **a battery fitting no single form 1** (Ch 13).

**B. Every separate test named in the fifteen sections.**

| Ch | The test, in the section's terms | Form | Note |
|---|---|---|---|
| 1 | Give the ranking to someone at the bottom of it and ask if it is fair | reader test |  |
| 1 | Give the display to someone who needs the data underneath and ask them to get it | reader test |  |
| 1 | Give the unscaled measure to the smallest unit in it and ask whether they can see themselves | reader test |  |
| 2 | Give the impact claim to a What Works analyst and ask what level it is | reader test |  |
| 2 | Give the £-headline to the person who wrote the report it came from and ask if they recognise their caveats | reader test |  |
| 2 | Give the property-value panel to a resident of the street and ask what it means to them | reader test |  |
| 2 | Give the "voices" panel to the people quoted in it and ask whether they could change it | reader test |  |
| 3 | Print the legend chart in greyscale and give it to someone with protanopia | removal | colour removed; then a reader |
| 3 | Give the truncated bar to someone for five seconds; ask how big the difference is, then ask them to read the numbers | reader test | timed; two answers compared |
| 3 | Give the error bar to a statistician and ask what it means for one person | reader test |  |
| 3 | Give the hover to someone on a phone | removal | hover removed by the device |
| 4 | Someone not in the room reconstructs how the number was made and what would change it, from the face and one tap | reader test | reconstruction task |
| 5 | Someone not in the room reconstructs how the composed number was made, what would change it, and what one part is worth in terms of another | reader test | reconstruction task |
| 5 | Audit rule: a year on, can anyone say whether the measured thing moved, from a source that is not the measure | recomputation | later, against an independent source — the loosest fit |
| 6 | Four questions to someone not in the room: who is in the record; gross or net; what rung; could this be noise | reader test |  |
| 6 | Alert rules: after a year, count the alarms answered and found to be nothing; compare with the declared false-alarm rate | recomputation | "later and arithmetical" |
| 6 | Small-number rules: as someone who knows the scene, try to name the venues behind a withheld count | adversarial walk | "the test is adversarial" |
| 7 | Four questions to someone not in the room: what is held equal; who chose the comparators; could these two be told apart; what else could have moved the line | reader test |  |
| 7 | Ranking rule: crop the display as a hostile reader would, and see whether what survives is a league table | adversarial walk | "the test is adversarial"; also a removal (the crop) |
| 7 | Projection rules: a year on, compare the projection with the outturn; did the range hold; was the switching value crossed | recomputation | "later and arithmetical" |
| 8 | Take one of the page's sources away, or stop its refresh, and open it on the baseline phone a week later | removal | then a reader not in the room reads the face |
| 8 | Live element: the chain arithmetic done with real numbers and written in the record | recomputation |  |
| 8 | Vector map: the renderer's weight counted against the script budget on the baseline device, with the twin table present | recomputation | a measurement |
| 8 | Platform dependency: the clause that permits what the dashboard does, quoted in the record beside the series | record check |  |
| 8 | Studio of one: the name of the second | record check |  |
| 9 | Show the felt result, with its record, to someone who gave an answer and to someone who was not asked; listen for three things | reader test |  |
| 9 | Trace or signal shown as an indicator: the number beside the descriptor it is supposed to predict, same place, correlation stated | recomputation | "the convergent one" |
| 9 | Public self-placement: the private version run first and compared | reader test | two collections compared |
| 9 | Departure from the floor: the interval shown and the reason given | record check |  |
| 10 | Someone who knows the scene and was not consulted tries to find a person or a room in the view in an hour | adversarial walk | the intruder's hour |
| 10 | Someone in the scene, described and not asked, is given the view and record; listen for three things | reader test |  |
| 10 | Departure from the floor: the intruder's hour with the floor's new value | adversarial walk |  |
| 10 | Departure from the held layer's resolution: the scene's own reading of the coarser map | reader test |  |
| 10 | Departure from the withdrawal tiers: a contributor asked, before contributing, to say back what they could and could not take back | reader test |  |
| 10 | Departure from "no ranking": the money view shown to the scene with the speculation column of the harm assessment beside it | reader test |  |
| 11 | Three-phones: one reader of each user group, own phone, three questions (what it says; which figure; what next) | reader test |  |
| 11 | Two-readers: one reader the authored account alone, one the views alone; both asked what the place is like | reader test | by removal — each has one layer covered |
| 11 | Interaction rules: show the static reading working without the control, then watch one real reader meet the control cold | removal | the control removed; then a reader |
| 11 | Hover rule: a touchscreen and a keyboard, in that order | removal | the pointer removed |
| 11 | Citation rule: cite the state, change the data, and after a year see whether the citation still finds what was cited | record check | later; the citation re-resolved |
| 11 | Map rules: ask a reader to point to the smallest area and the largest value, without the legend, and count | reader test | legend removed; counted |
| 12 | The five read-aloud tests of section 10 (wrong unit; not in it; the account is wrong; the counted won; you lost), with the three user groups and a holder of the harm frame | reader test | five tests; one of them ("the member check, recorded") is also a record check |
| 12 | Crop test, measured: screenshot each panel; someone who has not seen the page says what it is about, unit, source, date, gate, the other column | removal | the page removed; the pass rate is the measure |
| 12 | Review test: the recognition record's line 9 read back to the people who were in the room | record check | "a check on the record, not a validation of the account" |
| 13 | The scan: an automated checker on every layout; zero detected failures | none of the five | an instrument check |
| 13 | The keyboard walk: mouse unplugged; every view reached, every control used, every view left | removal | a capability removed; the chapter calls it a walk |
| 13 | The zoom walk: the phone layout at 400 per cent; text respaced | removal | screen width removed; the loosest fit |
| 13 | The screen-reader read: a screen-reader user who has not seen the page says the sentence, the figure and a next step | reader test | time against a sighted reader's recorded |
| 13 | The question: a blind reader and a sighted reader asked the trend, the figures and the neighbours; agreement is the pass | reader test | two readers compared |
| 14 | The four removals: mono, silent, still, undressed | removal |  |
| 14 | The fifth check: stripped and dressed say the same thing | removal | a comparison of the two renders |
| 14 | Write the register entry (the boundary log) | record check |  |
| 14 | The comparison: readers who saw the stripped view and readers who saw the dressed one, asked what the data said | reader test | two groups compared |
| 15 | Find the rule's entry in the precedent record; are its nine lines filled | record check |  |
| 15 | The reader test from section 14 for any change-over-time device: a reader shown the most recent period says what the data say about it | reader test |  |

**Count by form (55 named tests):** **reader test 27**; **removal 10**; **record check 7**; **recomputation 6**; **adversarial walk 4**; **none of the five 1**.

| Form | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reader test | 3 | 4 | 2 | 1 | 1 | 1 | 1 |  | 2 | 4 | 3 | 1 | 2 | 1 | 1 | 27 |
| removal |  |  | 2 |  |  |  |  | 1 |  |  | 2 | 1 | 2 | 2 |  | 10 |
| record check |  |  |  |  |  |  |  | 2 | 1 |  | 1 | 1 |  | 1 | 1 | 7 |
| recomputation |  |  |  |  | 1 | 1 | 1 | 2 | 1 |  |  |  |  |  |  | 6 |
| adversarial walk |  |  |  |  |  | 1 | 1 |  |  | 2 |  |  |  |  |  | 4 |
| none of the five |  |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  | 1 |
| **All** | 3 | 4 | 4 | 1 | 2 | 3 | 3 | 5 | 4 | 6 | 6 | 3 | 5 | 4 | 2 | **55** |

**What the sections say to do with the result.** Chapters 1–7 end by sending the break to Chapter 16's record: Ch 1 "log it in the four-line record Chapter 16 describes"; Chs 2 and 3 the same with the fields "(what rule, why, for whom, what proved it)"; Chs 4 and 5 "the four-line record Chapter 16 will describe (what rule, why, for whom, what proved it)"; Chs 6 and 7 "Log the break in the four-line record Chapter 16 will describe." Chapters 8, 9, 10 and 11 do not say to log anything. Chapter 12: "A break in any Fixed rule above is logged with these two results attached." Chapter 13: "A departure from any Fixed rule above is logged with the five results attached, and the statement's line 9 carries it until it is fixed." Chapter 14 writes "the register entry" (its own boundary log). Chapter 15 reads its own precedent record. None of Chapters 8–15 names Chapter 16 in this section.

**Who the section says the test is for.** "a Fixed rule" / "the Fixed rules above": Chs 1, 2, 3, 4, 5, 6 ("Most of the Fixed rules here"), 12, 13. "a comparison rule" / "one of this chapter's rules" / "a departure" without a tier: Chs 7, 8, 9, 10, 11, 15. Chapter 14 names no rule: it tests every expressive element.

---

## PART 4 — THE FLAGS TO CHAPTER 16 AND TO THE END

### 4.1 Lines containing `[Revisit → Ch 16]` — 6 lines

Searched with the arrow character and as plain text "Revisit → Ch 16"; also checked for combined forms such as `[Revisit → Ch 15; Ch 16]` (none exist: every `[Revisit → …]` flag in the book names exactly one chapter). Each line is quoted in full, with chapter, file line and the section it sits in.

**Ch 11 · L566 · in "Open questions and flags"**

> - `[Further research]` **What the regime costs the maker.** A face sheet per view, snapshots per release and two tests per first screen are not priced here, in a chapter that opens with the official warning that dashboards "require a lot of maintenance"; the Decision Book's candidate chapter should carry a minimum version `[Revisit → Ch 16]`.

**Ch 11 · L570 · in "Open questions and flags"**

> - `[Revisit → Ch 16]` The face sheet as a build artefact; the purchase table's cut list; the retirement plan.

**Ch 12 · L544 · in "Open questions and flags"**

> - `[Revisit → Ch 16]` The recognition record and the label rule as build artefacts; the crop test as a release gate.

**Ch 13 · L495 · in "Open questions and flags"**

> - `[Revisit → Ch 16]` The statement, the three walks and Chartability as release gates; the rules register's accessibility rows.

**Ch 14 · L560 · in "Open questions and flags"**

> `[Revisit → Ch 16]` The boundary log as the override log's specialisation; whether the tier vocabulary adopts "specific sensory experience"; the three-sentence evidence standard.

**Ch 15 · L562 · in "Open questions and flags"**

> `[Revisit → Ch 16]` The precedent record beside the boundary log and the override log; the status marks [p] [r] [f] against this book's own dagger; the twelve records as one document; the regulator's minimum list as a checklist the house can voluntarily meet; the retirement plan as a Fixed rule.

By chapter: Ch 11: 2, Ch 12: 1, Ch 13: 1, Ch 14: 1, Ch 15: 1. Chapters 0–10 print none. (Chapters 1–10 hand things to Chapter 16 in other words — see 4.3.)

### 4.2 Lines containing `[Revisit at end]` — 60 lines (44 uses of the flag; 16 lines that only list the flag in a legend)

| Ch | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lines with the flag | 1 | 4 | 2 | 2 | 3 | 2 | 5 | 4 | 5 | 7 | 6 | 5 | 3 | 3 | 4 | 4 | 60 |
| of which uses (not a legend listing) | 0 | 3 | 1 | 1 | 2 | 1 | 4 | 3 | 4 | 6 | 5 | 4 | 2 | 2 | 3 | 3 | 44 |

**4.2a The uses**, each quoted in full.

**Ch 1 · L196 · in "6 · The arithmetic of the biggest"**

> The last fact bites hardest for anyone trying to see a small scene. Statistical offices suppress or disturb small counts, for two reasons given in one breath: reliability and confidentiality. The US Centers for Disease Control's cancer registry does not show "statistics based on counts below 16." The ONS's standard rule for published tables is the "10-5 rule" — suppress below ten, round to the nearest five above. The 2021 Census swapped rare records between areas and added noise to "around 14% of cell counts," so that "where there is a cell count of one in a published output, there is a high chance that it could be a swapped record, a perturbed count or an imputed record." And the technique used to fill the gaps, small-area estimation, "will tend to shrink estimates towards the average level … so estimates at each end of the scales tend to be over- or under-estimated." The design of official statistics removes, by rule, precisely the small cells where a local reader would look for the interesting case — not from malice but from method. Any dashboard built only from official sources will be blind in exactly the places Carly's brief cares about, and must say so rather than show a blank. `[Revisit at end]` This is the statistical root of a problem that Chapters 4, 6 and 10 each inherit a piece of: a disclosure threshold decides, before any screen is drawn, how many people a scene must contain before it can be seen.

**Ch 1 · L359 · in "Open questions and flags"**

> - `[Revisit at end]` **The suppression threshold.** Its statistical root is here; its collection, display and ethical consequences are in Chapters 4, 6 and 10. Close the loop at the end.

**Ch 1 · L360 · in "Open questions and flags"**

> - `[Revisit at end]` **Is "dashboard" the right word for the whole book?** This chapter reclaims it; Chapter 16 should ask whether the reclaimed word survived fifteen chapters of use.

**Ch 2 · L530 · in "Open questions and flags"**

> - `[Revisit at end]` **Can one display be legible to eight graders?** This chapter aims at legibility without persuasion and concedes that the first screen is in somebody's grammar; whether the Part 3 chapters find a form that keeps the other grammars reachable is the test, and if they do not, truth 1's design consequence should be demoted from Fixed.

**Ch 3 · L526 · in "Open questions and flags"**

> - `[Revisit at end]` **Does "canonical" survive?** Nineteen truths is still a long list; the closing chapter should ask which were cited by later chapters and demote the rest.

**Ch 4 · L295 · in "6 · The six kinds of nothing"**

> The 2021 Census chose the opposite trade. Rather than suppress small cells, the ONS swapped rare records between areas and perturbed counts: "Where there is a cell count of one in a published output, there is a high chance that it could be a swapped record, a perturbed count or an imputed record, or a combination of these", and "the totals of all cells may in turn be different … the differences should be small and so should not change the conclusions of any analysis or research." A table with no blanks and no literal small numbers: every cell is quietly [e], and the small counts a local reader would lean on are the least literal. Each approach is defensible; each puts a different kind of nothing behind what looks like a number, and a display built on either should say which. `[Revisit at end]`

**Ch 4 · L652 · in "Open questions and flags"**

> - `[Revisit at end]` **Suppress or perturb** — the disclosure threshold's display and ethical consequences, with Chapter 1's root and Chapter 10's ethics.

**Ch 5 · L501 · in "Open questions and flags"**

> - `[Revisit at end]` **The form question.** Once Chapters 6–16 exist, the closing chapter should set the five forms against every reader and every rule and say which the book's own evidence favours — without making the decision, which is Carly's.

**Ch 6 · L619 · in "Open questions and flags"**

> - `[Revisit at end]` **The gross-to-net arithmetic as a house standard.** Whether the book adopts the Additionality Guide's sequence as the studio's own, given that the guide is withdrawn and nothing has replaced its definitions.

**Ch 6 · L620 · in "Open questions and flags"**

> - `[Revisit at end]` **The two tests for a canonical truth.** Whether "out-of-sample plus the agreement of the competent" becomes the book's definition of a canonical truth, which Chapter 0 currently leaves to the reader.

**Ch 6 · L639 · in "Looking back"**

> - **Opens a thread** for Chapter 0's legend: "reconstructed" (an abstract rebuilt from an index) is now used and should be defined; "Fixed as a procedure" is used more here than anywhere, for rules whose steps are fixed and whose parameter — run-length, base size, window, error rate — is open; and the chapter proposes that a "canonical truth" be defined by two tests, out-of-sample and the agreement of the competent, which Chapter 0 should either adopt or decline. `[Revisit at end]`

**Ch 6 · L769 · in "Gaps found while writing this chapter"**

> | The AQuA Book 2025 has no statement about validating a model against outturn; its validation is user-needs-based | Reported the negative finding; built the two-test standard (out-of-sample plus agreement of the competent) from the holdout literature and Glover | Amber — "validated" in UK guidance may mean "the users agreed", which a reader would not expect | Chapter 0 (definition of a canonical truth); `[Revisit at end]` |

**Ch 7 · L554 · in "Open questions and flags"**

> - `[Revisit at end]` **The comparison record and the three records before it.** Chapters 4, 5, 6 and 7 now ask for a provenance set, a recipe card, a claim record and a comparison record; the closing chapter should say whether they are one document with four parts.

**Ch 7 · L555 · in "Open questions and flags"**

> - `[Revisit at end]` **Whether the Vibe Map projects at all.** Section 13's last choice.

**Ch 7 · L697 · in "Gaps found while writing this chapter"**

> | Four records now sit beneath a dashboard's numbers across Chapters 4–7 | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

**Ch 8 · L526 · in "12 · What holds true regardless"**

> The truths are kept by a record, as Chapters 4 to 7 each produced one — the provenance set, the recipe card, the claim record and the comparison record — and whether these five are one document is a question for the end of the book `[Revisit at end]`. The *service record* is written before the dashboard launches, by the person who will keep it, and it answers ten questions. Each line is short; the point is that each is answered, and that the last — what is not promised — is answered too, because section 7 showed that a year of silent reliability makes a promise whether or not one was written.

**Ch 8 · L695 · in "Open questions and flags"**

> - `[Revisit at end]` **Five records.** The provenance set (Ch 4), recipe card (Ch 5), claim record (Ch 6), comparison record (Ch 7) and service record (Ch 8) may be one document with five parts; the service record's line 2 overlaps the provenance set's source lines. Chapter 0 should say.

**Ch 8 · L715 · in "Looking back"**

> - **Strengthens** Chapter 4 throughout. The provenance set's "revision status" becomes three dates and a frequency; its platform caveat becomes a dependency on terms; its "a zero that is a null" becomes "Invalidating or emptying local state as a result of a failed refresh". **Opens a thread**: line 2 of the service record and the provenance set's source lines overlap; one may contain the other. `[Revisit at end]`

**Ch 8 · L892 · in "Gaps found while writing this chapter"**

> | Five records now sit beneath a dashboard's numbers across Chapters 4–8 | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

**Ch 9 · L442 · in "14 · The studio's own positions, tested"**

> **"It fails if its an aggregation of 'the biggest'."** The scenes method, the vitality proxies and the trace studies all weight by what is listed, counted or connected most, and the trace literature's own authors name the "majority bias" and the hole where one of the poorest districts was. The failure register's sentence is the trace family's documented limitation. *Strengthened* — with one tension the chapter cannot resolve: the official floor of fifty answers, adopted in truth 3, would remove from a felt panel exactly the small rooms the brief says must not disappear. The two positions are both the studio's, and the chapter records the conflict rather than choosing: a room under the floor is shown as present and unmeasured, never as absent, and the floor itself is a question for the end of the book `[Revisit at end]`.

**Ch 9 · L468 · in "15 · What holds true regardless"**

> Chapters 4 to 8 each left a record beneath a dashboard's numbers — the provenance set, the recipe card, the claim record, the comparison record, the service record — and whether they are one document is for the end of the book `[Revisit at end]`. A felt measure needs its own, because none of the five says who was asked how they felt and how the asking was tested. The *measure record* has twelve lines; it is opened before the first person is asked and filled as the work proceeds.

**Ch 9 · L648 · in "Open questions and flags"**

> - `[Revisit at end]` **The floor and the small room.** The official floor of fifty answers for a felt estimate and the brief's rule against "an aggregation of 'the biggest'" pull against each other for the smallest rooms; this chapter shows an under-floor room as present and unmeasured, and leaves the floor's value to the end of the book and to Chapter 10's disclosure rules.

**Ch 9 · L649 · in "Open questions and flags"**

> - `[Revisit at end]` **Six records.** The provenance set, recipe card, claim record, comparison record, service record and measure record; whether they are one document; whether the measure record's line 12 and the service record's "what this changed" are the same field.

**Ch 9 · L851 · in "Gaps found while writing this chapter"**

> | The cold reader found "register", "measure", "instrument", "indicator", "co-produced", "recognition", "record" and "face" each used in more than one sense, the family of section 5 named by a word the chapter reserves for something stricter, and the floor of fifty unexamined against the brief's own "aggregation of the biggest" | Defined the words in Before you start; renamed the family; added the floor question to section 14 and the flags | Amber — the floor question is a real tension and is logged, not resolved | Entry 9; `[Revisit at end]` |

**Ch 9 · L852 · in "Gaps found while writing this chapter"**

> | Six records now sit beneath a dashboard's numbers | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

**Ch 10 · L572 · in "18 · The studio's own positions, tested"**

> *The floor of fifty against the small room.* Chapter 9 left this `[Revisit at end]`. This chapter separates the floors: fifty is a precision floor on a mean and has nothing to do with disclosure; the small room is lost to reliability, not to identification, and it is shown as *present, n answered, not scored*, or as *held*, never as absent — "potential risk should not necessarily be used as a rationale for avoiding local or small area data altogether". The tension is narrowed, not closed: the end of the book still decides whether a room under both floors is shown as unmeasured or held, and who decides which.

**Ch 10 · L614 · in "19 · What holds true regardless"**

> Chapters 4 to 9 each left a record — the provenance set, the recipe card, the claim record, the comparison record, the service record, the measure record — and whether they are one document is for the end of the book `[Revisit at end]`. This chapter leaves a seventh, because none of the six says what was done to protect the people in the data, on what basis, with whose voice, and what it cost them. The *safeguards record* takes its name from the statute's own phrase for what research and statistics must carry — "appropriate safeguards for the rights and freedoms of the data subject" — and has fourteen lines. Its first line is written before the first row is collected; it is dated, it names a person, and it is re-read against the current law on a stated schedule.

**Ch 10 · L812 · in "Open questions and flags"**

> - `[Revisit at end]` **Seven records.** Provenance set, recipe card, claim record, comparison record, service record, measure record, safeguards record — whether one document; whether the measure record's line 12, the service record's "what this changed" and this record's line 14 are one field.

**Ch 10 · L813 · in "Open questions and flags"**

> - `[Revisit at end]` **The room under both floors.** Unmeasured or held, and who decides which; the floor of fifty is a precision rule and this chapter has moved the tension there.

**Ch 10 · L1064 · in "Gaps found while writing this chapter"**

> | Seven records now sit beneath a dashboard's numbers | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

**Ch 11 · L390 · in "11 · What holds true regardless"**

> Chapters 4 to 10 each left a record beneath a dashboard's numbers, and whether the seven are one document is for the end of the book `[Revisit at end]`. This chapter leaves something different in kind: not an eighth record about the data but a sheet about the *surface* — one per view, which says what of the seven records sits on this face, what the view says and to whom, what it costs to touch, and how it is cited. It is called the *face sheet*, it has twelve lines, and its first line is written before the view is drawn.

**Ch 11 · L571 · in "Open questions and flags"**

> - `[Revisit at end]` **Seven records and a face sheet.** Whether the records are one document and the face sheet is its front page; whether the measure record's line 12, the service record's "what this changed", the safeguards record's line 14 and the face sheet's line 12 are one field.

**Ch 11 · L572 · in "Open questions and flags"**

> - `[Revisit at end]` **The 60-second version**, raised a seventh time: this chapter's runs long, and the chapter's own finding is that readers read 28 per cent.

**Ch 11 · L766 · in "Gaps found while writing this chapter"**

> | Seven records and now a face sheet | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 |

**Ch 12 · L375 · in "12 · What holds true regardless"**

> Chapters 4 to 11 each left a record; whether they are one document is for the end of the book `[Revisit at end]`. This chapter leaves a ninth, one per place-page, called the *recognition record*. Ten lines, written before the page is published and updated at every review.

**Ch 12 · L545 · in "Open questions and flags"**

> - `[Revisit at end]` Nine records; whether one document. The 60-second version's length (raised an eighth time).

**Ch 13 · L346 · in "11 · What holds true regardless"**

> Chapters 4 to 12 each left a record; whether they are one document is for the end of the book `[Revisit at end]`. This chapter's tenth is different in kind from the others and the same in kind as the public sector's: it is published, in the model statement's form, and it is the record. Its lines — the model's own (status; non-accessible content and why; alternatives; contact; preparation and testing) with the house's per-view lines between them:

**Ch 13 · L496 · in "Open questions and flags"**

> - `[Revisit at end]` Ten records; the statement as the public one. The 60-second version's length (raised a ninth time).

**Ch 14 · L342 · in "8 · The deaf reader of a dashboard about sound"**

> Chapter 13 reported that sonification is a route beside a text route and never instead of it, from the blind reader's side. This section adds the deaf reader's: the same rule, for the opposite reason. A sonified series without its document excludes one reader; a sonified series without its chart excludes the other; the series, the chart and the document are three routes to one view, and the view record (Chapter 11) lists all three. `[Revisit at end]` *(Reading.)*

**Ch 14 · L450 · in "11 · What holds true regardless"**

> `[Revisit at end]` Whether the eleven records beneath the dashboard are one document is the standing question; this one is the first that is a log, and a log may want to live in the design repository rather than on the public page, with its existence declared on the page.

**Ch 14 · L562 · in "Open questions and flags"**

> `[Revisit at end]` Whether the eleven records are one document, and whether a log belongs on the page or in the repository with a declaration on the page.

**Ch 15 · L452 · in "12 · What holds true regardless"**

> `[Revisit at end]` Whether the twelve records beneath the dashboard are one document; this one, like the boundary log, is a list that grows.

**Ch 15 · L564 · in "Open questions and flags"**

> `[Revisit at end]` The fold question (section 11); whether the twelve records are one document.

**Ch 15 · L682 · in "Gaps found while writing this chapter"**

> | The precedent record's place among twelve records | §12 | A growing list, like the boundary log | Chapter 16; `[Revisit at end]` |

**4.2b The legend listings** (the flag is named in the chapter's list of conventions, not used). For these, the sentence that lists the flags is quoted; the full line is the chapter's "Before you start" paragraph or Chapter 0's flag table row.

- **Ch 0 · L113 · in "The legend: what kind of claim is this, and how firm is it?"** — | `[Revisit at end]` | A question to return to once all chapters exist, because its answer depends on them |
- **Ch 1 · L12 · in "Before you start"** — And flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]` (something the Vibe Map can settle with its own data), `[Validate with users]`, `[Revisit at end]`, and `[Rich reference]` (worth your own time).
- **Ch 2 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]` (something the Vibe Map can settle with its own data), `[Validate with users]`, `[Revisit at end]`, `[Rich reference]` (worth your own time) and `[Counterbalance → Ch n]` (a finding that pulls against an earlier chapter's, recorded rather than resolved).
- **Ch 3 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]` (something the Vibe Map can settle with its own data), `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 4 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]` (something the Vibe Map can settle with its own data), `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 5 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 6 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 7 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 8 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 9 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 10 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 11 · L12 · in "Before you start"** — Flags in square brackets mark loose ends: `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → Ch n]`.
- **Ch 12 · L12 · in "Before you start"** — Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0 and used here as there.
- **Ch 13 · L12 · in "Before you start"** — Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0.
- **Ch 14 · L12 · in "Before you start"** — Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0.
- **Ch 15 · L12 · in "Before you start"** — Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0.

### 4.3 Supplement — other lines that name Chapter 16 or "the closing chapter" without either flag — 27 lines

Not asked for, but they are hand-offs to this chapter made in other words. 48 lines in all name "Chapter 16", "Ch 16" or "the closing/last/final chapter": 16 are already quoted in 4.1 or 4.2; 5 name the *Decision Book's* Chapter 16 (its chapter on structure and framing), not this book's — ch07 L576 and L704, ch12 L136, L693 and L720 — and are left out; the remaining 27 follow. For lines over 700 characters the sentence(s) naming Chapter 16 are quoted, marked "[sentence]"; shorter lines are quoted whole.

- **Ch 0 · L55 · in "How a chapter teaches"** — | **What holds true regardless** | The canonical part: numbered truths, each with its kind and firmness. Later chapters test them; the last chapter confirms or demotes them |
- **Ch 0 · L95 · in "The legend: what kind of claim is this, and how firm is it?"** — Two refinements the chapters use. A truth may be **Fixed as a statement of the record** — the evidence says this and the book will not pretend otherwise — without the design rule that follows from it being Fixed; the chapter says which. And a rule may be **Fixed as sequence**: the order of operations is the hard line (define the construct before the proxy; check recognition before release), while the form each step takes is Adaptable. Where you deviate from a Fixed or Adaptable rule, Chapter 16 gives the four-line record to keep and the test to run first.
- **Ch 0 · L157 · in "Words this book uses, and what they mean"** — - **The override log** — the four-line record kept whenever a rule is deliberately broken: trigger, rule and tier, alternative chosen, evidence. Chapter 16.
- **Ch 0 · L195 · in "Gaps found while writing this chapter"** — | The design system's interim rule says "never RAG tags" for public severity marks; the book's gap register uses red / amber / yellow | Kept RAG inside the gap register, which is an internal working record; anything that travels in the reader uses words, not coloured severity | Yellow | Chapter 16; design system open decision 12 |
- **Ch 0 · L197 · in "Gaps found while writing this chapter"** — | "Fixed" was being used for three things (a rule to obey; a fact the book is confident of; a sequence that is the hard line) and a cold reader of Chapter 2 could not tell which | Named the two refinements above — Fixed as a statement of the record; Fixed as sequence — so that chapters can say which they mean | Amber | Chapter 16's rule register should check every Fixed for which sense it carries |
- **Ch 1 · L245 · in "9 · What holds true regardless"** — The candidate canonical truths this chapter contributes, each with its kind and firmness. Later chapters test them; the closing chapter confirms or demotes them.
- **Ch 1 · L328 · in "What proves a break works"** — If you must build a dashboard that breaks one of the Fixed rules above — a ranking without intervals, a display without a data release, a measure that is not scaled — the test is the same in every case: **find the person the rule protects and show them.** Give the ranking to someone at the bottom of it and ask if it is fair. Give the display to someone who needs the data underneath and ask them to get it. Give the unscaled measure to the smallest unit in it and ask whether they can see themselves. If the break survives that, log it in the four-line record Chapter 16 describes. If it does not, it was not a break; it was a mistake.
- **Ch 1 · L467 · in "Gaps found while writing this chapter"** — | No independent measurement exists of how many dashboards go unused | Refused to print a percentage; stated the gap as a rule | Yellow | Chapter 16's rule register |
- **Ch 2 · L379 · in "10 · What holds true regardless"** — The candidate canonical truths this chapter contributes, each with its kind and firmness. Later chapters test them; the closing chapter confirms or demotes them.
- **Ch 2 · L476 · in "What proves a break works"** — [sentence] If the break survives that, log it in the four-line record Chapter 16 describes (what rule, why, for whom, what proved it).
- **Ch 2 · L686 · in "Gaps found while writing this chapter"** — | The chapter's first rule asserted that one display can be legible to all readers, while its own sources say the first screen is always in somebody's grammar | Rewrote the rule to require that the choice of grammar be made and declared; flagged the feasibility question for the end of the book | Red — a Fixed rule resting on an unproven premise | Chapter 16's rule register; Part 3 |
- **Ch 3 · L361 · in "13 · What holds true regardless"** — The brief asked for "the short list that survives". Here it is in two parts: the canonical truths — seven, each a rule a dashboard can be held to — and, beneath them, the findings of record that justify them, which are true statements about the evidence rather than rules in their own right. Later chapters test both; the closing chapter confirms or demotes.
- **Ch 3 · L467 · in "What proves a break works"** — [sentence] If the reading survives, log the break in the four-line record Chapter 16 describes (what rule, why, for whom, what proved it).
- **Ch 4 · L580 · in "What proves a break works"** — [sentence] Log the break in the four-line record Chapter 16 will describe (what rule, why, for whom, what proved it).
- **Ch 5 · L441 · in "What proves a break works"** — [sentence] Log the break in the four-line record Chapter 16 will describe (what rule, why, for whom, what proved it).
- **Ch 6 · L310 · in "9 · Pattern discovery, and the garden of forking paths"** — [sentence] That is a description of what "canonical truth" means in operation, and this book adopts it as a working definition until the closing chapter revisits it.
- **Ch 6 · L539 · in "What proves a break works"** — [sentence] Log the break in the four-line record Chapter 16 will describe.
- **Ch 7 · L480 · in "What proves a break works"** — [sentence] Log the break in the four-line record Chapter 16 will describe.
- **Ch 11 · L606 · in "Looking back"** — - **Opens threads** for Chapter 12 (the sentence per place as recognition; the two columns on a first screen), Chapter 13 (the criteria in full; the equivalent route), Chapter 14 (what a creative treatment may do to the sentence, the breaks and the stamp), Chapter 16 (the face sheet, the cut list and the retirement plan as build artefacts), and the end of the book (seven records and a face sheet; the 60-second version's length).
- **Ch 14 · L464 · in "12 · Where the choice is yours"** — **Open, and the house's to decide with a reason recorded.** Whether the boundary log is public or internal. Whether the committee export is a separate deliverable or the stripped state of the same page. Whether the studio adopts the W3C's third category, "specific sensory experience", into its tier vocabulary as a fourth tier or as a sub-kind of Decorative with an identification duty; this chapter uses it, requires the identification the W3C requires, and leaves its place in the house's vocabulary to Chapter 16. Whether a probe is built to test the two-audience claim, which has no measurement anywhere in this book. `[Prototype flag]`
- **Ch 14 · L572 · in "Looking back"** — **Chapter 0.** The tier vocabulary now has a formal ancestor (Mackinlay) and a missing category (the W3C's specific sensory experience). Strengthens; opens a thread for Chapter 16.
- **Ch 14 · L714 · in "Gaps found while writing this chapter"** — | The tier vocabulary lacks the W3C's "specific sensory experience" | §6, §11 | Used in the register; adoption left to Chapter 16 | Chapter 16; the Decision Book |
- **Ch 14 · L733 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"** — | Version 1 Ch 13 rule, genre Fixed | §10 | Re-tiered Adaptable | Carried to Chapter 16's register |
- **Ch 14 · L734 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"** — | Version 1 Ch 13 rule, five/ten words Fixed | §10 | Re-tiered Adaptable; distance and seconds Fixed beneath it | Carried to Chapter 16's register |
- **Ch 15 · L210 · in "4 · Finance and risk"** — [sentence] The UK's Analysis Function, in its symbols guidance (January 2022): "[p] = provisional", "[r] = revised", "[f] = forecast"; "Whenever you use a shorthand marker in a table it should be in square brackets, for example: '[r]'."; and "We do not recommend using symbols such as '. :', '*' or '†' anymore because they can be difficult to see and screen reader software can find them hard to recognise." (read once) — which this book's own dagger convention will meet in Chapter 16.
- **Ch 15 · L694 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"** — | This book's own dagger (†) convention | §4 | The Analysis Function advises against '†' because screen readers find it hard; the book uses it in prose, not tables | Carried to Chapter 16: whether the book's own marks meet the floor |
- **Ch 15 · L696 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"** — | Decision Book Ch 18 override log; Ch 14 boundary log | §12 | A third growing list, the precedent record | Chapter 16: whether three logs are one |

### 4.4 Lines containing "Awaiting Carly" (3) or "Carly's call" (2)

**Ch 14 · L736 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"**

> | Decision Book ARG-12 (from Chapter 12's log) | — | Unchanged by this chapter; still in direct conflict | Awaiting Carly |

**Ch 15 · L698 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"**

> | BRIEF-v2 §6 fold note | §11 | A count: about forty mechanisms, about six already in the book | Awaiting Carly |

**Ch 15 · L699 · in "Design system (Style Guide v1.5) and Decision Book — conflict log"**

> | ARG-12 (from Chapter 12) | — | Unchanged | Awaiting Carly |

**Ch 5 · L651 · in "Gaps found while writing this chapter"**

> | The one sector composite is named in a method audit; the brief says the sector is not researched | Read only its published methodology; reported nothing about any place; flagged the placement for Carly | Amber — a line the book must hold carefully | Carly's call: here or Chapter 15 |

**Ch 15 · L410 · in "11 · The symmetry test"**

> **The brief's "could fold into Chapters 2 and 5".** The chapter's own test was whether it found mechanisms with terms rather than examples. It found about forty, listed in section 9. Some were already in the book in another form: the recipe card's ancestry in the QMI; the comparison record's in the ELS; the service record's in the Observatory's drift; the rank interval; the funnel; the sentence-first rule. Most were not — among them the metric page template, the labelled log, the two ledgers, the incompleteness band, the RAG and arrow rules, vintages, revision against correction and the printed revision size, the release-calendar and early-reader rules, the band-rule footnote, the three regulator sentences, the paired usage text, the frozen base year, the refusal to aggregate, the dotted break line, the fixed trust question, the question of whether the data informed a decision, the sunset note and the retirement clause. On that count the chapter has found more than a reading list; whether that earns it a chapter of its own is Carly's call, which the brief reserved to her and which has not yet been made.

Chapter 0 defines the neighbouring phrase (L165): - **Steer** — Carly's direction on a draft. "Awaiting steer" means she has not read it yet. — "Awaiting steer" itself is used in no chapter (0 matches in Chapters 1–15).

### 4.5 Supplement — other lines that leave something to Carly in other words — 35 lines

Patterns searched: "for Carly", "via Carly", "is Carly's", "Carly;", "| Carly |", "Carly's timeline", "logged for Carly", "belongs to Carly". The matching sentence is quoted for long lines ("[sentence]"); table rows and short lines are quoted whole. Lines that only say the sector knowledge is Carly's are included because they match; they are not decisions.

- **Ch 0 · L4 · in "(top)"** — *Version 2 · revised 6 October 2026, after Chapters 1 and 2 · for Carly's steer*
- **Ch 0 · L39 · in "What this book is not"** — - **Not the creative decisions.** The question "how do we make nightlife data as exciting as a club flyer" belongs to Carly and her designers. Chapter 14 sets out where evidence meets expression and stops there.
- **Ch 1 · L469 · in "Gaps found while writing this chapter"** — | The Decision Book's data chapters do not say "the unit of aggregation is a decision" | Stated it here from Openshaw; the Decision Book may want the rule | Amber — it transfers to every place-based chart | Decision Book gap register, via Carly |
- **Ch 2 · L682 · in "Gaps found while writing this chapter"** — | The brief's three user groups are, on the evidence, at least seven graders with contradictory rules | Built the reader table in section 1 as a Reading and said so | Amber — the prototype's user testing is organised in three groups | The brief and the test protocols, via Carly `[Validate with users]` |
- **Ch 2 · L683 · in "Gaps found while writing this chapter"** — | The Decision Book's evidence rules say how to show a number fairly, not whether the display is monitoring or evaluation | Took the Magenta Book's distinction as a Standard and made it a Fixed rule | Red — an implied counterfactual is the error the official reader is trained to catch | Decision Book gap register, via Carly; design system evidence rules |
- **Ch 2 · L687 · in "Gaps found while writing this chapter"** — | No reader was interviewed for a chapter about readers; two rows of the table have no study behind them | Said so in section 1; made the table the first thing to validate | Amber | The test protocols, via Carly |
- **Ch 2 · L695 · in "Design system (Style Guide v1.5) — conflict log"** — **Conflicts.** One possible. The guide's register — joy first, then value, evidence, action — is a persuasion order, and section 5 reports one study in which the reader already opposed was better served by the plain table than by the handsome object. This is not a conflict in the design system's own domain (the public, the scene, the sympathetic reader) but it is a conflict for the officer who arrives hostile. The resolution this chapter proposes is not to change the register but to make a plain view a first-class route. Logged for Carly; the design system may want a line on it. `[Counterbalance → design system]`
- **Ch 3 · L417 · in "15 · What this means for a nightlife dashboard"** — [sentence] What the Vibe Map claims to be is Carly's decision; this chapter only says that whatever it claims, it should look like that at once.
- **Ch 3 · L443 · in "The rules"** — | Design the first glance for simplicity and for looking like what the display claims to be | Appeal forms in 50 ms on complexity and prototypicality — websites, small student samples | Evidence (adjacent domain) | Adaptable (what it claims to be is Carly's) | Lindgaard et al. 2006; Tuch et al. 2012 |
- **Ch 3 · L542 · in "Looking back"** — [sentence] These are logged for Carly as candidate additions to the Decision Book's data chapters.
- **Ch 3 · L697 · in "Gaps found while writing this chapter"** — | The Decision Book's chart chapter rests 3D and pie rules on the conjectural half of the perceptual hierarchy | Kept the rules, replaced the reasons, and logged the conflict | Amber — a reader who learns the real evidence will distrust the rule | Decision Book Ch 6, via Carly |
- **Ch 4 · L128 · in "3 · Grain — the unit of observation, and the unit of time"** — [sentence] The chapter takes the window only as an official definition and goes no further into the sector; that knowledge is Carly's.
- **Ch 4 · L277 · in "6 · The six kinds of nothing"** — [sentence] Whether "not applicable" is a seventh kind or a sub-kind of the fifth is a decision for Carly, and this chapter flags it rather than making it.
- **Ch 4 · L492 · in "12 · Where the choice is yours"** — **Which grain to display.** Venue, operator, room, event, night, person: each is a legitimate unit, each answers a different reader's question, and the chapter's only rule is that the one shown is named and that the row count under it is stated. The choice between them is Carly's and the readers' of Chapter 2.
- **Ch 4 · L516 · in "13 · What this means for a nightlife dashboard"** — An illustration, not a specification. The sector knowledge is Carly's; the method is the chapter's. Chapter 1's definition set the case: a public display of the people, activity, value and support systems that sustain a place's nightlife, for named readers who are not in general.
- **Ch 4 · L549 · in "The rules"** — | Distinguish *not applicable* (the value cannot exist) from *not asked* (it could, and nobody did) | Every official scheme makes the split; the studio's six do not | Standard + Reading | Adaptable (how to name it) — flagged for Carly | SDMX M/L; [z]/[x]; Codd I/A-mark; Understanding Society −8 |
- **Ch 4 · L624 · in "Open questions and flags"** — - `[Further research]` **A seventh kind of nothing.** Every official scheme splits "not collected" into *not applicable* and *not asked*; SDMX also has *included elsewhere* (K/W) and the ABS had *not yet available*. Whether the studio's vocabulary grows is for Carly; the chapter's table is the evidence. `[Validate with users]`
- **Ch 4 · L666 · in "Looking back"** — [sentence] All logged for Carly as candidate additions.
- **Ch 4 · L842 · in "Gaps found while writing this chapter"** — | The Decision Book's gap rule ("dashed, hatched, or broken") can be read as permitting a dashed join across a missing point, which the standard it cites rejects | Quoted the Analysis Function rule in full and made the book's rule "never join, dotted or dashed" | Red — a dashed join is a false claim about the gap | Decision Book Ch 6 (DAT-14), via Carly |
- **Ch 4 · L845 · in "Gaps found while writing this chapter"** — | The studio's six kinds of nothing merge *not applicable* with *not asked*, which every official scheme separates; and have no place for "included elsewhere" or "not yet available" | Built the mapping table; flagged the seventh-kind decision for Carly rather than making it | Amber — an empty cell with two meanings under one label | The data contract; Chapter 0's glossary; the design system's empty states |
- **Ch 5 · L281 · in "10 · How culture and place are measured now"** — One composite index exists in the studio's sector, and version 1 of this book named it. This chapter reads its public methodology only for what it discloses, reports nothing about any city, and applies to it exactly the test it has applied to the five instruments above. Whether a named method audit of a sector instrument belongs here or in Chapter 15, *Learning from the best*, is for Carly.
- **Ch 5 · L289 · in "11 · The form question"** — Whether to build a composite at all is a choice the literature has argued for the better part of two decades, and the studio's own framework keeps open — version 1 recorded that the result "may be an index, a diagnostic, a framework, a value ledger, a modular evidence toolkit or a hybrid — or a decision that a scored index is not useful". This section gives the forms and the arguments; the choice is Carly's.
- **Ch 5 · L386 · in "14 · Where the choice is yours"** — **Whether the sector composite's method audit sits here or in Chapter 15.** For Carly.
- **Ch 5 · L392 · in "15 · What this means for a nightlife dashboard"** — An illustration, not a specification, and not a decision about the measure's form. The sector knowledge is Carly's; the method is the chapter's.
- **Ch 5 · L501 · in "Open questions and flags"** — - `[Revisit at end]` **The form question.** Once Chapters 6–16 exist, the closing chapter should set the five forms against every reader and every rule and say which the book's own evidence favours — without making the decision, which is Carly's.
- **Ch 5 · L647 · in "Gaps found while writing this chapter"** — | No house position on whether the measure is one-tailed (shortfall) or two-tailed (thriving) | Raised it from the deprivation index's design; left it open | Amber — the arithmetic differs | Carly; Chapter 6 |
- **Ch 7 · L413 · in "13 · Where the choice is yours"** — **Whether to show a projection at all.** A dashboard of evidence may decide that the future is the reader's to imagine from the past the dashboard shows, and that any line drawn forward is a claim it would rather not make. That is a legitimate answer to section 9, and it is Carly's.
- **Ch 9 · L14 · in "Before you start"** — [sentence] The *brief* is Carly's written commission for this book; the *house framework* is the studio's own Vibe Setting Framework, unpublished and confidential, which this book cites and never reproduces; the *data contract* is the prototype repository's own rules for its data.
- **Ch 10 · L16 · in "Before you start"** — [sentence] The *brief* is Carly's written commission for this book; the *house framework* is the studio's own Vibe Setting Framework, unpublished and confidential, which this book cites and never reproduces.
- **Ch 10 · L582 · in "18 · The studio's own positions, tested"** — [sentence] *Who is in the room.* The studio's history with a policing form that asked promoters to describe who would attend an event is Carly's knowledge, enters this chapter as frame, and is not researched here.
- **Ch 11 · L14 · in "Before you start"** — [sentence] The *brief* is Carly's written commission for this book.
- **Ch 11 · L417 · in "12 · Where the choice is yours"** — *How long the sentence is.* The house rule is five words where possible and ten at most; the official limits are fifteen words and sixty characters. Which the Vibe Map uses, and whether a generated sentence is held to the poster rule, is Carly's.
- **Ch 15 · L468 · in "13 · Where the choice is yours"** — **The fold.** Whether Chapter 15 stands or folds into 2 and 5 is Carly's, as the brief says; section 11 gives the count.
- **Ch 15 · L676 · in "Gaps found while writing this chapter"** — | The Audience Agency's data arrangements | §6 | "No custodian named" as of 6 October 2026 | Research, by Carly's timeline |
- **Ch 15 · L681 · in "Gaps found while writing this chapter"** — | The fold question | §11 | A count given; the decision is Carly's | Carly |

---

## PART 5 — THE GAPS, ASSEMBLED

Every row of every `## Gaps found while writing this chapter` table: **207 rows** in 16 tables (Chapter 0 has one of its own, 4 rows). Rows per chapter: Ch 0: 4, Ch 1: 6, Ch 2: 9, Ch 3: 10, Ch 4: 18, Ch 5: 13, Ch 6: 16, Ch 7: 15, Ch 8: 19, Ch 9: 16, Ch 10: 19, Ch 11: 18, Ch 12: 9, Ch 13: 9, Ch 14: 13, Ch 15: 13.

**The tables are not all the same table.** Chapters 0–13 use the four columns `What the system missed | What I did instead | Cost | Where it belongs`. Chapters 14 and 15 use four different columns, `Gap | Where it bites | Interim position | Who closes it`, with no Cost column. They are reproduced separately below, as printed, with **Ch**, **#** (row number, ID `G-Ch.#`), **L** (file line) and a last column **Group [added]** (my classification; see 5.3).

The line printed under the heading (verbatim): Ch 1 and Ch 2 — "*The four-field log the Decision Book uses: what was missed, what was done instead, the cost of getting it wrong (red, amber, yellow), where a rule would belong.*"; Chs 3–11 — "*The four-field log the Decision Book uses: what was missed, what was done instead, the cost of getting it wrong (red — would mislead a reader; amber — would weaken the work; yellow — a tidy-up), where a rule would belong.*" (identical in each of Chapters 3 to 11); Chapters 0, 12, 13, 14, 15 — no line; the table follows the heading.

### 5.1 Chapters 0–13 — `What the system missed | What I did instead | Cost | Where it belongs`

| Ch | # | L | What the system missed | What I did instead | Cost | Where it belongs | Group [added] |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 194 | The design system has no component for a *kind-of-claim* mark (Standard / Evidence / Reading / Practice / Nightlife Culture) | In the markdown the kind is a word in a table column. For the HTML reader, the nearest existing component is the status chip; it will be shown as an option, marked provisional, not invented | Yellow | Design system `docs/gaps.md`, via the dashboard section | d |
| 0 | 2 | 195 | The design system's interim rule says "never RAG tags" for public severity marks; the book's gap register uses red / amber / yellow | Kept RAG inside the gap register, which is an internal working record; anything that travels in the reader uses words, not coloured severity | Yellow | Chapter 16; design system open decision 12 | d |
| 0 | 3 | 196 | The original four kinds had no home for practitioner frameworks, on which Chapters 1 and 2 both leaned | Added *Practice* as a fifth kind, defined above; Chapters 1 and 2 already use it | Yellow — closed | — | e |
| 0 | 4 | 197 | "Fixed" was being used for three things (a rule to obey; a fact the book is confident of; a sequence that is the hard line) and a cold reader of Chapter 2 could not tell which | Named the two refinements above — Fixed as a statement of the record; Fixed as sequence — so that chapters can say which they mean | Amber | Chapter 16's rule register should check every Fixed for which sense it carries | e |
| 1 | 1 | 467 | No independent measurement exists of how many dashboards go unused | Refused to print a percentage; stated the gap as a rule | Yellow | Chapter 16's rule register | a |
| 1 | 2 | 468 | No study found on staleness — what happens when a dashboard stops changing | Inferred from monitoring theory and the non-use literature; flagged | Amber | Chapter 8 | a |
| 1 | 3 | 469 | The Decision Book's data chapters do not say "the unit of aggregation is a decision" | Stated it here from Openshaw; the Decision Book may want the rule | Amber — it transfers to every place-based chart | Decision Book gap register, via Carly | d |
| 1 | 4 | 470 | The design system's evidence rules cover charts, not the conduct of release (fixed time, simultaneous release, open data route) | Treated the Code of Practice as an adopted standard | Yellow | Design system dashboard section, eventually | d |
| 1 | 5 | 471 | Chapter 0's four kinds of claim have no clean home for practitioner sources (Few, Eckerson, Behn) | Labelled them Reading and said "practitioner" in the text | Yellow | Chapter 0 — consider a fifth kind, *Practice* | e |
| 1 | 6 | 472 | Fixed rules resting on abstract-only reading were not visibly marked in the first draft | Added the † convention and a verification flag | Amber — a sceptical reader caught it | Chapter 0's legend; the ledger conventions | e |
| 2 | 1 | 681 | Chapter 0's legend has no kind for practitioner frameworks, and this chapter rests on a dozen of them | Used a fifth kind, *Practice*, in the rules table and sources before Chapter 0 carries it | Amber — a reader using Chapter 0's legend will not find the word | Chapter 0, next revision | e |
| 2 | 2 | 682 | The brief's three user groups are, on the evidence, at least seven graders with contradictory rules | Built the reader table in section 1 as a Reading and said so | Amber — the prototype's user testing is organised in three groups | The brief and the test protocols, via Carly `[Validate with users]` | d (also c (routed "via Carly")) |
| 2 | 3 | 683 | The Decision Book's evidence rules say how to show a number fairly, not whether the display is monitoring or evaluation | Took the Magenta Book's distinction as a Standard and made it a Fixed rule | Red — an implied counterfactual is the error the official reader is trained to catch | Decision Book gap register, via Carly; design system evidence rules | d |
| 2 | 4 | 684 | No source distinguishes "numbers for understanding" from "numbers for advocacy" in the terms the studio needs | Stated it as a Nightlife Culture position in section 8, consistent with the Code of Practice adopted in Chapter 1 | Amber | Chapter 10; the studio's own rules | a* |
| 2 | 5 | 685 | Two reads of Oliver et al.'s Table 1 returned different counts in draft 1 | The verification pass read the table twice and settled it; draft 2 prints the counts | Yellow — closed | — | e |
| 2 | 6 | 686 | The chapter's first rule asserted that one display can be legible to all readers, while its own sources say the first screen is always in somebody's grammar | Rewrote the rule to require that the choice of grammar be made and declared; flagged the feasibility question for the end of the book | Red — a Fixed rule resting on an unproven premise | Chapter 16's rule register; Part 3 | e |
| 2 | 7 | 687 | No reader was interviewed for a chapter about readers; two rows of the table have no study behind them | Said so in section 1; made the table the first thing to validate | Amber | The test protocols, via Carly | e (also a1) |
| 2 | 8 | 688 | Hastings & Weinstein is routinely cited (including by this chapter's own research agent) as evidence that re-sorting into a ranking changes decisions; the authors say the format added little | Quoted the authors' own conclusion and moved the finding from "rankings" to "timing" | Amber — the misreading flatters design | Chapter 11 (the first screen) should not inherit the misreading | e |
| 2 | 9 | 689 | The brief's recognition test ("do not recognise their place") has no stated method | Named it as member checking and specified the condition (dialogue that can change the account) as a Fixed sequence | Amber | Chapter 12; the test protocols | d |
| 3 | 1 | 697 | The Decision Book's chart chapter rests 3D and pie rules on the conjectural half of the perceptual hierarchy | Kept the rules, replaced the reasons, and logged the conflict | Amber — a reader who learns the real evidence will distrust the rule | Decision Book Ch 6, via Carly | d |
| 3 | 2 | 698 | "Label at the mark" is Fixed in the Decision Book and the design system with no direct experiment behind it | Stated its evidential status (Practice backed by analogous Evidence) and kept it Fixed on the accessibility logic | Yellow | Chapter 0's legend — a sub-kind; Decision Book Ch 6 source column | d (also a1) |
| 3 | 3 | 699 | The Decision Book says a line chart's axis "may be broken where necessary, and labelled", as if the label settled it; the Analysis Function checklist already warns that a signposted break still shows bar sizes "very strongly", and the experiments extend that to lines | Made the rule from Correll, Yang and the checklist: a broken line axis is a chosen effect size | Amber — "label it and move on" is too comfortable | Decision Book Ch 6 | d |
| 3 | 4 | 700 | The design system and the Decision Book have no rule on the title's power to decide the reading, or on how much text a chart carries | Made both rules from Kong and Stokes | Red — the title is the most-remembered and least-trusted component and nobody owns it | Design system evidence rules; Decision Book Ch 6 | d |
| 3 | 5 | 701 | No rule in either on stock against flow or linear against log for public displays | Made the public-defaults rule | Amber | Decision Book Ch 6 | d |
| 3 | 6 | 702 | The field's most-quoted interaction statistic is an anecdote about one button | Replaced it with Conlen et al.'s measured rates and kept Aisch's own correction | Yellow | Chapter 11 | a |
| 3 | 7 | 703 | No study of the big-number tile; no study of legends against labels; no UK measurement of chart literacy | Said so; flagged all three for the prototype | Amber — three of the commonest design decisions have no evidence | `03-tests/` probe candidates | a |
| 3 | 8 | 704 | Chapter 0's legend has no way to mark "a research agent's correction was itself wrong" | Logged the Jachimowicz episode in Looking back and in the research log | Yellow | The ledger's "how read" vocabulary | e |
| 3 | 9 | 705 | The chapter's first draft quoted a sentence from the Office for Statistics Regulation that the source does not contain, and built a headline on it | Replaced with the regulator's actual words and softened the claim; logged as the sprint's most serious catch | Red — caught by verification before delivery | Method note: quotations that flatter the argument are checked first | e |
| 3 | 10 | 706 | The cold reader found the Fixed tier applied to small and adjacent-domain studies while the chapter demanded that standard of others | Marked adjacent-domain and small-sample evidence in the rules table; re-tiered two rules Adaptable; split the truths into seven rules and a record | Amber | Chapter 0 — the legend may want "Evidence (adjacent domain)" as a recognised marking | e |
| 4 | 1 | 842 | The Decision Book's gap rule ("dashed, hatched, or broken") can be read as permitting a dashed join across a missing point, which the standard it cites rejects | Quoted the Analysis Function rule in full and made the book's rule "never join, dotted or dashed" | Red — a dashed join is a false claim about the gap | Decision Book Ch 6 (DAT-14), via Carly | d |
| 4 | 2 | 843 | The Decision Book's provenance set omits the responsible party and the issued/modified dates | Added both from the Code, PROV and DCAT; kept the book's "illustrative flag" | Amber | Decision Book Ch 8 (DTA-19) | d |
| 4 | 3 | 844 | Chapter 1 cited the Code of Practice's Q1–Q3; the Code is now edition 3.0 and those principles are Standards 6 and 7 | Mapped the old numbering to the new; flagged Chapter 1 | Yellow | Chapter 1; the ledger | e |
| 4 | 4 | 845 | The studio's six kinds of nothing merge *not applicable* with *not asked*, which every official scheme separates; and have no place for "included elsewhere" or "not yet available" | Built the mapping table; flagged the seventh-kind decision for Carly rather than making it | Amber — an empty cell with two meanings under one label | The data contract; Chapter 0's glossary; the design system's empty states | c (also d) |
| 4 | 5 | 846 | Version 1's gap vocabulary mixed kinds of nothing with reasons for a series break, and named a kind ("community-held") that no official vocabulary has | Separated them; carried "community-held" forward as a Nightlife Culture kind for Chapter 10 | Amber | Chapter 10 | e |
| 4 | 6 | 847 | Neither the Decision Book nor the design system has a rule on the unit of observation or the row count | Made the rule from Wickham, Eurostat and the regulation | Red — a count without its unit is undefined | Decision Book Ch 8 | d |
| 4 | 7 | 848 | No rule in either on the denominator, the reference class, or the funnel for small bases | Made them from the CDC primer, Hájek and Gelman & Price | Red for the funnel (raw ranks of small places mislead by arithmetic) | Decision Book Ch 6/8; Chapter 7 | d |
| 4 | 8 | 849 | No rule in either on reading a platform feed (coverage, selection, the ten characteristics) | Made the rules from Meng and Salganik | Red — the ticketing feed is the prototype's main source | The data contract; Chapter 8 | d |
| 4 | 9 | 850 | No rule in either on outliers beyond "show the gaps" | Made the procedure from Leys, Simmons, Bakker & Wicherts, Osborne & Overbay | Amber | Decision Book Ch 6; Chapter 6 | d |
| 4 | 10 | 851 | No rule in either on concentration measures beside totals | Made the rule from Lorenz, NIST and the ONS | Amber — the 78%/32% currently stands without its curve | Decision Book Ch 6; the prototype | d |
| 4 | 11 | 852 | "Reliable" is used in the failure register and the design system in the ordinary sense; official usage means revisions | Stated both senses; rule to use one | Yellow | Chapter 0's glossary; Chapter 8 | d |
| 4 | 12 | 853 | Hawkins, Barnett & Lewis, Grubbs, Tukey, Huber, Anderson: the canonical outlier and long-tail texts were all unreachable at source | Quoted via named reproductions and marked them; dropped Huber and Anderson | Yellow — the definitions are stable across reproductions | The ledger's "secondary" marking | b |
| 4 | 13 | 854 | Chapter 0's legend has no marking for a quotation reached through a named reproduction | Used "secondary" throughout and proposed it for the legend | Yellow | Chapter 0 | e |
| 4 | 14 | 855 | The data contract named in the brief was not available to this sprint | Said so; flagged | Amber — the chapter's mapping may not match the prototype's vocabulary | The next session with the prototype repository staged | b (also d (the data contract)) |
| 4 | 15 | 856 | The first draft applied the chapter's first truth to everyone's numbers but the studio's, and closed the worked case with "None of this weakens the finding" | Rewrote the close: the finding is undefined until its unit, period and base are supplied; flagged the prototype to supply them | Red — the cold reader's strongest objection, and a symmetry failure | Method note: run the symmetry test on the studio's own findings first | e |
| 4 | 16 | 857 | Three paraphrases stood inside quotation marks (OSR on users; DCAT on absent values; Salganik's grouping labels), two numbers were wrong (eight units; the Wang & Strong survey stages) and six quotations were silently truncated | Corrected from the verifier's report; ellipses or closing marks added | Amber — none changed a conclusion; all would have weakened trust in the apparatus | Method note: a standards-heavy chapter needs the verifier as much as an experiments-heavy one | e |
| 4 | 17 | 858 | The Fixed tier was used with four qualifiers ("as a stance", "as a procedure", "adopted", "as disclosure") that Chapter 0 does not define | Defined the first two in Looking back for Chapter 0; re-tiered the ten-characteristics audit Adaptable | Yellow | Chapter 0's legend | e |
| 4 | 18 | 859 | No evidence was found that provenance on the face changes a reader's decision — the chapter's thesis rests beside a gap | Said so in section 5; marked the provenance rules Standard (adopted), not Evidence; flagged a probe | Amber | `03-tests/`; Chapter 11 | a |
| 5 | 1 | 643 | The Decision Book has no rules on composites, weights, aggregation, sensitivity or what accompanies a score | Built the rules table from the handbook, the audits and the standards; logged as a candidate chapter | Red — the prototype's measure, if it is a composite, would be built with no house rule | Decision Book, a new data chapter | d |
| 5 | 2 | 644 | Version 1 cited the 20%/21% and 40%/81% figures without naming the index; a reader could take them as the HDI's | Traced them to Paruolo et al.'s Table 2 (the Times Higher Education ranking) and said the HDI is the well-behaved case | Amber | Version 1 archive note; this chapter | e |
| 5 | 3 | 645 | The studio's "validation by recognition" was a single rule; the measurement literature splits it into legitimacy (who chooses what counts) and validity (five sources), and does not count recognition as the latter | Kept the studio's authority claim and separated it from the validity claim; marked recognition as face validity and credibility | Amber — a measure the scene recognises could still be measuring the platform | Chapter 9; the data contract; Chapter 0's glossary | d (also e (a version 1 rule)) |
| 5 | 4 | 646 | The design system's evidence components (source line; comparability gate; provenance code) cover a chart's number, not a composed one | Proposed the card as the evidence component for a composite | Amber | Design system, evidence components | d |
| 5 | 5 | 647 | No house position on whether the measure is one-tailed (shortfall) or two-tailed (thriving) | Raised it from the deprivation index's design; left it open | Amber — the arithmetic differs | Carly; Chapter 6 | c |
| 5 | 6 | 648 | "Reliability" now has three senses in the book (revisions; replications; inter-rater) and the glossary has one | Stated all three; flagged Chapter 0 | Yellow | Chapter 0 glossary | e |
| 5 | 7 | 649 | Goodhart, Hoskin, Lincoln & Guba, Borsboom, Campbell & Fiske, Thomas — canonical texts unreachable at source | Quoted via named reproductions that agree with each other; marked secondary | Yellow | The ledger's "secondary" marking | b |
| 5 | 8 | 650 | A research agent's fetch tool fabricated quotations from a paper it had opened (Alkire 2008); the agent caught it by string search | Used no quotation from that paper; recorded the episode as a method finding | Red — caught before writing; would have been a fabricated citation | Method note: ask agents to string-verify body-text quotations whose wording matters | e |
| 5 | 9 | 651 | The one sector composite is named in a method audit; the brief says the sector is not researched | Read only its published methodology; reported nothing about any place; flagged the placement for Carly | Amber — a line the book must hold carefully | Carly's call: here or Chapter 15 | c |
| 5 | 10 | 652 | Draft 1's arithmetic test on that composite was unfair by the chapter's own rules: it declared that "no standard mean" recovered the headline when a weighted mean, a power mean or indicator-level equal weights would, misstated the harmonic mean, and applied the "recipe not on the face" verdict to one instrument while three others in the table also publish no sensitivity analysis | Rewrote the test fairly; stated the finding as disclosure, not arithmetic; applied the sensitivity verdict to all four | Red — the cold reader's strongest objection; a symmetry failure against the instrument the chapter was most tempted to judge | Method note: run the chapter's own rules against its own audits before dispatch | e |
| 5 | 11 | 653 | Five verification mismatches: harmonic mean; SPI indicator count; a Messick sentence not in the report read and a truncated one; the PASC 80% figure narrowed; a Holden sentence that is Holden quoting the Cabinet Office; plus web-guide sentences attributed to the 2008 handbook | All corrected | Amber | Method note: the handbook and its web guide are two texts | e |
| 5 | 12 | 654 | No evidence found that decision-makers prefer composites to dashboards; the belief underwrites most index projects | Marked it Practice; flagged | Amber | `03-tests/`; Chapter 15 | a |
| 5 | 13 | 655 | The handbook's own visualisation step says nothing about showing uncertainty, while its sensitivity step requires rank intervals | Made the rule from the sensitivity step and the JRC audit's reading instruction | Yellow | Chapter 11 | a* |
| 6 | 1 | 761 | No web search for the whole sprint; the scholarly web (Project Euclid, JSTOR, PNAS, PMC, Science, T&F, Wiley, ScienceDirect, IMF) closed to a fetch tool; seventeen canonical texts unreached | Named each, quoted none, used open substitutes (COS for Tukey; Walker et al. for Holling; Efron & Morris 1975 for 1977; Wainer's 2009 chapter for the 2007 article; the Eurostat guideline for Rao & Molina) and said so in the chapter | Amber — the argument stands on what was reached, but the canon is cited by name only | Library pass before the chapter is final; the ledger | b |
| 6 | 2 | 762 | Two UK method texts were replaced in 2026 at their old addresses (Magenta Book May 2026; Green Book February 2026); earlier chapters cite "Green Book 2022" from the live link | Quoted the 2026 editions and said so; flagged Chapter 2 and the ledger | Red — a book quoting "2022" from the live link would be quoting the wrong document | Chapter 2 re-point; ledger note on editions | e |
| 6 | 3 | 763 | The Decision Book has no rules on gross against net, distributional weights, causal rungs, leading indicators, multiple comparisons, alert policy, shrinkage, or the precision reason for withholding | Built the rules table; logged as a candidate chapter on claims about value | Red — the prototype would make causal, value and alert claims with no house rule | Decision Book, a new chapter | d |
| 6 | 4 | 764 | Version 1's claim ladder put a rung-one fact at the top labelled as a counterfactual, euphemised the lower rungs as "associational", and had no deadweight line; its two-track display asserted a lead | Tested it by the chapter's own standards (the symmetry test); amended, kept | Amber — the studio's strongest claim would have been displayed as something its evidence could not support | Version 1 archive note; this chapter §8; the prototype | e |
| 6 | 5 | 765 | The studio's ledger ("value created and value retained") used "created" for a gross figure | Relabelled by the Additionality Guide's arithmetic | Amber | This chapter §7; the prototype | d |
| 6 | 6 | 766 | Official suppression rules hide small numbers for two reasons (confidentiality; precision) and one official table colours both the same | Separated them; rule that the mark says which | Amber — a reader who mistakes noise for secrecy, or secrecy for noise | Decision Book Ch 8/15 addendum; the design system's empty states | d (also a2) |
| 6 | 7 | 767 | The national rules' identifying thresholds (2, 3, 5, 7) assume an intruder without local knowledge; a scene's regulars can name three venues | Rule that the scene's knowability sets the threshold; flagged for users | Red — a confidentiality breach by a national rule correctly applied | Chapter 10; the data contract; `[Validate with users]` | a* (also d (the data contract)) |
| 6 | 8 | 768 | No method found for commercial displacement (venues, promoters); the household literature is all there is | Said so; flagged | Amber — the form of displacement that matters most to a scene is unmeasured | `[Further research]`; Chapter 15 | a* |
| 6 | 9 | 769 | The AQuA Book 2025 has no statement about validating a model against outturn; its validation is user-needs-based | Reported the negative finding; built the two-test standard (out-of-sample plus agreement of the competent) from the holdout literature and Glover | Amber — "validated" in UK guidance may mean "the users agreed", which a reader would not expect | Chapter 0 (definition of a canonical truth); `[Revisit at end]` | a* |
| 6 | 10 | 770 | The fetch tool's reader declares a 125-character quote cap and merges sentences to fit it — the mechanism behind Chapter 5's "fabricated" quotations | Every agent string-checked by presence prompt; the chapter marks single-pass sentences; Entry 5's "fabricated" is corrected to "reshaped by the reader's cap" in the log | Yellow — method; already caught | Method note in the log; AGENTS.md | e |
| 6 | 11 | 771 | One agent's rendering of a table cell (Martin & Sunley's ecological-resilience definition) failed its string check after reading fluently | Not used | Yellow | Method note: table cells need the second check too | e |
| 6 | 12 | 772 | The Audience Agency entered liquidation on 10 September 2026; the sector's audience yardstick has no custodian | Reported; flagged Chapter 15 | Amber — any dashboard built on Audience Spectrum needs a fallback | Chapter 15; the prototype's data sources | a* |
| 6 | 13 | 773 | Draft 1 glossed Gelman's county as "the most dangerous place in the state" and "the radon capital of Minnesota"; the paper says only "an implausibly high estimate" | Cut to the source's claim; Minnesota confirmed from the paper | Yellow | Method note: a vivid gloss is a claim | e |
| 6 | 14 | 774 | Draft 1 credited a quotation to Easton et al. that they quote from Baeten et al.; misquoted Arvidson's abstract where the full text was on the record consulted; put an invented SROI ratio in quotation marks; and called the Additionality Guide's definition its "first sentence" | All corrected by the verifier's report | Amber | Method note: a sentence inside a source's own quotation marks needs its own attribution | e |
| 6 | 15 | 775 | Draft 1 licensed "contributed to" from observational data alone, against the Magenta Book's condition that alternatives be ruled out, and said so inconsistently across the truths, rules and checklist; and let the studio's claim ladder pass Hill's fundamental question with its main alternative (the trip was coming anyway) unaddressed | Moved the verb to the second rung throughout; re-tested the claim ladder; marked the deadweight question as stated preference | Red — the cold reader's strongest objection; the chapter would have handed the prototype a causal verb for free | This chapter §8 and §12; the prototype | e |
| 6 | 16 | 776 | No evidence at source for a positive-deviance method at small n | Pointed to shrinkage as the mechanism; flagged | Yellow | `[Further research]`; Chapter 7 | a |
| 7 | 1 | 686 | No web search again; twenty-two canonical or official texts unreached; the comparison literature's founding article (Espeland & Sauder 2007) and the funnel plot's founding paper (Spiegelhalter 2005) read at abstract only | Used the authors' open book chapter and the official technical briefings that implement the funnel; marked everything † or unreached | Amber — the argument stands on official practice and open texts; the canon is cited by name | Library pass before Part 1 closes | b |
| 7 | 2 | 687 | Version 1 paraphrased the C3 Monitor as "one city in five's rank reflects modelling choices rather than data"; the actual wording is rank intervals under ±3 for about 80% under weight and normalisation perturbation only | Gave the exact wording and the limits of the test | Amber — a paraphrase that overstated a source the chapter relies on | Version 1 archive note; Chapter 5's ledger entry | e |
| 7 | 3 | 688 | Version 1 proposed peers chosen by the place; the evidence reached on self-selected comparators (two abstracts, from executive pay, with qualifications) finds the choice tends to flatter the chooser | Failed the proposal under the symmetry test; amended to a published method with chosen peers shown beside and kept as data | Amber — the prototype would have let each place pick its own comparison set; the evidence is a caution by analogy rather than a verdict | This chapter §11; the prototype | e |
| 7 | 4 | 689 | Version 1's "a borough with a scene beats a borough with a superclub" is a ranking sentence | Restated as two denominators, two pictures, neither a rank | Yellow — but the kind of slip the symmetry test exists for | Version 1 archive note | e |
| 7 | 5 | 690 | The Analysis Function's chart standard ("Always rank bars by value") and the statistical guidance ("inappropriate to rank") pull against each other with no reconciliation in either | Reconciled through the funnel: order as a reading aid, position against limits as the finding | Amber — a designer following the chart standard builds a league table | Decision Book Ch 6; the design system's chart rules | a* (also d) |
| 7 | 6 | 691 | The two official traditions disagree on reading turning points (textbook: from the trend-cycle; Eurostat: withhold the end-point) | Showed both; rule that the end-point carries a warning | Amber | Chapter 13; the design system | a* |
| 7 | 7 | 692 | No official rule on percentage change from a small base, on minimum series length (ONS), or on pre-specifying comparator groups in the public sector | Said so; used the nearest official wording | Yellow | `[Further research]` | a* |
| 7 | 8 | 693 | The Decision Book has no rules on rankings, standardisation, peers, seasonal adjustment, regression to the mean, the designs, spillovers, power, the ladders, or projections | Built the rules table; logged as a candidate chapter on comparison | Red — the prototype would compare places and periods with no house rule beyond the comparability gate | Decision Book, a new chapter | d |
| 7 | 9 | 694 | The Magenta Book Annex A was read at a 2020 upload path; its title page reads May 2026 on two fetches | Cited as the May 2026 edition served at the 2020 path | Yellow | Confirmed by the verifier | e |
| 7 | 10 | 695 | Lee & Lemieux dispute the "only at the threshold" limitation that the Magenta Annex states as fact | Showed both | Yellow | — | a* |
| 7 | 11 | 696 | The chapter's filled comparison record uses an illustrative interval (3 of 34) computed by the author | Stated as approximate; the exact binomial interval (about 1.9% to 23.7%); Wilson's gives about 3% to 23%; the conclusion holds either way | Yellow | Confirmed by the verifier | e |
| 7 | 12 | 697 | Four records now sit beneath a dashboard's numbers across Chapters 4–7 | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 | e |
| 7 | 13 | 698 | Draft 1 said the Bank of England's fan chart was "abolished in 2024" and attached the OBR's chart caveat to it; the fan ran until February 2026 and the April 2026 report is the first without one | Corrected; the OBR's fan, still live, is now distinguished | Red — a dated factual claim about the official reader, wrong by two years | Method note: a recommendation is not its implementation | e |
| 7 | 14 | 699 | Draft 1 truncated three quotations before a qualifying clause (APHO on comparing standardised ratios; Bizjak on peer groups; HQIP on case-mix), credited a four-author paper to its two authors plus two commentators, gave the External Panel Review five recommendations where it made eleven and credited it with a sentence it was summarising from earlier reviews, dated the ONS nearest-neighbours output a year late, halved the C3 Monitor's simulation count, inserted a word into a Conference Board sentence, and put an agent's gloss in quotation marks | All corrected from the verifier's report | Amber — none reversed a conclusion; the Bizjak truncation had made the peer-selection evidence look cleaner than it is | Method note: a quotation that ends at a comma needs the clause after it read | e |
| 7 | 15 | 700 | Draft 1 gave "contributed to" to any comparison-group design and no verb to an interrupted series, a cut-off or a synthetic control, and called the band rule's reach unclear between quintiles and the ONS's three words | Attached a verb to each rung; distinguished bands of position from categories of separation; tested the funnel and the three words as public measures | Amber — the cold reader's strongest objection; the rule would have forbidden the chapter's own recommended forms | This chapter §5, §8, §11 | e |
| 8 | 1 | 874 | No web search for any agent; the fetch reader truncates at ~100–120k characters, so RFC 9110's `Retry-After` and conditional-request sections, DWBP's freshness and preservation practices and DCAT 3's frequency definition were all beyond reach | Used the sibling normative text (RFC 9111), the draft and implementation report for DWBP, and the official profiles (DCAT-AP, DCMI, UK and US) for frequency; marked each | Amber — the chapter's vocabulary is intact, but two standards are cited from the parts that could be seen | `[Further research]`; verifier | b |
| 8 | 2 | 875 | On first pass the fetch tool's reader invented standards-sounding sentences for sections it could not see (DWBP BP21/22; DCAT 3 frequency and temporal resolution) | Discarded by the agent on the presence check; nothing of them used | Red if missed — fabricated standard text in a chapter about trusting sources | Method note; Entry 8 | e |
| 8 | 3 | 876 | About a quarter of the brief's "stable" URLs and phrasings had drifted: Looker Studio renamed; Monte Carlo's domain and a pillar; Netlify's tier; the AWS library; Azure's bulkhead wording; the PMTiles tagline; the SRE workbook URL; GitHub's timezone rule; the OSM tile policy; YouTube's quota; "surprisingly powerful" never existed | Quoted the current wording and dated it; used the drift as first-hand evidence in §8 | Amber — a chapter that printed the brief's wording would have been wrong on the day it was written | §8; Entry 8 method note | e |
| 8 | 4 | 877 | Three expected quotations were not in the sources: GDS's "deprecation period" and "do not break backward compatibility"; OSM's "forbidden without prior permission"; YouTube's "100 units per search" | Reported the absence; quoted what is there | Yellow — but each would have been a misquotation | SOURCES; this table | e |
| 8 | 5 | 878 | Eventbrite's developer site, the OS plans page and the ONS geography portal are script-only shells; the search-endpoint removal and the OS free allowances could not be verified | Recorded as unverified; printed no figure from memory; used the failure as evidence in §9 | Amber — a widely repeated Eventbrite fact is left unconfirmed | `[Further research]` | b |
| 8 | 6 | 879 | The National Archives' OGL page returned a redirect loop | String-verified against SPDX's reproduction and said so | Yellow — re-check against the canonical page before print | SOURCES | b |
| 8 | 7 | 880 | One research agent could not find the Analysis Function dashboards guidance at guessed URLs; another found it at the policy-store path | Used the reading that found it; spot-checked; verified | Yellow | — | e |
| 8 | 8 | 881 | No open primary source for the "60–80% of lifecycle cost is maintenance" figure; GAO measures spending, not lifecycle | Asserted only that operating costs more than making, on GAO and practitioner authority | Amber — a figure the sector repeats could not be grounded | `[Further research]` | a* |
| 8 | 9 | 882 | No measured evidence that stale dashboards cost trust; no measured study of UK open-data staleness; no measured bytes-per-view for a map | Said so three times; flagged each for the prototype or users | Amber — three of the chapter's rules rest on standards and doctrine rather than measurement | `[Prototype flag]`; `[Validate with users]` | a |
| 8 | 10 | 883 | No design system reached (GOV.UK, Carbon, PatternFly) says a dashboard should show its last refresh | Grounded the rule in the catalogue standards, the protocol and one product's practice; marked precedent thin | Yellow | Design system gap log | a* (also d) |
| 8 | 11 | 884 | The Decision Book treats empty and error states as Decorative (DSH-21); this chapter makes the degraded state a Fixed procedure | Logged as a conflict, not resolved | Amber — a designer following DSH-21 may blank a tile on failure | Decision Book Ch 15; conflict log | d |
| 8 | 12 | 885 | The Decision Book has no rules on freshness display, dependencies and terms, refresh, watch and alarm, availability objective, budget and device, progressive enhancement, tile supply, or retirement | Built the rules table; logged as a candidate chapter | Red — the prototype would be run with no house rule beyond the boundary vintage | Decision Book, a new chapter ("Running it") | d |
| 8 | 13 | 886 | The design system has no map component, no freshness component, no degraded-tile state, no byte budget | Logged; design decisions not made | Amber | Design system | d |
| 8 | 14 | 887 | Several platform clause numbers (Spotify IV.3.a/b, IX.8.h) wavered between the fetch tool's passes | Quoted the text; advised confirming numbers by eye | Yellow | Before print | e |
| 8 | 15 | 888 | The fetch tool's reader invented publication years for the SRE book and its siblings on first pass (2017, 2020, 2016); none is on the pages | Gave the publishers' years and said the pages do not show them | Yellow | SOURCES | e |
| 8 | 16 | 889 | The chapter's chain arithmetic, Mapbox cost example, 12.6 KB per tile request, 75:1 boundary ratio and 43 per cent renderer share are all its own computations | Marked each as the chapter's; the verifier recomputed them and caught a like-for-unlike division in the boundary ratio, now corrected | Yellow | — | e |
| 8 | 17 | 890 | The verifier found a spliced quotation (two of Willison's sites run together), a quotation attributed to the wrong chapter of the SRE texts, a sentence attributed to the 2025 Almanac that is in the 2024 edition, five quotations closed before a qualifying clause, and the boundary-file ratio dividing unlike records | Each corrected in this draft | Amber — none changed a rule; one (the boundary ratio) changed a figure in the 60-second version | Entry 8 method note | e |
| 8 | 18 | 891 | The cold reader found "heartbeat" and "tile" each used in two senses, "page" (pager) unglossed, alert/ticket/alarm used loosely, and the observatory described in section 11 as version 1's model when it was its founding failure | Defined the terms in Before you start; used "stamp" for the date on the face, "panel" for a dashboard's parts, "ticket" throughout; rewrote the observatory paragraph | Amber — the observatory slip inverted a house position | Entry 8 method note | e |
| 8 | 19 | 892 | Five records now sit beneath a dashboard's numbers across Chapters 4–8 | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 | e |
| 9 | 1 | 837 | No web search for any agent, and the least open literature so far: the founding texts of the made and excess registers (Böhme; Anderson), the place-attachment review (Lewicka), the standard's own texts (ISO 12913) and the strongest sentiment test (Jaidka 2020) were all closed | Used what reachable sources quote of them, marked secondary; abstracts marked †; one abstract reconstructed from an index; nothing printed from memory | Amber — the chapter's structure stands on open and verified texts, but its two theoretical registers are cited at one remove | `[Further research]`; a library pass | b |
| 9 | 2 | 838 | The fetch tool's reader invented a word in one source (Fung's "effective governance" for "effective administration"), paraphrased two abstracts as if verbatim, and returned the wrong document for two guessed URLs | Caught by the agents' re-fetch and control strings; nothing of them used | Red if missed | Method note; Entry 9 | e |
| 9 | 3 | 839 | The brief's expected quotations drifted again: "singular affective qualities that emanate from but exceed the assembling of bodies" (Anderson) could not be verified; "safety paradox" is not in Reed et al.; Livehoods is "of a City" not "of Neighborhoods"; Park et al. never say "valence"; Nielsen's rule is 2006 not 1996; DeVellis has nine steps not eight; Nevo defends face validity's measurability rather than dismissing it; ISO/TS 12913-3:2019 is withdrawn | Corrected each; recorded the drift | Amber — several would have been misquotations in a chapter about validity | SOURCES; this table | e |
| 9 | 4 | 840 | Version 1's three-register split was asserted from a raw sweep; its sources (Böhme, Anderson, ISO) were not all reachable to re-test | Re-tested against what could be reached; the split held on every reachable source; marked where it rests on secondary quotation | Yellow | §1, §4 | e (also b) |
| 9 | 5 | 841 | Version 1 proposed the human dot plot as a collection instrument with no measurement source | Tested against the living-histogram artefact, the single-item evidence and the social-influence experiments; kept as a form, weakened as a measure | Red — the prototype would have collected a visible, single-item, self-selected self-placement and called it a measure | §5, §14; the prototype | e |
| 9 | 6 | 842 | Version 1 illustrated discordance with a finding about a place | Kept the method shape; removed the finding | Yellow — but the kind of slip the brief forbids | Version 1 archive note | e |
| 9 | 7 | 843 | "Co-production" was used in version 1 and the brief for any contribution by the scene | Adopted the Boyle & Harris boundary; "participatory" for contribution, "co-produced" for shared use | Amber — a dashboard would have claimed co-production for consultation | §6; glossary | e (also d (the brief)) |
| 9 | 8 | 844 | No empirical study of dot-voting bias; no ticketing-records network study with validation; no measured "you said, we did" effect; no study comparing crowdsourced place scores with residents' own ratings | Said so; used the nearest evidence; flagged for the prototype | Amber | `[Further research]`; `[Prototype flag]` | a |
| 9 | 9 | 845 | The Scenescapes limitation sentence is Silver & Clark's own, quoted by a reviewer; the Oldenburg characteristics are a secondary source's wording; the Lincoln & Guba phrase is a methods guide's report | Attributed each as it stands; advised checking the primary before quoting as the author's | Yellow | SOURCES | e |
| 9 | 10 | 846 | ONS4's cognitive testing is sometimes attributed to Dolan, Layard & Metcalfe; their paper does not use the words | Attributed the testing to ONS and the three-account structure to Dolan et al. | Yellow | §11 | e |
| 9 | 11 | 847 | The Mitchell et al. 2013 correlations are rendered as images on the published page | Took them from the preprint and said so | Yellow — check against the published PDF | Verifier | b |
| 9 | 12 | 848 | The Decision Book has no rules on felt measures at all | Built the rules table; logged a candidate chapter | Red — the prototype would build a felt layer with no house rule beyond provenance | Decision Book, a new chapter (*Felt data*) | d |
| 9 | 13 | 849 | The design system has no component for a distribution of felt responses, a sample on the face, a discordance matrix, "what this changed", or testimony in the respondent's register | Logged; not designed | Amber | Design system | d |
| 9 | 14 | 850 | The verifier found a reversed referent (Park et al.'s "these measures" are earlier methods, not the study's), a reviewer's praise quoted as a publisher's description, two ONS review sentences that belong to the office's user guide, a performance-score sentence and the pole-pairs that belong to Silver & Clark 2014 rather than 2010, "six settings" for six datasets from five, a diary measure called single-item, and the MSC "not-for" list overstated (the guide says other methods are less time-consuming) | Each corrected in this draft | Amber — none changed a rule; the MSC one changed a rule's wording | Entry 9 method note | e |
| 9 | 15 | 851 | The cold reader found "register", "measure", "instrument", "indicator", "co-produced", "recognition", "record" and "face" each used in more than one sense, the family of section 5 named by a word the chapter reserves for something stricter, and the floor of fifty unexamined against the brief's own "aggregation of the biggest" | Defined the words in Before you start; renamed the family; added the floor question to section 14 and the flags | Amber — the floor question is a real tension and is logged, not resolved | Entry 9; `[Revisit at end]` | e |
| 9 | 16 | 852 | Six records now sit beneath a dashboard's numbers | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 | e |
| 10 | 1 | 1046 | The brief's statutory map was out of date in four places on the day of reading (Article 89 and s.19 omitted; Article 14(5)(b) omitted; definitions moved to Article 4(2)–(7); the regulator renamed) | Cited the current text with in-force dates; said where the map had moved; made dating and re-reading a rule | Red — a chapter citing Article 89 would have cited a repealed provision | §8–§9; the rules; Chapter 0's legend for "Standard (law)" | e |
| 10 | 2 | 1047 | The regulator's guidance had caught up unevenly; most pages read carry "under review" | Dated every page; said which were updated and which were not; quoted the statute where the two differ | Amber | §9; SOURCES | a* |
| 10 | 3 | 1048 | No web search; several load-bearing bodies closed (Science; tandfonline; Springer; Bloomsbury; the EHRC code; PAS; Datatilsynet) | Marked †, secondary or unreached; quoted nothing from the unreached; used the complainant's account of the Norwegian decision and said so | Amber | `[Further research]` | b |
| 10 | 4 | 1049 | The fetch tool's reader invented a regulator's definition (FDA), a six-part list (ODI) and page numbers (Nissenbaum); misdated Grimmelmann; compressed statutory sub-paragraphs into paraphrase on first pass | Caught by second fetch and controls; nothing invented used; sub-paragraphs marked (read once) where not re-checked | Red if missed | Method note; Entry 10 | e |
| 10 | 5 | 1050 | The brief's expected quotations drifted: "release and forget" is not the regulator's phrase (it says "release model"); "reasonable degree of certainty" is not on the special-category page (the test is intention); GitHub's "consider … compromised" sentence is gone; the Grindr fine is Norwegian, not the ICO's; the 1 billion Strava activities is 700 million; the Census Bureau's 46/71/38/17% are not in Hawes; "forced visibility" has no source; Charlton's slogan origin is not on the publisher page; "no surprises" is not on the NSDEC page; the accessibility regulations' scope is reg 4, not reg 3 | Corrected each; recorded the drift | Amber — several would have been misquotations in a chapter about care with data | SOURCES; this table | e |
| 10 | 6 | 1051 | The ICO's two inference passages pull in different directions (a correct guess from anonymous data is not disclosure; an intended inference is Article 9 processing however uncertain) | Reported both; stated the separating variables as the regulator's own wording implies them (intention; attachment to an identifiable person); routed the onlooker case to the harm assessment | Amber — the house's "who is in the room" vocabulary sits on the line | §8; §18 | a* |
| 10 | 7 | 1052 | ONS's most direct guidance on interactive tools sits in a births-and-deaths policy, not in census or table-builder documentation; the census builder states no registration, logging or query limit | Reported both models; left the choice between them open; made "treated as a table builder" the rule for any reader-defined control | Amber | §7; §20 | a* |
| 10 | 8 | 1053 | No published protocol for intruder-testing an interactive view; the 2011 and 2021 census intruder-test results unreached | Adapted the microdata guidance; flagged for the prototype | Amber | `[Further research]`; `[Prototype flag]` | a* (also b) |
| 10 | 9 | 1054 | Neither the regulator's DPIA list nor its 2022 taxonomy names harm to a place; the statistical system's guidance does | Built the three-column harm assessment from the UKSA guidance; recorded the gap | Red — a DPIA done to the regulator's list alone would miss the harm a map does | §15; the record's line 11 | a* |
| 10 | 10 | 1055 | The leading redlining paper's effect sizes are in the working paper, not the published abstract; the counter-paper's 4–20% is a different quantity | Quoted each from where it is; said they are not comparable | Yellow — but the two are easily mis-set | §15 | e |
| 10 | 11 | 1056 | "Consent at scene level" (version 1; Chapter 9) has no form in law or in the ethics literature | Retired the phrase; replaced with consult, govern, agree, each with a record | Amber — the prototype would have claimed a consent nobody can give | §11; §18; Chapter 9's flag | e (also a2) |
| 10 | 12 | 1057 | OCAP's owner's caution is narrower than the chapter planned ("specifically First Nations—not Indigenous") and CARE is more permissive ("distinctive communities") | Quoted both exactly; made "questions and structure, never authority" the rule | Yellow | §12 | e |
| 10 | 13 | 1058 | The ONS Census 2021 geography floor for sexual orientation was not established on any page reached | Did not state one | Yellow | `[Further research]` | b |
| 10 | 14 | 1059 | Version 1's "threshold three" and "with the reason" were static-table rules applied to an interactive tool | Floor per view, higher for online tools; kind shown, rule optional | Amber | §18; Decision Book Ch 8/15 | e (also d) |
| 10 | 15 | 1060 | The Decision Book has no rules on query-time protection, the walk, the held status, lawful basis, the DPIA's consultation step, the Online Safety Act, withdrawal tiers or harm to places | Built the rules table; logged a candidate chapter | Red — the prototype would build an interactive public tool with a static table's protections and no record of basis, voice or harm | Decision Book, a new chapter (*Safeguards*) | d |
| 10 | 16 | 1061 | The design system has no component for a held layer, the three nothings, a record beside a panel, a withdrawal notice at contribution, or a stigma test for colour | Logged; not designed | Amber | Design system | d |
| 10 | 17 | 1062 | The verifier found a 48-hour take-down limit inserted into the Online Safety Act on 29 June 2026 that the first draft missed; "weakens" in quotation marks where the book says "deteriorates"; a 2012 crime-map review misdated to 2011 and miscalled the maps' own evaluation; the WCAG standard attributed to the regulations rather than the guidance; a different Glaeser paper behind the 29.2 per cent; the rounding sentences attributed to ONS rather than the Handbook; "Where appropriate" and "If possible" cut from statutory and official sentences | Each corrected in this draft | Amber — none changed a truth; two changed a rule's wording | Entry 10 method note | e |
| 10 | 18 | 1063 | The cold reader found that a held status marked on a single room is itself a disclosure, that version 1's "consent to be found" survived in the money-view rule as a permission the literature says a community cannot give, that T4's consent rule was the chapter's legal reading presented as the regulator's, that a rule was written backwards, and that "withheld" was doing duty for all three nothings | Held status moved to the category and tested by the walk; the forum's agreement restated as a condition the house sets on itself; T4 restated as a stance with the alternative reading given; the rule corrected; "not shown" used for the umbrella | Red for the first — the prototype would have flagged the rooms it meant to protect | §14; §18; §19; Entry 10 | e |
| 10 | 19 | 1064 | Seven records now sit beneath a dashboard's numbers | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 | e |
| 11 | 1 | 749 | The storytelling null — version 1's load-bearing evidence for "the story is never a gate" — could not be re-read at source; its two figures (~4,300 sessions; 35.4%) are not in the reachable abstract | Carried the direction as secondary through three papers that cite it; withdrew the figures; rested the house shape on three mechanisms that were read | Amber — a rule had rested on numbers nobody in this sprint could see | `[Further research]`; §4; Entry 11 | b |
| 11 | 2 | 750 | No empirical dashboard literature evaluates dashboards; the surveys describe, the catalogue says it ranks nothing, the official guidance is practice | Built the chapter from perception evidence (Chapter 3), single-mechanism experiments and design-system practice, each marked | Amber | §1; the rules' kinds | a |
| 11 | 3 | 751 | Version 1 attributed "descriptive, not prescriptive" to the interaction taxonomy's authors; they do not say it | Quoted what they do say ("a community project"; "may be incomplete") | Yellow | §6; SOURCES | e |
| 11 | 4 | 752 | Version 1 cited "4 percentage points" for prediction; the paper's figure is 4.08 and "percentage points" on the page is a different comparison | Corrected; added the familiarity nulls | Yellow | §3 | e |
| 11 | 5 | 753 | Chapter 3 summarised McKenna et al. as "engagement up, comprehension flat"; the engagement gain belongs to visuals and transitions, and scroller v stepper did not differ | Corrected here; flagged for Chapter 3 | Amber | `[Counterbalance → Ch 3]` | e |
| 11 | 6 | 754 | The ONS ten-word chart-title rule version 1 quoted is gone; the current rules are 15 words and 60 characters; "Writing for GOV.UK" and "Explore local statistics" have moved | Re-cited the current pages and dates | Yellow | §3; SOURCES | e |
| 11 | 7 | 755 | No study compares the six landing patterns; no study of empty states or map-first landing; no measured tooltip discovery; no reach figures newer than 2019; no dot-density or hex evaluations; no "red = bad" map study | Said so; used single-pattern evidence; flagged for the prototype | Amber | `[Further research]`; `[Prototype flag]` | a |
| 11 | 8 | 756 | The fetch tool's reader invented four quotations from a W3C specification and reshaped two design-system sentences on first pass | Caught by presence checks; nothing invented used | Red if missed | Method note; Entry 11 | e |
| 11 | 9 | 757 | The brief's expected details drifted: Kim/Setlur/Agrawala for the responsive-insights paper (it is Kim, Rossi, Sarma, Moritz & Hullman); Kong "Agrawala" (Karahalios); Sarma's author list; Lin & Thornton's title; Xiong et al.'s design; "Fooled by beautiful data"; Nielsen's two conditions | Corrected each | Yellow | SOURCES | e |
| 11 | 10 | 758 | Two published figures do not survive a sanity check as printed (a t-statistic with an impossible p; "596 participants" summed across three studies) | Reported them with the caveat; did not reprint the statistic | Yellow | §6 | e |
| 11 | 11 | 759 | The national web archive cannot hold interactive content, and the one public model that took citation seriously changed its practice in 2025 — neither was in the brief's expectations | Made the snapshot a layer of the citation rule | Red — version 1's "stable address" rule would have produced citations that drift | §7; the rules | a* |
| 11 | 12 | 760 | The design system's default map breaks (Jenks) sit against the one controlled experiment (quantiles) | Reported both; made quantiles the Adaptable default with a declared reason either way | Yellow | §8 | d (also a1) |
| 11 | 13 | 761 | The trust evidence says a source line is read as a reason not to check, and metadata changes perceived thoroughness, not accuracy | Made "followable, not only present" the rule; kept the furniture and made it open the record | Amber — the house's first-screen furniture could have become a credential | §8; `[Counterbalance → Ch 1]` | e |
| 11 | 14 | 762 | The Decision Book has no rules on the first screen's sentence per place, landing pattern as endorsement, citable states, the small screen first, map breaks across views, generated-text labels or a face sheet | Built the rules table; logged a candidate chapter | Red — the prototype would ship a first screen with an address but no snapshot, and a map whose legend changes with every filter | Decision Book, a new chapter (*The surface*) | d |
| 11 | 15 | 763 | The design system has no snapshot banner, generated-citation or generated-text-label component, no small-area inset, no "how this argues" link, and DSH-21 treats the degraded state as decorative | Logged; not designed | Amber | Design system | d |
| 11 | 16 | 764 | The verifier found the prediction gain attached to the wrong dataset and condition (4.08 is predict-and-explain on moderately familiar data; a bare guess bought nothing on unfamiliar); a map-reading percentage given a quotation that was not on the page (the 93.1 per cent chose the darker of two maps; with legends about half still read by lightness); a GOV.UK phrase ("history mode") read as a rule about replacement when it is about a previous-government banner; two Xiong quotations in the wrong words; a title share credited to the wrong study; and five truncations (the onboarding exception; the fifth target-size exception; Kong's "most often neither"; the strong-dominance condition; the hover exception's first limb) | Each corrected in this draft | Amber — the prediction and map errors each changed a rule's wording | Entry 11 method note | e |
| 11 | 17 | 765 | The cold reader found the pass test measured recitation of a sentence, which the chapter's own title evidence says readers do whether or not the chart supports it; the two-readers test could not be run under the chapter's own linking rule; the filled example broke the house's word limit and put the district line before the input; "view", "state", "on request" and "layer" were each used in more than one sense; and the title promised a path the body did not treat | The test now asks for the figure and a next step; the two readers are defined by what is covered; the example rewritten; the distances defined with scrolling placed; a path subsection added | Red for the first — the prototype would have passed a first screen that performed | §3; §11; the break test; Entry 11 | e |
| 11 | 18 | 766 | Seven records and now a face sheet | Flagged for the closing chapter | Yellow | `[Revisit at end]`; Chapter 0 | e |
| 12 | 1 | 704 | No controlled study of whether readers attend to or remember data about their own locality | Rested on 42 interviews and one official account; flagged | Amber — the chapter's second truth stands on interview evidence | `03-tests/`; prototype | a |
| 12 | 2 | 705 | No UK measurement of residents' own neighbourhood boundaries at scale | Used the American survey of 7,498; UK definitions shown to leave the unit to the respondent | Amber | `[Further research]`; a probe with the forum | a |
| 12 | 3 | 706 | No experiment on whether readers notice an absent category or series | Narrowed CALVI to what it tests; carried the rule as a reading | Yellow | `03-tests/` | a |
| 12 | 4 | 707 | No test of "equal visual dignity" | Stance on LAY-08; prototype flag | Yellow | `03-tests/` | a |
| 12 | 5 | 708 | No study of whether a profile form reads as "better" rather than "different" | Chose the form the accuracy evidence prefers; flagged | Amber | prototype | a |
| 12 | 6 | 709 | No lay-reader test of dominance displays | Chose the ONS's spreads-plus-sentence form | Yellow | `[Further research]` | a |
| 12 | 7 | 710 | No evaluation of any community-review procedure; one researcher's account of harm | Assembled a procedure from guides and principles; marked it so | Amber — the house's own test has no literature behind its effects | Chapter 9's flag; `03-tests/` | a |
| 12 | 8 | 711 | The founding texts unreached (Lynch; Stevens; Lincoln & Guba p. 314; Coulton 2001 body; Birt 2016) | Quoted nothing from memory; used reachable successors; flagged | Yellow | a library pass | b |
| 12 | 9 | 712 | The agents had no web search | Direct addresses only; several items reported as "not found" rather than "does not exist" | Yellow | the next sprint's budget | b |
| 13 | 1 | 587 | No controlled comparison of description, table and structure for the same chart with time and accuracy | Stated each route's evidence separately; left the order as a procedure | Amber — the chapter's fourth truth rests on three small studies and one preprint | `03-tests/`; prototype | a |
| 13 | 2 | 588 | Nothing measures convergence for charts | Stated the page-level evidence and the gap; flagged | Amber — the chapter's title claim | prototype | a |
| 13 | 3 | 589 | The EHRC's 2026 Code, Chapter 7, unreached at source | Quoted a secondary site, flagged | Yellow | a library pass | b |
| 13 | 4 | 590 | The reduced-motion definition, the aria-live table, EN v4.1.1 clause 9 unreached | Quoted the techniques and the Recommendation's reasons instead | Yellow | `[Further research]` | b |
| 13 | 5 | 591 | UK prevalence for colour vision deficiency, dyslexia and vestibular disorders has no official source | Charity and US figures, marked | Yellow | `[Further research]` | a* |
| 13 | 6 | 592 | Reading-age figures have no source anywhere official | Replaced with the literacy survey figure and COGA's level | Yellow — the trade's number is folklore | the design-system conversation | a* |
| 13 | 7 | 593 | Official bodies disagree on where a chart's description lives | Reconciled as the W3C's two parts; the house picks one | Yellow | design system | a* (also d) |
| 13 | 8 | 594 | No UK regulator text on overlays; no UK website judgment | Reported the absence | Yellow | `[Further research]` | a* |
| 13 | 9 | 595 | The search ration left the BBC's guidelines and R&D, the FT's and the Guardian's practice unread | Named them unreached | Yellow | a later pass | b |

### 5.2 Chapters 14–15 — `Gap | Where it bites | Interim position | Who closes it`

| Ch | # | L | Gap | Where it bites | Interim position | Who closes it | Group [added] |
|---|---|---|---|---|---|---|---|
| 14 | 1 | 706 | No reader study compares an expressive form with its precise twin on what readers take from the data | Truth 2; the probes | Arunkumar 2023 (correlational) as the nearest; the probes run the comparison | The build; `[Validate with users]` | a |
| 14 | 2 | 707 | The two-audience test has no measurement anywhere in the book | Version 1 Ch 13; this chapter §10 | Held as a stance; a probe can measure it | The build | a (also e (the book's own claim)) |
| 14 | 3 | 708 | Tufte's rules quoted only at second hand; "within reason" unlocatable | §6 | Quote only the 2006 note in his hand; mark the rest secondary | Research, from the physical books | b |
| 14 | 4 | 709 | Lau & Vande Moere and Vande Moere & Purchase full texts | §3 | Abstracts only; axes and triangle not printed as the authors' | Research | b |
| 14 | 5 | 710 | Morais 2020 and 2021 paper PDFs | §5 | Analysis pages and Sorapure; effect and n confirmed at the analysis page | Research (HAL/ACM) | b |
| 14 | 6 | 711 | The BBC's postcode interactives not audited | §7 | Reported as not read; method via the Handbook | A reader with access, or Chapter 15 | b |
| 14 | 7 | 712 | Whether Chalabi's published pieces carry a source line | §5, §7 | Not reported | A reader with access | b |
| 14 | 8 | 713 | The flowchart's OSF materials | §7 | Qualified as the Open Practices Review did | Research, when the component opens | b |
| 14 | 9 | 714 | The tier vocabulary lacks the W3C's "specific sensory experience" | §6, §11 | Used in the register; adoption left to Chapter 16 | Chapter 16; the Decision Book | d |
| 14 | 10 | 715 | Gallery audit read text, not pixels | §7 | Colour, hover and keyboard reported only where a page says them | A visual audit, if wanted | b |
| 14 | 11 | 716 | "Seven words" has no source | §5 | Mantra re-tiered Adaptable; measured numbers given | None needed | a* |
| 14 | 12 | 717 | Kineticharts' comprehension count: the paper names four aspects and asks three questions | §5 | Reported as three | None needed | e |
| 14 | 13 | 718 | Mackinlay's Figures 14 and 15 not machine-readable | §3 | Ranking not printed as a list | From the printed figure | b |
| 15 | 1 | 670 | Trust in a display is not measured anywhere read; the one randomised test measured trust in government | Truth 1 | The producers' method is adopted; the display's trust is a probe question | The build; `[Validate with users]` | a |
| 15 | 2 | 671 | The JHU papers' body (anomaly handling; back-distribution) | §3 | Repository README used; abstract only for the paper | A reader with library access | b |
| 15 | 3 | 672 | The retired UK dashboard's own documentation | §3 | Successor's documentation and blogs used | A reader with archive access | b |
| 15 | 4 | 673 | Fingertips' quintile rule and FAQ | §3 | API method names used | Research, when the pages return | b |
| 15 | 5 | 674 | Scotland's per-indicator arrow thresholds | §5 | Reported as unfindable; the lesson is the finding | None; the reformed framework may print them | b |
| 15 | 6 | 675 | The Health Index's status | §5 | "Not updated since June 2023; no notice" | The ONS | a* |
| 15 | 7 | 676 | The Audience Agency's data arrangements | §6 | "No custodian named" as of 6 October 2026 | Research, by Carly's timeline | a* (also b; "by Carly's timeline") |
| 15 | 8 | 677 | The Charities SORP's paragraphs | §6 | Secondary summary only | Research, from the SORP | b |
| 15 | 9 | 678 | The Culture and Heritage Capital multiplier warning the brief expected | §6 | Reported absent; Chapter 6's discipline stands on its own grounds | None needed | e |
| 15 | 10 | 679 | Fingertips' amber rule is narrower than first read: amber when a leave-one-out trend runs the opposite way | §3 | Stated as such | None needed | e |
| 15 | 11 | 680 | A 2025 PCOS wave | §7 | 2023 is the latest found | Research | b |
| 15 | 12 | 681 | The fold question | §11 | A count given; the decision is Carly's | Carly | c |
| 15 | 13 | 682 | The precedent record's place among twelve records | §12 | A growing list, like the boundary log | Chapter 16; `[Revisit at end]` | e |

**The Cost column, tallied (Chapters 0–13, 181 rows; first word of the cell):** Amber 84; Yellow 65; Red 32. Chapters 14–15 (26 rows) carry no cost. Cells that qualify the colour ("Red if missed", "Red for the first", "Yellow — closed") are counted under the colour they begin with: "Red if missed" ×4; "— closed" ×2.

### 5.3 The rows grouped

Each row is placed once, in the group that its first column describes. The four groups asked for are (a)–(d). Two things did not fit them and are kept visible rather than forced in: **(a\*)** rows where what is missing is not a study but an official rule, method, source or custodian (or two official sources that disagree) — counted with (a) and shown separately; and **(e)** rows that are about none of the four — the book's own legend and glossary, corrections caught by the verifier or the cold reader, behaviour of the research tools, drift between the brief's expected quotations and the sources, and version 1 positions re-tested. Where a row plainly belongs to a second group too, the "also" note in the tables above says so; the counts below use the first placement only.

| Group | Rows | Share of 207 |
|---|---|---|
| (a) evidence the field does not have — no study or measurement exists | 23 | 11.1% |
| (a*) no official rule, method, source or custodian exists, or official sources disagree | 25 | 12.1% |
| **(a) and (a*) together** | **48** | 23.2% |
| **(b) sources unreachable to this book** | **32** | 15.5% |
| **(c) decisions awaiting Carly** | **4** | 1.9% |
| **(d) gaps in the house's own systems** | **38** | 18.4% |
| (e) none of a–d: the book's own apparatus and corrections | 85 | 41.1% |
| **Total** | **207** | 100% |

By chapter:

| Group | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (a) |  | 2 |  | 2 | 1 | 1 | 1 |  | 1 | 1 |  | 2 | 7 | 2 | 2 | 1 | 23 |
| (a*) |  |  | 1 |  |  | 1 | 4 | 4 | 2 |  | 5 | 1 |  | 4 | 1 | 2 | 25 |
| (b) |  |  |  |  | 2 | 1 | 1 | 1 | 3 | 2 | 2 | 1 | 2 | 3 | 8 | 6 | 32 |
| (c) |  |  |  |  | 1 | 2 |  |  |  |  |  |  |  |  |  | 1 | 4 |
| (d) | 2 | 2 | 3 | 5 | 8 | 3 | 3 | 1 | 3 | 2 | 2 | 3 |  |  | 1 |  | 38 |
| (e) | 2 | 2 | 5 | 3 | 6 | 5 | 7 | 9 | 10 | 11 | 10 | 11 |  |  | 1 | 3 | 85 |
| All | 4 | 6 | 9 | 10 | 18 | 13 | 16 | 15 | 19 | 16 | 19 | 18 | 9 | 9 | 13 | 13 | 207 |

**(a) evidence the field does not have — no study or measurement exists — 23 rows.**

- G-1.1 — No independent measurement exists of how many dashboards go unused
- G-1.2 — No study found on staleness — what happens when a dashboard stops changing
- G-3.6 — The field's most-quoted interaction statistic is an anecdote about one button
- G-3.7 — No study of the big-number tile; no study of legends against labels; no UK measurement of chart literacy
- G-4.18 — No evidence was found that provenance on the face changes a reader's decision — the chapter's thesis rests beside a gap
- G-5.12 — No evidence found that decision-makers prefer composites to dashboards; the belief underwrites most index projects
- G-6.16 — No evidence at source for a positive-deviance method at small n
- G-8.9 — No measured evidence that stale dashboards cost trust; no measured study of UK open-data staleness; no measured bytes-per-view for a map
- G-9.8 — No empirical study of dot-voting bias; no ticketing-records network study with validation; no measured "you said, we did" effect; no study comparing crowdsourced place scores with residents' own ratings
- G-11.2 — No empirical dashboard literature evaluates dashboards; the surveys describe, the catalogue says it ranks nothing, the official guidance is practice
- G-11.7 — No study compares the six landing patterns; no study of empty states or map-first landing; no measured tooltip discovery; no reach figures newer than 2019; no dot-density or hex evaluations; no "red = bad" map study
- G-12.1 — No controlled study of whether readers attend to or remember data about their own locality
- G-12.2 — No UK measurement of residents' own neighbourhood boundaries at scale
- G-12.3 — No experiment on whether readers notice an absent category or series
- G-12.4 — No test of "equal visual dignity"
- G-12.5 — No study of whether a profile form reads as "better" rather than "different"
- G-12.6 — No lay-reader test of dominance displays
- G-12.7 — No evaluation of any community-review procedure; one researcher's account of harm
- G-13.1 — No controlled comparison of description, table and structure for the same chart with time and accuracy
- G-13.2 — Nothing measures convergence for charts
- G-14.1 — No reader study compares an expressive form with its precise twin on what readers take from the data
- G-14.2 — The two-audience test has no measurement anywhere in the book
- G-15.1 — Trust in a display is not measured anywhere read; the one randomised test measured trust in government

**(a*) no official rule, method, source or custodian exists, or the official sources disagree — 25 rows.**

- G-2.4 — No source distinguishes "numbers for understanding" from "numbers for advocacy" in the terms the studio needs
- G-5.13 — The handbook's own visualisation step says nothing about showing uncertainty, while its sensitivity step requires rank intervals
- G-6.7 — The national rules' identifying thresholds (2, 3, 5, 7) assume an intruder without local knowledge; a scene's regulars can name three venues
- G-6.8 — No method found for commercial displacement (venues, promoters); the household literature is all there is
- G-6.9 — The AQuA Book 2025 has no statement about validating a model against outturn; its validation is user-needs-based
- G-6.12 — The Audience Agency entered liquidation on 10 September 2026; the sector's audience yardstick has no custodian
- G-7.5 — The Analysis Function's chart standard ("Always rank bars by value") and the statistical guidance ("inappropriate to rank") pull against each other with no reconciliation in either
- G-7.6 — The two official traditions disagree on reading turning points (textbook: from the trend-cycle; Eurostat: withhold the end-point)
- G-7.7 — No official rule on percentage change from a small base, on minimum series length (ONS), or on pre-specifying comparator groups in the public sector
- G-7.10 — Lee & Lemieux dispute the "only at the threshold" limitation that the Magenta Annex states as fact
- G-8.8 — No open primary source for the "60–80% of lifecycle cost is maintenance" figure; GAO measures spending, not lifecycle
- G-8.10 — No design system reached (GOV.UK, Carbon, PatternFly) says a dashboard should show its last refresh
- G-10.2 — The regulator's guidance had caught up unevenly; most pages read carry "under review"
- G-10.6 — The ICO's two inference passages pull in different directions (a correct guess from anonymous data is not disclosure; an intended inference is Article 9 processing however uncertain)
- G-10.7 — ONS's most direct guidance on interactive tools sits in a births-and-deaths policy, not in census or table-builder documentation; the census builder states no registration, logging or query limit
- G-10.8 — No published protocol for intruder-testing an interactive view; the 2011 and 2021 census intruder-test results unreached
- G-10.9 — Neither the regulator's DPIA list nor its 2022 taxonomy names harm to a place; the statistical system's guidance does
- G-11.11 — The national web archive cannot hold interactive content, and the one public model that took citation seriously changed its practice in 2025 — neither was in the brief's expectations
- G-13.5 — UK prevalence for colour vision deficiency, dyslexia and vestibular disorders has no official source
- G-13.6 — Reading-age figures have no source anywhere official
- G-13.7 — Official bodies disagree on where a chart's description lives
- G-13.8 — No UK regulator text on overlays; no UK website judgment
- G-14.11 — "Seven words" has no source
- G-15.6 — The Health Index's status
- G-15.7 — The Audience Agency's data arrangements

**(b) sources unreachable to this book — 32 rows.**

- G-4.12 — Hawkins, Barnett & Lewis, Grubbs, Tukey, Huber, Anderson: the canonical outlier and long-tail texts were all unreachable at source
- G-4.14 — The data contract named in the brief was not available to this sprint
- G-5.7 — Goodhart, Hoskin, Lincoln & Guba, Borsboom, Campbell & Fiske, Thomas — canonical texts unreachable at source
- G-6.1 — No web search for the whole sprint; the scholarly web (Project Euclid, JSTOR, PNAS, PMC, Science, T&F, Wiley, ScienceDirect, IMF) closed to a fetch tool; seventeen canonical texts unreached
- G-7.1 — No web search again; twenty-two canonical or official texts unreached; the comparison literature's founding article (Espeland & Sauder 2007) and the funnel plot's founding paper (Spiegelhalter 2005) read at abstract only
- G-8.1 — No web search for any agent; the fetch reader truncates at ~100–120k characters, so RFC 9110's `Retry-After` and conditional-request sections, DWBP's freshness and preservation practices and DCAT 3's frequency definition were all beyond reach
- G-8.5 — Eventbrite's developer site, the OS plans page and the ONS geography portal are script-only shells; the search-endpoint removal and the OS free allowances could not be verified
- G-8.6 — The National Archives' OGL page returned a redirect loop
- G-9.1 — No web search for any agent, and the least open literature so far: the founding texts of the made and excess registers (Böhme; Anderson), the place-attachment review (Lewicka), the standard's own texts (ISO 12913) and the strongest sentiment test (Jaidka 2020) were all closed
- G-9.11 — The Mitchell et al. 2013 correlations are rendered as images on the published page
- G-10.3 — No web search; several load-bearing bodies closed (Science; tandfonline; Springer; Bloomsbury; the EHRC code; PAS; Datatilsynet)
- G-10.13 — The ONS Census 2021 geography floor for sexual orientation was not established on any page reached
- G-11.1 — The storytelling null — version 1's load-bearing evidence for "the story is never a gate" — could not be re-read at source; its two figures (~4,300 sessions; 35.4%) are not in the reachable abstract
- G-12.8 — The founding texts unreached (Lynch; Stevens; Lincoln & Guba p. 314; Coulton 2001 body; Birt 2016)
- G-12.9 — The agents had no web search
- G-13.3 — The EHRC's 2026 Code, Chapter 7, unreached at source
- G-13.4 — The reduced-motion definition, the aria-live table, EN v4.1.1 clause 9 unreached
- G-13.9 — The search ration left the BBC's guidelines and R&D, the FT's and the Guardian's practice unread
- G-14.3 — Tufte's rules quoted only at second hand; "within reason" unlocatable
- G-14.4 — Lau & Vande Moere and Vande Moere & Purchase full texts
- G-14.5 — Morais 2020 and 2021 paper PDFs
- G-14.6 — The BBC's postcode interactives not audited
- G-14.7 — Whether Chalabi's published pieces carry a source line
- G-14.8 — The flowchart's OSF materials
- G-14.10 — Gallery audit read text, not pixels
- G-14.13 — Mackinlay's Figures 14 and 15 not machine-readable
- G-15.2 — The JHU papers' body (anomaly handling; back-distribution)
- G-15.3 — The retired UK dashboard's own documentation
- G-15.4 — Fingertips' quintile rule and FAQ
- G-15.5 — Scotland's per-indicator arrow thresholds
- G-15.8 — The Charities SORP's paragraphs
- G-15.11 — A 2025 PCOS wave

**(c) decisions awaiting Carly — 4 rows.**

- G-4.4 — The studio's six kinds of nothing merge *not applicable* with *not asked*, which every official scheme separates; and have no place for "included elsewhere" or "not yet available"
- G-5.5 — No house position on whether the measure is one-tailed (shortfall) or two-tailed (thriving)
- G-5.9 — The one sector composite is named in a method audit; the brief says the sector is not researched
- G-15.12 — The fold question

**(d) gaps in the house's own systems — design system, Decision Book, data contract, the brief, the studio's stated rules — 38 rows.**

- G-0.1 — The design system has no component for a *kind-of-claim* mark (Standard / Evidence / Reading / Practice / Nightlife Culture)
- G-0.2 — The design system's interim rule says "never RAG tags" for public severity marks; the book's gap register uses red / amber / yellow
- G-1.3 — The Decision Book's data chapters do not say "the unit of aggregation is a decision"
- G-1.4 — The design system's evidence rules cover charts, not the conduct of release (fixed time, simultaneous release, open data route)
- G-2.2 — The brief's three user groups are, on the evidence, at least seven graders with contradictory rules
- G-2.3 — The Decision Book's evidence rules say how to show a number fairly, not whether the display is monitoring or evaluation
- G-2.9 — The brief's recognition test ("do not recognise their place") has no stated method
- G-3.1 — The Decision Book's chart chapter rests 3D and pie rules on the conjectural half of the perceptual hierarchy
- G-3.2 — "Label at the mark" is Fixed in the Decision Book and the design system with no direct experiment behind it
- G-3.3 — The Decision Book says a line chart's axis "may be broken where necessary, and labelled", as if the label settled it; the Analysis Function checklist already warns that a signposted break still shows bar sizes "very strongly", and the experiments extend that to lines
- G-3.4 — The design system and the Decision Book have no rule on the title's power to decide the reading, or on how much text a chart carries
- G-3.5 — No rule in either on stock against flow or linear against log for public displays
- G-4.1 — The Decision Book's gap rule ("dashed, hatched, or broken") can be read as permitting a dashed join across a missing point, which the standard it cites rejects
- G-4.2 — The Decision Book's provenance set omits the responsible party and the issued/modified dates
- G-4.6 — Neither the Decision Book nor the design system has a rule on the unit of observation or the row count
- G-4.7 — No rule in either on the denominator, the reference class, or the funnel for small bases
- G-4.8 — No rule in either on reading a platform feed (coverage, selection, the ten characteristics)
- G-4.9 — No rule in either on outliers beyond "show the gaps"
- G-4.10 — No rule in either on concentration measures beside totals
- G-4.11 — "Reliable" is used in the failure register and the design system in the ordinary sense; official usage means revisions
- G-5.1 — The Decision Book has no rules on composites, weights, aggregation, sensitivity or what accompanies a score
- G-5.3 — The studio's "validation by recognition" was a single rule; the measurement literature splits it into legitimacy (who chooses what counts) and validity (five sources), and does not count recognition as the latter
- G-5.4 — The design system's evidence components (source line; comparability gate; provenance code) cover a chart's number, not a composed one
- G-6.3 — The Decision Book has no rules on gross against net, distributional weights, causal rungs, leading indicators, multiple comparisons, alert policy, shrinkage, or the precision reason for withholding
- G-6.5 — The studio's ledger ("value created and value retained") used "created" for a gross figure
- G-6.6 — Official suppression rules hide small numbers for two reasons (confidentiality; precision) and one official table colours both the same
- G-7.8 — The Decision Book has no rules on rankings, standardisation, peers, seasonal adjustment, regression to the mean, the designs, spillovers, power, the ladders, or projections
- G-8.11 — The Decision Book treats empty and error states as Decorative (DSH-21); this chapter makes the degraded state a Fixed procedure
- G-8.12 — The Decision Book has no rules on freshness display, dependencies and terms, refresh, watch and alarm, availability objective, budget and device, progressive enhancement, tile supply, or retirement
- G-8.13 — The design system has no map component, no freshness component, no degraded-tile state, no byte budget
- G-9.12 — The Decision Book has no rules on felt measures at all
- G-9.13 — The design system has no component for a distribution of felt responses, a sample on the face, a discordance matrix, "what this changed", or testimony in the respondent's register
- G-10.15 — The Decision Book has no rules on query-time protection, the walk, the held status, lawful basis, the DPIA's consultation step, the Online Safety Act, withdrawal tiers or harm to places
- G-10.16 — The design system has no component for a held layer, the three nothings, a record beside a panel, a withdrawal notice at contribution, or a stigma test for colour
- G-11.12 — The design system's default map breaks (Jenks) sit against the one controlled experiment (quantiles)
- G-11.14 — The Decision Book has no rules on the first screen's sentence per place, landing pattern as endorsement, citable states, the small screen first, map breaks across views, generated-text labels or a face sheet
- G-11.15 — The design system has no snapshot banner, generated-citation or generated-text-label component, no small-area inset, no "how this argues" link, and DSH-21 treats the degraded state as decorative
- G-14.9 — The tier vocabulary lacks the W3C's "specific sensory experience"

**(e) none of a–d: the book's own apparatus and corrections — 85 rows.**

- G-0.3 — The original four kinds had no home for practitioner frameworks, on which Chapters 1 and 2 both leaned
- G-0.4 — "Fixed" was being used for three things (a rule to obey; a fact the book is confident of; a sequence that is the hard line) and a cold reader of Chapter 2 could not tell which
- G-1.5 — Chapter 0's four kinds of claim have no clean home for practitioner sources (Few, Eckerson, Behn)
- G-1.6 — Fixed rules resting on abstract-only reading were not visibly marked in the first draft
- G-2.1 — Chapter 0's legend has no kind for practitioner frameworks, and this chapter rests on a dozen of them
- G-2.5 — Two reads of Oliver et al.'s Table 1 returned different counts in draft 1
- G-2.6 — The chapter's first rule asserted that one display can be legible to all readers, while its own sources say the first screen is always in somebody's grammar
- G-2.7 — No reader was interviewed for a chapter about readers; two rows of the table have no study behind them
- G-2.8 — Hastings & Weinstein is routinely cited (including by this chapter's own research agent) as evidence that re-sorting into a ranking changes decisions; the authors say the format added little
- G-3.8 — Chapter 0's legend has no way to mark "a research agent's correction was itself wrong"
- G-3.9 — The chapter's first draft quoted a sentence from the Office for Statistics Regulation that the source does not contain, and built a headline on it
- G-3.10 — The cold reader found the Fixed tier applied to small and adjacent-domain studies while the chapter demanded that standard of others
- G-4.3 — Chapter 1 cited the Code of Practice's Q1–Q3; the Code is now edition 3.0 and those principles are Standards 6 and 7
- G-4.5 — Version 1's gap vocabulary mixed kinds of nothing with reasons for a series break, and named a kind ("community-held") that no official vocabulary has
- G-4.13 — Chapter 0's legend has no marking for a quotation reached through a named reproduction
- G-4.15 — The first draft applied the chapter's first truth to everyone's numbers but the studio's, and closed the worked case with "None of this weakens the finding"
- G-4.16 — Three paraphrases stood inside quotation marks (OSR on users; DCAT on absent values; Salganik's grouping labels), two numbers were wrong (eight units; the Wang & Strong survey stages) and six quotations were silently truncated
- G-4.17 — The Fixed tier was used with four qualifiers ("as a stance", "as a procedure", "adopted", "as disclosure") that Chapter 0 does not define
- G-5.2 — Version 1 cited the 20%/21% and 40%/81% figures without naming the index; a reader could take them as the HDI's
- G-5.6 — "Reliability" now has three senses in the book (revisions; replications; inter-rater) and the glossary has one
- G-5.8 — A research agent's fetch tool fabricated quotations from a paper it had opened (Alkire 2008); the agent caught it by string search
- G-5.10 — Draft 1's arithmetic test on that composite was unfair by the chapter's own rules: it declared that "no standard mean" recovered the headline when a weighted mean, a power mean or indicator-level equal weights would, misstated the harmonic mean, and applied the "recipe not on the face" verdict to one instrument while three others in the table also publish no sensitivity analysis
- G-5.11 — Five verification mismatches: harmonic mean; SPI indicator count; a Messick sentence not in the report read and a truncated one; the PASC 80% figure narrowed; a Holden sentence that is Holden quoting the Cabinet Office; plus web-guide sentences attributed to the 2008 handbook
- G-6.2 — Two UK method texts were replaced in 2026 at their old addresses (Magenta Book May 2026; Green Book February 2026); earlier chapters cite "Green Book 2022" from the live link
- G-6.4 — Version 1's claim ladder put a rung-one fact at the top labelled as a counterfactual, euphemised the lower rungs as "associational", and had no deadweight line; its two-track display asserted a lead
- G-6.10 — The fetch tool's reader declares a 125-character quote cap and merges sentences to fit it — the mechanism behind Chapter 5's "fabricated" quotations
- G-6.11 — One agent's rendering of a table cell (Martin & Sunley's ecological-resilience definition) failed its string check after reading fluently
- G-6.13 — Draft 1 glossed Gelman's county as "the most dangerous place in the state" and "the radon capital of Minnesota"; the paper says only "an implausibly high estimate"
- G-6.14 — Draft 1 credited a quotation to Easton et al. that they quote from Baeten et al.; misquoted Arvidson's abstract where the full text was on the record consulted; put an invented SROI ratio in quotation marks; and called the Additionality Guide's definition its "first sentence"
- G-6.15 — Draft 1 licensed "contributed to" from observational data alone, against the Magenta Book's condition that alternatives be ruled out, and said so inconsistently across the truths, rules and checklist; and let the studio's claim ladder pass Hill's fundamental question with its main alternative (the trip was coming anyway) unaddressed
- G-7.2 — Version 1 paraphrased the C3 Monitor as "one city in five's rank reflects modelling choices rather than data"; the actual wording is rank intervals under ±3 for about 80% under weight and normalisation perturbation only
- G-7.3 — Version 1 proposed peers chosen by the place; the evidence reached on self-selected comparators (two abstracts, from executive pay, with qualifications) finds the choice tends to flatter the chooser
- G-7.4 — Version 1's "a borough with a scene beats a borough with a superclub" is a ranking sentence
- G-7.9 — The Magenta Book Annex A was read at a 2020 upload path; its title page reads May 2026 on two fetches
- G-7.11 — The chapter's filled comparison record uses an illustrative interval (3 of 34) computed by the author
- G-7.12 — Four records now sit beneath a dashboard's numbers across Chapters 4–7
- G-7.13 — Draft 1 said the Bank of England's fan chart was "abolished in 2024" and attached the OBR's chart caveat to it; the fan ran until February 2026 and the April 2026 report is the first without one
- G-7.14 — Draft 1 truncated three quotations before a qualifying clause (APHO on comparing standardised ratios; Bizjak on peer groups; HQIP on case-mix), credited a four-author paper to its two authors plus two commentators, gave the External Panel Review five recommendations where it made eleven and credited it with a sentence it was summarising from earlier reviews, dated the ONS nearest-neighbours output a year late, halved the C3 Monitor's simulation count, inserted a word into a Conference Board sentence, and put an agent's gloss in quotation marks
- G-7.15 — Draft 1 gave "contributed to" to any comparison-group design and no verb to an interrupted series, a cut-off or a synthetic control, and called the band rule's reach unclear between quintiles and the ONS's three words
- G-8.2 — On first pass the fetch tool's reader invented standards-sounding sentences for sections it could not see (DWBP BP21/22; DCAT 3 frequency and temporal resolution)
- G-8.3 — About a quarter of the brief's "stable" URLs and phrasings had drifted: Looker Studio renamed; Monte Carlo's domain and a pillar; Netlify's tier; the AWS library; Azure's bulkhead wording; the PMTiles tagline; the SRE workbook URL; GitHub's timezone rule; the OSM tile policy; YouTube's quota; "surprisingly powerful" never existed
- G-8.4 — Three expected quotations were not in the sources: GDS's "deprecation period" and "do not break backward compatibility"; OSM's "forbidden without prior permission"; YouTube's "100 units per search"
- G-8.7 — One research agent could not find the Analysis Function dashboards guidance at guessed URLs; another found it at the policy-store path
- G-8.14 — Several platform clause numbers (Spotify IV.3.a/b, IX.8.h) wavered between the fetch tool's passes
- G-8.15 — The fetch tool's reader invented publication years for the SRE book and its siblings on first pass (2017, 2020, 2016); none is on the pages
- G-8.16 — The chapter's chain arithmetic, Mapbox cost example, 12.6 KB per tile request, 75:1 boundary ratio and 43 per cent renderer share are all its own computations
- G-8.17 — The verifier found a spliced quotation (two of Willison's sites run together), a quotation attributed to the wrong chapter of the SRE texts, a sentence attributed to the 2025 Almanac that is in the 2024 edition, five quotations closed before a qualifying clause, and the boundary-file ratio dividing unlike records
- G-8.18 — The cold reader found "heartbeat" and "tile" each used in two senses, "page" (pager) unglossed, alert/ticket/alarm used loosely, and the observatory described in section 11 as version 1's model when it was its founding failure
- G-8.19 — Five records now sit beneath a dashboard's numbers across Chapters 4–8
- G-9.2 — The fetch tool's reader invented a word in one source (Fung's "effective governance" for "effective administration"), paraphrased two abstracts as if verbatim, and returned the wrong document for two guessed URLs
- G-9.3 — The brief's expected quotations drifted again: "singular affective qualities that emanate from but exceed the assembling of bodies" (Anderson) could not be verified; "safety paradox" is not in Reed et al.; Livehoods is "of a City" not "of Neighborhoods"; Park et al. never say "valence"; Nielsen's rule is 2006 not 1996; DeVellis has nine steps not eight; Nevo defends face validity's measurability rather than dismissing it; ISO/TS 12913-3:2019 is withdrawn
- G-9.4 — Version 1's three-register split was asserted from a raw sweep; its sources (Böhme, Anderson, ISO) were not all reachable to re-test
- G-9.5 — Version 1 proposed the human dot plot as a collection instrument with no measurement source
- G-9.6 — Version 1 illustrated discordance with a finding about a place
- G-9.7 — "Co-production" was used in version 1 and the brief for any contribution by the scene
- G-9.9 — The Scenescapes limitation sentence is Silver & Clark's own, quoted by a reviewer; the Oldenburg characteristics are a secondary source's wording; the Lincoln & Guba phrase is a methods guide's report
- G-9.10 — ONS4's cognitive testing is sometimes attributed to Dolan, Layard & Metcalfe; their paper does not use the words
- G-9.14 — The verifier found a reversed referent (Park et al.'s "these measures" are earlier methods, not the study's), a reviewer's praise quoted as a publisher's description, two ONS review sentences that belong to the office's user guide, a performance-score sentence and the pole-pairs that belong to Silver & Clark 2014 rather than 2010, "six settings" for six datasets from five, a diary measure called single-item, and the MSC "not-for" list overstated (the guide says other methods are less time-consuming)
- G-9.15 — The cold reader found "register", "measure", "instrument", "indicator", "co-produced", "recognition", "record" and "face" each used in more than one sense, the family of section 5 named by a word the chapter reserves for something stricter, and the floor of fifty unexamined against the brief's own "aggregation of the biggest"
- G-9.16 — Six records now sit beneath a dashboard's numbers
- G-10.1 — The brief's statutory map was out of date in four places on the day of reading (Article 89 and s.19 omitted; Article 14(5)(b) omitted; definitions moved to Article 4(2)–(7); the regulator renamed)
- G-10.4 — The fetch tool's reader invented a regulator's definition (FDA), a six-part list (ODI) and page numbers (Nissenbaum); misdated Grimmelmann; compressed statutory sub-paragraphs into paraphrase on first pass
- G-10.5 — The brief's expected quotations drifted: "release and forget" is not the regulator's phrase (it says "release model"); "reasonable degree of certainty" is not on the special-category page (the test is intention); GitHub's "consider … compromised" sentence is gone; the Grindr fine is Norwegian, not the ICO's; the 1 billion Strava activities is 700 million; the Census Bureau's 46/71/38/17% are not in Hawes; "forced visibility" has no source; Charlton's slogan origin is not on the publisher page; "no surprises" is not on the NSDEC page; the accessibility regulations' scope is reg 4, not reg 3
- G-10.10 — The leading redlining paper's effect sizes are in the working paper, not the published abstract; the counter-paper's 4–20% is a different quantity
- G-10.11 — "Consent at scene level" (version 1; Chapter 9) has no form in law or in the ethics literature
- G-10.12 — OCAP's owner's caution is narrower than the chapter planned ("specifically First Nations—not Indigenous") and CARE is more permissive ("distinctive communities")
- G-10.14 — Version 1's "threshold three" and "with the reason" were static-table rules applied to an interactive tool
- G-10.17 — The verifier found a 48-hour take-down limit inserted into the Online Safety Act on 29 June 2026 that the first draft missed; "weakens" in quotation marks where the book says "deteriorates"; a 2012 crime-map review misdated to 2011 and miscalled the maps' own evaluation; the WCAG standard attributed to the regulations rather than the guidance; a different Glaeser paper behind the 29.2 per cent; the rounding sentences attributed to ONS rather than the Handbook; "Where appropriate" and "If possible" cut from statutory and official sentences
- G-10.18 — The cold reader found that a held status marked on a single room is itself a disclosure, that version 1's "consent to be found" survived in the money-view rule as a permission the literature says a community cannot give, that T4's consent rule was the chapter's legal reading presented as the regulator's, that a rule was written backwards, and that "withheld" was doing duty for all three nothings
- G-10.19 — Seven records now sit beneath a dashboard's numbers
- G-11.3 — Version 1 attributed "descriptive, not prescriptive" to the interaction taxonomy's authors; they do not say it
- G-11.4 — Version 1 cited "4 percentage points" for prediction; the paper's figure is 4.08 and "percentage points" on the page is a different comparison
- G-11.5 — Chapter 3 summarised McKenna et al. as "engagement up, comprehension flat"; the engagement gain belongs to visuals and transitions, and scroller v stepper did not differ
- G-11.6 — The ONS ten-word chart-title rule version 1 quoted is gone; the current rules are 15 words and 60 characters; "Writing for GOV.UK" and "Explore local statistics" have moved
- G-11.8 — The fetch tool's reader invented four quotations from a W3C specification and reshaped two design-system sentences on first pass
- G-11.9 — The brief's expected details drifted: Kim/Setlur/Agrawala for the responsive-insights paper (it is Kim, Rossi, Sarma, Moritz & Hullman); Kong "Agrawala" (Karahalios); Sarma's author list; Lin & Thornton's title; Xiong et al.'s design; "Fooled by beautiful data"; Nielsen's two conditions
- G-11.10 — Two published figures do not survive a sanity check as printed (a t-statistic with an impossible p; "596 participants" summed across three studies)
- G-11.13 — The trust evidence says a source line is read as a reason not to check, and metadata changes perceived thoroughness, not accuracy
- G-11.16 — The verifier found the prediction gain attached to the wrong dataset and condition (4.08 is predict-and-explain on moderately familiar data; a bare guess bought nothing on unfamiliar); a map-reading percentage given a quotation that was not on the page (the 93.1 per cent chose the darker of two maps; with legends about half still read by lightness); a GOV.UK phrase ("history mode") read as a rule about replacement when it is about a previous-government banner; two Xiong quotations in the wrong words; a title share credited to the wrong study; and five truncations (the onboarding exception; the fifth target-size exception; Kong's "most often neither"; the strong-dominance condition; the hover exception's first limb)
- G-11.17 — The cold reader found the pass test measured recitation of a sentence, which the chapter's own title evidence says readers do whether or not the chart supports it; the two-readers test could not be run under the chapter's own linking rule; the filled example broke the house's word limit and put the district line before the input; "view", "state", "on request" and "layer" were each used in more than one sense; and the title promised a path the body did not treat
- G-11.18 — Seven records and now a face sheet
- G-14.12 — Kineticharts' comprehension count: the paper names four aspects and asks three questions
- G-15.9 — The Culture and Heritage Capital multiplier warning the brief expected
- G-15.10 — Fingertips' amber rule is narrower than first read: amber when a leave-one-out trend runs the opposite way
- G-15.13 — The precedent record's place among twelve records

Within (d), by which system the row names (anywhere in the row): Decision Book 18; design system 10; other house system (data contract, brief, the studio's own rule) 5; both 5.

Rows in (d) that ask for a new Decision Book chapter ("logged as a candidate chapter" / "a new chapter"): G-5.1, G-6.3, G-7.8, G-8.12, G-9.12, G-10.15, G-11.14 — 7 rows, one each from Chapters 5, 6, 7, 8, 9, 10, 11.

Rows that name Carly anywhere (11): G-1.3 (d), G-2.2 (d), G-2.3 (d), G-2.7 (e), G-3.1 (d), G-4.1 (d), G-4.4 (c), G-5.5 (c), G-5.9 (c), G-15.7 (a*), G-15.12 (c). Only four of these are decisions she is asked to make (group c: G-4.4 the seventh kind of nothing; G-5.5 one-tailed or two-tailed; G-5.9 where the sector composite's audit sits; G-15.12 the fold question); the others are routed "via Carly" to the Decision Book, the brief or the test protocols.

Rows that only count the records (group e): G-7.12, G-8.19, G-9.16, G-10.19, G-11.18, G-15.13.

Rows that record the research tools' limits or behaviour (no web search; the fetch tool's reader inventing or reshaping text) — across groups b and e: G-5.8, G-6.1, G-6.10, G-7.1, G-8.1, G-8.2, G-8.14, G-8.15, G-9.1, G-9.2, G-10.3, G-10.4, G-11.8, G-12.9, G-13.9 (15 rows).

---

## PART 6 — THE CONFLICT LOGS, ASSEMBLED

Fifteen logs, one at the end of each of Chapters 1–15 (Chapter 0 has none; it describes the section in its template table, L65). The heading is `## Design system (Style Guide v1.5) — conflict log` in Chapters 1–3 and `## Design system (Style Guide v1.5) and Decision Book — conflict log` in Chapters 4–15.

**The form changes twice.** Chapters 1–7 and 12–13 print three labelled paragraphs — **Agrees.** / **Conflicts.** / **Silent on.** Chapters 8–11 print two — **Agrees.** / **Conflicts.** — and put what the other chapters call "Silent on" inside the Conflicts paragraph as "**Logged for the design system:**" and "**Logged for the Decision Book:**". Chapters 14–15 print a table, `Item | Where | What this chapter found | Status`. Only Chapters 14 and 15 therefore have a printed Status; for Chapters 1–13 the status is whatever the paragraph says in words. Each paragraph is treated below as one row.

### 6.1 Chapters 1–13 — the paragraphs, in full

**Chapter 1** (heading L474: `## Design system (Style Guide v1.5) — conflict log`)

> [Ch 1 · L476 · Agrees] **Agrees.** "Strong design must never make weak evidence look stronger than it is" is this chapter's evidence section in one line. The guide's requirement that every chart carry provenance, period, geography and a comparability declaration is Kitchin's conclusion and the Code's quality pillar applied. Suppressed data marked `[c]`, never blank, is section 6's last rule.

> [Ch 1 · L478 · Conflicts] **Conflicts.** None found.

> [Ch 1 · L480 · Silent on] **Silent on.** The conduct of release — fixed time, simultaneous release, data alongside display — which this chapter finds is where public trust was actually earned; the unit of aggregation as a declared choice; the measurement of use. All three are candidates for the design system's dashboard section when it exists.

**Chapter 2** (heading L691: `## Design system (Style Guide v1.5) — conflict log`)

> [Ch 2 · L693 · Agrees] **Agrees.** "Strong design must never make weak evidence look stronger than it is" is, in this chapter, the Dragicevic & Jansen finding and the Hullman finding made into a rule. The guide's comparability gate is the denominator rule of section 5. Provenance on every chart is the "checkable source first" rule of section 4. The guide's instruction never to show RAG tags publicly is consistent with the headline-to-caveat finding: a traffic light is a caveat-free headline.

> [Ch 2 · L695 · Conflicts] **Conflicts.** One possible. The guide's register — joy first, then value, evidence, action — is a persuasion order, and section 5 reports one study in which the reader already opposed was better served by the plain table than by the handsome object. This is not a conflict in the design system's own domain (the public, the scene, the sympathetic reader) but it is a conflict for the officer who arrives hostile. The resolution this chapter proposes is not to change the register but to make a plain view a first-class route. Logged for Carly; the design system may want a line on it. `[Counterbalance → design system]`

> [Ch 2 · L697 · Silent on] **Silent on.** The monitoring/evaluation label; the evidence-ladder level; the display of valuation caveats; the recognition sequence; the plain-table route. All candidates for the design system's dashboard section when it exists.

**Chapter 3** (heading L708: `## Design system (Style Guide v1.5) — conflict log`)

> [Ch 3 · L710 · Agrees] **Agrees.** "Strong design must never make weak evidence look stronger than it is" is, in this chapter, the truncation finding, the stock/flow finding and the within-the-bar bias. The guide's provenance-on-every-chart rule and its evidence components are consistent with the two-part text alternative and the data-download rule. The guide's one-type-rule and status chips are not contradicted by anything here.

> [Ch 3 · L712 · Conflicts] **Conflicts.** One, inherited from Chapter 2 and sharpened. The guide's joy-first register and its licence for expressive form sit against this chapter's first-glance evidence (appeal rewards simplicity and prototypicality), its ornament evidence (anything that touches the mark costs accuracy; anything behind the data costs time), and the Decision Book's own rule that in dashboards creativity lives in layout and hierarchy, not encodings. This is not a conflict in principle — the design system already says meaning never lives only in the decorative layer — but it is a conflict in practice every time a chart is styled, and the guide may want a line that says where on a dashboard the joy goes: words, hierarchy, register, imagery around the chart; never the mark, the axis or the colour that carries a value. `[Counterbalance → design system]`

> [Ch 3 · L714 · Silent on] **Silent on.** The title as the message-carrier (the guide governs headings, not chart titles); the amount and placement of text on a chart; the forms of uncertainty display; truncation; stock against flow; the public defaults for scale and risk; interaction use rates and the no-hover phone; defaults as advice. All candidates for the design system's dashboard section when it exists.

**Chapter 4** (heading L861: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 4 · L863 · Agrees] **Agrees.** The design system's provenance-on-every-chart rule and its status chips (COL-17: "Status and provenance chips carry a short code that states the tier in text") are the right furniture for truths 2 and 3: a code in text, never colour alone, is what the Analysis Function's square-bracket shorthand is. "Strong design must never make weak evidence look stronger than it is" is, in this chapter, the gap that is not joined, the [p] that is not dropped, and the platform figure that is not the city. The Decision Book's Chapter 8 — ISO 8601, boundary vintage, codes not names, disclosure before design, secondary suppression, the ~60% floor, the provenance set — is a correct reading of the GOV.UK, GSS and Analysis Function standards it cites, and its line that this layer "has almost no creative latitude, and that is a feature" is the right stance.

> [Ch 4 · L865 · Conflicts] **Conflicts.** Two in the Decision Book, logged in Looking back: the gap rule's "dashed" and the provenance set's two omissions. One in the design system, and it is small: the status-chip vocabulary (as far as this chapter has seen it) carries the *tier* of a claim — Fixed, Adaptable, Decorative — and the *status* of a figure (provisional, estimated, suppressed), but not the *kind of nothing* in an empty cell. A chip set for the six (or seven) kinds would be the design system's part of truth 2. `[Counterbalance → design system]`

> [Ch 4 · L867 · Silent on] **Silent on.** Everything in sections 3, 4, 8, 9 and 10: the unit of observation; the day boundary; the denominator; concentration beside totals; the reading of platform feeds; outlier procedure. These are not visual rules and may not belong in a style guide; they belong in the data contract and in the Decision Book's data chapters, and this chapter's rules table is the candidate list.

**Chapter 5** (heading L657: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 5 · L659 · Agrees] **Agrees.** "Every big number carries a source line. A statistic without one is a claim, not a finding" is, for a composed number, the card. "Illustrative or placeholder figures say so, in the chart, every time" covers a score published before its method is adopted: it is illustrative and must say so. "Every comparison between places declares whether the comparability gate was cleared" extends to a comparison of composite scores, which must additionally clear the aggregation gate — same recipe, same price list. "Strong design must never make weak evidence look stronger than it is" is, here, the rank shown without its interval and the score shown to two decimal places.

> [Ch 5 · L661 · Conflicts] **Conflicts.** None direct. One tension: the design system's status chips and the Decision Book's tiers mark a claim's firmness, but neither has a component for the firmness of a *composed* number — the width of its rank interval, the gap between its nominal and effective weights. A "robustness" mark for a score, kin to the provenance code, would be the design system's part of truths 2 and 4. `[Counterbalance → design system]`

> [Ch 5 · L663 · Silent on] **Silent on.** Everything in sections 3 to 9 and 12: the ten steps, weights, aggregation, sensitivity, the audit, validity, recognition and the card. The Decision Book's data chapters stop at the chart and the table; the composite between the data and the chart has no chapter. This chapter's rules table is the candidate.

**Chapter 6** (heading L778: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 6 · L780 · Agrees] **Agrees.** "Every big number carries a source line. A statistic without one is a claim, not a finding" extends here to a claim record: a value figure without its gross-or-net line, its rung and its small-number treatment is a claim. "Strong design must never make weak evidence look stronger than it is" is, in this chapter, the trend arrow on a modelled figure, the "significant" badge on a forked comparison, the alert without its false-alarm rate, and the rung-three verb on rung-one evidence. "Every comparison between places declares whether the comparability gate was cleared" now has a small-numbers clause: places of different sizes cannot be compared by raw rate without the interval. The Decision Book's tone example in Chapter 5 — the drop-in that cannot yet be said to have caused the fall — is this chapter's contribution sentence, already in the house voice; its Chapter 10 rule that every arrow is a claim about causation is Pearl's prohibition; its disclosure rules in Chapters 8 and 15 are the confidentiality half of the two reasons, and its Chapter 15 practice (a range below a base of 30, suppression below the disclosure threshold) operates the two reasons without naming them.

> [Ch 6 · L782 · Conflicts] **Conflicts.** None direct. Two tensions. The design system's status chips mark a claim's firmness and the Decision Book's tiers mark a rule's; neither has a component for the *kind* of claim — observed, gross, net, contributed, caused, modelled, borrowed — which is what the claim record carries, and which a reader needs before firmness means anything. And the Decision Book's Chapter 15 treats a misleading filter combination one at a time ("suppress it or annotate it"); this chapter's garden treats the filter set as a whole, so that the rule about any one view depends on how many views there are. `[Counterbalance → design system; Decision Book Ch 15]`

> [Ch 6 · L784 · Silent on] **Silent on.** Sections 7 to 11 almost entirely: the gross-to-net arithmetic; rent against product; distributional weights; the rungs and the verb; leading indicators; the exploratory status of a view, multiple comparisons and error control; models' known wrongness and validation dates; control charts, common and special cause, alert policy and seasonal baselines; shrinkage and modelled small-area figures; the precision reason for withholding; the scene's knowability as the identifying threshold. The Decision Book's data chapters govern the chart and the table and stop before the claim; this chapter's rules table is the candidate for the chapter between them.

**Chapter 7** (heading L702: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 7 · L704 · Agrees] **Agrees.** Style Guide §12 — "Every chart comparing two or more places must state whether the indicator comparability gate has been cleared… A comparison without this note is not publishable" — is this chapter's first truth, and the comparison record is the gate's content extended from the indicator to the places, the chooser, the season and the design. "Strong design must never make weak evidence look stronger than it is" is, here, the sorted bar chart of places with no interval, the smoothed line reaching its last point, the single projected figure, and the before/after marker with no rivals listed. "Every big number carries a source line" extends to every year-on-year figure carrying its base month. The Decision Book's interval rule (Ch 6), vintage rule (Ch 8), arrow rule (Ch 10), small-base filter rule (Ch 15) and "does the causal chain hold" (Ch 16) all agree with this chapter and are extended by it.

> [Ch 7 · L706 · Conflicts] **Conflicts.** None direct. Two tensions. The Decision Book draws on the Analysis Function's chart standard, which sorts bars by value; this chapter's ranking rule forbids a sorted display of places unless the sort is visibly a reading aid and the finding is position against limits — the design system needs a form for position against limits, or a rule for when a sorted bar is and is not a league table. And the design system's status chips mark a claim's firmness without a place for the comparison's terms — who chose the peers, what was held equal, which rung — which the comparison record carries and which a reader needs before a comparison's firmness means anything. `[Counterbalance → design system; Decision Book Ch 6]`

> [Ch 7 · L708 · Silent on] **Silent on.** Sections 3 to 10 almost entirely: rankings as such; standardisation and expected values; peer methods and self-selection; partial orders; the funnel; trend windows, end-points, seasonal adjustment and its revision, base effects, index bases, real terms; regression to the mean; the eight rivals; interrupted series, difference-in-differences, synthetic control, cut-offs, matching, placebos; spillover and displacement as an evaluation problem; power; the ladders; optimism bias, switching values, ranges, scenarios, the projection label and the record against outturn; nowcasts, leading indicators, concentration thresholds and survivorship. The Decision Book's data chapters govern the chart and the table and stop before the comparison; this chapter's rules table is the candidate for the chapter between them.

**Chapter 8** (heading L894: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 8 · L896 · Agrees] **Agrees.** The provenance code on every chart — "reference period, geography and boundary vintage" — is the geography half of this chapter's line 7 and the period half of line 1. DTA-05 and DTA-06 are the boundary rules as stated. BRF-15 ("Put version and date on the face of anything that will be superseded") and BRK-18 (name the version) are truth 1 in the house's own words, and the running foot already carries "v1.5 · date" for the document. DSH-13 (choose tooling against the requirements at the start) is the budget rule. DSH-15 (gaps render as gaps in every state) and DSH-03/DSH-18 (the default view answers unaided; explanation beside, not in a tooltip) are what this chapter needs to survive without script. The seven tests' "Phone" and "Screen-reader" lines are section 9 and the twin.

> [Ch 8 · L898 · Conflicts] **Conflicts.** One direct. DSH-21 classes "empty and error states" as Decorative, "free within the rules above"; this chapter holds that the degraded state — the last good copy kept, its age in words, which series is missing and since when — is a Fixed procedure (AWS REL05-BP01; RFC 5861; the SRE workbook), and that a tile which blanks on a failed fetch is a defect and not a style. The rule register needs the state split: how the degraded tile *looks* is Decorative; *that* it shows the last good copy with its age is Fixed. Two tensions. The design system's recognisable face is a styled vector map, and this chapter prices that at over two-fifths of the script budget of the seventy-fifth-percentile phone before a tile arrives; whether the face is worth the budget is a creative decision, but the system needs a raster or static fallback state and a twin-table component before the decision can be made with its cost visible. And the design system has no component for the four-part freshness statement (period, published, revised, frequency) and no running-foot slot for the data's date as distinct from the document's; the chapter asks for both and leaves their form to the designers. **Logged for the design system:** a freshness component; a degraded-tile state; a map component with twin, buttons, attribution and supplier-logo slots; a stated byte budget and baseline device; a script-free rendering requirement. **Logged for the Decision Book:** a chapter on running a dashboard — freshness, dependencies and terms, refresh, watch and alarm, objective and degraded mode, budget, tile supply, retirement, owner — or an extension of Chapter 15 that carries them.

**Chapter 9** (heading L854: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 9 · L856 · Agrees] **Agrees.** Provenance on every chart applies to a felt panel as to a counted one, and the measure record is its felt-data extension. DSH-15 and DSH-16 — gaps render as gaps; carry uncertainty through filtering or suppress below a base threshold — are the official floor and the silence cell. DSH-12's "Observed, task-based testing with real users" and the Style Guide's seven tests ("Dancefloor"; "Partner"; "Screen-reader") are the symmetry test of this chapter applied to a surface. BRF-04's three axes — "affected, influential, exposed" — are the selection question in the Decision Book's words.

> [Ch 9 · L858 · Conflicts] **Conflicts.** None direct. Three gaps that will become conflicts if unaddressed. The design system's chart components are built for counted series; a felt measure is a distribution with bands whose cut-points were chosen by a stated method, and the system needs a component that shows the spread, the bands, the n and the selection together, or a felt result will be drawn as a bar and read as a verdict. The Decision Book's data chapter treats provenance as source, period, geography and method; a felt measure's provenance is also *who was asked, who answered and who was not*, and the provenance set needs those lines or the measure record must sit beside it. And the Decision Book's "every chart carries a provenance code" has no status for *indicator, unvalidated here* — the right label for every trace or signal shown before it has been checked against a descriptor — and without it the system will either hide the trace or show it as the thing. **Logged for the design system:** a felt-distribution component (spread, bands, n, selection); a discordance/convergence matrix; a "what this changed" element; an attribution form for testimony in the respondent's own voice; an "unvalidated indicator" status. **Logged for the Decision Book:** a chapter on felt data — register, construct before item, distribution not point, sample on the face, the five sources, member checking as procedure, the integration protocol and discordance cell, "what this changed", the co-presence and trace cautions, the emotion-inference boundary — or an extension of the Decision Book's Chapter 8 that carries them.

**Chapter 10** (heading L1066: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 10 · L1068 · Agrees] **Agrees.** Suppression with secondary suppression (Decision Book Chapter 8) is this chapter's rule for static views. DSH-15 ("Gaps render as gaps in every filter state") and DSH-16 ("Carry uncertainty through filtering, or suppress below a base threshold") are the disclosure floor and the precision floor stated for every view; this chapter adds that the floor for an interactive view is higher than for a table. COL-17's text-coded status chips are the right furniture for *withheld*, *unmeasured* and *held*. BRF-04's "affected, influential, exposed" are the three names in the record's lines 7 and 8. The seven tests' "Dancefloor — retains cultural truth, avoids institutionalising the culture?" and "Partner — does the language make room for collaboration and recognise others' contribution?" are section 12 applied to a surface.

> [Ch 10 · L1070 · Conflicts] **Conflicts.** One direct. Version 1 and the Decision Book require a withheld cell to say *why*; the national office's practice, for a stated reason, is to say neither the rule nor the parameter, and this chapter narrows the house rule to the *kind* of reason — disclosure floor, precision floor, held — with the rule and parameter optional. The Decision Book's text should carry that narrowing, or state that the house publishes its parameters as policy and accepts the office's stated risk. Three gaps that will become conflicts if unaddressed. The Decision Book treats the identifying threshold as one number; an interactive dashboard needs one per view, higher than a table's, and a procedure for setting it against the scene's knowability. The Decision Book's disclosure chapter protects tables and has no rule for a filter as a query system — fixed classifications, a cap on combinations, a limit on overlapping views, a log, the walk — so the prototype would ship a table builder protected as a table. And neither the Decision Book nor the design system has the held layer as a status with a decider, a resolution, a reason and a review date, so a held room would be drawn as empty or not drawn. **Logged for the design system:** a held-status component, distinguishable from withheld and unmeasured, with its reason reachable; a three-nothings pattern for one face; a safeguards-record panel; a withdrawal notice at the point of contribution; a stigma check in the colour rules (no red or dark for low; no large empty areas dominating). **Logged for the Decision Book:** a chapter on safeguards — the record's fourteen lines as rules; the floor per view; the query-time controls; the walk; lawful basis before the first row; the DPIA's consultation step and publication; consult, govern, agree; the held status; withdrawal tiers; the three-column harm assessment; the Online Safety Act decision; the site's own analytics; the twelve-month question — or an extension of Chapters 8 and 15 that carries them.

**Chapter 11** (heading L768: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 11 · L770 · Agrees] **Agrees.** The Decision Book's Chapter 7 rule — a departure names what it buys — is this chapter's interaction procedure, now with the seven costs on the other side of the ledger. Its Chapter 15 rules on tooltips and misleading filter combinations hold and are given their standards (1.4.13; Chapter 10's query-time machinery). The design system's text-coded status chips (COL-17) are the right form for the records' kinds on the face. DSH-12 (observed, task-based testing with real users) is the two-readers and three-phones test. DSH-15 and DSH-16 are section 8's rules for gaps and uncertainty through filtering.

> [Ch 11 · L772 · Conflicts] **Conflicts.** One direct, carried from Chapter 8: DSH-21 treats error states as Decorative, and this chapter finds a degraded state is a state — a data version with an age — that belongs in the face sheet's line 8 and on the face with its stamp. Four gaps that will become conflicts if unaddressed. The Decision Book treats a view's address as a stable link; this chapter finds a link is not a citation and that a dated snapshot and a generated citation are needed, so the prototype's share button, as the Decision Book would have it, would produce citations that drift. The design system's map component has no rule that breaks are held constant across filter states, so two views of one series will be drawn on different legends and read as different. Neither document says what a generated sentence is labelled as, so a templated district sentence would read as written. And neither names the small screen as the first version, so the phone will receive what is left after the desktop is designed, which the corpus evidence says is the message's remainder. **Logged for the design system:** a snapshot banner (archive date; previous, next, live); a generated-citation block; a generated-text label; a small-area inset or tile-map pattern with the legend held; a "how this argues" link in the furniture; a status chip that opens its record; the degraded-state stamp. **Logged for the Decision Book:** a chapter on the surface — the sentence first and per place; the landing pattern as a declared endorsement; the small screen first; the authored account beside the open door with linking; the purchase table with costs; hover, pointer and target rules; one address per state; snapshot and citation; records' kinds on the face and followable; the three nothings; map rates, breaks and the stigma check; the two-readers and three-phones tests; own-use measured as how, not who; the retirement plan — or an extension of Chapters 7 and 15 that carries them.

**Chapter 12** (heading L716: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 12 · L718 · Agrees] **Agrees.** The comparability flag (charts) is this chapter's gate on the face, and is now a quality dimension with official cousins. The voice rule against "Defining people or places only through failure or need" is the label rule's test. The slide test "Does it paint a recognisable picture? … Record who is missing and what contributors change" is the review procedure, now with a record. The recommendation-strength meter "as filled ordinal steps in ink, never a colour scale" is the same discipline this chapter applies to the two columns. The Decision Book's DAT-18, DAT-21 and TBL-17 are the crop rule's spine; LAY-08 is equal dignity's ground; the geography rules (boundary vintage; stated lookup) are the unit rule's.

> [Ch 12 · L720 · Conflicts] **Conflicts.** One, direct. ARG-12, "Never repeat the opposing frame in order to deny it", tier Fixed, reason "Repetition reinforces it" (Decision Book Chapter 16): the reason no longer holds against the corrections literature, and the competitive-framing evidence says strength decides, not count. The chapter proposes the rule be re-based (value-first as a declared endorsement; no needless repetition) or retired; logged for the Decision Book, not changed here.

> [Ch 12 · L722 · Silent on] **Silent on.** A unit declaration on figures about places; a core-and-bands form for vague places; a reader-drawn unit; the identity/conditions split as a layout boundary and a data-contract field; a fixed-order profile component and a bar on filled radars; a label-writing rule and per-place hedge; in-frame provenance for charts (title, unit, source, base, gate, snapshot) against the design system's own preference for text outside images; matching and the display of weights; a review-and-errors footer; the recognition record. All logged for the design-system conversation.

**Chapter 13** (heading L599: `## Design system (Style Guide v1.5) and Decision Book — conflict log`)

> [Ch 13 · L601 · Agrees] **Agrees.** §13's floor is this chapter's rules table with the criteria beside each item; §02's hierarchy ("accessibility outranks brand") is confirmed by the narrowness of the W3C's "essential" exception; §04's register is COGA's clear-words pattern and gains its measurable form; the Decision Book's Chapter 15 ("nothing load-bearing in a tooltip"; "a non-interactive route to the same finding"; observed testing with real users) is 1.4.13, the written account and the Design System's own sentence. The design system's text-outside-images preference stands for the page; Chapter 12's frame meets 1.4.5 under the condition now stated.

> [Ch 13 · L603 · Conflicts] **Conflicts.** None found. One tension logged: the type scale's body size against the 18-point finding and the BDA's 12–14; the design system decides and records why.

> [Ch 13 · L605 · Silent on] **Silent on.** A status region and its wording; a reduced-motion variant for every animated component; a table-twin pattern with pagination and header cells; a long-description block in body text; a pause control for auto-updating panels; focus styling that is never obscured by the filter bar; an accessibility statement template with the twelve lines; the screen readers and platforms the house tests with. All logged for the design-system conversation.

*35 paragraphs in Chapters 1–13.*

### 6.2 Chapters 14–15 — the tables, as printed

| Ch | # | L | Item | Where | What this chapter found | Status |
|---|---|---|---|---|---|---|
| 14 | 1 | 726 | Style Guide §06, "Strong design must never make weak evidence look stronger than it is" | §4, §11 | Stands; needs two companions — timid design never makes strong evidence look weaker (version 1), and plain design never stands in for a record (this chapter, from Kennedy et al.) | Candidate addition: *the three-sentence evidence standard* |
| 14 | 2 | 727 | Decision Book Ch 18 tier test (Fixed / Adaptable / Decorative) | §3, §6 | Fixed = expressiveness, Adaptable = effectiveness, Decorative = what neither sees; a fourth category exists in the W3C ("specific sensory experience") with an identification duty | Candidate addition; no conflict |
| 14 | 3 | 728 | Decision Book Ch 18, BRK-07 "Run the removal test for the relevant chapter" | §6 | Formalised: four removals and a fifth check; a ten-line register | Candidate: *the boundary log* as the removal test's log |
| 14 | 4 | 729 | Decision Book Ch 7, "Name the purchase. Show the precise version that ships alongside." | §5, §10 | "Alongside" is not enough (Ottley): one step away, finding in words on the form; purchase bounded to what is measured | Candidate amendment |
| 14 | 5 | 730 | Decision Book Ch 7, "Beauty as an accessibility exemption. The most common failure in award-winning work." | §7 | Confirmed institutionally: the prize's eight criteria omit accuracy | No conflict; cite |
| 14 | 6 | 731 | Decision Book Ch 18, "Treat 'it looks better' as a reason. It is a valid reason in the Decorative tier and nowhere else." | §12 | Stands; the Decorative tier is unshrunk by this chapter | No conflict |
| 14 | 7 | 732 | Decision Book colour.md: Decorative grounds carry "no contrast requirement beyond any text sitting on it" | §5 | Text on a dark ground has a measured legibility cost beyond contrast; a light alternative is required | Candidate amendment: polarity choice |
| 14 | 8 | 733 | Version 1 Ch 13 rule, genre Fixed | §10 | Re-tiered Adaptable | Carried to Chapter 16's register |
| 14 | 9 | 734 | Version 1 Ch 13 rule, five/ten words Fixed | §10 | Re-tiered Adaptable; distance and seconds Fixed beneath it | Carried to Chapter 16's register |
| 14 | 10 | 735 | Version 1 Ch 13, "the human figure as a mark" in the expressive palette | §5, §10 | May serve recognition; may not be priced as empathy or giving; whole units | Candidate amendment |
| 14 | 11 | 736 | Decision Book ARG-12 (from Chapter 12's log) | — | Unchanged by this chapter; still in direct conflict | Awaiting Carly |
| 14 | 12 | 737 | Style Guide §06 "Generous… Defining people or places only through failure or need" | §7 (Dollar Street) | A street ordered by income is the thing the rule forbids for places; the method is imported, the ranking is not | No conflict; cite |
| 15 | 1 | 690 | Decision Book Ch 8 (service record): release and maintenance rules | §3, §4, §7 | Sector precedents at every line: release calendar with status, fixed time, log for surprises, retirement plan; the regulator lists the plan among the minimum | Candidate additions: *the retirement plan*; *vintages from the first release* |
| 15 | 2 | 691 | Decision Book Ch 5 / recipe card | §3, §5 | The metric page template and the 32-field record are the recipe card's sector forms; the ELS's twelve-item metadata list is the minimum | Candidate: adopt the field list |
| 15 | 3 | 692 | Decision Book Ch 7 / comparison record; Ch 12 identity line | §5 | The paired "can and cannot say" text; the refusal to aggregate with reason; County Health Rankings' groups | Candidate: *the usage text* as a required block beside any ordering |
| 15 | 4 | 693 | Decision Book DAT rules on colour and status chips | §3, §4 | Colour only for significance, amber default, blue ramp, the one-in-twenty sentence; [p] [r] [f] in square brackets not symbols | Candidate amendment; check against the design system's status-chip component |
| 15 | 5 | 694 | This book's own dagger (†) convention | §4 | The Analysis Function advises against '†' because screen readers find it hard; the book uses it in prose, not tables | Carried to Chapter 16: whether the book's own marks meet the floor |
| 15 | 6 | 695 | Style Guide §06 evidence standard: "Record uncertainty, missing data, disagreement and methodological judgement" | §4 | Ranges beside points, never hedges alone; the Health Index's count of unmeasurable change | No conflict; cite |
| 15 | 7 | 696 | Decision Book Ch 18 override log; Ch 14 boundary log | §12 | A third growing list, the precedent record | Chapter 16: whether three logs are one |
| 15 | 8 | 697 | Decision Book Ch 15 (dashboards): trust and use | §3, §8 | Trust measured as producers do or not at all; use measured only by asking | Candidate: *the two measurement rules* |
| 15 | 9 | 698 | BRIEF-v2 §6 fold note | §11 | A count: about forty mechanisms, about six already in the book | Awaiting Carly |
| 15 | 10 | 699 | ARG-12 (from Chapter 12) | — | Unchanged | Awaiting Carly |

*22 rows (12 + 10).* Status wordings, as printed: "No conflict; cite" ×3; "Awaiting Carly" ×3; "Candidate amendment" ×2; "Carried to Chapter 16's register" ×2; "Candidate addition: *the three-sentence evidence standard*" ×1; "Candidate addition; no conflict" ×1; "Candidate: *the boundary log* as the removal test's log" ×1; "No conflict" ×1; "Candidate amendment: polarity choice" ×1; "Candidate additions: *the retirement plan*; *vintages from the first release*" ×1; "Candidate: adopt the field list" ×1; "Candidate: *the usage text* as a required block beside any ordering" ×1; "Candidate amendment; check against the design system's status-chip component" ×1; "Carried to Chapter 16: whether the book's own marks meet the floor" ×1; "Chapter 16: whether three logs are one" ×1; "Candidate: *the two measurement rules*" ×1.

The last line of each of these two logs is "*End of Chapter 14, draft 2.*" (ch14 L739) and "*End of Chapter 15, draft 2.*" (ch15 L701).

**Total: 35 paragraphs + 22 table rows = 57 rows in fifteen logs.**

### 6.3 What is still open — de-duplicated across chapters

"Open" here means the log's own words say so: *direct conflict*, *possible*, *tension*, *will become conflicts if unaddressed*, *candidate*, *carried to Chapter 16*, *awaiting*. Nothing below has been resolved in any later chapter's log; where a later chapter mentions the item again it says "unchanged" or "carried". The wording in quotation marks is the log's. Related gap-table rows (Part 5) are cited as G-Ch.#.

**A. Direct conflicts — the log uses the word "direct", or names a conflict in the Decision Book (5 items).**

- **A1** Decision Book **ARG-12**, "Never repeat the opposing frame in order to deny it", tier Fixed. Raised: Ch 12 ("One, direct… the reason no longer holds against the corrections literature… The chapter proposes the rule be re-based… or retired; logged for the Decision Book, not changed here"); Ch 14 row 11 ("Unchanged by this chapter; still in direct conflict" — Status "Awaiting Carly"); Ch 15 row 10 ("Unchanged" — "Awaiting Carly"). Rule 12.9 is the book's side of it.
- **A2** Decision Book **DSH-21**, "empty and error states" classed Decorative, against the degraded state as a Fixed procedure. Raised: Ch 8 ("One direct… The rule register needs the state split: how the degraded tile *looks* is Decorative; *that* it shows the last good copy with its age is Fixed"); Ch 11 ("One direct, carried from Chapter 8"). G-8.11, G-11.15. Rules 8.13, 11.27.
- **A3** A withheld cell must say *why* (version 1 and the Decision Book) against the national office's practice of stating neither rule nor parameter. Raised: Ch 10 ("One direct… this chapter narrows the house rule to the *kind* of reason… The Decision Book's text should carry that narrowing, or state that the house publishes its parameters as policy and accepts the office's stated risk"). G-10.14.
- **A4** The Decision Book's gap rule "dashed, hatched, or broken" (DAT-14) against "never join, dotted or dashed". Raised: Ch 4 ("Two in the Decision Book, logged in Looking back: the gap rule's "dashed" and the provenance set's two omissions"). G-4.1 (Red). Rule 4.16.
- **A5** The Decision Book's provenance set (DTA-19) omits the responsible party and the issued/modified dates. Raised: Ch 4 (same sentence). G-4.2. Rule 4.7. Extended in Ch 9: "the provenance set needs those lines [who was asked, who answered and who was not] or the measure record must sit beside it".

**B. Possible conflicts, tensions, and "gaps that will become conflicts if unaddressed" (15 items).**

- **B1** The guide's joy-first register against the plain view for the reader who arrives opposed; where on a dashboard the joy goes. Raised: Ch 2 ("One possible… Logged for Carly; the design system may want a line on it"); Ch 3 ("One, inherited from Chapter 2 and sharpened… the guide may want a line that says where on a dashboard the joy goes: words, hierarchy, register, imagery around the chart; never the mark, the axis or the colour that carries a value").
- **B2** The status chips carry a tier and a status but have no component for what six chapters each need them to say. Raised: Ch 4 — the *kind of nothing* in an empty cell ("One in the design system, and it is small"); Ch 5 — the firmness of a *composed* number, a "robustness" mark ("One tension"); Ch 6 — the *kind* of claim; Ch 7 — the comparison's terms; Ch 9 — a status for "*indicator, unvalidated here*"; Ch 10 — a held status "distinguishable from withheld and unmeasured". Also G-0.1 (no kind-of-claim mark) and Ch 11's "a status chip that opens its record".
- **B3** The Decision Book's Chapter 15 treats a misleading filter combination one at a time; the filter set as a whole / the filter as a query system has no rule. Raised: Ch 6 (second tension: "this chapter's garden treats the filter set as a whole"); Ch 10 ("has no rule for a filter as a query system… so the prototype would ship a table builder protected as a table").
- **B4** The Analysis Function's "sort bars by value" (through the Decision Book) against the ranking rule; a form for position against limits is missing. Raised: Ch 7 (first tension). G-7.5.
- **B5** The styled vector map against the script budget; no raster or static fallback state and no twin-table component. Raised: Ch 8 (first tension: "whether the face is worth the budget is a creative decision, but the system needs a raster or static fallback state and a twin-table component before the decision can be made with its cost visible").
- **B6** No component for the four-part freshness statement; no running-foot slot for the data's date as distinct from the document's. Raised: Ch 8 (second tension). G-8.13.
- **B7** Chart components are built for counted series; no felt-distribution component (spread, bands, n, selection). Raised: Ch 9 (first of "Three gaps that will become conflicts if unaddressed"). G-9.13.
- **B8** The Decision Book's provenance has no lines for who was asked, who answered and who was not. Raised: Ch 9 (second gap). See A5.
- **B9** The identifying threshold is one number in the Decision Book; an interactive dashboard needs one per view. Raised: Ch 10 (first of "Three gaps that will become conflicts if unaddressed"). G-10.14; rules 6.42, 10.5.
- **B10** Neither document has the held layer as a status with a decider, a resolution, a reason and a review date. Raised: Ch 10 (third gap). G-10.16.
- **B11** The Decision Book treats a view's address as a stable link; a link is not a citation — a dated snapshot and a generated citation are needed. Raised: Ch 11 (first of "Four gaps that will become conflicts if unaddressed"). G-11.11.
- **B12** The design system's map component has no rule that breaks are held constant across filter states. Raised: Ch 11 (second gap). G-11.12 (the default breaks are Jenks; the one controlled experiment favours quantiles).
- **B13** Neither document says what a generated sentence is labelled as. Raised: Ch 11 (third gap).
- **B14** Neither document names the small screen as the first version. Raised: Ch 11 (fourth gap).
- **B15** The type scale's body size against the 18-point finding and the BDA's 12–14. Raised: Ch 13 ("Conflicts. None found. One tension logged… the design system decides and records why").

**C. Candidates — a status that begins "Candidate" (11 rows, 12 items; Chapters 14 and 15 only, because only they print a status).**

- **C · Ch 14 row 1** — Style Guide §06, "Strong design must never make weak evidence look stronger than it is" → "Stands; needs two companions — timid design never makes strong evidence look weaker (version 1), and plain design never stands in for a record (this chapter, from Kennedy et al.)" — Status: "Candidate addition: *the three-sentence evidence standard*"
- **C · Ch 14 row 2** — Decision Book Ch 18 tier test (Fixed / Adaptable / Decorative) → "Fixed = expressiveness, Adaptable = effectiveness, Decorative = what neither sees; a fourth category exists in the W3C ("specific sensory experience") with an identification duty" — Status: "Candidate addition; no conflict"
- **C · Ch 14 row 3** — Decision Book Ch 18, BRK-07 "Run the removal test for the relevant chapter" → "Formalised: four removals and a fifth check; a ten-line register" — Status: "Candidate: *the boundary log* as the removal test's log"
- **C · Ch 14 row 4** — Decision Book Ch 7, "Name the purchase. Show the precise version that ships alongside." → ""Alongside" is not enough (Ottley): one step away, finding in words on the form; purchase bounded to what is measured" — Status: "Candidate amendment"
- **C · Ch 14 row 7** — Decision Book colour.md: Decorative grounds carry "no contrast requirement beyond any text sitting on it" → "Text on a dark ground has a measured legibility cost beyond contrast; a light alternative is required" — Status: "Candidate amendment: polarity choice"
- **C · Ch 14 row 10** — Version 1 Ch 13, "the human figure as a mark" in the expressive palette → "May serve recognition; may not be priced as empathy or giving; whole units" — Status: "Candidate amendment"
- **C · Ch 15 row 1** — Decision Book Ch 8 (service record): release and maintenance rules → "Sector precedents at every line: release calendar with status, fixed time, log for surprises, retirement plan; the regulator lists the plan among the minimum" — Status: "Candidate additions: *the retirement plan*; *vintages from the first release*"
- **C · Ch 15 row 2** — Decision Book Ch 5 / recipe card → "The metric page template and the 32-field record are the recipe card's sector forms; the ELS's twelve-item metadata list is the minimum" — Status: "Candidate: adopt the field list"
- **C · Ch 15 row 3** — Decision Book Ch 7 / comparison record; Ch 12 identity line → "The paired "can and cannot say" text; the refusal to aggregate with reason; County Health Rankings' groups" — Status: "Candidate: *the usage text* as a required block beside any ordering"
- **C · Ch 15 row 4** — Decision Book DAT rules on colour and status chips → "Colour only for significance, amber default, blue ramp, the one-in-twenty sentence; [p] [r] [f] in square brackets not symbols" — Status: "Candidate amendment; check against the design system's status-chip component"
- **C · Ch 15 row 8** — Decision Book Ch 15 (dashboards): trust and use → "Trust measured as producers do or not at all; use measured only by asking" — Status: "Candidate: *the two measurement rules*"

**D. Carried to Chapter 16 by the log itself (4 rows).**

- **D · Ch 14 row 8** — Version 1 Ch 13 rule, genre Fixed → "Re-tiered Adaptable" — Status: "Carried to Chapter 16's register"
- **D · Ch 14 row 9** — Version 1 Ch 13 rule, five/ten words Fixed → "Re-tiered Adaptable; distance and seconds Fixed beneath it" — Status: "Carried to Chapter 16's register"
- **D · Ch 15 row 5** — This book's own dagger (†) convention → "The Analysis Function advises against '†' because screen readers find it hard; the book uses it in prose, not tables" — Status: "Carried to Chapter 16: whether the book's own marks meet the floor"
- **D · Ch 15 row 7** — Decision Book Ch 18 override log; Ch 14 boundary log → "A third growing list, the precedent record" — Status: "Chapter 16: whether three logs are one"

**E. Awaiting Carly (3 rows, 2 distinct items).**

- **E · Ch 14 row 11** — Decision Book ARG-12 (from Chapter 12's log) → "Unchanged by this chapter; still in direct conflict" — Status: "Awaiting Carly"
- **E · Ch 15 row 9** — BRIEF-v2 §6 fold note → "A count: about forty mechanisms, about six already in the book" — Status: "Awaiting Carly"
- **E · Ch 15 row 10** — ARG-12 (from Chapter 12) → "Unchanged" — Status: "Awaiting Carly"

ARG-12 is the same item as A1 (raised in Chapters 12, 14 and 15). The fold note is new in Chapter 15.

**F. The "Silent on" and "Logged for" lists — candidates in the chapters' own phrase, not de-duplicated item by item (they are quoted in full in 6.1).**

| Ch | What the log lists | The log's closing phrase |
|---|---|---|
| Ch 1 | 3 items (the conduct of release; the unit of aggregation as a declared choice; the measurement of use) | "All three are candidates for the design system's dashboard section when it exists." |
| Ch 2 | 5 items (the monitoring/evaluation label; the evidence-ladder level; the display of valuation caveats; the recognition sequence; the plain-table route) | "All candidates for the design system's dashboard section when it exists." |
| Ch 3 | 8 items (the title as the message-carrier; text on a chart; forms of uncertainty display; truncation; stock against flow; public defaults for scale and risk; interaction use rates and the no-hover phone; defaults as advice) | "All candidates for the design system's dashboard section when it exists." |
| Ch 4 | sections 3, 4, 8, 9 and 10 (unit of observation; day boundary; denominator; concentration beside totals; platform feeds; outlier procedure) | "they belong in the data contract and in the Decision Book's data chapters, and this chapter's rules table is the candidate list." |
| Ch 5 | sections 3 to 9 and 12 (the ten steps, weights, aggregation, sensitivity, the audit, validity, recognition and the card) | "the composite between the data and the chart has no chapter. This chapter's rules table is the candidate." |
| Ch 6 | sections 7 to 11 "almost entirely" | "this chapter's rules table is the candidate for the chapter between them." |
| Ch 7 | sections 3 to 10 "almost entirely" | "this chapter's rules table is the candidate for the chapter between them." |
| Ch 8 | Logged for the design system: 5 items; logged for the Decision Book: "a chapter on running a dashboard… or an extension of Chapter 15" |  |
| Ch 9 | Logged for the design system: 5 items; logged for the Decision Book: "a chapter on felt data… or an extension of the Decision Book's Chapter 8" |  |
| Ch 10 | Logged for the design system: 5 items; logged for the Decision Book: "a chapter on safeguards… or an extension of Chapters 8 and 15" |  |
| Ch 11 | Logged for the design system: 7 items; logged for the Decision Book: "a chapter on the surface… or an extension of Chapters 7 and 15" |  |
| Ch 12 | 10 items (from "A unit declaration on figures about places" to "the recognition record") | "All logged for the design-system conversation." |
| Ch 13 | 8 items (from "A status region and its wording" to "the screen readers and platforms the house tests with") | "All logged for the design-system conversation." |

Seven chapters in a row (5–11) each ask the Decision Book for a new chapter or an extension: on composites (5), on claims about value (6), on comparison (7), on running a dashboard (8), on felt data (9), on safeguards (10), on the surface (11). The same seven are the Red gap rows G-5.1, G-6.3, G-7.8, G-8.12, G-9.12, G-10.15, G-11.14.

**G. Not open.** Chapter 1 "**Conflicts.** None found."; Chapter 13 "**Conflicts.** None found." (with the one tension, B15); Chapters 5, 6, 7, 9 "None direct" (with the tensions above). In the tables: Ch 14 rows 5 and 12 and Ch 15 row 6 "No conflict; cite"; Ch 14 row 6 "No conflict".

**Count of open items, de-duplicated:** A 5 + B 15 + C 11 rows (12 items) + D 4 + E 1 new (the fold note; ARG-12 is A1) = **36 rows / 37 items**, plus the thirteen "silent on / logged for" lists in F.

---

## PART 7 — THE HOUSE'S MACHINERY AS PRINTED

Files, all under `/root/.claude/skills/synced/091ff5bc-68f1-4d60-99ca-b97be8d24434_c71f00e1-2463-4016-836c-443bd6e2824a/`: the Decision Book skill `design-decisions/SKILL.md` (240 lines) and its `references/` — `breaking-rules.md` (109 lines), `rule-register.md` (483), `gap-register.md` (436), `checklists.md` (379), plus `override-log-template.md` (15) and `found-a-gap.md` (103), which the first four point to; and the Style Guide skill's `nightlife-culture-design/references/voice.md`. Everything below is copied by line number; the number at the left of each code line is the line in the file.

### 7.1 The tier test — `design-decisions/SKILL.md`, section `## The tier test — run this first, on any disagreement` (L37–56), verbatim

````
  37  ## The tier test — run this first, on any disagreement
  38  
  39  Most arguments about "brand versus accessibility" are category errors. Establish the tier and
  40  the argument usually dissolves.
  41  
  42  | Tier | Status | Test | Breaking it is |
  43  |---|---|---|---|
  44  | **Fixed** | Uncertainty — there is a right answer | Pass or fail, measurable | Negligence |
  45  | **Adaptable** | Ambiguity — no single correct answer | Defensible or not, arguable | The job |
  46  | **Decorative** | Free | None | Expected |
  47  
  48  Fixed: contrast minimums, semantic structure, keyboard operability, disclosure thresholds,
  49  reading order, sourcing, real headings, alt text.
  50  Adaptable: type scale, grid, density, palette variants, annotation style, chart form within a task.
  51  Decorative: covers, pattern, illustration, pacing, campaign lines — **provided nothing that
  52  carries meaning lives there.**
  53  
  54  Treating an Adaptable decision as Fixed is deference. Treating a Fixed decision as Adaptable is
  55  negligence. Meaning drifting into the Decorative layer is the most common failure that looks
  56  like a creative choice.
````

The table alone, as a table (L42–46):

| Tier | Status | Test | Breaking it is |
|---|---|---|---|
| **Fixed** | Uncertainty — there is a right answer | Pass or fail, measurable | Negligence |
| **Adaptable** | Ambiguity — no single correct answer | Defensible or not, arguable | The job |
| **Decorative** | Free | None | Expected |

The decision stack that the tier test sits under (same file, L19–33), for reference:

````
  19  ## The decision stack
  20  
  21  Every decision resolves in this order. When two considerations compete, the higher one wins.
  22  
  23  ```
  24  1. legal and ethical requirements
  25  2. accessibility and user need
  26  3. factual and methodological integrity
  27  4. clarity and usability
  28  5. format conventions
  29  6. brand consistency
  30  7. stylistic preference
  31  ```
  32  
  33  **Accessibility does not dilute the brand. It decides where the brand should live.**
````

### 7.2 Chapter 18's `### Rules` table — `design-decisions/references/breaking-rules.md` L22–51, verbatim

The file's title and subtitle (L1, L3) and the chapter's decision line (L8, L10):

````
   1  # Breaking the rules well
   2  
   3  *The tier test, the taxonomy of deviation, the removal tests, the override log.*
   4  
   5  
   6  ---
   7  
   8  ## Chapter 18 — Breaking the rules well
   9  
  10  **The decision.** Is this a rule with a right answer, or a rule with a defensible range — and can you say what you are breaking it for?
````

| Rule | Why | Tier | Source |
|---|---|---|---|
| Establish the tier before arguing about a decision | Most brand-versus-accessibility arguments are category errors | **Fixed** | This book |
| Fixed rules are uncertainty; Adaptable rules are ambiguity | "Uncertainty implies there is something to be certain about" | **Fixed** | *Navigating Ambiguity* |
| Never let load-bearing meaning live in the decorative layer | The most common accessibility failure that looks like a creative choice | **Fixed** | Prior rule book |
| Name what the break buys: attention, retention, comprehension, context, register or fit | An unnamed break is a mistake made confidently | **Fixed** | Ch 7; this book |
| State the purpose in one sentence before defending a departure | Fuzzy values lose every argument to convention | Adaptable | *Drawing on Courage*; Ch 5 |
| Prototype the break before committing to it | "Close the gap between I wonder and I know" | Adaptable | *This Is a Prototype* |
| Run the removal test for the relevant chapter | Work that survives removal was built on structure | **Fixed** | This book |
| Log every override: trigger, rule, alternative, evidence | Turns an expedient decision into an earned one | **Fixed** | Prior rule book |
| Treat repeated small defensible departures as the route to a house style | "Stand up in small ways over and over again" | Adaptable | *Drawing on Courage* |
| Never negotiate a Fixed rule; relocate the brand instead | Accessibility decides where the brand lives, not whether it exists | **Fixed** | Prior rule book |
| State every value in the design system once; other mentions point to it | A value stated twice has already begun to diverge — measured: one guide carried 1.4–1.5 and 1.25–1.5 in a single section | **Fixed** | This chapter's review findings |
| Version and date the design system on its face, with a change list of decisions | A system with no version cannot be reviewed, because no reviewer can establish what they are reviewing | **Fixed** | Review findings; Ch 1 afterlife |
| Attach an interim rule to every known gap | A listed gap with no holding position is filled at 11pm by whoever has the file open | **Fixed** | A design system reviewed for this book, §15 |
| Give every rule in the system its tier | An untiered rule cannot be argued about productively; disagreement becomes authority rather than evidence | **Fixed** | Prior rule book; this book |
| State where the current version lives, in the system itself | Versioning without a location leaves a reviewer several candidates and no way to choose between them | **Fixed** | Review findings |
| Every artefact derived from the system states the source version it was built from | A skill, template, master or stylesheet embeds the system's values as a snapshot and cannot notice the source moved | **Fixed** | Measured: a brand skill four versions behind the guide it cited |
| A check compares each derived artefact to its source and fails on divergence | The defect is invisible by construction — the artefact is internally consistent while applying superseded rules | **Fixed** | This book's own build |
| A derived artefact never asserts its own settledness without naming its version | "Do not re-derive these rules" is correct when current, and suppresses the correction when stale | **Fixed** | Review findings |
| Render a decision rather than describing it, wherever it can be rendered | Prose asks the reader to rebuild the picture from words, then judge it; a written review is agreed with and not acted on | **Fixed** | This chapter |
| Build every demonstration with the mechanism it demonstrates | A mock-up of real-headings-versus-bold that fakes both has removed the only thing it shows | **Fixed** | This chapter |
| Show options side by side differing in one variable, and do not pre-select | Two variables at once makes the comparison unreadable; a recommendation turns a decision into an approval | **Fixed** | This chapter |
| Triage sheet before drill-down | Most decisions in a set resolve once they are next to each other; a stack of single decisions hides how many there are | Adaptable | This chapter |
| Quote the line every finding rests on, or mark the finding as inference | Findings drift from "the document says" to "you said" in three cheap steps; measured, it happened during this book's own review | **Fixed** | This chapter's review findings |
| Report an absence as a different class of claim from a quotation | "The guide does not state X" is much easier to get wrong than "the guide says X" | **Fixed** | This chapter's review findings |
| Log a gap in the system separately from a defect in the work, and close it in the source | A finding written into a review and not carried back will be found again | **Fixed** | This book's gap register |
| Treat a gap as closed only when a nameable rule exists that would have caught it | Anything less is an intention | **Fixed** | `build/check_gaps.py` |

*26 rows. Columns: `Rule | Why | Tier | Source` — four columns; there is **no Kind column** (this book's tables add one). Tiers: **Fixed** 22; Adaptable 4. No Decorative row.*

The same chapter's "In brief" (L14–20), which is where "deference" and "negligence" are defined:

````
  14  > The most useful distinction in this book was not written for designers. Stanford's *Navigating Ambiguity* separates two things people routinely confuse: **"Uncertainty implies that there is something to be certain about. An absolute truth or fact exists. With ambiguity there's no singular, correct answer."**
  15  >
  16  > That is the Fixed/Adaptable split, expressed better than this book has managed elsewhere. **Fixed rules are uncertainty** — 4.5:1 either passes or it does not, a heading is either marked up or it is not, a cell of two is either suppressed or it is a breach. **Adaptable rules are ambiguity** — there is no single correct type scale, grid, density or annotation style, and pretending otherwise is not rigour.
  17  >
  18  > Two symmetrical failures follow. Treating an Adaptable decision as if it were Fixed is **deference** — dressing a preference up as a standard so nobody has to defend it. Treating a Fixed decision as if it were Adaptable is **negligence**.
  19  >
  20  > And on why deference wins so often, *Drawing on Courage* is unusually precise: **"fear enlists its good friends reason and comfort."** The conventional choice always has an argument. That is exactly what makes it hard to see.
````

And its test (L77), the Decision Book's equivalent of this book's "What proves a break works":

````
  77  **What proves this chapter works.** Take any decision currently being argued about in a project. Name its tier. If it is Fixed, the argument is over and the brand relocates. If it is Adaptable, the argument is a design conversation and should be had properly rather than settled by seniority. If it is Decorative, there was never anything to argue about.
````

### 7.3 The override log — the four-line wording, as printed, and where

The exact wording asked about, "Trigger · rule and tier · alternative chosen · evidence", is printed once, at `design-decisions/SKILL.md` L87:

````
  87  **4. Log any override.** Trigger · rule and tier · alternative chosen · evidence. Four lines.
````

The other printings, each slightly different:

- `references/breaking-rules.md` L33 (Chapter 18 rule; `BRK-08` in the register) — four items, "rule" without "and tier", "alternative" without "chosen":
````
  33  | Log every override: trigger, rule, alternative, evidence | Turns an expedient decision into an earned one | **Fixed** | Prior rule book |
````
- `references/breaking-rules.md` L89–90 (Chapter 18 checklist) and, identically, `references/checklists.md` L361–362:
````
  89  - [ ] Override logged: trigger, rule and tier, alternative, evidence
  90  - [ ] The log lives with the project, not in someone's head
````
- `references/rule-register.md` L363:
````
 363  | `BRK-08` | Log every override: trigger, rule, alternative, evidence | Fixed | all | 18 | Turns an expedient decision into an earned one |
````
- `references/override-log-template.md`, the whole file (L1–15) — "Four lines per departure", but the table has **five** columns: Date, then the four:
````
   1  # Override log
   2  
   3  Four lines per departure. Keep it with the project, not in someone's head.
   4  Without it, a design system accumulates undocumented exceptions until nobody
   5  can tell which parts are rules and which are habits.
   6  
   7  | Date | Trigger | Rule and tier | Alternative chosen | Evidence |
   8  |---|---|---|---|---|
   9  | | what made the departure necessary | which rule, Fixed/Adaptable/Decorative | what you did instead | which test you ran, and what it showed |
  10  
  11  **Worked entry**
  12  
  13  | Date | Trigger | Rule and tier | Alternative chosen | Evidence |
  14  |---|---|---|---|---|
  15  | 2026-08-15 | 60pp of dense evaluation prose; pacing needed to sustain reading | All-caps display type — Adaptable at heading level; GOV.UK document guidance prefers sentence case | Caps retained for section openers only, applied via character format not typed. Sentence case for all H1/H2 in body. | Mono print check passed. Fonts-off check passed. Key statistic relocated out of the decorative field into body text. |
````

How this book prints it: Chapter 0 L157 — "- **The override log** — the four-line record kept whenever a rule is deliberately broken: trigger, rule and tier, alternative chosen, evidence. Chapter 16."; Chapter 14 L432 quotes the SKILL.md wording exactly ("Trigger · rule and tier · alternative chosen · evidence"); Chapters 2, 3, 4 and 5 give four different fields in their break tests — "(what rule, why, for whom, what proved it)".

### 7.4 The deviation taxonomy — "ignorant, lazy, expedient, earned"

Searched every file under `design-decisions/` (SKILL.md, the fifteen files in `references/`, and `scripts/`) for `ignorant`, `lazy`, `expedient`, `earned`. **The taxonomy is named but never set out.** `breaking-rules.md` L3 promises it in the subtitle — "*The tier test, the taxonomy of deviation, the removal tests, the override log.*" — and the only place the four words appear together is one checklist line, printed twice:

````
  88  - [ ] Deviation classified honestly: ignorant, lazy, expedient or earned
````
(identically at `references/checklists.md` L360.) There is no table, definition or paragraph for the four classes anywhere in the files read. The individual words occur as follows:

```
references/rule-register.md:280:| `LAY-11` | Establish the grid before breaking it, and break it rarely | Adaptable | all | 2 | A break is only legible against a system the reader has learned |
references/rule-register.md:363:| `BRK-08` | Log every override: trigger, rule, alternative, evidence | Fixed | all | 18 | Turns an expedient decision into an earned one |
references/rule-register.md:445:| `COL-05` | Functional colours — focus, error, success, link, visited — are not brand surfaces | Fixed | all | 4 | State signals are learned and safety-relevant |
references/layout-and-type.md:52:| Establish the grid before breaking it, and break it rarely | A break is only legible against a system the reader has learned | Adaptable | This book |
references/layout-and-type.md:69:*Breaking the grid to fit content.* This is the commonest break and it is never earned. It is a content problem presenting as a layout decision, and the correct response is to cut, split, or move to a different artefact — which is a Chapter 1 question, not a Chapter 2 one.
references/checklists.md:360:- [ ] Deviation classified honestly: ignorant, lazy, expedient or earned
references/colour.md:30:| Functional colours — focus, error, success, link, visited — are not brand surfaces | State signals are learned and safety-relevant | **Fixed** | Prior rule book; GOV.UK Design System |
references/breaking-rules.md:33:| Log every override: trigger, rule, alternative, evidence | Turns an expedient decision into an earned one | **Fixed** | Prior rule book |
references/breaking-rules.md:71:*The undocumented expedient decision.* Indistinguishable from negligence at the next audit, including to you.
references/breaking-rules.md:88:- [ ] Deviation classified honestly: ignorant, lazy, expedient or earned
references/choose-format.md:88:*Deliberately breaking mode separation — the two-layer artefact.* The rule says one artefact, one mode. The earned exception is a document explicitly built in two layers: sparse, presented-mode pages at the front, dense reference appendix behind, with a hard structural boundary between them and navigation that makes the boundary obvious. This works. What does not work is the *unmarke…
```

So: "expedient" and "earned" are used as a pair in BRK-08's Why ("Turns an expedient decision into an earned one") and "expedient" once more at `breaking-rules.md` L71 ("*The undocumented expedient decision.* Indistinguishable from negligence at the next audit, including to you."); "ignorant" and "lazy" occur only in the checklist line. The other "earned" hits (`layout-and-type.md` L69, `choose-format.md` L88) use the word in passing. "Deference" and "negligence" — the two named failures — are defined at `breaking-rules.md` L18 and `SKILL.md` L54–56 (quoted in 7.1 and 7.2). In this book's Chapters 0–15 the four taxonomy words are not used as a taxonomy anywhere (`lazy` 0, `expedient` 0, `ignorant` 1 in Chapter 6 in another sense; "deference" 0).

### 7.5 The gap register's four fields

`references/gap-register.md` does **not** print the four fields as a table header. Its header (L1–18) is a title, a rule and a status count:

````
   1  # The gap register
   2  
   3  **What testing found this system could not answer.**
   4  
   5  A review of real work is two-way: the work is judged by the book, and the book is judged
   6  by the work. This is the second half — the half that gets dropped, because it surfaces
   7  mid-review, under deadline, in conversation.
   8  
   9  > **A gap is closed only when a nameable rule exists that would have caught it.**
  10  
  11  `build/check_gaps.py` enforces that. A gap closed against a rule that does not exist fails
  12  the build. Generated from `reference/gaps.csv` — log new gaps there, or just say them and
  13  they will be logged.
  14  
  15  | Status | Count |
  16  |---|---|
  17  | open | 9 |
  18  | closed | 22 |
  19  
  20  ---
  21  
  22  ## Open — 9
  23  
  24  Found, not yet ruled on. This is the working list.
````

Each gap is then a heading, one sentence, and a two-column `Field | Value` table whose fields are **Found in · Date · Lands in · Note** (open gaps) with **Closed by** and the closing rules added for closed ones. One example entry, the first in the file (L26–35):

````
  26  ### 🔴 `GAP-28` · no rule
  27  
  28  The route that produces artefacts had five links and no test in it. Decision (did not exist yet), brand (stated outcomes not mechanisms), instrument (a general AI holding a pasted guide, which cannot verify or notice the guide moved), production (libraries with wrong defaults), verification (never existed). The book governs links 1 and 2 and says nothing about 3, 4 and 5.
  29  
  30  | Field | Value |
  31  |---|---|
  32  | Found in | Prompt 01 second pass — the production chain |
  33  | Date | 2026-08-16 |
  34  | Lands in | chapters/ch13;chapters/ch18 |
  35  | Note | Partly addressed: GAP-26 covers link 4, tools/inspect_docx.py covers part of link 5. The proposed answer is a third skill that writes artefacts and refuses to emit a file failing a Fixed check. That is a separate project, not a chapter amendment. Eleven requirements are specified in the live-testing output, eight of them machine-checkable. |
````

And one closed entry (L131–144), showing the "Closed by" lines:

````
 131  ### 🔴 `GAP-01` · rule wrong
 132  
 133  Line height was a single blanket 1.5 applied to body, tables, captions and display alike. WCAG 1.4.8 governs spacing within paragraphs; a table cell and a display line are different problems.
 134  
 135  | Field | Value |
 136  |---|---|
 137  | Found in | the design system under review — review |
 138  | Date | 2026-08-15 |
 139  | Lands in | chapters/ch03 |
 140  | Closed by | `TYP-17`, `TYP-18`, `TYP-19` |
 141  | `TYP-17` | Scope every typographic value to a style class and context |
 142  | `TYP-18` | The 1.5 line-spacing floor applies to running prose only |
 143  | `TYP-19` | Table cells, captions, display and statistics set their own leading |
 144  | Note | The book made the exact error its own chapter warns against. Found by the user, not by the book. |
````

*31 entries (9 open, 22 closed). Kinds, from the headings: no rule 20; stale 3; rule unusable 3; rule wrong 2; rule too weak 2; never the problem 1. Severity marks in the headings: 🟠 17; 🔴 12; 🟡 2 (red, amber, yellow circles).*

The four fields this book's chapters use ("what was missed, what was done instead, the cost of getting it wrong, where a rule would belong") are printed in two other files:

- `design-decisions/SKILL.md` L215–222:
````
 215  Write it in four fields, no more — the point is that it is cheaper to log than to skip:
 216  
 217  ```
 218  WHAT THE SYSTEM MISSED   one sentence, plain
 219  WHAT I DID INSTEAD       the working answer you used
 220  COST OF GETTING IT WRONG red / amber / yellow
 221  WHERE THE RULE BELONGS   a chapter, or "don't know"
 222  ```
````
- `design-decisions/references/found-a-gap.md` L40–49:
````
  40  ## The four fields, logged where you are
  41  
  42  Cheaper to log than to skip. That is the entire design requirement.
  43  
  44  ```
  45  WHAT THE SYSTEM MISSED   one sentence, plain, no hedging
  46  WHAT I DID INSTEAD       the working answer you actually used
  47  COST OF GETTING IT WRONG red / amber / yellow
  48  WHERE THE RULE BELONGS   a chapter, or "don't know" — "don't know" is a valid answer
  49  ```
````
- and the stored form, `found-a-gap.md` L59–72 (nine fields in `reference/gaps.csv`):
````
  59  Gaps live in `reference/gaps.csv` in the decision-book repository, one row each, with these
  60  fields:
  61  
  62  | Field | |
  63  |---|---|
  64  | `id` | `GAP-nn` |
  65  | `date` · `found_in` | When, and against what real artefact |
  66  | `kind` | One of the kinds above |
  67  | `what_the_system_missed` | The sentence |
  68  | `consequence` | `red` · `amber` · `yellow` |
  69  | `status` | `open` · `amending` · `closed` · `parked` |
  70  | `lands_in` | Chapter or file path, `;`-separated |
  71  | `closed_by` | Rule IDs from `reference/rule-register.md`, `;`-separated |
  72  | `note` | Anything worth saying, including "this was my error" |
````

The closure rule is printed as a block quotation at `gap-register.md` L9 and `found-a-gap.md` L12 — "**A gap is closed only when a nameable rule exists that would have caught it.**" — in running text at `SKILL.md` L224–225 ("a gap is **closed only when a nameable rule exists that would have caught it**"), and as rule BRK-26 ("Treat a gap as closed only when a nameable rule exists that would have caught it").

### 7.6 `references/rule-register.md` — columns, row count, and the BRK-07 row

````
   1  # The rule register
   2  
   3  **347 rules, every one from a chapter, rotated so you can query by what you are making.**
   4  
   5  The chapters answer *how do I decide?* This answers *what applies to a table cell in a Word document?*
   6  
   7  Generated from `chapters/` by `build/build_register.py`. Do not edit by hand — edit the chapter.
   8  
   9  | Tier | Count |
  10  |---|---|
  11  | Fixed | 258 |
  12  | Adaptable | 75 |
  13  | Decorative | 14 |
  14  
  15  ## By style class
  16  
  17  
  18  ### structure — 50 rules
  19  
  20  | ID | Rule | Tier | Context | Ch | What breaks without it |
  21  |---|---|---|---|---|---|
  22  | `BRF-01` | Reconstruct the need before accepting the named artefact | Fixed | all | 1 | The brief names a solution; needs must be actions or tasks, not solutions |
````

**Columns:** `ID | Rule | Tier | Context | Ch | What breaks without it` — six columns. There is no Why, Kind or Source column by those names; "What breaks without it" carries what the chapters call Why. **Rows:** 347 (counted; the file's own header says 347). **Tier, counted from the rows:** Fixed 258; Adaptable 75; Decorative 14 — matching the file's own table at L9–13 (Fixed 258, Adaptable 75, Decorative 14; that is 74.4% / 21.6% / 4.0%). The tier cells are plain words: no bold, and no qualifier such as "as a stance" or "as a procedure" anywhere in the register. **Arrangement:** one section "## By style class" with 20 sub-tables: structure — 50 rules; running prose — 43 rules; chart — 26 rules; heading — 26 rules; table — 22 rules; type token — 20 rules; document — 19 rules; container — 17 rules; interactive — 17 rules; data — 16 rules; colour token — 15 rules; general — 15 rules; diagram — 13 rules; image — 12 rules; metadata — 8 rules; slide layout — 8 rules; link — 7 rules; statistic — 5 rules; caption — 4 rules; list — 4 rules. **ID prefixes** (18): ARG 19, BRF 15, BRK 26, COL 19, CRV 15, DAT 22, DGM 15, DOC 26, DSH 21, DTA 20, FID 18, LAY 12, LNG 16, PLY 22, PRS 21, TBL 20, TYP 24, VOI 16.

**The BRK-07 row** (L71, in the sub-table "structure — 50 rules"), verbatim:

````
  71  | `BRK-07` | Run the removal test for the relevant chapter | Fixed | all | 18 | Work that survives removal was built on structure |
````

The same rule in Chapter 18's table (`breaking-rules.md` L32): `| Run the removal test for the relevant chapter | Work that survives removal was built on structure | **Fixed** | This book |`. And in the checklist (`breaking-rules.md` L86; `checklists.md` L358): "- [ ] The relevant chapter's removal test run, and passed".

All 26 BRK rows in the register, for reference (they are scattered across seven sub-tables by style class):

```
  71  | `BRK-07` | Run the removal test for the relevant chapter | Fixed | all | 18 | Work that survives removal was built on structure |
 117  | `BRK-05` | State the purpose in one sentence before defending a departure | Adaptable | all | 18 | Fuzzy values lose every argument to convention |
 118  | `BRK-11` | State every value in the design system once; other mentions point to it | Fixed | all | 18 | A value stated twice has already begun to diverge — measured: one guide carried 1.4–1.5 and 1.25–1.5 in a single section |
 119  | `BRK-19` | Render a decision rather than describing it, wherever it can be rendered | Fixed | all | 18 | Prose asks the reader to rebuild the picture from words, then judge it; a written review is agreed with and not acted on |
 120  | `BRK-23` | Quote the line every finding rests on, or mark the finding as inference | Fixed | doc | 18 | Findings drift from "the document says" to "you said" in three cheap steps; measured, it happened during this book's own review |
 184  | `BRK-20` | Build every demonstration with the mechanism it demonstrates | Fixed | all | 18 | A mock-up of real-headings-versus-bold that fakes both has removed the only thing it shows |
 331  | `BRK-02` | Fixed rules are uncertainty; Adaptable rules are ambiguity | Fixed | all | 18 | "Uncertainty implies there is something to be certain about" |
 359  | `BRK-01` | Establish the tier before arguing about a decision | Fixed | all | 18 | Most brand-versus-accessibility arguments are category errors |
 360  | `BRK-03` | Never let load-bearing meaning live in the decorative layer | Fixed | all | 18 | The most common accessibility failure that looks like a creative choice |
 361  | `BRK-04` | Name what the break buys: attention, retention, comprehension, context, register or fit | Fixed | all | 18 | An unnamed break is a mistake made confidently |
 362  | `BRK-06` | Prototype the break before committing to it | Adaptable | all | 18 | "Close the gap between I wonder and I know" |
 363  | `BRK-08` | Log every override: trigger, rule, alternative, evidence | Fixed | all | 18 | Turns an expedient decision into an earned one |
 364  | `BRK-09` | Treat repeated small defensible departures as the route to a house style | Adaptable | all | 18 | "Stand up in small ways over and over again" |
 365  | `BRK-10` | Never negotiate a Fixed rule; relocate the brand instead | Fixed | all | 18 | Accessibility decides where the brand lives, not whether it exists |
 366  | `BRK-13` | Attach an interim rule to every known gap | Fixed | all | 18 | A listed gap with no holding position is filled at 11pm by whoever has the file open |
 367  | `BRK-14` | Give every rule in the system its tier | Fixed | all | 18 | An untiered rule cannot be argued about productively; disagreement becomes authority rather than evidence |
 368  | `BRK-17` | A check compares each derived artefact to its source and fails on divergence | Fixed | all | 18 | The defect is invisible by construction — the artefact is internally consistent while applying superseded rules |
 369  | `BRK-21` | Show options side by side differing in one variable, and do not pre-select | Fixed | all | 18 | Two variables at once makes the comparison unreadable; a recommendation turns a decision into an approval |
 370  | `BRK-22` | Triage sheet before drill-down | Adaptable | all | 18 | Most decisions in a set resolve once they are next to each other; a stack of single decisions hides how many there are |
 371  | `BRK-24` | Report an absence as a different class of claim from a quotation | Fixed | doc | 18 | "The guide does not state X" is much easier to get wrong than "the guide says X" |
 372  | `BRK-25` | Log a gap in the system separately from a defect in the work, and close it in the source | Fixed | all | 18 | A finding written into a review and not carried back will be found again |
 373  | `BRK-26` | Treat a gap as closed only when a nameable rule exists that would have caught it | Fixed | all | 18 | Anything less is an intention |
 423  | `BRK-15` | State where the current version lives, in the system itself | Fixed | all | 18 | Versioning without a location leaves a reviewer several candidates and no way to choose between them |
 424  | `BRK-18` | A derived artefact never asserts its own settledness without naming its version | Fixed | data | 18 | "Do not re-derive these rules" is correct when current, and suppresses the correction when stale |
 438  | `BRK-16` | Every artefact derived from the system states the source version it was built from | Fixed | all | 18 | A skill, template, master or stylesheet embeds the system's values as a snapshot and cannot notice the source moved |
 482  | `BRK-12` | Version and date the design system on its face, with a change list of decisions | Fixed | all | 18 | A system with no version cannot be reviewed, because no reviewer can establish what they are reviewing |
```

### 7.7 The Style Guide's evidence standard — `nightlife-culture-design/references/voice.md` L88–100

````
  77  ## Editorial standard
  78  Frontload the point · mix sentence lengths naturally · break long sentences where ideas compete ·
  79  concrete verbs over abstract nouns · headings and short sections to guide the reader · real and
  80  relevant examples · cut filler, repetition and AI-style platitudes · **do not invent specificity,
  81  statistics or quotes** · keep nuance where it changes meaning.
  82  
  83  ## Avoid AI voice
  84  Never: "this matters" · "here is the bit everyone misses" · "in today's rapidly changing landscape" ·
  85  "unlock the potential" · "at the heart of" · "more important than ever" · repetitive three-part
  86  slogans, unless genuinely earned by the content.
  87  
  88  ## Evidence standard
  89  Strong design must never make weak evidence look stronger than it is.
  90  
  91  - Distinguish fact, estimate, interpretation, assumption and recommendation
  92  - Cite the original source; state publication date, data period, geography and population
  93  - Explain sector definitions and classifications, including SIC codes where relevant
  94  - Identify proprietary, commercial and restricted data
  95  - Describe primary research methods, recruitment, sample size and limitations
  96  - Do not imply causation from correlation
  97  - Avoid unsupported economic-impact multipliers and false precision
  98  - Separate commissioned from independent evidence
  99  - Record uncertainty, missing data, disagreement and methodological judgement
 100  - Link recommendations to evidence and identify who can act
````

The sentence is line 89: "**Strong design must never make weak evidence look stronger than it is.**" It stands alone under the heading `## Evidence standard` (L88), followed by ten bullets (L91–100). Chapter 14 L156 quotes it exactly and Chapter 15's conflict log quotes the ninth bullet ("Record uncertainty, missing data, disagreement and methodological judgement"). Both Chapter 14 and Chapter 15 cite it as "Style Guide §06"; the file read here has no section numbers.

---

## PART 8 — WHAT I NOTICED

Ten observations. Each is a statement about what is printed, with the place it can be checked. None is a recommendation.

### 8.1 The senses of Fixed that Chapter 0 names are almost unused in the tables; the senses the tables use are not in Chapter 0

Chapter 0 (L95) names two refinements: "Fixed as a statement of the record" and "Fixed as sequence". Across 433 Fixed-bearing rows the tables use "sequence" **twice** (1.15, 2.23) and "statement of the record" **never** (it is printed only on five truths in Chapters 1–2). What the tables use instead is "as a procedure" / "(procedure)" (102 rows) and "as a stance" / "(stance)" (90 rows), neither of which occurs in Chapter 0, and which are defined in the chapters' "Before you start" notes in four wordings (Ch 5; Chs 6–11; Ch 12; Chs 13–15 — quoted in 1.4). 212 rows (49.0%) say `**Fixed**` with no sense at all, and 31 carry some other qualifier ("adopted", "declared", "as defaults", "as disclosure", "as the planning assumption"…). The spelling of the qualifier also changes at Chapter 14, from "as a procedure" to "(procedure)". Chapter 15 is the only chapter with no unmarked Fixed: all 16 of its Fixed rows are "(procedure)" (14) or "(stance)" (2). Chapter 0's own gap row (L197) asks Chapter 16's register to "check every Fixed for which sense it carries"; Chapter 4's gap row G-4.17 had already recorded that the qualifiers were undefined. Chapter 0's two examples of "Fixed as sequence" — construct before proxy; recognition before release — are tiered `**Fixed**`, `**Fixed**`, `**Fixed** as a stance` (2.16, 5.1, 9.2) and "sequence", "sequence", "stance", "stance", "procedure" (1.15, 2.23, 5.19, 9.33, 12.36).

### 8.2 The same rule carries different tiers in different chapters

| The rule | Where, and the tier printed |
|---|---|
| Investigate an outlier before treating it as noise | 1.13 `Adaptable` · 4.33 `**Fixed**` · 4.36 `**Fixed**` |
| State where a causal claim stands on the evidence ladder | 2.3 `**Fixed**` · 7.29 `**Fixed**` · 15.15 `Adaptable` |
| Recognition is checked with the people described before release | 1.15 `Adaptable in method; Fixed as sequence` · 2.23 `**Fixed** as sequence` · 5.19 `**Fixed** as a stance` · 9.33 `**Fixed** as a stance` · 12.36 `**Fixed** as a procedure` |
| Construct before proxy, parts or items | 2.16 `**Fixed**` · 5.1 `**Fixed**` · 9.2 `**Fixed** as a stance` |
| Uncertainty as a numeric range, never a verbal hedge | 1.5 `**Fixed**` · 2.14 `**Fixed**` · 15.10 `**Fixed** (procedure)` |
| "Leading" only with a measured record | 6.23 `**Fixed**` · 7.35 `**Fixed** as a procedure` |
| The disclosure floor set by the scene's knowability | 6.42 `**Fixed** as a stance` · 10.5 `**Fixed** as a procedure; Adaptable in value` |
| The house's headline length | 11.4 `**Fixed**; the house limit Fixed as a stance` · 14.14 `Adaptable` |
| The retirement plan | 8.32 `**Fixed** as a procedure; Adaptable in period` · 11.38 `**Fixed** as a procedure` · 15.19 `**Fixed** (procedure)` |
| No league table / no ranking of places | 1.11 `**Fixed**` · 2.13 `**Fixed**` · 6.37 `**Fixed**` · 7.2 `**Fixed** as a stance` · 10.37 `**Fixed** as a stance` · 12.34 `**Fixed** as a stance` |
| Cognitive testing of a felt question | 5.18 `**Fixed** (test); Adaptable (combine)` · 9.31 `**Fixed** as a procedure` |

The clearest three: the outlier rule is `Adaptable` in Chapter 1 and `**Fixed**` in Chapter 4; the evidence-level label is `**Fixed**` in Chapters 2 and 7 and `Adaptable` in Chapter 15 (15.15 "with a declared minimum"); the house headline limit is "Fixed as a stance" in 11.4 and `Adaptable` in 14.14 — the last is a deliberate re-tiering that Chapter 14's conflict log records ("Version 1 Ch 13 rule, five/ten words Fixed… Re-tiered Adaptable… Carried to Chapter 16's register"), but row 11.4 is not marked as superseded. Chapter 15's flag (L562) lists "the retirement plan as a Fixed rule" as a question for Chapter 16 although three tables already print it as Fixed. The wordings of every one of these are side by side in 1.3 (D8, D10, D14, D15, D20, D21, D22, D25, D26, D31).

### 8.3 Rules that pull against each other across chapters

- **Whether places may be ranked at all.** 1.11 "Rankings by rate are screening instruments, never verdicts; show intervals" — `**Fixed**` and 2.13 "Treat a league table as acting on the ranked; never present one as a reader's decision aid without intervals" — `**Fixed**` allow a ranking with intervals. 7.2 "No league table of places on any measure, and no bands of position (quintiles and the like); position is shown within a distribution with its interval, in categories of statistical separation from an expectation if categories are needed" — `**Fixed** as a stance`, 10.37 "No panel grades or ranks places, and where a value is drawn by colour the scale is checked for stigma; a money view is lit for a scene only after its governance has agreed, the speculation reading has been assessed, and both are on the record" — `**Fixed** as a stance` and 12.34 "No screen carries an ordered all-places list" — `**Fixed** as a stance` forbid it. Then 12.35 "Any rank the house ever lets out carries the official wording: ordinal, relative, no distance" — `**Fixed**` and 15.12 "Any ordering of places ships with a question-and-answer text saying what it can and cannot be used to say, with worked examples and the reason comparability is lost between editions" — `**Fixed** (stance)` regulate rankings that the three before say will not exist. Chapter 7's own gap row G-7.15 notes that its first draft of the rule "would have forbidden the chapter's own recommended forms".
- **What form uncertainty takes.** 1.5 "Show uncertainty as a numeric range, never as a vague hedge or a hidden point" — `**Fixed**`, 2.14 "Show uncertainty as a numeric range; never as a verbal hedge; never omit it to protect the signal" — `**Fixed**` and 15.10 "Show uncertainty as a range beside a point; never a verbal hedge alone" — `**Fixed** (procedure)` ask for a numeric range. 3.23 "Never a bare interval or a hard boundary for uncertainty; prefer countable dots, gradients, violins or animated draws; show outcome spread, not only estimate uncertainty, where individuals are the subject" — `**Fixed**` forbids "a bare interval". The two can be reconciled (a range in words and numbers; not a bare error bar in the drawing) but no chapter says so in its table.
- **How use is measured.** 1.6 "Design and measure use from the first day" — `**Fixed**`; 10.24 "The site's own analytics count how the service is used, never who uses it, or run on consent" — `**Fixed**`; 11.37 "The dashboard measures its own use as how, not who; publishes it aggregate and dated; and reads "those who interacted did better" with the confound named" — `**Fixed** as a stance`; and 15.18 "Count reach in the unit counted and name it, never as "readers"; measure use only by asking, and print the response rate" — `**Fixed** (procedure)`. The first three have the dashboard count its own use; the last says use is measured "only by asking".
- **How far away the detail may be.** Chapters 4–7 say "one tap" (ch04 ×6, ch05 ×6, ch06 ×1, ch07 ×2; once more in ch11); Chapters 11, 13 and 14 say "one step" (ch11 ×15, ch13 ×1, ch14 ×8). 5.23 "Publish the recipe as a standard card, one tap from any composed number, with the fact of composition visible beside the number" — `**Fixed**` puts the recipe one tap away; 11.18 "Nothing the majority of readers need is one step away; nothing one step away is hidden behind a control readers think will take them off the page; detail on request is two levels at most, with an obvious route" — `**Fixed**` says nothing the majority need is one step away; 14.4 "The precise twin is one step away and the form states its finding, and any distortion, in words on itself" — `**Fixed** (procedure)` puts the precise twin one step away. Chapter 11 (L605) asks "whether the legend carries "on the face / one step away / on request"".
- **Text inside the chart frame.** 12.32 "Every chart carries, inside its frame, title, unit, source, base, address and snapshot date, for comparisons the gate and wording, and for either column the bridging sentence; the page text repeats them" — `**Fixed** as a stance` departs from official practice and from the design system's stated preference for text outside images; 12.33 and 13.13 make the departure "in addition to page text, never instead". The book records this itself (Chapter 12 conflict log, "Silent on… against the design system's own preference for text outside images"; Chapter 13 "Agrees… Chapter 12's frame meets 1.4.5 under the condition now stated").

### 8.4 The four-line record has two sets of fields, and the instruction to use it stops at Chapter 7

Chapter 0 (L157) and the Decision Book (`SKILL.md` L87) give the four lines as "trigger, rule and tier, alternative chosen, evidence". Chapters 2, 3, 4 and 5 give them, in their break tests, as "(what rule, why, for whom, what proved it)" (ch02 L476, ch03 L467, ch04 L580, ch05 L441) — "for whom" is in neither the Decision Book's list nor Chapter 0's, and "alternative chosen" is in neither of these four. Chapters 1, 6 and 7 name the record without fields. Chapters 8–11 do not mention logging a break at all; Chapters 12 and 13 say a break "is logged" with test results attached, without saying where; Chapters 14 and 15 log to their own records (the boundary log; the precedent record). Inside the Decision Book the record is also three things: four items without "tier" (BRK-08, `breaking-rules.md` L33), four with "rule and tier" (`SKILL.md` L87; the checklists), and a five-column table with a Date (`override-log-template.md` L7) under the words "Four lines per departure".

### 8.5 "Register", "log", "record", "sheet", "set", "card", "statement" — the names of the book's own documents drift

- Chapter 14 (L16) states the convention — "where this book names a log… it says "log" or "register" with its qualifier, and the record this chapter leaves is called the *boundary log* to keep the two apart" — and then calls the boundary log a register in five places (L436 "A register entry outlives the person who made the choice"; L448 "what a line in the register looks like"; L516 "write the register entry"; L714 "Used in the register"; L728 "a ten-line register"). Its conflict log says "a ten-line register" (L728); its rule 14.2, its 60-second version (L44) and its record section (L432) say eleven lines, and the table has eleven.
- "The recognition record" is the name of line 8 of Chapter 5's recipe (ch05 L316) and of Chapter 12's whole ten-line record (ch12 L373).
- "The record beneath them" is a heading in five chapters with two meanings: findings of record under the canonical truths (Chs 3, 4, 5 — 11, 21 and 22 bullets) and the document itself (Chs 6, 7).
- "Recipe card" does not occur in Chapter 5, which made it; the name is given by Chapter 6 (L420) and used from then on. "Provenance set" is the Decision Book's name ("the full provenance set", quoted at ch04 L179) for what Chapter 4 heads "The minimal set".
- The count of records wobbles at the face sheet. Chapter 11 (L390) says it leaves "not an eighth record about the data but a sheet about the *surface*" and its flags say "Seven records and a face sheet" (L571, L766); Chapter 12 then leaves "a ninth" (L375) and says "Nine records now" (rule 12.39); Chapter 14 (L16) lists "the ten documents earlier chapters left", the face sheet among them.
- The list this chapter is asked to make is "Chapter 16's rule register" (ch00 L197; ch01 L467; ch02 L686), "Chapter 16's register" (ch14 L733, L734) and "the rules register" (ch13 L495); "the rule register" without a qualifier is the Decision Book's in Chapters 5, 8, 9 and 14. The Decision Book has a "gap register" and an "override log"; this book adds a "boundary log", a "precedent record" (which "like the boundary log… grows"), a "conflict log" in every chapter and a "research log". Chapter 15's conflict log (row 7) asks "whether three logs are one".

### 8.6 Rules whose only source is the chapter itself

Source column is the chapter itself and nothing else (5 rows): 1.17 (Source: "This chapter's search") — Never print an unsourced adoption or failure percentage for dashboards — `**Fixed**`; 6.43 (Source: "This chapter §12") — Record the ten-line claim record beneath every statement of value; "not done" is written, not hidden — `**Fixed** as a stance`; 10.42 (Source: "This chapter §18") — The quotation rule applies to the dashboard as to the book: institutions are quoted; private persons are not identified by it or through it — `**Fixed** as a stance`; 12.39 (Source: "This chapter") — The recognition record, ten lines, sits beneath every place-page — `**Fixed** as a procedure`; 15.21 (Source: "This chapter") — Record every borrowed mechanism in the precedent record, nine lines, with its status, before it ships — `**Fixed** (procedure)`.

Source is only a section of the same chapter (3 rows): 12.18 (Source: "Section 6") — Conditions are shown as conditions with numbers, never folded into a type's name — `**Fixed** as a stance`; 13.31 (Source: "Section 4") — The distribution argument is recorded once, as funding and reputation — `**Fixed** as a procedure`; 13.32 (Source: "Section 4") — The law is cited by section with its date, and never as advice — `**Fixed**`.

Source is only this chapter, other chapters of this book, or version 1 of this book (9 rows): 7.1 (Source: "This chapter §12; Chapter 4"); 6.24 (Source: "Version 1 Ch 6; this chapter §8"); 7.11 (Source: "Version 1 Ch 5; this chapter §11"); 9.36 (Source: "Version 1 Ch 4; this chapter §13"); 11.30 (Source: "Chapters 3, 7, 9"); 12.2 (Source: "Section 3; Chapter 11"); 12.22 (Source: "Section 6; Chapter 7"); 12.29 (Source: "Version 1; Chapter 10"); 12.34 (Source: "Version 1; Chapter 7").

All 17 are tiered Fixed in some form: three are plain `**Fixed**` (1.17, 12.22, 13.32); the other fourteen are a stance or a procedure. Four of the twelve rules that carry a record are among them (6.43 claim record, 7.1 comparison record, 12.39 recognition record, 15.21 precedent record); 8.1, 9.1, 10.1 and 11.1 add an outside source beside "this chapter §…". The fourteen residual rows (open choices and Decorative; D42) are sourced to "Section n", "Design system", "Decision Book Ch 7" / "Ch 18", "Chapter 14 of this book" or "—", and have "—" as their Kind.

### 8.7 Conventions set in Chapter 0 that later chapters did not follow — and the reason is printed

Chapter 0's header (L4) reads "Version 2 · revised 6 October 2026, after Chapters 1 and 2". Seven later chapters "open a thread for Chapter 0" in their Looking back (ch05 L516, ch06 L639, ch07 L575, ch08 L720, ch09 L676, ch10 L845, ch11 L605) asking the legend to take up new terms; Chapter 0 has not been revised to answer any of them. What drifted:

- **The rules-table note.** Chapters 1–11 print an italic line under `## The rules` ("Kind and tier as in Chapter 0…"); Chapters 12–15 print none.
- **The gap table's four fields.** Chapter 0 (L64, L156) and the Decision Book say four fields: what was missed, what was done instead, the cost, where the rule belongs. Chapters 14–15 use `Gap | Where it bites | Interim position | Who closes it` and drop the cost.
- **The conflict log's three parts.** Chapter 0 (L65): "Where the chapter agrees with the style guide, where it conflicts, and where the guide is silent". Three parts in Chapters 1–7 and 12–13; two in 8–11; a status table in 14–15. From Chapter 4 the log also covers the Decision Book, which Chapter 0's description does not mention.
- **Section names.** "What this means for a nightlife dashboard" (Chs 1–5) becomes "An illustration from nightlife — method only" (6–7) and "A nightlife illustration — method only" (8–15). "Why people believe what they believe" (1–11) becomes "What people believe about …, and what the evidence says" (12–15). Chapter 0's "The idea, plainly" and "The evidence" are not headings in any chapter. All fifteen chapters do carry the other twelve template headings.
- **The dagger.** Chapter 0 (L99): "the authors' published abstract was read, not the full text". Chapters 7–11: "abstract or summary". Chapter 12: "an abstract, a secondary account or a press summary". Chapters 13–15: "an abstract or a secondary account". Chapter 15's conflict log (row 5) adds that the Analysis Function advises against "†" because screen readers find it hard.
- **† on a Fixed rule.** Chapter 0 (L99): "A Fixed rule resting on a † source is flagged `[Further research]` until the full text has been read." 49 Fixed-bearing rows have a † in their Source or Kind cell (Ch 1: 5, 2: 3, 3: 4, 4: 2, 5: 1, 6: 4, 7: 8, 8: 1, 9: 9, 10: 1, 11: 5, 12: 3, 14: 3). No row carries the flag. The table's note carries it for the whole table in Chapters 1–7; the notes of Chapters 8–11 do not; Chapters 12 and 14 have † rows and no note.
- **Marks Chapter 0 does not define.** "reconstructed" (from Ch 6), "(read once)" (from Ch 7), "adjacent domain" (in Kind cells from Ch 3; glossed in the table note from Ch 5), and the Kind sub-kinds (8.8).
- **The tiers' own definitions.** Chapters 1–5 repeat Chapter 0's ("*Fixed* is a hard line with a right answer; *Adaptable* is a stated default you may argue with and must log if you leave; *Decorative* is free"). Chapters 6–11 name the tiers without defining them. Chapters 12–15 define them differently: "*Fixed* (holds in any dashboard), *Adaptable* (holds unless a stated reason overrides it) or *Decorative* (open)".
- **Flags.** Chapter 0 defines `[Counterbalance → Ch n]` for a finding that pulls against an earlier chapter. Fifteen uses point somewhere else: `[Counterbalance → design system]` ×4, `→ Decision Book…` ×7, `→ design system; Decision Book Ch n` ×2, `→ version 1 Ch n` ×2 (Chapters 2–7).
- **A convention credited to Chapter 0 that is not in it.** Chapters 8, 9, 10 and 11 (L12 in each) write "The *symmetry test* (Chapter 0)". The word "symmetry" does not occur in Chapter 0. Chapter 7 (L12) credits it to Chapter 5; the phrase first appears in a Chapter 4 gap row (G-4.15).
- **Severity colours.** Chapter 0 (L156) says the gap register's red, amber and yellow are "internal only, never shown publicly", and its own gap row G-0.2 notes the design system's "never RAG tags" rule; Chapters 0–13 print the Cost column in the chapter (32 Red, 84 Amber, 65 Yellow).

### 8.8 The Kind column outgrew the legend

Chapter 0 defines five kinds. The fifteen tables print **182 distinct Kind wordings**; 141 of them are used once. Only 163 of 486 rows (34%) use one of the five words alone. The rest are combinations ("Evidence + Reading"), qualified kinds ("Evidence (adjacent domain)" ×20; "Evidence of method"), or sub-kinds of Standard introduced chapter by chapter — 30 distinct parentheses: Standard (Analysis Function), Standard (EEF; Magenta Book), Standard (ONS), Standard (SMS; EEF), Standard (W3C), Standard (W3C, AA), Standard (adjacent domain — financial reporting), Standard (adjacent domain — price indices), Standard (adjacent domain — psychometrics), Standard (adjacent domain), Standard (adopted), Standard (community), Standard (design system), Standard (epidemiological), Standard (government guidance), Standard (international), Standard (law), Standard (law, by analogy), Standard (method), Standard (official statistics), Standard (platform), Standard (policy), Standard (price list), Standard (professional), Standard (regulator), Standard (regulator, code), Standard (regulator; design system), Standard (the method's own), Standard (the period), Standard (voluntary). Some cells are sentences ("Evidence + Standard; the extension to every measure on a dashboard of small places is a Reading"). 14 rows have "—". Chapter 0's own rule for a Standard — "The text says whether it *binds* Nightlife Culture or is *adopted voluntarily*" — is met in eight rows: five carry it in the Tier column as "(adopted)" or "(adopted voluntarily)" (1.14, 2.11, 2.24, 4.10, 4.23 — two of which, 2.11 and 2.24, have no Standard in their Kind) and three in the Kind column (3.6 "Evidence + Standard (voluntary)"; 8.25 "Standard (adopted) + Evidence (one measurement)"; 13.25 "Standard (regulator), adopted"). 241 rows have "Standard" in their Kind; the other rows' cells do not say whether the standard binds (several chapters say it in the table note instead — e.g. Chapter 10: ""by analogy" marks a statute that binds public bodies and not the studio").

### 8.9 Almost nothing is Adaptable — least of all in Chapters 6–10

433 of 486 rows (89.1%) have Fixed in the tier; 45 (9.3%) are Adaptable only; 8 (1.6%) Decorative. The Decision Book's own register, which this book says it inherits, is 258 Fixed (74.4%), 75 Adaptable (21.6%), 14 Decorative (4.0%) of 347. Adaptable-only rows by run of chapters: Chapters 1–5, 21 of 140 (15.0%); Chapters 6–10, 5 of 193 (2.6%); Chapters 11–15, 19 of 153 (12.4%). Chapters 7 and 10 have none (36 and 43 rows, all Fixed in some form); Chapter 6 has one in 43. Chapters 6–11 and 15 have no Decorative row. Chapter 8 says so of itself (L720: ""Fixed", "Fixed as a procedure" and "Fixed as a stance" are nearly equal in number, with almost nothing Adaptable"). Chapter 0 (L92) describes Adaptable as "**A default you may argue with**… Breaking it is: The job. Deviation is expected — with a record"; the Decision Book calls treating an Adaptable decision as Fixed "deference" (`breaking-rules.md` L18). The 192 rows marked as a stance (90) or a procedure (102) are where this question sits: by the chapters' own definitions a stance is "a rule the studio adopts whose source is a reading or a practice" and a procedure "fixes the steps and not the parameter" — neither is Chapter 0's "There is a right answer and it can be checked" (L91).

### 8.10 The break-test section changed its job, and the Decision Book's vocabulary for breaking rules is not used

Chapter 0 (L59) says the section is "The test to run before deviating from a Fixed rule". In Chapters 1–6 it is that. From Chapter 7 it tests "a comparison rule" or "a departure from one of this chapter's rules" with no tier named (7, 8, 9, 10, 11, 15); in Chapters 12 and 13 it is the page's release test, run whether or not anything is broken ("Run the five tests of section 10 on the page as built"; "A scan, three walks and a question; each has a pass"); in Chapter 14 it is run on every expressive element. By form, 27 of the 55 named tests are reader tests and 10 are removals. Chapter 0's glossary (L151) says of the removal test "Chapter 14 collects every chapter's version"; the phrase "removal test" occurs in Chapter 0 once, Chapter 14 thirty-five times, Chapter 15 twice and in no other chapter, and only Chapters 8 and 14 lead with a removal. The Decision Book's BRK-07 is "Run the removal test for the relevant chapter". The Decision Book's other terms for a break do not appear in Chapters 0–15: the deviation classes "ignorant, lazy, expedient or earned" (0 uses as a taxonomy), "deference" (0), BRK-04's list of what a break buys — "attention, retention, comprehension, context, register or fit" — (0 uses; rule 14.3 names the purchase "in the affective-intent template" and rule 11.16 "from the table"), and "negligence" once outside Chapter 0's tier table (the Why of rule 14.2, "An unlogged break is indistinguishable from negligence at the next audit", which echoes `breaking-rules.md` L71).


---

*End of assembly.*
