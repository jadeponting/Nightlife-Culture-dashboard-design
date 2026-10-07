# Chapter 15 — agent returns (assembled 6 October 2026)

Four research agents, dispatched in one message; common brief in the research log, Entry 15. Returns reproduced as received, in full. Working notes, not the chapter; quotations carry the agents' own verification marks.



---

## Agent A

AGENT A — PUBLIC HEALTH DASHBOARDS. Report for Chapter 15. All fetches 6 October 2026.

WebSearch calls used: 15 of 30. Everything else was direct WebFetch.

Verification marks: SV = STRING-VERIFIED (a second fetch with a YES/NO presence prompt, most batches carrying a false control string, all controls correctly returned NO). SP = SINGLE PASS. ABSTRACT = only the abstract was reachable.

Pages I could not read, and why:
- Dong, Du & Gardner 2020 (Lancet Infect Dis 20(5):533-534). PMC returned a reCAPTCHA page; the Europe PMC REST copy (ebi.ac.uk, PMC7159018) was refused by the fetch proxy with HTTP 429 and an instruction not to retry; PubMed returned an empty page; thelancet.com returned 403; web.archive.org is blocked. Nothing is quoted from it.
- Dong et al. 2022 full text (Lancet Infect Dis 22(12):e370-e376): thelancet.com 403, ScienceDirect disallowed by robots.txt. Abstract only, via PubMed.
- The retired coronavirus.data.gov.uk "About the data" and "What's new" pages: the live host fails on robots.txt, the UK Government Web Archive returned 403, web.archive.org is blocked. The two-dates material in A1 therefore comes from PHE/UKHSA blogs, the successor dashboard's documentation and the archive-download page.
- OSR/UKSA "voluntary application" case study on the COVID dashboard: the URL now redirects to a generic Code of Practice page.
- Fingertips FAQ page and two PDFs (Good Indicators Guide, APHO Technical Briefing 2): server error 500.
- Public Health Scotland / ISD "Chart and Dashboard Guidance Paper" v1.1: the isdscotland.org URL now serves a site-retirement notice.
- Crepaz & Arikan journal article (tandfonline 403): only the authors' LSE blog was read.
- "Uncertainty displays in pandemic dashboards: a review of COVID-19 use cases" (PMID 42597657): PubMed returned an empty page twice. Located, not read.
- A caution on the tool: on one first pass it rendered the UKHSA sentence as "Data from the last 5 days by specimen date may be incomplete"; the presence check showed the printed text is "Data for the last 5 days by specimen date are considered incomplete". Treat every SP item below as provisional.

====================================================================
A1. UK COVID-19 DASHBOARD (retired 21 Dec 2023) AND UKHSA DATA DASHBOARD (live)
====================================================================

A1.1 Statement of voluntary compliance with the Code of Practice
URL: https://ukhsa-dashboard.data.gov.uk/compliance (page headed "Compliance"; "Last updated: Tuesday, 9 July 2024 at 09:20am" SP). Official documentation, live.
- "it is not possible for the dashboard to be classed as official statistics" SV. The reason given: "Because different classifications of data are displayed" (SP; quoted back in the verification pass).
- "It is also not possible to meet some other requirements of official statistics. For example, we cannot:" followed by the bullet "Pre-announce the release time of data (usually 4pm every Thursday) via the release calendar" (both SP).
- "so we commit to update the data at 4pm every Thursday" SV. Full sentence SP: "We know timely information is important to our users, so we commit to update the data at 4pm every Thursday."
- "On the rare occasions when delays are unavoidable, we announce this on our homepage" SV.
- "We announce any unexpected changes to the data we release on the homepage and add an explanation to our What's new or About pages" SV apart from the apostrophe glyph in "What's".
- "We have carried out over 100 individual user research sessions" SV.
- "allowing users to download data from every graph displayed on the dashboard" SV.
- "The dashboard has a steering group including members from NHS England, the DHSC and devolved administrations." SP.
Property: trust, provenance.
Mechanism: a public statement, pillar by pillar (trustworthiness, quality, value), of which Code requirements a mixed-status dashboard meets and which it cannot, plus a fixed weekly release time and a named place where unexpected changes are announced. Borrowable: the Code is open to voluntary application by non-official producers and the statement is a short page.
Role: the cleanest worked example of a dashboard saying in public what it is not.

A1.2 Metrics documentation (one page per metric)
URLs: https://ukhsa-dashboard.data.gov.uk/metrics-documentation (index; each entry carries name, description, category, topic, API name; SP) and https://ukhsa-dashboard.data.gov.uk/metrics-documentation/covid-19-cases-cases-by-day ("Last updated on Wednesday, 12 February 2025 at 10:32am" SP). Live.
- Section headings on a metric page: Summary, Rationale, Definition, Methodology, Caveats (SP, same on two metric pages).
- "New cases are reported by specimen date - the date the first sample that identified the infection was taken" SV.
- "Data for the last 5 days by specimen date are considered incomplete" SV; "as it takes time to get test results and record them on relevant lab systems" SV.
- "In England people are counted as new cases if they test positive again more than 90 days after their last positive test." SP.
- "This figure will underestimate the actual number of COVID-19 infections" SV.
- The change-log entry that announced the documentation (21 Dec 2023, "New Feature", https://ukhsa-dashboard.data.gov.uk/whats-new?page=7): "We've added detailed information about available data metrics. This will cover: definition (what the metric is), rationale (why we're showing the metric), methodology (how the metric is collected and calculated), caveats (additional information that will help users to understand what the metric is showing)" SP.
Property: provenance, trust.
Mechanism: every metric has its own page with a fixed five-part template and a machine name that matches the API. Note what the template lacks: no separate "source" or "update frequency" field was visible on the pages read; cadence lives in the compliance page and the change log. Borrowable.
Role: the template to set beside Fingertips' much longer one (A2.5).

A1.3 The change log ("What's new")
URL: https://ukhsa-dashboard.data.gov.uk/whats-new (8 pages on the day; 8 entries on page 1). Live.
- Intro: "We regularly update the dashboard with new data and features." SV. "Here we'll show a timeline of changes that have happened outside of the weekly data refresh" SV (a "that happened" variant returned NO).
- Category labels seen across pages 1, 4, 5, 6, 7 (SP as a set; "Data issue" SV): New metric, New Feature, New content, Update, Change to metric, Data issue, Other.
- Data-issue entries, opened and closed in public: 19 Jan 2024 "Issue: COVID-19 deaths data": "Due to a data issue, COVID-19 deaths data are only available to 29th December 2023" SV. 4 Jan 2024 "Resolved: duplicated rows in bulk download files" SV, ending "We appreciate the user feedback we received flagging this issue" SV. 16 Aug 2024 "Resolved: Issue with COVID-19 cases data": "We have resolved the issue with the COVID-19 cases and case rates data. Updated data has been published." SP. 28 Nov 2024: "On 11 November 2024, a data processing error led to a pipeline failure and prevented the COVID-19 positivity dataset from being produced." SP.
- Cadence changes logged as "Change to metric": "Respiratory viruses data to be updated every 2 weeks" (23 May 2024) SV; "The severity of the measles outbreak has been downgraded. As a result, we will report measles data monthly rather than every 2 weeks." (7 Nov 2024) SP.
- Geography/code changes logged with before-and-after codes (8 Aug 2024 "Changes to region definitions": "This will also affect the previous time series for this data." SP).
Property: change over time, trust.
Mechanism: a dated, labelled timeline separate from the routine refresh, with "Issue:" and "Resolved:" pairs. Borrowable: a label vocabulary and a dated list.
Role: the chapter's primary change-log specimen.

A1.4 The two-dates problem and incomplete recent days
(a) PHE blog, "Coronavirus (COVID-19): Using data to track the virus", 23 April 2020, https://ukhsa.blog.gov.uk/2020/04/23/coronavirus-covid-19-using-data-to-track-the-virus/ (official blog, historic). The passage describes PHE's weekly surveillance report, not the dashboard itself:
- "by the date the specimen was taken from the person being tested, rather than the date the lab carried out testing and sent data to PHE" SV.
- "While this gives the most accurate analysis of how the cases progress over time it does mean that the latest days' figures are usually incomplete – so it shouldn't be seen as a sudden large drop in cases." (fragments SV; whole sentence quoted back in the verification pass).
(b) Archive download page, https://ukhsa-dashboard.data.gov.uk/covid-19-archive-data-download (live; "last updated May 1, 2025" SP):
- "Data presented by 'publish date' is not a reliable indicator of trends over time since this represents the date on which data was first published and may include the publication of a backlog of data or subsequent revisions to the data." ("is not a reliable indicator of trends" SV; remainder SP.)
- "Users are encouraged to use data by case and testing specimen date, death date and vaccination date to explore the historical data series more accurately." SP.
(c) How incompleteness is drawn now (What's new page 5, 8 Aug 2024, "Update", "Updated measles chart"):
- "A blue shaded section now shows the reporting delay, affecting the last 4 weeks of data collected" SV. "This replaces the dashed lines that we previously used to represent these data" SV. "The figures shown in this period are likely to underestimate the number of cases" SV.
- "The cases are now represented by markers connected by straight lines to show the data more accurately." SP.
(d) A forced change of date basis, announced in the log (8 Feb 2024, "Change to metric", "Change to COVID-19 deaths metrics"):
- "stopped publishing data on deaths with COVID-19 on the death certificate by date of death occurrence" SV. "As the data is no longer being updated, we have changed the dashboard to show deaths with COVID-19 on the death certificate by date of registration" SV.
Property: change over time, trust.
Mechanism: (1) attribute events to the date they happened, not the date reported; (2) state a fixed incompleteness window in the metric's documentation (5 days for cases); (3) mark the window on the chart (blue shading replaced dashed lines) with a sentence saying the direction of the bias; (4) keep the by-publish-date series but warn that it is not a trend series. Borrowable in full for any series with late returns.
Role: the best-documented answer to "the last point always looks like a fall".
Not found: the old dashboard's own wording on greyed recent days.

A1.5 Reach, users and measured trust
(a) "The COVID-19 dashboard: bringing together data and statistics in one place", posted by Julian Flowers, 4 Sept 2020, https://ukhsa.blog.gov.uk/2020/09/04/the-covid-19-dashboard-bringing-together-data-and-statistics-in-one-place
- "over 300,000 unique users every day, and five million hits a week" SV.
- "within 48 hours we had 17,000 responses" SV (an on-dashboard feedback survey).
- "around 10,000 people online refreshing the page" SV (at the 4pm update).
- "Users tell us they are even using the dashboard to make decisions about whether they should go on holiday to a certain area, visit a friend or get their hair cut." ("get their hair cut" SV; sentence SP.)
(b) "Behind the scenes: Expanding the COVID-19 dashboard", posted by Julian Flowers, 22 March 2021, https://ukhsa.blog.gov.uk/2021/03/22/behind-the-scenes-expanding-the-covid-19-dashboard
- "nearly 200 metrics at 4pm each day" SV; "about 40 million individual figures" SV; "a team of 18" SV; "about 19 million page views across the site" SV (stated as weekly, SP); "76.5 million hits in just 24 hours" SV.
- "Results from our most recent survey showed an outstandingly high level of user trust in the dashboard data at 90.3%, up from an already high level in November when 73.4% of users responded that they trusted the data." (73.4% and 90.3% SV; sentence quoted back in the verification pass.) No n, question wording or sampling is given; it is a self-selected on-site survey.
- Users dislike "delays, changing definitions and big corrections" SV.
- "easy-read formats" SV.
(c) OSR, "The state of the UK's statistical system 2020/21" (14 July 2021), section "4. Clear and Insightful", Case Study 6, https://osr.statisticsauthority.gov.uk/publication/the-state-of-the-uks-statistical-system-2020-21/pages/8 (regulator's report):
- "The dashboard is one of strongest examples of open data and statistics being used by a huge number of individuals" SV.
- "the team carry out in depth user research and surveys to improve and develop the dashboard" SV.
- "is widely used and an exemplar for the provision of open data across government" SV (said of the API).
(d) Award (secondary source, trade press): PublicTechnology, 19 July 2022, https://www.publictechnology.net/2022/07/19/health-and-social-care/coronavirus-dashboard-and-infection-survey-recognised-statistical-excellence/ : the dashboard won the "Statistical Excellence in Trustworthiness, Quality and Value" award SV ("Campion" appears, SV), an RSS and OSR award that "recognises organisations that have voluntarily adopted the regulator's code of practice" SP. "More than a million people used the dashboard per day at its peak, including ministers, officials and the general public." (quoted back in verification; not on a primary page.) The article quotes Stian Westlake (RSS): "when the Covid-19 dashboard was essential for the entire population" SV, and Ed Humpherson (OSR): "This is a brilliant example of how to properly engage key audiences" SV.
Property: reach, trust.
Mechanism: reach is evidenced only by self-published analytics in blog posts and by a regulator's praise; trust by an on-site survey percentage with no method. Borrowable as a habit (publish the numbers); not borrowable as evidence (no denominators).
Role: shows how thin the reach and trust evidence is even for the most-used public dashboard in the UK.

A1.6 API and downloads
- https://ukhsa-dashboard.data.gov.uk/access-our-data (live): the API is "designed to support developers and other users to easily extract and save data, that is present in the dashboard" SP; Swagger documentation; Open Government Licence v3.0 (SP).
- What's new page 6: "JSON bulk downloads added to the dashboard" (7 March 2024) and "Guidance added to Access our data" (6 March 2024), titles SP.
- Dec 2023 blog: "data download functionality through application programming interfaces (APIs) for professional users, such as academics, media, and industry" SP.
Property: provenance, reach. Mechanism: per-chart download (CSV/JSON), bulk download and public API with metric names matching the documentation. Borrowable in principle; cost depends on the stack.

A1.7 Retirement and succession
(a) "UKHSA data dashboard takes over from the Coronavirus (COVID-19) dashboard", 21 Dec 2023, https://ukhsa.blog.gov.uk/2023/12/21/ukhsa-data-dashboard-takes-over-from-the-coronavirus-covid-19-dashboard/
- the old dashboard was "for use in the height of a global pandemic" SV; "the new dashboard is designed and built for longevity" SV.
- "some of the metrics are less useful than they were during the pandemic and could be misleading" SV.
- "over 5,000 respondents" SV; sessions included "those who aren't users of the dashboard" SV. The successor ran alongside the old one from September 2023 (SP).
(b) Archive: What's new, 12 March 2024: "Following the decommissioning of the COVID-19 in the UK dashboard, you can now download all the historic data on the COVID-19 archive data download page." SP. The archive page lists a full download of "1.4 GB" SV with subsets, and states its own gaps: "Some data is missing for the period October 2020 from files presented by Lower Tier Local Authority (LTLA)." SP; "October 2020 data has been imputed using available data currently held in internal UKHSA systems" SP.
Property: change over time, trust.
Mechanism: parallel running, a dated switch-over, a stated reason, and a complete archive with a page of known defects. Note the sequence: the archive download arrived about 12 weeks after decommissioning. Borrowable.
Role: one of three documented retirements (with JHU and OWID).

A1.8 Published evaluation (GDS service assessment)
"UKHSA Winter Viruses Dashboard Alpha Assessment", published 14 Feb 2025, https://digitalhealth.blog.gov.uk/2025/02/14/ukhsa-winter-viruses-dashboard-alpha-assessment/ (peer assessment against the Service Standard; result "Met" SP; assessment date given as 29 April 2023 SP).
- Service description: "a cost-effective, sustainable and scalable solution for an enduring public dashboard" SV.
- Must explore: "whether members of public need to access population health data outside of the COVID-pandemic" SV; "understand user needs of potential service users who are not already using the coronavirus data dashboard" SP.
- On measurement: "the team has identified sensible metrics to track, although it's unclear which goals these relate to" SP; must "create a measurement framework that demonstrates how metrics map to key performance indicators (KPIs) and goals" SV.
Property: reach, trust.
Mechanism: an external panel assesses the dashboard against a public standard and publishes the gaps. The route itself is for government services; its two criticisms (research with non-users; metrics tied to goals) transfer directly.
Role: evidence that even this team was told its usage metrics did not map to goals.

====================================================================
A2. OHID FINGERTIPS
====================================================================

A2.1 RAG rule
"Technical Guide: RAG Rating Indicator Values", Public Health England, Public Health Data Science, "Version: 20 June 2017" SV. https://fingertips.phe.org.uk/documents/PHDS%20Guidance%20-%20RAG%20Ratings.pdf (the Fingertips guidance index describes it as updated January 2018). Official technical guidance, still linked.
- "where green denotes a 'favourable' value, red an 'unfavourable' value and amber a 'neutral' value" SV.
- THE RULE: "indicator values should only be given red or green RAG ratings if they are statistically significantly higher or lower than the comparator" SV.
- Three comparator types (SP): "A fixed reference value (for example, 95% target for screening coverage)"; "A reference population indicator value (for example, England life expectancy at birth)"; "A reference sample comparator (for example, comparison of mortality rates for a geography with a baseline time period, or comparison of areas with peers)".
- Fixed comparator: "RAG ratings are defined as red or green if a fixed reference value falls above the UCL or below the LCL respectively, and amber otherwise." SP.
- Overlap: "If two confidence intervals do not overlap then it is accurate to state that the indicators differ at the appropriate significance level." SP. "where confidence intervals do overlap it is does not follow that there is no evidence that the indicator values differ significantly" SV (the "it is does" is as printed).
- Independence: "Values of indicators being compared should be independent of each other." SP. "overlapping 3 or 5-year periods, where sequential time periods share two-thirds or four-fifths of the data they are derived from: these can never be compared using methods that assume independence" SP.
- Multiple comparisons: "With 95% confidence there is a 5% risk that each such indicator is misclassified" SV; "one in twenty red or green ratings could be expected even where all the underlying distributions are essentially amber" SV.
- No polarity: "the terms 'higher' and 'lower' should be used with neutral colouring such as shades of blue, from light to dark" SV.
- Extra thresholds: "Setting such criteria is essentially subjective, unless there is scientific justification" SV; a minimum threshold "should be stated clearly and the reason for it should be documented" SP.
- Colours (SP, same on two passes): red R192 G0 B0; amber R255 G192 B0; green R146 G208 B80. "the choice of red, amber and green should be checked using a tool such as Vischeck." SP.
- Page 8 checklist (SP): "1. The 'polarity' of the indicator: is higher or lower better? 2. What type of comparator is being used? 3. What is the indicator type? 4. Are all assumptions and definitions clearly stated? 5. Are all definitions and parameters appropriately documented? 6. Is the method used appropriate? (For example, is a distributional assumption or an assumption of independence valid.)"
- No sentence containing "rank", "quintile" or "league" appears in this guide (SP, non-leading extraction).
Property: trust, change over time.
Mechanism: colour means significance, not size; amber is the default; a separate blue ramp for indicators with no good direction; an explicit warning that one rating in twenty will be wrong by chance. Borrowable where the data have confidence intervals; the multiple-comparison warning is borrowable regardless.
Role: the banding rule the chapter can quote exactly.

A2.2 Confidence intervals and the Wilson method
"Public health technical guidance" (OHID; live), https://fingertips.phe.org.uk/static-reports/public-health-technical-guidance/Basic_statistics/Confidence_intervals.html and .../Basic_statistics/Proportions.html. Stated purpose (index page, SP): to "ensure that statistics published in Fingertips and other reports by the national public health intelligence function, are produced using consistent, best-practice methodology."
- "If the target or benchmark value is outside the confidence interval, it can be inferred that the difference" SV, continuing "between the estimate and the target is statistically significant at the corresponding significance level" SP.
- "While it is safe to assume that confidence intervals which do not overlap indicate a statistically significant difference" SV, "it is not always the case that overlapping confidence intervals mean that there is no significant difference" SV.
- What to do instead: "A more exact approach is to calculate the ratio of the two estimates, or the difference between them, and construct a test or confidence interval based on that statistic." SP.
- "It does not include imprecision resulting from systematic error (bias)" SV.
- "the conventional practice is to use 95% confidence" SV; "but it is not uncommon to see alternatives, such as 99.8% confidence intervals" SP.
- For complete (non-sample) data: "the imprecision arises not because of sampling variation but of 'natural' variation" SP.
- "The preferred OHID method is the Wilson Score method" SV, "(Wilson, 1927) which has been evaluated and recommended by Newcombe and Altman" SV. Reason: "it does not fail to give an interval when the numerator count and, therefore, the proportion is zero" SV; the normal approximation "does not perform well when the numerator or denominator is small" SV.
Property: trust. Mechanism: named interval method per statistic type; the benchmark is treated as exact and the test is whether it lies outside the area's interval. Borrowable (methods also in the PHEindicatormethods R package).

A2.3 The comparison methods actually coded in the tool
Fingertips API, live JSON (official, machine-readable): https://fingertips.phe.org.uk/api/comparator_methods (8 methods), /api/comparators, /api/comparator_significances?polarity_id=1, /api/recent_trends.
- Methods: "Confidence intervals overlapping reference value (95.0)" SV, described "Confidence intervals overlap point value. As used in Health Profiles." SV; "Overlapping confidence intervals (95.0)" SP, described "Overlapping confidence intervals. Using confidence intervals on data point and reference value" SV; "Confidence intervals overlapping reference value (95.0 & 99.8)" SP; "Confidence intervals overlapping reference value (99.8)" SV; "Quintiles" SV; "Quartiles (Longer Lives only)" SP; "No comparison", described "Undefined. Indicator will not be coloured." SV.
- Significance labels for a polarity-1 indicator (SP): "None", "Worse", "Similar", "Better".
- Comparators (SP): "Subnational", "Target", "England".
- Recent-trend states (SP): "Cannot be calculated", "Increasing", "Decreasing", "No significant change".
Property: trust, provenance.
Mechanism: the comparison method is a per-indicator setting exposed in the API, so a user can check which rule coloured a given cell.
Not found: a prose rule for how quintiles are cut (the FAQ page errored), and the nearest-neighbour "compared with" options, which live in the JavaScript interface.

A2.4 Recent-trend markers
https://fingertips.phe.org.uk/static-reports/public-health-technical-guidance/Presentation/Trend_markers.html (live).
- Eligibility: "There must be at least five points in the series" SV; "Time periods must be independent of one another: not overlapping, or rolling time periods" SV; "Data must be for years: monthly or quarterly data are not tested" SP; no breaks in the series (SP).
- Calculation: "These calculations are derived using the most recent five indicator values in the time series as shown on the Trends display." SP; "In the Fingertips application, N is 5" SV. Proportions use logistic regression; other types use weighted linear regression from the confidence limits (SP paraphrase).
- Threshold: "If χ² > 9.5495 the trend is significant (p < 0.2%)" SV.
- Robustness: "If a significant trend is found, the direction of the trend is noted, and the gradient (β̂) calculation is repeated five times, each time excluding one of the five points." SP. If removing any one point changes the result, "an amber, horizontal trend marker will be displayed" SP.
- Colours: "an upward arrow will be green and a downward arrow red" SV (the high-is-good case); "a blue marker is used to identify significant trends in either direction" SV.
- Caveat: "The displays are provided to help users identify quickly indicators of interest from the vast array of indicators in Fingertips, but they do not constitute a rigorous analysis of the time series." ("they do not constitute a rigorous analysis of the time series" SV.)
Property: change over time.
Mechanism: an arrow appears only when five independent annual points give a trend significant at 99.8% that survives dropping any one point; otherwise amber/flat. Borrowable as a rule for when not to draw an arrow; the regression needs intervals or numerators and denominators.
Role: the most exact "trend arrow" rule found in any sector.

A2.5 The indicator metadata template
Fingertips API CSV for one indicator: https://fingertips.phe.org.uk/api/indicator_metadata/csv/by_indicator_id?indicator_ids=90366 (live).
- Header row (SP as a whole; 12 names SV individually, one invented control "Peer reviewer name" correctly NO): "Indicator ID, Indicator, Indicator number, Rationale, Specific rationale, Definition, Data source, Indicator source, Definition of numerator, Source of numerator, Definition of denominator, Source of denominator, Methodology, Standard population/values, Frequency, Confidence interval details, Disclosure control, Rounding, Caveats, Notes, Impact of COVID-19, Copyright, Data re-use, Links, Indicator Content, Simple Name, Simple Definition, Unit, Value type, Year type, Polarity, Date updated".
- Example values (SP): Frequency "The data will be updated annually."; Polarity "RAG - High is good"; Date updated "20/04/2026". The Caveats field carries revision notes, e.g. "The data for this indicator has been revised to use the rebased population estimates for 2012 to 2020 time periods." SP.
- The RAG guide's requirement: "Metadata should define clearly the polarity of the indicator, as well as detailing the data sources and methodology." SP.
Property: provenance, trust.
Mechanism: a 32-field record per indicator, with numerator and denominator defined and sourced separately, plus plain-language "Simple Name" and "Simple Definition" beside the technical ones. No field is titled "Data quality" in the CSV (the JSON has "DataQualityNote"). Borrowable as a template.
Role: the fullest provenance template found; pairs with UKHSA's five-heading version.

A2.6 Other Fingertips guides (all SP)
- Spine charts ("Technical Guide: Spine Charts", version 20 June 2017, https://fingertips.phe.org.uk/documents/PHDS%20Guidance%20-%20Spine%20Charts.pdf): "The spine is the comparator and is usually the national or regional average to which local area values are compared."; "Most often the vertebrae show the range of values (the minimum and maximum) and the 25th and 75th percentiles."; "Spine charts only display relative differences."
- Funnel plots ("Technical Guide: Funnel Plots", 13 December 2017, .../PHDS%20Guidance%20-%20Funnel%20Plots.pdf): "even within expected random variation, 2 out of every 1,000 observations are likely to lie outside the 3 standard deviation funnel and 5 out of every 100 observations are likely to lie outside the 2 standard deviation funnel, and this should be taken into consideration when interpreting funnel plots."
- No explicit warning against ranks or league tables was found in the guides that could be read. The warnings found are against reading overlap as "no difference" and against over-reading red/green under multiple testing.

A2.7 Fingertips' own change logs and its replacement
- Geography log, https://fingertips.phe.org.uk/profile/guidance/supporting-information/geochangelog : "lists a log of the changes to areas, area grouping options and other changes around geographies" SP; entries are dated one-liners, e.g. "EPCN version from June 2025 applied" SP.
- "New Service Updates", https://fingertips.phe.org.uk/profile/guidance/supporting-information/new-service : Fingertips is being replaced by a GOV.UK service named "Find public health data" (name SV). SP: "The new service has passed the Government Digital Service alpha assessment"; "Please be reassured that until the new service launches, health statistics will still be published on Fingertips". No closure date is stated.
Property: change over time. Mechanism: a monthly public diary of a platform replacement while the old tool keeps publishing.

====================================================================
A3. PUBLIC HEALTH SCOTLAND
====================================================================
Not quickly reachable. The PHS "Toolkit" README (https://github.com/Public-Health-Scotland/Toolkit; "Templates and resources for transforming publications" SP) points to a "Chart and Dashboard Guidance Paper" at an isdscotland.org address that now returns a site-retirement notice. Nothing is quoted from the standard. The README also says "Accessibility should be a primary consideration when developing any outputs" SP. No further attempts made.

====================================================================
A4. JOHNS HOPKINS CSSE COVID-19 DASHBOARD
====================================================================

A4.1 Dong, Du & Gardner 2020: UNREACHABLE (see top). The repository README gives the requested citation: "Dong E, Du H, Gardner L. An interactive web-based dashboard to track COVID-19 in real time. Lancet Inf Dis. 20(5):533-534. doi: 10.1016/S1473-3099(20)30120-1" SP.
Substitute read: Lauren Gardner, "Mapping COVID-19", JHU CSSE blog, 23 January 2020, updated 27 April 2020, https://systems.jhu.edu/research/public-health/ncov/ (the team's own account).
- Purpose: "to provide researchers, public health authorities and the general public with a user-friendly tool" SV.
- "From January 22-31 the entire data collection and processing was managed manually" SV. "During this period the number of updates were typically conducted twice a day, both morning and night (Eastern Time)." SP.
- "on February 1, we adopted a semi-automated living data stream strategy" SV.
- Data "initially as google sheets, now in a GitHub repository" SV.
- The primary source "was initially DXY, an online platform run by members of the Chinese medical community" SP.
- The often-repeated "updated every 15 minutes" does NOT appear on this page (control returned NO). Do not attribute it without the Lancet text.

A4.2 Dong et al. 2022 "lessons learned". ABSTRACT, via https://pubmed.ncbi.nlm.nih.gov/36057267/ . Lancet Infect Dis 2022;22(12):e370-e376; doi 10.1016/S1473-3099(22)00434-0; PMCID PMC9432867. A Personal View.
- "launched the first global real-time coronavirus surveillance system" SV.
- "As of June 1, 2022, the dashboard has served the global audience for more than 30 consecutive months, totalling over 226 billion feature layer requests and 3·6 billion page views." (fragments SV)
- "The highest daily record was set on March 29, 2020, with more than 4·6 billion requests and over 69 million views" SV.
- Scope: "including data collection, data fusion logic, data curation and sharing, anomaly detection, data corrections" SV "and the human resources required to support such an effort" SV.
The pipeline, anomaly-handling and back-distribution detail in the body was not read.

A4.3 Revision and errata practice, from the repository
https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/README.md (frozen since March 2023). All SP (non-leading extraction).
- "All cases, deaths, and recoveries reported are based on the date of initial report."
- "Exceptions to this are noted in the "Data Modification" and "Retrospective reporting of (probable) cases and deaths" subsections below."
- "This section will contain any modifications to our datasets as well as the reason for the change."
- "If the error results from an issue on our collection of the data, the error will be listed in the errata.csv in the csse_covid19_time_series folder."
- "If the error results due to a change from the source, the change and reasoning will be listed below."
- Entries are dated one-liners naming place and action, e.g. "April 24 2020: New York City, NY | Back distribution of probable deaths".
- Update window: "Once per day between 04:45 and 05:15 UTC." (US daily state reports).
Property: change over time, provenance, trust.
Mechanism: two ledgers. The producer's own errors go in a machine-readable errata file; changes made by sources go in a dated prose list with the reason. The default is date of report, with listed exceptions where history was back-distributed. Borrowable: a CSV and a list.
Role: the clearest separation of "our error" from "their revision" found.

A4.4 Retirement notice
"Johns Hopkins winds down pioneering pandemic data tracking", JHU Hub, https://hub.jhu.edu/2023/02/10/coronavirus-resource-center-ending-tracking (title SV; date from the URL, 10 Feb 2023; no byline). University news release, about four weeks before the stop.
- "Since the Coronavirus Resource Center's launch, the website has been viewed more than 2.5 billion times, and users around the world have generated more than 200 billion data requests." ("more than 2.5 billion" and "200 billion" SV.)
- Why: "Starting in 2021, however, U.S. states and counties began to consistently reduce the amount of publicly reported data—a shift that led the CRC in September 2022 to discontinue hourly reporting for testing and vaccine data." SP.
- "The final update of the CRC's data will take place on March 10, 2023." SP.
- "After that date, all of the resource center's raw data will remain publicly accessible through the site's Github repositories." SP.
- The article quotes Lauren Gardner: "we have reached the appropriate time to close this chapter" SV.
- Repository banner: "On March 10, 2023, the Johns Hopkins Coronavirus Resource Center ceased its collecting and reporting of global COVID-19 data" SV; licence "This data set is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0)" SV; users are pointed to WHO and CDC (SP).
- JHU CSSE project page (https://systems.jhu.edu/research-projects/jh-csse-covid-19-dashboard/): "between 3 – 4.5 billion usage requests per day" SV, "at certain periods of the pandemic" SP.
Property: reach, change over time.
Mechanism: advance notice with a date, a reason located in the sources (upstream reporting dried up), a frozen open archive, and named successors. Borrowable.
Caution for the chapter: the reach figures differ by unit and date (2.5 billion views in the Feb 2023 release; 3·6 billion page views as of June 2022 in the paper's abstract; "requests" are map-layer calls, not people). Reach here is counted in server events.

====================================================================
A5. OUR WORLD IN DATA COVID DATASETS
====================================================================

A5.1 Hasell et al. 2020, "A cross-country database of COVID-19 testing", Scientific Data 7:345, https://www.nature.com/articles/s41597-020-00688-8 (peer-reviewed data descriptor, open access).
- Per-observation provenance: a "Source URL" field, "a URL at which the specific observation of the corresponding raw data can be found" SV; a "Notes" field, "any notes to aid the interpretation of this specific observation" SV; and a "Source label" (SP).
- A "Units" field per series, with "people tested", "tests performed", "samples tested" (SP) or "units unclear" SV.
- Verification: automated collection "is subject to initial manual verification when it is added to our database for the first time" SV; reader feedback "serves as a final, 'crowd-sourced' method of verification" SP.
- Revisions: "Abrupt positive or negative daily changes are sometimes the result of data corrections in the official data, in which case our database includes them without alteration." ("in which case our database includes them without alteration" SV.) And "revisions to the data are included on the day the revision is made, not when the revised tests occurred" SV.
- Reach: "The testing data included in the database is viewed by tens of thousands of people every day, including many health researchers, policymakers and journalists, from which we receive a large amount of feedback concerning the data." ("is viewed by tens of thousands of people every day" SV.)
- The article page's counters (566 citations, 63k accesses) are live figures, SP, not part of the paper.
Property: provenance, change over time, reach.
Mechanism: every data point carries its own source URL and note; every series carries a unit label and a prose description; upstream corrections pass through unaltered and are flagged in metadata, with a 7-day smoothed series offered to damp the artefacts. Borrowable: three extra columns in the data file.
Role: the strongest per-observation provenance practice found.

A5.2 Mathieu et al. 2021, "A global database of COVID-19 vaccinations", Nature Human Behaviour 5:947-953, https://www.nature.com/articles/s41562-021-01122-8 (peer-reviewed resource).
- "Raw data on vaccination doses administered is collected through a combination of manual and automated means" SV.
- "These are also regularly audited for accuracy against the original official sources" SV.
- Limit of the audit: "We do not audit official reports beyond technical validation (Methods)" SP.
- Reproducibility: "This provides a transparent resource for users to download the data in CSV and JSON formats, replicate the data collection and metric derivation process, and monitor any changes or additions to this process." SP.
- Reach: "The World Health Organization (WHO) relies on this dataset for its official COVID-19 dashboard" SV; "Our COVID-19 vaccination dataset is widely used by journalists, policymakers, researchers and the public" SV.
- The paper as read does not describe a per-observation source URL (no "source URL", "source_url" or "metadata" sentence was found). Do not carry the testing paper's practice over to this one on the paper's authority.
Property: provenance, reach.

A5.3 Source switch and wind-down
(a) "Our World in Data will rely on data from the WHO to track confirmed COVID-19 cases and deaths", Edouard Mathieu and Lucas Rodés-Guirao, "February 28, 2023" SV, https://ourworldindata.org/covid-jhu-who
- OWID would "replace the entire time series with WHO data" SV (closest full sentence, SP: "Our team will replace our entire time series with WHO's data on 8 March 2023").
- "The URL of all our charts and the variable names in our dataset will remain the same" SV.
- "An archive of the last version (8 March 2023) of our dataset based on data from Johns Hopkins University is available for download here" SP.
(b) "Future updates of our data on COVID-19", Saloni Dattani and Lucas Rodés-Guirao, "November 15, 2024" SV, https://ourworldindata.org/future-updates-data-covid
- "countries have reduced their reporting frequency, some metrics have become more complex to interpret, and several datasets are no longer being updated" SV.
- "Most of these datasets are no longer being updated by the data provider, so we will no longer be updating them" SV.
- The note lists which datasets continue, with check and source cadence, and which stop (SP summary: three continue, twelve stop).
(c) Repository notice, https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/README.md : "Our GitHub datasets are no longer updated since 19 August 2024" SP.
Property: change over time, trust.
Mechanism: (1) when a source dies, swap the whole series rather than splice, keep URLs and variable names stable, and publish the last old-source vintage; (2) a dated note listing, dataset by dataset, what continues at what cadence and what stops and why. Borrowable.
Role: the best "ending a live dataset" note found. It says who stopped first (the provider).

====================================================================
A6. EVALUATIONS OF COVID DASHBOARDS
====================================================================

A6.1 Ivanković D, Barbazza E, Bos V, et al. "Features Constituting Actionable COVID-19 Dashboards: Descriptive Assessment and Expert Appraisal of 158 Public Web-Based COVID-19 Dashboards", J Med Internet Res 2021;23(2):e25682, https://www.jmir.org/2021/2/e25682 (peer-reviewed, open access).
Design: descriptive assessment and expert appraisal. Scorers (the abstract's "international panel of experts (n=17)" SP) rated each dashboard on a 5-point scale from "not actionable" to "extremely actionable" (SP). "Data extraction and the first round of scoring were conducted in a 2.5-week period between July 6 and 23, 2020." SP.
- "A total of 158 dashboards from 53 countries were assessed" SV.
- "Only 20 of the 158 dashboards (12.7%) stated both their primary purpose and intended audience" SV.
- "Approximately a quarter of the dashboards (39/158, 24.7%) did not report their data sources" SV.
- "Less than half of the dashboards (63/158, 39.9%) specified metadata" SV.
- "only one-fifth of the dashboards (31/158, 19.6%) included text explaining the quality and meaning of the data" SV.
- "The dashboards predominately reported indicators over time (138/158, 87.4%)." SP.
- "In total, 20/158 dashboards (12.7%) were appraised as highly actionable" (returned as the closest sentence in the verification pass; treat as SP).
- The seven features (abstract, quoted back in verification): "Actionable COVID-19 dashboards (1) know their audience and information needs; (2) manage the type, volume, and flow of displayed information; (3) report data sources and methods clearly; (4) link time trends to policy decisions; (5) provide data that are "close to home"; (6) break down the population into relevant subgroups; and (7) use storytelling and visual cues."
- On provenance and trust: "A clear source of data and explanation of an indicator's construction, including potential limitations, was found to be an important component of trust" SV. This is the panel's judgement, not a user measurement.
- Limitation: "the appraised actionability of the dashboards ultimately does not confirm their use in practice, and evaluating this was beyond the scope of this study" SV.
ANOMALY TO FLAG: the abstract prints "color-coding was common (93/158, 89.4%)" SV, but 93/158 is 58.9%. The body gives the consistent figure: "In these 104 dashboards, color-coding was most often used (n=93, 89.4%)" SP, i.e. 93 of the 104 dashboards that used visual cues. Use 93/104.
Counts per feature: the paper gives no count of dashboards per feature; the seven were derived from the 20 highly actionable ones.
Property: provenance, trust, change over time. Mechanism: a published assessment tool plus expert scoring, repeatable as a design; it measures the page, not the reader.
Role: the baseline for how rare stated purpose (12.7%), stated sources (75.3% did) and quality text (19.6%) were.

A6.2 Barbazza E, et al. "The experiences of 33 national COVID-19 dashboard teams during the first year of the pandemic in the World Health Organization European Region: A qualitative study". Read as the medRxiv PREPRINT (https://www.medrxiv.org/content/10.1101/2021.11.23.21266747v1.full); the published version (Digital Health, 2022; PMC9434660) sits behind the PMC block and was not read.
- Design: "Semi-structured group interviews were conducted between April– June 2021" SV. "Eighty informants, representing 33 national COVID-19 dashboard teams across the WHO European Region participated" SV. "The dashboards represented 31 out of 53 WHO European Region Member States" SP.
- "Lessons emerged around the themes of simplicity, trust, partnership, software and data, and change." SP.
- "COVID-19 dashboards were developed in a learning-by-doing approach" SV.
- Open data: "More than half of the dashboards reported open data (21/33, 64%)" SP. An informant: "The prime minister [country] sees the data at the same time as the guy down the road" SV (D10).
- Errors and trust: "Teams described the inevitably of errors, given the urgency and volume of data" SP ("inevitably" as returned); teams stressed "the importance of disclosing errors as they happen" (fragment returned in two passes; SP).
- Use was not measured: "In the early stages, following the dashboard's launch, monitoring user analytics was not pursued" SP; an informant: "there wasn't time for deep analysis of user behaviour" SV (D1).
- WHO/Europe news item on the study (20 Sept 2022, https://www.who.int/europe/news/item/20-09-2022-simplicity--transparency-and-trust---essential-in-health-data-reporting) quotes an informant: "We were flying the plane as we were building it." SP.
Property: trust, reach, change over time.
Role: producers' testimony that error disclosure, not error avoidance, is what they believed built trust, and that most teams did not study their users.

A6.3 Measured public use (one dashboard)
Ismail M, Morden E, Hussey H, et al. "Evaluation of a public COVID-19 dashboard in the Western Cape, South Africa: a tool for communication, trust, and transparency", BMC Public Health 2022;22:2453, https://link.springer.com/article/10.1186/s12889-022-14657-w (peer-reviewed, open access). Read for evaluation design.
- Design: "We analysed retrospective aggregate data on viewership over time for the first year since launch of the dashboard (30 April 2020 – 29 April 2021) and conducted a cross-sectional survey targeting adult users of the dashboard at one year post the initial launch." SP.
- Measures: views; survey n = 794 SV; "a total of 2,248,456 views during its first year" (number SV).
- Finding: "Overall, 76.4% of respondents reported that the dashboard influenced their personal planning and behaviour." (76.4% SV.)
- Limits stated by the authors: "due to the nature of online recruitment the sampling approach could not avoid the potential bias of subjective selection or nonresponse bias." SP; and the timing "may confer selection bias" by "only targeting those that are still making use of the dashboard one year later" (SP).
Property: reach, trust. Mechanism: web analytics plus an on-dashboard user survey at one year. Borrowable and cheap, but it samples survivors and reports self-declared behaviour change.
Role: the most complete published "who used it and did it matter" design found, and a statement of what that design cannot show.

A6.4 Experiments on trust and on cumulative vs daily
(a) Padilla L, Hosseinpour H, Fygenson R, Howell J, Chunara R, Bertini E. "Impact of COVID-19 forecast visualizations on pandemic risk perceptions", Scientific Reports 2022;12:2014, https://www.nature.com/articles/s41598-022-05353-1 (peer-reviewed, open access).
- "we conducted two experiments online in October and December of 2020 (N = 2549) where we presented participants with 34 visualization techniques (available at the time of publication on the CDC's website) of the same COVID-19 mortality data." (2549 and "34 visualization techniques" SV.) Measured: change in perceived risk before and after viewing.
- "We found that visualizing data using a cumulative scale consistently led to participants believing that they and others were at more risk than before viewing the visualizations." SP. "In contrast, visualizing the same data with a weekly incident scale led to variable changes in risk perceptions." SP.
- Why: "Our work suggests that using a cumulative y-axis will most reliably lead to people perceiving greater pandemic risk because cumulative y-axis can show only an upward or flat trend." SP.
- "Significant increases and decreases in perceived risk can be achieved simply by changing the y-axis without any modifications to the underlying data or forecast predictions." SP.
Property: change over time. Role: experimental evidence that cumulative vs per-period is not a neutral choice.
(b) Crepaz M, Arikan G, LSE COVID-19 blog, "COVID-19 dashboards have a polarising effect on public trust", 30 June 2021, https://blogs.lse.ac.uk/covid19/2021/06/30/covid-19-dashboards-have-a-polarising-effect-on-public-trust/ (authors' summary of an article in the Journal of Elections, Public Opinion and Parties, 2021; article not read; n not stated in the blog). Survey experiment, May 2020.
- "Respondents were randomly assigned to view the high or the low information version, or view nothing (control condition)." SP.
- "information disclosure has no direct effects on willingness to trust" SV.
- "Neither the high nor the low information condition produced a statistically significant effect on the respondents' levels of political trust compared to respondents in the control group." SP.
- "Among respondents with low levels of previous trust, information disclosure had a negative effect, accounting for a 6% drop in political trust (all else being equal)." SP. (A roughly 10% rise among the already trusting was returned on first pass only; SP.)
Property: trust. Role: the one randomised test found of whether a dashboard changes trust. The outcome is trust in government, not in the display, and the average effect is nil.

A6.5 Other evaluations (all SP)
- Clarkson MD, "Web-Based COVID-19 Dashboards and Trackers in the United States: Survey Study", JMIR Hum Factors 2023;10:e43819, https://humanfactors.jmir.org/2023/1/e43819 . Despite the title this is a survey of 111 websites, not of users. Conclusion: dashboards "relied on an ad hoc pipeline of data sources and data aggregators".
- Bos VLLC, Jansen T, Klazinga NS, Kringos DS, "Development and Actionability of the Dutch COVID-19 Dashboard", JMIR Public Health Surveill 2021;7(10):e31161, https://publichealth.jmir.org/2021/10/e31161 . Method: "a descriptive checklist over time to monitor changes made to the dashboard", an actionability scoring and a reflection meeting. "Data sources were noted at all 3 points in time, and the data used in the dashboard were largely open-source. Metadata were provided in a separate document." A borrowable design: score the same dashboard at three dates.
- "Dashboard fatigue": no study with data on a dashboard was found. The nearest (ABSTRACT, https://pubmed.ncbi.nlm.nih.gov/34222832/ , Human Behavior and Emerging Technologies 2021, doi 10.1002/hbe2.260) analyses page views of one university's COVID web pages, not a dashboard: "the need for information during the pandemic decreases as time passes ... and even new emergencies such as the beginning of the second wave of COVID-19 only affect this behavioral pattern to a minor extent."

====================================================================
A7. WHO COVID-19 DASHBOARD
====================================================================
https://data.who.int/dashboards/covid19/about (official documentation, live; no last-updated date shown).
- "official weekly counts of COVID-19 cases, deaths and vaccine utilisation reported by countries, territories and areas" SV.
- "As of 25 August 2023" SV, "WHO declared that it is no longer necessary for Member States to report daily counts of cases and deaths to WHO and requested strengthening of weekly reporting" SP.
- "All counts are subject to variations in case detection, definitions, laboratory testing, vaccination strategy, and reporting strategies" SV.
- "Caution must be taken when interpreting all data presented" SV, "and differences between information products published by WHO, national public health authorities, and other sources using different inclusion criteria and different data cut-off times are to be expected" SP.
- "While steps are taken to ensure accuracy and reliability, all data are subject to continuous verification and change" SV.
- No sentence on this page contains "retrospective", "negative", "lag", "delay" or "backlog" (SP).
Property: provenance, trust.
Mechanism: a standing disclaimer that the figures are the reporters' figures, that definitions vary, and that the numbers will change. Borrowable as wording for an aggregator of other bodies' returns; it is generic, not per-country.
Role: the reported-by provenance disclaimer in its plainest form, to contrast with OWID's per-observation source URL.

====================================================================
A8. UNASKED THREADS
====================================================================
1. OSR "Regulatory guidance: Dashboards" (Office for Statistics Regulation; published 21 August 2025, last modified 15 June 2026, SP), https://osr.statisticsauthority.gov.uk/publication/regulatory-guidance-dashboards (six pages at /guidance/regulatory-guidance-dashboards/pages/1 to 6). Regulator's guidance for official-statistics producers; not on the list of already-settled sources, though another agent may also cover it.
- "A dashboard is a visual tool used to share data." SP.
- "Producers should weigh up the advantages, disadvantages and risks of using a dashboard before developing one." SP.
- "At a minimum, a dashboard should:" then nine bullets (SP as a list): "adhere to accessibility legislation and guidelines, where possible."; "contain clear, visible links to the data source and the producer of the data."; "include appropriate labelling of the statistics' status. For example, if it's an accredited official statistic, the badge should be upfront and visible."; "have clear, concise and prominent information about the strengths and limitations of the statistics. ..."; "include information about revisions and corrections."; "be coherent with any other products available as part of the statistical release, ..."; "contain accurate details of the update schedule, the date of last update and links to other sources where the data may be available in different formats, including archived data."; "come with a plan for maintaining, updating and retiring the dashboard, so that it continues to meet user needs." (this bullet SV); "contain the contact details of the relevant producer team."
- "Critical caveats and quality warnings should be prominent and upfront" SV; "we have developed a three-layered communication framework" SP.
- "Where any errors are identified, a prominent note should be added to the dashboard, ideally on the initial interface" SV.
- Revisions: "It's important to consider how revisions are communicated on a dashboard, particularly where estimates presented change status over time, for example from provisional to updated estimates." ("particularly where estimates presented change status over time" SV.)
- "Visuals and graphics should be used, where possible, to help communicate any uncertainty" SV.
- Retirement: "There should be a plan in place to archive the dashboard when it is decided that there is no longer a user need for it" SV; "Before a dashboard is archived, a prominent notice should be added that informs users when the dashboard will be archived" SV "and from which point the data on it will no longer be updated, for full transparency" SV.
- "the underlying data should be made available by other means to comply with the Code" SV; "A non-proprietary format would more likely ensure future accessibility and useability" SP.
- "Visualisations that work for the whole population may fail when the user filters down to a small subgroup" SV.
- The guidance does not ask for usage analytics: no sentence containing "analytics" or "page views" on the Value page (SP).
Bears on all four properties. This is the nearest thing to a UK standard for a public dashboard, and it includes a retirement clause.
2. The UKHSA dashboard changed how it draws the incomplete tail (dashed lines replaced by a blue shaded "reporting delay" band, with a sentence on the direction of bias) and logged the change (A1.4c).
3. Three documented retirements with different orderings: JHU gave four weeks' notice and froze an open repository; OWID named the date, kept URLs and variable names, and published the last vintage; UKHSA ran old and new in parallel for three months and published the archive about twelve weeks after switch-off, with a page of its gaps.
4. JHU's two-ledger practice (errata.csv for the producer's own errors, a dated prose list for source-side revisions) (A4.3).
5. Fingertips is itself mid-retirement: a successor called "Find public health data" is in beta, with a monthly public progress page (A2.7).
6. Padilla et al. 2022: the cumulative vs per-period choice measurably shifts perceived risk (A6.4a).
7. Arleo A, Borgo R, Kohlhammer J, Ruddle RA, Scharlach H, Yuan X, "Reflections on the Use of Dashboards in the Covid-19 Pandemic", arXiv 2503.15529, https://arxiv.org/html/2503.15529 (preprint; interviews with researchers who used dashboards; all SP): "Data provenance was a general issue - sometimes it was stated in the small print but other times not."; "Clearly document data sources and methodologies used in dashboards."
8. The GDS alpha assessment told the UKHSA team its metrics did not map to goals and that it had not researched non-users (A1.8). Reach measurement is an acknowledged gap at the top of the field.

====================================================================
WHAT I LEFT OUT, AND WHY
====================================================================
- Everything in the body of the two JHU Lancet papers (blocked). The 2022 paper's anomaly-detection and back-distribution sections are the single biggest gap; a reader with library access should pull PMC9432867.
- The retired UK COVID dashboard's own "About the data", "What's new" and developers' guide pages (no reachable archive).
- Fingertips' quintile cut rule, nearest-neighbour comparison options and FAQ wording (interface text or errored pages).
- UKHSA dashboard accessibility statement (Chapter 13 territory) and the Swagger API detail.
- PHS standards (unreachable). Sorapure 2023, "User Perceptions of Actionability in Data Dashboards" (SAGE, likely blocked; not attempted). "Best Practices for the Design of COVID-19 Dashboards" (PMC, blocked).
- Trust surveys about government or health agencies in general (not about displays).

RICH REFERENCES (up to three)
1. OHID Public health technical guidance plus the PHE RAG guide: https://fingertips.phe.org.uk/static-reports/public-health-technical-guidance/index.html and https://fingertips.phe.org.uk/documents/PHDS%20Guidance%20-%20RAG%20Ratings.pdf . Exact, printed rules for colour, comparison and trend arrows, with their own warnings.
2. UKHSA data dashboard "What's new" plus "Compliance": https://ukhsa-dashboard.data.gov.uk/whats-new and https://ukhsa-dashboard.data.gov.uk/compliance . A live change log with issue/resolved pairs and a public statement of what the dashboard is not.
3. OSR Regulatory guidance: Dashboards (Aug 2025): https://osr.statisticsauthority.gov.uk/publication/regulatory-guidance-dashboards . The minimum list and the archive-notice rule.
(Runner-up for provenance: Hasell et al. 2020, per-observation Source URL and Notes fields.)

WHAT SURPRISED ME
- The trust evidence for the UK COVID dashboard is one sentence in a blog (73.4% rising to 90.3%) from a self-selected on-site survey with no n or question wording. The only randomised test found (Ireland) reported no average effect on trust and a split by prior trust.
- The most-cited evaluation's abstract carries an arithmetic slip (93/158 printed as 89.4%).
- Fingertips will not draw a trend arrow unless five independent annual points pass a 99.8% test and survive leave-one-out, and it still labels the result as not a rigorous analysis. No COVID dashboard documentation read here sets a comparable bar for its "up/down versus last week" figures.
- The RAG guide says in print that one red or green in twenty is expected by chance.
- The widely repeated "every 15 minutes" JHU update claim is absent from the team's own blog account; it could not be checked against the Lancet text.
- UKHSA's compliance page lists, as things it cannot do, pre-announcing via a release calendar, while committing in the next breath to 4pm every Thursday.
- Reach figures for JHU are quoted in at least three incompatible units.


---

## Agent B

AGENT B — FINANCE, RISK AND THE ECONOMICS OF CHANGE OVER TIME
All fetches 6 October 2026. WebSearch calls used: 16 of 30. Method only; no finding about any place.
Key: [SV] = string-verified by a second presence pass (false control strings were included in most checks and were all rejected). [SP] = single pass. [ABS] = abstract only.

Could not read (and why):
- pnas.org (403), pmc.ncbi.nlm.nih.gov (captcha), onlinelibrary.wiley.com (403), sciencedirect.com (robots). Reached instead via the Europe PMC full-text XML, RePEc and the Cleveland Fed.
- A Europe PMC search URL and doi.org/10.26509/frbc-wp-202128 were refused by the fetch proxy (HTTP 429, rate limited); not retried.
- The Bank of England's published response to the Bernanke review (robots disallowed). Nothing quoted from it.
- The Bank's 2026 Monetary Policy Report pages returned only a cookie/"to be published" stub, so the 2026 state of the fan charts is unverified.
- The EBA Risk Dashboard's methodological annex on the heatmap did not come through the reader.

==========
B1. CENTRAL-BANK COMMUNICATION TO THE PUBLIC, MEASURED

(a) Haldane & McMahon 2018, "Central Bank Communications and the General Public", AEA Papers and Proceedings 108: 578–83, May 2018. Peer-reviewed (P&P). https://www.aeaweb.org/articles?id=10.1257/pandp.20181082 ; text from the authors' final manuscript at mcmahonecon.com/wp-content/uploads/2018/01/HaldaneMcMahon_FinalManuscript-1.pdf
- Abstract: "it is unclear the general public have benefitted from these enhanced central bank communications" [SV]; "examines observational and experimental evidence following the recently adopted use of a layered communication at the Bank of England" [SV]; "there are compelling reasons for central banks to continue trying to target communication at the public" [SV].
- Design: "First, a survey of 285 members of the UK general public, recruited by a third-party company ("Public sample")." [SV]. Second sample: first-year Oxford economics graduate students; n = 68 appears only in the paper's Table 2 [SP]. Random assignment to the traditional Monetary Policy Summary or the new layered content [SP]. Three outcomes: comprehension, movement of expectations toward the Bank's forecast, perception of the institution [SP].
- Findings: "First, the results confirm that the new layered content is easier to read and understand, even for technically-advanced MPhil students." [SV]. "Second, those that read the new layered content tended to develop an improved perception of the institution. While this is not statistically significant in the public survey, it is highly significant in the MPhil sample." [returned identically on two passes]. Comprehension effect +0.71 points against +0.55 for having studied economics [SP].
- Reading level: "This layered content had a Flesch-Kincaid Grade Level of 7.8 (eighth grade level), which compares with the Monetary Policy Summary which had a Flesch-Kincaid Grade Level of 13.4." [two passes].
- Reach: "Website activity over the course of the 24 hours after the announcement increase markedly in November 2017, almost doubling compared with earlier IRs." [two passes]. "One clear finding is that monetary policy news itself, rather than the means by which it is communicated, is the largest single factor determining the reach of Twitter activity." [SV]. Note this sentence is about Twitter reach specifically; the first pass had truncated it.
- Agents' business survey: "More than 70% of respondents felt the new layered summary helped them to better understand the IR's messages." [SV]; the authors caution about self-selection and no direct comparison with the old report [SP].
- Bears on: reach, trust. Mechanism: layered publication plus a randomised reading test with a three-part outcome. Borrowable: yes, the evaluation design is small and cheap; note the trust effect was not significant in the public sample.
- Role: the founding measured case; the honest finding is that comprehension moved and public trust did not, and that news, not format, drove reach.

(b) Bholat, Broughton, Parker, Ter Meer & Walczak, Bank of England Staff Working Paper No. 750, published 15 August 2018 under the title "Enhancing central bank communications with behavioural insights". CORRECTION TO THE BRIEF: SWP 750 is 2018 and has five authors; the 2019 item with four authors (no Parker) and the "simple and relatable information" title is the Journal of Monetary Economics version, vol. 108, pp. 1–15.
https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2018/enhancing-central-bank-communications-with-behavioural-insights.pdf
- n: "A total of 2,275 respondents completed the entire experiment." [SV]. Online, Predictiv panel, sample built to match UK gender, age, region and income [SP]. "The experiment was conducted in April and May 2018." [SP].
- Four arms: Monetary Policy Summary of the February 2018 Inflation Report (control); the published Visual Summary; a Reduced Text version with half the words; a Relatable Summary [SP].
- Measures: five comprehension questions [SP]; trust on a scale where "0 means 'distrust completely' and 10 means 'trust completely.'" [SV]; perception of the Bank on a 1–5 scale, "Worsened Significantly (1) to Improved Significantly (5)" [SP].
- Comprehension: "compared to the Monetary Policy Summary, the Visual Summary improved the average comprehension score by 25% (0.5 points)" [SV]. Reduced Text "improved the average comprehension score by 30% (0.6 points)" [SV]. "the Relatable Summary improved direct comprehension scores by 42% (0.8 points) relative to the Monetary Policy Summary" [SV]. "This is equivalent to answering, on average, 2.85 out of 5 questions correctly in the Relatable Summary condition, compared to 2.02 on average in the Monetary Policy Summary condition." [SP]. "The Reduced Text Summary increased comprehension by a small amount, but not in a statistically significantly way compared to the current Visual Summary." [SP].
- Trust: "We found a small but statistically significant difference in trust for participants that read the Relatable Summary" [SV]; "There were no other statistically significant differences across treatments." [SV]. Perceptions of the Bank "on average 0.28 points higher" for the Relatable arm than control [two passes].
- Stated limits: "Respondents in the experiment received financial compensation in exchange for participating, whereas visitors to the Bank's website in reality do not receive remuneration." [SP].
- JME abstract (via RePEc): "the simplification of language increases public comprehension more than the inclusion of visuals" [SV, ABS].
- Bears on: trust, reach. Mechanism: four-arm randomised test separating visuals, word count and relatability, with comprehension and trust measured separately. Borrowable: yes, as a design.
- Role: the best evidence in the sector that simpler words beat pictures, and that even the best arm left people at under 3 of 5 questions correct.

(c) Why the Bank layers. Haldane, "Climbing the Public Engagement Ladder", speech, 6 March 2018 (Bank of England PDF).
- "My 'stylised fact' (itself a piece of technical jargon) is that around 95% of all the words central banks utter are inaccessible to around 95% of the population." [SV]. This is a self-described stylised fact, not a measurement.
- "a one-sentence, one-graphic version for the time-poor; a 60-page chart-tastic technical text for the masochist." [SV].
- "The number of website hits has increased markedly since publication of our first layered Inflation Report in November last year." [SV]. No figure is given.

(d) Later work.
- Haldane, Macaulay & McMahon, "The 3 E's of central bank communication with the public", Staff Working Paper No. 847, January 2020: "Explanation, Engagement and Education" [SV]; "The majority of people presumably do not even attempt to engage with the material in, for example, an Inflation Report" [SV]. The reader found no new experiment or reach figures in it [SP]; it is a model plus a survey of evidence, not an evaluation of the visual summary.
- McMahon & Naylor, "Getting through: communicating complex information", Staff Working Paper No. 1,047, 20 October 2023 (page says updated May 2026): "conceptual complexity matters more for getting through, even for economics‑trained individuals" [SV, ABS]; "recent central bank efforts to simplify language reduced traditional syntactic measures, but conceptual complexity has actually increased" [SV for the last clause, ABS]. n not given on the landing page.
- Current layering: the Bank's Quarterly Bulletin article of 17 October 2025 says "A new Monetary Policy Overview will set out how the analytical inputs have informed the MPC's collective policy decision." [SP]. The reader found no "in brief" or visual-summary layer in the November 2025 report [SP; absence not confirmed].
- I found no Bank evaluation of the visual summary later than (a) and (b).

==========
B2. THE FAN CHART

(a) The Bank's own description. Britton, Fisher & Whitley, "The Inflation Report projections: understanding the fan chart", Bank of England Quarterly Bulletin, 1998 Q1 (dated 1 March 1998). Official documentation; historical.
https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/1998/the-inflation-report-projections-understanding-the-fan-chart.pdf
- "The fan chart was chosen to meet the criterion that it should give information on the whole of the forecast distribution, without claiming a spuriously high degree of precision." [same sentence returned on two passes].
- The band rule: "…until there is 10% of the distribution in a single central band, with these two points marking the outside edges." [SV]. "That band is coloured the deepest shade of red" [SV]. "Each pair of bands covers 10% of the distribution but, if the risks are unbalanced, the same colour bands are not of equal width (representing unequal probability intervals)." [SV first clause]. "Pairs of bands continue to be added until 90% of the distribution is covered" [SV]. "There is an equal number of red bands on either side of the central band (eight)." [SV]. "The distribution is truncated, so that there is an implicit ninth and final pair of bands, occupying the white space outside the 90% covered." [two passes].
- "The central projection is, by construction, always in the deepest red band since it is associated with the mode." [SP]. "It was hoped that this would promote discussion of the risks to the economic outlook, rather than on small changes to the central projection." [SP].
- The page summary says the fan chart was introduced in February 1996, replacing a 1993–96 shaded band built from average absolute forecast errors [reader's paraphrase, not a quotation].

(b) The convention has changed. Monetary Policy Report, November 2025, footnote to Chart 3.1 (https://www.bankofengland.co.uk/monetary-policy-report/2025/november-2025):
- "The fan charts are constructed so that outturns are expected to lie within each pair of lighter areas on 30 occasions, with outturns expected to lie within the fan on 90 out of 100 occasions." [two passes; second clause SV].
- "…calibrated to match the historical forecast errors since 2004 and now up to 2025 Q2 for each variable at different horizons but exclude errors during the pandemic given its exceptional nature." [SV last clause].
- "The Committee no longer uses the calibration of the fan chart skew to reflect judgements on the balance of risks to the central projection." [SV].
- "For GDP growth, the distribution reflects uncertainty around past data revisions and future evolution, so that the mature estimate would lie within the darkest central band on only 30 out of 100 occasions." [SV].
So the 1998 rule was a 10% central band and eight 10% pairs; the 2025 rule is a 30% central band and 30% pairs. Both total 90%. The brief's "darkest band… 10%" is the 1998 convention only.

(c) The Bernanke review, 12 April 2024 (Bank of England Independent Evaluation Office).
- Recommendation 11: "Despite their distinguished history, the fan charts as published in the MPR have weak conceptual foundations, convey little useful information over and above what could be communicated in other, more direct ways, and receive little attention from the public." [SV in three fragments]. "They should be eliminated." [SV]. "However, it remains important to communicate the degree of forecast uncertainty and the balance of risks." [SP]. "A section in the MPR should be devoted to uncertainty and the balance of risks in the forecast" [SV].
- Box 1: "The empirical basis for the fan charts, in the first instance, is the historical record of the Bank's forecast errors (since 2004, with 2020 errors downweighted) for each variable." [SV parenthesis]. "A wider fan chart corresponds to a history of larger forecast errors on average…" [SV]. "A band corresponding to the full width of the fan chart is expected to include the realised path of the forecasted variable 90 out of 100 times." [SP]. "Technically, the MPC adds skew to the distribution of outcomes represented by the fan." [SP].
- The review asserts "little attention from the public" without citing a survey; a non-leading pass listing all twenty "fan chart" sentences found no evidence sentence behind it.

(d) What the Bank did. Quarterly Bulletin, "Monetary policymaking at the Bank of England in uncertain times", 17 October 2025:
- "For now, we will continue to provide fan charts, based on historical forecast errors" [SV]. "MPC judgements about the balance of risks will be communicated through qualitative statements, rather than judgemental adjustments to the fan charts" [SV].
So the charts were kept and the judgemental skew removed. Press headlines of April 2024 said "scraps"; the November 2025 report still printed them.

(e) Do readers understand fan charts?
- McMahon, Naylor, Rholes & Rickards, "Anchors aweigh? The effect of communicating forecast uncertainty", Bank of England Staff Working Paper No. 1,196, July 2026 (page dated 17 July 2026). Working paper, not yet peer reviewed. Part I: "Our first sample consists of 300 individuals representative of the UK general public, recruited via the Prolific online survey platform" [SV]; "Our second sample comprises 75 experts" [SV]. Formats: point forecast, fan chart with 70% and 90% bands, range, box-and-whisker, dot plot, speedometer [SP]. "We find that fan charts are well understood and perform best at jointly conveying both expectations and uncertainty" [SV]. Part II: "1,600 UK participants across four stages" [ABS, two passes]; fan charts act "as an 'insurance policy' that helps protect central bank reputation" [SV]; "the public consistently underestimates the degree of uncertainty" [SV]. It names its motive: the review "recommended discontinuing fan charts while emphasising the continued importance of communicating forecast uncertainty" [SV]. Limits: stylised, model-generated worlds; online panel [SP].
- Tak, Toet & van Erp 2014, IEEE TVCG 20(6): 935–943 [ABS]: "Participants (n = 140) rated the probability…" [SV]; "We conclude that perceived certainty is affected by its visual representation." [SV]; "the internal model relates to participants' numeracy" [SV]. Seven band-type visualisations, non-experts; not the Bank's chart.
- I found no Bank user research on the fan chart before 2026.

(f) The OBR's method.
- Briefing Paper No. 4, "How we present uncertainty", June 2012: "The chances of any economic or fiscal forecast being accurate in every dimension are infinitesimally small" [SV]. "…with successive pairs of lighter shaded areas around it representing 10 per cent probability bands" [SV]. "The final fan charts do not represent our assessment of specific risks to the central forecast" [SV]. "Neither can they fully capture the extreme range of potential outcomes" [SV].
- Box, Economic and fiscal outlook October 2021, "Using stochastic simulations to produce fan charts": "generating a very large number (thousands) of scenarios" [SV]; "Each of the four bands on each side of the median represents 10 percentage points within the overall probability distribution" [SV], "implying an 80 per cent chance that debt will be within the fan in each year" [SV].
- Box 2.1, Forecast evaluation report October 2024: "The probability bands are narrow in the first year of our forecasts because, historically, differences between forecast and outturn in the first forecast year were typically small" [SV]; "Instead, they show the outcomes that someone might anticipate if they believed that forecast errors in the past 20 years offered a reasonable guide to future forecast errors." [SP].

(g) Context: BIS Quarterly Review, 16 March 2026 (Bell, Chavaz, Hofmann, Rees, Rottner): "Fan charts are the most common tool, published by almost 75% of the 25 central banks in our sample in 2025" [SV]; "If too wide, fan charts risk diluting the central bank's messages about the outlook and raising questions about its forecasting ability" [SV]. The BIS dates the fan chart to 1993 [SP], which conflicts with the Bank's own 1996.

- Bears on: change over time, uncertainty, trust. Mechanism: a printed band rule in the chart footnote (what share of outcomes each shade should contain, what data calibrate it, what is excluded). Borrowable: the footnote convention yes; the chart itself needs a forecast-error history most projects lack.
- Role: the sector's best-documented uncertainty display, the only one with a published recommendation to abolish it, and now a randomised test in its favour.

==========
B3. RISK DASHBOARDS FOR REGULATORS

(a) ESRB Risk Dashboard. Official; live; Issue 56, published 2 July 2026. https://www.esrb.europa.eu/pub/rd/html/index.en.html
- "The ESRB risk dashboard is a set of quantitative and qualitative indicators of systemic risk in the EU financial system" [SV]. "It is published quarterly, one week after its adoption by the General Board" [SV], with two annexes on methodology and indicators. "The risk dashboard should not be considered to be a policy statement on systemic risks" [SV].
- In the dashboard PDF: "The risk dashboard is a set of quantitative indicators and not an early-warning system" [SV]. "Users may not rely on the indicators as a basis for any mechanical form of inference" [SV]. "Data available to the ECB by Friday, 12 June 2026 were taken into account" [SV].
- Indicator set: eight sections (interlinkages and composite measures; macro risk; credit risk; funding and liquidity; market risk; profitability and solvency; structural risk; central counterparties), the same list in the dashboard and Annex I [two documents, SP each]. Counts of charts varied between passes (about 70 to 89); do not print a number.
- Colours: none. Two passes found no heat map, no colour rule and no ranking; the only "threshold" sentences in Annex I are reference lines, e.g. "The line represents the 60% Stability and Growth Pact threshold for the government debt-to-GDP ratio." [SP]. The brief's "what the colours mean" has no answer because the ESRB does not colour.
- Mechanism: a stated data cut-off date, a per-indicator methodology annex and a two-sentence disclaimer of what the display is not. Borrowable: all three.

(b) EBA Risk Dashboard (Q4 2024 and Q4 2023 PDFs). Official; live quarterly. The one regulator display here with a printed traffic-light rule.
- "Traffic lights provide the trend of the RI risk indicator given the historical time series" [SV]. Data bar colour scale: "green for the "best bucket", yellow for the intermediate and red for the "worst bucket"" [SV]. The heatmap shows the share of banks' assets in each bucket over time [SP]; it does not rank [control string rejected].
- Thresholds: these strings are present in the document [SV]: "> 14%", "[11% - 14%]", "[12% - 15%]", "[5% - 8%]", "[3% - 8%]", "[40% - 55%]", "[1.5% - 4%]", "[6% - 10%]", "[50% - 60%]", "[100% - 150%]", "[110% - 140%]". WARNING: the reader misaligned rows and thresholds across three passes. Only two rows came back the same twice: NPL ratio < 3%, [3% - 8%], > 8%; return on equity > 10%, [6% - 10%], < 6%. The other row assignments must be read off the PDF by eye before printing.
- Borrowable: fixed, printed absolute thresholds per indicator, with colour applied to shares rather than to named institutions.

(c) Federal Reserve heat map. Aikman, Kiley, Lee, Palumbo & Warusawitharana, FEDS Notes, 5 August 2015. Staff research.
- "We first standardize the raw data by subtracting from each series its average value or its trend (10-year moving average) then dividing by its time-series standard deviation." [SV]. "In total, we assemble a set of 44 indicators (the purple boxes), which we group into 14 component sources of vulnerability" [SV]. Colour: values near zero "will appear "cool," (represented by deep blue); conversely, values near 1 will appear very "hot" (dark red), indicating acute vulnerabilities." [SP on a verification pass].
- Caveat: "…the arrival of additional data can change the standardized and rescaled values for the entire time series. This implies that the current measures of the vulnerabilities over history can differ from their "real time" counterparts constructed using only the data available as of a given date in the past." [SP on a verification pass].
- Mechanism: colour as a percentile of the series' own history. Borrowable with its stated cost: old cells recolour when new data arrive.

(d) ECB. The May 2026 Financial Stability Review has no heat map or colour-coded risk table, by the reader's account [SP]. The December 2011 special feature "Mapping the State of Financial Stability" says "Cold colours represent low values of the indicator and warm colours represent high values, as defined by the colour scale below each feature plane." [SP] and warns that euro-area aggregates "did not reflect the crisis in certain euro area countries" [SP].

(e) Bank of England. FPC policy statement on the countercyclical capital buffer, 12 July 2023: "The decisions are not mechanically tied to any level or rate of change for an individual or specific combination of indicators; rather, the FPC makes a comprehensive, qualitative assessment informed by the indicators." [SV]. The CCyB rate and "the core indicators that support its decisions, are published on the Bank of England's website each quarter" [SP]. A table of numbers, no colour.

- Bears on: change over time, trust. Role: the regulators mostly do not colour or rank, and each prints a sentence saying the display is not a verdict.

==========
B4. VINTAGES AND REVISIONS

(a) ALFRED, Federal Reserve Bank of St. Louis. Official; live.
- "ALFRED, ArchivaL Federal Reserve Economic Data, is a collection of vintage versions of U.S. economic data" [SV]. "ALFRED makes it possible to gather data as reported by a source on past dates in history" [SV]. Purpose: to "reproduce past research, build more accurate forecasting models, and analyze economic policy decisions of the past with data that were available at the time" [SV]. "In general, economic data for past observation periods are revised as more accurate estimates become available. As a result, previous vintages of data can be superseded and may no longer be available from various data sources." [SP].
- Homepage: "ALFRED® allows you to retrieve each economic data release (vintage) that was available on a specific date in history." [SV]; "Economic data time travel since 2006." [SV]; "Over 350,000 real-time economic time series" [SP, from the page's meta description].
- Bears on: provenance, change over time. Mechanism: every release kept and addressable by date. Borrowable in principle; it only needs each published file kept and dated.

(b) Croushore & Stark 2001, "A real-time data set for macroeconomists", Journal of Econometrics 105(1): 111–130. Peer-reviewed. Abstract via RePEc; text from the Philadelphia Fed working paper 99-4 (June 1999).
- "The data set consists of vintages, or snapshots, of the major macroeconomic data available at quarterly intervals in real time." [ABS, SP].
- "We refer to each data set corresponding to the information set at a particular date as a 'vintage' and to the collection of such vintages as a 'real-time data set.'" [SP].
- "In many cases, however, the data that should be used in these studies are not the (final, revised) data available from government statistical agencies today, but rather the original, unrevised data available to economic agents who were around at the time." [SV].
- "However, when we rerun the test on the same sample period (1948Q1 to 1977Q1) using vintage data from the first quarter of 1998, the coefficients change dramatically, and the F-test now rejects the hypothesis that the second-through-fourth lagged consumption terms are jointly zero." [SV first part].
- Balance: "it is somewhat reassuring that for many of the studies we examine, the results are generally robust, at least qualitatively, for different vintages of the data." [SP]. Vintages run quarterly from November 1965; the reader counted 15 variables [SP].

(c) ONS.
- National Accounts Revisions Policy: updated January 2026 (page dated 31 March 2026). "A revision is a scheduled change to any published Office for National Statistics (ONS) output" and "A correction is an unplanned revision to any published ONS output because of the identification of an error." [SP]. "Changes as a result of a correction will be clearly labelled as a correction rather than a revision" [SV]. "The scope of future planned revisions is regularly announced in advance of the annual reassessment of data" [SV]. "Revisions triangles supporting this information are also published on the ONS website, to allow users to analyse past revisions for themselves." [SP].
- Size, as the ONS states it. GDP first quarterly estimate, UK: April to June 2026 (13 August 2026), section 2: "Early estimates of GDP are subject to revision (positive or negative)" [SV]. "…since Quarter 1 2000 there is a mean revision of positive 0.08 percentage points between the first estimate and the final estimate, which is published three years later" [SV]. "The mean absolute revision between the first and final estimates is 0.27 percentage points" [SV].
- GDP QMI (last revised 8 April 2022): "revisions are typically small (around 0.1 to 0.2 percentage points), with the frequency of upward and downward revisions broadly equal" [SV]; "Revisions are an inevitable consequence of the trade-off between timeliness and accuracy" [SV]; "we have around 80% data content for the output measure, 60% data content for the expenditure measure and 40% data content for the income measure." [SP on verification pass].
- Revisions triangles dataset page: "Comparison of gross domestic product (GDP) first estimates against estimates published later." [SP]. The page showed a next-release date of 11 September 2026, already past on the fetch date; treat its dates as stale.
- Mechanism: a sentence in the headline section giving the mean and mean absolute revision since a stated date. Borrowable once a series has enough releases.

(d) Pre-release access.
- ONS: "As of 1 July 2017, pre-release access to Office for National Statistics (ONS) statistics was removed in all but exceptional circumstances" [SV]. "Equality of access to official statistics is a fundamental principle of statistical good practice" [SV]. "In March 2020 ONS moved the publication of its market-sensitive economic releases to 7:00am and this practice ended." [SP; refers to the lock-in briefing of news agencies].
- Other producers remain under the Pre-release Access to Official Statistics Order 2008 (SI 2008/2998, in force 1 December 2008) and devolved equivalents. Schedule para 4: "the person responsible may not grant pre-release access for a period in excess of 24 hours prior to the time set for the publication" [SV middle fragment]. Para 3(1)(d): "restrict pre-release access to the minimum number of persons" [SV]. Para 5(1)(a) allows longer only if "the public benefit likely to result from such access significantly outweighs the detriment to public trust in official statistics" [SP]. Para 9(b): publish "a list of the job title and organisation of persons to whom the person responsible has granted pre-release access to that statistic" [SP].
- The UKSA page listing the Orders (reader gives its date as 30 October 2025) says the Authority treats them as part of the Code [SP] and carries no statement on removal.

(e) IMF SDDS. SDDS Guide 2013 (imf.org/external/pubs/ft/sdds/guide/2013/sddsguide13.pdf):
- "the ARC provides release dates for the current month and at least the following three months" [SV]. "the SDDS prescribes (1) dissemination of advance release calendars (ARCs) and (2) simultaneous release to all interested parties." [SV second item]. Integrity: "the identification of internal government access to data before release to the public" [SV; one pass gave the Box 1.1 wording as "identify internal government access…"]. "provide information about revision and advance notice of major changes in methodology" [SP].
- IMF factsheet, 19 April 2023: "The SDDS was established in 1996…" and "The SDDS Plus is the highest tier of the IMF Data Standards Initiatives. It was established in 2012 to address data gaps identified during the global financial crisis." [SP].
- Mechanism: a calendar of at least a quarter ahead, same-moment release, and a published list of who sees figures early. All three borrowable.

==========
B5. ECONOMIC STATISTICS AND PUBLIC TRUST

(a) van der Bles, van der Linden, Freeman & Spiegelhalter 2020, PNAS, "The effects of communicating uncertainty on public trust in facts and numbers". Peer-reviewed. Read via Europe PMC full text (PMC7149229).
- Five experiments, "total n = 5,780" [SV]: 1,122, 877 and 1,200 on Prolific; 1,050 UK adults via Qualtrics Panels; BBC News field experiment n = 1,531 [SP each; they sum to 5,780].
- "we observed only a small decrease in trust in numbers and trustworthiness of the source, and mostly for verbal uncertainty communication" [SV].
- BBC field experiment (labour-market article, 15 October 2019): control; "… rose to an estimated 3.9%"; "… rose to an estimated 3.9% (between 3.7% and 4.1%)" [SP]. "Uncertainty communication, however, did not affect participants' trust in the number" [SV].
- "we therefore recommend that the communication of uncertainty around basic facts and numbers in the media is best conveyed through numerical ranges with a point estimate" [SV].
- Effect sizes reported by the reader, d = −0.55 verbal and −0.15 numeric [SP; check before printing].

(b) Galvão & Mitchell, "Communicating Data Uncertainty: Multi-Wave Experimental Evidence for U.K. GDP", ESCoE DP 2021-06 (23 June 2021); Cleveland Fed WP 21-28 (22 December 2021); later Journal of Money, Credit and Banking 2024 (not reachable).
- "Economic statistics are commonly published without any explicit indication of their uncertainty" [SV]. "we conduct two waves of a randomized controlled online experiment" [SV]. "It encourages the public not to take estimates at face-value, but does not decrease trust in the data" [SV]. "notably intervals, density strips and bell curves" [SV].
- n: wave one, 2018, "randomly sampled more than 3,000 (nationally representative) adults in the UK" [two passes]; wave two, 2020, "randomly sampled more than 4,000 adults" [SV]. Dynata quota sample [SP].
- Trust item: "Personally, how much trust do you have in economic statistics produced by the Office for National Statistics (ONS)?" on a 4-point scale, "Trust them greatly = 4" [SV fragment].
- "…improves the public's understanding of data uncertainty, but does not reduce its trust in the statistical office." [SV]. "The textual uncertainty qualifier given to Group 2 tends to have little effect." [SP].
- Role: the direct test for official economic figures; words like "estimated" did little, intervals did the work, and trust did not fall.

(c) Runge, ESCoE DP 2021-07 (23 June 2021): "20 online, semi-structured interviews with the UK public" [SP]; people confused measurement uncertainty with forecast uncertainty [SP paraphrase].

(d) Runge & Hudson-Sharp, "Public Understanding of Economics and Economic Statistics", ESCoE OP-03, 25 November 2020: "12 focus groups with 130 participants and a nationally representative survey with 1,665 respondents" [ABS, SP]. The landing page gives no finding on how people read charts. I found no ESCoE or Bank study of how the public reads economic charts as such.

(e) OSR, "Revisions of estimates of UK Gross Domestic Product (GDP)", 29 November 2023: "the uncertainty surrounding these statistics is in itself a key message" [SV]; "We consider that ONS has been clear in its communications in 2023 that revisions are normal and that in less-volatile times, revisions are small." [SV]; cites ESCoE that communicating uncertainty "improved the public's understanding of data uncertainty, without reducing its trust in the statistical office." [SV; the OSR quoting ESCoE].

(f) OSR, "Approaches to presenting uncertainty in the statistical system", 21 September 2022: "We found that uncertainty is typically better depicted and described in statistical bulletins and methodological documents than it is in data tables, data dashboards and downloadable datasets." [SV]. This is the regulator naming dashboards as a weak point.

==========
B6. WHAT FINANCE GETS WRONG

- Cox 2008, "What's Wrong with Risk Matrices?", Risk Analysis 28(2): 497–512 [ABS via RePEc]: "Typical risk matrices can correctly and unambiguously compare only a small fraction (e.g., less than 10%) of randomly selected pairs of hazards." [SV]. "For risks with negatively correlated frequencies and severities, they can be 'worse than useless,' leading to worse‐than‐random decisions." [SP]. "…different users may obtain opposite ratings of the same quantitative risks." [SP]. They "should be used with caution, and only with careful explanations of embedded judgments" [SV]. A mathematical argument, not an experiment.
- Bernanke on the fan chart (B2c): "weak conceptual foundations", asserted without cited reader evidence, and now contradicted on comprehension by the Bank's own 2026 experiment.
- The Fed heat map's own caveat (B3c): history recolours when data arrive.
- The ECB 2011 caveat (B3d): an aggregate can hide its parts.
- The OSR on small movements (2023): describing GDP as "estimated" without context may let "seemingly small changes – 0.1%, 0.2% etc" be over-read [SP].
- McMahon & Naylor (B1d): simpler sentences were achieved while conceptual complexity rose.
- Taleb: nothing documented and specific found; omitted.

==========
B7. UNASKED THREADS

1. Typographic labels. Eurostat, "Flags and special value used in Eurostat's online database": "Flags are codes added to the data and defining a specific characteristic:" [SP]; "b = break in time series" [SV], "e = estimated", "f = forecast", "p = provisional", "u = low reliability" [SV each], also c, d, n, r, s, z [SP]; ": = not available" [SP]. UK Government Analysis Function, "Using symbols and shorthand" (11 January 2022): "[p] = provisional", "[r] = revised", "[f] = forecast" [SV]; "Whenever you use a shorthand marker in a table it should be in square brackets, for example: '[r]'." [SV]; "We do not recommend using symbols such as '. :', '*' or '†' anymore because they can be difficult to see and screen reader software can find them hard to recognise." [SP]. The UK standard has moved away from the bare "p" and "r" the brief mentions.
2. Revision versus correction as two labelled things (ONS policy, B4c).
3. A fan drawn backwards over past data: the Bank's GDP fan covers "uncertainty around past data revisions" (B2b).
4. The statutory test for early access is framed as trust: "detriment to public trust in official statistics" (B4d).
5. Measured trust baseline. Public Confidence in Official Statistics 2023 (NatCen for the UKSA, published 14 May 2024): "a representative sample of 2,364 adults aged 18 and over in Britain from 1,695 households…Fieldwork took place between 4th October and 17th December 2023." [SP]. "87% of respondents said that they tend to trust it or trust it a great deal." [SV figure]. "Most also indicated that they agree that statistics produced by ONS are free from political interference (72%)." [SV figure]. Government presents official statistics honestly: "32%, compared to 35% in 2021" [SV figure]. 35% reported having used ONS statistics [SP]. Nothing in it on pre-release or calendars.
6. Reach is driven by the news, not the format (Haldane & McMahon's Twitter finding, B1a).
7. A stated data cut-off date on the face of the display (ESRB, B3a).
8. Fan-chart prominence falling without abolition: the BIS notes Norway "presents its main economic forecasts at the beginning of its monetary policy report as point forecasts and shows fan charts towards the end of the report" [SP].

==========
LEFT OUT AND WHY
- The Bank's formal response to Bernanke (blocked) and the 2026 reports (stub pages).
- Spiegelhalter, Pearson & Short 2011 and the hurricane "cone of uncertainty" literature: not fetched; the second is about places.
- The full PNAS supplementary results and the JMCB published version of Galvão & Mitchell: paywalled or blocked.
- EBA threshold rows beyond the two that agreed twice.
- ESRB Annex II, the interactive ESRB dashboard, and FRED usage figures: not fetched.
- The Code of Practice 3.0 text and WCAG, as instructed.

RICH REFERENCES
1. McMahon, Naylor, Rholes & Rickards, Bank of England SWP 1,196 (July 2026): the only randomised comparison of fan charts with five other formats, for public and expert readers.
2. Galvão & Mitchell, ESCoE DP 2021-06 / Cleveland Fed WP 21-28: two waves, over 3,000 and over 4,000 adults, formats against trust in the statistical office.
3. Bank of England Monetary Policy Report November 2025, Chart 3.1 footnote, read beside the 1998 Quarterly Bulletin article: one chart, two documented band rules, and a dated statement of what was removed.

WHAT SURPRISED ME
- The fan chart was not scrapped. Eighteen months after "They should be eliminated", the Bank still printed it, minus the judgemental skew.
- The band convention changed from 10% steps to 30% steps without the picture looking different.
- The review's claim that the charts "receive little attention from the public" carries no evidence in the text, and the Bank's later experiment found them the best-understood format.
- The ESRB dashboard uses no colour coding at all; the regulator display with traffic lights is the EBA's.
- The Bank's layered content raised comprehension but did not significantly raise trust among the public in either study; only "relatable" wording moved trust, and only slightly.
- Verbal hedges are the worst of both worlds in two independent studies: they lowered trust (van der Bles) and did little for understanding (Galvão & Mitchell), while numeric ranges did neither harm.
- SWP 750 is dated 2018, not 2019, and the fetch reader repeatedly scrambled table rows (EBA) while passing string checks, so table-derived numbers need an eyeball check.


---

## Agent C

AGENT C — ECONOMIC DEVELOPMENT AND PLACE. All fetches 6 October 2026. WebSearch calls used: 17 of 30.

Marking: SV = STRING-VERIFIED (YES on an exact-string presence re-fetch; every check batch carried a false control string, all controls returned NO). SP = SINGLE PASS (reader output, not re-checked; treat as unconfirmed wording). Direct download for grep was blocked by the proxy, so all verification is by presence prompt. No statistic about any named place is reported; where the reader returned one it was discarded.

---

C1. ONS EXPLORE LOCAL STATISTICS (ELS)

Sources
- ELS service QMI (official documentation; live; reader gave "Last revised: 25 April 2025", SP): https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/methodologies/explorelocalstatisticsserviceqmi
- "Clustering similar local authorities and statistical nearest neighbours in the UK" (official methodology; live; "Last revised: 18 March 2026", SP): https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing/methodologies/clusteringsimilarlocalauthoritiesandstatisticalnearestneighboursintheuk
- An indicator page, read for furniture only: https://www.ons.gov.uk/explore-local-statistics/indicators/gross-disposable-household-income-per-head
- Analysis Function case study (practitioner case; no date printed): https://analysisfunction.civilservice.gov.uk/case-studies/case-study-launching-explore-local-statistics-service-ons
- Analysis Function blog, Sian-Elin Wyatt, 13 June 2025: https://analysisfunction.civilservice.gov.uk/blog/bringing-local-data-to-life-the-journey-behind-explore-local-statistics
- National Statistical blog, Ian Diamond, 26 March 2024: https://blog.ons.gov.uk/2024/03/26/local-data-at-your-fingertips/
- GSS subnational data strategy: https://analysisfunction.civilservice.gov.uk/policy-store/gss-subnational-data-strategy/

Who it is for (QMI, "Uses and users")
- «inquiring citizens who are interested in finding out more about their local areas» SV. The fuller list (SP) names "expert analysts in local and central government", "policy influencers in local and central government" and inquiring citizens.
- Diamond blog: «from local and central government, devolved administrations, academia, the media, the private sector and all interested citizens» SV.

What was tested — this is thin
- Case study: «Conducted extensive user research and testing to ensure clarity and usability» SV; «93% of users found it easy to use» SV; «57% rated it» ['extremely useful'] SV. No n, no date, no method and no denominator are given for either percentage.
- QMI (SP): "We regularly conduct user research on the service." and "We run a feedback survey in the service, which allows us to understand user satisfaction, identify issues, enhance features, and improve the user experience."
- Wyatt blog (SP): "building the service in stages and constantly testing assumptions with real users."
- No participant numbers, rounds or findings are published in any source reached. A search of the ONS Digital blog found no ELS user-research post. The October 2024 ONS blog on local data contains no usage or decision evidence.
- Reuse claim: «The code has been reused by» SV (case study).

"Similar areas" method
- QMI: «These groups are created by using K-means clustering on a range of publicly available data sources» SV.
- QMI: «ordered list of the 20 most similar areas to the area of interest, ordered by Euclidean distance» SV.
- QMI (SP): "A global model that accounts for overall similarity is presented alongside economic- and demographic-themed models."
- Methodology: «Standardisation involves transforming each indicator to have a mean of zero and a standard deviation of one» SV.
- Methodology: «We optimise the number of clusters between 4 and 15 for each of our models» SV; silhouette scores guide the choice (SP); PCA is used to reduce indicators (SP).
- Indicator count: "an underlying dataset of 29 subnational indicators" was quoted on two passes, but the YES/NO check answered ambiguously; the page also says (SP) "We identified 33 UK indicators and 6 England only indicators that satisfied these conditions". Treat the count as SP.
- Caveats: «is designed as a snapshot, and should not be viewed as comparable over time with previous versions» SV; «so the nearest neighbours for an area may not all be in the same cluster» SV.

Indicator metadata and furniture
- QMI metadata list (SP): "title, description, link to the original statistical release, last updated date, department name of the data owner, any caveats, interpretation notes, whether the indicator is standardised …, whether the indicator is marked as official statistics in development, unit of measure, appropriate decimal place for the data."
- Uncertainty: «We provide confidence intervals, which give an indication of the uncertainty, when they are available in the original statistical release» SV.
- Timeliness: «We aim to update within three weeks of the updated statistics becoming available» SV.
- Stated limitation (SP): "a time lag between when the original statistical release source is published and when the indicators are added or updated on the service."
- Indicator page: headings «About these estimates» SV and «Get the data» SV; chart labels «Map», «Line chart», «Bar chart», «Table» SV; «is one of 116 local indicators on the Explore local statistics service» SV. The source line takes the form "Source: [producer] published [date]" (SP). "Get the data" links are XLSX, CSV, CSVW, the source producer and the QMI report (SP). No accreditation badge was seen on that page (SP).
- QMI (SP): time-series charts let users compare a selected area with "the median value of all areas over time (if this is available)".

Subnational data strategy
- Ambitions: «Produce more timely, granular and harmonised subnational statistics» SV; «Build capability and capacity for subnational statistics and analysis» SV; «Improve the dissemination of subnational statistics» SV.
- Geography: «should be collected and recorded at the lowest possible geographical level» SV (attributed in the document to GSS Geography Policy); «flexible user-defined areas» SV.
- Comparability (SP): "Work towards the harmonisation of subnational statistics and data, to make them more comparable, consistent and coherent across the GSS."
- Date: one pass gave "December 2021"; a second found no date printed. UNVERIFIED.
- The QMI (SP) says the service's vision "was set out in Section 6" of this strategy.

Properties: provenance; reach.
Mechanisms
- A per-indicator metadata record (the SP list above). Borrowable: it is a checklist.
- A "within three weeks" refresh target, with the lag stated as a limitation. Borrowable as a published service standard.
- Uncertainty shown only when the source publishes it. Borrowable as an honest rule.
- Similar areas (standardise, PCA, K-means with 4–15 clusters chosen by silhouette, plus a 20-nearest list by Euclidean distance) with the snapshot caveat. Borrowable in principle; it needs many comparable areas and published code.
Role: the best-documented UK provenance furniture for a place tool. Its reach evidence is two percentages without a denominator.

---

C2. NOMIS

Sources
- About: https://www.nomisweb.co.uk/home/about.asp
- First-time visitors: https://www.nomisweb.co.uk/home/newuser.asp
- A dataset page: https://www.nomisweb.co.uk/datasets/apsnew
- Release calendar: https://www.nomisweb.co.uk/home/release_group.asp
- "Nomis/NeSS update", 17/05/2004 (SP): https://www.nomisweb.co.uk/articles/77.pdf
All official service documentation, live.

History and purpose
- «Nomis is run by the University of Durham on behalf of the Office for National Statistics» SV.
- «First launched in 1981» SV. Full sentence, returned identically on two non-leading passes: "First launched in 1981, Nomis houses an extensive range of government statistical information on the UK labour market including Employment, Unemployment, Earnings and Annual Population Survey."
- «the most detailed and up-to-date statistics from official sources for local areas throughout the UK» SV.
- «All the facilities and data downloads on our Web site are free» SV; «You can access all the data on our site without registering» SV.
- Home page strapline (SP): "a service provided by Office for National Statistics (ONS), the UK's largest independent producer of official statistics."
- 2004 note (SP): "ONS and Durham University (Nomis) have signed a further two-year contract, so the Nomis service will continue in its current state until March 2006", alongside a plan to fold Nomis into Neighbourhood Statistics. Nomis is still running in 2026, so it outlived the service meant to absorb it.

Provenance furniture on a dataset page
- Section labels «Revisions and corrections» SV and «Contact details for this dataset» SV. Other labels (SP): Methodology; Other information (Coverage, Units, Analyses, Keywords); About this dataset; About the variables; Release calendar; Download options.
- «This is the reference period for the most recent figures available from this dataset» SV.
- «Data is usually released at 7am on the release day» SV.
- Revisions log is dated, one line per entry: «Estimates revised due to identified error» SV. Other entries (SP) take the form "Reweighted to [year] population estimates."
- Release calendar columns «Data series», «Next update», «Status», «How long?» SV; status values «Confirmed» and «Provisional» SV. No explanation of "How long?" is printed (SP).
- Confidentiality (SP, first-time visitors page): "Access to Business Register and Employment Survey (BRES) data requires special permission called a Notice, although there are also publically available BRES datasets subject to a higher degree of rounding."
- Discontinuity note on an older dataset page (SP): "…so are not continuous with BRES datasets for years after 2015."
- Not found: any statement on confidence intervals or reliability on the dataset landing page; these presumably sit inside query output, which the fetch tool cannot reach.

Usage figures: none published on the About page, the first-time visitors page or the 2004 note. A targeted search found none. Report as absent, not zero.

Properties: provenance; longevity; reach (unevidenced).
Mechanisms: a per-dataset dated revisions log; a release calendar with Confirmed/Provisional status and a fixed 7am release; a two-tier access rule (open rounded data, licensed unrounded data). All borrowable as patterns.
Role: the longevity case (45 years, a university operating for the statistical office), and the cleanest example of a per-dataset revisions log.

---

C3. ENGLISH INDICES OF DEPRIVATION (2025 edition published; it supersedes 2019)

Sources
- Collection page, published 30 October 2025: https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025
- FAQ 2025 (HTML): https://www.gov.uk/government/statistics/english-indices-of-deprivation-2025/english-indices-of-deprivation-2025-frequently-asked-questions
- Research Report 2025, 93 pp.: https://assets.publishing.service.gov.uk/media/68ff547a49d08dd781b48351/ID_2025_Research_Report.pdf
- Technical Report 2025, 134 pp.: https://assets.publishing.service.gov.uk/media/68ff59c80f801e57b5bef907/ID_2025_Technical_Report.pdf
- FAQ 2019 (no date printed): https://assets.publishing.service.gov.uk/media/5dfb3d7ce5274a3432700cf3/IoD2019_FAQ_v4.pdf
Official statistics documentation; 2025 live, 2019 superseded.

Correction to the brief's wording: the FAQ does not say "twice as deprived". The control string was absent and no sentence containing "twice" exists in the 2019 FAQ. The "twice" sentence is in the Research Report and is about scores, not ranks.

Rank is not a quantity
- FAQ 2025, Q23: "For example, a small area with a rank of 1,000 is not half as deprived as a place with a rank of 500." Returned identically on three non-leading passes. One YES/NO check answered NO while giving the identical sentence as "closest"; treat as verified by repetition. The same fragment is SV in the 2019 FAQ (Q19).
- FAQ 2025 (SP): "This means that each can tell you if one area is more deprived than another but not by how much."
- Research Report 3.2.3: «they show that one area is more deprived than another but not by how much» SV.
- Research Report 3.2.5: «an area with a score of 60 on the IMD is not simply twice as deprived as an area with a score of 30» SV; «It is recommended that ranks and deciles, but not scores, are used» SV (fragment checked from "it is recommended…").

Not a measure of affluence
- FAQ 2025: «is designed to identify aspects of deprivation, not affluence» SV (also SV in the 2019 FAQ, where the subject is "The IMD2019").
- FAQ 2025: «it is not necessarily among the most affluent» SV.
- Technical Report 3.6.4: «the Indices are specifically constructed to identify deprivation and not affluence» SV; «the Indices discriminate well between deprived neighbourhoods but not so well between those areas in the less deprived part of the distribution» SV.
- Research Report 3.2.10: «Differences between less deprived areas in the country are therefore less well defined than those between areas at the more deprived end» SV.

Comparison across editions
- FAQ 2025, Q25: «Indices releases should not be viewed or construed as a time-series» SV.
- FAQ 2025: «Updates and changes to methods and datasets come at the expense of» ['backwards' comparability with previous versions of the Indices] SV for the fragment.
- FAQ 2025, Q23: «But the Indices are not designed to provide 'backwards' comparability with previous iterations» SV.
- FAQ 2025 (SP): "…does allow some comparisons to be made, but only in terms of comparing the rankings as a snapshot in time, accompanied by appropriate caveats around changes as noted above".
- FAQ 2025, the stated reason (SP; both numbers recurred on two passes): "Overall, a total of 55 indicators comprise the IoD25 …, an increase from 39 in the IoD19." The reader also listed changed denominators and geographies.
- Research Report: «this comes at the expense of 'backwards' comparability with previous versions of the Indices» SV (paragraph number inconsistent between passes: 3.4.4 or 3.2.6).
- Research Report 3.4.6: «users should be aware, and make clear in analysis, that such changes are relative to other areas» SV.
- Research Report 3.4.8: «but this does not mean that there have been no changes to the level of deprivation in the area» SV.
- FAQ 2019, Q22: «they are not designed to provide 'backwards' comparability with previous iterations (2015, 2010, 2007, 2004 and 2000)» SV; «as if comparing snapshots in time» SV.

Rank and decile conventions
- FAQ 2025, Q13 (SP; the figure recurred across passes): ranks run "from 1 (most deprived area) to 33,755 (least deprived area)". FAQ 2019: «32,844» LSOAs SV.
- «dividing them into 10 equal groups» SV. The 2025 FAQ then admits (SP) the bands "are not precisely equal" and prints each decile's count (alternating 3,375 and 3,376).
- «although there is no definitive cut-off at which an area is described as 'deprived'» SV.
- FAQ 2025 (SP, recurred): "The Index is not a suitable tool for targeting individuals."
- Research Report 3.3.5: «No single summary measure is the 'best' measure» SV.

Method facts behind the rules
- Technical Report 3.4.1: «the resulting estimate may be unreliable, with an unacceptably high standard error» SV (the case for shrinkage).
- Technical Report 3.4.2: «weighted combination of that small area's score and the mean value for a larger grouping of areas» SV.
- Technical Report 3.7.3: «These weights are unchanged since the construction of the IMD 2004» SV. Domain weights as read (SP): 22.5, 22.5, 13.5, 13.5, 9.3, 9.3, 9.3.
- Research Report 3.2.13: «The exponential transformation stretches out the deprived end of the distribution» SV.
- No rank intervals are published; the control string about per-LSOA rank confidence intervals was absent.

Properties: change over time; trust.
Mechanisms
- A paired "can / can't be used for" FAQ, each line with a worked example. Borrowable as-is; it is the genre's best usage-rule text.
- Deciles published beside ranks, with an explicit "no definitive cut-off" sentence. Borrowable.
- The "snapshot, not time series" rule with the reason given. Borrowable wherever method changes between editions.
- Constant weights across two decades as a stability device. A design choice, not a text to copy.
Role: the reference case for stating, in plain sentences, what a rank cannot say.

---

C4. ONS HEALTH INDEX (ENGLAND)

Sources
- Bulletin "Health in England: 2015 to 2021", 16 June 2023: https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/bulletins/healthinengland/2015to2021
- "Health Index methods and development: 2015 to 2021", last revised 16 June 2023 (SP): https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/methodologies/healthindexmethodsanddevelopment2015to2019
- Earlier methods paper, 2015 to 2018: https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/methodologies/methodsusedtodevelopthehealthindexforengland2015to2018
- ONS blog, Greg Ceely, 3 December 2020: https://blog.ons.gov.uk/2020/12/03/developing-the-health-index-for-england
Official statistics documentation.

Structure: «Once fully constructed, the Health Index consists of 56 indicators» SV. Bulletin (SP): "56 indicators, summarised into 14 subdomains, 3 domains and the overall Health Index score." The three domains are Healthy People, Healthy Lives and Healthy Places (SP).

Base convention
- «The Health Index has been scaled to a base of 100 for England, with a base year of 2015» SV.
- «a score of 110 represents a score that is one 2015 standard deviation higher than England 2015's score» SV.
- «A score of 100 in the Health Index and its components represents health in England in 2015» SV.
- «A higher number always means better health and a lower number means worse health» SV.

Change over time as the design goal
- «meaning comparisons can be made between scores over time and between different geographies» SV.
- Blog: «provides a single value for health showing how health changes over time» SV; «to allow for comparison between areas» SV; the origin, quoted by the blog from the then Chief Medical Officer, «alongside GDP and the Measuring National Well-being programme» SV.
- 2015–2018 methods (SP): "the mean and standard deviation for each indicator are calculated for a base year and are then applied to the whole time series", so the approach "allows for comparisons across time and only causes back-series changes when the reference year is updated."

Weighting: «Equal weighting is used to weight the three domains» SV. Subdomains equal within domain (SP). Indicators weighted by factor loadings within subdomain (SP).

Uncertainty and data gaps
- No confidence intervals around index scores were found in the method as read.
- Robustness is by method comparison (SP): "Correlations between resultant scores from each pair of methods were above 0.9."
- External assurance (SP): "has collaborated with The Alan Turing Institute to quality assure the Health Index methods."
- «Just over 22% of all records were affected by imputation in some way» SV.
- «For 21 of 56 indicators, change may have been expected in 2021 but could not be measured because of unavailable or inconsistent underlying data» SV.
- Label (SP): experimental statistics "potentially have a wider degree of uncertainty than official statistics without this label."

Status
- Last release 16 June 2023. «Next release: To be announced» SV on the bulletin; the same was read (SP) on the scores dataset and the integrated care systems dataset.
- No discontinuation or pause notice was found on any ONS page fetched, and two targeted searches found no ONS statement. I could not confirm a formal discontinuation. The accurate description is: not updated for over three years, with no published status notice.
- A 2025 Lancet piece ("The Health Index: a framework to guide health-driven prosperity") exists but returned 403; nothing is quoted from it.

Properties: change over time.
Mechanisms
- Fixed base year (England 2015 = 100, 10 points = one base-year standard deviation), with standardisation parameters frozen so adding a year does not revise the back series. Borrowable as a rule; it needs a stable indicator set.
- A stated count of indicators where change could not be measured. Borrowable as a disclosure.
Role: the clearest "designed for change over time" method, and the cautionary case of an index that stalls without saying so.

---

C5. SCOTLAND'S NATIONAL PERFORMANCE FRAMEWORK; WALES

Sources
- Performance overview (old site, still serving; "as at: 17th October 2024", SP): https://nationalperformance.gov.scot/national-outcomes/performance-overview
- Consolidated indicator page (old site, still serving): https://nationalperformance.gov.scot/measuring-progress/national-indicator-performance
- gov.scot collection (reader gave last updated 30 September 2026, SP): https://www.gov.scot/collections/national-performance-framework/
- Letter, Cabinet Secretary for Public Service Reform to the Finance and Public Administration Committee, 15 September 2026: https://www.parliament.scot/-/media/files/committees/session-7/finance-committee/correspondence/2026/20260915-national-performance-framework-cab-sec-psr-to-fpac.pdf
- Wales, "Quality information for the Wellbeing of Wales report: 2026", 1 October 2026: https://www.gov.wales/quality-information-wellbeing-wales-report-2026-html

The arrow rule
- «Performance is assessed as improving, maintaining or worsening based on the change between the last two data points of an indicator» SV.
- Next sentence (SP, recurred on two passes): "The assessment of performance is made objectively and impartially by senior analysts in the Scottish Government." With «independently of Scottish Government Ministers» SV.
- Category labels (SP, with «Performance to be confirmed» SV): Performance Improving; Performance Maintaining; Performance Worsening; Performance to be confirmed; Indicator in development.
- «81 National Indicators» SV.

There is no single threshold. The rule is set indicator by indicator and appears only inside each indicator's prose:
- A significance rule: «This increase represents a significant change at the 95% confidence interval and the arrow is therefore performance improving» SV; «This decrease does not represent a significant change at the 95% confidence interval» SV.
- A margin rule against a moving comparator: «more than 0.1 percentage points above» SV, in a sentence comparing the latest rate with "the average for the previous three years" (place values discarded).
- A reference to an unprinted rule: «This suggests that performance is maintaining, under the methodology for this National Indicator» SV.
- The per-indicator pages that used to carry each criterion now redirect (302) to the gov.scot collection. Three URLs were tried, then I stopped. The exact per-indicator thresholds could not be retrieved; web.archive.org is blocked for the fetch tool.

Status
- The old site is partly retired: the two pages above still serve, indicator pages redirect.
- Collection page: «finalising a set of streamlined national indicators» SV; «aligned with the UN Sustainable Development Goals» SV; (SP) the government "earlier this year consulted on draft NPF proposals" and intends "to launch the full NPF soon".
- Letter (SP): seven National Outcomes (Connected, Healthy, Prosperous, Secure, Skilled, Sustainable, Fair), and "We intend to formally launch the reformed National Performance Framework soon." Neither source states the new number of indicators or how direction will be shown.

Wales
- «There are 17 national milestones in total, covering 16 national indicators» SV. The 2026 report page says (SP) "50 national indicators".
- «We assign each measure as either improved, deteriorated, no change or not assessed» SV.
- «Where possible confidence intervals are used to assess if the change is statistically significant» SV.
- «For some of the indicators that are not based on survey data, confidence intervals are not available» SV; followed (SP) by "In those cases, change over time has been assessed based on guidance from the data expert."
- «Change is assessed since 2015» SV.
- (SP) "Some of the 17 milestones have multiple parts to them, so in total there are 20 assessments of progress." and "We have not considered whether the milestones are on course to be met, simply the direction of change."

Properties: change over time; trust (who decides).
Mechanisms
- A three-state direction label plus two honest non-states ("to be confirmed", "in development"). Borrowable.
- Assignment by named analysts independent of ministers. Borrowable as a governance statement.
- Wales's four states with a significance test where intervals exist and a declared expert judgement where they do not, measured from a fixed baseline. Borrowable; the fallback is honest but not reproducible.
- Scotland's "last two data points" comparator is the weak part: it turns on a single interval and the thresholds are no longer findable.
Role: two national examples of direction-of-travel labelling. Wales's rule is printed and compact; Scotland's shows what is lost when the rule lives on pages that get retired.

---

C6. OECD REGIONAL WELL-BEING

Sources
- Landing page (live): https://www.oecdregionalwellbeing.org/
- User guide, reader gave version October 2025 (SP): https://www.oecdregionalwellbeing.org/assets/downloads/Regional-Well-Being-User-Guide.pdf
Official documentation.

Topics and coverage
- Landing page: «eleven topics» SV. As listed there (SP): income, jobs, housing, health, access to services, environment, education, safety, civic engagement and governance, community, and life satisfaction.
- Landing page: compare "with «467 OECD regions»" SV. User guide: «468 OECD regions» SV. These are consistent if the landing page counts the others (yours plus 467).
- Landing page (SP): "October 2025: Data updated to 2024 (or latest available year)."

No composite, by stated choice
- «The web tool does not include a regional composite well-being index» SV.
- «we do not make a single statement about the overall well-being in a region» SV.
- The reasoning in between (SP): "The trade-off between a composite index (which conveys a single unified view, but may dilute information) and a range of indicators (which offers detailed information, but is more difficult to communicate) is widely debated."

The 0–10 scale is relative
- «A higher score indicates better performance in a topic relative to all the other regions» SV.
- Method (SP): identify minimum and maximum across regions, normalise with the min–max formula, multiply by 10; where a topic has more than one indicator, "the score is defined by the arithmetic mean of the normalised value of the respective indicators."
- Outliers (SP): for two indicators "a threshold has been applied to eliminate the values that are below the 5th percentile and above the 95th percentile."

Similar regions
- «based on the sum of the absolute differences in the topics scores» SV; «the so-called Manhattan distance» SV.
- «The top four regions from different countries with the lowest distance to the selected region are displayed» SV.

Trend rule
- «Well-being trends compare the score of the region from the most recent year to its score in 2000 or the closest year available» SV.
- «It shows if the region has progressed in the topic, relatively to the other regions» SV.
- «Evolution of the score above +5% or below -5% over the period is considered respectively as an improvement» SV. The full sentence (returned by the verification pass) continues: "(increasing arrow) or a decline (decreasing arrow), otherwise as a stable situation (horizontal arrow)."
- No significance test; the control string was absent.

Does it rank? It publishes no overall rank. Within a topic it shows relative position: the guide speaks (SP) of whether a region "has increased or decreased its relative ranking since 2000" and of a top/bottom 20% disparity ratio.

Properties: comparison without rank; trust.
Mechanisms
- A printed refusal to aggregate, with the reason. Borrowable as a statement.
- Min–max relative scoring. Borrowable, with the catch that a score moves when other regions move.
- A ±5% dead-band arrow against a fixed start year. Borrowable as a simple three-state rule; it is a change in a relative score, not in the underlying measure.
- Four nearest regions by Manhattan distance, forced to be in other countries. Borrowable as a "peers elsewhere" rule.
Role: the strongest worked example of comparison without a league table, with a threshold rule for arrows printed in one sentence.

---

C7. CENTRE FOR CITIES; WHAT WORKS GROWTH

Centre for Cities
- Data tool: https://www.centreforcities.org/data/data-tool/ ; Cities Outlook 2026, 26 January 2026: https://www.centreforcities.org/wp-content/uploads/2026/01/Cities-Outlook-2026.pdf . Think-tank practitioner publication; live, annual.
- Tool purpose (SP): "…to show the scale and nature of the variation in the economic performance of cities and towns across the UK by highlighting the performance of the 63 largest urban areas on 17 indicators."
- Tool furniture (SP): "Data dashboard last updated on 4 Feb 2026"; a downloadable XLSX of the whole dataset.
- Unit: «defined as primary urban areas (PUAs)» SV; «rather than individual local authority areas» SV.
- It ranks. Table sections «10 cities with the highest» SV and «10 cities with the lowest» SV, with a «Rank» column SV.
- No confidence intervals (control absent). The reader found no sentence warning about comparison with earlier editions, changed boundaries or revisions; caveats are table footnotes (SP), e.g. data not available for one nation.
- The tool is JavaScript-rendered; its "about the data" panel could not be read.

What Works Growth evidence standards
- Scale page: https://whatworksgrowth.org/resources/the-scientific-maryland-scale/
- Scoring guide, "Updated June 2016": https://whatworksgrowth.org/wp-content/uploads/16-06-28_Scoring_Guide.pdf
- A current review using the standard (rapid evidence review, Enterprise Zones, May 2025; method only): https://whatworksgrowth.org/wp-content/uploads/Enterprise-Zones-May-2025.pdf
Practitioner framework; live.

- The threshold: «We define SMS 3 methods to be the minimum standard for our reviews» SV (guide, p.18 per reader). «We shortlist all those impact evaluations that could potentially score 3 or above on the SMS» SV.
- Level 3: «a comparison group used to provide a counterfactual (e.g. difference in difference)» SV. Full level text (SP): "Comparison of outcomes in treated group after an intervention, with outcomes in the treated group before the intervention, and a comparison group used to provide a counterfactual (e.g. difference in difference)."
- Level 5: «Reserved for research designs that involve explicit randomisation into treatment and control groups» SV.
- Levels 1, 2 and 4 (SP): 1 is a cross-sectional or before-and-after comparison without a comparison group; 2 adds adequate control variables; 4 exploits quasi-randomness in treatment.
- Why: «Establishing causality requires the construction of a valid counterfactual» SV; «That outcome is fundamentally unobservable, so researchers spend a great deal of time trying to rebuild it» SV.
- Judgement admitted: «The ranking of individual studies is not an exact science and often involves a degree of judgement» SV.
- The score covers method and implementation (SP): "In order for an RCT to achieve the maximum SMS 5 score on implementation, three criteria must be met"; a worked case in which all three are violated "achieves SMS 3 for implementation."
- In use, May 2025: «We identified 53 studies that met our evidence standards» SV; «Eleven studies were scored as SMS 4 and 42 SMS 3» SV; exclusion of simple before-and-after comparisons «because we cannot be sure that changes can be attributed to the effect of the EZ» SV; «Be cautious of findings based on a small number of studies» SV; «None of the studies considers cost effectiveness» SV.
- Also (SP): "We also exclude case studies or evaluations that focus on process (how the project is implemented) rather than impact (what was the effect of the project)."
- The "How to use our evidence reviews" page is disallowed by robots.txt; nothing is quoted from it.

Properties: trust (standards of evidence); change over time (a before-and-after change is not evidence of impact below level 3).
Mechanisms
- A five-level design scale with a declared inclusion floor, and counts of studies at each level printed in every review. Borrowable as a labelling scheme for any "what difference did it make" claim.
- Centre for Cities' top-10 / bottom-10 ranked tables are the opposite convention to the OECD's. Not a mechanism to borrow; a contrast.
Role: the clearest sector statement that change without a comparison group is description, not impact.

---

C8. LEVELLING UP WHITE PAPER TECHNICAL ANNEX AND WHAT FOLLOWED

Sources
- Technical annex, "missions and metrics", February 2022: https://assets.publishing.service.gov.uk/media/620b772be90e0710a7b3ffca/Technical_annex_-_missions_and_metrics.pdf
- Statement of Levelling Up Missions, 25 January 2024 (date SV on cover): https://assets.publishing.service.gov.uk/media/65b0f163160765000d18f7b7/Statement_of_Levelling_Up_Missions.pdf
- Levelling-up Missions Annual Report 2024-2025, May 2025: https://assets.publishing.service.gov.uk/media/682cac551be3f53ed5f45347/LURA_Annual_Report.pdf
- Levelling-up Missions Annual Report 2025-2026, July 2026: https://assets.publishing.service.gov.uk/media/6a509bbaa6586e258d371c52/LU_Report_25-26.pdf
Official policy documents; the framework is abandoned as policy but still statutory.

How many metrics, at what geography
- Twelve missions (SP: "sets out twelve missions"). Neither the annex nor the 2024 Statement prints a total count of metrics, as read; I did not count them and give no figure.
- Role of supporting metrics: «These metrics help measure intermediate outcomes, provide additional context and act as an early indicator» SV.
- Geography varies by mission (all SP): "These metrics will be measured over ITL1 areas"; "tracked at lower tier local authority level"; "measured over upper tier local authorities in England, local authorities in Wales, council areas in Scotland".

The annex's own caveats
- «but not by region, and this is an important data gap» SV.
- «most proxy measures of institutional capital are not produced in a timely and consistent manner» SV.
- «This mission is exploratory» SV.
- «There are considerable challenges to developing measures for pride of place» SV.
- (SP) "Further work will be undertaken, in consultation with external stakeholders, to develop and refine these metrics."
- (SP) "there are currently no official UK Government statistics that provide this data at a regional level."

2024 Statement
- «using metrics that are publicly available and routinely updated» SV.
- «In some cases, metrics listed are England only or England and Wales only» SV.
- «The Government will be required to report annually against its missions and metrics and lay the report before Parliament» SV.
- Still unfinished two years on (SP): "Survey-based measures for pride in place have been in development since the publication of the Levelling Up White Paper."

What has happened since
- May 2025 report: «This Government has moved away from the levelling up programme» SV; «Social Fabric Index: not implemented» SV; intends (SP) "to bring forward legislation to repeal Part 1 of the Levelling Up and Regeneration Act 2023 at the earliest opportunity".
- July 2026 report: «it has moved away from the levelling up programme» SV; «The Government intends to bring forward legislation to repeal Part 1 of the Levelling-up and Regeneration Act 2023» SV; «Social Fabric Index: not implemented» SV; metrics not refreshed because producers «have not published new data since last year's report» SV.
- Anomaly to check by eye: the July 2026 report's reporting-period string was verified as «from 25 January 2024 to 24 January 2025», the same period as the May 2025 report; the string for 2025–2026 was absent. Either the source carries the earlier period over or the reader conflated the two. Do not print the period without checking.
- No successor dashboard is referenced in either annual report (SP). The old ONS "Subnational indicators explorer" URL now serves the Explore Local Statistics page (observed on fetch; no notice read), so ELS is the de facto successor for the data, without mission framing.

Properties: change over time; provenance.
Mechanisms
- A per-mission statement of headline metric, supporting metrics and geography, with data gaps named in the same document. Borrowable as a format.
- A statutory annual report that outlives the policy and records "not implemented" and "no new data". Not borrowable as law; the lesson is that a metric set tied to a political programme has a short life.
Role: the cautionary tale for change over time. Metrics announced before they existed, some never built, reporting continuing only by legal obligation.

---

C9. UNASKED THREADS

1. Index users, measured (MHCLG "Indices Futures" consultation response, 22 December 2022): https://www.gov.uk/government/consultations/indices-futures-updating-the-english-indices-of-deprivation-iod-consultation/outcome/indices-futures-updating-the-english-indices-of-deprivation-iod-consultation-government-reponse
 - «In total, 117 respondents replied to the Indices Futures' consultation» SV. Local government 67 (57%), recurred on two passes.
 - Uses reported (SP): profiling service users, local needs assessments, and informing distribution of funding.
 - «Users requested that a release calendar be made available to aid planning» SV; «The Indices are typically updated every 3 to 5 years» SV; «They cannot be used to identify real change in deprivation over time» SV.
 - Bears on reach and change over time: the users asked for the thing the method cannot give.

2. A dashboard evaluated with its users (Scottish Government, "Near time data service: dashboard user engagement – research findings", 13 August 2024, SP for date): https://www.gov.scot/publications/near-time-data-service-dashboard-user-engagement-research-findings/ . Read for evaluation design only; it is a management-information dashboard, not a public one.
 - Design: survey, interviews and focus groups, usage metrics, personas.
 - Numbers, each returned on the verification pass: "41 users completed the survey in Microsoft Forms. This equates to a 5% response rate."; "809 individuals were invited."; "24 participants took part: 14 dashboard users and 10 developers."; "Around 400 individual users had accessed a dashboard. The dashboards were opened around 6,500 times." (January to March 2024).
 - Measures: ease of access (88% agreeing easy or very easy); data "informing their decisions or conclusions as part of their role" (49%); satisfaction with how up to date the data is (81%).
 - A borrowable evaluation template: three methods, a stated response rate, and one question that asks directly whether the data informed a decision.

3. What Works Centres evaluated (Frontier Economics for ESRC, January 2022): https://www.ukri.org/wp-content/uploads/2022/08/ESRC-110822-InvestmentInWhatWorksCentresEvaluation.pdf
 - «65 stakeholder interviews» SV and «over 300 users of WWCs» SV.
 - «WW Local Economic Growth: 61% (N = 66)» SV; the reader's gloss (SP) is that this is the share of respondents drawing on the Centre's evidence reviews regularly (2–3 times a year or more).

4. Ranks published with intervals (JRC statistical audit of the Global Innovation Index 2024): https://www.wipo.int/web-publications/global-innovation-index-2024/en/appendix-ii-joint-research-centre-jrc-statistical-audit-of-the-2024-global-innovation-index.html
 - «All published GII 2024 ranks lie within the simulated 90 percent confidence intervals» SV.
 - «not only at face value, but also within the 90 percent confidence intervals» SV.
 - «These confidence intervals also have to be taken into account when comparing economy rank changes from one year to the next» SV.
 - Computation: "a total of 5,000 Monte Carlo simulations" (wording returned by the verification pass), varying (SP) "the treatment of missing data, the aggregation weights applied to pillars and the aggregation formula used at the pillar level". Audited (SP) "for a 14th consecutive year".
 - A second example beside Chapter 5's. Borrowable in principle; it needs the full indicator data and simulation.

5. A major index that stopped ranking (County Health Rankings & Roadmaps, methods page, live): https://www.countyhealthrankings.org/health-data/methodology-and-sources/methods
 - «Beginning in 2024, Health Groups are displayed in the county health snapshot» SV.
 - «ten unequally-sized groups based on the data» SV.
 - «groups counties based on similarity and meaningful gaps in the data» SV.
 - «Where possible, we provide the margins of error (95% confidence intervals) for our measure values» SV; "Larger error margins suggest lower reliability for the associated data value." (wording from the verification pass).
 - The algorithm is not named on that page ("k-means" absent), and the stated reason for leaving ranks was not found there. The PubMed record for the 2020s methods paper returned no content.

6. The critique behind item 5 (Arndt, "Just How Useful Are Health Rankings?", Health Services Research, 2015; editorial, read for method only): https://pmc.ncbi.nlm.nih.gov/articles/PMC4600352
 - «rankings can be too unreliable to be helpful» SV.
 - «the degree to which the rankings are random directly drives the degree to which any decisions based on them are random» SV.
 - «Rankings are driven, in part, by random noise» SV.
 - Its device is a simulation with one constant underlying rate for every area, which still yields a spread of ranks. It comments on Courtemanche, Tchernis and Soneji, "Modeling Area-Level Health Rankings" (same journal, 2015), which a reCAPTCHA blocked.

7. UK guidance on describing change (GSS "Communicating quality, uncertainty and change", Data Quality Hub, 17 December 2018 (SP); the page says, on the verification pass, "This page is currently under review and awaiting updates."): https://analysisfunction.civilservice.gov.uk/policy-store/communicating-quality-uncertainty-and-change/
 - «Describe the direction of change, its absolute size and its relative size over time» SV.
 - «Emphasise that changes within the bounds of random variation are indicative, rather than definitive» SV.
 - "Phrases like 'care must be taken' and 'exercise caution' are not sufficient by themselves, because they do not help the reader to understand what they can and cannot do with the numbers." (fragment SV, full sentence from the verification pass).
 - "Use phrases like 'broadly stable' to emphasise that it is too early to make definitive statements about movements in the series." (same status).
 - Model sentence: «This decrease is not statistically significant and it is likely that the natural variation in the figures explains the change» SV.
 - It says nothing about small areas or ranks, as read. No GSS guidance specific to small-area change was found.

8. The nearest thing to small-area change guidance (ONS, "Small area gross value added estimates, UK: 1998 to 2022", 21 August 2024; flagged on the page as not the latest release): https://www.ons.gov.uk/economy/grossvalueaddedgva/bulletins/smallareagrossvalueaddedestimatesuk/1998to2022
 - «We advise a degree of caution when making comparisons between data at the most granular (building block) level» SV.
 - "This is because data at the lowest levels are more volatile than larger aggregated geographies." (fragment SV).
 - «We advise additional caution in interpreting results for wards» SV.
 - «Revisions can apply to the whole time series» SV.
 - The implied rule is to aggregate building blocks before comparing. By the GSS guidance's own standard in item 7, "a degree of caution" is the insufficient kind of phrase.

---

LEFT OUT, AND WHY
- Exact per-indicator arrow thresholds for the Scottish framework: the indicator pages now redirect and the web archive is blocked.
- A total count of levelling-up metrics: not printed in the annex or the 2024 Statement as read; not counted by hand.
- Any formal ONS statement on the Health Index's future: none found. The 2025 Lancet piece was 403.
- Nomis table-level confidentiality and reliability flags: inside query output, unreachable by fetch. Nomis usage figures: none published where I looked.
- The Centre for Cities tool's interactive "about the data" panel: JavaScript-rendered.
- What Works Growth "How to use our evidence reviews": robots.txt disallowed.
- The Wellbeing of Wales main report body: only the contents page rendered; the rule is taken from the quality report.
- Courtemanche et al. (2015) and the County Health Rankings methods paper: blocked.
- Place statistics returned by the reader on the Scottish, Centre for Cities and OECD pages were discarded.

RICH REFERENCES (three)
1. English Indices of Deprivation 2025 Research Report, chapter 3, with the FAQ Q22–Q25. The fullest plain-language account of what a rank, a decile and a score may be used to say, with worked examples and reasons.
2. OECD Regional Well-Being User Guide (October 2025). In a few pages: the refusal to aggregate, the relative 0–10 scale, the ±5% arrow rule and the Manhattan-distance peers.
3. ONS "Clustering similar local authorities and statistical nearest neighbours in the UK" with the ELS service QMI. A fully specified similar-areas method plus a service-level quality statement with a refresh target and stated limitations.

WHAT SURPRISED ME
- The deprivation FAQ never says "twice as deprived". The famous rule is "not half as deprived" for ranks and "not simply twice as deprived" for scores, in two different documents.
- Scotland's arrows had no common threshold; each indicator had its own rule, and those pages have now been redirected away while a 2024-dated overview still serves.
- The Health Index, built to track change, has had "Next release: To be announced" since June 2023 with no status notice anywhere I could reach.
- The levelling-up annual reports are still being laid before Parliament in 2026 by a government that says it has moved away from the programme, recording "not implemented" and "no new data".
- Explore Local Statistics is award-winning and well documented on provenance, yet its published reach evidence is two percentages with no n.
- Nomis, 45 years old, publishes no usage figure, and in 2004 was scheduled to be absorbed by a service it has since outlived.
- County Health Rankings, the best-known ranked place index, dropped ordinal ranks in 2024 for ten unequal groups.
- Cities Outlook prints rank columns and top/bottom-ten tables with no interval and no edition-comparison caveat that the reader could find.


---

## Agent D

AGENT D REPORT — culture and charity impact practice; public data projects
All fetches 6 October 2026. WebSearch calls used: 23 of 30.
Marking: [SV] = string-verified by a second presence-prompt pass (control strings were included and correctly rejected); [SP] = single pass only; [ABS] = abstract only.

THREE PREMISES IN THE BRIEF THAT THE SOURCES DO NOT SUPPORT
1. The Impact & Insight Toolkit did not end in 2023 and Illuminate is not its successor. The Toolkit is live (updates dated 1 Oct 2026). Illuminate replaced Audience Finder, the audience-data platform.
2. I found no independent evaluation of the Toolkit itself. The only independent evaluation is Nordicity's 2016 report on the national test.
3. I found no warning about economic-impact multipliers in the Culture and Heritage Capital documents. The words "multiplier", "GVA" and "economic impact" were reported absent from the 2024 guidance (two passes on the first 100k characters, one on the remainder) and from the 2021 framework (one pass).

-----------------------------------------------------------------
D1. ACE QUALITY METRICS, THE TOOLKIT, ILLUMINATE
-----------------------------------------------------------------
2016 national test (Knell & Whitaker): cite only, per brief. The Toolkit's history page links the report: https://impactandinsight.co.uk/app/uploads/2019/02/QualityMetricsNationalTest_Report_Knell_Whitaker_2016_0.pdf

(a) Independent evaluation: Nordicity, "Evaluation of Participants' Experience of the Quality Metrics National Test Phase", dated "6th September 2016" [SV].
URL: https://www.artscouncil.org.uk/sites/default/files/download-file/Nordicity%20Evaluation%20of%20Quality%20Metrics%20trial.pdf
What it is: commissioned independent evaluation; historic.
Sample and method:
- "two online surveys were designed and distributed concurrently to a total population ('N') of 316 contacts, receiving a total sample size ('n') of 209 responses and accounting for an overall 66% response rate." [SV]
- Participating organisations: N 144, n 97, 67% [SV]. Peer assessors: N 172, n 112, 65% [SV].
- "19 one-on-one interviews, four focus groups across the country with 20 individuals" [SV]
Findings:
- "Overall, a majority (63%) of respondent organisations either strongly agreed or somewhat agreed that the QM framework was useful to their organisation" [SV]
- "nearly half (47%) of respondent organisations somewhat or strongly agreed that the time and resources spent on the CC platform was appropriate" [SV]
- "For those who had completed full triangulation, the resulting data was regularly referenced as 'interesting' rather than 'useful'." [SV]
- "the majority of organisations do not see that it will be effective as a tool for benchmarking with other organisations" [SV]
- "it was commonly reporting that Audience Finder had to be deprioritised" [SV; "reporting" as printed]
- Slider: "there were concerns that public and self-assessors completed it too quickly without much thought on positioning (and with a natural movement to 'swipe' to the right)" [SV]
- "enthusiasm is measured and contingent upon a number of key amendments and assurances" [SV]
- "clearer articulation of the purpose of the QM programme is needed to ensure buy-in" [SV]
Single-pass figures, not re-verified: 62% likely to use the dimensions again; 71% useful for understanding audiences' assessments; 37% positive on cross-discipline comparability; 69% would use the platform if cost were disregarded; a recommendation to replace the slider with a numbered scale; and a concern about whether data would fall under Freedom of Information.
Property: trust; reach. Mechanism: a pilot evaluated independently, with N, n and response rate printed, before roll-out. Borrowable as an evaluation design. Role: the baseline evidence that a profile instrument was found "interesting rather than useful" and feared as a benchmark before it became a condition.

(b) The Toolkit, in its own words (impactandinsight.co.uk; live).
- History page [SP]: version 1 was commissioned by ACE "to be used by band 2 and 3 National Portfolio Organisations (NPO) and other ACE funded organisations and projects from 2019-2022 (extended to 2023 as a result of the COVID-19 Pandemic)."
- FAQs, https://impactandinsight.co.uk/resources-guidance/faqs/ : "it is not mandatory to sign up to the Impact & Insight Toolkit" [SV]. For Creative People and Places, "Toolkit registration and Culture Counts use is a funding requirement" [SV].
- Data ownership: "Culture Counts is a data processor." [SV] "It is not owned by Arts Council England." [SV]
- Relation to Illuminate: "PwC has been commissioned to offer a data collection service and to produce audience development focussed insights; this service is called Illuminate." [SV] "In a nutshell, Illuminate is about understanding who your work reaches; the Toolkit is about understanding how your works contribute to you achieving your overall ambition." [SP]
- John Knell, "A Decade of Solving the Evaluation Puzzle", 4 Nov 2025: "As of October 2025, there are over 800 organisations registered to the Impact & Insight Toolkit project; over 500 of which are NPOs." [SV] "It is fair to say that many NPOs were anxious about the Impact & Insight Toolkit when it was launched, particularly about how the resulting data might be used by Arts Council England." [SV] This is the provider's own account.
- ACE's page (https://www.artscouncil.org.uk/impact-and-insight-toolkit, metadata 1 Apr 2026): "All National Portfolio Organisations, Sector Support Organisations and Creative People and Places can use the toolkit." [SP]
Mechanism: the same instrument moved from mandatory (2019–23) to opt-in, with data ownership stated as the user's. Borrowable as a governance statement.

(c) Illuminate (https://www.artscouncil.org.uk/illuminate; live).
- "Illuminate is the Arts Council's Audience Data platform." [SV] "Built by PwC." [SV] "Illuminate went live on Thursday 1 June 2023." [SV]
- "All funded organisations must use Illuminate to report to the Arts Council on funded activity and audience or participant numbers." [SV]
- "Over 1,000 organisations are using the platform and we have seen more than 64,000 activities reported and over 220,000 survey responses collected via Illuminate in the first year." [SV]
- Stated purpose: "This data will help the Arts Council continue to make the case for investment in creativity and culture and deliver our ambitions for our strategy, Lets Create, deepening our understanding of audiences – who they are and what they want." [SP]
- Dimension sliders: none. The page does not mention "quality", "dimensions", "sliders" or "Audience Spectrum" [SV as absent]. The FAQ's mandatory questions are event information, group type and demographics [SP].
- FAQ: "Once data is input to Illuminate, the platform allows users to access a single view of their organisation's audience data, benchmarked against regional and sector datasets." [SP] "An audience classification system to support audience analysis will be developed and built using the data in Illuminate." [SP]
- ACE's reasons for the change: not stated on either page. The FAQ says only what Illuminate replaces in reporting terms (the CPP quarterly submission and the Activity and Audience sections of the Annual Survey) [SP].

(d) What went wrong with Illuminate (Arts Professional; trade journalism).
- 13 Sep 2023, Neil Puffett: ACE suspended the audience-survey requirement until 1 April 2024 and delayed box-office and events deadlines; three-year PwC contract of £1.6m [all SP]. ACE quoted: "We're developing a complex tool with huge potential for the sector, and we want it to be the best it can be." [SP]
- 27 Aug 2024, Neil Puffett: "The move extends a previous suspension of reporting requirements to the Illuminate platform by an additional year" [SV]. ACE spokesperson: "We made this decision to give organisations more time to adapt to the new reporting requirements and ensure they focus on contributing the essential information." [SV] "Following user feedback we are looking to make improvements to ensure the platform and survey collection mechanisms are as suitable and straightforward for as many users as possible" [SV]. "In 2022/23, NPOs were asked to collect a minimum of 380 survey responses over the course of the year." [SV] "In total for 2023/24, with a larger portfolio of 985 organisations, around 220,000 surveys were provided to Illuminate." [SV]
- 16 Dec 2025: Arts Professional quoting Baroness Hodge's review of ACE (the article is the source quoting the review; I did not fetch the review itself):
  "The present reporting requirements are not fit for purpose." [SV]
  "They are too onerous and there is widespread scepticism about whether ACE uses all the data it demands" [SV]
  "A more proportionate and targeted approach to reporting must be found" [SV]
  "The Arts Council is sitting on a wealth of data and analysis that people felt is not properly shared with arts organisations" [SV]
  "Despite criticism, such as a perceived overemphasis on performance data that is not relevant or helpful for museums, Illuminate has provided previously unavailable data for a range of interested parties on funding distribution and audiences." [SV]
- 10 Mar 2026, Emily Godwin: "Reporting data will still be collected through the annual survey and the council's audience data platform, Illuminate." [SP]

(e) Published academic criticism.
- Sara Selwood (2019), "A possible teleology of cultural sector data in England", Cultural Trends 28(2–3), 177–197, DOI 10.1080/09548963.2019.1617940. Full text read at a mirror: https://interaccio.diba.cat/sites/interaccio.diba.cat/files/a_possible_teleology_of_cultural_sector_data_in_england.pdf
  "NPOs are potentially compromised by their dual role as data providers and grant recipients, as is ACE in its capacity as an official statistics provider and development agency." [SV]
  "ACE requires those NPOs in receipt of at least £250,000 of its funding to use the Toolkit to report how their peers and publics rated at least four examples of their work per year." [SV]
  "The Toolkit's operation, which is largely determined by both vested and conflicting interests, contrasts starkly with the ways in which Taking Part, and ACE's other official statistics are expected to operate under UKSA's jurisdiction." [SV]
  Abstract: "greater investment in the latter would encourage the teleological development of cultural sector data designed for sectorial advocacy." [SV]
- Gilmore, Glow & Johanson (2017), "Accounting for quality: arts evaluation, public value and the case of 'Culture counts'", Cultural Trends, DOI 10.1080/09548963.2017.1382761. Publisher page 403; abstract read via the Semantic Scholar API [ABS]: the system "claims to provide a more effective, democratic tool for quality measurement of art" [SV against the API record]; method "qualitative research with two consortia of organisations involved in Culture Counts pilot projects" in England and Australia [SV]. The abstract gives no n and no finding.
- Phiddian, Meyrick, Barnett & Maltby (2017), "Counting culture to death: an Australian perspective on culture counts and quality metrics", Cultural Trends 26(2), DOI 10.1080/09548963.2017.1324014: unreachable (403; no abstract in the API). Nothing quoted.
Role for the chapter: a profile instrument that becomes a funding condition puts both data provider and funder in a dual role (Selwood), and the next platform's mandatory survey collection had to be suspended for two years.

-----------------------------------------------------------------
D2. THE AUDIENCE AGENCY
-----------------------------------------------------------------
Announcement: https://theaudienceagency.org/en/news/audience-agency-enter-voluntary-liquidation, dated 11 September 2026.
- "we regret to announce that The Audience Agency will enter a voluntary liquidation process" [SV]
- "This decision follows sustained financial pressures and extensive efforts to identify a viable way forward" [SV]
- "continuing to provide the full scope of our affordable and free services has proved impossible in the current financial climate" [SV]
- "The Company was placed into Liquidation on 10 September 2026" [SV], with "Simon Farr and Tom Bowes of FRP Advisory Trading Limited appointed Joint Liquidators" [returned as the closest sentence on the check].
- "Significant public investment has contributed to the development of The Audience Agency's research, platforms and evidence base." [SV]
- "colleagues and partners are exploring appropriate ways in which this legacy might benefit the sector in future." [SV]
The announcement does not name Audience Spectrum, Audience Finder, a data transfer or a successor.

ACE statement (in Arts Professional, 18 Sep 2026, Emily Godwin; the article is quoting an ACE spokesperson): "From 2015 until March 2023, we grant-funded TAA to deliver the Audience Finder programme, which gathered large-scale ticketing and audience data from the cultural sector. We are aware that on Friday, TAA announced that it will enter voluntary liquidation, and our understanding is that organisations are currently still able to access and download their historic data. We are in contact with TAA to understand next steps." [SV in fragments]
Same article: "it lost the new ACE contract in 2022 for £1.6m to PricewaterhouseCoopers to develop a new online data collection and analysis platform." [SV] Creative Scotland is "assessing the implications for organisations in Scotland" [SV].

Status on 6 October 2026:
- No successor custodian, data transfer or ACE takeover has been announced in anything I could reach.
- TAA's news page shows nothing after the liquidation notice (first 100k characters read).
- audiencespectrum.org still describes the tool and carries "Copyright © 2026 The Audience Agency" with only a link to the notice [SP].
- audiencefinder.org redirects to audienceanswers.org/intro, which still invites sign-in and carries only the linked headline [SP].
Property: provenance and custodianship. Mechanism: none documented; the continuity arrangement is one sentence of "our understanding" from the former funder. Not borrowable; it is the negative case.

-----------------------------------------------------------------
D3. DCMS SURVEYS AND CULTURE AND HERITAGE CAPITAL
-----------------------------------------------------------------
Participation Survey: ended September 2025 [SP, from the successor's methodology note].
- Collection page last updated 18 Dec 2025; last quarterly release July–September 2025; last annual 2024–25, published 30 July 2025 [SP].
- 2024/25 technical report: "In total 82,513 addresses were sampled, from which 36,074 respondents completed the survey – 31,596 via the online survey and 4,478 by returning a paper questionnaire." [SV]
- "This constitutes a 0.42 conversion rate (responses/sampled addresses), a 29% household-level response rate, and an individual-level response rate of 24%." [SV]
- After checks, "leaving 34,378 respondents in the final dataset." [SV]
- "The 2024/25 survey was not boosted; however, ACE plans to implement a LA boost every three years." [SV]
URL: https://www.gov.uk/government/statistics/participation-survey-2024-25-annual-publication/participation-survey-2024-to-2025-annual-technical-report

Community and Engagement Survey (CES): https://www.gov.uk/guidance/community-and-engagement-survey (published 19 Aug 2025, updated 12 Aug 2026 [SP]); live; Official Statistics.
- "Fieldwork for the CES began in October 2025" [SV]
- "the CES replaced DCMS' Participation Survey and Community Life Survey" [SV]
- "is a continuous push to web survey of adults aged 16 and over in England" [SV]
- "Verian is carrying out the survey on behalf of" DCMS [SV]
- "in 2025/26 the Community Life Survey questions was asked of a sample of 175,000 whilst the Participation Survey questions was asked of a sample of 33,000. A combined module of questions, comprising questions from both survey sets, was asked of the full sample of 208,000." [SV; grammar as printed]
- "The content for the CES has been kept broadly similar to the previous surveys but combining the surveys has resulted in efficiencies and more coherent outputs." [SV]
- 2025/26 methodology note: "The total sample size for the Community and Engagement Survey year was 192,244." [SV] "In October 2025 to March 2026, 173,481 people (90%) completed the Community and Engagement Survey online and 18,763 (10%) completed the paper version of the questionnaire." [SV] These two sentences do not obviously reconcile and I did not resolve it.
- Break-in-series rule: "A vertical dotted line is included in charts to indicate the change in survey name and structure, although estimates can still be compared." [SV]
- January–March 2026 technical report: "This constitutes a 0.25 conversion rate (responses/sampled addresses), a 27.69% household-level response rate, and an individual-level response rate of 14.65%." [SV] 435,052 addresses issued [SV]; 116,692 respondents in the quarter [SV]; £10 voucher [SP].
Property: change over time; comparability. Mechanism: a marked discontinuity line plus an explicit statement on whether estimates remain comparable. Borrowable: it is a one-line printed rule.

Culture and Heritage Capital: "Embedding a Culture and Heritage Capital Approach", DCMS, 17 Dec 2024, 74 pages; current guidance.
URL: https://www.gov.uk/government/publications/embedding-a-culture-and-heritage-capital-approach/embedding-a-culture-and-heritage-capital-approach
- "Standard economic measures are an incomplete measure of public welfare and value added, as they do not take into account assets and services that do not have market prices." [SV]
- Five steps [SV]: "Consider the culture and heritage assets"; "Consider the culture and heritage services"; "Consider the welfare impacts"; "Monetise the welfare impacts"; "Project future benefits across the asset's life to estimate total asset value".
- Cautions: SCBA "should always be conducted in a proportional way" [SV] and "should also sit alongside a wider set of evidence that can inform decision making" [SV].
- "One limitation that is important to be aware of is double counting between methods, and as such, some non-market valuation methods cannot be used in conjunction with each other" [SV]
- "It is important when presenting results in an appraisal to be clear how far economic valuation captures the full range of relevant effects." [SP]
- The CHC approach "should not replace, for example, existing artistic decisions" [SP].
Its cautions are double counting, proportionality and the incompleteness of monetised value. The 2021 framework's aim: "The programme's ultimate aim is to create publicly available statistics and guidance that will allow for improved articulation of the value of the culture and heritage sectors in decision making." [SP]

-----------------------------------------------------------------
D4. CHARITY-SECTOR IMPACT CODES
-----------------------------------------------------------------
Code of Good Impact Practice (Inspiring Impact, 2013; NPC-hosted 2022 version): https://www.thinknpc.org/wp-content/uploads/2019/03/Code-of-good-impact-practice-2022.pdf
Eight principles, each [SV]:
1. "Take responsibility for impact and encourage others to do so too"
2. "Focus on purpose"
3. "Involve others in your impact practice"
4. "Apply proportionate and appropriate methods and resources"
5. "Consider the full range of the difference you actually make"
6. "Be honest and open"
7. "Be willing to change and act on what you find"
8. "Actively share your impact plans, methods, findings and learning"
Also: "Impact is the difference you make." [SP] "you're willing to accept that you may not be having the impact you intended" [SV]. On contribution: "Equally, you're conscious that the changes you see may have occurred without your involvement, may be short term, or may be the result of the work of others." [SP] Developed "after a sector-wide public consultation and with input from a working group of 17 organisations" [SP]. Status: the programme "ran from 2011 until early 2022" [SV]; the Code survives as a re-hosted document.

NPC's four pillar approach (Kazimirski & Pritchard, 4 June 2014 [SV]): https://www.thinknpc.org/resource-hub/npcs-four-pillar-approach/
- "Map your theory of change"; "Prioritise what you measure"; "Choose your level of evidence"; "Select your sources and tools" [all SV]
- "A theory of change should be at the heart of your approach because it shows what you want to achieve and how you plan to achieve it, setting out the causal links between your activities and your end goal." [SV]
- "Choose an appropriate level of rigour of evidence that suits the needs of your stakeholders. This will depend on a combination of what is desired or needed and what is practical." [SV]

Charities SORP (FRS 102): the primary text was unreachable. charitysorp.org and charitiessorp.org document URLs returned 403 on four attempts, and the gov.uk copy of SORP 2019 returned 410. I quote no SORP paragraph. Secondary source only: ICAEW summary of changes, "Charities SORP 2026" (https://www.icaew.com/-/media/corporate/files/technical/charity/webinars/summary-of-changes.ashx):
- "It has an effective date of 1 January 2026" [SV]
- "Tier 1: All charities applying accruals accounts and with a gross income of not more than £500,000" [SV]; Tier 2 up to "not more than £15 million" [SV]
- "Tier 1 charities are asked to consider how their work made a difference to beneficiaries and provided benefit to wider society. Tier 2 and 3 charities are required to explain the impact the charity is making and must consider the long-term effect of its activities on individual beneficiaries and on society as a whole." (referenced to paragraphs 1.27–1.33) [SV as ICAEW's wording, not the SORP's]
The exact SORP paragraph still needs to be taken from the SORP itself.

Principles of Social Value (Social Value International; live): https://www.socialvalueint.org/principles
Titles, each [SV]: Involve stakeholders; Understand what changes; Value the things that matter; Only include what is material; Do not overclaim; Be transparent; Verify the result; Be responsive.
- Principle 2: "Articulate how change is created and evaluate this through evidence gathered, recognising positive and negative changes as well as those that are intended and unintended." [fragment SV]
- Principle 5: "Only claim the value that activities are responsible for creating." [SV]
- Principle 6: "Demonstrate the basis on which the analysis may be considered accurate and honest, and show that it will be reported to and discussed with stakeholders." [fragment SV]
- Principle 7: "Ensure appropriate verification of results in line with the decisions being supported. In cases where results are being reported to external audiences and/or are supporting significant decisions, independent assurance is required." [returned on the check]

Five dimensions of impact (Impact Management Project norms, hosted by Impact Frontiers; live): https://impactfrontiers.org/norms/five-dimensions-of-impact/
- "What tells us what outcome the enterprise is contributing to, whether it is positive or negative, and how important the outcome is to the people and communities experiencing it, as well as to the planet." [SP]
- "How Much tells us how many people experienced the outcome, what degree of change they experienced, and how long they experienced the outcome." [SP]
- "Contribution tells us whether an enterprise's efforts resulted in outcomes that were likely better than what likely would have occurred otherwise." [SV]
- "Risk tells us the likelihood that impact will be different than expected." [SV]
The page gives no account of how the consensus was reached.

What the sector's own reviews say about reporting quality:
- NPC, "Making an Impact" (Ní Ógáin, Lumley, Pritchard; 16 Oct 2012): "NPC surveyed 1,000 charities with incomes over £10,000" [SV]. "Today, 75% of charities measure some or all of their work, and nearly three-quarters have invested more in measuring results over the last five years." [SV] "Only 5% of charities say that wanting to improve services is a primary motivation for increasing their impact measurement efforts." [SV] "25% of charities still do not measure the impact of their work at all." [SV] Summary page, not the PDF: https://www.thinknpc.org/resource-hub/making-an-impact/
- NPC, "State of the Sector 2020" (18 May 2020): "95% of our respondents this year agreed that the use of data and evidence were important to them achieving their mission." [SP; n not given on the page]
- Charity Commission, Accounts Monitoring Review, public benefit reporting: "In May 2018, we selected a random sample of 105 trustees' annual reports from the register of charities, covering accounting years ending during the 12 months to 31 December 2016." [SV] "52% of the trustees' annual reports demonstrated a clear understanding of the public benefit reporting requirement, similar to last year's 51%." [SV] "It is disappointing that all too many charities do not explain the activities they undertake to improve the lives of their beneficiaries and make a difference." [SP] The accompanying press release (20 Dec 2018) is marked withdrawn 6 Nov 2023.
- Hyndman & McConville (2016), Nonprofit and Voluntary Sector Quarterly 45(4), 844–865; accepted manuscript at https://pureadmin.qub.ac.uk/ws/files/16695582/transparency.pdf. Sample: "The top 100 charities (by income) were identified using the Caritas Data Top 500 charities list for 2010/11" [SV]; 100 annual reports, 63 annual reviews, 99 websites [SP]. Finding: "the vast majority (94 per cent) of charities fail to report a single efficiency measure in any channel of communication (or conversely, only six per cent report an efficiency measure in any channel)." [SV] Abstract: efficiency reporting "is more concerned with legitimising these organisations rather than providing ethically-driven accounts of their efficiency." [SV]
Property: trust; provenance; change over time. Mechanism: a principle set that names contribution ("may be the result of the work of others"; "Do not overclaim") and risk as things to be stated. Borrowable as wording. The evidence on compliance is that roughly half of sampled reports met even the basic requirement.

-----------------------------------------------------------------
D5. CHARITY COMMISSION PUBLIC-TRUST RESEARCH
-----------------------------------------------------------------
2026 wave: "Public trust in charities 2026", BMG Research for the Charity Commission.
URL: https://www.gov.uk/government/publications/research-into-public-trust-in-charities-and-research-with-charity-trustees-2026/public-trust-in-charities-2026
- Mean trust 6.5 out of 10 [SV].
- "4681 completes were achieved." [SV]
- "Quantitative fieldwork took place between the 6th and 9th of January and the focus groups took place between the 12th and 19th of March." [SV]
- "Over half (57%) say they have high trust in charities" (7–10) [SV].
- Factors in whether to trust a charity [SV as table rows]: "Most of the money raised is spent directly on the causes the charity supports" 55%; "The charity makes a real difference to the people and communities that it serves by achieving its stated purpose" 51%; "It is easy to see how much the charity has raised, and how this money has been spent" 40%.
- "Money reaching the end cause remains the most important driver of trust" [SP]
- Comparators [SP]: doctors 7.1; charities 6.5; banks 6.2; police 5.7; MPs 3.4.
2025 wave (PDF: https://assets.publishing.service.gov.uk/media/6867bd2e2557debd867cbcbd/Public_Trust_in_Charities_2025.pdf):
- "4092 completes were achieved." [SV] Mean 6.5; 57% high trust [SV].
- Question: "Firstly, thinking about how much trust and confidence you have in charities overall, on a scale of 0-10 where 10 means you trust them completely and 0 means you don't trust them at all, how much trust and confidence do you have in charities?" [returned on the check]
- Top factor 53% [SV]; second factor 45% [SP].
- "an online panel was used to achieve a nationally representative split of participants" [SP]
- Series as printed [SP]: 2005 6.3; 2008 6.6; 2010 6.6; 2012 6.7; 2014 6.7; 2016 5.7; 2018 5.5; 2020 6.2; 2021 6.4; 2022 6.2; 2023 6.3; 2024 6.5; 2025 6.5.
2024 wave: not fetched; its mean (6.5) is from the later reports' tables.
Commission blog, 13 July 2026: "Each year we survey public attitudes to charities, something we first began over 20 years ago." [SP]
Property: trust, measured. Mechanism: one fixed 0–10 question repeated for two decades with bands printed (high 7–10, medium 4–6, low 0–3), and the drivers asked as a ranked list. Borrowable. The stated drivers are about where money goes and visible difference made.

-----------------------------------------------------------------
D6. OUR WORLD IN DATA AS AN INSTITUTION
-----------------------------------------------------------------
- Publisher: "Our World in Data is a project of the Global Change Data Lab, a non-profit organization based in the United Kingdom (Registered Charity Number 1186433)." [SP; /organization]
- Licence: "All visualizations, data, and articles produced by Our World in Data are completely open access under the Creative Commons BY license." [SV; /easier-to-reuse-our-data, 21 Nov 2024] Code: "made publicly available for transparency and educational reference under a custom license" [SP; /faqs].
- Funding [SP; /funding]: "We are supported by grants from foundations including the Wellcome Trust, the Gates Foundation, the Skip Foundation, Coefficient Giving, and the Mohn Westlake Foundation." "More than 4,000 people have donated over the past couple of years." No statement on funder influence was found on that page.
- Reach: the About page carries no reach figure (two passes). The latest figures I could verify are in the Global Change Data Lab Trustees' Annual Report for 2022, signed 23 September 2023 (https://assets.ourworldindata.org/uploads/2023/09/2022-Annual-Report.pdf):
  "In 2022, OWID had on average more than 3 million unique users per month" [SV]
  "nearly 100 million page views this year" [SV]
  "referenced in nearly 25,000 media articles in 2022" [SV]
  "cited in more than 6,500 academic publications" [SV]
  Total income 2022 £1,784,746 (2021: £2,416,307) [SP]. Later annual reports were not located.
- Pipeline conventions (ETL metadata reference, https://docs.owid.io/projects/etl/architecture/metadata/reference/; live):
  origin.date_published: "Exact day (or year, if exact day is unknown) when the producer's data (in its current version) was published" [SV]
  origin.date_accessed: "Exact day when the producer's data (in its current version) was downloaded by OWID" [SV]
  dataset.update_period_days: "Expected number of days between consecutive updates of this dataset by OWID" [SV]
  processing_level, as returned on the second pass: "Must be `minor` if the indicator has undergone only minor operations since its origin: Rename entities (e.g. countries or columns), Multiplication by a constant (e.g. unit change), Drop missing values. Must be `major` if any other operation is used: Data aggregates (e.g. sum data for continents or income groups), Operations between indicators (e.g. per capita, percentages, annual changes), Concatenation of indicators, etc."
  Licence follows processing level: "If the indicator's `processing_level` is major, assign `CC BY 4.0`. If the indicator's `processing_level` is minor, choose the most strict license among the origins' `licenses`." [SP]
  description_processing: "Relevant information about the processing of the indicator done by OWID" [SV]
  No "next expected update" field is documented. A data page (grapher/population-unwpp) shows a last-updated date and a next-expected-update date exactly three years apart [SP], so the displayed date appears to be last update plus update_period_days. That is my inference.
- Corrections: I found no published corrections policy. What exists is a feedback form and one sentence: "Our team regularly identifies and investigates data anomalies, often working with original data providers to correct errors." [SV]
- Measuring reach, 2020 audience survey [SP]: respondents were "not a representative sample of our total audience"; 17.5% said they download data while analytics showed "1.6% of sessions have a CSV download".
Property: trust; provenance; reach. Mechanism: provenance as required metadata fields with written rules, and a two-level processing label that drives both the on-chart credit and the licence. Borrowable: the rules are public and short.

-----------------------------------------------------------------
D7. PUBLIC CONFIDENCE IN OFFICIAL STATISTICS (NatCen for UKSA)
-----------------------------------------------------------------
2023 wave: https://natcen.ac.uk/publications/public-confidence-official-statistics (published 14 May 2024).
- "a representative sample of 2,364 adults aged 18 and over in Britain" "from 1,695 households" [SV]
- "This represents an adjusted household response rate of 21.2%" [SV]
- "Fieldwork took place between 4th October and 17th December 2023" [SV]
- Mode: "Respondents were encouraged to complete the 10 to 15-minute survey online, but paper self-completion surveys were offered to all non-responding households" [SV]
- "Most respondents trusted the Office for National Statistics (ONS), with 87% of respondents who gave an opinion indicating that they tend to trust it (71%) or trust it a great deal (16%)." [SV]
- "In 2023, 85% of respondents said they trusted ONS statistics (with 18% saying they trusted them a great deal and 67% saying they tended to trust them)." [SV]
- "Most also indicated that they agree that statistics produced by ONS are free from political interference (72%)." [SV for the figure]
- Government honesty "remained relatively low (32%, compared to 35% in 2021)" [SV]
- "Even fewer respondents (25%) tended to agree that newspapers present official statistics honestly." [SV]
- "Of all institutions included to this question, ONS had the highest level of reported trust of all (87%) among respondents, similar to levels of trust in the courts (82%) or the Bank of England (79%)." [SV] "Trust was lowest in the British media (25%), the Government (31%) and the UK Parliament (36%)" [SV]
- "Attitudes towards the independence of statistics were largely unchanged compared to 2021" [SV]
2021 wave: https://natcen.ac.uk/sites/default/files/2022-12/NatCen_Public-Confidence-in-official-statistics_2021.pdf (published 25 April 2022).
- "a representative sample of 3,398 adults aged 18 and over in Britain" [SV]; "This represents an adjusted household response rate of 24%" [SV]; fieldwork "between 15th October and 20th December 2021" [SV].
- "In 2021 PCOS was run for the first time as a stand-alone push-to-web survey." [SV]
- "In 2021 89% of those able to express a view said they trust ONS and 87% said they trust ONS statistics." [SV] "The equivalent figures in 2018 were 88% and 85%." [SP]
- Free from political interference: "74% agreed that this was the case in 2021, similar to 2018 (73%)" [SV]
- "Only 35% of people able to express a view agreed that the government presents official statistics honestly" and "this has increased (from 31%) since 2018" [SV]
- "Only 24% of those able to express a view agreed that newspapers present official statistics honestly" [SV]
- "82% of people able to express an opinion agreed that official statistics are generally accurate, up from 78% in 2018" [SV]
- "There is a need for caution when making comparisons between 2021 and earlier years of the study" [SV]; 'don't know' responses were "significantly lower in 2021 compared to 2018" [SP].
2014 baseline [SP] (British Social Attitudes, face to face, 1,907 interviews, report February 2015): 88% trusted ONS; 81% its statistics; 66% free from political interference; 28% government honest; 19% newspapers.
Trend (those expressing a view): trust in ONS 88 (2014), 88 (2018), 89 (2021), 87 (2023). Free from interference 66, 73, 74, 72. Government presents honestly 28, 31, 35, 32. The 2016 wave was not fetched.
2025 wave: none found. NatCen's publication page is still the 2023 report and mentions no further wave.
European Statistics Code of Practice (revised edition 2017): Principle 6, "European statistics are developed, produced and published in a professional and transparent manner, treating all users fairly and equally." [SP] The indicators on release calendars are not in the page text; I left this to Chapter 4.
Property: trust, measured for producers. Mechanism: the same question set repeated across waves, 'don't know' excluded and said so, and a printed caution when the mode changed. Borrowable. Trust in the producer runs about 55 points above trust in how government presents the same figures.

-----------------------------------------------------------------
D8. LONG-RUN CUSTODIANS AND SUNSET POLICIES
-----------------------------------------------------------------
UK Data Service: https://ukdataservice.ac.uk/about/ [all SP]. "The UK Data Service is the principal repository for economic, population, and social research data in the UK." "Funded by UK Research and Innovation (UKRI)". On DOIs (Service blog, 2020, Finn Dymond-Green): "Using the study's DOI will always bring the user back to this edition of this dataset, even if its location on the internet should change in the future." Citation guidance asks for "The precise version of the dataset used e.g. edition number or release date info". I could not reach a page stating the rule for when a change earns a new DOI, or the deposit standards in full (two attempts).

Human Mortality Database: https://www.mortality.org/Project/Overview; Methods Protocol "Last Revised: August 5, 2025 (Version 6)" [SV].
- "As much as possible, we have followed four guiding principles in creating this database: comparability, flexibility, accessibility, reproducibility." [SV]
- "However, the database is limited by design to populations where death registration and census data are virtually complete, since this type of information is required for the uniform method used to reconstruct historical data series." [SV]
- "However, we have not attempted to correct the data for systematic age misstatement (misreporting of age) or coverage errors (over- or under-enumeration of people or events)." [SV]
- "assistance from database users in identifying problems is always appreciated!" [SV]
- "The HMD contains original calculations of all-cause death rates and life tables for national populations (countries or areas), as well as the input data used in constructing those tables." [SP]
- Protocol: "The purpose of the database is to provide researchers around the world with easy access to detailed and comparable national mortality data via the Internet." [SV] Quality notes are "covered separately in the documentation for each population" [SP]. Appendix D covers "Period death rates around the time of a territorial change" [SP, heading only]. No statement on how published estimates are revised was found.
Mechanism: comparability by exclusion (only populations meeting the data standard), one uniform method, input data published beside estimates, a versioned and dated protocol. Borrowable as a rule set.

Sunset notes:
- OWID, "Future updates of our data on COVID-19" (15 Nov 2024, Dattani & Rodés-Guirao [SV]): "Most of these datasets are no longer being updated by the data provider, so we will no longer be updating them" [SV]. "For datasets from the CDC (United States), UKHSA (United Kingdom), and health ministries of specific other countries from which we previously updated data, we will now redirect users to the original country's webpage for further updates, potential revisions, and documentation." [SV] The page does not say whether discontinued charts stay online or carry a notice.
- OWID, source switch (28 Feb 2023) [SP]: "This change will be seamless for our users. The URL of all our charts and the variable names in our dataset will remain the same." "An archive of the last version (8 March 2023) of our dataset based on data from Johns Hopkins University is available for download".
- The COVID Tracking Project, "It's Time: The COVID Tracking Project Will Soon Come to an End" (1 Feb 2021, Kissane & Madrigal [SV]): https://covidtracking.com/analysis-updates/covid-tracking-project-end-march-7
  "But the work itself—compiling, cleaning, standardizing, and making sense of COVID-19 data from 56 individual states and territories—is properly the work of federal public health agencies." [SV]
  "We will spend the next five weeks publishing detailed guidance for data users who are looking for sources to replace our work, as well as gap analyses noting where replacement data still doesn't exist." [SV]
  "we're making sure that it comes as close to lasting forever as anything can on the internet" [SV]
  "On March 7, the one-year anniversary of our founding, we will release our final daily update and our data compilation will stop." [SP]
Mechanism: a retirement with a pre-announced end date, a frozen archive, stable URLs, a named replacement source and a published gap analysis. Borrowable, and the best-documented ending I found.

-----------------------------------------------------------------
D9. UNASKED THREADS
-----------------------------------------------------------------
1. A mandatory data platform whose core requirement was suspended for two years (Illuminate), and a review saying there is "widespread scepticism about whether ACE uses all the data it demands" [SV, via Arts Professional]. See D1(d).
2. Stated versus actual use of impact information by donors. NPC, "Money for Good UK" (March 2013): "The core of Money for Good UK was an online survey of 3,000 respondents." [SV] "60% of donors say they care about impact, 10% look mainly for information on impact and ultimately just 2% use an informed assessment of impact to choose between charities." [SV] "If charities improved the way they communicate impact and explain how donations are used, they could potentially attract around £665m more in donations." [SV; a projection] https://www.thinknpc.org/wp-content/uploads/2018/07/MONEY-FOR-GOOD-UK.pdf
3. Whether publishing impact evidence changes giving: Karlan & Wood, NBER Working Paper 20047 (April 2014, revised July 2015) [ABS, SP]. "We test how donors respond to new information about a charity's effectiveness." The reader's summary (not quotation) is no overall effect, larger prior donors giving more and smaller prior donors giving less. No n in the abstract. https://www.nber.org/papers/w20047
4. Funders drive measurement: only 5% of charities cite improving services as the primary motivation (NPC 2012; D4).
5. Intermediary failure, three documented forms: no arrangement at all (TAA; D2); re-hosting by a former partner (Inspiring Impact, which "ran from 2011 until early 2022" [SV]); planned wind-down with archive and gap analysis (COVID Tracking Project; D8).
6. A code that tightens over time: under SORP 2026 impact reporting moves from "asked to consider" (Tier 1) to "required to explain" (Tiers 2 and 3) from 1 January 2026 [SV as ICAEW's summary only].
7. Reach measured by survey overstates use: OWID's 17.5% stated versus 1.6% of sessions observed [SP].
8. Codes that require a theory of change or an evidenced contribution claim: NPC's first pillar; Social Value Principle 2 and Principle 5; the IMP "Contribution" dimension; Code Principle 5's caution. None is mandatory. The only requirement with force is the SORP's.

LEFT OUT, AND WHY
- Charities SORP primary text (403/410): no paragraph quoted.
- Phiddian et al. 2017 (403; no abstract available).
- Hodge review primary text, and any government response: read only through Arts Professional.
- ESS Code of Practice indicators: not in the page text.
- Charity Commission 2024 wave report; PCOS 2016 and 2018 primary reports; later OWID annual reports.
- UK Data Service DOI-versioning rule and deposit standards.
- NPC State of the Sector 2017 and 2024; "Making an Impact" was read on its summary page only, not the 73-page PDF.
- The current Toolkit's dimension statements and whether the slider survives: not checked.
- Knell & Whitaker 2016: cite only, per brief.

RICH REFERENCES
1. Nordicity (2016), Evaluation of Participants' Experience of the Quality Metrics National Test Phase. The fullest account of what a standardised instrument costs the organisations that feed it.
2. Selwood (2019), Cultural Trends 28(2–3). The dual-role argument, set against the standards for official statistics.
3. OWID ETL metadata reference (docs.owid.io). Provenance and processing written as field-level rules.

WHAT SURPRISED ME
- The yardstick's owner failed while the supposedly ended instrument is alive: the Toolkit has 800+ registered organisations and The Audience Agency is in liquidation with no custodian named 25 days on.
- The former funder's continuity statement rests on "our understanding".
- What the public says makes a charity trustworthy is money reaching the cause (55%) and a real difference made (51%), yet only about half of sampled trustees' reports met the basic public benefit requirement.
- Trust in the statistics producer (87%) and trust in government's presentation of the same figures (32%) have sat some 55 points apart across four waves.
- The Culture and Heritage Capital guidance carries no multiplier warning; its cautions are about double counting and proportionality.