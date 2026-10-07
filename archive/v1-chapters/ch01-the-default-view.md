# Chapter 1 — The default view

*Dashboard Design · Part 0: The glance*
*Version 2 · 5 October 2026 · rewritten to travel (see Chapter 0 for the legend); evidence as verified on 16 August 2026 unless stated*

---

## The decision

**What does the instrument say before anyone touches it — and to whom?**

---

## The 60-second version

> The first screen is not where the instrument begins. For most visitors it is the entire product. The New York Times' own analytics found that only 10–15% of readers touch the interaction layer of a graphic at all — so for five in six people, whatever the first screen says is all the instrument will ever say to them.
>
> Three measured findings govern that screen. **Judgement comes before reading**: people form a view of a page's appeal within about 50 milliseconds, and that view rewards low visual complexity and *looking like what the thing claims to be*. **Words carry the message**: eye-tracking and recall studies show that titles and supporting text, not the graphics, decide what people take away. And **a default is read as advice**: across 58 studies and 73,675 participants, a pre-selected option shifts people's choices substantially, partly because they assume the designer is recommending it.
>
> Meanwhile the data-visualisation field's best-known rule for first screens — "overview first, zoom and filter, then details on demand" — turns out to rest on no evidence at all. Its author called it a reminder he kept rediscovering; a systematic review found nobody had ever tested it; the studies that exist say overviews reliably *please* people and unreliably *help* them.
>
> So the decision is editorial, and it cannot be delegated to convention. **The default view is a sentence you are endorsing, addressed to a named person. Write the sentence first, then design the screen that says it.**

---

## How the decision is made

### Step one — accept that the default *is* the product

Gregor Aisch, then on the New York Times graphics desk, published the desk's own finding: readers interact with roughly 10–15% of interactive graphics. His correction of the folklore matters as much as the number — *"the 85% of readers didn't ignore the graphic, they just didn't click the button"* — and his working rule follows from it: *"if some information is crucial, don't make the user click or hover to see it."* This is evidence of the weaker kind — internal analytics reported by the desk's own staff, not a peer-reviewed study — but it is the only published figure of its kind, and nothing since has contradicted it.

Cho and colleagues then showed that the default does more than reach the most people: it steers the few who go further. In a controlled study with 81 participants, the *first view shown* in an interactive tool significantly shaped which views people spent time in afterwards, and figures seen in that first view biased their final estimates even after twenty-five minutes of free exploration. The default is not neutral ground the user departs from. It is the frame they carry with them.

### Step two — write the first sentence before designing the first screen

Borkin and colleagues' eye-tracking and recall study of 393 visualisations is unambiguous: *"titles and supporting text should convey the message of a visualization."* Text dominates both where people look and what they can later report. The Office for National Statistics (ONS) rebuilt its house style on the same finding, requiring every chart title to *"sum up the main message shown in the chart in 10 words or less"*; its reason was internal telemetry showing that its bulletins take 9.5 times longer to read than anyone spends on the page. That is practice guidance backed by unpublished numbers — weaker than a study, stronger than opinion.

Nightlife Culture already runs tighter. Carly's rule from club-poster practice is **five words where possible, ten at most**, and a poster is the harder test — read at walking pace, at night, in competition with every other poster on the wall. Where the two rules disagree, the poster wins. (A Nightlife Culture rule; Fixed.)

The audit of live instruments sharpened this into a rule about *whose* sentence it is. The strongest first screens put **a question in the visitor's own voice** at the top: the BBC's *"are hospital waiting times improving near you?"*, the Thriving Places Index's *"Does your place support people and planet to thrive?"* The weakest lead with the institution describing itself: *"London's first Cultural Infrastructure Map brings together new research…"*; *"The Creative Footprint is a non-profit initiative that measures and indexes live music space."* The visitor's question and the institution's self-description compete for the same line, and only one of them is about the reader.

### Step three — choose the landing pattern deliberately

The audit of ten live instruments (listed in the sources) found six distinct patterns for what a first screen does. None is neutral; each assumes a particular visitor.

| Pattern | Who uses it | What it assumes about the visitor | Where it fails |
|---|---|---|---|
| **Message-first** — a prose argument, data deferred | OECD Better Life Index; Creative Footprint | Must be persuaded the question matters | The data recedes into brochure. Creative Footprint's only results sit behind a form |
| **Input-first** — blank until you say where you are | ONS Explore Local Statistics | Arrives with a place in mind | The empty state proves nothing is worth typing for |
| **Message-then-input** — stakes first, then the postcode box | BBC postcode interactives | Needs the national story before wanting the local one | Costs four paragraphs before anything is theirs |
| **Select-first** — an instrument panel awaiting a dropdown | Thriving Places Index | A professional who knows which authority they manage | A citizen sees controls, not meaning; the score exists only after labour |
| **Exemplar-first** — one concrete case carries the dataset | The Pudding (*"This is a teenager… we'll call him Alex"*); Our World in Data's world-plus-continents default | Has no question yet and must be given a protagonist | The exemplar's framing is authorial and, on the anchoring evidence, sticky |
| **Map-first** — everything plotted, filter to focus | Greater London Authority Cultural Infrastructure Map | A browser who reads density before value | Says "this exists, everywhere" but never "so what"; staleness is invisible on a pin |

One cross-cutting observation from the audit: **none of the ten instruments asks for configuration at arrival.** The slider-first era — the early OECD "flower" that asked you to weight eleven dimensions before it would show you anything — appears to be over, and the OECD's current landing page has retreated all the way to prose and PDF downloads. The failure at both extremes is the same: a first screen that asks for work before it gives meaning.

### Step four — treat the default as an endorsement, because the reader does

This is the strongest evidence in the chapter. Jachimowicz and colleagues' meta-analysis — 58 datasets, 73,675 participants — puts the default effect at **d = 0.68** (95% confidence interval 0.53–0.83), which in a yes-or-no choice is an average shift of 27 percentage points toward the pre-selected option. The *mechanism* matters more than the size: *"individuals commonly perceive defaults as conveying an endorsement by the choice architect."* We read this paper at source and checked the figures.

Hullman and Diakopoulos named the same thing from the design side a decade earlier: *"default views provide an initial point of interpretation anchored to the default visual configuration."* Their example was the New York Times opening a national map *"zoomed-out… of all of New York City (the largest US city and presumed home of the default New York Times user)."* This is a named concept with worked examples, not a measurement.

Read together: whatever place, measure, comparison and time period the instrument shows first will be received as *what its maker thinks matters*. There is no configuration of the first screen that avoids this. The only choice is whether the endorsement is deliberate.

**And the absence is a finding.** No study appears to exist that measures whether users of an interactive visualisation ever change its defaults — the default filter, extent or sort — at what rate, or with what consequence. Behavioural economics has a precise effect size for defaults in decisions; visualisation has one anchoring experiment and a newsroom's internal telemetry. Nobody has run the defaults meta-analysis for dashboards. It is logged in the gaps below, and it is one of the cheapest probes the Vibe Map could run on itself.

### Step five — design for the glance you will be judged in

Visual appeal stabilises within 50 milliseconds of seeing a page (Lindgaard and colleagues), and Tuch and colleagues isolated what drives that snap judgement: **low visual complexity and high prototypicality** — the degree to which a thing looks like what it claims to be — with both effects detectable at 17 milliseconds. One scope caveat belongs beside this every time it is quoted: what stabilises in 50 milliseconds is *appeal*, not comprehension. The popular line "users judge your site in 50 ms" is an extrapolation from a narrower finding.

Glance cost also varies by chart form by roughly an order of magnitude. In Blascheck and colleagues' study, a simple comparison took about 200–285 milliseconds to read from a bar or donut chart and about 1,500–1,800 from a radial bar — measured at smartwatch scale, so the absolute numbers will differ on a phone or a laptop, but the ranking is the useful part. A default view built from slow-glance forms spends its 50 milliseconds losing.

**Where the prototypicality finding meets this project.** The first draft of this chapter said the finding "collides with the brief's demand not to look like the genre". That was wrong in one respect, and Carly caught it: the brief contains no such rule. The demand that the instrument not look like *"a government boring thing"* comes from Carly's own instruction (the Skiddle call) and from the project's opening prompt (*"explicitly not Power BI"*). It is a Nightlife Culture steer, not a brief-level rule, and it is Adaptable unless Carly fixes it. The apparent collision then softens: prototypicality rewards looking like what you *claim* to be, and this instrument's claim is nightlife's evidence, so the visual tradition to resemble is nightlife's own — the poster, the flyer, the lineup — not the dashboard genre's. Chapter 13 makes that argument in full; it is our *reading* of the evidence, open to challenge. The only rule this chapter contributes is narrower: the register has to be legible in the first glance, because there is no second one.

### Step six — hold "overview first" as a preference, not a law

Ben Shneiderman's mantra — *"Overview first, zoom and filter, then details-on-demand"* — is the most-cited rule in the field, and its evidential status is now clear. Shneiderman himself wrote: *"Each line represents one project in which I found myself rediscovering this principle and therefore wrote it down as a reminder."* Craft and Cairns audited the literature citing it and found, in their words, *"although numerous authors cite the Mantra, there are no reasonably obvious studies that have validated Shneiderman's recommendations"* — 52 citations, zero validations — concluding that it *"appears to act as an inspiration and guideline for practitioners rather than a scientifically studied methodological approach."* We read this at source.

Hornbæk and Hertzum's review of 23 empirical comparisons found the only near-unanimous benefit of an overview is that people *like* having one; task time improved in about half the comparisons, and on errors only 2 of 17 favoured the overview. And van Ham and Perer's counter-mantra — *"search, show context, expand on demand"* — argues that a large class of users *"are not interested in global patterns… they are trying to learn something more about a particular datapoint."* Their evidence is a single case study, by their own admission.

So neither overview-first nor detail-first is settled. What the evidence does support is narrower and more useful: **satisfaction favours an overview; the task decides the rest.** A visitor who arrives with a place in their pocket is van Ham and Perer's user, not Shneiderman's.

---

## The rules

*Kind and tier are explained in Chapter 0. Fixed is a hard line; Adaptable is a stated default you may argue with and log; Decorative is free.*

| Rule | Why | Kind | Tier | Source |
|---|---|---|---|---|
| The default view answers its question without any interaction | 10–15% of readers touch the interaction layer; crucial information never sits behind a click or hover | Evidence | **Fixed** | Aisch, NYT analytics; carried from Decision Book Ch 15 |
| Write the default view's sentence before designing its screen | Titles and text dominate attention and recall; the message is carried in words | Evidence | **Fixed** | Borkin et al. 2015; ONS house style |
| The first line is the visitor's question, not the institution's description | The audit's strongest openings address the reader; the weakest describe the maker | Reading | **Fixed** | Display audit, ten instruments |
| Headlines at poster discipline: five words where possible, ten at most | A poster is read at walking pace, at night, in competition; it out-toughens the ONS ten-word rule | Nightlife Culture | **Fixed** | Carly's club-poster rule |
| Name the landing pattern, in writing, from the six | Each pattern assumes a visitor; an unchosen pattern is still a choice, made by accident | Reading | **Fixed** | Display audit |
| Treat every element of the default state as an endorsed recommendation | Defaults shift choices at d = 0.68 partly *because* they read as the architect's advice | Evidence | **Fixed** | Jachimowicz et al. 2019, read at source |
| The initially shown view is assumed to anchor all subsequent exploration | Measured: first-view configuration biased process and outcomes through 25 minutes of free use | Evidence | **Fixed** | Cho et al. 2017 |
| No configuration demands before meaning | None of ten audited instruments pushes weighting at arrival; the era ended for a reason | Reading | **Fixed** | Display audit |
| Build the first screen from fast-glance forms | Glance cost varies about eightfold by chart form; appeal is judged in 50 ms on simplicity | Evidence | **Fixed** | Blascheck et al.; Tuch et al. |
| Freshness and provenance are first-screen furniture, not footer matter | Instruments that surface dates read as alive; stale content behind a live container is invisible from the front page. The scene asks for the same thing independently: a map not *"actively maintained and ethically governed… risks becoming outdated or extractive as soon as it is published"* | Reading + Nightlife Culture | **Fixed** | Display audit; Our World in Data pattern; Vibe Setting Framework, *Seeing the System* (unpublished — confidential) |
| Treat "overview first" as a satisfaction preference, not a performance law | 52 citations, zero validations; overviews please reliably, help unreliably | Evidence | Adaptable | Craft & Cairns, read at source; Hornbæk & Hertzum |
| Choose overview-first or detail-first by the visitor's arriving question | A visitor with a place in mind is the search-first user | Reading | Adaptable | van Ham & Perer |
| An empty input state must show what the answer will look like | The cost of an empty state has never been measured, but every craft source warns the same way | Reading (craft advice, no study) | Adaptable | Nielsen Norman Group |
| The instrument's first-glance register should read as nightlife's, not a government dashboard's | A Nightlife Culture steer, not a brief rule; the prototypicality evidence is compatible with it once the claim is named | Nightlife Culture | Adaptable | Carly, Skiddle call; Chapter 13 |
| The register of the first glance — imagery, colour, tone | Free within the design system's rules; this is where "looks like art" lives | — | *Decorative* | Style Guide v1.5; Chapter 13 |

---

## Worked example

*Illustrative. This applies the chapter to the Vibe Map to show the decision being made; it fixes nothing about the eventual design.*

**The brief.** "Measure your area at a click." The funding deck's promise: what systems count and what culture holds, on one screen, for someone who currently waits months for a team to assemble it.

**Step one — the sentence.** Before any layout: what does the default view say, and to whom? The brief's own phrase contains the answer — *your area* — so the honest default sentence is something like: *"Here is what [place]'s nightlife culture holds — and here is how little of it the official picture counts."* That sentence cannot be rendered until the instrument knows the place.

**Step two — so the pattern question becomes real.** Pure input-first (the ONS pattern) shows a search box and proves nothing — the empty state asks for work before giving meaning. Pure exemplar-first (the Pudding pattern) opens on one place in full authorial voice — but the anchoring evidence says the exemplar place will frame every place viewed after it, and a Bristol-first default quietly tells every other city this is Bristol's instrument. Map-first says "this culture exists, everywhere" — the abundance message, which is the advocacy point — but the audit's finding stands: an all-pins map answers "how much, where" and never "so what", and staleness is invisible on a pin.

**Step three — the decision this chapter's evidence supports.** A **message-then-input** opening (the BBC's hybrid), where the message is carried by an exemplar rendered honestly: one screen that shows a real place's two columns — counted and missed — as the proof of what typing your own postcode will get you, followed immediately by the input. The exemplar place should rotate, or be chosen deliberately *as an endorsement*, because it will be read as one either way. Since October 2026 the project's declared first place is Bristol; if Bristol is the exemplar, that is now a deliberate endorsement rather than an accidental one, and the screen should say so in a word. Freshness sits on the first screen, per the rule — the anti-observatory move: the instrument's first screen shows the age of its own data, so the container can never look more alive than its contents.

**What was rejected, and why it is recorded.** Select-first was rejected on the audit's evidence: a dropdown-first panel serves the professional who already knows their authority and loses everyone else, and this project's three user groups include advocates and funders, not only officers. The rejection is logged so it does not get re-argued at 11pm.

---

## Pressure points

**Where there is real latitude.**

*The exemplar's voice.* Exemplar-first is the most authored pattern and the most alive — *"we'll call him Alex"* is the strongest opening in the audit. A Vibe Map equivalent (*"It's 11pm on Stokes Croft…"*) is available, powerful, and entirely a craft decision. The constraint is only that the anchor is chosen knowingly.

*The question-headline.* "What does your city sound like?" is already the project's user-facing question, in the visitor's voice, and it is better than anything in the audit. The evidence says put it first.

*Everything decorative.* Register, imagery, motion at the threshold of the first glance — free, within the design system, and this is precisely where "make it look like art" lives without touching a Fixed rule.

**Where it looks sophisticated and fails.**

*The instrument panel.* Controls before meaning reads as rigour and is the select-first failure: the score exists only after labour, and the citizen leaves before performing any.

*The links hub.* A taxonomy of elsewhere. The audit's example communicates nothing about the night itself on arrival — no number, no picture, a promissory note for a product.

*The brochure.* Message-first without an exemplar decays into the institution describing itself above a download button. The audit caught a famous instrument mid-decay.

*The all-pins map with no sentence.* Abundance without argument. Every pin equal means no pin argued for.

**What proves a break works — the five-second test.** Show the default view, untouched, to someone from one of the three user groups for five seconds, then take it away and ask what it said and who it was for. If they answer with the sentence you wrote in step two, the default is working. If they answer with a description of the interface, it is not. Then check the other 85%: is everything crucial visible without a single click? This test serves the project's second question — *does it paint a recognisable picture?* — and belongs in the probe programme.

---

## Checklist

- [ ] The default view's sentence is written, before layout
- [ ] It is addressed to a named visitor, in their voice, not the institution's
- [ ] The headline is at poster discipline
- [ ] The landing pattern is chosen from the six, in writing, with the rejected ones logged
- [ ] Everything crucial is visible without click or hover
- [ ] The default place, measure, comparison and period are chosen *as endorsements*, and the exemplar place is named as a choice
- [ ] No configuration is demanded before meaning is given
- [ ] The first screen is built from fast-glance forms
- [ ] Freshness and provenance are on the first screen
- [ ] Any input state shows what the answer will look like before asking for input
- [ ] The five-second test has been run with someone from each user group
- [ ] Overview-versus-detail chosen from the visitor's arriving question, not from the mantra

---

## Sources

*Each entry says what kind of source it is and whether we read it at the link. "Read at source, 16 Aug 2026" means a person opened the link on that date and checked the figures quoted. Anything else is marked.*

- [Aisch, *In defense of interactive graphics*](http://www.vis4.net/blog/in-defense-of-interactive-graphics/) — Evidence (internal analytics, not peer-reviewed); read at source, 16 Aug 2026. The 10–15% figure, its correction, and "if some information is crucial, don't make the user click or hover to see it."
- [Borkin et al., *Beyond Memorability*, IEEE TVCG 2015](https://vcg.seas.harvard.edu/publications/20150101-beyond-memorability-visualization-recognition-and-recall) — Evidence (393 visualisations, eye-tracking and recall); read at source, 16 Aug 2026. Titles and text carry the message.
- [ONS Digital, *Say what you see*, 2019](https://digitalblog.ons.gov.uk/2019/01/28/say-what-you-see-the-way-we-write-chart-titles-is-changing) — Standard (ONS house style, adopted voluntarily here) backed by unpublished telemetry; read at source, 16 Aug 2026. Ten-word message titles; the 9.5× figure.
- [Jachimowicz et al., *When and why defaults influence decisions*, Behavioural Public Policy 2019](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/67AF6972CFB52698A60B6BD94B70C2C0/S2398063X1800043Xa.pdf/when-and-why-defaults-influence-decisions-a-meta-analysis-of-default-effects.pdf) — Evidence (meta-analysis, 58 datasets, 73,675 participants); read at source and figures checked, 16 Aug 2026. d = 0.68 [0.53–0.83]; 27.24 points; the endorsement mechanism quoted.
- [Cho et al., *Anchoring effects in visual analytics*, IEEE VAST 2017](https://webpages.charlotte.edu/~wdou1/publications/2017/Anchoring_bias_VAST17.pdf) — Evidence (controlled study, 81 participants); read at source, 16 Aug 2026. The initially shown view biases process and outcome.
- [Hullman & Diakopoulos, *Visualization Rhetoric*, IEEE InfoVis 2011](https://users.eecs.northwestern.edu/~jhullman/vis_rhetoric.pdf) — Reading of a conceptual paper (no measurement); read at source, 16 Aug 2026. Default views as anchored interpretation; the Mapping America example.
- [Shneiderman, *The Eyes Have It*, 1996](https://hci.stanford.edu/courses/cs448b/papers/shneiderman96eyes.pdf) — the mantra's wording and its author's own account of its origin; read at source, 16 Aug 2026.
- [Craft & Cairns, *Beyond Guidelines*, 2005](https://faculty.cc.gatech.edu/~john.stasko/8001/craft05.pdf) — Evidence (systematic review of citing literature); read at source and quotations checked, 16 Aug 2026. 52 citations, no validations.
- [Hornbæk & Hertzum, *The notion of overview in information visualization*, IJHCS 2011](http://mortenhertzum.dk/publ/IJHCS2011.pdf) — Evidence (review of 23 comparisons); read at source, 16 Aug 2026. Satisfaction yes, performance unproven.
- [van Ham & Perer, *Search, Show Context, Expand on Demand*, IEEE InfoVis 2009](https://perer.org/papers/adamPerer-DOIGraphs-InfoVis2009.pdf) — Reading of a single case study; read at source, 16 Aug 2026. The counter-mantra.
- [Lindgaard et al., *Attention web designers: you have 50 milliseconds*, Behaviour & Information Technology 2006](https://www.tandfonline.com/doi/abs/10.1080/01449290500330448) — Evidence (abstract read; full paper paywalled). Appeal stabilises at 50 ms.
- [Tuch et al., *The role of visual complexity and prototypicality*, IJHCS 2012](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38315.pdf) — Evidence; read at source, 16 Aug 2026. Simplicity and prototypicality drive the snap judgement, at 17 ms.
- [Blascheck et al., *Glanceable Visualization*, IEEE InfoVis 2018](https://www.microsoft.com/en-us/research/wp-content/uploads/2018/08/GlanceableVis-InfoVis2018.pdf) — Evidence (smartwatch scale); read at source, 16 Aug 2026. Glance cost by chart form.
- [Nielsen Norman Group, *Designing Empty States*](https://www.nngroup.com/articles/empty-state-interface-design/) — craft advice citing no studies; read at source, 16 Aug 2026.
- The display audit of ten live instruments, 16 Aug 2026, this project (`02-research-notes/ch01-display-audit.md`): OECD Better Life Index · ONS Explore Local Statistics · Thriving Places Index · Our World in Data · The Pudding · Creative Footprint · London Night Time Data Observatory · GLA Cultural Infrastructure Map · Gapminder · BBC NHS tracker. Landing states quoted from the live pages on that date, **except Gapminder**, whose tools page could not be loaded; its entry is inferred and carries no rule. These sources were read for *how they display*, never for what they say about nightlife.
- Nightlife Culture: Carly's club-poster rule (five words); the Skiddle-call instruction; the Vibe Setting Framework's *Seeing the System* community requirements (confidential — cited, not reproduced).

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No study exists on whether users of interactive visualisations change defaults — rate, consequence, anything. The defaults meta-analysis has never been run for dashboards | Carried the behavioural-economics effect size with its scope stated | Amber — the Vibe Map could measure this cheaply on itself | Ch 8; probe programme `03-tests/` |
| The cost of an empty state is entirely unquantified; the whole literature is craft advice | Marked every empty-state claim as craft advice, no study | Yellow | Ch 8 |
| **Corrected in this version.** The first draft claimed the brief forbade looking like the dashboard genre; the brief says no such thing — the steer is Carly's | Re-labelled it a Nightlife Culture steer, Adaptable; Chapter 13's resolution stands as a reading | Yellow — a provenance error, caught by Carly | Closed here; Ch 13 to match |
| Gapminder's default state could not be observed; it is inferred | Marked inferred; excluded from any rule. Carly has offered to observe it: open the tool, screenshot the first screen untouched, note chart, indicators, year, autoplay | Yellow | Ch 12 gallery; close when observed |

## Design system (Style Guide v1.5) — conflict log

**Agrees.** The guide's "frontload the point" is this chapter's step two at editorial scale. Its rule that every chart carries provenance extends naturally to the first screen; the chapter strengthens it to first-screen furniture. The seven tests' phone test is the five-second test's cousin.

**Conflicts.** None found. (v1.5's "no H5 or H6" and "one rule for all type" affect the reader's rendering, not this chapter's content.)

**Silent on.** Landing patterns; empty states; the default-as-endorsement principle; what the guide's slide and document rules imply for a *screen* that is neither. The last of these recurs every chapter and may eventually be the design system's dashboard section — a conversation for the design system, not this book.

---

## What changed in version 2 — the journey, kept

So that a reader can see how the chapter got here rather than only where it landed:

- The bracketed status marks (**[Measured]**, **[Evaluated]**, *practice-lore*) are gone; each claim now says in words what kind it is and how strong. The rules table gained a *Kind* column. See Chapter 0.
- The prototypicality "collision with the brief" was a provenance error and is corrected in step five and the gap log.
- The cross-reference for the art question now points to Chapter 13 (the chapter numbers moved when Discovery was inserted as Chapter 7 in August).
- "Carly's club-poster mantra" became an explicit rule row, since it was already doing a rule's work.
- The worked example notes that Bristol is now the project's declared first place, which turns an accidental endorsement into a deliberate one.
- The five-second test is tied to the project's three user groups and to its second discovery question.
- Gapminder's inference is scoped, and Carly's offer to observe it is recorded.
- Nothing in the evidence, the six patterns or the Fixed rules changed.
