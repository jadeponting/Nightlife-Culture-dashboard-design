# Chapter 10 — agent returns, kept whole

*Four research agents, dispatched in parallel on 6 October 2026 after Entry 10 was framed. Kept verbatim as working notes; every quotation used in the chapter was re-read at source or marked. No web search was available to any agent.*

## Agent A — Disclosure control and re-identification

CHAPTER 10 RESEARCH REPORT — FACET: DISCLOSURE CONTROL AND RE-IDENTIFICATION
Fetched 6 October 2026.

TOOLS AND METHOD
- WebSearch was unavailable (turn budget exhausted). I worked from direct URLs with WebFetch only. curl from the shell was refused by the egress proxy (403), so no local text grep was possible.
- Every quotation marked [SV] (STRING-VERIFIED) passed a second YES/NO presence fetch; most checks carried a false control string, and all controls came back NO. [SP] = SINGLE PASS. Where the checker corrected my candidate, I give the corrected wording and mark it [SP].
- Pages the fetch proxy refused with HTTP 429 (rate limit), not retried:
  - Europe PMC DOI lookups for Kenny et al. and for Curtis et al.
  - Springer: the Floridi 2014 article page and its PDF.
  - Springer: Int J Health Geographics 5:44 and 5:56.
- Blocked or erroring at source: nytimes.com, theguardian.com, bbc.co.uk (site blocked); science.org, pnas.org, dl.acm.org, nejm.org, unece.org, philpapers archive (403); PMC (reCAPTCHA on two of three tries); www2.census.gov PDFs (robots.txt).

ITEM 1 — THE SYNTACTIC METHODS

Sweeney 2002, "k-Anonymity: A Model for Protecting Privacy", Int J Uncertainty, Fuzziness and Knowledge-Based Systems 10(5):557–570. https://dataprivacylab.org/dataprivacy/projects/kanonymity/kanonymity.pdf. Peer-reviewed; foundational.
- Abstract: "A release provides k-anonymity protection if the information for each person contained in the release cannot be distinguished from at least k-1 individuals whose information also appears in the release." [SV]
- Definition 3: "RT is said to satisfy k-anonymity if and only if each sequence of values in RT[QIRT] appears with at least k occurrences in RT[QIRT]" [SV; subscripts flattened by the reader]
- Weld: "six people had his particular birth date; only three of them were men; and, he was the only one in his 5-digit ZIP code" [SV]. "For twenty dollars I purchased the voter registration list for Cambridge Massachusetts and received the information on two diskettes" [fragment "purchased the voter registration list for Cambridge Massachusetts" SV; rest SP].
- The 87% sentence appears here too, citing her own ref [1], with a footnote marker after "ZIP" [SV].
- Its own limits: "This paper also examines re-identification attacks that can be realized on releases that adhere to k-anonymity unless accompanying policies are respected." [SV]. Section 4 names three attacks: unsorted matching, complementary release, temporal [SP].
- Guarantees: each record is indistinguishable from k-1 others on the chosen quasi-identifiers (protection against linking). Does not promise anything about the sensitive value itself.

Sweeney 2000, "Simple Demographics Often Identify People Uniquely", Carnegie Mellon Data Privacy Working Paper 3. https://dataprivacylab.org/projects/identifiability/paper1.pdf. Working paper, not peer-reviewed.
- "It was found that 87% (216 million of 248 million) of the population in the United States had reported characteristics that likely made them unique" … "based only on {5-digit ZIP, gender, date of birth}" [SV]
- Basis: "I report on experiments I conducted using 1990 U.S. Census summary data" [SV]. It is an estimate from 1990 summary counts ("likely made them unique"), not a count of actual re-identifications.
- "132 million of 248 million or 53%" for {place, gender, date of birth} [SV]. County level: "are likely to uniquely identify 18% of the U.S. population" [SP; the checker returned the sentence but answered NO to the fragment].
- "Clearly, data released containing such information about these individuals should not be considered anonymous" [SV]

Machanavajjhala, Kifer, Gehrke & Venkitasubramaniam, "ℓ-Diversity: Privacy Beyond k-Anonymity". Authors' journal preprint at https://www.cs.rochester.edu/u/muthuv/ldiversity-TKDD.pdf (header reads "ACM Journal Name, Vol. V, No. N"; TKDD volume and year not confirmable, dl.acm.org 403; the Cornell copy returned 401).
- "In this paper we show using two simple attacks that a k-anonymized dataset has some subtle, but severe privacy problems." [SV]
- "First, an attacker can discover the values of sensitive attributes when there is little diversity in those sensitive attributes. This is a known problem." [SP, corrected wording]
- "Second, attackers often have background knowledge, and we show that k-anonymity does not guarantee privacy against attackers using background knowledge." [SV]
- "Observation 1. k-Anonymity can create groups that leak information due to lack of diversity in the sensitive attribute." / "Observation 2. k-Anonymity does not protect against attacks based on background knowledge." [SV, present with the "Observation n." prefix]
- Examples: "so Alice concludes that Bob has cancer" [SV]; "Therefore Alice concludes with near certainty that Umeko has a viral infection" [SV]
- Principle: "A q⋆-block is ℓ-diverse if contains at least ℓ "well-represented" values for the sensitive attribute S." [SV; "if contains" is sic]

Li, Li & Venkatasubramanian, "t-Closeness: Privacy Beyond k-Anonymity and ℓ-Diversity". https://www.cs.purdue.edu/homes/ninghui/papers/t_closeness_icde07.pdf (ICDE 2007 per the filename; venue not printed on the PDF).
- "Recently, several authors have recognized that k-anonymity cannot prevent attribute disclosure" [SV]
- On ℓ-diversity: "In particular, it is neither necessary nor sufficient to prevent attribute disclosure" [SV]
- Skewness attack: "When the overall distribution is skewed, satisfying ℓ-diversity does not prevent attribute disclosure." [SV]
- Similarity attack: "When the sensitive attribute values in an equivalence class are distinct but semantically similar, an adversary can learn important information" [SV]
- Definition: "An equivalence class is said to have t-closeness if the distance between the distribution of a sensitive attribute in this class and the distribution of the attribute in the whole table is no more than a threshold t" [SV]
- Cost and limit, in their words: "Of course, requiring that P and Q to be close would also limit the amount of useful information that is released" [SP]; "We note that t-closeness protects against attribute disclosure, but does not deal with identity disclosure." [SP]

Role: the ladder k → ℓ → t. Each fixes the previous attack by removing more information, and none addresses repeated queries or a group that is uniform on the sensitive value.

ITEM 2 — DIFFERENTIAL PRIVACY

Dwork 2006, "Differential Privacy". https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/dwork.pdf (ICALP venue not printed on the PDF).
- Abstract: "captures the increased risk to one's privacy incurred by participating in a database" [SV]; Dalenius's goal "cannot be achieved" [SV]; "Contrary to intuition, a variant of the result threatens the privacy even of someone not in the database" [SV]
- "A randomized function K gives ε-differential privacy if for all data sets D1 and D2 differing on at most one element" [SV]
- Promise: "even if the participant removed her data from the data set, no outputs (and thus consequences of outputs) would become significantly more or less likely" [SV]
- Non-promise: "Note that a bad disclosure can still occur, but our guarantee assures the individual that it will not be the presence of her data that causes it" [SV]

Dwork & Roth 2014, The Algorithmic Foundations of Differential Privacy. https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf
- "Differential privacy describes a promise, made by a data holder, or curator, to a data subject" [SV]: "You will not be affected, adversely or otherwise, by allowing your data to be used in any study or analysis, no matter what other studies, data sets, or information sources, are available" [SV]
- "Differential privacy addresses the paradox of learning nothing about an individual while learning useful information about a population" [SV]
- What it does not promise: "A medical database may teach us that smoking causes cancer, affecting an insurance company's view of a smoker's long-term medical costs" [SV]; "Has the smoker been harmed by the analysis?" [SV]; "It is the conclusions reached in the study that affect the smoker, not his presence or absence in the data set" [SV]. Also "differential privacy does not guarantee that what one believes to be one's secrets will remain secret" [SP].
- "overly accurate answers to too many questions will destroy privacy in a spectacular way" [SV]
- "Differential privacy is a definition, not an algorithm" [SV]
- Composition and budget: "the composition of two (ε, 0)-differentially private mechanisms is (2ε, 0)-differentially private" and "the epsilons and the deltas add up" [SP]. "Perhaps most crucially, the quantification of loss also permits the analysis and control of cumulative privacy loss over multiple computations." [SP]. The phrase "privacy budget" occurs in the text [SP].
- Groups: "Any (ε, 0)-differentially private mechanism M is (kε, 0)-differentially private for groups of size k" [SV]. The guarantee weakens linearly with group size.
- Role: DP protects a person's participation, not what a statistic reveals about a group. The smoker passage is the authors' own statement of that.

US Census 2020
- Why. Abowd, Census "Research Matters" blog, 17 Aug 2018, https://www.census.gov/newsroom/blogs/research-matters/2018/08/protecting_the_confi.html: "historical methods cannot completely defend against the threats posed by today's technology" [SV]; "Growth in computing power, advances in mathematics, and easy access to large, public databases" [SV].
- Abowd KDD '18 abstract (Cornell eCommons record, https://ecommons.cornell.edu/handle/1813/60392): "The U.S. Census Bureau announced, via its Scientific Advisory Committee, that it would protect the publications of the 2018 End-to-End Census Test (E2E) using differential privacy" [SV]. Only that abstract was reachable.
- Budget. Census press release CB21-CN.42, June 9 2021, https://www.census.gov/newsroom/press-releases/2021/2020-census-key-parameters.html: "total privacy-loss budget for the redistricting data product" … "of ε=19.61, which includes ε=17.14 for the persons file and ε=2.47 for the housing unit data" [SV]. Set by the "Data Stewardship Executive Policy Committee (DSEP)" [SV]. "The chosen global privacy-loss budget of ε= 19.61 is exponentially higher than the ε= 12.2 budget used in the April 2021 demonstration data." [SP]. Extra budget went to race and ethnicity queries [SP].
- TopDown in one sentence. Abowd et al., "The 2020 Census Disclosure Avoidance System TopDown Algorithm", arXiv 2204.08986 (same abstract at https://hdsr.mitpress.mit.edu/pub/7evz361i): "The algorithm then creates noisy versions of key queries on the data, referred to as measurements, using zero-Concentrated Differential Privacy" [SV]. Invariants are "statistics that the Census Bureau has determined, as matter of policy, to exclude from the privacy-loss accounting" [SP]. On sparse areas: "For well-populated geographies this answer will be useful; however, for sparsely populated geographies it will not be reliable." [SP]
- Bureau statement on small populations. "Developing the DAS" page (last revised 6 Aug 2026), https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/process/disclosure-avoidance/2020-das-development.html: "We encourage data users to aggregate small populations and geographies to improve accuracy and diminish implausible results" [SV]; "Noisy Measurement Files are the intermediate output of the Disclosure Avoidance System's TopDown Algorithm (TDA)" [SV].
- Abowd & Hawes, "Confidentiality Protection in the 2020 US Census of Population and Housing" (arXiv 2206.03524; preprint dated 27 Dec 2022, forthcoming in Annual Review of Statistics and Its Application): the budget in zCDP units is "ρ = 2.56" for person tables and "ρ = 0.07" for housing units [SV]; no ε equivalent is given there. "The top-down approach allocates PLB strategically such that data for individual blocks (where disclosure risk is often greatest) remain relatively noisy." [SP]

The controversy — small areas and small groups only
- Ruggles, Fitch, Magnuson & Schroeder 2019, AEA Papers and Proceedings 109:403–408, https://users.pop.umn.edu/~ruggles/Articles/Privacy.pdf (published version). "Differential privacy goes far beyond what is necessary to keep data safe under census law and precedent" [SV]; "represents a radical departure from established Census Bureau confidentiality laws and precedents" [SV]; "Reconstructing microdata from tabular data does not by itself allow identification of respondents" [SV]; "It may be impossible to create a differentially-private version of the ACS tables that would meet the needs of researchers and planners." [SP, corrected]
- Kenny, Kuriwaki, McCartan, Rosenman, Simko & Imai 2021, Science Advances 7(41) eabk3283; text at https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/. "We find that the DAS systematically undercounts the population in mixed-race and mixed-partisan precincts, yielding unpredictable racial and partisan biases" [SV]; "it does not prevent accurate predictions of an individual's race and ethnicity" [SV]; "census statistics must be postprocessed after noise injection to be usable" [SV]. Body: "mixed White/non-White precincts lose the most population relative to more homogeneous precincts" [SP]; on the final ε=19.61 data, "we observe the same pattern of bias as before, albeit around half the magnitude" [SP].
- Santos-Lozada, Howard & Verdery 2020, PNAS 117(24):13405–13412. ABSTRACT only, [SP], from the Europe PMC record: "differential privacy will more strongly affect mortality rate estimates for non-Hispanic blacks and Hispanics than estimates for non-Hispanic whites"; "significant changes in estimated mortality rates for less populous areas, with more pronounced changes when stratified by race/ethnicity". It tested the then-proposed algorithm, not the final settings.
- boyd & Sarathy 2022, Harvard Data Science Review, https://hdsr.mitpress.mit.edu/pub/3vj5j6i0 (issue and date not shown on the page). "this transformation exposed the statistical illusions and limitations of census data, weakening stakeholders' trust in the data and in the Census Bureau itself" [SV]; "a battle over uncertainty, trust, and legitimacy of the census" [SV]; "the root of the controversy is epistemic in nature" [SV]; "Data users did not want the government to intentionally introduce uncertainty for the sake of confidentiality; they wanted access to the bureau's ground truth." [SP]
- Role: the US case shows the cost of formal privacy lands on small areas and mixed or minority populations, and that the argument was about trust as much as mathematics.

ITEM 3 — THE UK CENSUS METHOD

ONS, "Protecting personal data in Census 2021 results" (last updated 9 March 2023 [SP]). https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/protectingpersonaldataincensus2021results. Official methodology.
- "We protected the confidentiality of individuals' data in three ways: swapping records between areas, applying a cell key method to each table, and applying disclosure rules in deciding which tables could be published." [SP]
- Swapping: "the geographies were changed for between 7% and 10% of households, and for between 2% and 5% of individuals in communal establishments" [SV]
- Perturbation: "a typical dataset would have around 14% of cell counts perturbed by a small amount, and small counts were more likely to have been perturbed than large counts" [SV]
- Same cell, same answer: "both instances will have the same cell value and cell key, and so receive the same perturbation" [SV]; "repeated requests of the same dataset will have the same perturbation applied consistently" [SV]
- "There is also some perturbation of cells where the counts are zero" [SV]
- "Where there is a cell count of one in a published output, there is a high chance that it could be a swapped record, a perturbed count or an imputed record, or a combination of these" [SV]
- Table builder: "These disclosure checks are automated rule-based checks run by the system, which decide if there is a low enough disclosure risk to allow the release of a dataset." [SP]; "up to four variables can be selected at Output Area (OA) or Lower layer Super Output Area (LSOA) level" [SV]; "up to five variables are allowed at MSOA level and above" [SV]; "we will not provide details of which rule or rules have caused the areas to fail" [SV]; "The rules in the table builder are necessarily more cautious since they are automated" [SV]
- Stated cost: "Overall, the differences should be small and so should not change the conclusions of any analysis or research" [SV]; "These disclosure control measures have been carefully designed to protect confidentiality without distorting the statistics unduly" [SV]
- Cumulative risk across a user's queries: the sentence is NOT THERE. Two separate checks found nothing on tracking, logging or limiting a user's queries on this page or in EAP168. The stated defence against differencing is the consistent cell key. "Fixed classifications" is not a phrase on the page, and "differential privacy" does not appear. I could not find a separate "Create a custom dataset" protections page (one guessed URL 404; the tool page carries no disclosure text).

UK Census Offices (ONS, NRS, NISRA), "Annex A. Transparency of SDC methods and parameters", EAP paper, August 2021. https://uksa.statisticsauthority.gov.uk/wp-content/uploads/2022/02/EAP168-Statistical-Disclosure-Control-for-Census.pdf
- "The production of tables from a table builder could allow one to build an extremely large bank of tables" [SV]. "One could have access to large and extremely sparse tables which could allow identification of individuals and disclosure of information" [SV]
- "The method offers protection against disclosure by differencing, and in instances where a number of tables can be constructed and could otherwise be linked together to reconstruct records from the microdata." [SP, corrected]
- "Several features of the SDC methodology are intended to be kept private" [SV]; "we intend to keep the perturbation rate private for those small cell counts" [SV]; "Knowledge of the exact swapping rate may increase confidence in apparent attribute disclosures" [SV]
- Rules aim to stop tables that "give the perception of disclosure" [SP]. Parameters are "subject to further testing including intruder testing on the 2021 data" [SP]. I found no published Census 2021 intruder-test results.

ONS Census 2021 QMI (last revised 23 Nov 2023 [SP]): "The use of perturbation causes small changes to cells but does not intrinsically impact the interpretation of the data" [SV]; "To minimise the effect of perturbation, we recommend where possible using totals from tables with fewer cells, at higher geographies" [SV]. No quantified small-area error is given on either page.

GSS/GSR guidance for tables (Analysis Function policy store, administrative sources): published "1 October 2014" [SV]; "Note: this guidance is currently under review" [SV]; "It was written in the context of version 1.0 of the code" [SV]. Its PDFs were unreachable (two attempts), so its thresholds are not quoted.

ONS, "Policy on protecting confidentiality in tables of birth and death statistics" (no page date; refers to a 2018 revision). https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/disclosurecontrol/policyonprotectingconfidentialityintablesofbirthanddeathstatistics. Official policy; used here for the suppression and rounding wording.
- "Consider a 0, 1 or 2 in any table cell as having potential disclosure risk." [SP; the checker returned it twice and answered YES once, NO once]
- "additional cells will have to be suppressed (secondary suppression)" [SV]; in full, "In order to ensure that the value cannot be discovered by differencing from the row or column total, additional cells will have to be suppressed (secondary suppression)." [SP]
- "suppressing very small numbers (usually numbers less than three)" [SV]; "rounding to a specific base to avoid very small numbers (usually three or five)" [SV]
- "Differencing involves an intruder using two or more overlapping tables and subtraction to gather additional information about the differences between them" [SV]; "it is not sufficient to consider the protection for each table separately" [SV]; "it is good practice, where possible, to have a set of standard classifications to use to release data" [SV]

Code of Practice for Statistics, "Edition 3.0", "Autumn 2025" [SV]. https://osr.statisticsauthority.gov.uk/wp-content/uploads/sites/3/2026/08/Code-of-Practice-for-Statistics-3.0.pdf. Standard 4, "Manage data responsibly".
- 4.5: "Protect the confidentiality of individual and business information when producing statistics" [SV] … "apply appropriate disclosure control methods before release" [SV]
- 4.3: "Always consider the rights of data subjects and manage in ways that are consistent with data protection legislation." [SV in fragments]
- 4.4: "Be transparent about breaches of privacy and act publicly in addressing weaknesses" [SV]
- 4.6: "Keep pace with changing circumstances such as technological advances" [SV]
- The Code sets no numeric thresholds (control string NO).

ONS, "Guidance on intruder testing" (undated; mainly about microdata). https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/disclosurecontrol/guidanceonintrudertesting
- "This involves using individuals described as "friendly intruders" to try and see if they are able to re-identify anyone in the dataset." [SV]
- "(around a half day is normal)" [SV]; "they do not need to be specialist hackers with the capability of employing advanced data exploration techniques" [SV]; "Each identification claim is given a percentage of confidence" [SV]
- "The aim is not to release a dataset with zero risk so a good result would be if there were a small number of correct claims with low confidence." [SP]
- The 2011 Census intruder-test paper (Spicer, Tudor & Cornish, UNECE 2013) returned 403 at two URLs. No results are reported here.

ITEM 4 — ANONYMISATION DECISION-MAKING FRAMEWORK

Elliot, Mackey & O'Hara, The Anonymisation Decision-Making Framework 2nd Edition: European Practitioners' Guide, UKAN, University of Manchester, 2020 (CC-BY). https://ukanon.net/wp-content/uploads/2024/01/adf-2nd-edition-european-practitioners-guide-final-version-cover-2024-version-2.pdf. Practitioner framework.
- "Functional anonymisation does not assume that anonymisation can be zero-risk or irreversible" [SV]; "it is meant instead to bring anonymisation practice in line with the art of the possible" [SP]
- "whether data are or are not anonymised is not a property of the data, but determined by the relationship between the data and the context(s) in which they are held." [SV for "Whether data are or are not anonymised is not a property of the data"; remainder SP]
- "all data are held in some sort of context, which we call the data environment" [SV]. Environment features: other data, agents, governance processes, infrastructure [SP].
- "a data situation is the aggregate set of relationships between some data and the set of their environments" [SV]
- "Anonymisation, then, is a process of risk management but it is also a dynamic decision-making process" [SP]
- Ten components [SP, from the contents list]: 1 Describe/Capture the Presenting Problem; 2 Sketch the Data Flow and Determine Your Responsibilities; 3 Map the Properties of the Environment(s); 4 Describe and Map the Data; 5 Engage With Stakeholders; 6 Evaluate the Data Situation; 7 Select and Implement the Processes You Will Use to Assess and Control Disclosure Risk; 8 Maintain Stakeholders' Trust; 9 Plan What to Do if Things Go Wrong; 10 Monitor the Evolving Data Situation. Grouped as data situation audit (1–6), disclosure risk assessment and control (7), impact management (8–10).

ITEM 5 — RE-IDENTIFICATION EVIDENCE

- Narayanan & Shmatikov, "Robust De-anonymization of Large Datasets (How to Break Anonymity of the Netflix Prize Dataset)", arXiv cs/0610105, version dated 5 Feb 2008 (the S&P 2008 venue is not printed; the utexas PDF 404). "We demonstrate that an adversary who knows only a little bit about an individual subscriber can easily identify this subscriber's record in the dataset" [SV]. "With 8 movie ratings (of which 2 may be completely wrong) and dates that may have a 14-day error, 99% of records be uniquely identified in the dataset." [SV; "records be" is sic]. "For 68%, two ratings and dates (with a 3-day error) are sufficient" [SV]. Dataset: 100,480,507 ratings from 480,189 subscribers [SV]. The IMDb test used "a few dozen" users and identified two [SP].
- de Montjoye, Hidalgo, Verleysen & Blondel 2013, Scientific Reports 3:1376, published 25 March 2013. https://www.nature.com/articles/srep01376. "We study fifteen months of human mobility data for one and a half million individuals" [SV]; "four spatio-temporal points are enough to uniquely identify 95% of the individuals" [SV]; "the uniqueness of mobility traces decays approximately as the 1/10 power of their resolution" [SV]; "Hence, even coarse datasets provide little anonymity" [SV]; "two randomly chosen points still uniquely characterize more than 50% of the users" [SV].
- de Montjoye, Radaelli, Singh & Pentland 2015, Science 347(6221):536–539. ABSTRACT via MIT DSpace, https://dspace.mit.edu/handle/1721.1/96321. "We study 3 months of credit card records for 1.1 million people and show that four spatiotemporal points are enough to uniquely reidentify 90% of individuals" [SV]; "knowing the price of a transaction increases the risk of reidentification by 22%, on average" [SV]; "women are more reidentifiable than men in credit card metadata" [SP].
- Rocher, Hendrickx & de Montjoye 2019, Nature Communications 10:3069, 23 July 2019. https://www.nature.com/articles/s41467-019-10933-3. "Using our model, we find that 99.98% of Americans would be correctly re-identified in any dataset using 15 demographic attributes" [SV]. It is a model estimate. "seriously challenge the technical and legal adequacy of the de-identification release-and-forget model" [SV]. They "reject the claim that sampling or releasing partial datasets" … "provide plausible deniability" [SP].
- Culnane, Rubinstein & Teague 2017, arXiv 1712.05627 (15 Dec 2017). ABSTRACT. "we describe successful re-identification of patients in an Australian de-identified open health dataset" [SV]; "As in prior studies of similar datasets, a few mundane facts often suffice to isolate an individual." [SP]; "Decreasing the precision of the unit-record level data, or perturbing it statistically, makes re-identification gradually harder at a substantial cost to utility." [SV for "at a substantial cost to utility"]; the work used "a 10% sample dataset" [SV].
- NYC taxi. Pandurangan, "On Taxis and Rainbows: Lessons from NYC's improperly anonymized taxi logs", 21 June 2014 (practitioner blog). https://www.vijayp.ca/articles/blog/2014-06-21_on-taxis-and-rainbows--f6bc289679a1.html. "more than 173 million individual trips" [SV]; "hasn't been anonymized properly" [SV]; identifiers were unsalted MD5 hashes; "there are only about 3M possible taxi licence numbers" [SV]; "computing the 22M hashes took less than 2 minutes" [SV for "took less than 2 minutes"]; "simply using hash functions is an ineffective way to anonymize data" [SP].
- Strava. Guardian, BBC and Strava's own 2018 letter were unreachable, so nothing is quoted from journalism. Primary source reached: Strava Engineering (Drew Robb), "Building the Global Heatmap", 1 Nov 2017, https://medium.com/strava-engineering/the-global-heatmap-now-6x-hotter-23fc01d301de: "700 million activities" [SV], "1.4 trillion latitude/longitude points" [SV], "the heatmap only contains public activities and respects all privacy settings" [SP]. The widely repeated "1 billion activities / 3 trillion points" is NOT on this page (checked NO). Official aftermath: US Deputy Secretary of Defense memo, 3 Aug 2018: "DoD personnel are prohibited from using geolocation features and functionality on both non-government and government-issued devices, applications, and services while in locations designated as operational areas" [SV]. The memo does not name Strava.
- AOL. JOURNALISM, reached only through a tertiary source (NYT blocked). Wikipedia, "AOL search log release": "twenty million search queries for over 650,000 users over a three-month period" [SV on Wikipedia]; "they exposed user #4417749 as Thelma Arnold, a 62-year-old widow from Lilburn, Georgia" [SV on Wikipedia]. It cites Barbaro & Zeller, "A Face Is Exposed for AOL Searcher No. 4417749", New York Times, 9 Aug 2006. The NYT text itself was not seen.

ITEM 6 — DIFFERENCING AND INTERACTIVE SYSTEMS

- Handbook on Statistical Disclosure Control, Second Edition, dated "2026, June" on its index page [SP] (Hundepool et al.; STACE project). https://sdctools.github.io/HandbookSDC/05-frequency-tables.html. The 2010 ESSnet PDF at ec.europa.eu returned 404. Chapter 5: "Differencing involves an intruder using multiple overlapping tables and subtraction to gather additional information about the differences between them." [SV for the phrase from "using multiple overlapping tables"]. "Importantly, when linked tables are produced from the same dataset it is not sufficient to consider the protection for each table separately. If a cell requires protection in one table then it will require protection in all tables, otherwise the protection in the first table could be undone." [SP]. Cell key method: "The cells are adjusted in such a way that the same cell is perturbed in the same way even when it appears across different tables." [SP]. Neither chapter 5 nor chapter 6 treats online table builders or query monitoring as a topic.
- ONS births and deaths policy, Annex B.2 (URL in Item 3): "A disclosure by differencing can occur when this comparison of two or more tables enables a small cell (0, 1, or perhaps 2, but most specifically 1) to be calculated" [SV]; "If these tables are compared they can reveal a new, previously unpublished table for the differenced area" [SV].
- Dinur & Nissim, "Revealing Information while Preserving Privacy" (PDF dated December 30, 2002; PODS 2003 not printed; dl.acm.org 403). https://crypto.stanford.edu/seclab/sem-03-04/psd.pdf. "Our main result is a polynomial reconstruction algorithm of data from noisy (perturbed) subset sums" [SV]; "in order to achieve privacy one has to add perturbation of magnitude Ω(√n)" [SP]; "That is, smaller perturbation always results in a strong violation of privacy" [SV]. In one sentence: if answers to enough aggregate queries are off by less than about √n, an adversary can rebuild almost the whole database.
- Garfinkel & Abowd, ACM Queue 16(5) (https://queue.acm.org/detail.cfm?id=3295691; title not visible in the fetched text): "the underlying microdata is recovered merely by finding a set of microdata that is consistent with the published statistical tabulations" [SV]; for 2010 "the Census Bureau published approximately 7.7 billion linearly independent statistics" [SV for "approximately 7.7 billion"]; "The 2010 census found a total population of 308,745,538." [SV for the number]
- The Bureau's own reconstruction figures. Hawes, "Seven Lessons Learned From the Implementation of Differential Privacy for the 2020 Census", Harvard Data Science Review [title SP]. https://hdsr.mitpress.mit.edu/pub/dgg03vo6. Researchers "were able to accurately determine location (census block), age (+/- one year), sex, race (63 categories), and ethnicity for 219 million individuals" [SV for "219 million individuals"]; "the Census Bureau was able to confirm accurate reidentifications for 52 million people" [SV]. Hawes does not print the percentages 46%, 71%, 38% or 17% (checked NO). My arithmetic on 308,745,538: 219 million is about 71%, and 52 million about 17%.
- Later figures. Abowd et al., "A Simulated Reconstruction and Reidentification Attack on the 2010 U.S. Census", arXiv 2312.11283 (comment line: accepted Harvard Data Science Review 2025 paper). ABSTRACT: "Ninety-seven million person records (every resident in 70% of all census blocks) are exactly reconstructed with provable certainty using only public information." [SP]; an attacker "can reidentify with 95% accuracy population unique individuals who are perfectly reconstructed and not in the modal race and ethnicity category in their census block (3.4 million persons)" [SV for "3.4 million"]. The harm is stated for people who are minorities within their block.
- Abowd & Hawes (arXiv 2206.03524): "Overall, 44% of the entire US population has a unique combination of sex and single year of age at the block level." [SV]; in blocks of 1–9 residents "over 95% of individuals are population uniques on sex and single year of age at the block level" [SP].

ITEM 7 — GROUP PRIVACY

- Taylor, Floridi & van der Sloot (eds) 2017, Group Privacy: New Challenges of Data Technologies, Springer, Philosophical Studies Series 126. Not open access. Chapter 1 ABSTRACT, https://link.springer.com/chapter/10.1007/978-3-319-46608-8_1: "Although their effects have so far been addressed only on the individual level" [SV], "profiling and machine learning technologies are directed at the group level and are used to formulate types, not tokens" [SV]; "they work to scale, and enable their users to target the collective as much as the individual" [SV]. "This means that our legal, philosophical and analytic attention to the individual may need to be adjusted, and possibly extended" [SV to "extended"].
- Mittelstadt 2017, "From Individual to Group Privacy in Big Data Analytics", Philosophy & Technology 30(4):475–494, open access. https://link.springer.com/article/10.1007/s13347-017-0253-7. "Analytics allows for a new type of algorithmically assembled group to be formed that does not necessarily align with classes or attributes already protected by privacy and anti-discrimination law" [SV]. Ad hoc group: "a group whose membership is assembled for a third party interest according to perceived links between members, often for a time- or purpose-limited period with volatile membership requirements" [SV to "between members"; rest SP]. "Algorithmically grouped individuals have a collective interest in the creation of information about the group, and actions taken on its behalf" [SV]. "Group privacy is proposed as a third interest to balance alongside individual privacy and social, commercial and epistemic benefits" [SV]. "An identity can be imposed on members unaware that they belong to the group." [SP]
- Floridi 2014, "Open Data, Data Protection, and Group Privacy", Philosophy & Technology 27(1):1–3. UNREACHABLE (Springer 429 twice; PhilPapers archive 403). Nothing quoted. Mittelstadt paraphrases it but, per the page, does not quote it directly.

ITEM 8 — SYNTHETIC DATA, RANGES, AND HOW A THRESHOLD IS CHOSEN

- ONS Methodology Working Paper 16, "Synthetic data pilot" (Bates, Špakulová, Dove, Mealor; no date on page). https://www.ons.gov.uk/methodology/methodologicalpublications/generalmethodology/onsworkingpaperseries/onsmethodologyworkingpaperseriesnumber16syntheticdatapilot. "Synthetic data are microdata records created to improve data utility while preventing disclosure of confidential respondent information" [SV; the paper attributes this definition to the US Census Bureau]. "Synthetic data is created by statistically modelling original data and then using those models to generate new data values that reproduce the original data's statistical properties." [SP]. Six levels [SP]: Synthetic structural; Synthetic valid; Synthetically-augmented plausible; multivariate plausible; multivariate detailed; replica. The replica level carries "extremely high disclosure risk, likely to be only available in secure research facility" [SP]. "it is not acceptable to release a synthetic dataset that could lead to a real or perceived risk of disclosure" [SV].
- ONS Data Science Campus with the Alan Turing Institute, 30 Nov 2023, https://datasciencecampus.ons.gov.uk/synthesising-the-linked-2011-census-and-deaths-dataset-while-preserving-its-confidentiality/: "A synthetic dataset contains artificially generated data as opposed to genuine, real-world data" [SV]; "the generator must adhere to the definition of DP, not the synthetic data itself" [SV]; "Ultimately, we chose to use ε = 1." [SP]; "While DP offers strong claims of protection against a litany of attacks, it does not provide an absolute guarantee of privacy." [SP]. ADR UK pages were not attempted.
- Rounding and bands. Handbook on SDC ch. 5: "Each method is flexible in terms of the choice of the base for rounding, although common choices are 3 and 5." [SV for "common choices are 3 and 5"]. Rounding removes all 1s and 2s, "which prevents cases of perceived disclosure as well as actual disclosure" [SP]. Controlled rounding keeps tables additive [SP].
- How a threshold is chosen (ONS births and deaths policy §4.2.2): "A cell with a count of one is a potential disclosure risk as it allows for possible immediate identification" [SV]; "Similar consideration needs to be given to a count of two" [SV]; "The producer of the tables will need to make a judgement call for other low counts, depending on the sensitivity of the table as a whole" [SV]. Rates: "A rate or other statistic may be disclosive if it is possible to infer that the underlying counts contain small numbers, even if the latter are not published" [SV]. Sparsity heuristic: "an average of 1 count/cell is sometimes used" [SV]. So the threshold is presented as judgement scaled to sensitivity, not a derived constant.

UNEXPECTED FINDINGS
1. ONS has an explicit official statement on online query tools, in the births and deaths policy §4.4 "Explorable datasets and online tools":
   - users are "able to generate multiple tables and potentially to attempt to breach confidentiality by specifying very detailed or overlapping outputs" [SP full sentence]
   - "it is likely that any disclosure control applied to online data will have to be stricter than is applied to outputs which the provider is able to assess individually for risk" [SV]
   - "A minimum cell count equal to five is suggested" [SV], because "A higher minimum frequency will be necessary to ensure comparisons with previously published tables do not lead to individuals and their characteristics being identified" [SV]
   - tools should "require user registration with a validated email address, name and contact details" [SV], "keep a log of data requests by user which is audited for potentially suspicious activity" [SV], and "place a limit on the number of similar tables which can be requested, this is to avoid disclosure by differencing" [SV]
   - "The use of online data access tools is still developing, and appropriate controls will have to be kept under review" [SV]
2. The Census 2021 table builder pages say none of that. No registration, logging or query limit is stated. The defence rests on consistent perturbation, automated sparsity rules and undisclosed parameters.
3. The UK census protects by doubt, not suppression: a published count of one has "a high chance" of being swapped, perturbed or imputed, and the rules aim to prevent even "the perception of disclosure".
4. Kenny et al. found the US system degraded counts for mixed-race precincts while not preventing race prediction. Dwork & Roth's smoker passage says this is by design: DP does not limit what a study reveals about a group.
5. The Census Bureau's final ε=19.61 was described in its own release as "exponentially higher" than the 12.2 used months earlier [SP], after accuracy objections.
6. ICO anonymisation guidance, "How do we ensure anonymisation is effective?" (page dated 10 October 2025), https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/how-do-we-ensure-anonymisation-is-effective/:
   - "With public release, you should have a very robust approach to anonymisation" [SV]; "when you release information publicly, you lose control of the data" [SV]
   - k-anonymisation is "susceptible to certain types of inference attacks (eg homogeneity and background knowledge attacks)" [SP]
   - "You should periodically review the decisions you take when anonymising personal data and the assessments that underpin them" [SV]
   - On a first-pass read it does not address query-based or interactive tools, differencing, or small-number thresholds.
7. Strava's engineering post says the heatmap respected all privacy settings. On Strava's own account, the map honoured individual settings; I could not reach a source describing what it exposed.
8. Suppression has its own small-group cost. Abowd & Hawes: "Suppression rules disproportionately impact small population groups and small areas because of the nonignorable missing data problem." [SP]

LEFT OUT, AND WHY
- Floridi 2014; the Curtis et al. and Brownstein et al. map re-identification papers; the NEJM letter "No place to hide": all unreachable. The "re-identification from a published map" thread therefore has no fetched academic source.
- NYT, Guardian and BBC texts (blocked); Ohm 2010 (404).
- GSS/GSR tables guidance PDFs and the ONS health-statistics confidentiality guidance PDF (400/404); EAP125 (the .docx came through as binary); the Census Bureau handbook and briefs on www2.census.gov (robots.txt).
- Census 2021 intruder-test results and 2011 results: not found or unreachable.
- Golle's 2006 re-estimate of Sweeney's figure: not attempted, so not quoted.
- NRS and NISRA census pages; ADR UK synthetic data pages: not attempted.
- The 2/3/5/7 threshold schemes already in the ledger: not re-derived, as instructed.

RICH REFERENCES
1. ONS, Policy on protecting confidentiality in tables of birth and death statistics: §4.2.2, §4.4 and Annex B.2 give thresholds, differencing and online-tool controls in official UK wording.
2. Elliot, Mackey & O'Hara, The Anonymisation Decision-Making Framework, 2nd ed. (UKAN 2020, CC-BY): the source for "not a property of the data" and the ten components.
3. Abowd & Hawes, "Confidentiality Protection in the 2020 US Census of Population and Housing" (arXiv 2206.03524): the Bureau's own account of reconstruction, budgets and the small-area trade-off. Read against Kenny et al. 2021.

WHAT SURPRISED ME
- ONS's most direct guidance on interactive tools sits in a births-and-deaths policy, not in the census table-builder documentation.
- Sweeney's 87% is an estimate from 1990 summary tables in an unreviewed working paper, yet it is the most repeated number in the field.
- The Bureau's widely cited 46/71/38/17% figures do not appear in Hawes's article; it gives 219 million and 52 million instead.
- The Strava engineering post gives 700 million activities, not the 1 billion usually repeated.
- Code of Practice 3.0 is labelled "Autumn 2025" on the document but sits at a 2026/08 upload path.

---

## Agent B — UK data-protection law for a private platform

CHAPTER 10 — FACET: UK DATA-PROTECTION LAW AND REGULATOR GUIDANCE FOR A PRIVATE PLATFORM
Read date for every source: 6 October 2026.

ACCESS AND METHOD
- WebSearch was unavailable (shared budget exhausted). curl was blocked by the proxy. Everything came through WebFetch on direct URLs at legislation.gov.uk, ico.org.uk and gov.uk.
- Marks: STRING-VERIFIED (SV) = a second fetch with a YES/NO presence prompt confirmed the string, with a false control string in the same batch (every control came back NO). SINGLE PASS (SP) = one extraction only.
- "Page date" for ICO pages is the page's metadata date (last modified), not necessarily first publication.
- Nothing is quoted from memory. This is a report of law and guidance, not advice.

HEADLINE FOR THE CHAPTER AUTHOR — the brief's statutory map is out of date in four places:
- Article 89 UK GDPR and DPA 2018 s.19 no longer exist. Both were omitted on 5 February 2026 and replaced by a new Chapter 8A (Articles 84A–84D).
- Article 14(5)(b), the research-flavoured "disproportionate effort" exemption, was omitted on 5 February 2026 and replaced by Article 14(5)(e), (f), (6) and (7).
- The research and statistics definitions and "broad consent" sit in Article 4(2)–(7), not Articles 4(29)–(31). Article 8A is "Purpose limitation: further processing".
- The office of Information Commissioner was abolished and its functions transferred to the Information Commission on 30 September 2026. The UK GDPR text now says "the Commission".

---------------------------------------------------------------
ITEM 1 — PERSONAL DATA AND ITS EDGES
---------------------------------------------------------------

1a. UK GDPR Article 4(1). Statute, binding.
URL: https://www.legislation.gov.uk/eur/2016/679/article/4 (banner: "There are currently no known outstanding effects" — SP)
- "'personal data' means any information relating to an identified or identifiable natural person ('data subject'); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person". SV in three fragments from "an identifiable natural person is one…" to the end; the opening clause is SP.
- Role: the threshold definition; "location data" and "cultural or social identity" are named in the statute itself.

1b. Article 4(5) pseudonymisation. Statute.
- "'pseudonymisation' means the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person". SV for "can no longer be attributed to a specific data subject without the use of additional information"; the rest SP.

1c. Recital 26. Recital, interpretive and not operative.
URL: https://www.legislation.gov.uk/eur/2016/679/introduction
- "Personal data which have undergone pseudonymisation, which could be attributed to a natural person by the use of additional information should be considered to be information on an identifiable natural person." First clause SV; remainder SP.
- "To determine whether a natural person is identifiable, account should be taken of all the means reasonably likely to be used, such as singling out, either by the controller or by another person to identify the natural person directly or indirectly." SV for "account should be taken of all the means reasonably likely to be used, such as singling out, either by the controller or by another person".
- "…account should be taken of all objective factors, such as the costs of and the amount of time required for identification, taking into consideration the available technology at the time of the processing and technological developments." SV for "such as the costs of and the amount of time required for identification".
- "The principles of data protection should therefore not apply to anonymous information, namely information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable." SV in two fragments.
- "This Regulation does not therefore concern the processing of such anonymous information, including for statistical or research purposes." SV for the final clause.
- Role: source of the "means reasonably likely" test; "singling out" is in the recital, not the Article.

1d. ICO "What is personal data?". Regulator guidance, non-statutory.
URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/what-is-personal-data/ (page date 7 September 2026). The parent page carries "Due to changes made by the Data (Use and Access) Act, this guidance is under review and may be subject to change." (SP)
- "Pseudonymised personal data remains personal data and within the scope of the UK GDPR". SV.
- "The UK GDPR does not apply to personal data that has been anonymised". SV.
- "…you must strip personal data of sufficient elements that mean the individual can no longer be identified". SV.
- "if you could at any point use any reasonably available means to re-identify the individuals to which the data refers, that data will not have been effectively anonymised". SP.
- "Information relating to a deceased person does not constitute personal data". Returned as closest wording by the presence check.
Sibling page: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/personal-information-what-is-it/what-is-personal-data/what-are-identifiers-and-related-factors/ (page date 19 November 2024; "under review")
- "If you can distinguish an individual from other individuals, then that person is 'identified' or is 'identifiable'." SV.
- "…whether any potential identifier, including a name, actually identifies an individual depends on the context." SV.
- "An individual's social media 'handle' or username, which may seem anonymous or nonsensical, is still sufficient to identify them as it uniquely identifies that individual." SP.
Not found:
- Neither page has a sentence using "singling out". That language is in the anonymisation guidance (1e).
- Neither page states when data about a small group is personal data.
- The sub-page "Can we identify an individual indirectly…" returned 404 at the URL I tried.

1e. ICO Anonymisation guidance. Regulator guidance.
Landing: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/ (page date 29 August 2025)
Status, from the "About this guidance" sub-page (all SP):
- "28 March 2025 - this guidance was published."
- "This guidance is not a statutory code. It contains advice on how to interpret relevant law on anonymisation and pseudonymisation."
- "Due to changes made by the Data (Use and Access) Act, this guidance is under review and may be subject to change."
Sub-pages: introduction (1 April 2025); "How do we ensure anonymisation is effective?"; pseudonymisation (10 October 2025); accountability and governance; glossary.

Definition (introduction page):
- "Anonymisation is the process of turning personal data into anonymous information so that a person is no longer identifiable." SV.
- "…anonymous information is data that does not relate to an identified or identifiable person (ie data that is not personal data). Data protection law does not apply to anonymous information." SV in two fragments.
- "We use the term 'effective anonymisation' to mean the technical and organisational measures you need to ensure that the status of the data meets the legal threshold for anonymisation under UK GDPR." Two consistent passes, not YES/NO-checked; treat as SP.
- "…applying anonymisation techniques to turn personal data into anonymous information counts as processing personal data." SP.
- "…when you create aggregate statistical information from personal data, that data is 'adapted' or 'altered'." Fragment SV.

Standard (effectiveness page: …/anonymisation/how-do-we-ensure-anonymisation-is-effective/):
- "Anonymisation is about reducing the likelihood of a person being identified or identifiable to a sufficiently remote level." SV.
- "You do not need to take into account any purely hypothetical or theoretical chance of identifiability, rather, what is reasonably likely relative to the circumstances." First clause SV.
- Key indicators: "You should use two key indicators for determining whether information is personal data or not. These are: singling out; and linkability." SP.
- "Singling out means that you can single out the same person across records, or isolate the records that relate to a person from a dataset." SP.
- "Distinguishing one record from others in the table is not sufficient by itself to make the person the record relates to identifiable." SV.
- "Linkability is sometimes known as the mosaic or jigsaw effect." SV.

Spectrum of identifiability:
- "Identifiability exists on a spectrum." SV.
- "In practice, identifiability may be viewed as a spectrum that includes the binary outcomes at either end, with a blurred band in between…" SV for "identifiability may be viewed as a spectrum that includes the binary outcomes at either end, with a blurred band in between".
- "Information may 'move' along the spectrum of identifiability to the point that data protection law starts to apply to it, or stops applying to it." SP.

Motivated intruder:
- "Applying a 'motivated intruder' test is a good starting point to consider identifiability risk." SV.
- "You must consider all practical steps and means that are reasonably likely to be used by someone motivated to identify people whose personal data was used to derive anonymous information. This is known as the motivated intruder test." SP.
- "A motivated intruder is someone who wishes to identify a person from the anonymous information that is derived from their personal information." SV.
- "You should assume that a motivated intruder is someone that: is reasonably competent; has access to appropriate resources (eg the internet, libraries, public documents); and uses investigative techniques (eg making enquiries with people who may have additional knowledge about a person, or advertising for anyone with that knowledge to come forward)." SV for "is reasonably competent" and "has access to appropriate resources (eg the internet, libraries, public documents)".
- "Intruders may be investigative journalists, estranged partners, stalkers, industrial spies or researchers attempting to demonstrate anonymisation weaknesses." SV to "researchers".
- "Depending on the perceived value of the data to them, a motivated intruder may well use specialist knowledge or equipment or resort to criminal acts…" SV.
- "Both the ICO and the First-tier Tribunal (General Regulatory Chamber)… use this test." SV for the opening words.
- Listed motivations include "curiosity (eg a local person's desire to find out who has been involved in an incident shown on a crime map)". SV.
- "Identifiability risk can arise where one person or group knows a great deal about another person." SV.

Public release versus controlled access. The phrase "release and forget" does not appear on this page; the ICO's term is "release model".
- "The assessment will be linked to your 'release model' (ie public release, release to defined groups, or if anonymising data sets for further internal use only)." SV.
- "Before you release data to the world at large, you should consider using robust techniques to reduce the higher risk of unauthorised personal data disclosure compared to intentional and controlled data release to known recipients." SV for the first clause.
- "With public release, you should have a very robust approach to anonymisation. This is because when you release information publicly, you lose control of the data. For example, it is almost impossible for you to retract the data if it later becomes clear that it relates to people that are identifiable." SV in three fragments.
- "You also do not have control over the actions and intentions of anyone who receives that information." SP.
- "Designing these access controls appropriately will help reduce identifiability risk and potentially allow you to include more detail, while continuing to ensure effective anonymisation." SP.

Aggregates and small numbers. The page states no numeric small-number rule of the ICO's own.
- "The NHS's standard for publishing health and social care data requires that, for strong anonymisation, k is set to five." SV. This is the ICO citing someone else's standard.
- "K-anonymisation does have some limitations, for example, it can be: susceptible to certain types of inference attacks (eg homogeneity and background knowledge attacks)." SP. Followed by: "If an attacker knows that a person is within a certain group, they can discover other attributes they did not know to link to that group (such as a health condition)". SP.
- Review example: an authority answers a yearly FOI request for programme statistics "including by number and characteristics such as age, sex, religious belief and nationality" for three years, then withholds in year four because "the number of participants in the programme had decreased compared to previous years; a high-profile event involving the participants increased the likelihood that there were people motivated to re-identify them; and there was more information available in the public domain…". SV for the first limb; rest SP.
- "Using these methods does not guarantee you will achieve anonymisation: successful anonymisation depends on contextual factors." First clause SV.

Inference and educated guesses:
- "An inference refers to the potential to infer, guess or predict details about someone who can already be identified directly or indirectly." SV.
- "Whether an inference is personal data depends on whether it relates to an identified or identifiable person." SV.
- "You must have a degree of certainty that information is about one person and not another. The mere possibility of making an educated guess about a person's identity does not present a data protection risk. Even if a guess based on anonymous information is correct, this does not mean that a disclosure of personal data has happened." SV, all three sentences.

Pseudonymised data (…/anonymisation/pseudonymisation/):
- "Pseudonymised personal data is in scope of data protection law." SV.
- "It is not a way of transforming personal data to the extent the law no longer applies." SV.
- "Pseudonymised data is personal data in the hands of someone who holds the additional information." SV.
- "If you share pseudonymised data (but not the additional information) with another organisation, it may be anonymous information in their hands. However, it does not change the status of the data as personal data when you process it in this way." Fragment SV; full sentences SP.

Role of 1e: the regulator's operational test for whether a published aggregate is outside the Act; ties the required robustness to public release; treats group-level guessing as distinct from disclosure.

---------------------------------------------------------------
ITEM 2 — SPECIAL CATEGORY DATA AND INFERENCE
---------------------------------------------------------------

2a. Article 9. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/9
- 9(1): "Processing of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership, and the processing of genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health or data concerning a natural person's sex life or sexual orientation shall be prohibited." SV in two fragments (opening to "trade union membership"; "data concerning health… shall be prohibited"); middle SP.
- 9(2)(a): "the data subject has given explicit consent to the processing of those personal data for one or more specified purposes, except where domestic law provides that the prohibition referred to in paragraph 1 may not be lifted by the data subject". First clause SV.
- 9(2)(e): "processing relates to personal data which are manifestly made public by the data subject". SV.
- 9(2)(j): "processing is necessary for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes, is carried out in accordance with Article 84B and is based on domestic law which shall be proportionate to the aim pursued and provide for suitable and specific measures to safeguard the fundamental rights and the interests of the data subject." SV for "is carried out in accordance with Article 84B"; the control "in accordance with Article 89(1)" returned NO. F-note (SP): substituted 5.2.2026 by Data (Use and Access) Act 2025 ss. 87(1)(b), 142(1); S.I. 2026/82 reg. 2(o).

2b. DPA 2018 Schedule 1 Part 1 paragraph 4 ("Research etc"). Statute.
URL: https://www.legislation.gov.uk/ukpga/2018/12/schedule/1/part/1
- "This condition is met if the processing— (a) is necessary for archiving purposes, scientific or historical research purposes or statistical purposes, (b) is carried out in accordance with Article 84B of the UK GDPR, and (c) is in the public interest." SV for (a), (b), (c). The control for the old wording "Article 89(1) of the UK GDPR (as supplemented by section 19)" returned NO.
- Role: the special-category research gateway has a public-interest limb that the ordinary research provisions lack.

2c. ICO "What is special category data?", section headed "What about inferences?". Regulator guidance.
URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-is-special-category-data/ (page date 22 September 2025; "under review" note confirmed)
- The brief's anticipated wording "If you can infer… with a reasonable degree of certainty" does NOT appear on the current page (presence check: NO). The current test turns on intention.
- "The UK GDPR is clear that special category data includes not only personal data that specifies relevant details, but also personal data revealing or concerning these details." SP.
- "…you may be able to infer a person's religion or ethnicity from their name or images of them." SV.
- "Whether or not inferred data counts as special category data and triggers Article 9 depends on whether: your processing intends to make an inference linked to one of the special categories of data; or you intend to treat someone differently on the basis of inferred information linked to one of the special categories of data." SV for both limbs.
- "If this is the case, then you are processing special category data regardless of how confident you are that the inference is correct." SV.
- "If you carry out any form of profiling which infers things like ethnicity, beliefs, politics, health status (condition or risks), sexual orientation or sex life, you will be processing special category data and must identify an Article 9 condition for processing." SV in two fragments.
- Example 1 (SP): a social media user posts that they are at a place of worship. "By itself, the user's statement is unlikely to be considered special category data… However, if the social media platform chooses to infer something about the user's religious beliefs, or decides to treat them differently on this basis… then the processing will involve special category data."
- Onlookers' inferences: "Even if you're not drawing an inference or treating people differently, there may still be an obvious risk that other people could (rightly or wrongly) infer something from the data that might be considered sensitive or private. If this is the case (especially if this relates to the special categories of data), you should think carefully about how you ensure fairness and whether there's anything more you can do to minimise those privacy risks." SV for both sentences' core strings.
- Not found: any sentence on data about a group, area or postcode implying special category data about individuals. The passage just quoted is the nearest. Combine with 1e (an inference is personal data only if it "relates to an identified or identifiable person").
- Role: the controller's intention triggers Article 9; third-party inference is routed to fairness.

---------------------------------------------------------------
ITEM 3 — LAWFUL BASES; CONSENT; LEGITIMATE INTERESTS; OBJECTION AND ERASURE
---------------------------------------------------------------

3a. Article 6(1). Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/6
- (a): "the data subject has given consent to the processing of his or her personal data for one or more specific purposes". SV.
- (ea): "processing is necessary for the purposes of a recognised legitimate interest". SV.
- (f): "processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data, in particular where the data subject is a child". SV.
- 6(5): "For the purposes of paragraph 1(ea), processing is necessary for the purposes of a recognised legitimate interest only if it meets a condition in Annex 1." SP.
- 6(11): "For the purposes of paragraph 1(f), examples of types of processing that may be processing that is necessary for the purposes of a legitimate interest include— (a) processing that is necessary for the purposes of direct marketing, (b) intra-group transmission of personal data… where that is necessary for internal administrative purposes, and (c) processing that is necessary for the purposes of ensuring the security of network and information systems." SP.
- F-notes (SP): DUAA 2025 s.70(2)(b), s.70(4); S.I. 2026/82 reg. 2(c).

3b. Annex 1, recognised legitimate interests. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/annex/1
- Headings (SP): "Disclosure for purposes of processing described in Article 6(1)(e)"; "National security, public security and defence"; "Emergencies"; "Crime"; "Safeguarding vulnerable individuals".
- F-note (SP): "Annex 1 inserted (5.2.2026) by Data (Use and Access) Act 2025 (c. 18), s. 142(1), Sch. 4; S.I. 2026/82, reg. 2(z6)".
- No condition covers research, statistics or analytics (SP; consistent with the ICO page below).
ICO guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/recognised-legitimate-interest/ — "23 March 2026 - this guidance was published." SV.
- "Recognised legitimate interest has five conditions containing pre-approved purposes that are in the public interest." SV.
- "For these purposes, you don't have to assess whether a person's rights, freedoms or interests outweigh the recognised legitimate interest." SV.
- "…you must satisfy yourself that using the information is necessary for the particular recognised legitimate interest condition." SV.
- "…you can only use this basis for the pre-approved purposes listed in its five conditions." SV.
- Role: closes off any reading that the 2025 Act created a no-balancing route for a cultural dashboard.

3c. Commencement of the Data (Use and Access) Act 2025, as stated on 6 October 2026.
- ICO, https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/ (page date 12 February 2026): "The Data (Use and Access) Act 2025 got Royal Assent on 19 June 2025." SV. "All the provisions affecting data protection law and the Privacy and Electronic Communications Regulations are now in force." Wording as returned by the presence check, which corrected my garbled first-pass string.
- ICO "what does it mean for organisations" (page date 19 June 2026): "…all data protection provisions in the Data (Use and Access) Act 2025 are now in force." SV. "The changes will be phased in between June 2025 and June 2026." SP.
- gov.uk, https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement ("Published: 25 July 2025", "Last updated: 5 February 2026"): "Stage 3, approximately 6 months after Royal Assent, will include the commencement of the main changes to data protection legislation in Part 5 of the Act except for section 103 on complaints by data subjects." SP. "Changes to the Information Commissioner's Office (ICO) governance structures in Part 6 of the Act will take place once members of the Information Commission's new Board have been appointed. This is expected in early 2026." SP. This page is stale on that point; see next bullet.
- S.I. 2026/82, "The Data (Use and Access) Act 2025 (Commencement No. 6 and Transitional and Saving Provisions) Regulations 2026" (title SV; made "29th January 2026" SV; "comes into force on 5th February 2026" returned as closest wording). Lists sections 67, 68, 70, 77, 81, 86 and 112 (SP; "section 86" and "section 112" SV).
- S.I. 2026/1015, "The Data (Use and Access) Act 2025 (Commencement No. 9 and Transitional and Saving Provisions) Regulations 2026" (title SV; "Made 10th September 2026" SV): "The following provisions of the Data (Use and Access) Act 2025 come into force on 30th September 2026—" including "section 118 (abolition of the office of Information Commissioner)" and "section 119 (transfer of functions to the Information Commission)". SV.
- Consequential F-note on Article 36: "Word in Art. 36(1)-(4) substituted (30.9.2026) by The Data (Use and Access) Act 2025 (Consequential Amendments and Transitional Provision) Regulations 2026 (S.I. 2026/386)…; S.I. 2026/1015, reg. 2(c)". SP.
- The ICO web pages I fetched (two dated 30 September 2026) still say "ICO" and did not mention the change.

3d. Article 7. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/7
- 7(1): "Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data." SP.
- 7(3): "The data subject shall have the right to withdraw his or her consent at any time. The withdrawal of consent shall not affect the lawfulness of processing based on consent before its withdrawal. Prior to giving consent, the data subject shall be informed thereof. It shall be as easy to withdraw as to give consent." First and last sentences SV (the brief's wording is confirmed); middle two SP.
- 7(4): "When assessing whether consent is freely given, utmost account shall be taken of whether, inter alia, the performance of a contract, including the provision of a service, is conditional on consent to the processing of personal data that is not necessary for the performance of that contract." SP.
- Article 4(11): "freely given, specific, informed and unambiguous indication of the data subject's wishes". SV. That phrase is statutory; it did not appear as a string on the ICO consent guide page I checked.

3e. ICO consent guidance. All pages carry the "under review" note. None mentions "broad consent" (checked on the valid-consent page).
"When is consent appropriate?", https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/consent/when-is-consent-appropriate/ (page date 4 August 2026):
- "Consent is one lawful basis for processing, but there are six others." Confirmed as actual text.
- "Consent won't always be the most appropriate or easiest." SV.
- "Consent will not usually be appropriate if there is a clear imbalance of power between you and the individual." SV.
- "Those who depend on your services, or fear adverse consequences, might feel they have no choice but to agree…" SV.
- "This will be a particular issue for public authorities and employers." SV.
- "If you would still process the personal data on a different lawful basis even if consent were refused or withdrawn, then seeking consent from the individual is misleading and inherently unfair." Final clause SV.
"What is valid consent?", …/consent/what-is-valid-consent/ (page date 4 August 2026):
- "Consent means giving people genuine choice and control over how you use their data." SV.
- "If the individual has no real choice, consent is not freely given and it will be invalid." SV.
- "Freely given consent will also be more difficult to obtain in the context of a relationship where there is an imbalance of power – particularly for public authorities and employers." SV.
- "…there is no such thing as 'evolving' consent." SV.
- Research and withdrawal: "If you would not be able to fully action a withdrawal of consent – for example because deleting data would undermine the research and full anonymisation is not possible – then you should not use consent as your lawful basis (or condition for processing special category data). Consent is only valid if the individual is able to withdraw it at any time." SV for key fragments. "There is no exemption to this for scientific research." SV.
Consent guide at-a-glance, …/a-guide-to-lawful-basis/consent/ (page date 19 August 2026): "Consent means offering individuals real choice and control." SV. "Consent requires a positive opt-in." SV. "Make it easy for people to withdraw consent and tell them how." SV.
- Role: the regulator's own statement that consent is the wrong basis where withdrawal cannot be honoured.

3f. ICO legitimate interests.
URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/legitimate-interests/ (page date 23 March 2026; updated for DUAA)
- "Legitimate interests is one of the seven lawful bases in the UK GDPR." SV.
- "Legitimate interests is the most flexible lawful basis for processing personal information. But it won't always be the most appropriate." SV.
- "It's likely to be most appropriate where you use people's information: in ways they would reasonably expect; in ways that have a minimal impact on their privacy; or where there's a compelling justification for what you want to do." SV for each limb.
- "If you choose to rely on legitimate interests, you're taking on extra responsibility for considering and protecting people's rights and interests." SV.
- "There are three elements to the legitimate interests basis. For this three-part test, you must: identify a legitimate interest; show that the use of personal information is necessary to achieve it; and balance it against the interests, rights and freedoms of the person whose information you want to use." SV for the three limbs.
- "You should keep a record of your legitimate interests assessment (LIA) to help you demonstrate compliance if needed." SP.
- Detailed page (…/legitimate-interests/what-is-the-legitimate-interests-basis/, SP): purpose test "Do you have a legitimate interest for using the personal information?"; necessity test "Is your use of personal information necessary for that purpose?"; balancing test "Do the person's interests, rights or freedoms override the legitimate interest you've identified?".

3g. Objection and erasure.
Article 21, https://www.legislation.gov.uk/eur/2016/679/article/21
- 21(1): "The data subject shall have the right to object, on grounds relating to his or her particular situation, at any time to processing of personal data concerning him or her which is based on point (e) [(ea)] or (f) of Article 6(1), including profiling based on those provisions. The controller shall no longer process the personal data unless the controller demonstrates compelling legitimate grounds for the processing which override the interests, rights and freedoms of the data subject or for the establishment, exercise or defence of legal claims." SV for "on grounds relating to his or her particular situation" and "compelling legitimate grounds for the processing which override the interests, rights and freedoms of the data subject"; rest SP. "(ea)" inserted 5.2.2026 (SP).
- 21(6): "Where personal data are processed for scientific or historical research purposes or statistical purposes…, the data subject, on grounds relating to his or her particular situation, shall have the right to object to processing of personal data concerning him or her, unless the processing is necessary for the performance of a task carried out for reasons of public interest." Last clause SV. The former reference to Article 89(1) is omitted (shown as dots; F-note 5.2.2026, SP).
Article 17, https://www.legislation.gov.uk/eur/2016/679/article/17
- 17(1)(b): "the data subject withdraws consent on which the processing is based according to point (a) of Article 6(1), or point (a) of Article 9(2), and where there is no other legal ground for the processing". First clause SV.
- 17(2): "Where the controller has made the personal data public and is obliged pursuant to paragraph 1 to erase the personal data, the controller, taking account of available technology and the cost of implementation, shall take reasonable steps, including technical measures, to inform controllers which are processing the personal data that the data subject has requested the erasure by such controllers of any links to, or copy or replication of, those personal data." SP.
- 17(3)(d): "for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 84B in so far as the right referred to in paragraph 1 is likely to render impossible or seriously impair the achievement of the objectives of that processing". SV from "in so far as"; the "Article 84B" words SP.
ICO right to object, https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/right-to-object/ (25 March 2025; "under review"):
- "Where you are processing personal data for scientific or historical research, or statistical purposes, the right to object is more restricted." SV.
- "…the responsibility is for you to be able to demonstrate that your legitimate grounds override those of the individual." SV.
- "You have one calendar month to respond to an objection." SV.
ICO right to erasure, …/individual-rights/right-to-erasure/ (10 January 2025; "under review"):
- "The right is not absolute and only applies in certain circumstances." SV.
- Applies where "you are relying on consent as your lawful basis for holding the data, and the individual withdraws their consent". SV.
- Does not apply "for archiving purposes in the public interest, scientific research, historical research or statistical purposes where erasure is likely to render impossible or seriously impair the achievement of that processing". SV for the final clause.
- "Where personal data has been made public in an online environment reasonable steps should be taken to inform other controllers…" SV.

---------------------------------------------------------------
ITEM 4 — RESEARCH, STATISTICS AND ARCHIVING
---------------------------------------------------------------

4a. What happened to Article 89 and s.19.
- https://www.legislation.gov.uk/eur/2016/679/article/89 — "Art. 89 omitted (5.2.2026) by virtue of Data (Use and Access) Act 2025 (c. 18), ss. 86(4), 142(1); S.I. 2026/82, reg. 2(n)". SP.
- https://www.legislation.gov.uk/ukpga/2018/12/section/19 — "S. 19 and cross-heading omitted (5.2.2026)". SV. Also "S.I. 2026/82, reg. 2(n)" SV. No substantive text is shown. Banner (SP): up to date with changes in force on or before 24 September 2026.

4b. Chapter 8A, Articles 84A–84D. Statute. Inserted "19.6.2025 for specified purposes, 5.2.2026 in so far as not already in force" (SV) by DUAA s.86(2).
- 84A(1)–(2) (https://www.legislation.gov.uk/eur/2016/679/article/84A): "This Chapter makes provision about the processing of personal data— (a) for the purposes of scientific research or historical research, (b) for the purposes of archiving in the public interest, or (c) for statistical purposes." "Those purposes are referred to in this Chapter as 'RAS purposes'." SP.
- 84B (…/article/84B): "Personal data may only be processed for RAS purposes if— (a) the processing consists of the collection of the personal data (whether from the data subject or otherwise), (b) the processing is carried out in order to convert the personal data into information which can be processed in a manner which does not permit the identification of a data subject, or (c) without the processing, the RAS purposes cannot be fulfilled." "Processing of personal data for RAS purposes must be carried out subject to appropriate safeguards for the rights and freedoms of the data subject." SV, all limbs.
- 84C (…/article/84C):
  (2) "The requirement is not satisfied if the processing is likely to cause substantial damage or substantial distress to a data subject to whom the personal data relates." SV.
  (3) "The requirement is not satisfied if the processing is carried out for the purposes of measures or decisions with respect to a particular data subject to whom the personal data relates, except where the purposes for which the processing is carried out include the purposes of approved medical research." SV.
  (4) "The requirement is only satisfied if the safeguards include technical and organisational measures for the purpose of ensuring respect for the principle of data minimisation (see Article 5(1)(c)), such as, for example, pseudonymisation." SV in fragments.
- 84D (SP): "The Secretary of State may by regulations make further provision about when the requirement for appropriate safeguards under Article 84B(2) is, or is not, satisfied."
- Role: the two exclusions the brief asked about survive, now in the Regulation and in the same words as old s.19.

4c. New definitions in Article 4(2)–(7). Statute, inserted 5.2.2026 (F-notes SP: DUAA ss. 67(1)(b), 68(3); S.I. 2026/82 reg. 2(a), (b)).
- 4(2): "References in this Regulation to the processing of personal data for the purposes of scientific research (including references to processing for 'scientific research purposes') are references to processing for the purposes of any research that can reasonably be described as scientific, whether publicly or privately funded and whether carried out as a commercial or non-commercial activity." SV for "any research that can reasonably be described as scientific, whether publicly or privately funded" and "whether carried out as a commercial or non-commercial activity". The control "carried out by an accredited university or public body" returned NO.
- 4(3)(a): "include processing for the purposes of technological development or demonstration, fundamental research or applied research". SV.
- 4(3)(b): "only include processing for the purposes of a study in the area of public health that can reasonably be described as scientific where the study is conducted in the public interest". SP.
- 4(4): "…include processing for the purposes of genealogical research." SV.
- 4(5): "References in this Regulation to the processing of personal data for statistical purposes are references to processing for statistical surveys or for the production of statistical results where— (a) the information that results from the processing is aggregate data that is not personal data, and (b) the controller does not use the personal data processed, or the information that results from the processing, in support of measures or decisions with respect to a particular data subject…" Limbs (a) and (b) SV; opening words SP.
- 4(6), broad consent: "A data subject's consent is to be treated as falling within the definition of 'consent' in point (11) of paragraph 1 if— (a) it does not fall within that definition because (and only because) the consent is given to the processing of personal data for the purposes of an area of scientific research, (b) at the time the consent is sought, it is not possible to identify fully the purposes for which personal data is to be processed, (c) seeking consent in relation to the area of scientific research is consistent with generally recognised ethical standards relevant to the area of research, and (d) so far as the intended purposes of the processing allow, the data subject is given the opportunity to consent only to processing for part of the research". Limbs (b), (c), (d) SV; (a) SP.
- 4(7): "References in this Regulation to consent given for a specific purpose (however expressed) include consent described in paragraph 6". SV.
- ICO summary (organisations page, 19 June 2026): "it makes it clearer when you can use personal information for the purposes of scientific research, including commercial scientific research." SV. "It clarifies that people can give 'broad consent' to an area of scientific research." SV.

4d. ICO "The research provisions". Regulator guidance, pre-dating the 2025 Act.
Landing: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/the-research-provisions/ (page date 3 March 2026)
- "Due to changes made by the Data (Use and Access) Act, this guidance is under review and may be subject to change." SP. The ICO states it has consulted on updated RAS guidance (SP).
- The safeguards sub-page (9 October 2025) still cites the repealed provisions: "Article 89 of the UK GDPR says that use of the research provisions is dependent on you having appropriate safeguards in place." SP.
- "To use the provisions, you need to demonstrate that your processing is necessary for one of these research purposes." SV.
- "Scientific or historical research has a broad meaning." SV. "It can also include research carried out in commercial settings, and technological development, innovation and demonstration." SV.
- "We developed a set of indicative criteria for each of the three types of research." SV. "Although you do not need to meet all of these criteria, we would expect you to meet more than one." SP.
- Listed indicative activities and standards (all SP) include "Formulating hypotheses, isolating variables, designing experiments", "Critical exposure to scrutiny, including peer review", "Publication of findings", "Ethics guidance", "Committee approval".
- "Processing for statistical purposes is processing where the main objective is to generate statistics." SV. "It is important to note that not all processing that creates statistical results counts as processing for statistical purposes." Wording as returned by the check.
- The organisation should "not use the results to make decisions or justify measures about people". SV.
- Exclusions: "You are not allowed to use the research provisions if the processing is likely to cause someone substantial damage or substantial distress." SV. "You are not allowed to use the research provisions if you are carrying out the processing for the purposes of measures or decisions with respect to particular people, unless the research is approved medical research." SV.
- "This means you cannot rely on the research provisions if you are intending to use that data, and the results of your research, to make specific decisions about the people involved, or to inform the services you provide to them." Closest wording as returned by the check.
- "…substantial damage would include both material and non-material harms, such as: financial loss; economic or social disadvantage; physical harm; damage to reputation; loss of confidentiality; or deprivation of rights." "damage to reputation" SV; rest SP.
- "Substantial distress would include upset, emotional or mental pain. It goes beyond annoyance, irritation, or strong dislike." SV.
- "Where possible, you should carry out your research using anonymous information." SV.

4e. Does this cover a private studio's dashboard? What the sources say and do not say:
- The statute is neutral as to who the controller is (4(2): "whether publicly or privately funded… commercial or non-commercial").
- "Statistical purposes" is defined by output and use (4(5)(a)–(b)), not by who does it.
- The ICO page I read does not expressly exclude market research or business analytics; it applies indicative criteria.
- No source addresses dashboards.
- The special-category research condition additionally requires that processing "is in the public interest" (2b).
- Excluded in terms: processing likely to cause substantial damage or substantial distress; processing for measures or decisions about a particular data subject; and, per the ICO, use "to inform the services you provide to them".

---------------------------------------------------------------
ITEM 5 — DATA PROTECTION BY DESIGN; DPIA; PRIOR CONSULTATION; MINIMISATION; PURPOSE LIMITATION
---------------------------------------------------------------

5a. Article 25. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/25
- 25(1): the controller shall "implement appropriate technical and organisational measures, such as pseudonymisation, which are designed to implement data-protection principles, such as data minimisation, in an effective manner". SV.
- 25(2): "…by default, only personal data which are necessary for each specific purpose of the processing are processed." SV. "In particular, such measures shall ensure that by default personal data are not made accessible without the individual's intervention to an indefinite number of natural persons." SV.
- 25(1A)–(1B) are new; see Item 8.

5b. Article 35. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/35
- 35(1): "Where a type of processing in particular using new technologies, and taking into account the nature, scope, context and purposes of the processing, is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data." SV from "is likely to result in a high risk" to "carry out an assessment"; rest SP.
- 35(3)(b): "processing on a large scale of special categories of data referred to in Article 9(1)…". SV.
- 35(3)(c): "a systematic monitoring of a publicly accessible area on a large scale". SV.
- 35(7): (a) "a systematic description of the envisaged processing operations and the purposes of the processing, including, where applicable, the legitimate interest pursued by the controller"; (b) "an assessment of the necessity and proportionality of the processing operations in relation to the purposes"; (c) "an assessment of the risks to the rights and freedoms of data subjects referred to in paragraph 1"; (d) "the measures envisaged to address the risks, including safeguards, security measures and mechanisms to ensure the protection of personal data and to demonstrate compliance with this Regulation". (a), (b), (d) SV in fragments; (c) SP.
- 35(9): "Where appropriate, the controller shall seek the views of data subjects or their representatives on the intended processing, without prejudice to the protection of commercial or public interests or the security of processing operations." SP. Relevant to the chapter's "who may speak for a community".

5c. ICO list of processing "likely to result in high risk". Regulator guidance; the Article 35(4) list.
URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/examples-of-processing-likely-to-result-in-high-risk/ (page date 19 November 2024; "under review")
- "The following list details processing operations for which the ICO requires you to complete a DPIA as they are 'likely to result in high risk'." SV.
Items that match a public dashboard on their face:
- Innovative technology: "Processing involving the use of new technologies, or the novel application of existing technologies (including AI)." SV.
- Data matching: "Combining, comparing or matching personal data obtained from multiple sources." SV.
- Invisible processing: "Processing of personal data that has not been obtained direct from the data subject in circumstances where the controller considers that compliance with Article 14 would prove impossible or involve disproportionate effort." SV. Examples (SP) include "Data aggregation/data aggregation platforms" and "Re-use of publicly available data".
- Tracking: "Processing which involves tracking an individual's geolocation or behaviour, including but not limited to the online environment." SV. Examples (SP) include "Social networks, software applications" and "Web and cross-device tracking".
- Targeting of children or other vulnerable individuals: "The use of the personal data of children or other vulnerable individuals for marketing purposes, profiling or other automated decision-making, or if you intend to offer online services directly to children." SV.
- Risk of physical harm: "Where the processing is of such a nature that a personal data breach could jeopardise the [physical] health or safety of individuals." SV.
- Large-scale profiling: "Any profiling of individuals on a large scale." SV.
- Qualifier (SP): innovative technology, biometric, genetic, invisible processing and tracking carry "when combined with any other criterion from WP248rev01". Data matching, large-scale profiling, targeting and risk of physical harm were not reported as carrying it.
- Companion page (SP): "If in any doubt, we would always recommend that you do a DPIA to ensure compliance and encourage best practice."

5d. ICO DPIA steps.
URL: …/data-protection-impact-assessments-dpias/how-do-we-do-a-dpia/ (page date 18 February 2026; "under review")
- "Step 1: identify the need for a DPIA; Step 2: describe the processing; Step 3: consider consultation; Step 4: assess necessity and proportionality; Step 5: identify and assess risks; Step 6: identify measures to mitigate the risks; Step 7: sign off and record outcomes". Steps 3, 4 and 7 SV; the others listed consistently on two passes.
- "You should seek and document the views of individuals (or their representatives) unless there is a good reason not to." SV.
- "If there is still a high risk, you need to consult the ICO before you can go ahead with the processing." SV.
- "To aid transparency and accountability, it is good practice to publish your DPIA." SP.

5e. Article 36, prior consultation. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/36
- 36(1): "The controller shall consult the Commission prior to processing where a data protection impact assessment under Article 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk." SV in two fragments. The control "consult the Commissioner" returned NO.
- 36(2): the Commission "shall, within period of up to eight weeks of receipt of the request for consultation, provide written advice to the controller…". SV. "That period may be extended by six weeks…". SV.
- 36(3) (paraphrase, SP): the controller supplies responsibilities, purposes and means, safeguards, DPO contact, the DPIA, and anything else requested.

5f. Minimisation and purpose limitation, one sentence each.
URL: https://www.legislation.gov.uk/eur/2016/679/article/5
- 5(1)(c): "adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed". SV.
  ICO (9 September 2025; SP): "adequate – sufficient to properly fulfil your stated purpose; relevant – has a rational link to that purpose; and limited to what is necessary – you do not hold more than you need for that purpose."
- 5(1)(b): "collected (whether from the data subject or otherwise) for specified, explicit and legitimate purposes and not further processed by or on behalf of a controller in a manner that is incompatible with the purposes for which the controller collected the data". SV in two fragments. This is amended wording; the old research-compatibility clause is gone (control NO).
  ICO (23 March 2026, updated for DUAA; SP): "You must only reuse the personal information for a new purpose if this is compatible with your original purpose. The rules on this are slightly different depending on whether you originally collected the information under the consent lawful basis."
- New 5(3): "For the avoidance of doubt, processing is not lawful by virtue only of being processing in a manner that is compatible with the purposes for which the personal data was collected." SV.
- 5(1)(e) (SP): longer storage allowed "solely for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes in accordance with Article 84B".

---------------------------------------------------------------
ITEM 6 — TRANSPARENCY AND "PUBLIC" DATA
---------------------------------------------------------------

6a. Article 14, data not obtained from the data subject. Statute, amended 5.2.2026.
URL: https://www.legislation.gov.uk/eur/2016/679/article/14
- 14(1): "Where personal data have not been obtained from the data subject, the controller shall provide the data subject with the following information:". SP.
- 14(3)(a): "within a reasonable period after obtaining the personal data, but at the latest within one month…". SV.
- 14(5)(b) is omitted (F-note, SP: DUAA ss. 77(2)(a)(ii), 142(1); S.I. 2026/82 reg. 2(i)). The old wording ("in particular for processing for archiving purposes in the public interest…") returned NO.
- 14(5)(e): "providing the information is impossible or would involve a disproportionate effort". SV.
- 14(5)(f): "the obligation referred to in paragraph 1 is likely to render impossible or seriously impair the achievement of the objectives of the processing for which the personal data are intended." SP.
- 14(6): "For the purposes of paragraph 5(e), whether providing the information would involve a disproportionate effort depends on, among other things, the number of data subjects, the age of the personal data and any appropriate safeguards applied to the processing." SV from "whether providing".
- 14(7): "A controller relying on paragraph 5(e) or (f) must take appropriate measures to protect the data subject's rights, freedoms and legitimate interests, including by making the information available publicly." SV.

6b. Article 13(5)–(6), new. Statute (F-note SP: DUAA s.77(1)(b); 5.2.2026).
URL: https://www.legislation.gov.uk/eur/2016/679/article/13
- "Paragraph 3 does not apply to the extent that— (a) the controller intends to further process the personal data— (i) for (and only for) the purposes of scientific or historical research, the purposes of archiving in the public interest or statistical purposes, and (ii) in accordance with Article 84B, and (b) providing the information is impossible or would involve a disproportionate effort." SV for the opening words, (a)(i) and (b); (a)(ii) SP.

6c. Article 8A(3)–(4), purpose limitation and further processing. Statute (inserted "19.6.2025 for specified purposes, 5.2.2026 in so far as not already in force"; DUAA s.71(5); SP).
URL: https://www.legislation.gov.uk/eur/2016/679/article/8A
- 8A(3): "Processing of personal data for a new purpose is to be treated as processing in a manner compatible with the original purpose where— … (b) the processing is carried out in accordance with Article 84B— (i) for the purposes of scientific research or historical research, (ii) for the purposes of archiving in the public interest, or (iii) for statistical purposes…". Opening words and "the processing is carried out in accordance with Article 84B" SV.
- 8A(4): "Where the controller collected the personal data based on Article 6(1)(a) (data subject's consent), processing for a new purpose is only processing in a manner compatible with the original purpose if— (a) it falls within paragraph 3(a) or (c), or (b) it falls within paragraph 3(d) or (e) and the controller cannot reasonably be expected to obtain the data subject's consent." SV, all three parts. The control "it falls within paragraph 3(b)" returned NO.
- On its face, data collected on consent is excluded from the research and statistics compatibility route.

6d. ICO right to be informed, exceptions. Regulator guidance, pre-DUAA wording.
URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/are-there-any-exceptions/ (page date 22 September 2025; "under review")
- "There is no automatic exception from the right to be informed just because the personal data is in the public domain." SV.
- "This is an exception to the general obligation of transparency, and should be treated as the exception, not the rule." SV.
- "The more significant the effect, the less likely you will be able to rely on this exception." SV.
- "If you determine that providing privacy information to individuals does involve a disproportionate effort, you must still publish the privacy information (eg on your website), and you should carry out a DPIA." SV from "you must still publish".
- "Situations in which it is impossible to provide privacy information to individuals are few and far between." SV.
- The page still frames the factors as applying "(particularly if you use personal data for archiving or research purposes)" (SP). That is superseded by Article 14(6).
- Companion page (…/what-privacy-information-should-we-provide/, 15 January 2026; SP): "Tell people where you obtained their information from." "If it was from a publicly accessible source you must say this."

6e. Publicly available data, general principle only.
- ICO statement accompanying the joint statement on data scraping, 24 August 2023, https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2023/08/joint-statement-on-data-scraping-and-data-protection/ — "Organisations must have a lawful reason for collecting and using people's data, even when it is publicly available." SV. Attributed on the page to Stephen Bonner, ICO Deputy Commissioner for Regulatory Supervision. This is a regulator's statement, not guidance. The joint statement's own "most jurisdictions" sentence was not present on this page (checked NO).
- ICO response to the generative AI consultation series, executive summary, https://ico.org.uk/about-the-ico/what-we-do/our-work-on-artificial-intelligence/response-to-the-consultation-series-on-generative-ai/executive-summary/ (page date 13 October 2025; the original publication date is not stated on the page as fetched): "Web scraping is a large-scale processing activity that often occurs without people being aware of it. This sort of invisible processing poses particular risks to people's rights and freedoms." SV, both sentences. No sentence containing "publicly" was found on that page.

---------------------------------------------------------------
ITEM 7 — COOKIES AND ANALYTICS (PECR)
---------------------------------------------------------------

7a. PECR regulation 6, substituted 5 February 2026 by DUAA s.112(2) (S.I. 2026/82 reg. 2(w)). Statute.
URL: https://www.legislation.gov.uk/uksi/2003/2426/regulation/6
- 6(1): "Subject to Schedule A1, a person must not store information, or gain access to information stored, in the terminal equipment of a subscriber or user." SP.
- 6(2) (SP): references to gaining access include "collecting or monitoring information automatically emitted by the terminal equipment".

7b. PECR Schedule A1, exceptions. In force. F-note (SP): "Sch. A1 inserted (5.2.2026) by Data (Use and Access) Act 2025 (c. 18), s. 142(1), Sch. 12; S.I. 2026/82, reg. 2(z13)".
URL: https://www.legislation.gov.uk/uksi/2003/2426/schedule/A1
- Cross-headings (SP on numbering): para 2 Consent; para 3 Transmission of a communication…; para 4 "Storage or access strictly necessary to provide an information society service"; para 5 "Collecting information for statistical purposes"; para 6 "Website appearance etc"; para 7 Emergency assistance.
- Para 4: "the storage or access is strictly necessary for the provision of an information society service requested by the subscriber or user". SV.
- Para 5(1): regulation 6(1) does not prevent storage or access if "(a) the person provides an information society service, (b) the sole purpose of the storage or access is to enable the person— (i) to collect information for statistical purposes about how the service is used with a view to making improvements to the service, or (ii) to collect information for statistical purposes about how a website by means of which the service is provided is used with a view to making improvements to the website, (c) any information that the storage or access enables the person to collect is not shared with any other person except for the purpose of enabling that other person to assist with making improvements to the service or website, (d) the subscriber or user is provided with clear and comprehensive information about the purpose of the storage or access, and (e) the subscriber or user is given a simple means of objecting, free of charge, to the storage or access and does not object." SV for (b)(i), (c), (d), (e); (a) and (b)(ii) SP.

7c. ICO "Guidance on the use of storage and access technologies". Regulator guidance.
Landing: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guidance-on-the-use-of-storage-and-access-technologies/ — "29 April 2026 - we have finalised this guidance following two consultations on the draft guidance…" (SP).
Exceptions page: …/what-are-the-exceptions/ (page date 29 April 2026)
- "There are five exceptions to the prohibition on storing or accessing information on people's devices." SV.
- Strictly necessary: "This means that without it the service couldn't be provided on a technical level." SV. "There are no advertising purposes that meet the strictly necessary exception." SV. "…you should assess 'strictly necessary' from the point of view of the subscriber or user, not your own." SP.
- "The exception is essentially for analytics purposes." SV. "However, it is not a broad exception that covers all types of analytics technologies or ways you can use them." SV.
- "It is about how your service is used, not about who uses it." SV.
- "It is not for identifying, tracking or monitoring people or groups of people who use your service." SV.
- "You must ensure that the information resulting from the storage or access is aggregate statistical information that you cannot use to identify people." SV.
- Consent is needed if you "make inferences or take decisions about people (or categories of people) based on information like their IP address…" (SV) or for "tracking or profiling individual visitors or categories of visitors" (SV).
- "Provided your use of storage and access technologies for this purpose is in line with the exception, you don't need to get consent under PECR." SP.
- Third-party analytics: "your third party provider must be a processor, not a joint controller". SP.
- "The statistical purposes exception does not apply to collecting or monitoring information automatically emitted by terminal equipment, such as wifi probe requests." SP.
- The ICO's example 2 (segmenting visitors "by demographic, including age group and gender" to decide what content to promote) "cannot rely on the statistical purposes exception". SP.
- ICO DUAA summary: "it allows you to set some types of cookies without having to get consent, such as those you may use to collect information for statistical purposes and improve the functionality of your website." SV.
- I did not find a statement on PECR penalty levels on the pages read.

---------------------------------------------------------------
ITEM 8 — CHILDREN
---------------------------------------------------------------

8a. ICO Age Appropriate Design Code (Children's Code). Statutory code of practice under DPA 2018 s.123.
Services covered: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/services-covered-by-this-code/ (page date 5 December 2024)
- "This code applies to 'information society services likely to be accessed by children' in the UK… It is not restricted to services specifically directed at children." Last sentence SV; rest SP.
- ISS definition as quoted by the ICO: "any service normally provided for remuneration, at a distance, by electronic means and at the individual request of a recipient of services". SV.
- "This code also covers not-for-profit apps, games and educational sites, as long as those services can be considered as 'economic activity' in a more general sense." SV.
- "If your website just provides information about your real-world business, but does not allow customers to buy products online or access a specific online service, it is not an ISS." SV.
- The test: "We consider that for a service to be 'likely' to be accessed, the possibility of this happening needs to be more probable than not. This recognises the intention of Parliament to cover services that children use in reality, but does not extend the definition to cover all services that children could possibly access." SV for the two key strings.
- "…whether your service is likely to be accessed by children or not is likely to depend on: the nature and content of the service and whether that has particular appeal for children; and the way in which the service is accessed and any measures you put in place to prevent children gaining access." SP.
- "…evidence later emerges that a significant number of children are in fact accessing your service…". SV.
- "A child is defined in the UNCRC and for the purposes of this code as a person under 18." SP.
The 15 standards (…/code-standards/, page date 2 December 2024; names listed on two consistent passes): 1 Best interests of the child; 2 Data protection impact assessments; 3 Age appropriate application; 4 Transparency; 5 Detrimental use of data; 6 Policies and community standards; 7 Default settings; 8 Data minimisation; 9 Data sharing; 10 Geolocation; 11 Parental controls; 12 Profiling; 13 Nudge techniques; 14 Connected toys and devices; 15 Online tools.
- Standard 10: "Switch geolocation options off by default (unless you can demonstrate a compelling reason for geolocation to be switched on by default, taking account of the best interests of the child). Provide an obvious sign for children when location tracking is active. Options which make a child's location visible to others must default back to 'off' at the end of each session." SV, all three sentences.
- Standard 12: "Switch options which use profiling 'off' by default (unless you can demonstrate a compelling reason for profiling to be on by default, taking account of the best interests of the child). Only allow profiling if you have appropriate measures in place to protect the child from any harmful effects (in particular, being fed content that is detrimental to their health or wellbeing)." SV for the opening words and the second sentence.

8b. Article 25(1A)–(1B), new statutory duty. Inserted 5.2.2026 (DUAA s.81(2); S.I. 2026/82 reg. 2(k); SP).
- "In the case of processing carried out in the course of providing information society services which are likely to be accessed by children, when assessing what are appropriate technical and organisational measures in accordance with paragraph 1, the controller must take into account the children's higher protection matters." SV in two fragments.
- "The children's higher protection matters are— (a) how children can best be protected and supported when using the services, and (b) the fact that children— (i) merit specific protection with regard to their personal data because they may be less aware of the risks and consequences… and (ii) have different needs at different ages and at different stages of development." (a) and (b)(ii) SV; (b)(i) SP.
- ICO gloss: "if you provide an online service that is likely to be used by children, the DUAA explicitly requires you to take their needs into account…" SV. "You should already satisfy this requirement if you conform to our Age appropriate design code (AADC)." SV.

8c. Online Safety Act 2023, overlap only. Ofcom's pages returned 404 at both URLs tried; I read the statute instead.
URL: https://www.legislation.gov.uk/ukpga/2023/50/section/35 (page notes pending amendments from "2026 c. 20" not yet applied — SP; for Agent D to check)
- One sentence: a "children's access assessment" is an assessment of a Part 3 service "to determine whether it is possible for children to access the service or a part of the service" and, if so, whether "the child user condition is met". First quoted clause SV.
- The child user condition is met if "there is a significant number of children who are users of the service or of that part of it" or the service "is of a kind likely to attract a significant number of users who are children". Both SV.
- A provider may only conclude access is not possible "if age verification or age estimation is used on the service with the result that children are not normally able to access the service or that part of it". SV.
- s.36(1) (SP): "A provider of a Part 3 service must carry out the first children's access assessment at a time set out in, or as provided by, Schedule 3."
- Overlap: both regimes use "likely to be accessed by children" but with different tests. The ICO's is "more probable than not" for any ISS; the OSA's is the "significant number" condition for Part 3 (user-to-user and search) services only, "based on evidence about who actually uses a service, rather than who the intended users of the service are" (SV). The phrase "more probable than not" does not appear in s.35 (checked NO).

---------------------------------------------------------------
ITEM 9 — ENFORCEMENT SCALE AND CASES (context only)
---------------------------------------------------------------

9a. Article 83 maxima. Statute.
URL: https://www.legislation.gov.uk/eur/2016/679/article/83
- 83(5): "£17,500,000, or in the case of an undertaking, up to 4 % of the total worldwide annual turnover of the preceding financial year, whichever is higher". SV. Covers "the basic principles for processing, including conditions for consent, pursuant to Articles 5, 6, 7 and 9" (SV) and "the data subjects' rights pursuant to Articles 12 to 21" (wording as returned by the check). A new point (ba) covers Articles 22B and 22C (SP).
- 83(4): "£8,700,000, or in the case of an undertaking, up to 2 % of the total worldwide annual turnover of the preceding financial year, whichever is higher". SV. Covers controller and processor obligations, including Articles 25 and 35.

9b. Home Office GPS monitoring pilot — enforcement notice and warning, 1 March 2024. ICO's own announcement; read for the legal point only.
URL: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/03/ico-finds-the-home-office-s-pilot-of-gps-electronic-monitoring-of-migrants-breached-uk-data-protection-law/
- The Home Office "failed to sufficiently assess the privacy intrusion of the continuous collection of people's location information". SV.
- "Having access to a person's 24/7 movements is highly intrusive, as it is likely to reveal a lot of information about them, including the potential to infer sensitive information such as their religion, sexuality, or health status." SV in two fragments. Attributed to John Edwards, Information Commissioner.
- Legal point: the regulator treats continuous location data as capable of revealing special-category characteristics by inference, and treats a failure to assess this in a DPIA as an infringement in its own right. No fine.

9c. 23andMe — monetary penalty £2.31 million, 17 June 2025. ICO's own announcement.
URL: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/06/23andme-fined-for-failing-to-protect-uk-users-genetic-data/
- "£2.31 million" SV. "155,592" UK residents SV.
- "The penalty follows a joint investigation conducted by the ICO and the Office of the Privacy Commissioner of Canada." SP.
- "The combination of personal information that could be found in 23andMe accounts, such as post codes, race, ethnic origin, familial connections, and health data could potentially be exploited by malicious actors for financial gain, surveillance or discrimination." SV in two fragments.
- Legal point: a security failing; the regulator names postcode combined with ethnicity as a discrimination and surveillance vector.

9d. Not reached.
- Easylife Ltd (the ICO's 2022 action concerning health conditions inferred from purchases): three ICO URLs returned 404. Nothing quoted.
- The ICO enforcement listing page loads its records by script and could not be read.

---------------------------------------------------------------
FOLLOW-THREADS REQUESTED
---------------------------------------------------------------
- ICO on anonymisation of location data: I found no dedicated ICO passage in the 2025 guidance pages read. "Location data" appears only as a listed identifier. The clearest ICO statement on location and inference is the Home Office quotation (9b). PECR's own "location data" rules were not read.
- ICO on small communities or minority groups: no dedicated statement found. The closest are the motivated-intruder passage "Identifiability risk can arise where one person or group knows a great deal about another person" (SV), the FOI review example (religious belief, shrinking counts, a high-profile event raising motivation), and the special-category "other people could (rightly or wrongly) infer" passage.
- ONS method (SP throughout; method only): "Protecting personal data in Census 2021 results", released 9 March 2023, https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/protectingpersonaldataincensus2021results
  - Targeted record swapping: "Households and their individuals that are unique or rare on one or more of those characteristics are highlighted as 'risky records', and all these households would be swapped."
  - Cell-key perturbation: "A typical dataset would have around 14% of cell counts perturbed by a small amount."
  - Plus disclosure checks on variable combinations.
  - The page mentions "ethnic group or country of birth, where minority population groups might be geographically clustered".
  - The reader found no specific mention of sexual orientation or gender identity on that page.
- DUAA commencement timetable as of today: see 3c. Data-protection and PECR provisions have been in force since 5 February 2026 (the ICO says all are now in force); the Information Commission took over on 30 September 2026.

---------------------------------------------------------------
UNEXPECTED FINDINGS
---------------------------------------------------------------
1. Article 89 and DPA s.19 are repealed. Any chapter text citing "Article 89 safeguards" or "s.19" is now wrong; the cite is Articles 84A–84C. The ICO's research guidance had not caught up on the pages I read (dated 2025, "under review", still citing Article 89 and s.19).
2. The regulator changed legal identity six days before the read date. The UK GDPR now reads "the Commission" (Article 36 SV), by S.I. 2026/1015 and S.I. 2026/386. The gov.uk commencement page (last updated 5 February 2026) still says the governance change was "expected in early 2026".
3. Article 8A(4): data collected on consent cannot use the research and statistics "compatible purpose" route. A contributed-data design that starts on consent stays on consent for re-use.
4. Article 14's research-specific exemption is gone. The general "disproportionate effort" exemption now carries a statutory duty (14(7)) to take protective measures "including by making the information available publicly".
5. The ICO's inference test is intention-based, not confidence-based ("regardless of how confident you are"). The "reasonable degree of certainty" wording the brief anticipated is not on the current page.
6. The ICO separates an "educated guess" from disclosure ("Even if a guess based on anonymous information is correct, this does not mean that a disclosure of personal data has happened"). This is the regulator's own line between group-level inference and personal-data disclosure. The special-category guidance sends the residual risk to fairness, not to Article 9.
7. The PECR analytics exception excludes exactly what a dashboard-builder might want from its own site analytics: "It is about how your service is used, not about who uses it"; no "categories of people"; the demographic-segmentation example fails; wifi probe collection is excluded.
8. Two smaller points. The ICO now counts "seven lawful bases" and its consent page still says "six others" besides consent. The ICO cites the NHS k = 5 standard as its only numeric anchor and gives no small-number threshold of its own.

---------------------------------------------------------------
LEFT OUT, AND WHY
---------------------------------------------------------------
- The journalism, academic, art and literature "special purposes" exemption (DPA 2018 Sch 2 Part 5). Not in my item list, but plausibly relevant to a studio that publishes; not researched. Flag for the lead.
- Article 10 criminal-offence data; the re-identification offences in DPA 2018 (the ICO pseudonymisation page mentions "two criminal offences", not read at source).
- Automated decision-making (Articles 22A–22D), international transfers, DSAR mechanics, the new complaints duty (DUAA s.103).
- EU-level material (EDPB, CJEU) on relative anonymisation: not UK law.
- The WP248rev01 nine criteria at source; the ICO DPIA template file; the ICO data sharing code.
- The ICO anonymisation accountability/governance page and glossary: time.
- Ofcom guidance: 404 twice. The ICO "plans for new and updated guidance" entries: script-loaded, unreadable. Easylife: unreachable.
- Article 6 commencement: the reader gave both 19.6.2025 and 5.2.2026 for point (ea); the F-note cites S.I. 2026/82 (5 February 2026). Treat the exact date for (ea) as SP.

---------------------------------------------------------------
RICH REFERENCES
---------------------------------------------------------------
1. ICO, "How do we ensure anonymisation is effective?" (guidance published 28 March 2025; under review) — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/how-do-we-ensure-anonymisation-is-effective/ — spectrum, motivated intruder, release model, inference, educated guesses, k-anonymity, review triggers.
2. UK GDPR as amended, Articles 4(2)–(7), 8A and Chapter 8A (84A–84D), legislation.gov.uk — the post-2025 research, statistics and consent architecture.
3. ICO, storage and access technologies, "What are the exceptions?" (finalised 29 April 2026) — the only fully post-DUAA ICO guidance in this set, with worked examples of where aggregate analytics tips into profiling.

---------------------------------------------------------------
WHAT SURPRISED ME
---------------------------------------------------------------
- How much of the statutory ground moved between February and September 2026, and how unevenly the regulator's guidance has followed. Most ICO pages read carry "under review and may be subject to change"; the lawful-basis, purpose-limitation and cookies pages are updated; the research, consent, DPIA, transparency and special-category pages are not.
- The ICO's two inference passages pull in different directions. For anonymisation, a correct guess about a person from anonymous data is not a disclosure. For special category data, a deliberate inference is Article 9 processing however uncertain. On the regulator's own wording, what separates the two is the controller's intention and whether the inference attaches to an identifiable person.
- The new statutory definition of "statistical purposes" requires that the result is "aggregate data that is not personal data". The anonymisation question and the statistics question have become the same question.

---

## Agent C — Consent, voice and governance at community level

CHAPTER 10 — FACET: CONSENT, VOICE AND GOVERNANCE AT COMMUNITY LEVEL
All fetches 6 October 2026.

TOOLS. WebSearch was unavailable (shared search budget exhausted). Everything came from direct URLs through WebFetch. Direct curl was blocked by the proxy, so "STRING-VERIFIED" means a second WebFetch pass with a YES/NO presence prompt and a false control string. In every check reported here the control came back NO, except the FDA document, which stayed unstable (see item 1).

Marks: SV = STRING-VERIFIED; SP = SINGLE PASS; ABSTRACT = abstract only reached.

--------------------------------------------------------------------
ITEM 1 — COLLECTIVE CONSENT AND COMMUNITY CONSULTATION
--------------------------------------------------------------------

1a. Belmont Report (US National Commission, April 18, 1979). Founding ethics statement.
https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html
- Principles (Part B): Respect for Persons; Beneficence; Justice (names SP).
- "Respect for persons incorporates at least two ethical convictions: first, that individuals should be treated as autonomous agents, and second, that persons with diminished autonomy are entitled to protection." SV (two fragments).
- Beneficence: "...but also by making efforts to secure their well-being" SV; "(1) do not harm and (2) maximize possible benefits and minimize possible harms" SV.
- Justice: "Who ought to receive the benefits of research and bear its burdens?" SV; "This is a question of justice, in the sense of "fairness in distribution" or "what is deserved."" SV.
- Groups appear only as classes of subjects: "Certain groups, such as racial minorities, the economically disadvantaged, the very sick, and the institutionalized may continually be sought as research subjects" SV.
- It contains no collective-consent provision (control string NO).
Role: the baseline is individualist; community appears only as a fairness-of-selection problem.

1b. ESRC Framework for Research Ethics, "Our core principles" (UKRI; page last updated 12 May 2025). Funder guidance.
https://www.ukri.org/councils/esrc/guidance-for-applicants/research-ethics-guidance/framework-for-research-ethics/our-core-principles/
"Our six key principles" (SP for that phrase). All six SV:
- "research should aim to maximise benefit for individuals and society and minimise risk and harm"
- "the rights and dignity of individuals and groups should be respected"
- "wherever possible, participation should be voluntary and appropriately informed"
- "research should be conducted with integrity and transparency"
- "lines of responsibility and accountability should be clearly defined"
- "independence of research should be maintained and where conflicts of interest cannot be avoided they should be made explicit"
"Groups" appears once, in principle 2. Nothing on collective consent on this page or the consent page (item 5).
Role: the UK funder's framework names groups as rights-holders and gives no mechanism.

1c. "Community-based participatory research: A guide to ethical principles and practice" (Centre for Social Justice and Community Action, Durham University, and NCCPE, November 2012). Practitioner framework.
https://www.publicengagement.ac.uk/sites/default/files/2023-08/cbpr_ethics_guide_web_november_2012.pdf
- Seven principles, names SV: Mutual respect; Equality and inclusion; Democratic participation; Active learning; Making a difference; Collective action; Personal integrity. One-line glosses were SP with ellipses; not safe to quote.
- "Sometimes it is not only the consent of individual people that is required, but also collective consent (e.g. of a community, group or organisation)." SV. Next sentence (SP): "It is also important to acknowledge that the purpose and uses of the research may change and develop over time, so consent may need to be continually reviewed and renegotiated, especially as specific plans for publication and dissemination are developed."
- "It may also be advisable to give organisations and places different names, as using real names may help identify people." SV.
- No sentence contains "withdraw" (SP). The NCCPE page says a 2nd edition exists; I did not fetch it.
- Not reached: ICPHR Position Paper 2 (404) and Banks et al. 2013 (tandfonline 403). This guide carries the seven names the brief lists.
Role: the one UK practitioner text found that names collective consent in terms, and ties it to renegotiation over time.

1d. Havasupai — Garrison 2013, Science, Technology, & Human Values 38(2):201–223. Peer-reviewed. ABSTRACT.
https://journals.sagepub.com/doi/10.1177/0162243912470009
- "In 2004, the Havasupai Tribe filed a lawsuit against the Arizona Board of Regents and Arizona State University (ASU) researchers upon discovering their DNA samples, initially collected for genetic studies on type 2 diabetes, had been used in several other genetic studies." SV
- "The lawsuit reached a settlement in April 2010 that included monetary compensation and return of DNA samples to the Havasupai but left no legal precedent for researchers." SV
- Finding (SP): interviewees "perceived no direct impact from the Havasupai case on their work"; where they did, it was "the perceived need to safeguard themselves by obtaining broad consent or shying away from research with indigenous communities altogether".
Role: the secondary-use harm case; it settled without precedent, and the reported reaction was avoidance.

1e. Dickert & Sugarman 2005, "Ethical goals of community consultation in research", American Journal of Public Health 95(7):1123–1127, DOI 10.2105/AJPH.2004.058933. Peer-reviewed, open in PMC.
https://pmc.ncbi.nlm.nih.gov/articles/PMC1449329/
- "Community consultation should not be mistaken for community consent, although the 2 are not mutually exclusive." SV
- "Consulting with a community includes eliciting feedback, criticism, and suggestions; it does not include asking for approval or permission." SV
- "For community consent to be valid, there must be a legitimate political system in place, with representatives properly empowered to make such decisions on behalf of the community." SV
- "Disease-based communities and many social groups typically lack a political structure, which makes community consent inappropriate." SV
- "Community consent may occur after community consultation and does not obviate the need for individual consent." SP. "Rather, the community decides whether to permit investigators to solicit participation from community members." SV
- Four goals (fragments SV): "Enhance protections for subjects and communities by identifying risks or hazards that were not previously appreciated"; enhanced benefits (SP); "Confer ethical/political legitimacy by giving those parties with an interest or stake in the proposed research the opportunity to express their views and concerns"; "Consulted communities may bear some degree of moral responsibility for the research project".
- "Community consultation must be tailored to the communities in which it is conducted" SV.
Role: the clearest statement of what community consent can and cannot be. It fills the gap left by Weijer & Emanuel.

1f. Weijer & Emanuel 2000 (Science 289:1142). UNREACHABLE: PubMed returned an empty shell, science.org 403, Europe PMC 429, NCBI eutils robots-disallowed. Nothing quoted.

1g. "Community consultation" — a regulator's definition. FDA guidance "Exception from Informed Consent Requirements for Emergency Research" (March 2011, updated April 2013).
https://www.fda.gov/media/80554/download
UNSTABLE; do not quote. The first pass produced a definition and a "not equivalent to… approval" sentence that both failed the presence check, and three further passes gave inconsistent wording. Only confirmed: a question reading «Is community consultation the same as "community consent" for the study?» (SV), a question on "representatives of the community" citing 21 CFR 50.24(a)(7)(i) (SV), and the phrase "substitute for individual informed consent" (SV). NIH/CDC definitions not fetched.

1h. Plain statements that a community cannot consent for its members (not asked for):
- UNESCO Universal Declaration on Bioethics and Human Rights, Article 6(3), adopted 19 October 2005 (General Conference, 33rd session). International soft law.
https://www.unesco.org/en/legal-affairs/universal-declaration-bioethics-and-human-rights
"In appropriate cases of research carried out on a group of persons or a community, additional agreement of the legal representatives of the group or community concerned may be sought." SV
"In no case should a collective community agreement or the consent of a community leader or other authority substitute for an individual's informed consent." SV
- CIOMS International Ethical Guidelines 2016, Guideline 9 commentary, "Individual informed consent and access to research populations" (heading SP). International standard.
https://cioms.ch/wp-content/uploads/2017/01/WEB-CIOMS-EthicalGuidelines.pdf (read at offset 60000)
"In no case, however, may the permission of a community leader or other authority substitute for individual informed consent." SV
Lead-in (SP): "...only after obtaining permission from an institution such as a school or a prison, or from a community leader, a council of elders, or another designated authority. Such institutional procedures or cultural customs should be respected."
Guideline 7 opens: "Researchers, sponsors, health authorities and relevant institutions should engage potential participants and communities in a meaningful participatory process" SV. Commentary names "community leaders and representatives, relevant NGOs and advocacy groups" SV.
No source fetched says in terms that communities "cannot consent in the legal sense but can be consulted and can govern". The nearest verified wording is these three: UNESCO and CIOMS (community agreement is additional, never a substitute) and Dickert & Sugarman (valid only with a legitimate political system).

--------------------------------------------------------------------
ITEM 2 — INDIGENOUS DATA SOVEREIGNTY AS MODEL, AND THE CARE IN BORROWING IT
--------------------------------------------------------------------

2a. Carroll et al. 2020, Data Science Journal 19:43. Peer-reviewed, open.
https://datascience.codata.org/articles/10.5334/dsj-2020-043
- Who it is for: "The CARE Principles are people– and purpose-oriented, reflecting the crucial role of data in advancing innovation, governance, and self-determination among Indigenous Peoples" SV
- "an assertion of the rights and interests of Indigenous Peoples in relation to data about them, their territories, and their ways of life" SV
- "Indigenous Peoples retain their rights to self-determine their forms of collective governance and rules of membership" SV
- Beyond Indigenous contexts (conclusion): "...have broader implications for other marginalized populations, highlighting the importance of local and group control for the quality and reproducibility of research and data" SV
- "Furthermore, the CARE Principles address issues of relevance for many populations (e.g., privacy, future use, reuse, stewardship), to the extent that the Principles provide a normative foundation for setting standards, crafting policy, and developing research agendas in relation to data acquired about populations as collectives." SV (three fragments; "Furthermore," SP)
- "Those populations might be minority groups, distinctive communities, or other collectives wanting to maintain high levels of trust and accountability in the use of data about their communities." SV
- Grounding (SP): "UNDRIP reaffirms Indigenous Peoples' rights to self-determination as political entities and honors the principle of Indigenous control over Indigenous data". Drafted at an "Indigenous-led workshop" (SP; Gaborone, 8 November 2018, SP).
Role: the paper itself licenses reading CARE as a "normative foundation" for other collectives, while resting its authority on Indigenous Peoples' rights as political entities.

2b. FNIGC, "The First Nations Principles of OCAP®". Rights-holder's own statement.
https://fnigc.ca/ocap-training/
- "Ownership refers to the relationship of First Nations to their cultural knowledge, data, and information." SV
- "Control affirms that First Nations, their communities, and representative bodies are within their rights to seek control over all aspects of research and information management processes that impact them." SV
- "Access refers to the fact that First Nations must have access to information and data about themselves and their communities regardless of where it is held." SV
- "Possession or stewardship is more concrete: it refers to the physical control of data." SV
- "OCAP® is a registered trademark of the First Nations Information Governance Centre (FNIGC)" SV
- The caution: "As such OCAP® operates as a set of specifically First Nations—not Indigenous—principles." SV. Preceded by (SP): "OCAP® is an expression of First Nations jurisdiction over information about their communities and its community members."
- "OCAP® is not a doctrine or a prescription" SV
- SP: "This principle states that a community or group owns information collectively in the same way that an individual owns his or her personal information."; established 1998 ("1998" SV); "In 2011, FNIGC's Board of Directors approved a multi-year plan designed to protect and ensure the integrity of OCAP®".
Role: the strongest justification for citing and not borrowing. The owner says the principles are not even pan-Indigenous.

2c. Te Mana Raraunga, "Principles of Māori Data Sovereignty", Brief #1, October 2018.
https://www.temanararaunga.maori.nz/s/TMR-Maori-Data-Sovereignty-Principles-Oct-2018.pdf (redirects to static1.squarespace.com)
- Six names SV: "Rangatiratanga | Authority"; "Whakapapa | Relationships"; "Whanaungatanga | Obligations"; "Kotahitanga | Collective benefit"; "Manaakitanga | Reciprocity"; "Kaitiakitanga | Guardianship".
- "Māori Data Sovereignty refers to the inherent rights and interests that Māori have in relation to the collection, ownership, and application of Māori data." SV
- "Māori data refers to digital or digitisable information or knowledge that is about or from Māori people, our language, culture, resources or environments." SV
- SP: 3.1 "Individuals' rights (including privacy rights), risks and benefits in relation to data need to be balanced with those of the groups of which they are a part. In some contexts, collective Māori rights will prevail over those of individuals." 5.2 "Free, prior and informed consent (FPIC) shall underpin the collection and use of all data from or about Māori. Less defined types of consent shall be balanced by stronger governance arrangements." 6.3 "Māori shall decide which Māori data shall be controlled (tapu) or open (noa) access."

2d. Kukutai & Taylor (eds) 2016, Indigenous Data Sovereignty: Toward an Agenda (ANU Press), ch. 1. Critical scholarship, open.
https://press-files.anu.edu.au/downloads/press/n2140/html/ch01.xhtml
- "Indigenous data sovereignty thus refers to the proper locus of authority over the management of data about indigenous peoples, their territories and ways of life." SV
- "...which are rooted in their inherent rights to self-determination as sovereign entities predating European settlers" SV
- "Missing from those conversations have been the inherent and inalienable rights and interests of indigenous peoples relating to the collection, ownership and application of data about their people, lifeways and territories." SV
- Peoples versus populations: "a demography of indigenous 'population' may be well suited to the provision of citizen rights but it does not provide for the expression of indigenous interests in inherent and proprietary rights as 'peoples'" SV (fragments)
- Scope: "the CANZUS group of Anglo-settler democracies" SV; "Although it is focused on the CANZUS states, the intended audience is global and varied." SV (main clause)
- "However, it should be recognised that the manner of application of these principles and practices will necessarily vary between jurisdictions and between indigenous polities." SV
- "This volume signals the beginning point in an ongoing conversation initiated by and for indigenous peoples." SV
Role: the claim rests on inherent sovereign rights of peoples, not on being a data-subject group. That is the sentence-level reason a place-based cultural community cannot adopt the framework wholesale.

2e. Walter & Suina 2019: tandfonline 403. Not reached. No stand-alone published "do not appropriate" warning was found; the caution rests on 2b and 2d.

--------------------------------------------------------------------
ITEM 3 — PARTICIPATORY DATA STEWARDSHIP
--------------------------------------------------------------------

3a. Ada Lovelace Institute, "Participatory data stewardship" (published 7 September 2021, date SP). Practitioner framework.
https://www.adalovelaceinstitute.org/report/participatory-data-stewardship/
- Definition: "The responsible use, collection and management of data in a participatory and rights-preserving way" SV
- Inform: "'Informing' people about data use and governance involves a one-way flow of information from those who use, gather, deploy and analyse data, to data subjects or 'beneficiaries'." SV (core)
- Consult: "Consultation can take place with individuals, groups, networks or communities, to enable people to voice their concerns, thoughts and perspectives." SV
- Involve: "The process of 'involvement' positions beneficiaries in an advisory role, which helps inform early-stage decision-making by data stewards and fiduciaries." SV
- Collaborate: "...enabling people to negotiate and engage in trade-offs with powerholders and those governing data about specific aspects of decision-making." SV (first clause)
- Empower: "Empowering data beneficiaries enables them to exercise full managerial power and agency, and take responsibility for exercising and actively managing decisions about data governance." SV (first clause)
- Legitimacy: "We redefine legitimacy in the context of data, therefore, as the broad base of public support that allows companies, designers, public servants and others to use data, and to design and develop data-governance frameworks." SV (core)
- Lineage: "Sherry Arnstein's 'ladder of citizen participation'" SV. Approaches "are most often not mutually exclusive" (SP).
- The final 19,000 characters were not read.

3b. ODI, "What is a data trust?" (Tue Jul 10, 2018).
https://theodi.org/insights/explainers/what-is-a-data-trust/
- "A data trust provides independent, fiduciary stewardship of data" SV
- "stewarding data with impartiality, prudence, transparency and undivided loyalty" SV
- "a fiduciary duty is considered the highest level of obligation that one party can owe to another" SV (tail)
- SP: "They involve one party authorising another to make decisions about data on their behalf, for the benefit of a wider group of stakeholders."

3c. ODI data trusts pilots report (page dated Sun Apr 14, 2019).
https://theodi.org/insights/reports/odi-data-trusts-report/ ; full text is a Google Doc (id 118RqyUAWP3WIyyCO4iLUT3oOobnYJGibEhspr2v87jg)
- "a legal structure that provides independent stewardship of data" SV. Note the 2019 wording differs from the 2018 "independent, fiduciary stewardship".
- "one approach to data stewardship" SV
- SP: "Data trusts are not legal trusts but they take what we have learnt from them. Trustees take on responsibility to make decisions about the data, along with some liabilities, to support the data trust to achieve its purpose."
- Pilots (SP, paraphrase): Greater London Authority and Royal Borough of Greenwich; WILDLABS Tech Hub; food and drink manufacturers and retailers.
- NOT VERIFIED: the six-part "what a trust needs" list. The reader produced it on first pass and could not find it as a list on second. Do not quote it. Leaflet PDF unreadable.

3d. Data cooperatives.
- EU Data Governance Act, Regulation (EU) 2022/868, Recital 31.
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R0868
"Data cooperatives seek to achieve a number of objectives, in particular to strengthen the position of individuals in making informed choices before consenting to data use" SV; "...potentially finding solutions to conflicting positions of individual members of a group on how data can be used where such data relates to several data subjects within that group" SV.
"In that context it is important to acknowledge that the rights under Regulation (EU) 2016/679 are personal rights of the data subject and that data subjects cannot waive such rights." SV (core)
Article 2(15), SP: "data intermediation services offered by an organisational structure constituted by data subjects, one-person undertakings or SMEs who are members of that structure, having as its main objectives to support its members in the exercise of their rights with respect to certain data".
Role: the statute that recognises data cooperatives also says rights stay personal. It is EU law, not UK law.
- MIDATA self-description. https://www.midata.coop/en/home/
"They may become members of the cooperative and thereby control the cooperative." SV; "MIDATA cooperatives are nonprofit institutions." SV; "They can also withdraw their personal data at any time." SV; "MIDATA shows how data can be used for the common good, while at the same time ensuring the citizens' control over their personal data." SV (tail).

3e. ODI Data Ethics Canvas — 15 headings, SV against the repository's language file.
https://raw.githubusercontent.com/theodi/data-ethics-canvas/master/lang/en.json
Data Sources; Limitations in data sources; Sharing data with others; Ethical and legislative context; Rights around data sources; Your reasons for using data; Communicating your purpose; Positive effects on people; Negative effects on people; Minimising negative impact; Engaging with people; Openness and transparency; Ongoing implementation; Reviews and iterations; Your actions.
No heading on consent or community (control NO). Licence string SP: "Creative Commons Attribution-ShareAlike 4.0 UK. International License". The landing page (theodi.org/insights/tools/the-data-ethics-canvas-2021/) shows no headings.

--------------------------------------------------------------------
ITEM 4 — CONTEXTUAL INTEGRITY AND "ALREADY PUBLIC"
--------------------------------------------------------------------

4a. Nissenbaum 2004, "Privacy as Contextual Integrity", Washington Law Review 79(1):119–158 (citation SP). Open.
https://digitalcommons.law.uw.edu/cgi/viewcontent.cgi?article=4450&context=wlr
- "I posit two types of informational norms: norms of appropriateness, and norms of flow or distribution." SV
- "Contextual integrity is maintained when both types of norms are upheld, and it is violated when either of the norms is violated." SV
- "norms of appropriateness dictate what information about persons is appropriate, or fitting, to reveal in a particular context" SV
- "...another set of norms govern what I will call flow or distribution of information—movement, or transfer of information from one party to another or others." SV (tail)
- "there are no arenas of life not governed by norms of information flow, no information or spheres of life for which "anything goes."" SV
- On public information: "is always tagged with that context and never "up for grabs"" SV (fragment only)
- Page numbers NOT verified; the reader returned impossible ones. Check against the PDF before citing pages.

4b. boyd & Crawford 2012, Information, Communication & Society 15(5):662–679, DOI 10.1080/1369118X.2012.678878.
Published version: https://www.microsoft.com/en-us/research/wp-content/uploads/2012/05/CriticalQuestionsForBigDataICS.pdf ; draft: https://www.danah.org/papers/2012/BigData-ICS-Draft.pdf ; tandfonline 403.
- Six headings as published (5, 4 and 6 SV; 1–3 SP): "Big Data changes the definition of knowledge"; "Claims to objectivity and accuracy are misleading"; "Bigger data are not always better data"; "Taken out of context, Big Data loses its meaning"; "Just because it is accessible does not make it ethical"; "Limited access to Big Data creates new digital divides".
- WORDING CHECK: the published heading is "Just because it is accessible does not make it ethical" (SV; "doesn't" absent). The draft has "Just Because it is Accessible Doesn't Make it Ethical" (SV; "does not" absent). The brief's wording matches the published version.
- "Data may be public (or semi-public) but this does not simplistically equate with full permission being given for all uses." SV in both
- "There is a considerable difference between being in public (i.e. sitting in a park) and being public (i.e. actively courting attention)." SV as published
- "rather than assuming that ethics boards will necessarily do the work of ensuring that people are protected" SV as published

4c. Zimmer 2010, Ethics and Information Technology 12(4):313–325, DOI 10.1007/s10676-010-9227-5. ABSTRACT; not open access.
https://link.springer.com/article/10.1007/s10676-010-9227-5
- "In 2008, a group of researchers publicly released profile data collected from the Facebook accounts of an entire cohort of college students from a US university." SV
- "While good-faith attempts were made to hide the identity of the institution and protect the privacy of the data subjects, the source of the data was quickly identified, placing the privacy of the students at risk." SV
- The name "Tastes, Ties, and Time" is not in the abstract; unverified here. boyd & Crawford's section opens (SP): "In 2006, a Harvard-based research group started gathering the profiles of 1,700 college-based Facebook users..."

4d. Metcalf & Crawford 2016, Big Data & Society 3(1), DOI 10.1177/2053951716650211. Open.
https://journals.sagepub.com/doi/full/10.1177/2053951716650211
- The sentence wanted: "Publicly available data can be put to a wide range of secondary uses, including being combined with other data sets, that can pose serious risks to individuals and communities." SV. Preceded by (SP): "But this assumption is founded on a misconception."
- "...that the risk to research subjects depends on what kind of data is obtained and how it is obtained, not what is done with the data after it is obtained." SV
- "...are arguably most risky for subjects, yet are a priori excluded from any review under the NPRM." SV

4e. UK Statistics Authority ethical principles (NSDEC). Page metadata 11 August 2026 (SP).
https://uksa.statisticsauthority.gov.uk/the-authority-board/committees/national-statisticians-advisory-committees-and-panels/national-statisticians-data-ethics-advisory-committee/ethical-principles/
- "The use of data has clear benefits for users and serves the public good." SV
- "The views of the public are considered in light of the data used and the perceived benefits of the research." SV
- "The access, use and sharing of data is transparent, and is communicated clearly and accessibly to the public." SV
- "...and the issue of consent is considered appropriately" SV
- "no surprises" does not appear on this page.

--------------------------------------------------------------------
ITEM 5 — WITHDRAWAL AGAINST THE ARCHIVE
--------------------------------------------------------------------

5a. ESRC consent guidance (UKRI; last updated 7 May 2026).
https://www.ukri.org/councils/esrc/guidance-for-applicants/research-ethics-guidance/consent/
- "In giving consent, participants have the right to withdraw this consent as well as the right not to answer particular questions." SV
- "All research should indicate the point at which data will have been anonymised and amalgamated and in certain circumstances cannot then be excluded." SV
- "Some projects give a date after which participants cannot withdraw consent or ask for data destruction." SV
- "Participants need, as far as possible, to give specific consent if data are to be archived and shared." SV (second pass corrected my candidate, which lacked "be")
- Consent should "be open to revision and withdrawal throughout the research lifecycle" SV; in participatory research "consent to participate is seen as an ongoing and open-ended process" SV
- SP: "Researchers should also ensure, wherever necessary, they have received the relevant permission from gatekeepers to undertake the research."
Role: the UK funder states the conflict and the practice in one place: a declared cut-off after which data "cannot then be excluded".

5b. UK Data Service, "Consent for data sharing". https://ukdataservice.ac.uk/learning-hub/research-data-management/ethical-issues/consent-for-data-sharing/
Thin page. SV: "Under the UK GDPR, consent is one of six lawful bases for processing personal data."; "avoid conflating ethical research consent with consent for data processing". "What is the procedure to withdraw?" appears only as a prompt (SP). Nothing on withdrawal after deposit; "archiv" does not appear. The CESSDA guide also has nothing on it (SP).

5c. UK Biobank participant privacy notice — graded withdrawal. Last-updated date NOT verified (two passes gave 24 September 2025 and 15 May 2025).
https://www.ukbiobank.ac.uk/taking-part/our-agreement-with-you/participant-privacy-notice/
- No further contact: "UK Biobank would no longer contact the participant directly but would have permission to retain and use information and samples provided previously" SV
- No further access: "UK Biobank would no longer contact the participant or obtain further information from health records in the future, but still has permission to use the information and samples provided previously" SV
- No further use: "Any information and samples collected previously would no longer be available to researchers." SV; "UK Biobank would destroy samples (although it may not be possible to trace all distributed sample remnants) and would only hold information for archival audit purposes." SV
- "Such a withdrawal would prevent information about the participant from contributing to further research, but it would not be possible to remove data from research that had already taken place." SV (supplied by the verifier)
Role: three tiers of withdrawal with the irreversible part stated, at national scale.

5d. Zenodo general policies (CERN). https://about.zenodo.org/policies/
- "If the uploaded research object must later be withdrawn, the reason for the withdrawal will be indicated on a tombstone page, which will henceforth be served in its place." SV
- "Withdrawal is considered an exceptional action, which normally should be requested and fully justified by the original uploader." SV
- "Data files are versioned. Records are not versioned." SV; "original content is never modified" SV; "Items will be retained for the lifetime of the repository." SV
- SP: "The DOI and the URL of the original object are retained."
Role: the tombstone pattern. The content goes; the identifier and the stated reason stay.

5e. The National Archives, takedown and reclosure policy (covers the UK Government Web Archive; no date shown).
https://www.nationalarchives.gov.uk/legal/takedown-and-reclosure-policy/
- "As a general rule, information published on a website will be considered to be in the public domain and will be removed from that website only in exceptional circumstances, at the discretion of The National Archives." SV (second pass added "As a general rule,")
- "Material will be taken down temporarily on receipt of a request" SV; "The case will then be considered by the Takedown Panel" SV
- "The information will be regarded as having been removed temporarily and may be restored at a date decided by The National Archives." SV
- SP: "It is rare that an open record is subsequently closed to public access, but there are circumstances... in which this may occur."; ground: "sensitive personal information about someone who is still alive and continued public access would be unlawful or unfair to them".
- UK Web Archive notice-and-takedown page UNREACHABLE (robots/certificate failure, two URLs).

5f. Internet Archive help. https://help.archive.org/help/how-do-i-request-to-remove-something-from-archive-org/
"We do not make any guarantees beforehand about the outcome of a request." SV. Requests go to info@archive.org (SV), stating "the time period that you wish to have excluded" (SV). SP: "This will initiate a review by our team."

5g. Version control as technical fact.
- Pro Git 2nd ed., §1.3. https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
"When you do actions in Git, nearly all of them only add data to the Git database." SV
"It is hard to get the system to do anything that is not undoable or to make it erase data in any way." SV
"Everything in Git is checksummed before it is stored and is then referred to by that checksum." SV
"This means it's impossible to change the contents of any file or directory without Git knowing about it." SV
- GitHub Docs. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
WORDING CHECK FAILED: "you should consider any sensitive data in the commit compromised" and "Once you have pushed a commit to GitHub" are NOT on the current page, nor on the Enterprise Server 3.10 version. Do not use them. Current wording:
"You cannot remove sensitive data from other users' clones of your repository" SV
"...the commits with sensitive data may still be accessible elsewhere" SV: "In any clones or forks of your repository" SV; "Directly via their SHA-1 hashes in cached views on GitHub" SV; "Through any pull requests that reference them" SV
SP: "Once the secret is revoked or rotated, it can no longer be used for access, and that may be sufficient to solve your problem."

5h. Mayer-Schönberger, Delete (Princeton UP; paperback 25 July 2011, ISBN 9780691150369). Publisher page only.
https://press.princeton.edu/books/paperback/9780691150369/delete
"Delete looks at the surprising phenomenon of perfect remembering in the digital age, and reveals why we must reintroduce our capacity to forget." SV. "expiration dates on information" SV. "right to be forgotten" does not appear on the page.

What the sources support together: no fetched source claims a withdrawal right that reaches back through what has already been published, analysed or copied. Practice is (i) a declared cut-off (ESRC), (ii) graded withdrawal with the irreversible part named (UK Biobank), (iii) removal from access with a tombstone and stated reason (Zenodo; TNA "temporarily"), and (iv) no guarantee (Internet Archive; GitHub on clones).

--------------------------------------------------------------------
ITEM 6 — KNOWN BUT NOT SHOWN
--------------------------------------------------------------------

6a. eBird, "Sensitive Species in eBird" (modified Fri, 15 May, 2026, SP).
https://support.ebird.org/en/support/solutions/articles/48000803210-sensitive-species-in-ebird
- Why: "Some bird species face risks from humans of capture, targeted killing, or significant targeted disturbance." SV; "Open-access data can be a risk for these birds that are targeted for exploitation." SV
- Resolution: "Shown at grid-cell level (400 km2 accuracy) on eBird species maps" ("400 km2" SV; "20x20 km" absent)
- Hidden (SP): "Hidden from checklist views, except to observers on the checklist"; "Hidden from all site-level output (e.g., Hotspot Explorer, bar charts for hotspots)"
- Still used: "These records are still seen by our eBird reviewers, who must check identifications for accuracy." SV
- Who decides: "eBird consults with our local partners worldwide in order to develop our list of Sensitive Species." SV

6b. iNaturalist geoprivacy help (modified "Thu, 12 Mar", year not shown).
https://help.inaturalist.org/en/support/solutions/articles/151000169938-what-is-geoprivacy-what-does-it-mean-for-an-observation-to-be-obscured-
- "The public positional accuracy is increased to the diagonal of a 0.2 x 0.2 degree cell (~500km2 at the equator or about the same size as the Isle of Man)." SV
- "Latitude and longitude are replaced with a random point within this cell" SV
- Private: "No geographic information is shared publicly" SV
- Taxon geoprivacy "automatically restricts geographic information associated with observations of taxa threatened by location disclosure" SV
- SP: "Locality notes and date are also publicly replaced with coarser representations"; "observations of certain orchids are automatically obscured because these species are sought after by poachers".
- The page does not name which conservation statuses trigger auto-obscuring.

6c. NBN Atlas sensitive species list (last modified 2026-05-13, SP). UK precedent.
https://docs.nbnatlas.org/sensitive-species-list/
- "Environmentally sensitive information is any which, if released to the public, would result in an 'adverse effect' on a feature of the environment." SV
- "These lists have been agreed by the UK's statutory bodies and relevant experts." SV
- "Any records for species that are listed on the sensitive species lists (shown below) will be blurred to the resolution stated (i.e., a generalised OS grid reference will be assigned to the record)." SV (two fragments)
- SP: "Data Partners do not have to make their own assessments on the sensitivity of their records"; a separate process exists for "Enhanced access to sensitive species records".

6d. Environmental Information Regulations 2004 (SI 2004/3391), regulation 12. Statute; banner reports no known outstanding effects (SP).
https://www.legislation.gov.uk/uksi/2004/3391/regulation/12
- reg 12(5): "a public authority may refuse to disclose information to the extent that its disclosure would adversely affect—" ... "(g) the protection of the environment to which the information relates." SV
- reg 12(1)(b): "in all the circumstances of the case, the public interest in maintaining the exception outweighs the public interest in disclosing the information" SV
- reg 12(2): "A public authority shall apply a presumption in favour of disclosure." SV
It binds public authorities, not a private platform. Its value is the structure: a presumption of openness, a named harm, and a public-interest test.

6e. Antiquities. PAS pages (finds.org.uk) returned 403 on two URLs. The parish / four-figure / 1 km claim is NOT VERIFIED. Nearest verified: Treasure Act 1996 Code of Practice (3rd Revision, 2023).
https://assets.publishing.service.gov.uk/media/64c909cb19f5622360f3c14a/Treasure_Act_1996__Code_of_Practice.pdf
- E.87: "Neither the precise location of findspots nor details (e.g. addresses and telephone numbers) of the finder, occupier or landowner, should be made public at the inquest" SV
- D.10: record "to at least a 10 metre square (equivalent to an 8-digit National Grid Reference)" SV
- "four-figure" and "confidential" do not appear in the Code. Historic England not fetched.

6f. ONS Census 2021 sexual orientation geography floor: NOT ESTABLISHED. Five pages tried; none states the lowest geography.
- TS077 dataset page (ons.gov.uk/datasets/TS077/editions/2021/versions/3 and /6): shows "Lower tier local authorities" as area type (SV as a string); generic text "output areas (which have a minimum of 100 persons)" (SP). Released 06 January 2023 (SP).
- Bulletin: presents national, regional and local authority figures; no floor stated (SP).
- Variable page (SP): "This question was voluntary and was only asked of people aged 16 years and over."
- Quality information page, last revised 8 April 2025 (SP): "gender identity estimates from Census 2021 should not be used as precise estimates to support service delivery, but they can be used to provide insights".
- Nomis query pages robots-disallowed. If Agent B has the floor, use theirs.

Clean precedents with data, reduced display and a stated reason: eBird; iNaturalist; NBN Atlas; EIR reg 12(5)(g) as the statutory form.

--------------------------------------------------------------------
ITEM 7 — WHO SPEAKS FOR A COMMUNITY
--------------------------------------------------------------------

7a. Cornwall 2008, Community Development Journal 43(3):269–283, DOI 10.1093/cdj/bsn010. ABSTRACT.
https://academic.oup.com/cdj/article/43/3/269/299854
- "It suggests that it is vital to pay closer attention to who is participating, in what and for whose benefit." SV
- "Vagueness about what participation means may have helped the promise of public involvement gain purchase..." SV; "...'clarity through specificity' if the call for more participation is to realize its democratizing promise." SV (fragments). The abstract attributes "clarity through specificity" to Cohen and Uphoff.
- Her typology discussion is behind the paywall; nothing quoted.

7b. Cooke & Kothari 2001: UNREACHABLE (Bloomsbury blocked; CABI 403). Nothing quoted.

7c. Young, Inclusion and Democracy (OUP, Oxford Political Theory; paperback 20 June 2002, ISBN 9780198297550). Publisher page only; the 2000 hardback is not mentioned.
https://global.oup.com/academic/product/inclusion-and-democracy-9780198297550
"Processes of debate and decision making often marginalize individuals and groups because the norms of political discussion are biased against some forms of expression." SV (tail). Chapter titles SV: "Inclusive Political Communication"; "Social Difference as a Political Resource"; "Representation and Social Perspective".

7d. Gatekeepers — McAreavey & Das 2013, International Journal of Qualitative Methods 12(1), DOI 10.1177/160940691301200102. Peer-reviewed, free access.
https://journals.sagepub.com/doi/full/10.1177/160940691301200102
- "Gatekeepers control access to a particular community or institution and as a result researchers are reliant on their input." SV (first clause)
- "Nevertheless, gatekeepers may also have other interests and may hold preconceived, conventional, and biased ideas of what constitutes good research." SV (core)
- "By acting as cultural mediators or brokers they can help the researcher become more culturally competent." SV (fragment)
- SP: "Ultimately, they may present barriers to accessing research participants or they may provide unlimited access to the same participants, leading to multiple studies that prevent a diverse understanding of the community."
- "We advance the notion of research ethics as an ongoing process that requires researcher skills and engagement, rather than a one-off bureaucratic exercise." SV
See also 1e (legitimate political system) and 1h (CIOMS). No UK local-government text on "community leaders" was fetched.

7e. "Nothing about us without us".
- Charlton, UC Press page. https://www.ucpress.edu/books/nothing-about-us-without-us/paper
"James Charlton has produced a ringing indictment of disability oppression" SV; "the first book in the literature on disability to provide a theoretical overview of disability oppression" SV. The page shows Aug 2000 (paperback, ISBN 9780520224810); "1998" does not appear. The origin of the slogan is NOT on the page ("South Africa" absent).
- Costanza-Chock, Design Justice (MIT Press open edition): "Disability rights and Disability justice activists popularized the phrase "nothing about us without us" in the 1980s and 1990s." SV. https://designjustice.mitpress.mit.edu/pub/cfohnud7 . The reader could not identify the chapter reliably, and "Charlton" does not appear on that page.

--------------------------------------------------------------------
ITEM 8 — DATA JUSTICE AND FEMINISM AS FRAMES
--------------------------------------------------------------------

8a. Taylor 2017, Big Data & Society 4(2), DOI 10.1177/2053951717736335. Open.
https://journals.sagepub.com/doi/full/10.1177/2053951717736335
- Definition: "fairness in the way people are made visible, represented and treated as a result of their production of digital data" SV
- "I propose three pillars as the basis of a notion of international data justice: (in)visibility, (dis)engagement with technology and antidiscrimination." SV
- "The first pillar, visibility, deals both with privacy and representation." SV
- "Engagement with technology is the second pillar of this putative conceptual framework." SV; "The freedom to control the terms of one's engagement with data markets is an essential component of any data justice framework because it underpins the power to understand and determine one's own visibility." SV
- "The third pillar within this proposed framework is nondiscrimination. It is composed of two dimensions: the power to identify and challenge bias in data use, and the freedom not to be discriminated against." SV
- Group level: "many of the negative impacts of data occur on the group as much as the individual level" SV; "New data technologies tend to sort, profile and inform action based on group rather than individual characteristics and behaviour" SV
- Her wording is "antidiscrimination" / "nondiscrimination", not "non-discrimination".

8b. Dencik, Hintz & Cable 2016, Big Data & Society 3(2), DOI 10.1177/2053951716679678. Open.
https://journals.sagepub.com/doi/full/10.1177/2053951716679678
- "Introducing the notion of 'data justice', we therefore go on to make the case that resistance to surveillance needs to be (re)conceptualized on terms that can address the implications of this data-driven form of governance in relation to broader social justice agendas." SV (two fragments)
- Body, SP (the verifier answered NO to my capitalised candidate and then supplied this sentence, so the tail is not confirmed): "Whilst recognizing the procedural inference in the term 'justice', by data justice we are referring to the implications that data-driven processes at the core of surveillance capitalism have for the pursuit of substantive social and economic justice claims."

8c. D'Ignazio & Klein 2020, Data Feminism (MIT Press, open), Introduction.
https://data-feminism.mitpress.mit.edu/pub/frfa9szd
All seven SV:
1. "Examine power. Data feminism begins by analyzing how power operates in the world."
2. "Challenge power. Data feminism commits to challenging unequal power structures and working toward justice."
3. Elevate emotion and embodiment. "Data feminism teaches us to value multiple forms of knowledge, including the knowledge that comes from people as living, feeling bodies in the world."
4. Rethink binaries and hierarchies. "Data feminism requires us to challenge the gender binary, along with other systems of counting and classification that perpetuate oppression."
5. Embrace pluralism. "Data feminism insists that the most complete knowledge comes from synthesizing multiple perspectives, with priority given to local, Indigenous, and experiential ways of knowing."
6. Consider context. "Data feminism asserts that data are not neutral or objective. They are the products of unequal social relations, and this context is essential for conducting accurate, ethical analysis."
7. Make labor visible. "...Data feminism makes this labor visible so that it can be recognized and valued."
Definition (SP): "A way of thinking about data, both their uses and their limits, that is informed by direct experience, by a commitment to action, and by intersectional feminist thought."

8d. Design Justice Network Principles ("Last update: summer 2018", SP; ten principles).
https://designjustice.org/read-the-principles
SV: 1 "We use design to sustain, heal, and empower our communities, as well as to seek liberation from exploitative and oppressive systems."; 2 "We center the voices of those who are directly impacted by the outcomes of the design process."; 3 "We prioritize design's impact on the community over the intentions of the designer."; 5 "We see the role of the designer as a facilitator rather than an expert."; 8 "We work towards sustainable, community-led and -controlled outcomes."; 10 ends "We honor and uplift traditional, indigenous, and local knowledge and practices."
SP: principles 4, 6, 7, 9.
CHECK: "Nothing about us without us" does NOT appear in the principles. The nearest is principle 2.

8e. Oxfam Responsible Program Data Policy (27/08/2015).
https://policy-practice.oxfam.org/resources/oxfam-responsible-program-data-policy-575950/
Five rights, names SV: the right to be counted and heard; the right to dignity and respect; the right to make an informed decision; the right to privacy; the right to not be put at risk. The policy PDF was unreachable (robots failure), so no one-sentence statements. SP from the landing page: "Oxfam is one of the first international NGOs to develop an explicit policy on the responsible use of data."

8f. Responsible data.
- The Engine Room, https://www.theengineroom.org/responsible-data/ : "Responsible Data is the collective duty to account for unintended consequences of working with data by: 1. Prioritising people's rights to consent, privacy, security and ownership when using data in social change and advocacy efforts, and 2. Implementing values and practices of transparency and openness." SV (three fragments)
- responsibledata.io, https://responsibledata.io/what-is-responsible-data/ : "Responsible Data (RD) is a concept outlining our collective duty to prioritise and respond to the ethical, legal, social and privacy-related challenges that come from using data in new and different ways in advocacy and social change." SV. The two wordings differ; this page does not name The Engine Room.

--------------------------------------------------------------------
FOLLOW THREADS
--------------------------------------------------------------------

T1. Rambaldi, Chambers, McCall & Fox 2006, "Practical ethics for PGIS practitioners, facilitators, technology intermediaries and researchers" (PLA 54, pp. 106–113; the PDF carries no citation line).
https://www.iied.org/sites/default/files/pdfs/migrate/G02957.pdf
"Who? and Whose?" questions, all SV: "Who decides on who should participate?"; "and who is left out?"; "Who decides, and who should decide, on what to visualise and make public?"; "Who controls the use of information?"; "Who owns the output?"; "Who owns the map(s)?"; "Who owns the resulting data?"; "What is left with those who generated the information and shared their knowledge?"; "Who gains and who loses?"; "Who is empowered and who is disempowered?"
Guideline headings SV: "Obtain informed consent"; "Avoid exposing people to danger". SP: "As in any research with people, participation must be voluntary."; the danger example opens "Villagers in a country in Southeast Asia working on a 3D model pointed to the hideouts of rebel groups, incurring immediate danger."
Role: a ready-made question set for community mapping, with a harm case of a map revealing what a community knew.

T2. Camden Council Data Charter. https://www.camden.gov.uk/data-charter
"Our Data Charter guides how we collect, process and share data ethically." SV. SP: "It was co-created with 2 resident panels made up of Camden citizens." Headings SV: "Build trust through transparency"; "Provide accountability and oversight"; "Camden's external partners should sign up to the Data Charter principles". No date or review commitment on this page. It is a council charter made with residents, not an agreement between a community group and a public body. No example of the latter was found.

--------------------------------------------------------------------
NOT ASKED FOR
--------------------------------------------------------------------
1. UNESCO 2005 Art 6(3) and CIOMS 2016 Guideline 9 commentary (1h): community agreement is additional to individual consent and never a substitute.
2. Dickert & Sugarman 2005 (1e): consultation is not consent; consent needs a legitimate political system.
3. EIR 2004 reg 12(5)(g) (6d): a UK statutory form of "known but not shown".
4. NBN Atlas (6c): a UK scheme where a statutory-body list fixes the blurring so partners "do not have to make their own assessments".
5. UK Biobank graded withdrawal and Zenodo tombstones (5c, 5d).
6. Te Mana Raraunga 5.2 (SP): weaker consent "shall be balanced by stronger governance arrangements".
7. Local Contexts TK Labels. https://localcontexts.org/labels/traditional-knowledge-labels/ "The Traditional Knowledge (TK) Labels are an initiative for Indigenous communities and local organizations." SV. "The Labels allow communities to express local and specific conditions for sharing and engaging in future research and relationships..." SV. Label names "TK Secret / Sacred", "TK Community Use Only", "TK Seasonal" SV. Same borrowing caution as OCAP.
8. DGA Recital 31 (3d): rights "are personal rights of the data subject" and "cannot" be waived.

--------------------------------------------------------------------
LEFT OUT, AND WHY
--------------------------------------------------------------------
- Weijer & Emanuel 2000: unreachable by four routes.
- Banks et al. 2013; Walter & Suina 2019: tandfonline 403.
- ICPHR Position Paper 2: 404.
- Cooke & Kothari 2001: publisher blocked, CABI 403.
- UK Web Archive takedown policy: robots/certificate failure.
- PAS findspot policy: finds.org.uk 403.
- NIH/CDC community-consultation definition: not fetched; the FDA substitute could not be stabilised.
- ODI "what a trust needs" list: could not be verified.
- ONS geography floor: not stated on any page reached.
- Cornwall's typology; Zimmer's T3 detail; Oxfam's per-right sentences: full texts not reachable.
- Floridi 2014 on group privacy: Springer 429. Historic England: not attempted. Data (Use and Access) Act 2025, erasure, crime-map snapping, Chambers: skipped as instructed.

--------------------------------------------------------------------
RICH REFERENCES
--------------------------------------------------------------------
1. Dickert & Sugarman 2005 (PMC1449329): short, open, separates consultation from consent and says when community consent is valid.
2. Rambaldi et al. 2006 (IIED G02957): the "Who? and Whose?" box and ethics list for community mapping.
3. Ada Lovelace Institute 2021: the five-level spectrum with worked mechanisms and the redefinition of legitimacy.

--------------------------------------------------------------------
WHAT SURPRISED ME
--------------------------------------------------------------------
- FNIGC says OCAP is "specifically First Nations—not Indigenous". The owner's caution is narrower than the one the chapter planned to make.
- The CARE paper is more permissive than expected: it names "minority groups, distinctive communities, or other collectives".
- The GitHub "consider any data … compromised" sentence is gone from the current page and the older one checked. The live wording is narrower and more useful: "You cannot remove sensitive data from other users' clones of your repository".
- boyd & Crawford's heading differs between draft ("Doesn't") and published ("does not").
- The DJN principles do not contain "nothing about us without us", and the UC Press page for Charlton gives neither the slogan's origin nor a 1998 date.
- The ODI's definition changed between 2018 ("independent, fiduciary stewardship") and 2019 ("a legal structure that provides independent stewardship").
- The reader invented text on first pass in two places: the FDA definition and the ODI six-part list. Both were caught on the presence check. It also returned impossible page numbers for Nissenbaum.
- Havasupai left "no legal precedent", and the reported reaction was withdrawal from research with such communities.


---

## Agent D — The other legal boundaries and the harms

CHAPTER 10 — FACET REPORT: THE OTHER LEGAL BOUNDARIES AND THE HARMS
Fetched 6 October 2026. Plain text. No files written.

ACCESS AND METHOD
- WebSearch was unavailable (the turn's shared search budget was already used up). Everything below came from direct URLs through WebFetch. Direct curl is blocked by the egress proxy, so verification was by re-fetching the same URL with YES/NO presence prompts, with a false control string in almost every check. Controls came back NO, with one exception noted in item 6.
- Marking: SV = string-verified on a second fetch; SP = single pass (reader output, not re-checked); ABSTRACT = only the abstract was reachable.
- legislation.gov.uk pages carry the standing notice "Revised legislation carried on this site may not be fully up to date." The reader reported each page as up to date to between 27 September and 5 October 2026, depending on the page.
- One page I could not read at all: a Poynter article (poynter.org) on the Journal News gun-permit map. The fetch proxy rejected it for rate-limiting and told me not to retry. Nothing is quoted from it.

==================================================
ITEM 1 — EQUALITY ACT 2010 FOR A PRIVATE SERVICE PROVIDER
==================================================
Type: statute (primary) throughout unless stated. Banner on every Equality Act page: outstanding changes "yet to be applied" from 2025 c. 36, which the reader said affect other sections (it named ss.40, 40B, 78, 153, 154, 208). I did not open 2025 c. 36 itself.

s.29 Provision of services, etc. — https://www.legislation.gov.uk/ukpga/2010/15/section/29
- (1) "A person (a "service-provider") concerned with the provision of a service to the public or a section of the public (for payment or not) must not discriminate against a person requiring the service by not providing the person with the service." SV in two fragments.
- (2) "A service-provider (A) must not, in providing the service, discriminate against a person (B)— (a) as to the terms on which A provides the service to B; (b) by terminating the provision of the service to B; (c) by subjecting B to any other detriment." SP.
- (3) "A service-provider must not, in relation to the provision of the service, harass— (a) a person requiring the service, or (b) a person to whom the service-provider provides the service." Opening words SV.
- (4) "A service-provider must not victimise a person requiring the service by not providing the person with the service." SV.
- (7) "A duty to make reasonable adjustments applies to— (a) a service-provider (and see also section 55(7)); (b) a person who exercises a public function that is not the provision of a service to the public or a section of the public." Opening SV; (a) and (b) SP.
- (8) "In the application of section 26 for the purposes of subsection (3), and subsection (6) as it relates to harassment, neither of the following is a relevant protected characteristic— (a) religion or belief; (b) sexual orientation." Middle fragment SV; list SP.
- Role: the core prohibition applies to any service to the public "for payment or not", so a free, non-commercial dashboard is inside it. The Part 3 harassment prohibition does not cover religion or belief or sexual orientation.

s.31 Interpretation — https://www.legislation.gov.uk/ukpga/2010/15/section/31 (SP)
- (2) "A reference to the provision of a service includes a reference to the provision of goods or facilities."
- (4) "A public function is a function that is a function of a public nature for the purposes of the Human Rights Act 1998."

s.4 Protected characteristics — https://www.legislation.gov.uk/ukpga/2010/15/section/4 (SP)
- "The following characteristics are protected characteristics— age; disability; gender reassignment; marriage and civil partnership; pregnancy and maternity; race; religion or belief; sex; sexual orientation."

s.19 Indirect discrimination — https://www.legislation.gov.uk/ukpga/2010/15/section/19
- (1) "A person (A) discriminates against another (B) if A applies to B a provision, criterion or practice which is discriminatory in relation to a relevant protected characteristic of B's." SV from "applies to B".
- (2)(b) "it puts, or would put, persons with whom B shares the characteristic at a particular disadvantage when compared with persons with whom B does not share it," First part SV.
- (2)(d) "A cannot show it to be a proportionate means of achieving a legitimate aim." SV.
- The s.19(3) list omits pregnancy and maternity (confirmed on re-fetch). A section 19A exists; I did not read it.

s.26 Harassment — https://www.legislation.gov.uk/ukpga/2010/15/section/26
- (1) "A person (A) harasses another (B) if— (a) A engages in unwanted conduct related to a relevant protected characteristic, and (b) the conduct has the purpose or effect of— (i) violating B's dignity, or (ii) creating an intimidating, hostile, degrading, humiliating or offensive environment for B." (a), (i), (ii) SV.
- (4) "In deciding whether conduct has the effect referred to in subsection (1)(b), each of the following must be taken into account— (a) the perception of B; (b) the other circumstances of the case; (c) whether it is reasonable for the conduct to have that effect." (c) SV; rest SP.

s.158 Positive action: general — https://www.legislation.gov.uk/ukpga/2010/15/section/158
- (1) "This section applies if a person (P) reasonably thinks that— (a) persons who share a protected characteristic suffer a disadvantage connected to the characteristic, (b) persons who share a protected characteristic have needs that are different from the needs of persons who do not share it, or (c) participation in an activity by persons who share a protected characteristic is disproportionately low." Opening, (a), (c) SV; (b) SP.
- (2) "This Act does not prohibit P from taking any action which is a proportionate means of achieving the aim of— (a) enabling or encouraging persons who share the protected characteristic to overcome or minimise that disadvantage, (b) meeting those needs, or (c) enabling or encouraging persons who share the protected characteristic to participate in that activity." Opening SV; paragraphs SP.
- Role: positive action is permissive ("does not prohibit"), not a duty.

s.149 Public sector equality duty — https://www.legislation.gov.uk/ukpga/2010/15/section/149
- (1) "A public authority must, in the exercise of its functions, have due regard to the need to— (a) eliminate discrimination, harassment, victimisation and any other conduct that is prohibited by or under this Act; (b) advance equality of opportunity between persons who share a relevant protected characteristic and persons who do not share it; (c) foster good relations between persons who share a relevant protected characteristic and persons who do not share it." Opening, (a), (c) SV; (b) SP.
- (2) "A person who is not a public authority but who exercises public functions must, in the exercise of those functions, have due regard to the matters mentioned in subsection (1)." SV in full.
- Role: the duty binds public authorities and those exercising public functions "in the exercise of those functions". The control string asserting a duty on private service providers was absent. A private studio's own service is outside s.149 unless it is exercising a public function (s.31(4) ties that to the Human Rights Act 1998 test).

Reasonable adjustments and accessible web services
- s.20 — https://www.legislation.gov.uk/ukpga/2010/15/section/20
  - (3) "The first requirement is a requirement, where a provision, criterion or practice of A's puts a disabled person at a substantial disadvantage in relation to a relevant matter in comparison with persons who are not disabled, to take such steps as it is reasonable to have to take to avoid the disadvantage." Closing fragment SV.
  - (5) third requirement, auxiliary aids: "...to take such steps as it is reasonable to have to take to provide the auxiliary aid." SV.
  - (6) "Where the first or third requirement relates to the provision of information, the steps which it is reasonable for A to have to take include steps for ensuring that in the circumstances concerned the information is provided in an accessible format." SV in full.
  - The Act names no technical standard: the control «websites must conform to WCAG» was absent.
- Schedule 2 para 2 — https://www.legislation.gov.uk/ukpga/2010/15/schedule/2 (SP except as marked)
  - (2) "For the purposes of this paragraph, the reference in section 20(3), (4) or (5) to a disabled person is to disabled persons generally." This is the anticipatory character of the duty for services.
  - (7) "If A is a service-provider, nothing in this paragraph requires A to take a step which would fundamentally alter— (a) the nature of the service, or (b) the nature of A's trade or profession." "would fundamentally alter" SV.
- Government guidance (GDS/CDDO, "Understanding accessibility requirements for public sector bodies", last updated 30 September 2024) — https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
  - "All UK service providers have a legal obligation to make reasonable adjustments under the Equality Act 2010 or the Disability Discrimination Act 1995 (in Northern Ireland)." SV.
  - "All public sector bodies have to meet the requirements, unless they are exempt." SV. The standard named for them is "WCAG 2.2 AA". SV.

Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018, S.I. 2018/952. "No known outstanding effects."
- Correction to the brief: reg 3 is Interpretation; scope is reg 4. Reg 2 revokes the earlier 2018 Regulations.
- reg 3 — https://www.legislation.gov.uk/uksi/2018/952/regulation/3
  - "“public sector body” means— (a) the State; (b) regional or local authorities; (c) bodies governed by public law; or (d) associations formed by one or more of the authorities in paragraph (b) or one or more of the bodies in paragraph (c), if those associations are established for the specific purpose of meeting needs in the general interest, not having an industrial or commercial character". Opening and (a) SV; rest SP.
  - "bodies governed by public law" must have all of: "(a) they are established for the specific purpose of meeting needs in the general interest, not having an industrial or commercial character" (SV); "(b) they have legal personality" (SP); and one of (c), including "(i) they are financed, for the most part, by the State, regional or local authorities, or by other bodies governed by public law" (SV).
- reg 4 — https://www.legislation.gov.uk/uksi/2018/952/regulation/4
  - (1) "These Regulations apply to a website or mobile application of a public sector body, except a website or mobile application of—" SV. Exception (b): "non-governmental organisations, unless they provide services that— (i) are essential to the public; or (ii) specifically address the needs of, or are meant for, persons with disabilities". Opening SV.
  - (2)(d) excluded content: "online maps and mapping services, as long as essential information is provided in an accessible digital manner for maps intended for navigational use". SV.
  - (2)(e) "third-party content that is neither funded nor developed by, nor under the control of, the public sector body". SV.
- Role: a private studio is outside these Regulations unless it meets the "public sector body" definition. The financed-for-the-most-part limb is the one a grant-funded body would need to check.

"Information society services" — Equality Act Schedule 25 — https://www.legislation.gov.uk/ukpga/2010/15/schedule/25 (only annotation shown: S.I. 2012/1809; no EU-exit amendment visible)
- para 5(1) hosting: "An information society service provider does not contravene this Act only by doing anything in providing so much of an information society service as consists in the storage of information provided by a recipient of the service, if— (a) the service provider had no actual knowledge when the information was provided that its provision amounted to a contravention of this Act, or (b) on obtaining actual knowledge that the provision of the information amounted to a contravention of that section, the service provider expeditiously removed the information or disabled access to it." Three fragments SV.
- para 7(2): the term "has the meaning given in Article 2(a) of the E-Commerce Directive" (SV), summarised as "any service normally provided for remuneration, at a distance, by means of electronic equipment for the processing (including digital compression) and storage of data, and at the individual request of a recipient of a service". First part SV.
- Role: hosted contributions that contravene the Act are covered by a knowledge-and-expeditious-removal exception; para 6 bars a general monitoring obligation (SP, paraphrased by the reader).

Explanatory Notes to s.29 — https://www.legislation.gov.uk/ukpga/2010/15/notes/division/3/3/2/1 (paras 107–111)
- s.29 "makes it unlawful to discriminate against or harass a person because of a protected characteristic, or victimise someone when providing services (which includes goods and facilities)". SV. The word "websites" does not appear on that page.

EHRC Services, Public Functions and Associations Statutory Code of Practice: UNREACHABLE. equalityhumanrights.com returned 403 on both the code page and the PDF. Nothing quoted; the Code's paragraph on websites as services still needs sourcing.

==================================================
ITEM 2 — ONLINE SAFETY ACT 2023 FOR A SMALL INTERACTIVE SITE
==================================================
Type: statute plus regulator guidance. Date note: OSA pages show pending changes from 2026 c. 20, the Crime and Policing Act 2026 (Royal Assent 29 April 2026, checked at https://www.legislation.gov.uk/ukpga/2026/20). The reader reported s.21(2A) inserted on 29.6.2026 and s.23(5) amended to refer to "section 10(2), (3) or (3A)". The duties text is therefore moving in 2026.

Definitions
- s.3 — https://www.legislation.gov.uk/ukpga/2023/50/section/3
  - (1) "In this Act “user-to-user service” means an internet service by means of which content that is generated directly on the service by a user of the service, or uploaded to or shared on the service by a user of the service, may be encountered by another user, or other users, of the service." SV.
  - (2)(a) "it does not matter if content is actually shared with another user or users as long as a service has a functionality that allows such sharing"; (b) "it does not matter what proportion of content on a service is content described in that subsection". Both SV.
  - (4) "In this Act “search service” means an internet service that is, or includes, a search engine (see section 229)." SV to "search engine".
  - No user-number threshold: control «a service with fewer than 10,000 users is not a user-to-user service» absent.
- s.4 — https://www.legislation.gov.uk/ukpga/2023/50/section/4
  - (2) a service is regulated if it "(a) has links with the United Kingdom" and "(b) is not— (i) a service of a description that is exempt as provided for by Schedule 1". (b)(i) SV.
  - (5) "(a) the service has a significant number of United Kingdom users, or (b) United Kingdom users form one of the target markets for the service (or the only target market)". SV.
  - (6)(b) "there are reasonable grounds to believe that there is a material risk of significant harm to individuals in the United Kingdom presented by" user-generated or search content. SV to "presented by".
- s.55 — https://www.legislation.gov.uk/ukpga/2023/50/section/55
  - (3) "user-generated content" means content "(a) that is— (i) generated directly on the service by a user of the service, or (ii) uploaded to or shared on the service by a user of the service, and (b) that may be encountered by another user, or other users, of the service". (i) and (b) SV.
  - (6) "comments and reviews on provider content" means "content present on the service consisting of comments or reviews relating to provider content". SV.
  - (7) "provider content" means content "published on a service by the provider of the service or by a person acting on behalf of the provider". SV.

Schedule 1 Part 1 exemptions — https://www.legislation.gov.uk/ukpga/2023/50/schedule/1
- para 1 "A user-to-user service is exempt if emails are the only user-generated content (other than identifying content) enabled by the service." SV. para 2 SMS/MMS (SP). para 3 "one-to-one live aural communications" (phrase SV).
- para 4 Limited functionality services: "A user-to-user service is exempt if the functionalities of the service are limited, such that users are able to communicate by means of the service only in the following ways— (a) posting comments or reviews relating to provider content; (b) sharing such comments or reviews on a different internet service; (c) expressing a view on such comments or reviews, or on provider content, by means of— (i) applying a “like” or “dislike” button or other button of that nature, (ii) applying an emoji or symbol of any kind, (iii) engaging in yes/no voting, or (iv) rating or scoring the content (or the comments or reviews) in any way". Opening, (a), (c)(iii), (c)(iv) SV; rest SP.
- para 7(2) internal business services (SP): "(a) the user-to-user service or search service is an internal resource or tool for a business... (c) ... is available only to a closed group of people".
- No size exemption: control «exempt if it has fewer than 100 users» absent.
- Reading on the definitional words only, not advice: a site where members of the public post pins, text or ratings that other users can see falls within s.3(1) unless what users can do is confined to the para 4 list. That list covers comments, reviews, reactions and ratings "relating to provider content". A free-standing user pin or text is not obviously a comment "relating to provider content".

Ofcom on scope — "Overview of regulated services" (PDF; no date printed, references to September 2024) — https://www.ofcom.org.uk/siteassets/resources/documents/online-safety/information-for-industry/illegal-harms/overview-of-regulated-services.pdf
- "The Act covers services of all sizes, ranging from large, well-resourced services, through to services run by micro businesses." SV.
- The exemption applies where the only way users can communicate is by "posting comments or reviews on the service provider’s own content (as distinct from another user’s content)". SV. Example: "For example, this would exempt services where users can only write 'below the line' comments or reviews on media articles..." (SP; "below the line" SV).
- "The Act does not define what is meant by a ‘significant number’ of UK users" (SV); "service providers should be able to explain their judgement" (SV).

Duties in the Act
- s.9 — https://www.legislation.gov.uk/ukpga/2023/50/section/9 — (1) "This section sets out the duties about risk assessments which apply in relation to all regulated user-to-user services." (2) "A duty to carry out a suitable and sufficient illegal content risk assessment at a time set out in, or as provided by, Schedule 3." (3) "A duty to take appropriate steps to keep an illegal content risk assessment up to date..." All SV. Control «This section does not apply to small services.» absent.
- s.10 — https://www.legislation.gov.uk/ukpga/2023/50/section/10 — (2) "A duty, in relation to a service, to take or use proportionate measures relating to the design or operation of the service to— (a) prevent individuals from encountering priority illegal content by means of the service, ..." (SP). (3)(b) "where the provider is alerted by a person to the presence of any illegal content, or becomes aware of it in any other way, swiftly take down such content." SV. No fixed period: «within 24 hours» absent.
- s.20 (SP) — (2) "A duty to operate a service using systems and processes that allow users and affected persons to easily report content...". (5) "affected person" includes a person who is "(a) the subject of the content, (b) a member of a class or group of people with a certain characteristic targeted by the content".
- s.21 (SP) — (2) a complaints procedure that "(c) is easy to access, easy to use (including by children) and transparent."
- s.23 (SP, reader truncated) — (2) "A duty to make and keep a written record, in an easily understandable form, of all aspects of every risk assessment under section 9 or 11..."; (6) "A duty to review compliance with the relevant duties in relation to a service— (a) regularly, and (b) as soon as reasonably practicable after making any significant change...".
- s.35 Children's access assessments — https://www.legislation.gov.uk/ukpga/2023/50/section/35
  - (2) "A provider is only entitled to conclude that it is not possible for children to access a service, or a part of it, if age verification or age estimation is used on the service with the result that children are not normally able to access the service or that part of it." SV in full.
  - (3) child user condition: "(a) there is a significant number of children who are users of the service or of that part of it, or (b) the service, or that part of it, is of a kind likely to attract a significant number of users who are children." SV.
  - (4)(b) the test "is to be based on evidence about who actually uses a service, rather than who the intended users of the service are". SV. No numeric threshold (control absent).
- s.12 (SP) — (1) "This section sets out the duties to protect children's online safety which apply in relation to regulated user-to-user services that are likely to be accessed by children." (3)(a) "prevent children of any age from encountering, by means of the service, primary priority content that is harmful to children".
- Schedule 13 para 4(1) — https://www.legislation.gov.uk/ukpga/2023/50/schedule/13 — "Where a penalty is imposed on a person in respect of a regulated service provided by that person, the maximum amount of the penalty for which the person is liable is whichever is the greater of— (a) £18 million, and (b) 10% of the person’s qualifying worldwide revenue for the person’s most recent complete accounting period (subject to sub-paragraph (5))." Three fragments SV; controls £20 million and 4% absent.

Ofcom dates and tiers
- "Time for tech firms to act: UK online safety regulation comes into force", 16 December 2024 — https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/time-for-tech-firms-to-act-uk-online-safety-regulation-comes-into-force
  - "Every site and app in scope of the new laws has from today until 16 March 2025 to complete an assessment to understand the risks illegal content poses to children and adults on their platform." First part SV.
  - "from 17 March 2025, sites and apps will then need to start implementing safety measures to mitigate those risks". SV.
  - "Some of these measures apply to all sites and apps, and others to larger or riskier platforms." SV.
  - "We have the power to fine companies up to £18m or 10% of their qualifying worldwide revenue". SV.
- "Statement: Protecting people from illegal harms online" (published 16 December 2024, updated 25 June 2026) — https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-protecting-people-from-illegal-harms-online
  - "Providers now have a duty to assess the risk of illegal harms on their services, with a deadline of 16 March 2025." SV.
  - "Subject to the Codes completing the Parliamentary process, from 17 March 2025, providers will need to take the safety measures set out in the Codes or use other effective measures to protect users from illegal content and activity." (the reader supplied the full sentence on the verify pass).
  - The linked overview PDF says "over 130 priority offences and 100K+ services in scope of our regulation" (SP).
- "Important dates for Online Safety compliance" (published 17 October 2024, updated 24 August 2026) — https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/important-dates-for-online-safety-compliance
  - The dates 16 March 2025, 16 April 2025, 24 July 2025 and 25 July 2025 are all on the page (SV as strings). The reader garbled the table rows on the verify pass, so treat these labels as SP: 16 March 2025 "Carry out illegal content risk assessment"; 17 March 2025 "Illegal content Codes of Practice comes into force"; 16 April 2025 children's access assessment; 24 July 2025 "Carry out children's risk assessment"; 25 July 2025 "Protection of Children Codes of Practice come into force".
- "Children's access assessment duties under the Online Safety Act" (published 7 May 2024, updated 29 June 2026) — https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/childrens-access-assessment-duties-under-the-online-safety-act
  - "All user-to-user and search services must carry out a children's access assessment by 16 April 2025." SV.
  - "highly effective age assurance" (SV); "All services need to record the outcome of each children's access assessment." (SV on the core phrase).
- "Illegal content duties under the Online Safety Act" (published 18 February 2026, updated 25 June 2026) — https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/illegal-content-duties-under-the-online-safety-act
  - "You have three months to complete a risk assessment after launching a service that the Act applies to". This is the rule for a new service launched now.
  - "swiftly remove illegal content when you become aware of it, and minimise the time it is present on your service"; "allow people to easily report illegal content and operate a complaints procedure" (SV); "You need to keep a written record of every risk assessment you carry out".
  - "If your service is low or negligible risk for all kinds of priority illegal content, you are a 'low risk service;' and the minimum number of measures apply." SV in two fragments.
  - "If your service is medium or high risk for two or more kinds of illegal harm, we define it as a 'multi-risk' service, and further measures may apply." First part SV.
  - "In our Codes of Practice, we have defined a large service as a service which has an average user base of 7 million or more per month in the UK." SV.
  - "Some measures will apply to all services." (SV). "For example, these include naming a individual accountable for online safety compliance and ensuring your terms of service (or publicly available statements) are clear and accessible." (SP).
  - "For small services without formal boards or oversight teams, this can simply mean reporting to a senior manager with responsibility for online safety." Second half SV.
  - "You can decide for yourself how to meet the specific legal duties; you can apply the measures that apply to your service set out in Ofcom's Codes of Practice or you can take alternative measures." Second half SV.
  - Control «Low risk services are exempt from the illegal content duties» absent.
- "Illegal content Codes of Practice for user-to-user services" (issued 24 February 2025, in force 17 March 2025) — https://www.ofcom.org.uk/siteassets/resources/documents/online-safety/information-for-industry/illegal-harms/illegal-content-codes-of-practice-for-user-to-user-services-24-feb.pdf
  - Large service: "more than 7 million monthly active United Kingdom users". SV. This wording differs from the web page's "7 million or more per month".
  - Measures said to apply "to a provider in respect of each service it provides" (SP for that list): ICU A2 "Individual accountable for illegal content safety duties and reporting and complaints duties" (SV); ICU C1 "Having a content moderation function to review and assess suspected illegal content" (SV); ICU C2 "Having a content moderation function that allows for the swift take down of illegal content" (SV); ICU D1 "Enabling complaints" (SP); ICU D2 "Having easy to find, easy to access and easy to use complaints systems and processes" (SV); ICU G1 "Terms of service: substance (all services)" (SP); ICU G3 "Terms of service: clarity and accessibility" (SP); ICU H1 "Removing accounts of proscribed organisations" (SP). The reader also listed ICU D7, D10, D12, D13 without titles.
  - The reader mentioned a "more than 700,000 monthly active United Kingdom users" threshold; I did not establish what it attaches to.
- "Protection of children duties under the Online Safety Act" (published 18 February 2026, updated 1 April 2026) — https://www.ofcom.org.uk/online-safety/protecting-children/protection-of-children-duties-under-the-online-safety-act
  - "All providers of user-to-user and search services in scope of the Act must establish whether their service is likely to be accessed by children". SV.
  - "You have three months to complete a children's risk assessment after launching a service that the protection of children duties apply to". SV.
  - Non-designated content presents a "material risk of significant harm to an appreciable number of children in the United Kingdom". SV.
- "Online Safety Act compliance guide for providers of online services" (published 27 February 2024, updated 21 May 2025) — https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/guide-for-services — "fines of up to 10% of your qualifying worldwide revenue, or £18 million, whichever is greater". SV.
- DSIT "Online Safety Act: explainer" (published 8 May 2024, updated 24 April 2025) — https://www.gov.uk/government/publications/online-safety-act-explainer/online-safety-act-explainer
  - "The Act’s duties apply to search services and services that allow users to post content online or to interact with each other." SV.
  - "Providers’ safety duties are proportionate to factors including the risk of harm to individuals, and the size and capacity of each provider." SV. "...we aren’t requiring small services with limited functionality to take the same actions as the largest corporations". SV.
  - "Companies can be fined up to £18 million or 10 percent of their qualifying worldwide revenue, whichever is greater." SV. Control «Small services are exempt from the Act.» absent.
- Role: there is no small-site exemption. Proportionality works through the low-risk / multi-risk / large tiers and the "alternative measures" route. For a service launched after 2025 the operative clock is three months from launch.

==================================================
ITEM 3 — TYPOLOGIES OF HARM
==================================================
Citron & Solove, "Privacy Harms", 102 Boston University Law Review 793 (2022) — https://www.bu.edu/bulawreview/files/2022/04/CITRON-SOLOVE.pdf (full text; SSRN returned 429). Legal scholarship.
- Typology headings: A. Physical Harms; B. Economic Harms; C. Reputational Harms; D. Psychological Harms (1. Emotional Distress, 2. Disturbance); E. Autonomy Harms (1. Coercion, 2. Manipulation, 3. Failure to Inform, 4. Thwarted Expectations, 5. Lack of Control, 6. Chilling Effects); F. Discrimination Harms; G. Relationship Harms. "Relationship Harms", "Discrimination Harms" and "Thwarted Expectations" SV; the rest SP.
- Why courts fail: "The requirement of harm has significantly impeded the enforcement of privacy law." SV. "Case law is an inconsistent, incoherent jumble with no guiding principles." SV. "Countless privacy violations are not remedied or addressed on the grounds that there has been no cognizable harm." SV.
- Mechanism (SP): "When privacy violations result in negative consequences, the effects are often small—frustration, aggravation, anxiety, inconvenience—and dispersed among a large number of people." "Over time, as people are individually inundated by a swarm of small harms, the overall societal impact is significant."
- Limit: a US-law frame. Defining sentences for the discrimination and relationship categories were beyond the reader's window.

ICO, "How do we do a DPIA?" (last updated 18 February 2026) — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/how-do-we-do-a-dpia/ . Regulator guidance.
- "Consider the potential impact on individuals and any harm or damage your processing may cause – whether physical, emotional or material." SV.
- List: "inability to exercise rights (including but not limited to privacy rights)" (SV); "inability to access services or opportunities" (SV); "loss of control over the use of personal data" (SV); "discrimination"; "identity theft or fraud"; "financial loss"; "reputational damage"; "physical harm"; "loss of confidentiality"; "re-identification of pseudonymised data" (SV); "any other significant economic or social disadvantage" (SV). Unmarked items SP.
- The list is framed on individuals. No group, place or community harm appears; the control on neighbourhood stigma was absent.

ICO, "Overview of Data Protection Harms and the ICO's Taxonomy" (April 2022) — https://ico.org.uk/media/about-the-ico/documents/4020144/overview-of-data-protection-harms-and-the-ico-taxonomy-v1-202204.pdf . Regulator framework.
- Individual harms: "Financial harm"; "Bodily harm"; "Costs of avoiding/mitigating harm"; "Discrimination"; "Unwarranted intrusion"; "Loss of control of personal data"; "Lack of autonomy; manipulation and influence"; "Psychological Harms"; "Chilling effects"; "Adverse effects on rights and freedoms". All SV.
- Societal harms: "Damage to law and justice" (ambiguous on verify, treat as SP); "Damage to media, democracy, information and public discourse" (SV); "Damage to public health"; "Damage to the economy"; "Damage to the environment" (SP).
- "It allows us to focus on what the consequences of an infringement of data protection rights are for individuals and for society." Returned on both passes.
- Role: the UK regulator's own taxonomy has a societal tier. No heading names stigma of place (control absent).

Algorithmic-harm taxonomy (one source): Shelby et al., "Sociotechnical Harms of Algorithmic Systems: Scoping a Taxonomy for Harm Reduction" (arXiv 2210.05791; submitted 11 October 2022, revised 19 July 2023) — https://arxiv.org/abs/2210.05791 . ABSTRACT.
- "Based on a scoping review of computing research (n=172), we present an applied taxonomy of sociotechnical harms". n=172 SV.
- "Five major themes related to sociotechnical harms - representational, allocative, quality-of-service, interpersonal harms, and social system/societal harms". List SV.
- I substituted this for a CDEI or Ada Lovelace taxonomy: the two pages I opened (CDEI bias review, 27 November 2020; Ada Lovelace AIA healthcare case study, 8 February 2022) contained no headed taxonomy.

==================================================
ITEM 4 — MAPS AND LABELS THAT HARMED PLACES
==================================================
Wacquant 2007, "Territorial Stigmatization in the Age of Advanced Marginality", Thesis Eleven 91(1): 66–77 — https://journals.sagepub.com/doi/10.1177/0725513607082003 . ABSTRACT only (paywalled). Critical scholarship.
- "...this article spotlights three distinctive spatial properties of `advanced marginality' — territorial fixation and stigmatization, spatial alienation and the dissolution of `place', and the loss of a hinterland". Fragments SV. No definitional sentence was reachable.

Wacquant, Slater & Pereira 2014, "Territorial Stigmatization in Action", Environment and Planning A 46(6): 1270–1280 — https://journals.sagepub.com/doi/10.1068/a4606ge . ABSTRACT; the reader said open access but showed only the abstract.
- The concept is used "to capture how the blemish of place impacts the residents of disparaged districts, the surrounding denizens and commercial operators, street-level public bureaucracies, specialists in cultural production (such as journalists, scholars, and politicians), and state officials and policies." First clause SV.
- "it has become autonomized, nationalized and democratized, equated with social disintegration, racialized through selective accentuation". SV.
- "Territorial stigmatization is not a static condition or a neutral process, but a consequential and injurious form of action through collective representation fastened on place." SV in two fragments.
- Policies should reduce "not only the burden of material deprivation, but also the press of symbolic domination in the metropolis." SV.
- Role: stigma is an action done through representations of place, and "scholars" are named among those who produce it. The abstract makes no claim about statistics or dashboards (control absent).

Redlining
- Mapping Inequality (dsl.richmond.edu): UNREACHABLE (robots failure on two URLs). Nothing quoted.
- Aaronson, Hartley & Mazumder, "The Effects of the 1930s HOLC 'Redlining' Maps", AEJ: Economic Policy 13(4): 355–92 (November 2021) — https://www.aeaweb.org/articles?id=10.1257/pol.20190414 . Peer-reviewed; ABSTRACT.
  - "The maps led to reduced home ownership rates, house values, and rents and increased racial segregation in later decades." SV.
  - "These results suggest the HOLC maps had meaningful and lasting effects on the development of urban neighborhoods through reduced credit access and subsequent disinvestment." SV.
  - The published abstract has no effect sizes. They are in the working paper (Chicago Fed WP 2017-12, revised August 2020) — https://www.chicagofed.org/-/media/publications/working-papers/2017/wp2017-12-pdf.pdf :
  - "Overall, we conclude that the maps account for between 15 to 30 percent of the overall gap in share African American and home ownership over the 1950 to 1980 period and 40 percent of the gap in house values." SV.
  - The gap in share African American "peaks at between 15 and 17 percentage points" (SV); the reader placed this at D–C boundaries, 1950–1970 (SP).
  - "The HOLC drew maps for over 200 cities as part of its City Survey Program to document the relative riskiness of lending across neighborhoods." SP.
  - "The term “redlining” is thought by many to derive from the red shading that demarcated the lowest ranked D neighborhoods". SV. Grade descriptions quoted in the paper: B "like a 1935 automobile" (SV), C "infiltration of a lower grade population" (SV).
- Counter-position: Fishback, LaVoice, Shertzer & Walsh, "The HOLC Maps: How Race and Poverty Influenced Real Estate Professionals' Evaluation of Lending Risk in the 1930s", NBER WP 28146 (November 2020, revised October 2021); Journal of Economic History 83(4): 1019–1056 (2023) — https://www.nber.org/papers/w28146 . ABSTRACT.
  - "We provide evidence that these maps were not the primary source used by the FHA to create their 'redlining' maps for insuring mortgages." First part SV.
  - "the HOLC maps provide a unique snapshot of how real estate professionals perceived lending risk in the 1930s". SV.
  - "racial bias in the construction of the HOLC maps can explain at most 4 to 20 percent of the observed concentration of black households in the lowest-rated zones." SV.
  - "decades of disadvantage and discrimination had already pushed them into the core of economically distressed neighborhoods". SV.
  - Role: the debate is whether the map caused the harm or recorded and formalised an existing judgement.

Crime maps (UK)
- ICO, "Crime-mapping and geo-spatial crime data: privacy and transparency" ("Crime-mapping 20140226 Version: 3.5") — https://ico.org.uk/media/for-organisations/documents/1543/crime_mapping.pdf . Regulator advice, 2014.
  - "Publishing exact household level mapping pins on crime maps will generally constitute the processing of personal data and is likely to breach the first data protection principle's requirement of fairness." SV to "principle".
  - "The greater the number of individuals (number of properties X number of residents) in a mapping area, the lower the privacy risk." SV (para 19).
  - "The privacy risk declines the less frequently the data is uploaded." SV.
  - "The use of heat maps, blocks and zones can help to represent crime location and type in a way which reduces privacy risks." SV.
  - "Crime-maps clearly have a range of secondary uses, for example to estate agents or insurance companies." SV (para 40). Then (SP): "...the publisher of a crime-map may be powerless to prevent secondary uses of the data recorded on it once it has gone into the public domain. Personal data is not 'fair game', even if it is already publicly available."
  - The phrase "house prices" does not appear.
- Braakmann 2017, "The link between crime risk and property prices in England and Wales: Evidence from street-level data", Urban Studies 54(8): 1990–2007 — https://journals.sagepub.com/doi/10.1177/0042098016634611 . ABSTRACT.
  - Data: land registry transactions and "recently published crime maps for the whole of the UK". SV.
  - "each case of anti-social behaviour per ten population in the same street leads to an approximately 0.6–0.8% drop in property prices, while a corresponding increase in violent crime decreases prices by roughly 0.6–1.6%". SV.
  - "Crime outside of the respective street does not appear to matter". SV.
  - Caution: this estimates the price of street-level crime risk using the maps' data. It does not test whether publishing the maps moved prices (control absent).
- Chainey & Tompson 2012, "Engagement, Empowerment and Transparency: Publishing Crime Statistics using Online Crime Mapping", Policing 6(3): 228–239 — https://academic.oup.com/policing/article/6/3/228/1456905 . ABSTRACT.
  - "many of the original objectives relating to improving engagement and empowerment have yet to be realized, poor cartographic discipline has led to misinterpretation and confusion". Both halves SV.
- Journalism on the 2011 police.uk launch: BBC and Guardian are blocked by the fetch tool. Nothing quoted.

Ecological fallacy
- Robinson 1950, IJE reprint 38(2): 337–341 (2009) — https://academic.oup.com/ije/article/38/2/337/658252 . Opening only; conclusion paywalled.
  - "An individual correlation is a correlation in which the statistical object or thing described is indivisible." SV. "In an ecological correlation the statistical object is a group of persons." SV.
  - The concluding "cannot validly be used as substitutes" sentence was not in the visible text and is not quoted.
- UK official statements of the same point: UKSA geospatial ethics guidance and the Indices of Deprivation FAQ, under Unexpected threads.

Neighbourhood labelling
- Sampson & Raudenbush 2004, "Seeing Disorder: Neighborhood Stigma and the Social Construction of 'Broken Windows'", Social Psychology Quarterly 67(4): 319–342 — https://journals.sagepub.com/doi/10.1177/019027250406700401 . ABSTRACT.
  - Data: interviews, census, police records and systematic observation "situated within some 500 block groups in Chicago". SV.
  - "Observed disorder predicts perceived disorder, but racial and economic context matter more." SV.
  - "As the concentration of minority groups and poverty increases, residents of all races perceive heightened disorder even after we account for an extensive array of personal characteristics and independently observed neighborhood conditions." First part SV.
  - "...generating self-reinforcing processes that may help account for the perpetuation of urban racial inequality." SV.
  - Read for mechanism only: perceptions of a place track who lives there more than what is observed there.
- Sampson 2012, Great American City (University of Chicago Press) — https://press.uchicago.edu/ucp/books/book/chicago/G/bo5514383.html . Publisher description, SP: "He discovers that neighborhoods influence a remarkably wide variety of social phenomena, including crime, health, civic engagement, home foreclosures, teen births, altruism, leadership networks, and immigration."

==================================================
ITEM 5 — COORDINATES FOR SPECULATION
==================================================
Glaeser, Kim & Luca 2018, "Nowcasting Gentrification: Using Yelp Data to Quantify Neighborhood Change", AEA Papers and Proceedings 108: 77–82 (May 2018) — https://www.aeaweb.org/articles?id=10.1257/pandp.20181034 . ABSTRACT.
- "We find that gentrifying neighborhoods tend to have growing numbers of local groceries, cafes, restaurants, and bars, with little evidence of crowd-out of other types of businesses." SV in two fragments.
- "Moreover, local economic activity, as measured by Yelp data, is a leading indicator for housing price changes and can help to predict which neighborhoods are gentrifying." SV.
- Companion (NBER WP 24010, November 2017, SP): Yelp data "can explain 29.2 percent of the residual variance after accounting for lagged CBP data". https://www.nber.org/papers/w24010
- Role: fine-grained public data on local venues is a leading price indicator, which is the mechanism by which a dashboard becomes an investment signal.

Barron, Kung & Proserpio 2021, "The Effect of Home-Sharing on House Prices and Rents: Evidence from Airbnb", Marketing Science 40(1): 23–47 — https://pubsonline.informs.org/doi/10.1287/mksc.2020.1227 . ABSTRACT.
- "a 1% increase in Airbnb listings leads to a 0.018% increase in rents and a 0.026% increase in house prices." SV.
- "an annual increase of $9 in monthly rent and $1,800 in house prices for the median zip code in our data, which accounts for about one-fifth of actual rent growth and about one-seventh of actual price growth." SV.

Braakmann 2017 (item 4) is the UK instance of published street-level place data being capitalised into prices.

Cortright 2009, "Walking the Walk": UNREACHABLE (three hosts: 404, 429, expired certificate). Nothing quoted. Opportunity Zones and "Zillow effect" literature not pursued.

==================================================
ITEM 6 — VISIBILITY AS A RISK TO COMMUNITIES
==================================================
Read as technology and harm mechanism only.

Hoang, Asano & Yoshikawa, "Your Neighbors Are My Spies: Location and other Privacy Concerns in GLBT-focused Location-based Dating Applications" (arXiv 1604.08235; manuscript dated 11 March 2016; follow-up to an 18th IEEE ICACT paper) — https://arxiv.org/pdf/1604.08235 . Peer-reviewed conference line; full text read.
- "Trilateration is one of the well-known threat models to the user's location privacy in location-based apps; especially those contain highly sensitive information such as dating apps." First clause SV.
- "The threat model mainly bases on the publicly shown distance from a targeted victim to the adversary to pinpoint the victim's location." SP.
- "...most of location-based apps have already implemented the "hide distance" function, or added noise to the publicly shown distance... The effectiveness of such approaches however is still questionable." Last sentence SV.
- "...we also show how the adversary can still figure out the location of a targeted victim even when the "show distance" function is disabled in Grindr." SV.
- Users on default settings "are facing a high risk of being located since the adversary can obtain an accurate location up to the victim's building". "up to the victim's building" SV.
- Earlier disclosure, as cited by the paper: "the trilateration threat model (aka: triangulation) is said to be first reported to Grindr in 2014" (SV), citing ref [11] titled "Grindr: A chronicle of negligence and irresponsibility" (title SV); "Grindr has adopted a function in which the user can opt to hide the distance since August 2014" (SV).
- The Synack / Colby Moore write-up itself was not fetched (Wired is blocked), so the paper does not name Synack in anything I verified.
- Role: hiding or coarsening one field (distance) did not prevent location inference. This is a concrete case of disclosure control defeated by repeated querying.

Norwegian Consumer Council, "Out of Control: How consumers are exploited by the online advertising industry" (14 January 2020) — https://storage02.forbrukerradet.no/media/2020/01/2020-01-14-out-of-control-final-version.pdf . NGO research with a commissioned technical test.
- "the ten apps were observed transmitting user data to at least 135 different third parties involved in advertising and/or behavioural profiling". SV.
- "Grindr shared detailed user data with a large number of third parties" (SV)... "This data included IP address, Advertising ID, GPS location, age, and gender." (SV).
- A large amount of the sharing "appears to be illegal under the General Data Protection Regulation". SV.
- "The extent of tracking and complexity of the adtech industry is incomprehensible to consumers, meaning that individuals cannot make informed choices about how their personal data is collected, shared and used." SP.
- The reader could not find a sentence saying the app's name alone reveals sexual orientation. It found, at 2.4.1, that keywords such as "gay" and "bi" were observed being transmitted (paraphrase; SP).

The fine. Correction to the brief: the authority is Datatilsynet, the Norwegian DPA, not the ICO. Datatilsynet's own decision page was UNREACHABLE (robots failure, three attempts). Secondary source, the complainant's own pages (NGO):
- Forbrukerrådet, 15 December 2021 — https://www.forbrukerradet.no/side/grindr-hit-with-e-6-2-million-fine-in-response-to-complaint-from-the-norwegian-consumer-council/
  - "The Norwegian Data Protection Authority confirmed that Grindr has been sharing personal data without a legal basis and fined the dating app 65 million NOK (€ 6.2 million)." Returned on the verify pass; "65 million NOK", "€ 6.2 million" and "Norwegian Data Protection Authority" SV.
  - "This information was illegally collected and must be considered as particularly sensitive as it concerns users' sexual orientation." Returned on the verify pass; "sexual orientation" SV.
  - My control string "100 million NOK" came back YES. I did not read the sentence it sits in, so I cannot say what it refers to.
- Forbrukerrådet, "Grindr loses appeal", 21 October 2025 — https://www.forbrukerradet.no/news-in-english/grindr-loses-appeal/
  - "Today it was announced that the appeal by dating app Grindr's was unsuccessful, and the administrative fine of 65 million NOK (ca €5.5 million) is upheld." Returned on the verify pass; "65 million NOK" and "Court of Appeal" SV.
  - "Following decisions from the Norwegian Data Protection Authority and the Privacy Appeals Board, plus a ruling in the Oslo District Court, the Court of Appeal has issued its decision." SP.

Inference by association
- Jernigan & Mistree 2009, "Gaydar: Facebook friendships expose sexual orientation", First Monday 14(10) — https://firstmonday.org/ojs/index.php/fm/article/view/2611 . ABSTRACT; open.
  - "Public information about one’s coworkers, friends, family, and acquaintances, as well as one’s associations with them, implicitly reveals private information." SV.
  - "Network data shifts the locus of information control away from individuals". SV.
  - "After analyzing 4,080 Facebook profiles from the MIT network" (SV)... "we developed a logistic regression classifier with strong predictive power." (SP).
  - "...raising significant privacy issues for communication technologies to which there are no neat solutions." SV.
  - Strength: a 2009 student study on one network; cite for the mechanism, not the accuracy.
- Kosinski, Stillwell & Graepel 2013 (PNAS): UNREACHABLE (PMC captcha; PNAS 403).

Counting and visibility
- Ruberg & Ruelos 2020, "Data for queer lives: How LGBTQ gender and sexuality identities challenge norms of demographics", Big Data & Society 7(1) — https://journals.sagepub.com/doi/10.1177/2053951720933286 . Open access; critical scholarship.
  - "we draw from the responses of 178 people who identified as non-heterosexual or non-cisgender". SV.
  - "Demographic data commonly imagines identity as fixed, singular, and discrete." SV.
  - "...queer perspectives destabilize the underlying logics of data by resisting classification and "capture."" Fragment SV.
  - "...the issue of who is or is not "counted" profoundly affects visibility, access, and power in the digital realm." Ending SV.
  - I did not find a paper that uses the phrase "forced visibility"; this is the nearest verified source.

eSafety Commissioner (Australia), Safety by Design principles — https://www.esafety.gov.au/industry/safety-by-design/principles-and-background . Regulator framework; no date shown on the page.
- "At the heart of Safety by Design are three principles that provide platforms and services with guidance as they incorporate, assess and enhance user safety." SV.
- 1. "Service provider responsibility" (SV): "The burden of safety should never fall solely upon the user." (SV). "This involves assessing the potential risks of online interactions upfront and taking active steps to engineer out potential misuse, reducing people's exposure to harms." (SP).
- 2. "User empowerment and autonomy" (SV): "The dignity of users is of central importance." (SV). "Products and services should align with the best interests of users." (SV).
- 3. "Transparency and accountability" (SV): "Transparency and accountability are hallmarks of a robust approach to safety." (SV).

==================================================
ITEM 7 — MODERATION AND HOSTILE CONTRIBUTORS
==================================================
Grimmelmann, "The Virtues of Moderation", 17 Yale J.L. & Tech. 42 (2015) — https://yjolt.org/sites/default/files/grimmelmann_the-virtues-of-moderation_0.pdf . Legal scholarship; full text. Citation line SV. The journal's landing page reader gave 2005; that is an error, the PDF prints 2015.
- Definition: "By 'moderation,' I mean the governance mechanisms that structure participation in a community to facilitate cooperation and prevent abuse." Fragment from "the governance mechanisms" SV.
- "The real study of moderation begins with the verbs of moderation—the basic actions that moderators can take to affect the dynamics of a community. There are four: excluding, pricing, organizing, and norm-setting." Last sentence SV.
- Headings: "A. Techniques (Verbs)" — "1. Excluding", "2. Pricing", "3. Organizing", "4. Norm-Setting"; "B. Distinctions (Adverbs)". All SV. Sub-items SP: under Organizing — Deletion, Editing, Annotation, Synthesis, Filtering, Formatting; the adverbs — Automatically / Manually, Transparently / Secretly, Ex Ante / Ex Post, Centrally / Distributedly.
- "Pricing inhibits participation, both good and bad, by raising its costs." SV. "Organization shapes the flow of content from authors to readers." SV. "Moderation's biggest challenge and most important mission is to create strong shared norms among participants." Ending SV. "Exclusion is fundamental in property theory because of its simplicity." SP.

Gillespie 2018, Custodians of the Internet: UNREACHABLE (Yale University Press disallowed by robots; the book's own site returned 429 twice). Nothing quoted.

Pew Research Center, "The State of Online Harassment" (Emily A. Vogels, 13 January 2021) — https://www.pewresearch.org/internet/2021/01/13/the-state-of-online-harassment/ . Survey research; "10,093 U.S. adults", "Sept. 8 to 13, 2020" (both SV). US data.
- "A Pew Research Center survey of U.S. adults in September finds that 41% of Americans have personally experienced some form of online harassment in at least one of the six key ways that were measured." Core SV.
- 25% have experienced more severe forms (figure on the page; the framing sentence is SP).
- Lesbian, gay or bisexual adults: "Roughly seven-in-ten have encountered any harassment online and fully 51% have been targeted for more severe forms of online abuse." SV.
- "About half or more Black (54%) or Hispanic online harassment targets (47%) say they were harassed due to their race or ethnicity, compared with 17% of White targets." SP.

Amnesty International, news release of November 2017 (the Ipsos MORI poll behind "Toxic Twitter") — https://www.amnesty.org/en/latest/news/2017/11/amnesty-reveals-alarming-impact-of-online-abuse-against-women/ . NGO research. The "Toxic Twitter" 2018 chapter URL failed with redirects; the reader did not show a headline or date on the release.
- "Nearly a quarter (23%) of the women surveyed across these eight countries said they had experienced online abuse or harassment at least once". SV.
- "Over three quarters (76%) of women who said that they had experienced abuse or harassment on a social media platform made changes to the way they use the platforms". SV.
- "32% of women said they’d stopped posting content that expressed their opinion on certain issues". SV.
- Survey details (SP): Ipsos MORI, about 4,000 women aged 18–55 in eight countries.
- Role: the participation cost. Harassment changes who contributes.

Contribution gating, method source
- Wikipedia and Stack Overflow documentation: both UNREACHABLE (Wikipedia domain "cache-only"; Stack Overflow and Stack Exchange blocked). The MediaWiki manual page did not show the thresholds.
- Substitute: Discourse, "Understanding Discourse Trust Levels" (Jeff Atwood, 25 June 2018; marked updated December 2025) — https://blog.discourse.org/2018/06/understanding-discourse-trust-levels/ . Practitioner documentation.
  - Trust levels are a way of "Sandboxing new users in your community so that they cannot accidentally hurt themselves, or other users while they are learning what to do." SV. And "Granting experienced users more rights over time, so that they can help everyone maintain and moderate the community they generously contribute so much of their time to." SV.
  - Levels 0–4: New, Basic, Member, Regular, Leader (SP). Level 0 users cannot, among other things, "Post more than 2 hyperlinks in a post" (SV). Level 1 requires "Entering at least 5 topics" (SV), "Reading at least 30 posts" (SV), and "Spend a total of 10 minutes reading posts" (SP).
  - In Grimmelmann's terms this is pricing and exclusion, applied automatically and ex ante.

==================================================
ITEM 8 — RESEARCH-ETHICS BASELINES FOR A NON-UNIVERSITY BODY
==================================================
UKRI/ESRC Framework for research ethics. Funder framework.
- Finding: none of the five ESRC pages I read contains a sentence about non-HEI organisations or organisations without their own ethics committee. "non-HEI", "independent research organisations" and "human participants" are absent from the core principles page.
- "Our core principles" (last updated 12 May 2025) — https://www.ukri.org/councils/esrc/guidance-for-applicants/research-ethics-guidance/framework-for-research-ethics/our-core-principles/
  - "This ESRC framework for research ethics sets out good practice for social science research, detailing our principles and expectations from researchers, research organisations (ROs) and research ethics committees (RECs)." SV.
  - "This guidance should be observed by ESRC-funded researchers and ROs, and may be useful to other research-related audiences." Returned on the verify pass.
- "Relevant ethics terms and conditions" (last updated 7 May 2026) — https://www.ukri.org/councils/esrc/guidance-for-applicants/research-ethics-guidance/framework-for-research-ethics/relevant-ethics-terms-and-conditions/
  - "Overall responsibility for ensuring that all ESRC-funded research is subject to appropriate ethics review and monitoring lies with the research organisation (RO)." SV. "Ethics review should be carried out before any work requiring ethics review is undertaken." SV.
- "Ethics reviews" (last updated 12 May 2025; SP) — https://www.ukri.org/councils/esrc/guidance-for-applicants/research-ethics-guidance/ethics-reviews/
  - Light-touch review applies where "the actual or potential risk or harm to participants (and others affected by the proposed research) is minimal."
  - "it is likely that much research activity will require full ethics review, and methods such as further analysis of data are not necessarily exempt from full review."
- Role: the framework binds ESRC-funded work. For a body not so funded, its own words are that it "may be useful".

Market Research Society Code of Conduct 2023 (effective 15 May 2023) — https://www.mrs.org.uk/pdf/MRS-Code-of-Conduct-2023.pdf . Professional self-regulatory code, binding on MRS members and company partners.
- Rule 31: "If consent is the legal basis for a data collection exercise, Members must ensure that participants are provided with appropriate information to allow informed consent to be given, at the point that they agree to participate." SV from "Members must ensure". Note the conditional opening.
- Rule 34: "Members must ensure that a participant’s right to withdraw from a project at any stage is respected." SV.
- Rule 23: "Members must take reasonable steps to assess, identify and consider the particular needs of vulnerable people involved in their professional activities." SV.
- Rule 49: "Members must ensure that the anonymity of participants is preserved unless participants have given their informed consent for their details to be revealed or for attributable comments to be passed on." Full sentence returned on the verify pass.
- Definitions: "A child is an individual under the age of 16." (SV). Vulnerable people are "individuals whose permanent or temporary personal circumstances and/or characteristics mean that they are less able to protect or represent their interests" (SV).
- Children (SP; rule number not confirmed, the reader gave the range 16–22): "Members must ensure that permission of a responsible adult is obtained and verified before a child participates in their professional activities."

AoIR, "Internet Research: Ethical Guidelines 3.0" (franzke, Bechmann, Zimmer, Ess and the AoIR Ethics Working Group; 6 October 2019) — https://aoir.org/reports/ethics3.pdf . Scholarly association guidelines. Page numbers are as the reader reported them.
- Public/private (p.7): "Even though these expectations were not warranted by the technical realities of a given forum or SNS, especially deontological ethics calls for respecting these expectations". Both halves SV.
- Judgement: "Taken together, all of this means that the best we can do is develop 'guidelines, not recipes'" (p.6; phrase SV). The emphasis is on "asking the right / relevant questions" (SV). "such judgment is deeply relational and intersubjective" (p.23; SV). "ethical pluralism" (SV).
- Consent at scale: "Such consent is manifestly impracticable in the case of Big Data projects, however, resulting in a serious ethical dilemma." SV.
- Vulnerability: "the greater the vulnerability of our subjects, the greater our responsibility and obligation to protect them from likely harms". SV.
- Community consent (p.8; SP): "Informed consent may need to be sought not only from individuals, but also from communities and online system administrators".
- The control «Public data may be used without any ethical review.» was absent.

==================================================
UNEXPECTED THREADS (8)
==================================================
1. UK Statistics Authority, "Ethical considerations in the use of geospatial data for research and statistics" (18 May 2021). The closest thing I found to a UK official statement on maps that harm places. Base URL https://uksa.statisticsauthority.gov.uk/publication/ethical-considerations-in-the-use-of-geospatial-data-for-research-and-statistics/ (chapters at /pages/3/, /5/, /6/).
   - "The use of geospatial data also has the potential to unfairly disadvantage or blight a geographic area or community." SV.
   - "there is always the possibility of an area or community being disadvantaged or 'redlined'." SV.
   - "The term ‘redlining’ was coined by the sociologist John McKnight in the 1960s". SV.
   - "The ecological fallacy arises from erroneously assuming that relationships observed for groups necessarily hold for individuals." SV.
   - "Area classifications (where areas are categorised in an attempt to capture the most common characteristics of their residents) is one topic where it is particularly easy to slip into assumptions." First part SV.
   - "Where there is any potential for discrimination, the purpose for any data access and use should be clearly stated." SV.
   - Disclosure: "An individual (X, Y) location can point at a single address or business. A small area can pinpoint a small enough number of cases to be disclosive." SV. Location "might have real implications for the personal safety of vulnerable people or groups". SV.
   - Balance: "potential risk should not necessarily be used as a rationale for avoiding local or small area data altogether". SV.
   - Presentation: "Red traditionally spells danger, while dark or dull colours can imply a negative association." SV. "Missing data is not the same as a zero value." SV. "Large areas, perhaps rural areas with relatively small populations, tend to dominate visually while physically small urban areas can get neglected." SV.
2. UKSA, "Considering Public Good in Research and Statistics: Ethics Guidance" (22 July 2021) — same site, /publication/considering-public-good-in-research-and-statistics-ethics-guidance/pages/2/ and /3/.
   - Public good concerns "What impact will your work have on people, communities, organisations, and companies?" SV. Under the legislation it "broadly includes" four heads, the first being "Providing an evidence base for public policy decision-making, public service delivery..." (SV); the reader attributed these to the Statistics and Registration Service Act 2007 and the Digital Economy Act 2017 research code (SP).
   - "Remember, harm can also include things like stigmatisation." SV. "Just because a project has risks associated with it, does not mean that it should not be done." SV. Consider "whether any remaining risks can be justified to achieve the intended benefits". SV.
3. Office for Statistics Regulation, Code of Practice for Statistics, Edition 3.0, published 3 November 2025 — https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/1/ (also /3/, /8/). The Code was re-issued; older citations to "Trustworthiness, Quality, Value" pillars and numbered principles need checking against it.
   - Glossary, "Serving the public good": "The principle that statistics should serve everyone, by enhancing knowledge about society and the economy, aiding understanding and shaping actions". SV.
   - "Everyone can apply or draw on the Code." SV. The Code Principles "can be used by anyone in any organisation who wants to ensure that the information they provide serves the public good." SV.
   - Ten principles (SP): Show integrity; Lead responsibly; Be transparent; Manage data responsibly; Prioritise quality; Be rigorous; Be open about quality; Be relevant; Be clear; Be accessible.
   - The word "harm" does not appear on the principles page. OSR's 2020 paper "The Public Good of Statistics: What we know so far" (9 December 2020) says the phrase "is not well understood" (SP) and also has no statement on harm.
4. MHCLG, "English indices of deprivation 2025: frequently asked questions" (statistics published 30 October 2025; FAQ updated 17 November 2025) — https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025/english-indices-of-deprivation-2025-frequently-asked-questions . An official place-ranking carrying its own anti-ecological-fallacy caveat.
   - "Within every area there will be individuals who are deprived and individuals who are not." SV. "The Index is not a suitable tool for targeting individuals." SV.
   - "This means that each can tell you if one area is more deprived than another but not by how much." SV.
   - The Indices are "designed to identify aspects of deprivation, not affluence". SV.
5. A place-data layer withheld because of harm: Redfin, "Neighborhood Crime Data Doesn’t Belong on Real Estate Sites" (Christian Taubman, 13 December 2021) — https://www.redfin.com/news/neighborhood-crime-data/ . Company statement.
   - "We recently decided not to add neighborhood crime data to Redfin.com." SP.
   - "...given the long history of redlining and racist housing covenants in the United States there's too great a risk of this inaccuracy reinforcing racial bias." Fragments SV.
   - "most crimes in the U.S. go unreported". SV.
   - This is a decision not to publish, not a withdrawal. I found no verified case of a withdrawn public map; the one I tried (Poynter on the Journal News) could not be read.
6. The 2018 accessibility regulations exclude "online maps and mapping services" from their content requirements (reg 4(2)(d), item 1), subject to essential information being accessible for navigational maps.
7. The Online Safety Act duties are being amended by the Crime and Policing Act 2026 during 2026 (item 2). Ofcom's duty pages were rewritten on 18 February 2026 around a "three months … after launching a service" clock.
8. The Equality Act hosting exception (Schedule 25 para 5, item 1) is a second, separate knowledge-and-removal rule alongside the Online Safety Act take-down duty. The Part 3 harassment prohibition excludes sexual orientation and religion or belief (s.29(8)).

==================================================
LEFT OUT, AND WHY
==================================================
- EHRC Statutory Code of Practice: 403 on both URLs.
- Mapping Inequality (Richmond): robots failure on both URLs.
- Datatilsynet's Grindr decision page: robots failure; the fine is sourced to the complainant NGO instead. The EDPB URL I tried returned only a news listing.
- Cortright "Walking the Walk"; Gillespie publisher page; Kosinski et al. PNAS; Wikipedia and Stack Overflow documentation; BBC, Guardian and Wired journalism; Strava's heat-map letter (dead link); a College of Policing crime-information trial (404): all unreachable or blocked.
- Robinson's conclusion and the bodies of both Wacquant papers: paywalled.
- Microsoft "Harms Modeling" and "Responsible Data" categories: skipped as the brief allowed. CDEI and Ada Lovelace taxonomies: replaced by Shelby et al. and the ICO taxonomy.
- Equality Act s.19A, Schedule 3 exceptions, s.29 Explanatory Notes examples: not read.
- OSA: Schedule 3 timing, s.11 children's risk assessment text, Schedule 1 Part 2, categorisation thresholds, and the Protection of Children Codes themselves (the statement URL I guessed 404'd).
- Agent B's and Agent C's territory (the Children's Code text, the DPIA process, the ESRC six principles) was left alone.

==================================================
RICH REFERENCES (3)
==================================================
1. UK Statistics Authority (2021), Ethical considerations in the use of geospatial data for research and statistics. Short, UK, official; it names redlining, the ecological fallacy, area "blight", disclosure by location and colour choice in one place.
2. Grimmelmann (2015), The Virtues of Moderation. Open full text; the verbs-and-adverbs grammar organises every contribution-gating choice.
3. Ofcom's "Illegal content duties under the Online Safety Act" page with the user-to-user Codes of Practice (24 February 2025). Together they state the tiers and the measures for every service in the regulator's words.

==================================================
WHAT SURPRISED ME
==================================================
- Neither the ICO's DPIA harm list nor its 2022 harms taxonomy names harm to a place or community by stigma. The UK statistical system's guidance does, in terms ("blight", "redlined", "stigmatisation").
- The published abstract of the leading redlining paper has no effect sizes; the 15–30 per cent and 40 per cent figures are in the working paper. The counter-paper's "at most 4 to 20 percent" is about bias in drawing the maps, a different quantity from the maps' effects. The two are easily mis-set against each other.
- Ofcom's two statements of "large service" do not match word for word ("7 million or more per month" on the web page; "more than 7 million monthly active United Kingdom users" in the Codes).
- The Online Safety Act has no size threshold at all; Ofcom's phrase is "services run by micro businesses". The limited-functionality exemption turns on whether user input "relat[es] to provider content".
- The ICO's 2014 crime-mapping advice already named estate agents and insurers as secondary users and said the publisher "may be powerless to prevent secondary uses".
- The ESRC framework pages contain no non-HEI sentence. The nearest is that the guidance "may be useful to other research-related audiences".
- The Grindr fine was still in the courts in October 2025, nearly six years after the January 2020 report.
- The fetch reader misdated Grimmelmann to 2005 on one pass and compressed several statutory sub-paragraphs into paraphrase on first pass (Equality Act Schedules 2 and 25; OSA s.10 and s.55). Every statutory quotation above marked SV was re-checked; those marked SP should be re-read before print.


---

