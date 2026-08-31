# Chapter 1 — The default view

*Dashboard Design · Part 0: The glance*
*Draft for steer · 16 August 2026 · sources verified at URL on this date*

---

## The decision

**What does the instrument say before anyone touches it — and to whom?**

---

## The 60-second version

> The default view is not a starting point for interaction. For most visitors it is the entire
> product: the New York Times' own analytics found only 10–15% of readers touch the interaction
> layer at all. So the first screen is not where the instrument begins — it is where, for five in
> six people, it ends.
>
> Three measured facts govern it. **Judgment precedes reading**: visual appeal stabilises within
> 50 milliseconds, and it rewards low complexity and looking like what the thing claims to be.
> **Text carries the message**: eye-tracking and recall studies show titles and supporting words —
> not the graphics — dominate what people take away. And **defaults are read as advice**: across
> 58 datasets and 73,675 participants, pre-selected options shift choices by d = 0.68, partly
> because people treat the default as the designer's recommendation.
>
> Meanwhile the visualisation field's own rule — "overview first, zoom and filter, then
> details-on-demand" — turns out to be doctrine, not evidence. Its author called it a reminder he
> kept rediscovering; a systematic review found nobody had ever validated it; the best available
> evidence says overviews reliably *please* and unreliably *help*.
>
> So the decision is editorial, and it cannot be delegated to convention: **the default view is a
> sentence you are endorsing, addressed to a named person. Write the sentence first.**

---

## How the decision is made

### Step one — accept that the default is the product

Gregor Aisch, then of the New York Times graphics desk, published the desk's own finding: readers
interact with roughly 10–15% of graphics, and his correction of the lore matters as much as the
number — *"the 85% of readers didn't ignore the graphic, they just didn't click the button."* His
operative rule follows directly: *"if some information is crucial, don't make the user click or
hover to see it."* **[Measured — internal analytics, reported by its own staff, not peer-reviewed.]**

Cho and colleagues then showed the default does more than reach the most people — it steers the
few who go further. In a controlled study (81 participants), the *initially shown view* of an
interactive tool significantly shaped which views users spent time in afterwards, and anchors in
the first view biased final estimates despite twenty-five minutes of free exploration.
**[Measured.]** The default is not neutral ground the user departs from. It is the frame they
carry with them.

### Step two — write the first sentence before designing the first screen

Borkin and colleagues' eye-tracking and recall work across 393 visualisations is unambiguous:
*"titles and supporting text should convey the message of a visualization"* — text dominates both
where people look and what they can later report. **[Measured.]** The Office for National
Statistics rebuilt its house style on the same finding, requiring chart titles to *"sum up the main
message shown in the chart in 10 words or less"*, on the strength of internal telemetry showing
its bulletins take 9.5 times longer to read than anyone actually spends on the page.
**[Practice guidance backed by unpublished telemetry.]** The house already runs tighter: Carly's
club-poster mantra is **five words or less**, and a poster is the harder test — read at walking
pace, at night, in competition. Where the two rules disagree, the poster wins.

The audit of live instruments sharpened this into a split worth stating as a rule. The strongest
first screens put **a question in the visitor's voice** at the top: the BBC's *"are hospital
waiting times improving near you?"*, the Thriving Places Index's *"Does your place support people
and planet to thrive?"* The weakest lead with the institution describing itself: *"London's first
Cultural Infrastructure Map brings together new research…"*, *"The Creative Footprint is a
non-profit initiative that measures and indexes live music space."* The visitor's question and the
institution's self-description compete for the same line, and only one of them is about the reader.

### Step three — choose the landing pattern deliberately

The audit of ten live instruments found six distinct patterns for what a first screen does. None
is neutral; each assumes a visitor.

| Pattern | Who uses it | What it assumes | Where it fails |
|---|---|---|---|
| **Message-first** — a prose argument, data deferred | OECD Better Life Index, Creative Footprint | The visitor must be persuaded the question matters | The data recedes into brochure. Creative Footprint's only results sit behind a form |
| **Input-first** — blank until you say where you are | ONS Explore Local Statistics | The visitor arrives with a place in mind | The empty state proves nothing is worth typing for |
| **Message-then-input** — stakes first, then the postcode box | BBC postcode interactives | The visitor needs the national story before wanting the local one | Costs four paragraphs before anything is theirs |
| **Select-first** — an instrument panel awaiting a dropdown | Thriving Places Index | A professional who knows which authority they manage | A citizen sees controls, not meaning; the score exists only after labour |
| **Exemplar-first** — one concrete case carries the dataset | The Pudding ("This is a teenager… we'll call him Alex"); Our World in Data's World-plus-continents default | The visitor has no question yet and must be given a protagonist | The exemplar's framing is authorial and, per the anchoring evidence, sticky |
| **Map-first** — everything plotted, filter to focus | GLA Cultural Infrastructure Map | A browser who reads density before value | Says "this exists, everywhere" but never "so what"; staleness is invisible on a pin |

One cross-cutting observation from the audit: **none of the ten instruments pushes configuration
at arrival.** The slider-first era — the early OECD flower asking you to weight eleven dimensions
before showing you anything — appears to be over, and the OECD's own current landing page has
retreated all the way to prose and PDF downloads. The failure at both extremes is the same
failure: a first screen that asks for work before giving meaning.

### Step four — treat the default as an endorsement, because the reader does

The behavioural evidence is the strongest in this chapter. Jachimowicz and colleagues'
meta-analysis — 58 datasets, 73,675 participants — puts the default effect at **d = 0.68 (95%
confidence interval 0.53–0.83)**, a 27.24 percentage-point average shift toward the pre-selected
option in binary choices. And the mechanism matters more than the size: *"individuals commonly
perceive defaults as conveying an endorsement by the choice architect."* **[Measured, verified at
source.]**

Hullman and Diakopoulos named the same thing from the design side a decade earlier: *"default
views provide an initial point of interpretation anchored to the default visual configuration"* —
their example being the New York Times opening a national map *"zoomed-out… of all of New York
City (the largest US city and presumed home of the default New York Times user)."*
**[Evaluated — a named concept with worked examples, no measurement.]**

Read together: whatever place, measure, comparison and time period the instrument shows first
will be received as *what its maker thinks matters*. There is no configuration of the first
screen that avoids this. The only choice is whether the endorsement is deliberate.

**And the absence is a finding.** No study appears to exist measuring whether end users of an
interactive visualisation ever change its defaults — default filters, default extents, default
sorts — at what rate, or with what consequence. Behavioural economics has a precise effect size
for defaults in decisions; visualisation has one anchoring experiment and a newsroom's internal
telemetry. Nobody has run the defaults meta-analysis for dashboards. Logged below.

### Step five — design for the glance you will be judged in

Visual appeal stabilises within 50 milliseconds of exposure (Lindgaard and colleagues), and Tuch
and colleagues isolated what drives it: **low visual complexity and high prototypicality** — the
degree to which the thing looks like what it claims to be — with both effects detectable at 17
milliseconds. **[Measured. Scope caveat: what stabilises is *appeal*, not comprehension — the
popular "users judge your site in 50ms" is an extrapolation.]**

Glance cost also varies by chart form by roughly an order of magnitude: in Blascheck and
colleagues' study, a simple comparison took ~200–285 milliseconds from a bar or donut chart and
~1,500–1,800 from a radial bar. **[Measured, at smartwatch scale.]** A default view built from
slow-glance forms is spending its 50 milliseconds losing.

For this instrument the prototypicality finding cuts interestingly: the brief demands it *not*
look like "a government boring thing" — but the measured aesthetic reward is for looking like
what you claim to be. The resolution is that the claim is nightlife's, so the prototype to match
is the culture's own visual language, not the dashboard genre's. That is Chapter 12's territory;
the rule this chapter contributes is only that the register must be legible in the first glance,
because there is no second one.

### Step six — hold "overview first" as a preference, not a law

Shneiderman's mantra — *"Overview first, zoom and filter, then details-on-demand"* — is the most
cited rule in the field, and its evidential status is now clear. Shneiderman himself: *"Each line
represents one project in which I found myself rediscovering this principle and therefore wrote it
down as a reminder."* Craft and Cairns audited the citing literature and found, verbatim,
*"although numerous authors cite the Mantra, there are no reasonably obvious studies that have
validated Shneiderman's recommendations"* — 52 citations, zero validations — concluding it
*"appears to act as an inspiration and guideline for practitioners rather than a scientifically
studied methodological approach."* **[Evaluated, verified at source.]**

Hornbæk and Hertzum's review of 23 empirical comparisons found the only near-unanimous benefit of
overviews is that people *like* them; task time improved in about half the comparisons, and on
errors only 2 of 17 favoured the overview. **[Measured — counts across studies.]** And van Ham and
Perer's counter-mantra — *"search, show context, expand on demand"* — argues a large class of
users *"are not interested in global patterns… they are trying to learn something more about a
particular datapoint."* **[Evaluated — case study only, by its authors' own admission.]**

So neither overview-first nor detail-first is settled. What the evidence does support is
narrower and more useful: **satisfaction favours an overview; the task decides the rest.** A
visitor who arrives with a place in their pocket is van Ham and Perer's user, not Shneiderman's.

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| The default view answers its question without any interaction | 10–15% of readers touch the interaction layer; crucial information never sits behind a click or hover | **Fixed** | Aisch, NYT analytics; carried from Decision Book Ch 15 |
| Write the default view's sentence before designing its screen | Titles and text dominate attention and recall; the message is carried in words | **Fixed** | Borkin et al. 2015; ONS house style |
| The first line is the visitor's question, not the institution's description | The audit's strongest openings address the reader; the weakest describe the maker | **Fixed** | Display audit, 10 instruments |
| Name the landing pattern, in writing, from the six | Each pattern assumes a visitor; an unchosen pattern is still a choice, made by accident | **Fixed** | Display audit |
| Treat every element of the default state as an endorsed recommendation | Defaults shift choices at d = 0.68 partly *because* they read as the architect's advice | **Fixed** | Jachimowicz et al. 2019, verified |
| The initially shown view is assumed to anchor all subsequent exploration | Measured: first-view configuration biased process and outcomes through 25 minutes of free use | **Fixed** | Cho et al. 2017 |
| No configuration demands before meaning | None of ten audited instruments pushes weighting at arrival; the era ended for a reason | **Fixed** | Display audit |
| Build the first screen from fast-glance forms | Glance cost varies ~8× by chart form; appeal is judged in ≤50ms on simplicity | **Fixed** | Blascheck et al.; Tuch et al. |
| Freshness and provenance are first-screen furniture, not footer matter | The audit splits cleanly: instruments that surface dates read as alive; stale content behind a live container is invisible from the front page. The scene requires the same thing independently: a map not "actively maintained and ethically governed… risks becoming outdated or extractive as soon as it is published" | **Fixed** | Display audit; Our World in Data pattern; Vibe Setting Framework, *Seeing the System* (unpublished — confidential) |
| Treat "overview first" as a satisfaction preference, not a performance law | 52 citations, zero validations; overviews please reliably, help unreliably | Adaptable | Craft & Cairns, verified; Hornbæk & Hertzum |
| Choose overview-first or detail-first by the visitor's arriving question | A visitor with a place in mind is the search-first user | Adaptable | van Ham & Perer |
| An empty input state must show what the answer will look like | The empty-state cost is unquantified but every craft source warns the same way | Adaptable | Nielsen Norman Group; practice-lore, marked as such |
| The register of the first glance — imagery, colour, tone | Free, within the style guide's rules; this is where "looks like nightlife's, not government's" lives | *Decorative* | Style Guide v1.4; Ch 12 |

---

## Worked example

*Illustrative. This applies the chapter to the vibe-map brief to show the decision being made; it
fixes nothing about the eventual design.*

**The brief.** "Measure your area at a click." The deck's promise: what systems count and what
culture holds, on one screen, for someone who currently waits months for a team to assemble it.

**Step one — the sentence.** Before any layout: what does the default view say, and to whom? The
brief's own phrase contains the answer — *your area* — which means the honest default sentence is
something like: *"Here is what [place]'s nightlife culture holds — and here is how little of it
the official picture counts."* That sentence cannot be rendered until the instrument knows the
place.

**Step two — so the pattern question becomes real.** Pure input-first (the ONS pattern) shows a
search box and proves nothing — the empty state asks for work before giving meaning. Pure
exemplar-first (the Pudding pattern) opens on one place with full authorial voice — but the
anchoring evidence says the exemplar place will frame every place viewed after it, and a
Bristol-first default quietly tells every other city this is Bristol's instrument. Map-first says
"this culture exists, everywhere" — the abundance message, which is genuinely the advocacy point —
but the audit's finding stands: an all-pins map answers "how much, where" and never "so what," and
staleness is invisible on a pin.

**Step three — the decision this chapter's evidence supports.** A **message-then-input** opening
(the BBC's hybrid), where the message is carried by an exemplar rendered honestly: one screen that
shows a real place's two columns — counted and missed — as the proof of what typing your own
postcode will get you, followed immediately by the input. The exemplar place should rotate or be
chosen deliberately *as an endorsement*, because it will be read as one either way. Freshness
sits on the first screen, per rule — this is also the anti-observatory move: the instrument's
first screen shows the age of its own data, so the container can never look more alive than its
contents.

**What was rejected, and why it's recorded.** Select-first was rejected on the audit's evidence —
a dropdown-first Power BI panel serves the professional who already knows their authority and
loses everyone else, and this instrument's brief names advocates and the scene, not only officers.
The rejection is logged so it does not get re-argued at 11pm.

---

## Pressure points

**Where there is real latitude.**

*The exemplar's voice.* Exemplar-first is the most authored pattern and the most alive — "we'll
call him Alex" is the strongest opening in the audit. A vibe-map equivalent ("It's 11pm on
Stokes Croft…") is available, powerful, and entirely a craft decision. The constraint is only
that the anchor is chosen knowingly.

*The question-headline.* "What does your city sound like?" is already the project's user-facing
question, in the visitor's voice, and it is better than anything in the audit. The evidence says
put it first.

*Everything decorative.* Register, imagery, motion at the threshold of the first glance — free,
within the style guide, and this is precisely where "make it look like art" lives without
touching a Fixed rule.

**Where it looks sophisticated and fails.**

*The instrument panel.* Controls before meaning reads as rigour and is the select-first failure:
the score exists only after labour, and the citizen leaves before performing any.

*The links-hub.* A taxonomy of elsewhere. The audit's example communicates nothing about the
night itself on arrival — no number, no picture, a promissory note for a product.

*The brochure.* Message-first without an exemplar decays into the institution describing itself
above a download button. The audit caught a famous instrument mid-decay.

*The all-pins map with no sentence.* Abundance without argument. Every pin equal means no pin
argued for.

**What proves a break works.** Show the default view, untouched, to someone in the intended
audience for five seconds, then take it away and ask what it said and who it was for. If they
answer with the sentence you wrote in step two, the default is working. If they answer with a
description of the interface, it is not. Then check the other 85%: is everything crucial visible
without a single click?

---

## Checklist

- [ ] The default view's sentence is written, before layout
- [ ] It is addressed to a named visitor, in their voice, not the institution's
- [ ] The landing pattern is chosen from the six, in writing, with the rejected ones logged
- [ ] Everything crucial is visible without click or hover
- [ ] The default place, measure, comparison and period are chosen *as endorsements*
- [ ] No configuration is demanded before meaning is given
- [ ] The first screen is built from fast-glance forms
- [ ] Freshness and provenance are on the first screen
- [ ] Any input state shows what the answer will look like before asking for input
- [ ] The five-second test has been run with a real intended visitor
- [ ] Overview-versus-detail chosen from the visitor's arriving question, not from the mantra

---

## Sources

*Verified at source 16 August 2026 where marked; evidence-status in text.*

- [Aisch, *In defense of interactive graphics*](http://www.vis4.net/blog/in-defense-of-interactive-graphics/) — the 10–15% figure, its correction, and "if some information is crucial, don't make the user click or hover to see it."
- [Borkin et al., *Beyond Memorability*, TVCG 2015](https://vcg.seas.harvard.edu/publications/20150101-beyond-memorability-visualization-recognition-and-recall) — titles and text carry the message.
- [ONS Digital, *Say what you see*, 2019](https://digitalblog.ons.gov.uk/2019/01/28/say-what-you-see-the-way-we-write-chart-titles-is-changing) — ten-word message titles; the 9.5× telemetry.
- [Jachimowicz et al., *When and why defaults influence decisions*, Behavioural Public Policy 2019](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/67AF6972CFB52698A60B6BD94B70C2C0/S2398063X1800043Xa.pdf/when-and-why-defaults-influence-decisions-a-meta-analysis-of-default-effects.pdf) — **verified**: d = 0.68 [0.53–0.83]; 27.24 points; endorsement mechanism quoted.
- [Cho et al., *Anchoring effects in visual analytics*, VAST 2017](https://webpages.charlotte.edu/~wdou1/publications/2017/Anchoring_bias_VAST17.pdf) — the initially shown view biases process and outcome.
- [Hullman & Diakopoulos, *Visualization Rhetoric*, InfoVis 2011](https://users.eecs.northwestern.edu/~jhullman/vis_rhetoric.pdf) — default views as anchored interpretation; the Mapping America example.
- [Shneiderman, *The Eyes Have It*, 1996](https://hci.stanford.edu/courses/cs448b/papers/shneiderman96eyes.pdf) — the mantra's wording and its author's own account of its origin.
- [Craft & Cairns, *Beyond Guidelines*, 2005](https://faculty.cc.gatech.edu/~john.stasko/8001/craft05.pdf) — **verified**: 52 citations, no validations, "inspiration and guideline… rather than a scientifically studied methodological approach."
- [Hornbæk & Hertzum, *The notion of overview in information visualization*, IJHCS 2011](http://mortenhertzum.dk/publ/IJHCS2011.pdf) — 23 comparisons; satisfaction yes, performance unproven.
- [van Ham & Perer, *Search, Show Context, Expand on Demand*, InfoVis 2009](https://perer.org/papers/adamPerer-DOIGraphs-InfoVis2009.pdf) — the counter-mantra, case-study evidence only.
- [Lindgaard et al., *Attention web designers: you have 50 milliseconds*, 2006](https://www.tandfonline.com/doi/abs/10.1080/01449290500330448) — appeal stabilises at 50ms.
- [Tuch et al., *The role of visual complexity and prototypicality*, IJHCS 2012](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/38315.pdf) — simplicity and prototypicality drive the snap judgment, at 17ms.
- [Blascheck et al., *Glanceable Visualization*, InfoVis 2018](https://www.microsoft.com/en-us/research/wp-content/uploads/2018/08/GlanceableVis-InfoVis2018.pdf) — glance cost by chart form.
- [Nielsen Norman Group, *Designing Empty States*](https://www.nngroup.com/articles/empty-state-interface-design/) — craft guidance; no studies cited; marked practice-lore.
- Display audit, 16 August 2026, this project (`02-research-notes/`): OECD Better Life Index · ONS Explore Local Statistics · Thriving Places Index · Our World in Data · The Pudding · Creative Footprint · London Night Time Data Observatory · GLA Cultural Infrastructure Map · Gapminder (inferred only — tools page unfetchable) · BBC NHS tracker. All landing states quoted from live pages; comparative sources read for display method only.

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No study exists on whether users of interactive visualisations change defaults — rate, consequence, anything. The defaults meta-analysis has never been run for dashboards | Carried the behavioural-economics effect size with its scope stated | Amber — a live probe could measure this cheaply on our own instrument | Ch 8, and possibly a test in `03-tests/` |
| The empty-state cost is entirely unquantified; the whole literature is craft guidance | Marked every empty-state claim practice-lore | Yellow | Ch 8 |
| "Prototypicality rewards looking like the genre" collides with the brief's demand not to look like the genre | Deferred the resolution to Ch 12 with the tension stated | Amber — Ch 12 must resolve it, not restate it | Ch 12 |
| Gapminder's tools page could not be fetched; its default state is inference | Marked inferred; excluded from any load-bearing claim | Yellow | Gallery chapter (Ch 11) can re-attempt |

## Style Guide v1.4 — conflict log

**Agrees.** §04 "Frontload the point" is this chapter's step two at editorial scale. §12's
"provenance on every chart" extends naturally to the first screen, and the chapter strengthens it
to first-screen furniture. The seven tests' phone test is the five-second test's cousin.

**Conflicts.** None found.

**Silent on.** Landing patterns; empty states; the default-as-endorsement principle; what the
guide's slide rules imply for a *screen* that is neither slide nor document. The last of these
will recur every chapter and may eventually be the design system's dashboard section — but that
is for the design-system conversation, not this one.
