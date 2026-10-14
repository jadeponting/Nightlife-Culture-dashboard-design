# Read: Chapter 13 — Accessible as the good version

## A. Coverage

- File: `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch13-accessible-as-the-good-version.md`
- `wc -l`: 605 lines.
- Ranges read with the Read tool: 1–175, 176–285, 286–395, 396–505, 506–605.
- Every line was read; nothing was summarised from headings. Context did not fill.
- Context read first: BRIEF-v2 §1, §4, §5; ch00 "How a chapter teaches" and "The legend"; LIBRARY-PASS "What the pass found, in one page".

## B. What the chapter teaches

The chapter decides that the accessible version of a public dashboard is the dashboard itself, on one page per layout, with the written account, the table twin and (optionally) a navigable structure sitting beside the chart as supplementary content; it grounds that in WCAG's own conformance text rather than house taste. It separates three legs of version 1's claim (standard, law, empirical convergence), reports UK law without advising, reads the small accessible-visualisation literature at its measured size, and ends with a published accessibility statement as the chapter's record. A newcomer (an analyst, a creative technologist, a tester) would come away knowing: no WCAG criterion names a chart; a chart's description should carry type, figures and trend, not interpretation; a table carries values but not geography; the keyboard walk and zoom find what scanners miss; and "accessible is the good version" is a stance with evidence for pages and a gap for charts.

Best passages that teach well (must survive any edit):
- Lines 90–92: the conforming-alternate-version finding and its reading ("a dashboard conforms as one page per layout or not at all"; "The phrase 'last resort', which circulates, is not the W3C's"). Concrete, quoted, with a clear point of view.
- Lines 176–180 and 186: the four-level model and what the finding "is and is not", ending "the table carries values, the structure carries shape, and the description carries the trend".
- Lines 248–268 (section 8, The routes): one paragraph per route, each saying what it carries and drops; line 268 closes it: "What no route carries alone is the whole".
- Lines 272–282 (section 9): the five failures each with a test; rhythmic and usable.

Passages a newcomer could not follow:
- Line 16: the "working words" paragraph is one 600-word block. It is the right content but unparagraphed; a newcomer will skim it and miss *table twin*, *four-level model*, *floor*.
- Line 56: "the thing the brief's failure register names twice — 'people dont use it' and 'people dont trust it'" assumes the reader knows what "the brief" and "the failure register" are (Chapter 1 material; not defined here).
- Line 98: "Chapter 3 holds 1.1.1, 1.3.1 … Chapter 11 holds 1.4.13 …" is a cross-reference list that reads as bookkeeping; fine for the author, opaque to a first reader.
- Line 320: "The Style Guide's §13 floor … §02's hierarchy … §04's register … LNG and DSH rules" (line 576) are house-document section numbers a newcomer cannot look up from the book.
- Line 391: "poster above door" (line 397) and "the missed column" (line 391) are Chapter 11/12 terms used without a gloss.
- Line 346: "This chapter's tenth [record]" assumes the reader knows Chapters 4–12 each left a record.

## C. Verdict on the chapter body

**Stands.** The teaching sections do their job as written. Reasons tied to lines:
- The question (line 24) is answered by the 60-second version (lines 30–42) in the same five parts, in the same order: standard (30), chart rules (32), law (34), readers (36), official bodies (38), convergence (40). The answer comes first in each paragraph's bold lead.
- Beliefs (lines 62–78) each end with the section that tests them, and each is in fact tested there (checked: lines 64→134ff; 66→100, 178, 220; 68→190; 70→164; 72→224–228; 74→194; 76→234; 78→234).
- The numbered sections do not contradict each other. The one place the chapter argues with itself is deliberate and explained: the house's rule is stricter than the standard's preference and is marked as the house's (lines 92, 314, 330).
- The truths (330–342) restate the body with quotations and section pointers, as the structure asks; the rules table (409–441) and checklist (453–472) follow from them one-to-one.
- The nightlife illustration (385–401) is labelled and invents nothing.
- Nothing large repeats beyond the designed structure (see F).

Light fixes worth noting but not required for the verdict (fewer than 10):
1. Line 16: break the working-words paragraph into short paragraphs or a list. No wording change.
2. Line 56: gloss "the brief's failure register" in six words, or drop "the brief's".
3. Line 108: "could not be read at source this sprint" → drop "this sprint".
4. Line 90: "(Standard (W3C); the orchestrator re-fetched the fallback sentence.)" → "spot-checked" or move to Sources.
5. Line 224: "the orchestrator re-fetched the 'rarely' sentence" → same.
6. Line 154: the EHRC Code Chapter 7 passage now needs the library-pass correction (see D13).
7. Line 148 and line 174: `[Rich reference]` sits mid-prose after a kind marker; harmless, but the bracket is furniture inside body text.
8. Lines 110, 112: "aria-live" and "role=status" are the only unexplained technical terms in the body; one clause each would do.

60-second version: lines 30–42, **1,463 words** (wc on those lines, including the bold leads). It gives the answer first in every paragraph, so it does not need re-ordering; it is long because it carries quotations rather than claims. Trimming for length alone is not recommended by this brief; the chapter itself raises its length at line 496 ("raised a ninth time"), so Carly already knows. If she wants it shorter, the quotations in paragraphs 32 and 38 are the padding candidates, not the structure.

## D. Furniture and status: inventory with lines

1. **Status/draft lines under the title.** Line 3: "*Dashboard Design · Part 3: The reading experience*" (keep; it is the part label). Line 4: "*Version 2, draft 2 · 6 October 2026 · research log, Entry 13*" — status; retire or move.

2. **"Before you start"** — lines 8–18. Line 10: book/Vibe Map re-introduction (repeated from Chapter 0). Line 12: the legend repeated in full (kinds, sub-kinds, tiers, dagger, secondary, read once, flags). Line 14: the chapter's "reports law, never advises" rule — this one is chapter-specific and worth keeping somewhere in the body (it is repeated at 136 and 164, so it could be dropped here). Line 16: working words — chapter-specific, keep but reformat. Line 18: "A note on sources" — process ("Four research agents … rationed to thirty calls each … the verifier's pass is recorded in the log"); move to Sources or retire.

3. **"Where the choice is yours"** — lines 367–381. Every open choice, as a question, with the chapter's stated position:
   - Whether to build a navigable structure, an audio route or a "where" route for the map, and when? Position: description and table are rules; "the order after the first two is the studio's" (369).
   - Which screen readers, browsers and platforms to test with? Position: the WebAIM survey shares are the evidence; the GOV.UK Design System's list is a precedent (371).
   - Which sans serif, and which size between 16 and 18 px? Position: a sans serif at a measured size; the design system's tokens decide and record why (373).
   - How does the reduced-motion page look? Position: open, "provided nothing crucial moved in the first place" (375).
   - Does the frame's provenance text fit a phone? Position: met for the criteria (section 7); legibility left for the prototype (377).
   - Which reading-level test: the community's phone-read test, COGA's lower-secondary summary, or both? Position: none stated (379).
   - Whether to seek the adviser's view now on the Act's duty, "funded", and the consequences of a published partial-compliance statement? Position: "the chapter reports and does not advise" (381).

4. **Other places the chapter asks for a decision or awaits steer.**
   - Line 164: "What 'funded' covers, and whether any of this touches the Vibe Map, is the studio's adviser's question."
   - Line 322: "whether the Regulations' own statement duty reaches the studio is not the chapter's to say."
   - Line 346: "whether they are one document is for the end of the book `[Revisit at end]`."
   - Line 373 / 603: "the design system decides and records why" (type size).
   - Line 513: "the type scale … must choose."
   - No occurrence of "steer", "awaits", "TBD", "has not chosen". "Carly" appears once, line 10 (the re-introduction).

5. **"The symmetry test"** — lines 286–322 (section 10). Seventeen italic-led paragraphs testing version 1's positions and the house documents. Process furniture by the brief's definition; candidate to move whole. Note two findings inside it a reader might want kept in body: line 310 (distribution argument re-based; already in section 4 at 162–164) and line 318 (convergence half-confirmed; already at 212 and truth 7). Nothing is lost by moving it.

6. **"Open questions and flags"** — lines 476–496. Counts: [Further research] 8 (478–485); [Prototype flag] 4 (486–489); [Validate with users] 4 (490–493); [Revisit → Ch 14] 1 (494); [Revisit → Ch 16] 1 (495); [Revisit at end] 1 (496); [Rich reference] 0; [Counterbalance] 0 in this section.
   - 486 [Prototype flag] Convergence for charts: do the accessible routes change what sighted readers take from a view.
   - 487 [Prototype flag] A text route for geography on the map: used, and what it changes.
   - 488 [Prototype flag] The frame's eight items at phone size, for legibility.
   - 489 [Prototype flag] Status-message wording: one per change, tested for "chatty".
   - 490 [Validate with users] The blind-fan question with readers from the user groups.
   - 491 [Validate with users] Whether the sound of a place serves a blind reader as content.
   - 492 [Validate with users] The phone-read test against COGA's lower-secondary summary.
   - 493 [Validate with users] Whether screen-reader users find the long description beneath the chart; whether the short description's trend reads as a repeat.
   - These likely already sit in PROBES.md; not checked here (outside the brief's file list).
   - Line 496 also carries a status note: "The 60-second version's length (raised a ninth time)" — process, retire.

7. **"Looking back"** — lines 500–513. Fourteen bullets against Chapters 1–12, version 1, Decision Book and design system. Two carry corrections to other chapters (504: Ch 3 "four approaches" → three; 509: Ch 11 misattribution of the "rarely" sentence). Move whole to the working record; the two corrections need to reach Chapters 3 and 11.

8. **"Gaps found" table** — lines 585–595, 9 rows (older four-column form with coloured cost).
   - Real knowledge gaps a reader needs (keep in text, already stated in body): row 587 (no controlled comparison of routes), row 588 (no convergence measurement for charts), row 591 (no official UK prevalence for CVD/dyslexia/vestibular), row 592 (reading-age figures unsourced), row 593 (ONS vs Analysis Function on description placement), row 594 (no UK regulator on overlays; no website judgment). All six are already in the body (170, 212, 200, 204, 220, 156/234), so the table adds nothing a reader lacks.
   - Process notes (move): row 589 (EHRC Code unreached), row 590 (reduced-motion/aria-live/EN clause 9 unreached), row 595 (search ration left BBC/FT/Guardian unread).

9. **Conflict log** — lines 599–605, 3 paragraphs (Agrees / Conflicts / Silent on).
   - Candidates for the Decision Book / design system working record: all of "Silent on" (605: status region, reduced-motion variant, table-twin pattern, long-description block, pause control, focus styling, statement template, test platforms); the type-size tension (603); the "candidate section, *The statement*" (512).
   - Facts a reader needs: none that are not already in the body; "Conflicts. None found" (603) is the one line worth a sentence in the chapter.

10. **Production words in body prose** (outside the sections above). Count: 7 instances.
    - 90: "the orchestrator re-fetched the fallback sentence"
    - 108: "could not be read at source this sprint"
    - 224: "the orchestrator re-fetched the 'rarely' sentence"
    - 505: "are in the ledger" (Looking back, already furniture)
    - 519: "a research agent read the page"; "the orchestrator re-fetched it" (Sources preamble)
    - 18: "Four research agents … the verifier's pass is recorded in the log" (Before you start)
    - 4: "research log, Entry 13"
    - No "cold reader", "our reading" (the chapter says "The reading" throughout, which is the book's convention), "SOURCES.md", "STATE.md", "[Proposal]". The dagger explanation appears at line 12 and again at 519.

11. **Flags inside body prose** (outside Open questions): 12. [Rich reference] 5 (148, 174, 178, 228, and 12 in the legend); [Prototype flag] 3 (190, 212, 244); [Further research] 1 (154); [Validate with users] 1 (298, in the symmetry test); [Revisit at end] 1 (346); [Counterbalance → Ch 11] 1 (224); plus 504 and 509 in Looking back. Removing each bracket leaves the sentence readable in every case; at 190 and 212 the sentence ends on the flag ("is a choice `[Prototype flag]`"; "can be made `[Prototype flag]`") and still reads as a full sentence without it.

12. **Rules table** — lines 409–441, **33 rows**. Tier words used: Fixed (16 rows), Fixed as a procedure (9), Fixed as a stance (6), "Fixed (2.4.13 as a stance)" (1, line 422), Adaptable (2: 417, 438), Decorative (1: 441). Rows whose source cell cites a † / abstract-only source: line 429 (Wery & Diliberto †, with Kuster at source and Rello at source); line 415 cites "Biggs et al." — the 0.23/0.44 figures are from the 2026 preprint read at source, but the 2022 Biggs is †, so the cell is ambiguous. No row cites Schmutz † or Chundury †. The table could be updated to the register's tiers (stance → Adaptable (house default) unless grounds show a requirement; procedure → requirement or sequence) without changing a single rule's wording; only the Tier column changes.

13. **Library-pass corrections touching this chapter.**
    - Correction 8 (EHRC Code 2026, Chapter 7), lines 154, 478, 536, 589: the Code's Chapter 7 is now read at source; it never mentions websites, and the capitalised "The duty is anticipatory" is not the Code's sentence. One-sentence fix: at line 154 replace the secondary quotations with the Code's own lower-case wording read off the page, drop the `[Further research]` flag at 478 and the "secondary … flagged" at 536, and retire gap row 589.
    - Correction 10 (smaller), EN 301 549 V4.1.1 clause 9 adds 9.7 "User preferences for web pages": touches line 130 (EN v4.1.1 "aligned to WCAG 2.2"), line 479 and line 529 ("clause 9 of v4.1.1 unreached"). One-sentence fix: note at 130 that clause 9 adds 9.7, and drop "unreached" at 479/529.
    - No other correction names Chapter 13.

14. **Nightlife illustration** — lines 385–401. Headed "A nightlife illustration — method only" (385) and opens "*Illustrative; fixes nothing about the design; invents no findings.*" (387). Uses no place data at all, real or invented: "A place-page from Chapter 12" (389), "the district" (393, 401), "District changed; 3 of 20 shown" (393, an example string). Correctly labelled.

## E. House style

- "night-time" hyphenated: 0. "cultural contribution": 0.
- Em dashes (—) used as punctuation: 146 (count only, as instructed).
- "robust": 1, line 140, inside the Regulations' quoted definition ("perceivable, operable, understandable and robust") — a quotation, not house prose. "leverage", "unlock", "empower", "deliver", "tackle", "this matters", "at the heart of": 0.
- Americanisms: all 30-odd hits (visualization(s), editorializing, favored, favorable, organized, behavior, color) are inside direct quotations or source titles (lines 36, 102, 104, 110, 116, 174, 178, 184, 194, 234, 274, 528, 544–552). None in house prose. British spelling is consistent elsewhere ("visualisation", "colour", "programme" not used).

## F. Repetition

The "no parallel accessible version / page conforms whole" rule appears at: line 30 (60-second), 50 (section 1), 90–92 (section 3), 268 (section 8), 282 (section 9), 314 (symmetry), 330 (truth 1), 409 (rule), 453 (checklist). Nine places. The 60-second, body, truth, rule and checklist instances are the chapter's teaching structure working as designed. The symmetry-test instance (314) and the section 9 instance (282) are extra; 282 earns its place as a test, 314 is furniture. Likewise the "distribution argument re-based" appears at 34, 52, 162–164, 310, 338, 439, 503: the body (164) and truth 5 are enough; 52 and 310 are the padding. Overall: designed repetition, not padding, with the symmetry test as the one layer that doubles the body without adding to it.

## G. One line for Carly

This chapter does not need rewriting: move its symmetry test, Looking back, gaps table and conflict log to the working record, retire the draft line and the "note on sources", apply the two library-pass corrections at lines 154 and 130, and the teaching stands as it is.
