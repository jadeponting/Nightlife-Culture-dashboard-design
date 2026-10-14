# Chapter 3 — newcomer read

Read in full (646 lines). Chapter 0 consulted only to check whether the kind and tier vocabulary is defined anywhere; it is.

## 1. What it teaches

The chapter sorts the received rules of data visualisation into those that were actually tested, those that survived testing, and those that are hard lines, and it finds the surviving list is short: choose the comparison, put the message in words, never let colour carry meaning alone, start bars at zero, show uncertainty as something countable, assume a glance on a phone by a sceptic, and treat every default as advice. It is written for whoever builds a public-facing dashboard and wants to know which rules can be argued with and which cannot. After reading it I would stop defending bar charts by citing the perceptual hierarchy, write the trend into every title, put the number next to every probability word, and never again assume a labelled axis break is honest because it is labelled.

## 2. One rule, and why it exists

"Bar axes start at zero; a broken line axis is declared and the effect size it implies is chosen deliberately." The chapter's evidence is that the usual defence of truncation, labelling it, does not work: Correll, Bertini and Franconeri found perceived severity rose with truncation (p < 0.0001) and that a broken-axis marker or a gradient fade made no significant difference, with people reading the numbers correctly and still feeling the gap as larger; Yang and colleagues found the effect persisted after people had been taught about it, across five studies and 83.5% of participants; Long and Kay found task accuracy often unaffected while the impression of effect size inflated. The rule exists because the exaggeration lives in perception, not in the reader's arithmetic, so no footnote can cancel it. The only honest move is to know that a truncated axis is a chosen effect size and own that choice.

## 3. Where I stalled

- **"Fixed rule in the Decision Book"** (section 5, line 169) and **"Practice and voluntary Standard, not Evidence"** (section 4, line 135). Capitalised kind and tier words are load-bearing from section 3 onwards, but the only pointer to where they are defined, "Kind and tier as in Chapter 0", arrives at the rules table on line 418. A reader starting here meets "Fixed", "Adaptable", "Standard", "Practice", "Evidence" and "Reading" as jargon for 280 lines.
- **"Fixed (requirement)"**, **"Fixed (ceiling)"**, **"Fixed (evidential status stated)"** (sections 13 and the rules table). The brackets imply sub-species of Fixed, and the chapter never says what distinguishes a requirement from a plain Fixed rule. Chapter 0 hints at it (line 61) but Chapter 3 does not point there.
- **"Japanese ethnicity".†** (line 133). The dagger first appears here and is explained in the Sources preamble on line 504, 370 lines later. By then I had guessed it meant "weaker source" but not that it meant abstract-only.
- **"d = 0.68 across 58 datasets"** (60-second version, line 23). *d* and *n* are defined in "Words this chapter uses" on line 497, after the chapter has used *d* four times and *n* throughout the rules table. The glossary belongs before the 60-second version or inside it.
- **"The Vibe Map could."** (line 319). First appearance of the Vibe Map in the chapter, as a one-sentence paragraph closer, with no gloss. It recurs in sections 14 and 15 as if introduced. I had to infer from context that it is the dashboard this book serves.
- **"The brief asked that the W3C documents be sorted"** (line 325) and **"The brief's own failure register"** (line 404). What brief, whose, and where? Never stated in the chapter. The failure register is quoted without saying what it is a register of.
- **"the studio's own rulebook"** (line 47). "The studio" is used as a proper noun from section 2; the name Nightlife Culture does not appear until section 12 (line 344), and the two are never joined in one sentence.
- **"the design system"** (lines 336, 384, 450). Referred to as a known document three times; never introduced.
- **"five success criteria are the hard lines that bite on charts"** (60-second version, line 25) against section 12, which lists eight criteria, and section 13, which names the five "with 1.4.3, 1.4.10 and 2.5.8 beside them". Section 4 had called 1.4.3 and 1.4.11 "two companion criteria", both AA, both contrast floors. Why one is a hard line and the other is "beside" is not explained; the sentence reads two ways.
- **"moved readers' perception by nine points"** (line 141, citing Chapter 2). Nine points of what, on what scale? The cross-reference carries a number without its unit.
- **"Chapter 2's plain table"** (line 410). A reference to a specific finding in another chapter with no clue what the plain table showed or why it is the sceptic's remedy.
- **"a quality score of 1.99 against 1.59"** (line 149) and **"pictograms (1.93 against 1.14)"** (line 201). Scales unstated; I cannot tell whether the gaps are large.
- **"Fixed"** against **"Ajani et al. 2022 (n = 24)"** in the first row of the rules table (line 422). The chapter has just said (line 207) that Ajani is small, unreplicated and "not a settled size", and Chapter 0 says single-study evidence is "a prompt, not a rule". A Fixed rule part-sourced to it reads as a contradiction unless the reader works out that Franconeri's review is doing the Fixed work and Ajani is illustration. One clause would settle it.
- **"The 60-second version"** (line 13). It is about 900 words. A newcomer who takes the heading at its word and budgets a minute is wrong-footed; the content is good, the label is not.

## 4. What reads like it was written for the people who made it, not for me

- "Those are Practice and voluntary Standard, not Evidence, and they are sensible precisely because..." (line 135). Classification talk aimed at people maintaining a register.
- "The kind is *Practice backed by analogous Evidence*, and the book should say so rather than cite a study that does not exist." (line 169). The chapter instructing its own authors.
- "Franconeri's review gives a global all-population figure of about 4%; the two are different denominators, not a disagreement, and this book uses Birch's." (line 133). An editorial decision recorded in the text.
- "Chapter 1 cited, from version 1 of this book, the finding that a default is read as a recommendation. Re-verified for this chapter:" (line 259). Version history and a verification note.
- "Its evidential basis is Practice, and the gap is logged." (line 239). Logged where, by whom; a process note.
- "Later chapters test both; the closing chapter confirms or demotes." (line 350). Pipeline language.
- "Where to set the Vibe Map's limit is a design-system decision informed by section 4." (line 384). Asks someone to decide.
- "how much more, and in what voice, is the studio's." (line 386) and "Adaptable; the studio's." (line 388). Hands a decision to an unnamed party.
- "Whether the Vibe Map claims to be a dashboard, a map, a flyer or something else ... is the creative decision this book never makes." (line 388). Waits on a decision.
- "What the Vibe Map claims to be is the studio's decision" (line 406). Same.
- "The Vibe Map could." (line 319). An action item for the prototype dressed as a sentence.
- "the form of the uncertainty display is itself something to test with sceptics" (line 410) and the rule "Test uncertainty displays with sceptical readers before release" (line 446). Instructions to a build team; acceptable in a rulebook, but note they are tasks, not findings.
- "If the reading survives, log the break in the deviation entry Chapter 16 describes." (line 456). Process.
- "Said so; flagged all three for the prototype." and "Replaced it with Conlen et al.'s measured rates and kept Aisch's own correction." (lines 460–461). First-person-plural working notes about what the authors did while writing.
- Sources preamble (line 504): "Two founding texts could not be read in full ... the last third of Franconeri et al. 2021 could not be reached, so the publisher's summary stands in for its ending." Also "At source for roughly the first two-thirds (publisher HTML and an archived PDF)" (line 507), "**Secondary** (standard reproductions; check against the second edition)" (line 554), "At source; the live tool could not be opened" (line 602), "also Chapter 2, where it was abstract-only" (line 615). Retrieval diaries and a to-do ("check against the second edition").
- "The brief, version 2 — the failure register; the request to classify the W3C documents; the reading-age steer." (line 641) and "Version 1, Chapter 1 (archived) — ... re-verified here where load-bearing." (line 643). Internal document versions.
- "Kind and tier as in Chapter 0." (line 418). Fine as a pointer, but it is the only one and it is late.

No sentence asks Carly to do anything or waits on her by name; the chapter does not use her name at all. The waiting is done through "the studio".

## 5. Best passage

"This is the review's central mechanism and the one most worth a first-time reader's attention." (section 3, line 103). The statistics-fast, comparisons-slow mechanism explained in a paragraph what twenty style guides never had: why a highlight, a title and a grouping all work, and why a tile with a count and no comparison has given the reader the easy thing and withheld the hard one.

## 6. Verdict

A research partner could use it as it stands; a creative technologist or a funder's analyst could use the body and the checklist but would stall on the kind and tier vocabulary, the dagger, and the unintroduced Vibe Map, brief, studio and design system until someone handed them Chapter 0 and a one-line cast list.
