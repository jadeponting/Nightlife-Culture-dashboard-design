# Reading brief: one chapter of the Dashboard Design book

You are reading one chapter of a research book, in full, to judge it. You are not rewriting it and you must not propose a rewrite unless the evidence forces it. The owner's steer is: "this is about closing a loop we were in, not redoing work we've already been happy with. Don't delete good content." Your job is to tell her, with line evidence, whether the chapter already does its job as a book for a newcomer, and exactly what in it is process furniture, status, or open-choice text that belongs in a reference section rather than in the chapter.

## Read first (briefly), for context only
- `/mnt/user-data/uploads/GitHub/dashboard-design/00-plan/BRIEF-v2.md` sections 1, 4 and 5 (what the book is for; how a chapter teaches).
- `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch00-how-to-read-this-book.md`, the sections "How a chapter teaches" and "The legend" (so you know what the furniture is called).
- `/mnt/user-data/uploads/GitHub/dashboard-design/01-sources/LIBRARY-PASS.md`, the first page only ("What the pass found, in one page"): ten proposed corrections. Note which touch your chapter.

## Then read your chapter, every line
Use `wc -l` first and record the count. Read the whole file with the Read tool in ranges until you have reached the last line. Do not skim. Do not summarise from headings. If your context fills, say so in the output rather than pretending.

## Write ONE file: `<output path given to you>`
Use British English. Plain words. No praise, no padding. Where you quote, quote exactly with the line number. Structure:

### A. Coverage
- File, total lines, the ranges you read, and a one-line confirmation that every line was read.

### B. What the chapter teaches (as a reader, not the author)
- In 3 to 5 sentences: what the chapter decides, for whom, and what a newcomer would take away.
- Name the two or three best passages (line ranges) that teach well: concrete, rhythmic, a clear point of view. These are the lines that must survive any edit.
- Name any passage a newcomer could not follow, with the line and why (undefined term, assumes another chapter, production jargon).

### C. Verdict on the chapter body
Choose ONE, with reasons tied to lines:
- **Stands**: the teaching sections (question, 60-second version, what it is, beliefs and evidence, numbered sections, what holds true, nightlife illustration, rules, break test, checklist, sources) teach as they are. Only furniture needs moving.
- **Stands with light edits**: as above, plus a short list of specific fixes (a term, a figure, a sentence) with lines. Fewer than ~20 edits.
- **Needs structural work**: say precisely why, with lines. This verdict needs strong evidence (e.g. the argument contradicts itself, the 60-second version does not give the answer, large sections repeat).
Also give: the word count of the 60-second version (lines), and whether it gives the answer first or needs trimming to do so. Do NOT recommend cutting body sections for length alone.

### D. Furniture and status: exact inventory with lines
For each, the line range(s) and what is there. These are candidates to MOVE to a reference section or RETIRE, not to delete silently:
1. Status/draft line(s) under the title (e.g. "Draft 2 · …", "for Carly's steer", "awaiting steer", "revised after a cold read").
2. "Before you start" section (re-introduction repeated from Chapter 0).
3. "Where the choice is yours" section: list EVERY open choice in it as a one-line question, and quote the chapter's current position if it states one (this feeds a decision log; be complete).
4. Any other place the chapter asks Carly to decide, awaits steer, or says "the house has not chosen": line and quote. Search for: Carly, steer, decide, awaits, "not yet", "has not", "open", TBD.
5. "The symmetry test" section.
6. "Open questions and flags" section: count flags by type ([Further research], [Prototype flag], [Validate with users], [Revisit → Ch n], [Revisit at end], [Rich reference], [Counterbalance → X]); list each [Prototype flag] and [Validate with users] line in one line each (these feed the probes file; many are already in PROBES.md, note that).
7. "Looking back" section.
8. "Gaps found" table: row count; which rows are real knowledge gaps a reader needs to know (keep in text) versus process notes (move).
9. "Design system and Decision Book conflict log": row/paragraph count; which items are candidates for the Decision Book/design system (move to a working record) versus facts the chapter's reader needs.
10. Production words in the body prose (not in sections above): orchestrator, verifier, cold reader, agent, sprint, "this sprint", "our reading", research log, ledger, SOURCES.md, STATE.md, [Proposal], dagger explanation. Count and give up to 10 example lines.
11. Flags inside the body prose (outside the Open questions section): count by type, and whether removing the bracket would leave the sentence readable.
12. Rules table: row count; tier words used (Fixed / Fixed as a stance / Fixed as a procedure / Adaptable / Decorative / other); any row whose source cell cites a † / abstract-only source. Note: the register (`06-register/rule-register.md`) is the current statement of tier; the chapter prints the older wording. Say whether the table could be updated to the register's tiers without changing the rule wording.
13. The ten library-pass corrections: which touch this chapter, at which line, and what the one-sentence fix would be (do not apply it).
14. Nightlife illustration section: is it labelled "method only" / "illustration, not a specification"? Does it use invented or real place data? Lines.

### E. House style
- Count of "night-time" (hyphenated) outside quoted titles; "cultural contribution"; em dashes (—) used as punctuation (give a count; the book uses them heavily, note only the count); "robust", "leverage", "unlock", "empower", "deliver", "tackle", "this matters", "at the heart of". Lines for anything other than em dashes.
- Any Americanisms.

### F. Repetition
- Where the same point is made more than twice across sections (e.g. a rule stated in the 60-second version, the body, the truths, the rules table and the checklist). Give one example with lines. Say whether this is the chapter's teaching structure working as designed (acceptable) or padding.

### G. One line for Carly
- One plain sentence: does this chapter need rewriting, or does it need its furniture moved and its status retired? No jargon.

Rules: do not edit any file except your output. Do not invent figures. If you cannot read a part, say which lines.
