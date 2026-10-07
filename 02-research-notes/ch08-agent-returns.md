# Chapter 8 — agent returns, kept whole

*Four research agents, dispatched 6 October 2026 after Entry 8 was framed. Returns are reproduced as handed back; nothing edited. No agent had web search for this sprint.*

---

## Agent A — Freshness, data decay and what a living series commits to

CHAPTER 8 RESEARCH REPORT — FACET: FRESHNESS, DATA DECAY AND WHAT A "LIVING" SERIES COMMITS TO
All fetches made 6 October 2026.

TOOLS AND LIMITS (read first)
- WebSearch: UNAVAILABLE (turn budget exhausted). Everything below is from direct URLs via WebFetch. Shell network access was blocked.
- WebFetch truncates every page at roughly 100-118k characters of text. This cut off the two longest specifications mid-document: the DWBP Recommendation ends inside Best Practice 18, and DCAT 3 ends at section 6.4.18. Everything after those points was unreachable in the Recommendation text.
- WARNING ON FABRICATION: on first pass the reader produced plausible "Why" sentences for DWBP BP21/BP22 and "definitions" for DCAT 3 frequency and temporal resolution that are NOT in the text it could see. I have discarded them. Do not use: "Data that is not up to date may be of limited use to data consumers..." (DWBP) or "The frequency with which changes and additions are made to a resource" / "The minimum spacing of items within a dataset" (DCAT 3).
- Marking: STRING-VERIFIED = confirmed by a second YES/NO presence fetch that also rejected a decoy string. SINGLE PASS = one read only. TWO-PASS = reproduced identically twice but not presence-tested.
- Pages I could not read: JMIR Ivanković et al. 2021 (jmir.org returned empty content twice; doi.org/10.2196/25682 was refused with HTTP 429 and an instruction not to retry; the PMC copy served a reCAPTCHA). Bank of England real-time database (robots.txt disallows). sre.google/workbook/data-processing-pipelines/ is a 404; the chapter lives at /workbook/data-processing/.

ITEM 1 — W3C Data on the Web Best Practices (Recommendation, 31 January 2017) https://www.w3.org/TR/dwbp/
What it is: standard (W3C Recommendation). Strength: high for what was reachable; the freshness and preservation BPs themselves were NOT reachable.
Exact BP names (from the contents list; SINGLE PASS, numbering corroborated by the implementation report for BP20/22/27): BP5 Provide data provenance information; BP6 Provide data quality information; BP7 Provide a version indicator; BP8 Provide version history; BP9 Use persistent URIs as identifiers of datasets; BP11 Assign URIs to dataset versions and series; BP20 Provide real-time access; BP21 Provide data up to date; BP22 Provide an explanation for data that is not available; BP27 Preserve identifiers; BP28 Assess dataset coverage. There is no BP called "Provide data version information" or "Provide data update frequency".
- BP5 Why: "Provenance is one means by which consumers of a dataset judge its quality." "Understanding its origin and history helps one determine whether to trust the data and provides important interpretive context." STRING-VERIFIED. Intended Outcome: "Humans will know the origin and history of the dataset and software agents will be able to automatically process provenance information." SINGLE PASS.
- BP7 Why: "Version information makes a revision of a dataset uniquely identifiable." STRING-VERIFIED. Intended Outcome: "Humans and software agents will easily be able to determine which version of a dataset they are working with." STRING-VERIFIED.
- BP8 Why: "In creating applications that use data, it can be helpful to understand the variability of that data over time." "Interpreting the data is also enhanced by an understanding of its dynamics." STRING-VERIFIED. Intended Outcome: "Humans and software agents will be able to understand how the dataset typically changes from version to version and how any two specific versions differ." SINGLE PASS.
- Data Versioning section intro: "Datasets published on the Web may change over time." "Some datasets are updated on a scheduled basis, and other datasets are changed as improvements in collecting the data make updates worthwhile." STRING-VERIFIED.
- BP11 summary: "Assign URIs to individual versions of datasets as well as to the overall series." Why: "Like documents, many datasets fall into natural series or groups." Both STRING-VERIFIED.
- BP21, BP22, BP27, BP28 and the Data Preservation intro: UNREACHABLE in the Recommendation. Quote nothing from them.
- Draft wording only (First Public Working Draft, 24 February 2015, https://www.w3.org/TR/2015/WD-dwbp-20150224/, superseded; "Provide data up to date" was BP25 there): "Data on the Web availability should closely coincide with data provided at creation time, collection time, or after it has been processed or changed." STRING-VERIFIED in the draft. "When new data is provided or data is updated, it must be published to coincide with the data changes." STRING-VERIFIED in the draft. Summary line "Data must be available in an up-to-date manner and the update frequency made explicit." TWO-PASS. Preservation intro "Data preservation is a well understood and commonly performed task for static and self-contained data." STRING-VERIFIED in the draft. Strength: weak (draft, not the Recommendation).
- DWBP Implementation Report (https://w3c.github.io/dwbp/dwbp-implementation-report.html; accompanies the 30 August 2016 Candidate Recommendation, date SINGLE PASS): "Concerning BP27 none of the data catalog solutions implement it." "In general, when a dataset is not available then just a 404 error message is returned." STRING-VERIFIED. What it is: W3C evidence of implementation. Strength: medium (2016, small sample of catalogue software).
Role: the standard treats version, provenance and series identity as things a publisher states; its own evidence says the retirement half ("Preserve identifiers") was implemented by nobody.

Data Quality Vocabulary (W3C Working Group Note, 15 December 2016, non-normative) https://www.w3.org/TR/vocab-dqv/
- dqv:Dimension: "Represents criteria relevant for assessing quality." "Each quality dimension must have one or more metric to measure it." STRING-VERIFIED.
- dqv:Category: "Represents a group of quality dimensions in which a common type of information is used as quality indicator." STRING-VERIFIED.
- Section 7.2, DQV reproducing ISO/IEC 25012 "Currentness": "The degree to which data has attributes that are of the right age in a specific context of use." STRING-VERIFIED (source quoting ISO).
- Section 7.3, DQV reproducing Zaveri et al.: "Timeliness measures how up-to-date data is relative to a specific task." SINGLE PASS (source quoting someone else).
- "The goal of the Data Quality Vocabulary is not to define a normative list of dimensions and metrics." SINGLE PASS.
Role: both borrowed definitions make freshness relative to a use, not a clock.

ITEM 2 — DCAT 3 (W3C Recommendation, 22 August 2024) https://www.w3.org/TR/vocab-dcat-3/
Reachable (section 6.4, Cataloged Resource):
- update/modification date (dcterms:modified). Definition: "Most recent date on which the resource was changed, updated or modified." STRING-VERIFIED. Usage note: "The value of this property indicates a change to the actual resource, not a change to the catalog record." STRING-VERIFIED. "An absent value MAY indicate that the resource has never changed after its initial publication" STRING-VERIFIED; continuation ", or that the date of last modification is not known, or that the resource is continuously updated." TWO-PASS.
- release date (dcterms:issued). "Date of formal issuance (e.g., publication) of the resource." "This property SHOULD be set using the first known date of issuance." Both STRING-VERIFIED.
- Section 5.1: "dcat:DatasetSeries is a dataset that represents a collection of datasets that are published separately, but share some characteristics that group them." STRING-VERIFIED (from "a dataset that represents" onward).
UNREACHABLE in the spec: Property frequency (dcterms:accrualPeriodicity), temporal resolution, Class Dataset Series (6.7), section 11 Versioning, section 12 Dataset series.
Substitutes, each official in its own right:
- DCAT 3 RDF file (https://raw.githubusercontent.com/w3c/dxwg/gh-pages/dcat/rdf/dcat3.ttl), dcat:DatasetSeries: skos:definition "A collection of datasets that are published separately, but share some common characteristics that groups them." [sic] STRING-VERIFIED. skos:scopeNote "Common scenarios for dataset series include: time series composed of periodically released subsets; map-series composed of items of the same type or theme but with differing spatial footprints." STRING-VERIFIED. changeNote "New class added in DCAT 3." SINGLE PASS.
- DCAT-AP 3.0.0 (SEMIC, 2024-06-14) https://semiceu.github.io/DCAT-AP/releases/3.0.0/ — frequency: "The frequency at which the Dataset is updated."; modification date: "The most recent date on which the Dataset was changed or modified."; release date: "The date of formal issuance (e.g., publication) of the Dataset."; temporal resolution: "The minimum time period resolvable in the dataset."; Dataset Series: "A collection of datasets that are published separately, but share some characteristics that group them."; usage note "It is recommended to avoid Dataset Series without a dataset in the collection." All STRING-VERIFIED.
- DCMI Terms (issued 2020-01-20) https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/accrualPeriodicity/ — "The frequency with which items are added to a collection." STRING-VERIFIED. "Recommended practice is to use a value from the Collection Description Frequency Vocabulary" STRING-VERIFIED.
UK profile (guidance.data.gov.uk, "Accepted DCAT and data.json fields", no date shown; the page now calls the service the "National Data Library directory"):
- frequency / dct:accrualPeriodicity: "The frequency at which dataset is published" then "Format: ISO 8601 Repeating Duration (or `irregular`)"; example values R/P1Y (=annual), R/P1W (=weekly). STRING-VERIFIED apart from the trailing full stop and code formatting. No closed list of values is given.
- "Date the dataset was most recently updated." / "Date the dataset was first published." / "The date period that the dataset applies to." STRING-VERIFIED.
- CKAN fields page, update_frequency: "For example, never, discontinued, annual, quarterly, monthly" SINGLE PASS.
US (DCAT-US Schema v1.1, https://resources.data.gov/resources/dcat-us/, dated November 6, 2014 SINGLE PASS):
- modified: "Most recent date on which the dataset was changed, updated or modified." STRING-VERIFIED. "If there is a need to reflect that the dataset is continually updated, ISO 8601 formatting can account for this with repeating intervals." STRING-VERIFIED. Examples R/P1D, R/P2W, R/PT5M TWO-PASS.
- accrualPeriodicity: "The frequency with which dataset is published." STRING-VERIFIED; "in which case the value should simply be irregular" STRING-VERIFIED.
Strength: high (standards and platform documentation). Role: the vocabularies separate three dates (issued, modified, period covered) and a stated frequency. "Frequency" means three different things across them: items added (DCMI), published (UK/US), updated (DCAT-AP).

ITEM 3 — Timeliness and punctuality
- Eurostat, Statistics Explained "Glossary:Timeliness" (no edit date visible; cites SDMX and the ESS handbook for quality and metadata reports, 2021 re-edition) https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:Timeliness — Timeliness: "the lapse of time between the end of a reference period (or a reference date) and the dissemination of the data". Punctuality: "the possible time lag existing between the actual delivery date of the data and the target date when the data should have been delivered". Both STRING-VERIFIED. Continuation "e.g. dates announced in an official release calendar or previously agreed among partners" SINGLE PASS. Strength: high (official vocabulary).
- European Statistics Code of Practice (revised edition 2017), Principle 13 "Timeliness and Punctuality": "European statistics are released in a timely and punctual way." STRING-VERIFIED but only as image alt text on the Eurostat page; indicators 13.1-13.5 not reachable. The ESS Quality Assurance Framework was not fetched.
- UK Code of Practice for Statistics, cover "Edition 3.0", "Autumn 2025" (both STRING-VERIFIED; the URL path is dated 2026/08). It does NOT define "timeliness" or "punctuality" (SINGLE PASS negative). Practices (numbers TWO-PASS):
 3.1 "Pre-announce the release of statistics with the time and date in a 12-month release calendar" / "Give a specific release date and time four weeks ahead where possible" STRING-VERIFIED.
 3.5 "Release on a timely basis, meeting the needs of users as far as possible" STRING-VERIFIED; "and as soon as the statistics are ready" SINGLE PASS.
 3.6 "Release at the standard time of 9.30am on a weekday" STRING-VERIFIED.
 3.9 "Release revisions and corrections of errors transparently and as soon as possible" + "in line with the organisation's published policy" STRING-VERIFIED; tail "being clear about the nature and scale of change" SINGLE PASS.
 8.4 "Review user satisfaction routinely, considering the relevance, timeliness, accessibility, clarity and accuracy" STRING-VERIFIED.
 9.7 "Give advance notice of material changes to the content of releases, such as the removal of data tables" STRING-VERIFIED; tail "or variables, and any change in the frequency of release" SINGLE PASS.
 10.7 "Ensure that statistics continue to be publicly available, such as through web or data archiving" STRING-VERIFIED.
 2.4 "to cease the production of official statistics that are no longer viable or required" STRING-VERIFIED (it requires Head of Profession approval).
Role: the official vocabulary splits what a dashboard conflates. Timeliness is the lag behind the period described; punctuality is whether the announced date was kept.

ITEM 4 — Link rot and reference rot, measured
- Bowers, Stanton & Zittrain, "What the ephemerality of the Web means for your hyperlinks", Columbia Journalism Review, 21 May 2021 https://www.cjr.org/analysis/linkrot-content-drift-new-york-times.php (the authors' own article on the Harvard study; the report title "The Paper of Record Meets an Ephemeral Web" does not appear on this page and the report itself was not fetched). All STRING-VERIFIED: "We found that of the 553,693 articles within the purview of our study"; "2,283,445 hyperlinks pointing to content outside of nytimes.com"; "Seventy-two percent of those were “deep links” with a path to a specific page"; "Of these deep links, 25 percent of all links were completely inaccessible."; "6 percent of links from 2018 had rotted, as compared to 43 percent of links from 2008 and 72 percent of links from 1998"; "Fifty-three percent of all articles that contained deep links had at least one rotted link."; "Thirteen percent of intact links from that sample of 4,500 had drifted significantly". Content drift of 4% (2019 links) and 25% (2009 links) is SINGLE PASS. Strength: high (large census of one publisher).
- Klein et al., PLoS ONE 9(12): e115253, 26 December 2014 https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253 — "reference rot, the combination of link rot and content drift"; "For over one million references to web resources extracted from over 3.5 million articles"; "We find one out of five STM articles suffering from reference rot, meaning it is impossible to revisit the web context that surrounds them some time after their publication."; "When only considering STM articles that contain references to web resources, this fraction increases to seven out of ten." All STRING-VERIFIED. Strength: high.
- Lawrence et al., "Persistence of Web References in Scientific Research", Computer 34(2), February 2001, pp. 26-31 (author-hosted PDF, https://clgiles.ist.psu.edu/papers/Computer-2001-web-references.pdf) — "The percentage of invalid links in the articles we examined varied from 23 percent in 1999 to a peak of 53 percent in 1994." STRING-VERIFIED. SINGLE PASS: "From the 100,826 articles cited by another article in the database ... we extracted 67,577 URLs."; "A single second searcher was able to locate 80 percent of the URLs reported as lost. As Figure 2b shows, this lowered the overall percentage of lost URLs to only 3 percent." Strength: medium (old, one corpus).
- Pew Research Center, "When Online Content Disappears", 17 May 2024 (Chapekis, Bestvater, Remy, Rivero) — "A quarter of all webpages that existed at one point between 2013 and 2023 are no longer accessible"; "38% of webpages that existed in 2013 are not available today" ... "compared with 8% of pages that existed in 2023"; "23% of news webpages contain at least one broken link, as do 21% of webpages from government sites"; "21% of all the government webpages we examined contained at least one broken link"; "54% of Wikipedia pages contain at least one link in their “References” section that points to a page that no longer exists". All STRING-VERIFIED. Strength: high.
Role: the base rate of decay for anything a dashboard links to or sources from.

ITEM 5 — Dataset decay in government open data
- No measured study of data.gov.uk staleness or withdrawal was reachable (the Data in Government blog search returned empty; no ODI study found by direct URL). Say so in the chapter.
- Open Data Barometer, 4th edition, Web Foundation (published 8 May 2017, modified 11 September 2018, SINGLE PASS) https://opendatabarometer.org/4thedition/report/ — "74% of the data we analysed is up-to-date, which is promising, but means that one quarter of all data surveyed has very limited value." STRING-VERIFIED. "only 7% of the data is fully open"; "only one of every two datasets is machine readable"; "the new US administration has already removed certain key datasets from websites" STRING-VERIFIED. "we assessed 1,725 datasets from 15 different sectors across 115 countries" SINGLE PASS. Strength: medium (global, expert-assessed, dated).
- Global Open Data Index methodology, 2016/2017 https://index.okfn.org/methodology/ — "Data should be updated every [Time Interval]: Is the data up-to-date?" STRING-VERIFIED, worth 15 points. SINGLE PASS: "Answer "No" if you cannot determine a date, or if the data are outdated." The site itself carries: "This is an archived project from the Open Knowledge Foundation and it is no longer active." SINGLE PASS.
- data.gov.uk publisher guidance, "Managing published data" (no date shown) https://guidance.data.gov.uk/publish_and_manage_data/managing_published_data/ — "Do not create new datasets for data you publish regularly, for example monthly spend data." "Instead, create a single dataset and add new data to it." "In the interests of transparency, you should not delete datasets from the National Data Library." "Only the National Data Library team can delete a dataset." All STRING-VERIFIED. SINGLE PASS: "Old datasets can help people compare trends over time, track corrections, and see historical data from organisations that do not exist anymore."
- GOV.UK withdrawal, official form. Live example https://www.gov.uk/government/publications/covid-19-stay-at-home-guidance : "This publication was withdrawn on 24 February 2022" STRING-VERIFIED. Publisher guidance (https://guidance.publishing.service.gov.uk/publish-update-retire-content/standard-content-types/withdraw-unpublish-standard/ ; no date shown; the old gov.uk/guidance/how-to-publish URL redirects here): "withdraw content if it’s no longer current"; "the page will remain on GOV.UK, but it’ll have a banner saying that the content has been withdrawn"; "users will not get an email notification when the page is withdrawn"; template "This page has been withdrawn because it’s out of date." All STRING-VERIFIED. SINGLE PASS: "unpublish content – the page will be taken off GOV.UK completely".
Role: retirement has an official form (stay at the same address, say so, give the date); the measured evidence on portals is thin and old.

ITEM 6 — The heartbeat as a display convention
- Government Analysis Function, "Data visualisation: building and managing dashboards", GSS Presentation Champions, published 6 February 2026 https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-building-and-managing-dashboards/ (the "/policy-store/dashboards/" URL is a 404). All STRING-VERIFIED unless noted:
 "A dashboard is a digital service, which means you must have the skills and resource to continually manage:" ... "the flow of data going into the dashboard" ... "relevance of the dashboard over time"
 "When updating the data in your dashboard, add a change note explaining the change and when it happened."
 "Always make it clear which dates or period your dashboard is relevant to."
 "Dashboards often require more resource than initially identified due to their complexity." "They are not an appropriate project for a single person or for temporary staff."
 "data updates are frequent and can be automated, with users likely to revisit the dashboard" (one of four conditions under "Only consider using a dashboard when:")
 "Retire your dashboard if it is not being maintained or user feedback indicates that it is no longer useful, relevant or providing value for money." (TWO-PASS in this exact form)
 "Add a banner on all pages of the service to let users know the dashboard will be retired and no longer updated." "Do this at least six months before retirement."
 Archiving: "keeping data and metadata available, with a clear note that it is no longer updated and the dates or period the data is associated with" STRING-VERIFIED; "retaining any code used for the dashboard in a public GitHub repository marked as archived" TWO-PASS.
 Suggested banner wording was reproduced twice as "This product is longer updated and will be withdrawn on [month] [year]." (apparent typo for "no longer"; the presence check contradicted itself). Check by eye before quoting; "Once withdrawn, the webpage will remain available via" is STRING-VERIFIED.
 What it is: official guidance. Strength: high, and the closest match to the chapter's question.
- GOV.UK "Write change notes" (no date) https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/change-notes/ — "When you update content on an already published page, you may need to write a change note."; "emailed to anyone who subscribed to the page"; "sometimes published on the page, along with the time and date"; "Do not say the page has been updated without saying what has changed." All STRING-VERIFIED. "Change notes are public." SINGLE PASS. No change note for typo fixes, style changes or broken links (SINGLE PASS).
- GOV.UK page furniture, seen on the withdrawn page: "Updates to this page", "Published: 12 March 2020", "Last updated: 15 February 2022", "Show all updates". SINGLE PASS.
- GOV.UK "Statistics" content-type guidance (no date): "Use a statistics announcement in the statistics release calendar to announce when official statistics or accredited official statistics will be released."; "You must give an exact date at least 4 weeks before your statistics are due to be released."; "add a change note to explain the change of date"; cancellation reason "is a mandatory field which will appear on the website." All STRING-VERIFIED. SINGLE PASS: "If you cancel an announcement, it will remain in the calendar until a month after the planned publication date."
- ONS release calendar https://www.ons.gov.uk/releasecalendar : labels "Release date:", "Published", "Upcoming", "Cancelled", "Provisional" STRING-VERIFIED. Counts on the day (TWO-PASS): Published (9112), Upcoming (413), Cancelled (322). There is no "Next release:" field on the calendar.
- ONS time series page (ABMI) https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/abmi/pn2 : "Release date:", "Next release:", "Series ID: ABMI", "View previous versions" STRING-VERIFIED.
- Google Search Central, "Add a Byline Date to Google Search Results", last updated 2025-12-10 UTC: "Add a user-visible date to the page and feature it prominently." "The dates must describe the publication or update date of the page, not the stories or events described therein." Both STRING-VERIFIED. The phrase "Don't artificially freshen" is NOT on this page.
- US: DCAT-US "modified" and "accrualPeriodicity" (Item 2). Census conventions not fetched. The DfE Analysts' Guide "Public dashboards" page says nothing on dates or retirement. The ONS "Explore local statistics" QMI was not fetched.
Role: UK government guidance already says a dashboard must state its period, log its changes and announce its own end.

ITEM 7 — "Last updated" versus "last revised"
- ONS, "National Accounts Revisions Policy: updated January 2026" (notice dated 31 March 2026, SINGLE PASS; the URL slug still reads "...updateddecember2017") https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions/revisionspoliciesforeconomicstatistics/nationalaccountsrevisionspolicyupdateddecember2017
 "A revision is a scheduled change to any published Office for National Statistics (ONS) output." STRING-VERIFIED.
 "In early estimates of GDP, there is also inherent levels of uncertainty because of the trade-off between timeliness and accuracy." STRING-VERIFIED.
 "Blue Book releases are usually open to revisions for the period back to 1997 (the earliest point for which data are available)." STRING-VERIFIED.
 "Monthly gross domestic product (GDP) publications will only revise previous months in the quarter that the data refers to (the reference period)." STRING-VERIFIED in this form (with "(GDP)").
 "Generally, quarters earlier than the latest quarter are only revised during the second of these releases." STRING-VERIFIED.
 SINGLE PASS: "A correction is an unplanned revision to any published ONS output because of the identification of an error."; "around six weeks – a first quarterly estimate of GDP with an output, expenditure and income breakdown"; "around 12 to 13 weeks – full quarterly national accounts, including a further update".
- ONS dataset "GDP in chained volume measures – revision triangles (ABMI)": "Quarterly and annual growth rates and revisions for UK gross domestic product (GDP), in chained volume measures at market prices." SINGLE PASS.
- ALFRED, Federal Reserve Bank of St. Louis https://alfred.stlouisfed.org/ : "ALFRED® allows you to retrieve each economic data release (vintage) that was available on a specific date in history." STRING-VERIFIED.
- Bank of England real-time database: UNREACHABLE (robots.txt).
Strength: high (official methodology). Role: a published figure's date is not the date its value became final; GDP back to 1997 can still move.

ITEM 8 — Freshness in the data-engineering literature (Google SRE; practice literature, no dates on the pages)
- SRE Workbook, ch. 2 "Implementing SLOs", Table 2-1 "Potential SLIs for different types of components" https://sre.google/workbook/implementing-slos/ — Pipeline SLIs, all STRING-VERIFIED:
 Freshness: "The proportion of the data that was updated more recently than some time threshold."
 Correctness: "The proportion of records coming into the pipeline that resulted in the correct value coming out."
 Coverage: "For batch processing, the proportion of jobs that processed above some target amount of data." "For streaming processing, the proportion of incoming records that were successfully processed within some time window."
 Storage, Durability: "The proportion of records written that can be successfully read."
- SRE Workbook, ch. 13 "Data Processing Pipelines" (Sodt and Maravić with Luo, O'Connor, Ward) https://sre.google/workbook/data-processing/ — all STRING-VERIFIED:
 "Most pipeline data freshness SLOs are in one of the following formats:" "X% of data processed in Y [seconds, days, minutes]." "The oldest data is no older than Y [seconds, days, minutes]." "The pipeline job has completed successfully within Y [seconds, days, minutes]."
 "A pipeline can fail if its input or output is delayed." "Without the proper precautions, a downstream job may start running even though it doesn’t have the necessary data." "Stale data is almost always better than incorrect data." (the last confirmed in three separate passes, under "Delayed data")
 "If undetected, corrupt pipeline data (input and/or output) can cause user-facing issues."
 SINGLE PASS: "Instead, if your pipeline stalls, waits for data, and then resumes once the data becomes available, the data remains high quality."; "Recovering from this kind of data corruption is labor-intensive and difficult to automate."
- SRE Book, ch. 25 "Data Processing Pipelines" (Dan Dennison, ed. Tim Harvey) https://sre.google/sre-book/data-processing-pipelines/ — all STRING-VERIFIED: "the periodic pipeline model is fragile"; "Periodic pipelines are generally stable when there are sufficient workers for the volume of data and execution demand is within computational capacity."; "organic growth and change inevitably begin to stress the system"; "Given a large enough periodic pipeline, for each cycle, potentially thousands of workers immediately start work."; "Delays of up to a few hours might well be acceptable for pipelines that run daily."
Strength: medium-high (practitioner doctrine from one firm, widely adopted). Role: freshness, correctness and coverage are three separate promises, and the doctrine ranks a late number above a wrong one.

ITEM 9 — The cost of staleness to trust
- Stanford Guidelines for Web Credibility (Fogg, May 2002) https://credibility.stanford.edu/guidelines/index.html — guideline 8 of 10: "People assign more credibility to sites that show they have been recently updated or reviewed." STRING-VERIFIED; basis "over 4,500 people" STRING-VERIFIED. The headline was read once as "Update your site's content often (at least show it's been reviewed recently)." and confirmed once with "(or at least ..."; quote the comment sentence, not the headline. Strength: medium (old, perception of credibility, not behaviour with stale data).
- Jakob Nielsen, "Original Top 10 Mistakes in Web Design", 30 April 1996, item 9 "Outdated Information" https://www.nngroup.com/articles/original-top-ten-mistakes-in-web-design/ — "Budget to hire a web gardener as part of your team." "You need somebody to root out the weeds and replant the flowers as the website changes, but most people would rather spend their time creating new content than on maintenance." "Of course, some pages are better off being removed completely from the server after their expiration date." All STRING-VERIFIED. Strength: weak as evidence (expert opinion).
- Open Data Barometer: stale data "has very limited value" (Item 5) — a value judgement, not a user study.
- NOT FOUND: any user study of misread stale dashboards. JMIR COVID-dashboard appraisal unreachable (see top). NN/g "Trustworthiness in Web Design" (2016) had nothing usable on currency. Inside GOV.UK blog search returned empty. Overall strength for this item: WEAK. The chapter should not claim measured evidence that users distrust stale dashboards on the strength of this.

ITEM 10 — Series and continuity
- DCAT: Dataset Series definitions and "time series composed of periodically released subsets" scope note (Item 2). DWBP BP11 "Assign URIs to individual versions of datasets as well as to the overall series." (Item 1). DWBP BP27 "Preserve identifiers": title only, body unreachable; implementation report says no catalogue implemented it.
- ONS series identifier: "This series ID is a unique random identifier for this individual time series." "The digits themselves do not have any specific meaning" Both STRING-VERIFIED (ABMI page). The time series explorer (https://www.ons.gov.uk/timeseriestool) labels results "Released on:", "Series ID:", "Dataset ID:" and does not use the term "CDID" (SINGLE PASS).
- data.gov.uk: one dataset, added to, not a new dataset per period (Item 5).
Role: a series is the thing with the stable name; each release is a member of it.

UNEXPECTED THREADS
1. HTTP's own definition of fresh and stale, RFC 9111 (HTTP Caching, June 2022, Standards Track) https://www.rfc-editor.org/rfc/rfc9111.html — "A "fresh" response is one whose age has not yet exceeded its freshness lifetime." "Conversely, a "stale" response is one where it has." "A response's "freshness lifetime" is the length of time between its generation by the origin server and its expiration time." "A cache MUST NOT generate a stale response unless it is disconnected or doing so is explicitly permitted by the client or origin server" "A typical setting of this fraction might be 10%." All STRING-VERIFIED. Freshness in the web's plumbing is a declared lifetime, not a property of the data.
2. DCAT-US lets the "modified" (Last Update) field hold a repeating interval such as R/P1D instead of a date: the last-updated field can carry a promise rather than a fact.
3. DCAT 3 says an absent modified date can mean three opposite things: never changed, unknown, or continuously updated.
4. data.gov.uk's publisher documentation now names the service the "National Data Library", and its search page title reads "Search directory - National Data Library" (SINGLE PASS). Deletion is discouraged and reserved to the central team.
5. The instruments that measured open-data freshness have themselves stopped: the Global Open Data Index is "an archived project ... no longer active"; the Barometer page was last modified in 2018.
6. Lawrence et al.: 80% of "lost" URLs could be found again by a second searcher, cutting true loss to 3% (SINGLE PASS). Rot of the address is not always loss of the content.
7. Harvard Library Innovation Lab, "Announcing the Data.gov Archive", 6 February 2025: "The 16TB collection includes over 311,000 datasets harvested during 2024 and 2025"; "a complete archive of federal public datasets linked by data.gov"; "It will be updated daily as new datasets are added to data.gov." All STRING-VERIFIED. A third party now keeps the heartbeat for a government catalogue.
8. On 6 October 2026 the ONS ABMI time series page and the revisions-triangle dataset page both read "Next release: 30 September 2026", a date already past (SINGLE PASS; may be a cached copy on the fetch side). Unconfirmed, but if real it is the chapter's point in miniature.

LEFT OUT AND WHY
- DWBP BP21/22/27/28 and Data Preservation text; DCAT 3 sections 6.6, 6.7, 11, 12: beyond the fetch truncation point.
- ISO/IEC 25012 and ISO 8000 originals: paywalled; only DQV's reproduction used. GSBPM: not fetched.
- ESS Quality Assurance Framework and ESS Handbook PDFs: the Eurostat glossary gave the definitions and cites the handbook.
- Bank of England, JMIR, any ODI report, US Census conventions, ONS "Explore local statistics" QMI, retail sales revisions policy: unreachable or not attempted within the two-attempt rule.
- Portal Watch (WU Vienna, https://data.wu.ac.at/portalwatch/): reachable but only its self-description read ("a scalable quality assessment and evolution monitoring framework for Open Data (Web) portals", SINGLE PASS); its freshness papers were not located without search.
- GOV.UK "history mode": the page reached does not define it.

RICH REFERENCES
1. Government Analysis Function, "Data visualisation: building and managing dashboards" (6 February 2026). The only official UK text found that covers a dashboard's whole life, including a six-month retirement notice and archiving the code.
2. Google SRE Workbook, ch. 13 "Data Processing Pipelines" with ch. 2 Table 2-1. Gives freshness, correctness and coverage as separate, measurable promises, plus "Stale data is almost always better than incorrect data."
3. Pew Research Center, "When Online Content Disappears" (17 May 2024), read alongside Bowers, Stanton & Zittrain (CJR, 2021). The best current base rates for decay, including government pages.

WHAT SURPRISED ME
- The reader invented clean, standards-sounding sentences for sections it could not see. Three of my first-pass "quotations" were fabrications that only the presence check caught.
- "Frequency" is defined three incompatible ways across DCMI, the UK/US profiles and DCAT-AP, and the W3C's own evidence says no catalogue implemented "Preserve identifiers".
- UK official guidance is more demanding than expected: a dashboard is "not an appropriate project for a single person", which bears directly on a small studio.
- The UK Code of Practice 3.0 uses "timely" and "timeliness" but never defines them; the precise definitions are Eurostat's.
- The evidence that stale displays cost trust is far thinner than the evidence that things go stale.
---

## Agent B — APIs and platform dependency

CHAPTER 8 — FACET: APIs AND PLATFORM DEPENDENCY. Research report, 6 October 2026.

METHOD AND TOOLING
- WebSearch was NOT available (the turn's shared search budget was already used up). Direct shell download (curl) was blocked by the egress proxy. Everything below came from WebFetch on direct URLs.
- Every quotation is marked STRING-VERIFIED (SV: a second fetch of the same URL confirmed the exact string with a YES/NO prompt) or SINGLE PASS (SP: seen once, or only as the reader's answer to a "quote the sentence" prompt).
- The reader truncates pages at roughly 100–120k characters. That made RFC 9110 §10.2.3 unreachable.
- Several things the brief expected to find are no longer true or not on the page. They are flagged "NOT FOUND" inline and collected under "Surprised".

====================================================================
ITEM 1 — UK GOVERNMENT API STANDARDS
====================================================================

1a. GDS, "API technical and data standards"
URL: https://www.gov.uk/guidance/gds-api-technical-and-data-standards
Dates: Published 7 February 2018; Last updated 19 July 2024 (confirmed on a second pass).
Type: official guidance (mandatory-style "must/should" for government API builders). Strength: high as a statement of UK government expectation; thin on operations.

Section "Version your API and support older versions" (the reader's label for it):
- "When you make new versions of your API, try not to make changes that will stop older versions of your API working properly." SV
- "If you cannot keep older versions working you should expose a new version of your API by adding the version number into the URI, for example https://myapi.service.gov.uk/v1." SP
- "You should try to keep the number of active versions of your API to a minimum, and encourage users to move to the latest version, to reduce the overhead of maintaining multiple versions." SV (returned identically on two passes)
- "You can think about retiring older versions of an API if you can tell from the logs that only a few people are using them anymore." SV
- "When you retire an old version you must tell users it is no longer supported and give them time to move on to the new version." SV

Section "Consider performance and scalability" (reader's label):
- "You should also implement rate limiting or throttling policies – making sure that users don't overuse your resources" SV
- "Anonymous endpoints should also be rate limited to prevent excessive or malicious use." SV

Section "Develop a specification before you start to code" (reader's label):
- "The OpenAPI Specification is a standardised way of describing RESTful web APIs, and is recommended by the government Open Standards Board." SV

NOT FOUND on this page (checked explicitly):
- No "deprecation period" wording.
- No "do not break backward compatibility", "backwards compatible" or "breaking change".
- No sentence on SLA, service level, availability or uptime.
- The sentence "Set clear API deprecation policies so you're not supporting old client applications forever" is not on the current page. The collection lists an archived "API technical and data standards (v1 - 2018)", which I did not fetch.

Role: the standard commits a publisher to tell users and "give them time". It sets no period and no availability figure. Those sit in the two sibling guides below.

1b. GDS/CDDO, "Managing your live API"
URL: https://www.gov.uk/guidance/managing-your-live-api
Dates: Published 27 November 2020. The first pass reported "Last Updated 9 September 2026"; the second pass said no "Last updated" label is in the body. Treat the update date as unconfirmed.
Section "Deprecating your API or a version of it":
- "You will need to give your users notice before you deprecate or retire your API, or an older version of it, so they have time to transfer over to your current version." SV
- "You should try to give users 6 months notice if your API is 'live'." SV (the page may use curly quotes)
- "You do not need to give as much notice if your API is in alpha or beta where your users are expecting breaking changes." SP
- "Keep older versions of your API running to allow your users time to migrate." SV
- "Normally, you will deprecate your API first and this will still allow users to access it, even though you will not be actively supporting their use. You should then retire your API so it is no longer visible." SP
- "You might have to deliver any breaking API changes as a new version of your API." SP
- The page does not mention Sunset or Deprecation HTTP headers or 410 Gone (checked).
Type: official guidance. Strength: high. This is the one number in UK guidance: six months, as "should try", and only for "live" APIs.
Role: the yardstick for platform behaviour. Beta APIs are explicitly exempt, and most of the public APIs in item 3 label themselves beta.

1c. GDS/CDDO, "Setting API service levels"
URL: https://www.gov.uk/guidance/setting-api-service-levels
Dates: Published 16 January 2019; page metadata "Updated at: 2026-09-09T14:55:03+01:00" (reader-reported; no body "Last updated" label).
- Opening: "When managing your API as a service, you need to understand what matters to your users and what you'll commit to in your service level agreement." SP
- "High service levels can be expensive to deliver, so you should not set them higher than necessary." SV
- "For instance, your API could drop 1 in 20 connections or it could be unreachable for 2 hours a day." SV. The first pass gave the continuation: "Both of these scenarios could result in the same percentage of uptime but one of them may be more problematic for users." SP
- "For example, use X-RateLimit_remaining in the header to let them know when they are close to your limit" SV (underscore as on the page)
- "When applying rate limiting or throttling, you should not let your users go over the limits you set even if you have spare capacity." SV. Next sentence: "This is because if you need to take the spare capacity away in future and the user has developed their application with the higher rates in mind, their application could break." SP
- No sentence on status pages or planned maintenance windows (checked).
Type: official guidance. Strength: high.
Role: the provider-side account of why a stated limit is the real limit, and why "uptime %" hides the shape of failure.

1d. "API design guidance" collection
URL: https://www.gov.uk/government/collections/api-design-guidance
Publisher: Government Digital Service and Central Digital and Data Office. Published 15 February 2019; last updated 11 July 2022.
Description: "Guidance on designing, building and running application programming interfaces (APIs), as well as standards for delivering the best service to users." SP
Contents: API technical and data standards; Using GraphQL for your API; Defining an API management strategy; Managing APIs to meet user needs; Managing your API discovery / alpha / beta; Managing your live API; Setting API service levels; Get an API domain on GOV.UK; Documenting APIs; Writing API reference documentation; archived v1 (2018).

1e. UK government API catalogue
URL: https://www.api.gov.uk/ — no date shown.
- "This catalogue is for APIs published by public sector organisations in the UK." SP
- No count of APIs is stated on the page. The reader's "50+ departments" was its own estimate; do not use it.

1f. Technology Code of Practice
URL: https://www.gov.uk/guidance/the-technology-code-of-practice — Published 14 July 2021; Last updated 7 July 2025 (as the page gives them).
- Point 3 "Be open and use open source": "Publish your code and use open source software to improve transparency, flexibility and accountability." SP
- Point 4 (titled "Make use of open standards" on the page): "Build technology that uses open standards to ensure your technology works and communicates with other technology, and can easily be upgraded and expanded." SP
- Point 10 "Make better use of data": "Use data more effectively by improving your technology, infrastructure and processes." SP
Role: background only; nothing operational.

====================================================================
ITEM 2 — RATE-LIMIT SEMANTICS IN THE STANDARDS
====================================================================

2a. RFC 6585, "Additional HTTP Status Codes", §4 "429 Too Many Requests"
URL: https://www.rfc-editor.org/rfc/rfc6585 — April 2012; Standards Track (Proposed Standard); M. Nottingham, R. Fielding.
- "The 429 status code indicates that the user has sent too many requests in a given amount of time ("rate limiting")." SV
- "The response representations SHOULD include details explaining the condition, and MAY include a Retry-After header indicating how long to wait before making a new request." SV
- "Note that this specification does not define how the origin server identifies the user, nor how it counts requests." SV
- "For example, an origin server that is limiting request rates can do so based upon counts of requests on a per-resource basis, across the entire server, or even among a set of servers." SP
- "Responses with the 429 status code MUST NOT be stored by a cache." SV
Type: standard. Strength: definitive.
Role: Retry-After is only a MAY, and the counting is undefined. A client cannot rely on being told when to come back.

2b. RFC 9110 §10.2.3 Retry-After — UNREACHABLE AT SOURCE
Two attempts (rfc9110 HTML and .txt) were truncated by the reader before §10. RFC 9110 header details seen: HTTP Semantics, Internet Standard (STD 97), 2022. Nothing quoted from it.
Secondary, clearly marked: MDN, https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After (last modified November 21, 2025), which cites "HTTP Semantics # field.retry-after":
- "The HTTP Retry-After response header indicates how long the user agent should wait before making a follow-up request." SP (MDN's wording, not the RFC's)
- MDN lists three uses: 503 ("how long the service is expected to be unavailable"), 429 ("how long to wait before making a new request"), and redirects. SP

2c. IETF draft "RateLimit header fields for HTTP"
URL: https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
- Version draft-ietf-httpapi-ratelimit-headers-11, dated 23 May 2026; expires 24 November 2026.
- WG state "WG Document"; IESG state "I-D Exists"; Intended RFC status "(None)". The first pass said "Standards Track (None currently assigned)"; the datatracker field reads "(None)" on the second pass.
- Authors: Roberto Polli (Team Digitale, Italian Government), Alejandro Martínez Ruiz (Red Hat), Darrel Miller (Microsoft).
- Abstract: "This document defines the RateLimit-Policy and RateLimit HTTP header fields for servers to advertise their quota policies and the current service limits, thereby allowing clients to avoid being throttled." SV
- Fields: RateLimit-Policy and RateLimit.
Type: Internet-Draft, not a standard. Strength: status fact is solid.
Role: in October 2026 there is still no standard header for advertising a quota. Every platform below invents its own (X-RateLimit_remaining in GDS guidance, Rate-Limit-Available at Ticketmaster, X-Ratelimit-Remaining at Reddit).

====================================================================
ITEM 3 — PUBLIC UK APIs: STATED LIMITS AND TERMS
====================================================================

3a. TfL Unified API
- FAQ, https://api-portal.tfl.gov.uk/faq (no date): "General users are able to access the main Product called "500 Requests per min" which lets users make 500 requests a minute against our Unified API." SV. "User accounts that haven't made a request in the last year will be automatically disabled and deleted." SV. "For large-volume requests please contact us by email." SP
- Products, https://api-portal.tfl.gov.uk/products (no date): "Anonymous access to our API is limited to 50 requests a minute." SV. "Customers are able to apply online here for the "500 requests a minute" Product which should cover most use-cases, but higher quotas are available upon request." SP
- Terms, https://tfl.gov.uk/corporate/terms-and-conditions/transport-data-service (no version date; attribution text cites 2016 and 2019):
  - "These licence terms and conditions apply to TfL's free transport data service and are based on version 2.0 of the Open Government Licence with specific amendments for Transport for London." SP
  - "Limit traffic requests up to a maximum of 500 calls per minute per data feed." SV. Following: "TfL reserves the right to throttle or limit access to feeds when it is believed the overall service is being degraded" SP
  - "Acknowledge TfL as the source of the Information by including the following attribution statement 'Powered by TfL Open Data'" SV on the phrase
  - "TfL does not guarantee the continued supply of the Information." SV
  - "TfL may at any time revise this Licence without notice." SV
  - No caching clause (checked).
Type: platform documentation plus licence. Strength: high.
Role: the generous end of the range. Note the dormant-account deletion after a year, which will hit a low-traffic unattended job.

3b. Companies House Public Data API
URL: https://developer-specs.company-information.service.gov.uk/guides/rateLimiting (no date)
- "Rate limiting is applied to the Companies House API to ensure a high-quality service is delivered for all users, and to protect client applications from unexpected loops." SP
- "You can make up to 600 requests within a five-minute period." SV
- "If you exceed this limit, you will receive a `429 Too Many Requests` HTTP status code for each request made within the remainder of the five-minute window." SP
- "We reserve the right to ban without notice applications that regularly exceed or attempt to bypass the rate limits." SV
Role: a fixed-window limit stated plainly. The "unexpected loops" clause shows rate limits framed as protecting the client from its own bug.

3c. ONS
- Developer hub, https://developer.ons.gov.uk/ (no date):
  - "This API is currently in Beta and still being developed." SV
  - "Please be aware that as a result of this there may occasionally be breaking changes as we enhance functionality and respond to feedback." SV
  - "The API is open and unrestricted - no API keys are required, so you can start using it immediately." SV
- "Guide to rate limiting and bot development", https://developer.ons.gov.uk/bots/ (no date):
  - "120 requests per 10 seconds - all site and API assets"; "200 requests per 1 minute - all site and API assets"; "15 requests per 10 seconds - high demand site assets". SV on all three figures.
  - "If you exceed these limits, the API will return a 429 Too Many Requests HTTP status code and a Retry-After header containing the number of seconds until you may try your request again." SV
  - "Your tooling should respect the Retry-After header and pause your requests for the specified duration." SP
  - "If this is not respected our algorithms may impose a block to our services for up to 1 hour." SV
  - "The time for which you will be blocked varies and is dynamically changed by the ONS, depending on release schedules and observed demand." SV
- "Guide to retirement of API endpoints", https://developer.ons.gov.uk/retirement/ (no date):
  - "This guide documents our approach to the retirement of API endpoints and what users can expect when an endpoint is going to be retired." SP
  - Headers used: "Deprecation (the date the decision was taken to deprecate this endpoint)" SP; "Sunset (the date of when this service will cease to return data on its endpoints and instead return blanket 404 status codes)" SV; "Link (a link where you can find more information)" SP
  - "When an endpoint is retired, 404 error codes will be received by clients still querying the endpoint." SV
  - "Rolling blackouts can be used to determine if any further users are impacted" SP
  - No minimum notice period is stated (checked).
- ONS Open Geography Portal, https://geoportal.statistics.gov.uk/ — JS-rendered. Only the meta description came back ("The UK's official Office for National Statistics Open Data Geography Site", SP). Terms not reached; nothing quoted.
Type: platform documentation by a public body. Strength: high.
Role: a UK statistical API that is "open and unrestricted" and still declares beta, breaking changes, dynamic blocking tied to release days, and deliberate rolling blackouts before retirement.

3d. Nomis API
URL: https://www.nomisweb.co.uk/api/v01/help (no date)
- "You have a 25000 cell limit on the number of data values downloaded in these formats." SV (CSV/TSV section; repeated per format). KML and RSS show "1000 cell limit" SP.
- "Use of the API key is optional. If you do not use an API key, then you will be an anonymous 'guest' user, the size of download will be limited to 25,000 cells." SP
- "To use the API without cell limits, you need to specify either your Unique ID for server-side calls (treat your Unique ID like a password, never pass it on to third parties) or your Signature for publically viewable URIs when you first create your RESTful URI." SP (spelling as on the page)
- No 1,000,000 limit is stated on this page (checked).
Role: a volume cap, not a rate cap. A refresh job has to page through results.

3e. data.gov.uk
- API doc, https://guidance.data.gov.uk/get_data/api_documentation/ (no date): "The directory API uses the CKAN API and its extensions." SV. "You do not need an API key to use the API and there are no rate limits." SV. Base URL given as https://data.gov.uk/api/action/. "Curated collections are not yet available via the API" SP
- About, https://www.data.gov.uk/about:
  - "Since 2010, the data.gov.uk website, now known as the National Data Library, has been helping people to find and use open government data." SV on "now known as the National Data Library"
  - "In early 2026, we started transforming the data.gov.uk website into the UK National Data Library." SV
  - "On the directory, you can: find links to data published by central government, local authorities and public bodies." SP
  - "You can republish any of the content available on the National Data Library as long as you meet the conditions of either the Open Government Licence or another licence it's covered by." SP
- NOT FOUND: an explicit sentence that datasets are hosted by publishers and only catalogued. The nearest is "find links to data".
Role: the catalogue is a directory of links, so each dataset's durability is its publisher's. The catalogue itself is mid-rebrand.

3f. Police API (data.police.uk)
- Call limits, https://data.police.uk/docs/api-call-limits/ (no date):
  - "The Police API call limit operates using a 'leaky bucket' algorithm as a controller." SP
  - "The current rate limit is 15 requests per second with a burst of 30." SV
  - "If you exceed the limit stated above, the API will return a HTTP 429 (Too Many Requests) response code." SP
- About, https://data.police.uk/about/ (no date):
  - "Frequency: Monthly" SV. The string "data is updated monthly" is not on the page; no publication lag is stated.
  - "The latitude and longitude locations of Crime and ASB incidents published on this site always represent the approximate location of a crime — not the exact place that it happened." SP
  - "We maintain a master list of anonymous map points." SP
  - "Each map point is specifically chosen so that it: Appears over the centre point of a street, above a public place such as a Park or Airport, or above a commercial premise like a Shopping Centre or Nightclub." SP
  - "Has a catchment area which contains at least eight postal addresses or no postal addresses at all." SV
  - "When crime data is uploaded by police forces, the exact location of each crime is compared against this master list to find the nearest map point." SP
  - "If the nearest map point is more than 20km away, the co-ordinates are zeroed out." SV
  - "The snap points list was created in 2012 and based on Ordnance Survey population and housing developments relevant to that year. The snap points list was refreshed in 2022 using more recent data from the same sources." SP
  - "Inconsistent geocoding policies in police forces mean we cannot be confident that the location data provided is fully accurate or consistent." SV
  - Licence: Open Government Licence v3.0.
Role: a boundary on what a map can honestly show. Points are snapped to a fixed list, and commercial premises are named as snap targets. I quote this as the publisher's method text only.

3g. Ordnance Survey
- Plans page, https://osdatahub.os.uk/plans and /support/plans — JS-only ("You need to enable JavaScript to run this app"). A guessed product URL returned 404. UNREACHABLE: the free OpenData allowance and the "£1,000 of free premium transactions" figure are NOT verified. Do not print them from memory.
- Rate limiting policy, https://docs.os.uk/os-apis/core-concepts/rate-limiting-policy (no date):
  - Live-mode projects: "Limit: 600 transactions per minute." SV on the figure, applied "per API and per individual project" SP
  - Development-mode projects: "Limit: 50 transactions per minute." SV on the figure
  - "If the rate limit for an API is exceeded, subsequent requests will be rejected (429) until the rate falls below the allowed threshold." SV
- OS Open Zoomstack, https://www.ordnancesurvey.co.uk/products/os-open-zoomstack (footer © 2026):
  - "An open vector basemap at multiple levels of resolution, showing coverage of Great Britain from a national level, right down to street detail." SV
  - "This product is updated every six months" SP; "Free to use for everyone" SP; "Format: GeoPackage, Vector Tiles" SP; "Data access: Download and API" SP
  - The words "Open Government Licence" were not returned from this page. The OGL basis for Zoomstack is unconfirmed here.
- OS Maps API, https://www.ordnancesurvey.co.uk/products/os-maps-api: "Accurate, up-to-date maps that offer a convenient way to add detailed OS data to your application." SP. Plans listed: OS OpenData Plan (FREE), Premium Plan, Public Sector Plan. SP
Role: a basemap that can be downloaded and self-hosted on a six-month cadence, set against an API basemap with per-minute throttles.

3h. OpenStreetMap Foundation policies (neither page shows a date)
- Nominatim Usage Policy, https://operations.osmfoundation.org/policies/nominatim/:
  - "No heavy uses (an absolute maximum of 1 request per second)." SV
  - "Provide a valid HTTP Referer or User-Agent identifying the application (stock User-Agents as set by http libraries will not do)." SV
  - "Results must be cached on your side. Clients sending repeatedly the same query may be classified as faulty and blocked." SV
  - "Scripts running longer than a day and scripts that are run at regular intervals are restricted to 4 requests per minute." SP (returned identically on two passes)
  - "Auto-complete search This is not yet supported by Nominatim and you must not implement such a service on the client side using the API." SP
  - "Please be aware that this usage policy may change without notice. In particular, the definition of heavy use may need to be modified in the future and you might have your access withdrawn." SP
  - "Data is provided under the ODbL license which requires to share alike (although small extractions are likely to be covered by fair usage / fair dealing)." SP
  - Capacity: "the service runs on donated servers and has a very limited capacity." SP (fragment)
- Tile Usage Policy, https://operations.osmfoundation.org/policies/tiles/:
  - "OpenStreetMap (OSM) data is free for everyone to use. Our tile servers are not: they are funded by donations and sponsorship, and capacity is limited." SP
  - "Availability is best-effort: there is no SLA or guarantee." SV
  - "We may block access, without notice, if your usage degrades the service." SV
  - "Cache tiles locally according to HTTP caching headers (or at least 7 days if your cache cannot read them)." SV
  - "Send a valid HTTP User-Agent that clearly identifies your application" SP; "From web pages, ensure a valid HTTP Referer header is sent" SP
  - Under "You must not:" — "Bulk download ("scrape") tiles or offer prefetch features." SV
  - "Offline use is not permitted on tile.openstreetmap.org." SV
  - "If you cannot meet these requirements, please use an alternative OSM-derived service (see below), or run your own." SP
  - NOT FOUND: "forbidden without prior permission". The policy has been rewritten since that wording.
Type: operator policy. Strength: definitive for these services.
Role: the clearest "free data, not free servers" statement. The Nominatim scheduled-script rule (4 per minute) bears directly on any cron-driven geocoding.

3i. Two further APIs chosen
- Food Standards Agency FHRS API (venue-relevant: ratings for premises)
  - https://api.ratings.food.gov.uk/help (no date): "The FHRS API provides free programmatic access to the Food Standards Agency Rating Data for England, Scotland, Wales and Northern Ireland." SV
  - "If a version is not supplied in the header, calls to FHRS API endpoints will not return data." SV
  - "The FSA will maintain at least one previous depreciated version of the API to allow developers to migrate their code steadily, however the FSA make no guarantees that older versions of the API will continue to work when they fall more than one version behind the current API." SP (returned identically on two passes; "depreciated" is the page's spelling)
  - https://ratings.food.gov.uk/open-data: "The XML data are updated daily and can be found below, grouped by local authority." SP. "The API can also be used to query the live system (the data are automatically updated as local authorities upload and publish data)" SP. "This is a free service and there is no need to register to use it." SP. The page says "Terms and conditions apply"; it does not name the OGL (checked). V1 guidance "updated April 2024".
- Environment Agency real-time flood-monitoring API, https://environment.data.gov.uk/flood-monitoring/doc/reference (no date; labelled beta):
  - "These APIs are provided as open data under the Open Government Licence with no requirement for registration." SV
  - "While they are intended to be stable and robust the open data APIs do not offer a guarantee of service level and should not be relied upon for safety critical applications." SV
  - "The efficient way to do this is to issue a single call every 15 mins: https://environment.data.gov.uk/flood-monitoring/data/readings?latest" SP
  - "API responses may be cached for a short period within the serving infrastructure or a content delivery network." SP
  - Attribution wording: "this uses Environment Agency flood and river level data from the real-time data API (Beta)" SP
  - "beta This is a trial service – your feedback will help us to improve it." SP
- DfT Bus Open Data Service: the URL I tried returned 404. Not pursued.

====================================================================
ITEM 4 — TICKETING PLATFORM INTERFACES (technology only; no listings fetched)
====================================================================

4a. Skiddle
- https://www.skiddle.com/api/ (footer © 2001-2026):
  - "The Skiddle API has been developed to follow RESTful principles where possible (and not overly complicated)." SP
  - "Please note, the Skiddle API is still in Beta and being developed." SP
  - "All requests require a valid API key." SP
  - "We monitor all requests and reserve the right to rate-limit or block any excessive requests. Limits are continually changed - please contact us if you are expecting to hit our API frequently." SV
  - "The API is for non-commercial use only. Any commercial use must be first approved in writing by emailing dev@skiddle.com" SV
  - No attribution or link-back sentence on this page (checked).
- https://github.com/Skiddle/web-api: banner "This repository was archived by the owner on Apr 30, 2024. It is now read-only." SV. The README documents three endpoint groups only: events (search, detail), venues, artists, under /api/v1/. "All requests must be made over HTTPS (TLS v1.2+)" SP. 24 commits.
- No endpoint for sales, orders, transactions or attendance appears in either source (checked). It is a listings interface.
- https://www.skiddle.com/terms/ is an index of separate documents; no API clause was readable there.
Type: platform documentation. Strength: high for what is stated. There is no numeric limit to cite because the platform declines to give one.
Role: a limit that is "continually changed", a beta label, a non-commercial default, and documentation in an archived repository.

4b. Ticketmaster
- Getting started, https://developer.ticketmaster.com/products-and-docs/apis/getting-started/ (no date):
  - "All API keys are issued with a default quota of 5000 API calls per day and rate limitation of 5 requests per second." SV
  - Quota headers: Rate-Limit, Rate-Limit-Available, Rate-Limit-Over, Rate-Limit-Reset. SP
  - On breach, HTTP 429 with faultstring "Rate limit quota violation. Quota limit exceeded." SP
  - "We do increase rate limits on case-by-case basis. In order to increase the rate limit for a particular application, we need to verify the following: 1. The application is in compliance with our Terms of Service 2. The application is in compliance with our branding guide 3. The application is representing the Ticketmaster data properly" SP (first sentence returned on both passes)
- Discovery API v2, https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/:
  - "The Ticketmaster Discovery API allows you to search for events, attractions, or venues." SV
  - "Deep Paging: we only support retrieving the 1000th item. i.e. ( size * page < 1000)" SP
  - "The API provides access to content sourced from various platform, including Ticketmaster, Universe, FrontGate Tickets and Ticketmaster Resale (TMR)." SP (grammar as on the page)
  - The reader found no fields for tickets sold or attendance. Reader judgement on the first 100k characters only.
- Terms of Use, https://developer.ticketmaster.com/support/terms-of-use/ — "Last Updated: June 27, 2023". The reader returned headings, not section numbers.
  - Under licensed uses / "shall not": "Cache or store any Event Content other than for reasonable periods in order to provide the service you are providing." SV. (The reader answered "NO" because it is a prohibition, but reproduced the identical string on both passes.)
  - "Use the Ticketmaster API for any application that replicates or attempts to replace the unique essential user experience of Ticketmaster.com or the Ticketmaster apps." SP
  - "Sell, lease, or sublicense the Ticketmaster API or access thereto or derive revenues from the use or provision of the Ticketmaster API, whether for direct commercial or monetary gain or otherwise, except as set forth below." SP
  - "We reserve the right to rate limit or block applications that make a large number of calls to the API that are not primarily in response to direct user actions." SV
  - "Ticketmaster may change, suspend, or discontinue any aspect of the Ticketmaster API at any time, including the availability of any Ticketmaster API." SV. Next: "Ticketmaster may also impose limits on certain features and services or restrict your access to parts or all of the Ticketmaster API or the Ticketmaster Web site without notice or liability." SP
  - Definition fragment: "Ticketmaster content (event name, dates, times, venue name, and additional information such as Tickets, Attendees, Orders ("Event Content")" SP
  - "THE API, API-WEBSITE AND ASSOCIATED MATERIALS ARE PROVIDED ON AN 'AS IS' AND 'AS AVAILABLE' BASIS." SP
  - No clause on aggregating with other providers, on attribution or link-back, or on refresh intervals was found in the terms (checked). Branding sits in a separate "branding guide" that I did not fetch.
Role: the rate-limit sentence is aimed at scheduled, non-user-driven calling, which is what an unattended refresh job does.

4c. Eventbrite — UNREACHABLE
- The changelog, API reference, rate-limits and events docs pages on eventbrite.com/platform are JS-only shells (four URLs tried). Nothing quoted.
- NOT VERIFIED: the removal of /events/search/, its date, and "1,000 calls per hour".
- One technical observation, weak: an unauthenticated GET of https://www.eventbriteapi.com/v3/events/search/ returned HTTP 404 on 6 October 2026. That is consistent with removal but is not Eventbrite's statement.

4d. DICE, Resident Advisor, See Tickets, Fatsoma (one attempt each, developer pages only)
- DICE: https://dice.fm/partners mentions no API, developers or integrations. https://partners-endpoint.dice.fm/graphql/docs returned HTTP 401. Record as "no public developer documentation found; a partner endpoint exists behind authentication".
- Resident Advisor: https://ra.co/developers returned 404. No public developer documentation found.
- See Tickets: https://www.seetickets.com/developers returned 403. Could not determine.
- Fatsoma: https://www.fatsoma.com/developers served only the web-app shell. No public developer documentation found.

====================================================================
ITEM 5 — STREAMING PLATFORM INTERFACES (technology only)
====================================================================

5a. Spotify Web API
- Rate limits, https://developer.spotify.com/documentation/web-api/concepts/rate-limits (no date):
  - "The Web API has rate limits in order to keep our API reliable and to help third-party developers use the API in a responsible way." SP
  - "Spotify's API rate limit is calculated based on the number of calls that your app makes to Spotify in a rolling 30 second window." SV
  - "The header of the 429 response will normally include a Retry-After header with a value in seconds." SV
  - "If your app is meant to be used by many Spotify users at the same time then you should apply for extended quota mode. Apps in this mode have a rate limit that is much higher than apps in development mode, the default mode for new apps." SP (second sentence returned on two passes)
  - "Spotify has some APIs — like the Get Multiple Albums endpoint — that allow you to fetch a batch of data in one API request." SP
  - The page gives no numeric limit (checked).
- Quota modes, https://developer.spotify.com/documentation/web-api/concepts/quota-modes (footer © 2026):
  - "The app owner must have a Spotify Premium account for apps in development mode to function." SV
  - "Up to 5 authenticated Spotify users can use an app that is in development mode" SV
  - "Please note that as of May 15th 2025, Spotify only accepts applications from organizations (not individuals)." SP
  - Criteria include "Established Business Entity (legally registered business or organisation)" SP and "Maintaining a minimum of active users (at least 250k MAUs)" SV
- Blog, 27 November 2024, https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api — title "Introducing some changes to our Web API" SV
  - Reason: "As we continue to review the experience provided on Spotify for Developers, we've decided to roll out a number of measures with the aim of creating a more secure platform." SP
  - "Effective today, new Web API use cases will no longer be able to access or use the following endpoints and functionality in their third-party applications." SV on the core clause
  - List, identical on two passes: Related Artists; Recommendations; Audio Features; Audio Analysis; Get Featured Playlists; Get Category's Playlists; 30-second preview URLs, in multi-get responses (SimpleTrack object); Algorithmic and Spotify-owned editorial playlists.
  - Affected: "Existing apps that are still in development mode without a pending extension request" and "New apps that are registered on or after today's date." SP
- Blog, 15 April 2025, "Updating the Criteria for Web API Extended Access" SV on title and date
  - "In addition, over 95% of the applications we receive for extended Web API access fall short of basic security, privacy, and licensing standards." SP
  - "Starting May 15, 2025, extended Web API access will be reserved for apps with established, scalable, and impactful use cases that help drive our platform strategy forward and promote artists and creator discovery." SV on the opening clause
  - "Developers previously granted extended access and actively using the Web API in compliance with our Developer Terms will remain unaffected by this change." SP
- "February 2026 Web API Dev Mode Changes - Migration Guide", https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide
  - "This guide is here to help developers with existing apps migrate to the updated Web API following the February 2026 announcement." SV
  - Timeline rows: "February 11, 2026 | New Development Mode apps are created with new restrictions"; "March 9, 2026 | Existing Development Mode apps are migrated to new restrictions". SP
  - "All Development Mode apps require the app owner to have an active Spotify Premium subscription." SP. "Users per app | 5"; "Client IDs per developer | 1"; "As of July 2026, the Client IDs per developer limit has been increased to 25." SP
  - Removed for development-mode apps: batch fetch endpoints (row "GET /tracks | GET /tracks/{id} (one request per track)"), browse endpoints, GET /artists/{id}/top-tracks, some user endpoints. SP
  - "Apps in extended quota mode are not affected by any of the changes described in this guide — all existing endpoints, fields, and behaviors remain unchanged." SP
  - No reason is given in the guide (checked).
Type: platform documentation and announcements. Strength: high on what changed.
Role: the cleanest dated sequence of a platform narrowing its interface: 27 Nov 2024, then 15 May 2025, then 11 Feb and 9 Mar 2026. The first took effect on the day it was announced.

5b. YouTube Data API — the brief's figure is out of date
- https://developers.google.com/youtube/v3/getting-started — "Last updated 2026-09-14 UTC."
  - "Projects that enable the YouTube Data API have a default quota allocation of 100 search.list calls, 100 videos.insert calls, and 10,000 units per day combined for all other endpoints." SV
  - "A search query costs 1 unit." SV. The page does NOT say a search costs 100 units (checked).
  - "A read operation that retrieves a list of resources -- channels, videos, playlists -- usually costs 1 unit." SP. "A write operation that creates, updates, or deletes a resource usually costs 50 units." SP
  - "All API requests, including invalid requests, incur at least a one-point quota cost." SV
- https://developers.google.com/youtube/v3/determine_quota_cost — "Last updated 2026-09-15 UTC."
  - Table row: "search | list | 100 quota per day. Each call costs 1 quota." SP
  - "The search.list and videos.insert methods have their own quota buckets. Each of these methods has a default daily limit of 100 per day. The quota cost is 1 per call." SP
  - "Daily quotas reset at midnight Pacific Time (PT)." SP
- Revision history, https://developers.google.com/youtube/v3/revision_history
  - June 1, 2026: "The YouTube Data API is transitioning to a granular quota system covering smaller sets of methods, starting with videos.insert and search.list." SV. "API calls to the videos.insert and search.list methods will be charged to their own respective quota buckets." SV
  - December 4, 2025: "The YouTube Data API documentation and Quota Calculator have been updated to reflect a change in the quota cost of a video upload from approximately 1600 units to approximately 100 units." SV
- My observation, not the source's: 100 searches a day is what 10,000 units at 100 each used to buy. The practical search ceiling looks unchanged, and searches no longer eat the general budget. I could not quote the old "100 units" wording from a live page.
Role: a live example that a quota figure in a book goes stale within a year. Cite with the date.

5c. MusicBrainz
URL: https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting — the page's own dating: "As of 2012-01-08 our rules are as follows:" SP
- "The rate at which your IP address is making requests is measured. If that rate is too high, all your requests will be declined (http 503) until the rate drops again. Currently that rate is (on average) 1 request per second." SV on the last sentence
- "We allow through 300 requests each second (on average), and decline (http 503) the rest." SV
- "For 'anonymous' user-agents (see below): we allow through (on average) 50 requests per second, and decline (http 503) the rest." SP
- "We may change the blocking/throttling rules at any time in order to protect the overall site health." SV
- User-Agent format: "Application name/<version> ( contact-url )". SP
Role: it signals rate limiting with 503, not 429. It also has a global cap, so a well-behaved client can still be declined.

5d. Last.fm API Terms of Service
URL: https://www.last.fm/api/tos — no date on the page (checked).
- Clause 4.4: "Last.fm sets and enforces limits on use of the API to prevent abuse and ensure reliability of service (e.g. limiting the number of API requests that you may make or the number of users you may serve), in our sole discretion." SV on the opening clause
- Clause 4.3.4: "The 'Reasonable Usage Cap' is a maximum of 100 MB, as may be updated by Last.fm from time to time." SV. "You will implement suitable caching in accordance with the HTTP headers sent with web service responses." SP
- Clause 3.1: "You are permitted to use the Last.fm Data solely for non-commercial purposes and for no other purpose." SP
- Clause 2.7: "You agree to use one of the buttons saying 'powered by AudioScrobbler' from the page located at http://www.last.fm/resources, such button linking back to Last.fm." SP
- Clause 9.2: "Last.fm may at any time in its sole discretion, without liability and with or without cause terminate this Agreement and/or terminate, restrict, block, disable or suspend Your access to the Last.fm Site or the Last.fm Data." SP
- No numeric requests-per-second limit is stated (checked).

5e. SoundCloud (all single pass; not re-verified)
- Guide, https://developers.soundcloud.com/docs/api/guide: "All API usage requires a registered application" SP. The reader reported registration needs a SoundCloud account with "Artist Pro required", and a "Get an API key" link marked new. OAuth 2.1 with PKCE; client-credentials tokens limited to "50 tokens per 12 hours per application" and "30 tokens per 1 hour per IP address". SP
- Rate limits, https://developers.soundcloud.com/docs/api/rate-limits: "Requests that result in access to a playable stream are limited to 15,000 per 24-hour window" SP. "No limit is currently enforced on the total number of calls a client application makes in aggregate." SP
- Status: registration appears open again but gated by a paid artist tier. Check before printing.

5f. Bandcamp
URL: https://bandcamp.com/developer (no date)
- "Labels and merchandise fulfillment partners can interact with their accounts via the Bandcamp API." SV
- "To register for API use, contact us, and include in your email a brief description of how you intend to use API access." SV
- APIs listed: Account API, Sales Report API, Merch Orders API. No public catalogue or listings API.

====================================================================
ITEM 6 — PLATFORM DEPRECATION AS A PATTERN
====================================================================

6a. Twitter/X, February–March 2023 — SECONDARY ONLY
- The official forum post is robots-disallowed; Wikipedia is not fetchable from this tool.
- TechCrunch, Ivan Mehta, 29 March 2023, "Twitter announces new API with only free, basic and enterprise levels", https://techcrunch.com/2023/03/29/twitter-announces-new-api-with-only-free-basic-and-enterprise-levels/ (headline SV). All sentences are the journalist's:
  - "Twitter's API saga started when the company announced in February that it is ending free API access in just a matter of days." SP
  - "The free tier provides only 1,500 post requests per month along with access to Login with Twitter." SP
  - "The basic tier — which is deemed 'for hobbyists or students' — provides 50,000 post requests and 10,000 read requests per app per month." SP. The $100 per month price for Basic appeared in the first pass only.
  - "Twitter mentioned that over the next 30 days, the company will discontinue old access levels, including Standard (for v1.1), Essential and Elevated (for v2), and Premium." SV on the core clause
  - "Twitter's new announcement mentions that it is 'looking at new ways' to serve the academic community, but didn't provide any information about potential solutions." SP
- Primary, current: https://docs.x.com/x-api/getting-started/pricing (no date): "The X API uses pay-per-usage pricing. No subscriptions—pay only for what you use." SV. "Pay-per-usage plans are capped at 3 million Post reads per monthly billing cycle." SV on the figure. The tier names of 2023 no longer appear (checked).

6b. Reddit, June 2023
- Reddit's own announcement post and redditinc.com are blocked from this tool. NOT VERIFIED: "$0.24 per 1K API calls" and the 1 July 2023 date. Nothing quoted.
- Primary, current: Reddit Data API Wiki, https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki — "Updated May 11, 2026 16:00"
  - "100 queries per minute (QPM) per OAuth client id" SV
  - "QPM limits will be an average over a time window (currently 10 minutes) to support bursting requests." SP
  - "Traffic not using OAuth or login credentials will be blocked, and the default rate limit will not apply." SV
  - Headers: X-Ratelimit-Used, X-Ratelimit-Remaining, X-Ratelimit-Reset. SP
  - "We strongly recommend routinely deleting any stored user data and content within 48 hours." SP

6c. Facebook/Instagram, 2018 — PRIMARY
Mike Schroepfer (CTO), "An Update on Our Plans to Restrict Data Access on Facebook", April 4, 2018, https://about.fb.com/news/2018/04/restricting-data-access/ (title and date SV)
- "Two weeks ago we promised to take a hard look at the information apps can use when you connect them to Facebook as well as other data practices." SP
- Events API: "Starting today, apps using the API will no longer be able to access the guest list or posts on the event wall." SV
- Groups API: "Apps will no longer be able to access the member list of a group." SP
- Pages API: "Starting today, all future access to the Pages API will need to be approved by Facebook." SV
- "We're making the recently announced deprecation of the Instagram Platform API effective today." SV
- "Overall, we believe these changes will better protect people's information while still enabling developers to create useful experiences." SP
Role: "Starting today" and "effective today" show zero notice, justified by privacy and security. Spotify used the same form on 27 Nov 2024 ("Effective today").

6d. Google Maps Platform Terms of Service — PRIMARY
URL: https://cloud.google.com/maps-platform/terms — "Last modified August 26, 2026". Section 1.3(c); the two passes gave different headings for it, so cite by number only.
- "Google will notify Customer at least 12 months before discontinuing a Service (or associated material functionality) without providing a materially similar replacement." SV
- "Further, Google will notify Customer at least 12 months before modifying any Customer-facing Google APIs in a backwards-incompatible manner." SV
- "Nothing in this Section 1.3(c) limits Google's ability to make changes required to comply with applicable law, address a material security risk, or avoid a substantial economic or material technical burden. This Section 1.3(c) does not apply to pre-general availability Services, offerings or functionality." SP
Role: the contractual best case is 12 months, with security and economic-burden exceptions. GDS guidance says "should try" six months. ONS, Skiddle, Ticketmaster and Spotify promise none.

====================================================================
ITEM 7 — OPEN GOVERNMENT LICENCE v3.0
====================================================================
Source note: the National Archives URL failed twice with "Too many redirects". The text below is string-verified against the SPDX reproduction, https://spdx.org/licenses/OGL-UK-3.0.html. That is a faithful secondary copy of the licence, not the canonical page; re-check against nationalarchives.gov.uk before print. The licence is undated on SPDX.
- Grant: "The Licensor grants you a worldwide, royalty-free, perpetual, non-exclusive licence to use the Information subject to the conditions below." SP
- You are free to: "copy, publish, distribute and transmit the Information" SV; "adapt the Information" SP; "exploit the Information commercially and non-commercially for example, by combining it with other Information, or by including it in your own product or application" SV
- You must: "acknowledge the source of the Information in your product or application by including or linking to any attribution statement specified by the Information Provider(s) and, where possible, provide a link to this licence" SV
- Default attribution: "If the Information Provider does not provide a specific attribution statement, you must use the following: Contains public sector information licensed under the Open Government Licence v3.0." SP
- Exemptions include "personal data in the Information" SV and "third party rights the Information Provider is not authorised to license" SV. Also logos, crests and the Royal Arms, military insignia, patents, trade marks and design rights, and identity documents. SP
- Non-endorsement: "This licence does not grant you any right to use the Information in a way that suggests any official status or that the Information Provider and/or Licensor endorse you or your use of the Information." SP
- No warranty: "The Information is licensed 'as is' and the Information Provider and/or Licensor excludes all representations, warranties, obligations and liabilities in relation to the Information to the maximum extent permitted by law." SV
- "The Information Provider and/or Licensor are not liable for any errors or omissions in the Information and shall not be liable for any loss, injury or damage of any kind caused by its use." SV
- "The Information Provider does not guarantee the continued supply of the Information." SV
Type: licence. Strength: definitive, subject to the source note.
Role: the last sentence carries the chapter's point. The licence is perpetual; the supply is not. OGL gives a right to reuse what you have, not a right to keep receiving it.

====================================================================
ITEM 8 — TERMS THAT FORBID WHAT A DASHBOARD MIGHT DO
====================================================================
Spotify Developer Terms — "Version 10, effective as of 15 May, 2025" (SV), https://developer.spotify.com/terms
- Section IV "Restrictions", 3 "Storing Spotify Content", a: "Except as otherwise set out in these Developer Terms, you may not store, aggregate or create compilations or databases of Spotify Content, other than as strictly necessary to operate your SDA." SV on the core clause. Same place: "Do not store Spotify Content indefinitely." SV
- IV.3.b (reader's label): "Do not locally cache any Spotify Content, except as strictly necessary to enhance the performance of your SDA and its functionality, and limited to the temporary caching of: (1) metadata and cover art; or (2) Conditional Downloads of sound recordings." SV on the first clause
- IV.2.a: "Do not misuse the Spotify Platform, including by using the Spotify Platform or any Spotify Content to train a machine learning or AI model or otherwise ingesting Spotify Content into a machine learning or AI model" SP
- V.5: "You will not sell any Spotify Content or other data obtained from Spotify." SV
- VI.2: "Spotify may limit the number of service calls that your SDA may make, the volume of Spotify Content that may be accessed, or anything else about the Spotify Service as Spotify deems appropriate, in its sole discretion, without notice." SV
- IX.8.h (reader's label): "Spotify has no obligation to maintain, support, upgrade, or update the Spotify Platform or Spotify Service, or to provide all or any specific content." SV
- Sub-letter labels come from the reader and wavered between passes. Confirm before citing by number.

Spotify Developer Policy — "Effective as of 15 May, 2025" (SV), https://developer.spotify.com/policy
- III.13: "Do not analyze the Spotify Content or the Spotify Service for any purpose, including without limitation, creating new or derived listenership metrics, benchmarking, functionality, usage statistics, user metrics, or building profiles of users, including for the purpose of targeting them with advertising or marketing." SV up to "user metrics"
- III.5: "Do not create any product or service which is integrated with streams or content from another service." SV
- III.9: "Do not build an SDA that enables the transfer of data to another service, except for the purpose of enabling a user to transfer their personal data, or the metadata of the user's playlists to another service." SP
- III.14: the AI/ML training prohibition, restated. SP
- II.4.1: "If you display any Spotify Content you must clearly attribute the content as being supplied and made available by Spotify, by using the Spotify Marks." SV
- II.4.2: "Metadata, cover art and Audio Preview Clips must be accompanied by a link back to the applicable album, content or playlist on the Spotify Service." SP
- II.4.3: "You must not offer metadata, cover art, and/or Audio Preview Clips as a standalone service or product." SV
- IV.2: "Except for the limited commercial uses for Non-Streaming SDAs (set out below) commercial uses are not permitted for SDAs." SP (the verifying pass elided the middle)
- No caching duration is specified (checked).

Others, quoted in full above:
- Ticketmaster API Terms (Last Updated June 27, 2023): the cache clause ("other than for reasonable periods"), the "replicates or attempts to replace" clause, the rate-limit clause on calls "not primarily in response to direct user actions", and change/suspend/discontinue "at any time". No cross-provider aggregation clause found.
- Skiddle API page (no date; © 2001-2026): "The API is for non-commercial use only."
- Last.fm API ToS (undated): 3.1 non-commercial; 2.7 button and link-back; 4.3.4 the 100 MB "Reasonable Usage Cap".
- Google Maps Platform ToS (Last modified August 26, 2026):
  - 3.2.3(b): "Customer will not cache Google Maps Content except as expressly permitted under the Maps Service Specific Terms." SV
  - 3.2.3(e): "To avoid quality issues and/or brand confusion, Customer will not use the Google Maps Core Services with or near a non-Google Map in a Customer Application." SV
  - 3.2.3(a): "Customer will not export, extract, or otherwise scrape Google Maps Content for use outside the Services." SP
- OSMF policies: no bulk download or prefetch, no offline use, mandatory caching, 4 requests per minute for scheduled scripts.
Role: the read is that the open-data licences forbid almost nothing and guarantee nothing, while the platform terms forbid the things a dashboard does: store, aggregate, derive metrics, combine providers, call on a schedule.

====================================================================
UNEXPECTED THREADS (not asked for)
====================================================================
1. YouTube rewrote its quota model on 1 June 2026 (item 5b). Search is now its own bucket of 100 calls a day at 1 unit each; an upload fell from about 1,600 units to about 100 in December 2025.
2. data.gov.uk is "now known as the National Data Library", with the transformation started "In early 2026". The catalogue's name and roadmap are moving under anyone citing it.
3. ONS implements standards-style retirement signalling: Deprecation, Sunset and Link response headers, plus deliberate "rolling blackouts" to flush out remaining users. It states no notice period. GDS says six months for live APIs, and the ONS API is beta. I did not fetch the IETF Deprecation and Sunset header RFCs; worth a follow-up.
4. Spotify's February 2026 development-mode changes: Premium required, 5 users, one Client ID (25 from July 2026), batch endpoints removed for dev-mode apps. The rate-limits page still advises batch endpoints to stay under the limit, which reads as an internal inconsistency in the documentation as fetched.
5. Nominatim's rule for scheduled scripts (4 requests per minute) and the tile policy's minimum 7-day cache and "no SLA or guarantee" are written for exactly the unattended-job case.
6. X's API is now pay-per-usage with a 3-million-read monthly cap. The 2023 tiers that secondary sources describe are already history: two re-pricings in about three years.
7. The provider-side rationale in GDS guidance: do not let users exceed limits "even if you have spare capacity", because their application "could break" when the slack is withdrawn. Useful for explaining why an API that worked faster yesterday is not a promise.
8. Smaller findings:
   - Police snap-point list built in 2012 and refreshed in 2022.
   - FSA guarantees only one "depreciated" version back.
   - Skiddle's API docs live in a GitHub repository archived on 30 April 2024.
   - Ticketmaster's terms define "Event Content" to include "Tickets, Attendees, Orders", although the public Discovery API showed no such fields in what the reader saw.
   - TfL's licence is still based on OGL v2.0 and deletes accounts idle for a year.

LEFT OUT, AND WHY
- Eventbrite: the whole developer site is JS-only for this tool. The search-endpoint removal and rate limit are unverified.
- OS Data Hub plans and free allowances: JS-only.
- ONS Open Geography Portal terms: JS-only.
- RFC 9110 §10.2.3 text: reader truncation; MDN given as marked secondary.
- National Archives OGL page: redirect loop; SPDX copy used.
- Reddit's June 2023 announcement and pricing, the Twitter/X original announcement, and Wikipedia: blocked, robots-disallowed or not fetchable.
- Bus Open Data Service: 404 on the URL tried.
- Skiddle's detailed site terms and Ticketmaster's branding guide: not fetched.
- The archived 2018 v1 of the GDS standard, which may hold the "deprecation policies" sentence: not fetched.
- SoundCloud: not re-verified.
- No event listings or cultural content were fetched from any platform.

RICH REFERENCES
1. GDS/CDDO "Managing your live API" and "Setting API service levels", read with ONS's "Guide to retirement of API endpoints". Together they give the UK public sector's stated norm (six months; limits are real; uptime hides shape) and one department's actual mechanism (headers, blackouts, 404).
2. OSMF Tile Usage Policy and Nominatim Usage Policy. Short, current, blunt operator policies that separate free data from free servers and speak directly to scheduled jobs.
3. The Spotify developer sequence: blog 27 Nov 2024, blog 15 Apr 2025, the February 2026 migration guide, and Developer Policy III.13. A dated, primary-source case of an interface narrowing in three steps, plus a clause that forbids derived metrics outright.

WHAT SURPRISED ME
- Three phrases the brief expected are not in the sources as they stand: GDS has no "deprecation period" or "do not break backward compatibility" wording; the OSM tile policy no longer says "forbidden without prior permission"; YouTube no longer charges 100 units for a search.
- The OGL, usually read as the permissive end of the spectrum, contains the bluntest supply disclaimer of anything I read: "The Information Provider does not guarantee the continued supply of the Information." TfL's licence repeats it.
- Almost every public UK API here labels itself beta or disclaims service level (ONS, Environment Agency, Skiddle). That takes them outside even the GDS six-month expectation.
- Spotify's policy prohibition on "creating new or derived listenership metrics, benchmarking ... usage statistics" is a direct description of dashboard-making.
- Skiddle's API is non-commercial by default with a limit that is "continually changed". Ticketmaster reserves the right to block callers whose calls are "not primarily in response to direct user actions".
- There is still no standard rate-limit header: the IETF draft is at -11 with intended status "(None)".
- Most developer pages carry no date. Only gov.uk, Google, Reddit's wiki, MDN and the legal terms did.

SOURCES (all fetched 6 October 2026)
https://www.gov.uk/guidance/gds-api-technical-and-data-standards
https://www.gov.uk/guidance/managing-your-live-api
https://www.gov.uk/guidance/setting-api-service-levels
https://www.gov.uk/government/collections/api-design-guidance
https://www.api.gov.uk/
https://www.gov.uk/guidance/the-technology-code-of-practice
https://www.rfc-editor.org/rfc/rfc6585
https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After
https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
https://api-portal.tfl.gov.uk/faq
https://api-portal.tfl.gov.uk/products
https://tfl.gov.uk/corporate/terms-and-conditions/transport-data-service
https://developer-specs.company-information.service.gov.uk/guides/rateLimiting
https://developer.ons.gov.uk/
https://developer.ons.gov.uk/bots/
https://developer.ons.gov.uk/retirement/
https://www.nomisweb.co.uk/api/v01/help
https://guidance.data.gov.uk/get_data/api_documentation/
https://www.data.gov.uk/about
https://data.police.uk/docs/api-call-limits/
https://data.police.uk/about/
https://docs.os.uk/os-apis/core-concepts/rate-limiting-policy
https://www.ordnancesurvey.co.uk/products/os-open-zoomstack
https://www.ordnancesurvey.co.uk/products/os-maps-api
https://operations.osmfoundation.org/policies/nominatim/
https://operations.osmfoundation.org/policies/tiles/
https://api.ratings.food.gov.uk/help
https://ratings.food.gov.uk/open-data
https://environment.data.gov.uk/flood-monitoring/doc/reference
https://www.skiddle.com/api/
https://github.com/Skiddle/web-api
https://developer.ticketmaster.com/products-and-docs/apis/getting-started/
https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/
https://developer.ticketmaster.com/support/terms-of-use/
https://developer.spotify.com/documentation/web-api/concepts/rate-limits
https://developer.spotify.com/documentation/web-api/concepts/quota-modes
https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api
https://developer.spotify.com/blog/2025-04-15-updating-the-criteria-for-web-api-extended-access
https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide
https://developer.spotify.com/terms
https://developer.spotify.com/policy
https://developers.google.com/youtube/v3/getting-started
https://developers.google.com/youtube/v3/determine_quota_cost
https://developers.google.com/youtube/v3/revision_history
https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting
https://www.last.fm/api/tos
https://developers.soundcloud.com/docs/api/guide
https://developers.soundcloud.com/docs/api/rate-limits
https://bandcamp.com/developer
https://techcrunch.com/2023/03/29/twitter-announces-new-api-with-only-free-basic-and-enterprise-levels/
https://docs.x.com/x-api/getting-started/pricing
https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
https://about.fb.com/news/2018/04/restricting-data-access/
https://cloud.google.com/maps-platform/terms
https://spdx.org/licenses/OGL-UK-3.0.html
---

## Agent C — Reliability engineering and the no-admin architectures

CHAPTER 8 RESEARCH REPORT — FACET: RELIABILITY ENGINEERING AND THE "NO-ADMIN" ARCHITECTURES
All fetches made 6 October 2026.

TOOLS AND METHOD
- WebSearch: UNAVAILABLE (the turn's shared search budget was already used up on my first call). Everything below came from direct URLs via WebFetch.
- curl through the proxy was refused (403), so no raw-text grep was possible. Verification is the two-pass method in the brief: first fetch, then a re-fetch with a YES/NO presence prompt.
- Marking: SV = STRING-VERIFIED on a second pass. SP = SINGLE PASS.
- Typography: the SRE book, Fowler and Willison pages use curly quotes and apostrophes. My check strings used straight ones, so one or two checks returned "NO" with an identical closest sentence. I treat those as verified apart from the glyph. Copy-edit the quote marks against the page before print.
- The reader invented publication years for three books on first pass (SRE book "2017", Workbook "2020", Software Engineering at Google "2016"). None of those pages shows a year. From general knowledge, NOT page-verified: SRE book 2016, Workbook 2018, SWE at Google 2020 (all O'Reilly).

====================================================================
ITEM 1 — HTTP CACHING

1a. RFC 9111, "HTTP Caching" — https://www.rfc-editor.org/rfc/rfc9111
Standard: Internet Standard, STD 98, June 2022. Strength: highest, normative.
- §1: «An HTTP "cache" is a local store of response messages and the subsystem that controls storage, retrieval, and deletion of messages in it.» SV
- §1: «A cache stores cacheable responses to reduce the response time and network bandwidth consumption on future equivalent requests.» SV
- §4.2: «A "fresh" response is one whose age has not yet exceeded its freshness lifetime.» SV
- §4.2: «Conversely, a "stale" response is one where it has.» SV
- §4.2: «A response's "freshness lifetime" is the length of time between its generation by the origin server and its expiration time.» SV
- §4.2: «When a response is fresh, it can be used to satisfy subsequent requests without contacting the origin server, thereby improving efficiency.» SV
- §4.2.4: «A cache MUST NOT generate a stale response if it is prohibited by an explicit in-protocol directive (e.g., by a no-cache response directive, a must-revalidate response directive, or an applicable s-maxage or proxy-revalidate response directive; see Section 5.2.2).» SV
- §4.2.4 (the "stale may be served under conditions" sentence): «A cache MUST NOT generate a stale response unless it is disconnected or doing so is explicitly permitted by the client or origin server (e.g., by the max-stale request directive in Section 5.2.1, extension directives such as those defined in [RFC5861], or configuration in accordance with an out-of-band contract).» SV
- §5.2.2.1: «The "max-age" response directive indicates that the response is to be considered stale after its age is greater than the specified number of seconds.» SV
- §5.1: «The "Age" response header field conveys the sender's estimate of the time since the response was generated or successfully validated at the origin server.» SV
- §4.3 opening (the reader truncated it; SV as far as shown): «When a cache has one or more stored responses for a requested URI, but cannot serve any of them (e.g., because they are not fresh, or one cannot be chosen; see Section 4.1), it can use the conditional request mechanism...»
- §4.3.1 (fragment, SV): «MUST send the relevant entity tags (using If-Match, If-None-Match, or If-Range) if the entity tags were provided in the stored response(s) being validated.»
- §4.3.3: «A 304 (Not Modified) response status code indicates that the stored response can be updated and reused; see Section 4.3.4.» SV
- §4.3.3: «However, if a cache receives a 5xx (Server Error) response while attempting to validate a response, it can either forward this response to the requesting client or act as if the server failed to respond.» SV. The following sentence, «In the latter case, the cache can send a previously stored response», is SP.
- §5.2.2.2: «The must-revalidate response directive indicates that once the response has become stale, a cache MUST NOT reuse that response to satisfy another request until it has been successfully validated.» SP
Role: gives the chapter its exact vocabulary (fresh, stale, freshness lifetime, validation) and the fact that the protocol itself carries an "age" field and a rule for serving stale when disconnected.

1b. RFC 5861, "HTTP Cache-Control Extensions for Stale Content" — https://www.rfc-editor.org/rfc/rfc5861
M. Nottingham, May 2010. INFORMATIONAL, not standards track (say so). RFC 9111 §4.2.4 cites it by number.
- Abstract: «This document defines two independent HTTP Cache-Control extensions that allow control over the use of stale responses by caches.» SV
- §1: «The stale-while-revalidate HTTP Cache-Control extension allows a cache to immediately return a stale response while it revalidates it in the background, thereby hiding latency (both in the network and on the server) from clients.» Returned verbatim on the verification pass; treat as SV.
- §3: «When present in an HTTP response, the stale-while-revalidate Cache-Control extension indicates that caches MAY serve the response in which it appears after it becomes stale, up to the indicated number of seconds.» SV
- §3: «If a cached response is served stale due to the presence of this extension, the cache SHOULD attempt to revalidate it while still serving stale responses (i.e., without blocking).» SV
- §4: «The stale-if-error Cache-Control extension indicates that when an error is encountered, a cached stale response MAY be used to satisfy the request, regardless of other freshness information.» SV
- §4: «In this context, an error is any situation that would result in a 500, 502, 503, or 504 HTTP response status code being returned.» SV
Role: the two directives that turn "the source is down" into "the reader sees yesterday's page"; graceful degradation written into a header.

1c. RFC 9110 §8.8.3 (ETag) and §13 (Conditional Requests) — NOT REACHED.
The reader truncates the page at about 118–120k characters (it ends in §8.3.3) on rfc-editor.org HTML, the .txt, and httpwg.org. Two attempts plus one alternate host; nothing quoted from RFC 9110. Substitutes: the RFC 9111 §4.3 sentences above (same standard family, normative) and MDN below (secondary).

1d. MDN (SECONDARY; documentation, not a standard)
Cache-Control — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control — «This page was last modified on Sep 17, 2026».
- «The HTTP Cache-Control header holds directives (instructions) in both requests and responses that control caching in browsers and shared caches (e.g., Proxies, CDNs).» SV
- «The max-age=N response directive indicates that the response remains fresh until N seconds after the response is generated.» SV
- «The stale-while-revalidate response directive indicates that the cache could reuse a stale response while it revalidates it to a cache.» SV
- «The stale-if-error response directive indicates that the cache can reuse a stale response when an upstream server generates an error, or when the error is generated locally.» SV
- The prose carries no browser-support caveat for these two directives. I did not read the compatibility table, so check it before claiming browser support.
ETag — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag — last modified Jul 28, 2025.
- «…response header is an identifier for a specific version of a resource.» SV (fragment)
- «It lets caches be more efficient and save bandwidth, as a web server does not need to resend a full response if the content has not changed.» SV
- «…the server sends back a 304 Not Modified status, without a body, which tells the client that the cached version of the response is still good to use (fresh).» SV (fragment)

1e. Rate limiting (in my facet line, not in the numbered items)
RFC 6585 — https://www.rfc-editor.org/rfc/rfc6585 — Nottingham and Fielding, April 2012, Proposed Standard.
- §4: «The 429 status code indicates that the user has sent too many requests in a given amount of time ("rate limiting").» SV
- «The response representations SHOULD include details explaining the condition, and MAY include a Retry-After header indicating how long to wait before making a new request.» SV
- «Note that this specification does not define how the origin server identifies the user, nor how it counts requests.» SV
- «Responses with the 429 status code MUST NOT be stored by a cache.» SV
IETF draft "RateLimit header fields for HTTP" — https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ — version 11, last updated 2026-05-23, expires 24 November 2026, Active Internet-Draft (httpapi WG), intended status shown as "(None)". Authors Polli, Martínez Ruiz, Miller. Not a standard.
- Abstract: «This document defines the RateLimit-Policy and RateLimit HTTP header fields for servers to advertise their quota policies and the current service limits, thereby allowing clients to avoid being throttled.» SV
Role: the only standardised rate-limit signals are a status code and an optional Retry-After. The standard explicitly declines to say how requests are counted, and the header that would advertise quotas is still a draft after many revisions.

====================================================================
ITEM 2 — SERVICE LEVELS AND MONITORING (Google SRE book, open at sre.google)
Practitioner text, widely treated as canonical. Strength: authoritative practice, not a standard, not empirical evidence. No dates on the pages.

2a. Ch. 4 "Service Level Objectives" — https://sre.google/sre-book/service-level-objectives/ — «Chris Jones, John Wilkes, and Niall Murphy with Cody Smith»
- «An SLI is a service level indicator—a carefully defined quantitative measure of some aspect of the level of service that is provided.» SV
- «An SLO is a service level objective: a target value or range of values for a service level that is measured by an SLI.» SV
- «Finally, SLAs are service level agreements: an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs they contain.» SV
- «An easy way to tell the difference between an SLO and an SLA is to ask 'what happens if the SLOs aren't met?'» SP
- «It's both unrealistic and undesirable to insist that SLOs will be met 100% of the time: doing so can reduce the rate of innovation and deployment, require expensive, overly conservative solutions, or both.» SV
- «Users build on the reality of what you offer, rather than what you say you'll supply, particularly for infrastructure services.» SV
- Chubby planned outage: «In any given quarter, if a true failure has not dropped availability below the target, a controlled outage will be synthesized by intentionally taking down the system.» SV
- «Big data systems, such as data processing pipelines, tend to care about throughput and end-to-end latency. In other words: How much data is being processed? How long does it take the data to progress from ingestion to completion?» SV
- «All systems should care about correctness: was the right answer returned, the right data retrieved, the right analysis done?» SP

2b. Ch. 3 "Embracing Risk" — https://sre.google/sre-book/embracing-risk/ — Marc Alvidrez
- «100% is probably never the right reliability target: not only is it impossible to achieve, it's typically more reliability than a service's users want or notice.» SV apart from the apostrophe glyph.
- «Extreme reliability comes at a cost: maximizing stability limits how fast new features can be developed and how quickly products can be delivered to users, and dramatically increases their cost, which in turn reduces the numbers of features a team can afford to offer.» SV
- «Put simply, a user on a 99% reliable smartphone cannot tell the difference between 99.99% and 99.999% service reliability!» SV
- Error budget: «Product Management defines an SLO, which sets an expectation of how much uptime the service should have per quarter.» … «The difference between these two numbers is the "budget" of how much "unreliability" is remaining for the quarter.» SV. NOTE: the two are not adjacent on the page; "these two numbers" are the SLO and the measured uptime. Do not run them together.
- «As long as the uptime measured is above the SLO—in other words, as long as there is error budget remaining—new releases can be pushed.» SV
- «The error budget provides a clear, objective metric that determines how unreliable the service is allowed to be within a single quarter.» SV
- «While there are significant differences between ISPs and protocols (e.g., TCP versus UDP, IPv4 versus IPv6), we've measured the typical background error rate for ISPs as falling between 0.01% and 1%.» SV
- Formulas (SP, paraphrased layout): time-based availability = uptime / (uptime + downtime); aggregate availability = successful requests / total requests.

2c. Ch. 1 "Introduction" — https://sre.google/sre-book/introduction/ — Benjamin Treynor Sloss
- «100% is the wrong reliability target for basically everything (pacemakers and anti-lock brakes being notable exceptions).» SV
- «Monitoring should never require a human to interpret any part of the alerting domain.» SV
- «Instead, software should do the interpreting, and humans should be notified only when they need to take action.» SV
- «Alerts: Signify that a human needs to take action immediately in response to something that is either happening or about to happen, in order to improve the situation.» SV
- «Tickets: Signify that a human needs to take action, but not immediately. The system cannot automatically handle the situation, but if a human takes action in a few days, no damage will result.» SV
- «Logging: No one needs to look at this information, but it is recorded for diagnostic or forensic purposes. The expectation is that no one reads logs unless something else prompts them to do so.» SV
- «Humans add latency.» SV
- Playbook: «…produces roughly a 3x improvement in MTTR as compared to the strategy of 'winging it.'» SP for the figure.
NOTE: the "human needs to take action" wording you wanted is in Chapter 1, not Chapter 6. I checked: it is absent from Chapter 6.

2d. Ch. 6 "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/ — Rob Ewaschuk, ed. Betsy Beyer
- «The four golden signals of monitoring are latency, traffic, errors, and saturation.» SV. Next sentence: «If you can only measure four metrics of your user-facing system, focus on these four.» SV
- Latency: «The time it takes to service a request.» SP. Traffic: «A measure of how much demand is being placed on your system» SP (opening words).
- Errors: «The rate of requests that fail, either explicitly (e.g., HTTP 500s), implicitly (for example, an HTTP 200 success response, but coupled with the wrong content), or by policy (for example, "If you committed to one-second response times, any request over one second is an error").» SV. This is the useful one: a 200 OK carrying wrong content is an error.
- Saturation: «How "full" your service is.» SV
- Symptoms vs causes: «Your monitoring system should address two questions: what's broken, and why? The "what's broken" indicates the symptom; the "why" indicates a (possibly intermediate) cause.» SV
- «Every page should be actionable.» SV
- «Every time the pager goes off, I should be able to react with a sense of urgency. I can only react with a sense of urgency a few times a day before I become fatigued.» SV
- «Every page response should require intelligence. If a page merely merits a robotic response, it shouldn't be a page.» SV
- «Pages should be about a novel problem or an event that hasn't been seen before.» SV
- «When pages occur too frequently, employees second-guess, skim, or even ignore incoming alerts, sometimes even ignoring a "real" page that's masked by the noise.» SV
- «Paging a human is a quite expensive use of an employee's time. If an employee is at work, a page interrupts their workflow.» SV
- «The rules that catch real incidents most often should be as simple, predictable, and reliable as possible.» SV
- White-box / black-box definitions: SP only.

2e. Appendix A "Availability Table" — https://sre.google/sre-book/availability-table/ (allowed unavailability)
- «Availability is generally calculated based on how long a service was unavailable over some period.» SV. Next: «Assuming no planned downtime, Table 1-1 indicates how much downtime is permitted to reach a given availability level.» SV
- 99%: per year 3.65 days; per month 7.2 hours; per day 14.4 minutes. SV. (Per quarter 21.6 hours, per week 1.68 hours: SP.)
- 99.9%: per year 8.76 hours; per month 43.2 minutes; per day 1.44 minutes. SV. (Per quarter 2.16 hours, per week 10.1 minutes: SP.)
- 99.99%: per year 52.6 minutes; per month 4.32 minutes; per day 8.64 seconds. SV. (Per quarter 12.96 minutes, per week 60.5 seconds: SP.)
- Also SP: 99.5% = 1.83 days/year; 95% = 18.25 days/year; 90% = 36.5 days/year; 99.999% = 5.26 minutes/year.
- «Using an aggregate unavailability metric (i.e., "X% of all operations failed") is more useful than focusing on outage lengths for services that may be partially available.» SV
Role: the conversion from a percentage to hours of a dead dashboard per year.

====================================================================
ITEM 3 — AVAILABILITY OF A CHAIN
Found, open: Treynor, Dahlin, Rau, Beyer, "The Calculus of Service Availability" — https://queue.acm.org/detail.cfm?id=3096459
The page shows «Originally published in Queue vol. 15, no. 2» and «Copyright © 2017 held by owner/author»; no day or month displayed. Practitioner article in an ACM magazine; strong as authoritative practice.
- «A service cannot be more available than the intersection of all its critical dependencies.» SV
- «A critical dependency is one that, if it malfunctions, causes a corresponding malfunction in the service.» SV
- "Rule of the extra 9": «Internally at Google, we use the following rule of thumb: critical dependencies must offer one additional 9 relative to your service—in the example case, 99.999 percent availability—because any service will have several critical dependencies, as well as its own idiosyncratic problems.» SV
- «If a service has N unique critical dependencies, then each one contributes 1/N to the dependency-induced unavailability of the top-level service, regardless of its depth in the dependency hierarchy.» SV
- «Can the service continue serving in degraded mode if one of its dependencies fails? In other words, design for graceful degradation.» SV
- The subtitle I remembered ("You're only as available as the sum of your dependencies") was NOT found by the reader on this page. Do not use it.
- NOT found, here or anywhere open that I reached: a sentence stating the plain product rule ("availability of N serial components is the product of their availabilities"). The reader said the page has no worked product for dependencies at 99.99%.
The product arithmetic therefore has to be the chapter's own, stated as such, assuming independent failures and every dependency critical:
- 3 dependencies at 99.9% each: 0.999^3 = 99.70%
- 5 at 99.9%: 0.999^5 = 99.50%, which the SRE table puts at 1.83 days a year
- 10 at 99.9%: 0.999^10 = 99.00%, which is 3.65 days a year
Role: the more live sources a page depends on at view time, the lower its ceiling. A baked page moves those dependencies from view time to build time.

====================================================================
ITEM 4 — STABILITY PATTERNS

4a. Nygard, Release It! 2nd ed. — the book is NOT open; partly reached through the publisher.
Publisher page — https://pragprog.com/titles/mnee2/release-it-second-edition/ — January 2018; the reader gave ISBN 9781680502398.
- Blurb: «A single dramatic software failure can cost a company millions of dollars—but can be avoided with simple changes to design and architecture.» SV
- Blurb: «Eighty percent of project life-cycle cost is in production, yet few books address this topic.» SV. Publisher's marketing claim, unsourced; weak. See Item 7.
- The table of contents lists the stability patterns by name: Timeouts, Circuit Breaker, Bulkheads, Steady State, Fail Fast, Let It Crash, Handshaking, Test Harnesses, Decoupling Middleware, Shed Load, Create Back Pressure, Governor (SP list). Names only; his definitions are in the closed chapter 5.
Free excerpt, Ch. 1 "Living in Production" — https://media.pragprog.com/titles/mnee2/intro.pdf — © 2018 The Pragmatic Programmers
- «Too often, project teams aim to pass the quality assurance (QA) department's tests instead of aiming for life in production.» SV
- «Systems spend much more of their life in operation than in development—at least, the ones that don't get canceled or scrapped do.» SV
- «Our analog of 'design for manufacturability' is 'design for production.'» SP
- «They should not crash, hang, lose data, violate privacy, lose money, destroy your company, or kill your customers.» SP
- «It's probably on the order of $1,000,000 (300 minutes of downtime at a very modest cost of $3,000 per minute).» SP. Illustrative figure, not evidence.
Free excerpt, Ch. 4 "Stability Antipatterns", Integration Points — https://media.pragprog.com/titles/mnee2/antipatterns.pdf
- «Integration points are the number-one killer of systems.» SV. Followed by: «Every single one of those feeds presents a stability risk. Every socket, process, pipe, or remote procedure call can and will hang.» SV
- «The blocked thread can't process other transactions, so overall capacity is reduced.» SP
- The excerpt stops before the "Remember This" box; "circuit breaker" does not appear in it.
Nygard's own blog: not attempted. I had no URL to try without search.

4b. Fowler, "CircuitBreaker" — https://martinfowler.com/bliki/CircuitBreaker.html — 6 March 2014. REACHED. This is the source for the circuit-breaker definition.
- «Remote calls can fail, or hang without a response until some timeout limit is reached.» SP. «What's worse if you have many callers on a unresponsive supplier, then you can run out of critical resources leading to cascading failures across multiple systems.» SV (sic: "a unresponsive")
- «In his excellent book Release It, Michael Nygard popularized the Circuit Breaker pattern to prevent this kind of catastrophic cascade.» SV
- «The basic idea behind the circuit breaker is very simple.» SV «You wrap a protected function call in a circuit breaker object, which monitors for failures.» SV «Once the failures reach a certain threshold, the circuit breaker trips, and all further calls to the circuit breaker return with an error, without the protected call being made at all.» SV «Usually you'll also want some kind of monitor alert if the circuit breaker trips.» SV
- «Circuit breakers are a valuable place for monitoring. Any change in breaker state should be logged and breakers should reveal details of their state for deeper monitoring.» SV
- Fallback (fragment SV): «…failure to get some data may be mitigated by showing some stale data that's good enough to display.»
- The reader reported that Fowler's article does not use the word "bulkhead".

4c. Bulkhead — Microsoft Azure Architecture Center (platform guidance) — https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead — last updated 2026-03-19
- «Isolate the elements of an application into pools so that if one element fails, the others continue to function.» SV
- «This approach, also known as a cell-based architecture, makes an application tolerant of failure and stops a fault in one part of the system from cascading across the rest.» SV
- «This pattern is named after the sectioned partitions (bulkheads) of a ship's hull. If the hull of a ship is compromised, only the damaged section fills with water, which prevents the ship from sinking.» SV
- The older wording in your brief («The Bulkhead pattern is a type of application design that is tolerant of failure…») is NO LONGER on the page.

4d. Graceful degradation — two open sources
AWS Well-Architected, Reliability Pillar, REL05-BP01 «Implement graceful degradation to transform applicable hard dependencies into soft dependencies» — https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html — no date shown; risk level if not established: «High».
- «Application components should continue to perform their core function even if dependencies become unavailable.» SV
- «They might be serving slightly stale data, alternate data, or even no data.» SV
- «Failure modes of components should be seen as normal operation.» SV
- Anti-patterns: «Serving no data on errors or when only one out of multiple dependencies is unavailable and partial results can still be returned.» SV. «Invalidating or emptying local state as a result of a failed refresh without considering the consequences of doing so.» SV. The second is exactly the "failed nightly job blanks the page" failure.
SRE book ch. 22 "Addressing Cascading Failures" — https://sre.google/sre-book/addressing-cascading-failures/ — Mike Ulrich
- «A cascading failure is a failure that grows over time as a result of positive feedback.» SV
- «Load shedding drops some proportion of load by dropping traffic as the server approaches overload conditions.» SV
- «Graceful degradation takes the concept of load shedding one step further by reducing the amount of work that needs to be performed.» SV
- «Graceful degradation shouldn't trigger very often—usually in cases of a capacity planning failure or unexpected load shift.» SV
- «Remember that the code path you never use is the code path that (often) doesn't work.» SV. The fallback you never exercise is the one that fails.
- «Always use randomized exponential backoff when scheduling retries.» SV
Timeouts, retries, jitter: AWS Builders' Library (Brooker) NOT REACHED. It redirects to builder.aws.com, which returned metadata only. Two attempts; nothing quoted.

====================================================================
ITEM 5 — SCHEDULED JOBS AND THEIR SILENT FAILURES

5a. GitHub Actions docs, `schedule` event — https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows (read at offset 100000). Platform documentation; no date on page. Strength: authoritative for the platform, and it changes.
- «Scheduled workflows run on the latest commit on the default branch.» SV. Also present: «Scheduled workflows will only run on the default branch.» SV
- «The shortest interval you can run scheduled workflows is once every 5 minutes.» SV
- «The schedule event can be delayed during periods of high loads of GitHub Actions workflow runs.» SV «High load times include the start of every hour.» SV «If the load is sufficiently high enough, some queued jobs may be dropped.» SV «To decrease the chance of delay, schedule your workflow to run at a different time of the hour.» SV
- «In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days.» SV
- CHANGED SINCE EARLIER DOCS: «By default, scheduled workflows run in UTC. You can optionally specify a timezone using an IANA timezone string for timezone-aware scheduling.» SV. Older docs said UTC only.
- «Notifications for scheduled workflows are sent to the user who last modified the cron syntax in the workflow file.» SV
- «Scheduled workflows will not run if the last `actor` associated with the scheduled workflow has been deprovisioned by the Enterprise Managed User identity provider (IdP).» SP. Applies to Enterprise Managed Users only.
Role: four documented ways the free scheduler silently stops (dropped under load, delayed, disabled after 60 quiet days, alerting one person), in the platform's own words. Note that "may be dropped" means not run at all, not merely late.

5b. Heartbeat / dead man's switch (vendor practice)
Healthchecks.io — https://healthchecks.io/docs/ — footer "© 2015-2026"
- «Healthchecks.io is a service for monitoring cron jobs and similar periodic processes:» SV
- «Healthchecks.io listens for HTTP requests ("pings") from your cron jobs and scheduled tasks.» SP «It keeps silent as long as pings arrive on time.» SV «It raises an alert as soon as a ping does not arrive on time.» SV
- «Healthchecks.io works as a dead man's switch for processes that need to run continuously or on a regular, known schedule.» SV
- Grace Time: «the additional time to wait before sending an alert when a check is late.» SP
Cronitor — https://cronitor.io/docs/heartbeat-monitoring — no date
- «Cronitor's heartbeat monitoring provides a simple way to ensure your systems, services, and processes are running as expected.» SP «Send periodic "I'm alive" signals to Cronitor and get alerted when something stops working.» SV
- «When heartbeats stop arriving or report failures an alert is sent to the monitor's alert recipients.» SV (link text aside). Cronitor does not use "dead man's switch" on that page.

5c. cron man pages (cronie, via man7.org) — reference documentation
crontab(5) — https://man7.org/linux/man-pages/man5/crontab.5.html — footer «cronie 2012-11-22 CRONTAB(5)»
- «If MAILTO is defined (and non-empty), mail is sent to the specified address. If MAILTO is defined but empty (MAILTO=""), no mail is sent. Otherwise, mail is sent to the owner of the crontab.» SV
- «Note that this means that non-existent times, such as the "missing hours" during the daylight savings time conversion, will never match, causing jobs scheduled during the "missing times" not to be run.» SV
cron(8) — https://man7.org/linux/man-pages/man8/cron.8.html — «This page was obtained from the project's upstream Git repository on 2026-08-03.»
- «When executing commands, any output is mailed to the owner of the crontab (or to the user specified in the MAILTO environment variable in the crontab, if such exists).» SV
- «The syslog output will be used instead of mail, when sendmail is not installed.» SV
- «If time was adjusted one hour forward, those jobs that would have run in the interval that has been skipped will be run immediately.» SV
HONEST NEGATIVE: neither page says "cron does not report failures". Both, on a direct check, say NOTHING about exit status or job failure. What can be written is: cron's only reporting channel is mailing a job's output to the crontab owner (or syslog if no mailer); the manual defines no notion of a failed job. That is the chapter's inference from silence, not a quotation.

5d. SRE book ch. 24 "Distributed Periodic Scheduling with Cron" — https://sre.google/sre-book/distributed-periodic-scheduling/ — Štěpán Davidovič, ed. Kavita Guliani
- «Cron's failure domain is essentially just one machine.» SV «If the machine is not running, neither the cron scheduler nor the jobs it launches can run.» SV
- «Cron jobs are designed to perform periodic work, but beyond that, it is hard to know in advance what function they have.» SV
- «Some cron jobs, such as garbage collection processes, are idempotent. In case of system malfunction, it is safe to launch such jobs multiple times. Other cron jobs, such as a process that sends out an email newsletter to a wide distribution, should not be launched more than once.» SP
- «For example, a garbage collection cron job scheduled to run every five minutes may be able to skip one launch, but a payroll cron job scheduled to run once a month should not be skipped.» SP
- «In general, we favor skipping launches rather than risking double launches, as much as the infrastructure allows.» SV
- «Cron job owners can (and should!) monitor their cron jobs; for example, an owner might have the cron service expose state for its managed cron jobs, or set up independent monitoring of the effect of cron jobs.» SV. "Monitoring of the effect" is the best single sentence for checking the output rather than the job.
- «anacron attempts to launch jobs that would have been launched when the system was down.» SV
- «When people think of a "daily cron job," they commonly configure this job to run at midnight.» SP. Pairs with GitHub's "start of every hour".

====================================================================
ITEM 6 — STATIC AND BAKED-DATA ARCHITECTURES

6a. Willison, "Git scraping: track changes over time by scraping to a Git repository" — https://simonwillison.net/2020/Oct/9/git-scraping/ — 9th October 2020. Practitioner blog; originates the term.
- «Git scraping is the name I've given a scraping technique that I've been experimenting with for a few years now.» SV «It's really effective, and more people should use it.» SV
- «The internet is full of interesting data that changes over time.» SV
- «We already have a great tool for efficiently tracking changes to text over time: Git.» SV ("Git" is bold on the page)
- «And GitHub Actions (and other CI systems) make it easy to create a scraper that runs every few minutes, records the current state of a resource and records changes to that resource over time in the commit history.» SV
- «Every 20 minutes it grabs the latest copy of that JSON endpoint, pretty-prints it (for diff readability) using jq and commits it back to the repo if it has changed.» SV. His cron line is `'6,26,46 * * * *'`, off the top of the hour.
- «It's an extremely effective way of turning all sorts of interesting data sources into a changelog over time.» SV
- CORRECTIONS TO THE BRIEF: "surprisingly powerful" does NOT appear; the words are "really effective" and "extremely effective". The word "free" does not appear. The post names no caveats or failure modes; that silence is worth stating.

6b. Willison, "The Baked Data architectural pattern" — https://simonwillison.net/2021/Jul/28/baked-data/ — 28th July 2021
- Opening: «I've been exploring an architectural pattern for publishing websites over the past few years that I call the 'Baked Data' pattern. It provides many of the advantages of static site generators while avoiding most of their limitations. I think it deserves to be used more widely.» SP
- Definition: «Baked Data: bundling a read-only copy of your data alongside the code for your application, as part of the same deployment» SV. Note it is "bundling", not "bundle" as in the brief.
- «Most dynamic websites keep their code and data separate: the code runs on an application server, the data lives independently in some kind of external data store—something like PostgreSQL, MySQL or MongoDB.» SV
- Benefits: «Inexpensive to host. Anywhere that can run application code can host a Baked Data application—there's no need to pay extra for a managed database system.» SV. «Scale to zero serverless hosts such as Cloud Run, Vercel or AWS Lambda will charge only cents per month for low-traffic deployments.» SP. «Easy to scale. Need to handle more traffic? Run more copies of your application and its bundled data. Horizontally scaling Baked Data applications is trivial.» SV. «Difficult to break. Hosting server-side applications on a VPS is always disquieting because there's so much that might go wrong—the server could be compromised, or a rogue log file could cause it to run out of disk space.» SV. «With Baked Data the worst that can happen is that you need to re-deploy the application—there's no risk at all of data loss, and providers that can auto-restart code can recover from errors automatically.» SP. Other benefit headings (SP): "Server-side functionality", "Templated pages", "Easy to support multiple formats", "Integrates well with version control".
- Trade-off: «Since every change to the data results in a fresh deployment this pattern doesn't work for sites that change often—but in my experience many content-oriented sites update their content at most a few times a day.» SV
- Cadence, of datasette.io: «The site is automatically deployed once a day by a scheduled action, and I can also manually trigger that action if I want to ensure a new software release is reflected on the homepage.» SP
- «The site content lives in a ~22MB SQLite database file, which is built inside GitHub Actions by the build.sh script» SP
- No size limit is named in the post.
Datasette publish — https://docs.datasette.io/en/stable/publish.html (stable docs; no version or date shown)
- «Datasette includes tools for publishing and deploying your data to the internet.» SV «The datasette publish command will deploy a new Datasette instance containing your databases directly to a Heroku or Google Cloud hosting account.» SV

6c. PMTiles — https://docs.protomaps.com/pmtiles/ — no date. Project documentation.
- «PMTiles is a single-file archive format for pyramids of tiled data.» SV. Current wording has "pyramids of"; the brief's wording is out of date.
- «A PMTiles archive can be hosted on a storage platform like S3, and enables low-cost, zero-maintenance map applications.» SV. Now "a storage platform like S3", not "commodity storage platform such as S3".
- «PMTiles readers use HTTP Range Requests to fetch only the relevant tile or metadata inside a PMTiles archive on-demand.» SV
- Limit: «PMTiles is a read-only format.» SV «It is not possible to update an archive in-place without re-writing the entire file, similar to CSV, JSON and Parquet.» SV
- The words "serverless" and "tile server" do not appear on that page.

6d. DuckDB-Wasm (practice) — https://duckdb.org/docs/current/clients/wasm/overview.html — page shows version 1.5.6
- «DuckDB-Wasm is a version of DuckDB that has been compiled to WebAssembly, the portable binary format that browsers can run at near-native speed.» SV
- «This lets a full DuckDB engine run entirely inside any browser on any device, with no server to send queries to and no data leaving the user's machine.» SV
- «Because DuckDB understands file formats such as Parquet, it reads only the bytes a query needs rather than downloading an entire file» SV
- Limits: «By default, the WebAssembly client only uses a single thread.» SV «WebAssembly limits the amount of available memory to 4 GB and browsers may impose even stricter limits.» SV

6e. Static-hosting free tiers (practice; figures as displayed 6 Oct 2026)
Cloudflare Pages limits — https://developers.cloudflare.com/pages/platform/limits/ — «Last updated Sep 5, 2026»
- «Builds per month | 500» (Free). SV «Cloudflare Pages sites can contain up to 20,000 files on the Free plan.» SV «The maximum file size for a single Cloudflare Pages site asset is 25 MiB.» SV «Builds will timeout after 20 minutes.» SV «Cloudflare Pages has a limit of 100 projects per account.» SV. "1 build at a time" and "100 custom domains per project": SP.
- 25 MiB per asset is a hard ceiling on a single baked data file or PMTiles archive served as a Pages asset. A larger file needs object storage.
Cloudflare Pages Functions pricing — https://developers.cloudflare.com/pages/functions/pricing/ — «Last updated Sep 8, 2026»
- «On both free and paid plans, requests to static assets are free and unlimited.» SV
GitHub Pages limits — https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits — no date (© 2026 footer)
- «Published GitHub Pages sites may be no larger than 1 GB.» SV «GitHub Pages sites have a soft bandwidth limit of 100 GB per month.» SV «GitHub Pages sites have a soft limit of 10 builds per hour. This limit does not apply if you build and publish your site with a custom GitHub Actions workflow.» SV «GitHub Pages deployments will timeout if they take longer than 10 minutes.» SV
- «GitHub Pages is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS).» SV
- «GitHub Pages is available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.» SV
GitHub Actions billing — https://docs.github.com/en/billing/concepts/product-billing/github-actions — no date
- «GitHub Actions usage is free for self-hosted runners and for public repositories that use standard GitHub-hosted runners.» SV (bold markup aside). GitHub Free row for private repositories: «500 MB | 2,000 | 10 GB» (artifact storage, minutes per month, cache). SV
Netlify — https://www.netlify.com/pricing/ — page carries a 4 September 2025 note on plan changes
- Free: «$0 forever», «300 credit limit / month». SV. «When a site reaches its monthly usage limits, it enters a paused state until the start of the next billing cycle.» SV «The free plan is always free, with hard monthly limits that cannot be exceeded or incur any costs.» SV
- Netlify's free tier is now metered in "credits", not bandwidth and build minutes, and a site that hits the cap is PAUSED. I did not establish what a credit buys.

====================================================================
ITEM 7 — THE MAINTENANCE BURDEN

7a. Maintenance share of cost. No open primary empirical source reached for the classic 60–80% figure. What is open:
- US GAO, "Information Technology: Agencies Need to Develop Modernization Plans for Critical Legacy Systems", GAO-19-471, published Jun 11, 2019 — https://www.gao.gov/products/gao-19-471. Official audit evidence about US federal IT SPENDING, not a software-engineering lifecycle study. Strong for what it measures.
  «The federal government plans to spend over $90 billion in fiscal year 2019 on IT.» SV «About 80 percent of this amount is used to operate and maintain existing IT investments, including aging (also called legacy) systems.» SV «As they age, legacy systems can be more costly to maintain, more exposed to cybersecurity risks, and less effective in meeting their intended purpose.» SV
- Pragmatic Bookshelf blurb for Release It!: «Eighty percent of project life-cycle cost is in production, yet few books address this topic.» SV. Marketing copy, unsourced; cultural reference only.
- Nygard ch. 1 excerpt: «Systems spend much more of their life in operation than in development—at least, the ones that don't get canceled or scrapped do.» SV. Practitioner assertion.
- Wikipedia "Software maintenance" (SECONDARY) — https://en.wikipedia.org/wiki/Software_maintenance: «If conceived of as part of the software development life cycle, maintenance is the last and typically the longest phase of the cycle, comprising 80 to 90 percent of the lifecycle cost.» SV, cited there to Ulziit et al. 2015, p. 764. «According to some estimates, enhancement (the latter two categories) comprises some 80 percent of software maintenance.» SV, cited to Varga 2018, p. 5 fn 4. The article does NOT mention Lientz and Swanson. I did not reach either cited source.
- Winters, Software Engineering at Google, ch. 1 — https://abseil.io/resources/swe-book/html/ch01.html (open). Authoritative practice.
  «Within Google, we sometimes say, 'Software engineering is programming integrated over time.'» SV «Your project is sustainable if, for the expected life span of your software, you are capable of reacting to whatever valuable change comes along, for either technical or business reasons.» SV «Over a span of a decade or more, most program dependencies, whether implicit or explicit, will likely change.» SV Hyrum's Law: «With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviors of your system will be depended on by somebody.» SV
- SRE book ch. 5 "Eliminating Toil" — https://sre.google/sre-book/eliminating-toil/ — Vivek Rau
  «Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.» SV «If a human operator needs to touch your system during normal operations, you have a bug.» SV, attributed on the page to Carla Geisser, Google SRE; the page is quoting her. «If your service remains in the same state after you have finished a task, the task was probably toil.» SV «If a machine could accomplish the task just as well as a human, or the need for the task could be designed away, that task is toil.» SV «At least 50% of each SRE's time should be spent on engineering project work that will either reduce future toil or add service features.» SV
Verdict: the chapter can say maintenance dominates on the strength of GAO (measured, for government IT) and practitioner authority. It should NOT present "60–80% of lifecycle cost" as an established open finding. The Lientz & Swanson, Boehm and Glass sources are closed and were not read.

7b. Open-source maintainers
- Tidelift 2024 maintainer survey: NOT VERIFIED. The landing page (https://tidelift.com/open-source-maintainer-survey-2024) carries no figures because the report is behind a form, and the blog URL I tried returned 404. Two attempts. The "60% of maintainers are unpaid" figure is UNCONFIRMED. Do not use it without the report.
- Eghbal, "Roads and Bridges: The Unseen Labor Behind Our Digital Infrastructure", Ford Foundation, 14 July 2016 — https://www.fordfoundation.org/learning/library/research-reports/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/ (summary page; qualitative foundation report):
  «Free, publicly available source code is the infrastructure on which all of digital society relies.» SV «However, few realize that public code is built and maintained almost exclusively by unpaid volunteers, and the enormous amount of work required is in desperate need of institutional support.» SV «Without effective support for coders' work on publicly available projects, not only will their labor go uncompensated, but the digital world risks security breaches, interruptions in service, and slowed innovation.» SV
- xkcd 2347 "Dependency" — https://xkcd.com/2347/ (CULTURAL REFERENCE). Title text: «Someday ImageMagick will finally break for good and we'll have a long period of scrambling as we try to reassemble civilization from the rubble.» SP. No date on the page and the reader could not transcribe the image. Do not quote the in-image caption from memory.

7c. Bus factor / truck factor
- Avelino, Passos, Hora, Valente, "A Novel Approach for Estimating Truck Factors", arXiv:1604.06766, submitted 22 Apr 2016, ICPC 2016 — https://arxiv.org/abs/1604.06766. Peer-reviewed evidence; 133 projects, 2016 data. Abstract:
  «Truck Factor (TF) is a metric proposed by the agile community as a tool to identify concentration of knowledge in software development environments.» SV «It states the minimal number of developers that have to be hit by a truck (or quit) before a project is incapacitated.» SV «…which we execute against a corpus of 133 popular project in GitHub» SV (sic "project") «…we find that the majority of our target systems (65%) have TF <= 2.» SV
  The verified wording is 65% with truck factor of 2 or less, not "most have 1 or 2". Also in the abstract (SP): surveyed developers from 67 systems; «in 84% of the valid answers… developers agree or partially agree that the TF's authors are the main authors of their systems; in 53% we receive a positive or partially positive answer regarding our estimated truck factors». Agreement with the estimates themselves was only about half.
- Wikipedia "Bus factor" (SECONDARY) — https://en.wikipedia.org/wiki/Bus_factor: «The bus factor (aka lottery factor, truck factor, or circus factor) is a measurement of the risk resulting from information and capabilities not being shared among team members, derived from the phrase "in case they get hit by a bus".» SV «Studies conducted in 2015 and 2016 calculated the bus/truck factor of 133 popular GitHub projects. The results show that most of the systems have a small bus factor (65% have bus factor ≤ 2) and the value is greater than 10 for less than 10% of the systems.» SV

====================================================================
ITEM 8 — DATA PIPELINE FAILURE MODES AND OBSERVABILITY

8a. SRE Workbook, "Data Processing Pipelines" — the brief's URL returns 404. The live URL is https://sre.google/workbook/data-processing/. Authors as given by the reader (SP): Rita Sodt and Igor Maravić (Spotify), with Gary Luo, Gary O'Connor, and Kate Ward. No year on the page. Authoritative practice. I read the first 100,000 of 104,025 characters.
- Data freshness: «Most pipeline data freshness SLOs are in one of the following formats:» SV, then «X% of data processed in Y [seconds, days, minutes].» «The oldest data is no older than Y [seconds, days, minutes].» «The pipeline job has completed successfully within Y [seconds, days, minutes].» SV
- Data correctness: «Creating SLOs for data correctness ensures that you are alerted about potential data errors in your pipeline. For example, a correctness error in a billing pipeline could result in customers being charged too much or too little.» SV
- Also named under SLOs: "Data isolation/load balancing" and "End-to-end measurement" (headings SP). «Measuring SLOs in this fashion doesn't capture your customer's experience or the end-to-end health of your system.» SP
- Coverage is NOT named as an SLI in this chapter as far as the reader showed. The brief's "freshness, correctness, coverage" is not what the chapter has; do not attribute "coverage" to it.
- Failure modes: Delayed data: «A pipeline can fail if its input or output is delayed.» SV «If your pipeline stalls, waits for data, and then resumes once the data becomes available, the data remains high quality.» SV. Corrupt data: «If undetected, corrupt pipeline data (input and/or output) can cause user-facing issues. You can circumvent many user-facing issues by having tests that identify corrupt data in place.» SV
- Potential causes (headings SP): Pipeline dependencies; Pipeline application or configuration; Unexpected resource growth; Region-level outage. «When you're trying to determine the cause of an outage, it's useful to investigate pipeline dependencies, such as storage, network systems, or other services. These dependencies may be throttling your requests/traffic or, if they are out of resources, refusing any new data.» SV
- Idempotency: «An idempotent mutation is a type of mutation that can be applied multiple times with the same result.» SV «Implementing this design pattern allows separate executions of a pipeline with the same input data to always produce the same result.» SV
- Checkpointing: «Checkpointing is a technique that enables long-running processes like pipelines to periodically save partial state to storage so that they can resume the process later.» SV
- The words "silent" and "silently" do NOT appear in the chapter.

8b. "Data observability", five pillars (VENDOR PRACTICE) — Monte Carlo. The brief's domain now 302-redirects from montecarlodata.com to https://montecarlo.ai/blog-what-is-data-observability. Author Barr Moses; page shows «Published: July 31, 2025» and «Modified: September 25, 2026» (an often-revised marketing page, not the original 2019–20 essay).
- «Data observability provides full visibility into the health of your data and systems so you are the first to know when the data is wrong, what broke, and how to fix it.» SV. The older definition in my prompt («an organization's ability to fully understand the health of the data in their systems») was not returned; do not use it.
- Pillars are section headings: Freshness, Quality, Volume, Schema, Lineage. The second is now "Quality", not "Distribution" as in the brief. No single sentence lists all five.
- «Freshness seeks to understand how up-to-date your data tables are, as well as the cadence at which your tables are updated.» SV «Freshness is particularly important when it comes to decision making; after all, stale data is basically synonymous with wasted time and money.» SV
- «Data downtime — periods of time when data is partial, erroneous, missing, or otherwise inaccurate — only multiplies as data systems become increasingly complex, supporting an endless ecosystem of sources and consumers.» SV
- Volume, Schema and Lineage definitions: SP only.

====================================================================
ITEM 9 — COST OF "LIVE" VERSUS "NIGHTLY"

Mapbox pricing — https://www.mapbox.com/pricing — fetched 6 Oct 2026; no date or year on the page. Pricing pages change, so date every figure.
- Map Loads for Web (Mapbox GL JS): free «Up to 50,000» monthly loads. SV. 50,001–100,000: «$5.00» per 1,000. SV. 100,001–200,000: «$4.00» per 1,000. SV. 200,001–1,000,000: $3.00; 1,000,001–5,000,000: $2.50; above that, contact sales. SP
- «A map load is counted every time Mapbox GL JS initializes on a webpage or in a web app.» SV «A map load includes unlimited Vector Tiles API and Raster Tiles API requests.» SV
- Temporary Geocoding API: free «Up to 100,000» monthly requests, then «$0.75» per 1,000 for 100,001–500,000. SV. Static Images API: free up to 50,000, then $1.00 per 1,000. SP
Against it (Item 6e, same date): Cloudflare Pages «requests to static assets are free and unlimited» (SV) with a 25 MiB per-asset cap; GitHub Pages 1 GB site and 100 GB/month soft bandwidth (SV); GitHub Actions free for public repositories on standard runners (SV).
Chapter's own arithmetic, mark as such: a page whose map initialises 60,000 times in a month is 10,000 loads over the free tier, so 10 × $5.00 = $50 that month. The same map from a static PMTiles file on a free static host is $0 in fees, subject to the size and bandwidth limits above. Billing is per map initialisation, not per visitor or per tile, so a page that re-initialises the map on each view pays per view.
Not established: Mapbox's terms on caching or offline tiles, and whether "free" static hosting carries any availability commitment (see Left out).

====================================================================
ITEM 10 — THE HEARTBEAT ON THE FACE (showing the time of last successful refresh)

No design-system pattern found that says "a dashboard should show its last successful refresh time".
- GOV.UK Design System patterns index — https://design-system.service.gov.uk/patterns/ — every pattern listed; NONE concerns dashboards, data freshness or "last updated" (direct YES/NO check: NO).
- IBM Carbon dashboards guidance — https://carbondesignsystem.com/data-visualization/dashboards/ — nothing on timestamps, freshness, or loading/error states (SP negative).
- PatternFly dashboard guidelines — https://www.patternfly.org/patterns/dashboard/design-guidelines — nothing on refresh timestamps (SP negative).
- Government Analysis Function dashboard guidance: NOT FOUND. Two guessed URLs returned 404; the policy-store index showed only 10 of 159 items, none relevant. I cannot say whether it exists. Not attempted: 18F/USDS, ONS service manual.
Nearest open support, to be labelled for what each is:
(a) General heuristic. Nielsen, "10 Usability Heuristics for User Interface Design", #1 Visibility of system status — https://www.nngroup.com/articles/ten-usability-heuristics/ — Jakob Nielsen, April 24, 1994; updated January 30, 2024. «The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time.» SV «When users know the current system status, they learn the outcome of their prior interactions and determine next steps.» SV «Predictable interactions create trust in the product as well as the brand.» SV. Expert heuristic, not about data freshness specifically.
(b) Platform practice. Google's dashboard product documents a last-refresh stamp on the report face — https://docs.cloud.google.com/data-studio/manage-data-freshness — «Last updated 2026-10-05 UTC.» «The time and date of the last data refresh is displayed in the bottom left corner of the report.» SV. Also: «Data freshness works by temporarily storing in memory the queries and result generated by your reports.» SP. Google Sheets refresh options «Every 15 minutes* Every 1 hour Every 4 hours Every 12 hours» SV. The product has been renamed: «Looker Studio is now called Data Studio.» SV
(c) Metadata standard, the machine-readable heartbeat. W3C DCAT 3, W3C Recommendation 22 August 2024 — https://www.w3.org/TR/vocab-dcat-3/ — dcterms:modified: «Most recent date on which the resource was changed, updated or modified.» SV. Usage note: «An absent value MAY indicate that the resource has never changed after its initial publication, or that the date of last modification is not known, or that the resource is continuously updated.» SV. That is a standard admitting a missing date is ambiguous three ways. The definition for "frequency" (dcterms:accrualPeriodicity) was not retrieved because the page was truncated.
(d) Protocol. RFC 9111's Age header (Item 1a) is the HTTP-level statement of how old what you are looking at is.
(e) GOV.UK patterns for when the thing is down:
 "Service unavailable pages" — https://design-system.service.gov.uk/patterns/service-unavailable-pages/ — «Tell the user a service is unavailable on purpose.» SV «These are also known as 503 and shutter pages.» SV «Use a service unavailable page when a service has been closed on purpose.» SV. The page should include «the day, date and time it is going to be available or what to do if it is permanently closed» SV. «If there is a problem with the service, use a There is a problem with the service page.» SV
 "There is a problem with the service pages" — https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/ — «Tell the user there is something wrong with the service. These are also known as 500 and internal server error pages.» SP «Use this page when there is an unexpected problem with the service. Use the same page for all unexpected problems.» SP. Should not include breadcrumbs, technical jargon, 'We are experiencing technical difficulties', or red text (SP list).

====================================================================
UNEXPECTED THREADS (not asked for)
1. GitHub scheduled workflows are now timezone-aware (IANA timezone string, default UTC). Any chapter text saying "cron on GitHub is UTC only" is out of date.
2. A dropped scheduled job is documented behaviour: «some queued jobs may be dropped». A nightly job on the free scheduler has no guarantee of running at all, and GitHub's own advice is to avoid the top of the hour.
3. The alarm has a bus factor of one: «Notifications for scheduled workflows are sent to the user who last modified the cron syntax in the workflow file.» When that person leaves, the failure emails go to nobody the studio reads.
4. AWS names the exact "failed refresh blanks the page" bug as an anti-pattern («Invalidating or emptying local state as a result of a failed refresh…»), and RFC 5861's stale-if-error is the protocol-level remedy. Standard and practice agree: on failure, keep the last good copy.
5. SRE's "golden signal" definition of an error includes «an HTTP 200 success response, but coupled with the wrong content». For a dashboard, a page that loads with stale or empty data is an error that uptime checks will not see. That is the argument for checking the data's date, not the page's status code.
6. The standard for rate limiting declines to say how limits are counted (RFC 6585), and the header that would advertise quotas is still an Internet-Draft at version 11 with no intended status. Every platform's rate-limit headers are therefore its own convention.
7. Vendor and product churn observed in this one run: Looker Studio renamed Data Studio; montecarlodata.com redirecting to montecarlo.ai; Netlify free tier re-denominated in credits with a paused state; AWS Builders' Library moved to builder.aws.com; Azure's bulkhead definition rewritten; the PMTiles tagline reworded; the SRE Workbook URL in the brief dead. That is first-hand evidence for the maintenance-burden section: about a quarter of the "stable" URLs and phrasings in the brief had drifted.
8. PMTiles and Baked Data share one stated limit: read-only, with any update meaning rewrite and redeploy. Willison draws the boundary at content that changes «at most a few times a day». That is the "nightly versus live" line in a practitioner's words.

LEFT OUT, AND WHY
- RFC 9110 §8.8.3 and §13: the reader truncates the document. Nothing quoted.
- Tidelift 2024 figures: gated or 404; unverified.
- AWS Builders' Library on timeouts, retries and jitter: client-rendered, body not returned.
- GitHub Online Services SLA: one attempt, HTTP 500. So I could NOT establish what uptime commitment, if any, attaches to GitHub Pages or Actions on free plans. The chapter should not assert either way.
- Lientz & Swanson, Boehm, Glass, Standish, ISO/IEC 14764, SWEBOK: closed or not attempted; no open primary for the 60–80% figure.
- Nygard's own definitions of circuit breaker, bulkhead, timeouts and fail fast (ch. 5): not in the free excerpts. His blog was not attempted.
- The ACM Queue subtitle and exact month: not shown to the reader.
- The last 4,025 characters of the Workbook pipelines chapter and the tail of DCAT 3 (the frequency definition): unread.
- The MDN browser-compatibility tables for stale-while-revalidate and stale-if-error: prose only was read.
- Mapbox terms of service, what a Netlify credit buys, Cloudflare R2 pricing for files over 25 MiB: not fetched.
- Per the brief, no ticketing or music platform, and nothing on what the dashboard should look like.

RICH REFERENCES (three)
1. Treynor, Dahlin, Rau, Beyer, "The Calculus of Service Availability", ACM Queue 15(2), 2017 — https://queue.acm.org/detail.cfm?id=3096459. The one open, quotable source for dependency-bounded availability, the rule of the extra 9, and "design for graceful degradation".
2. Willison, "The Baked Data architectural pattern", 28 July 2021 — https://simonwillison.net/2021/Jul/28/baked-data/ — with its sibling on git scraping. States the no-admin architecture, its benefits and its boundary in the originator's words.
3. RFC 9111 §4.2–4.3 with RFC 5861 — https://www.rfc-editor.org/rfc/rfc9111 and https://www.rfc-editor.org/rfc/rfc5861. Short, normative, and the source of the chapter's whole vocabulary of freshness and staleness.
Runner-up: SRE book ch. 24 on cron, for «monitoring of the effect of cron jobs» and skip-versus-double-launch.

WHAT SURPRISED ME
- The cron manual never mentions failure at all. The folk claim "cron doesn't report failures" is true only by omission: its entire reporting model is "mail the output to the owner".
- No major design system I could reach (GOV.UK, Carbon, PatternFly) says a dashboard should show when its data was last refreshed. The practice is found in a product's docs (the stamp in the report's bottom-left corner) and in a 1994 heuristic, not in public-sector design guidance. The Analysis Function remains unchecked.
- How much of the brief's own wording had already drifted (see thread 7), including two of the "exact" quotations I was asked to confirm (PMTiles, Azure bulkhead) and a third that never existed in the source ("surprisingly powerful").
- GitHub's documentation plainly says scheduled jobs "may be dropped", and that a public repository's schedule is switched off after 60 days without activity. A finished, stable dashboard is exactly the repository that goes quiet.
- The "five pillars" page is dated as published in 2025 and was modified eleven days before I read it, with one pillar renamed. A vendor's definitional page is not a stable citation.
- Avelino's own validation is weaker than the headline: 65% of projects at truck factor 2 or less, but only 53% of surveyed developers gave a positive or partly positive answer on the estimates.
---

## Agent D — Performance on a phone and map rendering

CHAPTER 8 RESEARCH — FACET: PERFORMANCE ON A PHONE AND MAP RENDERING
Fetched 6 October 2026.

ACCESS NOTE. WebSearch was unavailable (the turn's shared search budget was used up), so everything is from direct URLs via WebFetch. Direct curl is blocked by the egress proxy, so verification was the YES/NO re-fetch method. "STRING-VERIFIED" = confirmed on a second fetch; where the page puts numbers in bold the verifier matched the words but not the markup. Two pages could not be read: the ONS Open Geography Portal API records for the BGC and BUC versions of the December 2024 local authority boundaries (proxy returned HTTP 429, rate limited; not retried). Also unreachable: osdatahub.os.uk/plans (JavaScript-only), Think with Google original page (redirects to an unrelated 2025 article), OS blog "What are vector tiles" (404), MapTiler raster/vector doc (404), OS OpenData licence page (404 / redirect loop), Russell's possible 2026 edition (robots.txt disallowed).

---------------------------------------------------------------
ITEM 1 — CORE WEB VITALS
Source A: web.dev, "Web Vitals", https://web.dev/articles/vitals — "Last updated 2024-10-31 UTC." Official Google guidance (not a standard).
- "Core Web Vitals are the subset of Web Vitals that apply to all web pages, should be measured by all site owners, and will be surfaced across all Google tools." SINGLE PASS
- "To provide a good user experience, LCP should occur within 2.5 seconds of when the page first starts loading." STRING-VERIFIED. Note: the page says "within 2.5 seconds", not "2.5 seconds or less".
- "To provide a good user experience, pages should have a INP of 200 milliseconds or less." STRING-VERIFIED (sic "a INP")
- "pages should maintain a CLS of 0.1. or less" STRING-VERIFIED — the stray full stop after 0.1 is on the page.
- "a good threshold to measure is the 75th percentile of page loads, segmented across mobile and desktop devices." STRING-VERIFIED
Source B: web.dev, "How the Core Web Vitals metrics thresholds were defined", https://web.dev/articles/defining-core-web-vitals-thresholds — Bryan McQuade and Barry Pollard; "Last updated 2025-05-07 UTC."
- "By using the 75th percentile, we know that most visits to the site (3 of 4) experienced the target level of performance or better." STRING-VERIFIED
- "Additionally, the 75th percentile value is less likely to be affected by outliers." STRING-VERIFIED
- "to confirm that a threshold is achievable, we require that at least 10% of origins meet the "good" threshold." SINGLE PASS
- "we find that the 1.5 and 2 second thresholds are not consistently achievable, while 2.5 seconds is consistently achievable." SINGLE PASS
- Table figures (single pass): 3.5% of phone origins meet a 1-second LCP; 42% meet 2.5 seconds. The page cites Miller and Card on attention ("roughly 0.3 to 3 seconds") — that is web.dev quoting research, not the research itself.
Strength: strong as the definition of the thresholds; they are Google's, chosen partly for achievability, not a human-factors constant.
Role: the phone-speed yardstick and its honest basis (2.5s is "what 10%+ of sites can manage", not "what people need").

---------------------------------------------------------------
ITEM 2 — WEIGHT OF THE WEB
Source A: HTTP Archive Web Almanac 2024, Page Weight chapter, https://almanac.httparchive.org/en/2024/page-weight — Dave Smart and Jamie Indigo; dated 2024/12/30 (single pass). Evidence (crawl measurement).
- "In October 2024, the median page weight for a mobile page was 2,311 KB." STRING-VERIFIED
- "The median page weight for a desktop page, as measured in October 2024 is 2,652 KB" STRING-VERIFIED
- JavaScript: "the median desktop page serving 613 KB, on mobile pages it's 558 KB." STRING-VERIFIED (fragment)
- Images: "The median desktop page using images requests 1,054 KB, while mobile pages request 900 KB." STRING-VERIFIED
- "The median page makes 71 requests on desktop and 66 on mobile." STRING-VERIFIED (tense is "makes")
- "The median mobile page has seen a more significant increase of 357%, or 1.8 MB, during the same period" (2014 to 2024). SINGLE PASS
- "the median desktop page could cost a user up to $0.32 USD, or in some regions up to 1.7% of their Gross National Income." SINGLE PASS
Source B: Web Almanac 2024, Performance chapter, https://almanac.httparchive.org/en/2024/performance — Zigisova and Akrap; dated 2024/11/11 (single pass). Evidence (Chrome UX Report field data).
- "If we still used FID as a measure of interactivity, 48% of the websites would have good CWV on mobile devices. However, with the INP metric, this figure drops to 43%." SINGLE PASS for this full wording; the short form "In 2024, 48% of websites had good CWV with FID, and 43% had good CWV with INP" was confirmed YES on the second pass. Treat 43% mobile as verified, exact sentence wording as uncertain.
- "Interestingly, performance on desktop devices stays the same regardless of which responsiveness metric we use at 54%." SINGLE PASS
- Mobile by metric (single pass): "59% of mobile pages achieved a good LCP score"; "In 2024, 74% of mobile and 97% of desktop websites had good INP"; "For mobile sites, 79% of sites have a good score" (CLS).
- "Web performance is tied to what devices and networks people can afford." STRING-VERIFIED (the chapter here is drawing on Alex Russell).
Source C (not asked for — newer edition exists): Web Almanac 2025, published 15 January 2026.
- Page Weight (Richard Barret, Jamie Indigo), https://almanac.httparchive.org/en/2025/page-weight: "The median mobile home page is 2.6 MB, growing 8.4% from 2.4 MB in 2024." STRING-VERIFIED. "In 2025, the median desktop page size reached 2.9 MB, up 7.3% from 2024's median of 2.7 MB." STRING-VERIFIED. Mobile home page: "632 KB of JavaScript", "911 KB of images" (fragments verified). Measured July 2025; note 2025 reports home pages.
- Performance (Jariyal, Rasam, Humaira, Grogg), https://almanac.httparchive.org/en/2025/performance: "Mobile Core Web Vitals have shown consistent year-over-year improvement, increasing from 36% in 2023 to 44% in 2024, and reaching 48% in 2025." STRING-VERIFIED. "However, the improvement for 2025 was marginal, increasing only to 56%." (desktop) STRING-VERIFIED.
DISCREPANCY: the 2024 chapter gives 43% for mobile in 2024; the 2025 chapter's look-back gives 44%. Cite each with its own edition.
Strength: strong, large-sample, methodologically open; medians of the crawled web, not of public-sector sites.
Role: the baseline a dashboard is competing against, and the fact that over half of sites still fail on phones.

---------------------------------------------------------------
ITEM 3 — PERFORMANCE INEQUALITY
Source: Alex Russell, "The Performance Inequality Gap, 2024", https://infrequently.org/2024/01/performance-inequality-gap-2024/. The reader found no day-level date on the page; "January 2024" comes from the URL path only. Practitioner analysis (author's own blog), widely cited (including by the Web Almanac).
- JS-heavy, 5 seconds: "1.3MiB of compressed content to get interactive in five seconds. A page fitting this budget can afford: - 650KiB of HTML, CSS, images, and fonts - 650KiB of JavaScript" (reader's rendering of a list; "650KiB of JavaScript" confirmed present). STRING-VERIFIED in fragments.
- Markup-based, 5 seconds: "To load in five seconds over two connections, we should try to keep content under 2.5MiB, including: - 2.4MiB of HTML, CSS, images, and fonts, and - 100KiB of JavaScript." STRING-VERIFIED
- 3-second figures (single pass, reader summary not quotation): markup-based about 1.4MiB total with 75KiB JS; JS-based about 730KiB total with 365KiB JS.
- Device: "Re-using last year's P75 device calculus, our estimate is based on a device sold new, unlocked for the mid-2020 to mid-2021 global ASP of ~$350-375." STRING-VERIFIED. "Representative examples from that time period include the Samsung Galaxy A51 and the Pixel 4a." STRING-VERIFIED
- Network: "We, therefore, update our P75 link estimate 7.2Mbps down, 1.4Mbps up, and 94ms RTT." STRING-VERIFIED
- The gap: "Devices within the envelope of our attention are 15-25% as fast as those carried by programmers and their bosses — even in wealthy markets." STRING-VERIFIED
- "Inequality is growing faster than the bottom-end can improve." STRING-VERIFIED
Strength: moderate — reasoned estimate from market data, one author, global rather than UK baseline; the budgets are his model's outputs, not measurements.
Role: converts "fast on a phone" into a byte budget; names the developer-hardware blind spot.
Not established: whether a 2025 or 2026 edition exists (series index showed posts to 2024; a guessed 2026 URL was robots-blocked).

---------------------------------------------------------------
ITEM 4 — THE 53% FIGURE
Source: Google (DoubleClick), "The need for mobile speed", https://www.blog.google/products/admanager/the-need-for-mobile-speed/ — 8 September 2016; Alex Shellhammer and Juliette Neel (single pass on authors). Google's own research, vendor-published, ten years old.
- Exact wording on Google's page: "53% of visits are likely to be abandoned if pages take longer than 3 seconds to load" STRING-VERIFIED.
- The commonly repeated form "53% of mobile site visits are abandoned if pages take longer than 3 seconds to load" does NOT appear on this page (checked). Google's wording is "likely to be abandoned".
- Its footnote 6: "Google Data, Aggregated, anonymized Google Analytics data from a sample of mWeb sites opted into sharing benchmark data, n=3.7K, Global, March 2016" SINGLE PASS (the reader first attributed n=3.7K, then showed footnote 5 as n=3.5K and footnote 6 as n=3.7K with 6 attached to the 53% line).
- Also: "the average load time for mobile sites is 19 seconds over 3G connections." STRING-VERIFIED; study "based on our analysis of 10,000+ mobile web domains" (single pass).
Strength: weak-to-moderate. Vendor research, 2016, opt-in sample of 3.7K sites, method not published in detail, pre-dates Core Web Vitals. The Think with Google page that carried the stat now redirects elsewhere.
Role: a figure to cite with its age and origin attached, or not at all.

---------------------------------------------------------------
ITEM 5 — GDS PROGRESSIVE ENHANCEMENT
Source A: GOV.UK Service Manual, "Building a resilient frontend using progressive enhancement", https://www.gov.uk/service-manual/technology/using-progressive-enhancement — Published 23 May 2016; Last updated 27 September 2024. Official guidance.
- "Progressive enhancement is a way of building websites and applications based on the idea that you should make your page work with HTML first." STRING-VERIFIED
- "Only after this can you add anything else like Cascading Style Sheets (CSS) and JavaScript." SINGLE PASS
- "Government services should be functional using only HTML." STRING-VERIFIED
- "A user should be able to navigate through your service using only the HTML." STRING-VERIFIED
- "CSS and JavaScript can fail to load or run because of, for example:" then (list, single pass except the one marked): temporary network errors; third-party browser extensions like ad blockers; third-party supplier downtime, such as when using a content delivery network; DNS lookup failures; bugs introduced by browser updates; bugs introduced in third party JavaScript intentionally running on the same page; corporate firewalls blocking, removing or changing content; "mobile network providers changing content to speed up load times and reduce bandwidth usage" (STRING-VERIFIED); personal firewalls or antivirus software changing or blocking content; the use of unsecure connections, where internet providers insert their own code into the page.
- "Do not build your service as a single-page application (SPA). This is where the loading of pages within your service is handled by JavaScript, rather than the browser." STRING-VERIFIED
Source B: GDS blog, Pete Herlihy, "How many people are missing out on JavaScript enhancement?", 21 October 2013, https://gds.blog.gov.uk/2013/10/21/how-many-people-are-missing-out-on-javascript-enhancement/. Evidence (one measurement, GOV.UK homepage).
- "1.1% of people aren't getting JavaScript enhancements (1 in 93)." STRING-VERIFIED
- "0.2% of all people's browsers who have disabled, or don't support, JavaScript and 0.9% of all people's browsers have JavaScript enabled but don't receive it" STRING-VERIFIED (fragment, grammar as in the original)
- "We deployed this code and then collected the log data from over half a million visits." STRING-VERIFIED
- "progressive enhancement, done well, ensures we always will." STRING-VERIFIED (fragment)
Source C: GOV.UK Service Manual, "Designing for different browsers and devices", https://www.gov.uk/service-manual/technology/designing-for-different-browsers-and-devices — Published 23 May 2016; Last updated 30 January 2026.
- "Your service must be universally accessible. This means building it to work on every browser or device that your users access it on." STRING-VERIFIED
- "You should test your service in these browsers:" STRING-VERIFIED — the current wording is "should", not "must".
- "Some users may access your service using older or unsupported browsers." / "You should use analytics to understand how your users access the service and decide whether additional support is needed." / "Use progressive enhancement to give your service the best possible chance of working for the majority of your users." SINGLE PASS each.
- No statement about low-spec devices or slow connections was found on the page, and no 2% threshold.
Strength: A strong (current official standard for government services); B a single 2013 measurement, still the only public figure of its kind from GDS; C official but thinner than the brief assumed.
Role: the case that failure of JavaScript is mostly involuntary (0.9 of the 1.1 points), and that the remedy is architectural.

---------------------------------------------------------------
ITEM 6 — UK CONNECTIVITY
Source A: Ofcom, Connected Nations UK Report 2025, "Published 19 November 2025", https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/multi-sector/infrastructure-research/connected-nations-2025/connected-nations-uk-report-2025.pdf. Regulator's evidence (operators' predicted coverage).
- "4G coverage from at least one MNO now reaches 96% of the UK landmass." STRING-VERIFIED
- "5G coverage outside of premises from at least one MNO now ranging between 94% and 97%, based on our Very High and High Confidence levels." STRING-VERIFIED (fragment of a longer sentence)
- "5G Standalone (5G SA) is now available across 83% of areas outside of premises in the UK, based on our High Confidence levels." STRING-VERIFIED
- "The MNOs met their 2024 obligations to deliver good geographic coverage to 88% of the UK landmass and have continued to maintain coverage at around this level over the past year." STRING-VERIFIED
- "Overall, 4G geographic coverage remains stable compared to last year, with a one percentage point improvement reported by each individual MNO." STRING-VERIFIED
- "Urban areas, however, have moderately higher 4G geographic coverage, with coverage from all MNOs reaching 98%, and coverage from at least one MNO exceeding 99%." SINGLE PASS (urban only)
- "Indoor mobile coverage can vary depending on factors such as wall thickness, building materials used in construction and where in a building people are using their phone." SINGLE PASS
- NOT FOUND: a UK-wide 4G landmass figure "from all operators", and any not-spot percentage, in either the 2025 or the 2024 report text the reader could see (three passes on 2025). The reader covers only the first ~100,000 characters per call; figures may sit in charts or the interactive report. The complement of the 96% figure (about 4% of landmass with no 4G from anyone) is my inference, not Ofcom's sentence.
Source A2: Connected Nations UK Report 2024, "Published 5 December 2024":
- "4G geographic coverage across individual MNOs in the UK has increased significantly since 2023, rising from a range of 80-87% to 88-89% this year." STRING-VERIFIED
- "4G geographic coverage where it is available from at least one MNO has now reached 95% compared to 93% in 2023." STRING-VERIFIED
Source B: Ofcom, Adults' Media Use and Attitudes Report 2025, "Published 7 May 2025" (Adults' Media Literacy Tracker, 2024 fieldwork), https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/media-literacy-research/adults/adults-media-use-and-attitudes-2025/adults-media-use-and-attitudes-report-2025.pdf?v=396240
- "Around one in five (18%) of adults who go online do so only on a smartphone, not on any other device." STRING-VERIFIED
- "Among adults in a DE household, 30% reported only going online on a smartphone, compared to only 9% of those in AB households." STRING-VERIFIED
- "In 2024, 49% of these users said they struggled to complete forms on a smartphone compared to doing so on a laptop or PC, while 35% agreed that it was difficult to compare products or services." STRING-VERIFIED
- "Despite these challenges, in 2024, around three quarters of adults who use a smartphone only to go online reported never feeling disadvantaged by it (74%)." STRING-VERIFIED
- "Internet access has remained steady over the last few years, with 6% of adults continuing to not have access to the internet at home in 2024." SINGLE PASS
Strength: strong for survey and coverage headlines; coverage is predicted outdoor signal, not experienced speed.
Role: the phone is the only device for roughly a fifth of online adults and three in ten in DE households; coverage is near-universal by landmass from one operator but that is a floor claim.

---------------------------------------------------------------
ITEM 7 — VECTOR VS RASTER TILES
Source A: Mapbox Vector Tile Specification, https://github.com/mapbox/vector-tile-spec. Open specification (de facto standard, vendor-originated). Version 2.1, "January 19, 2016".
- "A specification for encoding tiled vector data." STRING-VERIFIED
- 2.1 README §1: "This document specifies a space-efficient encoding format for tiled geographic vector data." / "It is designed to be used in browsers or server-side applications for fast rendering or lookups of feature data." STRING-VERIFIED
- "The Vector Tile format uses Google Protocol Buffers as a encoding format." STRING-VERIFIED (sic)
- Licence: "The text of this specification is licensed under a Creative Commons Attribution 3.0 United States License." / "However, the use of this spec in products and code is entirely free: there are no royalties, restrictions, or requirements." STRING-VERIFIED
Source B: MapLibre. Homepage (https://maplibre.org/): "The MapLibre Organization is an umbrella for open-source mapping libraries." SINGLE PASS. Repository README (https://github.com/maplibre/maplibre-gl-js):
- "MapLibre GL JS is an open-source library for publishing maps on your websites or webview based apps." STRING-VERIFIED
- "Fast displaying of maps is possible thanks to GPU-accelerated vector tile rendering." STRING-VERIFIED
- "It originated as an open-source fork of mapbox-gl-js, before their switch to a non-OSS license in December 2020." STRING-VERIFIED
- "MapLibre GL JS is licensed under the 3-Clause BSD license." STRING-VERIFIED
Source C: Mapbox Docs, "Vector tiles introduction", https://docs.mapbox.com/data/tilesets/guides/vector-tiles-introduction/ (no date shown). Platform documentation.
- "A Vector tile is the vector data equivalent of raster image tiles for web mapping." STRING-VERIFIED
- "Tiles are styled at runtime, allowing for many map styles on global data." STRING-VERIFIED
- "Vector tiles are small, enabling global high-resolution maps, faster map loads, and efficient caching." STRING-VERIFIED
- Reported YES on a second pass, but I am less sure of these two because the verifier agreed even when I told it I doubted them: "Because all map data is loaded as vectors, the map can be re-rendered quickly in the browser or on a device, enabling smooth zooming, panning, tilt, and rotation." and "Rendering vector tiles in the browser or device requires more processing power compared to displaying pre-rendered raster images." Treat as PROBABLE; check by eye before printing.
Source D: Ordnance Survey docs, OS Vector Tile API, https://docs.os.uk/os-apis/accessing-os-apis/os-vector-tile-api (no date).
- "OS Vector Tile API is a vector tile service providing detailed Ordnance Survey data as a customisable basemap." STRING-VERIFIED
- "Vector tiles have the benefit of being optimised for use across the internet and are great for building interactive web maps." STRING-VERIFIED
- "You can customise the content and the style to create a map that perfectly meets your needs." STRING-VERIFIED
- "Loads maps quicker than traditional raster-mapping services." SINGLE PASS
- OS Maps API by contrast serves "pre-rendered raster tiles" (single pass, docs.os.uk/os-apis/accessing-os-apis/os-maps-api).
Strength: A and B strong as definitions; the client-CPU cost statement rests on one vendor doc and needs an eye check.
Role: the trade — vector moves styling and work to the phone; raster moves it to the server.

---------------------------------------------------------------
ITEM 8 — WHO SERVES THE TILES
8a. OpenStreetMap Foundation, Tile Usage Policy, https://operations.osmfoundation.org/policies/tiles/ (no date or version on the page). Operator policy.
THE POLICY HAS BEEN REWRITTEN. The sentence in the brief ("heavy use ... is forbidden without prior permission") does not appear, nor does "volunteers". Current text:
- "OpenStreetMap (OSM) data is free for everyone to use." STRING-VERIFIED
- "Our tile servers are not: they are funded by donations and sponsorship, and capacity is limited." STRING-VERIFIED
- "To protect the service for mappers and the wider community, you must follow this policy." STRING-VERIFIED
- "We welcome creative uses and do not require you to use a specific API." / "However, heavy or inappropriate use harms others' ability to edit and view the map." / "We may block access, without notice, if your usage degrades the service." STRING-VERIFIED
- "Availability is best-effort: there is no SLA or guarantee." STRING-VERIFIED
- "Access may be blocked without prior notice." STRING-VERIFIED
- "Honour server caching headers (Cache-Control, Expires, Etag). If your cache cannot read them, cache each tile for at least 7 days." STRING-VERIFIED
- "Bulk downloading is any pre-emptive fetching of tiles other than those a user is actively viewing." STRING-VERIFIED (definition; it sits under the heading "Prohibited: bulk downloading ("scraping") and offline use")
- "Offline use is not permitted on tile.openstreetmap.org." STRING-VERIFIED
- "Send a clear, unique User-Agent string that names your app and optionally includes a contact URL or email." SINGLE PASS
- No numeric request limit is stated.
8b. Ordnance Survey.
- osdatahub.os.uk/plans returned only "You need to enable JavaScript to run this app." Plan allowances (including any "£1,000 of premium data free" figure) could NOT be read or verified; nothing quoted.
- Rate limits (https://docs.os.uk/os-apis/core-concepts/rate-limiting-policy, no date): "The OS Data Hub implements rate limiting to maintain the reliability and efficiency of our services." Live mode "Limit: 600 transactions per minute."; development mode "Limit: 50 transactions per minute."; "If the rate limit for an API is exceeded, subsequent requests will be rejected (429) until the rate falls below the allowed threshold." STRING-VERIFIED
- OS Maps API product page lists "OS OpenData Plan (FREE)", Premium Plan, Public Sector Plan (single pass); "Each map style contains OS OpenData and Premium data layers" (single pass).
- Attribution (https://docs.os.uk/os-apis/core-concepts/os-api-branding): "Our logo should be positioned in the embedded map window across all your digital applications." / "Our copyright statement, terms and conditions and error reporting link should be positioned within the embedded map across your web applications." STRING-VERIFIED. The page uses "should", and does not give the copyright wording itself.
- OS Open Zoomstack: "Ordnance Survey's OS Open Zoomstack is an open vector basemap showing coverage of Great Britain from a national level, right down to street detail." STRING-VERIFIED (docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-open-zoomstack). "This product is updated every six months in June and December." STRING-VERIFIED. "Access to this OS OpenData product is free through the OS Data Hub" SINGLE PASS. Format "GeoPackage, vector tiles (MBTiles)". Product page (ordnancesurvey.co.uk/products/os-open-zoomstack): "The data is available in just one single file and provided in easy-to-use formats to help you get started quickly." and "Free to use for everyone" (single pass). The phrase "a single customisable basemap" was not found, and neither page names the Open Government Licence; the OGL statement is unverified here.
8c. Mapbox pricing, https://www.mapbox.com/pricing (no date on page; read 6 October 2026). Platform pricing.
- Map Loads for Web: "Up to 50,000" — Free; "50,001 – 100,000" — "$5.00" per 1,000; then (single pass) $4.00 to 200,000, $3.00 to 1,000,000, $2.50 to 5,000,000. First two rows STRING-VERIFIED.
- "A map load is counted every time Mapbox GL JS initializes on a webpage or in a web app." / "A map load includes unlimited Vector Tiles API and Raster Tiles API requests." STRING-VERIFIED
- Glossary: "The maximum session length for a map load is 12 hours." STRING-VERIFIED
MapTiler Cloud pricing, https://www.maptiler.com/cloud/pricing/ (footer "© 2026 MapTiler"; read 6 October 2026).
- Free plan: API requests "100k/month"; Sessions "5k/month"; "Suitable for testing, PoC, prototyping, personal, or non-commercial use."; "MapTiler logo on the map"; "On a FREE plan service will pause until the next month without an upgrade to paid plans." STRING-VERIFIED
- Flex: "$30/month (USD)", "500k/month" requests, "25k/month" sessions, "$0.15/1k requests", "$2.50/1k sessions". STRING-VERIFIED
- Request weighting table (single pass): vector tile = 1; rendered raster 512x512 tile = 4; raster 256x256 = 1; static maps image = 15.
8d. Protomaps / PMTiles. Project documentation (open source).
- "PMTiles is a single-file archive format for pyramids of tiled data." STRING-VERIFIED (docs.protomaps.com/pmtiles/)
- "A PMTiles archive can be hosted on a storage platform like S3, and enables low-cost, zero-maintenance map applications." STRING-VERIFIED
- "PMTiles readers use HTTP Range Requests to fetch only the relevant tile or metadata inside a PMTiles archive on-demand." STRING-VERIFIED
- "PMTiles is a read-only format. It is not possible to update an archive in-place without re-writing the entire file, similar to CSV, JSON and Parquet." SINGLE PASS
- Basemap: "A full planet file is roughly 120 gigabytes, including zoom levels from 0 to 15." STRING-VERIFIED; "Each additional zoom level roughly doubles the size of the file." STRING-VERIFIED; "It's available as a single PMTiles archive, distributed as an Open Database License Produced Work (OpenStreetMap attribution required)" STRING-VERIFIED; "Please note that URLs may change and hotlinking to these downloads are discouraged." STRING-VERIFIED (docs.protomaps.com/basemaps/downloads)
- Homepage (protomaps.com), single pass: "Protomaps enables frontend developers to easily 'self-host' maps - it's just a file, no server setup required."; hosted API "Noncommercial use is free; for commercial use, become a GitHub Sponsor."
Strength: policies and price lists are authoritative for the day read and will move; OS plan terms are the gap.
Role: the four supply models — donated and unguaranteed (OSM), national mapping agency with keys and rate limits (OS), metered commercial (Mapbox, MapTiler), self-hosted static file (Protomaps).

---------------------------------------------------------------
ITEM 9 — BOUNDARY FILES AND SIMPLIFICATION
Source A: ONS, "Digital boundaries", https://www.ons.gov.uk/methodology/geography/geographicalproducts/digitalboundaries — "Last updated: 4 October 2023". Official product description.
- "(BFC) Full resolution - clipped to the coastline (Mean High Water mark)" STRING-VERIFIED
- "(BFE) Full resolution - extent of the realm (usually this is the Mean Low Water mark but, in some cases, boundaries extend beyond this to include offshore islands)" STRING-VERIFIED
- "(BGC) Generalised (20m) - clipped to the coastline (Mean High Water mark)" STRING-VERIFIED
- "(BUC) Ultra Generalised (500m) - clipped to the coastline (Mean High Water mark)" STRING-VERIFIED
- "The four boundary types we produce are designed to be used in different contexts (such as analysis or visualisation)." STRING-VERIFIED. This page lists FOUR types and does not mention BSC.
- Licence: "Source: Office for National Statistics licensed under the Open Government Licence v.3.0" and "Contains OS data © Crown copyright and database right [year]" STRING-VERIFIED
Source B: Open Geography Portal dataset record (via the portal's API; the portal site itself is JavaScript-rendered), "Local Authority Districts (December 2024) Boundaries UK BSC":
- "This file contains the digital vector boundaries for Local Authority Districts, in the United Kingdom, as at December 2024." STRING-VERIFIED
- "(BSC) Super Generalised (200m) - clipped to the coastline (Mean High Water mark)." STRING-VERIFIED
- "Contains both Ordnance Survey and ONS Intellectual Property Rights." STRING-VERIFIED
- recordCount 361. So BSC exists as a product although the ONS explainer page omits it.
File-size indication (portal record "size" field; what exactly it measures is not documented, treat as indicative only): BFC 127,631,360 bytes; BSC 1,867,776 bytes (a second value 1,671,168 also appears). Roughly 68 to 1 (my arithmetic). BGC and BUC records could not be read (rate limited).
Versioning: the dataset names and descriptions carry the date ("as at December 2024"). ONS administrative geography page (no date shown): "Electoral ward and electoral division boundary changes are usually enacted on the first Thursday in May each year, to coincide with the local government elections in the UK." STRING-VERIFIED. Census 2021 geographies page: "New 2021 LSOAs were created by merging or splitting 2011 LSOAs to ensure that population and household thresholds were met." SINGLE PASS. An official "best-fit" sentence was not obtained (only the fragment "best-fit methodology that uses Census population data" on a 2016-dated postcode products page, single pass).
Source C: Mapshaper docs. Reference (https://mapshaper.org/docs/reference.html): "Mapshaper supports Douglas-Peucker simplification and two kinds of Visvalingam simplification." STRING-VERIFIED. Simplification guide (https://mapshaper.org/docs/guides/simplification.html, no date):
- "Simplification reduces the number of vertices in polylines and polygon boundaries while preserving as much of their shape as possible." SINGLE PASS
- Douglas-Peucker: "Guarantees that simplified lines stay within a fixed distance of the original." / "Good for stripping excess vertices to reduce file size, but tends to introduce visible spikes at high simplification." STRING-VERIFIED
- Visvalingam: "Iteratively removes the point that forms the triangle of smallest area with its two neighbors." STRING-VERIFIED
- "Weighted Visvalingam is Mapshaper's default method because it produces generalizations that look good enough for most web maps, even if they fall short of true cartographic quality." STRING-VERIFIED (corrected on second pass)
- "At high simplification, small polygons can disappear entirely." SINGLE PASS
- "Boundaries shared between the input layers — for example, aligned state and county polygon borders — are simplified identically across all layers, but only if their vertices are perfectly aligned to begin with." STRING-VERIFIED
Source D: TopoJSON README, https://github.com/topojson/topojson (not archived per reader).
- "TopoJSON is an extension of GeoJSON that encodes topology." STRING-VERIFIED
- "Rather than representing geometries discretely, geometries in TopoJSON files are stitched together from shared line segments called arcs." STRING-VERIFIED
- "As a result, TopoJSON is substantially more compact than GeoJSON, frequently offering a reduction of 80% or more even without simplification." STRING-VERIFIED. So the wording is "a reduction of 80% or more", not "typically 80% smaller".
Strength: strong for definitions; file sizes indicative only.
Role: the map's own data can outweigh the whole page budget unless the generalised product is chosen; boundaries are dated products, so a dashboard pins a vintage.

---------------------------------------------------------------
ITEM 10 — ACCESSIBLE MAPS
Source A: W3C WAI Tutorial, "Complex Images", https://www.w3.org/WAI/tutorials/images/complex/ — "Updated 08 April 2026"; non-normative tutorial.
- "Complex images contain substantial information – more than can be conveyed in a short phrase or sentence." STRING-VERIFIED
- list item: "maps showing locations or other information such as weather systems." STRING-VERIFIED
- "In these cases, a two-part text alternative is required." STRING-VERIFIED
- "The second part is the long description – a textual representation of the essential information conveyed by the image." STRING-VERIFIED
Source B: WCAG 2.2 Understanding documents (W3C; the success criteria are normative, the examples informative).
- SC 2.5.7 Dragging Movements (Level AA): "All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential or the functionality is determined by the user agent and not modified by the author." STRING-VERIFIED. Example: "A map allows users to drag the view of the map around, and the map has up/down/left/right buttons to move the view as well." STRING-VERIFIED
- SC 2.5.1 Pointer Gestures (Level A): "All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential." STRING-VERIFIED. Example: "A website includes a map view that supports the pinch/spread gesture to zoom into the map content." "As a single-pointer alternative, the map also includes plus/minus buttons to zoom in and out." STRING-VERIFIED
- SC 2.1.1 Keyboard (Level A): "All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes, except where the underlying function requires input that depends on the path of the user's movement and not just the endpoints." SINGLE PASS
- SC 1.4.1 Use of Color (Level A): "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element." SINGLE PASS
Source C: W3C WAI Research and Development Working Group wiki, "Accessible Maps", https://www.w3.org/WAI/RD/wiki/Accessible_Maps — "last modified on 6 November 2012"; a research note, not guidance. "These days, no standard does exist, which describes how to make a visual map accessible to people with visual disabilities." SINGLE PASS. It does not contain the alternative/keyboard/colour sentences the brief hoped for.
Source D: Government Analysis Function, "Data visualisation: colours", https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/ — published 23 November 2021; last updated "12 February 2026 - sequential colour palette guidance updated". Official cross-government guidance.
- "Maps provide a particular challenge for accessibility as colours are not presented in an order. This can make it difficult to match colours against a legend when there are insufficient contrast ratios between sequential colours. It is essential that data or messages from the data are communicated in an accessible way." STRING-VERIFIED
- For maps, "You should: make sure the data is available in another format such as a downloadable data table" STRING-VERIFIED
- "When you are presenting sequential data, it is best to use a single hue, or small set of closely related hues." SINGLE PASS
- "The more categories you use in a sequential colour palette, the less accessible the colours become, as there is less contrast ratio between neighbouring colours." STRING-VERIFIED
- "Where 5 sequential colours are required, the full set of blue colours shown in the palette table can be used." STRING-VERIFIED. The palette tops out at five blues; I found no sentence saying "no more than 5 bands". "We recommend a limit of four categories as best practice for basic data visualisations." (single pass) is about categorical colour.
GOV.UK Design System: the components list has no Map component (single pass); I found no Service Manual sentence of the form "if you use a map, provide the same information in another format".
Strength: WCAG criteria are the legal-standard layer (public sector bodies regulations point to WCAG AA); the map-specific material is examples and one guidance page.
Role: a map needs a non-map twin (table), buttons for pan and zoom, and a short sequential ramp.

---------------------------------------------------------------
ITEM 11 — MAP WEIGHT ON A PHONE
No source measuring the download size of a typical basemap view for a city was found. What exists:
- Library weight. Leaflet homepage: "Weighing just about 42 KB of JS (42 KB gzipped — that's 142 KB minified and 431 KB in the source form, with 14.5 KB of CSS (3.5 KB gzipped) and 6 KB of images.), it has all the mapping features most developers ever need." STRING-VERIFIED (the parenthetical is tooltip text). Bundlephobia (third-party measurement) reports leaflet 1.9.4 at 148,515 bytes minified, 42,736 gzipped; maplibre-gl "6.12.0" at 1,076,223 bytes minified, 287,311 gzipped (values confirmed on a second read; I have not checked that version number against MapLibre's releases). On those figures the vector renderer alone is about 44% of Russell's 650KiB JavaScript budget (my arithmetic).
- Tile ceiling, not a measurement. Tippecanoe README: "If a tile is larger than 500K, it will try encoding that tile at progressively lower resolutions before failing if it still doesn't fit." SINGLE PASS; option text "maximum compressed tile size instead of 500K".
- Aggregate raster traffic. OSM wiki "Tile disk usage" (last edited 22 September 2026; community wiki): "during August 2026 the tile.openstreetmap.org CDN served approximately 1.7 PB per month (outbound) and 135 billion requests per month" STRING-VERIFIED. That implies about 12.6 KB per request (my division; an average over all responses, not a per-view figure).
- Protomaps cost calculator (docs.protomaps.com/deploy/cost): JavaScript-driven; the reader's account of inputs was inconsistent. Output lines "Protomaps on Cloudflare" and "Hosted Map API" exist; the specific dollar outputs and defaults are unreliable. Do not quote.
- Billing units stand in for size: Mapbox counts a "map load" with unlimited tile requests; MapTiler counts a vector tile as 1 request.
Strength: weak. This is a genuine gap in the published record.

---------------------------------------------------------------
UNEXPECTED THREADS
1. The OSM tile policy has been rewritten in softer, more operational language. The much-quoted "forbidden without prior permission" line is gone; the new text adds "no SLA or guarantee" and an explicit ban on offline use.
2. The OS Data Hub plans page and the ONS Open Geography Portal both return nothing without JavaScript ("You need to enable JavaScript to run this app."). Two public data front doors fail the Service Manual's own "functional using only HTML" test.
3. Web Almanac 2025 (January 2026) is out: mobile median 2.6 MB and 48% of sites passing on mobile. Its 2024 look-back (44%) disagrees with the 2024 edition (43%).
4. Google's own 53% sentence says "likely to be abandoned"; the harder "are abandoned" version is not on Google's blog post, and the Think with Google page is gone.
5. The 2.5-second threshold was set partly by what at least 10% of origins could already achieve; only 3.5% of phone origins met 1 second.
6. WCAG 2.2 uses a map as its worked example for both dragging (2.5.7) and pinch gestures (2.5.1) — pan and zoom buttons are effectively the cited way to conform.
7. ONS's explainer says "four boundary types" while the portal publishes a fifth (BSC, 200m).
8. Ofcom's 2025 report reframes coverage around Map Your Mobile thresholds ("-95dBm and -105dBm ... 50m x 50m pixels") and no longer gives a plain "all operators" 4G landmass line in the text I could read; the 2024 report gave an 88-89% range across individual operators.

LEFT OUT, AND WHY
- OS plan allowances and the "£1,000" figure: unreadable source; not quoted from memory.
- OGL statement for Zoomstack and the OS copyright wording: not on the pages reached.
- ONS BGC/BUC sizes: rate limited.
- ONS boundary guidance document and a clean "best-fit" sentence: live behind the JavaScript portal.
- Russell's day-level date and any later edition: not on the page as read / blocked.
- Protomaps calculator numbers: unreliable read.
- INP's history (FID replaced March 2024), TTFB/FCP, Lighthouse scoring: outside the three-metric brief.
- Any raster/vector comparison from MapTiler or the OS blog: both 404.

RICH REFERENCES
1. Alex Russell, "The Performance Inequality Gap, 2024" — the only source that turns device and network distributions into byte budgets, with its working shown.
2. GOV.UK Service Manual progressive enhancement page together with Herlihy's 2013 measurement — principle and the one public number behind it.
3. HTTP Archive Web Almanac (2024 and 2025 Page Weight and Performance chapters) — open method, yearly series, mobile and desktop split.

WHAT SURPRISED ME
- How little measured evidence exists on what a map costs a phone: prices are per "load" or per "request", and nobody official publishes bytes per view.
- That the vector renderer (about 287 KB gzipped) is roughly seven times the raster library (about 42 KB) before a single tile arrives.
- That full-resolution local authority boundaries are recorded at about 128 MB against under 2 MB for the 200m version — the choice of suffix is the performance decision.
- That the GOV.UK browser-testing page now says "should", carries no device-capability or connection guidance, and was updated as recently as 30 January 2026.
- That 30% of online adults in DE households are smartphone-only, against 9% in AB.
