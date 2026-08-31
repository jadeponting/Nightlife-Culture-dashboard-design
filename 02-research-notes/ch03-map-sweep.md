# Ch 3 working notes — map sweep

*Full sweep return, 16 August 2026. Capped lean sweep; evidence-status marked.*

## 1. What map form fits what data

**Axis Maps (canonical practice-lore):** "never use choropleth with raw data/counts" —
choropleth data must be "standardized to show rates or ratios." Worked example: "*number of
people* is a count and not appropriate for choropleth maps; *number of people per square mile*
is a ratio." Escape hatch: dot density, proportional symbol and cartogram "can all handle raw
data." Most relevant sentence: **"The less the thing you are mapping is tied to enumeration
units, the less sense a choropleth map makes."** Venues are points — a venue choropleth is
doubly wrong (counts + non-areal phenomenon).

**Datawrapper (practice-lore):** "It would not be useful to map the absolute number of
unemployed people in each county since we can't compare that data without knowing the counties'
population."

**MAUP (evaluated, foundational):** results and visual patterns from area-aggregated data change
— sometimes reversing — with how boundaries are drawn and at what scale. Openshaw 1984, CATMOG 38.

Cairo's *How Charts Lie* covers the same ground (the "land doesn't vote" case) but no
page-anchored quote was fetchable; cite Axis Maps as the rule.

## 2. What a map communicates unintended

**Schiewe 2019 (measured):** review of empirical choropleth perception studies. Small regions
with extreme values **missed by 30–40% of users**; large areas detected at >90% — "larger
regions receive higher visual weight." **Dark-is-more bias:** ~90% assume darker = more, even
without a legend. **Legends ignored:** >90% read colour lightness alone, skipping the
classification scheme.

**Follow-up (evaluated):** "Sponge Maps" (Schiewe 2022) — value-by-area hybrid built "for
avoiding the area size bias in choropleth maps."

**xkcd 1138 "Heatmap":** three near-identical US heatmaps — "Our site's users," "Subscribers to
Martha Stewart Living," a third — as Pet Peeve #208: geographic profile maps that are basically
population maps. The shorthand for unnormalised human data.

**Dark/empty = "nothing there":** **no direct empirical study found** of empty map areas read as
"nothing there" vs "no data." Nearest anchors: dark-is-more (measured) and area-size bias.
Logged as a gap — the "unlit ≠ dead" point for night culture must be argued from these plus
first principles, or tested.

## 3. Points-on-a-map for venues/culture

**Pin cloud (vendor practice-lore):** Google Maps Platform — "Hundreds of data points clumped
together can get in the way of clarity"; clustering combines nearby markers into one icon. A
critique (thin, practice-lore): clusters hide category mix and read as false importance.

**Cultural asset mapping display research: weak.** What exists is method/politics, not display
(MAPC Arts & Planning Toolkit; McCandlish PhD chapter on digital cultural asset mapping,
Glasgow). **No strong empirical work found on how cultural-asset map displays are read — a
genuine literature gap the chapter claims.**

## 4. When NOT a map

**Ericson 2011 (canonical practice-lore, NYT graphics leadership):** "the impulse is since the
data **CAN** be mapped, the best way to present the data **MUST** be a map." Swing states
targeted "not because of their geographic location, which is what a map is most effective at
showing, but rather because of their voter demographics." Maps defeat analysis when readers must
"try and visually sum up all the colors in their head."

**Datawrapper:** "If you want to point out the numeric differences between regions, consider
another chart type, a table or text instead"; for correlation, "consider a dot plot or
scatterplot instead."

**Not found:** a controlled experiment comparing map vs non-map displays for the same
place-data task. Schiewe is perception-within-maps, not map-vs-alternative.

## 5. Display audit — two live venue maps

**Liverpool (LCR Music Board / University of Liverpool).** The app (`lcrmb.shinyapps.io`) is
**robots-blocked — audited second-hand from host/press pages.** Shows "precise locations,
capacity, and the primary functions (i.e. arena, small music venue, concert hall or festival
space) of all live music venues"; purpose framing explicitly economic ("determine the sector's
cultural and economic value"). Freshness model: venue **self-registration**; no visible
last-updated indicator on host pages. Framing line at livemusicresearch.org: venues "compiled by
Liverpool University as part of an economic study into how live venues are impacted by policy."
At-a-glance: a directory/census pin map serving an advocacy dataset.

**Toronto (City of Toronto).** "Music Venues, Spaces, Studios & Stores Map"; intro: "Explore
music services, retailers, supporting organizations and venues across Toronto." Page modified
15 May 2025 (metadata only, not surfaced as data freshness). Map app did not render in fetch;
title implies category-typed pins across the city — at a glance "music" = wherever pins are
densest, i.e. downtown.

**Audit pattern:** both are directory pin maps; meaning carried almost entirely by pin presence
and density; neither surfaces time (hours, night vs day, closures) or data freshness in the
default view — **"the map asserts a permanent daytime-neutral landscape of venues."**

## Could not find

- Empirical work on empty/dark regions read as "nothing there."
- Controlled map-vs-non-map task comparisons.
- Display-focused research on cultural asset map interfaces.
- Direct fetch of the Liverpool app and the Toronto widget — interface details second-hand.

## Post-sweep additions from steer (16 Aug 2026)

- **The design-thinking sense of "map"** (stakeholder maps, problem-space maps, systems maps,
  the Doughnut) reframed the chapter — step zero added. Decision Book Ch 10 supplies the
  vocabulary (bound · relate · decompose · sequence · diverge · converge).
- **The 78/32 finding** (ATTTF): venues under 1,000 capacity host 78% of paid events, take 32%
  of ticketing revenue — aggregate bias as the economic twin of acreage bias; the
  normalised-view rule generalised from it.
- **The community's requirements register** (Vibe Setting Framework, *Seeing the System*,
  confidential): eight groups of design questions for a future sector map; three findings bind
  the chapter directly (beyond-buildings; redistribute-not-display; maintained-or-extractive).
