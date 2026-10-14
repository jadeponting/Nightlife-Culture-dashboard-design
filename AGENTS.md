# Working on the Dashboard Design research book

*The working method for any session or agent in this repository. Carly Heath set it on 5 October 2026. `CLAUDE.md` points here.*

## What this repository is

A research book on how dashboards work and why — the methodological and theoretical foundation for deciding how evidence becomes a display that a reader trusts, reads and acts on. It is the third of Nightlife Culture's foundations, beside the Decision Book (how to choose) and the design system (what the values are). It serves the Vibe Map prototype but is not an assessment, specification or design of it. `00-plan/BRIEF-v2.md` governs: the mission in Carly's words, the six questions, what the book never does, the chapter map.

Carly Heath is the author of the mission and the final reader. She holds the sector knowledge; the book never researches it. She reviews and commits; agents never commit.

## How we research — the explorer's rules

1. **Reach the edges before moving on.** A chapter is finished when the research has run out of threads worth pulling, not when a word count or a prompt is satisfied. No arbitrary word limit; if a finding needs the room, give it the room. Edit later.
2. **Research is not ringfenced by the prompt.** When something turns up that we did not know to look for, pull the thread. If it reveals a new question, a new section, a new chapter or a different way of thinking about the topic, say so and record it. The chapter map is a plan, not a cage.
3. **Each chapter is a standalone addition to the canonical understanding.** It is not validated by the chapter before it. It argues from its own sources.
4. **Look backward at the end of every chapter.** Against each earlier chapter, record whether this chapter's findings *strengthen*, *weaken*, *counterbalance* or *open a thread* for it. Nothing earlier is rewritten on the spot; the log carries the note and a flag.
5. **Leave breathing space.** Where the evidence runs out, say so and leave a marked question to return to — at the end of the book, in a probe, in a conversation with users, or in the prototype itself.
6. **Quote the line or mark it as our reading.** Any claim relayed by a research agent is read at the source before it is written into a chapter. Every source carries how it was read and on what date.
7. **Tell Carly about the rich ones.** Not every URL; the handful of references worth her own time or worth returning to when building.
8. **One record, appended, never overwritten.** The research log grows; it is never versioned into copies.

## The flags

Used in the log, the ledger and the working record, always in square brackets so they can be searched. The finished chapters no longer carry them (see below):

| Flag | Means |
|---|---|
| `[Further research]` | A thread worth pulling that this chapter did not have room or evidence to finish |
| `[Prototype flag]` | Something the Vibe Map can settle with evidence that no literature can |
| `[Validate with users]` | Something to test in conversation with the three user groups or the scenes |
| `[Revisit → Ch n]` | A question that belongs to a later chapter and is handed to it |
| `[Revisit at end]` | A question to return to once all chapters exist, because its answer depends on them (Chapter 16 answered these) |
| `[Rich reference]` | A source Carly should read in her own time or return to when building |
| `[Counterbalance → X]` | This finding pulls against an earlier chapter's, or against the design system, the Decision Book or version 1; recorded, not resolved |

## The roles, and how the work is split for performance

**The orchestrator** (the session Carly is talking to) frames each chapter's questions from the brief, dispatches research, reads what comes back, verifies the load-bearing claims at source itself, writes the chapter in the studio's voice, writes the log entry, does the backward look, and shows Carly the result.

**Research agents** run in parallel, two to four per chapter, each with one facet — typically: the field's own literature; cross-sector practice (public health, finance, culture, charity, government); the critical and ethical scholarship; the statistics and methods. Every agent is briefed to fetch at source, return exact quotations with URLs and the date fetched, state each finding's strength, follow unexpected threads, report what it found that it was not asked for, list what it judged less important and why, and name any reference it thinks is rich.

**A verification agent**, never the one that found a claim, re-traces every load-bearing quotation and figure in a draft chapter before it is called done, and reports mismatches.

**A cold-reader agent** reads the finished chapter with no project context and must say what the chapter decided, name one hard line and one open choice, say where the headline evidence is, and raise its strongest objection. A chapter that fails this is rewritten before it is shown.

**Carly** reads what is shown, when she chooses; she is not a gate between chapters. Her steer, when it comes, is logged and applied.

## How a chapter sprint runs

1. Frame: the chapter's question, its sub-questions from the brief, and the first reading list — written into the log *before* research starts, so the log shows what we expected against what we found.
2. Dispatch research agents in parallel. Pull threads they open; dispatch again if a thread deserves it.
3. Verify load-bearing claims at source.
4. Write the chapter to the teaching template in `BRIEF-v2.md` section 5, in the studio's voice, with the legend from Chapter 0.
5. Append the log entry: sources, learned, left out, threads, open questions, backward look, flags, rich references.
6. Ledger entries for every source.
7. Cold-reader test; verification pass; fix.
8. Deliver the chapter and the log to Carly as files; place them in the repo. Update `STATE.md`. Continue to the next chapter without waiting, unless Carly says otherwise.

## Where things go

| | |
|---|---|
| `00-plan/BRIEF-v2.md` | Governs. The mission, the questions, the map |
| `00-plan/STATE.md` | The handover. Read first in any new session |
| `00-plan/DECISIONS.md` | The decision log: every open choice, with the book's steer and when the build raises it |
| `00-plan/EDIT-PLAN.md` | What the closing edit of 14 October 2026 agreed and did |
| `01-sources/SOURCES.md` | The ledger — every source, how read, verified when |
| `01-sources/RESEARCH-LOG.md` | The journey — one appended record of what was looked for, found, learned, left out and flagged, chapter by chapter |
| `01-sources/LIBRARY-PASS.md` | What was found when abstract-only sources were read in full; the ten corrections, applied on 14 October 2026 |
| `02-research-notes/` | Working notes and agent returns worth keeping |
| `03-tests/` | Probe candidates (`PROBES.md`) and protocols, as they accumulate |
| `04-chapters/` | The seventeen chapters, finished 14 October 2026 |
| `05-book/` | The reader, regenerated after any chapter edit |
| `06-register/` | The reference section: the rule register and the deviation log (generated from the Chapter 16 compilation by `build_register.py`; `work/` holds the classification files), and `working-record/`, how each chapter was made |
| `07-checks/` | Reserved for the build-time checks Chapter 16 §8 specifies; empty |
| `08-edit/` | The record of the closing edit: read log, issues register, briefs, chapter inventories and edit notes |
| `08-review/` | A parked plan (11 October 2026) for reading the finished book to find what travels into the Vibe Map project plan |
| `archive/` | Superseded material still cited somewhere, with a README |
| `_to_delete/` | What Claude believes can go; Carly decides |

## Now that the book is finished

*Added 7 October 2026 when the seventeenth chapter was done; rewritten 14 October 2026 when the book was finished. The method above is how the book was made; this is how to work with it now.*

The book is finished and published. An agent arriving now is a reader first: start from `00-plan/STATE.md`, which says what exists and what to know before relying on it. Four things follow from the rules above and are easy to miss.

- **Rule 4 holds, with one change.** A finding that bears on a chapter is logged in the research log and the chapter changes on Carly's word. The flags no longer live in the chapters: the sections that carried them (the symmetry test, Looking back, Gaps found, the conflict log, Open questions and flags) are in `06-register/working-record/`, one file per chapter, word for word; the probe candidates are `03-tests/PROBES.md`; the open choices are `00-plan/DECISIONS.md`.
- **Open choices carry a steer, never a gate.** Every open choice is in the decision log with the book's steer and the moment the build will raise it. Nothing in the chapters waits on anyone. A chapter never says "Carly decides", "review needed" or "awaiting".
- **The register is generated, not edited.** `06-register/rule-register.csv` comes from the compilation and the classification files in `06-register/work/`; change a chapter or a classification row and regenerate. The register is the current statement of each rule's tier and the chapters' tables follow it. The register queries at the end of the decision log say where the chapter and the register disagree.
- **Finishing includes retiring the status everywhere it is stated.** A change to a chapter is followed by the reader's rebuild and the republished artifact; a change to what the book is for is reflected in this file, the README, the state file and the Knowledge Base. New work gets a research-log entry, Entry 19 onwards, and its sources go in the ledger with how each was read.

## What never happens here

- Researching nightlife, the night time economy's data, or how government works from the inside — that is Carly's knowledge and enters as the frame.
- Answering the prototyping questions. Method is the book's; findings about actual places are the prototype's.
- Making the creative decisions. The club-flyer question belongs to Carly and her designers.
- Reproducing confidential material (the Vibe Setting Framework; the 2026 data).
- Writing anywhere other than this repository; committing; deleting. Superseded files go to `archive/` or `_to_delete/`.
- Bold-bracket status marks, "the instrument", AI voice, or explaining the sector to itself.
