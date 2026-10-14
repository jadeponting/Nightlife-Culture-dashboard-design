# Read: Chapter 8 — Automation without admin

## A. Coverage

- File: `/mnt/user-data/uploads/GitHub/dashboard-design/04-chapters/ch08-automation-without-admin.md`
- `wc -l`: 898 lines (the Read tool reports 899 with a trailing blank).
- Ranges read with the Read tool: 1–272, 273–472, 473–692, 693–899. Every line was read; nothing was summarised from headings.
- Context read: BRIEF-v2 §1, §4, §5; Chapter 0 "How a chapter teaches" and "The legend"; LIBRARY-PASS first page; register rows DD-173 to DD-196 and DD-007, DD-040, DD-045; PROBES.md rows citing Ch 8.

## B. What the chapter teaches

The chapter answers what it takes for a dashboard to stay alive without someone tending it daily, and its answer is that "no admin" is a sentence with a person in it: automate the refresh, bake the data before the reader arrives, keep the last good copy when a fetch fails, watch the data's date rather than the job, and route the ticket to a role. It is written for whoever will build and run the Vibe Map's page: a creative technologist or analyst meeting operations for the first time. A newcomer takes away four things: freshness is three dates and a frequency, not a stamp; every interface is someone else's promise with terms, and the open licence promises reuse, not supply; a scheduled job fails silently by default; the phone sets the byte budget and a map spends it faster than anything else. Beneath all of it sits the ten-line service record (lines 524–543), which is the chapter's own contribution.

Best passages, which must survive any edit:

- Lines 144–146 (the Open Government Licence read last line first; "The UK's open data is open the way a tap is open: the water that has run is yours, and the tap may be turned off").
- Lines 264–270 (availability as a chain; the arithmetic of ten sources at 99.9 per cent; "Move the calls to the night before, keep the result, and the reader's page depends on one thing").
- Lines 304–310 (cron and the free scheduler fail quietly; the heartbeat inversion: "the job's silence, which cron and the free scheduler both treat as success, becomes the signal").
- Lines 236–252 (the platform terms forbid, clause by clause, the five things a dashboard does: stores, derives, combines, calls on a schedule, is commercial).
- Lines 476–480 (the map's twin: "A dashboard whose map has no twin has made its most expensive element its only one").

Passages a newcomer could not follow:

- Line 12: the glossary paragraph defines seven terms in one block before any of them is needed. A newcomer will not retain "SLO", "bus factor", "page (pager)" from here; each is also defined where it first appears (lines 284, 294, 380), so the block is redundant for the reader and exists for the cold reader's benefit.
- Line 46: "The rest of the chapter is in four movements" and then lists five (sections 3–4, 5–6, 7–8, 9–10, 11). Minor, but a newcomer counting along will stumble.
- Line 190: "the chapter's inference, not the publisher's sentence" is clear, but "snap point" is introduced at line 190 without having been named in line 188, which describes the method without the word.
- Line 498: "it is a `[Prototype flag]` and a Chapter 10 question" uses the flag as a noun inside the sentence; a reader who does not know the legend cannot parse it.
- Line 541: the filled example uses "BSC", "OGL", "gz", "`data@`" and "MAUs" (line 211) without gloss in that paragraph. BSC is defined at 462 and OGL at 144, so this is a density problem rather than a definition gap.

## C. Verdict on the chapter body

**Stands with light edits.** The teaching sections do their job as written: the question (line 20) is one question; the beliefs (lines 52–82) are each answered in a sentence with a pointer; sections 3–10 are evidence in the body, concrete and dated; section 12's seven truths (510–522) each carry grounds; the illustration (567–593) is method only; the rules, break test and checklist agree with the body. No section contradicts another; the argument runs in one direction. The edits below are a term, a figure or a sentence each, and none changes a rule.

Light edits (12):

1. Line 46: "four movements" lists five. Change to five, or drop section 11 from the list.
2. Line 62: "Section 5 and 6." → "Sections 5 and 6." Same at line 74 ("Section 7 and 8") and line 488 ("Section 7 and 8 support").
3. Line 36: the closing paragraph of the 60-second version is the answer in seven clauses; see the note below on moving it to the top.
4. Line 420: double space in "found —  arrived".
5. Line 430: "people dont use it" — if this is the failure register's verbatim spelling, mark it; if not, apostrophe.
6. Line 498: "it is a `[Prototype flag]` and a Chapter 10 question" → "it is a question for the prototype and for Chapter 10" with the flag moved to the end of the sentence or removed (the same flag is in Open questions at 690).
7. Line 714: "costs half the script budget before a tile" against the body's "over two-fifths" / "about 43 per cent" (lines 470, 500, 522). Make it "over two-fifths".
8. Line 12: the seven-term glossary. Either cut to the three "terms of the trade" the chapter says it will use throughout (API, rate limit, tile) and let the other four be defined where they first appear (which they already are), or move the block to a reference section. This is the one edit that is also a furniture question.
9. Line 174: "the statistics office's 120 in ten seconds would allow 720 a minute if its 200 a minute did not also apply" is correct arithmetic but the parenthesis runs 40 words; split.
10. Line 190: name the "snap point" at line 188 where the master list is first described, so line 190's "a dot on a snap point" has a referent.
11. Line 599 (rules-table preamble): "Secondary marks a quotation…" repeats Chapter 0's legend, which Chapter 0 says the table should not repeat. Keep only the sentence about the 6 October 2026 date and the "adjacent domain" gloss.
12. Line 541: the filled example reads as a block of abbreviations. One sentence before it saying "the abbreviations are those of sections 6 and 10" would do, or expand BSC and OGL on first use in that paragraph.

The 60-second version: lines 26–36, **898 words**. It is a four-minute read. It does give answers first within each paragraph (the bold lead sentences at 28, 30, 32, 34 are the answers), but the chapter's actual answer in one breath, the seven truths, is the last paragraph (36). Moving line 36 to directly after line 26, and holding the four evidence paragraphs as they are, gives the answer first without cutting any content. If trimming is wanted, the candidates are the quoted strings in 28 and 30 that are repeated verbatim in the body (the DCAT "MAY indicate" sentence appears at 28 and 112; the OGL sentence at 30, 144 and 160; the GitHub "automatically disabled" clause at 32 and 306). I do not recommend cutting the body for length.

## D. Furniture and status: exact inventory

1. **Status lines under the title.** Line 3: "*Dashboard Design · Part 1: The analytical foundation*" (keep: it is the part label). Line 4: "*Version 2, draft 2 · 6 October 2026 · research log, Entry 8*" — status; retire or move.

2. **"Before you start"** (lines 8–14). Line 10 is the re-introduction repeated from Chapter 0 (who the book is for, the definition, the Vibe Map, "Where this chapter refers to Carly…"). Line 12 is the legend repeated plus a seven-term glossary. Line 14 is "A note on this chapter's sources" — pure process (research agents had no web search; twelve sources spot-checked; a verifier re-traced four hundred strings on 125 pages). Line 14 belongs at the head of Sources (line 730 already says most of it); line 10 and the legend half of line 12 go to the reference section; the glossary half of line 12 is edit 8 above. The one sentence in 14 that is content, not process, is the last: "every limit, price and quota in this chapter is given as read on 6 October 2026… That drift is recorded in section 8 as evidence." Keep that in the body (section 6's opening at 152 already says it).

3. **"Where the choice is yours"** (lines 547–563). Seven open choices:
   - Live or baked, panel by panel? Current position (551): "The chapter's architecture is nightly"; a live element is allowed if it "accepts the chain arithmetic of section 7, with its own dependency line in the record".
   - Vector or raster map? Position (553): none taken; "a creative decision and this book does not make it. It does require that the twin exist either way."
   - Which of the four tile supplies? Position (555): none; "The record states which was chosen and what was agreed to."
   - Which availability objective, and how large an error budget? Position (557): "'Eleven months in twelve' is the chapter's example"; set it "no higher than readers can tell".
   - What notice does the studio give when it retires a series? Position (559): none fixed; "the chapter's only requirement is that it be written in line 8 before the first series needs it."
   - Whether to call the platform interfaces at all? Position (561): "The decision is the prototype's and Chapter 10's".
   - Who reads the ticket? Position (563): "A role, the chapter says; but which role, with what second, at what hours, is an organisational choice."

4. **Other places the chapter asks for a decision or leaves one open** (searched: Carly, steer, decide, awaits, "not yet", "has not", open, TBD):
   - Line 10: "Where this chapter refers to Carly, it means the studio's founder" (furniture only; Carly is not otherwise addressed in the chapter).
   - Line 194: "whether a dashboard should use any of them is a question for the prototype and for Chapter 10, and this chapter does not answer it."
   - Line 214: "The chapter records that and nothing more about whether to proceed."
   - Line 248: "Whether a studio's free public page is 'commercial' under any of these is a legal reading this chapter cannot give; it is a question for line 2 of the service record".
   - Line 256: "the question this section most carefully did not answer — whether the studio's prototype should call any of the platform interfaces… is the prototype's `[Prototype flag]` and Chapter 10's".
   - Line 306: "whether the job's own nightly commits count as 'repository activity' is not stated on the page, and a studio should find out rather than assume."
   - Line 364: "whether any availability commitment attaches to these free tiers at all… the chapter does not say either way."
   - Line 498: "A choice, now with its evidence attached."
   - Line 526: "whether these five are one document is a question for the end of the book `[Revisit at end]`".
   - Line 543: "some of them will say 'not yet'" (about the prototype's record, not the chapter).
   - Line 720: "Chapter 0's legend should admit or rename" the use of "Standard" for platform terms.
   - Line 724: "These are design decisions and are logged, not made."
   - Line 884: "Logged as a conflict, not resolved."
   No sentence awaits Carly's steer by name; the open items are all addressed to the prototype, Chapter 10 or the Decision Book.

5. **"The symmetry test" section.** There is no heading of that name. Section 11, "The studio's own positions, tested" (lines 484–502), is the symmetry test by line 12's definition and line 486's own words ("Chapter 0 calls this the symmetry test"). Eight positions tested, each ending in a verdict in italics (Qualified; Strengthened, with two conditions; Strengthened and extended; Strengthened, made concrete; Counterbalanced; A choice; Qualified; Qualified). This is teaching content for a reader of the studio's position, not process; it stays, but the heading could carry the name Chapter 0 gives it.

6. **"Open questions and flags"** (lines 683–704). Counts: `[Further research]` 5; `[Prototype flag]` 4 (plus one nested inside a Further research item at 689); `[Validate with users]` 3 (one nested at 687); `[Revisit at end]` 1; `[Revisit → Ch 10]` 1; `[Revisit → Ch 9]` 1; `[Rich reference]` 7; `[Counterbalance]` 0 here (three in Looking back).
   Prototype flags and user validations, one line each:
   - 689: measure what a map view costs the baseline phone in bytes (PROBES 31, P-088/P-092).
   - 690: whether to call the platform interfaces at all, decided with the terms open (not a probe; a decision for Ch 10).
   - 691: break the job on launch day and look at the degraded page (PROBES 33, P-094).
   - 692: show the watch catches the sixty-day disabling (PROBES 33, P-095).
   - 687: do readers read "data to [date]" and what do they do when it is old (PROBES 30, P-091).
   - 693: single date against the four-part freshness statement (PROBES 30, P-096).
   - 694: vector or raster as experienced on the slowest phones (PROBES 32, P-097).
   All but 690 are already in PROBES.md; 690 is a decision, not a probe.

7. **"Looking back"** (lines 708–724). Thirteen bullets against Chapters 1–7, version 1, Chapter 0, Chapters 9 and 10, the Decision Book and the design system. The Decision Book and design system bullets (723–724) duplicate the conflict log at 894–898 almost word for word. Process furniture; move to the reference section, keeping one line in the body if anything: the inconsistency flagged at 714 (edit 7).

8. **"Gaps found"** table (lines 872–892): 19 rows. Real knowledge gaps a reader needs (keep in text, or in a reader-facing gaps section): 878 (Eventbrite removal and OS allowances unverified); 881 (the "60–80 per cent maintenance" figure has no open primary source); 882 (no measured evidence that stale dashboards cost trust; no UK staleness study; no bytes-per-view for a map); 883 (no design system reached shows last refresh); 884 (DSH-21 conflict); 885 (Decision Book has no running rules); 886 (design system has no map, freshness or degraded-tile component); 892 (five records across Chapters 4–8). Process notes (move to the working record): 874 (fetch reader truncation); 875 (reader invented sentences on first pass); 876 (a quarter of brief URLs drifted — already used as evidence at 378, so the table row is redundant); 877 (three expected quotations absent); 879 (OGL redirect loop); 880 (URL guessing); 887 (clause numbers wavered); 888 (invented publication years); 889 (verifier recomputed the arithmetic); 890 (verifier's corrections); 891 (cold reader's term findings). The table's Cost column uses the older coloured scheme Chapter 0 says is now internal.

9. **"Design system and Decision Book — conflict log"** (lines 894–898): two paragraphs, "Agrees" and "Conflicts", not the table-with-status Chapter 0 now specifies. Candidates for the Decision Book and design system (move to a working record): the two "Logged for" lists at the end of 898 (freshness component; degraded-tile state; map component with twin, buttons, attribution, logo slots; byte budget and baseline device; script-free rendering; a Decision Book chapter on running a dashboard). Facts the reader needs (keep in the chapter, and already there at 500–502 and 723): the DSH-21 conflict, that the degraded state is Fixed and only its look is Decorative; and that a styled vector face costs over two-fifths of the script budget.

10. **Production words in body prose** (lines 18–682). Count: about 14, all in the author's voice about how the research went rather than about dashboards. Examples:
    - 196: "one publishes it in a form this book's tools could not read"
    - 200: "as far as the fetch tool's reader could see"
    - 202: "which the research expected to confirm, is recorded as unverified"
    - 216: "The clause numbers are those the fetch tool's reader returned, and the research agent noted that sub-letter labels wavered between passes"
    - 218: "The research brief expected the long-standing rule… The agent's observation, marked as its own"
    - 228: "the company's own forum post is closed to this book's tools"
    - 256: "Three things the research expected could not be confirmed at source"
    - 378: "By the research agents' own count, roughly a quarter of the URLs and phrasings in their brief were no longer as expected"
    - 422: "has softened since the research brief was written — testing… is now something a service 'should' do, where the brief remembered a 'must'"
    - 440: "read as probable rather than confirmed because the verifying pass agreed too readily"
    - 448: "rewritten since the research brief was framed"
    - 474: "The research looked for a measurement… and found none"
    No "orchestrator" (one, at 730 in Sources), no "sprint", "ledger", "SOURCES.md", "STATE.md" or "[Proposal]" in the body. Most of these are evidence-discipline sentences ("read once", "unverified") that the brief's own voice asks for; 216, 218, 378 and 422 are the ones that read as the research reporting on itself and could be reduced to "on a single reading" / "as read on 6 October 2026" without loss. The 378 paragraph is a special case: it is first-hand evidence for the chapter's claim about drift and should stay, with "research agents" becoming "this book's research".

11. **Flags inside the body prose** (outside Open questions): `[Rich reference]` 1 (line 90); `[Further research]` 2 (256, 474); `[Prototype flag]` 4 (256, 474, 498, 613 in the rules table); `[Revisit at end]` 1 (526). Removing the brackets leaves 90, 256, 474, 526 and 613 readable as sentences. Line 498 does not survive removal ("it is a and a Chapter 10 question") and needs edit 6.

12. **Rules table** (lines 603–636): 34 rows. Tier words used: **Fixed** (10 plain); **Fixed** as a procedure (9, plus one "Fixed as a procedure; Adaptable in period"); **Fixed** as a stance (7, plus "stance; Adaptable for a declared live element", "stance; Adaptable in figure", "stance; Adaptable in value"); mixed "Fixed (period); Fixed as a stance (four parts)" (1); Adaptable (2); "Adaptable (which interfaces signal); Fixed (that the job reads them)" (1). No Decorative. One row cites a dagger source: line 635 (owner is a role; Avelino et al. 2016 †). The register carries all 34 as DD-007, DD-040, DD-045 and DD-173 to DD-196 with re-based tiers: for example row 603 (service record) and row 610 (beta treated as changeable) become Adaptable (house default), row 614 (fetch at build time) Adaptable (house default), rows 605, 608, 616, 620 become Fixed (requirement), row 617 Fixed (sequence). The rule wording in the register matches the table's wording cell for cell on every row I checked (603, 605, 608, 610–613, 614–617, 618–620, 622, 624–625, 629–630, 632, 635–636). The table could therefore take the register's tier column without touching the rule or why cells.

13. **Library-pass corrections.** None of the ten touches Chapter 8. The dagger-removal list and the two PubMed walls do not name any Chapter 8 source. The chapter's one dagger (Avelino et al.) is not in the pass's reports as far as the first page shows.

14. **Nightlife illustration** (lines 567–593). Heading reads "A nightlife illustration — method only" (567); line 569: "it draws no conclusions about any place, names no venue and proposes no design"; line 593: "Nothing in it says what the district is like, and nothing in it is a design". Data is hypothetical throughout ("Suppose a studio proposes a page about a district", 571); the only real figures are the interface limits already quoted in section 6 (200 a minute, four a minute, sixty days). Correctly labelled; no invented place data presented as real.

## E. House style

- "night-time" hyphenated: 0. "cultural contribution": 0.
- Em dashes used as punctuation: 388 (heavy; the book's habit, noted only).
- "robust": 1, at 835 inside a quoted GOV.UK title ("Building a robust frontend"). "deliver": 1, at 426 inside an Ofcom quotation ("to deliver good geographic coverage"). "leverage", "unlock", "empower", "tackle", "this matters", "at the heart of": 0.
- Americanisms: all inside quotations and correctly left as written — "licensed" (OGL text, 144), "favor" (SRE, 312), "analyze" (Spotify, 216), "center" (data.police.uk, 188), "canceled" (Nygard, 376), "organizations" (Spotify, 211). The chapter's own prose uses "licence", "colour", "programme". "Depreciated" at 180 is the FSA page's spelling and is marked as such. Nothing to change.

## F. Repetition

The "keep the last good copy and show its age" rule appears at 32 (60-second version), 278 (workbook quote), 330–334 (protocol), 344 (AWS anti-pattern), 384 (what section 8 settles), 490 (symmetry test), 516 (truth 4), 615 (rules row), 659 (checklist), 581 (illustration line 5) and 642 (break test): eleven statements. The "ticket goes to a role, not a person" rule appears nine times (306, 316, 384, 488, 512, 518, 533, 620, 663). This is the chapter's teaching structure working as designed: each appearance is in a different register (answer, evidence, standard, truth, rule, test) and the wording changes with the register. The one place it reads as padding is the pair at 723–724 against 894–898, which say the same things about the Decision Book and the design system twice within 175 lines; one copy should go (item 7 and 9 above). The verbatim repetition of long quotations between the 60-second version and the body (noted in C) is the other candidate, and is a matter for the 60-second version alone.

## G. One line for Carly

This chapter does not need rewriting: its argument, evidence and rules already teach as a book, and what it needs is a dozen one-line fixes, the research-process paragraphs (the title status, the source note at line 14, the Looking back and Gaps tables' process rows) moved to a reference section, and the seven-truth closing paragraph of the 60-second version lifted to the top so the answer comes first.
