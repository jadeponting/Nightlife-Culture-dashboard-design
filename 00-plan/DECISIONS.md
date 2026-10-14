# Dashboard Design · decision log

*14 October 2026. The one place an open choice lives. The book is finished; its chapters state positions and leave trade-offs open for the build. This log gathers every open choice the book carries, gives each the book's steer, and names the moment the build will raise it. When that moment comes, look at the steer, use it or change it, and move on. Nothing here waits on anyone before then.*

**How it works**

- Each entry: the question, what rides on it, the options, the book's steer and why, what it touches, its status.
- Ordered by when the build will raise them: what the first screen raises comes first. None holds anything up; each is a question to answer when it comes up, with the book's steer in hand.
- Where a chapter states a position, the steer is that position, in the chapter's words where possible. Where the chapter states none, the steer is the book's reading of its own evidence and is marked [Proposal].
- When a choice is made: status becomes *Decided*, with the date and the words used. The chapter text it touches is edited once. Options not chosen are removed.
- Identifiers are `DB-nn` (Dashboard book), so they never collide with the Data Brain's `D-nn` or the register's `DD-nnn`.
- Where a probe in `03-tests/PROBES.md` already tests the choice, "Comes up when" names it.

**Where these came from.** The sixteen chapters' "Where the choice is yours" sections, read through the chapter writers' edit notes (`08-edit/edit-notes/chNN-NOTES.md`, section 3); Chapter 16 §11, the book's own index of open choices in nine groups; the 7 October list in `00-plan/STATE.md`; the chapters themselves for a position's wording; and the probe register. Choices that recur across chapters (the floors and the small room; the peer method; the one record; the length of the 60-second version) are merged into one entry each, with every chapter and rule they touch listed. Merged, they made 91 entries. Items the edit itself settled are listed at the end, with the reason each is not a decision, followed by the queries for the register.

---

## At a glance

| ID | The question | The book's steer | Comes up when |
|---|---|---|---|
| DB-01 | Which job is the dashboard for: monitoring, analysis or communication? | A communication and analysis object with a monitoring heartbeat | The first screen is designed |
| DB-02 | Whose grammar does the first screen speak, and is it one sentence or three? | Choose and declare it; keep the other grammars one step away; test with probe 48 | The first screen is designed |
| DB-03 | How much to frame, and is the plain table a first-class route? | Authored framing, honestly labelled; the plain table as a route, held as a hypothesis until probe 7 | The first screen is designed |
| DB-04 | Is the Vibe Map a justified dashboard (named reader, cadence, combination, resource)? | Answer it in the face sheet before the first screen [Proposal] | The first screen is designed |
| DB-05 | Which failures to prevent first? | Non-use and distrust first; aggregation and non-recognition second; the rest degrade | The first year's tests are chosen |
| DB-06 | How much mud to let in? | A judgement about the reader; the floor (never a blank where there is a reason) is Fixed | The first panel with a gap or an interval |
| DB-07 | Monetise, quantify or describe; which numbers does the investor see? | Do both and label which is which; the investor's numbers are Adaptable, showing the choice is Fixed | The first claim about value is written |
| DB-08 | Where does lived experience sit: panel, frame, or route to change? | Adaptable in form; the dialogue that can change the account is Fixed; the supplement panel is prohibited | The first felt panel is built |
| DB-09 | Is keeping the problem documented between windows the dashboard's job? | The dashboard holds the dated record; the report makes the argument [Proposal] | The first policy window closes |
| DB-10 | Is a trust question run at all, and in whose waves? | Run it, as probe 73, in the studio's own waves [Proposal] | The first reader survey is designed |
| DB-11 | Is reach measured by asking, of whom and how often; are the dashboard's own figures published? | Server counts are not reach; ask, and publish under Chapter 10's rule [Proposal on publishing] | The first period's use is reported |
| DB-12 | Which grain and which unit does the page land on? | The scene scale, declared, with the administrative unit beside it; the grain shown is named with its row count | The first table is designed |
| DB-13 | Which instant or window stands for a day; is 6pm to 6am the display's night? | Any boundary that suits its subject, stated, never changed silently; the official window is a definition only | The first series over time is computed |
| DB-14 | Which denominator to lead with? | The chosen base visible, alternatives reachable, a small base carries its interval | The first rate is published |
| DB-15 | Which concentration instrument, and are distributional figures weighted? | A median beside the mean at minimum; weight openly or not at all | The first distribution is shown |
| DB-16 | Is "not applicable" a seventh kind of nothing? | Hold six; mark "not applicable" as a labelled sub-kind until probe 15 is read [Proposal] | The first table with an inapplicable cell; probe 15 |
| DB-17 | How is a nothing shown, and what can the status chip say? | A design decision under Chapter 3's colour and word rules; the kind is named, the form is Decorative | The first empty cell is drawn; probe 15 |
| DB-18 | How much provenance and composition on the face, in what form, and does it fit a phone? | Period, status, the fact of caveats and the fact of composition at minimum; the rest one tap away; the form within Chapter 13's criteria | The first screen is designed; probe 13 |
| DB-19 | Suppress, round, band or perturb? | Suppression with secondary suppression, once per layer, declared | The first table with a withheld cell |
| DB-20 | What value does the disclosure floor take, per view? | The procedure is Fixed; the number is set per view before it ships: three for tables, five for online tools, higher where the scene can name the units | The first view ships |
| DB-21 | The floor of fifty against the small room: unmeasured or held, and who decides? | Present and unmeasured, never absent; the scene's governance decides; the layer's house name is open | The first felt panel for a small room |
| DB-22 | Does a withheld cell state its rule, and is the parameter published as policy? | The cell says the kind, never the parameter; publish the parameter once in the safeguards record [Proposal] | The first withheld cell is published; probe 44 |
| DB-23 | Which outlier rule and threshold? | Median absolute deviation at 2.5; written before the data arrives | The first series is checked |
| DB-24 | Which peer method, and how many peers? | Published and fixed before use; which it is, and the variables, are the studio's and the scene's | The first peer set is computed; probe 28 |
| DB-25 | How is a vague place drawn, and may readers draw their own unit? | Core and bands, thresholds the studio's; no reader-drawn units in the first version [Proposal on the second] | The first place with no administrative boundary; probe 55 |
| DB-26 | Which form: composite, dashboard, profile, user-weighted, longitudinal self-profile, hybrid? | Start as a profile; compose only after probes 20 and 21 [Proposal] | The first composite is computed, or declined |
| DB-27 | Which construct, which parts, and how is the measure audited? | Written first; each part carries provenance; the independent measure named in the measure record [Proposal on the audit] | Before the first measure is specified |
| DB-28 | Who sets the weights? | The scene, as one candidate; equal weights as the declared null until then [Proposal] | The first composite is computed; probe 21 |
| DB-29 | Which aggregation, and which tail? | Declare one; build it to find both tails [Proposal] | The first composite is computed |
| DB-30 | How is recognition gathered, who checks, in what forum, with what power to say no? | Chosen with the scene; the scene is among the competent; a "no" must be able to change the next release | Before the first release; probes 1, 2, 40 |
| DB-31 | Which register of a vibe is measured first, is the excess register scored, and whose bands? | Begin with any; the third shown as testimony, never scored; national or the scene's cut-points once line 6 says how | The first felt panel is built; probe 39 |
| DB-32 | Standard attribute words, the scene's own, or a hybrid? | The hybrid: structured items beside open questions; "vibrant" not as an item [Proposal] | The first felt question is drafted; probe 38 |
| DB-33 | Private or public self-placement? | Both, in that order, if wanted | The first self-placement is asked; probe 34 |
| DB-34 | How much of the co-produced layer is held, at what resolution, governed by whom, called what? | The scene's and the studio's together; recorded in lines 5 and 12; the name is open | The first contribution is held back; probe 46 |
| DB-35 | Show a trace or signal indicator before validation? | Either, if labelled "an indicator, unvalidated here" | The first indicator from a trace is shown |
| DB-36 | What form does "what this changed" take? | A dated line per contribution in the recognition record [Proposal] | The first contribution is answered; probe 36 |
| DB-37 | Which sense of resilience? | Name the sense beside the first figure that claims it; until then do not use the word [Proposal] | The first panel that uses the word |
| DB-38 | How long before a visitor is lost, and before a pattern is a finding? | A judgement about the scene's rhythm; Hill's close: no freedom to postpone, none to overclaim | The first return figure; the first pattern promoted |
| DB-39 | Which highlighting control, and how often may an alert be wrong? | The NHS frame; 371 is what three-sigma gives; set it with the people who answer the alarm, and print it | The first alert rule is written; probe 18 |
| DB-40 | Whether, and against what, to standardise a scene's rate? | The crude rate with its base first; standardise only where a declared peer comparison needs it [Proposal] | The first cross-place rate |
| DB-41 | How does the display order places? | All four forms satisfy the rule; which a first-time reader reads correctly is probe 26 | The first ordered panel; probes 26, 27 |
| DB-42 | The smoothing window, and which growth rate leads? | Either, declared; both ends of a year-on-year figure shown and the display says which leads | The first smoothed or year-on-year figure; probe 29 |
| DB-43 | Which design when a cause is wanted, and does the Vibe Map project at all? | The Magenta Book's table; showing no projection is legitimate; if shown, generic uplifts, a declared judgement, an even number of scenarios | The first causal claim or projection; probe 12 |
| DB-44 | Live or baked, panel by panel? | Nightly; one live element allowed under section 7's arithmetic | The first panel is built |
| DB-45 | Vector or raster; which map form; which tile supply? | A creative decision the book does not make; the twin must exist; the record states the supply chosen | The first map is built; probes 31, 32 |
| DB-46 | Which availability objective, and who answers when it is missed? | "Eleven months in twelve" is the example; no higher than readers can tell; a role with a second | Before launch; probe 30 |
| DB-47 | What notice on retiring a series, and what does the retirement plan hold? | The plan exists before launch; its period and content are the studio's | Before launch; the first series retired |
| DB-48 | Call the platform interfaces at all; is a free public page "commercial"? | The prototype's and Chapter 10's, with the terms open, recorded in line 2 | The first platform call is written |
| DB-49 | Which lawful basis, and what goes to counsel? | Lines 1 and 2 written first and dated; the research-and-statistics fit, the nameable business and information-law exposure go to counsel together | Before the first personal datum is processed |
| DB-50 | Registration for deeper views, and which views sit behind the door? | No door in the first version; the held layer is the answer to depth [Proposal] | The first request for a deeper view |
| DB-51 | The withdrawal tiers and the cut-off? | Three tiers is the biobank's, quarterly the illustration's; named before the first contribution | The first contribution; probe 47 |
| DB-52 | Host contributions at all? | Yes, under Chapter 10's conditions, and not before DB-34, DB-51 and DB-53 are written [Proposal] | The first contribution is invited |
| DB-53 | Which moderation adverbs? | Written in Grimmelmann's grammar before contributions open | The first contribution is invited |
| DB-54 | Is the assessment published, and under which ethics frame? | Publish, redacted [Proposal]; any frame, recorded as a Nightlife Culture rule that says which | The assessment is complete |
| DB-55 | What does the Vibe Map claim to be in the first fifty milliseconds, and which genre? | The creative decision the book never makes; the evidence layer passes the removal test in any genre | The first screen is designed |
| DB-56 | Which landing pattern, and which exemplar? | The evidence names none as best; written in face-sheet line 2, the exemplar declared an endorsement | The first screen is designed; probe 49 |
| DB-57 | How long is the headline sentence, and is it generated? | Five words where possible, ten at most, the official limits beside it; generated either way, checked and labelled | The first headline is written; probes 48, 50 |
| DB-58 | How much furniture before the sentence, and in what order? | The records' kinds appear as text; which, order and distance are the studio's | The first screen is designed; probe 48 |
| DB-59 | Which interactions, and whether to hover at all? | The purchase list is a procedure; a postcode box and a share button may be all; a redundant tooltip harms nobody | The first interaction is built; probe 4 |
| DB-60 | When and how are states frozen? | The standards say what a snapshot must do; the studio decides when | The first share or citation; probe 53 |
| DB-61 | Quantiles or natural breaks? | Either, declared and held constant across views of the same measure | The first choropleth; probe 54 |
| DB-62 | Which chart form, uncertainty form, and may an axis be broken? | Convention, schema and the comparison decide; bare intervals and hard boundaries prohibited; a broken axis is a chosen effect size, declared | The first chart; probe 12 |
| DB-63 | How many colours, how much text, how many significant figures? | Four or five colours as the UK bodies' limit, seven the ceiling; more text than designers give; two or three figures within the data's precision | The first chart; the design system's palette |
| DB-64 | Overview or search first; animation or small multiples; scroll or step; an editorial layer? | The arriving question, the task and the device decide; the editorial layer is free, above the dashboard | The first multi-panel view |
| DB-65 | How are the place-page's two columns composed? | Any composition keeping scales separate, space and finish equal, missed column first | The first place-page; probe 57 |
| DB-66 | Which identity fields, in what order; does the house classify places? | Order fixed and stated; fields and question in the data contract; whether to classify is open | The data contract is written; probe 58 |
| DB-67 | How much of the discovery layer exists? | Matching with content cues, or none; the money view's existence open; findability set with the forum | The first discovery feature; probe 45 |
| DB-68 | The five tests' pass numbers, and does the advocacy sentence wait on them? | The numbers are the studio's; the filled example withholds the sentence until the gate passes | The first place-page is tested |
| DB-69 | Which routes for the map beyond description and table, in what order? | Description and table are rules; the order after is the studio's | The first map ships; probe 61 |
| DB-70 | Which screen readers, browsers and platforms are tested with? | The WebAIM shares are the evidence; the Design System's list a precedent | The first accessibility test |
| DB-71 | Which sans serif, and which body size between 16 and 18 px? | The design system's tokens decide and record why | The design system's type scale |
| DB-72 | How does the reduced-motion page look? | Open, provided nothing crucial moved in the first place | The first animation |
| DB-73 | Which reading-level test? | The phone-read test first (probe 66); COGA's summary when the statement is written [Proposal] | The first screen is tested; probe 66 |
| DB-74 | Is the adviser's view sought now on the Act's duty, "funded" and partial compliance? | Yes, in the same brief as DB-49, before the statement is published [Proposal] | Before the accessibility statement |
| DB-75 | Are the boundary log, the deviation log and the producer's view public? | Publish by default (16.27); the working file in the repository, its existence declared on the page | The first deviation is logged; probe 74 |
| DB-76 | Is the committee export a separate deliverable or the stripped state of the page? | The stripped state of the same page [Proposal] | The first committee paper; probe 68 |
| DB-77 | Is a probe built for the two-audience claim? | Build it, after probe 68 [Proposal] | The first expressive form ships; probe 67 |
| DB-78 | Which expressive choices are free, which priced, and does it ship dark? | The Decorative tier is free within sections 5 and 10; invented forms, humanised marks and mood palettes are priced; dark ships with light and the reader chooses | The first expressive form is proposed; probe 69 |
| DB-79 | Are the records one document, and what is it called? | One record, kept in the repository, drawn into two views; "the one record of the dashboard" until the house names it [Proposal on the name] | The first record is written |
| DB-80 | Publish a statement in the regulator's voluntary form and ask to be listed? | Write it in the TQV form at the first release; ask to be listed after a year's record [Proposal] | The first release |
| DB-81 | Which of Chapter 15's mechanisms and instruments are adopted, and what stands in where conditions cannot be met? | An offer with terms, written in the precedent record; SMS as Adaptable; in the first years the data, its dates, its log and hand-written sentences | The first claim about value is labelled |
| DB-82 | ARG-12: re-base or retire? | Carried as disputed; Chapter 12's rule governs the build until the Decision Book is next edited [Proposal] | The first place-page |
| DB-83 | Accept the four direct-conflict readings? | Build to the readings; amend the Decision Book's text when next edited | The first panel each touches |
| DB-84 | The fifteen tensions: what interim rule does each gap take? | Chapter 16's interim rule becomes the design system's row; the joy-first register is DB-03 | The design system's first components |
| DB-85 | How does the Decision Book grow, and are the twelve candidates accepted? | A pointer to this book now, with the twelve candidates as rows [Proposal] | The Decision Book is next edited |
| DB-86 | What changes when the register and the legend are next reviewed? | Sensory experience as a tier of element; "open in the decision log" retired [Proposal]; the legend gains "Practice backed by analogous Evidence" | The register is next reviewed |
| DB-87 | Is a register of 280 Fixed rules short enough to be read and obeyed? | Truth 2 is the test; the first year measures it | The end of the first year; probe 75 |
| DB-88 | Which probes run first? | The small ones that need no build, and probe 48 before any default is fixed [Proposal] | The first probe is run |
| DB-89 | Who checks and owns DL-001? | The accessibility reviewer checks, against the 1.4.5 condition; the design system's owner owns [Proposal] | The first release's crop test |
| DB-90 | The length of the "60-second version" sections? | Keep the text and the name; the reader shows them open; cut only if a reader test shows the length loses readers [Proposal] | The first reader test of the book |
| DB-91 | Trim the template's restatement; add a figure to the chapters? | Leave as the book stands; the prototype's first screens become the figures [Proposal] | The first reader test of the book |

---

## A · Before the first screen is designed

The first screen raises these. Each is a choice about what the dashboard is for and whom it speaks to, and every later choice inherits it.

### DB-01 · Which job is the dashboard for: monitoring, analysis or communication?
- **Question.** Is the Vibe Map built to watch, to explain, or to persuade?
- **What rides on it.** The cadence, the depth of each panel, and what counts as the dashboard failing.
- **Options.**
    - Monitoring: a heartbeat of figures, refreshed on a cadence.
    - Analysis: figures with their reasons, for a reader who digs.
    - Communication: an authored account, for a reader who decides.
- **Steer.** "A public-interest dashboard is realistically a communication and analysis object with a monitoring heartbeat; a position, not a law" (Chapter 1 §10).
- **Touches.** Chapter 1 §10; Chapter 11 (the layers).
- **Status.** Open · 14 Oct 2026.

### DB-02 · Whose grammar does the first screen speak, and is it one sentence or three?
- **Question.** Which reader comes first on the first screen, and does the headline speak once or once per user group?
- **What rides on it.** Chapter 2's evidence is that the official reader's grammar will be used to discount the others, and the scene's to judge whether the thing is real. Chapter 2 asked whether one display can be legible to eight graders at all.
- **Options.**
    - The official reader's grammar first, the scene's reachable.
    - The scene's grammar first, the official reader's reachable.
    - One sentence for all, or three to choose between (Chapter 11; probe 48).
- **Steer.** "Adaptable in the choice, Fixed in declaring it" (Chapter 2 §11, rule 2.25). Chapter 16 §7 closes Chapter 2's doubt: Part 3 found a form that keeps the other grammars reachable one step away rather than on the face, so "the grammar of the first screen is chosen and declared". One sentence or three is tested by probe 48 before any default is fixed.
- **Touches.** Rule 2.25; Chapter 2 §11 and 60-second version; Chapter 11 §11; Chapter 16 §7 and §11.
- **Status.** Open · 14 Oct 2026.

### DB-03 · How much to frame, and is the plain table a first-class route?
- **Question.** Does the dashboard author its framing or offer a configurable surface; and for the reader who arrives opposed, is a plain-table view a route of its own?
- **What rides on it.** The joy-first register against the sceptic's table is the one of Chapter 16's fifteen tensions that "is a design question". Chapter 2 holds the plain table as a hypothesis, not a rule.
- **Options.**
    - Authored framing, honestly labelled (Chapter 1).
    - A configurable surface the reader frames.
    - A plain-table view as a first-class route for the opposed reader (rule 2.10), or the table twin alone (DD-001).
- **Steer.** "Authored framing, honestly labelled" (Chapter 1 §10). The plain-table route stays "a hypothesis to test" (Chapter 2 §11, rule 2.10) until probe 7 shows whether opposed readers choose the table; the twin exists either way.
- **Touches.** Chapter 1 §10; rules 2.10, 2.25; Chapter 16 §7 (the fifteenth tension); DD-001 (see Register queries).
- **Status.** Open · 14 Oct 2026.

### DB-04 · Is the Vibe Map a justified dashboard?
- **Question.** Does it have a named reader, a cadence, a combination of figures that must be seen together, and a resource to keep it running?
- **What rides on it.** Chapter 11's symmetry test: a dashboard that cannot answer these four is a report with a refresh button.
- **Options.**
    - Answer the four in the face sheet before the first screen.
    - Build and see.
- **Steer.** Answer the four in the face sheet before the first screen is designed; Chapter 1's reading (DB-01) already supplies the first two. Chapter 11 states no position. [Proposal]
- **Touches.** Chapter 11 working record (symmetry test); Chapter 1 §10.
- **Status.** Open · 14 Oct 2026.

### DB-05 · Which failures to prevent first?
- **Question.** In what order does the build guard against the ways a dashboard fails?
- **What rides on it.** The first year's tests and the order of the probe programme (DB-88).
- **Steer.** "The evidence ranks them: non-use and distrust kill a dashboard outright; aggregation and non-recognition kill its truth; the others degrade it; the order is the studio's" (Chapter 1 §10).
- **Touches.** Chapter 1 §10; Chapter 16 §9.
- **Status.** Open · 14 Oct 2026.

### DB-06 · How much mud to let in?
- **Question.** How much uncertainty, gap and uncounted thing does the face admit?
- **What rides on it.** A tidier face is read as more certain than the data is; a muddier one is read as less finished.
- **Steer.** "Where to set that dial is a judgement about the reader. Adaptable; the floor — never a blank where there is a reason — is Fixed" (Chapter 1 §10).
- **Touches.** Chapter 1 §10; Chapter 4 §6 (the six kinds of nothing); Chapter 3 (uncertainty forms, DB-62).
- **Status.** Open · 14 Oct 2026.

### DB-07 · Monetise, quantify or describe; which numbers does the investor see?
- **Question.** Does the dashboard put a pound sign on value, a count, or words; and for the investor, property value, footfall, business births or something else?
- **What rides on it.** The money view is what the official reader discounts by, and what the scene says is not the point. Each investor number tells a different story about the same place, and each is what another reader fears. Whether the money view exists at all is part of DB-67.
- **Options.**
    - Monetise; quantify without money; describe; or do both and label which is which.
    - For the investor: any of the three numbers, with the choice shown.
- **Steer.** "Do both and label which is which; the labelling is Fixed" (Chapter 2 §11, rule 2.4). The investor's numbers: "Adaptable; showing the choice is Fixed" (rule 2.18).
- **Touches.** Rules 2.4, 2.18; Chapter 6 (claims about value); Chapter 12 §12 (the money view and the rising-value panel); probe 45.
- **Status.** Open · 14 Oct 2026.

### DB-08 · Where does lived experience sit: panel, frame, or route to change?
- **Question.** Is the scene's account a panel beside the figures, the frame around them, or the route by which the figures are changed?
- **What rides on it.** A supplement panel is what Chapter 2 found the field does and prohibits: testimony shown and nothing changed.
- **Steer.** "Adaptable in form; the dialogue that can change the account is Fixed; the supplement panel is prohibited" (Chapter 2 §11, rule 2.22).
- **Touches.** Rule 2.22; Chapter 9 §15; Chapter 12 (the recognition record); DB-30.
- **Status.** Open · 14 Oct 2026.

### DB-09 · Is keeping the problem documented between windows the dashboard's job?
- **Question.** When the policy window closes, does the dashboard carry the record of the problem, or does a report?
- **What rides on it.** Chapter 2's finding that the problem has to be documented when nobody is asking, so that it is ready when someone is.
- **Options.**
    - The dashboard holds the dated record.
    - A report does, cited from the dashboard.
- **Steer.** The dashboard holds the dated record, since its snapshots and vintages exist for exactly this (Chapters 8 and 11); the report makes the argument when the window opens. Chapter 2 states no position. [Proposal]
- **Touches.** Rule 2.9; Chapter 8 (vintages); Chapter 11 (snapshots).
- **Status.** Open · 14 Oct 2026.

### DB-10 · Is a trust question run at all, and in whose waves?
- **Question.** Does the studio ask its readers whether they trust the display, and does it ask in its own survey or ride on someone else's?
- **What rides on it.** Distrust is one of the two failures that "kill a dashboard outright" (DB-05) and the book has no measure of it without asking. Register DD-033 carries this as its open part.
- **Options.**
    - Run it in the studio's own waves.
    - Add a question to a sector wave.
    - Do not run it.
- **Steer.** Run it, as probe 73 "Trust in the display itself", in the studio's own waves until a sector wave will carry it; Chapter 16 names "the two measurement rules for trust and use" among the Decision Book candidates. No chapter states a position. [Proposal]
- **Touches.** Rule 1.14; Chapter 1 §4; Chapter 15 §9; Chapter 16 §11; DD-033; probe 73.
- **Status.** Open · 14 Oct 2026.

### DB-11 · Is reach measured by asking, of whom and how often; are the dashboard's own figures published?
- **Question.** How does the studio know who the dashboard reached, and does it say?
- **What rides on it.** Chapter 15 found that server counts are reported as reach across the sector and are not reach. Chapter 11 notes that publishing the dashboard's own use "would be the first public evidence of its kind".
- **Steer.** "Server counts are not reach and are not reported as reach; the asking is the studio's" (Chapter 15 §9; Chapter 16 §7). Publish the result under Chapter 10's analytics rule, since nothing else in the field does and the book's own argument asks for it. [Proposal on publishing]
- **Touches.** Chapter 11 §11; Chapter 15 §9; Chapter 16 §7 and §11; probes 4, 72.
- **Status.** Open · 14 Oct 2026.

---

## B · The data

What the first table and the first withheld cell raise.

### DB-12 · Which grain and which unit does the page land on?
- **Question.** Venue, operator, room, event, night or person; and the scene scale or the administrative unit?
- **What rides on it.** Everything is counted at the grain shown; the unit decides which reader recognises the place and which can compare it (the MAUP; comparability over time for settlement-shaped units).
- **Steer.** "The one shown is named and its row count stated" (Chapter 4 §12, rule 4.1). "The scene scale is the house's declared choice; declared, with the administrative unit beside it and the cost recorded" (Chapter 12 §12).
- **Touches.** Rule 4.1; DD-021; Chapter 12 §3 and §12; Chapter 16 §11.
- **Status.** Open · 14 Oct 2026.

### DB-13 · Which instant or window stands for a day; is 6pm to 6am the display's night?
- **Question.** What rule assigns an event that crosses midnight to a date, and is the official night time window the display's?
- **What rides on it.** "When an activity has a daily rhythm, the instant or window chosen to stand for the day decides how much of the activity is counted" (Chapter 4 §3).
- **Steer.** "Any boundary that suits its subject, provided it is stated and never changed silently" (Chapter 4 §12, rule 4.3). The chapter "takes the window only as an official definition"; the display's rule may be any rule, written down.
- **Touches.** Rule 4.3; DD-078; Chapter 4 §3 and §13.
- **Status.** Open · 14 Oct 2026.

### DB-14 · Which denominator to lead with?
- **Question.** Residents, visitors, venues, area, or something else, under each rate?
- **Steer.** "The chosen base visible, alternatives reachable, a small base carries its interval" (Chapter 4 §12, rule 4.5).
- **Touches.** Rule 4.5; DD-020; DB-40.
- **Status.** Open · 14 Oct 2026.

### DB-15 · Which concentration instrument, and are distributional figures weighted?
- **Question.** How is the spread of a quantity shown, and may it be weighted by another value?
- **Steer.** "A median beside the mean is the minimum; showing none is not an option under truth 5" (Chapter 4 §12, rule 4.25). The display "may show the distribution unweighted or weight by another value; may not weight silently" (Chapter 6 §11).
- **Touches.** Rule 4.25; DD-089; Chapter 6 §11; probe 19.
- **Status.** Open · 14 Oct 2026.

### DB-16 · Is "not applicable" a seventh kind of nothing?
- **Question.** Every official scheme splits "not collected" into *not applicable* and *not asked*; the studio's six kinds do not. Add a kind, split the fifth, or mark a sub-kind?
- **What rides on it.** "A decision about the display's vocabulary" (Chapter 4 §12): every status chip, legend and record uses the kinds.
- **Options.**
    - A seventh kind.
    - Split the fifth kind (not collected) in two.
    - A labelled sub-kind of the fifth.
- **Steer.** Hold the six until probe 15 ("Which nothing reads as which") has been read with readers; until then mark "not applicable" as a labelled sub-kind of *not collected*, so the vocabulary does not grow before the test. Chapter 4 states no position. [Proposal]
- **Touches.** Rule 4.14; DD-083; Chapter 4 §6 and §12; Chapter 16 §11; probe 15 (P-034, P-042).
- **Status.** Open · 14 Oct 2026.

### DB-17 · How is a nothing shown, and what can the status chip say?
- **Question.** Code, word, pattern or sentence; blank, hatched or annotation; and can one chip carry what six chapters ask of it (the kind of nothing; a robustness mark; the kind of claim; the comparison's terms; "indicator, unvalidated here"; held distinct from withheld)?
- **Steer.** "A design decision under Chapter 3's colour and word rules and the design system" (Chapter 4 §12). The holes' form on the place-page "is Decorative provided the kind is named" (Chapter 12 §12). The chip is the first of Chapter 16's fifteen tensions and owes an interim rule (DB-84).
- **Touches.** DD-015 (open part); Chapter 4 §12; Chapter 12 §12; Chapter 16 §7; probes 15, 16.
- **Status.** Open · 14 Oct 2026.

### DB-18 · How much provenance and composition on the face, in what form, and does it fit a phone?
- **Question.** What of the record, and of a composed number's recipe card, sits on the face of every panel; how is it set inside the frame (footer strip, margin block, stamp); and is it legible at phone size?
- **What rides on it.** The crop test: panels shared as screenshots lose their title, unit, source and date (DL-001). Chapter 12's in-frame rule is a departure from official practice.
- **Steer.** "Period, status and the fact that caveats exist at minimum; the rest one tap away" (Chapter 4 §12, rule 4.7). For a composed number, "the fact of composition and the existence of the card, at minimum; the rest is Chapter 11's layout decision" (Chapter 5 §14). "The departure from official practice is the chapter's rule; its form is open within Chapter 13's criteria" (Chapter 12 §12). Chapter 13 finds the criteria met and leaves legibility to the prototype.
- **Touches.** Rule 4.7; DD-005; DD-006; Chapter 5 §12 and §14 (DD-112); Chapter 12 §12; Chapter 13 §7 and §11; DL-001; probe 13; DB-89.
- **Status.** Open · 14 Oct 2026.

### DB-19 · Suppress, round, band or perturb?
- **Question.** By which method is a small cell protected, and is it the same across views?
- **Steer.** "The Decision Book chooses suppression with secondary suppression; made once and declared" (Chapter 4 §12, rule 4.18). "Once per layer, declared, consistent across views" (Chapter 10 §19, rule 10.7).
- **Touches.** Rules 4.18, 10.7; DD-015; Chapter 16 §7 tier table.
- **Status.** Open · 14 Oct 2026.

### DB-20 · What value does the disclosure floor take, per view?
- **Question.** Below what count is a cell withheld, in each view, and who sets it?
- **What rides on it.** The floor is what makes the small cells a local reader needs disappear; set too high it empties the map, too low it names people.
- **Options.**
    - Three, the static-table convention.
    - Five, the office's suggestion for online tools.
    - Higher, where the scene can name the units.
- **Steer.** "The procedure is Fixed; the number is the studio's, per view, and stated" (Chapter 10 §19, rule 10.5). Chapter 6: "the procedure in section 11 is fixed; its number is not". Chapter 16's register carries it as Fixed (sequence), "set per view before it ships; value Adaptable".
- **Touches.** Rule 10.5; Chapter 6 §11; Chapter 1 §10; Chapter 16 §7; probes 41, 42, 43.
- **Status.** Open · 14 Oct 2026.

### DB-21 · The floor of fifty against the small room: unmeasured or held, and who decides?
- **Question.** A felt measure for a room with fewer than fifty answers is not published. Is such a room shown as unmeasured or as held, who decides, and what does the house call the held layer?
- **What rides on it.** Most of the scene's rooms are small. Shown as absent they vanish; shown as held they look hidden.
- **Steer.** "A room under the floor is shown as present and unmeasured, never as absent" (Chapter 9 truth 3). "Who decides which of 'unmeasured' or 'held' is shown is the scene's governance under Chapter 10's record" (Chapter 16 §7); "the house's name for the layer is open" (Chapter 16 §11). The precision floor itself is a requirement with Chapter 9's value as the house default.
- **Touches.** Chapter 9 §15 and truth 3; Chapter 10 §5 "Two floors" and §14; Chapter 16 §7 and §11; Chapter 1 §10; Chapter 12 §12; probe 15; DB-34.
- **Status.** Open · 14 Oct 2026.

### DB-22 · Does a withheld cell state its rule, and is the parameter published as policy?
- **Question.** Does the cell say "withheld" or "withheld under five", and does the safeguards record publish the number?
- **Steer.** "The cell says the kind, never the parameter; publication is the house's" (Chapter 16 §7). Publish the parameter once, in the safeguards record's public view, since a reader who can find the rule can find the number anyway and the record is where Chapter 10 puts it. Chapter 10 states no position. [Proposal]
- **Touches.** Chapter 10 §6, §7 and §19; DD-255; DD-010; Chapter 16 §7 and §8; probe 44.
- **Status.** Open · 14 Oct 2026.

### DB-23 · Which outlier rule and threshold?
- **Steer.** "Median absolute deviation and 2.5 as the literature's default; rule written before the data arrives" (Chapter 4 §12, rule 4.32).
- **Touches.** Rule 4.32; DD-094; rule 1.13 and DD-030 (see Register queries).
- **Status.** Open · 14 Oct 2026.

### DB-24 · Which peer method, and how many peers?
- **Question.** CIPFA nearest neighbours, the ONS classification, a bespoke set, or none; twenty by Euclidean distance, ten with closeness labels, or the studio's own?
- **What rides on it.** A field of twenty-odd districts; the peer set is the comparison every other panel inherits, and its variables must not include the thing compared.
- **Steer.** "The method is published and fixed; which it is, and the variables, are the studio's and the scene's judgement" (Chapter 7 §12). Chapter 4: "open; must be shown; variables must not include the thing compared". Chapter 12 carries it unchanged.
- **Touches.** Rule 4.24; DD-088; Chapter 7 §12 (first choice); Chapter 12 §12; Chapter 16 §11; probe 28.
- **Status.** Open · 14 Oct 2026.

### DB-25 · How is a vague place drawn, and may readers draw their own unit?
- **Question.** Core and bands for a scene with no administrative boundary; and can a reader outline an area and get figures for it?
- **What rides on it.** A reader-drawn unit costs "a disclosure check at query time (Chapter 10's walk) for every drawn area; the ONS does it" (Chapter 12 §12).
- **Steer.** "Core and bands; thresholds (25/50/75 are one precedent) and n are the studio's" (Chapter 12 §12). Reader-drawn units not in the first version: the walk (probe 42) does not yet exist; revisit once the held layer and the intruder walk are built. Chapter 12 states no position on the second beyond the cost. [Proposal on the second]
- **Touches.** Chapter 12 §12; Chapter 10 §7; Chapter 16 §11; probes 42, 55.
- **Status.** Open · 14 Oct 2026.

---

## C · The measure

What the first composite and the first felt panel raise.

### DB-26 · Which form: composite, dashboard, profile, user-weighted, longitudinal self-profile, hybrid?
- **Question.** Is the vibe one number, a set, a profile, or something the reader weights?
- **What rides on it.** A composite is what decision-makers are said to want and what hides a failing part; a profile keeps the parts visible and is harder to quote.
- **Steer.** "Whichever is chosen, the components travel with it" (Chapter 5 §14). The chapters after 5 "added no evidence that one form is read better than another" (Chapter 16 §7). Start as a profile, which every form reduces to, and compose only once probes 20 (sensitivity) and 21 (what the weights really do) have been run on real data. [Proposal]
- **Touches.** Chapter 5 §11 and §14; Chapter 16 §7 and §11; probes 20, 21.
- **Status.** Open · 14 Oct 2026.

### DB-27 · Which construct, which parts, and how is the measure audited?
- **Question.** What the measure is of, which parts compose it, and against which independent measure, how often and by whom it is checked.
- **Steer.** "The framework is the studio's and the scene's; the rule is only that it is written first and each part carries Chapter 4's provenance" (Chapter 5 §14). The audit is "designed with the measure" (Chapter 5 §7); name the independent measure in the measure record before the first composite is computed, with Chapter 9's descriptor validation as the first candidate. [Proposal on the audit]
- **Touches.** Chapter 5 §7 and §14; rule 5.1 (DD-019); Chapter 9 §15; probes 22, 37.
- **Status.** Open · 14 Oct 2026.

### DB-28 · Who sets the weights?
- **Question.** Statistics, experts, the public, the reader, or equal weights as a declared null?
- **Steer.** "Each is defensible; each is declared; none is neutral" (Chapter 5 §14). The illustration names the scene as one candidate, on the studio's own position and Sen's argument. Until the scene has set them, equal weights as the declared null. [Proposal on the interim]
- **Touches.** Chapter 5 §14 and §15; rule row 4; probe 21.
- **Status.** Open · 14 Oct 2026.

### DB-29 · Which aggregation, and which tail?
- **Question.** Additive with its price list, geometric, power mean, non-compensatory, or none; and is the measure built to find shortfall, excess, or what thrives?
- **Steer.** None stated beyond the menu (Chapter 5 §5, §14, §15; Chapter 16 §11). Declare one before the first composite is computed, and build it to find both tails: Chapter 1's positive-deviance probe (probe 5) needs the thriving tail as much as the alerts need the struggling one. [Proposal]
- **Touches.** Chapter 5 §5, §14, §15; rule rows 6 and 8; Chapter 16 §11; probe 5.
- **Status.** Open · 14 Oct 2026.

### DB-30 · How is recognition gathered, who checks, in what forum, with what power to say no?
- **Question.** Member checks of fact, a synthesised late check, a deliberative choice of parts, or all three; who does the member checking and how often; what form the review takes (room, sheet, data walk, online draft) and where the errors channel sits; who the competent are.
- **What rides on it.** Recognition is one of the Vibe Map's four tests. "Anything less is a nod" (Chapter 2).
- **Steer.** "Chosen with the scene" (Chapter 12 §12). "The scene is among them; the rest is not answerable from a desk" (Chapter 6 §11). The dialogue must be able to change the next release (rule 2.22; DD-018). Chapters 5 and 9 state no further position.
- **Touches.** Chapter 5 §14; Chapter 6 §11; Chapter 9 §15; Chapter 12 §12; rules 2.22, 9.33 (DD-018); probes 1, 2, 40.
- **Status.** Open · 14 Oct 2026.

### DB-31 · Which register of a vibe is measured first, is the excess register scored, and whose bands?
- **Question.** Which of the three registers goes first; whether the third is ever scored; the national cut-points or the scene's own.
- **Steer.** "Begin with any; the third may be shown as testimony and never scored; the choice is named in record line 1" (Chapter 9 §15). Bands: "either is defensible once line 6 says how they were chosen" (Chapter 9 §15).
- **Touches.** Chapter 9 §15 (first and sixth items); Chapter 16 §11; probe 39.
- **Status.** Open · 14 Oct 2026.

### DB-32 · Standard attribute words, the scene's own, or a hybrid?
- **Question.** And is "vibrant" used at all, given it is a derived diagonal on the least evenly read axis?
- **Steer.** None stated ("this book does not make it"); the destination-image hybrid is named as precedent (Chapter 9 §15). Take the hybrid, structured items beside open questions, and do not use "vibrant" as an item; probe 38 tests whether the words are read as intended. [Proposal]
- **Touches.** Chapter 9 §15; STATE 7 Oct; probe 38.
- **Status.** Open · 14 Oct 2026.

### DB-33 · Private or public self-placement?
- **Steer.** "Private is a measure, public a conversation; both, in that order, if wanted" (Chapter 9 §15).
- **Touches.** Chapter 9 §15; probe 34.
- **Status.** Open · 14 Oct 2026.

### DB-34 · How much of the co-produced layer is held, at what resolution, governed by whom, called what?
- **Question.** What is community-held and not published; at what resolution the held layer sits; whether a forum, a convened panel or a public body's list governs it; and what the house calls it.
- **Steer.** "The scene's and the studio's together" (Chapter 10 §19, rule 10.34); "handed to Chapter 10's scene-level consent; recorded in record lines 5 and 12 whichever way" (Chapter 9 §15). The name is open (Chapter 16 §11). The held layer as a status with a decider, resolution, reason and review date is one of the fifteen tensions (DB-84).
- **Touches.** Rule 10.34; Chapter 9 §15; Chapter 10 §14; Chapter 16 §7 and §11; probe 46; DB-21.
- **Status.** Open · 14 Oct 2026.

### DB-35 · Show a trace or signal indicator before validation?
- **Steer.** "Either, if labelled 'an indicator, unvalidated here' with Chapter 4's provenance; the label is required, not the choice" (Chapter 9 §15).
- **Touches.** Chapter 9 §15; Chapter 16 §11; probe 35.
- **Status.** Open · 14 Oct 2026.

### DB-36 · What form does "what this changed" take?
- **Question.** Chapter 9 §6 says what the field must do and hands its design on.
- **Steer.** A dated line per contribution in the recognition record: what was said, what changed, or why nothing did. The Sjoberg evidence is that people contribute again when they can see the answer; probe 36 ("You said, we did") tests it. [Proposal]
- **Touches.** Chapter 9 §6 and §15; rule 9.17; Chapter 12 (the recognition record); probe 36.
- **Status.** Open · 14 Oct 2026.

---

## D · Claims about value, comparison and time

What the first trend, the first alert and the first comparison raise.

### DB-37 · Which sense of resilience?
- **Question.** Bounce back, absorb, or adapt?
- **Steer.** The chapter does not choose (Chapter 6 §11). Name the sense beside the first figure that claims it; until a figure does, do not use the word on the face. [Proposal]
- **Touches.** Chapter 6 §11.
- **Status.** Open · 14 Oct 2026.

### DB-38 · How long before a visitor is lost, and before a pattern is a finding?
- **Question.** What counts as a return and how long before a visitor is "lost"; how long a pattern waits before promotion.
- **Steer.** "The window is a judgement about the scene's rhythm" (Chapter 6 §11). "Hill's close: no freedom to postpone, no freedom to overclaim" (Chapter 6 §11).
- **Touches.** Chapter 6 §11; probe 25.
- **Status.** Open · 14 Oct 2026.

### DB-39 · Which highlighting control, and how often may an alert be wrong?
- **Question.** Family-wise or false-discovery control for what the display highlights; and the average run length before a false alarm.
- **Steer.** "Neither literature says; the NHS frame, 'decide the run-length based on how frequently you want to ask questions', is the right one. 371 is what three-sigma limits give; set it with the people who will answer the alarm, and print it" (Chapter 6 §11).
- **Touches.** Chapter 6 §11; probe 18.
- **Status.** Open · 14 Oct 2026.

### DB-40 · Whether, and against what, to standardise a scene's rate?
- **Steer.** None stated; "a choice about which misreading is worse" (Chapter 7 §12). Lead with the crude rate and its base (DB-14); standardise only where a declared peer comparison needs it, and say against what. [Proposal]
- **Touches.** Chapter 7 §12; rule 4.5.
- **Status.** Open · 14 Oct 2026.

### DB-41 · How does the display order places?
- **Question.** Funnel by size; distribution with the place marked; peer set in closeness order; unsorted small multiple?
- **Steer.** "All satisfy the rule; which a first-time reader reads correctly is to be tested" (Chapter 7 §12; probe 26). The form for position against limits, and when a sorted bar is and is not a league table, is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 7 §12; Chapter 16 §7; probes 26, 27.
- **Status.** Open · 14 Oct 2026.

### DB-42 · The smoothing window, and which growth rate leads?
- **Steer.** Smoothing and the latest smoothed point: "Either, declared" (Chapter 7 §12). Growth: "Fixed that both ends of a year-on-year figure are shown and the display says which leads; which leads is the choice" (Chapter 7 §12).
- **Touches.** Chapter 7 §12 (fourth and fifth choices); probe 29.
- **Status.** Open · 14 Oct 2026.

### DB-43 · Which design when a cause is wanted, and does the Vibe Map project at all?
- **Question.** The evaluation design when a causal claim is wanted; whether to show a projection; how much to adjust for optimism; how many scenarios.
- **Steer.** "The Magenta Book's feasibility table is the decision aid" (Chapter 7 §12). Showing no projection is "a legitimate answer to section 9, and the studio's" (Chapter 7 §12; Chapter 16 §7). If shown: "generic uplifts for costs and durations until the studio has a record, a declared judgement for benefits; an even number of scenarios as the default".
- **Touches.** Chapter 7 §9 and §12; Chapter 2 (the empty place for a comparison group); Chapter 16 §11; probes 8, 12.
- **Status.** Open · 14 Oct 2026.

---

## E · Running it

What the first panel built, the first map and the first alert raise.

### DB-44 · Live or baked, panel by panel?
- **Steer.** "The chapter's architecture is nightly; one live element is allowed if it accepts the chain arithmetic of section 7 with its own dependency line, and the rest of the page does not depend on it" (Chapter 8 §12).
- **Touches.** Chapter 8 §7 and §12; probe 30.
- **Status.** Open · 14 Oct 2026.

### DB-45 · Vector or raster; which map form; which tile supply?
- **Question.** Vector or raster for the face, given the renderer is over two-fifths of the script budget; choropleth with inset, hex tiles, cartogram, dots, or no map; which of the four tile supplies.
- **Steer.** "A creative decision and this book does not make it; the twin must exist either way" (Chapter 8 §12). "A design decision within Chapter 8's budget" (Chapter 11 §11). For the tiles, "the record states which was chosen and what was agreed to" (Chapter 8 §12). A raster or static fallback and the twin-table component is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 8 §12; Chapter 11 §11; Chapter 16 §7; DD-001; service record line 2; probes 31, 32.
- **Status.** Open · 14 Oct 2026.

### DB-46 · Which availability objective, and who answers when it is missed?
- **Question.** The objective and its error budget; who reads the ticket and who is second.
- **Steer.** "'Eleven months in twelve' is the chapter's example; set it no higher than readers can tell, and write it down before launch" (Chapter 8 §12). "A role, with a second; which role, at what hours, is an organisational choice." Two facts to find before the number is set, not assumed: whether the refresh job's own commits count as repository activity for the sixty-day disabling, and whether any availability commitment attaches to the free hosting tiers (Chapter 8 §7 and §8).
- **Touches.** Chapter 8 §7, §8, §12; service record line 5; probes 30, 33.
- **Status.** Open · 14 Oct 2026.

### DB-47 · What notice on retiring a series, and what does the retirement plan hold?
- **Question.** The notice period; the archive, licence, successor and gap analysis.
- **Steer.** "None fixed; it must be written in line 8 before the first series needs it" (Chapter 8 §12). "The plan exists before launch (truth 7); the content is the studio's" (Chapter 15 §9). Chapter 16's register: the plan Fixed (sequence), its period and content Adaptable.
- **Touches.** Chapter 8 §12; Chapter 15 §9; Chapter 16 §7 and §11; P-174 (the vintage naming rule).
- **Status.** Open · 14 Oct 2026.

### DB-48 · Call the platform interfaces at all; is a free public page "commercial"?
- **Question.** Spotify III.13, Ticketmaster's non-user-driven calls, Skiddle non-commercial: does the studio call any of them, and does a free public page fall under "commercial"?
- **Steer.** "The decision is the prototype's and Chapter 10's, made with the terms open and recorded in line 2" (Chapter 8 §12, rule 8.11). The legal reading "is a question for line 2 of the service record with the clause quoted" (Chapter 8 §6).
- **Touches.** Rule 8.11; Chapter 8 §6 and §12; Chapter 16 §11; probes 17, 22.
- **Status.** Open · 14 Oct 2026.

---

## F · Safeguards and consent

What the first personal datum and the first contribution raise.

### DB-49 · Which lawful basis, and what goes to counsel?
- **Question.** Which lawful basis is claimed; whether the research and statistics provisions are claimed at all ("a dashboard is not a research project"; the money view as "measures"); what is owed to a nameable business beyond confidentiality; and whether a public-body partner holding the held layer, the walk's claims or the assessment can be made to release them under information law.
- **Steer.** "Record lines 1 and 2 are written first and line 2 dated" (Chapter 10 §19, rules 10.18, 10.20). The research-and-statistics fit is "for counsel" (Chapter 10 §9); defamation and commercial harm are "not researched; for counsel" (§5); the information-law question is "asked before it holds them" (§4). Put the three to counsel in one brief, with DB-74's accessibility questions beside them.
- **Touches.** Rules 10.18, 10.20; Chapter 10 §4, §5, §9, §19; Chapter 16 §11; safeguards record lines 1 and 2.
- **Status.** Open · 14 Oct 2026.

### DB-50 · Registration for deeper views, and which views sit behind the door?
- **Steer.** None; "a design decision the chapter leaves" (Chapter 10 §19, rule 10.11). No door in the first version: the held layer (DB-34), not a login, is the book's answer to depth, and a door would make the official reader the only one who registers. [Proposal]
- **Touches.** Rule 10.11; Chapter 10 §7; DB-34.
- **Status.** Open · 14 Oct 2026.

### DB-51 · The withdrawal tiers and the cut-off?
- **Steer.** "Three tiers is the biobank's, quarterly the illustration's; named before the first contribution and told at it" (Chapter 10 §19, rule 10.32).
- **Touches.** Rule 10.32; Chapter 10 §13; probe 47.
- **Status.** Open · 14 Oct 2026.

### DB-52 · Host contributions at all?
- **Question.** If so, the Online Safety Act's duties at a small service's scale follow.
- **Steer.** None; "the chapter says what follows if it does" (Chapter 10 §19, rule 10.27). Yes, under Chapter 10's conditions, because the recognition route (DB-30) and "what this changed" (DB-36) need a way in; but not before the held layer (DB-34), the withdrawal tiers (DB-51) and the moderation adverbs (DB-53) are written. [Proposal]
- **Touches.** Rule 10.27; Chapter 10 §10 and §19; Chapter 16 §11.
- **Status.** Open · 14 Oct 2026.

### DB-53 · Which moderation adverbs?
- **Steer.** "Automatic or manual, transparent or secret, before or after, central or distributed — Grimmelmann's grammar is complete and the sentence is the studio's" (Chapter 10 §16, rule 10.39). Written before contributions open, with the gating form priced rather than excluding.
- **Touches.** Rule 10.39; Chapter 10 §16 and §19.
- **Status.** Open · 14 Oct 2026.

### DB-54 · Is the assessment published, and under which ethics frame?
- **Question.** Whether the data protection impact assessment is public, redacted, or on file; and which ethics frame the house adopts as a stance.
- **Steer.** "Good practice per the regulator; the walker's claims a reason to publish redacted; the studio decides what is public and what is on file" (Chapter 10 §19, rule 10.23). Publish, redacted: the regulator's good practice and Chapter 16's publish-by-default (DB-75) point the same way. [Proposal] The frame: "any; recorded as a Nightlife Culture rule and says which" (Chapter 10 §19).
- **Touches.** Rule 10.23; Chapter 10 §9, §17, §19; Chapter 16 §11; rule 16.27.
- **Status.** Open · 14 Oct 2026.

---

## G · The first screen and the surface

What the first screen, the first chart and the first place-page raise.

### DB-55 · What does the Vibe Map claim to be in the first fifty milliseconds, and which genre?
- **Question.** Dashboard, map, flyer, other; and the club-flyer question Chapter 14 set out and stopped at.
- **What rides on it.** What a thing resembles decides how it is read before a word is read (Chapter 3 §14). The genre is "Priced" in Chapter 14's register.
- **Steer.** "The creative decision this book never makes; the studio's" (Chapter 3 §14). "Adaptable; the house's to choose; the evidence layer passes the removal test in any genre" (Chapter 14 §11, rule 14.15).
- **Touches.** Chapter 3 §14 and §15; DD-068; rule 14.15; Chapter 16 §11.
- **Status.** Open · 14 Oct 2026.

### DB-56 · Which landing pattern, and which exemplar?
- **Steer.** "The evidence names none as best; the choice must be made, written in face-sheet line 2, the exemplar declared an endorsement" (Chapter 11 §11).
- **Touches.** Chapter 11 §11; Chapter 16 §11; probe 49.
- **Status.** Open · 14 Oct 2026.

### DB-57 · How long is the headline sentence, and is it generated?
- **Question.** The house rule (five words, ten at most) or the official limits (fifteen words, sixty characters); whether a sentence is generated per place, and whether a generated one is held to the poster rule.
- **Steer.** Chapter 16's register: "Adaptable (house default), the official limits beside it; five words where possible, ten at most" (illustrative row DD-008). Chapter 14: "set by distance and seconds rather than a word count; the count is the house's" (rules 14.13, 14.14, which supersede 11.4; see Register queries). Generation: "either; any generated sentence checked and labelled" (Chapter 11 §11); a label for generated text is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 11 §11; rules 11.4, 14.13, 14.14; DD-004; Chapter 16 §7 and §8; probes 48, 50.
- **Status.** Open · 14 Oct 2026.

### DB-58 · How much furniture before the sentence, and in what order?
- **Steer.** "That the records' kinds appear on the face as text is Fixed; which, order and distance are the studio's" (Chapter 11 §11). Probe 48 measures how much furniture sits above the sentence before a reader skips.
- **Touches.** Chapter 11 §11; DB-18; probe 48.
- **Status.** Open · 14 Oct 2026.

### DB-59 · Which interactions, and whether to hover at all?
- **Steer.** "The purchase list is a procedure; a dashboard may ship with a postcode box and a share button and nothing else" (Chapter 11 §11). "A redundant, keyboard-reachable tooltip harms nobody; the label at the mark may be enough." The filter set as a query system is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 11 §11; rules 11.21, 11.22 (DD-001); Chapter 16 §7; probe 4.
- **Status.** Open · 14 Oct 2026.

### DB-60 · When and how are states frozen?
- **Question.** Each release; on request; on share.
- **Steer.** "The standards say what a snapshot must do; the studio decides when and how" (Chapter 11 §11). A dated snapshot and generated citation is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 11 §11; Chapter 16 §7; probe 53.
- **Status.** Open · 14 Oct 2026.

### DB-61 · Quantiles or natural breaks?
- **Steer.** "Either, once declared and held constant across views of the same measure; a change of measure or population is a new legend" (Chapter 11 §11). Map breaks held across filters is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 11 §11; Chapter 16 §7; probe 54.
- **Status.** Open · 14 Oct 2026.

### DB-62 · Which chart form, which uncertainty form, and may an axis be broken?
- **Steer.** Chart form: "convention, the reader's schema, and the comparison you want made do … a donut is not worse than a pie; a treemap is defensible for part-of-whole with labels; a radial bar is six times slower" (Chapter 3 §14). Uncertainty: "depends on the question and the reader; the prohibition on bare intervals and hard boundaries is Fixed". Axis: "Permitted, and a chosen effect size; declare it."
- **Touches.** Chapter 3 §14 (first, fifth and sixth paragraphs); probe 12.
- **Status.** Open · 14 Oct 2026.

### DB-63 · How many colours, how much text, how many significant figures?
- **Steer.** Colours: "seven is the experimental ceiling for search; four or five is the house limit of the UK statistics bodies … a design-system decision informed by section 4" (Chapter 3 §14). Text: "more than designers give and the trend in the title; how much more, and in what voice, is the studio's." Figures: "two or three, by column, is a judgement. Adaptable within the Fixed ceiling of the data's own precision."
- **Touches.** Chapter 3 §4 and §14 (second, third and eighth paragraphs); Chapter 10 (the stigma test in colour rules); probe 10.
- **Status.** Open · 14 Oct 2026.

### DB-64 · Overview or search first; animation or small multiples; scroll or step; an editorial layer?
- **Steer.** "The reader's arriving question, the task, and the device decide; none is a law" (Chapter 3 §14). Scrollytelling and the editorial layer: "free, above the dashboard, carrying its states and snapshots" (Chapter 11 §11). The small screen named as the first version is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 3 §14; Chapter 11 §11; Chapter 16 §7.
- **Status.** Open · 14 Oct 2026.

### DB-65 · How are the place-page's two columns composed?
- **Steer.** "Side by side is the logical relation, not necessarily the layout; any composition keeping scales separate, space and finish equal, missed column first is open" (Chapter 12 §12).
- **Touches.** Chapter 12 §12; probe 57.
- **Status.** Open · 14 Oct 2026.

### DB-66 · Which identity fields, in what order; does the house classify places?
- **Question.** The profile's fields, their order and the question they answer; the house's type labels, and whether it classifies at all.
- **Steer.** "Order fixed and stated; fields and question are the house's, recorded in the data contract" (Chapter 12 §12). Labels "written by the classifier's rule; whether the house classifies at all is a choice the chapter does not make."
- **Touches.** Chapter 12 §12 (fifth and sixth items); the prototype data contract; probes 1, 58.
- **Status.** Open · 14 Oct 2026.

### DB-67 · How much of the discovery layer exists?
- **Question.** Matching with content cues; the money view; which categories are findable.
- **Steer.** "Matching with content cues, or no discovery at all; the money view's existence open; findability set with the forum" (Chapter 12 §12).
- **Touches.** Chapter 12 §12; rule 12.26; DB-07; probe 45.
- **Status.** Open · 14 Oct 2026.

### DB-68 · The five tests' pass numbers, and does the advocacy sentence wait on them?
- **Steer.** "The numbers are the studio's to set" (Chapter 12 §10). The filled example withholds the advocacy sentence until a gate passes without harmonisation, "marked as a choice the studio would make" (Chapter 12 §11).
- **Touches.** Chapter 12 §10 and §11; probes 56 to 60.
- **Status.** Open · 14 Oct 2026.

---

## H · Access

What the first accessibility test and the statement raise.

### DB-69 · Which routes for the map beyond description and table, in what order?
- **Question.** A navigable structure, an audio route, a "where" route, and when.
- **Steer.** "Description and table are rules; the order after the first two is the studio's" (Chapter 13 §11).
- **Touches.** Chapter 13 §11; Chapter 16 §11; probes 61, 62, 64.
- **Status.** Open · 14 Oct 2026.

### DB-70 · Which screen readers, browsers and platforms are tested with?
- **Steer.** "The WebAIM shares (JAWS, NVDA, VoiceOver; nine in ten on mobile) are the evidence; the Design System's list is a precedent" (Chapter 13 §11).
- **Touches.** Chapter 13 §11; rule 13.26 (DD-319).
- **Status.** Open · 14 Oct 2026.

### DB-71 · Which sans serif, and which body size between 16 and 18 px?
- **Question.** Against the 18-point finding and the BDA's 12 to 14.
- **Steer.** "A sans serif at a measured size; the design system's tokens decide and record why" (Chapter 13 §11). The body size against the 18-point finding is one of the fifteen tensions (DB-84).
- **Touches.** Chapter 13 §5 and §11; Chapter 16 §7 and §11.
- **Status.** Open · 14 Oct 2026.

### DB-72 · How does the reduced-motion page look?
- **Steer.** "Open, provided nothing crucial moved in the first place" (Chapter 13 §11).
- **Touches.** Chapter 13 §11; rule 13.17 (DD-047, open part).
- **Status.** Open · 14 Oct 2026.

### DB-73 · Which reading-level test?
- **Question.** The phone-read test, COGA's lower-secondary summary, or both.
- **Steer.** None stated (Chapter 13 §11). The phone-read test first, since probe 66 exists for it and runs on the first screen; COGA's summary when the statement is written. [Proposal]
- **Touches.** Chapter 13 §11; probe 66.
- **Status.** Open · 14 Oct 2026.

### DB-74 · Is the adviser's view sought now on the Act's duty, "funded" and partial compliance?
- **Question.** What the Act's duty asks of the studio; what "funded" covers under the Regulations; whether a published statement of partial compliance has consequences for a body not bound.
- **Steer.** "The chapter reports and does not advise" (Chapter 13 §11). Yes: put the three questions in the same brief as DB-49's, before the accessibility statement is published, since the statement's wording depends on the answers. [Proposal]
- **Touches.** Chapter 13 §4 and §11; Chapter 16 §11; rule 13.23 (the statement).
- **Status.** Open · 14 Oct 2026.

---

## I · Expression

What the first expressive form raises.

### DB-75 · Are the boundary log, the deviation log and the producer's view of the one record public?
- **Question.** Published in whole, in part by line as the safeguards record does, or declared on the page and kept in the repository.
- **Steer.** "The regimes publish by default; rule 16.27 'Adaptable (house default: publish)'" (Chapter 16 §7). The boundary log's working file "may want to live in the design repository rather than on the public page, with its existence declared on the page" (Chapter 14 §10); the published view is drawn from it.
- **Touches.** Chapter 14 §10 and §11; rule 16.27; Chapter 16 §11; P-170 (the boundary log as a working file); probe 74.
- **Status.** Open · 14 Oct 2026.

### DB-76 · Is the committee export a separate deliverable or the stripped state of the page?
- **Steer.** None stated (Chapter 14 §11). The stripped state of the same page, so the two never diverge; Chapter 14's removal test already requires the evidence layer to survive the stripping, and probe 68 tests the pair. [Proposal]
- **Touches.** Chapter 14 §11; Chapter 16 §11; probe 68.
- **Status.** Open · 14 Oct 2026.

### DB-77 · Is a probe built for the two-audience claim?
- **Steer.** The claim "has no measurement anywhere in this book" (Chapter 14 §11). Build it, as probe 67, after probe 68 has shown whether an expressive form costs its plain twin anything; the whole expressive layer rests on the claim. [Proposal]
- **Touches.** Chapter 14 §11; Chapter 16 §11; probe 67 (P-169, P-170).
- **Status.** Open · 14 Oct 2026.

### DB-78 · Which expressive choices are free, which priced, and does it ship dark?
- **Question.** The Decorative tier; the drawn or approximate register; an invented form; a humanised mark; a mood palette beside a scale; a dark ground.
- **Steer.** Free: "the whole Decorative tier within the conditions of sections 5 and 10". Priced: the approximate register "only where the data is imprecise" (truth 4); an invented form "with a glance-cost estimate and a measurement plan" (rule 14.16); a humanised mark "may serve recognition; may not be priced as empathy or giving; whole units" (rule 14.5); a mood palette "priced in the log; on the scale itself forbidden" (rule 14.8); a dark ground "ships with the light one; the reader chooses" (truth 5). (Chapter 14 §11.) The polarity choice for dark grounds is one of the twelve Decision Book candidates (DB-85).
- **Touches.** Rules 14.5, 14.8, 14.16; Chapter 14 §5, §10, §11; Chapter 16 §11; probes 68, 69.
- **Status.** Open · 14 Oct 2026.

---

## J · The records, the log and the house's documents

What the first record, the first deviation and the next edit of the Decision Book raise.

### DB-79 · Are the records one document, and what is it called?
- **Steer.** Chapter 0 now describes "the one record of the dashboard": the ten records Chapters 4 to 13 left beneath the dashboard, "written once per concept as sections of one record kept in the repository and drawn into a public view and a producer's view" (Chapter 16 §7). The house's name is open (Chapter 16 §11); use "the one record of the dashboard" until the house names it. [Proposal on the name]
- **Touches.** Chapter 0; Chapter 7 §12 (four records); Chapter 14 §10 (eleven records); Chapter 16 §7 and §11.
- **Status.** Open · 14 Oct 2026.

### DB-80 · Publish a statement in the regulator's voluntary form and ask to be listed?
- **Steer.** Chapter 15 names the compliance-style statement among section 9's mechanisms; Chapter 16 states none and names "the TQV statement" as the public view's model. Write the statement in the TQV form at the first release, and ask to be listed once a year's record exists to stand behind it. [Proposal]
- **Touches.** Chapter 13 §10 (the accessibility statement); Chapter 15 §9; Chapter 16 §7 and §11.
- **Status.** Open · 14 Oct 2026.

### DB-81 · Which of Chapter 15's mechanisms and instruments are adopted, and what stands in where conditions cannot be met?
- **Question.** Metadata fields beyond the minimum; which evidence scale labels contribution claims; the rest of section 9's forty mechanisms; the arrow, the revision size, the similar-areas model and the base-year index, whose conditions a new display cannot meet; and the sector's instruments (Toolkit, Illuminate, Audience Spectrum, the national survey).
- **Steer.** "Section 9 is an offer with terms; the precedent record is where each choice is written" (Chapter 15 §9); the rules table proposes the SMS as Adaptable (row 15). Where conditions cannot be met: "in its first years the display shows the data, its dates, its log and its revisions, with the sentences about change written by hand" (Chapter 15 §9). The instruments: "the studio's, with their documented state (live, suspended, orphaned, replaced with a dotted line) in front of it."
- **Touches.** Chapter 15 §9 and rules row 15; Chapter 16 §11; DB-10; probe 71.
- **Status.** Open · 14 Oct 2026.

### DB-82 · ARG-12: re-base or retire?
- **Steer.** "Carried as disputed, with Chapter 12's rule beside it" (Chapter 16 §7, rule 16.23). Chapter 12's rule governs the build until the Decision Book is next edited; the dispute is settled there, not on the page. [Proposal]
- **Touches.** Chapter 12 §5; rule 16.23; Chapter 16 §11.
- **Status.** Open · 14 Oct 2026.

### DB-83 · Accept the four direct-conflict readings?
- **Question.** DSH-21 split (the degraded state Fixed, only its look Decorative); the withheld cell's kind not parameter; DAT-14 never joined; DTA-19's missing lines; and the two corrections to the Decision Book's borrowed sentences.
- **Steer.** "The chapter resolves each as a reading; acceptance is the Decision Book's" (Chapter 16 §7). Build to the readings; amend the Decision Book's text when it is next edited.
- **Touches.** Chapter 4 §13; Chapter 8 "What the field does not know"; Chapter 16 §7; DB-22.
- **Status.** Open · 14 Oct 2026.

### DB-84 · The fifteen tensions: what interim rule does each gap take?
- **Question.** The status chip; the filter set as a query system; position against limits; raster fallback and twin-table component; freshness statement and running-foot date; felt-distribution component; provenance lines for who was asked; one identifying threshold per view; the held layer as a status; dated snapshot and generated citation; map breaks across filters; a label for generated text; the small screen first; body size against 18 point; joy-first against the plain view.
- **Steer.** "The rest are gap rows with interim rules owed" (Chapter 16 §7); each takes Chapter 16's interim rule as its design-system row until the component exists. The last "is the one that is a design question" and is DB-03.
- **Touches.** Chapter 16 §7 and §11; the design system; DB-17, DB-34, DB-41, DB-45, DB-57, DB-59, DB-60, DB-61, DB-64, DB-71.
- **Status.** Open · 14 Oct 2026.

### DB-85 · How does the Decision Book grow, and are the twelve candidates accepted?
- **Question.** By the seven chapters Chapters 5 to 11 asked for (composites; claims about value; comparison; running a dashboard; felt data; safeguards; the surface) plus the candidate sections from Chapters 12 and 13 (the place-page; the statement); by one chapter on dashboards; or by a pointer to this book. And the twelve candidates (eleven rows) logged by Chapters 14 and 15.
- **Steer.** None stated (Chapter 16 §11). A pointer to this book now, with the twelve candidates taken in as rows; chapters are written for the Decision Book once the build has tested the rules they would carry, not before. [Proposal]
- **Touches.** Chapter 16 §7 and §11; STATE 7 Oct (every chapter's "candidate" line).
- **Status.** Open · 14 Oct 2026.

### DB-86 · What changes when the register and the legend are next reviewed?
- **Question.** Whether "specific sensory experience" is a fourth tier or a sub-kind of Decorative; whether the register's status vocabulary keeps "open in the decision log"; whether Chapter 0's legend carries the sub-kind "Practice backed by analogous Evidence".
- **Steer.** Sensory experience: Chapter 14 "uses it, requires the identification the W3C requires, and leaves its place in the house's vocabulary to Chapter 16"; Chapter 0's tier table now calls it a tier of element, and that stands. Status vocabulary: Chapter 16 §8 states none; retire "open in the decision log", since a register row is Open with a steer or Decided with a date, and nothing in it waits. [Proposal] The legend: Chapter 3's position is yes, "the book should say so rather than cite a study that does not exist" (Chapter 3 §5; the "Label at the mark" row).
- **Touches.** Chapter 0 tier table and legend; Chapter 3 §5 and truth 3; Chapter 14 §11; Chapter 16 §3 and §8; `06-register/rule-register.md`.
- **Status.** Open · 14 Oct 2026.

### DB-87 · Is a register of 280 Fixed rules short enough to be read and obeyed?
- **Question.** 245 are build checks; are hard stops at that number obeyed or routed around?
- **Steer.** "Truth 2 is the test; the build's first year measures it" (Chapter 16 §3 and §10).
- **Touches.** Chapter 16 §3, §6, §10; probe 75.
- **Status.** Open · 14 Oct 2026.

### DB-88 · Which probes run first?
- **Steer.** The probe register ranks none. Run the small ones that need no build first, and probe 48 before any default is fixed, as its own row requires; probe 15 before the kinds of nothing are drawn. [Proposal]
- **Touches.** `03-tests/PROBES.md`; STATE 7 Oct; DB-05.
- **Status.** Open · 14 Oct 2026.

### DB-89 · Who checks and owns DL-001?
- **Question.** The deviation log's first entry (Chapter 12's in-frame furniture against official practice) has its checker and its review owner "to be named".
- **Steer.** The accessibility reviewer checks, against the 1.4.5 condition Chapter 13 stated, as the entry itself suggests; the design system's owner owns the review, since the review falls due "when the design system's in-frame provenance block exists". [Proposal]
- **Touches.** `06-register/deviation-log.md`; DD-006; Chapter 12 rules 32 and 33; Chapter 13 rule 13; DB-18.
- **Status.** Open · 14 Oct 2026.

---

## K · The book's own form

What the first reader test of the book itself raises.

### DB-90 · The length of the "60-second version" sections?
- **Question.** They run 440 to 1,650 words; the cold readers raised it nine times during the writing; six were reordered so the truths come first.
- **Steer.** Keep the text and the name; the reader shows each chapter's question and 60-second version open, so the reader meets them first; cut only if a reader test shows the length loses readers. [Proposal]
- **Touches.** Every chapter's "60-second version"; Chapter 16 §7 and §11; Chapter 12 inventory C1.
- **Status.** Open · 14 Oct 2026.

### DB-91 · Trim the template's restatement; add a figure to the chapters?
- **Question.** Whether the fixed sections each chapter repeats are trimmed (asked at Chapter 12); whether a figure is added, which no chapter has.
- **Steer.** None stated on either (Chapter 16 §11). Leave the template as the book stands: the reader collapses the fixed sections, and a trim would be a second edit of sixteen chapters for a cost the reader already pays once. No figure drawn for the book: the prototype's first screens become its figures once they exist, which is also when a figure could be true. [Proposal]
- **Touches.** Chapter 12 (the question and the cold reader's request); Chapter 16 §11.
- **Status.** Open · 14 Oct 2026.

---

## Not in this log, and why

Open in a chapter's wording, or in the 7 October list, but not a choice about the dashboard. Each is either settled by the edit, the book's stated position, or a step of the work rather than a decision.

| Item | Where | Why it is not here |
|---|---|---|
| Seventeen chapters; Chapter 15 kept | Chapter 16 §11; STATE | Settled by the edit: the chapter found about forty mechanisms the others do not carry |
| The register's identifier scheme | Chapter 16 §11; STATE | Settled by the edit: `DD-nnn` stays |
| Whether `06-register/` stays in this repository | STATE | Settled by the edit: it stays |
| The ten library-pass corrections; the stale daggers | STATE Entry 17 | Settled by the edit: applied; the daggers are off |
| The tier wordings in the chapters | Chapter 0; Chapter 16 | Settled by the edit: they follow the register |
| Moving the process sections to the working record; retiring the status lines; the reader rebuild | Chapter 0; Chapter 16 | Steps of the edit |
| Is a library pass scheduled for the 32 unreached full texts | Chapter 16 §11; Chapter 6 | Overtaken by `01-sources/LIBRARY-PASS.md`, 7 October |
| Does the sector composite's method audit sit in Chapter 5 or Chapter 15 | Chapter 5 §14; Chapter 16 §11 | Settled by the edit: Chapter 5 carries it, read for its published method only |
| Is the gross-to-net arithmetic adopted from a withdrawn guide | Chapter 6; Chapter 16 §11 | Chapter 16 §7 settles it: a Standard (adopted) in the register, with the withdrawn guide as its source and the flag it carries |
| Whether "two tests" becomes the book's definition of a canonical truth | Chapter 6 | Chapter 16 §7 settles it: adopted as Chapter 0's definition |
| Whether decision-makers prefer a composite to a dashboard | Chapter 5 §11; rule row 25 | A belief marked Practice until evidence is found, not a choice |
| The 78%/32% finding needs its unit, period, denominator and curve | Chapter 4 | A build step: the prototype supplies them |
| The prototype data contract set against Chapter 4's mapping table | Chapter 4 | A build step, under DB-66 |
| The design system's components each chapter asks for | STATE, every chapter | Build steps; the gaps that owe an interim rule are DB-84 |
| The Decision Book has no chapter on composites, claims about value, comparison, running a dashboard, felt data, safeguards or the surface | Chapters 5 to 11 | One question: DB-85 |
| The official reader as a potential intruder (Form 696) | Chapter 10 | The chapter's stated frame; the intruder walk is probe 42 |
| Gapminder: the five-minute observation | STATE | A reading-list note, not a choice about the dashboard |
| Anything in BRIEF-v2 section 8's reading list already held; mark-up of BRIEF-v2; emptying `_to_delete/` | STATE | Housekeeping, not decisions |
| Whether a break from a borrowed method is recorded differently | Chapter 12 | Chapter 16 answers it: one log, one entry shape |
| Whether a sonified series' three routes are listed in the view record | Chapter 14 | Chapter 16 §7 answers it: yes, in the face sheet's section of the one record |
| Whether "dashboard" and "canonical" survived the book | Chapter 16 §7 | Answered: they did |

---

## Register queries

Found during the edit. Not decisions about the dashboard: each is a place where the register's grouping or status disagrees with a chapter, with one line on what the register should say if the chapter is right.

| Register row | The query | If the chapter is right, the register says |
|---|---|---|
| DD-037 | Groups the validity-claim rules (5.15, 9.32: validity is claimed for an interpretation and a use, argued from the five sources) under the cognitive-testing rule | The two validity rows move to a row of their own, Fixed (requirement); DD-037 keeps cognitive testing alone |
| DD-030 | Groups the outlier rule (1.13) with 4.33 and 4.36 as Fixed (sequence), where Chapter 1 argues Adaptable ("a default stance") | 1.13 is listed as Adaptable with the chapter's reason, or the row's note says why Chapter 1's stance yields to Chapter 4's sequence |
| DD-001 | Groups 2.10 (the plain-table route as "a hypothesis to test") under the table twin as Fixed (requirement) | 2.10 is noted as a hypothesis within DD-001: the twin is required, the route is tested (probe 7; DB-03) |
| DD-004 | Carries "11.4 superseded by 14.14"; the "most important first; official lengths" half of 11.4 has no register row of its own | That half gets its own row, Fixed (requirement), or DD-004's note says it is carried by 14.13 |
| DD-171 | Still carries "full text not read" for Lazer et al., though register 1.3 names it among Chapter 7's stale daggers and the chapter prints rule 7.34 without the dagger | The row's status is updated to match the pass |
| DD-068 | The status field still hands "Design the first glance" to Carly | Open with a steer: DB-55 |
| DD-033, DD-083, DD-255 | Open parts recorded with no steer | Open with a steer: DB-10, DB-16, DB-22 |
