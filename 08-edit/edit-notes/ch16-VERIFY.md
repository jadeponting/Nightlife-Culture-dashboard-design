# Chapter 16 · verification, 14 October 2026

Draft 2: `archive/04-chapters-draft2/ch16-breaking-these-rules-well.md` (711 lines). Edited: `04-chapters/ch16-breaking-these-rules-well.md` (601 lines). Line numbers below are the edited file's unless marked (d2).

Chapter 16's subject is the tiers and flags: "Fixed as a stance", "Fixed as a procedure" and flag names used as objects of its counting (lines 83, 85, 87, 91, 93, 258, 273, 294, 318, 320, 324, 348, 465, 503) are not failures and are not listed under check 8.

## 1 · Diff — PASS

Word-level diff run after neutralising the `## N ·` renumbering. Every hunk is one of: a script move (status line; postscript notice; Before you start; symmetry test; Open questions; Looking back; Gaps; conflict log; closing italic; Postscript), a change listed in NOTES.md, or a brief edit (2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17). No unexplained change.

Two notes, not failures:
- Line 360 drops "provisionally `DD-nnn`, since the house's prefix scheme is the house's" (register 1.4: settled), but line 485 in section 11 still lists "the identifier scheme of the register, provisionally `DD-nnn`" as an open choice. The writer left 485 deliberately (NOTES, Not applied). The chapter now says both. One of the two should go; the decision log is the place to retire the item.
- Line 93 (section 3, "What the count means") rewrites the last two sentences from the postscript's facts rather than transplanting the postscript's words: "prohibitions a build can check" for the postscript's "prohibitions that a build can scan, recompute or check by date"; the old close "the shape the evidence says is read" becomes "whether 280 is short enough to be read is what truth 2 tests in the build's first year", which is the postscript's own position. Figures identical; argument as the postscript states it. Edit 17 required integration, so this is accepted here.

## 2 · Nothing new — FAIL (one item)

- Line 573, "Words this chapter uses", fourth bullet: "The *compilation* is the working file (`02-research-notes/ch16-assembly.md`) that gathered the chapters' rules, records, tests, flags, gaps and conflict rows by script, re-checked against their source lines; its counts are the chapter's evidence about the book." This sentence is not in draft 2. Its facts come from the moved "A note on sources" (workings line 13), not from the working-words paragraph the brief names, and the words are recomposed. The writer disclosed it (NOTES, Added sections). Options: accept as the one defined use of a term the chapter uses 29 times; or replace with the note's own words, "its compilation is kept as a working file beside this chapter and its counts are the chapter's evidence about itself".

Everything else added is verbatim from its source: the other seven bullets match workings line 11 word for word (bullet 8 drops "and is tested in section 10", the moved section, per edit 2); "Read next" (line 599) matches workings line 54; the eleven "What the field does not know" bullets (539–549) match gaps rows 653–655, 657–662, 666–667 (d2) in the rows' words, with §11 → section 10 for the renumbering; the Sources note (583) is stitched from workings line 13 with the agents and verifier removed; the postscript's figures (280; 245/35; 56; 34; 7; 74 per cent; 377; 51 of the 90; "Chapter 16 §8 row n") appear at lines 23, 93, 364, 386, 417, 445 as the postscript states them. "ninety Adaptable rules" (417) is 56 + 34, not printed in the postscript as 90. No new quotation or source.

## 3 · Nothing cut — PASS

Question; 60-second version (five paragraphs); sections 1–12; the rules (27 rows); What proves a break works; What the field does not know (new); Checklist; Words this chapter uses (new); Sources with Read next. No paragraph removed or shortened beyond the brief's named words: the postscript notice (d2 6); "the agent's" (105); "(D1)…(D37)" (252); `[Validate with users]` (210); `[Prototype flag]` (318); "and unanswered by Carly … once more and in the log as awaiting steer" (320); "provisionally … the house's" (360); "; unanswered" (473); "The book's closing" item (d2 526); "Agent returns" (d2 635); `[Further research]` ×3 in the truths.

## 4 · Rules unchanged — PASS

27 rows compared cell by cell. Rule, Why, Kind and Source cells identical to draft 2 except: 16.4 Why gains the Paterno parenthesis (register 1.3, correction 5); 16.10 Rule "section 11" → "section 10" and Source "§11" → "§10" (renumbering, edit 2; disclosed in NOTES as the one rule-wording change); 16.23 Source "§12" → "§11" and 16.27 Source "§12" → "§11" (renumbering). Tier cells: 16.23 "— (disputed; awaiting Carly)" → "**Fixed** (requirement) · disputed" (register 1.2's named exception). Spot check against `06-register/rule-register.md`: 16.1 Fixed (sequence) = DD-351; 16.4 Fixed (requirement) = DD-354; 16.21 Adaptable (house default) = DD-371; 16.23 Fixed (requirement), status disputed = DD-373; 16.26 Adaptable = DD-376. Note: 16.27 reads "Adaptable (house default: publish)" where DD-377 reads "Adaptable (house default)"; the ": publish" gloss is draft 2's and was not touched.

## 5 · Quotations — PASS

All 422 double-quoted spans of 25+ characters in the edited chapter were matched against draft 2. Every one is character-identical except the brief-required changes: the five failure-register sentences with apostrophes restored (35, 411, 417, 419, 421, 423) and "the deviation entry Chapter 16 describes" (312, edit 16). Ten read by hand (Small et al.; RFC 2119 §6; FRC 2021 "74 cases"; Ancker "30%"; GDS "without having carried out an assessment"; MISRA "convenience of the developer"; Lakens; Santana Junior "opened directly"; Paterno "29% vs. 10%"; Russ "two-thirds"): identical.

## 6 · Corrections applied — PASS

Correction 5 (Paterno 2009) applied at the register's three places: 60-second version para 3 (line 19), truth 2 (433), rule 16.4 Why (504), each as a clause added and nothing else in the passage changed. No stale dagger named for this chapter; none dropped. Note: the inventory's D13 also listed the belief at d2 line 56 (now line 41, "Where the severe rules are set apart from the rest, the severe ones are obeyed"), which the register did not name and the writer left; it points to section 6, which carries the caveat.

## 7 · Section references — PASS

All in-text references checked (grep for section/Section/§ + number): every one points at a section that exists under the new numbering and says what is claimed. "section 10" ×7 and "§10" ×1 point at What holds true regardless, where the entry is stated once; "section 11" ×18 and "§11" ×2 point at Where the choice is yours; no "section 12" remains; "§6" at 431 and 504 is RFC 2119's own section. Pre-existing, not the edit's: truth 4 (437) says "the eight records of section 5" where section 5 (176) says "Seven records of decisions were read" (the same in draft 2).

## 8 · No furniture left — FAIL (two items, both disclosed in NOTES as not applied)

- Line 523, rule 16.23: "ARG-12 is carried as *disputed*, with Chapter 12's rule beside it, until Carly decides". A wait on Carly inside a rule's wording. The brief forbids changing rule wording and the register's DD-373 carries the same words, so the fix is a register change (DD-373 and the chapter row together), not this edit's.
- Lines 362 and 378, section 8: the register's *Status* values "current; superseded by; disputed; awaiting Carly" and the register report's "disputed, awaiting Carly or full-text-not-read". The register file does use "awaiting Carly" as a status (DD-373 and four other rows), so the chapter describes the file accurately; it is still a wait on Carly printed in the teaching text. Renaming the status in the register (e.g. "the studio's") and regenerating would clear both lines.

All other hits are the chapter's subject (tier wordings and flag names as objects), a quotation of Chapter 0's rule (258), "the Decision Book's four-line record" as a description of the house's log (572), or "draft" meaning a draft of a document (282, 342, 577). No `dont`/`isnt`/`its just`/`its an aggregation`, "night-time", "cultural contribution", orchestrator, verifier, research agent, sprint, fetch tool.

## 9 · Workings file — PASS

All seven moved sections (Before you start, 9 lines; The symmetry test, 19; Open questions and flags, 14; Looking back, 20; Gaps found, 21; conflict log, 25; Postscript, 11) and the closing italic are present in `06-register/working-record/ch16-workings.md` word for word against the archive.

## 10 · Notes honesty — PASS

Every change NOTES.md lists was found at the place described (corrections; edit 17's nine items; C7, C9, C10, C11, C12, C18; truths' tier words; three flags removed and the kept mentions; "the agent's" and "Agent returns"; the four added sections; seven apostrophe fixes; the Chapter 0 tense changes; eleven hands-to-a-person rewordings; 28 section references, counted 7 + 18 + 1 + 2). Everything NOTES says was not applied was not: the fourteen "the compilation" parentheses (13 remain plus the Sources status list); belief 1; the status vocabulary; rule 16.23; "provisionally `DD-nnn`" at 485; "Chapter 0 gives the skill file's four" at 172; the postscript's fourth fact. Probes 74 and 75 exist in `03-tests/PROBES.md` as stated.

## Outside this chapter, for the owner

- `03-tests/PROBES.md` probe 75 still says "the Fixed register's estimated two hundred".
- Register rows DD-360 ("section 11"; "§11"), DD-373 ("§12") and DD-377 ("§12") carry the old section numbers (NOTES says so); DD-373's wording and the "awaiting Carly" status are the two check-8 items above.
