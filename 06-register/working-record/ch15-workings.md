# Working record · Chapter 15 — Learning from the best

*How this chapter was made. These sections stood in the chapter at draft 2 and were moved here, word for word, on 14 October 2026 when the book was finished. They are the record of the method: what the chapter expected against what it found, what it did to the chapters before it, the gaps it met, where it met the design system and the Decision Book, and the loose ends it flagged. Nothing here is a rule; the rules are in the register, the open choices in the decision log, the probes in `03-tests/PROBES.md`.*

## Before you start

This is the fifteenth chapter of a research book written for Nightlife Culture, a creative policy studio led by Carly Heath, about how dashboards work and why. The book exists to support the Vibe Map — a planned public, non-commercial, interactive account of the people, activity, value and support systems that sustain a place's nightlife culture, built first for the West of England. You do not need to have read the earlier chapters. Where this one leans on them it says so and gives the finding in a line, and it argues from its own sources.

The chapter's conventions are the book's. Every finding is marked by **kind** — *Standard* (a published rule from a standards body, a regulator, a design system or a method text, with the sub-kind named: Standard (regulator), Standard (official statistics), Standard (method), Standard (law)), *Evidence* (a measured result, with what was measured and on whom), *Evidence of method* (a published procedure whose results are reported), *Reading* (this book's interpretation of evidence or standards), *Practice* (what a named project, body or newsroom does, read for method), or *Nightlife Culture* (the house's own position) — and by **tier**: *Fixed* (holds in any dashboard), *Adaptable* (holds unless a stated reason overrides it) or *Decorative* (open). "Fixed as a stance" means the house has decided it and the chapter gives the grounds; "Fixed as a procedure" means the rule is a thing to do. A dagger (†) marks a figure or quotation taken from an abstract or a secondary account rather than from the paper's body; "secondary" marks a source read only through another; "(read once)" marks a quotation returned once by the fetch tool without a presence check. Findings in the body carry their kind in italics at the end of a paragraph; tiers are given in the rules table. Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0.

This chapter reads other sectors' public data displays for their *method* and for nothing else. It never reports a figure about any place's culture or people as subject matter, and where a page returned one it was discarded; the survey results it does report are about trust in institutions and are evidence about method. It never researches nightlife, which is the studio's domain and not this book's. And beyond the seven things it holds true regardless, and the procedures those entail, it does not say what the Vibe Map should borrow; it says what each sector's best work did, how that is documented, what it cost, and what the evidence is — so that the studio can decide the rest with the terms in front of it. The brief's words for the chapter are "what they got right about trust, provenance, change over time and reach, and what nightlife borrows"; the chapter reads "borrows" as the transfer of a mechanism, with its conditions, and never as the transfer of content.

The chapter's working words. The *failure register* is the list of eight sentences in the brief, in Carly Heath's own words and spelling, that say when a dashboard fails ("It fails if it looks the same every month"; "It fails if people dont use it"; and so on); section 10 reads it. The *four properties* are the brief's: *trust*, which the chapter treats as measured only where someone asked people a question about it, and distinguishes between trust in a *producer* (a statistics office, a charity) and trust in a *display*; *provenance*, the record of where a figure came from and what was done to it; *change over time*, which here means both how a display shows that a quantity moved and how a display's own figures move after first publication; and *reach*, who read it and whether it informed anything, which the chapter counts in the unit each source counts in and names the unit. A *mechanism* is a documented, repeatable rule or practice — a banding rule, a change log, a release calendar, a vintage archive, an evaluation design — as distinct from a design or a look. A mechanism is *borrowable* when its rule is printed, its reason is stated, and its evidence or its cost is known; the chapter's borrowing test is in section 1. A *vintage* is the version of a dataset as it stood on a given date; a *revision* is a scheduled change to a published figure and a *correction* an unplanned one, which is the ONS's distinction and the chapter keeps it. A *banding rule* is the rule by which a value is coloured or labelled against a comparator; a *direction-of-travel label* is the arrow or word that says a series rose, fell or held. *Actionability* is the term one 2021 study used for whether a pandemic dashboard gave its readers what they needed to act — a stated audience, sources and methods, trends tied to decisions, data close to home; section 3 gives its seven features. *Layered* communication is a central bank's term for publishing the same report at several depths — a one-sentence version, a short visual summary and the full technical text. A *release calendar* is a pre-announced list of publication dates and times. A *custodian* is the body that keeps a dataset comparable, available and citable over time; a *sunset* is a dataset's or display's planned ending. The *records beneath the dashboard* are the eleven documents earlier chapters left, one each: the *provenance set* (Chapter 4: where every figure came from and what was done to it); the *recipe card* (5: how a measure is built, with its weights and choices); the *claim record* (6: what the dashboard claims and on what footing); the *comparison record* (7: what was compared with what, and the gate it passed); the *service record* (8: how the display is run, refreshed, maintained and retired); the *measure record* (9); the *safeguards record* (10: disclosure and consent); the *face sheet* (11: what the first screen carries — the sentence, the unit, the date); the *recognition record* (12: how a reader finds their place); the *accessibility statement* (13); and the *boundary log* (14: the removal test's record). Names from earlier chapters used here in passing: the *funnel discipline* (Chapter 5: small bases vary more, so a value is read against the spread expected for its size); the *peer method* (Chapter 12: showing a place beside places like it rather than ranked above and below them); the *gross-to-net discipline* (Chapter 6: subtracting what would have happened anyway before claiming value); the *audience yardstick* (Chapter 6: the segmentation the culture sector used to compare an audience with the public); the *C3 Monitor* (Chapter 5: a city index that published intervals around its ranks); the *Observatory's drift* (Chapter 8: a public data page whose contents aged while its front page did not); the *write-the-sentence-first rule* (Chapter 1: the finding is written in a sentence before any chart is drawn); the *incumbents* (the existing place indices version 1 read); the *four removals* (Chapter 14: mono, silent, still, undressed — the test that strips a display's expressive layer); and the *identity line* (Chapter 12: a place's people are never ranked by a condition). The *floor* is Chapter 13's name for the accessibility requirements the house adopted. The *gate* is the condition a comparison must meet before it is shown (Chapter 7). The *adviser* is the studio's own legal adviser, to whom this book reports law and never advises. Abbreviations used below after their first appearance: *OSR*, the Office for Statistics Regulation; *PCOS*, the Public Confidence in Official Statistics survey; *UKHSA*, the UK Health Security Agency, and *PHE*, Public Health England, its predecessor; *QMI*, a quality and methodology information report; *ELS*, the ONS's Explore Local Statistics service; *RAG*, a red-amber-green colour scheme; *SMS*, the Scientific Maryland Scale of evidence; *ACE*, Arts Council England; *NPO*, a National Portfolio Organisation funded by it; *NPC*, New Philanthropy Capital; *SORP*, the charities' Statement of Recommended Practice for accounts. *Version 1* is this book's archived first draft; its Chapter 12 (*The gallery*) is this chapter's nearest predecessor and its sector claims are tested in section 11.

A note on sources. Four research agents worked with web search rationed to thirty calls each, and several things could not be read and are marked where they appear: the two *Lancet Infectious Diseases* papers on the Johns Hopkins dashboard (one unreachable, one abstract only); the retired UK coronavirus dashboard's own documentation pages (no reachable archive; the successor's documentation and the team's blog posts were read instead); the Fingertips FAQ and two of its older guides (server errors); the Charities SORP's primary text (read through an accountancy body's summary); the Bank of England's response to the Bernanke review and its 2026 reports; the body of the journal version of Galvão and Mitchell; the per-indicator pages of Scotland's National Performance Framework, which now redirect; and the Audience Agency's data arrangements, about which nothing has been published. The reader of the fetch tool, on one first pass, rendered a UKHSA sentence as "Data from the last 5 days by specimen date may be incomplete" when the printed text is "Data for the last 5 days by specimen date are considered incomplete"; every quotation below is marked where it was not checked by presence re-fetch — "(read once)", †, "secondary" or "two passes" — and the verifier's pass is recorded in the log.

---


## 11 · The symmetry test

**Version 1's Chapter 12 claimed public health as the exemplar of provenance furniture.** Holds and is now specified: the five-heading page, the thirty-two-field record, the labelled log, the two ledgers, the source URL per observation. It also now carries the sector's gap: trust and reach evidenced only by self-published numbers.

**Version 1 claimed the ONS as the exemplar of comparison without rank.** Holds for the service, with its method now specified (K-means, 4 to 15 clusters, twenty nearest by Euclidean distance, snapshot caveat), and gains two companions: the OECD's printed refusal to aggregate and County Health Rankings' move from ranks to groups. It also gains a correction: one ONS small-area release uses the kind of caution phrase the GSS says is insufficient.

**Version 1 claimed the incumbents as failure case law.** Chapter 14 confirmed the drift; this chapter adds the sector's own case law from inside government — the Health Index, the levelling-up metrics, Scotland's unfindable arrow rules.

**Chapter 2's trust line.** This chapter adds measurement to it rather than repeating it: the producer-versus-presenter gap in four waves; the two central-bank experiments; the five uncertainty experiments and the two GDP waves; the one randomised dashboard test. Chapter 2 said trust in a display is not the same as trust in its maker; this chapter finds the first is almost never measured and the second is, and gives the method.

**Chapter 5's composite audit.** This chapter adds three things Chapter 5 did not have: the deprivation indices' paired usage text as the form of words; the Health Index's frozen base-year method and its disclosure of unmeasurable change; and a second audited rank interval (the JRC's 5,000 simulations). It does not repeat the audit.

**Chapter 6's orphaned yardstick.** Confirmed and worsened: no custodian named twenty-six days after liquidation; the Participation Survey replaced by a combined survey with a dotted line and a comparability sentence.

**Chapter 7's C3 Monitor and the ELS as comparison without rank.** Both carried; the ELS's method is now the cited specification; the GSS's model sentence for non-significant change is the house's.

**Chapter 14's four removals and provenance a scroll away.** Carried into every sector read: the provenance here is at the depth of a documentation page or a quality report, which the chapter read, rather than on a first screen, which it did not; and the sectors' printed rules avoid meaning carried by colour alone — Fingertips' neutral ramp and neutral default are the removal test's "mono" done by rule — though the displays themselves were not audited for it.

**The brief's "could fold into Chapters 2 and 5".** The chapter's own test was whether it found mechanisms with terms rather than examples. It found about forty, listed in section 9. Some were already in the book in another form: the recipe card's ancestry in the QMI; the comparison record's in the ELS; the service record's in the Observatory's drift; the rank interval; the funnel; the sentence-first rule. Most were not — among them the metric page template, the labelled log, the two ledgers, the incompleteness band, the RAG and arrow rules, vintages, revision against correction and the printed revision size, the release-calendar and early-reader rules, the band-rule footnote, the three regulator sentences, the paired usage text, the frozen base year, the refusal to aggregate, the dotted break line, the fixed trust question, the question of whether the data informed a decision, the sunset note and the retirement clause. On that count the chapter has found more than a reading list; whether that earns it a chapter of its own is Carly's call, which the brief reserved to her and which has not yet been made.

---


## Open questions and flags

`[Further research]` The two *Lancet Infectious Diseases* papers on the Johns Hopkins dashboard — the 2022 paper's anomaly-detection and back-distribution sections are the largest single gap; the retired coronavirus dashboard's own documentation; the Fingertips FAQ and quintile rule; Scotland's per-indicator arrow thresholds; the Charities SORP 2026 paragraphs on impact; the Bank of England's response to the Bernanke review; Galvão & Mitchell's journal version; the UK Data Service's rule for a new edition; a 2025 wave of PCOS, if one exists; Sorapure 2023 on user perceptions of actionability; the review of uncertainty displays in pandemic dashboards (located, not read).

`[Further research]` Whether anything has been announced about the Audience Agency's data since 6 October 2026; the Hodge review at source.

`[Prototype flag]` The lag distribution of any late-returns series the house will publish, from which the window is set; the vintage naming rule, which must exist before the first release; the retirement plan; the precedent record as a working file.

`[Validate with users]` The reader test for the incomplete-tail band (section 14); whether readers of the house's displays read a neutral marker as "no arrow yet" or as "no change"; the one question that measures use, with its response rate.

`[Revisit → Ch 16]` The precedent record beside the boundary log and the override log; the status marks [p] [r] [f] against this book's own dagger; the twelve records as one document; the regulator's minimum list as a checklist the house can voluntarily meet; the retirement plan as a Fixed rule.

`[Revisit at end]` The fold question (section 11); whether the twelve records are one document.

`[Counterbalance → Ch 2]` Trust in a display is almost never measured; the producer-versus-presenter gap is measured and large. `[Counterbalance → Ch 5]` The deprivation indices' usage text and the Health Index's stall are the composite audit's case law. `[Counterbalance → Ch 6]` The yardstick's custodian has failed; the Culture and Heritage Capital guidance carries no multiplier warning. `[Counterbalance → Ch 11]` Fan charts were found well understood in the Bank's own staff test, against a review that said otherwise; the "sentence first" rule meets the GSS's model sentence. `[Counterbalance → Ch 12]` The similar-areas method is now specified; County Health Rankings left ranks for groups.

For the adviser: none; the only law read is the pre-release Order, reported.

---


## Looking back

*Verdicts: "strengthens" means the chapter's finding supports the earlier one; "bounds" means it limits its reach; "counterbalances" means it pulls the other way; "opens a thread" means it raises a question the earlier chapter did not.*

**Chapter 2.** The trust line gains its measurement: in 2023, 87 per cent trusted the statistics office and 32 per cent agreed the government presents its figures honestly, a gap held across four waves; a display's format moved comprehension and not trust. Strengthens, and bounds.

**Chapter 4.** The provenance set now has sector precedents at every line — the metric page, the record, the source URL per observation, the processing label. Strengthens.

**Chapter 5.** The recipe card's ancestry (the QMI) is confirmed and extended; the composite audit gains the deprivation indices' usage text, a second audited rank interval and the Health Index's frozen base year. Strengthens.

**Chapter 6.** The audience yardstick is orphaned with no custodian; the national survey has a dotted line; the multiplier warning the brief expected is not in the capital guidance. Counterbalances the chapter's expectation; strengthens its caution.

**Chapter 7.** Comparison without rank gains the OECD's refusal and the ELS's specification; the evidence scale for contribution arrives from the growth sector; the funnel's own warning is quoted from its home. Strengthens.

**Chapter 8.** The service record gains the sectors' case law: release calendars with status, fixed release times, a log for surprises, retirement plans, and three documented failures of custody. Strengthens.

**Chapter 9.** Nothing new on the measure itself; the Health Index is the nearest official analogue of an index built for change, and it stalled. Opens a thread.

**Chapter 11.** The GSS's model sentence for non-significant change is the house's sentence; the fan chart finding bounds the chapter's reading of uncertainty displays. Strengthens; counterbalances.

**Chapter 12.** The peer method has an official specification; the identity line gains County Health Rankings' move to groups and the OECD's peers elsewhere. Strengthens.

**Chapter 13.** The status marks in square brackets are a floor rule in the official guidance; the dashboards guidance asks for accessibility first. Strengthens.

**Chapter 14.** The sectors' printed rules avoid meaning carried by colour alone (colour only for significance; a neutral ramp), though their displays were not audited; provenance lives in documentation pages, as the gallery found it a scroll away. Strengthens.

**Version 1, Chapter 12.** Section 11: the sector claims hold and are specified; the fold question is answered with a count and left to Carly.

---


## Gaps found while writing this chapter

| Gap | Where it bites | Interim position | Who closes it |
|---|---|---|---|
| Trust in a display is not measured anywhere read; the one randomised test measured trust in government | Truth 1 | The producers' method is adopted; the display's trust is a probe question | The build; `[Validate with users]` |
| The JHU papers' body (anomaly handling; back-distribution) | §3 | Repository README used; abstract only for the paper | A reader with library access |
| The retired UK dashboard's own documentation | §3 | Successor's documentation and blogs used | A reader with archive access |
| Fingertips' quintile rule and FAQ | §3 | API method names used | Research, when the pages return |
| Scotland's per-indicator arrow thresholds | §5 | Reported as unfindable; the lesson is the finding | None; the reformed framework may print them |
| The Health Index's status | §5 | "Not updated since June 2023; no notice" | The ONS |
| The Audience Agency's data arrangements | §6 | "No custodian named" as of 6 October 2026 | Research, by Carly's timeline |
| The Charities SORP's paragraphs | §6 | Secondary summary only | Research, from the SORP |
| The Culture and Heritage Capital multiplier warning the brief expected | §6 | Reported absent; Chapter 6's discipline stands on its own grounds | None needed |
| Fingertips' amber rule is narrower than first read: amber when a leave-one-out trend runs the opposite way | §3 | Stated as such | None needed |
| A 2025 PCOS wave | §7 | 2023 is the latest found | Research |
| The fold question | §11 | A count given; the decision is Carly's | Carly |
| The precedent record's place among twelve records | §12 | A growing list, like the boundary log | Chapter 16; `[Revisit at end]` |

---


## Design system (Style Guide v1.5) and Decision Book — conflict log

| Item | Where | What this chapter found | Status |
|---|---|---|---|
| Decision Book Ch 8 (service record): release and maintenance rules | §3, §4, §7 | Sector precedents at every line: release calendar with status, fixed time, log for surprises, retirement plan; the regulator lists the plan among the minimum | Candidate additions: *the retirement plan*; *vintages from the first release* |
| Decision Book Ch 5 / recipe card | §3, §5 | The metric page template and the 32-field record are the recipe card's sector forms; the ELS's twelve-item metadata list is the minimum | Candidate: adopt the field list |
| Decision Book Ch 7 / comparison record; Ch 12 identity line | §5 | The paired "can and cannot say" text; the refusal to aggregate with reason; County Health Rankings' groups | Candidate: *the usage text* as a required block beside any ordering |
| Decision Book DAT rules on colour and status chips | §3, §4 | Colour only for significance, amber default, blue ramp, the one-in-twenty sentence; [p] [r] [f] in square brackets not symbols | Candidate amendment; check against the design system's status-chip component |
| This book's own dagger (†) convention | §4 | The Analysis Function advises against '†' because screen readers find it hard; the book uses it in prose, not tables | Carried to Chapter 16: whether the book's own marks meet the floor |
| Style Guide §06 evidence standard: "Record uncertainty, missing data, disagreement and methodological judgement" | §4 | Ranges beside points, never hedges alone; the Health Index's count of unmeasurable change | No conflict; cite |
| Decision Book Ch 18 override log; Ch 14 boundary log | §12 | A third growing list, the precedent record | Chapter 16: whether three logs are one |
| Decision Book Ch 15 (dashboards): trust and use | §3, §8 | Trust measured as producers do or not at all; use measured only by asking | Candidate: *the two measurement rules* |
| BRIEF-v2 §6 fold note | §11 | A count: about forty mechanisms, about six already in the book | Awaiting Carly |
| ARG-12 (from Chapter 12) | — | Unchanged | Awaiting Carly |

*End of Chapter 15, draft 2.*
