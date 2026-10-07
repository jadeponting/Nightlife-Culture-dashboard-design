# Chapter 0 — How to read this book

*Dashboard Design · the research book behind the Vibe Map's screens*
*Version 2 · revised 6 October 2026, after Chapters 1 and 2 · for Carly's steer*

---

## What this book is for

**To set out how dashboards work and why — the methodological and theoretical foundation on which a build team can decide how evidence becomes a display that a reader trusts, reads and acts on — so that the Vibe Map can prototype its *purpose* without having to prototype the function of data visualisation from scratch.**

That sentence is the whole job. Everything in the chapters that follow is either evidence for it, a rule derived from it, a choice it leaves open with the trade-offs named, or a note that the evidence ran out.

The book was written for Nightlife Culture, a creative policy studio led by Carly Heath, during 2026. It is research about *how dashboards work* — from the perspectives of data analysis, economic and policy evaluation, public-sector decision-making, persuasion research, ethics and accessibility, and the craft of display. It is written for someone meeting that subject for the first time. It is not research about nightlife, and it is not an assessment, specification or design of the Vibe Map. The studio holds the sector knowledge and the creative decisions; where the book needs a fact about the sector, it takes it from Carly or from the studio's published work and says so, and where a chapter illustrates with the Vibe Map it says "an illustration, not a specification".

Carly's own statement of the mission, and the eight ways she says a dashboard fails, are in `00-plan/BRIEF-v2.md` section 2 and are the spine of Chapter 1.

## Who it is written for

In order of priority:

1. **The people building the Vibe Map** — the creative technologists, analysts and designers named in the project's funding deck. You will have the deck, the design system and the prototype repository, but not the conversations this book came out of. The book is written so that you do not need them.
2. **The people running the testing** with the three user groups the project has chosen — policymakers and politicians; advocates and trade bodies; funders and investors — with artists, DJs, promoters, crews and venues as co-developers who check whether they recognise themselves in it. (Chapter 2 finds that those three groups are, on the evidence, at least seven kinds of reader who grade evidence by different rules; the testing may want to reflect that.)
3. **Research partners** who may be asked to strengthen the method or evaluate what happens.
4. **Carly**, who set the mission and is its final reader, and whose decisions it records.

If you are none of these and have arrived cold: read this chapter, then `00-plan/STATE.md` for where the work has got to, then whichever chapter's question you are facing. Each chapter is a standalone addition to the argument and opens with a "Before you start" note that repeats the two conventions below.

## What the Vibe Map is, in the project's own words

From the funding deck (September 2026): *a living, interactive map of the people, activity, value and support systems that sustain a place's nightlife culture.* It is a free, public-facing, non-commercial resource, developed with the people who create and use it. The project's priority places are Bristol first, then Bath and North East Somerset, South Gloucestershire and North Somerset, with national coverage as context. It is a UK platform; the standards and law referred to in this book are the UK's. Nightlife Culture is not a public body, and where a chapter adopts a public-sector standard (the Code of Practice for Statistics, say) it says that the adoption is voluntary.

The project's own tests for whether it is working are four: can something universally useful be co-designed; does it paint a picture a scene recognises; does it steer decisions and collective action; can it travel to another place and stay useful. Where this book proposes a test of its own, it says which of the four it serves.

## What this book is not

- **Not a programme plan, a task list or a question catalogue.** The project's live priorities and its research questions live elsewhere, under their own IDs. This book schedules nothing and asks only the questions a methodological foundation needs.
- **Not an assessment of the Vibe Map.** It does not judge the prototype; it gives the prototype grounds to judge itself.
- **Not the creative decisions.** The question "how do we make nightlife data as exciting as a club flyer" belongs to Carly and her designers. Chapter 14 sets out where evidence meets expression and stops there.
- **Not the design system.** Colours, type, components and their rules live in the Nightlife Culture Design System (Style Guide v1.5 at the time of writing). This book defers to it for every visual value and logs, chapter by chapter, where it found the system silent or in tension.
- **Not a data contract.** How data is sourced, counted, stored and released is governed by the prototype repository. This book's rules about *showing* gaps, uncertainty and provenance are written to match it, not replace it.
- **Not research into nightlife.** Never. Where a source happens to use a music scene as its example (as Chapter 2's key source does), the chapter quotes it as the source's illustration and goes no further.

## How a chapter teaches

Every chapter answers **one question**, stated in bold near the top, for a reader meeting the subject for the first time. Then, in the same order each time:

| Section | What it does |
|---|---|
| **Before you start** | Who the book is for and the two conventions below, so no chapter assumes you read another |
| **The 60-second version** | The answer and the reasons, in one reading. If you read nothing else, read this |
| **The idea, plainly** | What the thing *is*, with no prior reading assumed |
| **Why people believe what they believe** | The folklore, the convention, the textbook rule — stated fairly before it is tested |
| **The evidence** | What has been measured or evaluated, by whom, how strongly — and where the belief rests on nothing |
| **What holds true regardless** | The canonical part: numbered truths, each with its kind and firmness. Later chapters test them; the last chapter confirms or demotes them |
| **Where the choice is yours** | The open choices, with the trade-offs named |
| **What this means for a nightlife dashboard** | One worked illustration, labelled as such. It fixes nothing about the final design |
| **The rules** | A table. Each rule carries *why*, its *kind*, its *tier* and its *source* |
| **What proves a break works** | The test to run before deviating from a Fixed rule |
| **Checklist** | The build-time list |
| **Open questions and flags** | The loose ends, each with a flag (below) saying where it goes next |
| **Looking back** | Against every earlier chapter: does this one *strengthen*, *weaken*, *counterbalance* or *open a thread*? Nothing earlier is rewritten on the spot; the research log carries the note |
| **Sources** | Every source, with its kind and how it was read |
| **Gaps found** | What the field, the design system or this book could not answer, in four fields |
| **Design system conflict log** | Where the chapter agrees with the style guide, where it conflicts, and where the guide is silent |

The chapters are grouped in five parts (the map is in `00-plan/BRIEF-v2.md` section 6): **Part 0, Foundations** — what a dashboard is for (1), who reads it and what turns their decision (2), the canonical truths of showing data (3). **Part 1, The analytical foundation** — from data to evidence (4), building a measure (5), finding value in the data (6), comparison, time and intervention (7), automation without admin (8). **Part 2, The felt layer** — measuring a vibe (9), safety, ethics and consent (10). **Part 3, The reading experience** — the first screen and the path through it (11), recognising your place (12), accessible as the good version (13). **Part 4, The boundary and the practice** — where evidence meets expression (14), learning from the best (15), breaking these rules well (16).

## The legend: what kind of claim is this, and how firm is it?

Carly asked for two things of every claim in this book: say what kind of thing it is, and say whether it can be crossed. Both are answered on the face of every rule.

### Kind — where the claim comes from

| Kind | Meaning | What you may do with it |
|---|---|---|
| **Standard** | An external rule nobody in this project wrote: a law, a W3C standard, a Treasury manual, a statistical disclosure rule, a UK data-protection requirement. The text says whether it *binds* Nightlife Culture or is *adopted voluntarily*. | Comply, or record why not and get it signed off. A binding standard is never a design choice |
| **Evidence** | A finding from a named study, with its strength stated in plain words: how many people, whether it was replicated, whether it was peer-reviewed, whether it was read in full or at the abstract only (†). | Treat strong evidence as a default you need a reason to leave. Treat contested, single-study or abstract-only evidence as a prompt, not a rule |
| **Reading** | Our interpretation of reference material — a paper, a theory, an exemplar, the Decision Book. It is marked as ours so that you can disagree with it. | Challenge it. If you have a better reading, say why, and the chapter changes |
| **Practice** | A practitioner's framework or craft knowledge, not tested as research: a definition from a working designer, a funder's reporting principles, a placemaking protocol, a price list of social-value proxies. It is often what readers actually use. | Treat it as how a field works, not as proof that the field is right. Where a Practice source conflicts with Evidence, the chapter says so |
| **Nightlife Culture** | A decision, finding or piece of practice from Carly or the studio's published work: the failure register, the co-production theory of vibe, the five-word poster rule, the 78%/32% finding. | Fixed when Carly has said so; otherwise a default the prototype may test |

*Practice* was added after Chapters 1 and 2, which both leaned on practitioner frameworks that fitted none of the other kinds; the original four are unchanged.

### Tier — how firm it is

The book uses the Decision Book's three tiers, and they answer "can this be crossed?" directly:

| Tier | Plain meaning | Breaking it is |
|---|---|---|
| **Fixed** | **A hard line.** There is a right answer and it can be checked: contrast, keyboard access, disclosure thresholds, provenance on every number, no league table of identities, no implied counterfactual. | Negligence. Do not do it for taste |
| **Adaptable** | **A default you may argue with.** There is no single right answer; the book states a position and the reasons. You may take a different one if you can defend it and you log it. | The job. Deviation is expected — with a record |
| **Decorative** | **Free.** Register, imagery, pacing, texture — provided nothing that carries meaning lives only there. | Expected |

Two refinements the chapters use. A truth may be **Fixed as a statement of the record** — the evidence says this and the book will not pretend otherwise — without the design rule that follows from it being Fixed; the chapter says which. And a rule may be **Fixed as sequence**: the order of operations is the hard line (define the construct before the proxy; check recognition before release), while the form each step takes is Adaptable. Where you deviate from a Fixed or Adaptable rule, Chapter 16 gives the four-line record to keep and the test to run first.

### Three marks you will meet

- **†** after a source means the authors' published abstract was read, not the full text. A Fixed rule resting on a † source is flagged `[Further research]` until the full text has been read.
- **"Secondary"** in a sources list means the quotation reached the chapter through another named document, which is cited. It is on the verification list.
- **"At source · spot-checked · verified"** in a sources list says how far a claim has been traced: a research agent opened the link; the orchestrator re-opened it; an independent agent re-traced it. Every chapter goes through all three before it is called a second draft.

### The flags

Loose ends are marked in square brackets so they can be searched across the book:

| Flag | Means |
|---|---|
| `[Further research]` | A thread worth pulling that this chapter did not have room or evidence to finish |
| `[Prototype flag]` | Something the Vibe Map can settle with evidence that no literature can |
| `[Validate with users]` | Something to test in conversation with the three user groups or the scenes |
| `[Revisit → Ch n]` | A question that belongs to a later chapter and is handed to it |
| `[Revisit at end]` | A question to return to once all chapters exist, because its answer depends on them |
| `[Rich reference]` | A source worth your own time, or worth returning to when building |
| `[Counterbalance → Ch n]` | This finding pulls against an earlier chapter's; recorded, not resolved |

### Why the old marks have gone

Version 1 carried marks like **[Measured]**, **[Evaluated]** or **[House steer]** in bold brackets mid-sentence. They were a grading system that was never explained, and they made the text unreadable to anyone outside the project. They are gone. The prose now says in words what kind of claim it is making ("a controlled study of 81 people found…", "our reading is…", "Carly's rule is…"), the rules table carries the kind and the tier, and the sources list says how each source was read. Version 1 also called the Vibe Map "the instrument". It does not any more: the book is about dashboards, and the Vibe Map is one.

## Words this book uses, and what they mean

Plain definitions, in roughly the order you are likely to meet them. Each term is also explained the first time it appears in a chapter. Terms that version 1 coined and that version 2 has not yet reached are marked with the chapter that will take them up.

- **A dashboard** — the book's working definition, from Chapter 1: *a display that turns data into a decision for a named reader.* An argument, not a window. Few's single monitored screen, a layered analytic system, a public health tracker, a council's performance report and the Vibe Map are all dashboards, differing in reader and decision. Power BI is one species of the genus, not the genus.
- **A reader** — whoever the display is for. Chapter 2 names eight kinds and finds that each makes a different decision, is trained to accept different evidence, and keeps a different clock; the same display is graded by all of them at once.
- **A place** — whatever unit a reader is looking at: a city, a neighbourhood, a ward, a scene's territory. Not necessarily a council boundary; the chapters say which, and Chapter 1 shows that the choice of unit changes the answer.
- **A scene** — a community of people who make and attend a kind of night: a genre, a crew, a venue's regulars, a diaspora's nights. Scenes overlap and cross boundaries.
- **The failure register** — Carly's eight ways a dashboard fails: it looks the same every month; it is a fancy spreadsheet; the viewer asks "what am I looking at"; people do not recognise their place; people do not use it; it breaks; people do not trust it; it is an aggregation of the biggest. Chapter 1 reads them against the evidence.
- **Monitoring and evaluation** — the Treasury's distinction, from Chapter 2. Monitoring answers "did we do what we said we would do; how are our success metrics changing over time?"; evaluation answers "did it work, what was the impact, on whom, and why?" A dashboard is monitoring. It can host a comparison; it cannot supply one.
- **Appraisal; the business case; the five cases; social value; the benefit–cost ratio** — the official reader's grammar, explained in Chapter 2 section 3.
- **The counterfactual** — what would have happened without the intervention; the thing every claim of impact needs and no dashboard contains. Chapter 7.
- **An evidence ladder** — a grading of studies by causal design (Maryland, Nesta, the padlocks). A dashboard alone stands on the first or second rung. Chapter 2.
- **WELLBY; wellbeing valuation** — the one official route from how people feel to pounds (£13,000 per one-point change in life satisfaction per person per year, in the 2021 guidance), and the method behind most British "value of culture" headlines. Chapter 2 introduces them; Chapter 5 asks what it takes to use them.
- **Reactivity** — a published measure changes the behaviour it measures. Strathern's and Campbell's laws; Espeland's rankings. Chapter 1.
- **The unit of aggregation; the ecological fallacy; the modifiable areal unit problem** — the same numbers, regrouped, can give any answer; a place-level figure is not a person-level one. Chapter 1.
- **The suppression threshold** — a statistical disclosure rule: small counts are not shown, and a second suppression stops the hidden cell being worked out from the others. Shown as `[c]`, never as a blank. Chapter 1; its ethics in Chapter 10.
- **Six kinds of nothing** — not collected, unknown, zero, free, unavailable, suppressed: kept distinct on screen because they mean different things. The prototype's data contract uses the same six.
- **The heartbeat** — the visible age of a dashboard's data, on every state, so a live container can never look more alive than its stale contents. Chapter 8.
- **A boundary object** — a thing several communities can each use in their own way because it has a shared structure, not a shared meaning. Chapter 1 argues the Vibe Map must be one, and that being one is a social achievement, not a design feature.
- **Member checking; recognition** — taking an account back to the people it is about and asking whether they recognise it. Chapter 2: a test of credibility, not accuracy, and only when the answer can change the account.
- **Issue bias** — the way a choice of what to count decides which questions get asked. Chapter 2; Chapter 10.
- **Numbers for understanding and numbers for advocacy** — the studio's distinction, from Chapter 2: the first are produced with their caveats and released with their data; the second are selected from the first for a room. A sector's dashboard can only be the first kind.
- **Headline-to-caveat decay** — every valuation report carries its hedges; every downstream release drops them; the dashboard is the last place in the chain they can still be shown. Chapter 2.
- **Co-production of vibe** — Carly's principle that a vibe cannot be consumed, only made together; so feeling is *collected with* people, never scraped. Chapter 9.
- **Identity and conditions** — version 1's split, due to return in Chapter 7: a place's cultural identity is never ranked; the *conditions* places give their culture may be compared, with the comparison gated and shown with intervals.
- **The comparability gate** — the design system's rule that any comparison between places states whether the data is actually comparable (same period, same geography, same definition). A comparison without that note is not publishable.
- **Provenance** — where a number came from, for what period, for what geography, by what method. The design system puts a provenance code on every chart; Chapter 1 puts it on the face of the display.
- **The default view; the first screen** — what the dashboard shows before anyone touches it. Chapter 11 (version 1's Chapter 1 and its six landing patterns feed it).
- **The crop test** — screenshot any state; if what travels could be read as a league table of places, the state fails. Version 1; returns in Chapter 7 and Chapter 12.
- **The removal test** — take the interaction, colour, sound or decoration away; if the evidence is still complete, the thing removed was free. Chapter 14 collects every chapter's version.
- **The five-word rule** — Carly's rule from club-poster practice: a headline is five words where possible, ten at most. Chapter 14.
- **The 78%/32% finding** — from Nightlife Culture's ticketing analysis: venues under 1,000 capacity put on 78% of paid events but take 32% of ticketing revenue. The reason aggregates hide the grassroots. Chapter 1's "aggregation of the biggest".
- **The club flyer** — the brief's image of a display that turns information into a decision quickly and with pleasure; the standard the interactive layer is asked to reach. Chapter 1 introduces it; Chapter 2 finds it persuades the persuadable; Chapter 14 is about it.
- **The seven tests** — the design system's checks on any output: committee-room, dancefloor, phone, screen-reader, hostile-reader, partner, paid-work.
- **The gap register** — a four-field note kept whenever the evidence, the design system or this book had no answer: what was missed, what was done instead, the cost of getting it wrong (red, amber, yellow — internal only, never shown publicly), where the rule belongs.
- **The override log** — the four-line record kept whenever a rule is deliberately broken: trigger, rule and tier, alternative chosen, evidence. Chapter 16.
- **A probe** — a small, cheap test designed to settle one open question with real people. Candidates are flagged `[Validate with users]` or `[Prototype flag]` in each chapter and collected in `03-tests/`.
- **The Decision Book** — Nightlife Culture's book on how to make design decisions. This book inherits its method, its decision stack and its tiers and does not re-derive them.
- **The design system / the style guide** — the Nightlife Culture Design System and its Style Guide (v1.5). Owns every visual value.
- **The brief** — `00-plan/BRIEF-v2.md`, which governs this book: the mission in Carly's words, the six questions, what the book never does, the chapter map.
- **The research log** — `01-sources/RESEARCH-LOG.md`, one appended record of what each chapter looked for, found, learned, left out and flagged, with the backward look and what the cold reader and verifier caught.
- **The ledger** — `01-sources/SOURCES.md`, the master list of every source with how it was read and when it was verified.
- **The orchestrator; research agents; the cold reader; the verifier** — the roles the work is split into (`AGENTS.md`): the session Carly talks to, which frames, verifies and writes; parallel agents that research one facet each; an agent with no project context that reads the finished chapter cold; an agent that never found a claim re-tracing it at source.
- **Steer** — Carly's direction on a draft. "Awaiting steer" means she has not read it yet.
- **A commissioner** — whoever pays for and signs off a piece of work: a council, a combined authority, a funder.
- **Ticket Atlas** — Nightlife Culture's scoped ticketing-data method, named in the funding deck as the evidence base the Vibe Map expands.
- **Vibe Setting Framework (VSF)** — an unpublished Nightlife Culture framework from the A Ticket To The Future work. **Confidential.** Cited in this book, never reproduced at length.

## Three things to hold in mind while reading

**The evidence base is thinner than the field admits.** Several of the most-quoted rules in data visualisation have never been tested; the evidence that dashboards change decisions at all is thin everywhere and mixed where it is best; and the field that studies what moves a policy reader knows it mostly from asking them. Where the book finds that, it says so. A rule marked Adaptable with "no study exists" is an honest state, not a weakness.

**Strong design must never make weak evidence look stronger than it is** — the style guide's line — and its twin, which this book adds: strong evidence must never be made to look weaker than it is by timid design. Chapter 2 adds a third: for the reader who arrives already opposed, the handsome chart may read as advocacy and the plain table as evidence.

**Nothing here is finished until it has survived use.** Each chapter is shown to Carly when it is done and is not a gate on the next; her steer, when it comes, is logged and applied. `00-plan/STATE.md` says which chapters she has read.

---

## Sources

- *Artists Make Great Places*, Nightlife Culture, UK Dynamism Fund deck v2.1, September 2026 — the Vibe Map definition, the three user groups, the four tests, the team. **Nightlife Culture.**
- `00-plan/BRIEF-v2.md`, 5 October 2026 — the mission in Carly's words, the failure register, the six questions, the chapter map. **Nightlife Culture.**
- `vibe-map-prototype` repository, `AGENTS.md` and `README.md`, 5 October 2026 — purpose and authority, geographic priority, the evidence and visualisation rules this book's gap vocabulary matches. **Nightlife Culture.**
- The Decision Book — plain language and reading age; the decision stack; tiers, deviation and the override log. **Nightlife Culture; read directly.**
- Nightlife Culture Style Guide v1.5, 5 October 2026 — the seven tests, the evidence rules, the language rules. **Nightlife Culture.**
- ONS Service Manual, *Plain language* — reading age of about nine as a proxy for sentence and clause complexity, preferred by expert readers too. **Evidence; cited through the Decision Book, not re-fetched for this chapter.**
- Chapters 1 and 2 of this book — the working definition; the Practice kind; the † convention; the refinements to the tiers. **Reading.**

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| The design system has no component for a *kind-of-claim* mark (Standard / Evidence / Reading / Practice / Nightlife Culture) | In the markdown the kind is a word in a table column. For the HTML reader, the nearest existing component is the status chip; it will be shown as an option, marked provisional, not invented | Yellow | Design system `docs/gaps.md`, via the dashboard section |
| The design system's interim rule says "never RAG tags" for public severity marks; the book's gap register uses red / amber / yellow | Kept RAG inside the gap register, which is an internal working record; anything that travels in the reader uses words, not coloured severity | Yellow | Chapter 16; design system open decision 12 |
| The original four kinds had no home for practitioner frameworks, on which Chapters 1 and 2 both leaned | Added *Practice* as a fifth kind, defined above; Chapters 1 and 2 already use it | Yellow — closed | — |
| "Fixed" was being used for three things (a rule to obey; a fact the book is confident of; a sequence that is the hard line) and a cold reader of Chapter 2 could not tell which | Named the two refinements above — Fixed as a statement of the record; Fixed as sequence — so that chapters can say which they mean | Amber | Chapter 16's rule register should check every Fixed for which sense it carries |
