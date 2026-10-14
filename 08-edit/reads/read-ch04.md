# Read: Chapter 4 — From data to evidence

## A. Coverage

- File: `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch04-from-data-to-evidence.md`
- Total lines: 867 (`wc -l`).
- Ranges read with the Read tool: 1–220, 221–420, 421–620, 621–867.
- Every line was read; the last line read was 867 ("Silent on. Everything in sections 3, 4, 8, 9 and 10 …").
- Context read first: BRIEF-v2 §1, §4, §5 (lines 7–70); Chapter 0 "How a chapter teaches" and "The legend" (lines 44–127); LIBRARY-PASS "What the pass found, in one page" (lines 1–25).

## B. What the chapter teaches

The chapter decides what a number must carry before a dashboard may show it as evidence, and it answers with five things (grain, denominator, provenance, nothings, comparability) plus three facts about data (a total speaks for the biggest; size does not cure selection; an outlier is a question). It is for a first-time reader who will build or test the Vibe Map's data layer, and it teaches almost entirely from standards (OSR Code 3.0, Eurostat, SDMX, W3C, Analysis Function) with a smaller number of experiments. A newcomer would take away seven recitable truths (lines 446–458), a ten-line provenance set (207–218), a ten-line comparison declaration (332–341) and a vocabulary for six (or seven) kinds of empty cell (268–277). The chapter's own position is unusually honest about its weakest wall: no study shows provenance on the face changes a decision (222), and it says so where the thesis rests.

Best passages, which must survive any edit:
- 124–128, the midnight census: a period is a rule not a fact, with the hospital bed, the day-ward cap and the 6pm–6am window. Concrete, dry, and lands the general lesson in one sentence ("the official definition does not have to justify its choice").
- 244–248, Codd and `coalesce(sum(x), 0)`: the database history of nothing, ending in "the sentence that explains a thousand dashboards". The best-written stretch in the chapter.
- 385–389, Meng: "Quality times quantity times difficulty"; 2.3 million records worth 400; "the more the data, the surer we fool ourselves". Clear point of view, rhythmic.
- Honourable mention: 373–377, the 78%/32% worked case, where the chapter turns its own first truth on the studio's number ("the chapter owes it the same sentence it gives everyone else's").

Passages a newcomer could struggle with:
- 385, Meng's identity is given in notation ("ρ_R,X … √((N − n)/n) … σ_X") before the plain-words version arrives in the next sentence. Readable, but the symbols could sit after the words.
- 250, "relvar" is explained inline; fine. 254–260, the code lists ([b], [c], SDMX M/L/Q/K/W …) are dense; the summary table at 268–277 rescues them, but a reader meeting SDMX for the first time will skim 260.
- 197, "(The verifier could not settle the exact wording …)" is production voice inside teaching prose; a newcomer does not know who the verifier is.
- 532, the rules-table preamble says "Kind and tier as in Chapter 0" and then explains Practice, †, and Secondary again, which the Before-you-start already did at line 12.
- 580, "the four-line record Chapter 16 will describe" assumes a chapter the reader may not reach; and Chapter 0 now says the deviation entry is nine lines (Ch0 line 97), so the figure is stale.

## C. Verdict on the chapter body

**Stands with light edits.**

The teaching sections do their job as written. The question (20) is one question. The 60-second version (26–40) gives the answer first: line 26 states the thesis ("A number is not evidence until five things about it are settled"), lines 28–36 name the five, 38 the three facts, 40 the seven truths. The body sections 3–10 each test a belief named in section 2 and say which section answers it (68, 72, 76, 80, 84, 88, 92, 96), and the truths at 446–458 are traceable to the body. Nothing contradicts itself; the only tension (ten lines of provenance against Chapter 3's "nothing crucial behind a click") is named and resolved at 343 and 653.

60-second version: **763 words** over lines 26–40. It gives the answer first, but at 763 words it is a four-minute version. Lines 28–36 (the five things) carry the answer; line 38 (the three facts about data) is a second answer packed into one 150-word paragraph; line 40 then lists the seven truths a third time in the chapter's first page. Trimming to the five things plus one sentence on the three facts would get it near 400 without losing the answer. This is a recommendation about the 60-second section only, not about body length.

Specific fixes (12):
1. Line 10: "breaks or isnt reliable" — missing apostrophe in a quotation from Carly's register (and the same quotation is correct at line 46 in paraphrase). Check the brief's wording and fix.
2. Line 10: Before-you-start says "two of them bear on this chapter" then line 46 says "the second and fifth items on Carly's failure register" — the ordinal is only in one place; harmless, but 46 should match however Chapter 1 numbers the register.
3. Line 128: "published online in late 2023" versus the sources list (694) and rules table (538) which say "Pierce et al. 2024". Pick one.
4. Line 197: remove the parenthetical "(The verifier could not settle the exact wording of the temporal definition from the page; it is paraphrased.)" from the body; it is already in the sources list (726) and the flags (634). Leave "which it recommends be given as a closed interval" as the paraphrase.
5. Line 283: "a distinction no dashboard the author has seen makes" — author voice; "a distinction few dashboards make" says the same.
6. Line 377: "(see the flags)" points at the furniture; "the prototype can supply them" stands alone.
7. Line 385: move the notation after the plain-words sentence, or drop the subscripts.
8. Line 417: "[sic]" after "prescence" is correct practice but the quotation could be trimmed before the misspelling.
9. Line 532: the table preamble re-explains †, Practice and Secondary; cut to "Kind and tier as in Chapter 0" once the register carries the legend (Ch0 line 60 says the table should not repeat it).
10. Line 580: "the four-line record Chapter 16 will describe (what rule, why, for whom, what proved it)" — Chapter 16 now exists and Chapter 0 (line 97) calls it a nine-line deviation entry. Update the count and tense.
11. Line 171 and 643–644: the Chapter 1 Q1–Q3 re-mapping is stated in the body, the flags and Looking back. Keep the body sentence; the other two are furniture.
12. Lines 446–458: the seven truths carry "Fixed", "Fixed as a stance", "Fixed as a procedure" — see D12; once the register's tiers are adopted, 456 and 458 should say which Fixed sense (requirement/sequence/statement of the record) or Adaptable (house default).

No body section should be cut for length. Section 6 (226–295) is the longest at about 70 lines and is the chapter's centre; section 5's lists (173–177) are heavy but are the standard being quoted so it can be looked up, which line 14 says is the point.

## D. Furniture and status: inventory

1. **Status line under the title.** Line 4: "*Version 2, draft 2 · 6 October 2026 · revised after a cold read and an independent verification pass (research log, Entry 4)*". Retire; the research log holds it. Line 3 ("Dashboard Design · Part 1: The analytical foundation") is a part label and can stay.

2. **"Before you start".** Lines 8–14. Line 10 is the re-introduction (book, studio, Vibe Map, four things from Chapters 1–3, Decision Book, Style Guide). Line 12 repeats Chapter 0's kinds, tiers, flags, dagger and "as quoted in" conventions. Line 14 is chapter-specific and worth keeping somewhere in the body: it introduces OSR, the Analysis Function and Eurostat once, and explains why the chapter is standards-heavy. Recommendation: move 10 and 12 out (Chapter 0 owns them); keep 14, perhaps as the opening of section 1 or as a short "Three bodies you will meet" note.

3. **"Where the choice is yours"**, lines 488–510. Ten open choices:
   - 492 Which grain to display? Position: "the one shown is named and … the row count under it is stated. The choice between them is Carly's and the readers' of Chapter 2."
   - 494 Which instant or window stands for a day? Position: "any boundary that suits its subject, provided it says so and never changes it silently."
   - 496 Which denominator to lead with? Position: "the chosen base is visible and the alternatives reachable, and … a small base carries its interval."
   - 498 Which concentration instrument? Position: "A median beside the mean is the minimum … showing none is not an option under truth 5."
   - 500 Whether "not applicable" is a seventh kind of nothing? Position: none; "a decision about the display's vocabulary". `[Validate with users]`
   - 502 How to show a nothing (code, word, pattern, sentence; blank, hatched, annotation)? Position: "a design decision governed by Chapter 3's rules on colour and words, and the design system's."
   - 504 How much provenance on the face? Position: "period, status, and the fact that caveats exist, at minimum" on the face; the rest one tap away; "a layout decision for Chapter 11". `[Revisit → Ch 11]`
   - 506 Suppress or perturb? Position: "the Decision Book chooses suppression with secondary suppression … it should be made once and declared."
   - 508 Which outlier rule, and which threshold? Position: "The median absolute deviation is the literature's recommended default and 2.5 a common threshold".
   - 510 Which neighbours (CIPFA, ONS classification, bespoke, none)? Position: "the choice is open and must be shown, and the variables must not include the thing being compared."
   Row 573 of the rules table lists the same ten as one Adaptable row.

4. **Other places the chapter asks Carly to decide or awaits steer.**
   - 128: "The chapter takes the window only as an official definition and goes no further into the sector; that knowledge is Carly's." (scope statement, body)
   - 277: "Whether 'not applicable' is a seventh kind or a sub-kind of the fifth is a decision for Carly, and this chapter flags it rather than making it."
   - 492: "The choice between them is Carly's and the readers' of Chapter 2."
   - 516: "The sector knowledge is Carly's; the method is the chapter's."
   - 549 (rules table, tier cell): "Adaptable (how to name it) — flagged for Carly".
   - 624: "Whether the studio's vocabulary grows is for Carly".
   - 666: "All logged for Carly as candidate additions."
   - 842: "Decision Book Ch 6 (DAT-14), via Carly".
   - 623, 832, 855: the data contract "was not re-read in this sprint" / "not available to this sprint" — an awaiting-input note repeated three times.
   No "TBD", "awaits steer" or "the house has not chosen" strings.

5. **"The symmetry test" section.** None as a heading. The test is named once, in the gaps table at 856 ("a symmetry failure … run the symmetry test on the studio's own findings first"). Chapter 0 line 123 says the test "was born in Chapter 4's gap table"; that row is the birthplace and is process, not teaching. The body already applies the test at 375–377.

6. **"Open questions and flags"**, lines 621–654. 32 bullets. Flag counts in the section (one bullet can carry more than one flag): Further research 15; Prototype flag 5; Validate with users 4; Revisit → Ch 9 (Ch 1, 5, 6, 7, 8, 9, 10, 11, 13); Revisit at end 1; Rich reference 2; Counterbalance 1.
   - Prototype flags: 635 provenance-panel probe with the three user groups (also `[Validate with users]`); 637 measure Meng's defect correlation against a random benchmark; 638 count the nothings per source and month; 639 false-flag rate of the chosen outlier rule on shuffled data; 640 the 78%/32% as a Lorenz curve with Gini.
   - Validate with users: 624 seventh kind of nothing; 635 provenance panel probe; 641 which labelled nothing reads as which, then the same table with blanks; 642 which of the ten provenance lines readers open when they distrust a figure.
   - These are candidates for PROBES.md; I did not open PROBES.md and cannot say which are already there.
   - Lines 623, 625–634, 636 are research-log items (what could not be fetched, which tool truncated what). They are not open questions for a reader and belong in the ledger.

7. **"Looking back"**, lines 656–666. Seven bullets against Chapters 0–3, version 1 and the Decision Book. Bullet 665 (Chapter 0) proposes legend changes that Chapter 0 has since made (Ch0 lines 97, 102: "Fixed as a stance"/"procedure" re-based; "Secondary" defined). It is now historical. Bullet 666 is the Decision Book audit (agrees / conflicts / silent on) and duplicates the conflict log at 861–867 and gaps rows 842–843. Move the whole section to the working record; the one teaching point in it (662: the fact of qualification on the face, the qualification one tap away) is already in the body at 343.

8. **"Gaps found"**, lines 836–859: 18 rows (842–859). Uses the older four columns with coloured cost (Ch0 line 66 says the cost is now a word).
   - Real knowledge gaps a reader needs (keep in text, mostly already there): 842 dashed-join ambiguity (body 287); 843 provenance set omissions (body 220); 845 seventh kind (body 277); 847–851 the rules the Decision Book lacks (these are what the rules table is); 852 "reliable" two senses (body 187); 859 no evidence that provenance on the face changes a decision (body 222).
   - Process notes (move): 844 Q1–Q3 re-mapping (a Chapter 1 fix); 846 version 1 vocabulary; 853 unreachable canonical texts; 854 legend proposal (done); 855 data contract not available; 856 first-draft close rewritten; 857 verifier corrections (paraphrases, two wrong numbers, six truncations); 858 Fixed qualifiers (superseded by register).

9. **Conflict log**, lines 861–867: three paragraphs (Agrees / Conflicts / Silent on). Candidates for the Decision Book/design system working record: DAT-14 "dashed" wording (865, 842); DTA-19 provenance set omissions (865, 843); a status-chip set for the kinds of nothing (865). Facts the reader needs: none that are not already in the body (287, 220, 277). The "Silent on" paragraph (867) is a candidate list for the Decision Book and is process. Move all three.

10. **Production words in body prose (lines 44–527).** Count: 6.
   - 112 "One consequence for display is our reading rather than any source's"
   - 128 "that knowledge is Carly's" (scope)
   - 197 "(The verifier could not settle the exact wording …)"
   - 283 "no dashboard the author has seen"
   - 320 "the resemblance is, in our reading, a sign that the list is general"
   - 377 "(see the flags)"
   "Agent" at 201 and 209 is the PROV term, not production. "Our reading" is the book's own licensed phrase (Ch0 line 127) and is acceptable; "verifier" is not. Outside the body: 4 (cold read, research log), 532 (dagger explanation), 623/832/855 (sprint), 665 (cold reader), 671 (research agent, orchestrator, verification pass), 856–857 (cold reader, verifier).

11. **Flags inside the body prose (44–527).** 17: Rich reference 6 (48, 240, 320, 365, 387, 397); Revisit → Ch 6 (112, 164, 171, 197, 316, 504); Validate with users 3 (222, 277, 500); Further research 1 (222); Revisit at end 1 (295); Prototype flag 0; Counterbalance 0. In every case the bracket sits at the end of a sentence or paragraph and removing it leaves the sentence readable. Line 277's "this chapter flags it rather than making it" would still read correctly without the bracket.

12. **Rules table**, lines 536–574: 39 rows. Tier wording used: **Fixed** (24); Fixed (adopted) (2); Fixed as a stance (2, plus 536 "Fixed (unit); Fixed as a stance (count)" and 538 "Fixed as a stance; the rule itself Adaptable"); Fixed as a procedure (554; 567 "Fixed as a procedure; Adaptable (rule and threshold)"); Fixed as disclosure (562); "Fixed (that one is shown); Adaptable (which)" (560); Adaptable (2 plain, 549 "flagged for Carly", 564 "strong default …"); Decorative (574). The seven truths (446–458) also use "Fixed as a stance" (456) and "Fixed as a procedure" (458).
   - Source cells citing † or abstract-only: 540 (Hájek 2007†); 541 (Spiegelhalter 2005†); 565 (Aguiar & Waldfogel 2015 (abstract)). Row 538 cites Pierce et al. 2024 (secondary). Row 561 cites Juran and Elberse (secondary).
   - Could the table take the register's tiers without changing rule wording? Yes. Every tier qualifier lives in the Tier cell, not the Rule cell. The six rows with stance/procedure/disclosure/adopted wording (536, 538, 554, 556 n/a, 562, 563, 565, 567, 545, 558) would re-base per Ch0 line 97: stance → Adaptable (house default) unless the grounds show a requirement; procedure → requirement or sequence. The one place a rule's wording and tier are entangled is 573, whose Rule cell is a list of the ten open choices and whose tier is Adaptable; that row is a pointer to section 12, not a rule.

13. **The ten library-pass corrections.** None names Chapter 4. Checked each: 1 (Ch7/RSS), 2 (Ch1/Kaliisa), 3 (Ch9/FixMyStreet), 4 (Ch11/Zhi), 5 (Ch16/Paterno), 6 (Ch12/Tintarev), 7 (Ch2, Ch9/Birt), 8 (Ch13/EHRC), 9 (Ch12/Stevens), 10 (Mogstad, Becker, Yang Ch3, Berg & Pattillo Ch6, Weissgerber, Glaeser, Javed, EN 301 549) — no Chapter 4 line. Indirectly: correction 1's point that the RSS report supports "any ordering carries its interval" rather than a prohibition is consistent with Chapter 4's row 541 ("carry intervals and are shown in a funnel, never ranked raw or ranked adjusted") and body 164, which cite Gelman & Price and Spiegelhalter, not the RSS report; no change needed here. The "daggers that can be removed" list (LIBRARY-PASS line 22) names none of Chapter 4's three † rows.

14. **Nightlife illustration**, section 13, lines 514–526. Heading is the older form "What this means for a nightlife dashboard" (Ch0 line 59 says Chapters 1–5 use this heading). Line 516 opens "An illustration, not a specification. The sector knowledge is Carly's; the method is the chapter's." It uses no invented place data: the only figures are the studio's 78%/32% (518, 524), the 6pm–6am window (518) and the "under 1,000 capacity" threshold (518), all already in the body. No named venues or made-up counts. The worked declaration at 343 ("two councils' monthly counts of licensed premises … council A / council B") is invented and is not labelled as such, but it is a form-filling example of the ten-line declaration, not place data.

## E. House style

- "night-time" hyphenated: 1, at line 699, inside the ONS publication title *The night-time economy, UK: 2022* — a quoted title, so it stands. Body uses "night time" at 128, 478, 518.
- "cultural contribution": 0.
- Em dashes (—): 329 across the file, including those inside quotations and table cells. Count only.
- "robust": 421 ("the robust alternative they recommend") and 630/820/821 (Huber's and Hampel's titles). All are the statistical term, not the buzzword. "leverage", "unlock", "empower", "deliver", "tackle", "this matters", "at the heart of": 0. ("deliver" appears only inside the FINRA quotation at 122 and the PROV definition at 201.)
- Americanisms: all inside quotations or proper names (CDC "Centers", "behavior" at 397/413 in Salganik and Chandola, "organizations" at 435 in Bradley, "standardization" at 425 in Osborne & Overbay). Line 110 "organizational" is inside the EU regulation's own English. None in the chapter's own voice.

## F. Repetition

The gap rule is the clearest case: line 34 (60-second version, quoted), 287 (body, quoted in full), 472 (record beneath the truths), 551 (rules table), 597 (checklist), 842 (gaps), 865 (conflict log), 660/662 (Looking back). Eight statements. The first five are the chapter's teaching structure working as designed (answer, evidence, truth, rule, check) and are acceptable. The last three are furniture restating the same conflict and would collapse into one working-record entry.

A second case, the Chapter 1 Q1–Q3 re-mapping: 171 (body), 643 (flags), 660 (Looking back), 844 (gaps). One body sentence and one log entry would do.

Within the teaching sections the repetition is by design: the seven truths at 446–458 are the 60-second version's last paragraph (40) expanded, and the checklist (584–617) is the rules table (536–574) as imperatives. The one place the structure over-repeats is the 60-second version itself, which lists the seven truths (40) that section 11 then lists again with the same wording.

## G. One line for Carly

This chapter does not need rewriting: its teaching stands, and what it needs is the status line retired, the Before-you-start, Looking back, gaps table, conflict log and research-log flags moved to the working record, a dozen small fixes, and a 60-second version trimmed to actually take sixty seconds.
