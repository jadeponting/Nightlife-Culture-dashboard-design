# Chapter 11 — Accessible as the good version

*Dashboard Design · Part 2: The interaction*
*Draft for steer · 17 August 2026*

---

## The decision

**Can the accessible version be the primary version — and what does that require deciding at the start, when it is still cheap?**

---

## The 60-second version

> The floor is settled and inherited: full keyboard operation including chart elements, visible
> focus, 200% resize and 400% zoom without spill, semantic structure, alt text generated from
> the current state, user override of colour, contrast and font — and the tooling chosen
> against those requirements **at project start, because they are unfixable later.** That is
> the Decision Book's dashboard chapter and the style guide's §13, and none of it is
> re-derived here.
>
> What this chapter adds is the frontier position: for *this* instrument, accessibility is not
> a parallel version to maintain — **it converges with the product.** The evidence: charts
> served as navigable hierarchical structures reduced cognitive load for blind screen-reader
> users against flat tables (a real study, 13 participants); newer work authors visual, textual
> and *sonified* representations as peers from one data abstraction (5 participants —
> promising, not proven). And this is a **music instrument**: the sound of a place is
> simultaneously its most distinctive display (Chapter 7) and a native non-visual channel. The
> written story layer (Chapter 10) is simultaneously narrative craft and the screen-reader
> spine. The plain-language register (§04) is simultaneously house voice and cognitive access.
> **The good version and the accessible version keep turning out to be the same build.**
>
> The strategic frame seals it: the regulations likely don't bind this instrument, but a
> government user cannot embed or cite a non-compliant product without inheriting the problem.
> Meeting the standard is a **distribution decision**. The audit exists and is cheap: fifty
> heuristics, ten critical, two to eight hours.

---

## How the decision is made

### Step one — inherit the floor, and choose tooling against it now

The Fixed floor, consolidated from the Decision Book's Chapter 15 and §13 **[axioms]**: entire
instrument keyboard-operable *including chart elements, data points and legends*; visible
focus, logical tab order; 200% resize and 400% zoom without spill or horizontal scroll; large
tables paginated; semantic structure with no skipped levels; alt text **generated from the
current filter state, stating the finding**; users able to override colour, contrast and font
— which rules out canvas-only charting; observed task-based testing with real users. And the
rule that makes all of them affordable: **the tool choice is an accessibility decision made in
week one** — a charting stack that renders to inaccessible surfaces cannot be retrofitted at
the audit.

The audit instrument is Chartability: fifty heuristics under seven principles, ten flagged
critical, a two-to-eight-hour full pass, validated across audit environments and adopted by
major toolmakers. **[Evaluated, adopted.]** It is scheduled per release, not per crisis.

### Step two — serve structure, not pictures of structure

The strongest design model in the accessible-visualisation literature is
**structure / navigation / description**: a chart exposed to a screen reader as a *navigable
hierarchy* — overview, then axes and groupings, then marks — rather than one alt sentence or a
flat data table. In the founding study, hierarchical navigation **reduced cognitive load for
blind and visually-impaired users versus flat tables** (13 participants). **[Measured,
small-n.]** It ships as open tooling that builds the navigable tree from standard chart
specifications — turning the accessible chart from bespoke cost into **build step**.

For this instrument the model maps directly onto structures the book already built: the
portrait navigates as identity → axes → marks; the filter walk announces Chapter 8's states
("suppressed: fewer than three contributors" is *already* screen-reader-ready wording); the
two columns navigate as columns. The information architecture and the accessibility
architecture are one drawing.

### Step three — author multimodal from the abstraction, and notice what this instrument is

The frontier work authors visual, textual and **sonified** representations as peers from a
single data abstraction — not sonification bolted onto a finished chart, but three renderings
of one structure. Evaluated so far with five expert screen-reader users: **promising, not
proven** — and this book prices it that way. **[Evaluated, very small n.]**

But notice what the instrument is. Its subject is sound; its Chapter 7 discovery surface
already *plays places*; its most distinctive asset is audio nobody else holds. For every other
dashboard in the world, sonification is an accessibility feature. For this one, **the audio
channel is the product converging with access**: the sound of the scene serves the blind user
and the curious kid identically. The rule: audio renderings are designed once, as first-class
display, to serve both — never twice, as feature and afterthought. Sonification of *data*
(as opposed to playing recorded sound) stays flagged as unevaluated, per Chapters 4 and 7 —
a probe, honestly labelled.

### Step four — the written spine is the access spine

Chapter 10 committed to per-place written stories as the narrative layer. That decision now
pays twice: prose is the one form every assistive technology handles perfectly, so **the
generated story is the guaranteed non-visual route to every finding** — the "non-interactive
route to the same finding" the Decision Book requires, already built for editorial reasons.
Same convergence in the language: §04's plain-language register and contested-terms discipline
are cognitive accessibility by other names, and the Vibe Setting Framework's own materials
test — *"would a busy Night Time worker, creative worker or freelancer understand this in one
read on a phone?"* **[house, confidential]** — is this chapter's reading-level standard,
stated by the community before this book existed.

### Step five — the distribution argument, made once

The public-sector accessibility regulations almost certainly do not bind an independent
studio's instrument; the Equality Act's reasonable-adjustments duty does. So the case for
meeting the full standard is not compliance — it is **distribution**: a council officer, a
combined authority, a national body cannot embed, link or cite a non-compliant instrument
without inheriting its liability. For an instrument whose ambition is to be *cited into*
committee rooms and business cases, WCAG 2.2 AA is the price of being quotable by the people
the advocacy needs. **[Evaluated — the regulatory analysis from the raw phase, retained for
the argument, not the law.]** That argument goes in the build's decision log, once, so it
never has to be won again at 11pm against a deadline.

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| The floor is the Decision Book Ch 15 / §13 set, inherited whole | Settled; not re-derived | **Fixed** | Axioms |
| Tooling chosen against the floor in week one | Canvas-rendered charts cannot be retrofitted; the cost moves from tooling-change to project-loss | **Fixed** | Decision Book Ch 15, axiom |
| Charts ship as navigable structure (overview → groupings → marks), not alt-sentence pictures | Hierarchical navigation measurably reduced cognitive load for blind users | **Fixed** | The structure/navigation/description study, measured small-n |
| The accessible tree is a build step from the chart spec, not bespoke work | Tooling exists; cost collapses when it is pipeline | **Fixed** | The open tooling precedent |
| State announcements reuse Ch 8's honest-surface wording | "Suppressed: fewer than three" is already the right sentence in every modality | **Fixed** | Ch 8 |
| Audio is designed once as first-class display serving access and product together | The sound of the place serves the blind user and the curious kid identically | **Fixed** | Ch 7; this chapter |
| Data sonification remains a labelled probe | Promising, five participants, unproven | Adaptable | The multimodal-authoring work, priced honestly |
| The generated written story is the guaranteed non-visual route to every finding | Prose is the universal assistive format; the route already exists for editorial reasons | **Fixed** | Ch 10; Decision Book Ch 7's non-interactive-route rule |
| The community's phone-read test is the reading-level standard | "Would a busy night-time worker understand this in one read on a phone?" | **Fixed** | Vibe Setting Framework, confidential |
| Chartability full pass per release; the ten critical heuristics per significant change | Two to eight hours; there is no beauty exemption | **Fixed** | Chartability, evaluated |
| Observed task-based testing includes disabled users of the actual audience | A stakeholder demo is not testing | **Fixed** | Decision Book Ch 15, axiom |
| The distribution argument recorded once in the decision log | So it is never re-argued under deadline | **Fixed** | This chapter |
| Where access and register genuinely tension (motion, texture, density) | Resolve by the decision hierarchy — accessibility outranks brand | **Fixed** | §02 hierarchy, axiom |

---

## Worked example

*Illustrative — the ward view, heard and keyed.*

**By keyboard:** tab lands on the headline sentence (the story spine), then the heartbeat,
then the two columns as landmarks; into the portrait chart as a tree — *"Identity portrait,
Croydon. Four groupings. Grouping one: genre mix, jungle strongest…"* — arrow keys walk marks;
the filter walk announces each state change in Chapter 8's wording, including the suppression
explanation and the way back.

**By screen reader, without touching a chart:** the generated story carries every finding in
prose — the guaranteed route — with links into the tree for the reader who wants the
structure.

**By ear:** the place plays — the Chapter 7 sound-of-the-scene — as content, not
accommodation. The data-sonification probe (intensity as rhythm) sits behind a labelled
experimental toggle, honestly separate.

**At 400% zoom on a phone:** the poster-beside-the-door layout reflows to poster *above*
door; nothing crucial was in a hover (Chapter 9), so nothing is lost; the busy-night-worker
test passes because it was the writing standard all along.

---

## Pressure points

**Where there is real latitude.**

*The audio identity.* Nothing in the floor constrains how the instrument *sounds* — the one
register where access work and brand work are literally the same craft, and no incumbent has
touched it.

*Access as advocacy credibility.* An instrument about who gets excluded from visibility,
that is itself exemplary on access, argues by existing. The dancefloor community named care
as a value; the product performing care is on-message in the deepest sense.

*Beyond the floor.* Dyslexia-friendly toggles, calm-motion modes, the stim-friendly
permission the workshops named for rooms — translated to screens. Free territory above the
minimum.

**Where it looks sophisticated and fails.**

*The parallel "accessible version."* Two builds, one maintained. The second is the
observatory within a year.

*The beautiful canvas.* A WebGL scene-scape that no key can enter — chosen in week one,
condemned at the audit, per the axiom.

*Alt text written once.* Static descriptions on dynamic views — the finding changes when the
filter changes, and the description must be generated with it.

*Compliance theatre.* A badge and an untested widget bar. The audit is two to eight hours;
the widget bar is neither necessary nor sufficient.

**What proves a break works.** Unplug the mouse and complete the worked example's walk. Zoom
to 400% and repeat. Then hand the instrument to a blind music fan — not a compliance
auditor — and ask what Croydon's night is like. If the answer matches the sighted reader's
(the Chapter 10 two-readers test, extended), the good version and the accessible version are
one thing, which was the claim.

---

## Checklist

- [ ] Floor inherited; tooling assessed against it in week one, decision recorded
- [ ] Charts ship as navigable trees from the build pipeline
- [ ] All state announcements reuse the honest-surface vocabulary
- [ ] Written story route complete for every finding
- [ ] Audio designed once as display; data sonification labelled experimental
- [ ] Phone-read test applied to all generated text
- [ ] Chartability pass per release; criticals per change
- [ ] Observed testing with disabled users of the real audience
- [ ] Distribution argument in the decision log
- [ ] No parallel accessible version anywhere
- [ ] The three walks run: keyboard, zoom, blind-fan

---

## Sources

*All previously verified or house; ledger updated.*

- Decision Book Ch 15 and Style Guide §13 — the floor. **Axioms.**
- Chartability (fifty heuristics, ten critical, 2–8 hours, adopters) — evaluated; raw-phase
  sweep, ledger.
- The structure/navigation/description model and its 13-participant study; the open tooling —
  measured small-n; raw-phase sweep, ledger.
- The multimodal-authoring work (five participants) — evaluated, priced as promising; raw
  phase.
- The regulatory analysis (regulations' scope; the distribution argument) — raw phase,
  retained for the argument.
- Vibe Setting Framework — the phone-read materials test; care and stim-friendly design as
  community values. **House, confidential.**
- Chapters 7, 8, 9, 10 of this book.

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No evaluation exists of recorded-audio-as-display (the sound of the place) for blind users — the convergence claim is argued, not measured | Claimed it as design intention; flagged for observed testing | Amber — testable in the prototype's first user sessions | `03-tests/`; the prototype |
| The navigable-tree model is unevaluated on maps | Applied it to charts; the map's accessible structure remains open | Amber | The build; Ch 3's silence compounds here |
| Data sonification for cultural statistics has no evidence base at all | Labelled experimental throughout | Yellow | `03-tests/` |

## Style Guide v1.4 — conflict log

**Agrees.** §13 supplies the floor; §02's hierarchy resolves every access-versus-brand
tension by construction; §04 is cognitive access wearing editorial clothes.

**Conflicts.** None found.

**Silent on.** Navigable chart structures; state announcements; audio as display; the
distribution argument. Logged for the dashboard section.
