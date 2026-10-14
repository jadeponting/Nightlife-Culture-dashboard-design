# Chapter 6 — newcomer read

Read: the whole of `04-chapters/ch06-finding-value-in-the-data.md` (699 lines), plus the Kind/Tier legend in `ch00-how-to-read-this-book.md` to check what "Fixed (sequence)" is meant to mean. Nothing else.

## 1. What it teaches

The chapter decides that a dashboard about a place's cultural life may only ever describe (who came, what was offered, what lasted, who got the money) and must label every figure with how far it can be trusted: whose behaviour the record holds, whether the number is gross or net, whether a "because" is earned, whether a pattern has been tested outside the data that produced it, and how noisy a small place's figure is. It is written for whoever builds or reads such a dashboard, and specifically for the Vibe Map team, though a funder's analyst or a council officer who has to defend a number would get as much from it. After reading it I would stop putting trend arrows, "significant" badges, league tables and the word "because" on any screen without the ten-line claim record beside the figure, and I would write "not done" in the record rather than leave the line out.

## 2. One rule, and why it exists

**"Never read two points as a trend; show a measure against its own history with limits the data set."** The chapter's evidence is the NHS *Making Data Count* guide, which exists because hospital managers compared this month with last and chased "deteriorations" that were ordinary wobble: two points "tell you nothing about trends and how much the data varies naturally", and "'Green' can provide false assurance and mask deteriorating performance." The NIST handbook supplies the cost of the alternative: even a correctly drawn three-sigma chart on a process in which nothing has changed will false-alarm about once every 371 points, so a hundred monthly charts will cry wolf roughly every four months with nothing wrong. The rule exists because a red-amber-green tile is built on exactly two points, and the method that replaces it has a known false-alarm rate that can be printed, which a traffic light does not.

## 3. Where I stalled

Terms used before, or without, explanation:

- "KDD is the nontrivial process" (§1). KDD is quoted as the definition of finding anything in data, and the letters are not expanded until §9 ("knowledge discovery in databases"). Eight sections late.
- "there are multiple MNOs" (§3). Never expanded (mobile network operators).
- "from the EE network" (§3 and 60-second version). A UK-only brand name; a reader outside the UK cannot tell this is a phone company.
- "the ONS's travel-to-work areas" (§3). First appearance of "ONS"; the 60-second version says "national statistics office" but never joins the two.
- "the IDBR is an administrative dataset" (§5), "MSOAs", "ITL1", "FRS responses" (§11), "direct ACS estimates" (§11), "SPC tells us" (§10), "ASHE's dark green", "OPN base > 10", "QMI" (rules table), "DCMS" (§4), "NIST" (§10), "SAIPE" (rules table). All bare. Some are inside quotations and cannot be changed, but the surrounding sentence could gloss them; "SPC" in particular is the method the whole of §10 is about, and the abbreviation is never tied to "statistical process control".
- "AQuA Book" (§9). Named, quoted, never expanded or described (it is the UK government's analytical quality assurance guidance; the reader has to infer this).
- "Bevan and Hood called that synecdoche" (§6). Two names and a term dropped in half a sentence; neither appears in the Sources list for this chapter.
- "Chapter 5 found, through Sen" (§9). A bare surname carrying the chapter's own position on who counts as competent.
- "the brief's third sign of value" (§5), "the brief calls welcome" (§4), "the brief expected a table" (§7). "The brief" is defined only in Chapter 0; and if longevity is the third sign, the chapter never says what the first two are.
- "the failure register says" (§10, §11). Defined only in Chapter 0.
- "the studio's own steer" (§7, §8). Which studio, and what document is a "steer"? Nightlife Culture is named elsewhere, but "steer" is never a cited source.
- "Version 1 of this book" (§7, §8). Nothing says what version 1 was, when, or why it was superseded; the Sources call it "archived".
- "the three user groups" (§9). Never named in this chapter.
- "Decision Book Ch 8/15" (rules table source). Never described in this chapter.
- "the one peer-reviewed representativeness study reached" (§3). "Reached" is used throughout to mean "accessed online"; on first meeting I read it as "concluded". The same verb recurs forty-odd times ("not reached", "reached at abstract only") and is never defined in the body, only in the Sources preamble at line 591.
- "both papers at abstract only †" (60-second version). The dagger appears a dozen times before the Sources section explains it.

References that do not deliver:

- "a choice the next section leaves open" (§11, last paragraph). The next section is §12, the seven truths, which leaves nothing open; the base-size floor is in §13. Off by one.
- "The chapter's framing asked how an algorithmic assumption is validated into a canonical truth" (§9). No such question appears in the chapter's own "The question" at the top. The framing being answered lives somewhere I was told not to look.
- "The Warwick Commission's often-quoted finding about how concentrated the arts audience is could not be reached at source and is not stated here" (§4). I am told a finding is often quoted and then not told what it is; the sentence tells me only that a gap exists.
- "Chapter 4's sixth kind of nothing — not yet — is the whole of this method" (§3). A pointer to a taxonomy I have not seen; as written the sentence is unreadable without Chapter 4.
- Dense stacks of back-references with no gloss: "Chapter 5's cognitive testing and Chapter 9's care" (§4), "Chapter 5's price list again" (§7), "Chapter 4's provenance set applied to a parameter" (§7), "Chapter 5's one-tailed question returns here" (§11), "Chapter 3's small-multiples" (§8), "Chapter 4's assumptions log" (§9). Each is a sentence that means nothing on its own page.

Sentences that read two ways:

- "Freeman (2003, p.285) notes" (§3) and "Freeman's in 2005" (§7). Two different Freemans (an environmental economist and an urban sociologist), unmarked. I assumed one author and was briefly confused by the subject change.
- "Hill" names Austin Bradford Hill throughout, but the Sources list also carries "Hill, M. O. (1973)" on diversity, which the body never mentions. A reader checking the sources meets a second Hill with no body text to attach him to.
- "Fixed (sequence)" for "Keep a measure that is not the proxy beside the proxy" and for "Set the identifying threshold by the scene's knowability" (rules table). Chapter 0 says a sequence is an order of operations; neither rule is an order. I could not work out what sense of Fixed was meant. Several other rows say just "Fixed" with no sense named, though Chapter 0 says the register names it for every Fixed rule.
- "Kind: Standard for the definition; Evidence for the lag; Standard (adjacent domain) for the grading; Reading for the requirement to name the sense and to keep the second measure, held as Fixed (sequence)" (Truth Three). Four kinds and a tier in one italic clause; I had to read it three times to see which part was which.
- "the deaths data are not final until the third year" against "provisional for two years" (§5). Consistent on reflection, but the two phrasings sit two sentences apart and made me check.

## 4. What reads like it was written for the people who made it, not for me

Waiting on the prototype or the team:

- "The deadweight question can be asked of ticket-holders in the prototype, with its answer marked as stated preference." (§8)
- "the first awaits the prototype." (§9)
- "Which of the scene's people count as 'those judged competent' for the Vibe Map's patterns is a question for the three user groups, not for this chapter." (§9)
- "Whether the scene's own people can see their place in a shrunk figure — whether they recognise it, in the failure register's sense — is a thing to test and no literature can answer." (§11)
- "Whether those regulars recognise their street in what remains is a question the Vibe Map asks them." (§14)
- "the rules table above is the candidate for a Decision Book chapter on claims about value." (What the field does not know)
- "Log the break in the deviation entry Chapter 16 describes." (What proves a break works)

Drafts and the studio's own history:

- "Version 1 of this book proposed a form for all of this — a 'ledger strip' … and the studio's own steer asked for the attribution question to be put the other way round" (§7). The whole subsection "The ledger, as a Nightlife Culture position" is a note from one draft to the next.
- "Tested against this section, the form holds and the labels need work." (§7)
- "One more claim about cause wears a disguise, and the studio's own steer makes it" (§8)
- "Version 1 of this book, in its chapter on the measure on screen, proposed a display for the studio's strongest claim" and the whole of "The claim ladder, tested" (§8), which reviews an earlier draft's diagram rather than teaching me anything I could use without it.
- "it is the one that version 1 of this book was reaching for." (§8)
- "The seven truths this chapter states have themselves passed only the second test, by the agreement of the few people who have read them" (§9)

Research log in the body text (what the author could and could not download), which belongs in Sources:

- "both papers at abstract only †" (60-second version) and "the body that built the sector's audience segmentation went into liquidation four weeks before this chapter was researched" (60-second version).
- "The founder was not reached: Tukey's *The Future of Data Analysis* and *Exploratory Data Analysis* could not be opened, and nothing of his is quoted here." (§9)
- "Mazzucato's book-length version of the point could not be read at source" (§7); "Holling, whose 1973 original could not be reached" (§5); "Martin and Sunley's working paper (the published version was not reachable)" (§5); "the methodology documents could not be reached" (§8); "the 1996 original is behind a wall" (§10); "the 2020 wording was not reachable" (§8); "the 1977 magazine article that made it famous was unreachable beyond its standfirst" (§11); "Its four criteria are in the paywalled body and are not named here" (§5); "the study … was not reached and is not paraphrased" (§7); "the chapter must note that the text it quotes is the May 2026 edition" (§8); "reached at its abstract only and rebuilt from an index" (§8).
- "The chapter's framing asked how an algorithmic assumption is validated into a canonical truth" (§9) — a brief question addressed back to whoever set it.
- "Four weeks before this chapter was researched" (§4) — a date relative to the writing, not to the reader.
- In Sources: "string-checked", "single pass", "spot-checked (three sentences)", "third-pass string checks on the long definitions", "the magazine page returned 503", "one table cell failed verification and is not used", "consistently reported across two readings". Verification vocabulary that tells me about the author's process, not about the source.

"Carly" does not appear in the chapter body; nothing here is addressed to her by name.

## 5. Best passage

"A dashboard is a garden of forking paths built for walking." (§9, "The garden"). The paragraph that follows turned a statistics argument about researcher degrees of freedom into a description of what my own clicking on a filter bar does, and ended with "Nobody fished. The garden did." I understood multiple comparisons for the first time as something I do rather than something analysts do wrong.

## 6. Verdict

A research partner could use it as it stands; a creative technologist could use the rules table, the checklist and the claim record but would trip on the forty unexplained back-references and the undefined "brief", "studio", "steer", "version 1" and "Vibe Map"; a funder's analyst would get the argument and lose patience with the research log interrupting the body text, so the chapter is usable by two of the three readers now and by all three once the process notes move to Sources and the first use of each cross-reference carries a one-clause gloss.
