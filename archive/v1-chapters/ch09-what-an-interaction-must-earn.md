# Chapter 9 — What an interaction must earn

*Dashboard Design · Part 2: The interaction*
*Draft for steer · 17 August 2026*

---

## The decision

**What must an interaction buy to justify existing — and what does the evidence say each one costs?**

---

## The 60-second version

> The default position is measured, and it is against. Across roughly 4,300 real web sessions,
> adding narrative introductions to exploratory visualisations was null to negative — the
> *no-story* group explored roughly twice as long (108.8 seconds against 54) and performed more
> operations, and only 35.4% of readers followed the intended sequence at all. The newsroom
> telemetry points the same way: 10–15% of readers touch the interaction layer, and the author
> of that number's most famous correction drew the operative rule himself — *"if some
> information is crucial, don't make the user click or hover to see it."*
>
> The evidenced exceptions are narrow, and the narrowness is the useful part:
> **prediction-before-reveal** improves recall — in the visual modality only, for unfamiliar
> data only; **staged animated transitions** improve tracking and estimation — until
> over-staged. And the few readers who do interact are not free agents: the first-shown view
> measurably anchors what they explore and what they conclude, through twenty-five minutes of
> free use.
>
> So every interaction in this instrument starts owing. It pays its way with a **named
> purchase** — and this book has already accumulated the purchases that are genuinely worth
> paying for: personalisation (*your* place), collection (the placed mark), chosen comparison
> (your peers), adjacency (new to you), and contribution that returns. An interaction that
> cannot name its purchase from that list is decoration with a maintenance bill.

---

## How the decision is made

### Step one — start from the null, not from enthusiasm

The evidence base, all previously verified and in the ledger:

- **The null.** Boy, Détienne and Fekete's three field experiments: narrative introductions did
  not increase engagement with exploration; the no-story condition explored about twice as
  long; only about a third followed the authored sequence. **[Measured.]**
- **The reach.** The New York Times' internal analytics: 10–15% of readers interact — with
  Aisch's published correction that the famous 85% *"didn't ignore the graphic, they just
  didn't click the button."* The graphic worked; the button was optional. **[Measured,
  internal; the correction is the point.]**
- **The steering.** Cho and colleagues: the initially-shown view of an interactive tool
  significantly biased which views users then used *and* their final estimates, despite
  twenty-five minutes of free exploration. **[Measured.]** Interaction does not free the
  reader from the author; it hides the authorship.

None of this says "don't build interactions." It says: **the static reading of every view must
already work** (Chapters 1–8 built exactly that), and interaction is a paid extension, never a
prerequisite.

### Step two — the purchase list, house edition

The Decision Book's Chapter 7 established the general rule — a departure must name what it
buys — with the general purchases: attention, retention, comprehension, context, register,
fit. **[Axiom.]** This book's chapters have accumulated the instrument-specific purchases, and
they are better than the general ones because each carries its own evidence and its own
guard-rails:

| Interaction | What it buys | Earned in | Guard-rails already set |
|---|---|---|---|
| **Enter your place** (postcode, area) | Personalisation — the default sentence in *your* voice | Ch 1 (message-then-input) | The empty state shows what the answer looks like first |
| **Place your mark** (the playable survey) | Collection — the digital human dot plot; the instrument gets data back | Ch 4 | Consent, moderation-before-launch, self-selection labelled |
| **Choose your peers** | Fair comparison, and peer choice is itself scene knowledge | Ch 5 | Named scheme; no global ordering ever |
| **Wander adjacency** | Widening — "close to your taste, new to you" | Ch 7 | The anti-narrowing mechanism, not optional furniture |
| **Reweight** | A back-channel: what readers value, collected | Ch 6/7 (Better Life Index finding) | The default weighting is still an endorsement and says so |
| **Filter and drill** | The analyst's real task | Ch 8 | Query-time disclosure; uncertainty carried; gaps in every state |
| **Predict then reveal** | Measured recall improvement | This chapter | Visual modality, unfamiliar data, always skippable |

The rule: **every interaction in the instrument names its row.** An interaction with no row is
either a new purchase to be argued into the table with evidence, or it is cut.

### Step three — audit coverage with the taxonomy, not inspiration

Heer and Shneiderman's twelve interactive dynamics — data and view specification (visualise,
filter, sort, derive); view manipulation (select, navigate, coordinate, organise); process and
provenance (record, annotate, share, guide) — are explicitly unvalidated as prescriptions.
**[Evaluated — the authors say so.]** Their value is as a completeness check, and the check
finds something: the **process-and-provenance group is where evidence instruments
under-build.** *Record* (this state, saved), *annotate* (what I noticed, attached), *share*
(this exact view, to someone), *guide* (how I got here) — these are the interactions that make
an instrument **citable**, and citability is this instrument's whole strategic ambition.

Two rules follow. **Every reachable state has a stable address** — a filtered view someone
cites in a council paper must be reconstructable a year later (and the crop test extends: what
the share link renders must carry its provenance and gate with it). And **sharing is a
first-class interaction**, designed under Chapter 5's crop rules, not left to the browser's
screenshot.

### Step four — spend the evidenced exceptions where they fit

**Prediction-before-reveal** (recall improved ~4 percentage points; visual modality only;
unfamiliar data only; n=378 **[measured]**) has a natural home this instrument is lucky to
own: *"guess what your area's night is worth before we show you"* — the playable survey's
opening move, where the data is genuinely unfamiliar to the visitor and the guess itself is
collectable (a record of public perception against measured value — advocacy gold). Conditions
carried: always skippable, keyboard-operable, never gating the answer.

**Staged transitions** (object tracking and estimation improved; over-staging degrades; axis
rescaling degrades regardless **[measured, small-n]**) earn their keep exactly once per
pattern: when a view reshapes — peers swapped, denominator changed — the marks move through
one staged step so the reader keeps hold of what became what. Motion never carries meaning
alone **[axiom]**, and reduced-motion preferences are honoured with an instant-swap
equivalent.

### Step five — what may never hide behind an interaction

Consolidating the standing axioms into this chapter's floor: **nothing crucial behind click or
hover** (the Aisch rule, and Chapter 1's default-view discipline); **explanation beside the
chart, caveats visible by default, never in tooltips** — tooltips fail on touch, keyboard,
print and screenshot **[axiom, Decision Book Ch 15]**; **no filter combination may produce an
unannotated misleading result** — a constructible false picture is a defect, not user error
**[axiom]**; and the honest-surface rules of Chapter 8 hold in every state an interaction can
reach, because an interaction is precisely a machine for reaching states.

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| The static reading of every view works before any interaction is added | 85–90% never touch the layer; the null says narrative gating suppresses the rest | **Fixed** | Aisch; Boy et al., measured |
| Every interaction names its purchase from the table, or argues a new row with evidence | Unnamed interactions are decoration with a maintenance bill | **Fixed** | Decision Book Ch 7, generalised |
| The first-shown state of any interactive view is designed as an anchor, knowingly | It biases exploration and conclusions through 25 minutes of free use | **Fixed** | Cho et al., measured |
| Every reachable state has a stable, citable address | Citability is the instrument's ambition; a council paper must be able to point at a view | **Fixed** | This chapter; process-and-provenance audit |
| Share outputs obey the crop rules and carry provenance | The share is the state's afterlife | **Fixed** | Ch 5; Ch 6 |
| Prediction-before-reveal is used where data is unfamiliar, visually, skippably | The one interaction with measured comprehension gains — under those conditions | **Fixed** | Kim, Reinecke & Hullman, measured |
| Predictions may be collected as perception data, consented and labelled | The guess is itself evidence of the perception gap | Adaptable | This chapter; Ch 4 rules apply |
| One staged transition per reshape; instant-swap under reduced motion; meaning never in motion alone | Staging helps until over-staged; motion is inaccessible to some readers | **Fixed** | Heer & Robertson, measured; axiom |
| Nothing crucial behind click or hover; caveats visible by default, never tooltips | The 85% receive the surface only | **Fixed** | Aisch; Decision Book Ch 15, axiom |
| No filter combination yields an unannotated misleading result | Constructible falsehood is a design defect | **Fixed** | Decision Book Ch 15, axiom |
| The taxonomy audit is run on the built instrument | Coverage check, especially record/annotate/share/guide | Adaptable | Heer & Shneiderman, as checklist |
| Playfulness in *how* earned interactions feel — springs, sound, touch | Free, once the purchase is named and the floor holds | *Decorative* | Ch 13 |

---

## Worked example

*Illustrative — the interaction budget of the screens Chapters 1–8 already built.*

Run the table against the instrument as sketched so far. **Surviving:** the postcode entry
(personalisation; the empty state shows a real place first); the placed mark (collection; the
whole Chapter 4 architecture); peer choice (comparison; named scheme); the adjacency row
(widening); the filter walk (analysis; Chapter 8's honesty holding at every step); one guess
moment at the front of the playable survey (prediction; skippable; the guess collected as
perception data); one staged move when peers swap.

**Cut on sight:** hovers revealing numbers already printed at the mark (buys nothing, costs
accessibility); a "play all boroughs over time" autoplay (delight claiming meaning); filters
for dimensions no named user asked about (Chapter 1's fellow-tool-builder trap, as furniture);
scroll-hijacked narrative between the reader and the default sentence (the null, ignored).

**The budget statement**, one line per surviving interaction, lives in the build's decision
log — which is Chapter 14's override log, already waiting for it.

---

## Pressure points

**Where there is real latitude.**

*How earned interactions feel.* Once the purchase is named and the floor holds, the springs,
sounds and textures of interaction are decorative-tier and genuinely free — the play *of* the
thing, as distinct from play *instead of* the thing.

*The guess as an instrument of advocacy.* "The public thinks the night is worth X; it measures
Y" is a finding this instrument can generate about itself, cheaply, from a skippable moment.

*Instrumenting the instrument.* Nobody has published control-usage analytics for a statistical
interactive — the Chapter 1 gap. This instrument can simply measure its own: which
interactions are used, by whom, anonymously. The evidence hole in the whole field is one the
prototype can start filling from its first week.

**Where it looks sophisticated and fails.**

*The hover-reveal of the already-visible.* The commonest interaction in dashboards, and it
buys nothing at all.

*The narrative gate.* Story you must scroll through to reach the answer — the null result,
built on purpose.

*Filter abundance.* Twenty dimensions because the data had twenty columns. Every filter is a
promise that the combination is meaningful; Chapter 8 prices those promises.

*Animation as evidence.* Marks dancing to imply change the data doesn't establish. Motion
never carries meaning alone — and especially not meaning that isn't there.

**What proves a break works.** For any proposed interaction: name the row; show the static
reading working without it; then watch one real user of the intended audience meet it cold.
If they use it, note what it bought. If they don't, remember that they are the 85% — and that
the surface they saw was the product.

---

## Checklist

- [ ] Static reading of every view complete before interaction added
- [ ] Every interaction has its named row; cut list recorded
- [ ] First-shown states designed as anchors, deliberately
- [ ] Every state addressable; shares carry provenance and survive the crop test
- [ ] Prediction moments: unfamiliar data, visual, skippable, guesses consented if collected
- [ ] One staged transition per reshape; reduced-motion equivalent; no meaning in motion alone
- [ ] Nothing crucial behind click/hover; caveats visible; no load-bearing tooltips
- [ ] No filter combination misleads unannotated (Ch 8's walk re-run after any new filter)
- [ ] Taxonomy audit run; record/annotate/share/guide deliberately decided
- [ ] Usage instrumentation planned, anonymous, declared

---

## Sources

*All previously verified or house; ledger updated.*

- Boy, Détienne & Fekete (the storytelling null, ~4,300 sessions) — measured; ledger.
- Aisch, *In defense of interactive graphics* — the 10–15%, the correction, the crucial-info
  rule; ledger (Ch 1).
- Cho et al. (anchoring in visual analytics) — measured; ledger (Ch 1).
- Kim, Reinecke & Hullman (prediction and self-explanation) — measured; ledger.
- Heer & Robertson (animated transitions) — measured, small-n; ledger.
- Heer & Shneiderman (interactive dynamics taxonomy) — evaluated, unvalidated-as-prescription;
  ledger.
- Decision Book Ch 7 and Ch 15 — name-the-purchase; tooltip and misleading-combination axioms.
- Chapters 1–8 of this book — the purchase table's provenance.

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| Still no published control-usage analytics for any statistical interactive | Made instrumenting-the-instrument a design intention | Amber — the prototype fills the field's own hole | `03-tests/`; the prototype |
| The guess-as-perception-data pattern has no located precedent | Specified from prediction evidence + Ch 4 consent rules | Yellow — original contribution candidate | The prototype |
| Stable state-addressing for filtered views (citable permalinks) has no evaluated design literature found | Specified structurally from the citability ambition | Yellow | Ch 12 gallery hunt; build |

## Style Guide v1.4 — conflict log

**Agrees.** §15 gap 4's interim rule (keyboard, thresholds at query time) is inherited and
extended. The seven tests' phone test kills load-bearing hover outright.

**Conflicts.** None found.

**Silent on.** Interaction budgets; state addressing; prediction moments; motion rules beyond
slides. Logged for the dashboard section.
