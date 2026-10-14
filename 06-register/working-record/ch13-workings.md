# Working record · Chapter 13 — Accessible as the good version

*How this chapter was made. These sections stood in the chapter at draft 2 and were moved here, word for word, on 14 October 2026 when the book was finished. They are the record of the method: what the chapter expected against what it found, what it did to the chapters before it, the gaps it met, where it met the design system and the Decision Book, and the loose ends it flagged. Nothing here is a rule; the rules are in the register, the open choices in the decision log, the probes in `03-tests/PROBES.md`.*

## Before you start

This is the thirteenth chapter of a research book written for Nightlife Culture, a creative policy studio led by Carly Heath, about how dashboards work and why. The book exists to support the Vibe Map — a planned public, non-commercial, interactive account of the people, activity, value and support systems that sustain a place's nightlife culture, built first for the West of England. You do not need to have read the earlier chapters. Where this one leans on them it says so and gives the finding in a line, and it argues from its own sources.

The chapter's conventions are the book's. Every finding is marked by **kind** — *Standard* (a published rule from a standards body, a regulator, a design system or a method text, with the sub-kind named: Standard (W3C), Standard (law), Standard (EU law), Standard (regulator), Standard (official statistics), Standard (design system)), *Evidence* (a measured result, with what was measured and on whom), *Reading* (this book's interpretation of evidence or standards), *Practice* (what a named project does, read for method), or *Nightlife Culture* (the house's own position) — and by **tier**: *Fixed* (holds in any dashboard), *Adaptable* (holds unless a stated reason overrides it) or *Decorative* (open). "Fixed as a stance" means the house has decided it and the chapter gives the grounds; "Fixed as a procedure" means the rule is a thing to do. "Evidence (official statistics)" marks a figure from a national survey. A dagger (†) marks a figure or quotation taken from an abstract or a secondary account rather than from the paper's body; "secondary" marks a source read only through another; "(read once)" marks a quotation returned once by the fetch tool without a presence check. Findings in the body carry their kind in italics at the end of a paragraph; tiers are given in the rules table. Flags in square brackets — `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]`, `[Counterbalance → Ch n]` — are defined in Chapter 0.

This chapter reports law. It reports what a statute, a regulation, a code or a piece of official guidance says, with its wording, its section and its date as read on 6 October 2026. It never says what the law requires of the Vibe Map or of the studio; it quotes the texts that bear on a private, non-commercial provider of a public information service and leaves their application to the studio's own adviser, and it says so wherever a reader might otherwise take a sentence as advice.

The chapter's working words. *WCAG* is the W3C's Web Content Accessibility Guidelines; version 2.2 is a W3C Recommendation, republished 12 December 2024, whose rules are *success criteria* at three *levels*, A, AA and AAA; a page *conforms* at a level when it meets every criterion at that level and below, whole, not in part. A *conforming alternate version* is the standard's name for a separate accessible version of the same content; the W3C calls it a fallback, and section 3 quotes it. A *text alternative* is text programmatically tied to something that is not text; for a chart the W3C asks for two parts, a *short description* that names it and a *long description* that carries its information; an *alt attribute* is the HTML field that usually holds the short one. *Assistive technology* is software or hardware a disabled person uses to read or operate a page; a *screen reader* is the kind that speaks or brailles what is on it. *ARIA* is the W3C's vocabulary of roles and properties that tells assistive technology what a thing on a page is; *COGA* is the W3C's note on content for people with cognitive and learning disabilities. A *navigable structure* is a chart exposed to a screen reader as a tree the reader steps through, rather than as one sentence or one flat table. *Sonification* is data rendered as non-speech sound; an *audio graph* is a platform's way of letting a screen reader play a chart. The *table twin* is Chapter 8's rule that every map, and Chapter 11's that every dense chart, has the same figures as a table reachable before any script. The *four-level model* is a published account of what a chart description can contain, from the chart's looks (level 1) through its statistics (2) and its trends (3) to its meaning in the world (4); section 5 gives it. The *Regulations* are the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018, S.I. 2018/952, as amended; *the Act* is the Equality Act 2010; the *anticipatory duty* is the name the Act's explanatory notes give to the duty to make reasonable adjustments for "disabled persons generally", in advance of any individual asking. The *three user groups* are the studio's testing groups, named in its design repository and not here. An *overlay* is a third-party script added to a site that claims to make it accessible by altering the page for the visitor. The *ELS* is the ONS's Explore Local Statistics service (Chapter 12). The *floor* is version 1's name for the set of accessibility requirements the house adopted from its design system and its Decision Book — keyboard operation including chart elements, visible focus, 200 and 400 per cent zoom, semantic structure, alt text generated from the current state, user override of colour, contrast and font, and observed testing — which this chapter maps to the criteria. *View*, *layout* and *route* are used as in Chapter 11: a view is one chart or panel with its data, specification and selection; a layout is the page as presented at one screen size; a route is one way a reader reaches a view's content. "Version 1" is the first draft of this book, archived; its Chapter 11 is this chapter's predecessor and is cited as a set of positions to test.

A note on sources. Four research agents worked with web search rationed to thirty calls each, and the fetch tool cuts long single-page specifications, so the W3C's normative text was read through its Understanding pages, which reproduce it, and the United Kingdom's law through legislation.gov.uk regulation by regulation. Three things could not be read at source and are marked: the body of the EHRC's new 2026 Code's chapter on the anticipatory duty; the CSS specification's definition of the reduced-motion preference; and the aria-live property's table. Everything quoted was checked by presence re-fetch except where "(read once)" says otherwise, and the verifier's pass is recorded in the log.

---


## 10 · The symmetry test

*The floor inherited whole.* Version 1: Fixed, from the Decision Book's Chapter 15 and the Style Guide's §13. **Holds**, and is now mapped to the criteria that each item meets, with 2.2.2 (auto-update) and 4.1.3 (status messages) added, which the floor did not name.

*Tooling chosen against the floor in week one.* **Holds, strengthened**: canvas text is images of text under 1.4.12; official statements name the tools whose dashboards fail; the Analysis Function says open languages "give greater control".

*Charts as navigable structure, not alt-sentence pictures.* **Holds as a route, re-weighted**: the one study's significant result favoured the table on ease; the structure is built second and tested; the description and the table come first.

*The accessible tree as a build step.* **Holds**; the tooling exists for Vega-Lite and Observable Plot specifications.

*State announcements reuse version 1's plain wording for data states.* **Holds, sharpened**: one brief status message per change, polite, never the view or the sentence read unasked; "chatty" is the standard's own warning.

*Audio designed once, serving access and product.* **Holds as a stance** with the evidence attached: overview and trend with training; half find it somewhat beneficial; not maps. The claim that the sound of a place serves a blind reader and a curious reader identically is unmeasured and stays a design intention `[Validate with users]`.

*Data sonification a labelled probe.* **Holds.**

*The generated written story as the guaranteed non-visual route.* **Holds, strengthened**: it is the W3C's long description at Lundgard's levels 2 and 3; it is official practice's fallback.

*The community's phone-read test as the reading-level standard.* **Holds as a house standard**, with the observation that no official reading-age figure has a source and COGA's "lower secondary" is the W3C's; the house's test is a procedure with people, which is better than a number.

*Chartability per release.* **Holds as a procedure**, priced: 50 heuristics, 14 critical, two to eight hours for a novice; evaluated on auditors' confidence, not readers' outcomes; the keyboard walk and the screen-reader read are done as well, not instead.

*Observed testing with disabled users of the real audience.* **Holds**; the Design System's "user research must include disabled people"; the standard's "User testing should be carried out".

*The distribution argument recorded once.* **Re-based**: the Regulations exempt unfunded, uncontrolled third-party content; the argument stands as funding and reputation, not inheritance; recorded once, in the new form.

*Accessibility outranks brand in the hierarchy.* **Holds**; the W3C's "essential" exception is narrow and the house claims it for nothing but the map's pins.

*No parallel accessible version.* **Holds as the house's rule, on the standard's stated preference**: "fallback option"; "preferred method of conformance is to make all content directly accessible"; the standard permits what the house forbids itself.

*The blind-fan test.* **Holds, re-written by the evidence**: the question is not what the chart looks like but what the trend and the figures are, and for a map where — because that is what blind readers rank most useful in a description and what a chart carries for a sighted reader; the answers are compared on those things, and the two groups' different ranking of interpretation is the reason the account, not the description, carries it.

*"The good version and the accessible version keep turning out to be the same build."* **Half-confirmed**: measured for whole pages in two experiments, for typefaces, for captions; counter-measured for easy-to-read language; unmeasured for charts. Kept as a stance with its gap named.

*The house's.* The Style Guide's §13 floor is the criteria list with the standard's words beside each; §02's hierarchy resolves the brand-against-access cases as before; §04's register meets COGA's clear-words pattern and gains the 1,500-word check; the Decision Book's Chapter 15 rules ("nothing load-bearing in a tooltip"; the non-interactive route) are 1.4.13 and the written account. The Vibe Setting Framework's phone-read test is cited as the community's standard and not reproduced.

*The studio's own statement.* The chapter makes publishing an accessibility statement a house procedure, in the public sector's form, as the record of this chapter. **Fixed as a procedure**; whether the Regulations' own statement duty reaches the studio is not the chapter's to say.

---


## Open questions and flags

- `[Further research]` **The EHRC 2026 Code, Chapter 7**, at source: the anticipatory duty's paragraphs, carried here from a secondary site.
- `[Further research]` **The CSS reduced-motion definition** at source; the aria-live property table; EN 301 549 v4.1.1's clause 9 body.
- `[Further research]` **The Schmutz papers at source** — the 2016 and 2017 experiments beyond their abstracts, the 2018 paper on age and device, and the 2019 easy-to-read cost.
- `[Further research]` **Biggs et al. 2022's results** and any independent evaluation of a text map.
- `[Further research]` **A controlled comparison of a table against a description against a structure for the same chart, with time and accuracy**; none found.
- `[Further research]` **UK prevalence figures with sources** for colour vision deficiency, dyslexia and vestibular disorders; the charity figures are unsourced.
- `[Further research]` **Whether any UK regulator has spoken on overlay widgets.**
- `[Further research]` **BS 8878's status**, which the publisher shows as current and the trade says is superseded.
- `[Prototype flag]` **Convergence for charts.** Whether the accessible routes change what sighted readers take from a view; the experiment the literature has not run, and which a handful of sessions can begin and not finish.
- `[Prototype flag]` **A text route for geography** on the map: whether it is used and what it changes.
- `[Prototype flag]` **The frame's eight items at phone size**, for legibility (Chapter 12's question).
- `[Prototype flag]` **Status-message wording**: one message per change, tested for "chatty".
- `[Validate with users]` **The blind-fan question** with readers from the user groups: what they say the trend and figures are, by which route.
- `[Validate with users]` **Whether the sound of a place, if ever on the page, serves a blind reader as content**; version 1's convergence claim for audio, unmeasured.
- `[Validate with users]` **The phone-read test** against COGA's lower-secondary summary.
- `[Validate with users]` **Whether screen-reader users find the long description** in body text beneath the chart, and whether the short description's trend reads as a repeat.
- `[Revisit → Ch 14]` What a creative treatment may do under the floor: motion, texture, density, colour — the "essential" exception and the hierarchy; and what a dashboard about sound owes a deaf reader (a transcript or caption for any audio content; 1.4.2), which this chapter did not treat.
- `[Revisit → Ch 16]` The statement, the three walks and Chartability as release gates; the rules register's accessibility rows.
- `[Revisit at end]` Ten records; the statement as the public one. The 60-second version's length (raised a ninth time).

---


## Looking back

- **Strengthens** Chapter 1's "it fails if people dont use it" with the measured gap for screen-reader users and the survey's 73 per cent; its "a dashboard is a form to be justified" with the Analysis Function's "rarely meet".
- **Strengthens** Chapter 2's official reader: the public body's own statement, its exemption for third-party content, and its funding limb.
- **Strengthens** Chapter 3's classification and completes it (conformance; alternate versions; the interactive criteria; ARIA's absence; COGA's body); **corrects** its "four approaches" for the WAI tutorial, now three with no longdesc `[Counterbalance → Ch 3]`.
- **Strengthens** Chapter 4's table rules as adopted standards (the Analysis Function's spreadsheet rules were read and are in the ledger).
- **Strengthens** Chapter 7's worded comparison and Chapter 9's bands as COGA's "non-numerical concepts".
- **Strengthens** Chapter 8's table twin and figures-before-script with 1.4.10's exception and its limit, and the Regulations' map exemption; its tooling rule with 1.4.12's canvas sentence.
- **Strengthens** Chapter 10's statement-like records with the public sector's statement form; its "reported, not advised" with this chapter's own.
- **Strengthens** Chapter 11's sentence as the long description at levels 2 and 3; its "nothing crucial behind hover" with 1.4.13 and the Tableau tooltip failure; its status rule with 4.1.3; **corrects** its attribution of "Dashboards rarely meet full accessibility requirements" from the ONS to the Analysis Function `[Counterbalance → Ch 11]`; **counterbalances** its three-phones test with the screen-reader version of it.
- **Strengthens** Chapter 12's in-frame rule by testing it against 1.4.5 and finding it met under a condition, which is now the rule's condition; its errors channel as the statement's contact line; its clear-words discipline with COGA's 1,500.
- **Version 1:** the floor mapped to criteria and extended (2.2.2; 4.1.3; 2.4.11; 2.4.13; 1.4.12); "reduced cognitive load" corrected to the study's result; the distribution argument re-based; the blind-fan test rewritten by the four-level model; the convergence claim half-confirmed and its gap named; the Regulations' numbering corrected; the 2011 Code replaced by the 2026 one.
- **Decision Book:** Chapter 15's rules confirmed and given their criteria; the accessibility rules gain 1.4.12, 2.2.2, 2.3.3, 2.4.11, 2.4.13 and 4.1.3; a candidate section, *The statement*; no conflict found.
- **Design system:** §13's floor is confirmed and extended; §04's register gains COGA's measurable form; the type scale meets the 18-point finding and the BDA's 12–14 and must choose; no component for a status region, a reduced-motion variant, a table-twin pattern with pagination, a long-description block, or the statement. Logged, not designed.

---


## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No controlled comparison of description, table and structure for the same chart with time and accuracy | Stated each route's evidence separately; left the order as a procedure | Amber — the chapter's fourth truth rests on three small studies and one preprint | `03-tests/`; prototype |
| Nothing measures convergence for charts | Stated the page-level evidence and the gap; flagged | Amber — the chapter's title claim | prototype |
| The EHRC's 2026 Code, Chapter 7, unreached at source | Quoted a secondary site, flagged | Yellow | a library pass |
| The reduced-motion definition, the aria-live table, EN v4.1.1 clause 9 unreached | Quoted the techniques and the Recommendation's reasons instead | Yellow | `[Further research]` |
| UK prevalence for colour vision deficiency, dyslexia and vestibular disorders has no official source | Charity and US figures, marked | Yellow | `[Further research]` |
| Reading-age figures have no source anywhere official | Replaced with the literacy survey figure and COGA's level | Yellow — the trade's number is folklore | the design-system conversation |
| Official bodies disagree on where a chart's description lives | Reconciled as the W3C's two parts; the house picks one | Yellow | design system |
| No UK regulator text on overlays; no UK website judgment | Reported the absence | Yellow | `[Further research]` |
| The search ration left the BBC's guidelines and R&D, the FT's and the Guardian's practice unread | Named them unreached | Yellow | a later pass |

---


## Design system (Style Guide v1.5) and Decision Book — conflict log

**Agrees.** §13's floor is this chapter's rules table with the criteria beside each item; §02's hierarchy ("accessibility outranks brand") is confirmed by the narrowness of the W3C's "essential" exception; §04's register is COGA's clear-words pattern and gains its measurable form; the Decision Book's Chapter 15 ("nothing load-bearing in a tooltip"; "a non-interactive route to the same finding"; observed testing with real users) is 1.4.13, the written account and the Design System's own sentence. The design system's text-outside-images preference stands for the page; Chapter 12's frame meets 1.4.5 under the condition now stated.

**Conflicts.** None found. One tension logged: the type scale's body size against the 18-point finding and the BDA's 12–14; the design system decides and records why.

**Silent on.** A status region and its wording; a reduced-motion variant for every animated component; a table-twin pattern with pagination and header cells; a long-description block in body text; a pause control for auto-updating panels; focus styling that is never obscured by the filter bar; an accessibility statement template with the twelve lines; the screen readers and platforms the house tests with. All logged for the design-system conversation.
