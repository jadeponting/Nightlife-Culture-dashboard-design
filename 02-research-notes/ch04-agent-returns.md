# Chapter 4 — research agent returns

*Kept whole, as returned, 6 October 2026. Four agents ran in parallel, one facet each, briefed per `AGENTS.md`. Nothing here has been edited; the orchestrator's spot-checks, the verification agent's findings and the cold read are recorded in `01-sources/RESEARCH-LOG.md` Entry 4. A claim in these returns is not a claim in the chapter until it has been read at source.*

---

## Agent A — Provenance, data quality and analytical assurance

# RESEARCH REPORT — Provenance, data quality and analytical assurance: what the official world requires a number to carry before it counts as evidence

All fetches dated 2026-10-06. Method note: the fetch tool used here can only return quotations in pieces of ≤125 characters; where a longer passage is quoted below it was obtained as consecutive pieces and is reassembled without alteration. Direct curl to osr.statisticsauthority.gov.uk and both web archives (UKGWA, Wayback) were blocked by the egress proxy, so the Code of Practice edition 2.x text is reached via official secondary pages (flagged). PubMed and Europe PMC were rate-limited/captcha'd; ScienceDirect and Wiley refused — the two "midnight census" papers are therefore SECONDARY/ABSTRACT-ONLY.

HEADLINE FINDINGS THE AUTHOR SHOULD KNOW FIRST
1. The UK Code of Practice for Statistics is now **edition 3.0, published 3 November 2025 (launch date 30 October 2025)**. It abolished the 14 "principles" (T1–T6, Q1–Q3, V1–V5) in favour of **10 Standards** plus separate "Standards for the Public Use of Statistics, Data and Wider Analysis". The old Q1/Q2/Q3 become Standard 6 "Be rigorous" and Standard 7 "Be open about quality"; T6 becomes Standard 4 "Manage data responsibly"; V3 becomes Standard 9 "Be clear". Edition 2.0 (2018) was revised as 2.1 (2022) before being replaced. Anything written citing "Q3.3" is now historical.
2. The **Aqua Book has been replaced**: "The AQuA Book" (new capitalisation) was published on GOV.UK on **30 July 2025** as HTML guidance, co-badged by GORS, the Analysis Function, GAD and ONS. It adds a fourth named role (Approver), an explicit definition of verification/validation, and new chapters on multi-use models, black-box/AI systems, third parties and publishing models.
3. Across every framework reached, the irreducible "provenance set" a figure must carry is: (a) **source** — what data, from whom, why chosen; (b) **method** — how it was made, by which standard/classification, with what deviations; (c) **reference period** — the time the figure *describes*, distinct from the time it was *published*; (d) **status/vintage** — provisional/final, the date of this version, what changed since the last; (e) **quality statement** — strengths, limitations, uncertainty, comparability over time/place/domain, what the figure can and cannot be used for; (f) **responsibility** — who produced, assured and approved it. PROV-DM gives this a formal grammar (Entity–Activity–Agent); DCAT/schema.org give field names; FAIR R1.2 makes "detailed provenance" a condition of reuse; the Code of Practice and Aqua Book make it a condition of counting as official evidence.

---

## 1. CODE OF PRACTICE FOR STATISTICS (UK Statistics Authority / OSR)

### 1a. Edition 3.0 (current)
**Citation:** UK Statistics Authority / Office for Statistics Regulation, *The Code of Practice for Statistics*, Edition 3.0, published 3 November 2025.
**URLs read:** https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/1/ ; …/pages/3/ ; …/pages/4/ ; …/pages/5/ ; …/pages/6/ ; …/pages/7/ ; transition guidance https://osr.statisticsauthority.gov.uk/guidance/transition-guidance-moving-to-the-code-of-practice-for-statistics-edition-3-0/ ; summary of changes https://code.statisticsauthority.gov.uk/code-of-practice-for-statistics-3-0-what-has-changed/summary-of-key-changes ; quick reference guide https://osr.statisticsauthority.gov.uk/wp-content/uploads/2025/11/Code_3_quick_reference_guide.pdf
**How read:** at source (official web edition).
**Exact quotations:**
- Edition/date: "Edition 3.0, published 3 November 2025." Transition guidance: "Heads of Profession are expected to begin applying the principles of Code 3.0 from the launch date – 30 October 2025."
- Statutory basis: section 10 of the Statistics and Registration Service Act 2007 requires the Authority to "publish and maintain a code of practice."
- Scope: "the Code is not just for official statistics. Everyone can apply or draw on the Code."
- The three pillars (page 3, "Understanding TQV"): Trustworthiness — "Building confidence in the people and organisations that produce statistics and data"; Quality — "Data and methods that produce assured statistics"; Value — "Statistics that support society's needs for information".
- Structure: ten Standards for Official Statistics — 1 Show integrity, 2 Lead responsibly, 3 Be transparent, 4 Manage data responsibly, 5 Prioritise quality, 6 Be rigorous, 7 Be open about quality, 8 Be relevant, 9 Be clear, 10 Be accessible.
- **Standard 6 — Be rigorous:** "Producers must use suitable data sources and sound methods, and assure the quality of the statistics across the production and release processes".
  - 6.1 "Produce statistics to a suitable level of quality that means they meet their intended uses and are not misleading"
  - 6.2 "Use the most suitable data for what needs to be measured. Monitor for changes in the data sources and potential bias in the data. Explain any issues and their implications for use of the data in producing statistics"
  - 6.3 "Check the suitability and availability of existing data from governmental and non-governmental sources before collecting new data. Ensure that opportunities for data sharing, data linkage, cross-analysis of sources, and the reuse of data are taken wherever feasible"
  - 6.4 "Maintain constructive relationships with those involved in the data provision, statistics preparation and quality assurance processes. Be clear about your data supply and quality requirements and understand how these will be met. Where possible, provide feedback to data suppliers on your use of their data"
  - 6.5 "Ensure the burden on those providing their information is proportionate to the anticipated benefits"
  - 6.6 "Use data that are coherent when aggregated, consistent over time and comparable across and within geographies at regional, national and local levels, where possible. Seek to design new statistics in ways that achieve UK comparability and improve consistency and coherence with related statistics"
  - 6.7 "Base methods on national or international good practice, scientific principles or professional consensus. Identify potential bias and address limitations. Use recognised standards, classifications and definitions. Explain reasons for deviations from these standards and any related implications for use"
  - 6.8 "Collaborate with experts, other analysts and statistics producers in the UK and internationally, where appropriate and share best practice"
  - 6.9 "Use a proportionate quality assurance approach across production and release processes. Validate statistics through comparison with other relevant statistics and data sources where possible"
  - 6.10 "Verify that the statistics are representative and of suitable quality and monitor relevant quality dimensions for both input data and the statistics, such as completeness and validity, accuracy and reliability, coherence and comparability, and timeliness. Quantify statistical error, including bias, and produce measures of confidence, where possible"
  - 6.11 "Regularly review strengths and limitations in the data and statistics, including the continued suitability of data sources and methods. Be open about your decisions and reasons for change"
- **Standard 7 — Be open about quality:** "Producers must prominently explain the quality of the statistics, including strengths and limitations, and communicate the uncertainty in estimates".
  - 7.1 "Prominently communicate the quality of the statistics and the strengths and limitations that impact their use, reflecting the needs of different types of users"
  - 7.2 "Report on the key quality dimensions such as accuracy and timeliness, and, where possible, give estimates of error and confidence for the statistics. Summarise how uncertainty in the estimates may impact use by using qualifying words, numbers or graphics"
  - 7.3 "Explain the nature of data sources and why they were selected, anticipating possible areas of misunderstanding or misuse. Prominently communicate limitations in the underlying data and explain their impact on the statistics"
  - 7.4 "Be clear about the methods used. Explain quality issues related to the methods, systems and processes, including the extent to which the statistics are representative and comparable across the UK and internationally. Describe potential bias and steps taken to address it"
  - 7.5 "Give advance notice to users of planned changes to methods and sources that will impact the statistics. Explain the nature and extent of the change, and provide a consistent back series where possible"
  - 7.6 "Clearly flag where statistics are being developed and tested. Be transparent about developments, outlining the plans and expected outcomes, as well as the opportunities for users to be involved in the evaluation of the statistics"
- **Standard 5 — Prioritise quality:** "Producers must support a quality culture that promotes good practice and encourages learning and improvement, under the direction of the Chief Statistician/Head of Profession for Statistics"; practice: "Publish your quality management approach and explain how it aligns with your organisation's commitment to data quality".
- **Standard 3 — Be transparent** (revisions on the face of the release): 3.9 "Release revisions and corrections of errors transparently and as soon as possible in line with the organisation's published policy, being clear about the nature and scale of change"; 3.10 "Ensure the status of the statistics is clear in the release – state whether they are accredited official statistics, official statistics or official statistics in development, and if the accreditation has been removed, draw users' attention to the loss of accreditation".
- **Standard 4 — Manage data responsibly** (successor to T6): "Producers must manage data and statistics safely and securely and be open about how data will be used and protected". 4.1 "Be ethical in how you collect, access, use and share data to serve the public good and be transparent about your approach in a published data management policy". 4.3 "Always consider the rights of data subjects and manage in ways that are consistent with data protection legislation…".
- **Standard 9 — Be clear** (successor to V3): "Producers must clearly present the statistics to support appropriate interpretation, collaborating with other producers and experts to develop fuller insight for key topics". 9.2 "Communicate the statistics in a way that helps users understand issues and support them to make appropriately informed decisions. Provide a clear description of the main messages with suitable data visualisations". 9.3 "Provide comparisons to support interpretation and signpost other relevant statistics, including within the UK and internationally. Explain the consistency and coherence with other related statistics and sources". 9.5 "Aid understanding by highlighting potential misinterpretations. Clarify the meaning of the statistics when they are used inappropriately". 9.7 "Give advance notice of material changes to the content of releases, such as the removal of data tables or variables, and any change in the frequency of release".
- **Standard 10 — Be accessible** (metadata/reproducibility): 10.2 "Make sure statistics, data and related guidance are easily accessible. Provide other relevant information, such as metadata and coding where appropriate"; 10.5 "Support the reuse of data and statistics, preventing barriers to use where possible. Ensure statistics are reproducible. Support data and statistics to be shared, accessed and linked, using common data standards with associated metadata".
- **Standards for Public Use** (pages 6–7, apply to any public body using numbers in public, including "management information, research and economic modelling"): "Be clear about where statistics, data and wider analysis used in public communications come from. For example, cite sources in publications and on social media."; "Do not use statistics, data or wider analysis in a misleading way. This includes not cherry-picking figures, taking figures out of context or placing undue certainty on them."; "Clearly communicate any key context and limitations associated with statistics, data and wider analysis to help the public understand and interpret them." Defined "intelligent transparency" as "an open, clear and accessible approach to the use of data, statistics and wider analysis in the public domain."
- Summary of key changes (2.1→3.0): "T3 Orderly release is very similar to std 3 Be transparent; additionally, a published revisions and corrections policy and release practice policy are required."; "New: std 5 Prioritise quality has some new practices emphasising quality culture and a supportive learning environment."; "T6 Data governance is very similar to std 4 Manage data responsibly – plus, a practice related to social acceptability was added; a data management approach is required."
**What it establishes:** The current UK regulatory standard requires, on the face of a release: data source and reason for selection; methods and deviations from standards; quality dimensions with error/confidence; uncertainty expressed in "qualifying words, numbers or graphics"; comparability across time and geography; advance notice of method change plus a consistent back series; status of the statistic; nature and scale of revisions; and explicit flagging of likely misinterpretations.
**Strength:** Very strong (primary, current, verbatim).
**Role:** LOAD-BEARING.

### 1b. Edition 2.0 (2018) / 2.1 (2022) — the Quality pillar as it was
**Citation:** UK Statistics Authority, *Code of Practice for Statistics*, Edition 2.0, February 2018 (revised 2.1, May 2022).
**URLs read:** Original PDF and web pages now redirect to the 3.0 site. Text obtained via official Analysis Function/GSS guidance that reproduces the principles and practices: https://analysisfunction.civilservice.gov.uk/policy-store/quality-statistics-in-government/ (published 2 October 2019) and https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/ (17 December 2018); OSR "Spotlight on Quality" https://osr.statisticsauthority.gov.uk/publications/spotlight-on-quality-framework-assuring-confidence-in-economic-statistics/pages/6/ (10 July 2024); comparison document https://uksa.statisticsauthority.gov.uk/wp-content/uploads/2018/02/Comparison-Code-2-to-Code-1.pdf.
**How read:** SECONDARY (official government pages quoting the Code verbatim). Archive copies were blocked.
**Exact quotations (as reproduced by GSS/OSR):**
- Q1 Suitable data sources: "Statistics should be based on the most appropriate data to meet intended uses. The impact of any data limitations for use should be assessed, minimised and explained."
- Q2 Sound methods: "Producers of statistics and data should use the best available methods and recognised standards, and be open about their decisions."
- Q3 Assured quality: "Producers of statistics and data should explain clearly how they assure themselves that statistics and data are accurate, reliable, coherent and timely."
- Q1.5: "The nature of data sources, and how and why they were selected, should be explained."
- Q2.4: "Relevant limitations arising from the methods and their application, including bias and uncertainty, should be identified and explained."
- Q3.1: "The strengths and limitations of the statistics and data should be considered in relation to different uses, and clearly explained." (OSR Spotlight gives the fuller form: "Statistics are produced to a level of quality that meets users' needs. The strengths and limitations of the statistics and data are evaluated in relation to different uses.")
- Q3.3: "The extent and nature of any uncertainty in the estimates should be clearly explained."
- Q3.4: "Revisions should be explained alongside the statistics, being clear about scale, nature, cause and impact."
- Comparison doc: "Code 1.0 practices have otherwise been incorporated and extended into 14 principles" listing "Q1 Suitable data sources; Q2 Sound methods; Q3 Assured quality".
- T6 practices as characterised by OSR regulatory guidance (16 Oct 2018, https://osr.statisticsauthority.gov.uk/guidance/regulatory-guidance-building-confidence-in-the-handling-and-use-of-data/pages/2): T6.1 "emphasising the importance of producer organisations transparently committing to achieving the legal requirements that underpin data collection, handling and release"; T6.4 "addresses the need for the safe release of data and statistics, ensuring that the personal data are appropriately protected, for example by using statistical disclosure control techniques." (These are OSR's paraphrases of T6, not the practice text itself.)
- NOT OBTAINED verbatim: the T6 and V3 principle statements and V3.x practices of edition 2.x. Their 3.0 successors (Standards 4 and 9) are quoted in full above.
**Strength:** Moderate (verbatim but via secondary official pages; T6/V3 incomplete).
**Role:** SUPPORTING (historical context; most published commentary cites these codes).

### 1c. Voluntary application
**Citation:** OSR, *TQV Voluntary Application: Showing Trustworthiness, Quality and Value when working with data and statistics*, published 15 October 2025; and OSR "Voluntary Application of the Code" page.
**URLs read:** https://osr.statisticsauthority.gov.uk/guidance/tqv-voluntary-application-showing-trustworthiness-quality-and-value-when-working-with-data-and-statistics/ ; https://osr.statisticsauthority.gov.uk/the-code-of-practice-for-statistics/voluntary-application/
**How read:** at source.
**Exact quotations:**
- "a voluntary application (VA) scheme for any organisation that wants to promote public confidence in their statistics"
- For "any producer of data, statistics and analysis that are not official statistics"
- "Trustworthiness, Quality and Value benefit anyone producing data, statistics and analysis, whether they are inside or outside government."
- "Producers of data, statistics or analysis that are not official statistics and who apply the Code principles are encouraged to be part of the TQV voluntary application (VA) scheme."
- Steps: the organisation must "publish a TQV statement" explaining its approach to "each of the ten Code principles"; "OSR will add you to the online Register of TQV Voluntary Application when your TQV statement is published"; organisations "compare your processes, methods and outputs against the recognised standards in the Code".
- OSR's role: "We do not have a formal role in regulating the voluntary application of the TQV principles but we are responsible for managing the scheme." If concerns arise OSR will "contact the organisation involved and review its TQV statement and procedures. Any intervention will be made on an informal and advisory basis."
**What it establishes:** A non-public body (charity, company, local partnership) can adopt the Code by publishing a self-assessed TQV statement against the ten principles and being listed on a register; there is no OSR audit or badge, only informal review on complaint. The new "Standards for Public Use" apply to public bodies regardless.
**Strength:** Strong.
**Role:** LOAD-BEARING for any dashboard whose owner is not an official-statistics producer.

---

## 2. OSR QUALITY GUIDANCE
**Citation:** Office for Statistics Regulation, *Quality and statistics: an OSR perspective*, published 16 February 2023.
**URLs read:** https://osr.statisticsauthority.gov.uk/publications/quality-and-statistics-an-osr-perspective/ and …/pages/2/
**How read:** at source.
**Exact quotations:**
- Definition of quality: "statistics fit their intended uses, are based on appropriate data and methods, and are not materially misleading."
- "Publishing data and statistics that materially mislead is unacceptable. If the statistics do not bear the weight of the decisions made using them, producers should immediately review whether they should continue to publish them"
- On what users want: "Users would like prominent, succinct quality information, which helps them decide whether the statistics are suitable for their own use"
- On limitations: "producers should provide a proportionate explanation of the limitations and uncertainty in the statistics, helping users understand the nature and implications of potential sources of bias"
- "giving straightforward information about uncertainty, and being open when things go wrong, builds confidence in you as a trustworthy organisation"
- "Being clear about your confidence in the quality and value of the statistics and how you have come to your choice can provide reassurance."
- Dimensions named: "relevance, accuracy and reliability, timeliness and punctuality, coherence and comparability, and accessibility and clarity"
- "Quality is not independent of Trustworthiness and Value"
- Recommends a quality culture "emphasising learning from errors without blame" and an "emerging quality grade tool for succinct user statements".
**What it establishes:** The regulator's test is whether a number can "bear the weight of the decisions made using" it; quality information must be prominent and succinct enough for a user to judge fitness for *their* purpose.
**Strength:** Strong.
**Role:** LOAD-BEARING (the "bear the weight" test is quotable).

Related: GSS *Quality statistics in government* (2 Oct 2019, URL above) defines statistical quality as "the quality of our statistics in terms of their fitness for purpose" and reproduces the ESS dimensions in UK wording: Relevance "the degree to which statistics meet the current and potential needs of users"; Accuracy "the closeness between an estimated result and the (unknown) true value"; Reliability "the closeness of early estimates to subsequent estimated values"; Timeliness "the time gap between the publication date and the reference period"; Punctuality "the time lag between the actual and planned dates of publication"; Comparability "the degree to which statistics can be compared over time, region or another domain"; Coherence "the degree to which statistical processes use the same concepts and harmonised methods"; Accessibility "the ease with which users can access the statistics and data"; Clarity "the quality and sufficiency of the commentary, illustrations, accompanying advice and technical details." — SUPPORTING; strong.

---

## 3. EUROPEAN STATISTICS CODE OF PRACTICE / ESS QUALITY FRAMEWORK
**Citation (a):** European Statistical System Committee, *European Statistics Code of Practice*, revised edition 2017, "Adopted by the European Statistical System Committee 16th November 2017".
**URL read:** https://ec.europa.eu/eurostat/documents/4031688/8971242/KS-02-18-142-EN-N.pdf/e7f85f07-91db-4312-8118-f729c75878c7 — at source.
**Exact quotations:**
- Principle 11 Relevance: "European Statistics meet the needs of users."
- Principle 12 Accuracy and Reliability: "European Statistics accurately and reliably portray reality." Indicator 12.3: "Revisions are regularly analysed in order to improve source data, statistical processes and outputs."
- Principle 13 Timeliness and Punctuality: "European Statistics are released in a timely and punctual manner."
- Principle 14 Coherence and Comparability: "European Statistics are consistent internally, over time and comparable between regions and countries". 14.1 "Statistics are internally coherent and consistent (i.e. arithmetic and accounting identities observed)."; 14.2 "Statistics are comparable over a reasonable period of time."; 14.3 "Statistics are compiled on the basis of common standards with respect to scope, definitions, units and classifications"; 14.4 "Statistics from the different data sources and of different periodicity are compared and reconciled."; 14.5 "Cross-national comparability of the data is ensured within the European Statistical System through periodical exchanges".
- Principle 15 Accessibility and Clarity: "European Statistics are presented in a clear and understandable form, released in a suitable and convenient manner". 15.1 "Statistics and the corresponding metadata are presented, and archived, in a form that facilitates proper interpretation"; 15.5 "Metadata related to outputs are managed and disseminated by the statistical authority according to the European standards."; 15.6 "Users are kept informed about the methodology of statistical processes including the use and integration of administrative data"; 15.7 "Users are kept informed about the quality of statistical outputs with respect to the quality criteria for European Statistics."

**Citation (b) — the legal definitions:** Regulation (EC) No 223/2009 on European statistics, Article 12 "Statistical quality" (consolidated text).
**URL read:** https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02009R0223-20150608 — at source.
**Exact quotations:**
- "'relevance', which refers to the degree to which statistics meet current and potential needs of the users"
- "'accuracy', which refers to the closeness of estimates to the unknown true values"
- "'timeliness', which refers to the period between the availability of the information and the event or phenomenon it describes"
- "'punctuality', which refers to the delay between the date of the release of the data and the target date"
- "'accessibility' and 'clarity', which refer to the conditions and modalities by which users can obtain, use and interpret data"
- "'comparability', which refers to the measurement of the impact of differences in applied statistical concepts, measurement tools and procedures where statistics are compared between geographical areas, sectoral domains or over time"
- "'coherence', which refers to the adequacy of the data to be reliably combined in different ways and for various uses"

**Citation (c):** Eurostat, *ESS handbook for quality and metadata reports*, 2020 edition ("Manuscript completed: February 2020"). URL: https://ec.europa.eu/eurostat/documents/3859598/10501168/KS-GQ-19-006-EN-N.pdf — at source. Confirms the Article 12 definitions are the operative ones; notes reliability is treated under "S.17 Data revision" rather than accuracy, i.e. *reliability is measured by revisions*. The ESS QAF v1.2 PDF (https://ec.europa.eu/eurostat/documents/64157/4392716/ESS-QAF-V1-2final.pdf) was located but not fetched; v2.0 (2019) exists per UNSD slides.
**What it establishes:** The canonical five-part quality vocabulary and, crucially, that comparability is defined *across three axes* — geography, domain, time — and that "timeliness" is the distance between the reference period and availability, which presupposes a declared reference period.
**Strength:** Very strong (law + standard).
**Role:** LOAD-BEARING.

---

## 4. UK GOVERNMENT DATA QUALITY FRAMEWORK (2020)
**Citation:** Government Data Quality Hub (ONS), *The Government Data Quality Framework*, "Published 3 December 2020".
**URL read:** https://www.gov.uk/government/publications/the-government-data-quality-framework/the-government-data-quality-framework — at source.
**Exact quotations:**
- "Data quality can be thought of as 'fitness for purpose' – is this data set good enough for what I want to use it for?"
- Five principles: "Commit to data quality"; "Know your users and their needs" ("Understanding user needs is essential to ensuring that data is fit for purpose"); "Assess quality throughout the data lifecycle" ("Data should be managed across its lifecycle, paying close attention to quality measures at each stage"); "Communicate data quality clearly and effectively" ("Communicate quality to users regularly and clearly to ensure data is used appropriately"); "Anticipate changes affecting data quality" ("Anticipate and prevent future data quality issues through good communication and effective change management").
- "Data quality dimensions are 'measurable features or characteristics of data'." "There are six core data quality dimensions, as defined by DAMA UK (Data Management Association of the UK)."
- Completeness: "Completeness describes the degree to which records are present." "For a data set to be complete, all records are included, and the most important data is present in those records."
- Uniqueness: "Uniqueness describes the degree to which there is no duplication in records." "This means that the data contains only one record for each entity it represents, and each value is stored once."
- Consistency: "Consistency describes the degree to which values in a data set do not contradict other values representing the same entity." "Data is consistent if it doesn't contradict data in another data set."
- Timeliness: "Timeliness describes the degree to which the data is an accurate reflection of the period that they represent, and that the data and its values are up to date." "Data is timely if the time lag between collection and availability is appropriate for the intended use."
- Validity: "Validity describes the degree to which the data is in the range and format expected." "Valid data is stored in a data set in the appropriate format for that type of data."
- Accuracy: "Accuracy describes the degree to which data matches reality." "In a data set, individual records can be measured for accuracy, or the whole data set can be measured."
- Communicating: "Provide clear data quality information and describe its impact on use of the data."; "Communicate trade-offs in data quality clearly to aid understanding of the data's strengths and weaknesses."; "Be transparent about the quality assurance approach taken and communicate data quality issues clearly to users."
**What it establishes:** The six-dimension vocabulary for *datasets* (as opposed to the ESS vocabulary for *statistics*); note "Timeliness" here is defined relative to "the period that they represent" — again the reference period is built into the definition. Note there are FIVE principles, not four: "Commit to data quality" is first.
**Strength:** Very strong.
**Role:** LOAD-BEARING.

---

## 5. THE AQUA BOOK (2015 and 2025) AND THE MACPHERSON REVIEW (2013)

### 5a. Status check — the Aqua Book HAS been updated
**Citation:** Government Analysis Function / GORS / GAD / ONS, *The AQuA Book*, GOV.UK guidance, "Published: 30 July 2025" (page metadata shows later minor updates, latest 2026-07-20).
**URLs read:** https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government (landing, now points to the new edition); https://www.gov.uk/guidance/the-aqua-book (full text) — at source.
**Exact quotations:**
- "The last version of the AQuA Book was published in 2015, following Sir Nicholas Macpherson's Review of quality assurance of government models."
- Described as "a vital supporting guide for the Analysis Function Standard"; new material covers multi-use models, "assuring black box systems and AI", development/maintenance/continuous review, third parties, "publishing models".
- Quality analysis is "fit for the purpose it was commissioned to meet. It should be: accurate, appropriately assured, evidenced, proportionate to its effect, adequately communicated, documented, accepted by its commissioners"
- Verification: "Verification ensures the analysis meets it specified design requirements." Also: "tests the behaviour of the system, model or code to find errors that arise during execution"; "Verification that the implemented methodology meets the design requirements".
- Validation: "Validation ensures the analysis meets the needs of its intended users and the intended use environment." Also: "testing whether the product meets the requirements of users"; "Validation of models includes testing the validity of the conceptual model".
- Proportionality: "Assurance should be proportionate to the potential effect it will have and the size and complexity of the analysis. The level of assurance should be guided by a structured assessment of the business risks."; assurance "applied proportionately to the risk and value of the activity"; "the exact nature of any scrutiny made by the approver should be proportionate to the effect the analysis is likely to have".
- Roles (four): Commissioner — "Requests the analysis and sets out their requirements; agrees that what the analyst is going to do will satisfy the need; accepts the analysis and assurance as fit for purpose". Analyst — "Designs the approach, including the assurance, to meet the commissioner's requirements; agrees the approach with the commissioner; carries out the analysis; carries out their own assurance". Assurer — "may be known as the analytical assurer or assuring analyst"; "Reviews the assurance completed by the analyst; carries out any further validation and verification they may see as appropriate; reports errors and areas for improvement to the analyst"; "must be independent from the analysts". Approver — "may be known as senior analyst or senior responsible officer"; "Scrutinises the work of the analyst and assurer; confirms (if necessary) to the analyst, assurer and commissioner that the work has been appropriately assured".
- Assumptions log: "Register of assumptions…that have been risk assessed and signed off by an appropriate governance group or stakeholder. Assumption logs should: describe each assumption; quantify its effect and reliability"; more generally "logs of data, assumptions and decisions including their source, ownership, reliability".
- Documentation/provenance: analysts should "fully document any code" and "log the data, assumptions and inputs used in the analysis"; keep a "record of the analysis including methods used, dependencies, process maps, change and version control logs".
- Communication: outputs should include "advice on uncertainty and its affect on the outputs of the analysis" and "a description of the limits of the analysis and what it can and cannot be used for".
- Business critical: models that "influence significant financial and funding decisions, are necessary to the achievement of a departmental business plan" or "where an error could lead to serious financial, legal or reputational damage".
- Black box: "Black box models' internal workings are not visible, easily understood, or succinctly explained…Artificial Intelligence models (including Machine Learning) can often be considered a type of black box model."
**Strength:** Very strong.
**Role:** LOAD-BEARING (current edition).

### 5b. The Aqua Book 2015 (original)
**Citation:** HM Treasury, *The Aqua Book: guidance on producing quality analysis for government*, "March 2015".
**URL read:** https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/416478/aqua_book_final_web.pdf — at source (the alternative /media/ URL now redirects to the 2025 edition).
**Exact quotations:**
- "The InterCity West Coast franchise competition of 2012 illustrated both the importance of analysis and modelling in delivering a major government project and the consequences when things go wrong"
- Four principles: "Proportionality of response: The extent of the analytical quality assurance effort should be proportionate in response to the risks associated with the intended use"; "Assurance throughout development: Quality assurance considerations should be taken into account throughout the life cycle of the analysis"; "Verification and validation: Analytical quality assurance is more than checking that the analysis is error-free and satisfies its specification (verification). It must also include checks that the analysis is appropriate"; "Analysis with RIGOUR: Quality analysis needs to be repeatable, independent, grounded in reality, objective, have understood and managed uncertainty, and the results should address the initial question robustly" (RIGOUR = Repeatable, Independent, Grounded in reality, Objective, Uncertainty-managed, Robust).
- Para 6.3: "verification activities ask whether the analysis has been conducted correctly; validation activities ask whether the correct analysis has been performed"
- Assumptions log: "A register of assumptions whether provided by the commissioner or derived by the analysis and data that have been risked assessed and signed-off"; 8.7 "It may be useful to maintain an assumptions and data log for this purpose."
- Para 2.29 on fit for purpose: "ensure that: the analysis undertaken aligns with its intended purpose and is relevant to the original problem; the correct analysis has been performed; the analysis has been conducted correctly and it is accurate…"
- Roles: 2.13 "The commissioner must ensure that the analyst understands the context of the question being asked."; 2.14 "The analytical assurer must ensure they receive evidence of appropriate analytical quality assurance activity."; 2.22 "In addition to conducting the analysis, the analyst should also provide proportionate documentation that outlines the verification and validation activities." (The fetch tool did not surface a distinct "Approver" role statement in the 2015 text, though it is commonly described as present; the 2025 edition unambiguously names four roles.)
- Uncertainty: 8.43 "The principal output of uncertainty analysis is information on the range of alternative outcomes and their likelihoods. It is important to communicate this in ways that are accessible to commissioners and decision-makers."; 8.44 "A tiered approach to communication may be helpful; a concise headline conclusion in narrative form, accompanied by one or more levels of more detailed information."; 8.46 "It is important to provide an overall characterisation of the uncertainty, combining any that have been quantified by modelling with the contribution of any additional uncertainties."
**Strength:** Very strong.
**Role:** LOAD-BEARING for the verification/validation distinction (the 2015 one-liner is the best formulation).

### 5c. Macpherson Review
**Citation:** HM Treasury, *Review of quality assurance of Government analytical models: final report*, Sir Nicholas Macpherson, "March 2013"; interim report December 2012.
**URLs read:** https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/206946/review_of_qa_of_govt_analytical_models_final_report_040313.pdf ; interim https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/206947/psr_governance_risk_review_of_qa_of_govt_analytical_models_interim_report_191212.pdf — at source.
**Exact quotations:**
- Trigger: "The recent experience with the Intercity West Coast franchise competition underlines the importance of good quality assurance." Interim: "In light of the experience on the InterCity West Coast franchise competition, and given the Civil Service's commitment to better policy making, the Cabinet Secretary and the Head of the Civil Service have commissioned a review…"
- Definition of QA (interim): "those processes and systems which are applied to ensure the model's outputs meet its quality requirements, manage risk of errors and ensure the model is fit for purpose"
- Business-critical test: "the extent to which the model drives key financial and funding decisions, the extent to which it was essential to the achievement of their business plan, and the extent to which error could lead to serious financial, legal or reputational damage."
- Scale: "Just fewer than 500 business critical models"
- Recommendations: "All business critical models in government should have appropriate quality assurance of their inputs, methodology and outputs in the context of the risks their use represents."; "There should be a single Senior Responsible Owner for each model through its lifecycle."; the Model SRO must confirm "the model is fit-for-purpose" and that "the use of the model outputs is appropriate."; "QA needs to be proportionate, and the resources employed should represent value for money."; "Each business critical model should have clear documentation" including "the model's scope and specification" and "the quality assurance undertaken."; Accounting Officers "may wish to confirm that there is an up-to-date list of business critical models and that this is publicly available."
- Governance (interim): "This should make clear who is accountable for the model's use and how compliance with agreed processes is monitored."
**Strength:** Very strong.
**Role:** LOAD-BEARING (origin story + "single SRO" + "inputs, methodology and outputs" triad).

### 5d. What actually went wrong (NAO)
**Citation:** National Audit Office, *Lessons from cancelling the InterCity West Coast franchise competition*, "Date: 7 Dec 2012".
**URL read:** https://www.nao.org.uk/reports/lessons-from-cancelling-the-intercity-west-coast-franchise-competition/ — at source.
**Exact quotations:** "significant errors in the tool the Department used to calculate how big a loan it would require bidders to have"; "The model had been designed to inform internal discussions and received no extra quality assurance once the Department decided to use it to calculate the loan, a key commercial decision"; "The objectives of the Department for Transport were insufficiently clear during the franchise competition"; costs: "at least £1.9 million in staff and adviser costs, £2.7 million in legal costs and £4.3 million on external advisers for the reviews", full cost "unknown but likely to be significant".
**What it establishes:** The paradigm failure was a *purpose drift*: an internal model re-used for a decision it was never assured for — exactly the "fit for purpose" / validation point.
**Strength:** Strong. **Role:** COLOUR (but the best single anecdote on why provenance includes *intended use*).

---

## 6. ANALYSIS FUNCTION / GSS, "COMMUNICATING QUALITY, UNCERTAINTY AND CHANGE"
**Citation:** Government Statistical Service, *Communicating quality, uncertainty and change*, "Publication date: 17 December 2018" (page notes it is under review).
**URL read:** https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/ — at source.
**Exact quotations:**
- Purpose: "Provide practical advice on how to communicate quality, uncertainty and change for different types of statistics and for a range of audiences."
- Sources of uncertainty: "Tell people, in plain English, about the sources of data and any associated uncertainty, including any sampling and non-sampling variations, definitions, processes and systems used by data suppliers and model assumptions or errors."
- What users may conclude: "Explain what you can and what you cannot conclude from the findings" and "pre-empt any misunderstanding and overinterpretation."
- Strengths/limitations: "The strengths and limitations of the statistics and data should be considered in relation to different uses, and clearly explained alongside the statistics."
- Revisions: "Notify users as soon as is practicable about errors and revisions", being "clear about the scale, nature, cause and impact."
- Change/comparability: "Describe any changes in quality made since the previous release and how this impacts on the accuracy of the statistics."; describe "direction of change, its absolute size and its relative size over time".
- Plain-English rules: use "estimates" throughout to signal uncertainty; "Where possible, quantify the impact of uncertainty on the statistics precisely" and if not, make reasoned judgements about likely size and direction; phrases like "care must be taken" are vague unless backed by "practical advice"; include "high-level information on any adjustments made to the data".
- Definitions used: quality = "fitness for purpose" measured against the ESS QAF; "change" = the difference in measures of the same phenomenon between two distinct time points.
- Revisions section (as summarised by the fetch): scheduled revisions = planned amendments incorporating additional data unavailable at initial publication; unscheduled corrections = amendments following identification of errors; "provisional" phrasing emphasises figures are subject to change; a revisions policy "documents which statistics are subject to revisions, timings, reasons, and management approach."
**Strength:** Strong (exact for the first group; the revisions definitions are the tool's close paraphrase — treat as SUPPORTING unless re-verified).
**Role:** LOAD-BEARING for the checklist of what must accompany a figure.

---

## 7. MACHINE PROVENANCE STANDARDS

### 7a. W3C PROV-DM
**Citation:** W3C, *PROV-DM: The PROV Data Model*, "W3C (World Wide Web Consortium) Recommendation 30 April 2013".
**URL read:** https://www.w3.org/TR/prov-dm/ — at source.
**Exact quotations:**
- Provenance: "A record that describes the people, institutions, entities, and activities involved in producing, influencing, or delivering a piece of data or a thing."
- Core: "At its core, provenance describes the use and production of entities by activities, which may be influenced in various ways by agents."
- Entity: "A physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary."
- Activity: "Something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities."
- Agent: "Something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity."
- Generation (wasGeneratedBy): "The completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation."
- Usage (used): "The beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity."
- Derivation (wasDerivedFrom): "A transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity."
- Attribution (wasAttributedTo): "The ascribing of an entity to an agent."
- Association (wasAssociatedWith): "An assignment of responsibility to an agent for an activity, indicating that the agent had a role in the activity."
- Delegation (actedOnBehalfOf): "The assignment of authority and responsibility to an agent to carry out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some responsibility."
**Strength:** Very strong. **Role:** LOAD-BEARING (gives the book a three-noun grammar: thing, process, responsible party).

### 7b. DCAT 3
**Citation:** W3C, *Data Catalog Vocabulary (DCAT) – Version 3*, "W3C Recommendation" "22 August 2024".
**URL read:** https://www.w3.org/TR/vocab-dcat-3/ — at source.
**Exact quotations:**
- dcat:Catalog "A curated collection of metadata about resources."; dcat:Dataset "A collection of data, published or curated by a single agent, and available for access or download in one or more serializations or formats."; dcat:Distribution "An accessible form of a dataset such as a downloadable file."; dcat:DataService "A collection of operations accessible through an interface (API) that provide access to one or more datasets or data processing functions."
- dcat:DatasetSeries: "a dataset representing a collection of datasets published separately but sharing characteristics."
- Properties: dct:issued "Date of formal issuance (e.g., publication) of the resource." ("This property SHOULD be set using the first known date of issuance."); dct:modified "Most recent date on which the resource was changed, updated or modified." ("The value indicates a change to the actual resource, not the catalog record. An absent value may indicate continuous updates."); dct:accrualPeriodicity "The frequency at which the resource is updated."; dct:temporal "The temporal period that the resource applies to or covers." ("Values SHOULD use dcterms:PeriodOfTime"; "defining a dcterms:PeriodOfTime as a closed interval"); dcat:version "A version number or other designation of the resource."; prov:wasGeneratedBy "An activity that generated, produced, or created the resource." ("A resource describing the activity, such as a PROV Activity, that generated the cataloged resource can be linked using this property."); prov:qualifiedAttribution — "The PROV qualified-attribution pattern is recommended to provide more detailed information about the relationship between a resource and an agent."
- Versioning: "Addition of properties for supporting versioning, e.g., dcat:version, dcat:previousVersion, dcat:hasCurrentVersion."
**Strength:** Very strong. **Role:** SUPPORTING (field names; note the explicit separation of *issued*, *modified* and *temporal coverage* — three different dates).

### 7c. FAIR principles
**Citation:** Wilkinson, M.D. et al., "The FAIR Guiding Principles for scientific data management and stewardship", *Scientific Data* 3, 160018, "Published: 15 March 2016", DOI 10.1038/sdata.2016.18; principle text as maintained by GO FAIR.
**URLs read:** https://www.nature.com/articles/sdata201618 ; https://www.go-fair.org/fair-principles/ — at source.
**Exact quotations:**
- Paper: "Distinct from peer initiatives that focus on the human scholar, the FAIR Principles put specific emphasis on enhancing the ability of machines to automatically find and use the data"; machines must "keep an exquisite record of provenance such that the data they are collecting can be accurately and adequately cited".
- Headlines (GO FAIR): Findable — "Metadata and data should be easy to find for both humans and computers."; Accessible — "Once the user finds the required data, she/he/they need to know how they can be accessed, possibly including authentication and authorisation."; Interoperable — "The data usually need to be integrated with other data. In addition, the data need to interoperate with applications or workflows."; Reusable — "The ultimate goal of FAIR is to optimise the reuse of data. To achieve this, metadata and data should be well-described."
- All 15: F1 "(Meta)data are assigned a globally unique and persistent identifier"; F2 "Data are described with rich metadata"; F3 "Metadata clearly and explicitly include the identifier of the data they describe"; F4 "(Meta)data are registered or indexed in a searchable resource"; A1 "(Meta)data are retrievable by their identifier using a standardised communications protocol"; A1.1 "The protocol is open, free, and universally implementable"; A1.2 "The protocol allows for an authentication and authorisation procedure, where necessary"; A2 "Metadata are accessible, even when the data are no longer available"; I1 "(Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation"; I2 "(Meta)data use vocabularies that follow FAIR principles"; I3 "(Meta)data include qualified references to other (meta)data"; R1 "(Meta)data are richly described with a plurality of accurate and relevant attributes"; R1.1 "(Meta)data are released with a clear and accessible data usage license"; **R1.2 "(Meta)data are associated with detailed provenance"**; R1.3 "(Meta)data meet domain-relevant community standards".
**Strength:** Very strong. **Role:** LOAD-BEARING for R1.2 and A2 ("metadata are accessible, even when the data are no longer available" — a provenance record should outlive the number).

### 7d. schema.org Dataset
**URL read:** https://schema.org/Dataset — at source. Dataset: "A body of structured information describing some topic(s) of interest." distribution "A downloadable form of this dataset, at a specific location, in a specific format."; measurementTechnique "A technique, method or technology used in an Observation, StatisticalVariable or Dataset."; variableMeasured "The variables that are measured in some dataset…"; temporalCoverage "The period that the content applies to, i.e. that it describes, either as a DateTime or textual string in ISO 8601 format."; datePublished "Date of first publication or broadcast…"; dateModified "The date on which the CreativeWork was most recently modified…"; version "The version of the CreativeWork embodied by a specified resource."; isBasedOn "A resource from which this work is derived or from which it is a modification or adaptation."; license; creator; publisher; citation. **Role:** COLOUR.

### Synthesis: the minimal "provenance set" across these standards
Common to PROV, DCAT, FAIR, schema.org and the Code: (1) a persistent identifier for the thing; (2) the agent responsible (publisher/creator/attribution); (3) the activity/method that generated it (wasGeneratedBy / measurementTechnique / "methods used"); (4) what it was derived from (wasDerivedFrom / isBasedOn / "data sources and why selected"); (5) the period it describes (temporal coverage / reference period) separately from (6) when it was issued and (7) when last modified / its version; (8) the licence/terms of use; (9) a quality/limitations statement (FAIR R1 "plurality of accurate and relevant attributes"; Code Std 7). The Code adds (10) status (official / in development / provisional) and (11) a revisions record.

---

## 8. THE DATA-QUALITY LITERATURE

### 8a. Wang & Strong 1996
**Citation:** Wang, R.Y. & Strong, D.M., "Beyond Accuracy: What Data Quality Means to Data Consumers", *Journal of Management Information Systems*, Spring 1996, Vol. 12, No. 4, pp. 5–33 (author copy gives "Journal of Management Information Systems; Armonk; Spring 1996; Volume 12, Issue 4, pages 5").
**URL read:** https://web.mit.edu/tdqm/www/tdqmpub/beyondaccuracy_files/beyondaccuracy.html — at source (MIT TDQM author copy, full text). Publisher page (Taylor & Francis) returned 403.
**Exact quotations:**
- "Poor data quality (DQ) can have substantial social and economic impacts…A framework is developed that captures the aspects of data quality that are important to data consumers."
- "We define 'data quality' as data that are fit for use by data consumers." Reference [22]: "Juran, J.M. Juran on Leadership for Quality: An Executive Handbook. New York: The Free Press, 1989."
- Method: "This process resulted in 179 attributes…Of the 1,500 surveys mailed…355 viable surveys…were returned…An exploratory factor analysis…produced twenty dimensions…which in turn are grouped into four categories."
- Four categories and dimensions: Intrinsic DQ — accuracy, objectivity, believability, reputation; Contextual DQ — value-added, relevancy, timeliness, completeness, appropriate amount of data; Representational DQ — interpretability, ease of understanding, representational consistency, concise representation; Accessibility DQ — accessibility, access security.
- "Data consumers have a much broader data quality conceptualization than IS professionals realize…Intrinsic DQ denotes that data have quality in their own right."
**Strength:** Very strong. **Role:** LOAD-BEARING (origin of the "more than accuracy" argument; believability and reputation are *intrinsic* dimensions — i.e. provenance affects perceived quality even where the value is correct).

### 8b. Pipino, Lee & Wang 2002
**Citation:** Pipino, L.L., Lee, Y.W. & Wang, R.Y., "Data Quality Assessment", *Communications of the ACM*, April 2002, Vol. 45, No. 4, pp. 211–218.
**URL read:** https://web.mit.edu/tdqm/www/tdqmpub/PipinoLeeWangCACMApr02.pdf — at source.
**Exact quotations:** "Studies have confirmed data quality is a multi-dimensional concept."; "Companies must deal with both the subjective perceptions of the individuals involved with the data, and the objective measurements based on the data set in question."; "Three pervasive functional forms are simple ratio, min or max operation, and weighted average." Dimensions named in text include free-of-error, completeness, consistency, concise representation, relevancy, ease of manipulation, believability, appropriate amount of data, timeliness, accessibility (Table 1 lists 16; not fully extracted).
**Strength:** Strong. **Role:** SUPPORTING (subjective vs objective assessment; metrics as ratios).

### 8c. Batini et al. 2009
**Citation:** "Batini, C., Cappiello, C., Francalanci, C., and Maurino, A. 2009. Methodologies for data quality assessment and improvement. ACM Comput. Surv. 41, 3, Article 16 (July 2009), 52 pages."
**URL read:** https://dimacs-algorithmic-mdm.wdfiles.com/local--files/start/Methodologies%20for%20Data%20Quality%20Assessment%20and%20Improvement.pdf — institutional mirror (ACM DL returned 403).
**Exact quotations:** Abstract: "The literature provides a wide range of techniques to assess and improve the quality of data. Due to the diversity and complexity of these techniques, research has recently focused on defining methodologies that help the selection, customization, and application of data quality assessment and improvement techniques."; syntactic accuracy "the closeness of a value, v, to the elements of the corresponding definition domain, D."; "Completeness is defined as the degree to which a given data collection includes data describing the corresponding set of real-world objects."; "The consistency dimension refers to the violation of semantic rules defined over a set of data items."; "Currency is the degree to which a datum is up-to-date…"; "Volatility is a measure of information instability, the frequency of change of the value for an entity attribute."; "Timeliness is the extent to which data are sufficiently up-to-date for a task."; "Methodologies that address both the process modeling and measurement of quality steps, are based on the fitness for use approach."
**Strength:** Strong. **Role:** SUPPORTING (the currency/volatility/timeliness triad is useful for dashboards: a number's age matters relative to how fast the thing changes).

### 8d. Juran's "fitness for use"
Not fetched at source (book). Wang & Strong cite Juran 1989 for the phrase; Chandrupatla, *Quality and Reliability in Engineering* (Cambridge UP) excerpt (https://assets.cambridge.org/97805215/15221/excerpt/9780521515221_excerpt.pdf) states "Quality is fitness for use." "comes from Juran" without a dated citation. The phrase is conventionally traced to Juran's *Quality Control Handbook* (1st ed. 1951) — NOT VERIFIED here. **Role:** COLOUR; mark as attribution-by-convention.

---

## 9. REVISIONS AND THE VINTAGE OF A NUMBER

### 9a. ONS guidance on revisions
**Citation:** ONS, *Guide to statistical revisions* and *Revisions policies for economic statistics*.
**URLs read:** https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions ; …/revisions/guidetostatisticalrevisions ; …/revisions/revisionspoliciesforeconomicstatistics — at source.
**Exact quotations:** Revisions are "updates to previously published statistics, analysis or data that improve quality by incorporating improved methods, additional data sources or statistics that were unavailable at the point of initial publication."; Corrections are "amendments that are made to published statistics in response to the identification of mistakes following their initial publication."; revisions are "usually reported in the next release of the data by including a notice within the latest release". The economic-statistics page indexes the National Accounts revisions policy covering "Preliminary GDP" and "Second estimate of GDP" (policy PDFs not fetched).
**Note:** The ONS web guide does not itself use "scheduled/unscheduled"; that terminology lives in the Code (2.x Q3.4 / 3.0 3.9 "revisions and corrections of errors") and GSS guidance (section 6). The Code 3.0 now *requires* a published revisions and corrections policy.
**Strength:** Strong for the revision/correction distinction. **Role:** SUPPORTING.

### 9b. How much GDP revises (ONS)
**Citation:** ONS, *GDP revisions in Blue Book 2025*, "Release date: 31 October 2025".
**URL read:** https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/gdprevisionsinbluebook2020/2025 — at source.
**Exact quotations:** "There is a trade-off between the timeliness and accuracy of estimates of gross domestic product (GDP). As additional information becomes available, we have a more complete picture of economic activity in that period."; "Our focus is on those estimates published 3 months and 36 months after the first estimate of quarterly GDP, reflecting the three-year production cycle of UK GDP."; "The mean absolute revision (MAR) to quarterly GDP from Quarter 1 2020 to Quarter 2 2025 in Blue Book 2025 was slightly larger than in recent Blue Books, at 0.66 percentage points"; Table 1 (Q2 1961 to Q1 2025): mean absolute revision 0.2pp at t+3 months and 0.5pp at t+36 months; mean revision 0.0pp at t+3 and 0.1pp at t+36; pandemic-era (from Q1 2020) MAR 0.2pp at t+3 and 0.7pp at t+36; "initial revisions (t plus 3 months) are not statistically significant, those revisions…at t plus 36 months are marginally statistically significant over the full span".
**Strength:** Very strong. **Role:** LOAD-BEARING illustration: a quarterly growth figure typically moves by half a percentage point over three years — about the size of a typical quarter's growth.

### 9c. OSR on revisions as normal
**Citation:** OSR, *Revisions of estimates of UK Gross Domestic Product (GDP)*, "Published: 29 November 2023".
**URLs read:** https://osr.statisticsauthority.gov.uk/publication/revisions-of-estimates-of-uk-gross-domestic-product-gdp/ and …/pages/5 — at source.
**Exact quotations:** "Revisions to early, near real-time estimates are normal and unavoidable and are an inherent part of the evolving measurement process."; "Our overall conclusion is that the more extreme criticisms that ONS received are misplaced."; "ONS should enhance its communication of the uncertainty that lies around GDP estimates as they evolve."; "ONS should present such information in a central place so that users do not face the challenge of having to navigate through earlier publications."; figures: "MAR in the COVID period was 0.78pp, compared with pre-COVID and GFC periods of 0.12pp and 0.20pp"; "During COVID period, first estimate of quarterly GDP growth was revised up by 0.58pp at T+12 months".
**Strength:** Very strong. **Role:** LOAD-BEARING (regulator's statement that revision ≠ error, plus the recommendation that revision history be visible in one place — a dashboard requirement).

### 9d. Vintage databases
**Citation:** Federal Reserve Bank of St. Louis, ALFRED (ArchivaL Federal Reserve Economic Data).
**URLs read:** https://alfred.stlouisfed.org/ and https://alfred.stlouisfed.org/help — at source.
**Exact quotations:** "ALFRED® allows you to retrieve each economic data release (vintage) that was available on a specific date in history."; "a collection of vintage versions of U.S. economic data"; captures "data as reported by a source on past dates in history"; "In general, economic data for past observation periods are revised as more accurate estimates become available. As a result, previous vintages of data can be superseded and may no longer be available from various data sources."; purpose: to "reproduce past research, build more accurate forecasting models, and analyze economic policy decisions of the past with data that were available at the time."
**Bank of England GDP Real-Time Database** (https://www.bankofengland.co.uk/statistics/gdp-real-time-database) located but blocked by robots.txt — not read.
**What it establishes:** A "vintage" is the dataset as it stood on a given release date; the same observation period has many vintages; a number therefore has two dates — the period it describes and the date of the version you are looking at.
**Strength:** Strong. **Role:** LOAD-BEARING concept, SUPPORTING source.

---

## 10. REFERENCE PERIODS AND THE UNIT OF TIME

### 10a. Reference period
**Citation:** Eurostat Statistics Explained, Glossary: Reference period.
**URL read:** https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Reference_period — at source.
**Exact quotation:** "A reference period is the time period for which statistical results are collected or calculated and to which, as a result, these values refer. The time period may be either a calendar year (reference year), a fiscal year, a semester, a quarter, a month and even a day." "Some data, like population variables, relate to one specific time, a reference time point". "The reference period should be distinguished from the publication time, the period or point in time at which the statistical data are published."
**GSS harmonised principle "Survey Reference Period"** (v5.6, June 2017; https://gss.civilservice.gov.uk/wp-content/uploads/2019/04/Survey-Reference-Period-June-17.pdf — at source) does not define the term; it harmonises on financial year: "Most regular or continuous Government social surveys use financial year as the reference period though there are exceptions."; "The presentation of the financial year reference period should take the form '2001-02'."; rationale "There appears to be a significant need for annual figures on a common time basis."
**Strength:** Strong. **Role:** LOAD-BEARING (the Eurostat sentence is the cleanest definition; note the ESS Article 12 definition of timeliness depends on it).

### 10b. The statistical day: the midnight census
**Citation:** NHS England, *Bed Availability and Occupancy Quarterly Return Definitions (KH03)* guidance (document undated; file dated January 2023).
**URL read:** https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2023/01/KH03-Guidance-January-2023.pdf — at source.
**Exact quotations:** "For wards open overnight, an occupied bed day is defined as a bed which is occupied at midnight on the day in question."; "For wards open day only, an occupied bed day is defined as a bed in which the treatment or care of at least one patient has taken place during the day."
**Evidence that the midnight convention is a measurement artefact** (SECONDARY / ABSTRACT-ONLY — publisher and PubMed pages blocked): Pierce, L. et al., "Finding the time: Hourly variation in average daily census on a hospital medicine service", *Journal of Hospital Medicine* (online Nov 2023; DOI 10.1002/jhm.13233), as reported by *Today's Hospitalist* (31 Jan 2024, https://todayshospitalist.com/midnight-census/): "Measuring ADC at midnight, as traditionally done, may underestimate workload and therefore contribute to staffing shortages and physician burnout."; reported delta between midnight and 7 a.m. "about five or six patients"; 9.1-patient difference between an 11 a.m. peak and 7 p.m. trough, "5.5% of peak census". Companion editorial: Calderon et al., "Time to move past midnight census", *J Hosp Med* 2024 (DOI 10.1002/jhm.13267) — not read. Older: Simon/Yankovskyy et al., "Midnight census revisited: Reliability of patient day measurements in US hospital units", *Int J Nurs Stud* 2010 (PubMed 20673896) — ABSTRACT NOT REACHED; and a 2013 *Crit Care Med* abstract titled "Patient census at midnight does not accurately reflect peak bed utilization in a pediatric ICU" — title only (paywalled, 402).
**What it establishes:** An official UK statistic defines "a day" of occupancy by a single instant (midnight), so activity that peaks in daytime and troughs at night is systematically under-counted; the choice of census instant is part of the number's provenance.
**Strength:** KH03 definition very strong; the artefact evidence moderate (secondary). **Role:** LOAD-BEARING for the definition; SUPPORTING for the artefact.

### 10c. Calendar / trading-day effects
**Citation:** Eurostat Statistics Explained, Glossary: Calendar adjustment.
**URL read:** https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Calendar_adjustment — at source.
**Exact quotations:** Calendar adjustment: "A statistical method for removing the calendar effect from an economic time series."; calendar effect: "The variation caused by the changing number of particular week days or holidays in different months or other time periods."; working-day adjustment: "A part of the calendar adjustment which focusses on the changing number of working days (Monday - Friday) in the various months."; examples: "The timing of certain public holidays (Easter can fall in March or in April, depending on the year)."; "The possible overlap of certain public holidays and non-working days (1 May can fall on a Sunday)."; "The occurrence of a leap year."
**What it establishes:** Months are not equal containers — a month with five Fridays vs four is a different measurement window; official statistics correct for this explicitly. (Finance "trading day"/T+1 settlement sources found were all commercial explainers; not fetched as they add nothing methodological.)
**Strength:** Strong. **Role:** SUPPORTING.

### 10d. Night-time window (definition only, per instruction)
ONS, *The night-time economy, UK: 2022* (24 January 2023; https://www.ons.gov.uk/businessindustryandtrade/business/activitysizeandlocation/articles/thenighttimeeconomyuk/2022 — at source): "the night-time economy refers to activity that takes place between 6pm and 6am"; the LFS variables "USUWRK1, USUWRK2 and USUWRK3 identify whether a respondent's 'usual work pattern' include: (1) during the day (2) during the evening (3) at night". **Role:** COLOUR — shows an official 12-hour window that straddles midnight, i.e. the "statistical day" and the calendar day diverge. No further research done on this topic, as instructed.

### 10e. Dates as provenance: ISO 8601
**Citation (a):** GOV.UK, Open Standards for Government, *Dates, times and time-stamps standard*, first published 31 January 2018, updated 29 January 2026.
**URL read:** https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard — at source.
**Exact quotations:** "Use ISO 8601:2004 to represent dates and times in a machine-readable format in government systems."; "List date and time elements in descending order of size (years, months, days, hours, minutes, seconds)."; benefits: "more consistency in how your systems format data", "an easier way to sort documents by date and filename", improved "ability to exchange data internationally"; "You can add a Coordinated Universal Time (UTC) offset. For example, 2017-05-16T10:30:56+01:00".
**Citation (b):** ISO, "ISO 8601 — Date and time format" page; current edition ISO 8601-1:2019. URL: https://www.iso.org/iso-8601-date-and-time-format.html — at source. "ISO 8601 is the internationally accepted way to represent dates and times."; "The order of the elements used to express date and time in ISO 8601 is as follows: year, month, day, hour, minutes, seconds, and milliseconds."; "When dates are represented with numbers they can be interpreted in different ways. For example, 01/05/22 could mean January 5, 2022, or May 1, 2022."
**What it establishes:** Descending order of magnitude means that sorting the strings alphabetically sorts the moments chronologically (GOV.UK's "easier way to sort documents by date and filename" is the official statement of this). The UTC-offset point matters for any dashboard spanning a clock change: a "day" of 23 or 25 hours.
**Strength:** Very strong. **Role:** SUPPORTING.

---

## THREADS PULLED (not asked for, found anyway)
1. **Code 3.0's "Standards for Public Use"** — a new, separate set of standards that bind *any public body* using numbers in public (press releases, speeches, social media), explicitly including "management information". Requirement to "cite sources" and not to place "undue certainty" on figures. This is the closest thing in UK regulation to a rule about what a public dashboard must show, and it did not exist in 2.x. Worth a paragraph.
2. **AQuA Book 2025's black-box/AI chapter** — assurance guidance now contemplates models whose workings cannot be inspected; the answer it gives is heavier validation (does it meet the user's need in the use environment) where verification is impossible. Relevant to any dashboard with a model-generated metric.
3. **Reliability = revisions.** The ESS handbook files reliability under "data revision", and the UK GSS defines reliability as "the closeness of early estimates to subsequent estimated values". So "reliable" in official usage is a statement about the *vintage history* of a series, not a synonym for accurate. Useful corrective to loose dashboard language.
4. **FAIR A2** — "Metadata are accessible, even when the data are no longer available": a design principle that a provenance record should outlive the figure it describes (dashboards that overwrite yesterday's number fail this).
5. **DCAT 3 separates three dates** — issued, modified, temporal coverage — and recommends temporal coverage as a *closed interval*. That is a ready-made schema for the "date of the number" argument.
6. **OSR's "bear the weight of the decisions"** test (2023) is a more vivid formulation of fitness for purpose than anything in the Code itself.
7. **NAO on West Coast**: the model "received no extra quality assurance once the Department decided to use it to calculate the loan" — the failure was re-purposing, not arithmetic. This reframes "fit for purpose" as *fit for this purpose*.

## LEFT OUT AND WHY
- ESS QAF v2.0 full text and the ESS handbook's S.05 reference-period concept: the Article 12 legal definitions and the ES CoP indicators already give the dimension definitions verbatim; the QAF adds methods/indicators of lesser use to a first-time reader.
- Bank of England real-time database page: robots-blocked; ALFRED supplies the same concept at source.
- Code 2.x T6 and V3 principle text: archives blocked; 3.0 successors quoted in full and are what now applies.
- Commercial "T+1 settlement" explainers for "trading day": not authoritative and not about measurement; Eurostat calendar-adjustment covers the methodological point better.
- Juran's original 1951 Handbook: not reachable; attribution via Wang & Strong is adequate for a one-line origin note.
- Nelson/Lind-type older midnight-census literature: paywalled/captcha'd; the KH03 definition plus one recent study is enough to make the point.
- ISI/CSO/UN quality frameworks surfaced in searches: redundant with ESS.
- Code 3.0 Standards 1, 2, 8 practices: governance/engagement rather than provenance.

## RICH REFERENCES (max three)
1. **Code of Practice for Statistics, Edition 3.0, Standards 6, 7, 9 and 10** — https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/5/ . One page contains the whole checklist of what must accompany a number in the UK, in current, quotable form.
2. **The AQuA Book (2025)** — https://www.gov.uk/guidance/the-aqua-book . Roles, verification vs validation, proportionality, assumptions log, documentation, black boxes; readable end-to-end; and the 2015 paragraph 6.3 one-liner ("conducted correctly" vs "correct analysis") remains the best definition.
3. **W3C PROV-DM** — https://www.w3.org/TR/prov-dm/ . Entity/Activity/Agent and the six relations give the book a formal grammar that maps directly onto source/method/responsible-party; pairs with FAIR R1.2 and DCAT 3's three dates.

## WHAT SURPRISED ME
- Both of the UK's foundational documents in this facet were replaced within three months of each other in 2025 (AQuA Book 30 July; Code 3.0 published 3 November, launched 30 October) — anything the author has read citing "Q3.3" or "the Aqua Book (2015)" is already out of date.
- The 3.0 Code moved "comparable across and within geographies at regional, national and local levels" and "provide a consistent back series" into mandatory practice wording (6.6, 7.5) — local comparability is now an explicit requirement, not an aspiration.
- Official "reliability" is defined by revisions, not by truth; and the regulator's position is that half-a-point revisions to GDP over three years are "normal and unavoidable".
- The UK counts a hospital bed-day by whether a bed is occupied at a single instant, midnight; the published definition offers no rationale.
- GOV.UK's stated reason for ISO 8601 includes, in so many words, that it makes filenames sort by date — the lexical-equals-chronological property is official policy rationale, not folklore.
- The Code's voluntary route involves no assessment at all: an organisation publishes a self-statement and is listed; OSR intervenes only informally on complaint. The "badge" is self-awarded.

---

## Agent B — Missingness, nulls and the official vocabulary of nothing

# Research report — Missingness, nulls and the official vocabulary of "nothing"

All fetched 2026-10-06 via WebFetch (a summarising fetcher; where it returned paraphrase rather than text I say so and have not quoted it). Direct curl to source hosts is blocked from this sandbox, so every quotation below is what the fetcher returned as verbatim from the page; I have not altered wording. One known artefact: in the Schafer & Graham PDF the equals sign renders as "!" (OCR), noted inline.

The studio's six: ZERO · FREE · UNAVAILABLE · UNKNOWN · NOT COLLECTED · SUPPRESSED. The mapping table is at the end of section 4.

---

## 1. Rubin's missingness mechanisms

### 1a. Rubin, D.B. (1976) "Inference and missing data", Biometrika 63(3): 581–592. DOI 10.1093/biomet/63.3.581
- URL read: https://dash.harvard.edu/entities/publication/73120378-8764-6bd4-e053-0100007fdf3b (Harvard DASH record, "Metadata Only") · fetched 2026-10-06 · **ABSTRACT-ONLY** (OUP full text paywalled; ETS 1975 bulletin version on Wiley returned 403; Semantic Scholar 403).
- Exact quotation (abstract): "When making sampling distribution inferences about the parameter of the data, {theta}, it is appropriate to ignore the process that causes missing data if the missing data are 'missing at random' and the observed data are 'observed at random', but these inferences are generally conditional on the observed pattern of missing data. When making direct-likelihood or Bayesian inferences about {theta}, it is appropriate to ignore the process that causes missing data if the missing data are missing at random and the parameter of the missing data process is 'distinct' from {theta}. These conditions are the weakest general conditions under which ignoring the process that causes missing data always leads to correct inferences."
- Establishes: the origin of MAR; note Rubin's 1976 vocabulary is "missing at random" + "observed at random" (MCAR is the conjunction; the acronyms MCAR/MAR/MNAR are later usage). The phrase "ignore the process that causes missing data" is the whole point: the question is never "how much is missing" but "can the *process* be ignored".
- Strength: high for the abstract; do not quote body text from this.
- Role: LOAD-BEARING (as the origin), but quote the definitions from 1c/1d below.

### 1b. Schafer, J.L. & Graham, J.W. (2002) "Missing Data: Our View of the State of the Art", Psychological Methods 7(2): 147–177
- URL read: https://stat.ethz.ch/education/semesters/ss2012/ams/paper/missing_data_1.pdf (institutional copy, ETH Zürich course page) · fetched 2026-10-06 · at source (full PDF).
- Exact quotations:
  - Abstract: "Statistical procedures for missing data have vastly improved, yet misconception and unsound practice still abound. The authors frame the missing-data problem, review methods, offer advice, and raise issues that remain unresolved. They clear up common misunderstandings regarding the missing at random (MAR) concept. They summarize the evidence against older procedures and, with few exceptions, discourage their use. They present, in both technical and practical language, 2 general approaches that come highly recommended: maximum likelihood (ML) and Bayesian multiple imputation (MI). Newer developments are discussed, including some for dealing with missing data that are not MAR. Although not yet in the mainstream, these procedures may eventually extend the ML and MI methods that currently represent the state of the art."
  - Definitions (p. 151): "Rubin (1976) defined missing data to be MAR if the distribution of missingness does not depend on Ymis, P(R|Ycom) ! P(R|Yobs) [OCR: "!" = "="]. In other words, MAR allows the probabilities of missingness to depend on observed data but not on missing data." · "An important special case of MAR, called missing completely at random (MCAR), occurs when the distribution does not depend on Yobs either" · "When Equation 1 is violated and the distribution depends on Ymis, the missing data are said to be missing not at random (MNAR)".
  - Not testable (p. 152): "In general, there is no way to test whether MAR holds in a data set, except by obtaining follow-up data from nonrespondents".
  - Listwise deletion (p. 155): "Case deletion, also known commonly as listwise deletion (LD) and complete-case analysis, is used by default in many statistical programs" · "When the missing data are not MCAR, results from case deletion may be biased, because the complete cases can be unrepresentative of the full population" · "When MCAR holds, case deletion can still be inefficient. … Researchers become acutely aware of the inefficiency of case deletion in multivariate analyses involving many items, in which mild rates of missing values on each item may cause large portions of the sample to be discarded." · "Among older methods for missing data, the most popular is to discard units whose information is incomplete."
  - Ad hoc fixes: "Unfortunately, ad hoc edits may do more harm than good, producing answers that are biased, inefficient (lacking in power), and unreliable."
  - Multiple imputation: "MI, proposed by Rubin (1987), has emerged as a flexible alternative to likelihood methods for a wide variety of missing-data problems. MI retains much of the attractiveness of single imputation from a conditional distribution but solves the problem of understating uncertainty. In MI, each missing value is replaced by a list of m > 1 simulated values … Each of the m data sets is analyzed in the same fashion by a complete-data method. The results, which may vary, are then combined by simple arithmetic to obtain overall estimates and standard errors that reflect missing-data uncertainty as well as finite-sample variation."
  - Pairwise/available-case: "We believe that the underlying principle of AC analysis—to make use of all the available data—is eminently sensible, but deleting cases is a poor way to operationalize it."
- Establishes: canonical plain definitions; software defaults to the worst method; MI's selling point is honesty about uncertainty (it refuses to present one made-up number as if observed — directly relevant to what a display owes).
- Strength: high. Role: LOAD-BEARING.
- Note: I asked for a sentence saying "the rate is not what matters, the mechanism is" and the fetcher could not find one verbatim in this paper; do not attribute that phrasing to Schafer & Graham. Use NRC 2010 / Sterne 2009 below for that point.

### 1c. Sterne, J.A.C., White, I.R., Carlin, J.B. et al. (2009) "Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls", BMJ 338:b2393
- URL read: https://www.bmj.com/content/338/bmj.b2393 · fetched 2026-10-06 · at source (open access).
- Exact quotations (Box 1 — the best plain-English versions I found):
  - MCAR: "There are no systematic differences between the missing values and the observed values. For example, blood pressure measurements may be missing because of breakdown of an automatic sphygmomanometer"
  - MAR: "Any systematic difference between the missing values and the observed values can be explained by differences in observed data. For example, missing blood pressure measurements may be lower than measured blood pressures but only because younger people may be more likely to have missing blood pressure measurements"
  - MNAR: "Even after the observed data are taken into account, systematic differences remain between the missing values and the observed values. For example, people with high blood pressure may be more likely to miss clinic appointments because they have headaches"
  - "Unfortunately, it is not possible to distinguish between missing at random and missing not at random using observed data."
  - "the risk of bias due to missing data depends on the reasons why data are missing" (fetcher gave this as the mechanism-not-amount statement).
  - "Where complete cases and multiple imputation analyses give different results, the analyst should attempt to understand why, and this should be reported in publications."
- Strength: high. Role: LOAD-BEARING for plain-English definitions.

### 1d. National Research Council (2010) *The Prevention and Treatment of Missing Data in Clinical Trials* (panel chaired by Roderick Little), Chapter 4 "Drawing Inferences from Incomplete Data"
- URL read: https://www.nationalacademies.org/read/12955/chapter/6 · fetched 2026-10-06 · at source (open read-online).
- Exact quotations: p. 51 "Missing data are missing completely at random (MCAR) if missingness does not depend on values of the covariates, auxiliary and outcome variables (X,V,Y)." · p. 53 "When MAR fails to hold, missing data are said to be MNAR." · p. 52 "With incomplete data, assumptions about both the missing data mechanism and the full data model are unverifiable from the data." · p. 54 "Under MAR, the methods provided above will provide valid inferences. However, the MAR assumption cannot be verified from observed data." · p. 54 (sixth principle) "the analysts should assess the robustness of the treatment effect inferences by conducting a sensitivity analysis."
- Establishes: the authoritative Little-chaired statement that the *mechanism* decides validity and is unverifiable — hence sensitivity analysis, i.e. you must show the reader what would change if the nothing were something. This stands in for Little & Rubin (no open chapter of the book found).
- Strength: high. Role: SUPPORTING.

### 1e. How common is mishandling? Bell, M.L., Fiero, M., Horton, N.J., Hsu, C.-H. (2014) "Handling missing data in RCTs; a review of the top medical journals", BMC Medical Research Methodology 14:118
- URL read: https://link.springer.com/article/10.1186/1471-2288-14-118 · fetched 2026-10-06 · at source (open access).
- Exact quotation (abstract, results): "Of the 77 identified eligible articles, 73 (95%) reported some missing outcome data. The most commonly used method to handle missing data in the primary analysis was complete case analysis (33, 45%), while 20 (27%) performed simple imputation, 15 (19%) used model based methods, and 6 (8%) used multiple imputation. 27 (35%) trials with missing data reported a sensitivity analysis." Sample: RCTs published July–December 2013 in BMJ, JAMA, Lancet and NEJM.
- Establishes: even in the four top medical journals, 45% used the method Schafer & Graham discouraged a decade earlier; only 8% used MI.
- Strength: high (single review, narrow domain — say "in a 2014 review of top-four medical journals", not "in research generally"). Role: SUPPORTING.

---

## 2. David Hand, *Dark Data: Why What You Don't Know Matters* (Princeton UP, 2020)

### 2a. Publisher sample (Chapter 1), Princeton University Press
- URL read: https://pup-assets.s3.amazonaws.com/public/onix/images/9780691182377/9780691182377.pdf (linked from https://press.princeton.edu/books/hardcover/9780691182377/dark-data) · fetched 2026-10-06 · at source (publisher PDF sample). The fetcher declined to reproduce long consecutive passages from a copyrighted book, so quotes are short; page numbers are the book's.
- The taxonomy, exactly as printed (pp. 26–27), introduced by "The DD-Types, which are introduced in this book, and which are summarized in chapter 10, are as follows:":
  "DD-Type 1: Data We Know Are Missing
  DD-Type 2: Data We Don't Know Are Missing
  DD-Type 3: Choosing Just Some Cases
  DD-Type 4: Self-Selection
  DD-Type 5: Missing What Matters
  DD-Type 6: Data Which Might Have Been
  DD-Type 7: Changes with Time
  DD-Type 8: Definitions of Data
  DD-Type 9: Summaries of Data
  DD-Type 10: Measurement Error and Uncertainty
  DD-Type 11: Feedback and Gaming
  DD-Type 12: Information Asymmetry
  DD-Type 13: Intentionally Darkened Data
  DD-Type 14: Fabricated and Synthetic Data
  DD-Type 15: Extrapolating beyond Your Data"
  (Note lowercase "beyond" as printed.)
- Other exact quotations: p. 4–5 "The term 'dark data' arises by analogy with the dark matter of physics. About 27 percent of the universe consists of this mysterious substance, which doesn't interact with light or other electromagnetic radiation and so can't be seen." · "Dark data and dark matter behave in an analogous way: we don't see such data, they have not been recorded, and yet they can have a major effect on our conclusions, decisions, and actions." · "Dark data are concealed from us, and that very fact means we are at risk of misunderstanding, of drawing incorrect conclusions, and of making poor decisions." · "unless we are aware of the possibility that there's something unknown lurking out there, the consequences can be disastrous, even fatal." · p. 6 "Dark data arise in many different shapes and forms as well as for many different reasons, and this book introduces a taxonomy of such reasons, the types of dark data, labeled DD-Type x… Nonetheless, an awareness of these DD-Types, and examination of examples showing how dark data can manifest, can equip you to identify when problems occur and protect you against their dangers." · DD-Type 1 example (p. 7, trial with unknown outcomes): "So the 30-day survival was unknown for over 11 percent of the patients." and "We know these patients had some outcome—we just don't know what it was." · DD-Type 2 (p. 10–11): "Here we are unaware of them."; Street Bump pothole app — "ownership of cars and expensive smartphones is more likely to be concentrated in wealthier areas."; Hurricane Sandy — "those regions transmitting fewer tweets may have been doing so not because the storm had less impact but simply because there were fewer Twitter users." · p. 9 "A similar phenomenon happens with surveys, in which nonresponse is a source of difficulty." · p. 24 "we may not know that they [dark data] are not there".
- Chapter 1 does NOT contain one-sentence definitions of each DD-Type (confirmed by fetch); the sample ends at the list. I asked specifically for a sentence saying missing data is "worse than no data" or "worse than useless" and the fetcher reported it ABSENT from the sample. Do not attribute that phrasing to Hand without the full book in hand; the defensible paraphrase is DD-Type 2's point — the danger is in not knowing something is missing.
- Strength: high for the list and short quotes. Role: LOAD-BEARING.

### 2b. Hand, D.J. (2020) "Dark data", Significance 17(3): 42–44, June 2020, DOI 10.1111/1740-9713.01406
- URL read: https://academic.oup.com/jrssig/article/17/3/42/7037909 · fetched 2026-10-06 · at source (Wiley PDF blocked by robots; OUP mirror readable).
- Exact quotations: dark data are "data you do not have. They might be data you thought you had, or hoped to have, or wished you had." · "as a result of these dark data, the data missing from your view of the world, you are at risk of misunderstanding" · Challenger: "what was missing from the graph, however, were points for all those previous launches which had had no problems with the seals."
- Establishes: Hand's own one-line definition and his signature example of a *chart* that lied by omission — a plotted nothing (launches with zero incidents were left off, so zero was invisible). This is the best bridge from Hand to a dashboard chapter.
- Strength: high. Role: LOAD-BEARING.
- (Imperial College news piece, https://www.imperial.ac.uk/news/195274/dark-data-why-what-dont-know/, 12 Feb 2020, contains no direct Hand quotes — only journalist paraphrase; LEFT OUT.)

---

## 3. Database nulls

### 3a. Codd, E.F. (1986) "Missing Information (Applicable and Inapplicable) in Relational Databases", ACM SIGMOD Record 15(4): 53–78, December 1986
- URL read: https://sigmodrecord.org/publications/sigmodRecord/8612/pdfs/16301.16303.pdf · fetched 2026-10-06 · at source (ACM SIGMOD Record archive PDF; dl.acm.org 403s).
- Exact quotations:
  - p. 53 opening: "There has been some technical and justified criticism of the treatment of missing information in the data sublanguage SQL and in IBM's Database 2 system"; purpose "to clarify and extend the treatment of missing information by the relational model".
  - The two kinds (pp. 55–56): "A missing and applicable" versus "I missing and inapplicable." · "We begin with a definition of the 'missing-but-applicable-value mark'... Suppose that, represented in the database, there is an object z of type Z and, at this time, the value of P for this object is unknown. Then, P would be assigned an A-mark..." · "On the other hand, suppose that property P is inapplicable to the particular object z. Then P would be assigned an inapplicable-value mark."
  - Examples (p. 56): "1) an employee with a missing-but-applicable present salary -- his record would have an A-mark in the salary attribute; 2) an employee with an inapplicable sales commission (such an employee does not sell any products at this time) -- his record would have an I-mark."
  - Marks not values (pp. 56–57): "A basic principle of the relational approach to missing information is that of recording the fact that a db-value is missing by means of a mark...There is nothing imprecise about a mark" · "Why are we now calling these items 'marks', rather than 'values' or 'null values' or 'nulls'? We cite four reasons: 1) marks seldom behave like values; 2) we now have two kinds of marks, where there was previously just one kind of null; 3) some host languages deal with objects called 'nulls' which are quite different in meaning from database marks; 4) 'marked' and 'unmarked' are better adjectives than 'nulled'."
  - Three- vs four-valued logic (pp. 61–62): "From this we see that there is a clear need in any systematic treatment of missing values to extend the underlying two-valued predicate logic to a three-valued predicate logic." truth values "true or maybe or false" · "A natural subsequent question is: must the systematic treatment of inapplicable values cause an additional extension...to a four-valued logic? Such an extension has been proposed...We believe, however, that the need for a four-valued logic is not urgent" (he later adopted 4VL in RM/V2, 1990 — not reached at source here).
  - **Zero as a stand-in for missing (p. 73)**: "In at least one well-known... DBMS product, zero has been chosen as the value to indicate missing information in all numeric attributes. I consider the number zero to be far too valuable in its normal role in all kinds of business activities...Therefore, I do not consider zero to be an acceptable choice to be reserved by a DBMS for denoting a missing numeric db-value." · on default-value schemes (p. 74): "The DV scheme [does] not appear to provide any tools for the handling of missing information -- it merely provides a means for representing the fact that something is missing".
  - On SQL (p. 70): "In [CJD1] Date provides numerous cases in which the processing of nulls (i.e., A-marks) in DB2 is non-systematic. I find myself in agreement with these comments as criticisms of this particular implementation of the relational model".
- Establishes: the father of the relational model distinguished UNKNOWN (A-mark) from NOT APPLICABLE (I-mark) in 1986 and explicitly condemned coding missing as zero. SQL kept one NULL.
- Strength: high. Role: LOAD-BEARING.

### 3b. Console, Guagliardo & Libkin (2019) "Do We Need Many-valued Logics for Incomplete Information?", IJCAI-19, pp. 6141–6145
- URL read: https://www.ijcai.org/proceedings/2019/0851.pdf · fetched 2026-10-06 · at source.
- Exact quotations: "every database management system (DBMS) uses a three-valued logic for handling incomplete information, namely Kleene's logic … This was the design choice of SQL, the language of relational DBMSs, which is now written into the SQL Standard [ISO/IEC, 2016], presented in all database textbooks, and implemented in all database products. … The use of Kleene's logic was first proposed by Codd [1975], but many other variants appeared afterward. Codd [1987] looked at a four-valued logic, but in the end argued against it due to the additional complexity. Nonetheless, well-documented problems with incomplete information [Date and Darwen, 1996; Date, 2005] led to the search of more appropriate logics for handling incompleteness. … Darwen and Date [1995] suggested dropping nulls altogether and go back to the usual Boolean two-valued logic." Abstract: "This design by a committee from several decades ago is now part of the standard adopted by vendors of database management systems."
- References as printed: "[Codd, 1975] Edgar F. Codd. Understanding relations (installment #7). FDT - Bulletin of ACM SIGMOD, 7(3):23–28, 1975." · "[Codd, 1987] Edgar F. Codd. More commentary on missing information in relational databases. SIGMOD Record, 16(1):42–50, 1987." · "[Date and Darwen, 1996] … A Guide to the SQL Standard. Addison-Wesley, 1996." · "[Date, 2005] … Database in Depth – Relational Theory for Practitioners. O'Reilly, 2005."
- Strength: high. Role: SUPPORTING (authoritative history in one paragraph).

### 3c. Darwen, H. (2012) "How To Handle Missing Information Without Using NULL", CS319 lecture slides, University of Warwick, 28 Nov 2012
- URL read: https://www.dcs.warwick.ac.uk/~hugh/CS319/CS319-Missing-info-without-NULL.pdf · fetched 2026-10-06 · at source (author copy). Stands in for Date's "Why Three- and Four-Valued Logic Don't Work", which I could not reach at source (not open).
- Exact quotations: "SQL's NULL Is A Disaster" · "SELECT * FROM T WHERE X = Y UNION SELECT * FROM T WHERE NOT ( X = Y ) is not equal to SELECT * FROM T" · "SELECT SUM(X) + SUM(Y) FROM T is not equal to SELECT SUM(X + Y) FROM T" · "Relational theory is founded on classical, 2-valued logic"; SQL's WHERE "arbitrarily splits at the TRUE/UNKNOWN divide" · proposed decomposition into separate tables "EARNS" (known salaries), "SALARY_UNK" (amount unknown), "UNSALARIED" (no salary exists) — "Don't combine multiple meanings in a single relvar."
- Establishes: the practical absurdities (a total of two sums ≠ sum of totals) and — the thread worth pulling — Darwen's cure is exactly the studio's instinct: give each kind of nothing its own home rather than one blank.
- Strength: medium-high (lecture slides, but by the co-author of the critique). Role: SUPPORTING.

### 3d. ISO/IEC 9075:1992 (SQL-92) draft text
- URL read: https://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt · fetched 2026-10-06 · at source (widely-mirrored committee draft; the page served only ~127k chars, so later sections were summarised not quoted).
- Exact quotations: §3.1.3 null value: "A special value, or mark, that is used to indicate the absence of any data value." · §4.1: "A null value is an implementation-dependent special value that is distinct from all non-null values of the associated data type. There is effectively only one null value and that value is a member of every SQL data type."
- Paraphrase only (NOT verbatim — fetcher summary of §8.12, §8.2, §6.5): three truth values true/false/unknown with truth tables; comparison with a null operand yields unknown; nulls eliminated before AVG/SUM; COUNT(*) counts rows.
- Establishes: the standard itself says "effectively only one null value" — the single-bucket design.
- Strength: high for the two quotes. Role: LOAD-BEARING (one line).

### 3e. PostgreSQL 18 documentation (practical consequences)
- URLs read: https://www.postgresql.org/docs/current/functions-comparison.html and https://www.postgresql.org/docs/current/functions-aggregate.html · fetched 2026-10-06 · at source.
- Exact quotations: "Ordinary comparison operators yield null (signifying "unknown"), not true or false, when either input is null. For example, 7 = NULL yields null, as does 7 <> NULL." · "Do not write expression = NULL because NULL is not "equal to" NULL. (The null value represents an unknown value, and it is not known whether two unknown values are equal.)" · IS DISTINCT FROM "effectively act[s] as though null were a normal data value, rather than "unknown"" · count(*) "Computes the number of input rows." · count("any") "Computes the number of input rows in which the input value is not null." · sum "Computes the sum of the non-null input values." · avg "Computes the average (arithmetic mean) of all the non-null input values." · "It should be noted that except for count, these functions return a null value when no rows are selected. In particular, sum of no rows returns null, not zero as one might expect … The coalesce function can be used to substitute zero or an empty array for null when necessary."
- Establishes: NULL ≠ 0; NULL ≠ NULL; aggregates silently skip NULL (so an AVG over a column with unknowns is an average of the knowns, unflagged); COUNT(*) vs COUNT(col) differ by exactly the nothings; and `coalesce(sum(x),0)` is the one-line idiom by which "no rows" becomes a displayed 0 — the technical mechanism of the dashboard that shows a zero where it should show a reason.
- Strength: high. Role: LOAD-BEARING.

### 3f. R base documentation, `NA` (stat.ethz.ch R-devel manual)
- URL read: https://stat.ethz.ch/R-manual/R-devel/library/base/html/NA.html · fetched 2026-10-06 · at source.
- Exact quotations: "NA is a logical constant of length 1 which contains a missing value indicator." · "Numerical computations using NA will normally result in NA" · "Logical computations treat NA as a missing TRUE/FALSE value, and so may return TRUE or FALSE if the expression does not depend on the NA operand." · "The NA of character type is distinct from the string 'NA'. Programmers who need to specify an explicit missing string should use NA_character_." · "anyNA(NULL) is false; is.na(NULL) is logical(0)."
- Establishes: analysis software distinguishes NA (missing), NaN (not a number) and NULL (no object) — and the text "NA" is not missing. Pairs with the Analysis Function's "No to NA" below. COLOUR.

---

## 4. The official symbols for nothing

### 4a. UK Government Analysis Function, "Using symbols and shorthand in tables", published 11 January 2022 (owner: Analysis Function Central Team)
- URL read: https://analysisfunction.civilservice.gov.uk/policy-store/symbols-in-tables-definitions-and-help/ · fetched 2026-10-06 · at source.
- Contents as listed: "Who is this guidance for? · What we mean by 'shorthand' · Layout of shorthand · Where to put shorthand · No to NA · Recommended shorthand · Being more specific · Shorthand for a reason not listed here · Statistical significance · Benefits of using consistent shorthand · Related links · Any questions?"
- **Recommended shorthand — complete, verbatim:**
  - "b = break in time series — Use this shorthand when there is a break in a data series that means that data before the break cannot be directly compared with data after the break."
  - "c = confidential — Use this shorthand when a data point would give away confidential information. For example, if you would be able to identify details about a single respondent from the data. These data points must be replaced with this shorthand to maintain confidentiality clauses."
  - "e = estimated — Use this shorthand to show when a data point is estimated. Tables which are entirely estimates do not need a marker for each data point, as long as titles or accompanying information make it clear that all figures are estimates."
  - "er = earliest revision — Use this shorthand to show a period when the earliest revision was made in a particular time series. No other periods should be marked with a revision."
  - "f = forecast — Use this shorthand to show when a data point is a calculated future value instead of an observed value."
  - "low = a low figure but not a real zero — Use this shorthand to replace data points that appear as zero in a rounded table, but are not actually zero."
  - "p = provisional — Use this shorthand to show when data points are yet to be finalised, or are expected to be revised."
  - "r = revised — Use this shorthand to show when a data point has been revised since it was first published. This must not be confused with 'earliest revision'."
  - "u = low reliability — Use this shorthand to show when data points are of low quality."
  - "w = none recorded in survey — Use this shorthand when no people are estimated to be in a category. This could be because there were not any recorded by the survey or because none exist in the population."
  - "x = not available — Use this shorthand when data is unavailable for reasons other than those described in this list. For example, where data is not collected in a region."
  - "z = not applicable — Use this shorthand when a data point is not applicable. For example, in tables of employment where people under 16 cannot legally be employed."
  - Statistical significance: "ns = not significant", "s = significant at 0.05 or 5% level", "ss = significant at 0.01 or 1% level", "sss = significant at 0.001 or 0.1% level".
  - "Being more specific": "[u1]" and "[u2]" may distinguish causes; "data points of 499 or less should be replaced with the word '[low]'" (in the worked example); "A zero or '0' should only be used when a data point is a true zero." · "Use of the word low may be problematic for sensitive data such as data on deaths" — use "[k] to represent a low figure that appears as a zero when rounded." · "if some round to 100% but are not actually 100%, you can use the shorthand [high] instead."
  - NOTE: there is no "[i] imputed" in this list; imputation is covered by [e] estimated. There is no "[w] withheld" — [w] is "none recorded in survey".
- Layout/placement, verbatim: markers in square brackets "[r]", multiple as "[r][e]" — "This helps with machine readability and makes it easier to spot shorthand." · explanation above the table, e.g. "Some shorthand is used in this table, [e] = estimated, [f] = forecast." · in spreadsheets "in a cell in column A. This is because users of assistive technology will often navigate down from cell A1." · "You should never place shorthand in cells with data in spreadsheets." · "a notes column to the right-hand side of the table. Shorthand markers should go in this column along with information about which cell or cells the shorthand applies to, for example: '[x] applies to B10, C10 and D10'."
- Symbols rejected: "we do not recommend using symbols such as '. :', '*' or '†' anymore because they can be difficult to see and screen reader software can find them hard to recognise."
- "No to NA": "We do not recommend using 'NA' to describe cells with no data. This is because this shorthand is ambiguous. Some people may read it as 'Not Applicable', while other people may read it as 'Not Available'."
- Extensibility: "If you cannot find shorthand listed here for something you need to show in your tables, you can choose your own letter to use. But please check it is not one already listed in this guidance."
- Rationale: "Using consistent shorthand helps meet the requirements of the three pillars of the Code of Practice for Statistics: Trustworthiness, Quality, Value."
- **The "never blank" rule is NOT on this page.** It is in the companion guidance (4b).
- Strength: high. Role: LOAD-BEARING.

### 4b. UK Government Analysis Function, "Releasing statistics in spreadsheets", published 30 June 2021 — section "Cells with no data"
- URL read: https://analysisfunction.civilservice.gov.uk/policy-store/releasing-statistics-in-spreadsheets/ · fetched 2026-10-06 · at source.
- Exact quotations: "If you leave cells with no data blank, it can cause confusion for users of assistive technology because it makes it difficult to work out where a table starts and ends." · Exception: "However, if the following points are met, blank cells should not cause usability or accessibility issues: 1. There is only one reason a cell in a table may be left blank 2. The table is marked up correctly...3. There is a note above the table, in a cell in column A, explaining that some cells are left blank and why" · "If there are several reasons a cell in a table may be left blank you will need to use shorthand to explain why a particular cell has no data." · "Do not use symbols like full stops (..) or dashes (-). Instead, you should follow our guidance for Using symbols and shorthand in tables." · "We advise the use of square brackets for all shorthand used in a table because it makes it easier to spot." · "You should never use superscript text or symbols as your shorthand as these can be difficult for users with low vision to see."
- Establishes: the precise UK rule — a blank is tolerable only when there is exactly one reason for it and that reason is stated; more than one kind of nothing ⇒ every nothing must be labelled. This is the strongest single sentence in the whole report for the studio's thesis.
- Strength: high. Role: LOAD-BEARING.

### 4c. SDMX Global Registry — code list SDMX:CL_OBS_STATUS version 2.2 "Observation Status"
- URL read: https://registry.sdmx.org/sdmx/v2/structure/codelist/SDMX/CL_OBS_STATUS/2.2?format=sdmx-json · fetched 2026-10-06 · at source (the registry's own JSON; the 2014 .doc on sdmx.org is binary and unreadable here).
- Full code set (name only): A Normal value · B Time series break · D Definition differs · E Estimated value · F Forecast value · G Experimental value · I Value imputed by a receiving agency · K Data included in another category · W Includes data from another category · O Missing value · M Missing value; data cannot exist · P Provisional value · S Strike and other special events · L Missing value; data exist but were not collected · H Missing value; holiday or weekend · Q Missing value; suppressed · J Derogation · N Not significant · U Low reliability · V Unvalidated value.
- Full descriptions, verbatim, for the absence-related codes:
  - **O Missing value**: "This code is to be used when no breakdown is made between the reasons why data are missing. Data can be missing due to many reasons: data cannot exist, data exist but are not collected (e.g. because they are below a certain threshold or subject to a derogation clause), data are unreliable, etc."
  - **M Missing value; data cannot exist**: "Used to denote empty cells resulting from the impossibility to collect a statistical value (e.g. a particular education level or type of institution may be not applicable to a given country's education system)."
  - **L Missing value; data exist but were not collected**: "Used, for example, when some data are not reported/disseminated because they are below a certain threshold."
  - **Q Missing value; suppressed**: "Used, for example, when data are suppressed due to statistical confidentiality considerations."
  - **H Missing value; holiday or weekend**: "Used in some daily data flows."
  - **K Data included in another category**: "This code is used when data for a given category are missing and are included in another category, sub-total or total. Generally where code "K" is used there should be a corresponding code "W - Includes data from another category" assigned to the over-covered category…"
  - **N Not significant**: "Used to indicate a value which is not a "real" zero (e.g. a result of 0.0004 rounded to zero)."
  - **E Estimated value**: "Observation obtained through an estimation methodology (e.g. to produce back-casts) or based on the use of a limited amount of data or ad hoc sampling and through additional calculations … This code is to be used when the estimation is done by a sender agency. When the imputation is carried out by a receiver agency in order to replace or fill gaps in reported data series, the flag to use is I "Value imputed by a receiving agency"."
  - **I Value imputed by a receiving agency**: "Observation imputed by a receiving agency to replace or fill gaps in reported data series. This code is intended to cover all cases where a receiving agency publishes data about a sending agency that do not come from an official source in the sender agency's reporting framework. When the estimation is done by the sender agency, the flag to use is E "Estimated value"."
  - **U Low reliability**: "This indicates existing observations, but for which the user should also be aware of the low quality assigned."
  - **A Normal value**: "To be used as default value if no value is provided or when no special coded qualification is assumed. Usually, it can be assumed that the source agency assigns sufficient confidence to the provided observation and/or the value is not expected to be dramatically revised."
- Establishes: the international statistical data-exchange standard carries five distinct missing-value codes (O generic, M cannot exist, L exists-not-collected, Q suppressed, H calendar) plus K (hidden in another cell) and N (rounded-to-zero-not-zero) — the richest official vocabulary of nothing found. Note "H holiday or weekend" is a missingness code for exactly the "no report on a Sunday ≠ zero on Sunday" problem.
- Strength: high. Role: LOAD-BEARING.

### 4d. SDMX Global Registry — CL_CONF_STATUS version 1.4 "Confidentiality Status"
- URL read: https://registry.sdmx.org/sdmx/v2/structure/codelist/SDMX/CL_CONF_STATUS/latest?format=sdmx-json · fetched 2026-10-06 · at source.
- Codes (name = description): "A Primary confidentiality due to small counts" · "C Confidential statistical information" · "D Secondary confidentiality set by the sender, not for publication" · "E Not for publication, restricted for internal use only (equivalent to the code N) until the embargo time elapses; Free for publication (equivalent to the code F) after the embargo time elapses." · "F Free (free for publication)" · "G Primary confidentiality due to dominance by one or two units" · "M Primary confidentiality due to data declared confidential based on other measures of concentration" · "N Not for publication, restricted for internal use only" · "O Primary confidentiality due to dominance by one unit" · "P Information under non-statistical secrecy arrangements" · "S Secondary confidentiality set and managed by the receiver, not for publication" · "T Primary confidentiality due to dominance by two units" · "X (Deprecated) Confidentiality due to military secrecy".
- Establishes: SDMX separates *why a value is missing* (OBS_STATUS) from *why it was withheld* (CONF_STATUS), and distinguishes primary from secondary suppression and small-count from dominance reasons. Amusingly, "F" here means "Free" = free for publication — a reminder that "free" is overloaded. SUPPORTING.

### 4e. Eurostat flags
- (i) Eurostat database information page, https://ec.europa.eu/eurostat/data/database/information · fetched 2026-10-06 · at source. Verbatim: Flags "b = break in time series", "c = confidential", "d = definition differs, see metadata", "e = estimated", "f = forecast", "n = not significant", "p = provisional", "r = revised", "s = Eurostat estimate", "u = low reliability", "z = not applicable"; Special value ": = not available"; "Only one special value is used"; "The relevant explanations must be provided in the annex of the ESMS (metadata)".
- (ii) Statistics Explained, "Tutorial:Symbols and abbreviations", section "Eurostat standard flags", https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Tutorial:Symbols_and_abbreviations · fetched 2026-10-06 · at source. Table verbatim: "- (or z) | not applicable" · ": | not available (1)" · "0 | real zero" · "0n | less than half of the final digit shown and greater than real zero" · "| or b | break in time series" · "c | confidential" · "d | definition differs, see metadata" · "e | estimated value" · "f | forecast" · "n | not significant" · "p | provisional value" · "u | low reliability (2)". Footnote (1): "Never use NA or ND, or other variations to indicate data not available." Footnote (2): "For obvious reasons this flag should be used with extreme care." Also: "It is good practice to not overload tables with too many flags, which make it difficult for readers to grasp the main data patterns within tables quickly." and — the Eurostat never-blank rule — "empty table cells should be omitted. Therefore, flags for not available and confidential data should be always included."
- Establishes: Eurostat separates "0 real zero" from "0n rounds to zero" from ":" not available from "-" not applicable from "c" confidential — and forbids blank and "NA" alike. Strength: high. Role: LOAD-BEARING.

### 4f. ONS's own conventions
- Not separately located at source (style.ons.gov.uk returned binary; site search unproductive). ONS publications since 2022 use the Analysis Function set ([c] [x] [z] [low] etc.); the Analysis Function Central Team is the owner of 4a. I would state in the book that ONS follows 4a rather than claim a separate ONS list. (For the historical "— nil or negligible / .. not available" convention see 5c, ABS.)

### 4g. CDC NNDSS weekly data legend (a public-health vocabulary of nothing, found while hunting for "no report read as zero")
- URL read: https://data.cdc.gov/api/views/x9gk-5huc.json (Socrata metadata for "NNDSS Weekly Data") · fetched 2026-10-06 · at source.
- Verbatim: "U: Unavailable — The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data." · "-: No reported cases — The reporting jurisdiction did not submit any cases to CDC." · "N: Not reportable — The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction." · "NN: Not nationally notifiable — This condition was not designated as being nationally notifiable." · "NP: Nationally notifiable but not published." · "NC: Not calculated — There is insufficient data available to support the calculation of this statistic." · "Case counts for reporting years 2024 and 2025 are provisional and subject to change."
- Corroborated by MMWR 64(22), 12 June 2015, "Notice to Readers: Updated 'N' Indicators…", https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6422a6.htm: "NNICs designated 'not reportable' are indicated with an 'N'; those conditions that are reportable are recorded with either the number of cases or with a '—' (i.e., a dash symbol) to indicate that no cases were reported for that NNIC."
- Establishes: in disease surveillance the dash is deliberately *not* zero — it is "did not submit any cases", which sits between zero and unknown. Six distinct codes for "no number here". Strength: high. Role: SUPPORTING (strong illustrative).

### MAPPING TABLE — the studio's six against the official vocabularies

| Studio kind | Analysis Function (UK) | SDMX CL_OBS_STATUS 2.2 | Eurostat flag | SQL / Codd | Survey code (Understanding Society) | CDC NNDSS |
|---|---|---|---|---|---|---|
| **Zero** (counted, none) | "0" — "only … when a data point is a true zero"; [low]/[k] if rounded-to-zero; [w] "none recorded in survey" when observed-none ≠ known-none | value 0 with status A; N "not a 'real' zero" for rounded | "0 real zero"; "0n" rounds to zero | 0 (a value; Codd: zero "far too valuable" to mean missing) | a valid value, never negative | "-" No reported cases (nearest; strictly "did not submit") |
| **Free** (price of nothing) | no code — it is a value (0 with a unit) | value 0, status A | value 0 | 0, not NULL | n/a | n/a |
| **Unavailable** (exists, not obtainable) | [x] not available "for reasons other than those described" | L "data exist but were not collected"; O generic; H holiday/weekend | ":" not available | NULL (A-mark, applicable but missing) | -9 "Missing by error or implausible"; -7 proxy; -10/-11 not available for sample | U Unavailable; NP not published; NC not calculated |
| **Unknown** (asked, no answer) | [x] (no finer AF code; [u] if low reliability) | O / L | ":" | NULL (A-mark) | -1 "Don't know"; -2 "Refused" | — |
| **Not collected** (nobody measured) | [x] "where data is not collected in a region"; [z] "not applicable" when it *could not* apply | M "data cannot exist" (structural); L "exist but were not collected" | "-"/"z" not applicable; ":" | I-mark (inapplicable) — collapsed into NULL in SQL | -8 "Valid skip" (never asked, ineligible); -20/-21 not in that study | N Not reportable; NN not nationally notifiable |
| **Suppressed** (withheld) | [c] confidential — "must be replaced with this shorthand" | Q "Missing value; suppressed" + CONF_STATUS A/C/D/G/O/T… | "c" confidential | application-level NULL, indistinguishable | n/a (file-level SDC) | NP "notifiable but not published" |

Two things the table shows: (1) the official world splits the studio's "not collected" into two — *could not exist* (SDMX M, AF [z], Codd I-mark, structural zero) and *could exist but nobody asked* (SDMX L, AF [x], survey -8); the author may want to decide whether "not applicable" is a seventh kind or a sub-kind. (2) No official scheme has a code for "free": every scheme treats it as the value 0, which is the studio's point.

---

## 5. Zero against missing

### 5a. Analysis Function (4a above): "A zero or '0' should only be used when a data point is a true zero." · [low] "a low figure but not a real zero" · [k] for sensitive data · [w] "none recorded in survey — … This could be because there were not any recorded by the survey or because none exist in the population." — the official admission that a survey zero is ambiguous between sampling zero and population zero.
### 5b. SDMX N "not a 'real' zero (e.g. a result of 0.0004 rounded to zero)"; Eurostat "0 real zero" vs "0n less than half of the final digit shown and greater than real zero". Codd 1986 p. 73 on zero as a missing-marker (3a).
### 5c. Historical conflation, at source: Australian Bureau of Statistics, 4102.0 Australian Social Trends 2005 (12 July 2005), symbols list — https://www.abs.gov.au/AUSSTATS/abs@.nsf/7d12b0f6763c78caca257061001cc588/bb135efabb558eeaca25703b0080cca4!OpenDocument · fetched 2026-10-06 · at source. Verbatim: "— | nil or rounded to zero (including null cells)" · ".. | not applicable" · "n.a. | not available" · "n.y.a. | not yet available" · "n.p. | not published" · "* | subject to high sampling variability" · "** | data suppressed due to unacceptably high sampling variability" · "p | preliminary — figures or series subject to revision" · "r | figures or series revised since previous edition". Establishes: a single dash once meant nil OR rounded-to-zero OR null cell — three of the studio's kinds in one glyph — which is what the UK 2021–22 reform and SDMX were correcting. Note "n.y.a. not yet available" (temporal unavailability) as a kind the studio does not name. COLOUR/SUPPORTING.
### 5d. Structural vs sampling zero — CMU 36-402 lecture note "Fixed and Random Zeroes—A Quick Look", https://www.stat.cmu.edu/~brian/kim/36-402.s98-alt/week09/thu1/node1.html · fetched 2026-10-06 · at source (teaching note; secondary authority — Bishop, Fienberg & Holland and Agresti are the primary texts, not open). Verbatim: a sampling zero "comes about when the cell in the table has positive probability but we didn't observe anything there"; a structural zero "comes about when the cell in the cross-classification is not possible"; "Structural zeroes (i.e., fixed in advance) do not in themselves cause any estimation difficulties, but they may make it difficult to formulate a model." Strength: medium. Role: SUPPORTING.
### 5e. Data-loss case, at source: Public Health England, "PHE statement on delayed reporting of COVID-19 cases", 4 October 2020, https://www.gov.uk/government/news/phe-statement-on-delayed-reporting-of-covid-19-cases · fetched 2026-10-06. Verbatim: "15,841" cases from "25 September to 2 October" were not included because "some files containing positive test results exceeded the maximum file size that takes these data files and loads then into central systems" [sic, "loads then"]; "a rapid mitigation has been put in place that splits large files". **The statement does not name Excel or a row limit** — that detail is from press reporting, so the book should say "a file-size limit in the loading pipeline" if citing at source. One line only, as asked.
### 5f. Reporting lag read as decline: CDC NCHS, Provisional COVID-19 death counts, Technical Notes (last reviewed 20 Sept 2023), https://www.cdc.gov/nchs/nvss/vsrr/covid19/tech_notes.htm · fetched 2026-10-06. Verbatim: "The data shown on this page may be incomplete, and will likely not include all deaths that occurred during a given time period, especially for the more recent time periods." · "COVID-19 deaths are 65% complete within 2 weeks, 85% complete within 4 weeks, and 95% complete within 8 weeks of when the death occurred." Establishes: a not-yet-reported death is shown as not-a-death; the right-hand end of every lagged series is a nothing dressed as a low number. SUPPORTING.
### 5g. "No report read as zero" — I looked for a documented case at source in The COVID Tracking Project (analysis post "Daily COVID-19 Data Is About to Get Weird", Erin Kissane, 24 Nov 2020, which has only "Massachusetts and Wyoming have already noted on their dashboards that they will not report on Thanksgiving Day"; their FAQ and Data Definitions pages contain no null-vs-zero rule). NOT FOUND at source as a crisp case; the CDC NNDSS dash (4g) and SDMX H (4c) are the official recognitions of the same problem. Do not cite a "no report = zero" anecdote without a source.

---

## 6. Imputation and what a display owes

### 6a. Analysis Function (4a): [e] estimated covers imputation; "Tables which are entirely estimates do not need a marker for each data point, as long as titles or accompanying information make it clear". There is no [i].
### 6b. Analysis Function, "Communicating quality, uncertainty and change", 17 December 2018, https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/ · fetched 2026-10-06 · at source. Verbatim: "Include high-level information on any adjustments made to the data and statistics before publication (for example, imputation or seasonal adjustment)" · "publish quantitative measures of uncertainty, where they are available" including "imputation rates" · "Use words like 'estimates' throughout the publication, which helps to indicate that there is uncertainty around the numbers" · "Use phrasing such as 'provisional results'" · quality information "critical to allow users to assess and use statistics sensibly should be prominent, easy to find, clearly signposted and not hidden away in background appendices or footnotes". Strength: high. LOAD-BEARING.
### 6c. Analysis Function, "Data visualisation: charts", 19 May 2022, section "Breaks in time series", https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ · fetched 2026-10-06 · at source. Verbatim, complete: "Discontinuities in time series can occur due to missing data points and changes in methods. The best way to deal with discontinuity varies depending on the data and the story you are telling. But, it must always be highlighted. You do not always have to use a line for a time series with a discontinuity. Displaying the data as individual points may be better. If you do use a line, do not join the points either side of the missing data point, even if the line is dotted or dashed. Joining points implies we know something about the data." Example chart described: a gap marked by "two vertical dashed lines and annotation stating data was not collected in 2020 due to COVID-19" (approved) versus a dashed-line join (marked incorrect). The page has **no** guidance on styling provisional/forecast/imputed points differently (confirmed). Strength: high. **LOAD-BEARING — this is the one official rule on drawing a nothing on a chart.**
### 6d. Code of Practice for Statistics, Edition 3.0 (Autumn 2025), https://osr.statisticsauthority.gov.uk/wp-content/uploads/sites/3/2026/08/Code-of-Practice-for-Statistics-3.0.pdf · fetched 2026-10-06 · at source. Verbatim practices: 7.1 "Prominently communicate the quality of the statistics and the strengths and limitations that impact their use, reflecting the needs of different types of users" · 7.2 "Report on the key quality dimensions such as accuracy and timeliness, and, where possible, give estimates of error and confidence for the statistics. Summarise how uncertainty in the estimates may impact use by using qualifying words, numbers or graphics" · 7.3 "Prominently communicate limitations in the underlying data and explain their impact on the statistics" · 3.9 "Release revisions and corrections of errors transparently and as soon as possible … being clear about the nature and scale of change" · 1.3 "Present statistics impartially and objectively, ensuring statistical communication is balanced and does not mislead" · 4.5 "Protect the confidentiality of individual and business information when producing statistics … apply appropriate disclosure control methods before release". (The Code does not mention imputation by name.) Strength: high. SUPPORTING.
### 6e. NCES Statistical Standards (2002), Standard 4-1 "Data Editing and Imputation of Item Nonresponse", https://nces.ed.gov/statprog/2002/std4_1.asp · fetched 2026-10-06 · at source. Verbatim: Standard 4-1-7 "All imputed values on a data file must be clearly identified as such." · Guideline 4-1-7A "Imputed data should be flagged in associated 'flag' fields. The imputation method should be identified in the flag." · Standard 4-1-6 "When imputations are used, documentation indicating the weighted proportion of imputed data must be presented for all published estimates based on NCES data." (Fetcher paraphrase, not verbatim: items with response rates below 70% must be footnoted in tables; below 85% footnoted to alert readers.) Establishes: the clearest official "imputed values must be flagged" rule found. Strength: high. LOAD-BEARING for §6.
### 6f. SDMX E vs I (4c): the standard even distinguishes *who* imputed — sender (E) or receiver (I).
### 6g. Eurostat: "e estimated value", "s Eurostat estimate" (4e) — again distinguishing whose estimate.
### 6h. Ethics: American Statistical Association, Ethical Guidelines for Statistical Practice (2022), https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice · fetched 2026-10-06 · at source. Verbatim: B.1 "Communicates data sources and fitness for use, including data generation and collection processes and known biases...Communicates data processing and transformation procedures, including missing data handling." · B.2 "Is transparent about assumptions made in the execution and interpretation of statistical practices, including methods used, limitations, possible sources of error, and algorithmic biases." · C.2 "does not use statistical practices to mislead any stakeholder." I found no dedicated ethics paper on "presenting imputed values as observed" at source; the ASA B.1 line is the professional-ethics anchor. SUPPORTING.

---

## 7. "Not asked" and "no answer" in surveys

### 7a. Understanding Society (UK Household Longitudinal Study), Main Survey User Guide, "Missing values"
- URL read: https://www.understandingsociety.ac.uk/documentation/mainstage/user-guides/main-survey-user-guide/missing-values/ · fetched 2026-10-06 · at source.
- Verbatim: "For various reasons survey responses may not have a valid code or value. The missing value codes asigned [sic] to these data are described below." · -1 "Don't know" · -2 "Refused" · -7 "Proxy" — "Sometimes when a person cannot participate in the interview, someone else in the household (generally their spouse or partner or adult children) answers questions on their behalf, that is, by proxy." (continues: the question was not in the proxy questionnaire) · -8 "Valid skip" — "This information is missing because the person was never asked this question as they were not eligible for it." · -9 "Missing by error or implausible" · -10 "Not available for the IEMBS" — "Some questions were only asked in the W6 questionnaire for non-IEMBS and so individuals in IEMBS will have missing information for these variables." · -11 "Only available for the IEMBS" · -20 "No data from the BHPS W1-18" · -21 "No data from the UKHLS". All missing codes are negative so they can never collide with a valid answer.
- Establishes: a single UK survey distinguishes nine kinds of nothing — and splits the studio's "unknown" into don't-know (-1) vs refused (-2), and "not collected" into never-asked-ineligible (-8), asked-of-a-proxy (-7), and not-in-this-sample (-10/-11/-20/-21). Strength: high. LOAD-BEARING.
### 7b. Unit vs item nonresponse: NCES Standard 4-4 "Nonresponse Bias Analysis", https://nces.ed.gov/statprog/2002/std4_4.asp · fetched 2026-10-06 — purpose verbatim: "To identify the existence of potential bias due to unit and item nonresponse." The page uses but does not define the terms; NCES 4-1 defines item nonresponse (fetcher paraphrase: missing responses to individual items within records). Treat as SUPPORTING; the Schafer & Graham / Hand quotes above ("nonresponse is a source of difficulty") carry the concept.

---

## 8. Free (price of nothing) as a measurement category

### 8a. ONS, "Special case aggregates in consumer prices" (methodology; last revised 25 March 2026), section on services previously provided free
- URL read: https://www.ons.gov.uk/economy/inflationandpriceindices/methodologies/specialcaseaggregatesinconsumerprices · fetched 2026-10-06 · at source.
- Verbatim: "Some services that were previously provided free at the point of provision have become chargeable. For example, the introduction of university fees in 1998 and the London congestion charge in 2003. This creates two problems when calculating indices: there is no weight in the base period (expenditure is zero); there is no base period price with which to compare the new price to create a price relative. The solution is to use a variation on the Laspeyres formula which uses quantities and price levels (rather than expenditure weights and price relatives). We treat the new product as if it were already included in an existing item index with zero price but with non-zero quantity equal to its consumption in the base period."
- Establishes: the national statistician's formal position that free is a *price of zero attached to a real, non-zero quantity* — a value, not an absence; the arithmetic breaks (no relative, no weight) but the thing was consumed. This is the single best line for the studio's "free" category. Strength: high. LOAD-BEARING.
### 8b. Brynjolfsson, Collis, Diewert, Eggers & Fox (2019) "GDP-B: Accounting for the Value of New and Free Goods in the Digital Economy", NBER WP 25695, March 2019, https://www.nber.org/papers/w25695 · fetched 2026-10-06 · ABSTRACT-ONLY. Verbatim: "The welfare contributions of the digital economy, characterized by the proliferation of new and free goods, are not well-measured in our current national accounts." · "including the welfare gains from Facebook would have added between 0.05 and 0.11 percentage points to GDP-B growth per year in the US." Establishes: in GDP a free good contributes zero *by construction*, which is why economists propose a separate measure — free is a measurement category with its own problem, not a gap. COLOUR.
### 8c. Ticketing ("a £0 ticket is a sale"): no authoritative at-source statement found in the time available (vendor help pages were not reachable through search). Treat as the studio's own observation; it is consistent with 8a (zero price, non-zero quantity).

---

## 9. Disclosure as a kind of nothing (brief)

### 9a. Analysis Function, "An introduction to Statistical Disclosure Control (SDC)" (page dated 19 August 2026), https://analysisfunction.civilservice.gov.uk/policy-store/an-introduction-to-sdc/ · fetched 2026-10-06 · at source. Verbatim: "The suppression of unsafe cells is known as 'primary suppression'." · after primary suppression "other cells must also be suppressed to prevent the values of the unsafe cells being calculated by subtraction from the marginal totals." (secondary suppression) · suppressed values are shown by "replacing the value within the cells with a 'c' or some other symbol." · differencing risk where one table uses "0 to 4" and "5 to 9" and another "0 to 5" and "6 to 10". Together with 4a ([c] "These data points must be replaced with this shorthand") this is the display convention: a suppressed cell is marked, never blanked. Strength: high. LOAD-BEARING for §9.
### 9b. SDMX: Q "Missing value; suppressed" + CL_CONF_STATUS (4c, 4d) — the standard codes *that* and *why* separately, including secondary suppression (D, S).
### 9c. ONS, "Protecting personal data in Census 2021 results" (released 9 March 2023), https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/methodologies/protectingpersonaldataincensus2021results · fetched 2026-10-06 · at source. Verbatim: targeted record swapping — "Households and their individuals that are unique or rare on one or more of those characteristics are highlighted as 'risky records', and all these households would be swapped." · cell key perturbation — "The post-tabular method is based on an algorithm that applies a pre-defined level of perturbation to cells in each dataset." · "Data perturbation is a technique that adds 'noise' to datasets to allow individual record confidentiality." · "Where there is a cell count of one in a published output, there is a high chance that it could be a swapped record, a perturbed count or an imputed record, or a combination of these." · "Where two or more different datasets are constructed, the totals of all cells may in turn be different...the differences should be small and so should not change the conclusions of any analysis or research." Establishes: Census 2021 chose to publish *every* cell with a slightly-wrong number rather than blank some — i.e. it traded the suppressed kind of nothing for a universal, undeclared [e]; small counts including ones are not to be read literally and totals need not add. One paragraph as requested. Strength: high. SUPPORTING.

---

## THREADS PULLED (not asked for)
1. **SDMX "H Missing value; holiday or weekend"** — an official code for the calendar gap that dashboards habitually render as a Monday dip or a zero. Also **"K Data included in another category"**: the nothing that is actually hiding inside another cell (with a mandatory matching "W" on the host cell) — a kind the studio's six does not name.
2. **CDC NNDSS legend** (4g) — six codes, including "NP Nationally notifiable but not published" and "NC Not calculated — insufficient data", and a dash that means "did not submit any cases", explicitly not zero.
3. **Darwen's decomposition** (3c) — the relational-theory cure for NULL is to split one table into EARNS / SALARY_UNK / UNSALARIED, i.e. one table per kind of nothing. The studio's six-kinds scheme is the display-layer twin of this 1990s database argument.
4. **"Not applicable" vs "not collected"** — every official scheme splits these (AF [z] vs [x]; SDMX M vs L; Codd I-mark vs A-mark; survey -8 valid skip vs -9 error; CDC N vs U; Eurostat "-" vs ":"). The studio's "not collected" currently spans both.
5. **"No to NA"** appears independently in the UK (AF: ambiguous between Not Applicable and Not Available) and Eurostat ("Never use NA or ND") and R (the NA of character type "is distinct from the string 'NA'"). Three unrelated authorities converge on banning the two letters most dashboards print.
6. **Census 2021's perturbation** means the whole table is quietly [e] — the opposite trade-off to suppression, and a case for the book's "estimated" display state.
7. **Who estimated?** SDMX E vs I and Eurostat e vs s both encode the *author* of an estimate, which no dashboard I know of shows.
8. **ABS 2005 "n.y.a. not yet available"** — temporal unavailability ("will exist, not yet") as a distinct kind, relevant to lagged series (5f).

## LEFT OUT and why
- Little & Rubin, *Statistical Analysis with Missing Data*: no open chapter located; replaced by the NRC 2010 report chaired by Little (1d) and Schafer & Graham (1b), which together carry the same definitions with page numbers.
- Codd 1979 (TODS) and RM/V2 (1990): not reachable at source (ACM 403; book closed). 1986 SIGMOD Record paper (3a) is at source and carries the A-mark/I-mark distinction in Codd's own words; the IJCAI paper (3b) documents, with citation, that Codd later considered 4VL.
- Date, "Why Three- and Four-Valued Logic Don't Work": not open; Darwen 2012 slides and the IJCAI paper's citation of Date & Darwen 1996 / Date 2005 stand in.
- Peugh & Enders 2004 / Wood, White & Thompson 2004 prevalence reviews: not fetched; Bell 2014 (1e) is open and sufficient for one figure.
- COVID Tracking Project null-vs-zero: no crisp rule found on their FAQ/definitions pages — not worth a weak citation.
- The Excel-row-limit detail in the PHE story: not in the at-source statement; omitted per rules.
- Imperial College news piece on Hand: no direct quotes; journalist paraphrase only.
- Ticketing-vendor "free ticket is an order" statements: not found at source.
- Wikipedia pages on Null (SQL), Missing data: not at source.

## RICH REFERENCES (max three)
1. **SDMX CL_OBS_STATUS 2.2 + CL_CONF_STATUS 1.4** (registry.sdmx.org JSON) — the most finely-grained official vocabulary of nothing; five missing-value reasons, the rounded-zero code, the sender/receiver imputation split, and a separate list for why something was withheld. The author can build the whole mapping table from these two lists.
2. **UK Analysis Function pair** — "Using symbols and shorthand in tables" (11 Jan 2022) with "Releasing statistics in spreadsheets" (30 Jun 2021, "Cells with no data") and "Data visualisation: charts" (19 May 2022, "Breaks in time series"). Together: the codes, the blank-cell rule ("only one reason… explaining… why"), and the only official rule for drawing a gap ("do not join the points… Joining points implies we know something about the data").
3. **Codd 1986, SIGMOD Record 15(4)** — the primary source for two kinds of null, "marks" not values, and the explicit rejection of zero as a missing-marker; read alongside PostgreSQL's docs for what SQL actually does with its single NULL.

## WHAT SURPRISED ME
- The UK rule is subtler than "never leave a cell blank": a blank is permitted if and only if there is *exactly one* reason for blanks in that table and it is stated above the table. More than one kind of nothing forces a label on every nothing. That is the studio's thesis as an accessibility regulation.
- Codd, in 1986, used almost the studio's language — "I consider the number zero to be far too valuable in its normal role … to be reserved … for denoting a missing numeric db-value" — and the database world then standardised on one NULL anyway ("There is effectively only one null value", SQL-92 §4.1).
- The Analysis Function has no "[i] imputed" code; imputation hides inside [e] estimated. SDMX, by contrast, has E and I and defines them by *who* did the estimating.
- The dash in US disease surveillance means "the jurisdiction did not submit any cases", not zero — the ambiguity the studio worries about is a formal category in the CDC's own legend.
- The CPI treats a free service as "zero price but with non-zero quantity" — the national statistician already says, in method, that free is a value with a quantity behind it.
- "NA" is banned by the UK, Eurostat and (in effect) R for the same reason: nobody can tell whether it means not applicable or not available.
- Census 2021 did not suppress; it perturbed everything, so a published "1" may be swapped, perturbed or imputed — a table with no blanks and no literal small numbers.

---

## Agent C — Grain, denominator, aggregation and digital-trace data

RESEARCH REPORT — Facet: grain, denominator, aggregation and the long tail; digital-trace, transactional and administrative data as evidence.
All fetches made 2026-10-06. "At source" = the paper/standard itself or an author/institutional copy. Quotations are as returned by the fetch tool from the named page (the tool occasionally elides with "..."); I have not altered wording. Where a page could not be read I say so and do not invent content.

PAGES I COULD NOT READ (and why): Europe PMC REST API and Crossref API and Semantic Scholar API (proxy rate-limited, HTTP 429); PubMed (429); Wiley JHM article page and Science.org article pages (403); ScienceDirect article pages (robots.txt); HBR full text (paywall; only intro served); OECD income-inequality indicator page (served only header/navigation); King's Harvard PDF and DASH PDF of Lazer et al. (robots.txt), davidlazer.com (expired certificate); wired.com (site blocked); JSTOR (JavaScript wall); LWW Critical Care Medicine abstract (402).

=====================================================================
1. GRAIN — THE UNIT OF OBSERVATION
=====================================================================

1.1 Wickham, H. (2014). "Tidy Data." Journal of Statistical Software 59(10).
URL read: https://vita.had.co.nz/papers/tidy-data.pdf (author's copy) · fetched 2026-10-06 · AT SOURCE.
Exact quotations:
- Abstract: "Tidy datasets are easy to manipulate, model and visualise, and have a specific structure: each variable is a column, each observation is a row, and each type of observational unit is a table."
- §2.2 Data semantics: "A variable contains all values that measure the same underlying attribute (like height, temperature, duration) across units." / "An observation contains all values measured on the same unit (like a person, or a day, or a race) across attributes."
- §2.3 Tidy data: "In tidy data: 1. Each variable forms a column. 2. Each observation forms a row. 3. Each type of observational unit forms a table."
- On the slipperiness of "observation": "For a given dataset, it's usually easy to figure out what are observations and what are variables, but it is surprisingly difficult to precisely define variables and observations in general."
What it establishes: the row of a table IS the grain; the unit ("a person, or a day, or a race") is a choice, and the definition of an observation is context-dependent even for the author of the canonical paper.
Strength: strong (primary, canonical, author copy). Role: LOAD-BEARING.

1.2 Eurostat Statistics Explained glossary — "Statistical unit", "Observation unit", "Reporting unit", "Enterprise".
URLs read: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Statistical_unit ; ...Glossary:Observation_unit ; ...Glossary:Reporting_unit ; ...Glossary:Enterprise · fetched 2026-10-06 · AT SOURCE.
Exact quotations:
- Statistical unit: "The statistical unit is the entity for which the required statistics are compiled. It may be an observation unit in which information is received and statistics are compiled or an analytical unit, which statisticians create by splitting or combining observation units with the help of estimations or imputations in order to supply more detailed and/or homogeneous data than would otherwise be possible." The page lists four statistical units used in European business statistics: Enterprise; Kind-of-activity unit; Local kind-of-activity unit; Local unit (enterprise group used for register purposes).
- Observation unit: "the entity on which information is received and statistics are compiled in the process of collecting statistical data".
- Reporting unit: "The reporting unit is the entity from which the recommended data items are collected." (Page notes it varies by sector, country, institutional structures, legal frameworks, traditions, priorities and survey resources.)
- Enterprise: "An enterprise is an organisational unit producing goods or services which has a certain degree of autonomy in decision-making." / "An enterprise may consist out of one or more legal units."
What it establishes: official statistics distinguishes three things a dashboard usually conflates — who sends the data (reporting unit), what the data is about (observation unit), and what the statistic is compiled for (statistical/analytical unit).
Strength: strong (official glossary). Role: LOAD-BEARING.

1.3 Council Regulation (EEC) No 696/93 of 15 March 1993 on the statistical units for the observation and analysis of the production system in the Community. Annex, Section III.
URL read: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:31993R0696 · fetched 2026-10-06 · AT SOURCE.
Exact quotations (Annex III):
- A. Enterprise: "The smallest combination of legal units that is an organizational unit producing goods or services, which benefits from a certain degree of autonomy in decision-making, especially for the allocation of its current resources."
- B. Institutional unit: "An elementary economic decision-making centre characterized by uniformity of behaviour and decision-making autonomy in the exercise of its principal function."
- C. Enterprise group: "An association of enterprises bound together by legal and/or financial links. A group of enterprises can have more than one decision-making centre, especially for policy on production, sales and profits."
- D. Kind-of-activity unit: "Groups all the parts of an enterprise contributing to the performance of an activity at class level (four digits) of NACE Rev. 1 and corresponds to one or more operational subdivisions."
- E. Unit of homogeneous production: "Characterized by a single activity which is identified by its homogeneous inputs, production process and outputs."
- F. Local unit: "An enterprise or part thereof (e.g. a workshop, factory, warehouse, office, mine or depot) situated in a geographically identified place."
- G. Local kind-of-activity unit: "The part of a KAU which corresponds to a local unit."
- Preamble: "Only if the Member States use common definitions of statistical units will it be possible to provide integrated statistical information with the reliability, speed, flexibility and degree of detail required for the management of the internal market."
What it establishes: a "business" is at least seven different countable things in law; a count of "venues" or "firms" has a different value under each. Strength: strong (legal text). Role: LOAD-BEARING (for the enterprise/local-unit/group distinction).

1.4 Bhattacherjee, A. Social Science Research: Principles, Methods, and Practices (open textbook), §2.1 "Unit of Analysis".
URL read: https://socialsci.libretexts.org/Bookshelves/Social_Work_and_Human_Services/Social_Science_Research_-_Principles_Methods_and_Practices_(Bhattacherjee)/02%3A_Thinking_Like_a_Researcher/2.01%3A_Unit_of_Analysis · fetched 2026-10-06 · AT SOURCE (open textbook, LibreTexts edition).
Exact quotations: "The unit of analysis refers to the person, collective, or object that is the target of the investigation." It "shapes what type of data you should collect for your study and who you collect it from." The text notes the unit of analysis and the unit of data collection can differ (e.g. survey individual team members, aggregate to organisation-level findings).
What it establishes: unit of analysis is a decision made early, and it can differ from the unit the data were collected at — the bridge to the ecological-fallacy chapter (cross-reference only; not pursued).
Strength: moderate (textbook, standard statement). Role: SUPPORTING.

=====================================================================
2. GRAIN IN TIME
=====================================================================

2.1 Eurostat glossary — "Reference period".
URL read: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Reference_period · fetched 2026-10-06 · AT SOURCE.
Exact quotations: "A reference period is the time period for which statistical results are collected or calculated and to which, as a result, these values refer." / "The reference period should be distinguished from the publication time, the period or point in time at which the statistical data are published." / "The publication year of statistical results may be significantly later than the reference year for which they were collected." Page notes reference periods may be calendar years, fiscal years, semesters, quarters, months or days, and that for stock variables (population) a reference time point (e.g. 1 January) applies.
Strength: strong. Role: LOAD-BEARING for "a number refers to a period; the period is a choice".

2.2 GSS (UK Government Statistical Service) harmonised principle — "Survey reference period", Version 5.6, June 2017.
URL read: https://gss.civilservice.gov.uk/wp-content/uploads/2019/04/Survey-Reference-Period-June-17.pdf (landing page: https://gss.civilservice.gov.uk/policy-store/survey-reference-period) · fetched 2026-10-06 · AT SOURCE.
Exact quotations: "Most regular or continuous Government social surveys use financial year as the reference period." The document states there is "a significant need for annual figures on a common time basis" and acknowledges "cost and methodological considerations" in publishing on multiple bases.
Caveat: this GSS document does NOT give a formal definition of "reference period" — it is about harmonising the annual (financial-year) basis. Use Eurostat (2.1) for the definition and this for the UK harmonisation practice.
Strength: moderate. Role: SUPPORTING.

2.3 The hospital midnight census — three sources.
(a) NHS England, "Bed Availability and Occupancy Quarterly Return Definitions (KH03)", June 2020. URL read: https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2020/06/KH03-Guidance-June-2020-FINAL.pdf · AT SOURCE. Quotation: for overnight wards "an occupied bed day is defined as a bed which is occupied at midnight on the day in question." For day-only wards: "an occupied bed day is defined as a bed in which the treatment or care of at least one patient has taken place during the day." / "If more than one patient has occupied a bed during the same day this should be reported as only one bed day, therefore occupancy rates should not exceed 100%."
(b) NHS Data Dictionary (archive, May 2015 release), "Bed days in wards open overnight (occupied)". URL read: https://archive.datadictionary.nhs.uk/DD%20Release%20May%202015/data_dictionary/data_field_notes/b/be/bed_days_in_wards_open_overnight_(occupied)_de.asp@shownav=0.html · AT SOURCE. Quotation: "For wards open overnight, an occupied bed day is one which is occupied at midnight on the day in question."
(c) Pierce, L. et al. (2024). "Finding the time: Hourly variation in average daily census on a hospital medicine service." Journal of Hospital Medicine, doi:10.1002/jhm.13233. Wiley page returned 403; read via Maguire, P., "When should you measure hospital census?", Today's Hospitalist, January 2024, https://todayshospitalist.com/midnight-census/ · SECONDARY. Quotation of the study's conclusion as reproduced there: "Measuring ADC at midnight, as traditionally done, may underestimate workload and therefore contribute to staffing shortages and physician burnout." Figures reported: census peaked at 11 a.m.; delta of 9.1 patients between peak (11 a.m.) and trough (7 p.m.), about 5.5% of peak; at UCSF "a consistent delta of about five or six patients" between midnight and 7 a.m. A second trade piece (Thomas, J., The Hospitalist, 15 Aug 2024, https://www.the-hospitalist.org/hospitalist/article/37623/practice-management/finding-the-time-to-optimize-hospitalist-workflow/) confirms "In the Brief Report, ADC generally peaked around 11:00 AM." A companion JHM editorial exists: Calderon et al. 2024, "Time to move past midnight census", doi:10.1002/jhm.13267 (not read).
(d) Simon, M., Yankovskyy, E., Klaus, S., Gajewski, B., Dunton, N. (2011). "Midnight census revisited: Reliability of patient day measurements in US hospital units." International Journal of Nursing Studies 48(1):56–61. URL read: https://eprints.soton.ac.uk/186187/ (institutional repository record) · ABSTRACT-ONLY. Quotations: "Overall agreement between routine data and the quasi-gold standard was excellent (ICC [95% CI]: 0.967 [0.958–0.974])"; a Bayesian analysis found two of five accepted patient-day methods systematically underestimated patient days; "an interaction between the degrees of short stay patients and one of the data collection methods also affected patient day measurement by up to 7.6%."
What it establishes: the official UK definition of an occupied bed is a midnight snapshot (a); a peer-reviewed US study finds the midnight count is the trough of the day and understates daytime load (c); the size of the error depends on the mix of short-stay patients (d). Together: the boundary of the day is a measurement rule, and the rule changes the count.
Strength: (a),(b) strong; (c) moderate — figures via trade press, not the paper; (d) abstract-level. Role: (a)+(c) LOAD-BEARING as the worked example; (d) SUPPORTING.

2.4 Trade date / settlement date (T+1).
FINRA, "Understanding Settlement Cycles" (page dated 7 May 2026). URL read: https://www.finra.org/investors/insights/understanding-settlement-cycles · AT SOURCE. Quotations: trade date is "the day your order to buy or sell a security is executed"; settlement date is "the day your order is finalized and on which funds and the securities must be delivered"; "most securities transactions settle on the next business day following their transaction date" (T+1, effective May 2024).
SEC legacy investor publication "T+3" (historic). URL read: https://www.sec.gov/investor/pubs/tplus3.htm · AT SOURCE. Quotation: "Generally, those days when the stock exchanges are open are considered business days." (Example: Friday purchase counts from Monday.)
What it establishes: one transaction has at least two legitimate dates; "when did it happen" is a convention, and "day" means business day, not calendar day. Strength: strong. Role: SUPPORTING.

2.5 GOV.UK open standard — "Date-times and time stamps standard" (Open Standards for Government; page updated 29 January 2026).
URL read: https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard · AT SOURCE. Quotations: "Use ISO 8601:2004 to represent dates and times in a machine-readable format in government systems." / use it in "APIs, data for transferring between systems, date sorting, for example at the start of filenames". / "List date and time elements in descending order of size (years, months, days, hours, minutes, seconds, milliseconds and microseconds)." / Time zones: "You can add a Coordinated Universal Time (UTC) offset. For example, 2017-05-16T10:30:56+01:00 is 16 May 2017 10:30 and 56 seconds with an offset showing British summer time (BST), one hour ahead of UTC."
Note: the lexical-sort = chronological-sort property is stated on the page only as the reason for "date sorting ... at the start of filenames"; the exact phrase "lexical sort" does not appear. Strength: strong. Role: SUPPORTING.

=====================================================================
3. DENOMINATOR
=====================================================================

3.1 Tufte, E. R. (1997). Visual Explanations, ch. 2 "Visual and Statistical Thinking: Displays of Evidence for Making Decisions" (Snow's cholera map; Challenger).
URL read: https://library.stlawu.edu/system/files/2021-02/tufte-visual-and-statistical.pdf (St Lawrence University library copy of the chapter) · AT SOURCE (library copy).
Exact quotations: p.35, on Snow's dot map: "an area of the map may be free of cases merely because it is not populated." and the recurring Tufte question "Compared with what?". The fetch tool also returned, as Tufte's words on p.35, that "dot maps fail to take into account the number of people living in an area and at risk to get a disease" (treat as near-verbatim; verify against the page before quoting in print). Challenger, p.43: "Missing are 92 % of the temperature data, for 5 of the launches with erosion and 17 launches without erosion." p.53 lists the principles: documenting data sources and characteristics; enforcing appropriate comparisons; demonstrating cause-and-effect mechanisms; expressing mechanisms quantitatively; recognising multivariate problems; inspecting alternative explanations — displays should be "documentary, comparative, causal and explanatory, quantified, multivariate, exploratory."
What it establishes: Tufte's denominator point is made through Snow (deaths need population at risk) and Challenger (the omitted launches were the denominator of the comparison). Strength: strong on text; moderate on the one sentence flagged. Role: SUPPORTING (colourful anchor for "compared with what").

3.2 CDC, Principles of Epidemiology in Public Health Practice, 3rd ed., Lesson 3, Sections 1–2.
URLs read: https://archive.cdc.gov/www_cdc_gov/csels/dsepd/ss1978/lesson3/section1.html ; .../section2.html · AT SOURCE.
Exact quotations: "A ratio is the relative magnitude of two quantities or a comparison of any two values." / "A proportion is the comparison of a part to the whole. It is a type of ratio in which the numerator is included in the denominator." / "In epidemiology, a rate is a measure of the frequency with which an event occurs in a defined population over a specified period of time." / "Because rates put disease frequency in the perspective of the size of the population, rates are particularly useful for comparing disease frequency in different locations, at different times, or among different groups of persons with potentially different sized populations; that is, a rate is a measure of risk." All three share the form numerator ÷ denominator × 10^n. Section 2: "Incidence proportion is the proportion of an initially disease-free population that develops disease, becomes injured, or dies during a specified (usually limited) period of time." (denominator: "Size of population at start of period"). "Incidence rate or person-time rate is a measure of incidence that incorporates time directly into the denominator." The denominator is "the sum of the time each person was observed, totaled for all persons. This denominator represents the total time the population was at risk of and being watched for disease."
What it establishes: the vocabulary — ratio, proportion, rate, population at risk, person-time — and the reason a rate exists (comparison across different-sized populations). Strength: strong. Role: LOAD-BEARING.

3.3 Hájek, A. (2007). "The reference class problem is your problem too." Synthese 156:563–585.
URL read: https://link.springer.com/article/10.1007/s11229-006-9138-5 · ABSTRACT-ONLY.
Exact quotation (abstract): "The reference class problem arises when we want to assign a probability to a proposition (or sentence, or event) X, which may be classified in various ways, yet its probability can change depending on how it is classified." (Reichenbach, The Theory of Probability, 1949, is in the references; no Reichenbach quote obtained.)
What it establishes: the denominator problem has a philosophical name — every rate depends on which class you put the case in. Strength: moderate (abstract). Role: SUPPORTING.

3.4 Like-for-like sales (practice).
Moneyterms, "Like-for-like" (UK finance glossary). URL read: https://moneyterms.co.uk/lfl/ · SECONDARY (practitioner glossary; no standards body defines LFL — it is an "alternative performance measure" defined by each company). Quotation: like-for-like growth is "growth after to the stripping out of the effects of expansion and shop closures" [sic], calculated by "measuring the increase or decrease at stores that have been open for at least two years". (A Retail Think Tank white paper questioning LFL's usefulness exists but could not be fetched: https://www.retailthinktank.co.uk/whitepaper/are-like-for-like-sales-figures-still-a-useful-and-relevant-measure-of-retail-performance/ .)
What it establishes: finance's own habit of changing the denominator (per-store, constant estate) to make a total comparable. Strength: weak-moderate (glossary). Role: COLOUR.

3.5 Denominator neglect — one line only, as instructed: not researched (overlaps another chapter). Note that Meng (5.1) and boyd & Crawford (5.5) each supply a "size of numerator is meaningless without the frame" sentence that can stand in.

=====================================================================
4. WHY AGGREGATION HIDES THE SMALL — DISTRIBUTIONS AND CONCENTRATION
=====================================================================

4.1 Lorenz, M. O. (1905). "Methods of Measuring the Concentration of Wealth." Publications of the American Statistical Association 9(70):209–219.
URL read: https://archive.org/stream/jstor-2276207/2276207_djvu.txt (Internet Archive JSTOR early-journal-content copy) · AT SOURCE (OCR text).
Exact quotations: p.217: "Plot along one axis cumulated per cents of the population from poorest to richest, and along the other the per cent of the total wealth held by these per cents of the population." (equal distribution) "This will give a straight line. With an unequal distribution, the curves will always begin and end in the same points as with an equal distribution, but they will be bent in the middle; and the rule of interpretation will be, as the bow is bent, concentration increases." p.213 (on averages): "But that average income is no safe criterion is shown by the hypothetical case just presented, where the average income of the highest class shows a marked increase, although there was no change in the degree of concentration."
What it establishes: the curve's definition in the original words, plus an 1905 warning that averages do not reveal concentration. Strength: strong. Role: LOAD-BEARING.

4.2 Gini index — World Bank, World Development Indicators metadata, SI.POV.GINI.
URL read: https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SI.POV.GINI · AT SOURCE.
Exact quotations: "Gini index measures the extent to which the distribution of income (or, in some cases, consumption expenditure) among individuals or households within an economy deviates from a perfectly equal distribution." A Lorenz curve "plots the cumulative percentages of total income received against the cumulative number of recipients, starting with the poorest individual or household." The index "measures the area between the Lorenz curve and a hypothetical line of absolute equality, expressed as a percentage of the maximum area under the line." "a Gini index of 0 represents perfect equality, while an index of 100 implies perfect inequality." Statistical concept: "The Gini index is the average of all pairwise absolute differences between individual consumption or income, normalized by twice the mean" — i.e. "the average share of mean consumption or income that needs to be transferred between two randomly selected individuals to achieve equality."
Strength: strong. Role: LOAD-BEARING.

4.3 Herfindahl–Hirschman Index — US Department of Justice, Antitrust Division, "Herfindahl-Hirschman Index" (page updated 17 January 2024).
URL read: https://www.justice.gov/atr/herfindahl-hirschman-index · AT SOURCE.
Exact quotations: "The HHI is calculated by squaring the market share of each firm competing in the market and then summing the resulting numbers." / "For a market consisting of four firms with shares of 30, 30, 20, and 20 percent, the HHI is 2,600 (30² + 30² + 20² + 20² = 2,600)." / The HHI "approaches zero when a market is occupied by a large number of firms of relatively equal size and reaches its maximum of 10,000 points when a market is controlled by a single firm." / Under the 2023 Merger Guidelines: moderately concentrated = "markets in which the HHI is between 1,000 and 1,800 points"; highly concentrated = "markets in which the HHI is in excess of 1,800 points"; "Transactions that increase the HHI by more than 100 points in highly concentrated markets are presumed likely to enhance market power."
Strength: strong. Role: LOAD-BEARING (the squaring is the "big players count more than proportionally" idea in one formula).

4.4 Top-share measure — World Bank WDI metadata, SI.DST.10TH.10 "Income share held by highest 10%".
URL read: https://databank.worldbank.org/metadataglossary/world-development-indicators/series/SI.DST.10TH.10 · AT SOURCE.
Exact quotations: "Percentage share of income or consumption is the share that accrues to subgroups of population indicated by deciles or quintiles." It is "the percentage of total income in a population that is held by the tenth or top decile, meaning the top 10% of people when ranked from lowest to highest income."
(WID.world methodology page fetched — https://wid.world/methodology/ — but no standalone definition served; OECD income-inequality page served no content.) Strength: strong for the simple definition. Role: SUPPORTING.

4.5 Pareto principle — Juran's attribution and mea culpa.
(a) Juran, J. M. (1975). "The Non-Pareto Principle; Mea Culpa." Quality Progress, May 1975. Read via a blog reproduction: https://se-gestiona.radical-management.com/2013/07/the-non-pareto-principle-mea-culpa.html?m=0 · SECONDARY. Quotations as reproduced: "On subsequent challenge, I was forced to confess that I had mistakenly applied the wrong name to the principle." / "To my knowledge, the first exposition was by myself" (of the principle as universal across fields). The cumulative curves in his Quality Control Handbook should have been "properly identified with Lorenz". Phrase: "vital few and trivial many".
(b) Juran Institute, "A Guide to the Pareto Principle (80/20 Rule)", 12 March 2019 (updated 7 March 2024). URL read: https://www.juran.com/blog/a-guide-to-the-pareto-principle-80-20-rule-pareto-analysis/ · AT SOURCE (institutional). Quotations: "The Pareto Principle gets its name from the Italian-born economist Vilfredo Pareto (1848-1923), who observed that a relative few people held the majority of the wealth (20%) – back in 1895." / "Juran has also coined the terms 'vital few' and 'useful many' or 'trivial many' to refer to those few contributions, which account for the bulk of the effect and to those many others which account for a smaller proportion of the effect." / "the mathematician M.O. Lorenz developed graphs to illustrate it".
What it establishes: "80/20" is Juran's generalisation of an empirical pattern, misnamed by his own admission; the graph behind it is Lorenz's. Neither source states 80/20 as a law — a "critical source" saying explicitly it is not a law was not found at source; Juran's own framing ("universal" empirical observation) is the honest basis. Strength: (a) moderate (secondary copy of primary); (b) strong. Role: SUPPORTING.

4.6 Mean vs median in skewed distributions — two statistics-office/standards sources.
(a) ONS, "Guide to interpreting Annual Survey of Hours and Earnings (ASHE) estimates", 26 October 2017, section 4 "Why is the median used as the main measure of earnings?" URL read: https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/methodologies/guidetointerpretingannualsurveyofhoursandearningsasheestimates · AT SOURCE. Quotations: "the distribution of earnings is skewed, with more people earning lower salaries than higher salaries"; the mean is "highly influenced by those values at the upper end of the distribution".
(b) NIST/SEMATECH e-Handbook of Statistical Methods, §1.3.5.1 "Measures of Location" (Robustness). URL read: https://www.itl.nist.gov/div898/handbook/eda/section3/eda351.htm · AT SOURCE. Quotation: "Extreme values in the tails distort the mean. However, these extreme values do not distort the median since the median is based on ranks."
Strength: strong. Role: LOAD-BEARING for §7 as well (sensitivity of the total/mean to the largest contributors).

4.7 Rosen, S. (1981). "The Economics of Superstars." American Economic Review 71(5):845–858.
URL read: https://pdodds.w3.uvm.edu/files/papers/others/1981/rosen1981a.pdf (scan of the AER article hosted by P. S. Dodds, Univ. of Vermont) · AT SOURCE (third-party scholar's host). JSTOR page unreadable.
Exact quotations: "The phenomenon of Superstars, wherein relatively small numbers of people earn enormous amounts of money and dominate the activities in which they engage, seems to be increasingly important in the modern world... In certain kinds of economic activity there is concentration of output among a few individuals, marked skewness in the associated distributions of income and very large rewards at the top." / "Lesser talent often is a poor substitute for greater talent. The worse it is the larger the sustainable rent accruing to higher quality sellers because demand for the better sellers increases more than proportionately." / "A performer or an author must put out more or less the same effort whether 10 or 1,000 people show up in the audience or buy the book."
What it establishes: the two mechanisms (imperfect substitution; joint-consumption technology) that generate right-skew in cultural markets. Strength: strong. Role: LOAD-BEARING.

4.8 Salganik, M. J., Dodds, P. S., Watts, D. J. (2006). "Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market." Science 311(5762):854–856.
URL read: https://pdodds.w3.uvm.edu/research/papers/years/2006/salganik2006a.pdf (co-author's copy; landing page https://pdodds.w3.uvm.edu/research/papers/salganik2006a/) · AT SOURCE.
Exact quotations — Abstract in full: "Hit songs, books, and movies are many times more successful than average, suggesting that ''the best'' alternatives are qualitatively different from ''the rest''; yet experts routinely fail to predict which products will succeed. We investigated this paradox experimentally, by creating an artificial ''music market'' in which 14,341 participants downloaded previously unknown songs either with or without knowledge of previous participants' choices. Increasing the strength of social influence increased both inequality and unpredictability of success. Success was also only partly determined by quality: The best songs rarely did poorly, and the worst rarely did well, but any other result was possible." Main text: "Success inequality is defined by the Gini coefficient" / "In both experiments, we found that all eight social influence worlds (dark bars) exhibit greater inequality" / "Social influence also generates increased unpredictability of outcomes" / "In general, the ''best'' songs never do very badly, and the ''worst'' songs never do extremely well".
What it establishes: concentration in cultural markets is partly produced by the feedback of visible popularity, not only by quality — and they measured it with the Gini (ties 4.2 to 4.8). Strength: strong. Role: LOAD-BEARING.

4.9 Anderson, C. (2004/2006). "The Long Tail" (Wired, Oct 2004; book 2006).
wired.com is blocked from this environment; NOT READ AT SOURCE. Do not quote from me. The claim (aggregate demand for non-hits can rival hits once shelf space is unlimited) should be quoted by the author from the book or the Wired piece directly. Role: COLOUR (the thesis Elberse tests).

4.10 Elberse, A. (2008). "Should You Invest in the Long Tail?" Harvard Business Review, July–August 2008.
HBR page (https://hbr.org/2008/07/should-you-invest-in-the-long-tail) served only the intro/paywall summary ("Blockbusters are capturing even more of the market than they used to, and consumers in the tail don't really like niche products much"). Full text read from a reprint PDF: https://geminisufscar.wordpress.com/wp-content/uploads/2009/05/shouldyouinvestinthelongtail.pdf · SECONDARY (reprint copy; figures consistent with HBR's own summary and with the July 2008 HBR "Long Tail Debate" exchange).
Exact quotations: (Rhapsody, p.2) "The top 10% of titles accounted for 78% of all plays, and the top 1% of titles for 32% of all plays." (p.3) the tail is "becoming much longer and flatter", with "a rapidly increasing number of titles that sell very rarely or never." (Nielsen SoundScan 2007, p.3) "24% [of 3.9 million digital tracks] sold only one copy, and 91%—3.6 million tracks—sold fewer than 100 copies." (p.3) "The number of titles in the top 10% of weekly sales dropped by more than 50%" (concentration in the head rising). (p.7, advice) "Don't radically alter blockbuster resource-allocation or product-portfolio management strategies. A few winners will still go a long way."
What it establishes: the empirical shape — long, flat tail of near-zeros, with the head concentrating further — in the author's figures. Strength: moderate-strong (reprint, not HBR server). Role: LOAD-BEARING for the "long tail is mostly zeros" point.

4.11 Later streaming-concentration studies (method only; abstracts).
(a) Coelho, M. P., Mendes, J. Z. (2019). "Digital music and the 'death of the long tail'." Journal of Business Research 101:454–460, doi:10.1016/j.jbusres.2019.01.015. URLs read: https://ideas.repec.org/a/eee/jbrese/v101y2019icp454-460.html ; https://researchportal.ulisboa.pt/pt/publications/digital-music-and-the-death-of-the-long-tail/ · ABSTRACT-ONLY. Abstract sentences: "Digital distribution is a new technology that is revolutionizing the pop-rock music market." / "Our research tests the empirical evidence of such effects and elaborates on how the firms respond to this disruptive technological revolution and how this response changes strategic management." The abstract frames a test between long-tail (niche) and superstar (concentration) hypotheses but DOES NOT state the result or the data; the title's scare-quoted "death of the long tail" signals the finding, but I could not confirm figures. Do not cite numbers from it.
(b) Datta, H., Knox, G., Bronnenberg, B. J. (2018). "Changing Their Tune: How Consumers' Adoption of Online Streaming Affects Music Consumption and Discovery." Marketing Science 37(1):5–21. URL read: https://econpapers.repec.org/RePEc:inm:ormksc:v:37:y:2018:i:1:p:5-21 · ABSTRACT-ONLY. Quotations: "adoption of streaming leads to very large increases in the quantity and diversity of consumption in the first months"; "even after half a year, adopters play substantially more, and more diverse, music"; "adoption of streaming increases new music discovery"; "While repeat listening to new music decreases, users' best discoveries have higher play rates"; data: "a unique panel data set of individual consumers' listening histories across many digital music platforms". Method point: individual-level panel (user × track × time grain) — the opposite grain from chart data, and it finds diversification at the user level even where the market total is concentrated.
(c) Aguiar, L., Waldfogel, J. (2021). "Platforms, Power, and Promotion: Evidence from Spotify Playlists." Journal of Industrial Economics 69:653–691. Wiley page 403; author's research page https://www.luis-aguiar.com/research confirms citation but shows no abstract. NOT READ beyond citation. Also Aguiar & Waldfogel, NBER WP 21653 "Streaming Reaches Flood Stage" (https://www.nber.org/system/files/working_papers/w21653/w21653.pdf, AT SOURCE): abstract read in full; headline "137 Spotify streams appear to reduce track sales by 1 unit"; note that their data were limited to "the top 50 songs" in Spotify's public releases — itself a grain/coverage caveat (top-of-chart data say nothing about the tail). No concentration statistic in it.
Strength: (a) weak (abstract silent on result); (b) moderate; (c) citation only. Role: SUPPORTING / COLOUR.

=====================================================================
5. DIGITAL-TRACE AND TRANSACTIONAL DATA AS EVIDENCE
=====================================================================

5.1 Meng, X.-L. (2018). "Statistical paradises and paradoxes in big data (I): Law of large populations, big data paradox, and the 2016 US presidential election." Annals of Applied Statistics 12(2):685–726.
URL read: https://statistics.fas.harvard.edu/file_url/823 (Harvard Statistics department copy) · AT SOURCE. (Project Euclid page served only a firewall stub.)
Exact quotations: Abstract opening: "Statisticians are increasingly posed with thought-provoking and even paradoxical questions, challenging our qualifications for entering the statistical paradises created by Big Data." The three factors: "(1) a data quality measure, ρR,X, the correlation between Xj and the response/recording indicator Rj; (2) a data quantity measure, √(N − n)/n, where N is the population size; and (3) a problem difficulty measure, σX, the standard deviation of X." Data defect correlation: "the data defect correlation ρR,X ... precisely measures both the sign and degree of selection bias caused by the R-mechanism". Headline comparison: with "ρR,X ≈ −0.005 for self-reporting to vote for Donald Trump", "the simple sample proportion of the self-reported voting preference for Trump from 1% of the US eligible voters, that is, n ≈ 2,300,000, has the same mean squared error as the corresponding sample proportion from a genuine simple random sample of size n ≈ 400, a 99.98% reduction of sample size". Law of Large Populations: "Among studies sharing the same (fixed) average data defect correlation ER(ρR,G) ≠ 0, the (stochastic) error of Gn, relative to its benchmark under SRS, grows with the population size N at the rate of √N". Big Data Paradox: "the more the data, the surer we fool ourselves" (note: the paper's wording is "the more the data", not "the bigger the data").
What it establishes: for self-selected/transactional data, error = quality × quantity × difficulty; a tiny correlation between being recorded and the value recorded wipes out almost all of the apparent sample size. Strength: strong. Role: LOAD-BEARING.

5.2 Lazer, D., Kennedy, R., King, G., Vespignani, A. (2014). "The Parable of Google Flu: Traps in Big Data Analysis." Science 343(6176):1203–1205.
Author/institutional PDFs blocked (robots.txt / certificate). DASH record read: https://dash.harvard.edu/handle/1/12016836 · AT SOURCE for the one-line abstract: "Large errors in flu prediction were largely avoidable, which offers lessons for the use of big data." Body-text sentences read from a teaching copy that reproduces the paper's text (University of Nebraska–Lincoln handout, https://cse.unl.edu/~lksoh/Classes/CSCE100_Fall21/handouts/11LectureBigData_GoogleFluTrend.pdf) and a second summary (https://bookdown.org/paul/big-data6/lazer-et-al-2014-the-parable-of-google-flu-traps-in-big-data-analysis.html) · SECONDARY, two independent copies agree:
- "'Big data hubris' is the often implicit assumption that big data are a substitute for, rather than a supplement to, traditional data collection and analysis."
- "Algorithm dynamics are the changes made by engineers to improve the commercial service and by consumers in using that service".
- "Nature reported that GFT was predicting more than double the proportion of doctor visits for influenza-like illness" (than CDC).
- "The core challenge is that most big data that have received popular attention are not the output of instruments designed to produce valid and reliable data amenable for scientific analysis."
- "Quantity of data does not mean that one can ignore foundational issues of measurement and construct validity and reliability".
Strength: strong on content, moderate on provenance (verify against the Science PDF before print). Role: LOAD-BEARING.

5.3 Salganik, M. J. (2018). Bit by Bit: Social Research in the Digital Age, §2.3 "Ten common characteristics of big data" (open edition).
URLs read: https://www.bitbybitbook.com/en/1st-ed/observing-behavior/characteristics/ and the ten subsection pages (.../big/, .../always-on/, .../nonreactive/, .../incomplete/, .../inaccessible/, .../non-representative/, .../drift/, .../algorithmically-confounded/, .../dirty/, .../sensitive/) · AT SOURCE.
Framing: "Big data sources tend to have a number of characteristics in common; some are generally good for social research and some are generally bad." (three good: big, always-on, nonreactive; seven bad: incomplete, inaccessible, nonrepresentative, drifting, algorithmically confounded, dirty, sensitive.)
One defining sentence each (the section's opening summary, verbatim):
1. Big: "Large datasets are a means to an end; they are not an end in themselves."
2. Always-on: "Always-on big data enables the study of unexpected events and real-time measurement."
3. Nonreactive: "Measurement in big data sources is much less likely to change behavior."
4. Incomplete: "No matter how big your big data, it probably doesn't have the information you want." (plus: "Big data tends to be missing three types of information useful for social research: demographic information about participants, behavior on other platforms, and data to operationalize theoretical constructs.")
5. Inaccessible: "Data held by companies and governments are difficult for researchers to access."
6. Nonrepresentative: "Nonrepresentative data are bad for out-of-sample generalizations, but can be quite useful for within-sample comparisons."
7. Drifting: "Population drift, usage drift, and system drift make it hard to use big data sources to study long-term trends." (text: "population drift (change in who is using them), behavioral drift (change in how people are using them), and system drift (change in the system itself)".)
8. Algorithmically confounded: "Behavior in big data systems is not natural; it is driven by the engineering goals of the systems." (example: "Facebook encouraged people with few connections on Facebook to make more friends until they reached 20 friends.")
9. Dirty: "Big data sources can be loaded with junk and spam." (9/11 pager study: "Removing the messages generated by this single automated pager completely eliminates the apparent increase in anger over the course of the day.")
10. Sensitive: "Some of the information that companies and governments have is sensitive."
Strength: strong. Role: LOAD-BEARING (the checklist for any transactional feed on a dashboard).

5.4 Kitchin, R., McArdle, G. (2016). "What makes Big Data, Big Data? Exploring the ontological characteristics of 26 datasets." Big Data & Society 3(1).
URL read: https://journals.sagepub.com/doi/10.1177/2053951716631130 · AT SOURCE (open access).
Exact quotations: Abstract opening: "Big Data has been variously defined in the literature. In the main, definitions suggest that Big Data possess a suite of key traits: volume, velocity and variety (the 3Vs), but also exhaustivity, resolution, indexicality, relationality, extensionality and scalability. However, these definitions lack ontological clarity, with the term acting as an amorphous, catch-all label for a wide selection of data." Seven traits, small vs big: Volume ("Limited to large" vs "Very large"); Velocity ("Slow, freeze-framed/bundled" vs "Fast, continuous"); Variety ("Limited to wide" vs "Wide"); Exhaustivity ("Samples" vs "Entire populations"); Resolution and indexicality ("Coarse and weak to tight and strong" vs "Tight and strong"); Relationality ("Weak to strong" vs "Strong"); Extensionality and scalability ("Low to middling" vs "High"). Conclusion: "It seems to us, based on the datasets that we have examined, that the key boundary characteristics of Big Data, which together differentiate it from small data, are velocity (both frequency of generation, and frequency of handling, recording, and publishing) and exhaustivity."
Strength: strong. Role: SUPPORTING (note "exhaustivity" = n = all — the claim Meng dismantles).

5.5 boyd, d., Crawford, K. (2012). "Critical Questions for Big Data." Information, Communication & Society 15(5):662–679.
URL read: https://www.danah.org/papers/2012/BigData-ICS-Draft.pdf (author draft) · AT SOURCE (author copy; wording may differ slightly from the published version).
Exact quotations: definition — Big Data rests on the interplay of "Technology: maximizing computation power and algorithmic accuracy to gather, analyze, link, and compare large data sets." / "Analysis: drawing on large data sets to identify patterns in order to make economic, social, technical, and legal claims." / "Mythology: the widespread belief that large data sets offer a higher form of intelligence and knowledge that can generate insights that were previously impossible, with the aura of truth, objectivity, and accuracy." The six provocations (headings): 1. Big Data changes the definition of knowledge; 2. Claims to objectivity and accuracy are misleading; 3. Bigger data are not always better data; 4. Taken out of context, Big Data loses its meaning; 5. Just because it is accessible does not make it ethical; 6. Limited access to Big Data creates new digital divides. Under 3: "Twitter does not represent 'all people', and it is an error to assume 'people' and 'Twitter users' are synonymous: they are a very particular sub-set." / "Although a handful of companies have access to the firehose, very few researchers have this level of access. Most either have access to a 'gardenhose' (roughly 10% of public tweets), a 'spritzer' (roughly 1% of public tweets), or have used 'white-listed' accounts." / "Big data and whole data are also not the same. Without taking into account the sample of a dataset, the size of the dataset is meaningless."
Strength: strong. Role: LOAD-BEARING for the headline "bigger data are not always better data".

=====================================================================
6. ADMINISTRATIVE DATA AS EVIDENCE
=====================================================================

6.1 ADR UK, "What is administrative data?" URL read: https://www.adruk.org/our-mission/administrative-data/ · AT SOURCE.
Quotations: administrative data is "information created when people use public services, such as schools, the NHS, the courts or the benefits system." It "includes information about everyone who comes into contact with public services"; it reduces "the need for costly and time-consuming data collection"; "Although most of this data was not originally collected for research purposes, it can be used safely and responsibly to improve our understanding of society."
Strength: strong (institutional). Role: SUPPORTING.

6.2 ONS working paper, "Cataloguing errors in administrative and alternative data sources: what, when and how", 21 April 2023 (with Prof. Paul Smith, Southampton). URL read: https://www.ons.gov.uk/methodology/methodologicalpublications/generalmethodology/onsworkingpaperseries/cataloguingerrorsinadministrativeandalternativedatasourceswhatwhenandhow · AT SOURCE.
Quotations: "Administrative data are collected during the operations of an organisation." / "Administrative data are generally not collected for the sole purpose of producing statistics." Error typology: Measurement errors (validity, reliability, missing data — unit and item); Representation errors (coverage: under- and over-coverage; selection); Processing errors (data entry/coding/editing, model, imputation, unit errors, linkage, identification).
What it establishes: the official UK taxonomy of what goes wrong when operational records become statistics — "unit errors" and "coverage" map directly onto grain and denominator. Strength: strong. Role: LOAD-BEARING.

6.3 Connelly, R., Playford, C. J., Gayle, V., Dibben, C. (2016). "The role of administrative data in the big data revolution in social science research." Social Science Research 59:1–12.
URL read: https://wrap.warwick.ac.uk/id/eprint/78490/7/WRAP_Connelly_S0049089X1630206X-main.pdf (Warwick repository, open access) · AT SOURCE.
Quotations: Abstract opens "The term big data is currently a buzzword in social science, however its precise meaning is ambiguous." Definition (p.3): "data which are derived from the operation of administrative systems (e.g. data collected by government agencies for the purposes of registration, transaction and record keeping)". Strengths (p.5): "Administrative social science data will generally provide much larger sample sizes than social surveys, and at times administrative social science data may cover the entire population of interest"; "offers the possibility for creating cohorts of individuals to study change over time"; "may also offer savings in comparison to the costs of primary data collection". Caveats: (p.4) "administrative social science data differs from made data as it is not originally collected for the purpose of research"; "Researchers generally have no input into the design, structure and content of administrative social science data"; (p.6) "Administrative social science data were not collected for research purposes and therefore are not documented in order to support data analysis"; "researchers must put effort into uncovering the data generation processes which have governed how these data have been created"; (p.11) "Understanding the processes of how and why administrative data are collected will be central to assessing the data's quality".
Strength: strong. Role: LOAD-BEARING.

6.4 Bean, C. (2016). Independent Review of UK Economic Statistics (March 2016). URL read: https://assets.publishing.service.gov.uk/media/5a7f603440f0b62305b86c45/2904936_Bean_Review_Web_Accessible.pdf · AT SOURCE.
Quotations: para 1.13: "Relatively little use is made of administrative data, such as that held by Her Majesty's Revenue and Customs (HMRC) and still less of other (and growing) sources of big data. That is in stark contrast to some other NSIs... In large part, the limited exploitation in this country reflects the cumbersome legal framework governing the use of such information for statistical purposes." para 2.39: "Monthly VAT returns to HMRC on turnover and purchases of individual businesses, matched through an improved business register, has the potential to greatly enhance the output measure of GDP, as well as the consumption component of the expenditure accounts."
Strength: strong. Role: COLOUR (shows the national-accounts appetite for transactional admin data; note the reliance on "an improved business register" — i.e. on getting the unit right).

=====================================================================
7. AGGREGATION AND THE DASHBOARD'S "BIG NUMBER"
=====================================================================
Sources already gathered carry this: NIST §1.3.5.1 ("Extreme values in the tails distort the mean..."); ONS ASHE guide (mean "highly influenced by those values at the upper end of the distribution"); Lorenz 1905 p.213 (average income "no safe criterion"); HHI (squaring = the largest contributor dominates). Taken together: a sum or mean is, arithmetically, a weighted statement about its largest terms; a median or a share is not. Wainer and the sum-vs-rate league-table confusion: NOT researched (cross-reference to the other chapter). Role: SUPPORTING.

=====================================================================
THREADS PULLED (not asked for, found en route)
=====================================================================
- The UK's official bed-occupancy statistic is defined as a midnight snapshot in both the KH03 guidance and the NHS Data Dictionary — so the "artefact" is codified, not accidental; and the day-ward rule ("only one bed day" even if two patients used it, "therefore occupancy rates should not exceed 100%") is a second explicit boundary rule that caps a count by definition.
- Salganik et al. 2006 measured their inequality with the Gini coefficient — the same instrument as 4.2 — which gives the author a single thread from Lorenz 1905 → Gini → MusicLab.
- Meng's precise wording of the paradox is "the more the data, the surer we fool ourselves" (not "bigger").
- Aguiar & Waldfogel's Spotify paper (NBER 21653) could only see Spotify's public "top 50 songs" — a reminder that most public streaming data are head-only, so claims about the tail from such data are claims about what is not observed.
- Bit by Bit's "dirty" example is the 9/11 pager study (Back, Küfner & Egloff) where one automated pager produced the whole "rising anger" trend — a tidy case of one unit dominating an aggregate.
- Regulation 696/93's preamble ties unit definitions to comparability ("Only if the Member States use common definitions of statistical units...") — the political reason grain gets standardised.
- Datta et al. 2018 find diversification at the individual grain while market-level studies find concentration: the same market looks different depending on whether the row is a user or a track.

=====================================================================
LEFT OUT and why
=====================================================================
- Anderson 2006/2004: wired.com blocked; not quoted rather than quoted from memory.
- Elberse's HBR "Long Tail Debate" response (2 July 2008): paywalled; the reprint of the main article suffices.
- Denominator neglect, ecological fallacy, MAUP, Wainer league tables: assigned to other chapters; cross-reference only.
- OECD inequality indicator definitions (S80/S20, Palma): page served no content; World Bank definitions cover Gini and top-decile share adequately.
- Pierce et al. 2024 full abstract and Simon et al. 2011 full abstract: publisher pages blocked; used trade-press and repository copies and said so.
- A "critical source" stating 80/20 is not a law: none found at source; Juran's own mea culpa and "universal observation" framing is better evidence than a blog.
- Coelho & Mendes 2019 findings: abstract silent on result; refused to infer numbers from the title.
- Tufte Beautiful Evidence / Visual Display: not needed once the Visual Explanations chapter was in hand.
- Kitchin 2014 book: superseded by the open 2016 paper with the same seven traits.

=====================================================================
RICH REFERENCES (max three)
=====================================================================
1. Meng 2018 (Harvard copy, https://statistics.fas.harvard.edu/file_url/823) — one identity (quality × quantity × difficulty) and one number (2.3 million ≈ 400) that reorganise how a reader thinks about every transactional feed.
2. Salganik, Bit by Bit §2.3 (https://www.bitbybitbook.com/en/1st-ed/observing-behavior/characteristics/) — the ten characteristics are a ready-made audit list for any dashboard data source, each with a one-line summary already written for a first-time reader.
3. Lorenz 1905 (https://archive.org/stream/jstor-2276207/2276207_djvu.txt) — the curve in its inventor's words plus his warning about averages; short, quotable, and the root of Gini, HHI-style thinking and MusicLab's metric.

=====================================================================
WHAT SURPRISED ME
=====================================================================
- Wickham, author of the canonical paper on tidy data, writes that it is "surprisingly difficult to precisely define variables and observations in general" — the grain is a judgement even for him.
- The midnight bed count is not a quirk but the written UK definition (KH03 and the Data Dictionary), and the US literature finds it sits at the daily trough (peak ~11 a.m.).
- Elberse's 2007 SoundScan figure: 91% of 3.9 million digital tracks sold fewer than 100 copies and 24% sold exactly one — the "long tail" is mostly a tail of ones and zeros.
- Juran's own 1975 confession that the "Pareto principle" is misnamed and the curves belong to Lorenz; the Juran Institute's current page still credits Pareto and does not repeat the mea culpa.
- Meng's effective-sample-size collapse is driven by a data-defect correlation of only about −0.005.
- Regulation 696/93 defines seven distinct business units; a dashboard "number of businesses" is undefined until you say which.

---

## Agent D — Outliers, robust statistics, positive deviance and comparability

# RESEARCH REPORT — Outliers (artefact vs finding) and Comparability (what a comparison must declare)

All fetched 2026-10-06. "At source" = the paper/standard itself or an author/institutional copy. Tool constraint: the fetch layer sometimes returned only short exact quotes; where a quote is a fragment I say so. Several hosts were blocked from this sandbox (PMC/NCBI reCAPTCHA, Wiley, SAGE partial, Project Euclid, ScienceDirect robots, Europe PMC, PARE's own site behind Anubis) — noted per source.

---

## 1. OUTLIER DEFINITIONS

### 1.1 Hawkins 1980 — the standard definition, found quoted in two open sources
**(a) Osborne & Overbay 2004**, "The power of outliers (and why researchers should ALWAYS check for them)", *Practical Assessment, Research & Evaluation* 9(6). · URL read: https://www.researchgate.net/publication/242073851_The_Power_of_Outliers_and_Why_Researchers_Should_Always_Check_for_Them (full text visible; the journal's own host https://openpublishing.library.umass.edu/pare/article/id/1528/ and pareonline.net both blocked the fetcher) · How read: full text, author-deposited copy of an open peer-reviewed article.
Exact: Hawkins (1980) defined an outlier as "an observation that 'deviates so much from other observations as to arouse suspicions that it was generated by a different mechanism'".
**(b) Aggarwal, *Outlier Analysis*, 2nd ed., ch. 1** · URL: http://www.charuaggarwal.net/outlierbook.pdf (author's own copy) · At source.
Exact: "An outlier is an observation which deviates so much from the other observations as to arouse suspicions that it was generated by a different mechanism."
Note the two renderings differ by one word ("from other" vs "from the other"); Osborne & Overbay also elide the opening. Either can be cited as quoted-in; neither is Hawkins at source (Chapman & Hall 1980, not open).
Establishes: the canonical definition, and that its core is *mechanism*, not distance. Strength: strong (two independent open quotations agree). Role: LOAD-BEARING.

### 1.2 Barnett & Lewis — definition and the contaminant point (secondary only)
**Hodge & Austin 2004**, "A Survey of Outlier Detection Methodologies", *Artificial Intelligence Review* 22:85–126 · URL: https://eprints.whiterose.ac.uk/767/1/hodgevj4.pdf (White Rose institutional copy) · At source for Hodge & Austin; secondary for B&L.
Exact (B&L as quoted): "An observation (or subset of observations) which appears to be inconsistent with the remainder of that set of data."
Exact (Grubbs as quoted): "An outlying observation, or outlier, is one that appears to deviate markedly from other members of the sample in which it occurs."
Exact (causes): outliers arise from "human error, instrument error, natural deviations in populations, fraudulent behaviour, changes in behaviour of systems or faults in systems."
Hodge & Austin say how an outlier is handled "depends on the application area."
**Osborne & Overbay** quote Barnett & Lewis (1994) for the contaminant point: "Not all outliers are illegitimate contaminants, and not all illegitimate scores show up as outliers".
The formal discordant/contaminant terminology itself I could NOT reach at source (book paywalled). Strength: moderate (secondary). Role: SUPPORTING.

### 1.3 Grubbs 1969 and the normality assumption
Grubbs 1969 *Technometrics* 11(1):1–21 at Taylor & Francis returned 403; not read at source. Definition via Hodge & Austin above.
**NIST/SEMATECH e-Handbook of Statistical Methods**, §1.3.5.17 Grubbs' Test for Outliers and §1.3.5.17 "Detection of Outliers" · URLs: https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h1.htm and https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm · At source (US government public-domain).
Exact: "Grubbs' test (Grubbs 1969 and Stefansky 1972) is used to detect a single outlier in a univariate data set that follows an approximately normal distribution."
Exact: "If you suspect more than one outlier may be present, it is recommended that you use either the Tietjen-Moore test or the generalized extreme studentized deviate test instead."
Exact: "If the normality assumption for the data being tested is not valid, then a determination that there is an outlier may in fact be due to the non-normality of the data rather than the prescence [sic] of an outlier."
Exact: "An outlier is an observation that appears to deviate markedly from other observations in the sample."
Exact: "Outliers may be due to random variation or may indicate something scientifically interesting."
Exact: "An outlier may indicate bad data. For example, the data may have been coded incorrectly or an experiment may not have been run correctly."
Exact: "If it can be determined that an outlying point is in fact erroneous, then the outlying value should be deleted from the analysis (or corrected if possible)." and "However, if the data contains significant outliers, we may need to consider the use of robust statistical techniques".
Masking/swamping (fragments): "Masking can occur when we specify too few outliers in the test" … "Swamping can occur when we specify too many outliers in the test".
Test statistic G = max|Yi − Ȳ|/s; H0 no outliers, Ha exactly one outlier.
Establishes: the test's single-outlier, normality-dependent character; the test "finds" an outlier in a skewed distribution that is merely skewed. Strength: strong. Role: LOAD-BEARING (for "a test's verdict depends on its model").

### 1.4 Tukey 1977 fences
**NIST e-Handbook §7.1.6 "What are outliers in the data?"** · URL: https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm · At source.
Exact: "An outlier is an observation that lies an abnormal distance from other values in a random sample from a population."
Fences as given: lower inner fence Q1 − 1.5*IQ; upper inner fence Q3 + 1.5*IQ; lower outer fence Q1 − 3*IQ; upper outer fence Q3 + 3*IQ.
Exact: "A point beyond an inner fence on either side is considered a mild outlier. A point beyond an outer fence is considered an extreme outlier."
Exact: "Outliers should be investigated carefully. Often they contain valuable information about the process under investigation or the data gathering and recording process. Before considering the possible elimination of these points from the data, one should try to understand why they appeared and whether it is likely similar values will continue to appear."
(NIST does not name Tukey on that page.)
**Tukey's own terms** — Lin, Zhang & Tong 2025, "When Tukey meets Chauvenet: a new boxplot criterion for outlier detection", arXiv:2506.06491 (also *JCGS* 2025) · URL: https://arxiv.org/pdf/2506.06491 · At source (preprint).
Exact: "Tukey (1977) further referred to the fences with k = 1.5 as the 'inner fences'" and "the observations between the inner and outer fences as the 'outside' outliers, and those beyond the outer fences as the 'far out' or 'extreme' outliers"; and "if the data is sampled from the normal distribution, then about 0.7% of them will lie outside the two fences of the boxplot" (citing Hubert & Vandervieren 2008).
**Dawson 2011**, "How Significant Is A Boxplot Outlier?", *Journal of Statistics Education* 19(2) · URL: https://jse.amstat.org/v19n2/dawson.pdf · At source.
Exact (abstract): "It is common to consider Tukey's schematic ("full") boxplot as an informal test for the existence of outliers. While the procedure is useful, it should be used with caution, as at least 30% of samples from a normally-distributed population of any size will be flagged as containing an outlier, while for small samples (N<10) even extreme outliers indicate little."
Exact: "For the normal distribution, the incidence of samples with flagged outliers never drops below about 30%, and above sample size 13 starts to rise."
Establishes: Tukey's words were "outside" and "far out", a labelling rule for attention, not an error test; a perfectly normal sample will routinely show "outliers" under the rule. Strength: strong for the mechanics; the "outside"/"far out" wording is quoted via a 2025 paper, not EDA itself (book not open). Role: LOAD-BEARING.

### 1.5 Chandola, Banerjee & Kumar 2009, "Anomaly Detection: A Survey", *ACM Computing Surveys* 41(3), art. 15
URL: https://arindam.cs.illinois.edu/papers/09/anomaly.pdf (co-author Banerjee's copy; the UMN kumar001 link is dead, 404) · At source.
Exact (15:2): "Anomalies are patterns in data that do not conform to a well defined notion of normal behavior."
Exact (15:2): "The importance of anomaly detection is due to the fact that anomalies in data translate to significant, and often critical, actionable information in a wide variety of application domains."
Exact (15:2): "An anomalous traffic pattern in a computer network could mean that a hacked computer is sending out sensitive data to an unauthorized destination. An anomalous MRI image may indicate the presence of malignant tumors. Anomalies in credit card transaction data could indicate credit card or identity theft, or anomalous readings from a space craft sensor could signify a fault in some component of the space craft."
Exact (15:3): "The boundary between normal and anomalous behavior is often not precise. Thus an anomalous observation that lies close to the boundary can actually be normal, and vice versa."
Exact (15:3): "Often the data contains noise that tends to be similar to the actual anomalies and hence is difficult to distinguish and remove."
Exact (15:3): "Noise can be defined as a phenomenon in data that is not of interest to the analyst, but acts as a hindrance to data analysis." / "Noise removal is driven by the need to remove the unwanted objects before any data analysis is performed. Noise accommodation refers to immunizing a statistical model estimation against anomalous observations." / "The interestingness or real life relevance of anomalies is a key feature of anomaly detection."
Exact (15:7–8): "If an individual data instance can be considered as anomalous with respect to the rest of data, then the instance is termed a point anomaly." / "If a data instance is anomalous in a specific context, but not otherwise, then it is termed a contextual anomaly." / "If a collection of related data instances is anomalous with respect to the entire data set, it is termed a collective anomaly."
Hawkins is in the bibliography but not quoted. Establishes: same datum is "noise" or "anomaly" according to analyst interest; contextual anomalies (a value normal in July, anomalous in January) are the dashboard-relevant kind. Strength: strong. Role: LOAD-BEARING.

### 1.6 Aggarwal, *Outlier Analysis* (2nd ed., Springer 2017), ch. 1
URL: http://www.charuaggarwal.net/outlierbook.pdf · At source (author copy).
Exact: "An outlier is a data point that is significantly different from the remaining data." Then the Hawkins quote (1.1b). "Outliers are also referred to as abnormalities, discordants, deviants, or anomalies". "When the generating process behaves unusually, it results in the creation of outliers." "an outlier often contains useful information about abnormal characteristics of the systems". "In all these applications, the data has a 'normal' model, and anomalies are recognized as deviations from this normal model." "Some authors use the terms weak outliers and strong outliers in order to distinguish between noise and anomalies." Output is either outlier scores or binary labels.
Strength: strong. Role: SUPPORTING (gives the "normal model" framing cleanly).

---

## 2. ARTEFACT OR SIGNAL — THE PRACTICE

### 2.1 Osborne & Overbay 2004 (details as 1.1a)
Exact (general def.): "An outlier is generally considered to be a data point that is far outside the norm for a variable or population."
Exact (fringeliers, after Wainer 1976): "Unusual events which occur more often than seldom" — points near three SD from the mean.
Causes — section headings (verbatim headings) and first sentences:
- "Outliers from data errors" — "Outliers are often caused by human error, such as errors in data collection, recording, or entry."
- "Outliers from intentional or motivated mis-reporting" — "There are times when participants purposefully report incorrect data to experimenters or surveyers."
- "Outliers from sampling error" — "Another cause of outliers or fringeliers is sampling."
- "Outliers from standardization failure" — "Outliers can be caused by research methodology, particularly if something anomalous happened during a particular subject's experience."
- "Outliers from faulty distributional assumptions" — "Incorrect assumptions about the distribution of the data can also lead to the presence of suspected outliers."
- "Outliers as legitimate cases sampled from the correct population" — "Finally, it is possible that an outlier can come from the population being sampled legitimately through random chance."
- "Outliers as potential focus of inquiry" — "We all know that interesting research is often as much a matter of serendipity as planning and inspiration." and "Before discarding outliers, researchers need to consider whether those data contain valuable information that may not necessarily relate to the intended study, but has importance in a more global sense."
Recommendation: "If outliers of this nature cannot be corrected they should be eliminated as they do not represent valid population data points." (illegitimate ones); for legitimate ones they discuss transformation or truncation. Screening rule: "We tend to use a z = 3 guideline as an initial screening tool, and depending on the results of that screening, examine the data more closely." Results: cleaned correlations more accurate "70-100% of the time"; "Removal of outliers produced significant change in statistics primarily when there were strong group differences."
Establishes: the triage list — the first six causes are artefacts of process; the seventh is the finding. Strength: strong (open peer-reviewed; but fetched from ResearchGate mirror). Role: LOAD-BEARING.

### 2.2 Leys, Ley, Klein, Bernard & Licata 2013, *J. Experimental Social Psychology* 49(4):764–766
URL read: https://scispace.com/pdf/detecting-outliers-do-not-use-standard-deviation-around-the-xrxf8j7a6b.pdf (mirror of the author postprint; the ORBilu institutional postprint https://orbilu.uni.lu/handle/10993/59204 confirmed the abstract but its bitstream was robots-blocked; ScienceDirect robots-blocked) · Full text via mirror.
Exact (abstract, from ORBilu): "A survey revealed that researchers still seem to encounter difficulties to cope with outliers. Detecting outliers by determining an interval spanning over the mean plus/minus three standard deviations remains a common practice. However, since both the mean and the standard deviation are particularly sensitive to outliers, this method is problematic. We highlight the disadvantages of this method and present the median absolute deviation, an alternative and more robust measure of dispersion that is easy to implement."
Exact (three problems): "Firstly, it assumes that the distribution is normal (outliers included). Secondly, the mean and standard deviation are strongly impacted by outliers. Thirdly, as stated by Cousineau and Chartier (2010), this method is very unlikely to detect outliers in small samples."
Exact (MAD): "Usually, b = 1.4826, a constant linked to the assumption of normality of the data."
Exact (thresholds): "Miller (1991) proposes the values of 3 (very conservative), 2.5 (moderately conservative) or even 2 (poorly conservative)."
Exact (reporting): "The threshold should be justified and the justification should clearly state that other concerns than cherry-picking degrees of freedom guided the selection."
Exact: "Notwithstanding the decision to remove, correct or leave an outlier (for a discussion on this topic see McClelland, 2000), it is necessary to be able to detect its presence."
Survey: 127 articles; all used mean ± k·SD or the IQR method; none mentioned MAD.
Establishes: the robust rule and its thresholds; the mean±SD rule is self-defeating (the outlier inflates the yardstick used to catch it). Strength: strong. Role: LOAD-BEARING.

### 2.3 Simmons, Nelson & Simonsohn 2011, "False-Positive Psychology", *Psychological Science* 22(11):1359–1366
URL: https://journals.sagepub.com/doi/10.1177/0956797611417632 · At source (open access).
Exact: "Should more data be collected? Should some observations be excluded? Which conditions should be combined and which ones compared?"
Exact: "it is common (and accepted practice) for researchers to explore various analytic alternatives, to search for a combination that yields 'statistical significance,' and to then report only what 'worked.'"
Exact (requirement 5): "If observations are eliminated, authors must also report what the statistical results are if those observations are included."
Table 1: combining the four flexibilities yields a false-positive rate of about 61% at p<.05.
Strength: strong. Role: LOAD-BEARING for the rule "show the number with and without the exclusion".

### 2.4 Bakker & Wicherts 2014 — how often removal goes unreported
I could not reach the *Psychological Methods* paper (PubMed reCAPTCHA; not open). But a companion paper by the same authors is open and more directly on point:
**Bakker & Wicherts 2014, "Outlier Removal and the Relation with Reporting Errors and Quality of Psychological Research", *PLOS ONE* 9(7):e103360** · URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0103360 · At source.
Exact: "The removal of outliers to acquire a significant result is a questionable research practice that appears to be commonly used in psychology."
Exact: "Results show no significant difference between the two types of articles in median p value, sample sizes, or prevalence of all reporting errors, large reporting errors, and reporting errors that concerned the statistical significance."
Exact: "However, we did find a discrepancy between the reported degrees of freedom of t tests and the reported sample size in 41% of articles that did not report removal of any data values."
Exact: "We failed to find that the removal of outliers from the analysis in psychological articles was related to weaker evidence (against the null hypothesis of no effect), sample size, or the prevalence of errors. However, our control sample might be contaminated due to nondisclosure of excluded values in articles that did not report exclusion of outliers. Results therefore highlight the importance of more transparent reporting of statistical analyses."
Also: 2,667 results from 153 articles (92 reporting removal, 61 not); they recommend "an outlier handling protocol" set before analysis, that "researchers should be transparent in their articles about the exclusion of data", and preregistration as "preferred practice to explicate the handling of outliers in advance"; inconsistent thresholds (z=2 vs 3) permit "self-serving justifications".
Establishes: the only hard figure I found on silent removal — 41% of "no exclusions" papers show df/N discrepancies consistent with undisclosed exclusion. Strength: moderate-strong (indirect measure, authors say so). Role: LOAD-BEARING.

### 2.5 Robust statistics
**Hampel 2001, "Robust statistics: A brief introduction and overview", Research Report No. 94, Seminar für Statistik, ETH Zürich** · URL: https://pt-drw.aafco.org/CSPStatsDocs/Reports/FrankHampelOnRobStats.pdf (mirror; ETH Research Collection returned 500) · Full text, mirror.
Exact: "Robust statistics is the stability theory of statistical procedures. It systematically investigates the effects of deviations from modelling assumptions on known procedures and, if necessary, develops new, better procedures."
Exact (gross-error rate in real data): "For scientific routine data, not taken with utmost care, their fraction is typically between 1 percent and 10 percent (!)." (and >20% in some medical data).
Breakdown point: "for the median it is 1/2"; "for the arithmetic mean it is 0"; MAD also 1/2.
**Huber's one-sentence definition** ("robustness signifies insensitivity to small deviations from the assumptions", *Robust Statistics* 1981, p.1) — I could NOT verify at source (Project Euclid and Wiley blocked). Treat as SECONDARY/unverified; use Hampel's sentence instead, which is at source. Strength: strong (Hampel), unverified (Huber). Role: SUPPORTING.
NIST (1.3) supplies the practical rule: erroneous → correct/delete; legitimate but influential → robust methods rather than deletion.

---

## 3. POSITIVE DEVIANCE

### 3.1 Marsh, Schroeder, Dearden, Sternin & Sternin 2004, "The power of positive deviance", *BMJ* 329:1177–1179
URL read: https://www.bmj.com/content/329/7475/1177 and …/1177.full · How read: PARTIAL — BMJ shows only the opening; PMC (PMC527707), Europe PMC and the Sternin ResearchGate copy were all blocked (reCAPTCHA/robots/429). Marked PARTIAL.
Exact (opening/summary): "Identifying individuals with better outcome than their peers (positive deviance) and enabling communities to adopt the behaviours that explain the improved outcome are powerful methods of producing change."
Exact (definition): positive deviance is "an uncommon practice that confers advantage to the people who practise it compared with the rest of the community."
Steps visible before the cut: develop case definitions; identify four to six people who have achieved an unexpected good outcome despite high risk; interview and observe these individuals (remaining steps not read).
Egypt example visible: "parents of poor but well nourished children were found to feed their children a diet that included eggs, beans, and green vegetables"; teaching this plus "hand washing and hygienic food preparation, improved child growth."
Strength: moderate (partial read). Role: LOAD-BEARING for the definition; the author should obtain the full text for the six steps.

### 3.2 Vietnam case — Singhal, Sternin & Durá, "Positive Deviance Grows Roots in Vietnam: in the Land of a Thousand Rice Fields Combating Malnutrition" (Positive Deviance Initiative case study)
URL: https://positivedeviance.org/s/PDVietnam07112010.pdf (redirects to static1.squarespace.com) · At source (practitioner case study, not peer-reviewed).
Exact: "Positive Deviance enables communities to discover the wisdom they already have, and then to act on it."; "Family members added greens of sweet potato plants to their children's meals"; "Family members collected tiny shrimps and crabs from paddy fields"; "PD caregivers were feeding their children three to four times a day"; "PD caregivers washed the hands of the children before and after they ate"; "After the pilot project, which lasted two years, malnutrition had decreased by an amazing 85 percent"; eventually "help[ed] over 2.2 million people, including over 50,000 children improve their nutritional status".
Strength: moderate (advocacy source for figures; the 85%/2.2m claims are the movement's own). Role: COLOUR.

### 3.3 Bradley et al. 2009, "Research in action: using positive deviance to improve quality of health care", *Implementation Science* 4:25
URL: https://link.springer.com/article/10.1186/1748-5908-4-25 (BMC domain rate-limited; Springer mirror of the same OA article) · At source.
Exact (four steps): "Identify 'positive deviants,' i.e., organizations that consistently demonstrate exceptionally high performance in the area of interest." / "Study the organizations in-depth using qualitative methods to generate hypotheses about practices that allow organizations to achieve top performance." / "Test hypotheses statistically in larger, representative samples of organizations." / "Work in partnership with key stakeholders, including potential adopters, to disseminate the evidence about newly characterized best practices."
Exact: "The central premise of a positive deviance approach is that solutions to problems that face a community often exist within that community."
Exact (how deviants were picked): "We identified the exceptional performers, those that had accomplished median door-to-balloon times of 90 minutes or less for their previous 50 cases."
Exact (limitation): "In some cases, positive deviance studies may rely on self-reports of organizational practices rather than procedures of a controlled trial, which may result in reporting bias."
Establishes: the good-end outlier is explicitly a hypothesis generator (step 2) to be tested (step 3) — exactly "an outlier at the good end is a hypothesis about mechanism". Strength: strong. Role: LOAD-BEARING.

### 3.4 Critique — Baxter, Taylor, Kellar & Lawton 2016, "What methods are used to apply positive deviance within healthcare organisations? A systematic review", *BMJ Quality & Safety* 25:190–201
URL: https://qualitysafety.bmj.com/content/25/3/190 · At source.
Exact: "articles lacked detail and comparison groups were rarely included."; quality scores "ranging from 2.1% to 50.0%"; "many articles provided limited or no detail about what criteria constituted positive deviance"; "the criteria used often appeared arbitrary and cut-off points were not justified."; "The methods and criteria used to identify positive deviants must always be stated regardless of whether they are exceptionally performing individuals, teams or organisations."; "Further research is required to develop high quality yet practical methods…".
Establishes: the mirror of §2 — picking good outliers has the same undeclared-threshold problem as removing bad ones. Strength: strong. Role: LOAD-BEARING.
Pascale & Sternin 2005 HBR (https://hbr.org/2005/05/your-companys-secret-change-agents): paywalled; only the teaser read: "Somewhere in your organization, groups of people are already doing things differently and better. To create lasting change, find these areas of positive deviance and fan their flames." COLOUR.

---

## 4. THE SMALL-DENOMINATOR OUTLIER

### 4.1 Gelman & Price 1999, "All maps of parameter estimates are misleading", *Statistics in Medicine* 18:3221–3234
URL: https://sites.stat.columbia.edu/gelman/research/published/allmaps.pdf (author copy) · At source.
Exact (abstract): "Maps are frequently used to display spatial distributions of parameters of interest, such as cancer rates or average pollutant concentrations by county." … "very high (and low) observed rates are found disproportionately in poorly-sampled areas." … "the highest adjusted rates tend to be found disproportionately in well-sampled areas."
Exact (kidney cancer): "Because of this stochastic noise, a disproportionate fraction of low-population counties are observed to have extremely high (or low) cancer rates when compared to typical counties."
Exact: "Mapping county posterior means or highlighting the counties with highest posterior means leads to new problems."
Establishes (beyond Wainer): small units crowd BOTH tails; and the fix (shrinkage) creates the opposite artefact — large units then dominate the top. Strength: strong. Role: LOAD-BEARING.

### 4.2 Spiegelhalter 2005, "Funnel plots for comparing institutional performance", *Statistics in Medicine* 24:1185–1202
URL read: https://scispace.com/papers/funnel-plots-for-comparing-institutional-performance-4iskbhp4fo · How read: ABSTRACT-ONLY, fragments (Wiley 403; PubMed reCAPTCHA).
Exact fragments: "'Funnel plots' are recommended as a graphical aid for institutional comparisons, in which an estimate of an underlying quantity is plotted against an interpretable measure of its precision." … control limits form a funnel "analogous" to Shewhart charts … the method is "flexible", "attractively simple", and helps "avoid spurious ranking of institutions into 'league tables'."
Strength: moderate (fragmentary abstract). Role: SUPPORTING.

### 4.3 PHE/OHID Fingertips technical guidance — confidence intervals
URL: https://fingertips.phe.org.uk/static-reports/public-health-technical-guidance/Basic_statistics/Confidence_intervals.html · At source.
Exact: "A confidence interval is a range of values which quantifies the imprecision in the estimate of a particular value." / "Larger samples, or populations, give more precise estimates with smaller confidence intervals." / "It is particularly important to provide confidence intervals when numbers are small, and hence the random component of variation is likely to be large." / "If the target or benchmark value is outside the confidence interval, it can be inferred that the difference between the estimate and the target is statistically significant at the corresponding significance level."
Strength: strong. Role: SUPPORTING. (APHO Technical Briefing 2 on SPC/funnel plots exists at https://fingertips.phe.org.uk/static-reports/public-health-technical-guidance/PDF/APHO%20Tech%20Briefing%202.pdf but returned 500 twice — worth a retry by the author.)

### 4.4 Dawson 2011 (see 1.4) also belongs here: small N → "even extreme outliers indicate little".

---

## 5. COMPARABILITY — THE STANDARDS

### 5.1 Regulation (EC) No 223/2009 on European statistics, Art. 12(1)
URL: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009R0223 · At source (law).
Exact: comparability — "the measurement of the impact of differences in applied statistical concepts, measurement tools and procedures where statistics are compared between geographical areas, sectoral domains or over time"; coherence — "the adequacy of the data to be reliably combined in different ways and for various uses"; accuracy — "the closeness of estimates to the unknown true values"; timeliness — "the period between the availability of the information and the event or phenomenon it describes"; punctuality — "the delay between the date of the release of the data and the target date"; relevance — "the degree to which statistics meet current and potential needs of the users"; accessibility and clarity — "the conditions and modalities by which users can obtain, use and interpret data".
Strength: strong. Role: LOAD-BEARING (legal definition; comparability is explicitly about three axes: place, domain, time).

### 5.2 European Statistics Code of Practice (2017), Principle 14
URL: https://ec.europa.eu/eurostat/documents/4031688/8971242/KS-02-18-142-EN-N.pdf · At source.
Exact: "European Statistics are consistent internally, over time and comparable between regions and countries; it is possible to combine and make joint use of related data from different data sources." 14.1 "Statistics are internally coherent and consistent (i.e. arithmetic and accounting identities observed)." 14.2 "Statistics are comparable over a reasonable period of time." 14.3 "Statistics are compiled on the basis of common standards with respect to scope, definitions, units and classifications in the different surveys and data sources." 14.4 "Statistics from the different data sources and of different periodicity are compared and reconciled." 14.5 "Cross-national comparability of the data is ensured within the European Statistical System through periodical exchanges…"
Strength: strong. Role: LOAD-BEARING.

### 5.3 SIMS/SDMX concept definitions (the operational Eurostat vocabulary)
URL: https://sdmx.org/wp-content/uploads/SDMX_Glossary_Version_2_1_December_2020.htm · At source for SDMX glossary; each entry cites "Eurostat, Technical Manual of the Single Integrated Metadata Structure (SIMS), 2014".
Exact: Comparability — "Extent to which differences between statistics can be attributed to differences between the true values of the statistical characteristics." Comparability—geographical — "Extent to which statistics are comparable between geographical areas." Comparability—over time — "Extent to which statistics are comparable or reconcilable over time." Coherence—cross domain — "Extent to which statistics are reconcilable with those obtained through other Data Sources or statistical domains." Coherence—internal — "Extent to which statistics are consistent within a given Data Set." Data revision—policy — "Policy aimed at ensuring the transparency of disseminated data, whereby preliminary data are compiled that are later revised."
The SIMS structure (Eurostat, Nov 2015, https://ec.europa.eu/eurostat/documents/64157/4373903/SIMS-2-0-Revised-standards-November-2015-ESSC-final.pdf) lists 15.1.1 "CC1. Asymmetry for mirror flows statistics – coefficient" and 15.2.1 "CC2. Length of comparable time series" as the two standard comparability indicators. The Eurostat Quality Grading System (https://ec.europa.eu/eurostat/documents/10186/9049855/Quality-Grading-System.pdf) rates comparability over time by "number of data points from last methodological break" (>4 high; 3–4 medium; <3 low).
The best one-line definition of comparability for the book: "the extent to which differences between statistics can be attributed to differences between the true values" — i.e. a comparison is valid when the only thing that differs is the thing you are comparing. Strength: strong. Role: LOAD-BEARING.
ESS Handbook for Quality and Metadata Reports (2021), §S.15 pp.147–162 (https://ec.europa.eu/eurostat/documents/3859598/13925930/KS-GQ-21-021-EN-N.pdf/...): confirmed to contain the same definitions and the instruction that breaks be identified and their effects assessed, but the fetcher truncated the PDF before p.147 — PARTIAL.

### 5.4 Break in series — how it is flagged
**Government Analysis Function, "Using symbols and shorthand in tables" (11 Jan 2022)** · URL: https://analysisfunction.civilservice.gov.uk/policy-store/symbols-in-tables-definitions-and-help/ · At source.
Exact: [b] = "break in a data series that means that data before the break cannot be directly compared with data after the break"; [p] = "data points are yet to be finalised, or are expected to be revised"; [r] = "a data point has been revised since it was first published"; [c] = "a data point would give away confidential information"; [u] = "data points are of low quality"; [x] = "data is unavailable for reasons other than those described"; [z] = "a data point is not applicable"; [e] = "a data point is estimated"; [f] = "a data point is a calculated future value"; [low] = "low figure but not a real zero"; also [er], [w], [ns]/[s]/[ss]/[sss]. Advises against "NA" (ambiguous between not applicable and not available).
**Eurostat, "EU labour force survey – correction for breaks in time series"** (https://ec.europa.eu/eurostat/statistics-explained/index.php?title=EU_labour_force_survey_-_correction_for_breaks_in_time_series): the 2021 IESS regulation produced "breaks in the time series … resulting from updated labour status definitions in 2021"; countries supplied "complete break-free time series" or "correction factors" for 2009–2020; old tables renamed with "the letter 'h' for historical series".
Strength: strong. Role: LOAD-BEARING (the [b] definition is the cleanest statement of what a break means for a reader).

### 5.5 UK Code of Practice for Statistics 3.0 (2025)
URL: https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/5 · At source. (Note: numbering is the 2025 Code's "standards and practices", not the 2018 Q1/Q2/V3 scheme the brief mentions.)
Exact: Standard 6 "Producers must use suitable data sources and sound methods, and assure the quality of the statistics across the production and release processes". 6.6 "Use data that are coherent when aggregated, consistent over time and comparable across and within geographies at regional, national and local levels, where possible." 6.7 "Base methods on national or international good practice, scientific principles or professional consensus. Identify potential bias and address limitations. Use recognised standards, classifications and definitions. Explain reasons for deviations from these standards and any related implications for use". 6.9 "…Validate statistics through comparison with other relevant statistics and data sources where possible." 7.2 "Report on the key quality dimensions such as accuracy and timeliness, and, where possible, give estimates of error and confidence for the statistics." 7.4 "Be clear about the methods used. Explain quality issues related to the methods, systems and processes, including the extent to which the statistics are representative and comparable across the UK and internationally." 7.5 "Give advance notice to users of planned changes to methods and sources that will impact the statistics. Explain the nature and extent of the change, and provide a consistent back series where possible." 9.3 "Provide comparisons to support interpretation and signpost other relevant statistics, including within the UK and internationally." 3.9 "Release revisions and corrections of errors transparently and as soon as possible in line with the organisation's published policy, being clear about the nature and scale of change." 4.5 "Protect the confidentiality of individual and business information when producing statistics. Be transparent about the choices made in line with the producer's published confidentiality policy and apply appropriate disclosure control methods before release".
Caveat: two fetches rendered 6.7 slightly differently (the second, longer form is the one to trust; verify numbering against the PDF "Code-of-Practice-for-Statistics-3.0.pdf"). Strength: strong. Role: LOAD-BEARING.
**OSR, "The adequacy of UK-wide comparable statistics and data" (27 June 2025), §3** · URL: https://osr.statisticsauthority.gov.uk/publication/the-adequacy-of-uk-wide-comparable-statistics-and-data/pages/3 · At source. Introduces "meaningful comparability" = "the minimum level of comparability needed for drawing firm conclusions and for shaping action"; distinguishes coherence (consistency within/between related sources, with differences explained) from comparability (degree to which statistics can be meaningfully compared across geographies and time); says differences in methods/definitions must be documented and judged case by case against user need. Quotes the Code: "Comparisons should be provided where useful. Users should be signposted to other related statistics and the extent of consistency and comparability should be explained." SUPPORTING.

### 5.6 ONS/GSS geography: versioning, best fit, codes
**GSS Geography Policy — best-fit** (NRS-hosted copy) · URL: https://nrscotland.gov.uk/publications/geography-best-fit-policy · At source (GSS policy as published by NRS; ONS's own best-fit page 404'd).
Exact: "statistics for all geographies should be built from aggregations of statistical building blocks."; aims to "ensure outputs are accurate, consistent, and comparable in their use of geography."; best fit: lower geographies "do not fit exactly into the boundary of the higher geography; instead, they form an approximation to the shape of the boundary."; changes between censuses "can result in differences between OAs produced at each Census."; "The difference between best-fit and exact-fit estimates will depend on the target geography. Generally, the bigger the target geography, the less difference there will be."
**GSS Standard Names and Codes Policy** (NRS copy) · URL: https://nrscotland.gov.uk/publications/geography-standard-names-and-codes-policy · Exact: "Coding changes will be due to actual boundary changes."; "Codes are not re-used"; nine-character code, first letter = country. Name changes alone do not trigger a new code.
**ONS Code History Database** · URL: https://www.ons.gov.uk/methodology/geography/geographicalproducts/namescodesandlookups/codehistorydatabasechd · Exact: provides "details of codes, relationships, hierarchies and archived geographies and their metadata"; "contains the change history, where new codes have been allocated, from 1 January 2009."
**ONS Geospatial training, "Practical Geography for Statistics"** · URL: https://onsgeo.github.io/geospatial-training/docs/practical_geog_and_stats · Exact: "Local Authority boundaries change frequently so ensure you use the correct year to avoid errors."; mismatches arise when "you are joining data to boundaries which have different codes in areas due to boundary changes."; Register of Geographic Codes is "the definitive list of all codes in use for UK statistical geographies"; CHD "charts historic changes in codes, which can be useful when understanding how statistical geographies have changed over time."; best-fit is recommended "for statistical production, where it is important to ensure data is assigned to the correct area within the relevant geographical hierarchy."; "change management is one of the pillars of the GSS geography policy"; you "should avoid creating your own boundaries or modifying existing ones."
**ONS administrative geography (England)**: "Further local government reorganisation occurred in 2009, and again in 2019, 2020, 2021 and 2023."; "There are currently (as at 1 April 2023) 63 UAs in England, and 21 shire counties split into 164 (non-metropolitan) districts."
I did NOT find a sentence literally saying "statistical geographies are versioned"; the operational equivalent is the dated product names (e.g. "(December 2022)") plus the code rules above. The Open Geography Portal home page is a JS app and returned no text. Strength: strong on substance, with that wording caveat. Role: LOAD-BEARING.

### 5.7 GSS harmonisation
URL: https://analysisfunction.civilservice.gov.uk/government-statistical-service-and-statistician-group/gss-support/gss-harmonisation-support/ and …/harmonised-standards-and-guidance/ · At source.
Exact: "Harmonisation is about improving the consistency, comparability and coherence of data and statistics."; consistency = "using the same definitions and terms across different data sources and statistics"; "Without information about how data and statistics can be compared, users may come to incorrect conclusions."; example of a bad comparison: "surveys where the questions or definitions are different."; "Harmonised standards and guidance are tools for improving the comparability and coherence of statistics." Topics listed include Age and date of birth; Household definition; National identity; Sexual orientation; Sex and gender; Gender identity; General health; Long lasting health conditions and illness; Disability (Equality Act 2010); Unpaid care; Marital or civil partnership status; etc. (ethnicity is a separate standard not on the page fetched).
Strength: strong. Role: SUPPORTING.

### 5.8 Like-for-like
**Tesco PLC, Preliminary Results 2025/26, footnote 3 p.7** · URL: https://www.tescoplc.com/media/ch1fbgss/tesco-plc-preliminary-results-statement-fy26.pdf · At source.
Exact: "Like-for-like (LFL) sales growth is a measure of growth in Group sales from stores that have been open for at least a year and online sales (at constant exchange rates, excluding VAT and fuel). LFL excludes revenue from dunnhumby, Insurance & Money Services and mall rental income as this revenue is not directly linked to the sale of goods." Also: APMs "are presented for the 52 weeks to 22 February 2026 to aid comparability".
**ESMA Guidelines on Alternative Performance Measures (2015/1415)** · URL: https://www.esma.europa.eu/sites/default/files/library/2015/10/2015-esma-1415en.pdf · At source.
Exact: ¶20 issuers "should define the APMs used and their components as well as the basis of calculation adopted"; ¶26 "A reconciliation of the APM to the most directly reconcilable line item, subtotal or total presented in the financial statements of the corresponding period should be disclosed"; ¶37 "APMs should be accompanied by comparatives for the corresponding previous periods."; ¶41 "The definition and calculation of an APM should be consistent over time. In exceptional circumstances where issuers or persons responsible for the prospectus decide to redefine an APM, the issuer should: i. Explain the changes; ii. explain the reasons why these changes result in reliable and more relevant information on the financial performance, and iii. provide restated comparative figures."
Establishes: the commercial world has the same rule as the ESS — a like-for-like figure is a *defined* figure; change the definition and you must restate the comparators. Strength: strong. Role: LOAD-BEARING for the LFL element.

---

## 6. COMPARATOR SELECTION FOR PLACES

### 6.1 CIPFA Nearest Neighbours Model
URL: https://www.cipfa.org/services/cipfastats/nearest-neighbour-model · At source (official page, thin on method).
Exact: the model "uses statistical processes" to measure similarity; "40 metrics using a wide range of social‐economic indicators"; "The variables employed in making the assessment are all therefore descriptive of characteristics of the area each authority administers and not of the way in which resource of services are taken into account."; "Broadly speaking results and common sense go hand in hand reasonably well."; "Nevertheless, the outcome ultimately relies on the indicators and mathematical procedures used."
**PHE Fingertips, "Comparators Briefing – technical" (Nov 2016)** · URL: https://fingertips.phe.org.uk/documents/Comparators%20Briefing%20-%20technical.pdf · At source. Exact: "For each area, the nearest neighbour is derived by calculating the 'Euclidean distance' to all the other areas' data once they have been standardised to a normal distribution."; areas ranked by shortest distance; CIPFA variables are "descriptive features of the area each authority administers such as population, socio-economic, household and mortality characteristics"; comparator options: "CIPFA nearest neighbours", "Office for National Statistics (ONS) area classifications", "The English Indices of Deprivation", geographical hierarchies, target-based. Caveat: "if the selected comparator includes the factor being compared, the comparison becomes less meaningful. For example, comparing employment indicators with other areas that have a similar Index of Multiple Deprivation (IMD) will not provide full context as employment indicators make up 22.5% of the IMD calculation."; and "comparing areas to other areas within the same region or to a national value may not indicate performance."
Note: the usual "15 nearest neighbours" figure was not confirmed on either official page — do not assert it without a CIPFA technical note. Strength: strong for method shape; moderate for parameters. Role: LOAD-BEARING.

### 6.2 DfE Children's services statistical neighbour benchmarking model — technical report (May 2025)
URL: https://assets.publishing.service.gov.uk/media/682e32faa599d03a16bff3d8/Children_s_services_statistical_neighbour_benchmarking_model_-_technical_report.pdf · At source.
Exact: "Statistical neighbour models are a way for users to compare and benchmark local authority data (performance or otherwise) against meaningful comparators."; method: 23 background variables (reduced from 50 by correlation analysis; mainly Census 2021 plus Ofcom/DfE/PHE/DWP), standardised to mean 0 SD 1, "Weighted Euclidean distance on the standardised background variables", 10 neighbours per LA, weights 1–23 set by iterative optimisation; variables "updated annually"; built at lower geographies so they can be re-aggregated for local government reorganisations.
Establishes: a fully auditable comparator method published by a department — the model case for "comparable places is a modelled claim". Strength: strong. Role: LOAD-BEARING.

### 6.3 ONS 2011 Area Classifications — methodology
URLs: https://www.ons.gov.uk/methodology/geography/geographicalproducts/areaclassifications/2011areaclassifications and …/methodologyandvariables · At source.
Exact: classifications "aim to identify areas of the country with similar characteristics" using "socio-economic and demographic data from each census"; uses include "demonstrating broad geographic patterns, categorising data for further analysis, identifying similar areas for comparative studies and providing information for marketing purposes."; method: "a standard K-means clustering technique"; SOA classification built from "60 final 2011 Census statistics" across five domains, "eight supergroups and 24 subgroups"; Local Authority Classification: "8 supergroups, 16 groups and 24 subgroups" across 391 UK LADs; variables transformed by "inverse hyperbolic sine" with "range standardisation" so each counts equally in the distance.
Strength: strong. Role: SUPPORTING. (2021 OAC/LAC methodology page not fetched.)

### 6.4 LG Inform comparison groups
URL: https://help.lginform.local.gov.uk/faqs/display-and-comparison-groups/display-and-comparison-groups · At source. Standard groups: all English councils; council type; Children's services statistical neighbours; region; Mosaic near neighbours; fire authority groups; CIPFA nearest neighbours; Rural/Urban LA classification; ASC expenditure statistical neighbours. Purpose: to identify "where different approaches in comparable local authorities may yield lessons". COLOUR.

---

## 7. REVISIONS AND VINTAGES (brief)
**ONS Guide to statistical revisions** · URL: https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions/guidetostatisticalrevisions · Exact: "Revisions are updates to previously published statistics, analysis or data that improve quality by incorporating improved methods, additional data sources or statistics that were unavailable at the point of initial publication."; "Correction of errors are amendments that are made to published statistics in response to the identification of mistakes following their initial publication."
**MHCLG statistics revisions policy** · URL: https://www.gov.uk/government/publications/standards-for-official-statistics-published-by-mhclg/statistics-revisions-policy · Exact: scheduled revisions = "Planned changes to published statistics to improve quality by incorporating additional data that were unavailable at the point of initial publication."; unscheduled corrections = "An update to a published output to address mistakes made while producing, publicly sharing and communicating statistics."; material revisions "change the story told by the statistics."; scheduled revisions "will be accompanied by a statement which explains their impact."
[p]/[r] conventions: see 5.4 (Analysis Function). Code 3.0 practice 3.9: see 5.5.
**Real-time vintage** — Federal Reserve Bank of Philadelphia, Real-Time Data Set for Macroeconomists · URL: https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/real-time-data-set-for-macroeconomists · Exact: the data set consists of "vintages, or snapshots, of time series of major macroeconomic variables"; cite "A Real-Time Data Set for Macroeconomists," Dean Croushore and Tom Stark, *Journal of Econometrics* 105 (November 2001), pp. 111-30. One line: a vintage is the series as it stood on a given date; a comparison across dates must say which vintage each number came from. Strength: strong. Role: SUPPORTING.

---

## 8. WHAT A COMPARABILITY DECLARATION MUST CONTAIN (assembled, each element sourced)
Governing test (SDMX/SIMS, 5.3): a comparison is valid to the extent that "differences between statistics can be attributed to differences between the true values" — everything else must be held equal or declared.
1. **Same definition and classification** — ES CoP 14.3 ("common standards with respect to scope, definitions, units and classifications"); UK Code 6.7 ("Use recognised standards, classifications and definitions. Explain reasons for deviations"); GSS harmonisation ("surveys where the questions or definitions are different" are a bad comparison); ESMA ¶20, ¶41 (define the measure; keep the definition constant; restate if changed); Tesco LFL as a worked example.
2. **Same reference period / periodicity** — Reg. 223/2009 Art 12 (comparability "over time"); ES CoP 14.2, 14.4 (different periodicity "compared and reconciled"); ESMA ¶37 (comparatives for "the corresponding previous periods"); Tesco (52-week basis "to aid comparability").
3. **Same geography and same vintage** — UK Code 6.6 ("comparable across and within geographies"); GSS best-fit policy (build from building blocks; state best-fit vs exact-fit); GSS codes policy ("Coding changes will be due to actual boundary changes"; "Codes are not re-used"); ONS training ("ensure you use the correct year"); state the lookup used.
4. **Same method and collection mode** — Reg. 223/2009 (comparability = impact of differences in "concepts, measurement tools and procedures"); UK Code 7.4 ("Be clear about the methods used… comparable across the UK and internationally"); 7.5 (changes announced, "consistent back series where possible").
5. **Same disclosure/suppression treatment** — UK Code 4.5 (apply disclosure control, be transparent about choices); Analysis Function [c] and [low] markers so a suppressed cell is not read as zero.
6. **Breaks in series flagged** — Analysis Function [b] ("data before the break cannot be directly compared with data after the break"); Eurostat LFS practice (break-free series or correction factors; "h" historical tables); Eurostat grading by "data points from last methodological break"; UK Code 7.5.
7. **Revision status stated** — [p]/[r] markers; UK Code 3.9; SIMS "Data revision – policy"; name the vintage (Philadelphia Fed).
8. **Comparator group named and its method stated** — PHE Comparators Briefing (Euclidean distance on standardised variables; don't compare on a factor that is inside the comparator index; national/regional comparison "may not indicate performance"); DfE statistical-neighbour report (23 variables, weighted Euclidean, 10 neighbours — the template of an auditable method); CIPFA ("the outcome ultimately relies on the indicators and mathematical procedures used"); Baxter 2016 ("The methods and criteria used to identify positive deviants must always be stated").
9. **Precision declared, especially for small denominators** — UK Code 7.2 ("estimates of error and confidence"); Fingertips ("particularly important to provide confidence intervals when numbers are small"); Gelman & Price (both tails fill with small units); Spiegelhalter (funnel, not league table).
10. **Outlier handling declared** — Leys ("The threshold should be justified"); Simmons et al. (report results with the excluded observations included); Bakker & Wicherts (protocol set in advance; 41% silent-exclusion signal).

---

## THREADS PULLED (not asked for)
- **Shrinkage flips the artefact** (Gelman & Price): adjusting small-area rates toward the mean does not neutralise the small-denominator problem; it hands the top of the ranking to the big units instead. For a dashboard that means "ranked by raw rate" and "ranked by adjusted rate" are both biased, in opposite directions — the funnel is the only honest picture.
- **Dawson 2011**: under Tukey's rule ≥30% of perfectly normal samples (any size) contain a flagged "outlier"; the rule's false-flag rate is a property of the rule, not the data.
- **Positive deviance has the same undeclared-cut-off disease as outlier removal** (Baxter 2016: criteria "often appeared arbitrary and cut-off points were not justified"). Good-end and bad-end outliers need the same declaration.
- **PHE's circularity warning**: don't benchmark an employment indicator against IMD-matched peers because employment is 22.5% of IMD. A general rule: the comparator model must not contain the outcome.
- **OSR 2025 "meaningful comparability"**: a pragmatic standard — comparable enough "for drawing firm conclusions and for shaping action", with differences documented — useful for a book that must concede perfect comparability never exists.
- **Analysis Function shorthand** is a ready-made dashboard footnote vocabulary ([b], [p], [r], [c], [u], [low], [z], [x]); and it bans "NA".
- **UK Code is now 3.0 (2025)** with new numbering (Standards 1–9, practices 6.6, 7.4, 7.5, 9.3…); older citations to Q2/V3 will not match.

## LEFT OUT and why
- John, Loewenstein & Prelec 2012 QRP survey (self-admitted post-hoc exclusion rates): SAGE paywalled the table; Bakker & Wicherts PLOS ONE covers the point with a measured figure.
- Barnett & Lewis discordant/contaminant formalism and Hawkins at source: books not open; relied on quoted-in sources.
- Huber's own one-liner: unverifiable from here; Hampel at source is a sufficient substitute.
- Goldstein & Spiegelhalter 1996 league tables (JRSS A) and Spiegelhalter 2012 JRSS A: Wiley blocked; the 2005 abstract fragments plus Gelman & Price carry the argument.
- Pascale/Sternin book and HBR: paywalled; Marsh/Bradley are the peer-reviewed statements anyway.
- Zimek & Filzmoser 2018 (WIREs) statistics-vs-data-mining history of outliers: Wiley blocked; interesting but not essential.
- 2021 OAC/LAC methodology, Mosaic, Ofsted statistical neighbours: redundant once DfE and CIPFA are in.
- Lancet critique of PD: none found that is specific; Baxter (BMJ QS) is the substantive methodological critique.

## RICH REFERENCES (three)
1. **Chandola, Banerjee & Kumar 2009** (author copy) — the cleanest conceptual spine: anomaly vs noise, point/contextual/collective, "interestingness" as the defining property.
2. **Gelman & Price 1999** (author copy) — one paper that explains both the raw-rate artefact and why the obvious fix creates a new one; everything about small-denominator outliers on a map or table follows from it.
3. **ESMA APM Guidelines 2015 ¶20/26/37/41** — the most compact, enforceable statement anywhere of what a comparable metric must declare (definition, reconciliation, comparatives, consistency, restate on redefinition); it maps one-to-one onto the ESS/UK statistical standards and is a surprising cross-domain confirmation.

## WHAT SURPRISED ME
- How thin the *official* description of CIPFA's model is: the vendor page gives "40 metrics" and a shrug ("results and common sense go hand in hand reasonably well"); the Euclidean-distance description comes from PHE, and the only fully transparent comparator model I found is DfE's 2025 one.
- Bakker & Wicherts's 41%: not that papers remove outliers, but that two-fifths of papers *claiming no exclusions* have degrees of freedom that don't match their N.
- Dawson's ≥30%: the 1.5×IQR rule guarantees a steady supply of "outliers" from pure noise, which is exactly how a dashboard alert on fences would behave.
- The financial-reporting world (ESMA/Tesco LFL) and the official-statistics world (ESS/UK Code) converge on the same declaration list independently — a strong sign the list in §8 is a general requirement rather than a disciplinary habit.
- NIST's handbook page still carries the typo "prescence" in the key sentence about normality.

---

