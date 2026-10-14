# Chapter 4 — the newcomer read

Read cold, every line of `04-chapters/ch04-from-data-to-evidence.md` (789 lines), plus `ch00-how-to-read-this-book.md` for the kind/tier legend only. Nothing else opened.

## 1. What it teaches

The chapter decides that a number on a display is not evidence until five things about it are fixed and shown: what one row is and what span of time it covers, what it is counted against, where it came from and when, which of six (or seven) kinds of nothing a blank is, and what a comparison holds equal. It is written for whoever builds or audits a public dashboard fed by platform, administrative or survey data, and it borrows almost everything from official statistics, database theory and epidemiology rather than inventing anything. After reading it I would never show a total without a median beside it, never let a line cross a gap, never trust a feed's size as a reason to believe it, and I would write my outlier rule down before the data arrived.

## 2. One rule, and why it exists

"Never join a line across a missing point, dotted or dashed; highlight the gap and say why." The reason is in the chapter's one official source for drawing a gap, the Analysis Function's chart guidance: "Joining points implies we know something about the data." The chapter backs it with two cases where a nothing was drawn as a number: the CDC's provisional death counts, where the last weeks of every series are 65% complete and a line to the edge of the chart draws a decline that is a reporting delay; and the October 2020 Public Health England case, where 15,841 positive tests fell out of a pipeline for eight days and the display showed a low count indistinguishable from a true one. A dashed line still tells the eye there is a slope; the standard's point is that the display does not know that, and should not pretend to.

## 3. Where I stalled

- **"Carly's failure register"** (section 1, first paragraph; again in section 8, "The second failure on Carly's register"). Who Carly is and what the register contains are never said in this chapter. The 60-second version and section 1 both lean on it. Chapter 0 explains it; Chapter 4 does not, and Chapter 0 promises every chapter opens with a "Before you start" note repeating the conventions. This chapter has none.
- **"the Decision Book's companion rule"** (section 3, "Writing the date down"). The Decision Book is referred to seven or eight times, is relied on for the provenance set and the gap rule, and is never introduced. A newcomer reads it as a book they should have.
- **"The studio names six kinds"** (60-second version; section 6 opening). "The studio" is never identified in the chapter. Same for "a Nightlife Culture contribution" (section 5, minimal set): the name appears without the organisation being named as the commissioner.
- **"are Practice; the two cases are the evidence"** (section 4, Tufte paragraph) and **"are marked Practice"** (section 6, Darwen) and **"are therefore Standard"** (end of section 5). Capitalised kind-words used mid-prose before the rules table explains the vocabulary and with no pointer to Chapter 0. The same for "Fixed", "Adaptable", "house default" in the rules table, which says only "Kind and tier as in Chapter 0".
- **"(His principles on the chapter's last page"** (section 4). Which chapter: Tufte's or this one? It reads both ways on first pass.
- **"When it is smaller — inferring something"** (section 3, end of "What a row is"). "It" is the unit of analysis, but two sentences about *n* and Chapter 3 have intervened since the antecedent, so the sentence lands on nothing.
- **"the one-line idiom ... is in every warehouse"** (60-second version). A data warehouse; a non-technical reader will picture a shed. The body later explains `coalesce`, but the summary does not.
- **"Measuring ADC at midnight"** (section 3, midnight census). Bare abbreviation inside a quotation; "average daily census" never appears.
- **"When the missing data are not MCAR"** (section 6, Schafer & Graham) and **"MAR cannot be verified from data"** (rules table). The three mechanisms are defined in words two paragraphs earlier, but the abbreviations are never attached to them.
- **"SIMS"** (truth 4; rules table, comparison row). Expanded nowhere in the body; only the sources list says "SIMS Technical Manual" and even that does not say what the letters are.
- **"GSS quality dimensions"**, **"GSS geography policy"**, **"Analysis Function SDC"**, **"Eurostat LFS"**, **"ONS ASHE"**, **"PHE Fingertips"**, **"NIST"** (rules table and truths). Each is spelled out somewhere in the body or only in the sources ("Government Statistical Service", "statistical disclosure control", "labour-force", "Annual Survey of Hours and Earnings", "US standards body's handbook"), but the abbreviation is never tied to its expansion, so the table reads as code.
- **"the four-part form"** (rules table, reference period row: "declared frequency and the four-part form: Adaptable"). Never explained anywhere in the chapter.
- **"categories of separation"** (rules table, small-base row). Likewise unexplained.
- **"the illustrative flag"** (section 5, minimal set). Said to be worth keeping; never said what it is.
- **"the worked case the brief asks for"** (section 8) and **"the outlier the brief most cares about"** (section 10). Which brief? Not named in the chapter.
- **"the prototype can supply them"** (section 8, end). What prototype? First mention.
- **"finer than the studio's in two places and coarser in one"** (section 6, "How the six map"). "Second" and "Third" that follow give one finer place and the free/not-a-nothing point; the reader has to work out from the table that the "coarser" place is [x] covering both unknown and unavailable, and that the second finer place is SDMX K. The count does not match the enumeration.
- **"(abstract only †)"** (section 3, Simon et al.). The dagger is first used here and explained only in the Sources preamble 500 lines later.
- **Heading "What the field does not know"** (after the break test). Its ten bullets are about what the Decision Book, the design system and the studio's six kinds lack, and what the chapter changed. Only the last bullet is about the field. The heading promises one thing and the section delivers another.
- **"Log the break in the deviation entry Chapter 16 describes"** (break test). A forward pointer to a chapter a newcomer may not have, with no gloss.

## 4. What reads like it was written for the people who made it, not for me

Fetch and verification notes in the prose:
- "in the words reproduced by the trade press (the journal page was not reachable — secondary)" (section 3)
- "(abstract only †)" ... "(abstract †)" (sections 3, 4, 6, passim)
- "(a teaching note's wording; the textbooks are not open)" (section 6 table)
- "(The slides are a lecture, not a paper, and are marked Practice.)" (section 6)
- "(read in a reproduction — secondary)" (section 8, Juran)
- "could not be read at source for this chapter and is not quoted" (section 8, Anderson)
- "(read in a reprint — secondary)" (section 8, Elberse)
- "The article's body text was read in two independent teaching reproductions (secondary; the publisher page was not reachable)" (section 9)
- "(the book itself is not open)" (section 10, Hawkins)
- "(read in part — the full text was not reachable)" (section 10, Marsh)
- "(author draft — wording may differ from the published version)" (section 9)

Book housekeeping and pointers to internal documents:
- "anything in this book that cites 'Q1–Q3' should be read as pointing there" (section 5)
- "The Decision Book calls this 'the full provenance set' and ships it with every figure" (section 5)
- "The Decision Book's own list ... matches this with two omissions ... and one addition, the illustrative flag, which the standards do not have and which is a Nightlife Culture contribution worth keeping" (section 5)
- "Chapter 1 said this chapter would define them" (section 6)
- "The Decision Book's current rule ... can be read as permitting the dashed join the standard rejects" (section 6)
- "The Decision Book's disclosure rules are a correct reading of this guidance" (section 6); "The Decision Book's rules on boundary vintage and best-fit lookups are a correct reading of this policy" (section 7)
- "One consequence for display is our reading rather than any source's" (section 3); "in our reading" (section 7) — "our" is never identified
- "the row count is our reading of what the figure needs to bear weight" (rules table)
- "the audit itself is a Nightlife Culture choice" (rules table)
- "Log the break in the deviation entry Chapter 16 describes" (break test)
- The whole of "What the field does not know": "The Decision Book's gap rule ...", "The Decision Book's provenance set omits ...", "Neither the Decision Book nor the design system has a rule on ...", "'Reliable' is used in the failure register and the design system in the ordinary sense", "a probe is flagged"
- Checklist: "Not-applicable distinguished from not-asked (or the decision not to logged)"
- Sources: "No further use, per the brief" (ONS night-time economy); "Not researched; used as the brief's worked case"; "The prototype repository's data contract. Named in the brief; not read for this chapter."; "*Dashboard Design*, version 1 (archived) ... for the backward look only"

Sentences that ask someone to decide or wait on the studio:
- "The chapter takes the window only as an official definition and goes no further into the sector; that knowledge is the studio's." (section 3)
- "Whether 'not applicable' is a seventh kind or a sub-kind of the fifth is a decision for the studio, and this chapter flags it rather than making it." (section 6)
- "That is a *Nightlife Culture* finding; this chapter has not researched it, cannot verify it, and uses it only as the worked case the brief asks for." (section 8)
- "the chapter owes it the same sentence it gives everyone else's. Supplying them is what would turn it into something ... and the prototype can supply them." (section 8)
- "the outlier the brief most cares about" (section 10)
- "The choice between them is the studio's and the readers' of Chapter 2." (section 12)
- "is a layout decision for Chapter 11, bounded by ..." (section 12)
- "the Decision Book chooses suppression with secondary suppression" (section 12)
- "The sector knowledge is the studio's; the method is the chapter's." (section 13)
- "the seventh-kind decision is flagged rather than made" (What the field does not know)

Citations of Carly's brief as source are fine and not flagged: "the second and sixth items on Carly's failure register" is a source citation, but it stalls for the reason in section 3 (the register is never described here).

## 5. Best passage

"The single most important result in this chapter for any dashboard fed by a platform is Xiao-Li Meng's 2018 paper ..." (section 9, "Size does not cure selection"). Quality times quantity times difficulty, then the number: 2.3 million self-selected records worth 400 random ones at a correlation of half a per cent. It changes how I would read every feed, and it gives the builder two honest moves instead of a warning.

## 6. Verdict

A research partner could use it as it stands; a funder's analyst could use the 60-second version, the seven truths and the rules table but would trip on the undefined internal vocabulary (Decision Book, the studio, the brief, Practice/Standard/Fixed, SIMS, the four-part form) and on the fetch-notes in the prose; a creative technologist would get the rules and the checklist but has to tolerate 790 lines and a "What the field does not know" section that is really a note to the studio.
