# Chapter 1 — The instrument and its user

*Dashboard Design · Part 0: Start with people and place*
*Draft for steer · 16 August 2026*

---

## The decision

**Who is this for, and what are they doing at the moment they open it?**

---

## The 60-second version

> Every guidance document on this subject agrees that an identified user need gates the build. None
> of them says how you would know you have one. That gap is where these instruments die.
>
> The evidence base is thinner than the confidence around it. The famous claim that 85% of readers
> never touch an interactive control comes from one person measuring one button on a couple of news
> graphics in 2015 — and its author says it has been misread. Nobody has published equivalent
> figures for a statistical or place-data resource. **The honest position is that we do not know how
> people use these things, and anyone who tells you otherwise is quoting a footnote.**
>
> So the question cannot be answered from the artefact. It has to be answered from the decision.
> Four things, in order: **whose decision · what the decision is · when it happens · what is
> admissible in the room where it is made.** The fourth decides the most and is the one nobody asks.
> At a licensing hearing, cultural value is not admissible at all.
>
> And "explore" is not a mode of reading. It is a search task someone may invoke from within any
> mode. An instrument built around exploration has mistaken a capability for a need.

---

## How the decision is made

### Step one — name the decision, not the user

"Local advocates, policymakers, funders" is a list of people, not a list of decisions. It cannot be
tested and it cannot be wrong.

The reason to start at the decision is that decisions have properties a user group does not: a
moment, a duration, a room, a set of things that count as evidence in that room, and someone with
the authority to act. Every one of those constrains the instrument, and three of the four are
invisible if you start from the user.

Munzner's nested model calls the failure at this level the wrong-problem threat, stated flatly:
*"the target users do not in fact have these problems."* And it is the level that cascades — get it
wrong and no amount of craft downstream recovers it.

### Step two — find out what is admissible in that room

This is the step that changes the answer, and I have not seen it in any design guidance.

**Licensing.** Representations under the Licensing Act 2003 must be made within 28 consecutive days
and must relate to one of four licensing objectives: crime and disorder, public safety, public
nuisance, and protection of children. Council guidance is explicit that a representation about
commercial or competitive damage is not relevant. Cumulative Impact Assessments require an
evidential basis, and the sources named for it are crime and disorder statistics, anti-social
behaviour offences, alcohol-related ambulance and accident-and-emergency attendances, environmental
health complaints and resident questionnaires.

**Every admissible source is harm-side.** There is no statutory slot anywhere in the licensing
regime for a cultural value measure. An instrument that expects to change a licensing decision by
showing cultural value has misread the room, and no amount of design fixes that.

It gets sharper. The House of Lords post-legislative scrutiny of the Licensing Act found hearing
quality *"hugely variable"*, recorded a councillor who had *"in total… had three hours training on
licensing"* before sitting on a committee, and heard that hearings reach the right result *"by
chance rather than because of the quality of the licensing regime."* Practitioner briefings note
that strict rules of evidence do not apply, that hearsay is admissible with weight decided by the
committee, and that sub-committees are inclined to take residents' concerns at face value. This is
not a room a better dataset wins. It is a room a credible local person with a specific,
objective-framed claim wins.

**Public funding.** The route by which cultural value enters a public business case is monetised
valuation under the Green Book, which is why the Department for Culture, Media and Sport built the
Culture and Heritage Capital programme at all — its own working paper says the existing evidence is
*"qualitative or focused on outputs rather than the valuation of outcomes and impacts."*

**Competitive bidding.** Centre for Cities' interviews with local authority officers describe the
actual moment: a bid or strategy written in two to six weeks against someone else's template, often
by a consultant. Investment Zone responses were required *"within two weeks."* Greater Manchester's
ten authorities spent £1.1 million on consultants across two Levelling Up Fund rounds. That is when
an evidence resource is opened — not during a reflective policy review, which mostly does not happen.

### Step three — establish the need, and know what would tell you there isn't one

The prescriptive guidance is unanimous and unhelpful. The Government Analysis Function permits a
dashboard only when all four hold: *"there is an identified user need · data updates are frequent
and can be automated, with users likely to revisit the dashboard · users need flexibility of data
combinations and the ability to interact with data · you have sufficient resource to support the
dashboard."* Note that need and *need to interact* are separate conditions. The guidance then
offers questions to ask users, and the instruction *"Never create a dashboard in isolation"* — but
no method, no threshold, no sample.

The methods literature is more use, because it names the ways this goes wrong. Sedlmair, Meyer and
Munzner's design study pitfalls include *no need for visualization: problem can be automated* · *no
need for change: existing tools are good enough* · *no real, important, recurring task* · and the
one that should be read twice by anyone building a place-data instrument: **mistaking fellow tool
builders for real end users.** The people most enthusiastic about a place-data explorer are usually
the people who build place-data explorers.

Munzner's validation for this level is qualitative and immediate: *"interview and observe the target
audience to verify the characterization, as opposed to relying on assumptions or conjectures."*
Downstream, it is adoption — which she calls *"a weak signal with a large rate of false negatives
and some false positives."*

**And discovery has to be allowed to conclude "do not build this."** The GOV.UK Service Manual
describes discovery methods thoroughly and never states that outcome as a possibility. The clearest
worked case is the Office for National Statistics' Census 2021 local area stories: the team named
its user as *"citizen users, those without a background in statistics"*, acknowledged that
*"interactive maps, charts and dashboards are all wonderful ways of communicating data"*, and chose
331 pieces of prose instead, because *"we need to pull out the narrative and the story to help guide
our users through the numbers."*

### Step four — check that anyone is there to operate it

The Local Government Association's data capacity survey of 96 authorities found **62% report staff
data literacy is adequate only "to a small extent or not at all"**, and a **median of three
full-time analysts in a district council** against 24 in a single-tier or county authority. Three
people, already committed.

An instrument that needs an analyst to operate is, for most district councils, addressed to nobody.
This is a design constraint before it is a capacity problem.

The same applies to advocates. Data Orchard's survey of 162 not-for-profit organisations found
**under 1% at the highest data maturity level**, 87% analysing in spreadsheets, and 40% still
collecting on paper. And when 145 campaigners were asked what they needed, they named wellbeing
support, peer communities and mental health services. Not better data. Treat "campaigners are held
back by a lack of evidence" as an assumption with no primary source behind it.

### Step five — separate the mode from the capability

The Decision Book's five consumption modes — presented, sent, scanned, read, referenced — describe
how an artefact reached someone and what posture they are in. It is tempting to add exploration as a
sixth. The task literature says no.

Brehmer and Munzner place *consume* at the top level, with present, discover and enjoy beneath it.
*Explore* sits one level down inside **search**, defined by whether the target's identity and
location are known — alongside lookup, locate and browse. It is a search task, not a posture.

So exploration is **orthogonal** to the five modes, not an extension of them. A referenced use can
involve exploration. A scanned use rarely can. This matters because it separates two questions that
are routinely merged: *does this person need to explore?* and *how did this reach them?* The
Analysis Function's four-part gate already keeps them apart, and its second and third conditions
fail independently.

### The decision tree

```
Name the decision, not the user.
  Cannot name one? → the instrument has no user need yet. Stop.

What is admissible in the room where that decision is made?
  Nothing you hold is admissible → change the room, change the evidence,
    or build for a different decision. Do not build and hope.

Has need been established by observing and interviewing real users —
not fellow tool builders?
  NO  → that is the next piece of work, not this one
  YES → continue

Does the person who has to open it have the capacity to operate it?
  NO  → the instrument is addressed to nobody. Reduce what it asks of them.

Does this decision need exploration, or does it need an answer?
  An answer → a release, a report, a page, or 331 pages
  Exploration → state which search task: lookup, locate, browse or explore

Who refreshes each dataset after launch, by what mechanism, with what money?
  Unanswered → the container will outlive its contents, and look fine doing it.
```

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| Name the decision the instrument enters before naming its users | A user group has no moment, no room and no admissibility test; a decision has all three | **Fixed** | This book |
| Establish what counts as evidence in the room where the decision is made | Licensing representations must relate to the four objectives; every named Cumulative Impact Assessment source is harm-side | **Fixed** | Licensing Act 2003 s.5A; Home Office guidance |
| Do not expect a cultural value measure to move a licensing decision | There is no statutory slot for it | **Fixed** | Licensing Act 2003 |
| An identified user need gates the build, and an assumed need is not an identified one | All four Analysis Function conditions must hold | **Fixed** | Government Analysis Function |
| Treat "users need to interact" as a separate test from "users have a need" | They are separate gate conditions and fail independently | **Fixed** | Government Analysis Function |
| Verify the problem by interviewing and observing target users | The wrong-problem threat is that they do not in fact have these problems | **Fixed** | Munzner, nested model |
| Test the need with people who are not fellow tool builders | The named pitfall; enthusiasm for an explorer concentrates among explorer-builders | **Fixed** | Sedlmair, Meyer & Munzner |
| Discovery must be permitted to conclude "do not build this" | Three of the named pitfalls are forms of building something unneeded | **Fixed** | Sedlmair, Meyer & Munzner |
| Check the intended operator's capacity before designing what the instrument asks of them | Median three analysts in a district council; 62% report inadequate data literacy | **Fixed** | Local Government Association, 2024 |
| Name the refresh mechanism for each dataset, not just a maintenance owner for the whole | Measured: of ~24 datasets in the closest precedent, the one still current is the one an external body publishes monthly | **Fixed** | Analysis Function condition two; worked example below |
| Never judge a resource's currency from its front page | The container and its contents age independently, and the front page shows only the container | **Fixed** | Worked example below |
| Never cite the 85%-never-interact figure | One button, two graphics, 2015, and its author says it is misread | **Fixed** | Aisch, *In defense of interactive graphics* |
| Treat exploration as a search task, not a consumption mode | It sits under search alongside lookup, locate and browse — not alongside presented or read | **Fixed** | Brehmer & Munzner |
| State the decision's timescale in writing | Two weeks for an Investment Zone response; three-year cycles for Cumulative Impact Assessments; Arts Council decisions in July 2027 | Adaptable | Centre for Cities; Arts Council England |
| Where user groups are genuinely distinct, test three to four per group rather than five in total | The five-user model assumes a homogeneous base | Adaptable | Nielsen Norman Group |
| Say whether legitimation use is the intended outcome, or an accepted one | The commonest real fate of commissioned evidence is validating a decision already taken | Adaptable | This book |

---

## Worked example

**The London Night Time Data Observatory — a maintained container with unmaintained contents.**

This is the closest existing precedent to the instrument under discussion. **It is live.** All
figures below were checked directly on 16 August 2026 and quote the London Datastore's own labels.

**The recommendation.** The Night Time Commission's *Think Night* (2019), recommendation 3: *"The
Mayor should set up a London Night Time Data Observatory. This central hub of data… would help
boroughs create their Night Time Strategies and inform local decision making."* The diagnosis behind
it is one Nightlife Culture would recognise: *"It has been hard to access clear and consistent data
on which to base our findings"*, and *"it is hard to find good quality, robust data broken down by
time, with the detail required for local level decision making."*

**What exists.** The Mayor accepted it and it was built on the London Datastore, *"created primarily
to support local decision makers in improving the night time offer in their area."* It holds *"links
to over 30 data sources split across four themes"* — Vibrancy, Vitality, Safety and Livability —
plus geographic boundaries, the 2018 *London at Night* report and a guidance section. The pages are
current, the structure is intact, the copyright line reads 2026.

**What the update labels say**, verbatim, across all four themes — roughly two dozen datasets:

| Theme | The labels |
|---|---|
| **Vibrancy** | London's Night Time Economy by borough and Middle Layer Super Output Area: *"Updated almost 7 years ago"*. Entertainment licensing, floorspace, and alcohol and late-night refreshment licensing: *"almost 6 years ago"*. Pub closures: *"Added almost 6 years ago"*, coverage *"2000-18"*. Cultural Infrastructure Map: *"Updated over 2 years ago"* |
| **Vitality** | Seven of eight at *"almost 6 years ago"* — international visitors, domestic tourism, visitor perceptions, characteristics of night time workers, public transport origin and destination, trips by time of day, night bus users. High Street Busyness shows no date |
| **Safety** | Accident-and-emergency attendance and assault-related ambulance incidents at *"almost 6 years ago"*; Metropolitan Police notifiable offences by time of day at *"over 5 years ago"*. **Transport Crime in London: *"Updated 3 months ago"*** |
| **Livability** | Model-based income estimates: *"almost 7 years ago"*. Night-time jobs paid below the London Living Wage: *"over 5 years ago"*. Personal wellbeing and Indices of Deprivation: *"over 6 years ago"* |

**One dataset in roughly twenty-four is current.** It is Transport Crime in London, which Transport
for London publishes monthly and the observatory links to. **The only thing still alive is the thing
somebody else automates.**

**What Chapter 1 would have caught.** Not the design, and not the idea. Condition two of the
four-part gate — *"data updates are frequent and can be automated"* — arriving six years later and
resolving with unusual clarity. Where the refresh was automatic and external, it held. Where it
depended on someone at the observatory maintaining a dataset, it did not. The recommendation named
a hub and an audience; it named no maintainer, no refresh mechanism and no money.

**The transferable rule is narrower and more useful than "it failed."** An aggregator inherits the
update cadence of everything it aggregates, and the liveness of the container tells you nothing
about the liveness of its contents. Anyone assessing this observatory from its front page would
conclude it is a working resource. Anyone assessing it from its update labels would not. **Both
readings are correct, which is the problem.**

---

### Correction, and how it happened

An earlier draft of this chapter said the observatory was *"unmaintained and bypassed"* and
characterised it as dead. **That was wrong**, and Carly caught it by opening the page.

Two failures, both worth logging because both are procedural rather than factual.

First, **inference presented as finding.** "Dead" was my characterisation of a set of stale update
labels. The labels are the finding; "dead" was a conclusion drawn from them and stated as though it
were observed. This is precisely what the Decision Book's rule about quoting the line or marking the
inference exists to prevent, and it was breached in the first chapter written under it.

Second, **an unverified claim passed through a research agent into a draft.** The earlier version
stated that the London Nightlife Taskforce commissioned Mastercard and British Telecom data rather
than use the observatory, and recorded that *"no comprehensive unified nightlife dataset was
identified."* I have since tried to verify that from the Taskforce's own site and **could not**. It
may well be in the full report; it is not something I have seen. It has been removed rather than
softened, and it is logged below.

What survives verification is stronger than what was removed.

---

## Pressure points

**Where the rule genuinely bends.**

*The decision is sometimes plural and that is legitimate.* One canonical data layer serving several
expressions is a real architecture, not a hedge. What is not legitimate is one *interface* serving
several decisions, because the default view can only answer one question and the default view is
what most people see.

*Sometimes there is no room yet.* The most interesting case for a nightlife instrument is that the
decision it should serve does not currently exist — no statutory slot, no standing committee, no
line in a template. Building evidence to create a room is a legitimate strategy and it is how
several fields got their measures. But it should be **stated as that strategy**, with a named route
and a timescale, rather than smuggled in as a user need. The difference between the two is whether
you can say who will make the first decision using it, and when.

*Legitimation use is not automatically a failure.* Creative Footprint in Sydney was used by the
24-Hour Economy Commissioner to validate reforms already in train — *"This report demonstrates why
our new Vibrancy Reforms are essential."* That is legitimation rather than instrumental use, and it
is the most common real fate of commissioned evidence. It can be exactly what an advocacy movement
needs. Say so, and design for it, rather than claiming it will change minds.

**Where it looks like rigour and is not.**

*A user list standing in for user research.* Four named groups in a funding application is a
proposition, not a finding.

*Citing the interaction lore.* Every version of "most people never interact" traces back to one
button on a couple of graphics in 2015, whose author has objected in print to how it is read. There
are no published analytics on control usage in any official-statistics interactive that I could
find. If you need to know, you have to measure it.

*Assuming the scene wants the evidence.* There appears to be **no study** of whether artists,
promoters, venue staff or door teams read sector research. The closest empirical work — 36
interviews and 111 hours of ethnography with Amsterdam promoters — found their decision inputs were
genre conventions, granular spatial and regulatory knowledge, audience prediction and commercial
arithmetic. No dashboard, index or public dataset appeared anywhere in their decision-making. That is
an absence, not a refutation, but it should not be assumed away.

*Assuming the funder reads the data.* The Hodge review of Arts Council England found *"widespread
scepticism about whether ACE uses all the data it demands."* I could find no study of what a
cultural funding assessor actually reads, in what order, or for how long.

**What proves a break works.** Name the decision, the room, and one person with authority in it.
Show them what you have and watch whether they use it or explain why they cannot. If you cannot get
into the room, you have not established the need — you have described a hope.

---

## Checklist

- [ ] The decision is named in writing, not the user group
- [ ] The room where that decision is made is named
- [ ] What counts as admissible evidence in that room has been checked against the actual rules
- [ ] The decision's timescale is stated
- [ ] Someone with authority in that room has been observed or interviewed — not a fellow tool builder
- [ ] The intended operator's capacity to use it has been checked, not assumed
- [ ] Whether this decision needs exploration or an answer is stated
- [ ] If exploration: which search task — lookup, locate, browse or explore
- [ ] All four Analysis Function conditions assessed separately, with evidence for each
- [ ] The maintenance owner and the money are named before build
- [ ] Discovery was permitted to conclude "do not build," and did not
- [ ] Legitimation use declared as intended or accepted
- [ ] No claim in the brief rests on the 85% figure or its derivatives
- [ ] Every finding either quotes its source line or is visibly marked as inference
- [ ] Any claim relayed from a research assistant has been verified at source before it is written down

---

## Sources

- [Government Analysis Function — Building and managing dashboards](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-building-and-managing-dashboards/) — the four conditions, verbatim; "never create a dashboard in isolation."
- [Office for Statistics Regulation — Regulatory guidance: dashboards](https://osr.statisticsauthority.gov.uk/publication/regulatory-guidance-dashboards) — user need at the forefront. Cites no empirical research on how people use dashboards.
- [Munzner, *A Nested Model for Visualization Design and Validation*](https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf) — the wrong-problem threat; interview and observe as immediate validation; adoption as a weak downstream signal.
- [Sedlmair, Meyer & Munzner, *Design Study Methodology*](https://miriah.github.io/publications/dsm12.pdf) — 32 pitfalls, including mistaking fellow tool builders for real end users.
- [Brehmer & Munzner, *A Multi-Level Typology of Abstract Visualization Tasks*](https://www.cs.ubc.ca/labs/imager/tr/2013/MultiLevelTaskTypology/brehmer_infovis13.pdf) — explore as a search task under consume, alongside lookup, locate and browse.
- [Aisch, *In defense of interactive graphics*](http://www.vis4.net/blog/in-defense-of-interactive-graphics/) — the origin of the 85% figure, and its author's objection to how it is read.
- [Night Time Commission, *Think Night: London's Neighbourhoods from 6pm to 6am*](https://www.london.gov.uk/sites/default/files/ntc_report_online.pdf) — recommendation 3, and the diagnosis behind it.
- [London Night Time Data Observatory](https://data.london.gov.uk/night-time-observatory/) — "links to over 30 data sources split across four themes." Theme pages checked directly 16 August 2026: [Vibrancy](https://data.london.gov.uk/night-time-observatory/vibrancy/) · [Vitality](https://data.london.gov.uk/night-time-observatory/vitality/) · [Safety](https://data.london.gov.uk/night-time-observatory/safety/) · [Livability](https://data.london.gov.uk/night-time-observatory/livability/). All update labels quoted from those pages.
- [London Nightlife Taskforce](https://nightlife-research.london/) — research scale only. **The claim that it commissioned commercial data instead of using the observatory could not be verified from this source and has been removed from the chapter.**
- [House of Lords, post-legislative scrutiny of the Licensing Act 2003](https://publications.parliament.uk/pa/ld201617/ldselect/ldlicact/146/14606.htm) — hearing quality; three hours of training; "by chance."
- [House of Commons Library, *Alcohol licensing: cumulative impact*](https://researchbriefings.files.parliament.uk/documents/CBP-7269/CBP-7269.pdf) — the admissible evidence sources for a Cumulative Impact Assessment.
- [Local Government Association, *Local government data capacity and capability survey*](https://www.local.gov.uk/publications/local-government-data-capacity-and-capability-survey-local-authorities-october) — 96 authorities; 62% figure; median analyst headcount.
- [Centre for Cities, *L.A. Evidential*](https://www.centreforcities.org/publication/la-evidential/) — the bidding moment; consultant spend; two-week turnarounds.
- [Data Orchard, *State of the Sector 2021*](https://www.dataorchard.org.uk/data-maturity-nfp-sector-2021-report) — 162 organisations; under 1% at the highest maturity level.
- [Sheila McKechnie Foundation, *Under Pressure*](https://smk.org.uk/wp-content/uploads/2024/04/SMK-Under-Pressure-Report-FINAL-1.pdf) — 145 campaigners; what they said they needed.
- [Hodge Review of Arts Council England](https://data.parliament.uk/DepositedPapers/Files/DEP2025-0853/Arts_Council_England_Independent_Review.pdf) — scepticism about whether collected data is used.
- [Koren & Hracs, *Negotiating the night*](https://journals.sagepub.com/doi/10.1177/00420980241236384) — 36 interviews, 111 hours of ethnography; promoters' actual decision inputs.
- [Office for National Statistics, *Semi-automation and Census 2021*](https://digitalblog.ons.gov.uk/2023/01/27/semi-automation-and-census-2021-how-we-told-331-local-stories-in-one-go/) — the case where the research said write, not build.
- [Nielsen Norman Group, *Why You Only Need to Test with 5 Users*](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) — the model, and the distinct-groups caveat.

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No published analytics exist on control or filter usage in any official-statistics interactive | Reported the absence and refused to use the lore figure | Amber | Ch 4 — it is that chapter's central question and the evidence may not exist |
| No study of whether cultural practitioners read sector evidence at all | Used the nearest ethnography and marked the absence | Amber | Ch 2 |
| No study of what a cultural funding assessor actually reads | Reported the Hodge review's scepticism finding instead | Yellow | Ch 13 |
| Guidance names an identified user need as a gate and defines no threshold for it | Used the methods literature's pitfalls as the working test | Amber | This chapter; may become a rule once tested |
| **A research assistant's characterisation reached a draft as a finding. "Unmaintained and bypassed" was written as observed fact; it was inference, and one half of it could not be verified at all** | Corrected at source, logged, and two rules added to the chapter it broke | **Red — the correction came from Carly, on the first chapter written under a rule designed to prevent exactly this** | This chapter, and the working method |
| Could not verify whether the London Nightlife Taskforce used, or declined to use, the observatory | Removed the claim rather than softening it | Amber — the full Taskforce report may settle it in one read | Ch 13 |

## Style Guide v1.4 — conflict log

**Agrees.** §02 method stage 2, "separate the stated brief from the underlying decision," is this
chapter's step one arriving from the studio side. §15 gap 4's interim rule is consistent with the
four-condition gate used here.

**Conflicts.** None found.

**Silent on.** The guide has no position on establishing user need before building, and no position
on what to do when the decision an instrument serves does not yet exist. Both are live for this work.
