# Chapter 13 — newcomer read

## 1. What it teaches

The chapter decides that a public dashboard has one page per screen size and that everything a disabled reader needs — a written description, a data table, optionally a keyboard-navigable tree and audio — sits on that page as supplementary content, never as a separate "accessible version"; and because no WCAG rule names a chart, it writes down which general criteria bite on a chart and how. It is for a small studio building a free public dashboard that public bodies might embed, and for the people who will test and fund it. After reading it I would stop treating an alt-text sentence as "the accessibility", would generate a two-to-eight sentence description of figures and trend into the body text with a native HTML table beneath, and would not release without a keyboard walk, a 400 per cent zoom, a screen-reader read and a blind reader asked for the trend, the figures and, on a map, where.

## 2. One rule, and why it exists

"The chart's description carries the chart and not the author's interpretation; interpretation lives in the authored account on the page, read by everyone." The reason is Lundgard and Satyanarayan's ranking with 30 blind and 90 sighted readers: blind readers ranked statistics (level 2) and trends (level 3) most useful and 63 per cent were "emphatic" that the description should not carry the author's interpretation, while sighted readers, who have the chart, ranked interpretation highly. Both groups still want meaning, so the chapter puts it on the page for everyone rather than in the text that stands in for the chart. The supporting evidence that descriptions are already thin (half omit extrema, seven in ten omit the trend) explains why the rule fixes what the description must carry rather than leaving it to taste.

## 3. Where I stalled

- "Version 1's rule — no parallel" (60-second version, and a dozen more times: "Version 1 made one claim", "version 1's 'the regulations likely don't bind'", "Version 1 wrote that hierarchical navigation", "Version 1's position ... holds"). I do not know what version 1 is. The Sources list calls it "Version 1, Chapter 11 (archived)", so it is an earlier draft, but the chapter argues with it as if I had read it.
- "the ELS's rule that turns" (section 3, COGA reading). Abbreviation never expanded anywhere in the chapter.
- "touches the Vibe Map" (section 4, distribution argument). Named once, never explained; I assume it is the dashboard, but the chapter otherwise says "the dashboard" or "the prototype".
- "the brief's failure register" (section 1). "The brief" is not introduced; the register's five failures are only recoverable from section 9's headings.
- "(†)" in the 60-second version ("which was fastest (†)"). The mark is defined only in the Sources note at the very end. Same for "secondary" in "(2019, secondary)".
- "COGA, read in its body" (60-second version). Used bare there; expanded only at section 3's subheading.
- "the 'how this argues' page" (section 3, and the COGA rule). A page of the product I have never been shown.
- "a tenth record" / "Chapters 4 to 12 each left a record". I do not know what the nine earlier records are or what "record" means here.
- "in the model's form" (60-second version, closing paragraph). The "model accessibility statement" is only explained at regulation 8, two sections later.
- "poster above door" (section 12, 400 per cent walk) and "the missed column's profile", "the two-column view". Chapter 12's page layout is assumed; a newcomer cannot picture any of it.
- "at one median absolute deviation" (section 3). A statistical threshold dropped in as if familiar.
- "Born Accessible visualizations" / "Top Results visualizations" (section 5). Fan et al.'s two groups are quoted by their labels with no gloss of what each group was.
- "the one official statements fall back on" (section 5, structure reading). Reads two ways on first pass ("the one official statement" versus "the one [route] that official statements fall back on").
- Does the chart get an alt attribute or not? Section 6 reconciles the ONS formula as "the short part" and the Analysis Function's body text as "the long part"; the rules say the long description is "never duplicated in an alt attribute"; the filled example says "no alt attribute duplicates them"; the Analysis Function, quoted, says mark the image decorative; and "What the field does not know" ends "the house picks one" without saying which. I could not tell what to put in the alt attribute.
- "Kind" and "Tier" columns in the rules table ("Standard (W3C) + Evidence", "Fixed (requirement)", "Fixed (sequence)", "Adaptable (house default)", "Decorative"), and the running parentheticals "*(Standard (W3C); Reading for the house line.)*". The classification scheme is never introduced in this chapter.
- "the furniture around them not" (section 8, the eye). Trade word for headings and controls, unexplained until the zoom walk at the end.
- "the community's phone-read test" (section 11). Which community, what test; Sources says it is confidential and not reproduced.
- "the three user groups" (filled example, tests). Glossary says they are "named in its design repository and not here".
- "reg 13" as the source of line 12 of the statement table. Regulation 13 is never described in section 4.
- "ISO/IEC 40500:2025 is the October 2023 text". Which text is "the October 2023 text" is not said.
- Section 2's "A public body cannot embed" belief says bodies "handle it three ways in practice" and points to section 4; section 4 delivers the three, but by then the promise in section 1 that the argument "survives in a different shape" has been made three times before the shape arrives.

## 4. What reads like it was written for the people who made it, not for me

- "Version 1's rule — no parallel accessible version — is the standard's stated preference before it is the house's rule" and every other "version 1" sentence: "Version 1 made one claim in three forms"; "version 1's 'the regulations likely don't bind this instrument' is replaced here by what the regulations say"; "Version 1 wrote that hierarchical navigation 'reduced cognitive load'"; "Version 1's position — audio designed once as first-class display ... — holds"; "the audit checklist version 1 adopted"; "rather than letting version 1's 'keep turning out to be the same build' stand as a finding". These are arguments with a superseded draft.
- "The brief's own numbering of the Regulations was out by one or more throughout (reg 2 is a revocation)."
- "Chapter 11 attributed the 'rarely' sentence to the ONS; it is the Analysis Function's, and the correction is logged."
- "One tension is logged".
- "The regulator's Code changed while this book was being written."
- "whose specification sentence could not be read at source"; "the Code's other chapters were not reached"; "Two texts could not be read at source and are marked unreached"; "'(read once)' marks a quotation returned once without a presence check"; "Read 6 October 2026; the EHRC Code's Chapter 7 on 7 October 2026"; "its contents and clause 9's headings read, its body not"; "BBC R&D: unreached (domain blocked)". Verification bookkeeping.
- "Section 4 reports the texts and leaves their application to the studio's adviser."; "What 'funded' covers, and whether any of this touches the Vibe Map, is the studio's adviser's question."; "Whether to seek the adviser's view now." Each waits on someone to decide.
- "the order after the first two is the studio's"; "the design system's tokens decide which face and where between 16 and 18 pixels the body sits, and record why".
- "Tooling is chosen against these rules in week one". Schedule language.
- "Invented, to show the record's shape; nothing in it is a decision or a finding." and "Illustrative; fixes nothing about the design; invents no findings." Useful caveats, but written to defend the text against the project's own approval process.
- "The three user groups are the studio's testing groups, named in its design repository and not here."
- "Nightlife Culture" as the Kind of the rule "The law is cited by section with its date, and never as advice", and the House documents block: "Style Guide v1.5: §13 (the floor); §02 (hierarchy); §04 (register); LNG and DSH rules. Read directly."; "The Decision Book, Chapter 15 (dashboards) and the rule register. Read directly."; "Version 1, Chapter 11 (archived). Positions tested, not sources."
- "Chapter 14 of this book" as the source for the Decorative tier; a forward reference the reader cannot check.

## 5. Best passage

"The reading, and it is a strong one for this book: COGA is not against charts; it is against numbers and charts *without words*." The paragraph that follows turns a long quotation dump into one usable idea and shows where the book's existing rules already satisfy it.

## 6. Verdict

A research partner or creative technologist could use sections 3, 5, 8, the rules table and the test section as they stand; a funder's analyst could use sections 4, 6 and 10 but would be slowed throughout by the arguments with "version 1", the undefined house terms (ELS, Vibe Map, the records, the tiers) and the unresolved question of what goes in the alt attribute.
