# Research Plan v0.3 — the interactive evidence instrument
### Researching the methodology for displaying nightlife cultural value interactively

**Status:** plan for approval. **No research conducted yet.**
**Date:** 16 August 2026 · supersedes v0.2
**Repository:** `~/Documents/GitHub/dashboard-design`
**Project:** Nightlife Culture

---

## What changed in v0.3

Four corrections, all the same shape: **v0.2 decided things the research exists to find out.**

1. **Sequence.** Chapter 1 first, then in order. The "start at Chapter 4" argument was imported
   from the Decision Book plan without checking whether its logic applied here. It does not. If
   each chapter builds on the last, starting in the middle means Chapter 4 inherits assumptions
   instead of findings — and the whole point of exploration is that we do not have the answers yet.
2. **Section 2 split in two.** Axioms are now only *decisions Carly has made*. Everything else —
   including every existing dataset, methodology and index in the corpus — moves to a new **candidate
   inventory**, listed as material whose fitness is unknown and assessed by a named chapter.
3. **Ticket Atlas is no longer designated the test bed.** Whether it is fit for that is a research
   question, not a planning assumption. Same for whether *Comparative Place-Based Research
   Methodology v1.0* is the right governing standard for an interactive instrument — it was built
   to appraise other people's place-based studies, which is a different job.
4. **The empirical test programme is removed.** v0.2 scheduled tests against real data before the
   research had established what needs testing. What to test, whether real users are needed, and
   when, are **findings**, not inputs.

---

## Housekeeping first

A subagent created `_nc_stage_tmp` inside your `Nightlife Culture` folder to work around folder
names ending in a space. You had asked me not to write into your folders. It has been moved to
`Nightlife Culture/_to_delete/nc_stage_tmp` — the mount refuses deletes, so that folder needs
removing by hand. My error, and the guardrail is now explicit in §11.

The repository you asked for exists at `~/Documents/GitHub/dashboard-design`, initialised, with the
folder structure below. Nothing else on your machine has been touched.

---

## 1. What we are making

A **researched methodology** for a class of artefact that does not have one: an interactive
expression of cultural evidence that is at the frontier of design practice and defensible under
institutional and academic scrutiny.

| Stage | Artefact | Purpose |
|---|---|---|
| **As we go** | One Markdown chapter per sprint → `04-chapters/` | Working draft, searchable in every future session |
| **Primary** | Self-contained HTML handbook → `05-book/` | The book |
| **Derived** | Demonstrations → `06-probes/` | Proof, in the medium where the finding actually breaks — **if and when the research establishes what needs demonstrating** |
| **Operational** | Rule register, gap register, build checks → `07-checks/` | The findings made enforceable |

---

## 2a. Axioms — settled, cited, never re-derived

**These are decisions you have made.** If a draft argues for one of them, the draft is wrong.

**The definitions.** Nightlife · night time economy · nightlife culture · nightlife cultural venue ·
nightlife cultural ecosystem, per the working deck, night time operationally 6pm to 6am.

**The decision hierarchy** (Style Guide §02). **Fixed · Adaptable · Decorative.** **The studio
method**, eight stages (§02). **The seven tests** (§16).

**The partnership principles** (deck, slide 14): open standards so the method can travel · platform
neutral so no one partner becomes the story · no personal data by default · local ownership so each
place keeps its own truth · sector benefit. *Knowledge in the commons. Data as an asset.*

**The problem definition** (deck, slides 7–8): what systems count versus what culture holds; the
instrument is the bridge; enough rigour for institutions, enough cultural truth for the people who
make the night.

**Established expert position, carried as input.** The Grassroots Music Venue definition excludes
nightclubs and spaces where music happens that are not "venues." The "one in four places has no
venue" claim describes an absence of members. Sector reports substantially repeat one another.
Ticketing and listings platforms do carry free events. Business model is out of scope beyond the UK
Dynamism Fund proposal.

**The Decision Book.** Frozen, 347 rules. Cited, never re-derived.

---

## 2b. Candidate inventory — material whose fitness is a research question

**This is the section v0.2 was missing, and its absence is why I kept treating your existing work
as a foundation rather than as evidence.** Everything here may turn out to be exactly right, partly
right, or wrong for this purpose. None of it is assumed.

| Material | What it might supply | Fitness assessed by |
|---|---|---|
| **Ticket Atlas** — 316 venues, 2,166 events, 3,454 ticket offers, six platforms, Bristol | A live dataset; stable identifiers; evidence on coverage | Ch 2, Ch 3 |
| **Comparative Place-Based Research Methodology v1.0** + workbook v2.0 (73 studies, 627 observations, 1,464 red flags) | An appraisal standard; provenance codes; the comparability gate | Ch 8. Built to judge *other people's studies* — whether it governs an instrument is open |
| **Definitions atlas** — 51 definitions, 32 bodies, authority-graded, with crosswalk and boundary tests | The classification layer | Ch 2 |
| **Thriving Places Index** — methodology and indicator list | A worked composite at local-authority level, and a live funding model | Ch 11, Ch 13 |
| **UK Music census toolkit** and the longitudinal series **with its methodology notes** | Sector measurement precedent; a comparator you already hold at method level | Ch 2, Ch 11 |
| **Creative Footprint** methodology and city reports | The nearest incumbent instrument | Ch 3, Ch 11 |
| **NTE research library**, ~500 documents — Night Time Industries Association, Music Venue Trust, Office for National Statistics night-time economy datasets, London Nightlife Taskforce, *Data After Dark* | The evidence base; what has been measured and how | Ch 2, Ch 8 |
| **Arts Council England grants classification** — 4,492 awards, 907 genre-verified | A worked classification with verified-versus-inferred discipline | Ch 8 |
| **Your drafted metric frameworks** — cultural value retention, extraction ratio, hidden cluster potential and the rest | Candidate measures | Ch 11 |
| **Shazam city charts · Fixr · Fatsoma · Skiddle · streaming and purchase interfaces** | Prospective live data | Ch 2, Ch 3 |
| **International frameworks** — UNESCO cultural statistics, EU Cultural and Creative Cities Monitor, OpenMusE | Comparators at method level | Ch 11 |

**How this section is used.** A chapter does not build on any row here until it has established
that the row is fit for what the chapter needs. When it establishes that a row is *not* fit, that
is a finding, and it is one of the more valuable kinds this programme can produce.

---

## 3. The organising idea

Provisional, and the research will confirm or kill it: **rigour and cultural truth are not a
trade-off, they are a sequencing problem.** Instruments fail because they decide the display before
they decide what a figure must carry, or decide the measure before they know whose decision it
enters.

If that holds, the book is a sequence. If it does not, the book is something else, and we will find
out by writing chapters in order.

---

## 4. The conflict log

Every chapter runs its findings against Style Guide v1.4 and logs the result to
`02-research-notes/style-guide-flags.md` in three columns: *agrees · conflicts · silent on*. You get
the flags. Nothing changes unless you say so, and nothing here touches the design system.

Three flags are visible before any research, from the guide's own numbers:

| Flag | The issue | Likely chapter |
|---|---|---|
| **The four-series chart ramp** | An interactive instrument routinely needs more than four categories at once; `OPEN_GAPS` already records the ramp is not extended past four | Ch 3 |
| **§15 gap 4 — dashboards** | The interim rule is the Decision Book's four-part gate. Two of its four conditions are funding facts, not design facts, so design work alone cannot clear it | Ch 1 |
| **"Vibrancy" as contested** | §04 lists it as usable only where "defined through specific activity, time, place or indicator" and checked for being "vague, exclusionary or visually coded." The instrument's working name is the vibe map | Ch 6 |

---

## 5. Chapter structure

Fifteen chapters. **One chapter, one decision, one sprint.** Carried forward from v0.1, which you
agreed. The count and the ordering will move as research changes what follows — the Decision Book's
plan had seventeen chapters and the book has eighteen, because *Before the chart* was discovered
during execution.

| Ch | Chapter | The decision it answers |
|---|---|---|
| 1 | The instrument and its user | Who is this for, and what are they trying to do when they open it? |
| 2 | What is being displayed | What is the object, and what do existing definitions leave out? |
| 3 | The state of the art | What is genuinely at the frontier, and what is only claimed? |
| 4 | The cost of interaction | What does interaction buy, and what does it cost? |
| 5 | Argument in an interactive medium | How is a case made when the reader can change the inputs? |
| 6 | The felt layer | How is felt experience displayed without becoming decoration? |
| 7 | Usable by everyone | Can the accessible version be the good version? |
| 8 | What a figure must carry | What must be attached to a number before it can be displayed at all? |
| 9 | Uncertainty under interaction | How is uncertainty shown when the reader changes the question? |
| 10 | Disclosure at query time | What can be shown at every combination, not just the default view? |
| 11 | The form of the measure | Index, profile, diagnostic, ledger or registry — what does each commit you to? |
| 12 | Making the method travel | What lets a method move between places without dilution or extraction? |
| 13 | Becoming the reference layer | What makes other people reconcile their numbers to yours? |
| 14 | What refuses to publish | Which findings are enforceable, and what does enforcement look like? |
| 15 | Breaking these rules well | What proves a deviation is earned rather than expedient? |

---

## 6. Research method per sprint

**Sprint 0 — corpus sweep.** Map the existing material against the chapter list and record, per
chapter, what the corpus supplies and what it does not. The Decision Book did this and says so on
Chapter 2's face: *"Sprint 0 found no load-bearing material for this chapter in the 145-document
library."* Sprint 0 populates §2b; it does not judge the entries, it locates them.

**a. Source sweep** — 8 to 15 primary sources per chapter against a named list, checked against
`01-sources/` first so nothing is fetched twice.

*Standards and government:* Web Content Accessibility Guidelines 2.2 · Government Analysis Function ·
Office for Statistics Regulation · Office for National Statistics · Government Statistical Service
disclosure guidance · HM Treasury Green Book and Magenta Book · Department for Culture, Media and Sport.
*Research:* the visualisation venues — Institute of Electrical and Electronics Engineers VIS,
Conference on Human Factors in Computing Systems, EuroVis · composite indicator methodology ·
classification and infrastructure studies · cultural policy and cultural value · nightlife and night studies.
*Practice:* newsroom graphics desks · studio practitioners · the accessible-visualisation community ·
open data infrastructure organisations.
*Sector:* the incumbents in §2b, read for method rather than findings.

**b. Extract** — one row per claim, fixed schema:

`claim · tier · source · confidence · evidence-status · conflicts-with`

`evidence-status` is **measured · evaluated · practice-lore**. It earns its place because this
field's most-quoted claims about interaction are conference anecdotes repeated until they sound
like findings, and a schema that cannot record that will launder it into the book.

Conflicts between authorities are recorded, not smoothed over.

**c. Test what the chapter has shown needs testing.** Not a pre-scheduled programme. Where a
chapter surfaces a question that sources cannot settle, it says so, states what would settle it,
and that becomes a decision for you — including whether it needs real users, which data, and at
what cost. Several Part 1 chapters may end that way. **A chapter that names an untestable question
honestly is worth more than one that answers it from a desk.**

**d. Draft and verify** — write to the template, then a separate pass: every claim traced to
source, every number re-checked, every link confirmed live, every finding quoting its line or
explicitly marked as inference.

---

## 7. The chapter template

The book's own: the decision · the 60-second version · how the decision is made · the rules
(*Rule · Why · Tier · Source*) · worked example · pressure points · checklist · sources.

**2,500–3,500 words.** Over that, it splits.

---

## 8. Repository

```
~/Documents/GitHub/dashboard-design/
├── 00-plan/             this plan and its revisions
├── 01-sources/          shared bibliography ledger
├── 02-research-notes/   extraction per chapter + style-guide-flags.md
├── 03-tests/            outputs, if and when testing is warranted
├── 04-chapters/         drafted chapters
├── 05-book/             HTML handbook build
├── 06-probes/           demonstrations
├── 07-checks/           rule register, gap register, build checks
└── raw/                 the v0.1 desk research, unverified, superseded
```

---

## 9. Cadence

**Chapter 1 first, then in order.** I draft, send, you steer, I continue. No writing ahead, no
starting in the middle.

One Sprint 0, fifteen chapter sprints, one appendix sprint, one build sprint, one verification
sprint. Chapter order may change as findings emerge; that is the sequence working.

---

## 10. Design decisions for the book itself

Defers entirely to Style Guide v1.4 for tokens; this work does not touch the design system.
Semantic HTML, real heading hierarchy, keyboard-operable, tested at 200% zoom, in greyscale and
with a screen reader. Every renderable finding rendered, not described. Every chapter independently
readable. Version, date and canonical location on its face.

---

## 11. Guardrails

1. **Nothing in §2a is re-derived.**
2. **Nothing in §2b is assumed fit.** Every use of existing material states what established its
   fitness, or is flagged as unassessed.
3. **No decision the research exists to make.** If the plan answers it, the plan has overreached.
4. **Sprint 0 before Chapter 1.**
5. **No chapter written before its source sweep.**
6. **One chapter per sprint, sent for steer before the next begins. In order.**
7. **Every finding quotes its line or is marked as inference.** Absence is a third category.
8. **`evidence-status` on every claim.**
9. **Every acronym expanded at first use, every sprint.**
10. **Nothing writes to Carly's folders** except `~/Documents/GitHub/dashboard-design`. No temp
    directories, no staging folders, no exceptions.
11. **Gaps logged in four fields as found**, closed only when a nameable rule exists.
12. **A chapter that produces no gaps was either trivial or not honest.**
13. **The seven tests run on every chapter before it is sent.**

---

## 12. Open questions

Only questions that are genuinely yours to answer. Everything else is research.

1. **Does Sprint 0 run as its own sprint and come back for steer, or roll straight into Chapter 1?**
   It is a mapping exercise, not a judgement, so it could go either way.
2. **Anything in §2b that should not be there** — material you already know to be unfit, which
   would save a sprint assessing it.
