# Chapter 8 — Gaps, uncertainty and freshness

*Dashboard Design · Part 1: The display*
*Draft for steer · 17 August 2026*

---

## The decision

**How does the surface stay honest about what it doesn't know — what is missing, how sure, and how old — in every state a reader can reach?**

---

## The 60-second version

> Three honesties, and the evidence says each fails differently. **Gaps**: readers cannot detect
> missing data unaided — it was the joint-hardest defect in the misleading-chart literacy study
> (0.39 baseline) — so a silent gap simply reads as *less*. **Uncertainty**: the best-evidenced
> territory in the whole visualisation field — discrete, frequency-framed forms measurably beat
> intervals and text, and hard visual boundaries make readers sort the world into inside/outside
> even after extensive instruction. **Freshness**: the failure that killed the closest precedent
> — a live container over contents up to seven years stale, one dataset in twenty-four current,
> and the one alive being the one somebody else automates.
>
> Interaction multiplies all three. A static chart makes one claim you can check; an instrument
> makes a claim for **every combination of filters**, and honesty that holds only on the default
> view is a demo, not a design. Gaps render as gaps in every state; intervals widen as the base
> shrinks and are carried or the value is withheld; suppression is enforced at query time and
> *explained* — because "no data for this combination" and "suppressed to protect
> confidentiality" and "not yet measured anywhere" are three different messages, and only the
> instrument that distinguishes them keeps a reader's trust.
>
> This chapter is where the instrument's thesis and its craft coincide: for the value column,
> **the gaps are the argument** — so the honest surface is not a compliance layer here. It is
> the display of the case itself.

---

## How the decision is made

### Step one — gaps are rendered, at full size, with their reason

The Decision Book settles the baseline — *a gap in the data is a finding*: dashed segments,
hatched fills, visible breaks, never a silent omission, never interpolation across a collection
break **[axiom, carried into Style Guide §12]** — and the literacy evidence explains why it is
Fixed rather than nice: in the misleading-chart study, **missing data was among the defects
readers were least able to detect unaided** (baseline correctness 0.39 against 0.80 on clean
items). **[Measured.]** A reader will not infer the hole. The display must draw it.

This book has already extended the rule twice, and both extensions consolidate here. Every gap
carries its **reason**, from a fixed vocabulary: *never measured* · *not yet collected* ·
*suppressed for confidentiality* · *community-held* (consented non-publication, per Chapter 4)
· *collection break*. And gaps render **in every filter state** — the Decision Book's
interactive rule **[axiom, Ch 15]** — because a gap that appears on the default view and
vanishes under filtering has become a silent zero somewhere a reader is standing.

For this instrument the rule is also the rhetoric: the value column's labelled gaps — *belonging:
not yet measured anywhere* — are the two-columns thesis made visible. Honest absence is not
this instrument's weakness to manage. It is its central exhibit.

### Step two — uncertainty in forms the evidence supports

This is the most settled evidence in the field, verified in the raw research and graduating
here:

- **Discrete, frequency-framed forms win.** Quantile dotplots — the value as fifty countable
  dots — achieved **97% of optimal decision performance** (n = 408, incentive-compatible
  payoffs, confidence interval [95%, 98%]), beating a no-uncertainty control and halving
  decision variance; cumulative-probability curves performed nearly as well; **textual interval
  statements were unstable** and improved little with practice. **[Measured.]**
- **Hard boundaries mislead durably.** Error bars and cone-style bounds induce *deterministic
  construal* — readers sort outcomes into inside/outside — and the effect "persists even with
  extensive instructions." **[Measured.]** An interval drawn as a hard-edged bracket is a claim
  about a cliff that does not exist.
- **There is no one-size-fits-all.** Animated outcome draws beat static forms for multi-variable
  judgements and lose for single-value estimates on volatile data; the value-suppressing
  palettes shifted behaviour in a 24-person study without improving accuracy. **[Measured,
  with the small-n caveat carried.]** The form is chosen per task, and the choice is recorded.

The house rules already say the rest and are inherited as axioms: *a range is a legitimate
headline; uncertainty can itself be the finding* — "±1.4" belongs in the headline, not the
footnote — and *never round to imply precision the evidence does not support* **[axioms, §12
and Decision Book Ch 6]**.

**Under interaction, one more rule becomes load-bearing.** Intervals widen as the reader
filters and the base shrinks; most instruments show the point estimate regardless. The Decision
Book's rule is inherited whole: **carry the uncertainty through every filter state, or below a
stated base threshold replace the estimate with a range, and below the disclosure threshold
withhold it entirely** **[axiom, Ch 15]**. The felt layer already obeys this by construction —
Chapter 4's distributions of placed marks *are* the uncertainty display — which is one reason
the placed-self form was the right choice.

### Step three — freshness is a display element with a heartbeat

The observatory gave this book its founding case: a maintained container over unmaintained
contents, update labels reading "almost 7 years ago," one dataset in roughly twenty-four
current — the one an external body publishes monthly. The community named the same requirement
independently: a map not *"actively maintained and ethically governed… risks becoming outdated
or extractive as soon as it is published."* **[House, confidential.]** And the scene's own
steer made freshness economic: the dynamic census only means anything if the series visibly
lives.

The consolidated rules:

- **The heartbeat on the face**: every view states when its data last moved — *data to
  Thursday* — as first-screen furniture (Chapter 1's rule), not dataset-page metadata.
- **Per-dataset refresh mechanism named** (Chapter 1's observatory rule): not a maintenance
  owner for the whole, but the mechanism for each layer — because the container and its
  contents age independently, and the front page shows only the container.
- **Seasonality honesty** (Chapter 6): nightlife breathes annually; a series shown without its
  rhythm makes January a lie about July.
- **Staleness degrades visibly.** When a layer stops refreshing, the display says so and shows
  its age — it does not keep rendering confidently from a stopped clock. The instrument that
  cannot afford to maintain a layer retires it *visibly*, which is the anti-observatory move:
  better an honest amputation than a phantom limb.

### Step four — suppression is enforced at query time, and explained

The thresholds are axioms — no published figure rests on fewer than three contributing units;
secondary suppression so totals cannot give the cell away; categories fixed across editions so
tables cannot be differenced **[axioms, §13]**. What this chapter adds is *where* and *how they
display* in an interactive instrument:

- **At query time, on every combination** — because aggregate-safe does not mean filter-safe;
  a drill-down that reaches a cell of two is "a disclosure breach with a user interface"
  **[axiom, Decision Book Ch 15]**.
- **With the reason stated.** The empty state distinguishes its three species: *no data for
  this combination* · *suppressed to protect confidentiality — fewer than three contributors* ·
  *not yet measured*. The second message is the one that builds trust rather than spending it,
  and the style guide's `[c]` marker already exists for it — the row stays, the gap is visible.
- **On the national statistical office's precedent**, held in the raw research: the census
  flexible-table architecture enforces fixed classifications (users cannot request category
  subsets — which is what prevents differencing), applies perturbation keyed to the cell so
  the same cell answers identically every time, and **accepts, openly, that it does not track
  cumulative risk across a user's query history**. That accepted trade-off is available to
  this instrument too — *if declared*. Undeclared, the same choice reads as ignorance.

### Step five — small scenes are where all four honesties collide

At city scale these rules are hygiene; at scene scale they are safety. A scene of forty people
makes one placed mark with a genre and a night attached **a name** (Chapter 4); an
under-threshold cell in a hyperlocal cut is a person; a freshness stamp on a tiny layer can
reveal *when* someone contributed. The standing test is inherited and sharpened: **filter
deliberately, as an adversary, toward a small scene** — through genre × ward × month — and
verify that what appears is the explained suppression message, the widened range, the labelled
gap; never the confident small number. If that walk has not been taken, the instrument has
been demoed, not tested.

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| Every gap renders at full size with its reason, from the fixed vocabulary | Readers cannot detect missing data unaided (0.39); a silent gap reads as less | **Fixed** | CALVI, measured; Decision Book Ch 6; Ch 2 |
| Gaps render as gaps in every filter state | A default-view gap that vanishes under filtering becomes a silent zero | **Fixed** | Decision Book Ch 15, axiom |
| Never interpolate across a collection break | A continuous line over a break is a false claim | **Fixed** | Decision Book Ch 6, axiom |
| Uncertainty displays in discrete, frequency-framed forms; form chosen per task and recorded | Dotplots at 97% of optimal; text intervals unstable; no one-size-fits-all | **Fixed** | The uncertainty evidence, measured |
| No hard-edged interval brackets on modelled values | Deterministic construal persists despite instruction | **Fixed** | Measured |
| A range is a legitimate headline; precision matches the data | ±1.4 is a finding; false precision is a claim the data cannot support | **Fixed** | §12; Decision Book Ch 6, axioms |
| Uncertainty carries through every filter state; ranges below a stated base; nothing below the disclosure threshold | Intervals widen as the base shrinks; the point estimate lies hardest exactly where filtering goes | **Fixed** | Decision Book Ch 15, axiom |
| The heartbeat on the face of every view | The container and contents age independently; the front page shows only the container | **Fixed** | Ch 1; the observatory case |
| Refresh mechanism named per layer; retired layers retire visibly | The one live dataset was the one somebody else automates; a stopped clock must not keep telling the time | **Fixed** | Ch 1; this chapter |
| Series display their seasonality | January bare is a lie about July | **Fixed** | Ch 6 |
| Suppression enforced at query time on every combination, with secondary suppression | Aggregate-safe is not filter-safe | **Fixed** | §13; Decision Book Ch 15, axioms |
| The three empty states are worded distinctly: no data · suppressed (with threshold) · not yet measured | Only the distinguished messages keep trust; the second is the one that builds it | **Fixed** | Decision Book Ch 15; style guide `[c]` |
| Fixed classifications in the query interface; no category subsets | What prevents disclosure by differencing | **Fixed** | §13 axiom; the census architecture precedent |
| The no-cumulative-tracking trade-off, if taken, is declared | The national office accepts it openly; undeclared it reads as ignorance | **Fixed** | The census precedent, from raw |
| The adversary's walk is run before any release | Filter to a small scene deliberately; verify the messages, not the demo | **Fixed** | Decision Book Ch 15; Ch 4 |
| The craft of gap-rendering — hatching, ghosted vessels, the visual language of honest absence | Where this instrument's most distinctive surface lives | *Decorative* | Ch 2; Ch 12 |

---

## Worked example

*Illustrative — one reader's filter walk; fixes nothing about the design.*

**A reader lands** on a ward view — heartbeat top right: *ticketing to Thursday · felt layer
to March · grants layer: retired June 2026, shown at last state.* Three ages, three honesties,
no pretence of one.

**They filter to a genre.** The intensity figure becomes a range — *base below 200; showing
the spread, not the point* — and the felt-layer panel switches from median-plus-distribution
to distribution only, because at this base the middle is noise.

**They filter to genre × month.** Two venues' rows now read `[c]` — *suppressed: fewer than
three contributors* — and the monthly series shows a hatched band across February: *collection
break — platform outage, not absence of events.*

**They push to genre × ward × month** — the adversary's walk, taken by an ordinary user. The
panel yields entirely: *below the disclosure threshold at this combination. Zoom out one step
to see this scene safely.* The message names the threshold, offers the way back, and never
shows the confident small number.

**Nothing on any screen** in the walk displayed a bare point estimate on a shrunken base, a
silent zero, or a stale layer wearing a live face. That, rather than any single chart, is what
"honest surface" means.

---

## Pressure points

**Where there is real latitude.**

*The visual language of absence.* Hatching, ghosted vessels, the unlit-but-not-dead treatment
on dark ground — Chapter 2 opened this and it remains the most distinctive craft surface the
instrument owns. Honest absence, beautifully drawn, is the house style nobody can copy.

*Uncertainty as the headline.* "Somewhere between 90 and 140 nights a month — and that width
is itself the finding about how little the city counts" is a stronger sentence than any point
estimate. The house already believes this; the evidence licenses it.

*The retirement notice.* A layer retired with a dated, dignified marker — *this count ended
when the funding did* — turns a maintenance failure into evidence about the sector. Even the
instrument's own decay can tell the truth.

**Where it looks rigorous and fails.**

*The silent zero.* The empty cell rendered as nothing — indistinguishable from measured
absence. The single most common honest-surface failure in the wild.

*The confident tail.* Point estimates surviving filtering down to bases where the interval is
wider than the value.

*The hard bracket.* Crisp error bars on soft numbers — inside/outside sorting installed by the
display itself.

*Freshness in the footer.* The observatory's disease: the label exists, where nobody looks.

*The undeclared trade-off.* Adopting the no-cumulative-tracking compromise silently, or
perturbing inconsistently so the same query wobbles — either discovered later costs more trust
than both cost to declare.

**What proves a break works.** Take the adversary's walk to a small scene and read every
message aloud. Then unplug the pipeline for a week in staging and look at the instrument: does
it *visibly* age — heartbeats lagging, layers greying — or does it keep smiling? An instrument
that cannot look stale cannot be trusted to look fresh.

---

## Checklist

- [ ] Every gap at full size, with its reason from the fixed vocabulary
- [ ] Gaps present in every filter state; no interpolation across breaks
- [ ] Uncertainty forms discrete and frequency-framed; per-task choice recorded
- [ ] No hard-edged brackets; ranges as headlines where the finding is the width
- [ ] Uncertainty carried through filtering; ranges below stated bases; nothing below threshold
- [ ] Heartbeat on every view; refresh mechanism named per layer
- [ ] Retired layers visibly retired; seasonality shown on all series
- [ ] Suppression at query time with secondary suppression; `[c]` rows stay visible
- [ ] Three empty states worded distinctly, thresholds named
- [ ] Fixed classifications in the query interface; trade-offs declared
- [ ] The adversary's walk run and recorded; the staging-decay test run

---

## Sources

*The uncertainty evidence graduates to the ledger with this chapter; house axioms as marked.*

- The uncertainty display studies (quantile dotplots at 97% of optimal, n=408; hypothetical
  outcome plots' trade-off, n=288; deterministic construal; value-suppressing palettes, n=24) —
  verified in the raw research phase; ledger entries carry the links. Measured.
- Ge, Cui & Kay, the misleading-chart literacy instrument — missing data at 0.39. Measured;
  already in the ledger (Ch 2).
- Decision Book Ch 6, Ch 8 and Ch 15 — gaps as findings; provenance and suppression;
  the interactive inheritance (query-time thresholds, gaps in every state, uncertainty through
  filtering, the explained empty state). **House, read directly; axioms.**
- Style Guide §12 and §13 — show gaps, show the range, the `[c]` marker, threshold three,
  secondary suppression, fixed categories. **Axioms.**
- The census flexible-table architecture (fixed classifications, consistent perturbation, the
  declared no-cumulative-tracking trade-off) — from the superseded-phase research; graduated
  for the precedent, not the politics.
- The observatory case — Chapter 1's worked example, verified on the live pages.
- Vibe Setting Framework — the maintained-or-extractive requirement. **House, confidential.**

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| The uncertainty evidence is all single-view; almost nothing tests uncertainty display *under interactive filtering* | Inherited the Decision Book's carry-through rule as the working answer; flagged the evidence hole | Amber — a probe could test range-switching thresholds cheaply | `03-tests/` |
| No evaluated precedent for the "visibly ageing instrument" (staleness degrading the display) | Specified it from the observatory case; the staging-decay test is this book's own | Amber — original contribution candidate #4 | Ch 12 gallery; the prototype |
| The three-empty-states wording has no user testing behind it | Took the Decision Book's trust argument; wording untested | Yellow | The prototype's content design |
| Seasonality display for highly rhythmic annual data (nightlife's year) has no located research | Stated the rule from first principles | Yellow | Ch 12 gallery |

## Style Guide v1.4 — conflict log

**Agrees.** §12 and §13 supply half this chapter's rules as axioms — the guide is strongest
exactly here. The `[c]` marker, the range rule and the disclosure floor transfer without
friction.

**Conflicts.** None found.

**Silent on.** The heartbeat as furniture; retirement display; the three-empty-states
vocabulary; seasonality rendering; query-time enforcement mechanics. All flagged for the
eventual dashboard section.
