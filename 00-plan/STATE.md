# STATE — dashboard-design research book
*Updated 17 August 2026, end of live session. If a fresh session ever picks this up: read
`00-plan/BRIEF-v1.md` first, then this file, then the latest chapters.*

## Done (committed)
- `00-plan/BRIEF-v1.md` — governs. 14 chapters. §"What is never researched" and the working
  method are binding. Chapter count moved once already (Discovery added on steer).
- Chapters 1–8 drafted in `04-chapters/` — Part 0 and Part 1 complete.
- `01-sources/SOURCES.md` — ledger: conventions, house corpus locations, per-chapter sources
  with verification status. **Rule: no chapter is done until its sources are here.**
- `02-research-notes/` — per-chapter working notes; use-case register (4 moves incl. platform
  horizon); context note (confidentiality register; CBS/WECA horizon; live-prototype plan).
- `raw/` — superseded early research. Unverified. Nothing graduates without landing in ledger.

## UPDATE — overnight run complete (17 Aug, early hours)
**All fourteen chapters are drafted and committed.** Chapters 9–14 were written consecutively
in-session (the scheduled triggers were cancelled once the limit reset). Ledger updated
(consolidated Ch 9–14 section); working notes at `02-research-notes/ch09-ch14-working-notes.md`.
Awaiting Carly's steer on: (1) chapter revisions from her read-through; (2) the HTML handbook
build; (3) the verification sprint (re-trace agent-fetched claims — the ledger marks which;
gallery entries flagged for re-verification); (4) the probe programme in `03-tests/` — now
effectively a research agenda the field itself lacks; (5) the live prototype alongside the
CBS work. **None started — they are decisions, not defaults.**

## The original plan for the remaining chapters (now superseded — kept for the record)
9. **What an interaction must earn** — from verified material: the null (no-story group explored
   2×), prediction-before-reveal (narrow), staged transitions, 10–15% + Aisch correction, Cho
   anchoring, Heer/Shneiderman taxonomy as coverage audit. NO new agents.
10. **Story and exploration** — Segel & Heer genres/martini glass (menu, unevaluated),
    scrollytelling essentially unevaluated, Hullman rhetoric, BLI reweighting-as-collection,
    ONS 331-stories case. NO new agents.
11. **Accessible as the good version** — Chartability (50 heuristics, 10 critical, 2–8h),
    Olli (structure/navigation/description, 13 blind users), Umwelt (5 users — promising),
    WCAG 2.2 AA as distribution decision, §13 axioms, sonification flagged. NO new agents.
12. **The gallery** — assemble from Ch 1 audit + raw exemplars (Pudding ×2, OWID, ONS ELS,
    BLI, Every Noise, Better Catastrophe incl. its evaluation data, Fragapane/MoMA) + incumbent
    display audit (TPI select-first, Creative Footprint gated, observatory hub). Each: what
    rule it breaks, what substitutes, why it holds. Mark anything not re-verified.
13. **Make it look like art** — Bateman/Borkin/Alebri embellishment line, Lupi, Fragapane MoMA,
    the prototypicality tension (Ch 1 gap — resolve it here), five-word poster rule,
    sound-bounce register, Chartability's no-beauty-exemption, name-the-purchase (DB Ch 7).
14. **Breaking these rules well** — assemble every chapter's proof tests into the removal-test
    table; deviation taxonomy; override log; seed `07-checks/` rule register; summarise the
    book's own gap register.

## After the chapters (needs Carly's steer — do not start unprompted)
- HTML handbook build (`05-book/`), Decision-Book style; verification sprint (every claim
  re-traced); probes (`06-probes/` — candidates flagged in chapters: mock two-columns screens,
  dominance-display readability, dot-plot collection, staging-decay, night-map absence test).
- The live prototype alongside the CBS/WECA work (see context note).

## Standing rules for continuation turns
No new research agents. Write from ledger/raw/house material already gathered. Every chapter:
template → acronym pass → seven tests → ledger entry → working note → commit via
device_commit_files (git index.lock on the repo may still need a local `rm`). Chat summaries
short. Confidential items (Vibe Setting Framework, 2026 data) cited, never reproduced at
length. If blocked, log here and stop cleanly.

## UPDATE — 4 October 2026 (picked back up)
**Nothing in the book changed between 17 Aug and today.** Pushed 31 Aug (commit 62e665e). The
five decisions remain open and unstarted: (1) Carly's redlines on Ch 9–14 — never happened;
(2) HTML handbook; (3) verification sprint; (4) probe programme; (5) live prototype.
Since 1 Oct the book is read in full by THE-PLAN step 6 (dataviz design standards,
`~/Documents/GitHub/nightlife-culture-dataviz`) as the implementation brief for chart rules —
read only, never written to. The book is therefore load-bearing for live work while six of its
chapters are unsteered.

**New this session:** `05-book/reader.html` — a navigable, searchable reader built from
`04-chapters/*.md` on the design system (v1.4.1 skill). Front matter carries: where we got to;
the five decisions with dependencies; the flagged glosses G1–G7 in four-field format; the
still-to-do register (validate / probe / prototype and build). It is regenerated from the
chapter files, never edited by hand, and it is **not** the handbook (decision 2).

**Flagged glosses (G1–G7, detail in the reader):** Ch 9–14 unverified twice over (red);
suppression threshold is a collection-design problem not only a display one — cf. UKDF review
GAP-13 (red); gaming the vibe score / hostile contributors untested (red); who speaks for a
scene (amber); phone-first unowned (amber); change over time barely treated (amber); committee
export inherits the production-chain failure FB-09/FB-10 (amber).

**Housekeeping done:** repo git identity set to Carly's GitHub no-reply address; stale lock
files moved to `.git/stale-locks/` (safe to delete). Git write operations through the device
bridge leave lock files behind — commit from GitHub Desktop or Terminal, not via the bridge.

**Still awaiting Carly's steer. Nothing starts unprompted.**
