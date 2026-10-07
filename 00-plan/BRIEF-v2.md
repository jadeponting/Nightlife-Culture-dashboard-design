# Dashboard Design — the brief, version 2

*For Carly's approval · 5 October 2026 · supersedes BRIEF-v1 (16 August) when approved. Nothing from version 1's research is discarded; section 7 says where each existing chapter goes.*

---

## 1 · What this book is

A knowledge base on **how dashboards work and why** — so that Nightlife Culture can prototype the *purpose* of the Vibe Map without having to prototype data visualisation from first principles each time. It sits in the same family as the Decision Book (how to choose) and the design system (what the values are). This book is the third: **how evidence is turned into a display that a reader can trust, read, and act on — and what that costs when it is done badly.**

It is written for someone meeting this for the first time: a creative technologist, an analyst, a research partner, a facilitator running a testing session. It teaches. It does not report what its author read.

It is a dashboard. The word is kept and defined: *a display that turns data into a decision for a named reader.* Power BI is one bad species of the genus, not the genus. The Vibe Map is the specific case, and appears only in worked examples.

## 2 · The mission, in Carly's words

These lines are the frame the book is written inside. They are not researched, re-argued or softened. They are the brief.

> A dashboard fails if it looks the same every month. It fails if it's just a fancy spreadsheet with some charts that tell you lots of big numbers, but not what actually happens. It fails if a viewer reads it and asks "what am I looking at". For nightlife, it fails if they do not recognise their place within the front-end interface. It fails if people don't use it. It fails if it breaks or isn't reliable. It fails if people don't trust it. It fails if it's an aggregation of "the biggest".

> If a music ecosystem map measures what happens in a place, the institutions with the biggest footprint will always crowd out the noise of a suburban community hub who holds music communities together. … What's flattened as an outlier could actually be an indicator that something is happening here, something is working well for the people who come here.

> Nightlife is civic infrastructure. It is flattened by the measurements that are currently used to talk about it — which effectively tell us the price of everything and the value of nothing. … Instead of measuring "feeling of safety", why are we not instead measuring the vibe that night time communities create?

> Places don't make great artists; artists make great places. People collectively make a place what it is.

> So yes. It's a dashboard. But what does it DO, why does it matter, what do we risk when it's done poorly, and what do we gain when it's done well? How do we prove it? How might one measure a vibe?

## 3 · The questions the book must answer

Six, from Carly's brief. Every chapter serves at least one and says which.

| | Question | What the book owes |
|---|---|---|
| Q1 | **What are the canonical truths?** What must hold true in any dashboard, regardless of field, for it to be read correctly and trusted | The short list of findings that survive scrutiny across sectors, with their evidence and strength |
| Q2 | **What turns a decision?** How policymakers, placemakers, inward-investment teams, developers, advocates, funders and investors actually read evidence, and what moves them | The reader's frame for each audience: what they count, what they discount, how a display reaches a decision |
| Q3 | **How is value found and measured in the data?** How to ask a database "how is value created here?", find positive indicators, build a measure, validate algorithmic assumptions into canonical truths, show value created and value extracted, spot vulnerability, track interventions and ripples over time, compare places honestly, and read market movement | The analytical and statistical methods, taught, with what each can and cannot claim |
| Q4 | **What are the safety and ethical considerations?** How to tell the story without exposing or exploiting the communities in the data | The standards, the law for a UK private platform, the disclosure methods, consent at scene level, and the lines that are not crossed |
| Q5 | **What are the technological boundaries?** Live APIs, government open data, automation without admin, reliability, refresh, phones, maps | What is feasible, what it costs, where it breaks |
| Q6 | **How does the creative layer sit on the evidence layer?** How the interactive, expressive surface reads from the data and responds to it without weakening it | The boundary rules: what must stay true under any creative treatment — not the creative decisions themselves |

**And the question that runs through all six: how might one measure a vibe?** The book does not answer it for Bristol. It sets out, with evidence, the families of method by which it *could* be answered, what each would need, and how any answer would be validated — above all by whether the people who make a scene recognise themselves in it.

## 4 · What the book never does

- **It never researches nightlife.** Sector facts, the night time economy's datasets, how Whitehall's Green, Magenta, Teal and Orange Books are used, how local government works from the inside, how culture and the arts measure value — Carly holds this knowledge. It enters the book as the frame readers already have, quoted from her or the studio's published work, and is never looked up.
- **It never answers the prototyping questions.** "Does Bristol have X?" is for the prototype. "By what method, with what data, validated how, would anyone establish X?" is for the book.
- **It never makes the creative decisions.** The club-flyer question — how to make nightlife data as exciting as a club promotion — belongs to Carly and her visual designers. The book marks the boundary between expression and evidence and stops.
- **It never specifies the build.** No schema, no stack, no screen designs. Worked examples illustrate a principle and say so.
- **It never reproduces confidential material.** The Vibe Setting Framework and the 2026 data are cited, never quoted at length.

What *is* in scope, and was under-served in version 1: how **other sectors** construct, read and trust evidence displays — public health, finance and risk, economic development and placemaking, the culture and charity sectors' impact frameworks, the critical scholarship on indicators and urban dashboards. The book reads them for method, and asks what nightlife can borrow.

## 5 · How a chapter teaches

Each chapter answers one question, for a first-time reader, in this order:

1. **The idea, plainly.** What a default view *is*; what a composite index *is*; what disclosure control *is*. No prior reading assumed.
2. **Why people believe what they believe about it.** The folklore, the convention, the textbook rule — stated fairly.
3. **The evidence.** What has been measured or evaluated, by whom, how strongly — and where the belief turns out to rest on nothing.
4. **What holds true regardless.** The canonical part. Marked Fixed when it has a right answer.
5. **Where the choice is yours.** The Adaptable and Decorative part, with the trade-offs named.
6. **What this means for a nightlife dashboard** — one worked illustration, labelled as such.
7. **The rules**, in a table carrying *kind* (Standard · Evidence · Reading · Nightlife Culture) and *tier* (Fixed · Adaptable · Decorative), per Chapter 0's legend.
8. **What proves a break works**, the checklist, the sources (linked, with how they were read), the gaps found, and the design-system conflict log.

**Voice.** The studio's: culturally literate, plainspoken without flattening, warm, precise about uncertainty, generous, constructive. Joy → value → evidence → action. It never explains the sector to itself. Technical and policy language is used where it is the most accurate language, and explained at first use. No "instrument". No bold-bracket marks.

**Evidence discipline.** Quote the line or mark it as our reading. Any claim relayed by an agent is read at source before it is written. Every chapter's sources go into the ledger before the chapter is called done.

## 6 · The chapter map, version 2

Seventeen chapters in five parts. Old chapter numbers in brackets show where version 1's research goes; nothing is thrown away.

### Part 0 — Foundations

**0 · How to read this book** — the legend, the glossary, who it is for. *(Exists; revise for "dashboard".)*

**1 · What a dashboard is for.** What it does, why it matters, what is risked when it is done poorly, what is gained when done well. Carly's failure register as the organising spine: looks the same every month · a fancy spreadsheet · "what am I looking at" · people don't recognise their place · nobody uses it · it breaks · nobody trusts it · an aggregation of the biggest. The dashboard literature's own taxonomy of purposes; the evidence on whether dashboards change decisions at all. Q1, Q2. *(New; absorbs old Ch 1's "write the sentence first" and old Ch 9's "what an interaction must earn".)*

**2 · Who reads it, and what turns their decision.** The audiences — policy and politicians; economic development, placemaking, inward investment and developers; advocates and trade bodies; funders and investors; the scenes themselves — and how each reads evidence: appraisal logic, theory of change, cultural and social value frameworks, investor due diligence. What the research says moves a decision, and what merely decorates one. How other sectors articulate benefit, and what nightlife can borrow. Q2. *(New; absorbs the leverage-points work.)*

**3 · The canonical truths of showing data.** The short list that survives: defaults are read as advice; words carry the message; the glance is judged in milliseconds; "overview first" is folklore; label at the mark; colour never carries meaning alone; uncertainty shown honestly is trusted more, not less. Q1. *(Old Ch 1's evidence, parts of Ch 9 and Ch 10, the Decision Book's data chapters as axioms.)*

### Part 1 — The analytical foundation

**4 · From data to evidence.** Grain and denominator; provenance; the six kinds of nothing (zero, free, unavailable, unknown, not collected, suppressed); comparability; why aggregation hides the grassroots (the 78%/32% finding as the worked case) and why an outlier is a signal before it is noise. Q3. *(Old Ch 3's aggregate-bias work, old Ch 8's gap vocabulary, the prototype data contract.)*

**5 · Building a measure.** What a composite index is and how the OECD/JRC method constructs one; weighting, normalisation, sensitivity; Goodhart's and Campbell's laws; the rule that no composite cultural-value score exists without an adopted method; validation — including validation by recognition. The recipe on the face. Q3. *(Old Ch 6.)*

**6 · Finding value in the data.** How to ask "how is value created here?": revealed preference (who comes, from where, how often, how far, whether they return); diversity and access (programme breadth, price, time, welcome); longevity and resilience; red flags of vulnerability; value created and value extracted; the hollow success — every standard marker met and nobody local goes. The methods: pattern discovery, anomaly detection as signal, small-area and small-n statistics, and how an algorithmic assumption is validated into a canonical truth. Q3. *(New; absorbs old Ch 6's origination claim ladder.)*

**7 · Comparison, time and intervention.** Comparing places without a league table; change over time and seasonality; tracking an intervention and its ripples (before/after, difference-in-differences, synthetic control, and what each can honestly claim); scenario and prediction — "x policy change gives y benefit at z risk" — and the honesty rules around it; reading market movement. Q3. *(Old Ch 5, expanded.)*

**8 · Automation without admin.** Living series; APIs for ticketing, streaming and government open data; refresh, freshness and the heartbeat; reliability; what breaks; performance on a phone; map rendering; caching and rate limits. The technological boundaries. Q5. *(Old Ch 8's freshness work, plus new.)*

### Part 2 — The felt layer

**9 · Measuring a vibe.** The families of method by which a felt quality of place can be evidenced: co-produced contribution (the human dot plot, the "what this changed" field); relational measures (co-appearance, networks, with the data contract's caution that co-appearance is not a social tie); revealed behaviour; the three registers of feeling; what affective and sentiment methods can and cannot do; and validation by whether the scene recognises itself. Q3, Q6. *(Old Ch 4, expanded into the book's central chapter.)*

**10 · Safety, ethics and consent.** Telling the story without exposing or exploiting the communities in it. Disclosure control at query time; k-anonymity and differential privacy in plain terms; UK GDPR and the ICO's anonymisation guidance; the Equality Act position for a private platform; consent and withdrawal at scene level, and who speaks for a scene; hostile contributors and gaming; data justice and data feminism as frames. Q4. *(Old Ch 7's consent work, old Ch 8, the seven glosses G2–G4.)*

### Part 3 — The reading experience

**11 · The first screen and the path through it.** The default view and the six landing patterns; story and exploration; what an interaction must earn; citable states. How a display reads from the data layer and responds to it. Q1, Q6. *(Old Ch 1's patterns, old Ch 9, old Ch 10.)*

**12 · Recognising your place.** The two columns — counted beside missed; identity never ranked, conditions compared with a gate; the scene scale; discovery as matching, not ranking; the crop test. The failure "they do not recognise their place" answered. Q2, Q3. *(Old Ch 2, old Ch 5's identity split, old Ch 7's discovery.)*

**13 · Accessible as the good version.** The W3C standards classified — WCAG 2.2 AA, ARIA, COGA, the WAI principles — and the UK legal frame; audio and written routes; the blind-fan test. Q4, Q1. *(Old Ch 11.)*

### Part 4 — The boundary and the practice

**14 · Where evidence meets expression.** The boundary rules: what must stay true under any creative treatment; the removal test; the embellishment evidence as a licence with conditions; the gallery of studied exemplars, each with what it breaks and why it holds. Not the creative decisions — the line they may not cross. Q6. *(Old Ch 12 and old Ch 13, reduced to their methodological core.)*

**15 · Learning from the best.** Sector by sector — public health dashboards, finance and risk, economic development, the culture and charity sectors' impact practice, the great public data projects — what they got right about trust, provenance, change over time and reach, and what nightlife borrows. Q1, Q2. *(New; absorbs old Ch 12's exemplars.)*

**16 · Breaking these rules well.** Tiers, deviation, the override log, the assembled removal tests, the gap register, the rule register for the build. *(Old Ch 14.)*

*Chapter 15 could fold into Chapters 2 and 5. Kept separate here because "take inspiration from the best in the world" was named in the brief; Carly's call.*

## 7 · Where version 1's chapters go

| Version 1 | Version 2 |
|---|---|
| Ch 1 The default view | Evidence → Ch 3; patterns → Ch 11; "write the sentence first" → Ch 1 |
| Ch 2 The two columns | Ch 12 |
| Ch 3 The map | Aggregate bias → Ch 4; map-as-thinking-tool and marks → Ch 11 and Ch 12 |
| Ch 4 The felt layer | Ch 9 |
| Ch 5 Comparison without a league table | Identity split → Ch 12; comparison methods → Ch 7 |
| Ch 6 The measure on screen | Ch 5; claim ladder → Ch 6 |
| Ch 7 Discovery | Matching → Ch 12; consent → Ch 10; platform dependency → Ch 8 |
| Ch 8 Gaps, uncertainty, freshness | Gap vocabulary → Ch 4; heartbeat and reliability → Ch 8; uncertainty → Ch 3 |
| Ch 9 What an interaction must earn | Ch 11; the purchase idea → Ch 1 |
| Ch 10 Story and exploration | Ch 11 |
| Ch 11 Accessible as the good version | Ch 13 |
| Ch 12 The gallery | Ch 14 and Ch 15 |
| Ch 13 Make it look like art | Boundary rules → Ch 14; creative decisions removed (Carly's) |
| Ch 14 Breaking these rules well | Ch 16 |

## 8 · The research programme

Each new or expanded chapter is researched before it is written: canonical texts read at source, cross-sector practice studied for method, every claim's strength stated. The candidates below are **a reading list, not findings** — nothing is a claim until it has been read and verified. Carly adds or strikes.

- **Dashboards as a class** — the field's own taxonomy of what dashboards are and do; the design-pattern literature; the performance-management origins (balanced scorecards and their critics); the critical scholarship on urban dashboards and indicators; the evidence on whether public dashboards change decisions.
- **Indicators and indices** — the OECD/JRC handbook on composite indicators; sensitivity and robustness; Goodhart, Campbell and the audit-culture literature; the reactivity of rankings (already in the ledger).
- **Value frameworks in other sectors** — how the culture sector's cultural value and social value practice is built and criticised; theory of change and evaluation logic as readers use it; social infrastructure and "third place" theory as the frame other sectors use for gathering places; wellbeing and belonging measures and their validation.
- **Evaluation and causal method** — before/after, difference-in-differences, synthetic control, small-area estimation; what each honestly claims; how prediction is presented without false precision.
- **Public health and finance** — what the 2020 public dashboards taught about trust, provenance and change over time; how risk displays are built to be read under pressure.
- **Ethics and law** — disclosure control, k-anonymity and differential privacy in plain terms; UK GDPR and ICO anonymisation guidance; data justice and data feminism; consent in participatory data.
- **Technology** — live-data architectures, API constraints for ticketing and streaming sources, government open data, map rendering and performance on phones.
- **Already in hand** — the visualisation evidence from version 1 (defaults, anchoring, overview-first, glance, memorability, uncertainty, accessibility standards), verified where marked.

## 9 · How the work runs

One chapter per sprint, in order, research then draft, sent for steer. Short chat replies. Every chapter: template → ledger entry → working note → delivered as a file. Carly reviews and commits; Claude never commits. The reader is regenerated at the end of each part. The old chapters stay in the repo under `archive/v1-chapters/` with a note until their material has landed in the new ones.

**Estimated:** seventeen chapter sprints, of which seven are largely rewrites of existing research (3, 5, 11, 12, 13, 14, 16) and the rest need new research. Realistically four to six weeks at the August cadence.

## 10 · The first sprint, if approved

**Chapter 1 — What a dashboard is for.** It tests the register on one real piece: a teaching chapter, in the studio's voice, built on Carly's failure register and the field's own evidence about what dashboards are and whether they work. If it reads right, the rest follows the same shape. If it doesn't, nothing else has been built on it yet.

---

## For Carly to decide

1. Approve this brief as version 2 (or mark up).
2. Seventeen chapters, or fold Chapter 15 into 2 and 5.
3. Anything in section 8's reading list to add or strike — particularly where you already hold the canonical text and want it used rather than found.
4. Confirm the first sprint is Chapter 1.
