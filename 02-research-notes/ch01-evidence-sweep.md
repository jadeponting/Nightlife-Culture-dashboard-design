# Ch 1 working notes — evidence sweep on the default view

*Full sweep return, 16 August 2026. Five sub-questions; evidence-status marked throughout.
The two most load-bearing numbers (Jachimowicz; Craft & Cairns) were independently re-verified
at source before the chapter was written.*

## Q1. "Overview first" — doctrine, not evidence

**The mantra's wording and origin.** Shneiderman 1996: "Overview first, zoom and filter, then
details-on-demand." The paper is explicit that this is distilled experience: "Each line
represents one project in which I found myself rediscovering this principle and therefore wrote
it down as a reminder." Small usability studies of specific techniques exist in the paper (18-
and 20-subject); nothing tests the mantra as a whole. **Status: the mantra is practice-lore by
its author's own account.**

**Nobody validated it.** Craft & Cairns 2005 surveyed the citing literature — at least 52
citations, categorised as implementations (34), methods (7), evaluations (6), taxonomies (4),
other (1) — and found zero empirical validations: "although numerous authors cite the Mantra,
there are no reasonably obvious studies that have validated Shneiderman's recommendations";
it "appears to act as an inspiration and guideline for practitioners rather than a
scientifically studied methodological approach." Most citing authors "don't actually specify how
they use it." **Status: evaluated (systematic citation review); VERIFIED at source 16 Aug 2026.**

**The counter-mantra.** van Ham & Perer 2009 invert it for large graphs: "search, show context,
expand on demand" — "there is also a very large class of users that frequently deal with large
network data but are not interested in global patterns… they are trying to learn something more
about a particular datapoint." Evidence: one case study (3M+-edge citation network); authors
concede "this anecdotal evidence should obviously be confirmed through more rigorous evaluation."
**Status: evaluated (case study only) — the alternative is no better validated than the
original.**

**What overviews are worth.** Hornbæk & Hertzum 2011: review of 60 papers, 1,391 sentences using
"overview," 23 empirical comparisons. Satisfaction/preference is the only near-unanimous
benefit; task time faster in ~half; on errors only 2 of 17 comparisons favoured overviews, 3
against; "the performance benefits of overviews are not in any way clear across the studies
reviewed." **Status: measured (counts across comparisons). People *like* overviews; performance
benefits unproven.**

## Q2. First impressions form before the first click

**Lindgaard et al. 2006:** three studies rating homepage screenshots at 500ms then 50ms: "visual
appeal can be assessed within 50 ms," ratings highly correlated across exposure times.
**Measured — scope: appeal, not comprehension. "Users judge your site in 50ms" is extrapolation.**

**Tuch et al. 2012:** visual complexity (VC) and prototypicality (PT) manipulated; 59
participants/119 screenshots and 82/80; lower complexity → higher beauty (η²p = .58/.52), higher
prototypicality → higher (η²p = .81/.55); both present "even within 17ms," complexity processed
earlier. Best: low complexity + high prototypicality. **Measured.**

**Blascheck et al. 2018:** glance duration to extract a simple comparison from small charts —
bar ~245–285ms, donut ~159–216ms, radial bar ~1548–1772ms. **Measured — chart form changes
glance cost by roughly an order of magnitude (smartwatch scale).**

**Borkin et al. 2015:** eye-tracking + recall, 393 visualisations, 33 participants: "titles and
supporting text should convey the message of a visualization"; "a memorable visualization is
often also an effective one." Titles and text dominate attention and recall. **Measured; the
effectiveness-memorability link is their interpretive claim.**

## Q3. Defaults stick — but visualisation has barely tested its own

**Jachimowicz et al. 2019** meta-analysis: 58 datasets / 55 studies / 35 articles, n = 73,675
(51 to 41,952 per set). Overall default effect d = 0.68 (95% CI 0.53–0.83, p < .001); binary
outcomes: +27.24 percentage points absolute. Mechanisms: endorsement (b = 0.32, p = .038) and
endowment (b = 0.31, p = .044) moderate; ease did not. "Individuals commonly perceive defaults
as conveying an endorsement by the choice architect." Heterogeneity enormous (I² = 98.2%).
**Measured; VERIFIED at source 16 Aug 2026.**

**Johnson & Goldstein:** opt-in countries ~12–27% organ-donation consent, opt-out 86–99%;
regression: +16.3% actual donations under opt-out. **Measured.**

**Defaults in visualisation specifically — mostly an absence.**
- Cho et al. 2017 (VAST): 81 participants, 2×2; the *initially shown view* (map vs calendar)
  significantly shaped which views users subsequently used, and numerical anchors biased final
  estimates despite ~25 minutes of free exploration: "visual anchors impact users'
  decision-making processes while numerical anchors affect the analysis outcomes." **Measured —
  the first-seen configuration biases process and outcome.**
- Petrescu 2024: how Tableau practitioner communities bypass tool defaults — about authors, not
  audiences. **Evaluated.**
- **The absence: no study found measuring whether end users of an interactive visualisation
  change its defaults — filters, extents, sorts — at what rate, with what consequence. Nobody
  has run "Jachimowicz for dashboards."**

## Q4. The default view as editorial act

**Hullman & Diakopoulos 2011:** default views as procedural rhetoric — "Default views provide an
initial point of interpretation anchored to the default visual configuration." Example: NYT
"Mapping America" opening on "a default zoomed-out view of all of New York City (the largest US
city and presumed home of the default New York Times user)." Qualitative analysis of 51 pieces,
no experiment. **Evaluated.**

**Newsroom practice.** Tse's Malofiej 2016 talk exists (Nieman Lab confirms the title) but the
famous rules and 10–15% figure circulate second-hand; slides unfetchable. Primary confirmation
is Aisch, "In Defense of Interactive Graphics": "85% of readers didn't ignore the graphic, they
just didn't click the button"; "15% of readers aren't nobody"; operative rule — "if some
information is crucial, don't make the user click or hover to see it." **The 10–15% click rate is
measured (NYT internal analytics, non-peer-reviewed); "assume no one will see it" is
practice-lore built on it; "85% ignore interactives" is a documented misreading.**

**Titles.** ONS "Say what you see" (2019): titles should "sum up the main message shown in the
chart in 10 words or less"; internal telemetry: "bulletins take 9.5 times longer to read than
people spend on the page." **Practice guidance backed by unpublished telemetry.** Datawrapper
guidance points the same way — **practice-lore**. Borkin is the peer-reviewed anchor.

## Q5. Empty states: pure practice literature

NN/g empty-states article: three guidelines (communicate status; learning cues; direct
pathways); asserts costs ("confusion and decreased user confidence") citing **no studies** —
heuristics applied to examples. Broader search surfaced only vendor/design-blog content.
**Finding: no peer-reviewed research quantifying the cost of showing users an empty tool.**

## Absences that are findings

1. No experimental validation of the Mantra, then or since.
2. No study of whether visualisation users change defaults.
3. No peer-reviewed empty-state research.
4. Second-hand wording risk: Tse's slide text unfetchable; automated extraction used for
   sentence-level quotes — page-level verification advisable before print.

**Net:** the strongest evidence chain for the default view runs *around* the visualisation
field, not through it: aesthetic judgment ≤50ms on simplicity and prototypicality (measured);
titles/text dominate what's taken (measured); defaults read as endorsements, d ≈ 0.68
(measured); the first-shown view anchors exploration (measured once); ~85–90% never touch the
interaction layer (measured, internal). The field's own "overview first" rule is uncorroborated
doctrine — and its author said so.
