# Dashboard Design: closing the book

*Agreed with Carly, 14 October 2026, and done the same day. The record of how draft 2 became the finished book.*

## What was asked, and what changed

Carly asked for the dashboard book to be brought to the state the Data Brain reached: a book a person can read, a reference section behind it, published, with no status line anywhere still calling it a draft. Then she corrected the frame: the dashboard book was in much better shape than the Data Brain had been; the chapters were good; the job was closing a loop, not redoing work; nothing good was to be deleted. So the Data Brain's six stages were run with one change: stage 1 read every chapter to judge it, not to rewrite it, and the pilot and the rewrites were replaced by a line-level edit that left the teaching text as it stood.

## The stages, as run

1. **Read everything.** Sixteen agents read a chapter each in full to one brief (`08-edit/READ-BRIEF.md`); Claude read Chapters 0, 1 and 9. Output: `08-edit/READ-LOG.md`, `08-edit/ISSUES-REGISTER.md`, and sixteen inventories in `08-edit/reads/`. Verdict: every chapter stands; most want a dozen word-level fixes.
2. **Move the furniture out.** A script (`08-edit/move_workings.py`) moved each chapter's status line and its process sections (Before you start; the symmetry test; Open questions and flags; Looking back; Gaps found; the conflict log; Chapter 16's postscript) verbatim to `06-register/working-record/chNN-workings.md`, and renumbered the sections. Carly chose moving over folding: "this is likely Claude's reference to itself; it doesn't improve readability".
3. **Edit each chapter.** A writer per chapter to `08-edit/CHAPTER-EDIT-BRIEF.md`: the library-pass corrections; the inventory's light edits; tier words to the register's; flags and production words out; the truths paragraph moved first in six 60-second versions; "Read next", "Words this chapter uses" and "What this chapter could not settle" built from the moved sections' own words; Carly's words restored; stale pointers fixed. Nothing added, nothing cut for length, no rule reworded. Notes in `08-edit/edit-notes/chNN-NOTES.md`.
4. **Verify, read cold, verify again.** An independent verifier per chapter (`08-edit/VERIFY-BRIEF.md`) diffed the edit against draft 2 and checked every change was allowed; a newcomer reader per chapter (`08-edit/NEWCOMER-BRIEF.md`) read it with no context. The fixes that followed are in `08-edit/edit-notes/second-verification-fixes.md`, `merged-rows-tier-fix.md` and `tool-phrasing-sweep.md`. The newcomer reads found what the Data Brain's pilot had found: once "Before you start" moved out, the chapters' shared words had no introduction. The remedy was the same: a fixed "Reading this chapter" paragraph at the top of every chapter, and a fuller glossary in Chapter 0.
5. **Build the reference section.** The decision log, `00-plan/DECISIONS.md` (91 entries, each with the book's steer and the moment the build raises it, built from the chapters' "Where the choice is yours" sections, Chapter 16's index and the 7 October open list); the working record; the register's status value "awaiting Carly" retired to "open in the decision log"; Chapter 0 rewritten to introduce the finished book.
6. **Check the whole book, rebuild, retire, publish.** A whole-book check (`08-edit/WHOLE-BOOK-CHECK.md`) for terms with two meanings, cross-references, counts, furniture, voice and section order, and the fixes it led to. The reader rebuilt with the chapter rail and appendices A to D. Every status line retired: the state file, the README, the agent instructions, Chapter 0, the reader masthead, the Knowledge Base entry, the map and the project memory. Then published.

## What stays the same

- The research, the 377 rules and their tiers, the sources, the evidence. The edit changed presentation, not evidence; the one exception is the ten corrections the library pass had already found.
- The chapters' length and shape. The 60-second versions keep their text and their name (decision log, DB-90).
- Nothing is committed by an agent.
