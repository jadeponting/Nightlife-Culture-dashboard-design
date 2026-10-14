# Read log: Chapter 3 — The canonical truths of showing data

## A. Coverage

- File: `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch03-the-canonical-truths-of-showing-data.md`
- Total lines: 714 (`wc -l`).
- Ranges read with the Read tool: 1–180, 181–360, 361–540, 541–714.
- Every line was read; no range was skipped and context did not fill.
- Context read first: BRIEF-v2 §1, §4, §5 (lines 7–70); Chapter 0 "How a chapter teaches" and "The legend" (lines 44–128); LIBRARY-PASS first page (lines 1–25).

## B. What the chapter teaches

The chapter asks which of the field's rules for showing data were ever tested, which survived, and which survivors are hard lines. It answers for a first-time reader (a technologist, analyst or facilitator) by walking the folklore (seven beliefs, lines 56–84) through the experiments, topic by topic: perception, colour, words, the glance, ornament, axes and scales, interaction and defaults, uncertainty, risk and literacy, and the accessibility standards. The newcomer leaves with seven rules a dashboard can be held to (lines 365–371), a record of the evidence under them (377–387), and a clear sense of how thin or thick each piece of evidence is, because the chapter names sample sizes and caveats as it goes. The most useful single idea is "choose the comparison, not the chart" (lines 114–116, 365); the most surprising is that the title decides what a chart "showed" and is trusted least while remembered most (168–170).

Best passages, which must survive any edit:
- Lines 92–102: the hierarchy of encodings told as a story — what Cleveland and McGill tested, what they called conjectural, who replicated the top, how pies are actually read, and the plain restatement at 102 ("So here is what the hierarchy settles, stated plainly").
- Lines 264–266: the "85% ignore interactives" footnote traced to its origin and replaced with measured rates, ending "People finish; they do not fiddle; and on a phone, where hover does not exist, they do less of both."
- Lines 216–218: Ajani's declutter-against-focus experiment and the closing judgement: "the thing that makes a chart communicate is not the ink you remove but the message you add … and that clean reads as professional, not as honest."
- Also strong: 160–170 (title first, longest, instead), 226 (truncation: "People read the right numbers and feel the wrong size"), 302 (confidence interval against prediction interval: "the reader hears that everyone gets the mean").

Passages a newcomer could struggle with:
- Line 32 and line 270: "d = 0.68" is explained only in "Before you start" (line 14). If that section moves, the definition of *d* and *n* must stay in the chapter; line 14 is chapter-specific, not a re-introduction, and should be kept (see D2).
- Line 10: "Chapter 2's finding that there is no reader in general" and line 152 "Chapter 2 found that … moved readers' perception by nine points" assume Chapter 2. Both are cross-references, not dependencies; a reader can carry on.
- Line 349: `role="img"`, `graphics-document`, "accessible name" are production terms for a builder; appropriate for the section but opaque to a facilitator. Not an error.
- Line 467: "protanopia" is defined inline. Fine.

## C. Verdict on the chapter body

**Stands with light edits.**

The teaching sections do their job as written. The question (line 20) is one question; the body tests each belief in turn and says so (line 84 "Each belief has a true core. The sections below say how much"); the truths (365–371) and record (377–387) are distinct and honestly caveated; the rules table carries why, kind, tier and source; the break test (467) is concrete; the illustration (411–423) is labelled and uses no place data. Nothing contradicts itself. The edits below are a term, a figure or a sentence each.

Specific fixes (12):
1. Line 226: "83.5% of participants across all 5 studies" — the library pass (correction 10) found the paper says "these 5 studies", not "all 5 studies". One-word fix.
2. Line 415: the brief is quoted as "people dont trust it"; BRIEF-v2 line 19 reads "people don't trust it". Restore the apostrophe.
3. Line 526: "Nineteen truths is still a long list" — the chapter prints seven truths and eleven record bullets (18 items). The count is from an earlier draft; correct it or drop the number.
4. Line 467: "log the break in the four-line record Chapter 16 describes (what rule, why, for whom, what proved it)". Chapter 0 line 97 says Chapter 16 gives "the nine-line deviation entry". One of the two is wrong; check Chapter 16 and align.
5. Lines 370, 371, 452, 458: "Fixed as the planning assumption" and "Fixed as a stance" are the older tier wordings Chapter 0 (line 97) says the register has re-based. Update to the register's wording (see D12); the rule text need not change.
6. Line 429: the rules-table preamble restates the legend and the dagger. Chapter 0 line 60 says the table does not repeat the legend. Candidate to cut to one line or remove.
7. Line 12: the chapter's own dagger definition ("read at the authors' published abstract only") is the narrow Chapters 1–6 sense; Chapter 0 line 101 gives the widened one. If "Before you start" moves, nothing is lost; if it stays, align the wording.
8. Line 336: "Carly asked that the W3C documents be sorted into hard lines and interpretable guidance" — fine as provenance, but for a reader it reads better as "The brief asked …", matching line 361 and 415, which already use "the brief".
9. Line 541: proposes a new legend sub-kind, "Practice backed by analogous Evidence". Chapter 0 (line 85) added "(adjacent domain)" and Practice but not this. Either Chapter 0 adopts it or truth 3 (line 367) and rule row 441 use a kind the legend recognises (for example "Practice + Evidence (analogous)"). Decision for Carly; the chapter's reasoning stands either way.
10. Line 176: "people are spend on the page" [sic] — the chapter already marks the ONS typo. No change; noted so nobody "fixes" it.
11. Line 266: Boy et al. carries a dagger in the body but Sources (628) lists two Boy papers, one secondary and one abstract. Say which the dagger refers to, or leave as is; minor.
12. Line 379: "from 36 people on a smartwatch" and line 442 repeat the same caveat; acceptable, but the record bullet could drop it since the table carries it. Optional.

60-second version: lines 26–36, **710 words**. It does not give the answer first. The seven truths, which answer the question at line 20, arrive in the final paragraph (line 36); the first paragraph (26) sets up the search and paragraphs 28–34 are findings. A reader with sixty seconds gets the method and not the list. The fix is a reorder, not a cut: move line 36's sentence ("So the canonical truths are these: …") to follow line 26, or open with it, and let 28–34 stand as the reasons. At 710 words it is a four-minute read; if Carly wants it to fit its name, paragraphs 28–34 could be tightened to one sentence per topic, but that is a choice, not a requirement, and the body should not be cut for it.

## D. Furniture and status: inventory with lines

1. **Status/draft lines under the title.** Line 3: "*Dashboard Design · Part 0: Foundations*" (keep; it is the part label). Line 4: "*Version 2, draft 2 · 6 October 2026 · revised after a cold read and an independent verification pass (research log, Entry 3)*" — status, retire.

2. **"Before you start"** lines 8–14. Lines 10 and 12 re-introduce the book, Carly, the Vibe Map, the Decision Book, the design system, the three user groups, and the kind/tier/flag/dagger conventions — repeated from Chapter 0; move. Line 14 (the *d* and *n* conventions, "since this chapter reports experiments") is chapter-specific teaching and should stay in the chapter, under section 1 or as its own short note.

3. **"Where the choice is yours"** lines 391–407. Eight open choices:
   - Line 393: Which chart form, below a precise ratio comparison? Position: "convention, the reader's schema, and the comparison you want made do … A donut is not worse than a pie; a treemap is defensible … a radial bar is six times slower." *Adaptable.*
   - Line 395: How many categorical colours should the Vibe Map allow? Position: "Seven is the experimental ceiling for search; four or five is the house limit of the UK statistics bodies … Where to set the Vibe Map's limit is a design-system decision." *Adaptable.*
   - Line 397: How much text on a chart, and in what voice? Position: "more than designers give and the trend in the title; how much more, and in what voice, is the studio's." *Adaptable.*
   - Line 399: Should the Vibe Map look like a dashboard, a map, a flyer or something else in the first fifty milliseconds? Position: none; "the creative decision this book never makes. *Adaptable; Carly's.*"
   - Line 401: Which uncertainty form (dotplot, HOP, gradient, violin, ensemble)? Position: "depends on the question … and the reader … *Adaptable; the prohibition on bare intervals and hard boundaries is Fixed.*"
   - Line 403: May a line-chart axis be broken? Position: "Permitted, and a chosen effect size; declare it. *Adaptable.*"
   - Line 405: Overview or search first; animation or small multiples; scroll or step? Position: "The reader's arriving question, the task, and the device decide; none is a law. *Adaptable.*"
   - Line 407: Two or three significant figures? Position: "which, by column, is a judgement. *Adaptable within the Fixed ceiling of the data's own precision.*"

4. **Other places the chapter asks Carly to decide or awaits steer:**
   - Line 336: "Carly asked that the W3C documents be sorted into hard lines and interpretable guidance." (provenance, not a pending decision)
   - Line 399: "*Adaptable; Carly's.*"
   - Line 417: "What the Vibe Map claims to be is Carly's decision; this chapter only says that whatever it claims, it should look like that at once."
   - Line 443 (rules table): "Adaptable (what it claims to be is Carly's)"
   - Line 542: "These are logged for Carly as candidate additions to the Decision Book's data chapters."
   - Line 697 (gaps table): "Decision Book Ch 6, via Carly"
   - No "steer", "awaits", "TBD" or "the house has not chosen" in the file. "not yet" appears once (line 286) and "has not" once (line 218), both about evidence, not decisions.

5. **"The symmetry test"** — absent. The word "symmetry" appears once (line 110) as a Gestalt principle. Consistent with Chapter 0 line 123 (the test runs from Chapter 4).

6. **"Open questions and flags"** lines 499–528. Flag counts in the section: [Further research] 14; [Prototype flag] 4; [Validate with users] 3; [Revisit → Ch n] 6 (Ch 5, 7, 11, 12, 13, 14); [Revisit at end] 1; [Rich reference] 1 (a single long entry listing nine sources); [Counterbalance → Ch 2 §5] 1.
   - [Prototype flag] line 501: legends against direct labels — run the experiment in the prototype.
   - [Prototype flag] line 505: the big-number tile — is a KPI number read, trusted or misread against a chart or table cell.
   - [Prototype flag] line 515: measure the glance — time-to-first-interaction, what is touched, which device.
   - [Prototype flag] line 516: measure chart literacy — a short VLAT-style test with the three user groups.
   - [Validate with users] line 517: the sceptic's uncertainty — same finding as bare line, ensemble, dotplot, to readers who arrive opposed.
   - [Validate with users] line 518: the designer's blind spot — someone who did not choose the default says what the first screen shows.
   - [Validate with users] line 519: big number against sentence — which is remembered, which trusted.
   - Body-prose flags that feed the same list: [Prototype flag] at 250 (big number) and 330 (chart literacy); [Validate with users] at 272 (blind spot). These duplicate 505/516/518. Whether they are already in PROBES.md was not checked (the brief did not give that file's path); the caller should cross-reference.

7. **"Looking back"** lines 530–542. Thirteen bullets against Chapters 0, 1, 2, version 1, and the Decision Book, including (line 540) the Jachimowicz verification episode and (line 542) the Decision Book agrees/conflicts/silent-on log in prose. Move to the working record; the Decision Book paragraph (542) is the conflict log Chapter 0 line 67 describes, written as prose.

8. **"Gaps found"** lines 691–706: 10 rows, in the older four-column form with coloured cost (Chapter 0 line 66 notes this for Chapters 0–13).
   - Real gaps a reader should know (keep in text, or in a short "what the field has not tested" note): row 7 (line 703) — no study of the big-number tile, legends against labels, or UK chart literacy; row 6 (702) — the 85% statistic is an anecdote. Rows 1–5 (697–701) are Decision Book/design-system gaps: the reader benefits from knowing them, and the body already states each (lines 102, 180, 228, 174/168, 242–244), so the rows themselves can move to the working record.
   - Process notes (move): row 8 (704) — "a research agent's correction was itself wrong"; row 9 (705) — the first draft's misquotation of the OSR, "the sprint's most serious catch"; row 10 (706) — "The cold reader found the Fixed tier applied to small … studies"; row 2's second half (698) — legend sub-kind proposal.

9. **"Design system (Style Guide v1.5) — conflict log"** lines 708–714: three paragraphs (Agrees, Conflicts, Silent on). The Decision Book half is in Looking back at 542 (one long paragraph). Candidates for the design system/Decision Book (move to a working record): the "where on a dashboard the joy goes" line (712), the "Silent on" list (714), the Decision Book "Conflicts" and "Silent on" at 542. Facts the reader needs are already in the body (3D and pie reasons at 234–236; title's power at 166–170; truncation at 226–228).

10. **Production words in the body prose** (lines 18–497): essentially none. "orchestrator", "verifier", "cold read(er)", "research agent", "sprint", "research log", "ledger" appear only at lines 4 (status), 540 (Looking back), 548 (Sources preamble), 704–705 (Gaps). SOURCES.md, STATE.md, [Proposal], "our reading" do not appear. Near-misses in the body: line 250 "the gap is logged"; line 180 "This chapter searched for the experiment behind it" (fine); line 12 and line 429 explain the dagger (furniture). Count of listed words in body prose: 0.

11. **Flags inside the body prose** (lines 18–497, excluding the legend list at line 12 and the table note at 429): [Rich reference] 2 (44, 296); [Further research] 4 (180, 232, 286, 316); [Prototype flag] 2 (250, 330); [Validate with users] 1 (272); [Counterbalance → Ch 2 §5] 2 (316, 386); [Revisit → Ch 13] 1 (355). Total 12. All sit at the end of a paragraph or bullet; removing the bracket leaves every sentence readable. Line 330 is the one case where the flag carries a clause ("`[Prototype flag]` — the Vibe Map could."); it would need "The Vibe Map could." as a sentence.

12. **Rules table** lines 433–461: 29 rows. Tier words used: "Fixed" (plain, 17 rows); "Fixed for precise comparison; Adaptable as a general form rule" (434); "Fixed (pattern maps); Adaptable where the task is reading a value" (437); "Adaptable within the ceiling" (438); "Fixed (evidential status stated)" (441); "Adaptable (strong default)" (442, 445); "Adaptable (what it claims to be is Carly's)" (443); "Fixed as defaults" (448); "Fixed (ceiling); Adaptable (digits)" (450); "Fixed as a stance" (452); "Fixed as the planning assumption" (458); "Adaptable" (449, 453, 457, 460); "Decorative" (461). No "Fixed as a procedure". Rows whose source cell cites a † source: 435 (Birch 2012†), 446 (Yang et al. 2021†), 448 (Romano et al. 2020†; Pighin et al. 2011†), 449 (Vessey & Galletta 1991†), 458 (Galesic & Garcia-Retamero 2011†). The table could take the register's tiers without touching the rule wording: the tier cell is a separate column and the rule and why cells do not mention tier. The only knock-on is the truths at 370–371, whose italic tails repeat the old wording.

13. **Library-pass corrections touching this chapter.** One: correction 10, Yang et al. — line 226, "83.5% of participants across all 5 studies" should read "these 5 studies". None of the other nine touches Chapter 3. The "daggers that can be removed" note (Javed et al. 2010) does not apply: the chapter already lists Javed at source (line 622) without a dagger.

14. **Nightlife illustration** lines 411–423. Labelled at line 413: "*An illustration, not a specification.*" (the heading is the Chapters 1–5 form, "What this means for a nightlife dashboard"). It uses no place data, invented or real; it reads the brief's three failures (line 415, quoting BRIEF-v2 line 19) through the chapter's mechanisms. Line 417 defers the "what it claims to be" decision to Carly.

## E. House style

- "night-time" hyphenated: 0. "night time economy" appears once (line 421), two words, correct.
- "cultural contribution": 0.
- Em dashes used as punctuation: 235 in the file (count only, as instructed; many are inside quotations).
- "robust": 1, line 316, inside a quotation ("evaluate its robustness"). "deliver": 3, lines 345 ("delivers information", plain use), 353 ("no deliverables", plain use), 705 ("before delivery", gaps table). "leverage", "unlock", "empower", "tackle", "this matters", "at the heart of": 0.
- Americanisms: all instances of "color", "visualization", "behavior", "organization", "labeled", "percent" sit inside quotations or source titles (lines 44–328 as quoted; 516 "Visualization Literacy Assessment Test" and 528 are titles). The chapter's own prose is British throughout ("colour", "visualisation", "behaviour", "programme" not used).
- Line 176 "[sic]" marks an ONS typo correctly.

## F. Repetition

"Colour is never the only carrier of meaning" appears at line 36 (60-second version), 150 (section 4, with the WCAG text), 342 (section 12 list), 367 (truth 3), 387 (record), 423 (illustration), 435 (rules row), 473 (checklist): eight statements. "Start bars at zero" similarly at 36, 226–228, 368, 446, 482. This is the chapter's teaching structure working as designed: each layer says it in the register of that layer (answer, evidence, truth, rule, check) and the body states it once with its evidence. The one place it reads as padding is the illustration's fourth paragraph (line 423), which restates three rules (defaults, hover, colour) already in the truths and the table without adding a nightlife mechanism; it could lose its last sentence. Not a structural issue.

## G. One line for Carly

Chapter 3 does not need rewriting: its body teaches as it stands, and what it needs is its status line retired, "Before you start", "Looking back", the gaps table and the two conflict logs moved to the working record, the seven truths put at the top of the 60-second version, and a dozen one-word or one-line fixes (chiefly "all 5 studies" to "these 5 studies" at line 226 and the old tier wordings brought in line with the register).
