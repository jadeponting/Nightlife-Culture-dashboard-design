# Read: Chapter 5 — Building a measure

### A. Coverage

- File: `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch05-building-a-measure.md`
- `wc -l`: 663 lines (the Read tool reports 664 including the trailing newline).
- Ranges read with the Read tool: 1–196, 197–346, 347–506, 507–664. Every line was read; no context limit was hit.
- Context read: BRIEF-v2 §1, §4, §5 (lines 7–70); ch00 "How a chapter teaches" and "The legend" (lines 44–128); LIBRARY-PASS "What the pass found, in one page" (lines 1–25) plus the Becker and Birt rows it points to (lines 64, 72, 108, 200, 202).

### B. What the chapter teaches (as a reader, not the author)

The chapter decides that a composite score is a model, not a measurement, and that every step from indicators to one number (normalisation, weights, aggregation, robustness) is a judgement that must travel with the number. It is written for someone who has never built an index and might be asked to. A newcomer leaves knowing: weights are not importance; addition is a hidden exchange rate; a rank needs its interval; a published measure changes what it measures so the audit is designed with it; validity belongs to a reading for a use, not to the number; and "the scene recognises it" is necessary but is face validity, not proof. It deliberately does not choose the form (index, profile, dashboard, user-weighted, longitudinal) and says so.

Best passages, which must survive any edit:
- Lines 136–140 (section 5, "Compensability"): the (21,1,1,1) against (6,6,6,6) illustration and the worked price list in venues and years, line 140, where "one year of operation therefore exchanges for five events per month, and the index is indifferent between them. … Nobody chose any of those prices." The clearest teaching in the chapter.
- Lines 118–128 (section 4): the Times Higher Education 20%/21% against 40%/81% and the closing image at line 128, "told the reader something that is true about the recipe and false about the dish."
- Lines 173–177 and 187–189 (section 7): the Goodhart/Strathern/Campbell record set straight, then the symmetry: "every rigorous comparison found the targeted thing really improved; every audit found the numbers were also massaged at the margin … The centre, by not verifying, was gaming too."
- Lines 237 and 247–249 (section 9): "A member check validates *resonance* and corrects *fact*" and "A measure that the scene recognises and that correlates with platform coverage is a recognised measure of the platform."

Passages a newcomer could not follow:
- Line 10: "Version 1 of this book recorded…" and lines 138, 289, 305, 313, 321, 415, 431, 432, 515, 632: "version 1" is referred to eleven times as if the reader knows what it was. A newcomer does not. One clause at first use ("the studio's earlier draft of this book, now archived") would fix it; the rules table could cite "studio position" rather than "version 1 Ch 6".
- Lines 333, 414, 416: "IMD" is used without expansion; the table at 273 and the sources call it "IoD 2019", and line 165 spells out "Index of Multiple Deprivation" once in passing. Two abbreviations for one instrument.
- Line 32 (60-second version): "the one study found that tested community-chosen indicators against field science found most of them valid" is garbled (two "found"s); the body at line 243 has the intended sentence.
- Line 90: the two canonical lists (2008 handbook against the JRC web guide) and which the chapter follows is production housekeeping a newcomer does not need in the body; a footnote or the sources list.
- Lines 138, 209, 235, 241, 243: parenthetical asides about fetch tools, verifiers and agents (see D.10) interrupt the argument and mean nothing to a reader outside the project.

### C. Verdict on the chapter body

**Stands with light edits.**

The teaching sections do their job as written. The question (line 20) is answered; the beliefs (lines 56–82) are each met in the named section; sections 3–12 are evidence-dense and argued, not listed; the truths (329–341), rules (409–435), break test (441) and checklist (445–467) are consistent with the body. No contradiction found. The argument moves in one direction and does not repeat itself beyond its designed structure (see F).

Specific fixes (16):
1. Line 4: retire the status line (see D.1).
2. Line 32: repair the garbled sentence ("the one study found that directly tested community-chosen indicators against field science found most of them valid and not all of them reliable" → "the one study that tested community-chosen indicators against field science found most valid and not all reliable").
3. Line 36: the canonical truths are the answer to the question and sit last in the 60-second version; move this paragraph (or its first sentence) to the top so the answer comes first.
4. Lines 44 and 46: the handbook's "misleading policy messages" warning is quoted in full at 44 and again as the first con at 46; keep one.
5. Line 90: move the two-lists housekeeping ("The Joint Research Centre's current web guide has quietly revised the list … where it cites the toolbox") to the sources note at 525–526.
6. Line 120: add the Becker caveat the library pass found (D.13): the gap between weight and importance cannot always be closed by re-weighting; with strongly correlated parts it needs negative weights. One sentence.
7. Line 138: remove "(the printed Part II was beyond the fetch tool's reach — `[Further research]`)"; the flag is already at line 473.
8. Line 209: remove "(the fetch tool returned the sentence in two halves; the join is verified)"; the sources list (581) carries it.
9. Line 235: shorten the three provenance parentheses to "(secondary)" / "(abstract)"; the sources list (591–593) carries the detail. The library pass has since read Birt in full, so "in a partial copy of the body" is stale.
10. Line 241: remove the two agent/verifier parentheses; mark Fraser and Reed "(at source)" as the sources list does at 597 and 599.
11. Line 283: remove "the first draft of this chapter ran it badly, so the fair version is given here"; the gap table at 652 is the record of that, and the chapter should show the final state.
12. Line 289: "the choice is Carly's" → "the choice is the studio's" (the chapter otherwise uses "the studio"); same at 392 and 501.
13. Lines 333, 414, 416: one abbreviation for the English Indices of Deprivation, matching the table (IoD 2019) and the sources (546).
14. Line 414 why-cell: "the HDI, Legatum and the IMD all changed their arithmetic" — the deprivation index did not change its arithmetic; it was designed one-tailed (line 150: "reach the same end by a different route"; line 273: weights inherited from 2000). "the HDI changed its arithmetic, and Legatum and the IoD chose theirs, to stop…".
15. Line 405: the rules-table preamble repeats the legend; Chapter 0 line 60 says the register carries the legend "so the table does not repeat it". Cut to the dagger/secondary/adjacent-domain sentence or remove.
16. Line 10: give "version 1" its one-clause introduction at first use (see B).

60-second version: lines 26–36, **722 words**. That is three to four minutes aloud, not sixty seconds. It does not give the answer first: line 26 opens with the handbook's definition and candour, and the answer the question asks for ("what has to be shown with that number") arrives as the canonical truths at line 36. Fix 3 above repairs the order without cutting evidence. The paragraph could lose about a third (the Goodhart attribution history at line 30 and the Zimbabwe figure at line 28 are body material), but the brief says not to cut for length alone, and the figures are the chapter's best hooks; the reorder is the material fix.

### D. Furniture and status: exact inventory with lines

1. **Status line.** Line 3: "*Dashboard Design · Part 1: The analytical foundation*" (keep; it is the part label). Line 4: "*Version 2, draft 2 · 6 October 2026 · revised after a cold read and an independent verification pass (research log, Entry 5)*" — retire.

2. **"Before you start."** Lines 8–14. Line 10 is the re-introduction repeated from Chapter 0 (who the book is for, the Vibe Map, the definition, Chapters 1–4's four recurring findings, who Carly is, the Decision Book and Style Guide v1.5); line 12 repeats the legend (kinds, tiers, flags, dagger, secondary); line 14 defines construct / indicator / composite. Lines 10 and 12 are Chapter 0 furniture. Line 14 is teaching and should stay (move it to the head of section 1 if the section goes). Line 10 also carries the form-question disclaimer ("One decision this chapter does not make and could not…") which belongs with D.3.

3. **"Where the choice is yours."** Lines 370–386. Eight open choices:
   - Line 372: Which form — composite, dashboard, profile, user-weighted, longitudinal self-profile, or a hybrid? Position: "the studio's framework keeps the choice open and this chapter does not close it."
   - Line 374: Which construct, and which parts? Position: "the framework is the studio's and the scene's"; the only rule is that it is written first and each part carries Chapter 4's provenance.
   - Line 376: Who sets the weights — statistics, experts, the public, the reader, or equal weights as a declared null? Position: "Each is defensible; each is declared; none is neutral."
   - Line 378: Which aggregation, and which tail (thriving, struggling, both)? Position: none stated beyond "additive with its price list shown; geometric; a power mean…; non-compensatory; or none".
   - Line 380: How much of the card sits on the face? Position: "The fact of composition and the existence of the card, at minimum"; the rest is Chapter 11's. `[Revisit → Ch 11]`.
   - Line 382: How is recognition gathered — member checks of fact, a synthesised late check, a deliberative choice of parts, or all three? Position: none.
   - Line 384: How is the audit run — which independent measure, how often, by whom? Position: none.
   - Line 386: Does the sector composite's method audit sit here or in Chapter 15? "For Carly."

4. **Other places the chapter awaits a decision.**
   - Line 10: "One decision this chapter does not make and could not: whether the studio's measure of nightlife culture should be an index, a profile, a scoreboard, a ledger or something else. Version 1 of this book recorded that the studio has kept that question open on purpose".
   - Line 281: "Whether a named method audit of a sector instrument belongs here or in Chapter 15, *Learning from the best*, is for Carly."
   - Line 289: "This section gives the forms and the arguments; the choice is Carly's."
   - Line 297: "No empirical study was found of whether decision-makers use or trust a composite more than a dashboard; the belief that they do is, on this chapter's evidence, Practice." (an open finding, kept in text)
   - Line 392: "The sector knowledge is Carly's; the method is the chapter's."
   - Line 396: "The deprivation index's one-tailed design poses a question the studio has not yet had to answer: is the measure built to find where nightlife culture thrives, where it is at risk, or both".
   - Line 501: "without making the decision, which is Carly's."
   - Line 647 (gap table): "No house position on whether the measure is one-tailed … Carly; Chapter 6".
   - Line 651 (gap table): "flagged the placement for Carly … Carly's call: here or Chapter 15".
   - "steer", "awaits", "TBD": none.

5. **"The symmetry test" section.** None as a heading. The test is run inside the gap table at line 652 ("a symmetry failure against the instrument the chapter was most tempted to judge") and in the fair re-run at line 283. Chapter 0 line 123 records that Chapter 5 "used" the test before it became a numbered section.

6. **"Open questions and flags."** Lines 471–505, 33 flag lines. By type: `[Further research]` 12 (473–484); `[Prototype flag]` 4; `[Validate with users]` 2; `[Revisit → Ch n]` 10 (Ch 1, 2, 3, 4, 6, 7, 9, 10, 11, 15); `[Revisit at end]` 1 (501); `[Counterbalance → X]` 3 (502–504); `[Rich reference]` 1 (505, a reading list). One further `[Revisit → Ch 9]` is nested inside line 484.
   - Line 485 `[Prototype flag]` Run the sensitivity analysis and publish rank intervals — PROBES.md P-045 (probe 20).
   - Line 486 `[Prototype flag]` Compute the effective importances by Paruolo's method — P-046 (probe 21).
   - Line 487 `[Prototype flag]` Compute the price list and answer the refusal test — P-047 (probe 21).
   - Line 488 `[Prototype flag]` Discriminant test against ticketing-platform coverage — P-048 (probe 22).
   - Line 489 `[Validate with users]` Recognition, recorded: profile against composite with the three user groups and co-developers — P-049 (probe 1).
   - Line 490 `[Validate with users]` The card: which of the nine lines readers open — P-050 (probe 14).
   All six are already in `03-tests/PROBES.md`.
   - Line 482 is a process note, not a reader's open question: "One fetch fabricated quotations. Agent C reports…" — move to the research log / method notes.
   - Lines 480–481 (abstract-only list; secondary list) duplicate the sources list's marks and belong with it.

7. **"Looking back."** Lines 507–517. Seven bullets against Chapters 1–4, version 1 and the Decision Book. Line 515 carries a real correction a reader needs somewhere (the 20%/21%, 40%/81% figures are the Times ranking's, not the HDI's) but the body already states it correctly at line 120; the rest is cross-chapter bookkeeping for the research log.

8. **"Gaps found" table.** Lines 641–655: 13 rows.
   - Real knowledge gaps a reader needs (keep in text, already stated in the body): row 643 (Decision Book silent on composites — also at 517 and 663); row 645 (recognition split into legitimacy and validity — section 9); row 647 (one-tailed or two-tailed — line 396); row 654 (no evidence decision-makers prefer composites — line 297); row 655 (handbook's visualisation step silent on uncertainty — line 110).
   - Process notes (move): rows 644 (version 1 misattribution traced), 646 (design-system card proposal — belongs in the conflict log), 648 (glossary has one sense of reliability), 649 (canonical texts unreachable), 650 (fabricated-quotation episode), 651 (placement for Carly), 652 (draft 1's unfair arithmetic — history of development), 653 (five verification mismatches).

9. **"Design system and Decision Book — conflict log."** Lines 657–663: three paragraphs (Agrees; Conflicts: none direct, one tension; Silent on). Candidates for the Decision Book / design system working record: the "robustness mark" for a composed number (661) and "the rules table is the candidate chapter" (663, also 517 and 643). Fact a reader needs: none that the body does not already carry (line 319 proposes the card as the evidence component).

10. **Production words in body prose** (lines 40–400, excluding the sections above). 11 instances:
   - Line 138: "the printed Part II was beyond the fetch tool's reach"
   - Line 175: "the original conference volume was not reachable — secondary"; "his chapter was not reachable"
   - Line 197: "the paper's definitions of the two were not reachable; the book is in Chapter 2"
   - Line 209: "the fetch tool returned the sentence in two halves; the join is verified"
   - Line 213: "reached as quoted in two later papers — secondary"
   - Line 217: "the latter's standard bands reached only by paraphrase †"
   - Line 221: "the original was not reachable; the definitions are the *Standards'* and a methods text's"
   - Line 235: "reached as quoted with page number in two later sources — secondary"; "in a partial copy of the body"; "the publisher page was blocked; the abstract was reached only in reconstruction and through a later summary"
   - Line 241: "quotations string-verified by the research agent; the paper is not open and the verifier could not reach it"; "likewise string-verified by its agent and unreachable to the verifier"
   - Line 243: "abstract reached in reconstruction — treat the wording with care"
   - Line 283: "the first draft of this chapter ran it badly, so the fair version is given here"
   Outside the body: line 4 (cold read, research log), 522 (orchestrator, agent, verified), 482 (Agent C, fetch), 633 ("not re-read this sprint"), 652 ("the cold reader's strongest objection"). "orchestrator" 1, "verifier" 3, "agent" (research sense) 7, "sprint" 1, "research log" 1, "cold read(er)" 2, "fetch" 9. No SOURCES.md, STATE.md, [Proposal] or "our reading". "Ledger" appears only in the "value ledger" sense (lines 10, 289, 291) and once as the sources ledger (649).

11. **Flags inside body prose.** 9 flags on 8 lines: `[Rich reference]` 4 (44, 120, 225, 295); `[Further research]` 3 (138, 260, 297); `[Revisit → Ch 10]` 1 (199); `[Revisit → Ch 11]` 1 (380, in section 14). All sit at sentence end; removing the bracket leaves every sentence readable. Line 138's flag is inside a parenthesis that should go whole (D.10).

12. **Rules table.** Lines 409–435: 27 rows. Tier words: **Fixed** 15; **Fixed** (stated/declared/test); Adaptable (which/combine) 3 (411, 416, 426); **Fixed** as a procedure 2 (420, 421); **Fixed** as a stance 2 (427; 428 "the studio's"); Adaptable 3 (429, 433, 434); Adaptable (strong default) 1 (422); *Decorative* 1 (435). Rows whose source cell carries †: 413 (Becker et al. 2017†, beside Paruolo at source — Fixed), 422 (Bevan & Hamblin 2009† — Adaptable), 429 (Reed, Dougill & Baker 2008† — Adaptable), 433 (Saltelli 2007† — Adaptable). Only one Fixed row rests partly on a dagger, and the library pass has now read Becker in full (LIBRARY-PASS line 72), so that dagger can be dropped once the caveat is added. The register re-bases: 5.12/5.13 → DD-028 Fixed (sequence); 5.19 → DD-018 Fixed (sequence); 5.20 → DD-109 Adaptable (house default); 5.14 → DD-106 Adaptable (house default); the "(stated)/(which)" split rows → "Fixed (requirement) · which …: Adaptable". The table can take the register's tiers by editing the Tier column alone; no rule wording changes.

13. **Library-pass corrections touching this chapter.** Two of the ten.
   - Correction 10, Becker et al. 2017 (LIBRARY-PASS lines 20, 72, 108), register row 5.5: line 120 says the gap "can be closed rather than discovered"; the paper says two strongly correlated variables "can hardly have very different influence in the overall index, without resorting to the use of negative weights". Fix: add to line 120 "— though where parts are strongly correlated the fit may need a negative weight, which is its own warning", and drop the † from rows 413 and 532 now the full text is read.
   - Correction 7, Birt et al. 2016 (LIBRARY-PASS lines 17, 64, 202), named for Chapters 2 and 9 but used here at 235, 361, 427 and 592: the paper's own synthesised check changed nothing (28 of 50 returned; returning to the data "proved unnecessary"). This supports line 237's position; fix: one sentence at 235 and "body partial" at 592 updated to "at source".
   - Not touching this chapter: corrections 1–6, 8, 9. (The gap table at 648 and the Lincoln & Guba p. 314 citation at 591: the library pass found Birt does not give p. 314; the chapter's "p. 314 as quoted in Roller (2021) and Dahal (2025)" stands as secondary.)

14. **Nightlife illustration.** Lines 390–400, headed "What this means for a nightlife dashboard". Line 392: "An illustration, not a specification, and not a decision about the measure's form. The sector knowledge is Carly's; the method is the chapter's." Line 394: "Suppose, for the illustration only…". Labelled. It uses no place data at all, invented or real: the only figures are the handbook's (21,1,1,1)/(6,6,6,6) and the hypothetical "between eighth and nineteenth, most likely twelfth" (398). No Bristol, no venue, no number about any place.

### E. House style

- "night-time": 0. "cultural contribution": 0. "robust/robustness": 8 (lines 28, 90, 106, 161, 187, 273, 277, 533) — all the technical term for sensitivity analysis or inside quotations; none is the filler word. "leverage", "unlock", "tackle", "this matters", "at the heart of": 0. "empower": 1 (241, inside a Fraser quotation). "deliver": 4 (260 twice, 477, 610; "delivering against" is inside a quotation, the rest are "delivery team"). Em dashes used as punctuation: 233.
- Americanisms: 16 spellings, every one inside a quotation or a title (Campbell 177 "recognized", "organization"; Kelman 187 "hypothesized"; Espeland 197 "behavior"; Morse 235 "synthesized", "decontextualized"; Trochim 247 "operationalization"; UNECE 295 "visualization(s)"; Manheim & Garrabrant 574 "Categorizing"; Dartmouth 557 "Center", "Program"; 317 and 422 Campbell's "recognized"). None in the chapter's own voice.

### F. Repetition

"Equal weighting does not mean 'no weights'" appears at lines 28 (60-second), 62 (belief two), 100 (handbook quotation in full), 312 (recipe line 4), 331 (truth 2), 412 (rule why-cell) and 448 (checklist, paraphrased): seven times. (21,1,1,1) against (6,6,6,6) appears at 28, 138, 333, 396 and 414: five times. The $0.51 / $9,000 pair at 28, 144, 333 and 415: four. This is the chapter's teaching structure working as designed: 60-second version, body, truths, rules, checklist each have a job and the brief (BRIEF-v2 §5) requires them. The one place it is padding is lines 44 and 46 (the same handbook warning quoted twice in consecutive paragraphs).

### G. One line for Carly

Chapter 5 teaches as it stands and needs no rewriting: retire the status line, move the "Before you start", "Where the choice is yours", "Looking back", gap-table process rows and conflict log to the reference sections, strip the dozen fetch-tool and agent asides out of the body, and make about fifteen one-sentence fixes (the Becker caveat, the garbled line 32, the answer-first reorder of the 60-second version, one name for the deprivation index).
