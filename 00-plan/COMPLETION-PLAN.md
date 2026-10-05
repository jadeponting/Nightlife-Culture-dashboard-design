# Finishing the research book — completion plan

*For approval · 4 October 2026 · supersedes nothing; it sits beside `BRIEF-v1.md` and says how the book reaches "complete". Nothing in it starts until Carly says so.*

---

## What this plan is, and is not

It finishes the version of the book we were on. It does not think about the prototype, and it does not take in the new Vibe Map framing — that arrives after this is done and may change the recommendations. Where the book's thinking is good, it is kept whole and the journey is shown; the fixes are about **travel** (a reader with none of our context can use it), **provenance** (every claim says what kind of claim it is and how firm), **references** (visible, linked, verifiable), and **depth** in the chapters that were rushed.

---

## 1 · The deep view: what was actually produced

**Chapters 1–8 are research.** Each was built from sources verified live on the day, revised on Carly's comments, and carries worked examples, pressure points, a rules table and a gap log. They are the standard.

**Chapters 9–14 are assembly.** They were written in one overnight run under a rule of *no new research* — only material already gathered. The file sizes tell the story: Chapters 1–8 run 19–25 KB each; Chapters 9–14 run 8.5–15.6 KB. What thinned out was exactly what a reader needs: worked examples shrank or vanished, sources became "see ledger" instead of links, the gallery (Ch 12) is a table of fifteen rows rather than fifteen studied entries, and Chapter 14 is an index of the other chapters rather than a chapter.

**Three defects run across all fourteen, and they are the ones that stop the model travelling.**

| Defect | What it looks like | Why it matters |
|---|---|---|
| **Insider vocabulary** | "house", "commissioner", "steer", "axiom", "the poster mantra", "78/32", "removal test", "Fixed/Adaptable" — used without definition | A third reader cannot tell a rule from a reference from an in-joke |
| **Unexplained status marks** | **[Measured]**, **[House steer]**, *practice-lore*, **[Axiom — Decision Book Ch 7]** in bold brackets mid-sentence | They encode a grading system that was never stated to the reader; they read as noise |
| **Provenance without firmness** | A claim is cited, but the text does not say whether it is a law, a standard, a study, our reading of a reference, or a Nightlife Culture decision — nor whether it can be crossed | Exactly what Carly asked for: hard line, default, or open to interpretation if it serves another goal |

Two specific errors found on this read, both discussed in section 3: the gallery's "nobody has built this" claim is wider than its evidence, and the "brief demands not looking like the genre" rule is not in the brief.

---

## 2 · How we finish it — five sprints, in order

Each sprint ends with files in the repo, the ledger updated, the reader rebuilt, and a short note to Carly. Nothing moves to the next sprint without her nod. Estimated effort is in sessions of the kind we have been running.

### Sprint A — Make the model travel *(cross-cutting; first, because everything after writes in the new conventions)*

1. **A Chapter 0: "How to read this book."** Who it is for (including a reader with no Nightlife Culture context), the one-paragraph purpose, the method in plain words, the glossary, and the two legends below. Whether this is a numbered chapter (count moves to 15) or front matter is Carly's call.
2. **The provenance legend** — replaces every bold bracket in the book. Four kinds of claim, each with its own visible label and what the reader may do with it:

   | Label | Means | Firmness |
   |---|---|---|
   | **Standard** | An external rule we did not write — law, a W3C standard, a statistical disclosure rule. Cited. The text says whether it binds Nightlife Culture or is adopted voluntarily | Hard line when binding; stated default when voluntary |
   | **Evidence** | A measured or evaluated finding from a named study. Cited, with its strength (sample, replication) | Strong evidence is a default you need a reason to leave; contested evidence is a prompt, not a rule |
   | **Reading** | Our interpretation of reference material — the Decision Book, a paper, an exemplar. Marked as ours and open to challenge | Flexible by definition; the reader may disagree and should say why |
   | **Nightlife Culture** | A decision or piece of practice from Carly or the studio's published work. Named as such | Fixed if Carly says so; otherwise a default that the prototype may test |

   Plus one firmness mark on every rule in every rules table: **Hard line · Default · Open.**
3. **A glossary pass on all fourteen chapters.** Every term of art explained at first use, one phrasing per idea (Decision Book Ch 5, Adaptable), no term used that the glossary does not hold. "House" becomes "Nightlife Culture's own practice". "Commissioner" is defined once. The three-word evidence grading (measured / evaluated / practice-lore) is folded into the legend and dropped as inline jargon.
4. **The outsider test**, run on every chapter: a cold reader with no project context reads only the 60-second version and must (a) state the decision, (b) name one hard line and one open choice, (c) say where the evidence for the headline claim is. I run this with an agent given nothing but the chapter; any chapter that fails is rewritten until it passes. This is the Decision Book's "someone outside the sector reads the first screen" test, made mechanical.

*About two sessions. Delivers the conventions every later sprint writes in.*

### Sprint B — Verification and visible references

1. **Re-trace every agent-fetched claim at source.** The ledger already marks which. Each either becomes *verified at URL on date* or is removed and logged.
2. **Links back into the chapters.** Every source cited in a chapter is linked in that chapter, not deferred to the ledger. The ledger stays the master list; the chapters stop saying "see ledger".
3. **The gallery re-fetched** (Ch 12): each of the fifteen entries opened again, its default state recorded, its claim rechecked.
4. **The specific items:** Gapminder's default view observed, not inferred (Carly's help — see 3.4); the Fan-Led Review fetched at source; the ISO citations marked *sample pages only — purchase before publication*.
5. **The "nobody has built this" claim scoped** to the instruments actually examined, and a bounded landscape search run with a written protocol (UK and international cultural, nightlife and place-based mapping instruments; what was searched, where, when) so that whatever the claim becomes, it can be defended.

*About two sessions, mostly agent time. Can run in parallel with Sprint A.*

### Sprint C — Bring Chapters 9–14 up to the standard of 1–8

Each gets what the early chapters have: a full "how the decision is made", a worked example on a named place, pressure points, a rules table with provenance and firmness, linked sources, the acronym and glossary pass. Specific expansions:

- **Ch 9 — behavioural economics, validated and bounded.** The two claims already used (defaults as endorsement, d = 0.68; first-view anchoring) re-verified at source and their strength stated. Then a deliberately short expansion to the effects that touch display decisions and nothing else: defaults, anchoring, framing (the losers' test is a framing question), social proof in contribution, and friction in consent. Each with the replication caveat the field deserves. And one hard line drawn: **no manipulative choice architecture in consent or contribution** — the UK regulators' guidance on harmful online choice architecture is a *standard* here, not a suggestion.
- **Ch 11 — the standards chapter it should have been.** The W3C material Carly sent is integrated and classified, with the legal position stated for a UK private platform rather than a public body (see 3.5). WCAG 2.2 AA, ARIA and the Authoring Practices, COGA, the WAI principles and design/develop guidance — each marked *law / standard / guidance / Nightlife Culture*, each with what it changes in the instrument.
- **Ch 12 — a gallery, not a table.** Fifteen studied entries after Sprint B's re-fetch: what the default view shows cold, what rule it breaks, why it holds, what we take and what we refuse. The white-space claim rewritten to its evidence.
- **Ch 13 — the prototypicality provenance corrected** (see 3.3) and the expressive-moves table given worked examples.
- **Ch 10 and Ch 14** — worked examples; Chapter 14's gap register becomes a real register holding G1–G7 from the reader with their four fields and owners.

*About three sessions. The largest piece of writing.*

### Sprint D — Backfill Chapters 1–8

The cross-cutting changes applied (legend, glossary, firmness marks, links), the **UK-only framing** made explicit where it changes a rule (geographies, UK GDPR and the ICO anonymisation code, the Equality Act; US exemplars kept as exemplars only), and the glosses placed where they belong: the threshold-as-collection-design problem (G2) into Ch 4 and Ch 8; hostile contributors (G3) into Ch 4; who speaks for a scene (G4) into Ch 7; change over time (G6) into Ch 5 and Ch 6; phone-first (G5) into Ch 9 or Chapter 0.

*About two sessions.*

### Sprint E — Close the version

Reader rebuilt from the revised chapters (its own front matter rewritten in the same travelling language); ledger complete; STATE updated; the Style Guide conflict logs re-pointed from v1.4 to v1.4.1 and marked for re-check if v1.4.2 is adopted. Then it stops, and Carly reads. Her redlines are the last step of this version. Only after that does the new Vibe Map framing come in and a Part 5 get scoped.

*One session.*

**Total: roughly ten sessions**, run economically, one sprint at a time, each ending with a short note and a decision point.

---

## 3 · Answers to the questions in Carly's note

### 3.1 Has the style guide or skill moved on?

Checked. The installed skill is generated from **Style Guide v1.4.1** (colour law corrected at source, 31 Aug). A **v1.4.2 draft** exists in the design-system repo — "replaces v1.4.1", September 2026 — but is **not adopted**; adopting it is open decision 4 on THE-PLAN. Nothing in either changes the research findings. Two things change how the book is written: the guide's decision hierarchy puts *legal and ethical requirements* first (which this plan's provenance legend now mirrors), and the 29 September decisions on tables (first column bold; editorial table as house document style) affect the reader's presentation. The book's conflict logs currently cite "v1.4" and will be re-pointed in Sprint E.

### 3.2 Behavioural economics — validate or expand?

Both, in that order and narrowly. The book leans on two findings; both are re-verified first. Expansion is limited to effects that decide a display choice (defaults, anchoring, framing, social proof, friction) — not a tour of the field — and every effect carries its replication status, because this literature has a known problem there. One hard line comes out of it (no manipulative choice architecture in consent), which the current text does not state.

### 3.3 "Prototypicality rewards looking like the genre" versus the brief — where is this rule in the brief?

It is not in the brief. Honest provenance: the "do not look like the genre" demand came from Carly's opening prompt ("explicitly not PowerBI") and from the Skiddle-call instruction ("make it look like art, not a government boring thing"). Those are **Nightlife Culture** steers, not brief rules, and Chapter 1 should have said so. The prototypicality finding itself is **Evidence** (a measured effect on first-impression judgements of websites) and the "collision" was partly manufactured by treating a steer as a rule. Chapter 13's resolution — the claim picks the genre, and this instrument's genre is nightlife's own visual tradition — still stands, but it is a **Reading**, not a rule, and will be relabelled. If Carly wants "not the dashboard genre" as a brief-level rule, the brief is amended deliberately; otherwise it stays a default the prototype can test.

### 3.4 Gapminder — "could not be fetched; its default state is inference"

What the reference is for: Gapminder's tools are one of the ten instruments in the Chapter 1 display audit, chosen because they are the best-known example of an *animated* default view. The question the audit asks of every instrument is the same: **shown cold, before anyone touches it, what does the first screen say, and does anything move?** For Gapminder we could not load the tools page, so the audit guessed. Carly can replace the guess in five minutes: open the tool (web `tools.gapminder.org` is the canonical one; the desktop app may differ, so note which), screenshot the very first screen without clicking anything, and jot down: which chart loads first, which two or three indicators are on the axes, which year is showing, whether it autoplays, and what text is on screen. That becomes a verified entry.

### 3.5 The W3C links — COGA, ARIA, WAI standards, design and develop, accessibility principles, the WCAG 2.2 quick reference

All useful, and they sort into three different kinds of thing, which is the point of the legend:

- **WCAG 2.2 Level AA** — a *standard*. For a UK private platform it is not directly mandated by the Public Sector Bodies Accessibility Regulations 2018 (those bind public bodies), but the Equality Act 2010 duty on service providers to make reasonable adjustments is real and WCAG AA is the recognised benchmark for meeting it — and the moment a council or combined authority embeds or procures the instrument, the public-sector regulations reach it through them. So: **hard line**, adopted voluntarily now, likely binding by procurement later. (Not legal advice; a lawyer should confirm before any contract.)
- **ARIA and the Authoring Practices Guide** — a *standard* that becomes a hard line the moment the instrument has custom interactive widgets, which a map and charts are. Charts and maps need roles, accessible names, keyboard patterns and text alternatives, or Chapter 11's convergence claim fails on contact.
- **COGA (Making Content Usable for People with Cognitive and Learning Disabilities)** — *guidance*, a W3C Note, not normative. Its objectives map directly onto what this book already wants for the third reader and the dancefloor: clear language, help people find what they need, do not rely on memory, give time, prevent and tolerate mistakes. It will be adopted as a **default**, cross-referenced to the style guide's "Plainspoken" quality and the Decision Book's reading-age guidance (Ch 5: reading age about nine as a proxy for sentence and clause complexity, *Adaptable*) — which is also the language steer for this book's own prose.
- **The WAI principles and design/develop pages** — orientation, not rules; cited as the frame Chapter 11 sits inside.

### 3.6 The gallery's white-space claim, and the links

The claim should read: *of the fifteen instruments studied in the gallery and the ten audited in Chapter 1, none displays cultural value, origination, or a consented scene layer.* It currently reads as "anywhere", which the evidence does not support. Sprint B scopes it, and runs a bounded landscape search so it can either be strengthened or dropped. The links stopped in Chapters 9–14 because the overnight run deferred everything to the ledger; Sprint B puts them back in the chapters.

### 3.7 UK-only platform, not a public body, reading age

Noted as a frame for every standards claim. Practical consequences for the book: UK geographies and the postcode–UPRN–LSOA chain are the reference set; UK GDPR and the ICO anonymisation code govern the origination work, not US frameworks; the Equality Act position above; English copy with Welsh as an *open* choice (Welsh Language Standards bind public bodies, not Nightlife Culture); reading-age guidance applied to both the book and the instrument's own copy. International exemplars stay as design references only.

---

## 4 · My questions for Carly

1. **Who is the third reader?** A build team, a funder, an academic partner, a council officer — the glossary's depth and Chapter 0's tone depend on it. If it is more than one, say which comes first.
2. **Chapter 0: a numbered chapter or front matter?** It changes the count the brief carries.
3. **The brief amendment** in 3.3 — do you want "not the dashboard genre" as a rule, or left as a default?
4. **Is "nobody has built this" a claim you want to make in public?** If yes, the landscape search in Sprint B is worth its cost; if it is internal, scoping the sentence is enough.
5. **Gapminder** — can you do the five-minute observation in 3.4?
6. **Budget.** Ten sessions is the honest estimate. If you want it faster, Sprint C is where depth can be traded; Sprints A and B should not be.
