# Chapter 7 — Discovery: finding your tribe

*Dashboard Design · Part 1: The display*
*Draft for steer · 17 August 2026*

---

## The decision

**How does the instrument let a person find a scene that sounds like them — and let money find under-backed scenes — without ranking places, narrowing tastes, or exposing anyone who didn't ask to be found?**

---

## The 60-second version

> *"You cannot be what you cannot see."* The discovery use case has two faces: the kid who likes
> jungle choosing Bristol over Birmingham because they can hear where their tribe is, and the
> funder, journalist or Business Improvement District finding the underground scene that's
> creating dynamism before it registers anywhere. Both are legitimate; both are dangerous; and
> the display evidence for both is better than expected.
>
> **Matching is not ranking.** The best place-matcher ever built produced a different list for
> every user, from their own weights, with the score decomposed — no global "best city" existed
> anywhere in it. **Explanations work**: in the classic study, showing *why* something was
> recommended measurably improved acceptance, the winning display was a simple histogram, and
> 86% of users wanted explanations kept. And **absence made visible** is already how the grants
> world displays underinvestment: query a place, get almost nothing back, and the nothing is
> the signal.
>
> Two warnings structure everything else. The finest scene-discovery display ever made — a map
> of six thousand genres where position meant sound and every scene was equally clickable —
> **died the day its maker was laid off**, because it ran at a platform's pleasure. And
> discoverability is a consent question before it is a feature: the live precedent for safe
> discovery of marginal communities is strict **opt-in self-declaration**. Being findable is
> something a scene does, never something done to it.

---

## How the decision is made

### Step one — matching, not ranking: every ordering is yours

Chapter 5 banned the league table; discovery is where the ban gets tested, because "which place
suits me" genuinely wants an ordering. The resolution is in the precedents: Teleport, the
city-matching tool, had users pick which aspects of life mattered *to them*, then produced "a
list of cities that match your preferences, including a breakdown of your match score" —
adjustable, regenerating, personal. **[Practice-lore; the tool is now defunct.]** No global
ranking existed anywhere in the system: **every ordering was the user's own, and the
decomposition was the explanation.**

That is the discovery display's constitutional rule, and it is Chapter 5's crop test surviving
contact with recommendation: an ordering derived from *your* stated taste, displayed *to you*,
decomposed so you can see why — that is not a league table, because it does not exist until you
ask and it is nobody's ordering but yours. The moment the instrument publishes "best cities for
jungle," Chapter 5 has been breached and every reactivity mechanism fires.

The state already operates this pattern one door down: Discover Uni, the Office for Students'
course-comparison service, presents standardised statistics as comparison cards with no league
table — the official answer to "inform choice without ranking." **[Policy precedent.]** And it
contains nothing about scene or culture, which is precisely the hole the house steer names: the
kid choosing a university chooses a city's sound, and no instrument shows it to them.

### Step two — show the why, and know the persuasion trap

The recommendation-explanation evidence is directly usable. Herlocker, Konstan and Riedl tested
21 explanation interfaces with 78 users: the winning display — a simplified **histogram of
similar users' ratings** — measurably beat unexplained recommendations, and in the follow-up,
**86% of users wanted explanations added permanently**. **[Measured.]** The design lesson from
the winner: it reduced the judgement to "a single binary visual comparison."

For this instrument the explanation writes itself from Chapter 4's materials: *"Why this
matches you"* rendered as concrete cues, not vibes-talk — you listen to jungle; Bristol runs
*n* jungle nights a month; these *x* crews; free-entry tiers exist; the scene's own belonging
distribution. Concrete cues are auditable (Chapter 4's rule) and they are what a life decision
deserves.

**And the trap is measured too.** Tintarev and Masthoff's evaluation work found personalised
explanations can be *liked more but less effective* — persuasiveness and effectiveness are
different aims, and a display tuned to please converts worse decisions at higher satisfaction.
**[Measured.]** For an instrument advising someone where to live or study, the rule follows:
**explanations are built for effectiveness — helping the person decide well — and tested
against that, not against how much they are liked.** A discovery surface that flatters its user
into a bad move fails the dancefloor test at the scale of a life.

### Step three — the similarity surface, and the platform-dependency rule

Every Noise at Once is the exemplar this chapter is lucky to have: roughly 6,300 genres as a
spatial word-map where **position encodes sound** — organic to mechanical on one axis, dense to
spiky on the other — every genre equally clickable, each playable in a thirty-second sample,
with drill-down to artists and to *"The Sound of [City]"* playlists. **[Practice-lore — a
working artefact, never formally evaluated.]** It demonstrates three things at once: similarity
can be displayed without any rank; a place can be *heard*, which is the literal answer to "what
does your city sound like?"; and wandering — adjacency browsing — is a discovery mode that no
list affords.

**And then it died.** Its maker was laid off in Spotify's December 2023 cuts; he "lost the
ability to fix any errors caused by changes on Spotify's end" and the site froze — the best
scene-mapping instrument in the world, gone because it ran on one platform's data at that
platform's pleasure. **[Measured fact of record.]** The rule this yields is structural, and it
echoes both the observatory and the Centre for Thriving Places' funding logic: **the discovery
layer runs on data the instrument owns or is durably licensed — never at a platform's
pleasure.** For a studio whose data spine is its own ticketing relationships, this is an
argument the business model already makes.

### Step four — scene-curated pools, machine-matched delivery

Spotify's own published account of algotorial playlists gives the hybrid pattern: human editors
define the pool — capturing qualities "difficult to describe in algorithms" — and the machine
personalises selection and order from within it. One editorial object, millions of personal
instances. **[Practice-lore, first-party.]** Bandcamp's discovery runs the fully human version:
editorial, visible fan trails, curation by named people. **[Practice-lore.]**

Translated to this instrument, the pattern solves two problems at once. **The scene defines the
pool** — which nights, crews and spaces are in the discovery layer is a curatorial and
*consent* act by the scene (the community register's data-ethics questions bind here), keeping
cultural truth in human hands. **The matching personalises within it** — the kid's taste finds
its subset. And Bandcamp's visible-people principle serves the shine-a-light ambition directly:
discovery through *named* promoters, resident DJs and crews — people as guides, not algorithms
as oracles — which is also Chapter 4's authorship rule arriving in the discovery layer.

### Step five — design against narrowing, without the folk theory

The filter-bubble claim should not be load-bearing: the strongest review evidence "finds no
support for the filter bubble hypothesis" in news consumption, echo chambers measure far
smaller than public debate assumes, and almost nothing tests music or place discovery.
**[Measured/synthesised — and the literature is news-focused, which limits transfer.]** So the
chapter does not justify its rules by bubble-fear. It designs against *narrowing* on first
principles: a discovery instrument for scenes exists to widen what people can see, so adjacency
is a feature — "close to your taste, new to you" — and the wandering surface (step three)
affords it structurally. Engineered serendipity is a live research area rather than settled
practice **[evaluated but immature]**; it is probe territory for the prototype, not a rule.

### Step six — the money view: absence made visible

For funders, philanthropists, brand partners and Business Improvement Districts, the display
precedent is GrantNav, the open UK grants navigator: funders use it to "see how your grants
align or overlap with others" and to "find gaps, overlaps or chances to work with others."
**[Practice-lore, verbatim.]** Its deep pattern: **underinvestment displays as visible
absence** — query the place, get almost nothing back, and the nothing is the finding. The map
of money, never a league table of the deserving.

The instrument's move is the overlay this sector has never had: **the map of money laid over
the map of scenes.** High intensity (Chapter 6's measure, denominator visible) where the grants
layer is empty *is* the opportunity display — "underinvested but alive" as a picture rather
than a plea. The sweep found no platform anywhere that displays high-potential underground
culture to investment — genuine white space, and this book's second candidate original
contribution after Chapter 4's "what this changed" field.

Two guards, both already in the book's spine. The exposure risk: an opportunity display is
"vocabulary and coordinates" for speculation as well as for support, so the community
register's governing question — *redistribute opportunity, rather than simply display what
already exists* — decides what the money view shows, and consent (step seven) decides who is
in it. And the return mechanism: Fairbnb's cooperative precedent — half of platform fees
funding community projects chosen by residents — shows discovery revenue flowing back to the
discovered. **[Practice-lore.]** The house already built that logic: a 1% ticket contribution
into a community-owned fund *is* the return mechanism, constituted. The discovery layer and
the Community Benefit Society are the same argument at two scales.

### Step seven — consent to be found

The live precedent for safe discovery of marginal communities is Everywhere Is Queer: a world
map of queer-owned businesses that is strictly **opt-in — businesses submit themselves** —
where being on the map is an act of self-declaration shaped by safety. **[Practice-lore.]**
That, plus Chapter 4's consent architecture, plus the sector's own history — a scene findable
to audiences is also findable to enforcement, and Form 696 is the case study nobody in this
house needs explained — yields the closing rules:

- **Discoverability is opt-in at scene level**, with granularity the scene controls: findable
  to audiences but not to the money view; findable this season but not archived forever;
  findable as a genre presence but not as named nights.
- **A scene can see how it is findable, and change it.** The sweep found no platform with
  community-level control over being *recommended* — another white space this instrument would
  pioneer, and one the Community Benefit Society's governance is built to hold.
- **Default invisibility for the informal.** The unlicensed and the underground appear in
  aggregate character (the city sounds like this) without coordinates, unless they opt
  upward. Chapter 3's unlit-is-not-dead rule, now with a consent mechanism behind it.

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| Discovery orderings are personal, decomposed, and exist only on request | An ordering from your weights shown to you is not a league table; a published "best cities for jungle" is | **Fixed** | Teleport precedent; Ch 5 |
| No global discovery ranking is ever published or publishable | The crop test applies to outputs of matching too | **Fixed** | Ch 5 |
| Every match displays its why, as concrete cues | Explanation measurably improves acceptance; 86% wanted it; cues are auditable | **Fixed** | Herlocker et al.; Ch 4 |
| Explanations are tuned and tested for effectiveness, not persuasiveness | Personalised explanations can be liked more and decide worse | **Fixed** | Tintarev & Masthoff |
| The similarity surface carries no rank axis; places can be heard | Position-as-character with equal clickability is proven display; sound is the honest medium | **Fixed** | Every Noise at Once pattern |
| The discovery layer runs on owned or durably licensed data | The field's best instrument died at a platform's pleasure | **Fixed** | Every Noise's end; observatory lesson |
| The scene defines the pool; the machine matches within it | Cultural truth and consent stay in human hands; personalisation still works | **Fixed** | Algotorial pattern; community register |
| Named people are visible as guides in discovery | Shine the light on independents; authorship rule extended | **Fixed** | Bandcamp pattern; Ch 4 |
| Adjacency ("close to your taste, new to you") is designed in | Against narrowing, on first principles — not on filter-bubble folk theory | **Fixed** | This chapter; the evidence review |
| The money view displays underinvestment as visible absence — money map over scene map | The grants world's own pattern; the overlay is the sector's missing picture | **Fixed** | GrantNav pattern; Ch 6 |
| The money view shows only consented scenes, governed by the redistribute question | Opportunity display is coordinates for speculation too | **Fixed** | Community register; superseded-phase risk research |
| Discovery revenue flows back to the discovered, visibly | The return mechanism exists — the fund is it | **Fixed** | Fairbnb precedent; house model |
| Scene discoverability is opt-in, granular, and revocable — and scenes can see how they're findable | Findable to audiences is findable to enforcement; self-declaration is the safe precedent | **Fixed** | Everywhere Is Queer; Form 696 history; Ch 4 |
| Serendipity mechanics beyond adjacency | Live research, not settled practice — probe territory | Adaptable | Serendipity literature |
| The wandering surface's expressive craft — sound, motion, the map that plays | Where discovery becomes the artful thing no incumbent owns | *Decorative* | Ch 12 |

---

## Worked example

*Illustrative — the kid who likes jungle; fixes nothing about the design.*

**They arrive** from a "what does your city sound like?" link. They give taste — pick genres,
or play three tracks they love. No account, no harvest; the input is the consent.

**They get portraits, not a podium:** three cities whose scenes match, as Chapter 5 identity
portraits — *different, never better* — each with its **why** in concrete cues: *"Bristol: 14
jungle and 140+ nights a month · 6 active crews · free-entry tiers at 40% of events · scene
running 30 years."* Each city **plays** — thirty seconds of the sound of the place. Beside the
match: *near your taste, new to you* — the adjacency row. Under each: named guides who opted
in — a promoter, a resident, a crew — and what studying or living there costs, the wage-to-rent
line the university prospectus never shows.

**The university angle, explicit:** beside Discover Uni's earnings statistics, this is the
missing card — the scene data for the city the course is in. The student chooses with both.

**The money view, separately and gated:** a funder sees the scene-intensity layer over the
grants layer; three consented scenes glow where the money map is dark. Each carries its
origination and intensity evidence (Chapter 6 discipline) and the return route — the fund —
by which backing them feeds the scene rather than strip-mining it.

**The five-second tests:** the kid says *"I can hear where my people are."* The scene says
*"we chose to be here, and we can see how we look."* The funder says *"I know where the gap
is."* If any of the three says something else, the surface fails.

---

## Pressure points

**Where there is real latitude.**

*Sound as the display medium.* A discovery surface that plays is native to this domain and
almost unoccupied. The sound-of-place is the one artefact in this book nobody else can fake.

*The wandering map.* Adjacency browsing across scene-space — the Every Noise affordance,
rebuilt on owned data with the night's aesthetics — is probe-ready and gallery-worthy.

*Named guides.* Human curation as interface — the promoter as the door into the scene — extends
the studio's whole philosophy into the product surface.

*The repeatable task.* **[House steer, 17 Aug.]** An advocacy instrument is opened twice a
year; a discovery instrument is opened twice a week — and the twice-a-week use is what keeps
the data fresh, the scenes visible and the instrument fundable. Discovery is therefore not a
feature of the dashboard; it is the **retention engine** — the repeatable task (finding events
and scenes, beyond a basic listing site) that makes the whole instrument a habit rather than a
report. The platform horizon this could grow into — partnership data spines, an affiliate
return-path that benefits musicians — is recorded in the use-case register as hypothetical and
post-prototype; the retention requirement binds now.

**Where it looks sophisticated and fails.**

*The listicle output.* Any export, share-card or press view that flattens matches into "top
cities." The crop test applies to what the *user's* screen can generate too.

*Taste-lock.* Matching so tight the kid only ever sees jungle. The adjacency row is not
optional furniture; it is the anti-narrowing mechanism.

*The unconsented spotlight.* Surfacing a scene to the money view, or to anyone, because its
data was harvestable. Opt-in or absent.

*Platform-borrowed discovery.* Building the layer on a streaming service's similarity data —
the exact dependency that killed the exemplar.

*Vibes-talk explanations.* "This city has amazing energy" is a persuasion display. Cues or
nothing.

**What proves a break works.** Run the three five-second tests above. Then the reversibility
test: a scene asks to change how it is findable — if the change cannot be made, seen and
confirmed by them, the consent architecture is decoration. And the Form 696 test, standing for
the whole chapter: if an enforcement body opened the discovery layer tomorrow, what could they
do that they cannot do today? The answer must be *nothing the scene didn't choose to show.*

---

## Checklist

- [ ] All orderings personal, decomposed, on-request; nothing publishable as a league table
- [ ] Every match shows its why as concrete, auditable cues
- [ ] Explanations tested for decision quality, not likeability
- [ ] The similarity surface has no rank axis; places play
- [ ] Discovery data owned or durably licensed; no platform's-pleasure dependency
- [ ] Pools scene-defined; matching within, never beyond
- [ ] Named guides visible; independents lit
- [ ] Adjacency row present in every match view
- [ ] Money view: consented scenes only; absence-made-visible pattern; return route shown
- [ ] Scene-level discoverability opt-in, granular, revocable, and visible to the scene
- [ ] Informal scenes default to aggregate character, no coordinates
- [ ] The kid test, the scene test, the funder test, the reversibility test, the Form 696 test

---

## Sources

- [Every Noise at Once — overview](https://en.wikipedia.org/wiki/Every_Noise_at_Once) and
  [McDonald's own account, Significance](https://www.significancemagazine.com/culture/93-every-noise-at-once-using-big-data-to-explore-new-music) — the spatial similarity display; the Sound of the City; the shutdown. Agent-fetched.
- [Herlocker, Konstan & Riedl 2000 (PDF)](https://grouplens.org/site-content/uploads/explain-CSCW-20001.pdf) — explanations improve acceptance; the histogram winner; 86%. Agent-fetched; measured.
- [Tintarev & Masthoff, explanation aims and evaluation](https://link.springer.com/article/10.1007/s11257-011-9117-5) — persuasive ≠ effective; liked-more-decided-worse. Agent-fetched; measured.
- [Kotkov et al., serendipity survey](https://www.sciencedirect.com/science/article/abs/pii/S0950705116302763) — immature evaluation base. Agent-fetched.
- [Reuters Institute, echo chambers and filter bubbles review](https://reutersinstitute.politics.ox.ac.uk/echo-chambers-filter-bubbles-and-polarisation-literature-review) — "no support for the filter bubble hypothesis"; news-focused caveat. Agent-fetched.
- [Spotify Engineering, algotorial playlists](https://engineering.atspotify.com/2023/04/humans-machines-a-look-behind-spotifys-algotorial-playlists) — human pool, machine match. Agent-fetched; first-party.
- [Teleport, via Smithsonian](https://www.smithsonianmag.com/innovation/where-should-you-live-app-will-tell-you-180962588/) — personal weights, decomposed match, no global rank. Agent-fetched.
- [Discover Uni](https://discoveruni.gov.uk/) — state precedent: inform choice without ranking. Agent-fetched.
- [GrantNav / 360Giving funder guidance](https://www.360giving.org/explore/using-360giving-data-as-a-funder/) — gaps and overlaps; absence visible. Agent-fetched, verbatim quotes.
- [Fairbnb](https://www.positive.news/lifestyle/the-ethical-alternative-to-airbnb-fairbnb/) — discovery revenue returning to community. Agent-fetched.
- [Everywhere Is Queer](https://www.goodgoodgood.co/articles/everywhere-is-queer-app) — opt-in self-declaration. Agent-fetched.
- House: the use-case register (steers 17 Aug); community register (confidential); Ch 4 consent architecture; Ch 5 crop test; Form 696 history from the superseded-phase research, retained as sector memory.

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No design/HCI evaluation exists of any scene-discovery interface — Every Noise, Resident Advisor, Bandcamp are all unevaluated artefacts | Used them as pattern precedents, marked practice-lore | Amber — the prototype's discovery probe would be the first evaluated instance | `03-tests/` |
| Recommendation-explanation research has never been run in a place/scene domain | Transferred with the domain difference stated | Amber | `03-tests/` |
| No platform precedent for community-level control over being recommended | Specified it from CARE-shaped principles; the instrument would pioneer it | Amber — original contribution candidate #3; governance lands with the Community Benefit Society | Ch 13 |
| Filter-bubble literature barely touches music/place | Refused to make it load-bearing; designed against narrowing on first principles | Yellow | — |

## Style Guide v1.4 — conflict log

**Agrees.** §01's "help people find one another" is this chapter's purpose statement. §04's
contested-terms rule kills vibes-talk explanations. The audience framework's plural users match
the register.

**Conflicts.** None found.

**Silent on.** Discovery and matching displays entirely; consent-to-be-found as a display
property; sound as a display medium. All three now logged for the eventual dashboard section.
