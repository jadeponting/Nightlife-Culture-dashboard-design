# Working record · Chapter 14 — Where evidence meets expression

*How this chapter was made. These sections stood in the chapter at draft 2 and were moved here, word for word, on 14 October 2026 when the book was finished. They are the record of the method: what the chapter expected against what it found, what it did to the chapters before it, the gaps it met, where it met the design system and the Decision Book, and the loose ends it flagged. Nothing here is a rule; the rules are in the register, the open choices in the decision log, the probes in `03-tests/PROBES.md`.*

## Before you start

This is the fourteenth chapter of a research book written for Nightlife Culture, a creative policy studio led by Carly Heath, about how dashboards work and why. The book exists to support the Vibe Map — a planned public, non-commercial, interactive account of the people, activity, value and support systems that sustain a place's nightlife culture, built first for the West of England. You do not need to have read the earlier chapters. Where this one leans on them it says so and gives the finding in a line, and it argues from its own sources.

The chapter's conventions are the book's. Every finding is marked by **kind** — *Standard* (a published rule from a standards body, a regulator, a design system or a method text, with the sub-kind named: Standard (W3C), Standard (regulator), Standard (official statistics), Standard (design system), Standard (method)), *Evidence* (a measured result, with what was measured and on whom), *Evidence of method* (a published procedure whose results are reported), *Reading* (this book's interpretation of evidence or standards), *Practice* (what a named project, museum, newsroom or practitioner does, read for method), or *Nightlife Culture* (the house's own position) — and by **tier**: *Fixed* (holds in any dashboard), *Adaptable* (holds unless a stated reason overrides it) or *Decorative* (open). "Fixed as a stance" means the house has decided it and the chapter gives the grounds; "Fixed as a procedure" means the rule is a thing to do. A dagger (†) marks a figure or quotation taken from an abstract or a secondary account rather than from the paper's body; "secondary" marks a source read only through another; "(read once)" marks a quotation returned once by the fetch tool without a presence check. Findings in the body carry their kind in italics at the end of a paragraph; tiers are given in the rules table. Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0.

This chapter is about a line, not about what to put on either side of it. The brief's sixth question asks how the creative layer sits on the evidence layer, and asks for "the boundary rules: what must stay true under any creative treatment … Not the creative decisions — the line they may not cross." So the chapter never says what the Vibe Map should look like, which colours it should use, what register its type should carry or what its opening image should be. It says what any treatment must leave intact, how that is tested, what the evidence says expression buys and cannot buy, what the conventions of plainness themselves do, and what the strongest expressive work in the field does when read for what each piece breaks. Where a sentence could be read as a design decision, it is a method for making one.

The chapter's working words. The *evidence layer* is everything in a display that makes or supports a claim about the world: the data, the encodings that carry it (position, length, colour, area, motion where it means something), the titles, the units, the sources, the dates, the gates on a comparison and the written account. The *expressive layer* is everything else that a designer adds on purpose: register, palette beyond the encoding, type beyond legibility, illustration, pattern, sound, motion that does not mean anything, pacing, and the form chosen for its feel. The *removal test* is the procedure this chapter formalises: take the expressive layer away — in version 1's four words, *mono, silent, still, undressed* — and check that the evidence layer still expresses all of the data and only the data. *Expressiveness* and *effectiveness* are Mackinlay's 1986 names for two different questions about a graphic — whether it can say exactly what the data says, and how well a human can read what it says — and the chapter uses them as the formal names of the house's tier test. An *anthropographic* is a chart whose marks are made to look like the people they count. *Affective design* is the field's term for designing a display to carry a feeling. *Display polarity* is whether text is dark on light (positive) or light on dark (negative); *contrast polarity* is the same thing said of a chart. *Redundant encoding* is carrying one variable in two visual channels at once. A *legibility index* is the sign trade's ratio of reading distance to letter height. *Register*, on its own, means tone and style — the look a display wears; where this book names a log (the *failure register*, the Decision Book's *rule register*) it says "log" or "register" with its qualifier, and the record this chapter leaves is called the *boundary log* to keep the two apart. The *precise twin* is the Decision Book's rule that any expressive form ships beside the same data in a precise, standard form; the *committee export* is version 1's name for the same thing at the scale of a whole page. The *tier test* is the Decision Book's first move on any disagreement: establish whether a rule is Fixed, Adaptable or Decorative before arguing about it. The *floor* is Chapter 13's name for the accessibility requirements the house adopted — keyboard operation, visible focus, zoom, semantic structure, generated alt text, user override of colour, contrast and font, and observed testing. The *cut-out rule* is Chapter 12's: a chart that may be screenshotted carries its title, unit, source, base, address, snapshot date and any gate on the image itself. The *identity line* is Chapter 12's stance that a place's people are never ranked by a condition. A *gate* is the condition a comparison must meet before it is shown (Chapter 7); a *base* is the denominator a figure rests on. The *probes* are the small working prototypes the studio plans to test with its user groups. The *two-audience test* is version 1's requirement that a display serve a committee room and a dancefloor at once. The *records beneath the dashboard* are the ten documents earlier chapters left, one each: the provenance set (Chapter 4), the recipe card (5), the claim record (6), the comparison record (7), the service record (8), the measure record (9), the safeguards record (10), the face sheet (11), the recognition record (12) and the accessibility statement (13). *Decorative* has two official senses that the chapter keeps apart: ornament, in the plain meaning; and the technical status a design system or the W3C gives to an image that carries no information and may be skipped by assistive technology. A *specific sensory experience* is the W3C's third category, between information and decoration, for content "that words cannot fully capture" (read once). The *gallery* is version 1's set of studied exemplars, audited live for this chapter. The *evaluated exception* is version 1's name for the one gallery entry with a published evaluation. "Version 1" is the first draft of this book, archived; its Chapters 12 (*The gallery*) and 13 (*Make it look like art*) are this chapter's predecessors and are cited as sets of positions to test.

A note on sources. Four research agents worked with web search rationed to thirty calls each. Several sources could not be reached and are marked where they appear: the full texts of Lau & Vande Moere 2007 and Vande Moere & Purchase 2011 (abstracts only); Kostelnick 2008; Munzner's 2014 textbook (her slides and two course pages instead); Tufte's books (no reliable scan, so his rules are quoted only as others quote them, or from his own 2006 forum post); the papers of Morais et al. 2020 and 2021 (their published analysis pages and a secondary account instead); and the newsroom sites of the BBC, the *New York Times*, the *Guardian*, Reuters, the *Washington Post* and the *Financial Times*, which the fetch tool could not read, so no BBC interactive was audited and the FT's vocabulary was read from its public code repository. The gallery audit could read text but not pixels: colour, decoration, hover behaviour and keyboard operation are reported only where a page says them in words. Everything quoted was checked by presence re-fetch except where "(read once)" says otherwise, and the verifier's pass is recorded in the log.

---


## 10 · The symmetry test

Version 1's Chapters 12 and 13 took positions; this section tests each against what the chapter found, and says whether the position stands, is re-based, is re-tiered or falls.

**"The art lives in the decorative tier and the register; load-bearing meaning never lives only there." (Fixed.)** Stands, and acquires its formal name: Mackinlay's second clause, Munzner's encoding level, Kosara's "must be able to stand on its own" (read once). Re-based from an axiom to a definition.

**"Every expressive form names its purchase and ships the precise version alongside." (Fixed.)** Stands, re-based. Section 5's Ottley finding is that a twin beside a form is not thereby read, so "alongside" becomes "one step away, with the finding stated in words on the form"; and the purchase it may name is bounded by the evidence — engagement, mood, recognition, register, and memorability from Chapter 3 — and may not be "persuasion" or "empathy", which are not measured to be bought.

**"No beauty exemption from the accessibility audit." (Fixed.)** Stands, and gains an institutional counter-example: the field's own prize has no accuracy criterion. The house audits in the opposite order.

**"The prototype genre is the culture's visual tradition, not the dashboard's; the claim decides the genre." (Fixed.)** Re-tiered to Adaptable, as a stance the house holds with named grounds, because the evidence for it is Chapter 11's prototypicality line (which is about speed of judgement, not about accuracy or trust) and the counter-evidence is the focus-group sentence about unfamiliar forms and the glance-cost ratio. The genre is the house's to choose; what is Fixed is that the evidence layer passes the removal test in whatever genre it wears.

**"Titles and text carry the message so that decoration can be free." (Fixed.)** Stands; it is the settled embellishment line (Chapter 3) and the gallery's observed pattern, and the official bodies require a message-bearing title (Analysis Function; GOV.UK; the ONS: "The chart title should describe the main trend you want the chart to show to the user.").

**"The poster discipline governs headlines: five words where possible, ten at most." (Fixed.)** Re-tiered to Adaptable. The mantra is the house's; the measured numbers are a letter-height ratio, three or four words a glance, four seconds for four to eight words, and capitals at threshold. What is Fixed beneath it is that a headline read in passing has its letter height set from its reading distance and its finding restated at reading distance in the body.

**"Salient distinctiveness over normalised ornament." (Adaptable.)** Stands, with a price now attached: the glance cost of an unfamiliar form, and the image-not-information finding.

**"Strong evidence is never made to look weaker by timid design." (Adaptable.)** Stands, and acquires a third sentence beside it: plain design can make weak evidence look stronger too. The three together are the house's evidence standard as this chapter reads it.

**"The expressive-moves palette, each priced." (Adaptable.)** Stands, and section 11's register is the pricing form. One row of version 1's palette is withdrawn on evidence: "the human figure as a mark" may still be used for recognition but may not be priced as buying empathy or giving.

**"The committee export at lower volume." (Adaptable; version 1 flagged it as having no located precedent.)** Stands and now has precedents: the Analysis Function's plain-text version of an infographic; the Doughnut's bar chart in Figure 2; Chalabi's computed chart beneath the drawing. It is the removal test's *undressed* output kept as a deliverable.

**"The two-audience test."** Stands as a stance; Chapter 11 and this chapter give it no measurement and the probes can.

**"The removal test: mono, silent, still, undressed." (Fixed, as a procedure.)** Stands, formalised in section 6, with the fifth check (the dressed and stripped versions say the same thing) added from the DWP case and the Doughnut's caption, and the deaf reader's requirement attached to *silent*.

**"The gallery's strong-work pattern: words and structure carry the message; craft spent on one authored thing; interaction optional." (Fixed.)** Holds under live audit, with one addition: provenance a scroll away is the gallery's practice and the house's rule is stricter.

**"The failure pattern: gated results, undisclosed recipes, platform dependency, unmaintained contents." (Fixed.)** Holds; both incumbents have drifted further since version 1 read them.

**"The evaluated exception is the standard for this dashboard's probes." (Adaptable.)** Holds, and the standard is now specified and qualified: no control; self-report against logs; materials a reviewer could not open. The house can meet it and add the comparison.

**"Definition-as-interaction and the misconception quiz as probe candidates." (Adaptable.)** Hold, with Gapminder's method verified and its ranking of households by income named as the part the house would not import.

**"The institutional proof exists: an expressive rendering of noise data hangs in MoMA's permanent collection."** Re-stated to what the record says: MoMA holds *Noise Pollution* as a "Digital image", "Gift of the designer", object 98.2023, "Not on view", with no label and no exhibition on its record. Custody, which proves that institutions file such work as design; not proof of anything about readers.

**The house's own: the Skiddle-call instruction; the five-word mantra; Style Guide §06; the Decision Book's Chapters 7, 10 and 18.** The instruction and the mantra enter as the house's stance and its grounds are given above; §06 is read as cutting both ways; Chapter 7's "Name the purchase. Show the precise version that ships alongside. Pass Chartability's shortlist. And read the text alternative on its own" is the removal test's ancestor and stands; Chapter 18's tier test is Mackinlay in plainer words and stands.

---


## Open questions and flags

`[Further research]` The full texts of Lau & Vande Moere 2007, Vande Moere & Purchase 2011, Kostelnick 2008 and Vande Moere et al. 2012 (the style study, whose n was not obtained); Munzner's textbook pages for the two principles; Tufte's books for the rules quoted here only at second hand; Morais et al.'s paper PDFs; the Garvey 1997 full text and the 2024 case study at source; Chevalier et al.'s full role list for animation; Shi et al. 2021; the Traffic Signs Manual's x-height table.

`[Further research]` A reader study of an expressive form against its precise twin that measures what each reader takes from the data — the test this chapter asks the probes to run — does not exist in the literature read. Arunkumar et al. is the nearest, and it is correlational.

`[Further research]` Gomasta et al. (arXiv 2601.17893, January 2026), on music in data videos — preregistered; abstract only: default music made a video more persuasive, music did not increase engagement, and participants reported more intense emotions without music. Bears on *silent*; unread beyond the abstract. And arXiv 2607.01593 ("Made to Feel", on how designers bring emotion into affective visualisation) returned a rate limit and was not read.

`[Prototype flag]` The deaf reader's document for any sound the probes carry; the boundary log as a working file; a probe designed to meet and exceed the evaluated exception's standard; the two-audience test, which has no measurement in this book.

`[Validate with users]` The glance cost of any form the house invents, against a bar; the stripped-against-dressed comparison for each expressive element; the dark register against the light one, by reader, since the better polarity is individual.

`[Revisit → Ch 15]` The gallery's audited pattern is this chapter's; Chapter 15 reads sector by sector and should carry the four removals and the provenance-a-scroll-away finding into each sector it reads.

`[Revisit → Ch 16]` The boundary log as the override log's specialisation; whether the tier vocabulary adopts "specific sensory experience"; the three-sentence evidence standard.

`[Revisit at end]` Whether the eleven records are one document, and whether a log belongs on the page or in the repository with a declaration on the page.

`[Counterbalance → Ch 11]` The plain-to-trust path beside the beauty-to-trust path. `[Counterbalance → Ch 12]` The orthodox look is available to anyone and is not the house's evidence of trustworthiness. `[Counterbalance → Ch 3]` The embellishment line's "memorable" is confirmed and bounded: image-rated displays are liked more and convey less of their message.

For the adviser, none: this chapter reports no law beyond the W3C's criteria, which Chapter 13 already placed in the Regulations' frame.

---


## Looking back

**Chapter 0.** The tier vocabulary now has a formal ancestor (Mackinlay) and a missing category (the W3C's specific sensory experience). Strengthens; opens a thread for Chapter 16.

**Chapter 1.** The exemplar-first opening is confirmed by the gallery audit as the strong-work pattern, with the official exemplar's landings as the exception. Strengthens.

**Chapter 2.** The persuasion line stands; the affect evidence adds that the ornament does not persuade, the claim and the frame do. Strengthens, and bounds.

**Chapter 3.** The embellishment line stands and is bounded: "memorable" is confirmed; "image-rated" displays convey less of their message. Counterbalances.

**Chapter 4.** The provenance set is what the source-line convention promises; the gallery keeps provenance a scroll away. Strengthens the rule and names its rhetoric.

**Chapter 6.** The claim in the title is the house's declared point of view, which is the answer to Viégas and Wattenberg's question. Strengthens. The uncertainty rule gains a register (the drawn mark) that can carry it.

**Chapter 7.** The frame is what the two-dimensional convention conceals. Strengthens.

**Chapter 8.** Both incumbents have drifted further; the service record's case law grows. Strengthens.

**Chapter 10.** One mark per person: the safeguards record's cost has no measured return in empathy or giving. Strengthens.

**Chapter 11.** The beauty-to-trust path has a plain-to-trust twin; prototypicality is re-read as speed of judgement and the genre re-tiered. Counterbalances; the two-audience test is still unmeasured.

**Chapter 12.** The orthodox look is explained and is not the house's evidence; the cut-out rule is confirmed by the Census page's furniture and by a chart publisher's logo rule; the humanised mark's whole-unit condition arrives. Strengthens; counterbalances the "orthodox" reading.

**Chapter 13.** The deaf reader is placed; the description rule and the two senses of "decorative" are re-read as the removal test in markup; the floor's colour and contrast override gains its measured reason. Strengthens.

**Version 1, Chapters 12 and 13.** Section 10: most positions stand; two are re-tiered (genre; headline count); one is re-stated to what the record says (MoMA); the removal test is formalised and gains its fifth check; the committee export gains precedents; the evaluated exception is specified and qualified.

---


## Gaps found while writing this chapter

| Gap | Where it bites | Interim position | Who closes it |
|---|---|---|---|
| No reader study compares an expressive form with its precise twin on what readers take from the data | Truth 2; the probes | Arunkumar 2023 (correlational) as the nearest; the probes run the comparison | The build; `[Validate with users]` |
| The two-audience test has no measurement anywhere in the book | Version 1 Ch 13; this chapter §10 | Held as a stance; a probe can measure it | The build |
| Tufte's rules quoted only at second hand; "within reason" unlocatable | §6 | Quote only the 2006 note in his hand; mark the rest secondary | Research, from the physical books |
| Lau & Vande Moere and Vande Moere & Purchase full texts | §3 | Abstracts only; axes and triangle not printed as the authors' | Research |
| Morais 2020 and 2021 paper PDFs | §5 | Analysis pages and Sorapure; effect and n confirmed at the analysis page | Research (HAL/ACM) |
| The BBC's postcode interactives not audited | §7 | Reported as not read; method via the Handbook | A reader with access, or Chapter 15 |
| Whether Chalabi's published pieces carry a source line | §5, §7 | Not reported | A reader with access |
| The flowchart's OSF materials | §7 | Qualified as the Open Practices Review did | Research, when the component opens |
| The tier vocabulary lacks the W3C's "specific sensory experience" | §6, §11 | Used in the register; adoption left to Chapter 16 | Chapter 16; the Decision Book |
| Gallery audit read text, not pixels | §7 | Colour, hover and keyboard reported only where a page says them | A visual audit, if wanted |
| "Seven words" has no source | §5 | Mantra re-tiered Adaptable; measured numbers given | None needed |
| Kineticharts' comprehension count: the paper names four aspects and asks three questions | §5 | Reported as three | None needed |
| Mackinlay's Figures 14 and 15 not machine-readable | §3 | Ranking not printed as a list | From the printed figure |

---


## Design system (Style Guide v1.5) and Decision Book — conflict log

| Item | Where | What this chapter found | Status |
|---|---|---|---|
| Style Guide §06, "Strong design must never make weak evidence look stronger than it is" | §4, §11 | Stands; needs two companions — timid design never makes strong evidence look weaker (version 1), and plain design never stands in for a record (this chapter, from Kennedy et al.) | Candidate addition: *the three-sentence evidence standard* |
| Decision Book Ch 18 tier test (Fixed / Adaptable / Decorative) | §3, §6 | Fixed = expressiveness, Adaptable = effectiveness, Decorative = what neither sees; a fourth category exists in the W3C ("specific sensory experience") with an identification duty | Candidate addition; no conflict |
| Decision Book Ch 18, BRK-07 "Run the removal test for the relevant chapter" | §6 | Formalised: four removals and a fifth check; a ten-line register | Candidate: *the boundary log* as the removal test's log |
| Decision Book Ch 7, "Name the purchase. Show the precise version that ships alongside." | §5, §10 | "Alongside" is not enough (Ottley): one step away, finding in words on the form; purchase bounded to what is measured | Candidate amendment |
| Decision Book Ch 7, "Beauty as an accessibility exemption. The most common failure in award-winning work." | §7 | Confirmed institutionally: the prize's eight criteria omit accuracy | No conflict; cite |
| Decision Book Ch 18, "Treat 'it looks better' as a reason. It is a valid reason in the Decorative tier and nowhere else." | §12 | Stands; the Decorative tier is unshrunk by this chapter | No conflict |
| Decision Book colour.md: Decorative grounds carry "no contrast requirement beyond any text sitting on it" | §5 | Text on a dark ground has a measured legibility cost beyond contrast; a light alternative is required | Candidate amendment: polarity choice |
| Version 1 Ch 13 rule, genre Fixed | §10 | Re-tiered Adaptable | Carried to Chapter 16's register |
| Version 1 Ch 13 rule, five/ten words Fixed | §10 | Re-tiered Adaptable; distance and seconds Fixed beneath it | Carried to Chapter 16's register |
| Version 1 Ch 13, "the human figure as a mark" in the expressive palette | §5, §10 | May serve recognition; may not be priced as empathy or giving; whole units | Candidate amendment |
| Decision Book ARG-12 (from Chapter 12's log) | — | Unchanged by this chapter; still in direct conflict | Awaiting Carly |
| Style Guide §06 "Generous… Defining people or places only through failure or need" | §7 (Dollar Street) | A street ordered by income is the thing the rule forbids for places; the method is imported, the ranking is not | No conflict; cite |

*End of Chapter 14, draft 2.*
