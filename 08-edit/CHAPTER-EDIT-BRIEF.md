# Closing a chapter of the Dashboard Design book · the writer's brief

You are finishing one chapter of a research book that its owner, Carly Heath, is happy with. Her words: "this is about closing a loop we were in, not redoing work that we've already been happy with. Don't delete good content." The chapter's teaching stands as written. Your job is a careful, line-level edit from a list that has already been made. You add nothing new: no new figures, quotes, sources, sections or arguments. You do not cut any body section for length. You do not change a rule's wording. You do not improve prose you were not asked to touch.

Working directory: `/home/claude/dd-work`. All paths below are relative to it.

## What has already been done to your chapter (by script)

A script has already removed the status line under the title and moved these sections, verbatim, to `06-register/working-record/chNN-workings.md`: "Before you start"; the symmetry test ("The studio's own ... tested" / "The symmetry test"); "Open questions and flags"; "Looking back"; "Gaps found while writing this chapter"; the "Design system ... conflict log"; and, for Chapter 16, the Postscript. It renumbered the chapter's numbered sections. `08-edit/edit-notes/chNN-MOVES.md` lists what moved and the old → new section numbers. Read it first.

## Read, in this order

1. `08-edit/edit-notes/chNN-MOVES.md` (what moved; renumbering).
2. `08-edit/reads/read-chNN.md`: the inventory of your chapter, made from a full read of the draft-2 text. Sections C (light edits) and D (furniture, open choices, corrections) are your list. Line numbers in it refer to the **draft-2 text**, which is at `archive/04-chapters-draft2/chNN-*.md`; your working file is `04-chapters/chNN-*.md` and its line numbers have shifted. Use the archive copy to find each passage, then find it in the working file by its words.
3. `08-edit/ISSUES-REGISTER.md`, sections 1.2 to 1.9: the book-wide rules for this edit.
4. `06-register/working-record/chNN-workings.md`: what moved out (so you can recover the "read next" references and the knowledge gaps).
5. `01-sources/LIBRARY-PASS.md`, the first page: the ten corrections. Apply the ones that touch your chapter (the inventory's D13 and the register's 1.3 say which).
6. `06-register/rule-register.md`: the current statement of each rule's tier. Find your chapter's rows (the `chapters` column lists them as chapter.row).
7. `00-plan/BRIEF-v2.md` line 19: the failure register in Carly's words, for the apostrophes.
8. Your chapter, in full, before you change anything.

## The edits, in order

1. **Part label.** Line 3 keeps its italic part label. Chapter 10's says "Part 2: The central questions"; make it "Part 2: The felt layer" (Chapter 0 names the parts). Leave the others.
2. **In-text section numbers.** Where sections were renumbered, update every "section N", "Section N", "§N", "sections N and M" and "(section N)" in the chapter to the new number, including in the Sources section's group headings. Where the text points at the moved symmetry section (e.g. "section 14 tests the studio's own positions"), reword to what the chapter now does or drop the pointer; the working record has the content. Do not change references to other chapters' section numbers.
3. **Corrections from the library pass.** Apply each one that lands in your chapter, exactly as the register's section 1.3 and the inventory's D13 describe: a sentence or a cell, no more. Drop the daggers the register lists as stale for your chapter. Never change a quotation except where the pass found the chapter misquoted the source (Chapter 1's "lived up the promise").
4. **Light edits from the inventory's section C.** Apply each one that is a fix with one right answer (a term defined at first use, a figure made consistent, a stale cross-reference, a garbled sentence, a production word, a misplaced parenthesis). Do **not** apply items the inventory marks as a choice, a question for Carly, or "optional": list those in your notes instead. Do not trim the 60-second version or any section for length.
5. **The 60-second version, order only.** In Chapters 3, 5, 8, 9, 10 and 11 the inventory found the canonical truths arrive in the last paragraph. Move that paragraph (the one beginning "So the canonical truths" or equivalent) to directly after the first paragraph, keeping every word. No other chapter's 60-second version changes.
6. **Tier words.** In the rules table, and in "What holds true regardless", replace the older tier wordings ("Fixed as a stance", "Fixed as a procedure", "Fixed as the planning assumption", "(stance)", "(procedure)") with the register's wording for that rule: *Fixed (requirement)*, *Fixed (sequence)*, *Adaptable (house default)*, *Adaptable*, *Decorative*. Edit the Tier cell only; the Rule, Why and Source cells do not change. Where the register merged or reworded a rule (the inventory's D12 says), leave the chapter's row as it is and list it in your notes. Where a truth carries a tier in its italic grounds, use the register's word for the rule that carries that truth, or "Fixed (statement of the record)" where Chapter 0 says a truth is a statement of the record.
7. **The rules-table preamble.** Replace any re-explanation of the legend (what Fixed means, what † means, what Practice is) with "*Kind and tier as in Chapter 0.*" plus any chapter-specific sentence worth keeping (the date a law was read; what "adjacent domain" means in this chapter).
8. **Flags in body prose.** Remove every `[Further research]`, `[Prototype flag]`, `[Validate with users]`, `[Revisit → Ch n]`, `[Revisit at end]`, `[Rich reference]` and `[Counterbalance → X]` bracket that remains in the body, the truths, the choices, the illustration, the rules or the sources. Keep the sentence. Where the bracket is the subject of the sentence (the inventory says where), reword minimally so the sentence stands. Before removing a `[Prototype flag]` or `[Validate with users]`, check the test it names is in `03-tests/PROBES.md`; if it is not, list it in your notes.
9. **Production words.** Remove or replace, per the inventory's D10: orchestrator, verifier, research agent, "the agent's", "this sprint", "the fetch tool", "in the first reading's words", "the first draft of this chapter", "the author has seen", "on the verification list", "before this version closes", "corrected in draft 2". Where a parenthesis says how a source was read, the Sources list already carries it: delete the parenthesis. Where a sentence says what the chapter could not read, keep the fact ("the full text could not be reached") and drop the tool.
10. **The note on sources.** Where the chapter had "A note on this chapter's sources" (now moved out with "Before you start"), write one sentence at the top of the Sources section, in italics, saying which founding texts could not be read and how unread or partly read sources are marked. Nothing about agents, rations or verifiers.
11. **Words this chapter uses.** If the moved "Before you start" carried a working-words paragraph with terms the chapter coined and relies on (the inventory's section B or D2 says), add a short section "## Words this chapter uses" immediately before "## Sources", as a bullet list of those coinages only, in the chapter's own words from that paragraph. Terms shared across the book (the dashboard, a reader, a scene, the failure register, the kinds and tiers, the records) are Chapter 0's and are not repeated. List in your notes any shared term the chapter used that Chapter 0 lacks.
12. **Read next.** From the moved "Open questions and flags", take the `[Rich reference]` entries and add them as a final short paragraph of the Sources section headed in bold **Read next.**, keeping their descriptions. Nothing else from that section returns.
13. **What the field does not know.** From the moved "Gaps found" table, the inventory's D8 says which rows are knowledge gaps a reader needs. Add them back as a short bullet list under "## What the field does not know", placed after "What proves a break works" and before "Checklist", one line each in the row's own words (the gap and the interim position). Process rows stay in the working record. If the inventory found no knowledge rows, add no section.
14. **"Where the choice is yours."** The section stays. Remove any sentence that hands a choice to a person or says it is unmade ("Carly's call ... has not yet been made", "the choice is Carly's", "awaiting steer", "unanswered by Carly"); where the chapter uses "the studio's" elsewhere, use that. List every choice in this section in your notes as a one-line question with the chapter's stated position, if it states one (the inventory's D3 already has this; check it against the text).
15. **Carly's words.** Restore the apostrophes in every quotation of the failure register to the brief's wording: "it's", "don't", "isn't", "it fails if it breaks or isn't reliable". Search the whole chapter for "dont", "isnt", "its just", "its an aggregation", "if breaks".
16. **Stale machinery references.** "the four-line record Chapter 16 describes" and variants → "the deviation entry Chapter 16 describes". "Chapter 0 will carry from its next revision" and variants → Chapter 0 now carries it; reword or drop. Any sentence saying a later chapter "will" do something that Chapter 16 has done: present tense or drop.
17. **Chapter 16 only.** Write the postscript's three facts into the body where the old numbers sit (the register's section 1.6): 280 Fixed rules (245 requirements, 35 sequences), 56 house defaults, 34 Adaptable, 7 Decorative; the illustrative identifiers labelled as illustrative; the Paterno caveat in the 60-second version, truth 2 and rule 16.4. Remove line 6's notice that a postscript exists and the closing italic about Carly. Remove the "book's closing" housekeeping item from section 12.

## What you never do

- Change a rule's wording, a quotation (except the one misquotation named), a figure, a source, or a section's argument.
- Cut a paragraph because it is long or repeats a point. Repetition between the 60-second version, the truths, the rules and the checklist is the book's design.
- Add a sentence of your own beyond what an edit above needs.
- Write "Carly decides", "review needed", "awaiting", "TBD", "not yet decided" anywhere.
- Use "night-time" with a hyphen, "cultural contribution", or add an em dash.
- Touch any file other than your chapter and your notes file.

## Your notes file: `08-edit/edit-notes/chNN-NOTES.md`

Short, in this order:
1. **Changes made**, one line each: what and where (quote four or five words so the verifier can find it). Group as: corrections; light edits; tier words; flags; production words; order; added sections (words, read next, what the field does not know); Carly's words; stale references.
2. **Not applied**, one line each, with the reason (a choice, not a fix; the inventory marked it optional; the register reworded the rule).
3. **For the decision log**: every choice from "Where the choice is yours" and any other open choice the chapter states, as "Question · the chapter's position (or: none stated) · the lines".
4. **For Chapter 0**: shared terms your chapter uses that Chapter 0's glossary lacks.
5. **For the probes file**: any `[Prototype flag]` or `[Validate with users]` test not already in `03-tests/PROBES.md`.
6. **Section cross-references updated**: the count, and any you could not resolve.

When you finish, reply with the "Changes made" counts by group and the "Not applied" list, nothing else.
