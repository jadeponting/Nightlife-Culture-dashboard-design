# The reference section

*Behind the book. The chapters teach; this section holds the machinery an agent or a build needs, and the record of how the book was made.*

The reader (`05-book/reader.html`) carries four of these as appendices: A, the rule register; B, the decision log; C, the deviation log; D, the probe candidates.

| Part | File | Holds |
|---|---|---|
| Decision log | `00-plan/DECISIONS.md` | Every open choice in one place, each with the book's steer and the moment the build will raise it. The only place an open choice lives |
| Rule register | `06-register/rule-register.md`, `.csv` | All 377 rules, stated once, with tier, kind, source, chapter rows, test, record and status. The current statement of each rule's tier |
| Deviation log | `06-register/deviation-log.md` | The nine-line entry every departure from a rule is written to, and the entries so far |
| Working record | `06-register/working-record/` | How each chapter was made: the sections moved out of the chapters on 14 October 2026, word for word |
| Probes | `03-tests/PROBES.md` | Seventy-five small proposed tests; none has run |
| Sources ledger | `01-sources/SOURCES.md` | Every source read, how and when |
| Research log | `01-sources/RESEARCH-LOG.md` | Each chapter's plan, written before its research, and what it found |
| Library pass | `01-sources/LIBRARY-PASS.md` | What was found when abstract-only sources were read in full; its ten corrections are applied |
| Research notes | `02-research-notes/` | The agents' returns behind each chapter, and the compilation Chapter 16 was built from |

## The register and the deviation log

What the build inherits from the book (Chapter 16 §8). First generated on 7 October 2026 (research log, Entry 17) and regenerated from the finished chapters on 14 October 2026, when the status value "awaiting Carly" became "open in the decision log" and rule DD-373's wording changed from "until Carly decides" to "until the decision log settles it".

- `rule-register.csv` / `rule-register.md` — 377 rules from the 513 rows of the sixteen chapters' rules tables. One rule per group of duplicates, stated once in a chapter's own words, with: the tier in Chapter 16's senses (Fixed as a requirement or a sequence; Adaptable (house default); Adaptable; Decorative) and the open part of any rule whose order is fixed and form is not; the reason for that tier; kind, sub-kind of Standard, and whether a Standard binds the studio (B) or is adopted (A); the source of the stated row; every chapter row that states the rule, as chapter.row; the form of its test and what is checked; the section of the record it writes to; its status (*current*, *superseded*, *disputed*, *open in the decision log*, *full text not read*); and `cited_by`, left empty for the build. One statement of the record is listed apart as `DS-001`. Identifiers are provisional.
- `deviation-log.md` — the nine-line entry every departure from a rule is written to, the extra lines for an expressive element (Chapter 14) and a borrowed mechanism (Chapter 15), and the entries. One so far, proposed.
- `build_register.py` — `parse` reads `02-research-notes/ch16-assembly.md` Part 1 and Chapter 16's own table into `work/rows.csv` and `work/groups.csv`; `build` merges the classification files into the register. Run from the repository root. Do not edit the register by hand.

## `work/`

| File | What it is |
|---|---|
| `rows.csv` | The 513 source rows as printed: chapter, row, file line, rule, why, kind, tier, source |
| `groups.csv` | The compilation's 42 groups of rules stated in more than one chapter |
| `BRIEF.md` | The rules the classifiers applied: Chapter 0's tier table and Chapter 16 §3, §7 and §8, as they stood on 7 October |
| `classified-1.csv`, `-2`, `-3` | One line per source row (Chapters 1–5; 6–10; 11–16): the re-based tier, open part, a reason of twelve words or fewer, test, check, record section, kind fields, status, notes. This is where a tier decision is changed |
| `groups-decided.csv` | For each group, the member row whose wording stands for it, and the group's tier |
| `group-splits.csv` | Groups split after the first pass, by Chapter 16 §7's two- and three-rule decisions and the verifier's findings |
| `dagger-fixed-rows.csv` | The 51 Fixed rows resting on an abstract or secondary source; the library pass's list |
| `library-A.md`, `library-B.md` | The two library-pass reports as returned; `01-sources/LIBRARY-PASS.md` joins them under a summary |
| `probe-lines.md` | The 189 flagged lines `03-tests/PROBES.md` was compiled from |

## What to know

The register has 280 Fixed rules (74 per cent); Chapter 16 estimated about two hundred before it was built. The chapter's postscript says what that changes. A verifier sampled thirty rules and every grouped rule and its fourteen findings were fixed; the other rules' tiers rest on one classifier's reading against the brief, with the reason recorded beside each. Where the register and a chapter's own table differ on a tier, the register is the current statement.
