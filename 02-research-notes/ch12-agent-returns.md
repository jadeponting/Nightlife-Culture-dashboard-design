# Chapter 12 — research agent returns (6 October 2026)

*Four agents, dispatched in one message; returns kept whole. Marks: STRING-VERIFIED / SINGLE PASS / ABSTRACT as the agents reported them.*


---

## Agent A

AGENT A — RECOGNITION. Report of 6 October 2026 (all URLs fetched on that date).

TOOLS AND LIMITS
- WebSearch was unavailable for the whole run (the turn's shared search budget was already spent). I worked from direct URLs with WebFetch only. curl from Bash is blocked by the egress proxy, so no quotation could be grep-verified; every check is a WebFetch YES/NO presence re-fetch with a false control string.
- I did not use archive.org or any reader/proxy service.
- Pages I could not read:
  - Rate-limited (429, not retried): doi.org/10.5311/JOSIS.2016.12.232 (paper obtained from josis.org instead); Europe PMC full text for PMC6088455; link.springer.com/article/10.1007/s10464-012-9550-6 (Coulton 2013); ijbnpa.biomedcentral.com/articles/10.1186/1479-5868-7-34 (Smith et al. 2010); pubmed.ncbi.nlm.nih.gov/11446289.
  - Blocked: all tandfonline.com and Wiley pages (403); PMC (reCAPTCHA); psycnet.apa.org, sciencedirect.com and mitpress.mit.edu (robots).
  - Other failures: miguelangelmartinez.net Lynch PDF (connection failed twice); DePaul ABCD Institute (403 twice); JRF report pages (404); tannerlectures (moved, then SSL failure); seeingdata.org sub-pages; gowellonline.com (no content); academic.oup.com (no body served).
- The discipline earned its keep. The reader invented "140 of 192" for Tunstall (true figure 120 of 192) and gave Montello's analysed sample the gender split of the recruited sample. Both were caught on re-fetch.
- Marking: STRING-VERIFIED = presence check passed with a control. SINGLE PASS = read once or twice consistently, no presence check. ABSTRACT = only the abstract was reachable.

A1. COGNITIVE MAPS AND THEIR METHOD
Lynch 1960 — NOT REACHED AT SOURCE. I quote nothing from the book and give no sample sizes. To retrieve: the interview protocol and samples are in Appendix B ("The Use of the Method"); the limits of the sample are discussed there and in the opening of chapter 2.
- Secondary only: Wikipedia "Mental mapping" (https://en.wikipedia.org/wiki/Mental_mapping) attributes to the book the instruction «Make it just as if you were making a rapid description of the city to a stranger, covering all the main features» and «We don't expect an accurate drawing- just a rough sketch». STRING-VERIFIED as present on the Wikipedia page, which is itself quoting Lynch; not checked against the book.
- Same page lists «nodes, edges, districts, paths and landmarks». STRING-VERIFIED on Wikipedia.
Milgram & Jodelet 1976 — NOT REACHED. Nothing quoted, no n.
Kitchin 1994 — NOT REACHED (ScienceDirect robots).
Later methodological evidence I did reach:
- Wang & Schwering 2015, "Invariant spatial information in sketch maps — a study of survey sketch maps of urban areas", Journal of Spatial Information Science 11, 31–52. https://josis.org/index.php/josis/article/download/62/62. Peer-reviewed, open.
  - Task: «Participants were asked to choose two familiar study areas and draw them only based on their memories.» SINGLE PASS.
  - Sample: «In total 21 participants with the average age of 26.5 years (sd =2.7) took part in the study.» «Participants drew in total 45 sketch maps. Three sketch maps were discarded…»; 42 valid maps. SINGLE PASS (returned in the verification pass).
  - Starting point: «sketch maps are incomplete, distorted, and schematized». STRING-VERIFIED.
  - On Lynch: «Lynch proposed five key elements found in the sketch maps of American cities». STRING-VERIFIED.
  - Finding: «a set of seven sketch aspects that constitute invariant spatial information». STRING-VERIFIED. Accuracies reported: topology of street segments 98.0%, orientation of street segments 97.7%, cyclic order 98.7%, topology of city blocks 99.4%, orientation of landmarks 94.9%. SINGLE PASS.
  - Distances «were found either lengthened or shortened without discernable patterns». STRING-VERIFIED.
  - Role: what a hand-drawn map can be trusted for (order, adjacency, which things are there) and what it cannot (distance, angle). Small student-age sample in one German city.
- Gieseking 2013, "Where We Go From Here: The Mental Sketch Mapping Method and Its Analytic Components", Qualitative Inquiry 19(9). https://journals.sagepub.com/doi/10.1177/1077800413500926. ABSTRACT, SINGLE PASS: «I found that the method's development has been uneven and its analytics ad hoc and piecemeal»; «Drawing on 32 mental sketch maps… details a total of 57 analytic components and techniques». Role: a published review saying the method's analysis is not standardised.
Strength of A1 overall: weak. The two founding sources were not read.

A2. RESIDENTS' NEIGHBOURHOODS AGAINST ADMINISTRATIVE UNITS
Coulton, Korbin, Chan & Su 2001, American Journal of Community Psychology 29(2), 371–383. https://link.springer.com/article/10.1023/A:1010303419034. ABSTRACT only, SINGLE PASS.
- «This pilot study tested several methods of defining neighborhood units based on maps drawn by residents, and compared the results with census definitions of neighborhoods.»
- «When residents' maps were used to create neighborhood boundary definitions, the resulting units covered different space and produced different social indicator values than did census-defined units.»
- «Residents' agreement about their neighborhoods' boundaries differed among the neighborhoods studied.»
- n, city and the size/overlap figures are in the paywalled body: NOT OBTAINED.
Coulton, Jennings & Chan 2013 — NOT REACHED (rate-limited). The same Making Connections survey is reported in an open predecessor:
- Coulton, Chan & Mikelbank 2010, "Finding Place in Making Connections Communities: Applying GIS to Residents' Perceptions of Their Neighborhoods", Urban Institute, 30 March 2010. https://www.urban.org/sites/default/files/publication/28471/412057-Finding-Place-in-Making-Connections-Communities.PDF. Research report, not journal-reviewed.
  - Prompt read to residents: «By neighborhood, I mean the area around where you live and around your house. It may include places you shop, religious or public institutions, or a local business district.» First sentence STRING-VERIFIED.
  - Task: draw the boundary in pencil on a street map with the home marked; maps digitised. SINGLE PASS.
  - «A total of 7,498 households was interviewed.» STRING-VERIFIED (7,498). Ten US cities. SINGLE PASS for the list.
  - «Eighty-three percent of the respondents completed maps.» STRING-VERIFIED (figure).
  - «The median area of the RD maps was 0.35 square miles, but there was considerable variation in RD map sizes among sites, from a high of 1.2 square miles in San Antonio to a low of .09 square miles in Hartford.» 0.35 STRING-VERIFIED; range SINGLE PASS.
  - Comparison is with the initiative's own target areas, not tracts: «the typical initiative target area (2.23 square miles)». STRING-VERIFIED.
  - Consensus rule: blocks «included by at least 33 percent of the respondents» who gave the same neighbourhood name. SINGLE PASS.
  - No tract-overlap percentage is given in this report. That figure remains unobtained.
  - Role: the largest reachable measurement of residents' own units. The median drawn area is roughly one sixth of the administrative target area.
Campbell, Henly, Elliott & Irwin 2009; Lee & Campbell 1997; Kearns & Parkinson 2001 (Sage page serves references only); Smith et al. 2010 (the UK drawn-map pilot) — NOT REACHED. Nothing quoted.
UK material reached:
- Lupton 2003, "'Neighbourhood Effects': Can we measure them and does it matter?", CASEpaper 73, LSE. https://sticerd.lse.ac.uk/dps/case/cp/CASEpaper73.pdf. Working paper.
  - Lupton summarising Kearns & Parkinson's three scales (secondary): «One, the home area, has a psycho-social purpose, fostering attachment and belonging, demonstrating and reflecting one's values and making connections with others.» First clause STRING-VERIFIED. «A second, the locality, is the locale for residential activities, and denotes social status and provision.» «Finally, the urban district or region provides a wider landscape of social and economic opportunities.» SINGLE PASS. p. 5 (SINGLE PASS).
  - The "5–10 minutes walk" wording is NOT in Lupton (checked, NO).
  - Lupton quoting Dietz 2002: «neighbourhood delineation has been defined by the limitations of an available data set». STRING-VERIFIED. Lupton quoting McCulloch & Joshi: «ward is a political boundary and therefore arbitrary». STRING-VERIFIED.
  - Lupton cites no UK empirical data on resident-drawn boundaries (reader's finding, SINGLE PASS).
- Understanding Society, variable scopngbha. https://www.understandingsociety.ac.uk/documentation/mainstage/variables/scopngbha/. Official survey documentation. «Here are some statements about neighbourhoods.» «I feel like I belong to this neighbourhood.» Both STRING-VERIFIED. The page gives no spatial definition of "neighbourhood" (checked: no 15- or 20-minute-walk wording). Role: a major UK panel leaves the unit to the respondent.
- OCSI on why the Community Needs Index uses wards: wards «align more closely with community boundaries and are of a sufficient size to cover locally recognised neighbourhoods». https://ocsi.uk/2019/10/21/community-needs-index-measuring-social-and-cultural-factors/. SINGLE PASS. Practitioner rationale, not evidence.
- ONS "Build a custom area profile": see Unasked threads 1.

A3. VERNACULAR AND FUZZY PLACE
Montello, Goodchild, Gottsegen & Fohl 2003, "Where's downtown?: Behavioral methods for determining referents of vague spatial queries", Spatial Cognition and Computation 3(2–3). Author copy: https://people.geog.ucsb.edu/~montello/pubs/downtown.pdf. Peer-reviewed.
- Sample: «Thirty-nine people agreed to participate, 17 females and 22 males. One female and two males were excluded from data analysis because they did not complete the task. The remaining 36 participants ranged in age from 20 to 70 years, with a median age of 42.» SINGLE PASS (returned in the verification pass; the 36 is STRING-VERIFIED via the sentence below).
- Recruitment: «Participants were pedestrians stopped at one of eleven locations on sidewalks near or within the area we anticipated that most people would consider downtown.» SINGLE PASS.
- Task: «outline the area of the city that you consider to be downtown» (STRING-VERIFIED); then the area they were «100% confident was downtown» and «50% confident was downtown» (SINGLE PASS); then a core point.
- «Of the 36 participants, 33 drew 50% regions that are larger than their 100% regions». STRING-VERIFIED.
- «The core was located an average of nearly 300 meters from the centroid of the 100% region». STRING-VERIFIED.
- «respondents will be willing to make discrete judgments about area membership». STRING-VERIFIED. The area studied is described as «a vague region». STRING-VERIFIED.
- Role: the standard small behavioural method for a fuzzy place: default boundary, two confidence boundaries, core. One city, street-intercept sample, read for method only.
Hollenstein & Purves 2010, "Exploring place through user-generated content: Using Flickr tags to describe city cores", JOSIS 1, 21–48. https://josis.org/index.php/josis/article/download/3/3. Peer-reviewed, open. All SINGLE PASS.
- «harvesting georeferenced and tagged metadata associated with 8 million Flickr images».
- «Between 0.5–2% of tags associated with georeferenced images analyzed describe city core areas generically.»
- Tag-location check: «8398 of 9775 (86%) instances were located either within Hyde Park or on adjacent main roads.»
- Prolific-user bias: «42% of the outliers stem from only three contributors who posted 196, 184, and 172 items, respectively.»
- «the demographic of Flickr users themselves who should not be considered to be representative of society as a whole.»
- Vague regions from Gaussian kernel density surfaces.
- Role: passive crowd data can outline a vernacular area, with a measured contributor-concentration problem.
Bostonography, "Crowdsourced neighborhood boundaries, Part One: Consensus", Andy Woodruff, 2 July 2012. https://bostonography.com/2012/crowdsourced-neighborhood-boundaries-part-one-consensus/. Named project/case, read for method only.
- «when we hit 300 submissions recently it seemed like a good enough milestone to take a crack at it.» SINGLE PASS.
- Method: an «arbitrary hexagonal grid» (STRING-VERIFIED); for each cell they tallied the polygons covering it and «divided that count by the total number of respondents» (STRING-VERIFIED).
- Thresholds: «greater than 25% agreement, greater than 50%, and greater than 75%» (SINGLE PASS), described as «a notable minority, a majority, and a strong majority» (STRING-VERIFIED).
- Caveat: agreement holds «at least among the self-selected people who responded to the survey». SINGLE PASS.
- Role: a published way to show agreement bands rather than one line.
Twaroch/Jones "vernacular geography" and Brindley et al. 2018 — NOT REACHED.

A4. PERSONAL RELEVANCE AND ATTENTION TO DATA ABOUT ONE'S OWN PLACE OR GROUP
Peck, Ayuso & El-Etr 2019, "Data is Personal", CHI 2019. https://arxiv.org/pdf/1901.01920. Peer-reviewed; qualitative.
- Method: «In 42 semi-structured interviews in rural Pennsylvania (USA)» (STRING-VERIFIED). Participants ranked 10 charts on one topic with the prompt «Based on how useful they are to you, arrange the graphs from most useful to least useful» (STRING-VERIFIED). Recruitment: 13 university staff, 5 construction-site employees, 24 farmers' market visitors (SINGLE PASS).
- Headline, authors' words: «The most recurring theme in our analysis were decisions framed or driven by personal experience». STRING-VERIFIED.
- «Regardless of style, clarity, or ease-of-understanding, our interviews served as a reminder that data can be intimate and personal, and that those ties may supersede many other dimensions of design.» Core clause STRING-VERIFIED.
- Counts: «We found more than 20 instances in which participants referenced a relatable component» (STRING-VERIFIED). «When participants commented about the geographical data, we found at 6 instances in which conversation focused on locations where they either live currently (looking for 'home') or had lived previously» (SINGLE PASS; "at 6" is as returned).
- Participant: «It has my own county in it. If this would have been like all the countries of the world or something, I really wouldn't have been interested in it because it just affects me personally.» First and last clauses STRING-VERIFIED.
- Participant: «I think in this one, Pennsylvania stuck out more to me than this one.» STRING-VERIFIED.
- Design implication, authors: «our participants' focus on their local region may have design implications for rural populations» (STRING-VERIFIED). Also «it may be necessary to not only provide mechanisms that allow people to explore personal dimensions of data, but to make sure those personal dimensions are front-and-center in first encounters with a visualization.» (SINGLE PASS).
- Political identity: «Breitbart, for example, is a far-right news outlet that expectantly drew lower rankings from participants who identified as liberals.» SINGLE PASS.
- Limits: «It is unclear how representative our sample is» and «The findings in this paper should be replicated with controlled studies, different populations, and larger sample sizes». Both STRING-VERIFIED. They also say the "useful" framing should be contrasted with others (SINGLE PASS).
- Role: the best-known evidence that "is my place in it" drives attention. It is interview evidence on one topic with a self-reported "usefulness" ranking, not a measured attention or recall effect.
Kennedy, Hill, Allen & Kirk 2016, "Engaging with (big) data visualizations: Factors that affect engagement and resulting new definitions of effectiveness", First Monday 21(11). https://firstmonday.org/ojs/index.php/fm/article/download/6389/5652. Peer-reviewed, open. This is the Seeing Data study.
- «We carried out nine focus groups with a total of 46 participants». STRING-VERIFIED.
- «Twenty-seven participants were female and 19 male; ages ranged from 11 to 70». STRING-VERIFIED.
- Diaries and interviews: 13 asked; «Seven participants agreed to do this». STRING-VERIFIED.
- Six factors: subject matter; source/media location; beliefs and opinions; time; emotions; confidence and skills. SINGLE PASS.
- «When subject matter spoke to participants' interest, they were engaged» (STRING-VERIFIED) «— this was particularly evident with Civil Society group members who were interested in issues relating to migration and therefore in the migration visualizations.» (SINGLE PASS).
- «Strong emotions may arise when considering a visualization, and these also affect engagement». STRING-VERIFIED.
- Role: relevance is one of six engagement factors. The paper frames it as interest in a subject, not as seeing one's own place. I found no "I'm in there" wording in any text I could read.
Kennedy & Hill 2018, "The Feeling of Numbers", Sociology 52(4). https://journals.sagepub.com/doi/full/10.1177/0038038516674675. ABSTRACT only, SINGLE PASS (Sage served it as restricted): «We draw on an empirical study to show a wide range of emotional engagements with diverse aspects of data and their visualisation, and so demonstrate the importance of emotions as vital components of making sense of data.» Method, n and any own-place findings: NOT OBTAINED.
Kennedy, Hill, Aiello & Allen 2016 ("The work that visualisation conventions do") — NOT REACHED. seeingdata.org findings pages — NOT REACHED (home page only).
Burns, Xiong, Franconeri, Cairo & Mahyar 2020, BELIV. https://arxiv.org/pdf/2009.01747. All SINGLE PASS.
- «We diagnose levels of understanding of visualized data by adapting Bloom's taxonomy, a common framework from the education literature.»
- Six levels: knowledge, comprehension, application, analysis, synthesis, evaluation.
- «we found few examples of dependent relationships between performance at different levels for our three case studies.»
- Reader reported 60 Mechanical Turk workers per case study (not checked).
- Role: a test frame in which "recognising" is a different level from reading a value off.
Experimental evidence on own-locality — the only experiment I could reach:
- Kim, Hullman & Agrawala 2016, "Generating Personalized Spatial Analogies for Distances and Areas", CHI 2016. https://idl.cs.washington.edu/files/2016-SpatialAnalogies-CHI.pdf.
  - Result: users «rate the helpfulness of the information for understanding a distance or area 1.9 points higher (on a 7 pt scale)» than with no analogy, and «0.7 points higher than when they see generic spatial analogy». Both STRING-VERIFIED.
  - Premise: «people struggle to understand these measurements when they cannot relate them to measurements of locations that they are personally familiar with». STRING-VERIFIED.
  - 40 Mechanical Turk workers, 399 valid trials; means 4.31 against 2.41. SINGLE PASS.
  - The measure is self-rated helpfulness, not comprehension or recall.
- PersaLog (Adar et al., CHI 2017; http://www.cond.org/persalog.pdf) has no reader-effect experiment: only a survey of 22 journalists and a language-usability test with 11 students (SINGLE PASS).
- I found no controlled study showing readers attend to or remember more when a chart is about their own locality. That may be a real gap or a search failure; I could not search.

A5. MEMBER CHECKING AS COMMUNITY REVIEW
Lincoln & Guba 1985, p. 314 — the book was not reached. How I got the phrase: the Qualitative Research Guidelines Project page "Member Checks" (http://www.qualres.org/HomeMemb-3696.html; I know this as Cohen & Crabtree's RWJF-funded project, 2006, but the page as read did not name its publisher).
- «Lincoln and Guba posit that this is the most crucial technique for establishing credibility». STRING-VERIFIED on that page. It is the page's paraphrase with the phrase embedded, gives no page number («p. 314» checked: NO), and references «Lincoln, YS. & Guba, EG. (1985). Naturalistic Inquiry. Newbury Park, CA: Sage Publications.»
- Same page's definition: «This is when data, analytic categories, interpretations and conclusions are tested with members of those groups from whom the data were originally obtained». STRING-VERIFIED.
- Note "members of those groups": the definition already allows review by a group, not only by the individuals sampled.
- The page-314 attribution itself remains unverified.
Candela 2019, "Exploring the Function of Member Checking", The Qualitative Report 24(3), 619–628. https://nsuworks.nova.edu/cgi/viewcontent.cgi?article=3726&context=tqr. Peer-reviewed, open; a reflective case.
- «Member checking is commonly used in qualitative research as a means to maintain validity». STRING-VERIFIED.
- Design: three teachers. What was returned was the completed written analysis (each person's analysis plus cross-case themes), emailed, with a meeting requested; two were interviewed about it, one approved by email. SINGLE PASS. The abstract speaks of «the experiences of two participants».
- Harm: the returned analysis was described as «not flattering» (STRING-VERIFIED); «I may have caused harm to Mrs. O'Neill as I was sending back a negative analysis of her situation» (STRING-VERIFIED).
- Proposal: «member checking should be used as a reflective space for participants». STRING-VERIFIED.
- Candela does NOT contain "the most crucial technique" (checked: NO). She cites «Lincoln and Guba (1986)… (p. 77)» for a definition.
- Role: a documented case of a check harming a participant by returning an unflattering portrait, which is the dashboard's risk at community scale.
Carlson 2010, "Avoiding Traps in Member Checking", The Qualitative Report 15(5). https://nsuworks.nova.edu/cgi/viewcontent.cgi?article=1332&context=tqr. SINGLE PASS: form of return: «Choices may include hard copies, electronic copies, listening to the audiotapes with the researcher, or having the researcher read the transcripts aloud.» Does not cite Lincoln & Guba.
Birt et al. 2016 (Synthesized Member Checking procedure) — full text NOT REACHED; procedure not obtained. Motulsky 2021 — NOT REACHED (APA robots).
Data Walks: Murray, Falkenburger & Saxena, Urban Institute, 10 November 2015. https://www.urban.org/sites/default/files/2022-03/2000510-data-walks-an-innovative-way-to-share-data-with-communities.pdf. Practitioner guide.
- Definition: an interactive way for community stakeholders «to engage in dialogue around research findings about their community» (SINGLE PASS; spacing in the PDF text is broken). Participants «rotate through 'stations'» (STRING-VERIFIED).
- Purposes (SINGLE PASS): share key data and findings with residents and programme participants; ensure a more robust analysis and understanding of the data; inform better programming and policies «to address both strengths and needs»; inspire individual and collective action.
- Procedure: groups of «no more than four or five people» (STRING-VERIFIED); «five stations at about six minutes per station» (STRING-VERIFIED); data on large posters in text and graphic form with benchmarks; one or two broad questions plus station questions; a chime to rotate; then a full-group share-out with one takeaway per station (SINGLE PASS).
- Ground rule: «leave titles at the door». STRING-VERIFIED.
- Caution: «We feared that sharing too many bleak statistics around risky youth behaviors would only reinforce negative messages and stereotypes, disempowering residents even further.» Opening STRING-VERIFIED.
- Evaluation: none. Outcomes are anecdotal; no counts or satisfaction data. The control string about an RCT returned NO; closest text: «DataWalks have proven to be a useful and effective tool».
- Role: the most concrete procedure for putting findings in front of a community before publication. It is a guide, not an evaluated method.
CBPR principles: Detroit Urban Research Center, nine principles after Israel et al., "Revised and Adopted by the Detroit URC Board on January 20, 2011". https://www.detroiturc.org/about-cbpr/community-based-participatory-research-principles. Practitioner standard.
- Principle 7 heading: «CBPR disseminates findings and knowledge gained to the broader community and involves all partners in the dissemination process». SINGLE PASS.
- Text: «CBPR projects produce, interpret and disseminate findings to community members in clear language respectful to the community» and «in ways which will be useful for developing action plans that will benefit the community». Both STRING-VERIFIED.
- Partners are involved «as reviewers and co-authors of publications, and co-presenters at conferences and workshops». STRING-VERIFIED.
- Principle 2: «CBPR recognizes community as a unit of identity». SINGLE PASS.
- Israel et al. 1998 itself: abstract only at Annual Reviews; principles text not served.
Urban Institute, Gaddy & Scott, "Principles for Advancing Equitable Data Practice", June 2020. https://www.urban.org/sites/default/files/publication/102346/principles-for-advancing-equitable-data-practice.pdf. Practitioner framework. All SINGLE PASS: «Seek out and incorporate communities' interpretation of the data.» «Return data and research results to community members in a form they can use.» «Account for how publication may reinforce inequities or close disparities.»
Participatory mapping, the community review step: Rambaldi, Chambers, McCall & Fox 2006, "Practical ethics for PGIS practitioners, facilitators, technology intermediaries and researchers", Participatory Learning and Action 54, 106–113. https://www.iied.org/sites/default/files/pdfs/migrate/G02957.pdf. Practitioner ethics code.
- «Who owns the output? Who owns the map(s)? Who owns the resulting data?» STRING-VERIFIED.
- Under "Review and revise the maps": «The maps are never final or static» and «they have to be crosschecked, improved, and updated». Both STRING-VERIFIED.
- Under "Ensure genuine custodianship": «the original physical output of a participatory mapping exercise stays with those who generated it». STRING-VERIFIED. Continues «and specifically with a trusted entity nominated by the informants». SINGLE PASS.
- «Avoid exposing people to danger». STRING-VERIFIED.
Sieber 2006, Elwood 2006, Peluso 1995 — NOT REACHED. Secondary only, Wikipedia "Counter-mapping" (https://en.wikipedia.org/wiki/Counter-mapping):
- «Counter-mapping is the creation of maps that challenge 'dominant power structures, to further seemingly progressive goals'.» Inner phrase STRING-VERIFIED on Wikipedia; Wikipedia attributes it to Hodgson & Schroeder 2002, not Peluso.
- «The term came into use in the United States when Nancy Peluso used it in 1995 to describe the commissioning of maps by forest users in Kalimantan, Indonesia, to contest government maps of forest areas that undermined indigenous interests.» SINGLE PASS.
- Criticism recorded there: counter-mapping may «reify, reinforce, and extend settler boundaries even as it seeks to challenge dominant mapping practices». STRING-VERIFIED on Wikipedia.

A6. RECOGNITION AS A POLITICAL CATEGORY — FRAME ONLY, NO AUTHORITY DRAWN
Taylor, "The Politics of Recognition". Primary text not reached. Via the Internet Encyclopedia of Philosophy, "Social and Political Recognition" (Paddy McQueen), https://iep.utm.edu/recog_sp/, which quotes Taylor and cites (Taylor, 1994: 26):
- «Nonrecognition or misrecognition can inflict harm, can be a form of oppression, imprisoning someone in a false, distorted, and reduced mode of being». STRING-VERIFIED on the IEP page; IEP is the source quoting Taylor.
- «can inflict a grievous wound, saddling its victims with a crippling self-hatred». STRING-VERIFIED on IEP.
- The sentence "Due recognition is not just a courtesy…" is NOT on the IEP page (checked: NO); only the phrase «a vital human need» appears.
Honneth: IEP's summary gives three spheres — love, rights, solidarity. Reader paraphrase, SINGLE PASS, not verbatim. Honneth's book not reached.
Fraser 2000, "Rethinking Recognition", New Left Review 3. https://newleftreview.org/issues/ii3/articles/nancy-fraser-rethinking-recognition. Only the opening paragraphs are outside the paywall.
- «questions of recognition are serving less to supplement, complicate and enrich redistributive struggles than to marginalize, eclipse and displace them». STRING-VERIFIED.
- «I shall call this the problem of displacement». STRING-VERIFIED. «I shall call this the problem of reification». STRING-VERIFIED.
- «Both problems—displacement and reification—are extremely serious: insofar as the politics of recognition displaces the politics of redistribution, it may actually promote economic inequality; insofar as it reifies group identities, it risks sanctioning violations of human rights and freezing the very antagonisms it purports to mediate.» SINGLE PASS (returned identically twice, no presence check).
- "parity of participation" and "status subordination" are not in the visible portion (checked: NO).
Fraser 1995, "From Redistribution to Recognition?", NLR I/212. https://newleftreview.org/issues/i212/articles/nancy-fraser-from-redistribution-to-recognition-dilemmas-of-justice-in-a-post-socialist-age. Opening only. SINGLE PASS: «The 'struggle for recognition' is fast becoming the paradigmatic form of political conflict in the late twentieth century.» «Cultural domination supplants exploitation as the fundamental injustice.» (The second states the view she goes on to contest.)
Participatory parity, via IEP quoting Fraser & Honneth 2003, p. 36: «justice requires that social arrangements permit all (adult) members of society to interact with one another as peer». STRING-VERIFIED as IEP prints it, including "peer" for "peers", which looks like IEP's typo. Fraser's Tanner Lecture, which would give this at source, was not reachable.
Critique: IEP's criticism headings are The Reification of Identity; The Accusation of Essentialism; The Danger of Subjectivism; The Problem of the Other; The Post-Structural Challenge (SINGLE PASS). I found no reachable source on misuse of the frame in policy.
Role: gives the chapter two named hazards for any "recognition" claim — displacement (a display of identity standing in for a comparison of conditions) and reification (a profile freezing a group identity).

A7. TERRITORIAL STIGMA AND ITS MEASUREMENT
Wacquant 2007, Thesis Eleven 91, 66–77. Author copy: https://loicwacquant.org/wp-content/uploads/2019/03/lw-2007-territorial-stigmatization-in-the-age-of-advanced-marginality.pdf. Theory.
- «Whether or not these areas are in fact dilapidated and dangerous, and their population composed essentially of poor people, minorities and foreigners, matters little in the end: the prejudicial belief that they are suffices to set off socially noxious consequences.» Opening and closing clauses STRING-VERIFIED.
- «A blemish of place is thus superimposed on the already existing stigmata traditionally associated with poverty and ethnic origin or postcolonial immigrant status, to which it is closely linked but not reducible.» Main clause STRING-VERIFIED.
- Of Goffman's three types of stigma, «it is to the third that territorial stigma is akin». STRING-VERIFIED.
- «People there commonly hide their address». STRING-VERIFIED.
- Printed page 66 for the first two (SINGLE PASS).
Wacquant, Slater & Pereira 2014, Environment and Planning A 46(6), 1270–1280. https://journals.sagepub.com/doi/10.1068/a4606ge. ABSTRACT; fragments STRING-VERIFIED.
- The concept is meant «to capture how the blemish of place impacts the residents of disparaged districts».
- It has become «autonomized, nationalized and democratized, equated with social disintegration, racialized through selective accentuation».
- Residents' strategies span a «panoply ranging from submission to defiance».
- «Territorial stigmatization is not a static condition or a neutral process, but a consequential and injurious form of» «action through collective representation fastened on place».
- Policy should reduce «not only the burden of material deprivation, but also the press of symbolic domination in the metropolis».
- No measurement instrument is offered (control string about a scale: NO).
Tunstall, Green, Lupton, Watmough & Bates 2014, Urban Studies 51(4). https://journals.sagepub.com/doi/10.1177/0042098013492230. Peer-reviewed field experiment, JRF-funded; full text readable.
- Design: «2001 applications to 667 real jobs by fictional candidates nominally resident in neighbourhoods with poor and bland reputations» (figures STRING-VERIFIED). Three candidates per job, three local labour markets in England and Wales, low-skilled jobs (SINGLE PASS).
- «In 475 (71 per cent) of the 667 jobs applied for, none of the three candidates received a first-stage positive response. In the remaining 192 (29 per cent) of jobs, employers gave a positive response to one or more of our candidates for the same post.» SINGLE PASS.
- «A total of 17 per cent of the 2001 applications received one of a range of first-stage positive responses.» SINGLE PASS.
- Table 2, among the 192 jobs with any positive response: bland reputation 120 of 192 = 62.5%; poor reputation 230 of 384 = 59.9%. 120, 59.9 and 62.5 STRING-VERIFIED; 140 confirmed absent.
- Net preference «2.6 percentage points» (STRING-VERIFIED), p = «0.1170» (STRING-VERIFIED), «two-sample z-test for proportions» (STRING-VERIFIED).
- «However, the net preference was small and it was not statistically significant at the 1 per cent, 5 per cent or 10 per cent level.» SINGLE PASS.
- Abstract conclusion: people in such neighbourhoods «did not face 'postcode discrimination' in the labour market, at the initial selection stage». STRING-VERIFIED.
- Limits: «It remains possible that, in a larger correspondence test study, the net preferences found would achieve statistical significance.» SINGLE PASS.
- Role: the one causal UK test of a reputation penalty. The direction ran against poor-reputation addresses, the size was small, and it was not significant. It tests only employers' first response, not other harms of a label.
Slater 2018, "The invention of the 'sink estate'", The Sociological Review. https://journals.sagepub.com/doi/10.1177/0038026118777451. ABSTRACT, SINGLE PASS: a category «invented by journalists, amplified by free market think tanks and converted into policy doxa (common sense) by politicians»; «This derogatory designator… has become the symbolic frame justifying current policies towards social housing». Role: a case of a label doing policy work.
Hastings 2004, Journal of Housing and the Built Environment 19, 233–254. https://link.springer.com/article/10.1007/s10901-004-0723-y. ABSTRACT, SINGLE PASS: the literature shows «a subtle adherence to pathological explanations»; the paper offers a framework that moves «beyond pathological explanations to focus on the roles and contributions of external actors and influences». Number of estates and interviews not shown.
Permentier, van Ham & Bolt 2008 (Housing Studies) — NOT REACHED; no n, no insider/outsider figures. Their related paper, Permentier, Bolt & van Ham 2011, Urban Studies 48(5), https://journals.sagepub.com/doi/10.1177/0042098010367860, ABSTRACT, SINGLE PASS:
- Defines perceived reputation as «how they think other city residents see their neighbourhood».
- Survey in Utrecht (n not in the abstract).
- «subjective assessment of the dwelling and neighbourhood attributes are more important in explaining neighbourhood satisfaction than in explaining perception of reputation. Objective neighbourhood variables are more important in explaining perception of reputation than in explaining neighbourhood satisfaction.»
Kearns, Kearns & Lawson 2013 — NOT REACHED (T&F 403; GoWell site closed). No article counts obtained.

A8. THE OFFICIAL LABEL DEBATES
(a) English Indices of Deprivation.
IoD2019 FAQ, MHCLG. https://assets.publishing.service.gov.uk/media/5dfb3d7ce5274a3432700cf3/IoD2019_FAQ_v4.pdf. Official guidance. Question numbers are SINGLE PASS.
- «This means it can tell you if one area is more deprived than another but not by how much.» SINGLE PASS for the whole sentence; «but not by how much» STRING-VERIFIED.
- «For example, a small area with a rank of 1,000 is not half as deprived as a place with a rank of 500.» STRING-VERIFIED (Q19).
- «Within every area there will be individuals who are deprived and individuals who are not.» STRING-VERIFIED. «The Index is not a suitable tool for targeting individuals.» STRING-VERIFIED.
- «It is common to describe how relatively deprived a neighbourhood is by saying whether it falls among the most deprived 10 per cent» (STRING-VERIFIED, Q9), with «there is no definitive cut-off at which an area is described as 'deprived'» (STRING-VERIFIED).
- «The IMD2019 is designed to identify aspects of deprivation, not affluence.» STRING-VERIFIED. Continues: «Such an area may be ranked among the least deprived in the country, but it is not necessarily among the most affluent.» SINGLE PASS.
- "Can't be used for" items: «Quantifying how deprived a small area is» (STRING-VERIFIED); «Identifying deprived people»; «Measuring real change in deprivation over time» (SINGLE PASS).
IoD2025 exists: published 30 October 2025, Ministry of Housing, Communities and Local Government.
IoD2025 FAQ. https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025/english-indices-of-deprivation-2025-frequently-asked-questions.
- «This means that each can tell you if one area is more deprived than another but not by how much.» STRING-VERIFIED (Q23, number SINGLE PASS).
- «It is common to describe how relatively deprived a neighbourhood is by saying whether it falls among the most deprived 10%, 20% or 30% of small areas in England» (STRING-VERIFIED) «(although there is no definitive cut-off at which an area is described as 'deprived')» (STRING-VERIFIED).
- The 2019 sentences on individuals and on rank 1,000/500 recur (STRING-VERIFIED / SINGLE PASS respectively).
IoD2025 Statistical Release, Introduction. https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025/english-indices-of-deprivation-2025-statistical-release. All STRING-VERIFIED:
- «High ranking LSOAs or neighbourhoods can be referred to as the 'most deprived' or as being 'highly deprived' to aid interpretation».
- «However, there is no definitive threshold above which an area is described as 'deprived'».
- «Across the IoD25, deprivation is measured on a relative rather than an absolute scale» … «a neighbourhood ranked 100th is more deprived than a neighbourhood ranked 200th, but this does not mean it is twice as deprived».
- «At the neighbourhood-level, the IoD25 provides a place-based insight into deprivation». «However, this description does not apply to every person living in these areas». «Many non-deprived people live in deprived areas, and many deprived people live in non-deprived areas.»
- «the IoD25 is designed to identify and measure specific aspects of deprivation, rather than measures of affluence».
- Cannot be used to «quantify how deprived a neighbourhood is», «identify deprived people», «say how affluent a place is».
- I found no official sentence contrasting "deprived" with "relatively more deprived" as such. The nearest is the "no definitive cut-off/threshold" wording plus the licence to say "most deprived" or "highly deprived".
(b) Output Area Classifications.
Gale, Singleton, Bates & Longley 2016, "Creating the 2011 area classification for output areas (2011 OAC)", JOSIS 12, 1–27. https://josis.org/index.php/josis/article/download/66/66. Peer-reviewed, open. Section 7, pp. 15–16 (location SINGLE PASS).
- Why names are contentious: «Vickers et al. [58] noted that names and descriptions of clusters may be contentious, especially if they reinforce negative stereotypes.» … «However, past experience in both the private and public sector confirms that this procedure does help end users to identify with the names and descriptions given to local areas.» SINGLE PASS.
- «words and phrases that might be construed as pejorative were not used». STRING-VERIFIED.
- «all descriptors had strong and literal links to the underlying distributions revealed by the data». STRING-VERIFIED.
- «Words that were overtly negative or positive were avoided where possible». STRING-VERIFIED.
- The aim was to present cluster characteristics «as consequences of factors that have happened to areas rather than the consequences of human agency». STRING-VERIFIED.
- «final approval of the cluster names was sought from ONS who conducted their own internal review and consultation». STRING-VERIFIED.
- Names were «checked against local knowledge of areas» and checked so as not to duplicate earlier commercial and non-commercial classifications. SINGLE PASS.
- Supergroup names (Table 4): Rural Residents; Cosmopolitans; Ethnicity Central; Multicultural Metropolitans; Urbanites; Suburbanites; Constrained City Dwellers; Hard-Pressed Living. The last two STRING-VERIFIED, the rest SINGLE PASS.
- Role: a stated naming rule — literal, not pejorative, neither negative nor positive, conditions not agency — and its own output still includes "Hard-Pressed Living" and "Constrained City Dwellers".
2021 OAC: names and naming procedure NOT OBTAINED. The ONS page (https://www.ons.gov.uk/methodology/geography/geographicalproducts/areaclassifications/2021residentialbasedareaclassifications) hosts neither names nor a naming statement and points to the Geographic Data Service and to Wyszomierski et al. 2024 (DOI 10.1111/geoj.12550; Wiley 403). The Geographic Data Service page says «8 different supergroups, into which are nested 21 groups and 52 sub-groups» (SINGLE PASS); pen portraits are behind a login. I list no 2021 names.
(c) "Left behind" neighbourhoods. Local Trust/OCSI, "Left behind? Understanding communities on the edge", August 2019. https://localtrust.org.uk/wp-content/uploads/2019/08/local_trust_ocsi_left_behind_research_august_2019.pdf. Funder/consultancy research.
- Definition: wards in the worst 10% on both the IMD and the new Community Needs Index; 206 wards (STRING-VERIFIED), population 2,193,000 (STRING-VERIFIED). The web page reports 225 wards after the IMD 2019 update (SINGLE PASS; https://localtrust.org.uk/insights/research/left-behind-understanding-communities-on-the-edge/).
- Index: 19 indicators in three domains — Civic Assets, Connectedness, Active and Engaged Community (SINGLE PASS, OCSI page).
- The report's boxed "A note on terminology" (pp. 6–7, location SINGLE PASS): «The term 'left behind' is controversial and contentious. It has been argued that it is patronising…» (SINGLE PASS). «Some suggest that a better term would be 'held back'…» (SINGLE PASS).
- «We do not use it to imply that the areas so described lack people with skills and commitment or a rich heritage.» STRING-VERIFIED.
- «they have tended not to receive a fair share of the investment available». STRING-VERIFIED.
- «It is also a term that people seem to instinctively understand» (STRING-VERIFIED), «which has political, social and cultural resonance. This is why, despite its difficulties, and in the absence of better, we decided to use it for the research described in this report.» (SINGLE PASS).
- Caveat on unit: «ward-level data can mask variations in need at the very local level». STRING-VERIFIED.
- Independent published criticism was not reached (the OUP article served no body; T&F blocked). The criticism I can report is the one the authors themselves record.
(d) SIMD 2020, Scottish Government. Official guidance. All STRING-VERIFIED.
- Collection page, https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/:
  - «The Scottish Index of Multiple Deprivation is a relative measure of deprivation across 6,976 small areas (called data zones).»
  - «SIMD is an area-based measure of relative deprivation: not every person in a highly deprived area will themselves be experiencing high levels of deprivation.»
  - «If an area is identified as 'deprived', this can relate to people having a low income but it can also mean fewer resources or opportunities.»
- "How can I use SIMD?", https://www.gov.scot/publications/scottish-index-multiple-deprivation-2020/pages/4/, under the heading "Do not use SIMD for":
  - «Saying how much more deprived one area is from another» – «the difference between two ranks can be tiny or large».
  - Identifying all people experiencing deprivation – «not everyone facing disadvantage lives in a deprived area».
  - «Identifying affluent areas» – «lack of deprivation is not the same as being rich».
  - Comparing ranks over time – «changes are relative and may not reflect actual changes in the neighbourhood».
- Next page (/pages/5/): «SIMD identifies deprived areas - not people.» SINGLE PASS.
- The wording you gave ("not every person in a highly deprived area will themselves be experiencing high levels of deprivation") is exact.

A9. STRENGTHS-BASED REPORTING GUIDANCE
GCPH, "Asset based approaches for health improvement: redressing the balance", Briefing Paper 9, Concepts Series, Dr Jennifer McLean, October 2011. https://www.gcph.co.uk/assets/0000/2627/GCPH_Briefing_Paper_CS9web.pdf. Practitioner briefing.
- Definition (quoting Morgan & Ziglio 2007): «A health asset is any factor or resource which enhances the ability of individuals, communities and populations to maintain and sustain health and wellbeing». STRING-VERIFIED.
- The balance: the case rests on «achieving a better balance between responding to needs» and respecting assets. STRING-VERIFIED fragment.
- Cautions, all STRING-VERIFIED:
  - «Asset based approaches are not a replacement for investing in service improvement or attempting to address the structural causes of health inequalities».
  - «evidence of the effectiveness of these approaches at present largely comes from case studies and small scale exploratory research».
  - «Asset based approaches are not a no-cost or money saving option».
  - «…it is also conceivable that the adoption of asset based approaches may increase health inequalities.» (fragment verified).
- «asset based approaches should be embedded alongside, and be complementary to, traditional health promotion interventions.» SINGLE PASS.
GCPH, "Putting asset based approaches into practice: identification, mobilisation and measurement of assets", Briefing Paper 10, July 2012. https://www.gcph.co.uk/assets/000/000/214/GCPHCS10forweb_1__original.pdf?1700036395.
- «difficulties are inherent in measuring assets». STRING-VERIFIED.
- «One of the initial challenges for asset working is to find and collate data that measure positive health and wellbeing» (STRING-VERIFIED) «…in order to balance the traditional mortality, morbidity and conditions related statistics that describe individuals and communities in deficit terms.» (SINGLE PASS).
- Asset mapping is «the essential starting point» and «more than just gathering data». Both STRING-VERIFIED.
Fogarty, Lovell, Langenberg & Heron 2018, "Deficit Discourse and Strengths-based Approaches", The Lowitja Institute, Melbourne. https://www.lowitja.org.au/wp-content/uploads/2023/05/deficit-discourse-strengths-based.pdf. Commissioned review. Page numbers varied between passes; treat as approximate.
- Definition: «discourse that represents people or groups in terms of deficiency – absence, lack or failure». STRING-VERIFIED. It «narrowly situates responsibility for problems with the affected individuals or communities, overlooking the larger socio-economic structures». STRING-VERIFIED.
- Not denial: «These should not be mistaken for calls to deflate the realities of disadvantage». STRING-VERIFIED.
- On gap framing: it «certainly appears to carry (and replicate) an implicit assumption of deficit». STRING-VERIFIED.
- «Halpern (2015) further argues that continual reporting of negative stereotypes and prevalence rates actually reinforces undesired behaviour.» STRING-VERIFIED core; the report is citing Halpern.
- Quoting Jirra Lulla Harvey: «These statistics became like a mantra» … «I felt like statistics were defining my cultural identity» … «I was worried about the rhetoric of disadvantage governing the lives of young Aboriginal people». Each STRING-VERIFIED; the report is quoting her.
- Quoting Stoneham, Goodman & Daube 2014: «74 percent of media coverage of Indigenous related articles were negative, 15 percent were positive and 11 percent were neutral». «74 percent of media coverage» STRING-VERIFIED; the report is quoting that study.
- Evidence base: «a real paucity of strong qualitative evaluation»; «almost a complete lack of evaluation of actual impact on discourse itself»; «we found no evaluation techniques specifically designed to measure or demonstrate shifts in the discourse». All STRING-VERIFIED.
- Recommended practice for data reporting is thin in what I read: balance, correcting negative stereotypes, and wording choices. I found no worked statistical recommendation. The last ~14,000 characters of the PDF were not read.
Kretzmann & McKnight 1993 — NOT REACHED (403 twice). The needs-map/assets-map passage is not quoted.
Evaluation evidence, not advocacy:
- The two reviews above both say the effectiveness evidence is case-study level.
- Quinn 2020, "Experimental Effects of 'Achievement Gap' News Reporting…", Educational Researcher. https://journals.sagepub.com/doi/10.3102/0013189X20932469. ABSTRACT, SINGLE PASS. Three randomised experiments.
  - A news story about group gaps, against a control or counter-stereotypical video, «led viewers to express more exaggerated stereotypes… (Study 1 effect size = .30 SD; Study 2 effect size = .38 SD)».
  - It «did not affect viewers' explicit competence-related racial stereotyping, the explanations they gave for achievement inequalities, or their prioritization of ending achievement inequalities».
  - «After 2 weeks, the effect on stereotype exaggeration faded.»
  - n is not in the abstract.
- Holder & Xiong 2022, "Dispersion vs Disparity: Hiding Variability Can Encourage Stereotyping When Visualizing Social Outcomes", IEEE TVCG. https://arxiv.org/pdf/2208.04440.
  - «But bar charts may encourage deficit thinking», defined as «the perception that outcome disparities are caused by groups' personal strengths or deficiencies, rather than external factors». Both STRING-VERIFIED.
  - «We conducted four experiments examining design choices that influence attribution biases». STRING-VERIFIED.
  - «Hiding variability tends to increase stereotyping while emphasizing variability reduces it». STRING-VERIFIED.
  - Participants 329, 434, 281 and 266, Mechanical Turk, US. SINGLE PASS. Experiment 1 personal-attribution difference 7.06 points on a 0–100 slider, d = 0.322; Experiment 4 no significant effect. SINGLE PASS.
  - ANOMALY: on two passes the reader returned the abstract as saying participants «agreed less with personal explanations» in BOTH conditions, and the check for "agreed more" in the first clause returned NO. Either the arXiv text has a typo or the reader erred. The verified closing sentence gives the direction. Do not quote the "Overall, when participants saw…" sentence without checking the IEEE version.
  - Role: experimental evidence that a group-comparison chart can itself produce deficit readings.

ALSO ASKED: DO PEOPLE USE OR TRUST A PUBLIC DATA TOOL DIFFERENTLY WHEN IT SHOWS THEIR OWN AREA?
- ONS Digital blog, Daniel Wainwright, 27 January 2023, "Semi-automation and Census 2021: how we told 331 local stories in one go". https://digitalblog.ons.gov.uk/2023/01/27/semi-automation-and-census-2021-how-we-told-331-local-stories-in-one-go/. Official practice blog, not a research report. All STRING-VERIFIED unless marked.
  - «We tested the concept with different users who really valued being able to read all about the place they call home in a journalistic style.» (SINGLE PASS for the full sentence; "really valued… journalistic style" verified.)
  - «It was something they didn't expect from the Office for National Statistics (ONS) and they meant that in a good way».
  - «Within a few days of publication in December 2022, every individual area's page had been read».
  - «The story was taken up by dozens of local news titles».
  - Audience: «citizen users, those without a background in statistics».
  - No participant numbers, no page-view counts and no trust measure are given.
- Peck et al. (A4) is the only reachable study touching attention to one's own area.
- Statistics Canada: nothing found; I had no URL and could not search.

UNASKED THREADS
1. ONS "Build a custom area profile". https://digitalblog.ons.gov.uk/2023/01/17/custom-profiles/ (Ahmad Barclay, 17 January 2023). Official practice. Previously «getting data for your own custom area required an ability to work with GIS mapping software»; now users «simply select an area on a map and get the data directly, skipping all the complicated middle steps»; output areas «can be added together to provide data for any larger area», selected by «population weighted centroid». All STRING-VERIFIED. The May 2025 update post says the tool was «designed to help people get census data that didn't fit standard geographies» (SINGLE PASS). An official statistics body already lets a reader draw their own unit.
2. House of Commons Library MSOA Names. https://houseofcommonslibrary.github.io/msoanames/. Named project.
   - «MSOAs were not given recognisable names when designed» (STRING-VERIFIED); the default looks like «Ashfield 004» (STRING-VERIFIED).
   - Names are «based on the towns, villages and neighbourhoods that they cover» (STRING-VERIFIED).
   - Community review: «In January 2019 we published draft names on an interactive map website to invite feedback and suggestions on our first draft set»; «This remained open until July 2019 and provided invaluable local knowledge» (SINGLE PASS).
   - «The names aren't intended to supplant any names that might already be used locally and they aren't 'official' names for MSOAs» (STRING-VERIFIED).
   - «Because MSOAs are a statistical geography designed to divide the country into nearly-equal units, they do not always reflect ordinary borders of settlements.» (SINGLE PASS).
   - «This is version 2.3 of the 2021 MSOA Names, published on 13 February 2026.» (SINGLE PASS). 7,264 MSOAs (SINGLE PASS).
   - A working UK case of making a statistical unit recognisable through public correction, with a standing errors channel.
3. Gale et al.'s rule that descriptors present characteristics as things that «have happened to areas rather than the consequences of human agency» is the same distinction the chapter draws between what a place has and what it is, stated as a naming standard for an official classification.
4. Holder & Xiong and Quinn together are the nearest thing to evidence on deficit-framed displays. Both concern social groups, not places.
5. The Data Walks guide's rule that poster text should not over-explain the charts or draw conclusions for participants (reader's summary, SINGLE PASS) sits against the settled guidance on message titles. For a community review step the practitioner advice is to withhold the conclusion.
6. Rambaldi et al.'s custodianship rule (the original output stays with those who generated it, held by an entity they nominate) is a procedural answer to who holds a community-reviewed profile.
7. Brennan-Horley & Gibson 2009, Environment and Planning A 41(11), 2595–2614. https://journals.sagepub.com/doi/10.1068/a41406. ABSTRACT, SINGLE PASS, read for method only: creative practitioners were interviewed and «hard-copy maps were used as anchoring devices around spatially orientated interview questions»; results «were accumulated and analysed in a geographical information system (GIS)». A published interview-mapping method applied to cultural activity; full text not served.
8. Aadland, Farah & Magee 2016, "µ-shapes", JOSIS 12. https://josis.org/index.php/josis/article/download/67/67. ABSTRACT, SINGLE PASS, method only: neighbourhood boundaries «rely on a social definition rather than a well-defined physical or administrative boundary»; a fuzzy-set algorithm outputs a core and a boundary zone rather than a line.

LEFT OUT
- Lynch 1960, Milgram & Jodelet 1976, Kitchin 1994: not reachable from any direct host. I have not supplied sample sizes from memory.
- Coulton et al. 2001 figures; Coulton, Jennings & Chan 2013; Campbell et al. 2009; Lee & Campbell 1997; Kearns & Parkinson 2001; Smith et al. 2010: paywalled, blocked or rate-limited.
- Kennedy & Hill 2018 full text; Kennedy et al. 2016 (conventions); Seeing Data findings pages.
- Birt et al. 2016 procedure; Motulsky 2021; Sieber 2006; Elwood 2006; Peluso 1995; Israel et al. 1998 principles text.
- Honneth 1995 and Fraser & Honneth 2003 at source; Fraser's Tanner Lecture.
- Kearns, Kearns & Lawson 2013; Permentier et al. 2008; Hastings 2004 method detail.
- 2021 OAC names and naming procedure; independent criticism of "left behind"; Kretzmann & McKnight.
- SEP "Recognition": the reader returned only paraphrase and one pseudo-quotation I judged unsafe, so I used nothing from it.
- Lowitja report's final ~14,000 characters and the Tunstall page's final ~3,500 were not read.
- Most of these are publisher blocks rather than absent sources; a session with search and library access should recover them.

RICH REFERENCES
1. Gale, Singleton, Bates & Longley 2016, JOSIS 12, section 7. An explicit, peer-reviewed naming standard for official area labels, with its own contestable outputs in the same table.
2. Tunstall et al. 2014, Urban Studies 51(4). The only causal UK test of a place-reputation penalty, readable in full, with a null result and stated limits.
3. Coulton, Chan & Mikelbank 2010, Urban Institute. 7,498 households drawing their own neighbourhoods, with the exact prompt, the median drawn size against the administrative target area, and a stated consensus rule.

SURPRISED
- The official wording is stronger than I expected. IoD2025 says outright that there is «no definitive threshold above which an area is described as 'deprived'» while licensing "most deprived" and "highly deprived". SIMD publishes a plain "Do not use SIMD for" list.
- The "left behind" report contains its own boxed admission that the term is «controversial and contentious», kept «in the absence of better».
- The sources on returning findings to a community (Data Walks, CBPR principle 7, PGIS ethics) are procedures and principles with no evaluation behind them. The one evaluated member-checking case I could read (Candela) records harm from returning an unflattering portrait.
- The one field experiment on area reputation (Tunstall) found no significant penalty at first-stage selection, against the weight of the theoretical literature.
- I could not find any controlled experiment on own-locality attention or recall. The claim rests on Peck's interviews and one self-rated-helpfulness study.
- The page-314 attribution to Lincoln & Guba circulates in secondary sources without a page number; the one member-checking paper I read in full cites a different year and page.

---

## Agent B

AGENT B — THE TWO COLUMNS. Report of 6 October 2026.

ACCESS (read first)
- WebSearch was NOT available: every call returned "this turn's web search budget is used up". I worked from direct URLs with WebFetch only. Nothing here comes from a search.
- curl from the shell is blocked by the egress policy (403 on CONNECT), so every quotation rests on the WebFetch reader plus a YES/NO presence re-fetch, usually with a false control string.
- The reader invented content twice and I caught it on the presence pass. On the ONS "main points" page it produced a whole paragraph about avoiding "because / due to / driven by"; none of it is on the page. It also garbled one sentence of the Holder & Xiong abstract. Neither is quoted below.
- Pages I could not read:
  - Rate-limited by the fetch proxy (429, "do not fetch again"): Europe PMC search endpoint (two DOI look-ups); link.springer.com/article/10.1186/s41235-020-00241-6 (Ecker, Lewandowsky & Chadha 2020); Europe PMC PMC7447737; doi.org/10.1109/TVCG.2011.160; the Semantic Scholar API.
  - Blocked at target: PMC (reCAPTCHA), HAL (Anubis), ACM DL, Wiley, Taylor & Francis, PNAS, DePaul (all 403); APA PsycNet and ScienceDirect (robots); PubMed, mjskay.com, petra.isenberg.cc (429); IEEE Xplore (empty to the reader); Nature Reviews Psychology (main text paywalled); climatechangecommunication.org (robots 526); lsr.nellco.org (DNS).
- All URLs were fetched on 6 October 2026.
- Labels: STRING-VERIFIED = presence re-fetch said YES. SINGLE PASS = one reading only. ABSTRACT = abstract page only.

====================================================================
B1. "Never repeat the opposing frame" — empirical status
====================================================================
Bottom line: the rule does not survive as an absolute in the corrections literature. Its own author, Lakoff, cites no evidence for it where I could read him. The corrections literature tests belief in a factual claim, not evocation of a frame, so it weakens the rule's usual justification without directly testing Lakoff's mechanism.

1. Lewandowsky et al., The Debunking Handbook 2020 (22 authors; DOI 10.17910/b7.1182). Practitioner consensus document written by the researchers. https://skepticalscience.com/docs/DebunkingHandbook2020.pdf
- "Early evidence was supportive of this idea" — STRING-VERIFIED.
- "exhaustive experimental attempts to induce a backfire effect through familiarity alone have come up empty" — STRING-VERIFIED.
- "repeating a myth while refuting it has been found to be safe in many circumstances" and "can even make the correction more salient and effective" — the second fragment STRING-VERIFIED; the first returned NO on presence with an identical "closest sentence", so treat as near-certain.
- "Debunking a myth makes it more familiar but the debunking usually overpowers the increase in familiarity" — STRING-VERIFIED.
- "Repeat the misinformation, only once, directly prior to the correction" and "One repetition of the myth is beneficial to belief updating" — both STRING-VERIFIED.
- "Although backfire effects are uncommon, we know that repetition makes information appear true" — STRING-VERIFIED. This is the residue of the old rule: no needless repetition.
- "Do not refrain from attempting to debunk or correct misinformation out of fear that doing so will backfire" — STRING-VERIFIED.
- Definition: "A backfire effect is where a correction inadvertently increases belief in, or reliance on, misinformation relative to a pre-correction or no-correction baseline" — STRING-VERIFIED.
- "Backfire effects are not as common as we used to think. We cannot reliably predict the circumstances under which they occur." — second sentence STRING-VERIFIED; the first read identically on three passes but the presence check said NO each time (probably a line-break artefact).
- Control «never repeat the myth under any circumstances»: absent.

2. Swire-Thompson, DeGutis & Lazer 2020, "Searching for the Backfire Effect: Measurement and Design Considerations", J. Applied Research in Memory and Cognition 9(3): 286–299. Peer-reviewed review. Full text via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7462781/fullTextXML
- "We suggest that backfire effects are not a robust empirical phenomenon" — STRING-VERIFIED.
- On familiarity: "The weight of evidence suggests that this rarely, if ever, occurs when the misinformation is paired with a clear and salient correction" — STRING-VERIFIED.
- On worldview: "Failures to find or replicate previously observed backfire effects have been widespread" — STRING-VERIFIED.
- Origin of the familiarity idea: "an unpublished manuscript (Skurnik, Yoon, & Schwarz, 2007)", a flu-vaccine "myth vs. fact" flyer — SINGLE PASS. "There have been failures to directly replicate this study (Cameron et al., 2013)" — SINGLE PASS.
- "a recent meta-analysis of 10 studies found that there was no significant difference in belief updating when comparing whether or not the initial misconception was repeated within the correction" — SINGLE PASS.
- "found that repeating the misconception immediately prior to the correction facilitated belief updating" — STRING-VERIFIED.
- Recommendation: "Avoiding the repetition of the original misconception within the correction appears to be unnecessary and could even hinder corrective efforts" — STRING-VERIFIED. "the misinformation should always be clearly and saliently paired with the corrective element" — STRING-VERIFIED. "needless repetitions of the misconceptions should still be avoided" — SINGLE PASS.

3. Wood & Porter 2019, "The Elusive Backfire Effect", Political Behavior 41: 135–163. ABSTRACT, SINGLE PASS. https://link.springer.com/article/10.1007/s11109-018-9443-y
- "five experiments in which we enrolled more than 10,100 subjects and tested 52 issues of potential backfire"; "we found no corrections capable of triggering backfire".
- The brief's "n = 10,100" is "more than 10,100". This is the worldview backfire effect, not the familiarity one; do not cite it for repetition.

4. Skurnik, Yoon, Park & Schwarz 2005, J. Consumer Research 31(4): 713–724. ABSTRACT. https://academic.oup.com/jcr/article-abstract/31/4/713/1812915
- "Repeatedly identifying a claim as false helped older adults remember it as false in the short term but paradoxically made them more likely to remember it as true after a 3 day delay" — STRING-VERIFIED.
- "In two experiments"; sample sizes not visible. The effect is in older adults, after a delay, on memory for truth status.

5. Not reached: Schwarz, Sanna, Skurnik & Yoon 2007 (ScienceDirect robots-blocked); Ecker et al. 2022 Nature Reviews Psychology 1: 13–29 (only abstract and reference list served; two attempts); Ecker, Lewandowsky & Chadha 2020 (rate-limited). Nothing quoted from them.

6. Lakoff in his own words. Blog post, 22 November 2016. https://george-lakoff.com/2016/11/22/a-minority-president-why-the-polls-failed-and-what-the-majority-can-do/
- "In general, negating a frame just activates the frame and makes it stronger" — STRING-VERIFIED.
- "not to repeat the language of the other side or negate their framing of the issue" — STRING-VERIFIED.
- No study or citation supports the claim on that page; he refers to his own book (SINGLE PASS).
- Later softening: "Use a truth sandwich when reporting on lies" — STRING-VERIFIED, post of 1 December 2023, https://george-lakoff.com/2023/12/01/2024-have-political-journalists-learned-anything-since-2016/. The steps of the sandwich are not on that page.
- The book itself was not reached.

7. Chong & Druckman 2007, "Framing Theory", Annual Review of Political Science 10: 103–126. Peer-reviewed review. Author copy https://faculty.wcas.northwestern.edu/~jnd260/pub/Chong%20Druckman%20Annual%20Review%202007.pdf
- Framing effects "occur when (often small) changes in the presentation of an issue or an event produce (sometimes large) changes of opinion" — SINGLE PASS (the reader's first rendering opened "Framing effects occur when…" and failed presence; this wording is the corrected one).
- "strong predispositions reduce framing effects by increasing one's resistance to disconfirming information" — STRING-VERIFIED.
- On competition: "individual preferences are a function of prior values and the relative strengths of the competing frames" — SINGLE PASS.

8. Chong & Druckman 2007, "Framing Public Opinion in Competitive Democracies", APSR 101(4). Experiments. https://faculty.wcas.northwestern.edu/~jnd260/pub/Chong%20Druckman%20APSR%202007.pdf
- "framing effects depend more heavily on the qualities of frames than on their frequency of dissemination" — STRING-VERIFIED.
- "competition alters but does not eliminate the influence of framing" — STRING-VERIFIED.
- "A total of 869 individuals participated in the urban growth experiment, and 1,277 took part in the rally experiment"; 17 conditions each — SINGLE PASS.
- "In no case did repetition of a weak frame allow it to prevail over a strong opposition frame" — SINGLE PASS.
- A weak frame set against a strong one "produced a contrast effect among more knowledgeable respondents" — SINGLE PASS.
- Role: when both frames are present, strength decides, not repetition count.

9. Othering & Belonging Institute. I could not find the "never repeat" rule in OBI's public pages. The Blueprint for Belonging page lists five 2018 narrative essays; I read three (Godsil, "Mind Sciences and Creating New Narratives"; Robinson, "Changing Our Narrative About Narrative"; Jenkins, "Shifting the Narrative") plus the bridging curriculum page and powell's "Bridging or Breaking?" (Nonprofit Quarterly, 15 February 2021). None mentions Lakoff, myth-busting or a no-repetition rule (SINGLE PASS each). If the house document attributes the rule to OBI, I could not confirm that; the two unread essays and any PDF toolkits remain unchecked.

10. FrameWorks UK, "How to talk about poverty" (JRF, 12 April 2018). Practitioner research with experiments. https://frameworksuk.org/wp-content/uploads/JRFUKPovertyMessageMemo2018Final.pdf
- "more than 20,000 people from across the United Kingdom were included in this research" — STRING-VERIFIED.
- "a nationally representative sample of 12,448 respondents" — SINGLE PASS (presence check said NO but returned the same words inside a longer sentence).
- "leading with prevalence data had no significant effect on issue salience" — STRING-VERIFIED.
- "leading with data is the same as saying nothing at all" — SINGLE PASS.
- No recommendation against myth-busting found, and no frame reported as backfiring.

====================================================================
B2. Asset-based and deficit-based accounts
====================================================================
1. McKnight & Kretzmann, "Mapping Community Capacity" (Center for Urban Affairs and Policy Research, Northwestern, © 1990). This is the paper behind the 1993 book's needs-map and assets-map idea; the 1993 introduction at DePaul returned 403. https://mn.gov/mnddc/parallels2/pdf/90s/90/90-MCC-McKnight_Kretzmann.pdf — all STRING-VERIFIED:
- "most Americans think about lower income urban neighborhoods as problems"
- "They are noted for their deficiencies and needs."
- "residents come to believe that their well-being depends upon being a client"
- "They see themselves as people with special needs to be met by outsiders."
- "every neighborhood has a map of riches, assets, and capacities"
- "The alternative is to develop policies and activities based on the capacities, skills, and assets of low-income people and their neighborhoods"
- SINGLE PASS: "It is important to recognize that this is a map of the same territory as the neighborhood needs map."
- Practitioner framework, not evidence.

2. The Chapter 1 case, identified and checked.
- Source of the wording: Sarikaya, Correll, Bartram, Tory & Fisher 2019, IEEE TVCG 25(1), preprint https://alper.datav.is/assets/publications/dashboards/dashboards-preprint.pdf
- Actual sentence: "Where urban social planners previously used an asset-based model of neighborhood health (social cohesion, resilience), the move to a data-driven representation refocused the conversation on a deficit-based model (crime, code violations)." — both halves STRING-VERIFIED.
- The string «refocused the conversation from an asset-based model» is NOT in the paper; Chapter 1's "from … to" is the chapter's own joining.
- The reader placed this in §5.3.1; Chapter 1's notes say §5.3.2. Check the section number.
- Their reference [45]: "K. O'Connell, Y. Lee, F. Peer, S. Staudaher, A. Godwin, M. Madden, and E. Zegura. Making public safety data accessible in the westside Atlanta data dashboard. In Bloomberg Data for Good, pp. 1–7. New York, Sept. 2016."
- I read the original (arXiv:1609.09756, https://arxiv.org/pdf/1609.09756). It does not contain "refocused the conversation"; that is Sarikaya's gloss. What it says, all STRING-VERIFIED:
  - "Community engagement experts often take an asset-based approach to development"
  - "emphasized over community deficits such as crime and poverty"
  - "The asset-based approach is challenging in settings such as the Data Dashboard project"
  - "Yet the data sets of key relevance to public safety are largely negative"
  - "We invited the community to suggest place-based assets that we could include on the map"
- SINGLE PASS: the portal was named "Public Safety" rather than "Crime" as "a step in an asset-based direction"; "We do not yet know how effective our methods have been in conveying an asset-based approach"; the focus group was still planned, so there was no evaluation.
- Status: a design case report, not a finding about readers. The original authors describe a supply problem (the available data are negative) and three attempted responses. The stronger causal reading belongs to the secondary source.

3. Experiments on deficit framing of the same data.
- Holder & Xiong, "Dispersion vs Disparity: Hiding Variability Can Encourage Stereotyping When Visualizing Social Outcomes" (IEEE TVCG; arXiv:2208.04440, https://arxiv.org/pdf/2208.04440).
  - "bar charts may encourage deficit thinking" — STRING-VERIFIED.
  - "Hiding variability tends to increase stereotyping while emphasizing variability reduces it" — STRING-VERIFIED.
  - Four experiments, US crowdworkers. After exclusions: 329 (152 jitter plot, 177 bar chart); 434; 281 (141 confidence interval, 140 prediction interval); 266 — sum 1,310. SINGLE PASS on the n's.
  - Measure: 0–100 agreement with personal versus external explanations of a group disparity. Experiment 1: "d = 0.322" — STRING-VERIFIED.
  - This is the nearest thing I found to a controlled test of how one dataset's presentation moves readers toward blaming the people shown.
- Quinn 2020, Educational Researcher 49(7): 482–492. ABSTRACT. https://journals.sagepub.com/doi/10.3102/0013189X20932469
  - Three randomised experiments; n not visible. A TV news story about racial "achievement gaps" raised exaggerated stereotypes: "Study 1 effect size = .30 SD; Study 2 effect size = .38 SD" — STRING-VERIFIED.
  - "The video did not affect viewers' explicit competence-related racial stereotyping, the explanations they gave for achievement inequalities" — STRING-VERIFIED.
  - "After 2 weeks, the effect on stereotype exaggeration faded" — STRING-VERIFIED.
- I found no experiment comparing an asset-framed and a deficit-framed presentation of the same AREA data. Without search that is "not found", not "does not exist".

4. Urban Institute, Do No Harm Guide (Schwabish & Feng 2021). https://www.urban.org/sites/default/files/publication/104296/do-no-harm-guide.pdf
- The words "asset" and "strength" do not appear in the guide (reader report across the whole text). "Deficit" appears only in the Urban case study near p. 31.
- "deficit-based perspective" (attributed to Pieta Blakely 2019) — STRING-VERIFIED.
- "we felt we did not go into such historical factors in sufficient detail to mitigate the possibility of a deficit-based interpretation" — STRING-VERIFIED.
- SINGLE PASS: "Some counter that this deficit framing perspective is not always applicable depending on how much context regarding the issue being visualized is offered."
- Missing groups (section 08, pp. 16–21), all STRING-VERIFIED:
  - "It is also important to acknowledge who is and is not included in our data and charts"
  - "Groups whose data are and are not collected or shown often reflects who society deems as most important or valuable"
  - "Spots that we've left blank reveal our hidden social biases" (the guide quoting Mimi Ọnụọha)
  - "it may be worth listing in the notes section all racial and ethnic groups included in the original dataset"
  - "Just by calling out the absence and by doing it explicitly, it gives a prompt to the reader" (the guide quoting Lauren Klein)
  - "Rather than excluding those options from the tool" … "ProPublica displayed a message over the chart explaining how the lack of sufficient data" … "would result in estimates that were too imprecise to be reliable"
- "Research and analysis should be done with communities, not on behalf of them" (section 04) — STRING-VERIFIED.

5. Glasgow Centre for Population Health, Briefing Paper 9, "Asset based approaches for health improvement: redressing the balance" (October 2011). https://www.gcph.co.uk/assets/0000/2627/GCPH_Briefing_Paper_CS9web.pdf
- "Asset based approaches are not a replacement for investing in service improvement or attempting to address the structural causes of health inequalities" — STRING-VERIFIED.
- "evidence of the effectiveness of these approaches at present largely comes from case studies and small scale exploratory research" — STRING-VERIFIED.
- SINGLE PASS: "Assessing assets alongside needs will give a better understanding".

====================================================================
B3. Precision as a cue; does honest uncertainty cost trust?
====================================================================
Earlier chapters hold Jerez-Fernandez (press summary), Zhang & Schwarz (reconstructed abstract), Xie & Kronrod (paraphrase), Joslyn & LeClerc (ERIC abstract), van der Bles 2020 and Hullman 2020. What is new or upgraded:

1. Zhang & Schwarz 2012, JCR 39(2): 248–259 — now from the publisher. ABSTRACT. https://academic.oup.com/jcr/article/39/2/248/1797784
- "Consumers attend to the granularity chosen by a communicator and draw pragmatic inferences that influence judgment and choice" — STRING-VERIFIED.
- SINGLE PASS: "They consider estimates expressed in finer granularity more precise and have more confidence in their accuracy (studies 1–4). This effect is eliminated when consumers doubt that the communicator complies with Gricean norms of cooperative conversational conduct (studies 2–3)." Sample sizes not visible.

2. Jerez-Fernandez, Angulo & Oppenheimer 2014, Psychological Science 25(2): 633–635 — bibliographic details confirmed on SAGE; text restricted. Nothing new to quote; n still unverified. Xie & Kronrod: 403. Løhre et al. 2019: 403. Joslyn & LeClerc: PsycNet robots-blocked, PubMed 429.

3. Thomas, Simon & Kadiyali, Marketing Science 29(1): 175–190. ABSTRACT, SINGLE PASS. https://pubsonline.informs.org/doi/10.1287/mksc.1090.0512
- "Results from five studies suggest that buyers underestimate the magnitudes of precise prices"; "participants in this experiment incorrectly judged $395,425 to be smaller than $395,000".
- This is precision affecting perceived magnitude, not confidence. It is a different effect from Jerez-Fernandez and should not be merged with it.

4. Direction of the trust effect.
- van der Bles et al. 2020, PNAS 117(14). Full text via https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7149229/fullTextXML
  - "total n = 5,780" (five experiments, UK, one on the BBC News site) — STRING-VERIFIED.
  - "a common assumption is that communicating uncertainty will reduce public trust" — STRING-VERIFIED.
  - SINGLE PASS: "we observed only a small decrease in trust in numbers and trustworthiness of the source, and mostly for verbal uncertainty communication."
  - SINGLE PASS, one experiment: verbal uncertainty versus control on trust in numbers "M = 3.51 vs. 4.52 … d = 0.75"; numeric range versus control "M = 4.31 vs. 4.52 … d = 0.17", reported as not significant.
  - Control «uncertainty communicated as a numeric range increased trust substantially»: absent.
- Gustafson & Rice 2020, Public Understanding of Science 29(6): 614–633. Review, ABSTRACT. https://journals.sagepub.com/doi/10.1177/0963662520942122
  - "k = 48" experiments — STRING-VERIFIED.
  - "most findings of negative effects (such as reduced credibility and beliefs) are from experiments that operationalized uncertainty as disagreement or conflict in science" — STRING-VERIFIED.
  - "consensus uncertainty was never found to have positive effects" — STRING-VERIFIED.
  - Quantified error ranges and probabilities "has had only positive or null effects, not negative effects" — STRING-VERIFIED.
- Dries, McDowell, Rebitschek & Leuker 2024, Public Understanding of Science. ABSTRACT, SINGLE PASS. https://journals.sagepub.com/doi/full/10.1177/09636625241228449
  - "(N = 800, convenience sample)"; "communicating uncertainty buffers against a loss of trust when evidence changes"; "explaining uncertainty does not appear to harm trust".
- Hullman, "Why Authors Don't Visualize Uncertainty" (arXiv:1908.01697) — the producer side.
  - "surveying 90 authors … and interviewing thirteen influential visualization designers" — STRING-VERIFIED.
  - "a clear contradiction arises between authors' acknowledgment of the value of depicting uncertainty and the norm of omitting direct depiction of uncertainty" — STRING-VERIFIED.
  - SINGLE PASS reasons list: "not wanting to confuse or overwhelm viewers (53/85; 62%), not having access to uncertainty information (40/85; 47%), not knowing how to calculate uncertainty (22/85; 26%), and not wanting to make data seem questionable (15/85; 17%)."
- Padilla, Kay & Hullman's handbook chapter mentions trust once, about icon arrays (SINGLE PASS); it does not settle the question.

Answer to the brief's question, on what I could read: numeric ranges cost little or no stated trust; vague verbal hedges cost more; disagreement between experts is the form that reliably damages credibility; stated uncertainty protects trust when a figure is later revised. The belief that intervals make data "seem questionable" is held by a minority of producers (17% in one survey). I found no experiment on trust in a chart with error bars versus the same chart without them.

====================================================================
B4. Dual-axis and dual-scale charts
====================================================================
1. Isenberg, Bezerianos, Dragicevic & Fekete 2011: not reachable this session (HAL and author site blocked). Chapter 3's notes already hold it at source: 15 participants, and it concerns one series at two resolutions, not two measures on two axes. A secondary source confirms the n and one quotation: Muth, "Why not to use two axes, and what to use instead" (Datawrapper, 8 May 2018, updated), https://www.datawrapper.de/blog/dualaxis — "showed 15 people four different charts" (SINGLE PASS); quoting the paper, "We found across the board that the superimposed chart performed poorly both in terms of accuracy and time" (STRING-VERIFIED as present in the blog, i.e. secondary). The blog treats the study as evidence on dual-axis charts; Chapter 3's caveat stands.

2. Few, "Dual-Scaled Axes in Graphs: Are They Ever the Best Solution?" (Visual Business Intelligence Newsletter, March 2008). Practitioner argument, no data. https://www.perceptualedge.com/articles/visual_business_intelligence/dual-scaled_axes.pdf — all STRING-VERIFIED:
- "I certainly cannot conclude, once and for all, that graphs with dual-scaled axes are never useful"
- "I cannot think of a situation that warrants them in light of other, better solutions"
- "we are still encouraging people to compare their magnitudes"
- "Magnitude comparisons between values with different units of measure and scales are not appropriate"
- SINGLE PASS: "When lines are associated with different quantitative scales, however, their intersection means nothing."

3. Analysis Function, "Data visualisation: charts", section 11 Line charts, sub-heading "Dual axis line charts". Official standard. https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ — all STRING-VERIFIED:
- "Dual axis line charts can be used to present two variables with differing scales"
- "In general, we do not recommend using dual axis charts because"
- "they can be easily misinterpreted"
- "the way we display lines in relation to each other can manipulate the data story, even if it is not intentional"
- "It is best practice to separate the datasets and present them with their own y-axis"
- It is a "do not recommend", not a prohibition; the control «must never be used» is absent. Page metadata date 19 May 2022 (SINGLE PASS).

4. ONS Digital blog, Frank Donnarumma, 3 July 2019. https://digitalblog.ons.gov.uk/2019/07/03/dueling-with-axis-the-problems-with-dual-axis-charts/ — all STRING-VERIFIED:
- "By putting several lines or bars on the same canvas we are inviting the user to make comparisons"
- "we've compromised the user's ability to interpret relative differences and left ourselves open to misinterpretation"
- "Using annotation and/or splitting the chart up are easy things to do to help users understand the data faster"
- No user testing is cited.

5. Lo et al. 2022, "Misinformed by Visualization" (EuroVis; arXiv:2204.09548).
- "In total, 6,500 images were examined, 1,979 of them were candidate images, 1,143 were tagged with at least one issue, and 74 tags were discovered" — the 1,143 and 74 STRING-VERIFIED.
- Dual axis is the 4th most common issue in a corpus of charts people reported as misleading (SINGLE PASS). That is prevalence in complaints, not a measured effect on readers.

6. Xiong, Shapiro, Hullman & Franconeri, "Illusion of Causality in Visualized Data" (arXiv:1908.00215). ABSTRACT, SINGLE PASS. Three crowdsourced experiments: "causality ratings were highest for text descriptions and bar graphs, but weaker for scatter plots". Not about dual axes.

I found no experiment on readers inferring correlation or causation from a two-measure dual-axis chart. Chapter 3 found the same. The case against rests on argument and an official standard.

====================================================================
B5. Rendering absence
====================================================================
1. Ge, Cui & Kay, CALVI (CHI 2023). https://mucollective.northwestern.edu/files/2023-CALVI.pdf
- "trying out the provisional test on 497 participants" — STRING-VERIFIED. Prolific, US, fluent English (SINGLE PASS). Final bank of 45 trick items; each participant saw 15 trick and 15 normal items.
- "Participants' correctness (proportion of correct answers) for the 15 trick items ranged from 0 to 0.93 (M = 0.39, SD = 0.16)." — STRING-VERIFIED.
- "Participants' correctness for the 15 normal items ranged from 0.27 to 1 (M = 0.80, SD = 0.13)." — STRING-VERIFIED.
- So 0.39 is the mean proportion correct across participants on trick items, against 0.80 on normal items. Version 1's "0.39 on trick items" is right. No chance level is stated.
- Hardest misleaders: "Overplotting, Missing Data, and Missing Normalization" — fragment STRING-VERIFIED; the surrounding sentence came back garbled, so quote only the three names.
- Definitions (Table 1, SINGLE PASS): Missing Data — "A visual representation implies data exist but the data is actually missing." Missing Normalization — "Displaying unnormalized data in absolute quantity when normalized data in relative quantity is of interest."
- Caution: CALVI's "Missing Data" is a mark drawn where no data exist (for example a line across a gap). It does not test whether readers notice an absent category or series. I found no study of that.

2. Analysis Function, "Using symbols and shorthand" (published 11 January 2022). https://analysisfunction.civilservice.gov.uk/policy-store/symbols-in-tables-definitions-and-help/
- Three passes gave the same meanings but three different formattings (capitalised; "x = …"; "[x] = …"). Take the meanings as reliable and check the exact typography by eye before printing.
  - [b] break in time series
  - [c] confidential
  - [e] estimated
  - [er] earliest revision
  - [f] forecast
  - [low] a low figure but not a real zero
  - [high] and [k] are mentioned in running text
  - [p] provisional
  - [r] revised
  - [u] low reliability
  - [w] none recorded in survey
  - [x] not available
  - [z] not applicable
  - ns, s, ss, sss for significance levels
- "Use this shorthand when data is unavailable for reasons other than those described in this list" (for [x]) — STRING-VERIFIED.
- "Whenever a table contains shorthand, you should mention it and explain what the shorthand means" — STRING-VERIFIED.
- "A zero or '0' should only be used when a data point is a true zero" — STRING-VERIFIED.
- SINGLE PASS: for [z], "For example, in tables of employment where people under 16 cannot legally be employed"; for [c], "if you would be able to identify details about a single respondent from the data".
- No sentence about blank cells was found on this page, and the tables guidance only points here. I found no official guidance on a whole missing series or panel.

3. Practice: the ProPublica message-over-the-chart and the notes-listing recommendation in B2 item 4.

====================================================================
B6. Does the better-crafted panel get believed?
====================================================================
In the project already: Pandey 2014 (n = 720, with the reversal), Tal & Wansink (abstract), Dragicevic & Jansen (N = 623), Lin & Thornton, Kennedy et al. Re-checked today:
- Dragicevic & Jansen, authors' page https://www.aviz.fr/blinded: "(N = 623)" and "no more persuasive – and sometimes less persuasive – than text alone" — both STRING-VERIFIED.
- Tal & Wansink: the SAGE page shows no retraction notice (SINGLE PASS); the study n's are still not visible.
- Pandey: the SSRN abstract carries no findings; the chapter's figures must keep coming from the author PDF already logged.

New: Wood, Isenberg, Isenberg, Dykes, Boukhelifa & Slingsby 2012, "Sketchy rendering for information visualization", IEEE TVCG. Peer-reviewed; two studies. https://openaccess.city.ac.uk/id/eprint/1274/1/wood_sketchy_2012.pdf
- "Results suggest relative area judgment is compromised by sketchy rendering and that its influence is dependent on the shape being rendered" — STRING-VERIFIED.
- "where a visualization is clearly sketchy, engagement may be increased and that attitudes to participating in visualization annotation are more positive" — STRING-VERIFIED.
- SINGLE PASS: perception study, "137 unpaid volunteers … 84 completed the tasks in full, with 42 participating in each shape condition"; engagement study, "52 unpaid participants (40 male, 12 female)".
- SINGLE PASS: "exploiting expectations that a hand-drawn design has not yet been finalised and is open to redesign".
- It did not measure perceived accuracy, trust or authority.
- Bearing: the one experiment I reached on deliberately rougher rendering found it costs accuracy of reading and raises willingness to engage and critique. It says nothing on belief.

I found no experiment where two panels of differing craft sit side by side and belief in each is measured. "The sketchier column loses" is untested in what I reached.

====================================================================
B7. Juxtaposition and superposition
====================================================================
1. Gleicher, Albers, Walker, Jusufi, Hansen & Roberts 2011, Information Visualization 10(4): 289–309. Taxonomy and survey; ABSTRACT, SINGLE PASS. https://journals.sagepub.com/doi/10.1177/1473871611416549
- "we propose a general taxonomy of visual designs for comparison that groups designs into three basic categories, which can be combined"; "all designs are assembled from the building blocks of juxtaposition, superposition and explicit encodings".
- Full text not reached, so no quotation on when each works.

2. L'Yi, Jo & Seo, "Comparative Layouts Revisited" (IEEE VIS 2020; arXiv:2009.00192). Systematic review. https://arxiv.org/pdf/2009.00192
- "127 research papers, including 15 papers with quantitative user studies" — STRING-VERIFIED.
- "chart-wise juxtaposition has almost never outperformed any other layouts in terms of accuracy, completion time, and precision" (for local tasks; the source italicises "almost never") — STRING-VERIFIED.
- Guideline heading "Avoid Chart-wise Juxtaposition for Local Comparison" (§5.2.1) — STRING-VERIFIED.
- On juxtaposition, quoting Tominski et al.: "eyes have to move from one part to the other part" — STRING-VERIFIED.
- The review does not discuss comparing visualisations with different units or scales (SINGLE PASS, reader's negative).

3. Ondov, Jardine, Elmqvist & Franconeri 2019, "Face to Face: Evaluating Visual Comparison", IEEE TVCG 25(1). https://visualthinking.psych.northwestern.edu/publications/OndovFacetoFace2018.pdf
- "Confirming prior intuition, we observe high levels of performance for overlaid versus standard small multiples" — STRING-VERIFIED.
- "we also find performance improvements for both mirror symmetric small multiples and animated transitions" — STRING-VERIFIED.
- "mirrored bar charts outperformed all other arrangements for detection of correlated data" — SINGLE PASS.
- Four Mechanical Turk experiments. "We recruited 50 new participants for each experiment"; exclusions "3, 4, 2, and 2" — SINGLE PASS. My arithmetic: 189 retained of 200.
- Layouts: stacked, adjacent, mirrored, overlaid, animated. Tasks: largest change between two series; which pair is most correlated. Both series share a scale.

4. Javed & Elmqvist 2012: the URL I tried returned 404; not reached. Chapter 3 holds Javed, McDonnel & Elmqvist 2010.

Bearing on "side by side, never on one scale": for like-with-like data on one scale, the experiments favour overlay for precise local comparison, and plain side-by-side is the weakest layout for that task. No study I reached tests unlike units. Separation for two unlike measures is therefore supported by Few's argument and the Analysis Function standard, not by comparison experiments, and it has a measured cost: comparing across panels is slower and relies on memory.

====================================================================
B8. The bridging sentence
====================================================================
Very little exists.
- GSS, "Communicating quality, uncertainty and change" (17 December 2018): two passes found no guidance on relating two measures with different units or on avoiding an implied ratio. https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/
- ONS service manual, "Writing main points and analysis": "Include up to six bullet points, with one trend or point per bullet, to ensure they are concise." — STRING-VERIFIED. "Accompanying text should add context and detail to your charts; it should not repeat the trends shown in them." — STRING-VERIFIED. No sentence about causal wording exists on this page. https://service-manual.ons.gov.uk/content/writing-for-users/writing-main-points-and-analysis
- The nearest thing to a rule is Few's sentence in B4 on magnitude comparisons between different units.
- I found no guidance or evidence on "and also" constructions.

====================================================================
PRODUCTS THAT PUT ASSETS BESIDE NEEDS (method only)
====================================================================
- OCSI Community Needs Index (for Local Trust; blog by Kimberley Gregory, 21 October 2019). https://ocsi.uk/2019/10/21/community-needs-index-measuring-social-and-cultural-factors/
  - "The index covers 19 indicators, across three domains" — SINGLE PASS on the sentence; the 19 confirmed.
  - Civic Assets: "Measures the presence of key community, civic, educational and cultural assets in close proximity of the area" — STRING-VERIFIED.
  - Active and Engaged Community: "Measures the levels of third sector civic and community activity and barriers to participation and engagement" — STRING-VERIFIED.
  - "In each case, a higher score indicates higher levels of community need." — SINGLE PASS.
  - "The CNI has been created to offer a different perspective to more economically-based measures of local need." — SINGLE PASS.
  - Ward level in 2019. The 2023 version uses 2021 LSOAs and the two versions "are not directly comparable" (SINGLE PASS, https://ocsi.uk/community-needs-index/). The thresholds used with the IMD to define "left behind" areas are not on either page.
- Westside Atlanta Data Dashboard (B2 item 2): a public-safety map with a community-suggested asset layer (schools, places of worship, parks, transit) over crime and code-violation data; no evaluation reported.
- Thriving Places Index (already in the project): pages read today give standardised scores showing "how a place compares to other local authorities" and headline elements Local Conditions, Sustainability, Equality. No use of "asset-based" found on the About or FAQ pages (SINGLE PASS).
- California Healthy Places Index: the home page describes indicators "positively associated with life expectancy at birth" (SINGLE PASS). The FAQ did not state score direction or a framing rationale. The 2024 Do No Harm volume has an essay titled "Uplifting Communities with the California Healthy Places Index", but the reader's text stopped before it; title only.
- I found no official statistics product with an assets panel beside a needs panel as two co-equal displays. Fingertips and "Our Place" tools were not checked.

====================================================================
UNASKED THREADS
====================================================================
1. Peck, Ayuso & El-Etr 2019, "Data is Personal" (CHI; arXiv:1901.01920). "In 42 semi-structured interviews in rural Pennsylvania (USA)" — STRING-VERIFIED. "People often determined the quality of a graph containing geographical information based on how easy or difficult it was to find their home state." — STRING-VERIFIED. Ten charts ranked "from most useful to least useful" (SINGLE PASS). Already in the project, but this sentence is direct evidence for the chapter title: readers judged a map by whether they could find themselves on it.
2. Lakoff's truth sandwich and the Debunking Handbook's "repeat once, directly prior to the correction" converge on the same shape from opposite starting points.
3. The Community Needs Index measures assets and reports them as need (higher = worse). It is a worked example of the counted column absorbing the other.
4. The 2024 Do No Harm volume (Schwabish, Feng & Jenkins, 16 February 2024; 12 essays) includes Koyejo, "Elite Omitted Variable Bias: Missing Datasets and the Political Economy of Data Collection" and Rembert & Blatchly, "Rural Definitions and Their Consequences". Titles only; the second bears on the spatial-unit agent's items. https://www.urban.org/sites/default/files/2024-04/Do_No_Harm_Guide_Crafting_Equitable_Data_Narratives.pdf
5. The FrameWorks finding that leading with prevalence data did nothing (B1 item 10) is independent of the repetition question and bears on any panel that opens with a count.

====================================================================
LEFT OUT, AND WHY
====================================================================
- Not reached, nothing quoted: Schwarz et al. 2007; Ecker et al. 2022 main text; Ecker, Lewandowsky & Chadha 2020; Lakoff's book; Kretzmann & McKnight 1993 itself; Jerez-Fernandez full text; Xie & Kronrod; Løhre et al. 2019; Joslyn & LeClerc; Hullman et al. "In Pursuit of Error"; Isenberg et al. at source; Javed & Elmqvist 2012; Gleicher 2011 full text; Tal & Wansink full text.
- Everything that needed a search: asset- versus deficit-framed area data experiments; perception of omitted categories; aesthetics and credibility beyond what the project holds; dual-axis misreading experiments; Fingertips, "Our Place" and other asset dashboards; the phrase search for Welsh's precision work.
- The Co-op Community Wellbeing Index: its domain now serves unrelated gambling content. Not used.
- Two OBI narrative essays ("Building a Strategic Narrative for All of California"; "California Dog Whistling") and any OBI PDF toolkits were not read.

====================================================================
RICH REFERENCES
====================================================================
1. Swire-Thompson, DeGutis & Lazer 2020 — the single best source for B1; open full text through the Europe PMC XML endpoint, with a practitioner recommendations section.
2. O'Connell et al. 2016 (arXiv:1609.09756), section 5 "Asset-based approaches to data" — a first-hand account of a team trying to put assets on a deficit dataset and saying they do not know whether it worked.
3. L'Yi, Jo & Seo 2020 (arXiv:2009.00192) — 127 papers, 15 user studies, seven guidelines; the evidence base for any side-by-side claim.

====================================================================
SURPRISED
====================================================================
- The Chapter 1 case is weaker and more interesting than its secondary telling. The original authors never say the dashboard "refocused the conversation"; they say the relevant data "are largely negative" and describe what they tried.
- Lakoff gives no evidence for his own rule where I could read him, and now recommends a format that states the falsehood.
- The comparison literature runs against side-by-side for precise reading. The case for separating unlike measures is an argument about meaning, not a perceptual finding.
- Quantified uncertainty has "only positive or null effects" on credibility in a 48-experiment review, while the producers' fear of looking "questionable" is a minority view (17%).
- CALVI's "missing data" is not about absence going unnoticed; it is about a mark drawn where nothing was measured.
- The Do No Harm Guide never uses the word "asset".
- A named community-wellbeing index site has been taken over by a gambling page — reference rot in the chapter's own subject area.

---

## Agent C

AGENT C REPORT — IDENTITY, CONDITIONS AND SCALE
All fetches made 6 October 2026.

TOOLS AND ACCESS. WebSearch was unavailable (the shared search budget was already used up), so everything below came from direct URLs through WebFetch. curl was blocked by the proxy and web.archive.org was blocked. Several API or publisher pages were refused with HTTP 429 and not retried: PubMed DOI look-ups (Diehl 2010, Albo 2016, Javed 2010, Johansson & Forsell 2016), Europe PMC (two pages), three Crossref records, two Springer pages, Semantic Scholar and OpenAlex. IEEE Xplore, IEEE CSDL, JSTOR, mapmaker.geods.ac.uk and the JRC composite-indicators tool returned empty JavaScript shells.

Labels: STRING-VERIFIED = confirmed by a second YES/NO presence fetch (with false control strings) or returned identically in two independent passes. SINGLE PASS = one pass only. ABSTRACT = only the abstract was reachable.

One fabrication was caught: the fetch reader invented "page 147/151/154" definitions from the ESS Handbook for Quality and Metadata Reports, whose extracted text does not contain that section. Those were discarded and replaced from SIMS and Regulation 223/2009 (see C4).

----------------------------------------------------------------
C1. LEVELS OF MEASUREMENT AND THE CRITIQUE

Stevens 1946 (Science 103: 677–680) — NOT REACHED at source. Six hosts tried (okstate redirect, marces 404, mpopa 404, cmru 404, science.org 403, TU/e robots failure). I quote nothing from Stevens directly. The exact "permissible statistics" sentence for nominal scales still has to be taken from the paper itself.

Velleman & Wilkinson 1993, "Nominal, ordinal, interval, and ratio typologies are misleading", The American Statistician 47(1): 65–72 (bibliographic details as printed on the copy, SINGLE PASS). Author copy: https://www.cs.uic.edu/~wilkinson/Publications/stevens.pdf. Peer-reviewed methodological critique.

Their rendering of Stevens's rule (V&W paraphrasing Stevens, not Stevens's words):
- "By this reasoning, analyses on nominal data, for example, should be limited to summary statistics such as the number of cases, the mode, and contingency correlation, which require only that the identity of the values be preserved." STRING-VERIFIED (core string).
- Preceding sentence: "A scale that preserves meaning under some class of transformations should, according to Stevens, be restricted to statistics whose meaning would not change were any of those transformations applied to the data." SINGLE PASS.
- On nominal scales: "They do not even require the assignment of numerical values, but only of unique identifiers (numerals, letters, colors, etc.)." STRING-VERIFIED.
- "Thus it is permissible to perform almost any operation on the values as long as we do not combine or confuse identities." SINGLE PASS (the reader corrected my word order).

Their central objections:
- "the use of Stevens's categories in selecting or recommending statistical analysis methods is inappropriate and can often be wrong" STRING-VERIFIED.
- "They do not describe the attributes of real data that are essential to good statistical analysis" STRING-VERIFIED.
- "Scale type, as defined by Stevens, is not an attribute of the data, but rather depends upon the questions we intend to ask of the data and upon any additional information we may have." STRING-VERIFIED (two fragments). Section heading: "Stevens's categories do not describe fixed attributes of data" (SINGLE PASS).
- "It is relatively easy to construct situations in which the scale type of data depends on its interpretation or on what additional information is available." STRING-VERIFIED (two passes).
- "Worse, they assert that the scale type is evident from the data independent of the questions asked of the data" STRING-VERIFIED.
- "Meaning in statistical analysis derives not only from the data but also from the questions being investigated, the patterns discovered in the course of the analysis, and the additional data that may be available." SINGLE PASS.
- Lord's statistician, quoted by V&W: "the numbers don't know where they came from" STRING-VERIFIED.

Examples (SINGLE PASS on detail):
- A raffle ticket numbered 126 at an ASA reception was read as nominal (did I win?), as ratio ("It doesn't look like there are 126 people here") and as ordinal (the holder of ticket 56 "had arrived too soon").
- Number of engine cylinders can be nominal, ordinal, interval or ratio depending on the question.

What they concede:
- "The concept of scale type is an important one, and Stevens's terminology is often suitable." STRING-VERIFIED.
- "It would be wrong to conclude that there is no value to data types." STRING-VERIFIED.
- "Considering whether scale types are plausible subsequent to the analysis can help ferret out nonsense" STRING-VERIFIED.
- "Statistics software that facilitates any analysis on any data permits irresponsible analyses" and "But software that imposes arbitrary restrictions is likely to generate equally misleading conclusions" both STRING-VERIFIED.

Also relevant to C8: "Scales can be multidimensional" (STRING-VERIFIED), followed by "Here is a partially ordered binary scale, for example" (SINGLE PASS).

The other side (strongest statements I could reach):
- Hand & Keynes (1993), as quoted by V&W: "[The] argument that 'there is no reason to believe that the data come to us measured in the best way' is false if the numbers have been assigned in a representational way so as to preserve the empirical relational structure." SINGLE PASS; source quoting someone else.
- Hand 1996, "Statistics and the Theory of Measurement", JRSS A 159(3), from p. 445 (Crossref record, https://api.crossref.org/works/10.2307/2983326). Text and abstract NOT REACHED (JSTOR shell, Wiley robots-blocked).
- Wikipedia "Level of measurement" attributes to Hand (2017): "the essential soundness of his hierarchy has been established for representational measurement by mathematicians". Tertiary, SINGLE PASS; do not print without checking Hand.
- Chrisman 1998, Cartography and Geographic Information Systems 25(4): 231–242 (Crossref). Text NOT REACHED. Wikipedia lists his ten levels (nominal, gradation of membership, ordinal, interval, log-interval, extensive ratio, cyclical ratio, derived ratio, counts, absolute). Tertiary, SINGLE PASS.

On the chapter's question, what the sources say: V&W hold that scale type is fixed by the question, not the data. The representational side (Hand & Keynes via V&W) holds the restriction is binding only where numbers were assigned to preserve an empirical relational structure. On either reading, "identity is nominal, so it cannot be ranked" holds for a stated use of the profile. Neither side says categories can never acquire an order under a different question.

----------------------------------------------------------------
C2. DISPLAY FORMS FOR A NOMINAL, MULTI-ATTRIBUTE PROFILE

Radar and radial forms

Albo, Lanir, Bak & Rafaeli 2016, "Off the Radar: Comparative Evaluation of Radial Visualization Solutions for Composite Indicators", IEEE TVCG 22(1): 569–578. CORRECTION: the fourth author is Sheizaf Rafaeli, not Berkovich. https://cris.haifa.ac.il/en/publications/off-the-radar-comparative-evaluation-of-radial-visualization-solu. ABSTRACT; peer-reviewed controlled experiment.
- Compared radar charts, flower charts (as in the OECD Better Life Index) and circle charts, shown as small multiples, under a formal task taxonomy; measured performance and preference.
- "Results indicate that the Radar chart was the least effective and least liked, while performance of the two other options were mixed and dependent on the task." First clause STRING-VERIFIED; remainder SINGLE PASS.
- "Results also showed strong preference of participants toward the Flower chart." SINGLE PASS.
- n is not in the abstract; NOT VERIFIED.

Feldman 2013, "Filled Radar Charts Should not be Used to Compare Social Indicators", Social Indicators Research 111(3): 709–712. https://link.springer.com/article/10.1007/s11205-012-0028-6. ABSTRACT; a geometric argument, not an experiment, as far as the abstract shows.
- "Filled radar charts are not appropriate for such comparisons because the size of the area within the polygon is not invariant to the placement of the measures on the axes." STRING-VERIFIED.
- "altering the placement of the measures on the axes can result in reversing the order of observations or reversing the order of the same observation over time" STRING-VERIFIED.

Waldner, Diehl, Gracanin, Splechtna, Delrieux & Matkovic, "A Comparison of Radial and Linear Charts for Visualizing Daily Patterns", IEEE TVCG 26(1): 1033–1042. Full text: https://www.cg.tuwien.ac.at/research/publications/2019/waldner-2019-rld/waldner-2019-rld-paper.pdf. Peer-reviewed crowdsourced experiment.
- "In a crowd-sourced experiment with 92 non-expert users" STRING-VERIFIED.
- Four charts (12-hour and 24-hour, radial and linear bars); four low-level tasks and one interpretation task; accuracy, time and ratings.
- "the most elementary 24-hours linear bar chart is most accurate and efficient and is also preferred by the users" STRING-VERIFIED.
- "This provides strong evidence for the use of linear layouts" STRING-VERIFIED.
- "visualizations for the masses should rely on linear bar charts instead of radial rose charts" STRING-VERIFIED.
- Limit: it tested one time series of hourly counts, not multi-attribute profiles or two-profile comparison (reader's reading of the full text).

Diehl, Beck & Burch 2010, IEEE TVCG 16(6): 935–942 — primary NOT REACHED (five routes failed). Only Waldner et al.'s summary: "memorizing specified locations is also more difficult for radial visualizations than Cartesian visualizations, but circle sectors are easier to memorize than rings." SINGLE PASS, secondary. n and tasks NOT VERIFIED.

Burch & Weiskopf 2014, "On the Benefits and Drawbacks of Radial Diagrams", in Handbook of Human Centric Visualization. https://link.springer.com/chapter/10.1007/978-1-4614-7485-2_17. ABSTRACT, SINGLE PASS: "One reason for this popularity is the aesthetic look of those diagrams. However, there are advantages for corresponding Cartesian (rectangular) representations as well, including possible perceptual benefits, more efficient use of rectangular screen space, or ease of implementation due to simpler graphical primitives."

Other secondary summaries in Waldner et al. (all SINGLE PASS):
- Goldberg & Helfman 2011: "reading values is clearly more difficult in radial charts".
- Fuchs et al. 2013 (CHI): "linear glyphs were most accurate and efficient for value comparison, but the radial glyphs were more accurate and efficient, respectively, for time comparisons".
- Adnan et al. 2016: "For all tasks, the linear charts outperformed the radial charts."

Glyphs

Borgo et al. 2013, "Glyph-based Visualization: Foundations, Design Guidelines, Techniques and Applications", Eurographics STAR, pp. 39–63. https://www.cg.tuwien.ac.at/research/publications/2013/borgo-2013-gly/borgo-2013-gly-report.pdf. Review; guidelines DG1–DG14 synthesised from Ward, Ropinski, Lie, Maguire and others.
- "[DG4] Perceptually uniform glyph properties. When mapping a data variable to a glyph property, equal distances in data space should be perceived equally as well." STRING-VERIFIED.
- DG6: "important variables should be enhanced in the visualization, for instance, by using a redundant mapping" STRING-VERIFIED.
- DG8: "According to Gestalt laws [War04], simple and symmetric shapes facilitate the perception of visual patterns." STRING-VERIFIED.
- DG9: "it should be possible to perceive each visual cue independently" STRING-VERIFIED.
- "[DG10] Intuitive mapping based on semantics. Semantics of the data should be incorporated in the glyph mapping" SINGLE PASS.
- DG11: "Such aggregations should be avoided, since they may be erroneously identified as features" STRING-VERIFIED.
- On star glyphs: "Peng et al. [PWR04], for instance, automatically reorder the data-to-property mapping for generating more symmetric and simple star glyphs." SINGLE PASS. The report itself records that axis order changes the shape read.

Chernoff 1973 and Morris, Ebert & Rheingans 2000 — NOT REACHED (IBM copy gone, SPIE bot wall; the Lee, Reilly & Butavicius 2003 copy also failed). Nothing quotable on unequal perception of face features.

Small multiples

Tufte, Envisioning Information (1990), p. 67, as quoted by Wikipedia "Small multiple" (https://en.wikipedia.org/wiki/Small_multiple). STRING-VERIFIED on the Wikipedia page only; not checked against the book:
"At the heart of quantitative reasoning is a single question: Compared to what? Small multiple designs, multivariate and data bountiful, answer directly by visually enforcing comparisons of changes, of the differences among objects, of the scope of alternatives. For a wide range of problems in data presentation, small multiples are the best design solution."

Javed, McDonnel & Elmqvist 2010, "Graphical Perception of Multiple Time Series", IEEE TVCG 16(6): 927–934. https://pure.au.dk/portal/en/publications/graphical-perception-of-multiple-time-series. ABSTRACT; peer-reviewed experiment; comparison, slope and discrimination tasks.
- "techniques that create separate charts for each time series - such as small multiples and horizon graphs - are generally more efficient for comparisons across time series with a large visual span" STRING-VERIFIED.
- "shared-space techniques - like standard line graphs - are typically more efficient for comparisons over smaller visual spans where the impact of overlap and clutter is reduced" STRING-VERIFIED.
- n NOT VERIFIED (not in the abstract; three author-copy URLs failed).

Parallel coordinates

Johansson & Forsell 2016 and Inselberg — NOT REACHED. No guidelines quotable.

On the chapter's question: none of the studies reached measured whether a form leads a reader to read one profile as "better" rather than "different". They measured accuracy, time, memorability and preference. The only evaluative finding is Feldman's: filled area implies an ordering of units, and that ordering can reverse when axes are reordered.

----------------------------------------------------------------
C3. CLASSIFICATION AS IDENTITY IN OFFICIAL STATISTICS

(a) 2021/22 area classifications (ONS; GeoDS)

ONS index page, https://www.ons.gov.uk/methodology/geography/geographicalproducts/areaclassifications. Official practice.
- "Using socio-economic and demographic data from each census, they aim to identify areas of the country with similar characteristics." SINGLE PASS.
- "Possible applications include demonstrating broad geographic patterns, categorising data for further analysis, identifying similar areas for comparative studies and providing information for marketing purposes." Two phrases STRING-VERIFIED.
- The word "rank" does not appear on the page (presence check).

ONS "2021 and 2022 residential-based area classifications", https://www.ons.gov.uk/methodology/geography/geographicalproducts/areaclassifications/2021and2022residentialbasedareaclassifications. No date visible.
- The local authority classification covers "374 UK local authority districts", with "six supergroups, 19 groups, and 32 subgroups" (both phrases confirmed present).
- Supergroup names 1–5 STRING-VERIFIED: Services and industrial legacy; Densely populated urban centres; Education and heritage centres; English metropolitan living; Coastal and countryside living. Supergroup 6, Commuter living, SINGLE PASS (read from the page tail).
- Method: "A standard K-means clustering technique was applied to group together local authority districts with similar characteristics, to produce a hierarchical classification." SINGLE PASS.
- Naming caveats, all three STRING-VERIFIED:
  - "The following pen portraits (descriptions) and the names given to them are based on the average characteristics of each cluster."
  - "While they may not necessarily reflect the characteristics of the entire population, they are intended to be illustrative of the characteristics of areas in terms of their demographic structure, household composition, housing, socio-economic characteristics and employment patterns, and provide greater insight than examining the statistical outputs of cluster analysis alone."
  - "Given the subjective nature of producing names based on these average characteristics and their descriptive nature, there may be instances where individual local authorities are more or less closely associated with these descriptions."
- Each pen portrait carries plots of "the difference (either positive or negative) from the standardised mean used for comparison" (SINGLE PASS).
- "rank" does not appear in the first 100,000 characters. No explicit "this is not a ranking" sentence was found; no description of how names were agreed.
- "The Output Area Classification for 2021 and 2022 was developed by the Geographic Data Service (GeoDS) in partnership with the Office for National Statistics (ONS)." STRING-VERIFIED.

GeoDS, https://data.geods.ac.uk/dataset/output-area-classification-2021 (SINGLE PASS):
- "The UK 2021/2 Classification for Output Areas (2021/2 OAC) is a hierarchical geodemographic classification across the UK which identifies areas of the country with similar characteristics."
- 8 supergroups, 21 groups, 52 subgroups; v3.2 released January 2025.
- Pen portraits and technical report sit behind a login.
- THE EIGHT SUPERGROUP NAMES WERE NOT VERIFIABLE at any reachable source. On a first pass the reader mislabelled group names as supergroups. Do not print supergroup names from this report.
- The 21 group names as listed in the GeoDS postcode search app (https://apps.geods.ac.uk/oac/OACSearch, SINGLE PASS): 1a Spacious Rural Living; 1b Small Town Suburbia; 1c Established Mature Families; 2a Inner Suburbs and Small Town Living; 2b Rural Amenity; 2c Ageing Communities; 3a Student Living and Professional Footholds; 3b Ethnically Diverse Young Families; 3c Diverse Educated Urban Singles; 4a Ethnically Diverse Families in Less Connected Locations; 4b Established Multi-Ethnic Communities; 4c Challenged Multicultural Communities and Students; 5a Outer Suburbs; 5b Suburban Professionals; 6a Challenged Communities; 6b Legacy Industrial and Coastal Communities; 6c Multicultural Inner Suburbs; 7a Established but Challenged; 7b Young Families in Industrial Towns; 8a Routine Occupations or Retirement; 8b Legacy and Demographically Mixed Communities.

Wyszomierski, Longley, Singleton, Gale & O'Brien 2024, The Geographical Journal 190(2), e12550, CC BY (Crossref record https://api.crossref.org/works/10.1111/geoj.12550). ABSTRACT only; Wiley full text 403.
- "some of the variables now collected across different jurisdictions do not bear direct comparison with one another." SINGLE PASS.
- "Here we develop a methodology to accommodate these issues alongside the more established procedures of variable selection, standardisation, transformation, class definition and labelling." Final phrase STRING-VERIFIED.
- The paper's naming procedure for 2021/22 was not reached.

(b) Gale, Singleton, Bates & Longley 2016, "Creating the 2011 area classification for output areas (2011 OAC)", Journal of Spatial Information Science 12: 1–27. Open: https://josis.org/index.php/josis/article/download/66/66. Peer-reviewed methodology. Naming is in Section 7, "Describing UK geodemographic patterns", pp. 15–16. All five quotations STRING-VERIFIED (core strings):
- "The 2011 OAC comprises 8 Supergroups, 26 Groups, and 76 Subgroups."
- "Given the predominant public sector usage that was anticipated in creating the 2011 OAC, words and phrases that might be construed as pejorative were not used, and all descriptors had strong and literal links to the underlying distributions revealed by the data."
- "Words that were overtly negative or positive were avoided where possible, and the abiding sense of the descriptors was to present the characteristics of each cluster as consequences of factors that have happened to areas rather than the consequences of human agency."
- "Additional checks were undertaken to ensure that names where possible did not duplicate those used by previous commercial and non-commercial geodemographic classifications, and final approval of the cluster names was sought from ONS who conducted their own internal review and consultation."
- "Names and descriptions of clusters are, of course, based on the characteristics of their centroids, and the workings of the cluster assignment procedure means that specific areas differ in the degrees to which they conform to these average characteristics."

The 2011 supergroups (Table 4, SINGLE PASS; "Hard-Pressed Living" confirmed present): Rural Residents; Cosmopolitans; Ethnicity Central; Multicultural Metropolitans; Urbanites; Suburbanites; Constrained City Dwellers; Hard-Pressed Living.

On stigma, the only published statement reached is inside the same paper: "Vickers et al. [58] noted that names and descriptions of clusters may be contentious, especially if they reinforce negative stereotypes. Additionally, the procedure of conflating individual variables with one another opens up the risk of ecological fallacy within the analysis [47]." STRING-VERIFIED. [58] is Vickers, Rees & Birkin 2005, a University of Leeds technical report. No later published criticism of the 2011 names was located; without search this is absence of a find, not evidence of absence.

(c) ONS Explore Local Statistics. QMI, last revised 25 April 2025: https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/methodologies/explorelocalstatisticsserviceqmi. Official practice.
- The word "rank" does not appear anywhere on the QMI page (presence check).
- "The first chart is an interactive beeswarm chart, which shows individual data points spread out to avoid overlapping." STRING-VERIFIED.
- Comparison wording rule (SINGLE PASS; "median absolute deviation" confirmed present): "The text says 'higher' if the selected area is 1 or more median absolute deviations above the comparison value. … The text says 'similar' if the values are within 1 median absolute deviations of each other."
- Similar areas, STRING-VERIFIED: "These groups are created by using K-means clustering on a range of publicly available data sources"; "A global model that accounts for overall similarity is presented alongside economic- and demographic-themed models"; "This uses the same data as the clustering models to create an ordered list of the 20 most similar areas to the area of interest, ordered by Euclidean distance."
- Stated audience includes use "by enquiring citizens to explore which areas are similar to their own" STRING-VERIFIED.
- Comparability gate, STRING-VERIFIED (core strings): "The service strives to provide a UK-wide picture, allowing valid comparisons between local areas"; "This is to mitigate the risk of incorrect comparisons across statistical releases that are not methodologically coherent, or where data are provided for different time periods"; "The service presents these data as separate indicators to try to avoid inappropriate comparisons"; "We always check the coherence and comparability between indicators and agree this with data owners".
- Users can show confidence intervals "where applicable" (SINGLE PASS).

(d) Understanding Scottish Places. https://www.usp.scot/StaticPage/Methodology, https://www.usp.scot/StaticPage/AboutContact, and one town page read for template only. Official/practitioner tool; launched April 2015; now run by Scotland's Towns Partnership with the University of Stirling (SINGLE PASS).
- THE "NO GOOD OR BAD TOWN TYPE" WORDING WAS NOT FOUND on the Methodology page, the About page or the town-page template (explicit negative checks). The Carnegie UK and STP pages I tried returned 404. Do not use that phrase unless found in the 2015 Carnegie/CLES report.
- Typology: "K-Means Clustering is a data driven clustering procedure which seeks to maximise differences between clusters, with cases being as similar as possible to others in any cluster and as dis-similar to cases in other clusters as possible." STRING-VERIFIED (first clause).
- "Combining the typology with size categories 19 different groupings (the typology) were established (i.e. there were 5 types in the typology which contained no town entries)." STRING-VERIFIED (phrase).
- The page lists six descriptive cluster names (SINGLE PASS; not individually verified): Aspiring and Active towns; Comfortable Mature towns; Prosperous University; Affluent towns; Least Privileged towns; Diverse Social Circumstances. The current typology uses the 2022 Scottish Census.
- Base: 508 towns; localities with "a minimum rounded population of 500 people or more" (SINGLE PASS).
- Inter-relationships: "Twelve indicators are used which explore the inter-relationships within and between towns in Scotland." (SINGLE PASS); "For each indicator, towns have then been split into sevenths depending on their position across the 508 towns and given an appropriate score." (SINGLE PASS); "The highest aggregated total score is 62 with the lowest -62" STRING-VERIFIED.
- Seven bands from Independent to Dependent. "Dependent towns have a low number of assets in relation to their population; a reliance on one sector for jobs; and residents travel longer distances to work and study." SINGLE PASS.
- Town-page template, STRING-VERIFIED: "The typology groups Scottish towns based on socio-demographic characteristics using data from the 2022 census and size classification."; "Similarity is framed in the context of the socio-demographic typology."; "The town's are then classified by population size and finally ordered within groups based on their inter-relationship scores." [sic]; "The inter-relationships scale is split into seven possible scores ranging from independent through several levels of interdependence to dependent."
- No "ranked" sentence or league position appears on the template (negative check).
- Page order (SINGLE PASS): typology description; inter-relationships scale; similar towns; data tables; PDF download; comparison tool.
- Findlay et al. 2018, Scottish Affairs 27(3): 294–318 (Crossref abstract, SINGLE PASS): USP "has become a key tool for evidence gathering, town comparison, knowledge exchange, regeneration planning and informed decision making for Scottish towns."

(e) OECD Regional Well-Being. User Guide and FAQ, both October 2025: https://www.oecdregionalwellbeing.org/assets/downloads/Regional-Well-Being-User-Guide.pdf and .../FAQ-Regional-Well-Being.pdf. Official practice. All STRING-VERIFIED unless marked:
- "For each topic, a score on a scale from 0 to 10 is attributed to the region, based on one or more indicators."
- "A higher score indicates better performance in a topic relative to all the other regions."
- "The web tool does not include a regional composite well-being index." Then (SINGLE PASS): "The trade-off between a composite index (which conveys a single unified view, but may dilute information) and a range of indicators (which offers detailed information, but is more difficult to communicate) is widely debated."
- "We do not make a single statement about the overall well-being in a region."
- "Instead, we present the information in such a way that users can consider the relative importance of each topic and bring their own personal evaluations to these issues." (first part verified).
- "There is no single ranking associated to the regional well-being web tool" (under the FAQ question "What are the best and worst ranked regions?").
- "Ranking regions according to their level of well-being depends on what users consider important. There can therefore be many rankings according to the criteria the users will choose."
- But within a topic: "Regions are ranked according to their values in each topic."
- The display shows "the relative position of the region compared to the other regions in the same country, and its relative position compared to all of the OECD regions" (SINGLE PASS).
- Similar regions: "The calculation to identify similar regions is based on the sum of the absolute differences in the topics scores, the so-called Manhattan distance." Also "The top four regions from different countries with the lowest distance to the selected region are displayed." (SINGLE PASS).
- 468 regions and eleven topics in the guide; the home page says 467.

(f) ONS "How life has changed in [area]: Census 2021" (https://www.ons.gov.uk/visualisations/censusareachanges/; one area page read for template only).
- Descriptive articles, one per local authority. On the page as fetched, "ranked/ranks/ranking" and "out of N local authority areas" did not appear (negative check; the page is partly script-rendered, so treat as SINGLE PASS).
- The template does use ordinal comparison within the region (patterns such as "saw the [region]'s largest percentage-point rise", "Only [nearby area] saw a greater…") and compares with region and England. SINGLE PASS.
- Caveats: "Because the census question about religious affiliation is voluntary and has varying response rates, caution is needed when comparing figures between different areas or between censuses." STRING-VERIFIED (core). "Caution should be taken when making comparisons between 2011 and 2021 because of changes in question wording and response options." STRING-VERIFIED.

(g) EU Cultural and Creative Cities Monitor. The live tool renders by script and could not be read. From the 2019 edition report (https://publications.jrc.ec.europa.eu/repository/bitstream/JRC117336/uk.pdf; text only partly extractable; SINGLE PASS): cities are placed in four population groups (XXL, XL, L, S-M) and five GDP-per-capita groups; one figure caption reads "Cities are ordered alphabetically within each population group" (confirmed present). Whether a city page shows a rank, a radar or both was NOT VERIFIED.

----------------------------------------------------------------
C4. COMPARABILITY AS A QUALITY DIMENSION

European Statistics Code of Practice, revised edition 2017 ("Adopted by the European Statistical System Committee 16th November 2017"). https://ec.europa.eu/eurostat/documents/4031688/8971242/KS-02-18-142-EN-N.pdf. Standard. Principle 14, Coherence and Comparability:
- "European Statistics are consistent internally, over time and comparable between regions and countries; it is possible to combine and make joint use of related data from different data sources." STRING-VERIFIED.
- 14.2 "Statistics are comparable over a reasonable period of time." STRING-VERIFIED.
- 14.3 "Statistics are compiled on the basis of common standards with respect to scope, definitions, units and classifications in the different surveys and data sources." STRING-VERIFIED.
- 14.4 "Statistics from the different data sources and of different periodicity are compared and reconciled." STRING-VERIFIED.
- 14.1 and 14.5 SINGLE PASS.
- 15.7 "Users are kept informed about the quality of statistical outputs with respect to the quality criteria for European Statistics." SINGLE PASS.

Regulation (EC) No 223/2009, Article 12(1). https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009R0223. Both STRING-VERIFIED:
- (f) "'comparability', which refers to the measurement of the impact of differences in applied statistical concepts, measurement tools and procedures where statistics are compared between geographical areas, sectoral domains or over time"
- (g) "'coherence', which refers to the adequacy of the data to be reliably combined in different ways and for various uses"

Eurostat SIMS Technical Manual (2014 reference; concepts numbered S.17 in this version). https://ec.europa.eu/eurostat/documents/64157/4373903/03-Single-Integrated-Metadata-Structure-and-its-Technical-Manual.pdf.
- Comparability – geographical: "The extent to which statistics are comparable between geographical areas." STRING-VERIFIED.
- Comparability – over time: "The extent to which statistics are comparable or reconcilable over time." STRING-VERIFIED.
- What the producer must report, geographical (SINGLE PASS): "Describe any problems of comparability between countries or regions. The reasons for the problems should be described and as well an assessment (preferably quantitative) of the possible effect of each reported difference on the output values should be done."
- Over time (SINGLE PASS): "provide information on the length of comparable time series, reference periods at which series breaks occur, the reasons for the breaks and treatments of them."

UK Code of Practice for Statistics 3.0 (OSR; published 3 November 2025; page last modified 10 August 2026). Standards for Official Statistics: https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/5/. Standard. Ten standards: Show Integrity; Lead Responsibly; Be Transparent; Manage Data Responsibly; Prioritise Quality; Be Rigorous; Be Open About Quality; Be Relevant; Be Clear; Be Accessible. Practices, all STRING-VERIFIED (two or three passes):
- 6.6 "Use data that are coherent when aggregated, consistent over time and comparable across and within geographies at regional, national and local levels, where possible. Seek to design new statistics in ways that achieve UK comparability and improve consistency and coherence with related statistics"
- 6.7 "… Use recognised standards, classifications and definitions. Explain reasons for deviations from these standards and any related implications for use"
- 6.10 includes "such as completeness and validity, accuracy and reliability, coherence and comparability, and timeliness"
- 7.3 "… Prominently communicate limitations in the underlying data and explain their impact on the statistics"
- 7.4 "Be clear about the methods used. Explain quality issues related to the methods, systems and processes, including the extent to which the statistics are representative and comparable across the UK and internationally. Describe potential bias and steps taken to address it"
- 9.3 "Provide comparisons to support interpretation and signpost other relevant statistics, including within the UK and internationally. Explain the consistency and coherence with other related statistics and sources"
- 9.5 "Aid understanding by highlighting potential misinterpretations. …"
- Headline of "Be Open About Quality" (SINGLE PASS): "Producers must prominently explain the quality of the statistics, including strengths and limitations, and communicate the uncertainty in estimates so that the public can have confidence in using the statistics to make decisions and take actions."

Standards for the Public Use of Statistics, Data and Wider Analysis (pages/7/): practice wording came back paraphrased (for example, avoid cherry-picking; communicate key context and limitations). SINGLE PASS; not quotable as exact.

OECD/JRC Handbook on Constructing Composite Indicators — NOT REACHED (two attempts).

What the frameworks require a producer to state when comparing places:
- Code 3.0: say how far the statistics are comparable (7.4), explain deviations from standard definitions and classifications (6.7), and explain consistency and coherence with related statistics (9.3).
- ESS/SIMS: describe comparability problems between regions, their reasons and, preferably, their quantitative effect.
- None of the texts reached sets a numeric threshold for when a comparison may be shown.

----------------------------------------------------------------
C5. THE MODIFIABLE AREAL UNIT PROBLEM, DEMONSTRATED

Fotheringham & Wong 1991, Environment and Planning A 23(7): 1025–1044. https://journals.sagepub.com/doi/10.1068/a231025. ABSTRACT only. The design (study area, number of zonings) and the size of coefficient changes were NOT reachable; no numbers can be given. All STRING-VERIFIED:
- "The modifiable areal unit problem is shown to be essentially unpredictable in its intensity and effects in multivariate statistical analysis and is therefore a much greater problem than in univariate or bivariate analysis."
- "they provide strong evidence of the unreliability of any multivariate analysis undertaken with data from areal units"
- "this paper serves as a topical warning"

Openshaw & Taylor 1979 — primary NOT REACHED. THE "−0.99 TO +0.99" FIGURE COULD NOT BE VERIFIED and should not be printed from this report. What was reached, in Jelinski & Wu 1996, Landscape Ecology 11(3): 129–140 (https://leml.asu.edu/jingle/Web_Pages/Wu_Pubs/PDF_Files/Jelinski_Wu_1996.pdf), secondary, STRING-VERIFIED there:
- "correlations ranging from + 0.979 to - 0.811 could be produced by varying the scale and zoning strategies." (percentage of elderly voters against Republican voters; "the 99 counties in the state of Iowa").
- Definitions, quoted by Jelinski & Wu from Openshaw & Taylor: the scale problem is "the variation in results that may be obtained when the same areal data are combined into sets of increasingly larger areal units of analysis"; the zoning problem is "any variations in results due to alternative units of analysis where n, the number of units, is constant".

Flowerdew 2011, "How serious is the Modifiable Areal Unit Problem for analysis of English census data?", Population Trends 145: 106–118. Full text: https://link.springer.com/content/pdf/10.1057/pt.2011.20.pdf. ONS journal; empirical; UK census. Tests the scale effect only.
- Design (SINGLE PASS on counts): 2001 Census, England; Output Areas (165,665), wards (7,969), districts (354).
- "Eighteen variables were selected for investigation" STRING-VERIFIED.
- "The eighteen variables in the data set, taken pairwise, provide 153 correlations at each of the three scales." STRING-VERIFIED.
- "68 of these were negative at all three scales, while 60 were positive at all three. Of the remainder, there was no clear trend: 12 were negative at the OA level but positive at the district level, while 12 changed in the opposite direction and 10 changed in one direction and then back again." Returned identically in two passes. FLAG: 68+60+12+12+10 = 162, not 153. Check the PDF by eye before printing these counts.
- "In other words, the MAUP does make a difference in about 60 per cent of cases." STRING-VERIFIED (Fisher's Z tests between scales).
- "How serious is the MAUP? Most of the time, not very – but there are occasions when it can make a great deal of difference. Unfortunately it remains difficult to predict these occasions." First two sentences STRING-VERIFIED; third SINGLE PASS.
- "Some studies indicate that correlations over virtually the whole range from -1 to +1 can be reached by judicious placement of zone boundaries." STRING-VERIFIED. This is the nearest verified wording to the −0.99/+0.99 claim, and it is Flowerdew's general statement.

Wong 2009 and Manley 2014 — NOT REACHED.

ONS on best-fit. https://www.ons.gov.uk/methodology/geography/geographicalproducts/postcodeproducts. Official practice. All STRING-VERIFIED:
- "These OAs are then referenced to a wide range of higher geographies (for example, local authority districts) by a best-fit methodology that uses Census population data."
- "You should note that postcodes with addresses that straddle a boundary will be assigned to the area where the mean grid reference of all the addresses within that postcode falls."
- "The methodology used within the NSPL to allocate postcodes to higher geographies is different from that used in the ONSPD."
- "If you are a producer of National Statistics, you should use the NSPL to allocate your source statistics at postcode level to a wide range of higher geographies." (SINGLE PASS.)
- No tolerance or accuracy figure for best-fit is stated on any ONS page reached (negative check). The detailed best-fit note and the "Hierarchical representation of UK statistical geographies" sit on the Open Geography Portal, which could not be read.

----------------------------------------------------------------
C6. UK STATISTICAL GEOGRAPHIES: WHAT EACH UNIT IS FOR

Census 2021 thresholds. https://www.ons.gov.uk/methodology/geography/ukgeographies/statisticalgeographies and https://www.ons.gov.uk/census/census2021dictionary/areatypedefinitions.
- Output Areas: "the lowest level of geographical area for census statistics" STRING-VERIFIED. "Each Output Area is made up of between 40 and 250 households and a usually resident population of between 100 and 625 persons." (dictionary page, SINGLE PASS; the figures are STRING-VERIFIED on the geography page in the sentence about unchanged 2011 OAs).
- LSOAs: "They comprise between 400 and 1,200 households and have a usually resident population between 1,000 and 3,000 persons." STRING-VERIFIED. 33,755 in England and 1,917 in Wales (SINGLE PASS).
- MSOAs: "They comprise between 2,000 and 6,000 households and have a usually resident population between 5,000 and 15,000 persons." STRING-VERIFIED. 6,856 in England and 408 in Wales (SINGLE PASS).
- These are minimum and maximum ranges. No "target" size is stated for 2021 on the pages reached.

Design for statistics, not recognition. https://www.ons.gov.uk/methodology/geography/ukgeographies/censusgeography. All STRING-VERIFIED:
- "They were designed to have similar population sizes and be as socially homogenous as possible based on tenure of household and dwelling type (homogeneity was not used as a factor in Scotland)."
- "The minimum OA size was 40 resident households and 100 resident people, but the recommended size was rather larger at 125 households."
- "Urban/rural mixes were avoided where possible; OAs preferably consisted entirely of urban postcodes or entirely of rural postcodes."
- "SOAs were designed to improve the reporting of small area statistics and are built up from groups of output areas (OA)."
- "This had drawbacks because electoral wards/divisions vary greatly in size, from fewer than 100 residents to more than 30,000. This was not ideal for nationwide comparisons, and also meant that some data could not be released for smaller wards due to disclosure issues and the need to protect the confidentiality of individuals."
- No sentence was found saying OAs follow neighbourhoods residents recognise (negative check).

Wards. https://www.ons.gov.uk/methodology/geography/ukgeographies/administrativegeography/england. All STRING-VERIFIED:
- "As of 5 May 2022, the UK has 8,483 electoral wards and electoral divisions, with 6,904 in England."
- "Ward population counts can vary substantially, even within a single LAD, but the UK average is about 7,900."
- "Electoral ward and electoral division boundary changes are usually enacted on the first Thursday in May each year, to coincide with the local government elections in the UK."

Built-up areas 2022. ONS article of 2 August 2023: https://www.ons.gov.uk/peoplepopulationandcommunity/housing/articles/townsandcitiescharacteristicsofbuiltupareasenglandandwales/census2021. All STRING-VERIFIED:
- "Built-up areas (BUAs) are a geography based on the physical built environment, using Ordnance Survey topographic data to recognise developed land, such as cities, towns, and villages."
- "The main change is that the geography has been simplified into a single layer, providing one boundary and a single set of statistics for each settlement."
- "Changes and updates to the geography boundaries since 2011 mean that statistics from 2021 BUAs cannot be directly compared with those from 2011."
- Size bands (SINGLE PASS): minor 0–4,999; small 5,000–19,999; medium 20,000–74,999; large 75,000–199,999; major 200,000+.

Postal geography. https://www.ons.gov.uk/methodology/geography/ukgeographies/postalgeography. SINGLE PASS:
- "Royal Mail maintains a UK-wide system of postcodes to identify postal delivery areas."
- "Postcode boundaries are subject to continuous change…"
- "Postcode boundaries mostly do not align with other geographic boundaries."
- A unit postcode "may contain up to 100 addresses, but 15 is a more typical number".

Why the Index of Multiple Deprivation uses LSOAs.
- IoD2019 Technical Report (MHCLG, September 2019), https://assets.publishing.service.gov.uk/media/5d8b387740f0b609909b5908/IoD2019_Technical_Report.pdf. Both STRING-VERIFIED: paragraph 3.3.11, "The Indices of Deprivation 2019 have been produced at Lower-layer Super Output Area level, using the current (2011) Lower-layer Super Output Areas."; footnote, "Lower-layer Super Output Areas are homogenous small areas of relatively even population size containing approximately 1,500 people." The technical report gives no fuller reason, and no sentence comparing LSOAs with wards was found.
- IoD2019 Statistical Release (26 September 2019), https://assets.publishing.service.gov.uk/media/5d8e26f6ed915d5570c6cc55/IoD2019_Statistical_Release.pdf. All STRING-VERIFIED: "LSOAs are small areas designed to be of a similar population size, with an average of approximately 1,500 residents or 650 households."; "They are a standard statistical geography produced by the Office for National Statistics for the reporting of small area statistics."; "LSOAs are also referred to as 'neighbourhoods' throughout this release."
- English Indices of Deprivation 2025 (MHCLG, 30 October 2025), https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025/english-indices-of-deprivation-2025-statistical-release. SINGLE PASS: 33,755 LSOAs on 2021 boundaries; "LSOAs (Lower-layer Super Output Areas) are referred to as 'neighbourhoods' throughout this release."; boundary and other changes make "comparison over time more problematic".

----------------------------------------------------------------
C7. "SCENE" AS A UNIT OF ANALYSIS — METHOD ONLY

Straw 1991, Cultural Studies 5(3): 368–388 (Crossref). Author copy: https://willstraw.com/wp-content/uploads/2019/06/systems-of-articulation-logics-of-change.pdf; p. 373. Peer-reviewed; conceptual. All STRING-VERIFIED (three fragments each):
- Community: "The latter presumes a population group whose composition is relatively stable—according to a wide range of sociological variables—and whose involvement in music takes the form of an ongoing exploration of one or more musical idioms said to be rooted within a geographically specific historical heritage."
- Scene: "A musical scene, in contrast, is that cultural space in which a range of musical practices coexist, interacting with each other within a variety of processes of differentiation, and according to widely varying trajectories of change and cross-fertilization."

Bennett & Peterson 2004 — NOT REACHED (publisher robots-blocked; Bennett's Poetics article has no open abstract). The three types (local, translocal, virtual) are named but no definition can be quoted.

Silver, Clark & Navarro 2010, "Scenes: Social Context in an Age of Contingency", Social Forces 88(5): 2293–2324. https://academic.oup.com/sf/article-abstract/88/5/2293/1891969. ABSTRACT; three phrases STRING-VERIFIED:
- The "'scene' as a cluster of urban amenities".
- "This framework adds to concepts such as neighborhood and workplace by specifying 15 dimensions of the urban scenescape."
- "We introduce a new amenities-focused database to measure and analyze scenes and their dimensions for each of 40,000 U.S. zip codes."

Silver, Clark & Rothfield, "A Theory of Scenes" (University of Chicago working paper, undated). http://scenes.uchicago.edu/theoryofscenes.pdf. Method statements:
- "Scenes are spaces within which different kinds and aspects of consumption are given symbolic meaning." STRING-VERIFIED.
- Fifteen sub-dimensions (SINGLE PASS on labels). Theatricality: transgressive, formal, neighborly, glamorous, exhibitionistic. Authenticity: local, ethnic, state, rational, corporate. Legitimacy: traditionalism, utilitarianism, expressivism, egalitarianism, charisma.
- Coding: "Scores range from 1-5, where 5 indicates that participation in the activities promoted by an amenity is fundamentally defined by the given sub-dimension, 1 indicates that participation in these activities fundamentally and actively opposes the sub-dimensions, and 3 indicates that the amenity is neutral with respect to the sub-dimensions." STRING-VERIFIED (first clause).
- Attaching a score to a zip code, both STRING-VERIFIED: "We multiply the number of amenities of a given type in a zip code by that amenity-type's score, and then sum the results for each sub-dimension."; "We divide the intensity score for each zip code by the total number of amenities in the zip code." Then (SINGLE PASS): "We call this measure the 'performance rating.' This rating shows the average degree to which a zip code's amenities support a given sub-dimensions."
- Sources: "the U.S. census of business, online yellow pages sources, and the Unified Database of Arts Organizations compiled by the Urban Institute" (phrase verified); "over 700 indicators of amenities" (SINGLE PASS).
- Reliability: "Though weights did of course vary, inter-correlations of coders' scores showed a high degree of reliability." STRING-VERIFIED. No coefficient or number of coders is given.
- The authors rank on it: "We can also use these profiles to create rankings and maps of the U.S. in terms of zip codes' scores on individual sub-dimensions as well as their scores in terms of different groups of sub-dimensions." STRING-VERIFIED.
- Stated limits: none found in this paper (negative check for words such as limitation, cannot, caution). Scenescapes (2016), where limits would be discussed, was NOT REACHED.

Method critique reached: Straw, "Some Things a Scene Might Be", Cultural Studies (postface; the copy is paginated 1–10, 2014). https://willstraw.com/wp-content/uploads/2019/01/straw-cultural-studies-2014-scenes.pdf. All STRING-VERIFIED:
- Places the Chicago approach within "debates over the status of culture as amenity" and says it has "found their fullest academic development in the 'scenes perspective' developed by sociologists originally based at the University of Chicago". He offers no explicit criticism of the measurement.
- On what a unit built from listed amenities can and cannot see: scenes are "spaces of mediation which regulate the visibility and invisibility of cultural life and the extent of its intelligibility to others".
- "Scenes make cultural activity visible and decipherable by rendering it public, taking it from acts of private production and consumption into public contexts of sociability, conviviality and interaction."
- "Just as clearly, though, scenes make cultural activity invisible and indecipherable by 'hiding' cultural productivity behind seemingly meaningless (or indistinguishable) forms of social life."

No dedicated methodological critique of the amenity-scoring method was located without search.

----------------------------------------------------------------
C8. PARTIAL ORDERS AND INCOMPARABILITY AS A DISPLAY

Fattore 2016, "Partially Ordered Sets and the Measurement of Multidimensional Ordinal Deprivation", Social Indicators Research 128(2): 835–858 (online 5 August 2015). https://link.springer.com/article/10.1007/s11205-015-1059-6. ABSTRACT; peer-reviewed. All STRING-VERIFIED:
- "Evaluation is addressed in terms of multidimensional comparisons among achievement profiles, rather than through attribute score aggregations."
- "This makes it unnecessary to scale ordinal attributes into numerical variables, overcoming the limitations of aggregative procedures and counting approaches."
- "The evaluation procedure is fuzzy in nature, accounts for both vagueness and intensity of deprivation"
- "Hasse diagram" is a keyword and the figures are Hasse diagrams (reader's report).

Fattore, Maggino & Colombo 2012 — NOT REACHED (Springer chapter and Crossref record both rate-limited). Confirmed only as a reference in Fattore 2016, where the title reads "From composite indicators to partial order: evaluating socio-economic phenomena through ordinal data" (SINGLE PASS; note "partial order", singular, in that listing). No argument can be quoted.

Annoni & Brüggemann 2009, "Exploring Partial Order of European Countries", Social Indicators Research 92(3): 471–487. https://link.springer.com/article/10.1007/s11205-008-9298-4. ABSTRACT. Annoni's affiliation there is the University of Milan, so this is not a JRC publication. Both STRING-VERIFIED:
- "Partial Order Theory has been recently more and more employed in applied science to overcome the intrinsic disadvantage hidden in aggregation, if a multiple attribute system is available."
- "there are many practical cases where the interpretation of the partial order can be rather troublesome."

JRC and Hasse diagrams for the EU Regional Competitiveness Index: nothing located. Without search I could not test this properly; treat as not found, not as non-existent.

Usability evaluation of Hasse diagrams or dominance displays with lay readers: none found in anything reached. The only relevant statement is the practitioners' own admission above that interpretation "can be rather troublesome". A systematic search was not possible.

----------------------------------------------------------------
ALSO REPORTED: TOOLS THAT SHOW "PLACES LIKE MINE" BY A PUBLISHED METHOD AND, SEPARATELY, CONDITIONS COMPARED

No tool reached states a separation of identity from conditions as a layout principle. What is on screen:
- Understanding Scottish Places. Page order puts the typology description first, then the inter-relationships scale, then "Similar towns", then indicator tables and a compare tool. Similar towns are chosen by typology, then size, then ordered by inter-relationship score. No league position is shown. The inter-relationship score is itself built from each town's position in sevenths across 508 towns.
- ONS Explore Local Statistics. A "Similar areas" section (k-means clusters in global, economic and demographic models, plus the 20 nearest neighbours by Euclidean distance) sits apart from the indicator pages. Indicator pages show a beeswarm of all local authorities, with a comparator the user chooses (which can be demographically similar areas) and "higher / lower / similar" text set by a one-MAD rule. The QMI never uses the word "rank".
- OECD Regional Well-Being. Similarity is computed from the same eleven topic scores that are being compared (Manhattan distance; four regions from other countries). So "similar" there means similar outcomes; there is no separate identity layer. No composite; within-topic ranking only.
- ONS local authority classification. Identity only (cluster, name, pen portrait, difference-from-mean plots); no conditions comparison on that page.
- Not reached or not attempted: LG Inform comparison groups (page gave no descriptive text), CIPFA (settled earlier), Discover Uni, Trust for London.

----------------------------------------------------------------
UNASKED THREADS
1. Gale et al.'s naming rule that descriptors present cluster characteristics "as consequences of factors that have happened to areas rather than the consequences of human agency". A published, peer-reviewed rule for naming a place type without blame.
2. ONS's standing caveat that names rest on "average characteristics" and that areas "are more or less closely associated with these descriptions". Official wording for a per-place hedge on an identity label.
3. The Explore Local Statistics wording rule: "higher / lower / similar" decided at one median absolute deviation. A published threshold governing comparison language, not just the chart.
4. The same service's gate: non-coherent data are kept "as separate indicators to try to avoid inappropriate comparisons".
5. Flowerdew 2011. A UK census test of the scale effect, with a moderate conclusion ("Most of the time, not very") alongside "difficult to predict these occasions".
6. Both IoD2019 and IoD2025 call LSOAs "neighbourhoods" by definition, although LSOAs were designed for size and homogeneity, not recognition.
7. Built-up areas 2022 are settlement-shaped units, but "cannot be directly compared with those from 2011", and Greater London follows borough boundaries. The recognisable unit costs comparability over time.
8. The Chicago scenes method, although framed as qualitative character, explicitly offers "rankings and maps" of zip codes by sub-dimension. A profile built as identity is ranked by its own authors.

LEFT OUT, AND WHY
- No direct quotation from Stevens 1946, Hand 1996, Chrisman 1998, Diehl et al. 2010, Johansson & Forsell 2016, Inselberg, Chernoff 1973, Morris et al. 2000, Bennett & Peterson 2004, Scenescapes, Openshaw & Taylor 1979, Wong 2009, Manley 2014, Fattore et al. 2012 or the OECD/JRC Handbook: all unreachable within two attempts or rate-limited.
- Sample sizes for Albo 2016, Javed 2010 and Diehl 2010: not in the abstracts reached.
- The eight 2021/22 OAC supergroup names: not verifiable at source.
- The live CCCM, LG Inform, Discover Uni and Trust for London displays.
- Any finding about a particular place. One USP town page and one ONS area page were read for template wording only.
- The Code 3.0 public-use standards' practice wording: paraphrased by the reader, so not quoted as exact.

RICH REFERENCES
1. Gale, Singleton, Bates & Longley 2016, JOSIS 12: 1–27, Section 7. Open access. The fullest published account of how an official place typology was named, including the ecological-fallacy and stereotype cautions.
2. ONS Explore Local Statistics QMI (last revised 25 April 2025). Similarity method, beeswarm display, the MAD wording rule and the comparability gate in one official document.
3. Velleman & Wilkinson 1993. Open author copy. Both the critique and its concessions, with the Hand & Keynes counter-position quoted inside it.

SURPRISED
- The "no good or bad town type" line attributed to USP is not on its current methodology, about or town pages.
- The OECD tool says "There is no single ranking" yet defines "similar regions" from the outcome scores themselves.
- Feldman's point is purely geometric (four pages, no experiment), yet it bears most directly on whether a radar reads as "better".
- The Openshaw & Taylor range that could be verified was +0.979 to −0.811 (via Jelinski & Wu), not ±0.99.
- Flowerdew's sign-change counts, as extracted twice, sum to 162 against a stated 153 pairs.
- The brief's author list for "Off the radar" was wrong (Rafaeli, not Berkovich).
- Code of Practice 3.0 writes geography into the practice itself ("comparable across and within geographies at regional, national and local levels, where possible").


---

## Agent D

AGENT D REPORT — DISCOVERY AND THE CROP
All fetches 6 October 2026.

ACCESS: WebSearch was unavailable (the shared search budget was already used up on my first call). Everything below came from direct URLs through WebFetch. Blocked or unreachable: web.archive.org and the UK Government Web Archive, ACM Digital Library, ScienceDirect, Wiley, Science, tandfonline, the Guardian, Semantic Scholar and OpenAlex (rate-limited). Direct curl is blocked by proxy policy, so string checks were done by re-fetching with YES/NO prompts and false controls.

Marks: SV = STRING-VERIFIED, SP = SINGLE PASS, ABSTRACT = abstract only.

---------------------------------------------------------------
D1. RECOMMENDER EXPLANATIONS

Herlocker, Konstan & Riedl 2000, "Explaining collaborative filtering recommendations" (CSCW). Peer-reviewed; two experiments on MovieLens users. https://grouplens.org/site-content/uploads/explain-CSCW-20001.pdf
- Experiment 1: "The survey was presented to 78 users of the MovieLens site" (SV). "Each user was then provided with 21 individual movie recommendations" (SV), each with a different explanation, and "asked to rate on a scale of 1" to 7 how likely they would be to go and see the movie (SV to "scale of 1"; rest SP). The measure is likelihood of going to see the film, which is persuasion, not decision quality.
- Top three (table rows SV): "Histogram with grouping" 5.25; "Past performance" 5.19; "Neighbor ratings histogram" 5.09. The no-explanation base cases sat 11th–12th at 4.53 and 4.51 (SP).
- Some explanations "had significantly lower mean response than the base cases" (SV; the reader gave these as numbers 18–21, SP). "Poorly designed explanations can actually decrease the effectiveness of a recommender system" (SV).
- Why the grouped histogram won (SP): "Explanation 1 performed better than a basic bar chart because it reduced the dimensionality of the data to a point where only one binary comparison is necessary (the good versus the bad)."
- Experiment 2: "210 users participated in this study, filling out 743 mini-surveys" (SV). On decision performance: "There was no statistically significant difference between any two experimental groups" (SV) and "The filtering performance measurements performed during this study were inconclusive" (SV).
- CORRECTION TO VERSION 1's "86%": "86% of these users said that they would like to see their explanation interface added to the system" (SV). "These users" are "97 experimental subjects filled out the exit survey" (SV), who were "users in non-control groups were asked if they would like to see the explanation interface they had experienced added" (SV). So it is 86% of 97 exit-survey respondents in the non-control groups of experiment 2, asked about the interface they had just used. It is not 86% of all 210, and not a general "users want explanations".
- Abstract: "providing explanations can improve the acceptance of ACF systems" (SV).
Role: the founding evidence shows explanations raise acceptance and liking; it does not show better decisions, and bad explanations did worse than none.

Tintarev & Masthoff 2007, "A Survey of Explanations in Recommender Systems" (ICDE'07 workshop). Practitioner framework. Author copy: http://navatintarev.com/papers/TintarevMasthoffICDE07.pdf
Table 1, in the paper's order (all SV):
1. Transparency: "Explain how the system works"
2. Scrutability: "Allow users to tell the system it is wrong"
3. Trust: "Increase users' confidence in the system"
4. Effectiveness: "Help users make good decisions"
5. Persuasiveness: "Convince users to try or buy"
6. Efficiency: "Help users make decisions faster"
7. Satisfaction: "Increase the ease of usability or enjoyment"
"It is hard to create explanations that do well on all our criteria, in reality it is a trade-off" (SV).

Tintarev & Masthoff 2012, UMUAI 22(4–5):399–439. ABSTRACT only (full text paywalled). https://link.springer.com/article/10.1007/s11257-011-9117-5
- "Contrary to expectation, personalization was detrimental to effectiveness, though it may improve user satisfaction" (SV on abstract). Direction confirmed.
- "four empirical studies in two domains: movies and cameras" (SV).
- n per study NOT verified.

Nunes & Jannach 2017, UMUAI 27(3–5):393–444 (journal reference SP). Systematic review; author version https://arxiv.org/pdf/2006.08672
- "we ended up with a total of 217 primary studies" (SV), from "we obtained 1209 papers (excluding duplicates) as result" (SP; written without a comma).
- "less than a quarter (21.5%) of the studies involving techniques and tools contains any form of evaluation" (SV).
- User studies "occurring in more than half (52.4%) of the cases" (SV).
- "the most common explanation purpose is to provide transparency" (SV).
- "no clear consensus on what constitutes a good explanation" (SV).

Kunkel et al. 2019 (CHI): UNREACHABLE (ACM 403 three times; metadata APIs 429). Nothing quoted; n and finding unverified.

Concrete cues against vague social proof: Bilgic & Mooney, "Explaining Recommendations: Satisfaction vs. Promotion". https://www.cs.utexas.edu/users/ml/papers/submit.pdf (venue not printed on the copy; I have not verified it).
- "34 subjects" (SV), "53 recommendations" (SV).
- "NSE causes the user to overestimate the actual-rating by 0.74 on average" (SV). NSE is the neighbour-rating style, the "people like you rated this" kind.
- SP: "For the promotion approach, the best explanation is the one that is most successful at convincing the user to adopt an item. For the satisfaction approach, the best explanation is the one that lets the users assess the quality of the item the best."
- SP: keyword-style (content of the item) and influence-style (the user's own past ratings) explanations "were found to be significantly more effective at enabling accurate assessments."
Role: small peer-reviewed study and the direct evidence that concrete content cues support accurate judgement while neighbour-popularity cues inflate it.

---------------------------------------------------------------
D2. EXPOSURE FAIRNESS AND POPULARITY BIAS

Singh & Joachims 2018 (KDD). https://arxiv.org/pdf/1802.07281
- "ranking systems have a responsibility not only to their users but also to the items being ranked" (SV, abstract).
- "the scarce resource that ranking systems allocate is the exposure of items to users" (confirmed in an A/B wording check) "and exposure is largely determined by position in the ranking" (SV).
- Worked example: six applicants with relevance 0.80/0.79/0.78 and 0.77/0.76/0.75; under a 1/log(1+j) position drop-off "the female applicants will get 30% less exposure" (SV) "even though the average difference in relevance between male and female applicants is just 0.03" (SP).
- "It is unlikely that there will be a universal definition of fairness that is appropriate across all applications" (confirmed in an A/B check).
- Formal definition (SP): exposure of item i under probabilistic ranking P is the sum over positions j of P(i,j)·v(j), where v(j) is position bias; group exposure is the mean over the group.
- The sentence that small relevance differences produce large exposure differences is present, but two passes disagreed on "can cause" versus "can lead to". Paraphrase it; do not quote.

Abdollahpouri, Mansoury, Burke & Mobasher 2019, "The Unfairness of Popularity Bias in Recommendation". https://arxiv.org/pdf/1907.13286
- "Presented at the RMSE workshop held in conjunction with the 13th ACM Conference on Recommender Systems" (SV).
- Data: MovieLens 1M, "1,000,209" ratings (SV); about 3,900 movies and 6,040 users (SP); six algorithms (SP).
- Niche users: "These are the bottom 20% of users in terms of the ratio of popular items in their profile" (SV).
- Finding: "recommendations the users get are extremely concentrated on popular items even if a user is interested in long-tail" (SV); "the niche users are seeing the largest discrepancy" (SV).
The companion re-ranking paper (arXiv 1901.07555) was ABSTRACT only and the reader paraphrased it; it is a mitigation method and does not carry the niche-user finding.

Ekstrand, Das, Burke & Diaz 2022, "Fairness in Information Access Systems". https://arxiv.org/pdf/2105.05779
- "Universal fairness is not an achievable (or arguably even meaningful) concept" (SV).
- R. Burke (2017) "distinguishes between provider- and consumer-side fairness" (SV).
- Popularity-bias and rich-get-richer work "can be viewed as a type of fairness problem" (SV fragment; full sentence SP).
- SP: "The system should not inordinately favor popular, well-known, and possibly well-funded content creators."
- The reader saw only the first 100,000 of about 117,000 characters. I did not capture a one-sentence definition of provider fairness or exposure; section 6.2 is titled "Provider Exposure and Utility" (SP).

Salganik, Dodds & Watts 2006, Science 311:854–856. Author-hosted: https://pdodds.w3.uvm.edu/research/papers/years/2006/salganik2006a.pdf
Read as method about ranked displays:
- "14,341 participants" (SV), "recruited mostly from a teen-interest World Wide Web site" (SV); "48 songs" (SV).
- Independent condition against a social-influence condition split into eight separate "worlds" (SV on "eight").
- Experiment 1 showed download counts in a 16 × 3 grid with random positions (near-verified; the "×" was lost in the PDF text). Experiment 2 showed songs in "one column in descending order of current popularity" (SV).
- "inequality increased when the salience of the social information signal was increased from experiment 1 to experiment 2" (SV).
- "Increasing the strength of social influence increased both inequality and unpredictability of success" (SV).
- "The best songs rarely did poorly, and the worst rarely did well, but any other result was possible" (SV).
- n per experiment was not found in the text read.
Role: the cleanest experimental evidence that sorting by popularity is itself the treatment.

Fleder & Hosanagar 2009, Management Science 55(5). ABSTRACT (pages not confirmed). https://pubsonline.informs.org/doi/10.1287/mnsc.1080.0974
All SV on the abstract:
- "some well-known recommenders can lead to a reduction in sales diversity"
- "these recommenders can create a rich-get-richer effect for popular products and vice versa for unpopular ones"
- "This bias toward popularity can prevent what may otherwise be better consumer-product matches"
- "it is possible for individual-level diversity to increase but aggregate diversity to decrease"
- "Recommenders can push each person to new products, but they often push users toward the same products"
This is an analytical model plus simulation, not a field result.

---------------------------------------------------------------
D3. THE FILTER-BUBBLE NULL AND SERENDIPITY

Arguedas, Robertson, Fletcher & Nielsen, Reuters Institute, 19 January 2022. Literature review. https://reutersinstitute.politics.ox.ac.uk/echo-chambers-filter-bubbles-and-polarisation-literature-review
- "A filter bubble, on the other hand, is an echo chamber primarily produced by ranking algorithms" (SV) "engaged in passive personalisation without any active choice on our part" (SP).
- Algorithmic selection "generally lead to slightly more diverse news use – the opposite of what the 'filter bubble' hypothesis posits" (SV).
- "We are not aware of any comparable studies that have found support for the filter bubble hypothesis" (SV).
- Reliance on search and social media "is in most cases associated with more diverse news use" (SV).
- "self-selection, primarily among a small minority of highly partisan individuals" (SV).

Zuiderveen Borgesius et al. 2016, Internet Policy Review 5(1), DOI 10.14763/2016.1.401. https://policyreview.info/articles/analysis/should-we-worry-about-filter-bubbles
- Abstract: "at present there is little empirical evidence that warrants any worries about filter bubbles" (SV).
- Conclusion: "at present, there is no empirical evidence that warrants any strong worries about filter bubbles" (SV).
- The two wordings differ ("little … any worries" against "no … strong worries"); cite whichever you mean.
- Caveat (SP): "if personalisation technology improves, and personalised news content becomes people's main information source, problems for our democracy could indeed arise".

Bruns 2019. The book was not reached; I read his article of the same argument, "Filter bubble", Internet Policy Review 8(4), DOI 10.14763/2019.4.1426 (metadata SP). https://policyreview.info/concepts/filter-bubble
- The concept "remains vague and founded in anecdotes" (SV).
- An echo chamber "emerges when a group of participants choose to preferentially connect with each other, to the exclusion of outsiders" (SV).
- A filter bubble "emerges when a group of participants choose to preferentially communicate with each other, to the exclusion of outsiders" (SV).
- "moral panic" is present (SV). "the dumbest metaphor of the Internet" (SV) is Bruns quoting Sebastian Meineck.
- SP: "Yet, there is scant empirical evidence for their existence".

Kotkov, Wang & Veijalainen 2016: the survey itself was UNREACHABLE. Substitute: Kotkov's 2018 dissertation, "Serendipity in recommender systems" (Jyväskylä Studies in Computing 281, ISBN 978-951-39-7438-1), which includes the survey as its Paper I. https://jyx.jyu.fi/bitstreams/15d94718-9cc8-40b4-80f4-8b67ec09c1a2/download
These are the dissertation's sentences; do not attribute them word for word to the 2016 article.
- "serendipitous items are relevant, novel and unexpected" (SV).
- "There is no consensus on definition of serendipity in recommender systems" (SV).
- "there is no agreement on the evaluation metric to measure serendipity in recommender systems" (SV).
- User study on MovieLens: "475 users" (SV); "up to 8.5% are serendipitous according to at least one variation" (SV).

Ziarani & Ravanmehr 2021, J. Computer Science and Technology 36:375–396. ABSTRACT, SP: "The over-emphasis on the accuracy of the recommendations can cause information over-specialization and make recommendations boring and even predictable." The number of papers reviewed is not in the abstract.

Experiment on novelty and acceptance: Ekstrand, Harper, Willemsen & Konstan 2014 (RecSys). https://md.ekstrandom.net/pubs/listcmp.pdf
- "582 users completed the study over 81 days" (SV).
- "We find that satisfaction is negatively dependent on novelty and positively dependent on diversity in this setting" (SV).
- "Too many unfamiliar recommendations may give users a poor impression of a particular recommender" (SV).
Role: the evidence is against assuming "adjacent or novel" is welcomed; diversity helped and novelty hurt, in one film setting.

Ge et al. 2010 and Castells, Hurley & Vargas: UNREACHABLE.

---------------------------------------------------------------
D4. MATCHING TOOLS — METHOD AND SCREEN ONLY

(a) Teleport. The Internet Archive is blocked. teleport.org's root still returns an early beta page:
- "tell us what qualities of life matter to you the most" (SV).
- "Results of your search are sorted by how well they match your criteria" (SV).
So there is an ordering, but it is a per-user match ordering. The later Teleport Cities decomposed score, any global rank, and whether weightings were stored could NOT be verified (teleport.org/cities is robots-disallowed).

(b) Discover Uni (UK funding and regulatory bodies including the Office for Students; SP).
- https://discoveruni.gov.uk/how-to/ : "You can choose up to seven to view side by side" (SV). Courses are saved, then compared. The compare screen is script-rendered and I could not see it.
- https://discoveruni.gov.uk/about-our-data/ : "It's important that you don't make decisions based on small differences between courses" (SV); "Instead look for large differences, and particularly where figures are much lower than for other courses you are considering" (SV).
- https://discoveruni.gov.uk/about-our-data/guidance-comparing-courses/ : "These students may or may not be similar to you" (SV); "a useful part of the picture, but not the whole" (SV).
- https://discoveruni.gov.uk/how-do-i-choose-course/rankings-and-other-information/ : "League tables can seem like an easy way of finding the best places to study" (SV); "some may weight the things that are important to you more highly than others" (SV); "It is worth checking what they use and what is given greatest importance when arriving at the final scoring" (SV).
- I found NO sentence on any of these pages saying Discover Uni "is not a league table". The no-ranking is by construction (a user-chosen set of up to seven), not by declaration. No global ordering was seen.

(c) ONS Explore Local Statistics. QMI, last revised 25 April 2025: https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/methodologies/explorelocalstatisticsserviceqmi
- "The first chart is an interactive beeswarm chart, which shows individual data points spread out to avoid overlapping" (SV).
- "The median line shows the median across all areas for each year" (SV).
- The comparison is put in words, not ranks. "This text helps distinguish between small differences that might be because of uncertainty in the statistics" (SV). Rule: the text says "higher" if the area "is 1 or more median absolute deviations above the comparison value" (SV); "similar" if "within 1 median absolute deviations of each other" (SV).
- Similar areas: "create an ordered list of the 20 most similar areas to the area of interest, ordered by Euclidean distance" (SV).
- Confidence intervals can be shown from the chart options (SV).
- Indicators-page controls (SP): "Distribution chart" or "Line chart", "Show confidence intervals", "Change areas".
- No national rank is shown; the reader found no use of "rank" for areas. The only ordered list is nearness to the chosen area.

(d) Understanding Scottish Places. https://www.usp.scot/StaticPage/AboutContact and /StaticPage/Methodology
- "It supports practitioners to understand how places across Scotland are similar" (SV).
- "USP will generate comparisons on each indicator against other comparable or local towns" (SV).
- SP: 508 towns; a six-type typology by K-means on 2022 Census data; a seven-point scale from Independent to Dependent. The reader gave two different population thresholds, so that is unverified.
- No no-ranking statement found. The type labels are themselves evaluative (for example "Least Privileged towns", "Affluent towns"; SP).

(f) Others with an explicit method page:
- Numbeo. https://www.numbeo.com/quality-of-life/indices_explained.jsp : "The index is calculated using an empirical formula that assigns weights to each factor based on its importance" (SV); "Our formulas have changed in the past; different formulas were used before December 2017" (SV). It is a global ordering with fixed weights, no user weighting, components listed. It is the ranking counter-case.
- CHE University Ranking (Germany). https://www.che.de/en/ranking-germany/ : "Rather than giving HEIs an individual ranking position, the CHE University Ranking assigns them to one of three ranking groups: a top group, a middle group or an end group" (SV); "no overall value is derived from weighted individual indicators" (SV, lower-case n). Reason: "a situation is avoided in which minor differences in the nominal value of an indicator are misinterpreted as differences in performance and quality" (SV).
- The Guardian and Economist tools were not attempted.

---------------------------------------------------------------
D5. "ABSENCE MADE VISIBLE" AS AN OFFICIAL METHOD

360Giving. https://www.360giving.org/explore/using-360giving-data-as-a-funder/
- Under the heading "Compare funding": "Find gaps, overlaps or chances to work with others" (SV).
- "360Giving data shows who is funding what, where and when" (SV); "Spot funders working on the same issues or in the same places" (SV).
- 360Insights (https://insights.threesixtygiving.org/): "Combine and visualise 360Giving, charity and location data to see an overview of grants" (SV).
- No caveat on those pages that a gap may be a publishing gap rather than a funding gap.

Arts Council England, "Methodology for identifying priority places", September 2021. Official practice. https://www.artscouncil.org.uk/media/18175/download?attachment
- Need indicators and weights (confirmed on a second pass, not string-level): Arts Council investment per head, 2017/18–2019/20 average (1.5); Active Lives engagement (1.5); Indices of Deprivation 2019 (1); British Red Cross Covid vulnerability index (1); a children and young people composite (1); ethnicity, 2011 Census (1); disability, 2011 Census (1).
- Engagement measure: "any arts or museum engagement, three or more times in past 12 months" (SV).
- Standardised within each Arts Council area: "The same number in the raw data could translate into a different need score in different areas" (SV); "priority places have been selected by comparison with other places in their area, not other places nationally" (SV).
- High need means "above the mid-point of the range of need scores in the area" (SV).
- Opportunity is "factors that make it likely we would be able to increase investment and staff resource in a place" (SV), judged by staff: "Scores were arrived at by area teams giving each place a score between 1 and 5" (SV) on ambition, capacity and timing.
- "Need and opportunity scores were not designed to be added together" (SV).
- "Balancing is a process that considers the portfolio of priority places within an area as a whole" (SV). "Medium need places could only be selected as a priority place if their selection was critical to address one or more of the balancing criteria" (SV).
- "Each of our five Arts Council areas identified up to 15 priority places" (SV); 54 in total.
- "Cold spots" does NOT appear in the document.

Levelling Up for Culture Places. https://www.artscouncil.org.uk/LUCPs
- "We've worked with the Department for Digital, Culture, Media and Sport (DCMS) to identify 109 local authority areas" (SP sentence; 109 SV).
- "The 53 local authority areas that are within the 49 existing Priority Places that are outside of London" (SV) plus "A further 56 local authority areas outside of London that have the highest need" (SV).

Published criticism of the method: NONE FOUND without search. The DCMS Committee report "Reimagining where we live" (2 November 2022; https://publications.parliament.uk/pa/cm5803/cmselect/cmcumeds/155/report.html) mentions the 54 priority places but, in the text I read, does not criticise the selection method. Its "cold spots" (para 72, in quotation marks) are social mobility cold spots: organisations wrote that they worked in such places, "primarily rural or coastal areas and areas with high levels of pre-existing inequality and deprivation or limited established cultural infrastructure" (SV). The term there is not Arts Council's.

DCMS Participation Survey 2023/24 technical report. https://www.gov.uk/government/statistics/participation-survey-2023-24-annual-publication/participation-survey-2023-to-2024-annual-technical-report
- "was commissioned by DCMS in partnership with Arts Council England (ACE)" (SV).
- "182,318 respondents completed the survey" (SV).
- "The design sought a minimum four-quarter respondent sample size of 500 in each local authority area" (SV).

Creative People and Places (SP): it "focuses on parts of the country where involvement in creativity and culture is significantly below the national average."

Warwick Commission 2015 "8%" sentence: UNREACHABLE (three report URLs 404; Guardian blocked). Version 1's wording stays UNVERIFIED; nothing quoted. Centre for Cultural Value and Gilmore 2013 were also not reached.

---------------------------------------------------------------
D6. OPT-IN DIRECTORIES — MECHANISMS ONLY

Everywhere Is Queer. https://www.everywhereisqueer.com/
- "We do ask that the person filling out the application is the owner of the organization" (SV).
- "our resource is listing only queer-owned organizations at this time" (SV).
- "It's free, takes about 5 minutes" (SV).
- No safety reasoning is stated on the page; owner-only submission is a rule without a published rationale.

Safe Space Alliance. https://safespacealliance.com/add-listing/
- "Submit your space for verification and approval" (SV).
- "Once verified and approved, your space is listed on the Safe Space Alliance online directory" (SV).
- "Please allow up to 5 working days for verification and approval" (SV).
- No definition, rationale or removal rule on that page; the FAQ URL returned 404.

Ask for Angela. https://askforangela.co.uk/ (mechanism only; no venues read)
- The pledge is "a free, simple way for businesses to formally show their commitment to operating the scheme" (SV).
- "Once you have signed the Pledge you will be added to the Ask for Angela map" (SV).

In all three, the listed party applies. None publishes a safety rationale for that rule on the pages read.

---------------------------------------------------------------
D7. CHARTS IN CIRCULATION

Lee, Yang, Inchoco, Jones & Satyanarayan 2021 (CHI). https://arxiv.org/pdf/2101.07993
- Corpus: "close to half a million tweets" (SV); "over 41,000 images" through a computer-vision model (SV); 21 January–31 July 2020 (SP). Ethnography: "followed five Facebook groups" (SV) for six months.
- "anti-mask groups practice a form of data literacy in spades" (SV).
- "unorthodox viewpoints do not result from a deficiency of data literacy" (SV).
- They "use orthodox methods to make unorthodox arguments" (SV).
- They "post screenshots of graphs" from mainstream outlets for critique (SV).
- Visualisations "are a battleground that highlight the contested role of expertise in modern American life" (SV).
- SP: "anti-maskers often create polished counter-visualizations that would not be out of place in scientific papers".

Lisnic, Polychronis, Lex & Kogan 2023 (CHI). https://sci.utah.edu/~vdl/papers/2023_chi_misleading.pdf
- Corpus: "2.2 billion tweets" collected (SV), filtered to "9,958" coded posts with visualisations (SV).
- "only 12% of all posts contain data visualizations that violate common visualization design guidelines" (SV).
- "the majority (55.3%) being screenshots of existing charts" (SV on the figure and phrase).
- "more than 40% of all COVID-skeptic charts in the COVID-19 discourse on Twitter are screenshots of data exploration dashboards" (SP; the phrase "screenshots of data exploration dashboards" is SV).
- Abstract: "even faithfully plotted data visualizations can be used to support misinformation online" (SV).
- "the designer should also anticipate how a biased viewer may use and misuse the chart" (SV).
- On a chart's caveat note (SP): "This note is not a prominent feature of the chart and is not reflected in the visual design of the case curve."
- Reasoning-error shares (all SP): causal inference 6.9% of all posts, cherry-picking 5.2%, arbitrary threshold 4.5%, incorrect reading 0.1%; design violations were dual axes 5.4% and truncated axes 1.2%.

Lo, Gupta, Shigyo, Wu, Bertini & Qu 2022 (EuroVis). Author list confirmed. https://arxiv.org/pdf/2204.09548
- "a total number of 129,125 images" collected (SV); "1,979 images" were candidate visualisations (SV); 1,143 were tagged with issues (SV on the number).
- "74 different types of issues" (SV) in "a taxonomy of 12 categories" (SV).
- "we can locate the frequently discussed issues of Truncated Axis (1st), 3D (2nd)" (SV); the sentence continues with Dual-axis (4th) and Area Encoding (12th) (SP).
- "Missing Title" is an issue (SV) under "Incomplete Chart". Its rank as 3rd came from the reader's reading of a figure and is NOT text-verified.
- "Selective Data" (SV) is the cherry-picking issue; rank about 10th, unverified.
- There is NO "cropping" issue and no "missing source" issue. The nearest is "Dubious Data" (SP).

Pandey, Rall, Satterthwaite, Nov & Bertini 2015 (CHI): ABSTRACT only (SSRN 2566968). A crowdsourced experiment on four distortion techniques; n NOT verified; nothing quoted.

How charts are shared stripped of context: the best evidence is Lisnic 2023's 55.3% screenshots figure, plus Lisnic, Cutler, Kogan & Lex 2025 (see Unasked 1). No dedicated study of caption-stripping was found without search.

---------------------------------------------------------------
D8. GUIDANCE ON CHARTS THAT TRAVEL

Analysis Function, "Data visualisation: charts". Official standard. https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/
- "All charts need at least one title, but it is considered best practice to give them two" (SV).
- "The statistical subtitle should say what the data is, the geography the data relates to and the time period shown" (SV).
- Under "Placement of the title": "titles should be in the body of the page or document, as opposed to within the image" (SV).
- "This is because images of text are difficult to read for some people and should only be used when essential" (SV).
- "This does mean the image of the chart can be taken out of context if it is copied and pasted elsewhere" (SV).
- SP, the next sentences: "But, while putting the title within the image may make it harder to take a chart out of context, it does not stop it completely as titles can be cropped out. Therefore, we prioritise accessibility and advise for the title and subtitle to be in the body text."
- Source: "You should give the specific data source for each chart and link directly to it if you can" (SV); "this text should be in the body text of the page and not part of the chart image" (SV).
- No section on charts for social media was found.

GOV.UK publishing guidance, "Images". https://guidance.publishing.service.gov.uk/formatting-content/images/
- "Avoid using images with text" (SV).
- "Do not use the image to convey information without also explaining it in the text of your content" (SV).
- "If you do use an infographic you should provide a plain text version of the content" (SV).
- SP: "All charts should have two titles - a headline title and a statistical title."

ONS service manual, chart text. https://service-manual.ons.gov.uk/data-visualisation/guidance/chart-text
- Title "15 words or fewer" (SV).
- "Use the chart subtitle to provide a specific description of the data used in the chart" (SV).
- "Each chart must include the source of the data directly after the chart" (SV), that is, after it and not in it.
- Nothing on image download, embedding or sharing.

Our World in Data.
- FAQ (https://ourworldindata.org/faqs): the embed code "will adapt to the selections that you make on the chart" (SV); a choice of "a live embed that always reflects our latest data updates" (SV) or "an archived embed that will never change or update" (SV); "You do not need permission from us" (SV); "cite the page that it's found on" (SV). SP: "you must credit both Our World in Data and the underlying third-party data provider".
- A live chart page (https://ourworldindata.org/grapher/life-expectancy; furniture only): title, subtitle, a source line ending "with major processing by Our World in Data" (SV), "Creative Commons BY license" (SV). Its "How to cite" blocks give a retrieval date and an archive.ourworldindata.org URL with an archive date (SP).
- Whether the downloaded PNG itself carries title, source and licence is not stated on either page; I could not inspect the image.
- Chart API docs (https://docs.owid.io/projects/etl/api/chart-api/): image presets include "uncaptioned" (SV), with "Minimal mode (1 to enable). Affects thumbnails and uncaptioned images" (SV).

Government Communication Service: the old social-media guidance URL is 404 and the accessible-communications URL redirects to a link list with no rule on text in images. UK coronavirus dashboard: archives blocked; not verified.

Answer to the question: I found NO official minimum for what a shared chart image must carry. UK official guidance points the other way: title, subtitle and source go in the page text beside the image, for accessibility, and the Analysis Function says in terms that this lets the image be taken out of context.

---------------------------------------------------------------
D9. PRESS USE OF RANKINGS AND WORDING GUIDANCE

World Bank, 16 September 2021. https://www.worldbank.org/en/news/statement/2021/09/16/world-bank-group-to-discontinue-doing-business-report
- "Trust in the research of the World Bank Group is vital" (SV).
- "World Bank Group management has taken the decision to discontinue the Doing Business report" (SV).
- "Going forward, we will be working on a new approach to assessing the business and investment climate" (SV).
- SP: "After data irregularities on Doing Business 2018 and 2020 were reported internally in June 2020".

English Indices of Deprivation 2019 (wording side).
FAQ: https://assets.publishing.service.gov.uk/media/5dfb3d7ce5274a3432700cf3/IoD2019_FAQ_v4.pdf
- The measure "can tell you if one area is more deprived than another but not by how much" (SV, Q19).
- "a small area with a rank of 1,000 is not half as deprived as a place with a rank of 500" (SV).
- "The Index is not a suitable tool for targeting individuals" (SV).
- "there is no single summary measure that is the 'best' measure" (SV, Q13).
- "The IoD2019 ranks every neighbourhood in England from 1 (most deprived area) to 32,844 (least deprived area)" (SV).
- Describing deciles: the FAQ says "among the most deprived 10 per cent" (the reader corrected my "amongst"; treat as SP).
- The FAQ has no "which is the most deprived area" question.
Statistical Release: https://assets.publishing.service.gov.uk/media/5d8e26f6ed915d5570c6cc55/IoD2019_Statistical_Release.pdf
- "Many non-deprived people live in deprived areas, and many deprived people live in non-deprived areas" (SV).
- "so a neighbourhood ranked 100th is more deprived then a neighbourhood ranked 200th, but this does not mean it is twice as deprived" (SV, typo "then" in the original).
- The summary measures "each lead to a different ranking of areas" (SV).
- Areas "can be referred to as the 'most deprived' or as being 'highly deprived' to aid interpretation" (SV), so the superlative is officially licensed.
For Agent A: an Indices of Deprivation 2025 page exists, dated 30 October 2025 (SP), with a new FAQ (33,755 neighbourhoods; "less directly comparable to previous Indices"; SP). https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025

Published analysis of how local press report deprivation ranks: NONE FOUND without search.

ONS caution against ranking. "Personal well-being in the UK QMI", last revised 14 January 2025. https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/methodologies/personalwellbeingintheukqmi
- "simply ranking local authorities by their numerical scores can be misleading for several reasons, including sample sizes and mode effects" (SV).
- "The most appropriate comparisons to make are progress over time within the same local authority, or across local authorities that share a similar demographic composition to one another" (SV).
ONS Health Index: I found NO caution against ranking in the bulletin or the methods page (SP on both). The phrase "should not be used to rank" was not found anywhere.

Hazelkorn: only her 2009 article was reachable (https://arrow.tudublin.ie/cgi/viewcontent.cgi?article=1001&context=cserart). It has no sentence on media simplifying rankings. The nearest (SP): guides "were usually produced by media organisations or independent agencies". Her books were not reachable. No Hazelkorn sentence on media simplification can be cited from this pass.

"Share this view" carrying filters and data version: only OWID was confirmed (above). UKHSA dashboard pages say only that data downloads come as ".csv and .json" (SP). Fingertips gives a citation format (SP). Eurostat help URL 404. Statistics Canada not attempted.

---------------------------------------------------------------
UNASKED THREADS

1. Lisnic, Cutler, Kogan & Lex 2025 (CHI), "Visualization Guardrails". https://sci.utah.edu/~vdl/papers/2025_chi_guardrails.pdf . The one study I found that designs for the crop.
   - Guardrails "automatically show the contextual data that expose cherry-picking" (SV).
   - Design goal, tamper-evidence: "it should be difficult to get rid of the guardrail, for instance by cropping a screenshot" (SV).
   - "Juxtaposed approaches are croppable and thus not tamper-evident" (SV).
   - Three experiments: "130 participants", "160 participants", "675 participants" (each SV).
   - "Superimposed Primary Data guardrail was the most effective against cherry-picking" (SV).
   - Limit: "38% of participants did not notice them, and 23% noticed them but did not understand their meaning" (SV).
   - SP: earlier work "showed that most of misleading charts shared on Twitter were screenshots using various levels of cropping."
2. The Analysis Function names the trade-off itself (D8): accessibility is put ahead of resistance to decontextualisation, and it notes titles in images "can be cropped out".
3. OWID's image API offers an "uncaptioned" preset (D8), so the publisher itself issues the stripped image.
4. ONS Explore Local Statistics turns a comparison into three words by a published rule, one median absolute deviation (D4c). It is a worded alternative to rank.
5. Berlin Principles on Ranking of Higher Education Institutions, Berlin, 20 May 2006, 16 principles (SP on count). https://www.che.de/downloads/Berlin_Principles_IREG_534.pdf
   - Principle 15: "Provide consumers with a clear understanding of all of the factors used to develop a ranking, and offer them a choice in how rankings are displayed" (SV); users "have some opportunity to make their own decisions about how these indicators should be weighted" (SV).
   - Principle 6: "Be transparent regarding the methodology used for creating the rankings" (SV).
6. CHE's three groups with no overall value, and its stated reason (D4f): an official-grade precedent for refusing rank positions.
7. The Arts Council "absence" method is two-stage and partly discretionary (D5): a weighted need score relative to the region, then staff-scored opportunity, then "balancing". The published method does not make a place's selection reproducible from data alone.
8. Novelty lowered satisfaction while diversity raised it (Ekstrand et al. 2014, D3); and ONS's well-being guidance recommends demographic peers over ranks (D9).

LEFT OUT, AND WHY
- Kunkel et al. 2019; Ge et al. 2010; Castells et al.; the Kotkov 2016 article text; Pandey et al. full text; Tintarev & Masthoff 2012 full text: publisher blocks. Their n are unverified.
- Warwick Commission 2015: report PDF not found at three URLs.
- Teleport's later product, the UK coronavirus dashboard, anything needing the Internet Archive: blocked.
- Bruns's book; Hazelkorn's books; Gilmore 2013; Centre for Cultural Value: not reachable.
- Press analyses of deprivation headlines; criticism of the Priority Places method; Guardian and Economist tools; Eurostat and Statistics Canada share features: need search.
- No findings about any place were read or reported. One country-level ONS page was opened for screen layout only.

RICH REFERENCES
1. Lisnic et al. 2023 together with Lisnic et al. 2025: the measured problem (55.3% screenshots; 12% design violations) and the tested response (tamper-evident guardrails, with their noticing limits).
2. Herlocker et al. 2000 read beside Bilgic & Mooney: the exact line between explanations that persuade and explanations that help someone judge.
3. Arts Council England, "Methodology for identifying priority places" (September 2021): a fully published official method for naming where provision is low, including where judgement enters.

SURPRISED
- Version 1's "86%" is 86% of 97 exit-survey respondents about the interface they had just used, and the same paper found no measurable gain in decision performance.
- UK official guidance tells producers to keep title and source OUT of the chart image, and says outright that this lets the image travel without them.
- OWID publishes an "uncaptioned" image preset.
- "Cold spots" does not appear in the Arts Council method, and in the Select Committee report it means social mobility cold spots.
- Zuiderveen Borgesius et al. word their conclusion two ways ("little … any worries" in the abstract; "no … strong worries" in the conclusion).
- Discover Uni never says it is not a league table on the pages I read.
- The ONS Health Index pages carry no caution against ranking; the explicit ONS caution is in the personal well-being QMI.
- Lo et al.'s 74-issue taxonomy has "Missing Title" but no issue for cropping or missing source.