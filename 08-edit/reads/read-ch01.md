# Read: Chapter 1 — What a dashboard is for

## A. Coverage

- File: `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch01-what-a-dashboard-is-for.md`
- `wc -l`: 480 (the Read tool shows 481, the last being an empty line).
- Ranges read: 1–340, 341–481. Every line was read; nothing summarised from headings.
- Context read: BRIEF-v2 sections 1, 4, 5; Chapter 0 "How a chapter teaches" and "The legend" (lines 44–128); LIBRARY-PASS lines 1–32; register rows citing chapter 1 (`06-register/rule-register.md`).

## B. What the chapter teaches

The chapter decides what a dashboard is (a display that turns data into a decision for a named reader, line 56), shows that the field cannot agree on the word and that the evidence it works is thin (sections 1 and 3), and then spends its real weight on two things a newcomer would not have expected: that trust belongs to the people who make a number and how they behave, not to the chart (sections 4 and 5), and that aggregation is arithmetic that makes the biggest win and blanks out the small (section 6). It is written for someone meeting the subject for the first time; it assumes no statistics. A newcomer would take away: name the reader first, expect nobody to open it, expect the measure to change the thing it measures, show your working and your uncertainty, and never trust a ranking of small units. Section 7 then gives them the vocabulary (legibility, commensuration, data inertia, boundary object) for why a dashboard built for several communities is a social achievement before it is a design.

Best passages, which must survive any edit:
- Lines 24–30, the 60-second version. "The job never changed: a dashboard keeps the mud out." Gives the answer first and carries the whole chapter.
- Lines 36–38 and 66, the mud and the cockpit-versus-car argument ("Breadth against focus — most arguments about what to put on a dashboard are that collision replayed").
- Lines 82–84, Behn and reactivity: "The display was the agenda. The meeting was the intervention." Then the New York surgeons case.
- Lines 186–192, Wainer and Gelman & Price: "Raw maps put the extremes in the small places; smoothed maps move them to the big ones. … A league table may tell you where to look. It cannot tell you what you will find."
- Lines 208–212, Scott, Merry and the O'Connell case: "That is not a conspiracy; it is gravity." "Nobody decided to describe the neighbourhood by its problems. The available columns decided."

Passages a newcomer could not follow:
- Line 166: "Carly's eighth failure — 'an aggregation of the biggest'". The failure register has not been introduced; it first appears as a list at line 228. A newcomer meets "eighth failure" with no list to count against. One sentence of forward reference would fix it (or the register table could be placed earlier).
- Line 200: "The analytical move is the one Carly describes in words" assumes the reader has Carly's brief in front of them.
- Line 196: "the places Carly's brief cares about" likewise.
- Line 228: "the heartbeat" and "the six kinds of nothing" are defined in the bracket, which is adequate; but "heartbeat" also appears bare at line 232 and 270, before or without that bracket being nearby.
- Line 300 and the sources list (line 375): "verification list", "orchestrator", "independent agent" are process terms, not reading terms.
- Line 328: "the four-line record Chapter 16 describes" — Chapter 16 now describes a nine-line deviation entry (ch00 line 97); the figure is stale.
- Line 12: the summary of flags omits `[Revisit → Ch n]` and `[Counterbalance → X]`, both of which the chapter then uses (lines 368). Minor.

## C. Verdict on the chapter body

**Stands with light edits.**

The teaching sections do their job as written. The question (line 18) is answered in the first paragraph of the 60-second version (lines 24–30); the definition arrives at line 30 and again, argued, at line 56. Sections 1 to 7 are the evidence as body, not as a section called "The evidence", which is what Chapter 0 asks for. The truths (lines 247–262), the choices (270–278), the illustration (284–294), the rules (304–322), the break test (328) and the checklist (332–345) all follow from the body and do not contradict it. Nothing repeats at a length that would count as padding (see F). There is no case for structural work.

The light edits, all specific:

1. Line 4: retire the status line (see D1).
2. Lines 8–12: move "Before you start" out (see D2); it duplicates Chapter 0 and its flag list is already incomplete.
3. Line 114: library-pass correction 2. "the clearest demonstration in any field" overstates Kaliisa et al. (nine of 38 studies; larger effects mostly confounded). Soften to "the clearest signal in any field" or state the nine-of-38 split; and correct "lived up the promise" to "lived up to the promise" in the quotation.
4. Line 310: rule 1.7's source cell cites Kaliisa 2024†; its why-cell ("Dashboards move the countable before the intended") should carry the same caveat, or the chapter should note the register does.
5. Lines 304 and 308: the † on Ivanković et al. 2021 and van der Bles et al. 2020 can be dropped, since the ledger records a later full-text read (LIBRARY-PASS line 27). The same applies to Dong et al. 2022 at line 307, which carries no dagger in the table but is marked "full text; verified" at line 410 anyway.
6. Line 166: introduce the failure register before calling on "Carly's eighth failure", or re-order so the table at 228 comes first. A one-clause fix: "The eighth of the brief's failures, listed in section 8 — …".
7. Line 328: "the four-line record Chapter 16 describes" should read "the nine-line deviation entry" (ch00 line 97) or simply "the deviation record Chapter 16 describes".
8. Line 12: add `[Revisit → Ch n]` and `[Counterbalance → X]` to the flag list, or (better) drop the section and let Chapter 0 carry it.
9. Line 232, 270: "heartbeat" used bare; the definition sits only in the bracket at 228. Either define at first use (232 follows 228, so fine) or leave as is; 270 is after the definition. Minor; could be left.
10. Line 300: the table's preface says "the full text is on the verification list before this version closes" — status text in the body; replace with a plain statement that † means abstract-only, which the register carries.
11. Line 375: the sources preface explains "orchestrator", "independent agent", "research log". Keep the three-grade meaning (at source / spot-checked / verified) but strip the process nouns, or point to Chapter 0's legend (ch00 line 104) which already defines them.
12. Lines 247, 249: the truths use "Fixed as a stance" and "Fixed as a statement of the record". The register has re-based stances (ch00 lines 97–99). Truth 1 could read "Adaptable (house default); the design consequence is Fixed (requirement)". Truth 3 is "a statement of the record", which Chapter 0 now defines as a truth listed apart and not a rule. Change the words, not the content.
13. Line 426: the Julious & Mullee discrepancy (83% vs 87%) sits in the sources list; line 180 prints 83%. Either print the arithmetic (86.7%) or note the discrepancy where the figure appears. One sentence.
14. Line 148: "a self-selected user survey, so strong as a signal and weak as a population estimate" is good; but register DD-033 says "never report an on-site percentage as trust", which this paragraph does (90.3%). Not a contradiction, since the caveat is present; a four-word nod to the register's rule would close the loop.

Fourteen edits, each a word, a figure or a sentence.

**60-second version**: lines 24–30, 441 words. It gives the answer in the first paragraph (what a dashboard is, in the mud image) and the definition in the last. It does not need trimming to put the answer first. At 441 words it reads in nearer two minutes than one, but the brief says not to cut body for length, and this passage is the best in the chapter.

## D. Furniture and status: inventory

1. **Status/draft lines.** Line 3: "*Dashboard Design · Part 0: Foundations*" (keep: part label). Line 4: "*Version 2, draft 2 · 5–6 October 2026 · revised after a cold read and an independent verification pass (research log, Entry 1)*" — retire or move to the research log.

2. **"Before you start".** Lines 8–12. Two paragraphs: who the book is for and what the Vibe Map is (10); the kind/tier/flag conventions (12). Both repeat Chapter 0. Line 12's flag list is incomplete (omits `[Revisit → Ch n]`, `[Counterbalance → X]`) and its tier wording predates the register's re-basing. Move: retire the section and rely on Chapter 0, or keep only line 10's first two sentences as orientation.

3. **"Where the choice is yours".** Lines 266–278. Five open choices:
   - Which job is the dashboard for: monitoring, analysis or communication? Current position (line 270): "A public-interest dashboard is realistically a communication and analysis object with a monitoring heartbeat; that is a position, not a law. *Adaptable.*"
   - One screen or many layers? Position (272): "The choice depends on the reader and the decision, and Chapter 11 returns to it with evidence about first screens. *Adaptable.*" No position stated beyond deferral.
   - How much to frame: author openly, or present a configurable surface? Position (274): "both argue for authored framing, honestly labelled. *Adaptable.*"
   - Which failures to prevent first? Position (276): "The evidence ranks them: non-use and distrust kill a dashboard outright; aggregation and non-recognition kill its truth; the others degrade it. *Adaptable — and the order is a Nightlife Culture decision.*"
   - How much mud to let in (how much uncertainty, gap and uncounted knowledge to admit)? Position (278): "Where to set that dial is a judgement about the reader. *Adaptable; the floor — never a blank where there is a reason — is Fixed.*"
   The register carries these as DD-051 (Adaptable) and the "which job" part under DD-049. The section itself is a teaching section (Chapter 0 lists it) and should stay; only the decision-log extraction above moves.

4. **Other places the chapter asks Carly to decide or awaits steer.** Searched for Carly, steer, decide, awaits, "not yet", "has not", open, TBD.
   - Line 276: "the order is a Nightlife Culture decision" (open; no order chosen).
   - Line 469 (gaps table): "Decision Book gap register, via Carly".
   - Line 300: "the full text is on the verification list before this version closes" (process status, not a decision).
   - Line 176: "the full paper is on the verification list" (process status).
   - Line 471: "Chapter 0 — consider a fifth kind, *Practice*" (now done; ch00 line 82. Row is stale).
   - No "steer", "awaits", "TBD", "has not chosen" in the chapter. The other hits for "Carly" (lines 10, 166, 196, 200, 228, 456) are references to her brief, not requests for decisions.

5. **"The symmetry test".** Absent. Chapter 0 (line 123) says it runs "from Chapter 4", so its absence here is as designed. Nothing to move.

6. **"Open questions and flags".** Lines 349–361. Counts: `[Further research]` 5 (351–355); `[Prototype flag]` 2; `[Validate with users]` 1; `[Revisit → Ch n]` 0; `[Revisit at end]` 2 (359, 360); `[Rich reference]` 1 entry listing five sources (361); `[Counterbalance → X]` 0 here (one in Looking back, 368).
   - Line 356 `[Prototype flag]` Measure use: record who opens the Vibe Map, what they touch, what they take away, from day one.
   - Line 357 `[Prototype flag]` Positive deviance on the project's own data: find the small places doing well on the same resources and ask what they do.
   - Line 358 `[Validate with users]` The four discovery tests read as tests of whether a boundary object is forming; ask each of the three user groups whether they recognise the same structure.
   These are likely already in PROBES.md (not checked; the brief says many are). Line 354's `[Further research]` on abstract-only sources is superseded by the library pass and the register's dagger status; it is a status line and can be retired. Line 355 (Porter) and 352 (Bevan & Hood) are real reading gaps and belong wherever the book's reading list lives.

7. **"Looking back".** Lines 363–369. Three bullets against version 1 (strengthens, counterbalances with `[Counterbalance → old Ch 5 / new Ch 7]`, opens a thread). Process record; move to the research log or a cross-chapter register. The one substantive point (line 368: a comparison of conditions by rate needs intervals, not only a comparability note) is already carried by rule 1.11 and register DD-012.

8. **"Gaps found" table.** Lines 465–472: 6 rows.
   - Real knowledge gaps a reader needs (keep in text, and the body already states them): row 1 (no independent non-use figure; stated at 124 and rule 1.17), row 2 (no staleness study; stated at 232 and 351).
   - Process notes (move): row 3 (Decision Book lacks the aggregation rule, via Carly), row 4 (design system silent on conduct of release), row 5 (fifth kind *Practice* — now done, stale), row 6 (dagger convention added after a sceptical reader caught it — history, not a gap).
   The table uses the old four-column form with a colour cost; Chapter 0 (line 66) now specifies *Gap · Where it bites · Interim position · Who closes it*.

9. **Design system conflict log.** Lines 474–480: three prose paragraphs (Agrees / Conflicts: none / Silent on). Chapter 0 (line 67) now wants a table with a status column. Candidates for the design system working record: the three "silent on" items (conduct of release; unit of aggregation as declared choice; measurement of use). The "Agrees" paragraph is a fact the reader might find useful but is already implied by the body (Kitchin, the Code, the `[c]` mark); it can move. No Decision Book log as such; the Decision Book appears only in gaps row 3.

10. **Production words in body prose** (lines 16–345, excluding sections above). Count: 4 instances.
    - Line 120: "Only its abstract has been read for this chapter; the typology belongs in Chapter 7 (`[Further research]`)."
    - Line 176: "(Read at the authors' abstract and a university summary; the full paper is on the verification list.)"
    - Line 300: "† marks a source read at the authors' abstract only; the full text is on the verification list before this version closes (`[Further research]`)."
    - Line 92: "(Porter is quoted here from a published excerpt collection; the book itself is on the reading list for Chapter 5.)" — borderline; reading-list, not process.
    Also honest reading notes that are not process words and should stay: line 66 ("the original article is paywalled and the wording has not been checked against it here"), line 76 ("since the original is paywalled"), line 52 ("The only survey this chapter could find"), line 124 ("This chapter looked for the number and could not find one that was independent"). These are evidence discipline on the face and read well.
    Outside the body: line 4 (cold read, verification pass, research log); line 375 (agent, orchestrator, independent agent); line 383 ("full text read by a research agent"); line 472 (ledger). No "sprint", "our reading", "SOURCES.md", "STATE.md" or "[Proposal]" anywhere.

11. **Flags inside body prose** (outside Open questions): 7. `[Further research]` 3 (120, 232 in the failure table, 300); `[Prototype flag]` 2 (200, 236 in the failure table); `[Validate with users]` 1 (222); `[Revisit at end]` 1 (196). Removing the brackets leaves every sentence readable: at 196, 200 and 222 the flag is a trailing mark on a complete sentence; at 120 and 300 the sentence closes before the bracket; at 232 and 236 the flag sits in a table cell after a full clause.

12. **Rules table.** Lines 304–322: 19 rows. Tier words used: **Fixed** (15 rows), **Fixed (adopted voluntarily)** (317), "Adaptable in method; Fixed as sequence" (318), Adaptable (316, 321), *Decorative* (322). No "Fixed as a stance" or "Fixed as a procedure" in the table (those appear only in the truths, lines 247 and 249). Rows citing † sources: 304 (Ivanković†), 308 (van der Bles†), 310 (Kaliisa†, Gerrish†), 318 (Turnhout†), 319 (Subramanian†). The register maps these rows to DD-043, DD-049, DD-005, DD-022, DD-014, DD-032, DD-028, DD-021, DD-020, DD-012, DD-015, DD-030, DD-033, DD-018, DS-001, DD-050, DD-051, DD-052; the register's tiers are "Fixed (requirement)" or "Fixed (sequence)" with an Adaptable open part named. The table could carry those tiers without changing a word of the rule column: every row's rule wording is identical or near-identical to the register's stated row (e.g. 312/DD-021, 314/DD-012, 320/DD-050). Two rows change kind of thing rather than wording: 318 becomes DD-018 "Fixed (sequence) · method of checking: Adaptable", which is what the chapter already says in other words; 319 becomes DS-001, a statement of the record listed apart, and would leave the rules table for the truths.

13. **Library-pass corrections touching this chapter.** One of ten, plus the dagger note.
    - Correction 2, line 114 and rule 1.7 at line 310: Kaliisa et al. 2024. Fix: replace "the clearest demonstration in any field" with wording that carries the nine-of-38 split and the authors' confounding caveat, and correct the quotation to "lived up to the promise".
    - Dagger removal (LIBRARY-PASS line 27): 1.1 (Ivanković, line 304) and 1.5 (van der Bles, line 308) can lose their †, since a later chapter's full-text read is in the ledger. Fix: delete two daggers and the matching entry in line 354.
    - Subramanian et al. 2009 (line 319, 176) is behind a PubMed Central wall, not unread by choice (LIBRARY-PASS line 29). No text change; the status stays.

14. **Nightlife illustration.** Lines 282–294, headed "What this means for a nightlife dashboard" (the Chapter 1–5 heading Chapter 0 allows) with the italic label at line 284: "*An illustration, not a specification.*" It uses no place data at all, invented or real; it quotes the Vibe Map's own description from the funding deck (line 286, sourced at 457) and the three user groups, and reads three phrases through the chapter's concepts. The "suburban hub" at line 292 is generic, not a named place. Correctly labelled.

## E. House style

- "night-time" hyphenated: 0. "cultural contribution": 0 (line 216 uses "Cultural Value Project", a proper name, and "value").
- Em dashes used as punctuation: 223 in the file; 112 in the body (lines 34–296). Count only.
- "robust": 3. Line 220 is inside the Star & Griesemer quotation ("robust enough"); line 433 is a paper title; line 108 "the one robust lesson is that *use* is the hinge" is the chapter's own and is the one instance to consider changing (e.g. "the one firm lesson").
- "leverage", "unlock", "empower", "tackle", "this matters", "at the heart of": 0. "empowering" at line 401 is a paper title. "deliver": line 44 inside Eckerson's quotation ("information delivery system"); line 78 "delivers the first level" (verb, plain use, fine).
- Americanisms: none in the chapter's own prose. "visualization" (38, 214), "customize" (64), "recognize" (92), "realizing" (118), "realize" (208) are all inside quotations; 381, 394, 424 are paper titles. "percent" at line 180 and 188 is inside quotations.

## F. Repetition

The chapter's spine is repeated five times by design: body, failure register, truths, rules, checklist. Example, "name the reader and the decision": line 56 (definition), line 234 (failure table, "Name the reader and the decision first"), line 248 (truth 2), line 304 (rule), line 332 (checklist). Likewise "show uncertainty as a number": 158, 190, 238, 254, 257, 308, 314, 336, 341. This is the teaching structure Chapter 0 lays out working as designed: each repetition is in a different register (argument, mechanism, truth, rule, check) and none adds prose beyond a line. Not padding.

One genuine double: the three summary findings at lines 128–134 ("What the evidence, taken together, says") restate conclusions already drawn in the preceding sector paragraphs (108, 114, 124) and then appear again as truths 3, 4 and 5. Within the body this is the one place a paragraph exists only to summarise. It reads well and is short (seven lines); I would not cut it, but it is the only candidate.

## G. One line for Carly

This chapter does not need rewriting: the body teaches as it stands, and what it needs is one source correction (Kaliisa, line 114), two daggers dropped, a dozen word-and-figure fixes, and its status line, "Before you start", "Looking back", gaps table and conflict log moved to the working records.
