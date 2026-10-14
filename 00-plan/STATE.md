# Dashboard Design — state

*The handover. Read first in any new session. Updated 14 October 2026. **The book is finished and published. There is no outstanding work on it.** It changes only when the build changes a steer in the decision log, or Carly asks for an edit.*

## Where the book stands

- **The book.** Chapters 0 to 16 in `04-chapters/`. Written 5 to 7 October 2026 as draft 2 and finished on 14 October 2026 by a closing edit that left the teaching text as it was: every chapter was read in full and judged to stand; its process sections were moved to the working record; its status lines were retired; the ten library-pass corrections were applied; its tier words were brought to the register's; and the open choices scattered through it were gathered into one decision log. Each chapter went through a writer, an independent verifier, a newcomer reader and a second verification; the whole book was then checked for consistency and voice.
- **The reader.** `05-book/reader.html`, published as the artifact "Dashboard Design" (https://claude.ai/artifact/BME2Ec3A3MfBTddFEraSe7): the seventeen chapters, then the reference section as appendices A (the rule register), B (the decision log), C (the deviation log) and D (the probe candidates). Left-hand chapter rail, search, links from every chapter reference and every `DB-nn` and `DD-nnn` identifier to its entry.
- **The reference section.** Explained in `06-register/README.md`. The decision log, `00-plan/DECISIONS.md`, is the only place an open choice lives: 91 entries, DB-01 to DB-91, each with the book's steer and the moment the build will raise it. The rule register holds all 377 rules and is the current statement of each rule's tier. The deviation log holds the nine-line entry and its one proposed entry. The working record, `06-register/working-record/`, holds how each chapter was made, one file per chapter, word for word. The probe candidates are `03-tests/PROBES.md`.
- **The record of the edit.** `00-plan/EDIT-PLAN.md` (what was agreed and done), `08-edit/READ-LOG.md`, `08-edit/ISSUES-REGISTER.md`, the sixteen chapter inventories in `08-edit/reads/`, the briefs the writers, verifiers and newcomer readers worked to, and `08-edit/edit-notes/` (what each chapter's edit changed, what its verifier found, what its newcomer could not follow, and the fixes made after). Draft 2 of every chapter is in `archive/04-chapters-draft2/`.
- **The research.** `01-sources/SOURCES.md` (the ledger), `01-sources/RESEARCH-LOG.md`, `01-sources/LIBRARY-PASS.md`, `02-research-notes/`. Unchanged by the edit, except that the library pass's ten corrections are now applied in the chapters.

## What to know before relying on it

- Every open choice has the book's steer, in the decision log and in the chapter it touches. Open entries are not outstanding work: when the build raises a question, look at the steer, use it or change it, and move on. When Carly changes one, the entry is marked decided, the chapter text it touches is edited once, and the reader is rebuilt and republished.
- The register is the current statement of each rule's tier; the chapters' tables follow it. Seven places where the register's grouping looks wrong are listed at the end of the decision log as register queries, with what the register should say if the chapter is right.
- Chapter 16's counts of the chapters' tier wordings are of the chapters at second draft, as the chapter now says; they are the audit that produced the register.
- Every claim says how its source was read: at source, spot-checked or verified; a dagger for a source read at the authors' abstract or summary only; "secondary" for a quotation reached through a named reproduction; "(read once)" for a quotation not re-checked. Twenty-one sources remain open on the web but unread, behind pages the research could not open; `01-sources/LIBRARY-PASS.md` lists them.
- Law is reported with its wording and date, never advised on: data protection as it stood on 6 October 2026 (Chapter 10); the Equality Act and the accessibility regulations (Chapter 13).
- Nothing has been tested with people or with the prototype's data. The seventy-five probe candidates are candidates; none has been run. The nightlife illustrations show method and decide nothing about any place.
- Confidential material (the Vibe Setting Framework; the 2026 data) is cited, never reproduced.

## Open, and whose

- Nothing. The decision log holds a steer for every open question; each is answered when the build raises it. Carly commits; no agent commits.
- A separate job, parked: reading the finished book to find what travels into the Vibe Map project plan. Its plan is `08-review/PLAN.md` (11 October 2026); it resumes from the finished book, not from draft 2.

## Regenerating

From the repository root, after any chapter edit:

    python3 05-book/build_reader.py --assets "<nightlife-culture-design skill>/assets" --kick "Nightlife Culture · Dashboard Design · finished 14 October 2026"
    python3 06-register/build_register.py parse    # only if a rules table changed
    python3 06-register/build_register.py build

The reader needs the Python packages `markdown` and `beautifulsoup4`. The builder reads `04-chapters/`, `06-register/rule-register.md`, `00-plan/DECISIONS.md`, `06-register/deviation-log.md` and `03-tests/PROBES.md`.
