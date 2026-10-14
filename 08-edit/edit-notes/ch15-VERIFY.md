# Chapter 15 · verification, 14 October 2026

Checked `04-chapters/ch15-learning-from-the-best.md` (597 lines) against `archive/04-chapters-draft2/ch15-learning-from-the-best.md` (701 lines), `ch15-MOVES.md`, `ch15-NOTES.md`, `merged-rows-tier-fix.md`, `read-ch15.md`, `ISSUES-REGISTER.md` 1.3 and 1.9, `rule-register.md` and `ch15-workings.md`. Line numbers below are the edited chapter's unless marked (archive).

Eight pass, two fail. Both fails are small; neither touches the teaching.

## 1. Diff · PASS

`diff` with section numbers normalised: 173 lines out, 69 in. Every difference is accounted for:
- Script moves (MOVES.md): status line (archive 4); Before you start (archive 6–18); symmetry test (archive 390–410); Open questions and flags (archive 552–568); Looking back (archive 572–598); Gaps table (archive 665–682); conflict log (archive 686–699); the "End of Chapter 15, draft 2" line.
- NOTES.md: dagger drops at 21, 111, 547; C.5 at 31; C.6 at 351; C.8 (the `[Revisit at end]` sentence, archive 452); C.9 (the fold paragraph, archive 468); C.10 at 111; House source at 595; tier cells at 453–463, 470–471, 473; truths 381–393; production words at 537, 540, 544, 569, 572, 590; Carly's words at 41, 361, 367, 369, 371, 373; stale references at 195 and 321; renumbered pointers at 25, 37, 39, 341, 439, 480; the three added sections at 484–491, 522–529, 535.
- merged-rows-tier-fix.md: Tier cells at 464 and 465 (`**Fixed** (stance)` → `**Fixed (requirement)**`).
- Brief edit 10: the Statuses line at 537 ("returned by the fetch tool once" → "returned once and not re-checked").

No unexplained change.

## 2. Nothing new · FAIL (one clause)

- Sources note (535): the writer's sentence, built from the moved note; every named text is in the archive's note. Two sentences rather than the brief's one; the Bank item drops "and its 2026 reports". Not new matter.
- Words this chapter uses (524–528): bullets 1–5 verbatim from the moved working-words paragraph.
- **Line 529, FAIL.** The sixth bullet, *precedent record*, was not in the moved paragraph. Its body is section 11's sentence (399) cut short, and the tail "; section 11 gives its nine lines" is wording that exists nowhere in draft 2. The inventory's C.2 names the term as one to keep, so the bullet is defensible; the clause is not. Fix: end the bullet at "on what terms" (the chapter's own words), or drop the bullet.
- What the field does not know (486–491): the six rows the inventory's D8 names, in the rows' words; only the row's quotation marks dropped (Health Index, Audience Agency).
- Read next: none; the moved section had no `[Rich reference]` entries (inventory D6).
- Line 31's closing sentence ("It found about forty, listed in section 9; about six were already in the book in another form") replaces the dead pointer "Section 11 says whether it passed"; both figures are the symmetry test's and the conflict log's. Allowed by brief edit 2.
- Line 547, "*Verified* (full text, read for Chapter 1)": the source-cell correction register 1.3 names (archive 614).

## 3. Nothing cut · PASS

Sections 1–13 present and renumbered as MOVES.md says; the question, the 60-second version (six paragraphs, unchanged apart from one dagger), the seven truths, the precedent-record table and filled example, the illustration, the rules (22 rows), the break test, the checklist (22 items) and the sources all present. Removed, as allowed: the `[Revisit at end]` sentence after the filled example (inventory C.8; its content is in the working record twice) and the fold paragraph (brief edit 14; settled). No paragraph shortened.

## 4. Rules unchanged · PASS

All 22 rows compared cell by cell: Rule, Why, Kind and Source identical to draft 2 in every row. Tier changes: rows 1–11 and 18 procedure → `**Fixed** (requirement)`; rows 19 and 21 → `**Fixed** (sequence)`; rows 12 and 13 stance → `Fixed (requirement)` per merged-rows-tier-fix.md; rows 14–17, 20, 22 Adaptable, unchanged. Spot-checked seven against the register: row 1 DD-033 Fixed (requirement); row 6 DD-007 Fixed (requirement); row 10 DD-014 Fixed (requirement); rows 12–13 DD-012 Fixed (requirement); row 14 DD-346 Adaptable; row 19 DD-026 Fixed (sequence); row 21 DD-349 Fixed (sequence). All match. Rows 15 and 16 (DD-024, DD-007, both Fixed with an Adaptable part) stay Adaptable and are listed in NOTES, as the brief allows for merged rows.

Observation, not a fail: rows 12 and 13 are set as `**Fixed (requirement)**` where every other Fixed row is `**Fixed** (requirement)`. Same words; bold placed differently. One-character fix each.

## 5. Quotations · PASS

Every unchanged line is identical by diff, so its quotations are. In the changed lines, all quotations were compared programmatically: the only differences are the failure-register apostrophes (41, 361, 367, 369, 371, 373), each now matching BRIEF-v2 line 19 character for character, and the removed brief quotation "could fold into Chapters 2 and 5" (31). Ten read by eye in addition: "87% of respondents who gave an opinion…" (15), "Issue: COVID-19 deaths data" (17), "χ² > 9.5495" (19), "over 300,000 unique users every day, and five million hits a week" (21), "U.S. states and counties began to consistently reduce…" (23), "outstandingly high level of user trust…" (87), "the simplification of language increases public comprehension more than the inclusion of visuals" (153), "the coefficients change dramatically" (19), "a small area with a rank of 1,000 is not half as deprived…" (19), "come with a plan for maintaining, updating and retiring the dashboard" (139). All identical.

## 6. Corrections applied · PASS

Register 1.3 names no numbered correction for this chapter; it names the Dong et al. 2022 dagger drops at archive 126, 614 and 671. Applied: 21 (one dagger), 111 (three daggers, the verdict's dagger, and "paper's abstract" → "paper", which the drop requires), 547 (*Abstract* → *Verified* with the reason). Archive 671 is the gaps row, now in the working record untouched, and the "What the field does not know" list rightly omits it. Nothing else changed in those passages beyond the C.10 double space at 111.

## 7. Section references · PASS

Thirty in-chapter references checked against the new headings: 25, 37, 439, 529 → 11 (What holds true regardless; the precedent record); 31, 39, 341, 419, 474 → 9 (What is borrowed); 39, 341 → 12 (Where the choice is yours); 41 → 10; 47 → 3 and 7; 49, 51 → 4; 53, 55 → 5; 57 → 6; 59 → 1 and 8; 61 → 7; 319 → 3 and 6; 365 → 5; 399, 525 → 1; 480 → 13 (the illustration's "Fifth, the test"). Each points at a section that says what the reference claims. Line 595's §6 and §7 are BRIEF-v2's sections, not the chapter's. None unresolved.

## 8. No furniture left · PASS

Hits: "awaiting a condition" at 410, 413 and 439. All three are the precedent record's own status vocabulary, present in draft 2, and the inventory's D4 excludes them. No other term on the list appears outside a quotation or title ("draft", "orchestrator", "verifier", "the agent", "fetch tool", the flags, the old tier wordings, the missing apostrophes, "night-time", "cultural contribution": none).

## 9. Workings file · PASS

All six moved sections compared programmatically against the archive: Before you start, 11 · The symmetry test, Open questions and flags, Looking back, Gaps found, the conflict log. Each identical, word for word.

## 10. Notes honesty · FAIL (stale on one point)

Everything NOTES.md says was changed, was: the dagger drops, C.5, C.6, C.8, C.9, C.10, the House source, 14 tier cells, seven truths, six production-word edits, the sources note, the Words section, the six knowledge bullets, the apostrophes, the two stale references, seven renumbered pointers. Everything it says was not applied was not, with one exception:

- **NOTES.md line 48 (Not applied) and line 64 (decision log), FAIL.** Both say rules rows 12 and 13 "still read `**Fixed** (stance)` (lines 464–465)". They now read `**Fixed (requirement)**`, set by `merged-rows-tier-fix.md` on 14 October. The inconsistency with truth 6 that line 48 describes is therefore gone. NOTES.md was honest when written and is now stale; the two lines need a sentence each saying the fix was applied, or deletion.

Count slip, not a fail: NOTES says "Seven fixes" for Carly's words; there are eight token changes on six lines (41 and 369 each carry two). Immaterial.

## Fail list

1. Line 529: the *precedent record* bullet's tail "; section 11 gives its nine lines" is new wording; the bullet itself was not in the moved paragraph. Cut to the chapter's own words or drop.
2. NOTES.md lines 48 and 64: rows 12 and 13 recorded as unapplied `**Fixed** (stance)`; merged-rows-tier-fix.md has since set them to Fixed (requirement) at 464–465. Update the notes.
