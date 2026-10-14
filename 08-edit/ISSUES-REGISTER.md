# Dashboard Design · issues register

*Stage 1, 14 October 2026. What stands between the book as it is and a finished, published book. Nothing here has been changed yet. The line-by-line inventory for each chapter is in `08-edit/reads/read-chNN.md`; this file is the summary.*

**The headline.** All seventeen chapters stand. Sixteen were read in full by an agent working to one brief; two were also read in full by Claude. Every verdict is "stands" (Chapters 2, 6, 11, 13) or "stands with light edits" (the rest). None needs structural work. The teaching text, from the question to the sources, is kept as written. What follows is the loop to close around it.

**Kinds of action used below**
- **Retire:** a status or process line that describes the book as unfinished or describes how it was made. It goes, or moves to the record of how the book was made.
- **Move:** belongs in the reference section behind the book, not in the chapter.
- **Fix:** a factual or internal error with one right answer, applied once.
- **Log:** an open choice; it goes into the one decision log with the book's steer and the moment the build will raise it.
- **Keep:** noted so that nobody "fixes" it.

---

## 1 · Book-wide

### 1.1 The book still says it is a draft

| Where | What it says | Action |
|---|---|---|
| Every chapter, line 4 | "Version 2, draft 2 · [date] · research log, Entry N" (Chapters 1 to 4 add "revised after a cold read and an independent verification pass") | Retire |
| Chapter 0, lines 3 to 4 and the closing section | "for Carly's steer"; "`00-plan/STATE.md` says which chapters she has read"; "'Awaiting steer' means she has not read it yet" (glossary) | Retire; the glossary entry for "steer" is rewritten as Carly's direction, full stop |
| Chapter 16, lines 6 and 697, and the Postscript | "a postscript exists"; "nothing in it is finished until it has survived her"; the postscript itself | Retire once the postscript's three facts are in the body (1.6) |
| `00-plan/STATE.md` | "draft 2 and unread by Carly"; "Everything open is Carly's" | Rewrite as the Data Brain's: finished, published, where things are, what to know before relying on it |
| `README.md` | "seventeen chapters at second draft"; "Carly has not yet read the chapters; nothing in them is finished until she has" | Rewrite |
| `AGENTS.md`, "Now that the chapters exist" | "The book is at draft 2 and Carly has not yet read it" | Rewrite the section; the method above it is history and stays |
| `05-book/reader.html` masthead | "Draft reader. Chapters 1–16 are at draft 2 and have not yet been read by Carly" | Rebuild |
| Knowledge Base entry (the map) | "seventeen chapters, draft 2"; labels "Working draft", "Human review needed"; "The second draft is written; Carly's design review is still needed" | FAO Carly with the replacement wording |
| MASTER, Claude's node | "Working on: nothing open" | Replace when the book is published |
| Project memory for this project | Says the plan for a review was settled 11 October | Update when published |

### 1.2 Process furniture in the chapters

The chapters were written by a method that left its scaffolding in the text. None of it is wrong; none of it is for the reader. Counts are from the sixteen inventories.

| What | Where | Action |
|---|---|---|
| "Before you start": re-introduces the studio, the Vibe Map, the kinds, the tiers and the flags in every chapter; Chapters 7, 9, 13, 14 and 15 add a working-words paragraph of 600 to 1,000 words | Chapters 1 to 16 | Move: Chapter 0 introduces the book once. Where a chapter's working-words paragraph coins terms the chapter needs (Chapter 9's construct/measure/descriptor set; Chapter 15's seven coinages), the coinages stay as a short list at the head of the chapter; the shared terms go to Chapter 0's glossary |
| "A note on sources" paragraph: agents, the fetch tool, thirty calls each, the verifier | Chapters 7 to 16, usually line 14 to 18 | Move to the sources section as one sentence listing what could not be read and how it is marked; the agents, rations and verifier go to the research log |
| Older tier wordings printed as current: "Fixed as a stance", "Fixed as a procedure", "Fixed as the planning assumption" | The Before-you-start legend (Chapters 5 to 15), the truths and the rules tables | Fix: the register's tier words, by editing the Tier column only. Every agent confirmed its chapter's rule wording matches the register, so no rule text changes. Exceptions to check by hand: 7.2 (register reworded it as DD-011); 14.3, 14.4, 14.11 (merged into DD-036, DD-001, DD-005); 16's ARG-12 row (chapter says "disputed; awaiting Carly", register says Fixed with status disputed) |
| The rules-table preamble that re-explains the legend and the dagger | Chapters 3, 4, 5, 8, 9 and others | Fix: "Kind and tier as in Chapter 0", plus any chapter-specific gloss (adjacent domain, the date of a legal reading) |
| "The symmetry test" section | Chapters 4 to 16 | Move to the working record. Chapter 10's section 18 carries findings a reader needs (the floor per view; "consent to be found" does not hold; the two floors separated): move the frame, keep the findings in the body |
| "Looking back" section | Every chapter | Move to the working record. Chapter 15's symmetry test and Looking back repeat each other almost line for line; one goes |
| "Gaps found" table | Every chapter | Split: rows that are knowledge gaps a reader needs (typically a third of each table) stay in the chapter as a short "What the field does not know" list; process rows (what a draft did, what a tool could not reach) move to the working record |
| "Design system and Decision Book — conflict log" | Every chapter | Move to the working record (`CONFLICTS.md`): candidates for the Decision Book and the design system, logged once |
| "Open questions and flags" | Every chapter | Split: the [Prototype flag] and [Validate with users] lines are already in `03-tests/PROBES.md` (every agent checked; two exceptions noted in the inventories); the [Further research] lines go to the working record as threads; the [Revisit → Ch n] and [Revisit at end] lines were answered by Chapter 16 and retire; the [Rich reference] lines become a "read next" line at the end of each chapter's sources, which is the one part of this section a reader wants |
| Flags in body prose | 7 to 17 per chapter, all at sentence ends | Fix: remove the bracket; every agent confirmed each sentence reads without it. Where the flag is the subject of the sentence (Chapter 10 line 478; Chapter 8 line 498), reword |
| Production words in body prose: orchestrator, verifier, research agent, "this sprint", "the fetch tool", "in the first reading's words", "the author has seen", "the first draft of this chapter" | 3 to 12 instances per chapter, listed with lines in each inventory | Fix: each is a word or a parenthesis; the sources list already carries what the parenthesis says |
| "Where the choice is yours" | Every chapter | Keep in the chapter as the teaching of the trade-offs (the brief's section 5 asks for it); each choice is also logged (1.4), and the sentences that hand the choice to a person go: "Carly's call ... has not yet been made" (Chapter 15 line 410), "the choice is Carly's" (Chapter 5 lines 289, 392, 501), "unanswered by Carly ... awaiting steer" (Chapter 16 line 335) |

### 1.3 The ten library-pass corrections, and where each lands

None has been applied. The method said an earlier chapter is not rewritten without Carly's word; this edit is that word. Each is a sentence or a cell.

| # | Source | Lands in | The fix |
|---|---|---|---|
| 1 | RSS working party 2005 | Chapter 7, rule 7.2 (line 440); register DD-011 | The report supports the interval rule, not the prohibition; the prohibition stands on the house's grounds and the *Doing Business* review. Source cell says so; dagger drops (now read at source) |
| 2 | Kaliisa et al. 2024 | Chapter 1, line 114 and rule 1.7 (line 310) | "the clearest demonstration in any field" → state the nine-of-38 split and the authors' confounding caveat; "lived up the promise" → "lived up to the promise" |
| 3 | Sjoberg, Mellon & Peixoto 2017 | Chapter 9, lines 220, 430, 458, 561, 658 | The 57 per cent is 11.6 against 18.2 per cent; reports from 154,957 people, not people; a problem fixed, not a contributor told; "cannot estimate causal effects" |
| 4 | Zhi, Ottley & Metoyer 2019 | Chapter 11, lines 32, 82, 164, 174, 224 and rule row 473 | Strike "improved recall"; keep the engagement, time and interaction findings |
| 5 | Paterno et al. 2009 | Chapter 16, line 34 (60-second version), truth 2 (line 470), rule 16.4 (line 543) | Add the caveat already at line 245: the hundred per cent was a hard stop; the free-choice evidence is 29 against 10 per cent |
| 6 | Tintarev & Masthoff 2012 | Chapter 12, rule 12.26 (line 471) | "raised satisfaction" → "may have raised satisfaction"; effectiveness half stands |
| 7 | Birt et al. 2016 | Chapter 2 (lines 371, 401, 467); Chapter 5 (line 235); Chapter 9 (lines 404, 577) | A method-and-critique paper; in the authors' own check returning to the data "proved unnecessary". The rules stand on the chapters' reading; the cells say so |
| 8 | EHRC Code 2026, Chapter 7 | Chapter 13, line 154; close flags at 350 and 931 in Chapter 10 and 478, 536, 589 in Chapter 13 | Now read at source: never mentions websites; the capitalised "The duty is anticipatory" is not the Code's sentence |
| 9 | Stevens 1946 | Chapter 12, line 182; flag at 525 | Replace "could not be read at source" with Stevens's "basic empirical operations" and "pragmatic sanction"; attribution to Velleman & Wilkinson at 36 and 182 is already right |
| 10 | The smaller eight | Chapter 3 line 226 ("these 5 studies"); Chapter 5 line 120 (Becker: negative weights); Chapter 6 lines 154 and 689 (Berg & Pattillo: journal abstract, not working paper); Chapter 7 line 440 (Mogstad: "on any measure" is wider than the source); Chapter 10 lines 504 and 728 (Glaeser: "little to say about causation"; establishment counts); Chapter 13 lines 130, 479, 529 (EN 301 549 clause 9.7); Chapter 14 (Weissgerber: already as the pass has it) | One sentence or one cell each |

**Daggers that come off without new reading**, because the ledger records a later full-text read: Chapter 1 rows 304 and 308 (Ivanković; van der Bles); Chapter 7 rows 447, 471, 661 (van der Bles; Faulkender & Yang; Lazer et al.); Chapter 15 lines 126, 614, 671 (Dong et al.); Chapter 5 row 413 (Becker). The register's status on those rules follows.

### 1.4 Open choices are scattered

- Every chapter has a "Where the choice is yours" section: roughly 130 choices across sixteen chapters, each with options and trade-offs, most saying "the studio's call" or "this book does not make it".
- Chapter 16 section 12 indexes them in nine groups; `00-plan/STATE.md` lists them again chapter by chapter with additions from the library pass and the register.
- A further set is phrased as a question to Carly in the body (see 1.2, last row) or sits in the gaps tables as "Who closes it: Carly".
- **Log:** one decision log, `00-plan/DECISIONS.md`, in the Data Brain's form: the question; what rides on it; the options; the book's steer and why; what it touches; when the build will raise it. Ordered by when the build raises them. The chapters state the steer as the book's position. Where the chapter already states a position (most do), the steer is that position; where it does not, the steer is the book's reading of its own evidence, marked [Proposal].
- Settled by this edit, and so not entries: seventeen chapters, Chapter 15 kept (the book's steer: the brief named "learn from the best"; the chapter found about forty mechanisms the others do not carry); the register's identifier scheme stays `DD-nnn`; `06-register/` stays in this repository.

### 1.5 The "60-second version" is not sixty seconds

| Chapter | Words | Answer first? |
|---|---|---|
| 1 | 441 | Yes |
| 2 | 790 | Yes |
| 3 | 710 | No: the truths arrive in the last paragraph |
| 4 | 763 | Yes |
| 5 | 722 | No: the truths arrive last |
| 6 | 1,024 | Yes |
| 7 | 961 | Yes |
| 8 | 898 | Per paragraph yes; the seven truths are the last paragraph |
| 9 | 941 | Half: the first sentence, then the truths last |
| 10 | 1,476 | No: four paragraphs of quotation, then the truths |
| 11 | 1,614 | No: the truths arrive at the end |
| 12 | 1,405 | Yes, per paragraph |
| 13 | 1,463 | Yes, per paragraph |
| 14 | 1,653 | Yes: the first paragraph is the answer |
| 15 | 1,515 | Yes, per paragraph |
| 16 | 1,095 | The verdict first; the answer assembled last |

The cold readers raised this nine times during the writing and the chapters say so. Two different things are tangled here. **The order** is a fix with one right answer in six chapters (3, 5, 8, 9, 10, 11): move the "So the canonical truths" paragraph to the top; nothing is cut. **The length** is a choice: every sentence in these sections is good and every figure in them is in the body. The steer goes in the decision log, not in this register, because it is not an error. The agents' one consistent observation: the quotation strings repeated verbatim from the body are the only material that reads as padding.

### 1.6 Chapter 16's numbers are superseded by its own postscript

- Lines 30, 38, 108, 379, 432, 482, 601 print "about two hundred" Fixed rules and "two hundred and fifty" Adaptable. The register has 280 Fixed (245 requirements, 35 sequences), 56 house defaults, 34 Adaptable, 7 Decorative. The postscript says so and the body is unchanged. **Fix** in the body; retire the postscript.
- Lines 405 to 414: the `DD-001` to `DD-010` identifiers are illustrative, not the register's (its rows for Chapter 16 are DD-351 to DD-377). **Fix:** label the column illustrative or re-key.
- Line 108 sets aside the chapter's first reading ("dashboards are a subject of right answers"); line 705 says that reading was nearer the truth. One sentence.
- Line 526, the "book's closing" item in section 12 (commits, `_to_delete/`, the reader rebuild): process. **Retire.**

### 1.7 Carly's own words, misquoted

The failure register is quoted from the brief in several chapters without its apostrophes: "if its just a fancy spreadsheet", "people dont use it", "people dont trust it", "if its an aggregation", "It fails if breaks or isnt reliable". `BRIEF-v2.md` line 19 has them right. **Fix** at: Chapter 3 line 415; Chapter 4 line 10; Chapter 8 line 430; Chapter 10 line 10; Chapter 11 line 326; Chapter 14 lines 60, 174, 352, 358, 360, 362, 364; and check Chapters 0, 1, 2, 5, 6, 7, 9, 12, 13, 15, 16 by search.

### 1.8 Stale cross-references

- "the four-line record Chapter 16 describes" (Chapter 1 line 328; Chapter 3 line 467; Chapter 4 line 580; check the rest). Chapter 16 describes a nine-line entry. **Fix.**
- Chapter 2 line 12 and others: "a kind this chapter needs and Chapter 0 will carry from its next revision". Chapter 0 now has Practice. **Fix.**
- Chapter 10 line 3: "Part 2: The central questions"; Chapter 0 names Part 2 "The felt layer". **Fix.**
- Chapter 3 line 526: "Nineteen truths" where the chapter prints seven truths and eleven record lines. **Fix.**
- Chapter 8 line 46: "four movements" lists five. **Fix.**
- Chapter 14 line 728: "a ten-line register" where the chapter says eleven everywhere else. **Fix.**

### 1.9 House style

- "night-time" hyphenated: none outside quoted titles in any chapter. **Keep.**
- "cultural contribution": none. **Keep.**
- Em dashes: 220 to 280 per chapter, used as the book's punctuation. Not changed in this edit; the style guide's "minimal" applies to new writing.
- "This matters"/"Why this matters": Chapter 14 lines 52 and 94. **Fix.**
- Americanisms: only inside quotations and titles. **Keep.**
- Typos marked "(as printed)" or "[sic]" in quoted sources (Chapter 3 line 176; Chapter 11 line 250; Chapter 15 lines 114, 282): **Keep**; they are the source's.

---

## 2 · Chapter by chapter

Each chapter's inventory (`08-edit/reads/read-chNN.md`) lists its light edits with lines. Counts here; the detail is there.

| Ch | Verdict | Light edits | Corrections (1.3) | Of note |
|---|---|---|---|---|
| 0 | Stands | The "awaiting steer" lines; the glossary's file pointers are kept and brought current | — | Already the book's one introduction; the chapters' "Before you start" duplicates it |
| 1 | Stands with light edits | 14 | 2 | "Carly's eighth failure" (line 166) arrives before the register is introduced (228) |
| 2 | Stands | 6 | 7 | Define "section 106", "What Works Centre", "BCR" |
| 3 | Stands with light edits | 12 | 10 (Yang) | Proposes a legend sub-kind Chapter 0 never adopted (line 541); log it |
| 4 | Stands with light edits | 12 | — | "published online in late 2023" v "Pierce et al. 2024": pick one |
| 5 | Stands with light edits | 16 | 7, 10 (Becker) | Garbled sentence at line 32; one name for the deprivation index |
| 6 | Stands | 5 | 10 (Berg & Pattillo) | The Decision Book "Silent on" list is printed twice (640, 784) |
| 7 | Stands with light edits | 14 | 1, 10 (Mogstad) | Looking back and the conflict log duplicate one bullet |
| 8 | Stands with light edits | 12 | — | "half the script budget" (714) v "over two-fifths" (470, 500, 522) |
| 9 | Stands with light edits | 16 | 3, 7 | Truth 3 and section 14 state the small-room position differently; one clause |
| 10 | Stands with light edits | 12 | 8, 10 (Glaeser) | Section 18 is framed as symmetry test but carries findings a reader needs |
| 11 | Stands | 4 | 4 | Truths last in a 1,614-word opening |
| 12 | Stands with light edits | 13 | 6, 9 | Line 36 says a filled radar's *area* reverses; the body (188) says the order of observations does |
| 13 | Stands | 8 | 8, 10 (EN 301 549) | Clean |
| 14 | Stands with light edits | 14 | — | Carly's words misquoted seven times; rule 14.17's tier differs from the register |
| 15 | Stands with light edits | 12 | — | The fold question appears five times; symmetry test and Looking back near-identical |
| 16 | Stands with light edits | 18 | 5 | The postscript's facts belong in the body (1.6) |

---

## 3 · The 11 October review

`08-review/PLAN.md` is the plan for a different job: reading the book to find what travels into the Vibe Map project plan. It reached step 3 of its ten (the folder and the plan) and stopped; no chapter note was written and nothing went on the map. It is not part of this edit. It stays as a parked plan, to be run from the finished book, and the state file says so.
