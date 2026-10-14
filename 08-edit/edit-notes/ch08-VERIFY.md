# Chapter 8 · verification, 14 October 2026

Checked against `08-edit/VERIFY-BRIEF.md`. Archive: `archive/04-chapters-draft2/ch08-automation-without-admin.md` (898 lines). Edited: `04-chapters/ch08-automation-without-admin.md` (811 lines). Also read: `08-edit/edit-notes/merged-rows-tier-fix.md`, whose ch08 lines (590, 594) explain two Tier cells the NOTES file says were left as printed.

**Result: all ten pass.** Two notes for the record, neither a failure, at the end.

## 1 · Diff — PASS

328-line diff, every hunk accounted for:

- Script moves (MOVES.md): status line (archive line 4); "Before you start" (8–14); "11 · The studio's own positions, tested" (484–505); "Open questions and flags" (683–704); "Looking back" (706–724); "Gaps found" (866–892); conflict log (894–898).
- NOTES.md: section 1 movements sentence; Beliefs three, four, six plurals; section 3 "which section 11 will turn on the studio" clause; snap-point naming (line 177); double space (409); "people don't use it" (419); nineteen Tier cells; preamble (566); flags at 79, 245, 463, 493, rule 8.11 Source; production words at 185, 189, 205, 207, 217, 367, 411, 429, 437, Sources preamble, Spotify and Web Almanac entries; 60-second order; "Words this chapter uses"; Sources note; "Read next"; "What the field does not know"; "House positions" heading; seven section-number updates (241, 359, 445, 475, 570, 580, heading 803); "Chapter 16 gathers these five" (493).
- merged-rows-tier-fix.md: rules 8.21 (line 590) and 8.25 (line 594) Tier cells → `Fixed (requirement)`.

No unexplained line.

## 2 · Nothing new — PASS

Quotation census: 788 in-line quoted strings in the archive, 713 in the edited text. The only string present in the edited text and absent from draft 2 is "people don't use it" (brief edit 15). Every string absent from the edited text is in the workings file, except "people dont use it" (corrected) and "Secondary" (preamble sentence the brief drops).

Permitted additions, checked against the workings file:
- "Words this chapter uses" (664–667): four bullets; tile/panel, heartbeat, page, KB/KiB. Words are the moved paragraph's (line 9 of the workings), recast from "a *tile* (one square …)" to "A *tile* is one square …"; nothing added.
- Sources note (673): names RFC 9110 `Retry-After`/conditional requests, DWBP BP21/22/27/28, DCAT 3 frequency — all three from the workings' "The unreached" bullet and Gaps row 92. No agents, rations or verifiers.
- "Read next" (809): character-identical to the seven `[Rich reference]` entries joined (checked by script).
- "What the field does not know" (617–623): seven bullets from Gaps rows 96, 99–104 (old 878, 881–886). Row 100's "flagged each for the prototype or users" → "each is a test for the prototype or for users" (the brief retires "flagged"); row 102's "makes the degraded state a Fixed procedure" → "holds that the degraded state is Fixed and only its look Decorative" — the second clause is the conflict log's own words (workings line 117), the first retires an old tier wording. No new fact.
- Line 493 "Chapter 16 gathers these five, with the records of later chapters, into one record of the dashboard": brief edit 16; the phrase is Chapter 0's glossary entry (ch00 line 168) and Chapter 16 section 7 (ch16 lines 298, 449).

## 3 · Nothing cut — PASS

Heading diff: the only headings gone are the six moved sections; the only headings new are the two the brief adds. Sections 1–10 and 11–13 (renumbered), the 60-second version (five paragraphs, reordered, every word), seven truths, service record table and filled example, "Where the choice is yours" (seven choices), the illustration (ten lines), 34 rules, break test, checklist (30 items), Sources (all seven groups plus House positions) all present. Removed words: one movements sentence and one clause pointing at the moved section 11; flags; "the fetch tool's reader" / "research agent" / "orchestrator" / "verifying pass" phrases; two preamble sentences; "(one agent sentence corrected)". All named by the brief.

## 4 · Rules unchanged — PASS

34 rows compared cell by cell. Rule, Why and Kind cells identical on every row. Source cells identical except 8.1 (§12 → §11), 8.11 (§13 → §12; `[Prototype flag]` dropped) — both brief-required. Dagger on 8.33 (Avelino et al. 2016 †) retained; register 1.3 names no ch08 correction and no ch08 dagger drop.

Tier cells use only: Fixed, Fixed (requirement), Fixed (sequence), Adaptable, Adaptable (house default), with the chapter's own open-part qualifiers unchanged. Spot-checks against `06-register/rule-register.md`:
- 8.1 `Fixed (sequence); what each line says: Adaptable` = DD-173.
- 8.2 `Fixed (requirement) (period); Adaptable (house default) (four parts)` = DD-007.
- 8.15 `Fixed (sequence); the schedule of later exercises: Adaptable` = DD-184.
- 8.32 `Fixed (sequence); period and content: Adaptable` = DD-026.
- 8.33 `Adaptable (house default)` = DD-196.
- Also 8.12 = DD-181, 8.24 = DD-040, 8.34 = DD-045, 8.21 → DD-007 Fixed (requirement), 8.25 → DD-001 Fixed (requirement).

## 5 · Quotations — PASS

Exhaustive (see check 2): every quoted string identical. Ten named: RFC 9111 "A 'fresh' response is one whose age has not yet exceeded its freshness lifetime" (33); OGL "The Information Provider does not guarantee the continued supply of the Information" (133); Ticketmaster "not primarily in response to direct user actions" (189); Spotify III.13 "creating new or derived listenership metrics, benchmarking, functionality, usage statistics, user metrics" (205); Facebook "Starting today, apps using the API will no longer be able to access the guest list or posts on the event wall" (215); Treynor "A service cannot be more available than the intersection of all its critical dependencies" (255); GitHub "automatically disabled when no repository activity has occurred in 60 days" (295); SRE "Stale data is almost always better than incorrect data" (267); Russell "15-25% as fast as those carried by programmers and their bosses" (397); OSMF "Our tile servers are not: they are funded by donations and sponsorship, and capacity is limited" (437).

## 6 · Corrections applied — PASS

Register 1.3: none of the ten lands in Chapter 8; no dagger listed for it. Nothing to apply; nothing applied.

## 7 · Section references — PASS

All in-text `section N`/`Section N`/`§N` resolved. Chapter-internal pointers: 241, 359, 445 (service record → section 11, which holds "Beneath the dashboard: the service record"); 475 (nightlife case → 13); 570 (§11); 580 (§6, §12 — section 12 holds "Whether to call the platforms at all"); 617 (script-only shells as evidence → section 9, line 411); Sources group headings 1/3, 4–10 match their sections. Remaining §-numbers (RFC 9111 §4.2, §5.2.1, §4.2.4; Google Maps §1.3(c), §3.2.3; Code of Practice §10.7; DCAT 3 §5.1, §6.4, §6.7, §11, §12; RFC 9110 §8.8.3, §10.2.3, §13) are the sources' own. Belief pointers (43–71) all correct. No pointer to the moved section remains.

## 8 · No furniture left — PASS

Hits: "Internet-Draft" (129, 163, 713 — a document class and an IETF identifier); "drafted now" (540, ordinary verb in the illustration); "marked as draft" (683, the W3C First Public Working Draft's status). No other term on the list appears. "night-time", "cultural contribution": none.

## 9 · Workings file — PASS

All six moved sections compared line by line with the archive (blank lines and rules ignored): "Before you start" 4/4, section 11 10/10, "Open questions and flags" 21/21, "Looking back" 15/15, "Gaps found" 23/23, conflict log 3/3 — identical.

## 10 · Notes honesty — PASS

Every change in NOTES §1 is in the diff; every count (nineteen Tier cells, seven cross-references, two dropped pointers, four words bullets, seven Read-next entries, seven gap bullets) matches. §2 "not applied" items C9, C12, C6/C7, plain-Fixed rows, 8.9, row 892, "Where the choice is yours" all verified unchanged. §5 probe mapping checked against the inventory's D6. One statement is now stale, below.

## Notes (not failures)

1. **NOTES §2 lines 82–83 are superseded.** They say rules 8.21 and 8.25 were "Left as printed" with "Fixed as a stance". `merged-rows-tier-fix.md` has since set both to `Fixed (requirement)` (DD-007, DD-001). The two lines in ch08-NOTES.md should be removed or replaced with a pointer to the merged-rows note, so the notes show the final state.
2. **Bold formatting on lines 590 and 594** is `**Fixed (requirement)**`; every other requirement row in the table is `**Fixed** (requirement)`. Words are the register's; the markup differs. Cosmetic.
3. NOTES line 86 is right: register DD-180's Source cell still reads "This chapter §6, §13; `[Prototype flag]`" and will follow the chapter on regeneration.
