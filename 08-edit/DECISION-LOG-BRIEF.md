# Building the decision log · the brief

You are writing `00-plan/DECISIONS.md` for the Dashboard Design book: the one place an open choice lives. The book is finished; its chapters state positions and leave trade-offs open for the build. This log gathers every open choice the book carries, gives each the book's steer and names the moment the build will raise it. It is a reference for the people who build the Vibe Map, not a to-do list for anyone.

Working directory: `/home/claude/dd-work`.

## The model to copy, exactly

`/mnt/user-data/uploads/GitHub/vibe-map-data-brain/00-plan/DECISIONS.md` is the Data Brain's log. Read its header, its "How it works", its at-a-glance table and three or four of its entries (D-01, D-02, D-30, D-76) in full. Copy its form: the header note; the at-a-glance table (ID · The question · The book's steer · Comes up when); then grouped entries, each with **Question**, **What rides on it**, **Options**, **Steer**, **Touches**, **Status**; then "Not in this log, and why". Identifiers here are `DB-01`, `DB-02` ... (DB for Dashboard book), so they never collide with the Data Brain's D-nn or the register's DD-nnn.

Words the log never uses: "blocks", "needs Carly", "Carly decides", "review needed", "none set", "TBD", "awaiting". Every entry has a steer. Where the chapter states a position, the steer is that position, in the chapter's words where possible. Where the chapter states none, the steer is the book's reading of its own evidence and is marked [Proposal]. Nothing in the log waits on anyone: "Comes up when" names the moment in the build (the first screen is designed; the first composite is computed; the first felt panel is built; the first table with a withheld cell is published).

## Sources, in this order

1. `08-edit/edit-notes/chNN-NOTES.md`, section 3 ("For the decision log") in all sixteen files. These were written by the chapter writers from the chapters' "Where the choice is yours" sections and body choices, each with the chapter's position where stated. This is your main input.
2. `04-chapters/ch16-breaking-these-rules-well.md`, section 11 ("Where the choice is yours"): the book's own index of open choices in nine groups. Every item there must be in the log or in "Not in this log".
3. `00-plan/STATE.md`, "What is open, and whose it is": the 7 October list. Anything there not already covered goes in, unless it is settled by the edit (see below).
4. The chapters themselves (`04-chapters/`) to confirm a position's wording where a note is unclear. Do not read whole chapters; grep for the choice.
5. `03-tests/PROBES.md`, so that a choice the probes already test can say so in "Comes up when".

## Merging

Many choices recur across chapters (the floor and the small room appears in Chapters 1, 4, 6, 9, 10, 12; the 60-second version's length in every chapter; the identifier scheme; whether the records are one document; the Decision Book candidates). Merge each into one entry whose "Touches" lists every chapter and rule. Aim for a log of about 60 to 90 entries, not 150.

## Settled by the edit, and so listed under "Not in this log, and why"

- Seventeen chapters; Chapter 15 kept (the chapter found about forty mechanisms the others do not carry).
- The register's identifier scheme stays `DD-nnn`.
- `06-register/` stays in this repository.
- The ten library-pass corrections are applied; the stale daggers are off.
- The tier wordings in the chapters follow the register.
- Moving the process sections to the working record; retiring the status lines; the reader rebuild.
- Anything that was a step of the edit rather than a choice about the dashboard.

Register queries found during the edit go in a short final table "Register queries", not as decisions: DD-037 groups the validity-claim rule (5.15, 9.32) under cognitive testing; DD-030 groups the outlier rule (1.13) as Fixed (sequence) where Chapter 1 argues Adaptable; DD-001 groups 2.10 (the plain-table route as a hypothesis) under the table twin as Fixed (requirement); DD-004/11.4 superseded by 14.14. Each with one line on what the register should say if the chapter is right.

## The 60-second versions

One entry, DB for the length of the "60-second version" sections: they run 440 to 1,650 words; the cold readers raised it nine times during the writing; six were reordered so the truths come first. Steer [Proposal]: keep the text and the name; the reader shows each chapter's question and 60-second version open, so the reader meets them first; cut only if a reader test shows the length loses readers. Comes up when: the first reader test of the book itself.

## Writing

British English, plain words, no jargon the chapter does not define. Keep each Question to one line, each Steer to one to three sentences. Date every Status "Open · 14 Oct 2026". Quote the chapter's position where you can; mark anything the chapters did not say [Proposal].

## Output

Write `00-plan/DECISIONS.md`. Then reply with: the number of entries; the number marked [Proposal]; the five entries you were least sure how to steer, with the chapter and rule each touches.
