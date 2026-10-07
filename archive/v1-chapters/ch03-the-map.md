# Chapter 3 — The map

*Dashboard Design · Part 1: The display*
*Draft for steer · 16 August 2026*

---

## The decision

**What kind of map is this — and where geography is the projection, what does it do well, what does it do badly, and when is it the wrong surface?**

---

## The 60-second version

> The instrument's working name is the vibe *map*, so this chapter earns its place early: the map
> is the most seductive surface in place data and the least examined. The reflex is named exactly
> in the practice literature — *"the impulse is since the data CAN be mapped, the best way to
> present the data MUST be a map."* It usually isn't.
>
> The measured misreadings are severe. Small areas with extreme values are missed by 30–40% of
> readers while large areas are detected over 90% of the time — **the map weights attention by
> acreage, not importance**. Around 90% of readers assume darker means more, with or without a
> legend. And an unnormalised map of anything human is a population map wearing a costume.
>
> The audit of live music-venue maps found one pattern everywhere: the **directory pin map** —
> meaning carried by pin density alone, no time, no freshness, asserting what one auditor called
> *"a permanent daytime-neutral landscape of venues."* For an instrument whose subject runs 6pm
> to 6am, a surface with no time axis is not a neutral simplification. It deletes the subject.
>
> And the house critique is already an axiom: the Liverpool map was *"created by academics for
> local authorities… which is why they've got buses on it."* Buildings and infrastructure, when
> the scene is people. The chapter's job is to turn that critique into display rules.

---

## How the decision is made

### Step zero — a map is not necessarily geography

The word "map" belongs to design thinking before it belongs to cartography, and the house uses it
that way **[axiom, stated on steer]**: stakeholder maps, problem-space maps, systems maps, the
Doughnut. The Decision Book's Chapter 10 already holds the vocabulary — six jobs a diagram can do
(*bound, relate, decompose, sequence, diverge, converge*), with the **Systems Map** defined as
nested containment, not flow, and the ecosystem framing is itself one: tallest trees, grassroots,
mycelium — a vertical map of a living system with no geography in it. Doughnut Economics is the
proof that a non-geographic map can carry an entire economic argument in one figure: a normative
boundary drawn as a shape, readable in a glance, non-compensatory by construction — nothing on
one side of the ring buys back an overshoot on the other.

And the live precedent is the house's own. In the *Seeing the System* workshop (A Ticket to the
Future, Vibe Setting Framework — **unpublished, confidential until release**), participants built
a co-created map of Bristol's music ecosystem and **placed themselves on it** — the
insert-yourself-into-the-map move, already prototyped on paper, in a room. (Chapter 4 takes this
further: the placed self is a collection instrument, not only a mark.) What the mapping
process showed, in the framework's own words: *"Bristol cannot be mapped only through buildings,
venues or organisational structures"* and *"the feelings, relationships and people who make the
scene matter also need to be seen."*

So the step-zero question is: **which kind of map is this view, and what is its job?** Geographic
projection is one answer among several, correct only when *where* is the finding. A scene's
influence structure wants a systems map. Value flows want a flow map. The ecosystem's health
against its boundaries may want a doughnut. The rest of this chapter governs the geographic case
— but choosing geography is now a decision with named alternatives, not a reflex triggered by the
word "map" in the project's name.

### Step one — where geography is chosen, establish that it earns its place

Matthew Ericson, then deputy graphics director of the New York Times, wrote the canonical
warning: campaigns target swing states *"not because of their geographic location, which is what
a map is most effective at showing, but rather because of their voter demographics"* — and a map
of a non-geographic argument forces readers *"to try and visually sum up all the colors in their
head."* **[Practice-lore, from newsroom leadership; no controlled study exists — see gaps.]**
Datawrapper's version: to show numeric differences between regions, *"consider another chart
type, a table or text instead."* **[Practice-lore.]**

The test transfers directly: **a map is the right surface when location itself is the finding** —
where things are, how they cluster, what is near what. When the finding is *how much*, *how
good*, or *compared to what*, the map is the wrong surface wearing the right subject. "What does
Bristol sound like?" is not intrinsically a map question; parts of its answer are.

### Step two — match the form to the data, and venues are points

The cartographic rule is stated flatly by Axis Maps: **"never use choropleth with raw
data/counts"** — choropleth requires rates or ratios — and, the sentence that matters most here:
*"The less the thing you are mapping is tied to enumeration units, the less sense a choropleth
map makes."* **[Practice-lore, but canonical across the field.]**

Venues, events, crews and scenes are not properties of wards. They are points, and point
phenomena painted onto administrative areas inherit the **modifiable areal unit problem**:
the patterns you see change — and can reverse — depending on where the arbitrary boundaries
fall and at what scale (Openshaw 1984). **[Evaluated, foundational.]** A ward-choropleth of
"cultural vibrancy" is therefore twice wrong before it renders: counts in a choropleth, and a
point phenomenon forced into boxes someone else drew for a different purpose. This lands on
material already in hand — the comparative methodology's boundary-vintage discipline exists
precisely because areas are unstable containers.

### Step three — design against the three measured misreadings

Schiewe's review of empirical choropleth perception supplies numbers **[measured]**:

- **Acreage is attention.** Small regions with extreme values were missed by 30–40% of readers;
  large regions detected at over 90%. A city-centre ward holding half the night economy is, on a
  map, a speck beside suburbs holding none of it.
- **Dark is more.** ~90% of readers assume darker means more, legend or no legend. For a
  night-time instrument the trap is doubled: dark basemaps are the genre's aesthetic, and on
  them, *unlit reads as empty*. No empirical study exists on empty map areas being read as
  "nothing there" rather than "no data" — logged as a gap — but the dark-is-more bias points one
  way, and for this subject **unlit is not dead**; it may be exactly where the unlicensed,
  informal and DIY scene lives, or where data was never collected. The two-columns rule arrives
  here: absence on the map must be legible as *unmeasured*, not as *nothing*.
- **The legend is ignored.** Over 90% read colour lightness alone and skip the classification.
  Whatever the bins say, the lightness ramp is the message.

And the oldest trap of all, best stated by xkcd 1138: three near-identical heatmaps of "our
site's users," a magazine's subscribers and something else entirely — all just population maps.
An unnormalised map of nightlife activity is a map of where people live and go out, which is to
say: a population map with a lens flare. Normalisation — per resident, per venue, per licensed
premises, per something — is the fix, and Chapter 1's evidence already established that missing
normalisation is the defect readers are least able to catch on their own.

**The house holds the decisive worked case.** A Ticket to the Future's research found that
Bristol's venues under 1,000 capacity put on **78% of the city's paid events but take only 32% of
ticketing revenue** **[ATTTF; the finding is in the published foreword and was given on steer]**.
In every aggregate economic view — revenue, GVA, jobs — the arenas are the biggest player and
swamp the story, exactly as the biggest ward swamps the choropleth: **acreage bias has an
economic twin, and it is aggregate bias**. Normalise — per event, per venue, per pound of
revenue retained locally — and the story inverts: the small rooms are doing most of the work,
programming the local artists, generating the originality and the community wealth, and
struggling hardest with the economics. The display rule this yields is general: **whichever unit
the aggregate flatters, offer the normalised view that lets the rest of the ecosystem be seen —
because the biggest player will otherwise swamp every surface it appears on, map or not.**

### Step four — a pin cloud is a directory, not an argument

The audit found the same pattern on both live music-venue maps examined: **the directory pin
map**. Liverpool's (audited second-hand — the app itself is robots-blocked) shows *"precise
locations, capacity, and the primary functions"* of venues, framed explicitly as serving an
economic study; Toronto's mixes venues, studios and stores across one city surface. In both,
meaning is carried almost entirely by pin presence and density; at a glance, "music" equals
wherever pins are densest, which is downtown, which is the population map again.

Chapter 1 classified map-first landing states and found their failure: abundance without
argument — *"this exists, everywhere,"* but never *so what*; **every pin equal means no pin
argued for**. Clustering, the standard fix for the pin cloud **[vendor practice-lore]**, makes
it worse in one respect: a cluster count hides category mix and reads as pure quantity, so the
map's only remaining message is *more*.

The display rule that follows: **a map earns its place in this instrument only when its pins
carry an argument** — differentiated by something that matters (a value dimension, a trend, a
gap, a tier), not merely present. A directory has real uses; Chapter 1 filed it as a pattern with
an assumed visitor. But the deck's promise is *measure*, and a pin cloud measures nothing.

### Step five — a night map without time deletes its subject

Neither audited map surfaces time in any form: no hours, no night-versus-day, no closures, no
data age. The audit's summary line deserves quoting because it is the finding: both maps assert
*"a permanent daytime-neutral landscape of venues."*

The house definition makes night time operational — 6pm to 6am **[axiom]** — which means the
instrument's subject is a *time-slice of place*, and a static map is a display that has silently
integrated over the one dimension that defines the subject. The same venue is a café at 4pm and
a scene at 1am; a map that cannot tell the difference is not simplifying the night, it is
removing it. **Time is therefore a first-class display dimension for any map in this
instrument** — which specific form that takes (a time scrubber, small multiples by hour, a
night-only default) is a craft decision downstream; the Fixed rule is only that the map states
*when* it is true, exactly as Chapter 1 requires it to state *how fresh* it is.

### Step six — decide what a pin is, because the Liverpool critique is a display rule

The house critique — *"less about buildings and infrastructure and more about the people who
make the vibe happen"* **[axiom]** — is usually read as a data question. It is also a display
question: **what does a mark on this map represent?** A building outlasts the scenes inside it;
a scene can move buildings and remain itself. A venue-pin map is a map of *containers*. The
audit shows both incumbents chose containers, because containers have addresses and
self-registration forms.

This chapter cannot resolve the unit — that is entangled with questions the research reaches
later — but it can set the display rule: **the map's marks must represent the thing the
instrument values, and where that thing is not addressable (a crew, a scene, a recurring night
that moves), the map either finds a form for it or hands that content to a different surface.**
The one thing the map may not do is quietly substitute buildings for culture because buildings
have coordinates.

---

## The rules

| Rule | Why | Tier | Source |
|---|---|---|---|
| Name which kind of map a view is — its job in the diagram vocabulary — before choosing geography | "Map" is a design-thinking genre; geographic projection is one answer, not the default | **Fixed** | House axiom; Decision Book Ch 10 |
| The community's design questions govern any sector map | The scene has already authored the requirements: purpose, representation, data ethics, power, maintenance, accessibility, accountability | **Fixed** | Vibe Setting Framework, *Seeing the System* (unpublished — confidential) |
| Whichever unit the aggregate flatters, provide the normalised view | 78% of paid events, 32% of revenue: the biggest player swamps every un-normalised surface | **Fixed** | ATTTF research; this book |
| A map is used only where location itself is the finding | "Can be mapped" is not "must be a map"; non-geographic arguments force readers to sum colours in their head | **Fixed** | Ericson; Datawrapper |
| Never choropleth raw counts | Canonical; counts demand normalisation or a point/symbol form | **Fixed** | Axis Maps |
| Point phenomena are not painted onto administrative areas without stating the boundary choice and its effect | Patterns can reverse with the boundary drawn (modifiable areal unit problem) | **Fixed** | Openshaw 1984; Comparative Methodology v1.0 |
| Every map of activity is normalised, and the denominator is on the face | Unnormalised human data is a population map; readers cannot detect missing normalisation unaided | **Fixed** | xkcd 1138 as shorthand; CALVI via Ch 1 |
| Design for acreage bias: small high-value areas get labels, callouts or non-area encoding | 30–40% of readers miss small extreme regions; >90% detect large ones | **Fixed** | Schiewe 2019, measured |
| The lightness ramp is treated as the message; bins are secondary | ~90% read lightness alone and ignore classification | **Fixed** | Schiewe 2019, measured |
| On dark ground, unmeasured is visibly distinct from empty | Dark-is-more bias plus a night aesthetic makes unlit read as dead; unlit may be the informal scene or a data gap | **Fixed** | Schiewe 2019 + Ch 2's absence rule; the specific misreading is unmeasured — logged |
| Pins carry an argument, not just presence | Every pin equal means no pin argued for; density defaults to the population map | **Fixed** | Ch 1 audit; this book |
| Any map in this instrument states when it is true | The subject is 6pm–6am; a timeless map integrates away the subject | **Fixed** | House definition; display audit |
| Freshness on the map surface, not the dataset page | The GLA's staleness confession lives where map users never look | **Fixed** | Ch 1; GLA audit |
| Marks represent what the instrument values, never buildings-because-they-have-coordinates | The Liverpool critique as a display rule | **Fixed** | House axiom |
| Cluster only when the cluster itself says something | A cluster count hides category mix and reads as pure quantity | Adaptable | Practice-lore, marked |
| Choropleth remains available for genuinely areal, normalised questions | The form is imprecise, not forbidden — rank 6 used for pattern, per the Decision Book | Adaptable | Decision Book Ch 6 |
| Basemap aesthetics, night register, decorative geography | Free within contrast rules — this is where the map looks like nightlife's | *Decorative* | Style Guide |

---

## Worked example

*Illustrative — the vibe map's map decision, not its design.*

**The question the surface must answer:** "what does this city sound like, at night, now?"

**Step one says:** parts of that are map questions — where scenes cluster, what is near what,
where the gaps are — and parts are not: *how much*, *how strong*, *compared to last year* belong
to other surfaces. So the map is a view within the instrument, not the instrument.

**Steps two and three say:** no ward-choropleth of "vibrancy" — points, symbols or a normalised
surface, with the denominator visible; city-centre wards protected from acreage bias by labels
and callouts; the lightness ramp designed as the message because it will be read as one.

**Step five says:** the default map is a *night* map — its stated slice is, say, 6pm–6am this
quarter — and freshness sits on the surface. The anti-observatory move again: this map's own age
is part of its display.

**Step six says:** if the pin set is venues-only, the map must say so — *"showing licensed and
listed spaces; recurring nights, crews and scenes not yet mappable"* — rendering its own
missing layer per Chapter 2, rather than letting containers stand in for culture.

**The five-second test:** shown cold, a reader should say *"the night is alive here, here and
here — and the dark bits mean uncounted, not empty."* If they say *"there are lots of venues
downtown,"* the surface has produced the population map with a lens flare.

---

## Pressure points

**Where there is real latitude.**

*The night register.* Dark basemaps, neon accents, the whole aesthetic of the genre — free
within contrast rules, and this is the surface where "looks like nightlife's" is most available.
The constraint it inherits is only the unmeasured-versus-empty rule.

*Non-standard geography.* Cartograms, gridmaps, distorted or schematic geographies that trade
shape fidelity for value fidelity — legitimate, arguable, and well-suited to killing acreage
bias. Adaptable craft.

*Refusing the map for a view.* Some of the instrument's best answers may be lists, profiles or
small multiples. Declining the map where location is not the finding is a decision this chapter
explicitly licenses.

**Where it looks sophisticated and fails.**

*The vibrancy choropleth.* Wards coloured by a blended score. Three failures at once: counts in
a choropleth, a point phenomenon in boxes, and Chapter 2's forbidden blended score — now with
acreage bias on top.

*The beautiful pin cloud.* A thousand glowing dots on a dark basemap. Gorgeous, and it says
"population density" while reading as "vibrancy."

*The timeless night map.* Any map in this instrument with no stated time slice.

*Heat-mapping the informal.* Interpolated "vibe heat" smeared from sparse points manufactures
data where there is none — the exact opposite of rendering the gap.

**What proves a break works.** State what the map's marks represent and what its denominator is,
out loud. Show it for five seconds; collect the sentence. Then show it to someone who knows one
small, intense scene the map covers: if their scene is invisible and they cannot tell whether
that means *uncounted* or *absent*, the map fails the dancefloor test regardless of its beauty.

---

## Checklist

- [ ] Location established as the finding before a map was chosen
- [ ] No raw-count choropleth anywhere
- [ ] Boundary choice stated wherever areas are used; vintage per the methodology
- [ ] Denominator chosen and visible on the face
- [ ] Small high-value areas protected from acreage bias
- [ ] Lightness ramp designed as the message
- [ ] Unmeasured visibly distinct from empty, especially on dark ground
- [ ] Every mark carries an argument beyond presence
- [ ] The map states its time slice and its freshness on the surface
- [ ] Marks represent the valued thing; missing layers rendered per Ch 2
- [ ] Five-second test and dancefloor test run

---

## Sources

- [Ericson, *When Maps Shouldn't Be Maps*, 2011](https://www.ericson.net/content/2011/10/when-maps-shouldnt-be-maps/) — the reflex named; swing-state example.
- [Axis Maps, *Choropleth Maps*](https://www.axismaps.com/guide/choropleth) — never choropleth counts; the enumeration-units sentence.
- [Datawrapper Academy, choropleth guidance](https://academy.datawrapper.de/article/134-what-to-consider-when-creating-choropleth-maps) — normalisation; when to use a table instead.
- [Openshaw, *The Modifiable Areal Unit Problem*, 1984](https://www.uio.no/studier/emner/sv/iss/SGO9010/openshaw1983.pdf) — boundaries change the pattern.
- [Schiewe, *Empirical Studies on the Visual Perception of Spatial Patterns in Choropleth Maps*, 2019](https://link.springer.com/article/10.1007/s42489-019-00026-y) — acreage bias 30–40%/90%; dark-is-more ~90%; legends ignored. Measured.
- [xkcd 1138, *Heatmap*](https://xkcd.com/1138/) — the population-map trap, as shorthand.
- [Google Maps Platform, marker clustering](https://mapsplatform.google.com/resources/blog/how-cluster-map-markers/) — the pin-cloud fix and its costs. Practice-lore.
- Display audit, this project: [Liverpool City Region venues map](https://lcrmusicboard.co.uk/venues-map/) (interface robots-blocked; audited from host pages — marked second-hand) · [University of Liverpool announcement](https://news.liverpool.ac.uk/2022/10/06/were-working-with-liverpool-city-region-to-map-local-music-venues/) · [Toronto music map](https://www.toronto.ca/business-economy/industry-sector-support/music/music-directories/music-venues-spaces-studios-stores-map/) · GLA Cultural Infrastructure Map (Ch 1 audit).
- House axioms: the 6pm–6am definition; the Liverpool critique; the people-not-buildings principle.

---

## Gaps found while writing this chapter

| What the system missed | What I did instead | Cost | Where it belongs |
|---|---|---|---|
| No empirical study of whether empty/dark map regions read as "nothing there" versus "no data" | Argued from the adjacent dark-is-more finding, marked the inference | Amber — directly testable with two mock night maps | `03-tests/`; Ch 8 |
| No controlled comparison of map versus non-map displays for the same place-data task | Used newsroom practice-lore, marked as such | Yellow | Gallery (Ch 11) |
| No display-focused research on cultural asset maps at all — the literature is method and politics | Claimed the gap; built rules from cartographic perception + the audits | Amber — this instrument will be generating the evidence | This book's contribution, eventually |
| Liverpool's actual interface unverifiable (robots-blocked) | Audited from host pages, marked second-hand throughout | Yellow | Re-attempt in Ch 11 with browser tooling |

## The community's own requirements register

*Recorded here because it changes the chapter's status: the design questions for this map do not
need inventing. The scene wrote them.* The Vibe Setting Framework's *Seeing the System* workshop
(**unpublished — confidential until release**) produced a full set of design questions for a
future sector map, in eight groups: purpose and intent · representation and inclusion · data
ethics and ownership · what gets mapped · power, access and use · maintenance and sustainability
· design and accessibility · impact and accountability. Three findings from it bind this chapter
directly:

- *"Participants were clear that a useful map cannot only show buildings, venues, jobs and
  economic outputs"* — it must make the case for the unseen connections: *"the 'aunty networks',
  the chats, the favours, the care, the genre knowledge, the joy."* Step six, from the
  community's mouth.
- *"How can the map actively redistribute opportunity, rather than simply display what already
  exists?"* — a bar higher than any in the display literature, and now on the register.
- *"A future map must be community-shaped, actively maintained and ethically governed, otherwise
  it risks becoming outdated or extractive as soon as it is published."* — Chapter 1's
  observatory rule, arrived at independently by a workshop in Trinity Centre.

Every future chapter that touches the map defers to this register before inventing requirements.

## Style Guide v1.4 — conflict log

**Agrees.** §12's provenance-on-every-chart extends to the map surface; the ink-steps discipline
kills the vibrancy heat ramp before it starts. §02 stage 3 ("map the system") confirms the
design-thinking sense of map as the house's native one.

**Conflicts.** None found.

**Silent on.** Maps entirely — §12 covers charts only. No basemap rules, no geographic colour
guidance, no marker system. This is now the largest known silence in the guide for this
project's purposes, and it will recur in every spatial chapter.
