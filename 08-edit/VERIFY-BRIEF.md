# Verifying a closed chapter · the verifier's brief

You did not write this chapter and have not seen the writer's reasoning. Your job is to check that the edit did exactly what the brief allowed and nothing else. You are the second pair of eyes the owner, Carly, relies on; she will not re-read 485,000 words. Be exact and be short.

Working directory: `/home/claude/dd-work`.

## Read
1. `08-edit/CHAPTER-EDIT-BRIEF.md`: what the writer was allowed to do.
2. `08-edit/edit-notes/chNN-MOVES.md` and `08-edit/edit-notes/chNN-NOTES.md`: what the script moved and what the writer says it changed.
3. `08-edit/reads/read-chNN.md`: the inventory the writer worked from.
4. The draft-2 text at `archive/04-chapters-draft2/chNN-*.md` and the edited text at `04-chapters/chNN-*.md`.
5. `06-register/working-record/chNN-workings.md`.

## Check, and report each as PASS or FAIL with the line

1. **Diff.** Run `diff` between the archive and the edited chapter (`diff <(sed 's/^## [0-9]* · /## N · /' archive) <(same for edited)` helps ignore renumbering). Every differing line must be explained by one of: the script's moves (MOVES.md); a change listed in NOTES.md; or an edit the brief requires. List any change not explained.
2. **Nothing new.** No sentence, figure, quotation or source exists in the edited chapter that was not in draft 2, except the brief's permitted additions (the one-sentence sources note; "Words this chapter uses" built from the moved paragraph; "Read next" built from the moved rich references; "What the field does not know" built from the moved gaps table; the Chapter 16 postscript facts). Check each addition against its source in the workings file: same words.
3. **Nothing cut.** Every numbered section, the 60-second version, the truths, the illustration, the rules, the break test, the checklist and the sources are present and no paragraph has been removed or shortened, except the parentheses and words the brief names (production words, flags, the rules-table preamble, the sentences handing a choice to Carly).
4. **Rules unchanged.** Compare every row of the rules table: Rule, Why and Source cells identical to draft 2 (allowing the dagger drops and source-cell corrections the register's 1.3 names for this chapter). Tier cells use only the register's wordings. Spot-check five Tier cells against `06-register/rule-register.md`.
5. **Quotations.** Pick ten quotations across the chapter and confirm each is character-identical to draft 2.
6. **Corrections applied.** For each library-pass correction that lands in this chapter (register 1.3), confirm it is applied as described, and that nothing beyond it changed in that passage.
7. **Section references.** Grep the edited chapter for `section \d+`, `Section \d+`, `§\d+`, `sections \d+`. Each must point at a section that exists under the new numbering and says what the reference claims. List any that do not.
8. **No furniture left.** Grep for: `draft`, `Carly decides`, `awaiting`, `review needed`, `orchestrator`, `verifier`, `research agent`, `the agent`, `sprint`, `fetch tool`, `verification list`, `before this version`, `four-line record`, `\[Further research\]`, `\[Prototype flag\]`, `\[Validate with users\]`, `\[Revisit`, `\[Rich reference\]`, `\[Counterbalance`, `Fixed as a stance`, `Fixed as a procedure`, `(stance)`, `(procedure)`, `dont`, `isnt`, `its just`, `its an aggregation`, `night-time`, `cultural contribution`. Report every hit that is not inside a quotation from a source or a title.
9. **Workings file.** Every moved section is present in full, word for word (compare against the archive).
10. **Notes honesty.** Everything NOTES.md says was changed, was; everything it says was not applied, was not.

## Output
Write `08-edit/edit-notes/chNN-VERIFY.md`: the ten checks, PASS/FAIL, and for each FAIL the exact line and what is wrong. Then reply with only the FAIL list (or "All ten pass").
