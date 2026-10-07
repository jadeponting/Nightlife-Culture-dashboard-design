# Chapter 11 — research agent returns (6 October 2026)

*Kept whole. Four agents; no web search; fetch at source with YES/NO presence checks. SV = string-verified; SP = single pass.*

---

## Agent A — Dashboards and first screens

CHAPTER 11 RESEARCH — FACET: DASHBOARDS AND FIRST SCREENS
All fetches made 6 October 2026.

TOOLS AND METHOD
- WebSearch was unavailable (the shared search budget was already exhausted). Everything below came from WebFetch on direct URLs, plus site-own listings (the Analysis Function search you asked for, the Tableau Research publication index, UKHSA "What's new").
- Marks: SV = string-verified by a second YES/NO fetch (false control strings were included and correctly rejected in most checks). SP = single pass. ABSTRACT = abstract or landing page only.
- Unreachable, nothing quoted: IEEE Xplore (empty pages), HAL (403), PMC (reCAPTCHA), JMIR (empty), Europe PMC and arXiv author listings (429), NIHR Journals Library (405), Taylor & Francis (403), gov.uk site search (robots), oecdbetterlifeindex.org /faq and /about and the OECD working-paper PDF (robots), files.grouplens.org (403), NN/g empty-states article (404), dublindashboard.ie, the UKHSA and GDS blog searches.
- coronavirus.data.gov.uk returned text dated February 2021 on two attempts. I treated it as unreliable and quote nothing from it.

CORRECTIONS TO THE BRIEF
- Item 4's "Kim, Setlur, Agrawala" is wrong. The TVCG paper is by Hyeok Kim, Ryan Rossi, Abhraneel Sarma, Dominik Moritz and Jessica Hullman.
- Item 2's ONS title rule ("sum up the main message … in 10 words or less") is not on the current ONS pages. style.ons.gov.uk now redirects to service-manual.ons.gov.uk/content. The current rules are quoted under item 2.
- "Writing for GOV.UK" has moved: gov.uk/guidance/content-design/writing-for-gov-uk redirects to guidance.publishing.service.gov.uk.
- "Explore local statistics" has left its beta subdomain: explore-local-statistics.beta.ons.gov.uk redirects to www.ons.gov.uk/explore-local-statistics/, and the word "beta" no longer appears on the page.

=====================================================================
ITEM 1 — THE EMPIRICAL DASHBOARD LITERATURE

1a. Sarikaya, Correll, Bartram, Tory & Fisher 2019, "What Do We Talk About When We Talk About Dashboards?", IEEE TVCG 25(1) (InfoVis 2018).
Source: https://alper.datav.is/assets/publications/dashboards/dashboards-preprint.pdf (author preprint). Peer-reviewed survey and design space; it is not an evaluation.
- Corpus: "Our design space is based on a chosen corpus of 83 dashboards" (SV).
- Coding: open coding; two authors independently coded all dashboards, "κ = 0.64; 86.5% agreement", then discussed to consensus (SV for the figures).
- Definition: "consider a display a dashboard if it matches either the visual genre or the functional genre, or both" (SV).
- The two genres: "We distinguish between the visual genre of dashboards (a visual data representation structured as a tiled layout of simple charts and/or large numbers as in Figure 1 left) and the functional genre (an interactive display that enables real-time monitoring of dynamically updating data)." (SP, returned in a verification pass.)
- The paper quotes Wexler et al.: "a visual display of data used to monitor conditions and/or facilitate understanding" (SV; this is the source quoting someone else).
- It quotes Few narrowly: "a predominantly visual information display that people use to rapidly monitor current conditions that require a timely response to fulfill a specific role" (SV; source quoting Few).
- Design-space dimensions (SP, paraphrased list): purpose (strategic, tactical, operational, learning, communication); audience (circulation, visualization literacy, domain expertise); visual features and interactivity (construction, multipage, interactive interface, highlighting, data modification); data semantics (alerting, benchmarks, updateability).
- Seven clusters with counts (SP): Strategic Decision-Making 16, Quantified Self 7, Static Operational 10, Static Organizational 8, Operational Decision-Making 14, Communication 13, Dashboards Evolved 15. These sum to 83.
- On evidence: "Despite their prevalence, the visualization research community has rarely given dashboards their due consideration, with few exceptions [46]." (SV.)
- Limitation: "We did not directly consult dashboard users or designers and may therefore have missed some important design considerations" (SV).
- Beyond the single screen: "The dashboard concept has evolved from single-view reporting screens to include interactive interfaces with multiple views and purposes, including communication, learning, and motivation, in addition to the classic notions of monitoring and decision support." (SP.)
- Role: establishes that "dashboard" names a family of things, and that the field's own base is descriptive, not evaluative.

1b. Bach, Freeman, Abdul-Rahman, Turkay, Khan, Fan & Chen, "Dashboard Design Patterns", IEEE TVCG (arXiv gives 2023; presented at VIS 2022).
Sources: https://arxiv.org/pdf/2205.00757 and https://dashboarddesignpatterns.github.io/. Peer-reviewed pattern catalogue.
- Corpus: "We gathered a corpus of 144 dashboards by starting with the 83 dashboards collected by Sarikaya et al. [44] but discarding three due to lack of clarity or context. We then added 64 new dashboards found on news websites and personal applications." (SV for the first clause and the numbers; 83 − 3 + 64 = 144.)
- "Our final coding describes 42 design patterns, grouped into eight categories" (SV).
- Groups: CONTENT covers Data Information, Meta Information and Visual Representations. COMPOSITION covers Page Layout, Screenspace, Structure, Interactions and Color (SP for the wording; the paper files Interactions under composition, the website under components).
- Website pattern names (SP):
  - Screenspace: Screenfit, Overflow, Detail-on-demand, Parameterized, Multiple page.
  - Structure: Single Page, Hierarchical, Parallel, Open, Semantic.
  - Page Layout: Open, Table, Stratified, Grouped, Schematic.
  - Meta Information: Data source, Disclaimer, Data description, Update information, Annotations.
- Menu, not findings: "Our patterns are purely descriptive in that they capture existing solutions and can serve as speculation tools in the design process and discussion, as well as providing a resource for concepts that can inform the structured evaluation of dashboards, a current gap in the literature." (SV for the first clause.)
- "It was beyond the scope of this work to determine what makes for a 'good' dashboard, and this will depend on many subjective and domain-specific factors." (SV.)
- Trade-off: "Reducing one of the parameters (screenspace, abstraction, number of pages, interaction) requires an increase in one of multiple of the other parameters." (SV as the closest sentence; the website's "Minimizing one parameter…" wording is not in the paper.)
- Genres (SP): Static, Analytic, Magazine, Infographic, Repository, Embedded Mini dashboards.
- Workshop: "We ran a two-week dashboard design workshop" (SV) with 23 participants (ABSTRACT). "The workshop showed that our pattern collection and the associated terminology provided a useful framework to streamline dashboard design for both novice and advanced designers…" (SP). Participants' designs were not tested with readers.
- Role: the vocabulary for layout and structure choices, with the authors' own statement that it ranks nothing.

1c. Tory, Bartram, Fiore-Gartland & Crisan, "Finding Their Data Voice: Practices and Challenges of Dashboard Users", IEEE CG&A, DOI 10.1109/MCG.2021.3136545.
Source: https://www.tableau.com/sites/default/files/2023-01/tory_data_conversation.pdf (full paper). Peer-reviewed interview study. I could not verify volume and issue because IEEE Xplore returned nothing.
- Method and n: "We conducted 1 hour semi-structured interviews with 20 participants over video conferencing." (SP.) "By this categorization, 7 participants were analysts and 13 were dashboard users." (SP.) Recruitment and analysis details (usertesting.com n=16, 18 organisations, modified grounded theory) are SP and paraphrased.
- Findings: "By far the most common tool switch was the 'data dump': extracting data out of a dashboard for ad hoc analysis in a spreadsheet." (SP.) "they use Tableau as a cross tab generator" (SV, participant quotation). "it's really a jumping off point for questions" (SV, participant quotation).
- Barriers, from the abstract: "their engagement with data was often intermittent, dependent on experts, and involved an awkward assembly of tools" (SV).
- Limit that matters for "people don't use it": "Notably, individuals who experience such significant barriers that they forego dashboard use are absent from our study, but may still be relevant to consider." (SP.)
- Role: evidence that readers treat a dashboard as a starting point and take the data elsewhere. It supports export and citable states. It says nothing about public audiences.

1d. Dimara, Zhang, Tory & Franconeri, "The Unmet Data Visualization Needs of Decision Makers within Organizations", IEEE TVCG, DOI 10.1109/TVCG.2021.3074023.
Source: https://visualthinking.psych.northwestern.edu/publications/Dimara_DecisionMakers_2021.pdf. Peer-reviewed survey plus interviews.
- n: "We received 177 complete responses, after removing 30 participants whose responses were incomplete or nonsensical." (SV.) "…consisting of 122 decision makers (red dots) and 42 data analysts (blue dots)." (SV.) Interviews: "10 answered our email and participated in an interview." (SV.)
- Method: "We used the critical incident interview technique [62] asking them to narrate a difficult decision they made in the past." (SV.) Thematic analysis (SP).
- Needs named (SP, paraphrased): trade-off overviews, scenario or "what-if" analysis, interrogation tools, flexible data interfaces, collaboration support, information reduction, qualitative information alongside quantitative.
- On dashboards: "Only one participant reported the use of dashboards during the decision making meeting." (SP.)
- Abstract: "Our findings stress the need to expand visualization design beyond data analysis into tools for information management" (SV).
- Caveat: "Yet, our findings, as in most qualitative studies, should not be interpreted as conclusive or cases for drawing causal inferences, as they are grounded in the data that we gathered." (SV.)
- Role: organisational decision makers; of limited transfer to a public cultural dashboard, but the one-in-ten finding is quotable.

1e. Few's definition.
Source: https://www.perceptualedge.com/articles/ie/dashboard_confusion.pdf, "Dashboard Confusion", Intelligent Enterprise, 20 March 2004. Practitioner framework.
- "A dashboard is a visual display of the most important information needed to achieve one or more objectives; consolidated and arranged on a single screen so the information can be monitored at a glance." (SV.)
- "The means is a single-screen display; the purpose is to efficiently keep in touch with the information needed to do something." (SV.)
- "Dashboard Confusion Revisited" (March 2007, perceptualedge.com/articles/visual_business_intelligence/dboard_confusion_revisited.pdf): "Displays that are used for monitoring what's going on (dashboards) must be designed and must function quite differently than displays that are used to analyze data." (SP.)
- Role: the single-screen sentence, from an open source and not the closed book.

1f. Use over time, abandonment, decay, "dashboard fatigue".
- Not established. I found no peer-reviewed study measuring abandonment or decay of dashboard use, and none of "dashboard fatigue". The one literature-index query I tried (Europe PMC) was rate-limited.
- Unverified lead, from memory and not fetched: an NIHR realist evaluation of QualDash (Randell et al., DOI 10.3310/WBKW4927) that used log files. The QualDash VIS 2020 paper (arXiv 2009.03002) reports deployment in five NHS hospitals but no usage numbers (SP).
- Glanceable and ambient displays: not pursued, as not directly relevant.

=====================================================================
ITEM 2 — PUBLIC DESIGN SYSTEMS

GOV.UK Design System (design system; live pages)
- Start page pattern, https://design-system.service.gov.uk/patterns/start-using-a-service/ : "GOV.UK services must start on a GOV.UK content page." (SV.) The lead-in is "A service's start point should:" (SV), followed by five bullets (SP, copied on a second pass):
  - "give the user just enough information to help them understand what the service does and whether it will meet their need – including giving the service a name that reflects the problem it solves for users"
  - "include a 'button' linking into the service, with text that's consistent with the action you're asking users to take – for example, 'Start now', 'Sign in' or 'Register or update your details'…" (SV)
  - "let users sign in, resume an application they've already started or update their details (if relevant)"
  - "include any other information that most users are likely to need before they start using the service online…"
  - "include details of other ways to access the service…"
- Page template, /styles/page-template/ : "Use this template to keep your pages consistent with the rest of GOV.UK." (SP.) It bundles the skip link, header and footer. It says nothing about content order.
- Summary list, /components/summary-list/ : "Use a summary list to show information as a list of key facts." (SV.) "You can use it to display metadata like 'Last updated' with a date like '22 June 2018'" (SV.) "Do not use it for tabular data or a simple list of information or tasks" (SV.)
- "One thing per page" is a forms rule. https://www.gov.uk/service-manual/design/form-structure , page title "Structuring forms", last updated 7 August 2018: "Start by splitting the form across multiple pages with each page containing just one thing, for example:" (SV.) "User research will tell you when you can merge pages together." (SV.) The control string claiming it applies to all GOV.UK content was rejected. The Question pages pattern adds: "Asking just one question per question page helps users understand what you're asking them to do, and focus on the specific question and its answer." (SP.)
- Absence: the component and pattern lists contain no chart, data visualisation, dashboard, statistic, tooltip or map entry (SP, from the two index pages).

GOV.UK content guidance (standard; now at guidance.publishing.service.gov.uk; no dates shown on the pages)
- Structure, …/writing-guidelines/clear-structure/ : "Put the most important information first." (SV.) "The quicker you get to the point, the greater the chance your users will see the information you want them to." (SV.) "This is sometimes called an 'inverted pyramid' approach." (SV.) "only read 20 to 28% of text on a webpage" (present as link text to NN/g). For headings: "frontloaded – put the most important information first" (SV). The spelling is "frontloaded" and it attaches to headings.
- Titles, …/clear-titles/ : "Your title should be 65 characters or less (including spaces)." (SV.) "Titles must be unique and informative so that users know which page they are on." (SV.) "Most people who use GOV.UK start with a search engine." (SV.) There is no front-loading sentence on the titles page.
- Summaries, …/summaries/ : "Keep all summaries to 160 characters, including spaces" (SP).

ONS service manual (design system and style guide)
- Dashboards, https://service-manual.ons.gov.uk/data-visualisation/guidance/dashboards :
  - "A dashboard is a visual tool that shows different views of data to provide an overview of a specific topic." (SV.)
  - "Only use a dashboard if you have clear justification for doing so." (SV.)
  - "Dashboards can be problematic, as they:" (SV), followed by: "are not well-suited to highlighting important findings; they put the burden of interpreting and understanding data onto the user" (SV for the second clause); "are not well-suited to data that need a large amount of explanation to be understood"; "can quickly become obsolete, as findings and user needs change"; "require a lot of maintenance if they need regular updating"; "are difficult to make accessible and responsive for different devices" (SV).
  - "Only consider using a dashboard when:" … "you are communicating high-level indicators; the more specific the issues and insights are, the less likely it is that a dashboard will be useful" (SV) … "the data are updated frequently, and users are likely to revisit the dashboard".
  - Tips: "put the most important insights at the top or in the most prominent position" (SV); "you do not have to fit everything onto one screen; if the most important information is visible, the user can scroll up and down" (SV for the first clause).
  - "All requests for dashboards on the ONS website will be reviewed by the Digital Content teams." (SP.) "In most cases it is better to use charts that provide users with specific insights." (SP.)
- Interactive charts, …/guidance/interactive-charts-and-animations :
  - "Only consider using an interactive chart where the most important information for the user cannot be clearly shown through a non-interactive chart." (SV.)
  - "Interactive charts need the user to make a selection to see information. This may:" "make it more difficult for users to get messages" (SV); "hide the main messages from users" (SV); "prevent the chart from being useful outside of the Office for National Statistics (ONS) website, for example, on social media".
  - "consider starting your visualisation from a view that either shows the main message without needing any interaction, or helps users navigate the chart" (SV).
  - "This does not include charts where the only interactive element is a tooltip." (SV.) "A tooltip displays data values when the user hovers over or selects part of a chart." (SP.)
- Chart titles, …/guidance/chart-text : "All charts must have a title that is: front-loaded, in the active voice, in sentence case, as concise as possible, 15 words or fewer" (SV for "15 words or fewer"; "10 words or less" and "sum up the main message" both confirmed absent). "The chart title should describe the main trend you want the chart to show to the user." (SV.) Alt-text pattern: "A [chart type] showing that [chart title]." (SP.)
- Titles and headings, /content/writing-for-users/titles-and-headings : "be concise, preferably fewer than 60 characters"; "be frontloaded with the most important information" (SP; "10 words or less" confirmed absent).
- Main points, …/writing-main-points-and-analysis : "Include up to six bullet points, with one trend or point per bullet, to ensure they are concise." (SV.) "The first bullet point should be the one trend or figure that you want users to focus on or take away from the publication." (SV.) "Use fewer than 25 words for each bullet, or what you can say in one breath." (SV.)
- Structure, …/structuring-content : "We use the inverted pyramid model, which recommends ordering content by its importance, to achieve this." (SP.) "The most important information in your content should be placed at the start of each sentence, paragraph or section." (SV.)
- How people read, …/how-people-read-online : "Data show that users only read around 28% of content on a page." (SV.) "Over half of users view the ONS website on a mobile device." (SV.) "80% of users on a phone or tablet do not scroll past the first quarter of a release" (SV; the page gives no source and no date).
- The ONS Design System now lists chart components (area, bar, column, line, scatter) alongside Table, Summary, Hero, Card and Tabs (SP). The line-chart component requires a title and "A textual description of the chart for screen readers" (SP). I found no "describe the chart in words first" sentence and no page titled "data-led content".

NHS design system (design system)
- Do and Don't lists, https://service-manual.nhs.uk/design-system/components/do-and-dont-lists : "Use Do and Don't lists to help users understand more easily what they should and shouldn't do." (SV.) "The Do and Don't lists stack on desktop and mobile, rather than sitting side by side on the page. We found that users read down the page, not across it." (SP.) "We've tested the Do and Don't lists in pages with lots of content. We aren't using them in forms or transactional content and haven't tested them there." (SP.)
- "Know that a page is up to date", …/patterns/know-that-a-page-is-up-to-date (updated November 2025): "Use review dates to let users know when a page was last checked and will be checked again." (SV.) "Put whole page review dates at the bottom of the page." (SP.) Research: "At first we tested them away from the main content, closer to the footer of the page, separated by a rule, but users didn't notice them there." (SP.) The old "Review date" component has been withdrawn in favour of this pattern.
- I found nothing in the NHS manual specific to data pages.

Analysis Function (civil-service guidance; four pages published 6 February 2026; owner GSS Presentation Champions)
- Search for "dashboard" returned 92 results. The four core pages are: building and managing dashboards; testing dashboards for design and accessibility; examples of dashboards; dashboard software.
- Building and managing, https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-building-and-managing-dashboards/ :
  - Definition (SP): "A dashboard is a valuable visual tool that: is updated regularly with minimal effort; is interactive and visualises data; immediately presents data to the user without lots of commentary or analysis".
  - "Only consider using a dashboard when: there is an identified user need; data updates are frequent and can be automated, with users likely to revisit the dashboard; users need flexibility of data combinations and the ability to interact with data; you have sufficient resource to support the dashboard" (SP).
  - Dashboards "put the burden of understanding data and important messages onto the users" (SV); "are not suitable for data that requires a large amount of explanation" (SV); "can quickly become obsolete if findings and user needs change" (SV).
  - "Dashboards often require more resource than initially identified due to their complexity." (SP.)
  - Lifecycle: Discovery, Alpha, Beta, Live, Retirement (SP).
- Testing, …/data-visualisation-testing-dashboards-for-design-and-accessibility/ : "Design your dashboard using an inverted pyramid structure, with your most important headline content up front and detailed information in other tabs." (SV to "up front".) "Avoid internal and horizontal scrolling." (SV.) "limit the number of clicks a user needs to get to the data they want" (SV.) "Two-thirds of users of the ONS website will view content on a mobile device" (SV; undated). "when users hover or select on the chart, it is clear what is being focused on" (SP).
- Examples page names the UKHSA data dashboard, a HeatRisk forecast tool, DfT's Transport Statistics Finder and a local-authority interactive tool (SP). It notes: "Some of the examples in this guidance are not typical of dashboards produced by government analysts." (SP.)
- Role: the nearest thing to an official UK standard for public dashboards. It treats a dashboard as something that needs justifying and that has a retirement stage.

=====================================================================
ITEM 3 — RETIREMENTS AND "PEOPLE DON'T USE IT"

GOV.UK Performance Platform (case)
- What and when: "The Performance Platform was a service provided by the Government Digital Service until March 15 2021. The historical archives will be available from March 18 via the National Archives Government Web Archive. The service provided a central hub for data on the performance of Government Services." (SP; https://www.data.gov.uk/dataset/731b25a8-0462-4a7d-aa3f-5a5d44ae26d2/historical-performance-platform , updated 22 March 2021; gov.uk/performance redirects there.)
- Closure announcement, CDDO Data Standards Authority team, 18 February 2021, https://dataingovernment.blog.gov.uk/2021/02/18/new-guidance-for-publishing-data/ : "GDS is closing 2 of its data services on 16 March 2021." (SP.) "For GOV.UK Performance, we are moving away from the existing platform to a model which sees each department publish service data individually." (SV, with the lead-in.) "This data will be findable through data.gov.uk, and available for download in spreadsheet format." (SP.) The sources disagree on the day (15 or 16 March). No usage figure is given.
- National Audit Office, "Digital transformation in government", HC 1059, 30 March 2017 (nao.org.uk/wp-content/uploads/2017/03/Digital-transformation-in-government.pdf), in the paragraphs the reader numbered 2.9–2.11:
  - "GDS publishes data on 802 government services on an online Performance Platform." (SV.)
  - "But only 118 services publish data on costs per transaction and not all services publish required data on digital take-up, the completion rate for online transactions or user satisfaction." (SP.)
  - "In an internal review in 2015, GDS found that there was a lack of clarity about the purpose of the Performance Platform." (SV.)
  - "Some data have not been updated since March 2016." (SV.)
- GDS's own 2016 re-discovery (blog series, Roxanne Asadi and Tingting Zhao):
  - "In 5 weeks, we visited 14 organisations and spoke to 55 people doing various roles." (SV; 8 June 2016.)
  - Theme 5 heading: "Analysis cannot be automated; data without context is dangerous for decision-making" (SV; 15 June 2016).
  - "The capture of performance metrics that are then immediately available on dashboards is an attractive idea but does not provide the full context and detail that is required for decision making." (SV for the second half.)
  - "The value of a dashboard is in provoking a conversation, to raise awareness of something requiring attention." (SV.)
  - "The Performance Platform has to stop trying to be all things to all people, and become a focused product that meets our primary user's needs." (SV; 16 June 2016.)
- Not found: any published statement that low public use was the reason for closure. The stated record is unclear purpose, stale and incomplete data, and a move to departmental publishing.

UK coronavirus dashboard (case; read as method only)
- UKHSA "What's new", 12 March 2024, "COVID-19 archive data download added to the dashboard": "Following the decommissioning of the COVID-19 in the UK dashboard, you can now download all the historic data on the COVID-19 archive data download page." (SV, apart from an inline link.)
- Archive page, https://ukhsa-dashboard.data.gov.uk/covid-19-archive-data-download : "You can download all the historic data from the decommissioned Coronavirus (COVID-19) in the UK dashboard on this page by clicking the Download all button." (SV.) "The full dataset is 1.4 GB." (SV.) "It has not been possible to fully validate these archived datasets against the latest version of the decommissioned Coronavirus (COVID-19) in the UK dashboard." (SV; my first pass had reshaped this into a phrase that is not on the page.) Zip files are split into Cases, Deaths, Healthcare, Testing and Vaccinations, and the page lists known gaps (SP).
- Stated reasons for decommissioning: not found. The archive practice is a data download with a caveat. It is not a preserved working interface.

Other documented retirements with stated reasons
- US Federal IT Dashboard, https://www.itdashboard.gov/ , open letter from the Federal CIO, undated on the page: "To that end, we are taking steps to sunset this site, eliminating a costly, inefficient process and allowing agencies to focus on higher value activities." (SV.) "Effective April 2026, agencies will pivot to a streamlined state that refocuses on statutorily required data" (SV). Also: "Unfortunately, it does not fully deliver on that promise today." (SP.)
- Johns Hopkins Coronavirus Resource Center, https://coronavirus.jhu.edu/ : "After three years of 24-7 operations, the CRC is ceasing its data collection efforts due to an increasing number of U.S. states slowing their reporting cadences." (SV.) "…the federal government has improved its pandemic data tracking enough to warrant the CRC's exit." (SV.) The data remain in two GitHub repositories (SP).
- COVID Tracking Project, 1 February 2021, https://covidtracking.com/analysis-updates/covid-tracking-project-end-march-7 : "But the work itself—compiling, cleaning, standardizing, and making sense of COVID-19 data from 56 individual states and territories—is properly the work of federal public health agencies." (SV.) "Documentation, analysis, and archival work will continue for another two months, and we will bring the project to a close in May." (SP.)
- Office for Local Government (England): closed 16 December 2024. The Minister's letter says: "Oflog was hampered with a vague and broad remit that risked duplication of functions performed elsewhere." (SP.) The letter does not mention the Data Explorer, so this is weak as a dashboard case.
- Pattern across cases: every stated reason is about the supply side (upstream data drying up, cost, duplication, unclear remit). None cites measured public non-use.

Peer-reviewed study of why public dashboards stop being used: none found. Scottish, Welsh and city cases were not established (statistics.gov.scot shows no notice; StatsWales now redirects to a new beta at stats.gov.wales with no stated reasons).

=====================================================================
ITEM 4 — MOBILE AND RESPONSIVE EVIDENCE

- Brehmer, Lee, Isenberg & Choe 2019, "Visualizing Ranges over Time on Mobile Phones: A Task-Based Crowdsourced Evaluation", TVCG 25(1).
  Source: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/07/ranges_preprint.pdf. Peer-reviewed experiment.
  - "In the first crowdsourced visualization experiment conducted exclusively on mobile phones" (SV). "With results from 87 crowd workers" (SV). Planned N = 100; final counts 40 (temperature) and 47 (sleep) (SP).
  - Linear versus radial layouts at week, month and year granularity; five tasks, from locating a date to comparing ranges (SP).
  - "Averaged across all granularities, participants completed trials between 2.8 and 5.4 seconds with Linear layouts and between 3.3 and 6.9 seconds with Radial ones" (SV). "both layouts generally incurred a similar number of errors" (SP).
  - Role: on a phone the conventional linear layout was faster with no accuracy penalty.
- Brehmer, Lee, Isenberg & Choe 2020, "A Comparative Evaluation of Animation and Small Multiples for Trend Visualization on Mobile Phones", TVCG (VIS 2019).
  Source: https://arxiv.org/pdf/1907.03919.
  - "we conducted an experiment where 96 crowdworker participants performed nine trend comparison tasks" (SV). 113 completed and 17 were excluded (SP). 16 items, animated scatterplot versus a 4×4 small-multiples grid (SP).
  - "those using a small multiples design consistently completed tasks in less time, albeit with slightly less confidence than those using an animated design" (SP, abstract). Accuracy was task-dependent (SP).
  - "When visualizing a multivariate dataset to support trend comparison tasks on a mobile phone display, we advocate for the use of a static small multiples scatterplot with trajectories encoded as trails over an animated scatterplot." (SP.)
- Hoffswell, Li & Liu 2020, "Techniques for Flexible Responsive Visualization Design", CHI.
  Source: https://jhoffswell.github.io/website/resources/papers/2020-ResponsiveVisualization-CHI.pdf. Corpus analysis plus a system; no reader study.
  - "We collected a corpus of 53 news articles gathered from twelve sources, to produce a corpus of 231 visualization examples." (SV.) Sources date from 2014–2019; five journalists were interviewed (SP).
  - "For the landscape orientation, 69 of the visualizations exhibited no changes (29.9%) as opposed to only 6 in the portrait orientation." (SP.)
  - "The most common action in our corpus is to remove content from the mobile visualization." (SV.) "It was also more common to remove elements from the view (87 or 37.7%, portrait orientation) than to add new elements (26 or 11.3%, portrait orientation)." (SP.)
  - "Similar to the visual techniques, many visualizations removed the interactivity completely from the mobile version rather than redesigning the interactive capabilities." (SV.)
  - Proposed techniques (SP): simultaneous cross-device edits, device-specific customisation, cross-device previews, propagation of edits.
- Kim, Rossi, Sarma, Moritz & Hullman 2021, "An Automated Approach to Reasoning About Task-Oriented Insights in Responsive Visualization", TVCG.
  Source: https://arxiv.org/pdf/2107.08141. Modelling paper.
  - "However, transformations can alter relationships or patterns implied by the large screen view, requiring authors to reason carefully about what information to preserve while adjusting their design for the smaller display." (SV.)
  - Three loss measures: identification, comparison, trend (SP).
  - "From the task, we collected human-judged rankings of 1,080 pairs each of which was ranked by three labelers." (SV.) The labellers were the five authors plus four visualisation experts. Random-forest accuracy 84.07 (SV).
  - "A limitation is that our experiment was conducted on desktop devices." (SP.) No reader test.
- Companion: Kim, Moritz & Hullman 2021, "Design Patterns and Trade-Offs in Responsive Visualization for Communication" (EuroVis; https://arxiv.org/pdf/2104.07724).
  - "By comparing the LS and SS views of 378 public facing visualizations, we identify 76 design patterns for responsive visualizations." (SV.)
  - "…the overarching design challenge in responsive visualization is a density-message trade-off where authors seek to balance goals of maintaining graphical density with those of preserving the message or intended takeaways" (SP).
  - "authors often omitted hovering interactions for short labels (E19, E126) or tooltips (E226, E128)…" (SP). "Complex interaction features are often removed, formulated as the pattern Disable X…" (SP.)
- Hover and tooltip reach on touch: I found no measured study. What exists is corpus evidence that authors strip hover on mobile (above) and one standard, WCAG 2.2 SC 1.4.13 Content on Hover or Focus (Level AA), with its Dismissible, Hoverable and Persistent conditions (SP; https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html). The Understanding text has no sentence on devices without hover.
- UK mobile share (one number, measured): StatCounter, "Desktop vs Mobile vs Tablet Market Share in United Kingdom - September 2026": Mobile 53.56%, Desktop 41.78%, Tablet 4.66% (SV; practitioner data, page views). https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/united-kingdom
- Official companion, a different measure (time, not traffic): Ofcom Online Nation 2025 (updated 10 December 2025), p.12: "Smartphones remained the primary device for accessing the internet for UK online adults, accounting for 77% of all time spent online on the average day, up slightly from 75% the previous year." (SV.) Source: Ipsos iris, May 2025, adults 18+.
- The two official ONS-site figures disagree: "Over half" (ONS manual) and "Two-thirds" (Analysis Function). Neither is dated.

=====================================================================
ITEM 5 — THE SIX LANDING PATTERNS AGAINST EVIDENCE

Headline: I found no empirical study that compares landing or entry patterns for data tools head-to-head. There is none on empty states, none on map-first landing, and none on exemplar-first openings that I could reach. What exists bears on single patterns.

- Message-first, with a title as the entry point. Sultanum & Setlur, "Not Always Top-Left: Untangling the Signals that Guide Dashboard Reading Order", IEEE TVCG / VIS 2026 (listed for 9 November 2026).
  Source: https://www.tableau.com/sites/default/files/2026-08/2026-vis-reading-order-cr-preprint_1.pdf (preprint). Peer-reviewed mixed-methods study.
  - "we conducted a mixed-methods study with 18 dashboard authors and 16 end-users" (SV). Eight dashboards; participants ordered components in a "flow specification tool" while thinking aloud (SP).
  - "Most flows began with either the title (42/64, 65.6%) or with adjacent logo → title sequences" "(17/64, 26.6%)" (SV).
  - "Titles, headers, and primary overview components were consistently visited first" (SV).
  - "A comparison between author and user flows showed that author flows tended to be cleaner and more coherent" (SV).
  - Participant on long text: "if the text is too large, I will tend to skip over it" (SV).
  - Limit: "our study relies on self-reported and externally articulated reading sequences rather than direct behavioral measures such as eye tracking" (SV). The sample skews to business users and to first contact (SP).
- Message-first, guidance. ONS: start from a view that "shows the main message without needing any interaction" (SV). Analysis Function: the "inverted pyramid structure" (SV).
- Input-first and select-first, nearest evidence on search as entry. Feng, Deng, Peck & Harrison, "The Effects of Adding Search Functionality to Interactive Visualizations on the Web", CHI 2018 (https://web.cs.wpi.edu/~ltharrison/docs/feng2018effects.pdf).
  - "In total, we recruited 830 participants through Amazon's Mechanical Turk for the study." (SV.) Five visualisations, with search versus without (SP).
  - "In general, a majority of people used text-based search when present in a visualization." (SP.) Adoption ranged 66.7–80.6%, except 32.5% for one visualisation (SP).
  - "the data people looked for while using search was often deeply personal." (SP.)
  - "participants spent significantly more time with data items when search was active, for all conditions except Exoplanets" (SP).
  - Note: here search was added to a display that already showed everything. It does not test a blank-until-input screen.
- Input before content, as prediction. Kim, Reinecke & Hullman, "Explaining the Gap", CHI 2017 (https://mucollective.northwestern.edu/files/2017-ExplainingTheGap-CHI.pdf).
  - "We then recruited 378 participants (42 per condition) from AMT" (SP).
  - "participants who are prompted to reflect on their prior knowledge by predicting and self-explaining data outperform a control group in recall" (SP).
  - "The user is shown the observed data, but with some of the data omitted. The user is prompted to predict the omitted data." (SP.) The authors report that the Predict-Only effect did not replicate (SP).
  - This is an input-first pattern with a measured benefit, but the input is a guess about the data. It is not a location or a setting.
- Exemplar-first and map-first: no study reached. Adjacent only: Peck, Ayuso & El-Etr, CHI 2019 (arXiv 1901.01920; ABSTRACT), 42 interviews on personal relevance.

The two exemplars as they stand on 6 October 2026 (landing structure only)
- ONS "Explore local statistics", https://www.ons.gov.uk/explore-local-statistics/ :
  - Heading "Explore local statistics". Intro: "Find, compare and visualise statistics about places in the United Kingdom." (SV.)
  - A "Find an area" search (SV), with the hint "Search for a postcode, local authority, region, parliamentary constituency or other named area." (SP.)
  - A "Local indicators" card ("Explore 116 indicators, including…", SP), country starting links, and a "Get the data" section.
  - No chart, map or place figure before input (SP, from page text). So it remains input-first, with a browse alternative.
- Our World in Data, https://ourworldindata.org/grapher/life-expectancy :
  - The static page carries the title "Life expectancy" and a rendered chart image, followed by description, sources and citation blocks (SP).
  - The chart's config.json has no "tab" key, has "hasMapTab": true, and "selectedEntityNames": ["World", "Americas", "Europe", "Africa", "Asia", "Oceania"] (SP).
  - So it arrives as a populated chart with authored default entities, and the map is one tab away. I could not observe the live interactive state directly.
- Bonus live case: the UKHSA data dashboard changed its landing twice, with public change notes.
  - 15 October 2024, "Re-designed dashboard homepage": "The homepage's layout is now grouped according to theme. You can now instantly see data for any outbreaks and respiratory viruses." (SP.)
  - 2 July 2026, "Updated landing page": "The landing page now features a Popular Topics section and a complete list of Health Topics that can be filtered and searched." (SP.)
  - Today the first screen shows a hero sentence ("The UKHSA data dashboard shares public health data in a simple, inclusive and accessible way."), summary cards with figures and "Up to [date]" stamps, and a Beta banner (SP).

=====================================================================
ITEM 6 — "NO CONFIGURATION BEFORE MEANING"

- OECD Better Life Index on arrival, https://www.oecdbetterlifeindex.org/ (text view only):
  - Headline "How's life?" with "There is more to life than the cold numbers of GDP and economic statistics" (SP).
  - A "Create your Better Life Index" block: "What is your recipe for a better life — a good education, clean air, nice home, money?", "Rate the topics according to their importance to you" (SP).
  - I could not render the chart, so I cannot confirm whether countries are drawn with default equal weights before any rating, nor any later change to a weighting-first design. The FAQ and About pages were blocked. Treat both as not established.
- Uptake of the configuration step:
  - Designer's account (Moritz Stefaner, https://truth-and-beauty.net/projects/oecd-better-life-index): "With over six million visitors and tens of thousands of indexes shared, the project became a huge success for the OECD…" (SV; practitioner self-report, undated).
  - OECD responses page: "To date, the OECD has received more than 60 000 of these indexes from some 180 countries and territories." (SV.) "Anyone can create their own index, so the results may not represent statistically relevant samples." (SP.)
  - OECD Statistics Working Paper 2018/03 (author shown as Elena Tosetto; ABSTRACT): "…analysing the responses given by close to 130 000 users since 2011 to date." (SV on the landing page.)
  - The 60,000 and 130,000 figures conflict and I could not reconcile them. On either, submitted indexes are of the order of 1–2% of the visitors Stefaner reports. That ratio is my arithmetic across two sources, not a published figure.
- Preference elicitation before content: no peer-reviewed study reached. Practitioner only: NN/g, "Login Walls Stop Users in Their Tracks" (Raluca Budiu, 2 March 2014): "Demanding that users register or log in before they can use an app or see website information has high interaction cost and defies the reciprocity principle." (SP; guidance from usability testing, no n reported.)
- Nearest official statement of the rule is ONS's: interactive charts "hide the main messages from users" (SV), so start from a view that "shows the main message without needing any interaction" (SV).

=====================================================================
UNASKED-FOR FINDINGS

1. Sultanum & Setlur's VIS 2026 reading-order study (item 5) is the most direct evidence I found on what a first screen says first.
2. A census of ordinary dashboards. Srinivasan, Purich, Correll, Battle, Setlur & Crisan, "From Dashboard Zoo to Census: A Case Study with Tableau Public", TVCG 2024 (https://www.tableau.com/sites/default/files/2024-12/Analyzing_Dashboard_Design_in_the_Wild.pdf):
   - "a census of 25,620 dashboards on Tableau Public" (SV).
   - "We found that 19,304 of the 25,620 dashboards in our corpus (75%) were interactive" (SV).
   - "The number of blocks per dashboard ranged from 2 to 267 (median: 8, mode: 4)." (SV.)
   - "53,267 text blocks (21%)" (SV).
   - "many being far simpler than prior research accounts for" (SV).
   - Sample: the top 10% of workbooks by impressions (≥42).
3. Text on dashboards. Sultanum & Setlur, "From Instruction to Insight", VIS 2024 (https://www.tableau.com/sites/default/files/2024-08/textdash-cr-accessibility-checked.pdf):
   - 190 public dashboards and 13 expert interviews.
   - "Title (present in 92% of dashboards in our corpus)" (SV). "Interaction Guidance (58%)" (SV).
   - Heuristic HN1: "Text makes it clear to the user where they need to start interacting with the dashboard." (SP.)
   - Experts split on stating takeaways: "the last thing I want to do is to feed conclusions to the user" (P12, SV). On instructions: "They're really useful, but they're only useful once, right?" (P9, SV.)
4. An official retirement procedure exists. Analysis Function: "Retire your dashboard if it is not being maintained or user feedback indicates that it is no longer: useful; relevant; providing value for money" (SP). A banner "at least six months before retirement" (SP). Archive by preserving the original state, keeping data and metadata with a note that they are no longer updated, and "retaining any code used for the dashboard in a public GitHub repository marked as archived" (SP).
5. ONS's dashboard guidance explicitly drops Few's single-screen rule: "you do not have to fit everything onto one screen" (SV).
6. Setlur, Correll, Satyanarayan & Tory, "Heuristics for Supporting Cooperative Dashboard Design", VIS 2023 (ABSTRACT): 39 heuristics from conversational principles, applied by 52 graduate students. It is a framework. It is not reader evidence.
7. Hoque & Sultanum, "DashGuide", EuroVis 2025: guided tours for first-time dashboard users, evaluated with 12 dashboard creators only. The authors say "we have not formally evaluated DASHGUIDE with them" [end-users] (SP). So onboarding tours remain untested with readers in this source.
8. Quotation discipline caught two reshaped sentences on first pass (the GOV.UK summary-list opening and the UKHSA archive caveat). Both are corrected above.

LEFT OUT, AND WHY
- Unreachable (HAL, ACM, PMC, JMIR, T&F): Boy, Detienne & Fekete 2015 on storytelling and exploration; Kong et al. 2018/2019 on titles and recall; Ivanković et al. 2021 on 158 public COVID dashboards; Kitchin et al. on city dashboards; Dhanoa et al. and Stoiber et al. on onboarding; Blascheck et al. on glanceable displays; the "Mobile Data Visualization" book chapters (no open PDF); recommender cold-start elicitation studies; exemplification theory.
- Not pursued: the Analysis Function "dashboard software" page; learning-analytics and clinical dashboard reviews (wrong setting, and unreachable).
- The reason for the UK coronavirus dashboard's decommissioning and the BLI's default state are reported as not established. I did not infer them.

THREE RICH REFERENCES
1. Sultanum & Setlur 2026, "Not Always Top-Left" — https://www.tableau.com/sites/default/files/2026-08/2026-vis-reading-order-cr-preprint_1.pdf
2. Analysis Function dashboard guidance set (6 February 2026), starting at https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-building-and-managing-dashboards/ , read with ONS's https://service-manual.ons.gov.uk/data-visualisation/guidance/dashboards
3. Bach et al., "Dashboard Design Patterns" — https://arxiv.org/pdf/2205.00757 and https://dashboarddesignpatterns.github.io/ , read with the Tableau Public census as its corrective on typicality.

WHAT SURPRISED ME
- The two UK official bodies that publish dashboard guidance both frame the dashboard as a form to be justified. They use nearly the same sentence about putting the burden of understanding on the user.
- No retirement notice I read cites measured non-use. The reasons given are stale data, cost, duplication and unclear purpose.
- The ONS "10 words" title rule has gone, replaced by 15 words for chart titles and 60 characters for headings.
- "One thing per page" is scoped to forms in its own source, and the page was last updated in 2018.
- For an index whose content is the reader's own weighting, the published numbers imply only about one or two visitors in a hundred ever submitted one.

---

## Agent B — Story and exploration

CHAPTER 11 RESEARCH REPORT — FACET: STORY AND EXPLORATION
Fetched 6 October 2026.

Access and method. WebSearch was unavailable (the turn's shared search budget was already used up), so I worked from direct URLs with WebFetch only. Shell curl was blocked by the proxy (403), so there was no PDF-to-text check. Every "STRING-VERIFIED" below means a second WebFetch pass with a YES/NO presence prompt, most with a false control string that correctly came back NO. "SINGLE PASS" means one reading only. "ABSTRACT" means only the abstract was reachable.

Pages I could not read, and why:
- HAL (inria.hal.science, hal.science, hal.inria.fr): Anubis bot wall.
- dl.acm.org, tandfonline.com, Stasko's Georgia Tech page: 403.
- IEEE Xplore: empty JavaScript shell.
- PubMed: reCAPTCHA.
- Europe PMC API and Crossref API: refused by the fetch proxy (429, "do not fetch again").
- Semantic Scholar and OpenAlex APIs: intermittent 429.
- CiteSeerX: blocklisted.
- pa.media, bbcnewslabs.co.uk, blog.ap.org: "site blocked".
- urbsmedia.com, bongshiny.com, cond.org, danyelfisher.info: robots fetch rate-limited on both attempts.
- vis.berkeley.edu and visualdata.wustl.edu: certificate errors.

Corrections to the brief, up front:
(a) The storytelling null (Boy et al.) could not be read at source. Neither "~4,300 sessions" nor "35.4%" could be verified; neither appears in the abstract.
(b) Kong 2018 and Kong 2019 are by Kong, Liu & Karahalios, not Agrawala.
(c) "4 percentage points" is not on the page of Kim et al. 2017; the figure is 4.08.
(d) "Defaults as procedural rhetoric" is not a sentence in Hullman & Diakopoulos; the phrase "procedural rhetoric" is.
(e) McKenna et al. found no engagement difference between stepper and scroller; the engagement gain came from visuals and animated transitions.

------------------------------------------------------------
ITEM 1. THE TAXONOMY AND ITS EVIDENCE STATUS

1a. Segel & Heer 2010, "Narrative Visualization: Telling Stories with Data", IEEE TVCG 16(6).
Source: http://vis.stanford.edu/files/2010-Narrative-InfoVis.pdf (author copy; the journal header is not printed on it — it shows "Manuscript received 31 March 2010; accepted 1 August 2010").
Type: peer-reviewed design-space analysis (case-study and corpus coding). There is no user study. 2010.
- Corpus: "In total we analyzed 58 visualizations using the case study method illustrated in Section 3. The examples were taken from online journalism (71%), business (20%), and visualization research (9%)." STRING-VERIFIED.
- Genres: "We found that our examples can be characterized by the 7 basic genres shown in Figure 8: magazine style, annotated chart, partitioned poster, flow chart, comic strip, slide show, and film/video/animation." SINGLE PASS (consistent across two readings).
- Axis: "A purely author-driven approach has a strict linear path through the visualization, relies heavily on messaging, and includes no interactivity." STRING-VERIFIED. "A purely reader-driven approach has no prescribed ordering of images, no messaging, and a high degree of interactivity." SINGLE PASS.
- Introduction of the three structures: "Despite the range of possible combinations, a few hybrid models have become most common. Below we discuss three common schemas." SINGLE PASS.
- Martini glass:
  - "The Martini Glass visualization structure begins with an author-driven approach, initially using questions, observations, or written articles to introduce the visualization." SINGLE PASS (two consistent readings).
  - "Occasionally no text is used at all, as the visualization instead relies on an interesting default view or annotations." STRING-VERIFIED.
  - "Once the author's intended narrative is complete, the visualization opens up to a reader-driven stage where the user is free to interactively explore the data." STRING-VERIFIED.
  - "This structure is the most common across the interactive visualizations we examined." STRING-VERIFIED (it sits in the Martini Glass paragraph).
- Interactive slideshow: "The Interactive Slideshow structure follows a typical slideshow format, but incorporates interaction mid-narrative within the confines of each slide." SINGLE PASS (two consistent readings).
- Drill-down: "The Drill-Down Story visualization structure presents a general theme and then allows the user to choose among particular instances of that theme to reveal additional details and backstories." SINGLE PASS (two consistent readings). Also: "Nevertheless, it still requires significant amounts of authoring to determine the possible types of user interaction, what candidate stories to include, and the details included for each story." SINGLE PASS.
- The authors on the missing reader evidence:
  - "By investigating the narrative devices used in a corpus of visualizations, our analysis has focused primarily on the design decisions made by visualization creators. A promising direction for future research is to focus squarely on readers' experiences when viewing and interacting with narrative visualizations." Second sentence STRING-VERIFIED.
  - "How do such behaviors apply to visualization?" STRING-VERIFIED.
  - "Further research is needed to characterize how readers perceive narratives presented via visualizations." STRING-VERIFIED.
  - "However, we must acknowledge that we are not experts in the study of narrative." STRING-VERIFIED.
  - The control string claiming a 120-participant user study returned NO.
- The phrase "reader-centric" was not found by the reader; do not attribute it to the paper.
Role: the taxonomy every later paper inherits. By its authors' own account it is a description of designers' choices, not evidence about readers.

1b. Hullman & Diakopoulos 2011, "Visualization Rhetoric: Framing Effects in Narrative Visualization", IEEE TVCG 17(12), December 2011, pp. 2231–2240 (header read from the copy).
Source: https://users.eecs.northwestern.edu/~jhullman/vis_rhetoric.pdf
Type: peer-reviewed analytical framework (qualitative coding). No user study.
- Definition: "We use the term rhetoric to refer to the set of processes by which intended meanings are represented in the visualization via a designer's choices and then shaped by individual end-user characteristics, contextual factors involving societal or cultural codes, and the end-user's interaction." STRING-VERIFIED.
- Layers: "We distinguish between four editorial layers that can be used to convey meaning, including the data, visual representation, textual annotations, and interactivity." STRING-VERIFIED.
- Sample: "We gathered a sample of fifty-one professionally-produced narrative visualizations, many from international news outlets like the New York Times (NYT) or BBC." STRING-VERIFIED.
- Categories: "information access rhetoric functioning to limit the amount of information presented, provenance rhetoric functioning to provide background information, mapping rhetoric functioning to map elements of the visualization to non-explicit concepts, and procedural rhetoric functioning to constrain interaction over time". SINGLE PASS (two consistent readings). A fifth cluster originates in linguistic rhetoric.
- "Procedural rhetoric" does exist, as a category citing Bogost: "Procedural rhetoric is based in an artifact's procedural mode of representation, in other words, the expression of meanings through rule-based representations and interactive functions". SINGLE PASS (returned twice).
- "defaults are a form of procedural rhetoric" is NOT a sentence in the paper (checked: NO). What exists, inside the procedural-rhetoric section under "anchoring": "Default views provide an initial point of interpretation anchored to the default visual configuration." STRING-VERIFIED. Also: "Anchoring techniques primarily direct a user's attention in a way that subsequently helps convey a message." SINGLE PASS.
- On evidence status: "Applying a similar experimental approach to narrative visualizations is a natural parallel. Our work sets the stage for such studies by providing a taxonomy of specific information presentation manipulations used in narrative visualizations." SINGLE PASS.
Role: supplies the vocabulary for saying how a display argues. Its "provenance rhetoric" section is used under Item 7.

1c. Hullman, Drucker, Riche, Lee, Fisher & Adar 2013, "A Deeper Understanding of Sequence in Narrative Visualization", IEEE TVCG 19(12), pp. 2406–2415. ABSTRACT ONLY, and only as OpenAlex's word index reassembled by the reader, so the wording is approximate. Quote nothing from it.
- What the index supports: a qualitative analysis of 42 narrative visualizations (the token "42" is present); a graph-driven approach that ranks visualization-to-visualization transitions by a cost "from the audience perspective"; validating studies; and results including a relative ranking of transition types and "support for memory and subjective rating benefits" of "parallelism as a structural device".
- The n of the user studies was not reachable. Four author-copy guesses failed.

1d. Scope only.
- Riche, Hurter, Diakopoulos & Carpendale (eds.) 2018, Data-Driven Storytelling (Routledge/CRC, 28 March 2018, 314 pp.; publisher page, SINGLE PASS). Description: "Resulting from unique discussions between data visualization researchers and data journalists, it offers an integrated definition of the topic, presents vivid examples and patterns for data storytelling, and calls out key challenges and new opportunities for researchers and practitioners."
- Chapters relevant here: ch. 3 "Exploration and Explanation in Data-Driven Storytelling" (Thudt, Gschwandtner, Walny, Dykes, Stasko); ch. 4 Stolper, Lee, Riche & Stasko, "Data-Driven Storytelling Techniques: Analysis of a Curated Collection of Visual Stories"; ch. 5 Bach et al., narrative design patterns; ch. 11 Amini et al., "Evaluating Data-Driven Stories & Storytelling Tools".
- The Stolper 2016 technical report was unreachable (404/403). It is a content analysis, not an evaluation.

------------------------------------------------------------
ITEM 2. THE STORYTELLING NULL

Boy, Détienne & Fekete 2015, CHI 2015, DOI 10.1145/2702123.2702452. FULL TEXT UNREACHABLE. I tried HAL at four URLs, the ACM page, Fekete's and Aviz's publication pages (they list only 2018 onward and 2024 onward), CORE, and Semantic Scholar. This is well past two attempts, and I stopped.
- ABSTRACT only, reassembled from OpenAlex's word index; approximate, not string-verified, so do not quote it. It supports: "three web-based field experiments"; evaluating the impact of "initial narrative visualization techniques and storytelling on user-engagement with exploratory information visualizations"; run at a popular news and opinion outlet; and, "In contrast to our hypotheses", that augmenting the visualizations with introductory "stories" "does not seem to increase user-engagement in exploration". The tokens "three", "web-based", "field", "does", "not", "seem", "increase" and "user-engagement" are confirmed present in the index.
- Semantic Scholar's machine summary (not the authors' words) says the same.
- Per-experiment n, conditions, measures, and the 35.4% who followed the authored sequence: NOT VERIFIED. The tokens "4,300", "sessions" and "35.4%" are not in the abstract index.
- Recommendation: carry version 1's numbers only with a flag, or have someone with ACM or HAL access check them.

Secondary descriptions I could verify (each is another paper describing Boy et al.):
- Conlen, Kale & Heer 2019 (https://idl.cs.washington.edu/files/2019-IdyllAnalytics-EuroVis.pdf): "Boy et al. [BDF15] present a case study examining the effect of the presence of narrative text on users' engagement with visualizations in the wild." SINGLE PASS.
- McKenna et al. 2017: "For steppers, Boy et al. showed that readers engage with all sections on a page but that this may not occur linearly [BDF15], whereas scrolling linearly confines navigation." SINGLE PASS.
- Schröder et al. 2023 systematic review (arXiv 2312.01164): "It is important to note, however, that some studies have found no impact on engagement when combining storytelling visualizations with exploratory data analysis [23]." STRING-VERIFIED. The reference list was cut off, so [23] is not confirmed to be Boy et al.

------------------------------------------------------------
ITEM 3. LINKING TEXT AND CHART; TITLES; PREDICTION

3a. Zhi, Ottley & Metoyer 2019, "Linking and Layout", Computer Graphics Forum (EuroVis), DOI 10.1111/cgf.13719. ABSTRACT only, read at the Eurographics Digital Library (https://diglib.eg.org/handle/10.1111/cgf13719). All STRING-VERIFIED.
- Design: "(i) different text and visualization spatial arrangements (layout), namely, vertical and slideshow; and (ii) interactive linking of text and visualization (linking)."
- "Here, linking refers to a bidirectional interaction mode that explicitly highlights the explanatory visualization element when selecting narrative text and vice versa."
- "Through a crowdsourced study with 180 participants, we measured the effect of layout and linking on the degree to which users engage with the story (user engagement), their understanding of the story content (comprehension), and their ability to recall the story information (recall)."
- "We found that participants performed significantly better in comprehension tasks with the slideshow layout."
- "Participant recall was better with the slideshow layout under conditions with linking versus no linking."
- "We also found that linking significantly increased user engagement."
- "Additionally, linking and the slideshow layout were preferred by the participants."
- Caution: the recall sentence is an interaction (slideshow, with linking versus without), not a main effect of linking. The strings "Recall was significantly increased" and "linking significantly increased recall" returned NO.
- Per-cell n, statistics and effect sizes were not reachable.
Type: peer-reviewed crowdsourced experiment, 2019.

3b. Kong, Liu & Karahalios 2018, "Frames and Slants in Titles of Visualizations on Controversial Topics", CHI 2018.
Source: https://www.hidykong.com/papers/Kong-CHI18.pdf
- Two studies on Qualtrics panels matched to US demographics. Study 1 (title writing): "We began by recruiting 100 participants; 11 participants were added to meet the goal of a nationally representative sample." Study 2 (title effect): "resulting in 104 survey responses in total." Both SINGLE PASS (returned on the verification pass).
- "the slant of the title influenced the perceived main message of a visualization" and "with viewers deriving opposing messages from the same visualization". STRING-VERIFIED.
- "The slant of visualization titles resulted in a significant difference in the perceived main message (χ² = 27.06, df = 2, p < 0.001)." STRING-VERIFIED on 27.06.
- "viewing visualizations with slanted titles did not result in a statistically significant attitude change overall". STRING-VERIFIED. The abstract: "The results did not show any significant effect on attitude change."
- "a majority of the participants reported the information as being neutral. Similar ratios of participants answered that the information was neutral whether they saw an attitude-consistent (80%), attitude-inconsistent(80%), or attitude-irrelevant (89%) visualization". SINGLE PASS.
- Abstract: "we highlight the danger of subtle statistics frames and viewers' unwarranted conviction of the neutrality of visualizations." SINGLE PASS.

3c. Kong, Liu & Karahalios 2019, "Trust and Recall of Information across Varying Degrees of Title-Visualization Misalignment", CHI 2019.
Source: https://www.hidykong.com/papers/Kong-CHI19-titles.pdf
- "We conducted the survey on Qualtrics and recruited 100 participants per condition." Two conditions, miscued slant and contradictory slant, so about 200 in all (the total is a first-pass figure).
- "people's recall of the visualization's message more frequently aligned with the titles than the visualization." STRING-VERIFIED.
- "the number of the recalled messages that aligned with the message of the titles (133 out of 398) was still greater than the number of messages that aligned with the message in the visualization". STRING-VERIFIED on 133 out of 398. A first-pass figure of 68 aligned with the visualization is unverified.
- "visualizations were persistently perceived as impartial by the majority." STRING-VERIFIED. "the majority of the people (72-87%) in all conditions reported that the information was neutral." SINGLE PASS.
- On trust: "Data, visualization, and title were all seen as less credible when there was a bigger visualization-title misalignment". This was returned as the closest sentence to my candidate, so the wording is the paper's but treat it as SINGLE PASS.
- So misaligned titles were not simply trusted: credibility ratings fell as misalignment grew, yet most readers still called the information neutral and recalled the title's message.

3d. Kim, Reinecke & Hullman 2017, "Explaining the Gap: Visualizing One's Predictions Improves Recall and Comprehension of Data", CHI 2017.
Sources: https://idl.cs.washington.edu/files/2017-ExplainingTheGap-CHI.pdf and https://users.eecs.northwestern.edu/~jhullman/explaining_the_gap.pdf
- "We then recruited 378 participants (42 per condition) from AMT, rewarding their participation with $1.50." STRING-VERIFIED.
- Nine conditions, first-pass list: None, Explain-Only, Predict-Explain and Predict-Only in each of Vis and Text, plus Predict-Feedback-Vis.
- Abstract: "We find that participants who are prompted to reflect on their prior knowledge by predicting and self-explaining data outperform a control group in recall and comprehension." STRING-VERIFIED.
- Recall task: "participants in all conditions were asked to recall the percentage of voters of different ethnicities". SINGLE PASS. Absolute error is the absolute difference between recalled and observed value.
- Main effect: "The Predict-Explain-Vis condition had the lowest absolute error relative to the None-Vis condition by -4.08 (i.e., participants in the Predict-Explain-Vis condition were, on any given recalled point out of the 12 total, more accurate at recalling the voting percentage by 4.08% out of 100% compared to the those in the None-Vis condition: t = −4.02, p < .0001)". STRING-VERIFIED on the "4.08% out of 100%" fragment.
- "4 percentage points" is NOT on the page (checked: NO). The correct figure is 4.08, expressed as "4.08% out of 100%". The only "percentage points" phrase is a different comparison, by modality: "Overall, we observed 3.76 percentage points (36%) more errors on average per recalled value among visual conditions compared to text." STRING-VERIFIED.
- Other visual conditions on the main (voting) dataset, SINGLE PASS: Predict-Feedback-Vis −3.54; Explain-Only-Vis −3.52; Predict-Only-Vis −2.30 (t = −2.25, p < .05).
- Text modality: "The Explain-Only-Text condition was the only condition that led to lower absolute errors than the None-Text condition". STRING-VERIFIED.
- Familiarity replications (visual conditions only; their n was not found):
  - Low familiarity (a mouse blood-glucose experiment): "The Explain-Only-Vis condition had lower errors by 1.78 (t = −3.75, p < .001), and the Predict-Explain-Vis conditions had lower errors than the None condition by 1.27 (t = −2.62, p < .01)." SINGLE PASS. "Predict-Only-Vis condition had no effect compared to the None condition (t = −1.43, p = .152)." Returned on the verification pass, where the reader attributed it to the low-familiarity dataset.
  - High familiarity (fast-food calories): "Results of the mixed effect model for absolute error (Fig. 7(b)) and trend error indicate no differences between any conditions for the fast food dataset." Returned on two passes.
- The authors' explanation: "One possible reason that we did not see an effect here is that participants were already relatively accurate in estimating the values, such that the initial 'gap' is too small to see much positive impact from the elicitation techniques." SINGLE PASS.
- So: Predict-Only helped modestly on the main dataset and not on the low-familiarity one; nothing helped on the highly familiar one; in text only self-explanation helped.

3e. Kim, Reinecke & Hullman 2018, "Data Through Others' Eyes": unreachable (two guessed URLs 404). Nothing quoted.

------------------------------------------------------------
ITEM 4. SCROLLYTELLING'S EVALUATIONS

4a. McKenna et al. 2017, re-read because it bears on the summary in hand.
Sources: https://vdl.sci.utah.edu/publications/2017_eurovis_narrative-flow/ and https://sci.utah.edu/~vdl/papers/2017_eurovis_narrative-flow.pdf
- Abstract: "Our results indicate that visuals and navigation feedback (e.g., static vs. animated transitions) have an impact on readers' engagement, while level of control (e.g., discrete vs. continuous) may not." SINGLE PASS on the landing page.
- "Regarding the stepper versus scroller debate, we did not find a significant difference in engagement via our questionnaire, failing to support H3." STRING-VERIFIED.
- "Overall, participants comprehended the story well, scoring on average 4 out of 5. We did not find any major differences in comprehension across condition pairs." SINGLE PASS.
- "In total, 240 participants read through the story". STRING-VERIFIED.
- Limitations: "this could be localized to this particular story". SINGLE PASS.
- So "engagement up" belongs to visuals and animated transitions, not to scrolling as against stepping.

4b. Schneiders 2020, "What Remains in Mind? Effectiveness and Efficiency of Explainers at Conveying Information", Media and Communication 8(1), 218–231. Open access: https://www.cogitatiopress.com/mediaandcommunication/article/view/2507
Type: peer-reviewed between-subjects online experiment. This is the one controlled recall test of a format called scrollytelling that I could reach.
- "I conducted an experimental online survey (N = 381) with medium as the independent variable (explainer text vs. audio vs. video vs. scrollytelling) and the recall of information as the dependent variable." STRING-VERIFIED.
- "the results show that scrollytelling and video lead to a significantly more extensive recall than audio and in part text media. However, when considering exposure time, text turns out to be the most efficient medium." STRING-VERIFIED in fragments.
- Detail, SINGLE PASS:
  - Mean recall: video .66, scrollytelling .65, text .61, audio .59.
  - "the medium exerted a significant influence on the recall of information (F(3, 358) = 2.87, p < .05)".
  - Exposure: text 275 s, audio 312 s, video 335 s, scrollytelling 355 s; efficiency index text 100, video 89, audio 84, scrollytelling 81.
  - "text conveys significantly more information than audio, video and scrollytelling in the same amount of time".
- Stimulus: "The scrollytelling contribution was created using the digital storytelling tool Pageflow. It consisted of a 529-word text interrupted by an information graphic and three video clips". So it is a multimedia longform, not a chart-driven scroller.
- Sample: German, recruited largely through social networks, 75% female, immediate recall, one topic. The author lists these as limits.

4c. Hohman, Conlen, Heer & Chau 2020, "Communicating with Interactive Articles", Distill, 11 September 2020. https://distill.pub/2020/communicating-with-interactive-articles/
Type: review and position article in a peer-reviewed venue.
- "They have been shown to be more engaging, can help improve recall and learning, and attract broad readership and acclaim". STRING-VERIFIED.
- "There is limited empirical evaluation of the effectiveness of interactive articles." STRING-VERIFIED. It continues: "The problem is exacerbated by the fact that large publishers are unwilling to share internal metrics, and laboratory studies may not generalize to real world reading trends." (sentence verified as the closest match).
- "The New York Times provided one of the few available data points, stating that only a fraction of readers interact with non-static content, and suggested that designers should move away from interactivity." STRING-VERIFIED.
- "However, other research found that many readers, even those on mobile devices, are interested in utilizing interactivity when it is a core part of the article's message." STRING-VERIFIED.
- "This means designers are potentially choosing a suboptimal presentation of their story due to this anecdote." STRING-VERIFIED.
- "More research is needed in order to identify the cases in which interactivity is worth the cost of creation." STRING-VERIFIED.
- On McKenna: "McKenna et al. found that their study participants largely preferred content to be displayed with a step- or scroll-based navigation as opposed to traditional static articles, but did not find a significant difference in engagement between the two layouts." STRING-VERIFIED.
- "In the worst case, interactivity may be distracting to readers or the functionality may go unused, the author having wasted their time implementing it." (closest-match wording). "It is also important to remember that not everything needs to be interactive." STRING-VERIFIED.
- "The act of creating a successful interactive article is closer to building a website than writing a blog post." STRING-VERIFIED.
- It does not cite Boy et al. 2015.

4d. Practitioner admission. The Pudding, Russell Samora, "Responsive scrollytelling best practices", April 2017, https://pudding.cool/process/responsive-scrollytelling/ : "Whether scrollytelling increases interest and comprehension is up for debate, but it doesn't hide content." STRING-VERIFIED.

4e. Absence, stated plainly.
- I found no published newsroom A/B test of scrollytelling against another format for comprehension. NYT, Guardian and FT sites could not be searched or are blocked. Hohman et al.'s sentence about publishers not sharing metrics is the citable statement of that gap.
- Seyser & Zeiller 2018 (IEEE iV): unreachable; nothing quoted.
- Amabili 2019 (Nightingale on Medium): a practitioner essay, member-only, with no evaluation in the reachable part.
- I could not identify or reach a "Zhao, Marr & Elmqvist" scrollytelling evaluation.
- Tjärnhage et al. 2023, "The Impact of Scrollytelling on the Reading Experience of Long-Form Journalism", is a title I know of but could not locate or verify; treat it as an unverified lead.
- Schröder et al. 2023, "Telling stories with data – A systematic review" (arXiv 2312.01164; "This stage resulted in 184 remaining publications.", STRING-VERIFIED) describes scrollytelling as a genre and reports no evaluation of it. It also says "As a consequence, field experiments are rare [30, 204]." STRING-VERIFIED.

------------------------------------------------------------
ITEM 5. INTERACTIVITY STAYS OPTIONAL

Bret Victor, "Explorable Explanations", dated March 10, 2011 on the page (a February 2024 postscript is also present). https://worrydream.com/ExplorableExplanations/
Type: practitioner essay. All STRING-VERIFIED.
- "Like the proposition example earlier, the filter description works as a static explanation -- it can be read like normal text. The reader is not forced to interact in order to learn. The reader interacts if they wants to go deeper, if they have piqued curiosity or unanswered questions." ("forced" is italic in the original; "they wants" is as the page now reads.)
- "There are no UI elements screaming for attention. The reader is not transported off to a separate "interactive" context. Instead, the reader simply nudges the examples that the author has already presented."
- "An active reader asks questions, considers alternatives, questions assumptions, and even questions the trustworthiness of the author."
- "Up and Down the Ladder of Abstraction" (https://worrydream.com/LadderOfAbstraction/): the reader found no sentence about optional interaction (SINGLE PASS). Nothing quoted.

------------------------------------------------------------
ITEM 6. AUTOMATED WRITTEN NARRATIVE AT SCALE, AS METHOD

6a. ONS Census 2021 local articles. The ONS's own account: Daniel Wainwright, "Semi-automation and Census 2021: how we told 331 local stories in one go", ONS Digital blog, 27 January 2023. https://digitalblog.ons.gov.uk/2023/01/27/semi-automation-and-census-2021-how-we-told-331-local-stories-in-one-go/
Type: producer's case account. Read for method only.
- The version 1 quotation is confirmed, in the author's own voice: "Interactive maps, charts and dashboard are all wonderful ways of communicating data, but we need to pull out the narrative and the story to help guide our users through the numbers." STRING-VERIFIED.
- "Theo Jolliffe and Tim Kershaw created 331 individual pages – one for each local authority area of England and Wales." STRING-VERIFIED.
- "Each article was different according to what the data told us. This was no 'fill in the blanks' exercise. The story would highlight notable differences in the area compared with others." STRING-VERIFIED.
- "Checking the articles took time and care from the Census Outputs team and our content designers." STRING-VERIFIED.
- "Semi-automation is not a labour-saving tool. It doesn't mean we can do things more quickly. It means we can do things we never could before." STRING-VERIFIED.
- "Within a few days of publication in December 2022, every individual area's page had been read." STRING-VERIFIED.
- "This built on our previous automation on local health by taking the 'robo-journalism' out of an embedded tool." SINGLE PASS.
- Tools named: "Combining analysis in Python, front end development in Svelte, data visualisation in d3.js and old-fashioned journalism". SINGLE PASS.
- The post gives no thresholds or rule list.

The on-page disclosure, under the heading "About these articles" (https://www.ons.gov.uk/visualisations/censusareachanges/; index page only, no place read). All STRING-VERIFIED.
- "The articles have been written and semi-automated by our data journalists and are a new publishing format for the Office for National Statistics."
- "Topics are chosen and ordered automatically based on how relevant they are for each area, however all data are checked before publishing."
- "There is an article like this for every local authority district in England and Wales."

The tooling, from the ONSvisual GitHub READMEs.
- robo-utils (https://github.com/ONSvisual/robo-utils): "A library of utilities to make Natural Language Generation (NLG) for semi-automated journalism a bit easier." STRING-VERIFIED. It renders Pug templates "into structured JSON for each place". It has helper functions that turn numbers into phrases (approximations, described changes, ranks, fractions, lists). SINGLE PASS on the function list. No mention of large language models (checked: NO).
- robo-article (https://github.com/ONSvisual/robo-article): "A Svelte Kit template for creating semi-automated journalism (AKA 'robo-journalism') content on a standard article page", built from Pug templates and wide-format CSV. SINGLE PASS.
- So the method is rule-and-template generation from a table, with human checking.

6b. Associated Press earnings reports and the general method. Source: Andreas Graefe, Guide to Automated Journalism, Tow Center, published at CJR January 2016. https://www.cjr.org/tow_center_reports/guide_to_automated_journalism.php
Type: research-institute report. The AP's own blog was blocked.
- Method: "First, the software collects available data...Second, algorithms employ statistical methods to identify important and interesting events in the data...Third, the software classifies and prioritizes the identified insights by importance and, fourth, arranges the newsworthy elements by following predefined rules to generate a narrative." SINGLE PASS; the ellipses are the reader's.
- Conditions: "Automated journalism works for fact-based stories for which clean, structured, and reliable data are available." Returned as the true sentence on the verification pass.
- "the automation allowed for the generation of more than 3,000 stories per quarter, compared to about three hundred stories that AP reporters and editors previously created manually." STRING-VERIFIED.
- "Lou Ferrara, former vice president and managing editor for entertainment, sports, and interactive media at the Associated Press, reports that automation has decreased the rate of errors in AP's company earning reports from about seven percent to only about one percent, mostly by eliminating typos or transposed digits." STRING-VERIFIED. This is the source reporting an AP executive's claim.
- Error handling: "A prominent example is a July 2015 report about Netflix's second-quarter earnings. This article, which was later corrected, wrongly reported that the company missed expectations and that the share price had fallen by seventy-one percent since the beginning of the year when, in fact, it had more than doubled during that period. The reason for the error was that the algorithm failed to realize that the Netflix stock underwent a seven-to-one split." SINGLE PASS (returned on the verification pass).
- Disclosure line the AP used: "This story was generated by Automated Insights using data from Zacks Investment Research." (the page continues with a link sentence).
- Limits: "Algorithms cannot ask questions, explain new phenomena, or establish causality and are thus limited in their ability to observe society and to fulfill journalistic tasks, such as orientation and public opinion formation." STRING-VERIFIED.
- Templates: "trained journalists pre-write text modules and sample stories with the appropriate frames and language and adjust them to the official style guide of the publishing outlet." SINGLE PASS.

6c. RADAR (PA Media and Urbs Media) and BBC News Labs' Salco: unreachable (site blocked; robots fetch rate-limited twice). Nothing quoted.
Statistics Netherlands, Statistics Norway, Eurostat and the Bank of England: without search I could not locate any account of text generation; I cannot say whether one exists.

6d. Readers' perceptions of automated news text.
Graefe & Bohlken 2020, "Automated Journalism: A Meta-Analysis of Readers' Perceptions of Human-Written in Comparison to Automated News", Media and Communication 8(3), 50–59, DOI 10.17645/mac.v8i3.3019. https://www.cogitatiopress.com/mediaandcommunication/article/view/3019
Type: peer-reviewed meta-analysis.
- "based on experimental and descriptive evidence from 12 studies with a total of 4,473 participants, showed no difference in readers' perceptions of credibility, a small advantage for human-written news in terms of quality, and a huge advantage for human-written news with respect to readability." STRING-VERIFIED in three fragments.
- "Experimental comparisons further suggest that participants provided higher ratings for credibility, quality, and readability simply when they were told that they were reading a human-written article." SINGLE PASS.
- Effect sizes, SINGLE PASS: "credibility (d = 0.0; SE = 0.02), quality (d = 0.5; SE = 0.03), readability (d = 2.8; SE = 0.04)".
- On declared source, SINGLE PASS: "While experimental evidence showed a medium-sized effect in favor of human-written news (d = 0.5; SE = 0.04), descriptive evidence revealed a small effect in favor of automated news (d = −0.3; SE = 0.08)."
- Its study table (SINGLE PASS, and the reader's listing was incomplete) includes Wölker & Powell (N = 300, sports and finance, credibility), Haim & Graefe 2017 (N = 313) and Jung et al. 2017 (N = 400).
- The texts were short, routine, data-driven stories (sport, finance). None tested statistical-area narratives.

The primary studies, as the Tow guide describes them (the papers themselves are paywalled):
- "Clerwall presented forty-six Swedish undergraduates in media and communication studies with an article that provided a recap of an American football game."
- Graefe et al.: "This study used a larger sample of nine hundred and eighty-six participants, also varying the actual article source and its declared source."
- Both returned on the verification pass.
- The guide's summary: "people rate automated news as more credible than human-written news but do not particularly enjoy reading automated content". SINGLE PASS. The later meta-analysis moved credibility to no difference.

------------------------------------------------------------
ITEM 7. STATING THE DISPLAY'S RHETORIC

Precedents, each organisation in its own words.
- Our World in Data FAQs (https://ourworldindata.org/faqs). All STRING-VERIFIED.
  - "In every chart, we clearly indicate the source of the data being shown."
  - "We also indicate whenever we have combined data sources or made changes to the original datasets (such as regional aggregations, per capita transformations, etc.)."
  - "Citation instructions for all data on our site can be found by clicking 'Learn more about this data' at the bottom of our interactive charts, and at the bottom of our pages dedicated to specific data indicators."
  - The citation form ends "– processed by Our World in Data".
- Our World in Data, Boukarim, Swinehart & Mersmann, "Redesigning our interactive data visualizations", 18 October 2023 (https://ourworldindata.org/redesigning-our-interactive-data-visualizations). All STRING-VERIFIED.
  - "In each of our visualizations, the source of the data is always displayed prominently."
  - "Clicking 'Learn more about this data' shows an overlay with more in-depth information."
  - The stated reason is credit to producers: "For this to continue, these individuals and institutions must receive the recognition they need to continue their essential work."
  - The one "default" sentence found: "Maps typically show the entire world by default but can be focused on particular regions using the menu in their upper right corner."
- I did NOT find a "charter sentence about defaults" on the About, FAQs or redesign pages, and the exact panel label "Sources and processing" was not on the redesign page (checked: NO). If version 1 used either, re-source it.
- The Markup (https://themarkup.org/about). All STRING-VERIFIED.
  - "Our approach is scientific: We build datasets from scratch, bulletproof our reporting, and show our work. We call this The Markup Method."
  - "Whenever possible, we will publish the underlying datasets and code that we use in our investigations, as well as a detailed methodology describing the data, its provenance and the statistical techniques used in our analysis."
  - "We invite academics, journalists, policymakers, consumer activists, and community organizers to engage with our findings—after all, this is for you."
- ONS Quality and Methodology Information (last updated 28 January 2016): "Quality and methodology information reports are overview notes designed to give you information on the strength and limitations of the data and to allow you to decide what the data are suitable to be used for." STRING-VERIFIED. Tied on that page to the code of practice requirement that "users are informed about the quality of statistical outputs". https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/qualityinofficialstatistics/qualityandmethodologyinformation
- The ONS "About these articles" panel (Item 6a) is a precedent for a display saying how it was composed.
- ProPublica Nerd Blog strapline: "How we make stuff. Secrets for data journalists, developers, newsroom designers, engagement specialists, and more." SINGLE PASS. It is addressed to practitioners, not readers.
- The Pudding's About page carries no statement about publishing method (SINGLE PASS).
- FT, Guardian and NYT method-note conventions could not be read (news sites blocked or unsearchable).

Scholarly grounding for doing this.
- Hullman & Diakopoulos 2011, section 3.2.3 "Provenance Rhetoric":
  - "A number of visualization rhetoric techniques observed in our sample work to signal the transparency and trustworthiness of the presentation source to end-users." STRING-VERIFIED on the fragment.
  - "Data provenance strategies include citing and/or linking data sources, additional references, methodological choices, and relevant facts, as well as annotating exceptions and corrections, thus achieving goals proposed by Tufte for graph provenance." STRING-VERIFIED on the first clause.
  - On uncertainty: "yet appeared more often in our sample via textual means". STRING-VERIFIED.
  - Note the framing: the paper treats source notes as themselves rhetoric.
- Dörk, Feng, Collins & Carpendale 2013, "Critical InfoVis: Exploring the Politics of Visualization", CHI 2013 Extended Abstracts (alt.chi). https://mariandoerk.de/criticalinfovis/altchi2013.pdf. Conceptual, no study ("We have derived these principles by synthesizing values advocated by critical approaches in related domains and recent developments in visualization.").
  - The Disclosure principle: "Creating visualizations involves a range of decisions about data, representation, and interaction. Disclosing some of these decisions is a way to establish trust between visualization creators and viewers. When the designer's intentions and decisions are concealed, it is difficult to trust a visualization and engage with the presented issue." Second sentence STRING-VERIFIED; the paragraph SINGLE PASS.
  - Plurality: "exposing multiple facets and enabling a variety of interpretations is preferable to limited views and singular readings". STRING-VERIFIED.

Does stating method change trust?
- Burns, Lee, On, Xiong, Peck & Mahyar, "From Invisible to Visible: Impacts of Metadata in Communicative Data Visualization". Author copy https://cyxiong.com/wp-content/uploads/2022/12/impactsMetadata.pdf (LaTeX template header; the venue is not printed; work dated about 2022). Two crowdsourced experiments on Prolific (platform is first-pass).
  - "We presented 64 participants with four real-world visualizations"; "We asked 144 participants to explain the main message of two pairs of visualizations". Both returned on the verification pass.
  - "visualizations with metadata were perceived as more thorough than those without metadata, but similarly relevant, accurate, clear, and complete." STRING-VERIFIED.
  - "metadata did not impact the accuracy of the information extracted from visualizations, but may have influenced which information participants remembered as important or interesting." SINGLE PASS.
  - "participants assigned higher probabilities that visualizations with metadata were chosen for a presentation to policymakers." SINGLE PASS. A first-pass figure of 53% versus 47%, p = 0.004, is unverified.
  - "metadata significantly increased trust" is not in the paper (checked: NO).
  - Six metadata kinds were tested (first pass): data source, cleaning and processing, perceptual challenges, encoding explanation, creators, intended audience.
- Peck, Ayuso & El-Etr 2019, "Data is Personal", CHI 2019, arXiv 1901.01920.
  - "In 42 semistructured interviews in rural Pennsylvania (USA), we find that a complex set of factors intermix to inform attitudes and perceptions about data visualization". STRING-VERIFIED.
  - Participants ranked ten charts, then the sources were shown. "17 of 42 participants changed their rankings after the sources of the data visualizations were revealed." STRING-VERIFIED.
  - "However, once the source was revealed, 8 out of 17 participants ranked them higher." STRING-VERIFIED. This concerns a government-source chart first judged crude.
  - Sites: university staff (13), a construction site (5), a farmers market (24). SINGLE PASS.
  - Caveat in their words: "we must consider how political biases and beliefs may negate the impact of even the most lauded institutions for data visualization design and implementation". SINGLE PASS.
- Xiong, Padilla, Grayson & Franconeri 2019, "Examining the Components of Trust in Map-Based Visualizations" (EuroVis TrustVis workshop; preliminary). Author copy via cyxiong.com.
  - "77 participants were recruited from Amazon's Mechanical Turk". SINGLE PASS.
  - "perceived clarity, amount of disclosure, and thoroughness significantly predicted individuals' selection of a Google Maps-like application with either less information or more information." STRING-VERIFIED on the fragment.
  - "Trust and perceived accuracy did not significantly predict which navigation application visualization participants decided to use." SINGLE PASS.
  - "an individual's ratings of accuracy and disclosure of a visualization predicted their ratings of the trustworthiness of that visualization." SINGLE PASS.
  - "Disclosure is about the perceived completeness of relevant information". SINGLE PASS.
  - It does not test provenance or source cues; the word "provenance" does not appear (checked: NO).
- Elhamdadi et al., "Vistrust" (arXiv 2309.16915): a trust framework and an experiment on visual complexity, not provenance. Scope only.
- Kennedy et al. on conventions and trust: unreachable (403); nothing quoted.

------------------------------------------------------------
UNASKED-FOR FINDINGS
1. Segel & Heer's martini glass allows an opening with no text at all, the stem being "an interesting default view or annotations" (quoted in Item 1a). This is a source-level link between the first screen and the authored account.
2. Hullman & Diakopoulos treat source and method notes as rhetoric ("provenance rhetoric"), and observed that uncertainty in news graphics was carried mostly by text.
3. Stokes, Setlur, Cogley, Satyanarayan & Hearst 2022, "Striking a Balance" (IEEE TVCG; arXiv 2208.01780), abstract, STRING-VERIFIED: "302 participants ranked univariate line charts containing varying amounts of text"; "We find that heavily annotated charts were not penalized."; "participants preferred the charts with the largest number of textual annotations over charts with fewer annotations or text alone"; "some kinds of information are best placed in the title, while others should be placed closer to the data".
4. Kim, Setlur & Agrawala 2021 (CHI; arXiv 2101.08235), abstract, STRING-VERIFIED: "when the caption describes a low-prominence chart feature, readers rely on the chart and report a higher-prominence feature as the takeaway". A limit on what a title or caption can do against the picture; it sits beside Kong 2019, where the title won recall.
5. The ONS states that semi-automation "is not a labour-saving tool" (Item 6a).
6. The automated-news meta-analysis finds credibility equal but readability far worse for automated text (d = 2.8, SINGLE PASS), and that telling readers a text is human-written raises ratings. This bears on how any generated narrative is labelled.
7. Schneiders 2020: scrollytelling's recall edge over text disappears, and reverses, once reading time is counted.
8. ONS Data Science Campus, "StatsChat" (23 August 2023; SINGLE PASS; https://datasciencecampus.ons.gov.uk/using-large-language-models-llms-to-improve-website-search-experience-with-statschat/): an experimental language-model search over ONS publications that answers from retrieved documents and links back to them. The authors say of avoiding fabrication, "we have not yet conducted enough testing and refinement to ensure this is always true for all search queries".

LEFT OUT, AND WHY
- Everything unreachable listed above. The gaps that matter most: Boy et al. 2015 full text; Hullman et al. 2013 full text; Zhi et al. 2019 full text.
- The NYT "fraction of readers" data point (Tse) and Conlen et al.'s reach findings: already settled in earlier chapters.
- Topic findings of every study (voting, drugs, meat, census areas): read for method only.
- Bostock's "How to Scroll" (404) and several tool papers on linking text and charts: not evaluations.

THREE RICH REFERENCES
1. Hullman & Diakopoulos 2011: the four editorial layers, default views as anchoring, and provenance rhetoric give the chapter a sourced vocabulary for a page that says how a display argues. https://users.eecs.northwestern.edu/~jhullman/vis_rhetoric.pdf
2. Hohman, Conlen, Heer & Chau 2020: the field's own review saying the evidence is thin, publishers do not share metrics, and a single anecdote became a rule of thumb. https://distill.pub/2020/communicating-with-interactive-articles/
3. Burns et al., "From Invisible to Visible": the closest experiment to "does a method note change anything". Answer: perceived thoroughness and what is remembered as important, not accuracy, clarity or relevance. https://cyxiong.com/wp-content/uploads/2022/12/impactsMetadata.pdf
(Worth obtaining and not reached: Thudt et al., "Exploration and Explanation in Data-Driven Storytelling", ch. 3 of Riche et al. 2018.)

WHAT SURPRISED ME
- In McKenna et al., scroller versus stepper made no measurable difference to engagement, and comprehension did not differ across conditions.
- Kong et al.'s readers recalled the title's message more often than the chart's even when the title contradicted the chart, and 72–87% still called the information neutral.
- Kim et al.'s prediction benefit vanished entirely on a familiar dataset, and in text only self-explanation helped.
- The storytelling null, the most-cited negative result in this area, sits behind a bot wall on its open repository.
- OWID's stated reason for prominent sourcing is credit to data producers, not reader trust.

Sources (all fetched 6 October 2026)
- http://vis.stanford.edu/files/2010-Narrative-InfoVis.pdf
- https://users.eecs.northwestern.edu/~jhullman/vis_rhetoric.pdf
- https://api.openalex.org/works/doi:10.1109/TVCG.2013.119
- https://api.openalex.org/works/doi:10.1145/2702123.2702452
- https://www.routledge.com/Data-Driven-Storytelling/Riche-Hurter-Diakopoulos-Carpendale/p/book/9781138197107
- https://diglib.eg.org/handle/10.1111/cgf13719
- https://www.hidykong.com/papers/Kong-CHI18.pdf
- https://www.hidykong.com/papers/Kong-CHI19-titles.pdf
- https://idl.cs.washington.edu/files/2017-ExplainingTheGap-CHI.pdf
- https://users.eecs.northwestern.edu/~jhullman/explaining_the_gap.pdf
- https://vdl.sci.utah.edu/publications/2017_eurovis_narrative-flow/
- https://sci.utah.edu/~vdl/papers/2017_eurovis_narrative-flow.pdf
- https://idl.cs.washington.edu/files/2019-IdyllAnalytics-EuroVis.pdf
- https://www.cogitatiopress.com/mediaandcommunication/article/view/2507
- https://distill.pub/2020/communicating-with-interactive-articles/
- https://pudding.cool/process/responsive-scrollytelling/
- https://arxiv.org/abs/2312.01164
- https://worrydream.com/ExplorableExplanations/
- https://digitalblog.ons.gov.uk/2023/01/27/semi-automation-and-census-2021-how-we-told-331-local-stories-in-one-go/
- https://www.ons.gov.uk/visualisations/censusareachanges/
- https://github.com/ONSvisual/robo-utils
- https://github.com/ONSvisual/robo-article
- https://www.cjr.org/tow_center_reports/guide_to_automated_journalism.php
- https://www.cogitatiopress.com/mediaandcommunication/article/view/3019
- https://ourworldindata.org/faqs
- https://ourworldindata.org/redesigning-our-interactive-data-visualizations
- https://themarkup.org/about
- https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/qualityinofficialstatistics/qualityandmethodologyinformation
- https://www.propublica.org/nerds
- https://mariandoerk.de/criticalinfovis/altchi2013.pdf
- https://cyxiong.com/wp-content/uploads/2022/12/impactsMetadata.pdf
- https://arxiv.org/abs/1901.01920
- https://secureservercdn.net/45.40.150.47/79z.71f.myftpupload.com/wp-content/uploads/2019/07/TrustVis_2019.pdf
- https://arxiv.org/abs/2309.16915
- https://arxiv.org/abs/2208.01780
- https://arxiv.org/abs/2101.08235
- https://datasciencecampus.ons.gov.uk/using-large-language-models-llms-to-improve-website-search-experience-with-statschat/

---

## Agent C — Interaction and its cost

CHAPTER 11 RESEARCH REPORT — FACET: INTERACTION AND ITS COST
Date of all fetches: 6 October 2026.

TOOLS I HAD. WebSearch was NOT available (the call returned "this turn's web search budget is used up"), so everything below came from direct URLs through WebFetch. Direct curl was blocked by the egress proxy. Pages I could not read and why: Europe PMC REST (proxy 429 rejection); arXiv author-listing pages (proxy 429); doi.org resolver (proxy 429); OpenAlex API (worked for five DOI lookups, then proxy 429); HAL (Anubis bot wall, 2 attempts); cs.ubc.ca Lam PDF (403, 2 URLs); PubMed and PMC (reCAPTCHA); jmir.org (empty body); ScienceDirect (robots); Wiley pdfdirect (403); DOAJ (403); CiteSeerX (blocklisted); cond.org (robots.txt fetch rate-limited, 3 attempts); Apple HIG accessibility page (JavaScript only); W3C Media Queries 4 hover section (fetcher truncates the page before that section, on both w3.org and drafts.csswg.org); ACM Queue id 2146416 (resolves to a different article); cs.umd.edu/hcil (robots).
Marking: STRING-VERIFIED = re-fetched with a YES/NO presence prompt, with a false control string in the same check (every control was correctly rejected). SINGLE PASS = one read only. ABSTRACT = only the abstract reached.

A caution worth knowing: on W3C Media Queries 4 the first pass returned four fluent "quotations" about touchscreens and hover; the presence check returned NO on every one. They were invented. Nothing from that spec is quoted below.

====================================================================
ITEM 1 — TAXONOMIES AND WHAT THEY CLAIM
====================================================================

1a. Heer & Shneiderman 2012, "Interactive Dynamics for Visual Analysis", CACM 55(4).
URL: https://idl.cs.washington.edu/files/2012-InteractiveDynamics-CACM.pdf (landing page https://idl.uw.edu/papers/interactive-dynamics).
What it is: practitioner/researcher framework (magazine article). It reports no user study of its own (reader's judgement, SINGLE PASS).
- "The taxonomy consists of 12 task types grouped into three high-level categories" — STRING-VERIFIED.
- "analysis process and provenance (record, annotate, share, and guide)" — STRING-VERIFIED. Full list sentence, SINGLE PASS for the first two groups: "data and view specification (visualize, filter, sort, and derive); view manipulation (select, navigate, coordinate, and organize)".
- Table rows, STRING-VERIFIED: "Select items to highlight, filter, or manipulate them"; "Navigate to examine high-level patterns and low-level detail"; "Record analysis histories for revisitation, review, and sharing"; "Annotate patterns to document findings"; "Share views and annotations to enable collaboration"; "Guide users through analysis tasks or stories". Other six rows SINGLE PASS: "Visualize data by choosing visual encodings"; "Filter out data to focus on relevant items"; "Sort items to expose patterns"; "Derive values or models from source data"; "Coordinate views for linked, multidimensional exploration"; "Organize multiple windows and workspaces".
- CORRECTION TO VERSION 1. The string «The taxonomy is descriptive rather than prescriptive» is NOT in the paper. What the authors do say, all STRING-VERIFIED:
  - "Validating and evolving this taxonomy is a community project that proceeds through feedback, critique, and refinement"
  - "Of course, by attempting to provide an abstracted picture of a domain, taxonomies may be incomplete"
  - "these examples do not constitute an exhaustive survey"
  - "Within each branch of the taxonomy, we describe example systems that exhibit useful interaction techniques"
  - "The goal of this article is to assist designers, researchers, professional analysts, procurement officers, educators, and students" ... "in evaluating and creating visual analysis tools"
  So the honest wording is: the authors call validation an unfinished community project and say the taxonomy may be incomplete. They do not use the words descriptive/prescriptive.
- The word "tooltip" does not appear in the article (reader's statement, SINGLE PASS).
Role: the standard map of what interactions exist, written for analysts' tools. By its own words it is unvalidated and possibly incomplete, so it cannot be cited as evidence that any of the twelve is needed.

1b. Yi, Kang, Stasko & Jacko 2007, TVCG 13(6).
URL: https://faculty.cc.gatech.edu/~stasko/papers/infovis07-interaction.pdf
What it is: peer-reviewed literature and systems review; no user study.
- "it has garnered a relatively low level of attention from the Infovis community" — STRING-VERIFIED (abstract).
- "the representation component has received the vast majority of attention in Infovis research" — STRING-VERIFIED.
- "we surveyed 59 papers and 51 systems and collected 311 individual interaction techniques" — STRING-VERIFIED.
- "Based on the notion of user intent" — STRING-VERIFIED.
- Categories, STRING-VERIFIED: "Select: mark something as interesting"; "Explore: show me something else"; "Abstract/Elaborate: show me more or less detail"; "Connect: show me related items". SINGLE PASS: "Reconfigure: show me a different arrangement"; "Encode: show me a different representation"; "Filter: show me something conditionally".
- Limits, STRING-VERIFIED: "the categories are not collectively exhaustive"; "Some techniques are difficult to classify and do not quite fit into any one of the categories". SINGLE PASS: "Some other interaction techniques appear to fulfill multiple user intents".
Role: seven intent-named categories. The paper says interaction is under-studied, and says its own categories are neither exhaustive nor exclusive.

1c. Dimara & Perin 2020, "What is Interaction for Data Visualization?", TVCG 26(1), pp. 119–129 (bibliographic details SINGLE PASS from the Utrecht portal).
URL reached: https://research-portal.uu.nl/en/publications/what-is-interaction-for-data-visualization — ABSTRACT only. Full text unreachable (HAL bot wall).
- "We argue that this confusion is due to a lack of consensual definition" — STRING-VERIFIED.
- "we synthesize a definition of interaction for visualization" — STRING-VERIFIED.
- "Our definition is meant to be a thinking tool and inspire novel and bolder interaction design practices" — STRING-VERIFIED.
- NOT OBTAINED: the definition sentence itself, the number of papers reviewed, and any "interaction is costly / no interaction" passage. The words "cost" and "costly" do not occur in the abstract. I quote nothing from the body. Version 2 should not attribute a cost claim to this paper unless someone reads the full text.
Role: a definitional paper whose own abstract calls the definition a "thinking tool".

====================================================================
ITEM 2 — THE COST FRAMEWORKS
====================================================================

2a. Lam 2008, "A Framework of Interaction Costs in Information Visualization", TVCG 14(6). DOI 10.1109/TVCG.2008.109.
ABSTRACT only, read from the OpenAlex index and checked word by word by position (numbers and costs 1–3 checked position by position; costs 4–7 consistent with the position lists for "to" and "costs"). Full text unreachable.
- Numbers: "From 484 papers, we collected 61 interaction-related usability problems reported in 32 user studies and placed them into our framework of seven costs".
- The seven, in her words: "(1) Decision costs to form goals; (2) System-power costs to form system operations; (3) Multiple input mode costs to form physical sequences; (4) Physical-motion costs to execute sequences; (5) Visual-cluttering costs to perceive state; (6) View-change costs to interpret perception; (7) State-change costs to evaluate interpretation."
- Also in the abstract (first-pass reconstruction; "poorly" and "Norman's" confirmed present): "Interaction cost is an important but poorly understood factor in visualization design"; framework "inspired by Norman's Seven Stages of Action".
What it is: peer-reviewed literature synthesis; no new experiment. Strength: a framework built from 32 studies' reported usability problems. It gives no sizes for the costs.
Role: the vocabulary for "what an interaction costs". It supports naming costs, not weighing them.

2b. Mosca, Ottley & Chang 2021, "Does Interaction Improve Bayesian Reasoning with Visualization?", CHI 2021.
URL: https://arxiv.org/pdf/2103.01701
What it is: peer-reviewed, two crowdsourced experiments. Population: US Mechanical Turk workers. Task: a two-part Bayesian reasoning question read from icon arrays (grouped, aligned, randomised); both parts had to be correct. Compared: static against checkbox filters, drag-and-drop, hover-linking of text and chart, and tooltips.
- "We recruited 530 participants from Amazon Mechanical Turk" — STRING-VERIFIED; "This left N = 472" — SINGLE PASS.
- "We recruited 2,149 participants from Amazon Mechanical Turk" — STRING-VERIFIED; "This left N = 1, 980 participants distributed among stimuli as shown in Table 5." — SINGLE PASS.
- "adding interaction to a static Bayesian reasoning visualization does not improve participants' accuracy on a Bayesian reasoning task" — STRING-VERIFIED.
- "In some cases, it can significantly detract from it" — STRING-VERIFIED.
- "interaction is not as unambiguously good as we often believe" — STRING-VERIFIED.
- "a well designed static visualization can be as, if not more, effective than an interactive one" — STRING-VERIFIED.
- "a cautious use of interactivity in cases where it does not add additional information to a visualization" — STRING-VERIFIED.
- Use of the control: "Out of the 246 participants assigned to cbAll, only 43% used the checkboxes on the visualization" — STRING-VERIFIED. "out of the 371 participants assigned to cbAll, only 44% actually interacted" — STRING-VERIFIED.
- "We find no statistically significant difference in accuracy between participants using different interaction techniques" — STRING-VERIFIED.
- SINGLE PASS: Experiment 1 static 57% correct against 53% with checkboxes, χ²(1, N=472)=0.69, p=0.41. Hover against static for high-spatial-ability participants χ²(1, N=332)=12.44, p<0.001, static better. Tooltip described as "When a participant hovers their mouse over any icon in the visualization a text box appears" (this fragment STRING-VERIFIED).
- Authors' explanation: "may have induced an extraneously high cognitive load" — STRING-VERIFIED. Limit: "fundamentally limited in scope" — STRING-VERIFIED.
- Flag: the first pass reported the overall Experiment 2 test as χ²(5, N=2206), which does not match the stated N of 1,980. Do not print that N without reading the table.
Role: the nearest measured evidence for "an interaction added without a task buys nothing and can cost". One reasoning task, one chart family.

2c. Zikmund-Fisher, Dickson & Witteman 2011, "Cool but Counterproductive: Interactive, Web-Based Risk Communications Can Backfire", J Med Internet Res 13(3):e60. DOI 10.2196/jmir.1665.
ABSTRACT only, from the OpenAlex index, with every number checked by position. jmir.org and PMC unreachable.
- n and population: "A total of 3371 members of a demographically diverse Internet panel".
- Task: a hypothetical choice between two thyroid-cancer treatments. Static pictographs against interactive "fill-in-the-blank" pictographs the reader had to build.
- "The interactive graphic conditions had significantly worse survey completion rates (1110/1695, 65.5% vs 1316/1659, 79.3%, P < .001) than the static image conditions."
- "respondents who viewed interactive graphs were less likely to select the dominant treatment option (234/380, 61.6% vs 343/465, 73.8%, P < .001) in the strong dominance condition."
- "Interactivity, however visually appealing, can add to respondent burden and distract people from understanding relevant statistical information."
Role: a large randomised study in which a required interaction lowered both completion and correct choice. Health risk graphics, 2011, Flash.

2d. Hohman, Conlen, Heer & Chau, "Communicating with Interactive Articles", Distill, published "Sept. 11, 2020".
URL: https://distill.pub/2020/communicating-with-interactive-articles/
What it is: peer-reviewed survey essay over "a corpus of over sixty interactive articles" (SINGLE PASS).
- "In the worst case, interactivity may be distracting to readers or the functionality may go unused" — STRING-VERIFIED.
- "There is limited empirical evaluation of the effectiveness of interactive articles" — STRING-VERIFIED.
- "large publishers are unwilling to share internal metrics, and laboratory studies may not generalize to real world reading trends" — STRING-VERIFIED.
- On the New York Times they are reporting someone else's statement: "provided one of the few available data points"; "only a fraction of readers interact with non-static content"; "designers should move away from interactivity" — all STRING-VERIFIED.
- "closer to building a website than writing a blog post" — STRING-VERIFIED (authoring cost).
Role: it explains why newer reach figures are scarce. Publishers do not share metrics.

2e. Newer measured reach study: NONE FOUND. Without search I could not look for OWID, ONS or newsroom analytics. The only new use figures are Mosca's experimental ones (43% and 44% used an available checkbox filter), which are not field reach. Blascheck et al. "Glanceable Visualization": not reachable (HAL).

====================================================================
ITEM 3 — PROGRESSIVE DISCLOSURE
====================================================================

3a. Nielsen, "Progressive Disclosure", NN/g, December 3, 2006.
URL: https://www.nngroup.com/articles/progressive-disclosure/
What it is: practitioner framework. It reports no participant numbers for any study (reader's statement, SINGLE PASS).
- Definition: "Initially, show users only a few of the most important options" ... "Offer a larger set of specialized options upon request" — STRING-VERIFIED.
- "Progressive disclosure defers advanced or rarely used features to a secondary screen, making applications easier to learn and less error-prone" — STRING-VERIFIED.
- CORRECTION TO THE BRIEF. Nielsen's two conditions are not "split correctly" and "make the initial set the important one". They are, both STRING-VERIFIED: "You must get the right split between initial and secondary features" and "It must be obvious how users progress from the primary to the secondary disclosure levels". The "frequently used" point is his gloss on the first.
- "You have to disclose everything that users frequently need up front" ... "so that they have to progress to the secondary display only on rare occasions" — STRING-VERIFIED.
- "The primary list can't contain too many options or you'll fail to sufficiently focus users' attention on truly important issues" — STRING-VERIFIED.
- "designs that go beyond 2 disclosure levels typically have low usability because users often get lost when moving between the levels" — STRING-VERIFIED.
- How to find the split: "Task analysis and field studies can give you insights into what people need"; "frequency-of-use statistics can help you prioritize the features" — STRING-VERIFIED.
- "Progressive disclosure thus improves 3 of usability's 5 components" — STRING-VERIFIED (named as learnability, efficiency of use and error rate, SINGLE PASS).
- "people understand a system better when you help them prioritize features and spend more time on the most important ones" — STRING-VERIFIED. It is introduced by "Research says", with a link to another NN/g article and no study named (SINGLE PASS).
- The only empirical reference is "46 web-based applications" (STRING-VERIFIED), which is about a hotel-booking form and staged disclosure.
Role: the definition and two tests everyone repeats. It is expert opinion from 2006.

3b. Springer & Whittaker 2019, IUI (arXiv title "Progressive Disclosure: Designing for Effective Transparency").
URL: https://arxiv.org/pdf/1811.02164
What it is: peer-reviewed; two studies of an emotion-from-text predictor ("E-meter"). Participants wrote about an emotional experience and saw either a document-level rating or word-by-word highlighting.
- Study 1: "We recruited 100 users to test the E-meter system" — STRING-VERIFIED. "we eliminated 26 respondents based on their responses to open ended questions, leaving us with a sample of 74 users" — STRING-VERIFIED.
- "Participants anticipated greater accuracy for the word-level system" — STRING-VERIFIED. The statistic is printed as "t(73)=5.452, p=0.022" (STRING-VERIFIED as printed). A t of 5.45 on 73 degrees of freedom does not give p=0.022, so do not reprint it.
- After use: "participants also showed no overall differences in trust after using the two different system versions" — STRING-VERIFIED (first pass gives t(73)=.910, p=.343).
- "Fifty percent of participants (37) said that they would prefer the document-level version" — STRING-VERIFIED.
- Study 2: "Twelve users were recruited from an internal participant pool at a large United States west-coast university" — STRING-VERIFIED; think-aloud.
- Heading: "Transparency May Violate User Expectations Even When the System is Correct" — STRING-VERIFIED.
- "incremental feedback is distracting and undermines simple heuristics users form about system operation" — STRING-VERIFIED.
- "users may benefit from initially simplified feedback that hides potential system errors" — STRING-VERIFIED.
- Principle: "advanced information and explanation is provided on an 'as needed' basis" and "explanation is presented as two-way communication with the user driving exactly when and how explanations are provided" — STRING-VERIFIED. Their example: "the E-meter could show a 'How was this rating calculated?' button" — STRING-VERIFIED.
- Authors' limits (SINGLE PASS): one domain, moderate error rate, low cost of error.
What happened to trust: more detail raised the accuracy people expected before use. After use, trust did not differ and preference split 37/37.
Role: measured support for showing the simple account first and detail on request. It concerns algorithm explanations, not charts.

3c. Stokes, Setlur, Cogley, Satyanarayan & Hearst 2023, "Striking a Balance", TVCG (PRIORITY).
URL: https://arxiv.org/pdf/2208.01780
What it is: peer-reviewed crowdsourced experiment on synthetic single-line charts with fictional topics.
- "We recruited 512 participants from Amazon Mechanical Turk" — STRING-VERIFIED. "302 participants ranked univariate line charts containing varying amounts of text" — STRING-VERIFIED. Exclusions for failed comprehension checks and low-quality answers (SINGLE PASS). US, desktop or laptop only (SINGLE PASS).
- Conditions (SINGLE PASS): Set A had four versions — no text; title plus one annotation; many annotations; a paragraph with no chart. Set B had title only; title plus one annotation; title plus two. Text content was classed at four semantic levels (L1 encodings, L2 statistics, L3 perceptual trends, L4 outside context).
- "We find that heavily annotated charts were not penalized" — STRING-VERIFIED.
- "participants preferred the charts with the largest number of textual annotations over charts with fewer annotations or text alone" — STRING-VERIFIED.
- "42, or 14% of participants — ranked the all-text option as their first choice for Set A" — STRING-VERIFIED.
- What readers took away: "L1 annotations had almost no effect" — STRING-VERIFIED. "6.1x as likely than when provided with L1" (taking away outside context when the annotation gave it) — STRING-VERIFIED. SINGLE PASS: "annotations belonging to L2 and L4 had the greatest influence on the participants' takeaways, followed by L3"; 736 takeaways collected.
- Guidelines, STRING-VERIFIED: "Rather than aiming for maximally minimalist design, annotate charts with relevant text"; "Higher quantities of annotations are not penalized for the 'clutter' they may cause"; "Perceptual content relating to patterns or trends should be positioned in the title"; "Consider a text-only variant that can stand alone". SINGLE PASS: statistical information and outside context "should be positioned by a relevant point".
- Limits, STRING-VERIFIED: "The line charts created clearly showed abrupt peaks and trends, which is not often the case in practice"; "Future work should explore how readers integrate text with other chart types, including dashboards".
Role: the strongest evidence in this facet for putting detail on the face. More annotation was preferred and it steered what readers reported. Measured on preference and free-text takeaways, on tidy synthetic line charts. The authors say dashboards are untested.

3d. Kim, Setlur & Agrawala 2021, "Towards Understanding How Readers Integrate Charts and Captions", CHI.
URL: https://arxiv.org/pdf/2101.08235
- "219 participants" — STRING-VERIFIED (marking prominent features on 43 line charts; "43" STRING-VERIFIED). "2168" participants — STRING-VERIFIED (4953 takeaways, SINGLE PASS).
- "readers treat the doubly emphasized high-prominence feature as the takeaway" — STRING-VERIFIED.
- "readers rely on the chart and report a higher-prominence feature as the takeaway" (when the caption names a low-prominence feature) — STRING-VERIFIED.
- SINGLE PASS: outside information in the caption made readers more likely to mention the captioned feature (p=0.011 synthetic, p=0.021 real).
Role: text on the face steers the reading only when the chart's shape agrees with it.

3e. Ajani, Lee, Xiong, Knaflic, Kemper & Franconeri 2021/22, "Declutter and Focus", TVCG.
URL: https://visualthinking.psych.northwestern.edu/publications/Ajani_Declutter_2021.pdf
- n: "All 24 participants whose data were used in the final analysis are either students or community members at Northwestern University." — SINGLE PASS sentence; "24" confirmed present.
- Design (SINGLE PASS): cluttered, decluttered, and decluttered-plus-focused (highlight colour and a one-sentence annotation). 10-second exposure, then redraw from memory, write conclusions, and rate.
- "Decluttering designs led to higher ratings on professionalism" — STRING-VERIFIED.
- "adding focus to the design led to higher ratings on aesthetics and clarity, and better memory for the highlighted pattern" — STRING-VERIFIED.
- SINGLE PASS: "There is no significant difference between relevance scores for the cluttered and decluttered designs (Est = 0.13, p = 0.81)."; some participants called focused designs "pushy" (word confirmed present).
Role: small-n evidence that stripping a chart did not improve recall but an on-face highlight and sentence did.

====================================================================
ITEM 4 — HOVER, TOOLTIPS, TOUCH AND KEYBOARD
====================================================================

4a. WCAG 2.2 normative text (standard; W3C Recommendation), read on the W3C Understanding pages. All fragments STRING-VERIFIED unless marked.

SC 1.4.13 Content on Hover or Focus, Level AA.
URL: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html
- Lead-in (SINGLE PASS): "Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:"
- Dismissible: "A mechanism is available to dismiss the additional content without moving pointer hover or keyboard focus" + "unless the additional content communicates an input error or does not obscure or replace other content"
- Hoverable: "If pointer hover can trigger the additional content," (SINGLE PASS) + "then the pointer can be moved over the additional content without the additional content disappearing"
- Persistent: "The additional content remains visible until the hover or focus trigger is removed, the user dismisses it" + "or its information is no longer valid"
- Exception: "The visual presentation of the additional content is controlled by the user agent and is not modified by the author"

W3C's own explanation of the problem (same page, STRING-VERIFIED):
- "Additional content that appears and disappears in coordination with keyboard focus or pointer hover often leads to accessibility issues"
- "the user may not have intended to trigger the interaction"; "the user may not know new content has appeared"; "the new content may interfere with a user's ability to do a task"
- "The magnified view generally follows the mouse pointer or keyboard focus" ... "so screen magnification users navigate by moving the mouse or moving the keyboard focus to pan the magnified viewport"
- "Here, the pointer can obscure a significant area of the additional content"
- "Users with disabilities may require more time for many reasons, such as to change magnification, move the pointer, or simply to bring the new content into their visual field"
- "Content which can be triggered via pointer hover should also be able to be triggered by keyboard focus"
- NEGATIVE FINDING: the word "touch" does not appear on this page (checked twice). W3C's case against hover content here is about magnification, large pointers, time and keyboard. It is not about touchscreens. I could not obtain a W3C sentence saying touchscreens cannot hover.

SC 2.1.1 Keyboard, Level A. URL: https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html
- "All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes" + "except where the underlying function requires input that depends on the path of the user's movement and not just the endpoints"

SC 2.5.1 Pointer Gestures, Level A. URL: https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html
- "All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture" + "unless a multipoint or path-based gesture is essential"
- Example (SINGLE PASS): "A website includes a map view that supports the pinch/spread gesture to zoom into the map content. As a single-pointer alternative, the map also includes plus/minus buttons to zoom in and out."

SC 2.5.7 Dragging Movements, Level AA, new in 2.2. URL: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- "All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging" + "unless dragging is essential or the functionality is determined by the user agent and not modified by the author"
- "Some people cannot perform dragging movements in a precise manner" — STRING-VERIFIED.
- SINGLE PASS: "This requirement is separate from keyboard accessibility because people using a touchscreen device may not use a physical keyboard."; "achieving keyboard equivalence for a dragging operation does not automatically meet this success criterion"; slider example "allows tapping or clicking on any point of the slider track"; map example "the map has up/down/left/right buttons to move the view as well."

SC 2.5.8 Target Size (Minimum), Level AA, new in 2.2. URL: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- "The size of the target for pointer inputs is at least 24 by 24 CSS pixels, except when"
- Spacing: "Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that" (SINGLE PASS) "if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target" (STRING-VERIFIED) "or the circle for another undersized target" (SINGLE PASS)
- Equivalent: "The function can be achieved through a different control on the same page that meets this criterion"
- Inline: "The target is in a sentence or its size is otherwise constrained by the line-height of non-target text"
- User agent control: "The size of the target is determined by the user agent and is not modified by the author"
- Essential: "A particular presentation of the target is essential or is legally required for the information being conveyed"
- UNASKED-FOR AND IMPORTANT, STRING-VERIFIED, in the explanation of the Essential exception: "If there are many pins close together, the spacing between pins and neighboring pins will often be below 24 CSS pixels"; "It is essential to show the pins at the correct map location, therefore the Essential exception applies"; "A similar example is an interactive data visualization where targets are necessarily dense". The same passage adds (SINGLE PASS): "When the 'Essential' exception is applicable, authors are strongly encouraged to provide equivalent functionality through alternative means to the extent practical."
- For comparison, SC 2.5.5 Target Size (Enhanced), Level AAA: "The size of the target for pointer inputs is at least 44 by 44 CSS pixels except when" — STRING-VERIFIED (https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html).

4b. W3C ARIA Authoring Practices, Tooltip pattern (guidance, not normative).
URL: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- "This design pattern is work in progress; it does not yet have task force consensus" — STRING-VERIFIED.
- "A tooltip is a popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it" — STRING-VERIFIED.
- "Escape: Dismisses the Tooltip" — STRING-VERIFIED. The page does not mention touch (SINGLE PASS).

4c. ONS and Analysis Function.
ONS Service Manual, "Interactive charts and animations". URL: https://service-manual.ons.gov.uk/data-visualisation/guidance/interactive-charts-and-animations (design-system guidance; undated; no evidence cited). All STRING-VERIFIED:
- "Only consider using an interactive chart where the most important information for the user cannot be clearly shown through a non-interactive chart"
- "Interactive charts need the user to make a selection to see information"
- "This may make it more difficult for users to get messages"; "hide the main messages from users"
- "A tooltip displays data values when the user hovers over or selects part of a chart" (this follows the sentence you already hold)
- "Consider using several small charts, known as small multiples"
- SINGLE PASS: a third cost in the same list, "prevent the chart from being useful outside of the Office for National Statistics (ONS) website, for example, on social media"; on animation, "never make an animation the only way to get the information".

ONS Service Manual, "Dashboards". URL: https://service-manual.ons.gov.uk/data-visualisation/guidance/dashboards. All STRING-VERIFIED:
- "Only use a dashboard if you have clear justification for doing so"
- "they put the burden of interpreting and understanding data onto the user"
- "A dashboard may or may not have interactive elements, such as filtering"
- "are difficult to make accessible and responsive for different devices"
- "put the most important insights at the top or in the most prominent position"
- "the data are updated frequently, and users are likely to revisit the dashboard"

ONS Service Manual, "Annotations" (SINGLE PASS throughout). URL: https://service-manual.ons.gov.uk/data-visualisation/guidance/annotations
- "Keep annotations concise. Limit them to around 50 characters (10 to 12 words) and a single sentence."; "Annotations may not display on mobile devices in certain chart templates."; "Make sure any essential information you include in annotations is also included in the main text or footnotes."
- Note the tension with Stokes et al.: ONS caps annotation length and warns it may vanish on phones.

Analysis Function, "Data visualisation: charts". URL: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ (published 19 May 2022, SINGLE PASS).
- "It does not cover interactive visualisations." — STRING-VERIFIED. Context (SINGLE PASS): "However, the approaches discussed are applicable to them." The page has no sentence on tooltips, hover, keyboard or touch.

Analysis Function, "Data visualisation: building and managing dashboards". URL: https://analysisfunction.civilservice.gov.uk/policy-store/top-tips-for-designing-dashboards/ ("Publication date: 6 February 2026", SINGLE PASS).
- "Only consider using a dashboard when" ... "there is an identified user need" ... "users need flexibility of data combinations and the ability to interact with data" — STRING-VERIFIED.
- "Dashboards are not good at explaining what's happening in the data and users may have to discover insights for themselves" — verified (the checker returned the identical sentence as its "closest").
- "Get prototypes in front of users quickly, so you can iterate on the design" — STRING-VERIFIED.
- SINGLE PASS: "Dashboards rarely meet full accessibility requirements."
- No mention of tooltips, hover or keyboard.

4d. Measured study of tooltip discovery or use: NONE OBTAINED. The two candidates I know of (Boy et al. 2016, "Suggested Interactivity", TVCG; Blascheck et al. 2019, "Exploration Strategies for Discovery of Interactivity in Visualizations", TVCG) were unreachable, and I quote nothing from them. Nearest in hand: Mosca et al. 2021 included a tooltip condition (435 assigned, SINGLE PASS) and found no accuracy gain, but the paper gives no tooltip use rate (reader's "NOT GIVEN", SINGLE PASS). NN/g's tooltip guideline cites no study (reader's statement).

4e. Practitioner statement on tooltips: Kendrick, "Tooltip Guidelines", NN/g, January 27, 2019.
URL: https://www.nngroup.com/articles/tooltip-guidelines/ — all STRING-VERIFIED:
- "Don't use tooltips for information that is vital to task completion"
- "Users shouldn't need to find a tooltip in order to complete their task"
- "Because tooltips are initiated by a hover gesture, they can be used only on devices with a mouse or keyboard"; "They are not normally available on touchscreens"
- "Tooltips are hard to discover because they often lack visual cues"
- "Tooltips that appear only on mouse hover are inaccessible for users that rely on keyboards to navigate"

4f. Touch-target accuracy.
Parhi, Karlson & Bederson 2006, MobileHCI. URLs: http://www.cs.umd.edu/~bederson/images/pubs_pdfs/p203-parhi.pdf and the Microsoft Research page.
- "Twenty participants (17 male, 3 female)" — STRING-VERIFIED. SINGLE PASS: recruited in the University of Maryland computer science department, right-handed only, aged 19 to 42 (mean 25.7); HP iPAQ handheld; sizes "3.8, 5.8, 7.7, 9.6 and 11.5 mm" for discrete taps.
- "target size of 9.2 mm for discrete tasks and targets of 9.6 mm for serial tasks should be sufficiently large for one-handed thumb use" + "without degrading performance and preference" — STRING-VERIFIED.
- "there were no significant differences in error rate between target sizes" (≥ 9.6 mm discrete, ≥ 7.7 mm serial) — STRING-VERIFIED.
- Strength: one small lab study of young right-handed computing students on a 2006 stylus-era device. W3C lists it under related resources for SC 2.5.8 (SINGLE PASS).
Apple, "UI Design Dos and Don'ts". URL: https://developer.apple.com/design/tips/ — "Create controls that measure at least 44 points x 44 points so they can be accurately tapped with a finger." — STRING-VERIFIED. Practitioner standard. The HIG accessibility page itself was unreadable.
Google, Android Accessibility Help, "Touch target size". URL: https://support.google.com/accessibility/android/answer/7101858?hl=en — STRING-VERIFIED: "A touch target of 48x48dp results in a physical size of about 9mm, regardless of screen size"; "The recommended target size for touchscreen objects is 7-10mm"; "Consider making touch targets at least 48x48dp, separated by 8dp of space or more". Practitioner standard.
So the ladder is 24 CSS px (WCAG AA floor), 44 CSS px (WCAG AAA), 44 pt (Apple), 48 dp or about 9 mm (Google), 9.2 to 9.6 mm (Parhi).

====================================================================
ITEM 5 — ONBOARDING, GUIDED TOURS, ANNOTATION AND GUIDE
====================================================================

5a. Stoiber, Walchshofer, Pohl, Potzmann, Grassinger, Stitz, Streit & Aigner 2022, "Comparative Evaluations of Visualization Onboarding Methods", Visual Informatics 6(4), 34–50.
URL: https://data.jku-vds-lab.at/papers/2022_visinf_compare_evaluations_onboarding.pdf
What it is: peer-reviewed, three studies.
- "However, empirical evidence on the effectiveness of such approaches is scarce" — STRING-VERIFIED.
- "We performed a between-subject experiment with 596 participants in total" — STRING-VERIFIED. Per the body (SINGLE PASS) 596 is the total across all three studies: 388 Mechanical Turk workers in Study 1, 145 more in Study 2, 63 students in Study 3 (65 recruited).
- Study 1 compared a step-by-step interactive guide against none, for a bar chart, horizon graph, change matrix and parallel coordinates plot, on answer correctness and time. "there are no significant differences between the answer correctness of the questions with and without onboarding" — STRING-VERIFIED. "p = .533" and "F(1,396)=6.675" — STRING-VERIFIED as present. SINGLE PASS detail: only the change matrix gained (0.81 ± .39 with, 0.70 ± .46 without, p=.010); for parallel coordinates, "The answer correctness without onboarding showed surprisingly more correct answers (0.58±.49) than for surveys with the onboarding (0.52 ± .50), but with a large variance."
- "for highly familiar visualization types no onboarding is needed" — STRING-VERIFIED (participants' comment).
- Study 2 (SINGLE PASS) compared step-by-step guide, scrollytelling tutorial and video for parallel coordinates. No correctness difference; video drew the most positive comments (42.86%, then scrollytelling 32.65%, step-by-step 27.66%). The first-pass recruitment figures for Study 2 do not add up (100 recruited, 5 excluded, 145 analysed). Check before printing.
- Study 3 (SINGLE PASS): students using the Netflower tool. In-situ scrollytelling against a landing-page tutorial: correctness .71 against .74, p=.517. Scrollytelling preferred. Eight said the tutorial was "not needed and that they just started working" (fragment STRING-VERIFIED).
- Limits, STRING-VERIFIED: "the MTurk workers may not take enough time with the onboarding concept itself to carefully read through the text"; "They were overconfident about their ability to solve problems".
Role: the largest measured test of guided introductions found. It showed preference effects and almost no comprehension effect, and readers skipped or skimmed the guide.

5b. Dhanoa, Walchshofer, Hinterreiter, Stitz, Gröller & Streit 2022, "A Process Model for Dashboard Onboarding", Computer Graphics Forum (EuroVis).
URL: https://data.jku-vds-lab.at/papers/2022_eurovis_dashboard-onboarding.pdf
What it is: conceptual model, described through real-world examples. No controlled user study (reader's judgement).
- "To bridge the gap between non-expert dashboard users and potentially complex datasets and/or visualizations" — STRING-VERIFIED.
- "The onboarding author decides the what, how, where, and when of the onboarding process" — STRING-VERIFIED.
- "Active approaches have been shown to be more effective than passive ones in specific cases" — STRING-VERIFIED.
- "we acknowledge that the proof of generalizability is limited and can only be solidified by future applications of the model" — STRING-VERIFIED.
Role: vocabulary (onboarding loop, onboarding author). Not evidence that onboarding works.

5c. Dhanoa, Hinterreiter, Fediuk, Elmqvist, Gröller & Streit 2025, "D-Tour", TVCG. DOI 10.1109/TVCG.2024.3456347.
URL: https://data.jku-vds-lab.at/papers/2025_d-tour.pdf
- "five authors from various departments and divisions of our industrial collaborators" and "six end users from our industrial collaborators" — STRING-VERIFIED.
- "All users responded positively to the onboarding experience" — STRING-VERIFIED.
- "with the option of switching to a free exploration at any time" — STRING-VERIFIED.
- "A primary challenge in measuring the effectiveness of an onboarding experience is the subjectivity of learning" — STRING-VERIFIED.
- "Due to the small number of participants and consequently dashboards" — STRING-VERIFIED (limitation).
- No no-tour baseline (reader's statement). Qualitative only, in-house industrial users.
Role: a guided tour the reader can leave at any point, with six end users and no comparison.

5d. Stoiber et al. 2022, "Visualization Onboarding Grounded in Educational Theories" (arXiv 2203.11134): a design-space chapter with no user study. ABSTRACT only.

5e. Annotation and guide effects on readers.
- Measured effects: Stokes et al. (3c), Kim et al. (3d), Ajani et al. (3e).
- Ren, Brehmer, Lee, Höllerer & Choe 2017, "ChartAccent", PacificVis. URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2017/02/chartaccent-pacificvis2017.pdf. A "survey of 106 annotated charts published by six prominent news graphics desks" (abstract, SINGLE PASS). The study had 11 participants who reproduced annotated charts with the tool (SINGLE PASS). Reader comprehension was not tested. The authors say they did not count how common each annotation form is (SINGLE PASS). An authoring study, not a reader study.
- Kong & Agrawala 2012, "Graphical Overlays", InfoVis. URL: http://vis.berkeley.edu/papers/grover/. ABSTRACT only. Five overlay types (reference structures, highlights, redundant encodings, summary statistics, annotations). The page reports no user study (SINGLE PASS).
- Hullman et al. 2013, "Contextifier": not reached.

====================================================================
ITEM 6 — "NAME THE PURCHASE": NEAREST EVIDENCE
====================================================================

6a. An interaction added without a task hurts or buys nothing: Mosca et al. 2021 (2b) and Zikmund-Fisher et al. 2011 (2c) are the two measured cases. Stoiber et al. 2022 (5a) adds that an interactive guide bought no correctness. Springer & Whittaker 2019 (3b) adds that more detail raised expectations but not trust after use.

6b. Hullman, Adar & Shah 2011, "Benefitting InfoVis with Visual Difficulties", TVCG 17(12). DOI 10.1109/TVCG.2011.175.
ABSTRACT only, SINGLE PASS (OpenAlex reconstruction; the position check was refused and the tail of the reconstruction was garbled, so treat these as unverified). Full text unreachable.
- "Yet several recent studies in visualization research provide evidence that non-efficient visual elements may benefit comprehension and recall on the part of users."
- "We identify conditions under which the application of visual difficulties is appropriate"
- "We characterize effective graph design as a trade-off between efficiency and learning"
The authors' caveats in their exact words were NOT obtained. All I can say is that the abstract itself frames the claim as conditional and as a trade-off. Do not quote this paper in version 2 without a full-text check.

6c. Perin, Vuillemot & Fekete 2013: skipped as instructed.

====================================================================
UNASKED-FOR FINDINGS (8)
====================================================================
1. WCAG's own explanation of SC 2.5.8 names "an interactive data visualization where targets are necessarily dense" as a case for the Essential exception. Dense chart marks can lawfully fall under 24 px, and W3C then encourages an equivalent route "to the extent practical".
2. GOV.UK Design System records evidence against click-to-reveal. Details (https://design-system.service.gov.uk/components/details/): "There is evidence that some users avoid clicking the link to show more details, as they think it will take them away from the page" (verified; checker returned the identical sentence) and "Do not use the details component to hide information that the majority of your users will need" (STRING-VERIFIED). Accordion (https://design-system.service.gov.uk/components/accordion/), STRING-VERIFIED: "Accordions hide content from the user. Not all users will notice them or understand how they work."; "Do not use an accordion for content that all users need to see"; "Test with users to decide if using an accordion outweighs the potential problems with hiding content". Tabs (https://design-system.service.gov.uk/components/tabs/), STRING-VERIFIED: "Tabs hide content from users and not everyone will notice them or understand how they work"; "the first section is more relevant than the others for most users"; and "This component has not yet been tried in research with users".
3. None of the three UK public design systems has a tooltip component. I read the component lists of GOV.UK, NHS and ONS; no Tooltip, popover or toggletip in any (SINGLE PASS each). W3C's own tooltip pattern is still marked as lacking consensus.
4. The ONS Design System now ships chart components (area, bar, column, line, scatter) built on Highcharts (https://service-manual.ons.gov.uk/design-system/components/line-chart-component). STRING-VERIFIED: "Use the Tab key to move focus into the chart. Once inside, use the arrow keys to navigate between data points."; "As you move, tooltips will be announced to describe each point."; "A url for a fallback image to display instead of the chart or iframe visualisation if JavaScript is disabled"; "Download options displayed below the chart". SINGLE PASS: "Touch device users, explore by touch or with swipe gestures." So ONS guidance exempts tooltip-only charts from "interactive" while its components make tooltips keyboard-reachable.
5. Chartability (Elavsky et al.), https://chartability.github.io/POUR-CAF/: "7 principles and 50 heuristics, 14 of which are considered critical" (SINGLE PASS). STRING-VERIFIED heuristic titles and text: "Interaction modality only has one input type"; "No interaction cues or instructions" — "If chart has any interactive capabilities at all, it must be explained somewhere for users to understand"; "Target pointer interaction size is too small" — "should have a minimum size of at least 24px x 24px"; "Scrolling experiences cannot be altered". SINGLE PASS: where marks are sized by data, "alternative means must be provided to select, activate, or otherwise interact".
6. NHS service manual, Expander (https://service-manual.nhs.uk/design-system/components/expander), STRING-VERIFIED: "We tested several expanders in our information about type 1 diabetes where users felt overwhelmed by the amount of information"; "They tested well and seemed to meet users' emotional needs"; "there's a risk that expanders will distract users". A public-sector case where hiding detail tested well, when readers were overwhelmed.
7. The Analysis Function published new dashboard guidance on 6 February 2026 (4c). It makes "the ability to interact with data" a condition for having a dashboard at all, and says dashboards "rarely meet full accessibility requirements" (SINGLE PASS).
8. Mosca et al.'s use rate: when a filter control was offered beside a chart in a paid experiment, 43% and 44% of those assigned used it. This is a controlled-setting figure to set beside the field reach figures already in hand.

====================================================================
LEFT OUT AND WHY
====================================================================
- Dimara & Perin's definition and review size; Lam's full text; Hullman et al.'s caveats; Boy et al. 2016; Blascheck et al. 2019; Blascheck "Glanceable"; Contextifier: all unreachable (see tools note). Nothing quoted from memory.
- W3C Media Queries 4 hover feature: unreachable past the fetcher's cut-off; first-pass quotes proved invented; nothing quoted.
- Apple HIG accessibility page: JavaScript only. The Apple "Dos and Don'ts" page stands in.
- Any newer field reach study: I had no search and no known URL.
- Hearst et al. word clouds and Perin et al. horizon graphs: skipped as instructed.
- Kong et al. on titles: belongs to the titles work already settled.
- Reach, defaults, overview-first, animation: not re-researched, per the brief.

====================================================================
THREE RICH REFERENCES
====================================================================
1. Stokes, Setlur, Cogley, Satyanarayan & Hearst 2023, "Striking a Balance" — https://arxiv.org/pdf/2208.01780. The best single source on how much to put on the face and where, with its own limits stated.
2. Mosca, Ottley & Chang 2021, "Does Interaction Improve Bayesian Reasoning with Visualization?" — https://arxiv.org/pdf/2103.01701. A direct static-against-interactive test over five interaction types, with use rates.
3. W3C, Understanding SC 2.5.8 Target Size (Minimum) and SC 1.4.13 Content on Hover or Focus — https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html and .../content-on-hover-or-focus.html. The normative text plus W3C's reasoning, including the data-visualisation exception.
(Runner-up: Stoiber et al. 2022 on onboarding, n=596.)

====================================================================
WHAT SURPRISED ME
====================================================================
- Heer & Shneiderman never say "descriptive, not prescriptive". They say validation is "a community project". Version 1's attribution needs rewording.
- Nielsen's second condition is that the route to the hidden layer must be obvious. It is not about which items go first.
- W3C's hover criterion does not mention touch at all. The touch argument against hover rests on practitioner sources (NN/g) and on SC 2.5.7's remark about touchscreen users lacking a keyboard.
- WCAG explicitly lets dense interactive data visualisations under the 24-pixel floor.
- The evidence splits on reveal versus show. For text on the chart face, more was preferred and it steered takeaways (Stokes; Ajani). For interactive guides, more made almost no difference to correctness (Stoiber). For interactive controls, they went unused by over half and never beat static (Mosca; Zikmund-Fisher).
- Two published statistics do not survive a sanity check as printed: Springer & Whittaker's t(73)=5.452 with p=0.022, and the Stoiber abstract's "between-subject experiment with 596 participants", which the body shows is three studies summed.
- Hohman et al. state plainly why reach data is thin: publishers will not share metrics.

---

## Agent D — Citable states and the data-to-display architecture

CHAPTER 11 RESEARCH REPORT — FACET: CITABLE STATES AND THE DATA-TO-DISPLAY ARCHITECTURE
Fetched 6 October 2026.

TOOLS AND LIMITS. WebSearch was unavailable (the turn's shared search budget was already used up), so everything is from direct URLs via WebFetch. Raw download with curl was blocked by the egress proxy, so verification is by YES/NO re-fetch with false control strings, not by grep. For papers with no open copy I used DOI look-ups on OpenAlex and Crossref to get abstracts. Tags: STRING-VERIFIED (second-pass presence check, controls correctly rejected), SINGLE PASS, ABSTRACT.

Pages I could not read:
- Springer book page for Wilkinson 2005 (link.springer.com/book/10.1007/0-387-28695-0): proxy 429, not retried.
- tandfonline DOI for Kennedy et al.: 429 (White Rose accepted manuscript used instead).
- arXiv author listings, Semantic Scholar API, PubMed, Europe PMC: 429.
- api.osf.io and osf.io download: robots-disallowed.
- IEEE Xplore and computer.org pages for Song & Szafir: empty JavaScript shells.
- diglib.eg.org PDF for Xiong et al.: robots fetch failed twice.
- DiVA record for Andreasson & Riveiro: robots timeout.
- UK Data Service citing-data pages: two 404s.
- ONS Census maps and the Vega editor: JavaScript-only, no text.

Corrections to the brief:
(a) Sarma et al. 2023 is by Sarma, Guo, Hoffswell, Rossi, Du, Koh & Kay, not "Sarma, Kale, Moon, Taylor & Kay".
(b) The Perma Supreme Court figure is 49.9% in the body and "50%" in the summary sentence; there is no bare "49%".
(c) Lin & Thornton's preprint is now titled "Visualization aesthetics influence trust in science, news, and social media"; "Fooled by beautiful data" does not appear in the Crossref record.
(d) Xiong et al. 2019 did not test source, provenance or visual style cues; it tested four transparency dimensions.
(e) Schloss et al. 2018 (recycling) is about assigning colours to concepts, not "red = bad".
(f) The ONS "Guide to statistical revisions" URL now serves a page titled "The Office for National Statistics' Revisions Policy and Correction of Errors Policy".

==================================================
ITEM 1. STABLE ADDRESSES
==================================================

1a. Berners-Lee, "Cool URIs don't change" (W3C Style, 1998). https://www.w3.org/Provider/Style/URI
Practitioner/standards-body essay; canonical. STRING-VERIFIED (control rejected).
- "What makes a cool URI?" "A cool URI is one which does not change." "What sorts of URI change?" "URIs don't change: people change them."
- "There are no reasons at all in theory for people to change URIs (or stop maintaining documents), but millions of reasons in practice."
- Excuse headings, in order. Verified individually: "We just reorganized our website to make it better." / "I didn't think URLs have to be persistent - that was URNs." / "We would like to, but we just don't have the right tools." SINGLE PASS: "We have so much material that we can't keep track of what is out of date and what is confidential and what is valid and so we thought we'd better just turn the whole lot off." / "Well, we found we had to move the files..." / "We used to use a cgi script for this and now we use a binary program."
- "It is the duty of a Webmaster to allocate URIs which you will be able to stand by in 2 years, in 20 years, in 200 years." (STRING-VERIFIED; first sentence of "So what should I do? Designing URIs".)
- What to leave out of a URI (SINGLE PASS list): authors name, subject, status, access, file name extension, software mechanisms, disk name.
Role: the founding statement that address stability is a publisher's decision, not a technical accident.

1b. RFC 7089, "HTTP Framework for Time-Based Access to Resource States -- Memento" (Van de Sompel, Nelson, Sanderson; December 2013; Informational). https://www.rfc-editor.org/rfc/rfc7089
IETF RFC. STRING-VERIFIED (control rejected).
- Abstract: "The HTTP-based Memento framework bridges the present and past Web." "It facilitates obtaining representations of prior states of a given resource by introducing datetime negotiation and TimeMaps." "The framework also facilitates recognizing a resource that encapsulates a frozen prior state of another resource."
- "A Memento for an Original Resource is a resource that encapsulates a prior state of the Original Resource."
- "A TimeGate for an Original Resource is a resource that is capable of datetime negotiation to support access to prior states of the Original Resource."
- SINGLE PASS: "A TimeMap for an Original Resource is a resource from which a list of URIs of Mementos of the Original Resource is available." Headers: Accept-Datetime (request), Memento-Datetime (response).
Role: the standard vocabulary for "a frozen prior state of a resource", which is exactly what a citable dashboard state is.

1c. Perma: "Scoping and Addressing the Problem of Link and Reference Rot in Legal Citations", 127 Harv. L. Rev. F. 176 (2014). https://harvardlawreview.org/forum/vol-127/perma-scoping-and-addressing-the-problem-of-link-and-reference-rot-in-legal-citations/
Law-review empirical study. STRING-VERIFIED (control rejected).
- "more than 70% of the URLs within the above mentioned journals, and 50% of the URLs within U.S. Supreme Court opinions suffer reference rot" ... "meaning, again, that they do not produce the information originally cited"
- "Our finding is that 49.9% of the links cited in the Supreme Court opinions no longer had the cited material."
- "only 29.9% of the HRJ links, 26.8% of the HLR links, and 34.2% of the JOLT links contained the material cited"
- Bases (SINGLE PASS): Harvard Law Review, Harvard Journal of Law & Technology and Harvard Human Rights Journal, from 1999, 1996 and 1997 respectively to 2012; 555 Supreme Court hyperlinks, 1996 to October Term 2011. Journal link counts given by the reader (5,911 HLR; 2,358 HRJ; 5,428 JOLT) are unverified.
- Definition (SINGLE PASS): "Link rot refers to the URL no longer serving up any content at all. Reference rot, an even larger phenomenon, happens when a link still works but the information referenced by the citation is no longer present, or has changed."
- Caveats: the oft-quoted abstract wording "do not link to the originally cited information" is NOT in the Forum text. The reader gave the byline order as Lessig, Zittrain, Albert on both passes; the usual citation is Zittrain, Albert & Lessig. Check before printing.

1d. Klein et al. 2014, "Scholarly Context Not Found: One in Five Articles Suffers from Reference Rot", PLoS ONE (26 December 2014). https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253
Peer-reviewed, very large corpus. STRING-VERIFIED (control rejected).
- "For over one million references to web resources extracted from over 3.5 million articles"; three corpora (arXiv, Elsevier, PMC), publication years 1997 to 2012.
- "We find one out of five STM articles suffering from reference rot"; among articles with web references "this fraction increases to seven out of ten".
- Definitions (SINGLE PASS): link rot: "The resource identified by a URI may cease to exist and hence a URI reference to that resource will no longer provide access to referenced content." Content drift: "The resource identified by a URI may change over time and hence, the content at the end of the URI may evolve, even to such an extent that it ceases to be representative of the content that was originally referenced."

1e. Jones et al. 2016, "Scholarly Context Adrift: Three out of Four URI References Lead to Changed Content", PLoS ONE (2 December 2016). https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0167475
Peer-reviewed. STRING-VERIFIED (control rejected).
- "we use 19 web archives"; "We find that representative snapshots exist for about 30% of all URI references."
- "We find that for over 75% of references the content has drifted away from what it was when referenced."
- "the content on the live web has drifted away from the content that was originally referenced for three out of four references (184,065 out of 241,091, which equals 76.35%)."
- SINGLE PASS: "even for articles published in 2012 only about 25% of referenced resources remain unchanged by August of 2015"; about 10% for 2003 to 2005.
Role: content drift is the dashboard problem. The link still works; the numbers behind it have changed.

1f. Pew Research Center, "When Online Content Disappears" (Chapekis, Bestvater, Remy, Rivero; 17 May 2024). https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/
Research-organisation measurement. STRING-VERIFIED (control "61% of government webpages" rejected).
- "A quarter of all webpages that existed at one point between 2013 and 2023 are no longer accessible, as of October 2023."
- "38% of webpages that existed in 2013 are not available today, compared with 8% of pages that existed in 2023."
- "23% of news webpages contain at least one broken link, as do 21% of webpages from government sites"; "Overall, 21% of all the government webpages we examined contained at least one broken link."
- "54% of Wikipedia pages contain at least one link in their "References" section that points to a page that no longer exists."
- SINGLE PASS bases: "We sampled around 500,000 pages from government websites using the Common Crawl March/April 2023 snapshot of the internet, including a mix of different levels of government (federal, state, local and others)."; of the links on them "6% point to pages that are no longer accessible."; "Local-level government webpages (those belonging to city governments) are especially likely to have broken links." The decade samples are from Common Crawl (about 90,000 pages per year, per the reader).
- Note: these are US government pages. I found no UK equivalent.

1g. UK Government Web Archive (The National Archives).
About page: https://www.nationalarchives.gov.uk/webarchive/about/ STRING-VERIFIED (control rejected).
- "We carry out web archiving to preserve the websites and some social media accounts of central government."
- "We started archiving in 2003 but some of our archived websites go as far back as 1996."
- "Since then, we have archived over 6,000 websites and we continuously add new archive snapshots to the collection, at a current rate of around 100 a month."
- "The archived materials are kept in the web archive and can be accessed online by anyone."
How-to-use page: https://www.nationalarchives.gov.uk/webarchive/information/ STRING-VERIFIED (control rejected).
- "Interactive content usually cannot be archived." "Some examples would be: interactive maps, site search, contact forms, and some interactive animations."
- "links from archived websites to other non-government websites usually don't work"
- NOT FOUND: any "how to cite an archived page" statement or explanation of the timestamped URL pattern on either page. Both point users to a bookmarklet and the Memento browser plug-in.
Role: the national archive of record states that it generally cannot capture interactive content. A dashboard cannot rely on web archiving for citability.

==================================================
ITEM 2. DATA CITATION AND IDENTIFIERS
==================================================

2a. FORCE11 Joint Declaration of Data Citation Principles (Data Citation Synthesis Group; Martone M., ed.; San Diego: FORCE11, 2014). https://force11.org/info/joint-declaration-of-data-citation-principles-final/
Community standard, widely endorsed. STRING-VERIFIED (control rejected).
Headings exactly: 1. Importance; 2. Credit and Attribution; 3. Evidence; 4. Unique Identification; 5. Access; 6. Persistence; 7. Specificity and Verifiability; 8. Interoperability and Flexibility.
- Preamble: "Sound, reproducible scholarship rests upon a foundation of robust, accessible data."
- 1: "Data should be considered legitimate, citable products of research."
- 3: "In scholarly literature, whenever and wherever a claim relies upon data, the corresponding data should be cited."
- 4: "A data citation should include a persistent method for identification that is machine actionable, globally unique, and widely used by a community."
- 6: "Unique identifiers, and metadata describing the data, and its disposition, should persist — even beyond the lifespan of the data they describe."
- 7: "Data citations should facilitate identification of, access to, and verification of the specific data that support a claim." ... "sufficient to facilitate verifying that the specific timeslice, version and/or granular portion of data retrieved subsequently is the same as was originally cited."
- Principles 2, 5 and 8 full texts are SINGLE PASS; the headings are verified.
Role: principle 7 ("timeslice, version and/or granular portion") is the standard that a cited dashboard state has to meet.

2b. DataCite, "Versioning". https://support.datacite.org/docs/versioning
Registration-agency practitioner documentation. STRING-VERIFIED (control rejected).
- "For major content changes, we recommend assigning a new DOI and linking the new DOI to the previous DOI with related identifiers."
- "For minor content changes, the same DOI may be used with updated metadata." "A new DOI is not required."
- SINGLE PASS: relation types IsNewVersionOf / IsPreviousVersionOf / HasVersion / IsVersionOf; the page defers to the Metadata Schema for "Citation of Dynamic Datasets".
- DataCite "DOI basics" (https://support.datacite.org/docs/doi-basics), SINGLE PASS: "A DOI is a digital identifier of an object, any object — physical, digital, or abstract."; "a DOI string cannot be changed or deleted once it has been registered in the Global Handle server."

2c. RDA Working Group on Data Citation, "Data Citation of Evolving Data: Recommendations of the Working Group on Data Citation (WGDC)" (Rauber, Asmi, van Uytvanck, Pröll; 20 October 2015; 4 pages). https://www.rd-alliance.org/wp-content/uploads/2024/05/RDA-DC-Recommendations_151020.pdf (landing page: https://www.rd-alliance.org/group/data-citation-wg/outcomes/data-citation-recommendation.html)
RDA-endorsed recommendation. STRING-VERIFIED for the heading list and the sentences marked * (two controls rejected); the rest SINGLE PASS.
Headings exactly: R1 – Data Versioning; R2 – Timestamping; R3 – Query Store Facilities; R4 – Query Uniqueness; R5 – Stable Sorting; R6 – Result Set Verification; R7 – Query Timestamping; R8 – Query PID; R9 – Store Query; R10 – Automated Citation Texts; R11 – Landing Page; R12 – Machine Actionability; R13 – Technology Migration; R14 – Migration Verification.
Group headings: "Preparing the Data and the Query Store"; "Persistently Identify Specific Data Sets"; "Resolving PIDs and Retrieving the Data"; "Upon Modifications to the Data Infrastructure".
- *R1: "Apply versioning to ensure earlier states of data sets can be retrieved."
- *R2: "Ensure that operations on data are timestamped, i.e. any additions, deletions are marked with a timestamp."
- *R3: "Provide means for storing queries and the associated metadata in order to re-execute them in the future."
- *R5: "Ensure that the sorting of the records in the data set is unambiguous and reproducible"
- *R6: "Compute fixity information (checksum) of the query result set" (continues: "to enable verification of the correctness of a result upon re-execution.")
- *R8: "Assign a new PID to the query if either the query is new or if the result set returned from an earlier identical query is different due to changes in the data."
- *R10: "Generate citation texts in the format prevalent in the designated community for lowering the barrier for citing the data."
- R11 (first clause verified): "Make the PIDs resolve to a human readable landing page" (continues, SINGLE PASS: "that provides the data (via query re-execution) and metadata, including a link to the superset (PID of the data source) and citation text snippet.")
- *Summary: "Instead of providing static data exports or textual descriptions of data subsets, we support a dynamic, query centric view of data sets." ... "identifying data sets by storing and assigning persistent identifiers (PIDs) to timestamped queries that can be re-executed against the timestamped data store."
- SINGLE PASS: "It allows identifying, retrieving and citing the precise data set with minimal storage overhead by only storing the versioned data and the queries used for creating the data set."
Role: the closest thing to a standard for "cite a state". A citable state is a stored, timestamped query over versioned data, plus a checksum and a landing page.

2d. Digital Curation Centre, "How to Cite Datasets and Link to Publications" (Ball & Duke; published 18 October 2011, last updated 30 July 2015 per the reader). https://www.dcc.ac.uk/guidance/how-guides/cite-datasets
UK practitioner guide. STRING-VERIFIED (control rejected).
- "If a dataset exists in several versions, be sure to cite the exact version you used."
- "The most important of these elements – the ones that should be present in any citation – are the author, the title and date, the location, and the publisher."
- Three ways to make dynamic data citable: "With the time slice approach, the citable entity is the set of updates made to a dataset during a particular time period." / "At regular intervals or at the request of a citing author, a snapshot is taken of the entire dataset and made citable." / "The citable entity is the result of a particular query on a dataset run at a certain time." (labelled partial snapshots)
- "The recommendation of the Research Data Alliance Working Group on Data Citation (RDA WGDC) is however to use partial snapshots." (SINGLE PASS)
- UK Data Service and ONS dataset-citation guidance: UNREACHABLE (two 404s on UKDS); nothing quoted. The DCC guide is the UK substitute.

==================================================
ITEM 3. HOW PUBLIC DASHBOARDS VERSION, ARCHIVE AND LET READERS CITE A STATE
==================================================

3a. Our World in Data. Case; current practice.
Test URL: https://ourworldindata.org/grapher/life-expectancy?time=1950..2020&country=~GBR
- State in the URL: confirmed. The page's og:url is "https://ourworldindata.org/grapher/life-expectancy?country=~GBR&time=1950..2020", the preview image is "life-expectancy.png?country=~GBR&time=1950..2020", and the filtered download link carries "csvType=filtered&useColumnShortNames=false&country=~GBR&time=1950..2020". (Reader-reported snippets; presence of "country=~GBR" verified.)
- Cite block, STRING-VERIFIED (control rejected): "To cite this page overall, including any descriptions, FAQs or explanations of the data authored by Our World in Data, please use the following citation:" and "If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:".
- The full citation ends "Retrieved October 6, 2026 from https://archive.ourworldindata.org/20260910-005924/grapher/life-expectancy.html" followed by "archived on September 10, 2026" (URL and "Retrieved October 6, 2026 from" verified; the reader disagreed with itself on round versus square brackets). So the citation carries the retrieval date and points to a dated archive snapshot, not the live URL. The archive URL in the citation does NOT carry the reader's ?time/?country selection.
- Downloads: "Download full data" ("Includes all entities and time points") and "Download displayed data" ("Includes only the entities and time points currently visible in the chart", verified). "Data API" section (SINGLE PASS): "Use these URLs to programmatically access this chart's data and configure your requests with the options below."; e.g. https://ourworldindata.org/grapher/life-expectancy.csv?v=1&csvType=full&useColumnShortNames=false and .metadata.json. The page also showed "Last updated: 2025-10-22" and "Next expected update: 2026-10-22" (SINGLE PASS).
- Archived page (https://archive.ourworldindata.org/20260910-005924/grapher/life-expectancy.html): banner "Archive September 10, 2026 at 00:59 UTC", with "Go to the previous version" (linking to .../20260904-080400/...), "Go to the next version" and "Go to the live version". ("Go to the live version" and the previous-version link verified; control rejected.)
- OWID's own statement: Gerber & Giattino, "New feature: embed archived versions of our interactive charts in your website" (9 July 2025). https://ourworldindata.org/new-feature-embed-archived-charts STRING-VERIFIED (control rejected).
  "Our citation instructions now point to archived versions of charts, to ensure that any data points you are referring to in the cited chart remain stable and unchanged."
  "The new archived versions, in contrast, will never change or update, offering you more control over how our charts appear on your site."
  Why (SINGLE PASS for the first clause): "But we've heard from others that they'd prefer to have an option where the chart didn't change; for instance, when referring to specific data points in an article."
  Archived embed: "will always show the exact data, text, and other content as it does on the day of embedding; it is frozen in time"; "will not be deleted"; and (SINGLE PASS) "may contain outdated data that has since been updated in the live version of the chart, or data that has since been found to contain quality issues."
  Live embed (SINGLE PASS): "will likely change in the future"; "in rare cases may be deleted; for example, if we decide that the data quality is no longer up to our standards".
- FAQ (https://ourworldindata.org/faqs), STRING-VERIFIED: "you can choose between a live embed that always reflects our latest data updates, or an archived embed that will never change or update"; "The iframe code (and URL) will adapt to the selections that you make on the chart."; "To cite one of our charts, cite the page that it's found on or that is linked to at the bottom of the chart."
- Chart API docs (https://docs.owid.io/projects/etl/api/chart-api/), practitioner documentation, SINGLE PASS: "Once you've found the chart with the data you need, simply append ".csv" to the URL to download the data or ".metadata.json" to retrieve the metadata."
Role: the fullest working model found. It has three layers: URL parameters for the selection, a dated immutable archive for the data and text, and a citation block that names the archive and the retrieval date.

3b. ONS.
- Versions list: https://www.ons.gov.uk/datasets/wellbeing-quarterly/editions/time-series/versions STRING-VERIFIED (control "Version 12" rejected). Heading "All versions of Quarterly personal well-being estimates time-series dataset"; nine versions, each with a date, "Version: n" and xls/csv/csvw downloads; version 9 (28 November 2023) marked "(latest)"; a "Corrections" label and "View superseded version" links on earlier ones. URL pattern .../editions/time-series/versions/9; downloads at download.ons.gov.uk/downloads/datasets/.../versions/9.csv. No reason text accompanies the correction labels on that page.
- Revisions policy: "The Office for National Statistics' Revisions Policy and Correction of Errors Policy" (reader gives last revised 9 August 2024). https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions/guidetostatisticalrevisions STRING-VERIFIED (control rejected).
  "Revisions are updates to previously published statistics, analysis or data that improve quality by incorporating improved methods, additional data sources or statistics that were unavailable at the point of initial publication."
  "Revisions are usually reported in the next release of the data by including a notice within the latest release."
  "Correction of errors are amendments that are made to published statistics in response to the identification of mistakes following their initial publication."
  "Correction of errors are reported at the top of the affected release in a blue collapsible banner titled 'Correction'."
  SINGLE PASS: "The fact that the publication has been updated is clearly stated with details of when and why the change was made."
  The page says nothing about where superseded versions are kept.
- Explore local statistics: the old beta host redirects to https://www.ons.gov.uk/explore-local-statistics/areas/[GSS code]-[name]. The area is in the URL path, with sub-paths such as /indicators. Links out to other ONS tools also carry the area code as a query string, hash or path (e.g. /census/maps/?lad=[code]; /visualisations/customprofiles/build/#[code]). The reader found no "share", "embed" or "download" wording on the area page. SINGLE PASS; read for URL structure only.

3c. GOV.UK.
- Publisher guidance, "Retire outdated content". https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/retire-content/ (the old gov.uk/guidance/content-design URL redirects here). STRING-VERIFIED (control rejected): "withdraw the content - this keeps the content on the site, but it does not appear in internal search results and there'll be a banner to it to explain that the content is no longer current". SINGLE PASS: "The exceptions to these rules are fatality notices and statistics, which are never eligible for history mode"; "Unpublished content will go into an 'unpublished' state in Whitehall publisher." The page does not mention The National Archives' web archive as part of the process.
- Live example of the convention (read for convention only): https://www.gov.uk/government/publications/covid-19-stay-at-home-guidance STRING-VERIFIED (control rejected): banner "This publication was withdrawn on 24 February 2022"; heading "Updates to this page"; control "Show all updates"; dated change notes down to "12 March 2020 First published." (the reader counted 65 entries).
- The statistics release finder labels each entry with a document type ("Official Statistics" / "Accredited official statistics") and a release state (confirmed / cancelled). SINGLE PASS.

3d. UKHSA data dashboard.
- https://ukhsa-dashboard.data.gov.uk/access-our-data STRING-VERIFIED (control rejected): "The UKHSA data dashboard API is designed to support developers and other users to easily extract and save data, that is present in the dashboard." "It allows for easy access to data, integration with software, tailed responses for each use case." [sic: "tailed"]
- https://ukhsa-dashboard.data.gov.uk/bulk-downloads SINGLE PASS: "You can download all the data from the UKHSA data dashboard charts on this page by clicking the Download button."
- Topic page: chart tabs "Chart", "Tabular data", "Download" (CSV / JSON); "Last updated on Thursday, 1 October 2026 at 04:00pm"; under each chart "Up to and including 30 Sep 2026" (SINGLE PASS).
- Is a state linkable? Yes for area selection. A URL with ?areaType=UKHSA+Region&areaName=North+West returned a page headed "COVID-19 in North West", and ?areaType=Nation&areaName=England returned "COVID-19 in England". One test each. I found no versioned or archived snapshot of a chart and no cite block.

3e. Shareable state URLs: sources.
- Heer, Viégas & Wattenberg 2007, "Voyagers and Voyeurs: Supporting Asynchronous Collaborative Information Visualization" (CHI 2007). https://idl.cs.washington.edu/files/2007-sense.us-CHI.pdf Peer-reviewed system paper. STRING-VERIFIED (control rejected).
  "The browser's location bar always displays a URL that links to the current state of the visualization, defined by the settings of filtering, navigation, and visual encoding parameters."
  "the browser's back and forward buttons are tied to the visualization state, allowing easy navigation to previously seen views."
  "These different parameter settings result in different URLs, and yet provide exactly the same visualization view."
  "they must be able to share what they are seeing to establish a common ground for conversation"
  Studies: a pilot with 6 subjects, then 12, then a further 12 (SINGLE PASS).
  Role: the peer-reviewed origin of "state as URL", including its known snag that many URLs can map to one view.
- Shiny, "Bookmarking state" (Winston Chang; 15 October 2019 per the reader). https://shiny.posit.co/r/articles/share/bookmarking-state/ Practitioner documentation. Verified on the YES/NO pass (control rejected):
  "As of version 0.14, users can save the state of an application and get a URL which will restore the application with that state."
  "There are two types of bookmarking: encoding the state in a URL, and saving the state to the server."
  "Some browsers have a limit of about 2,000 characters for the length of a URL, so if the bookmark URL is longer than that, it will not work properly in those browsers."
- Vega editor permalinks: UNREACHABLE (JavaScript-only). Observable docs: 404.

==================================================
ITEM 4. THE DATA-TO-DISPLAY SEPARATION
==================================================

4a. Wilkinson. The Springer page for the 2005 book was refused (429), so nothing is quoted from it. Reachable substitute: Wilkinson, "The Grammar of Graphics", in Gentle, Härdle & Mori (eds), Handbook of Computational Statistics (Springer, 2012), pp. 375–414. https://link.springer.com/chapter/10.1007/978-3-642-21551-3_13 ABSTRACT, STRING-VERIFIED (control rejected):
- "The Grammar of Graphics, or GOG, denotes a system with seven orthogonal components. By orthogonal, we mean there are seven graphical component sets whose elements are aspects of the general system and that every combination of aspects in the product of all these sets is meaningful."
The seven are not named on the reachable page.

4b. Wickham 2010, "A Layered Grammar of Graphics", Journal of Computational and Graphical Statistics 19(1): 3–28. https://vita.had.co.nz/papers/layered-grammar.pdf Peer-reviewed. STRING-VERIFIED (control rejected).
- "A grammar of graphics is a tool that enables us to concisely describe the components of a graphic."
- "Data are obviously a critical part of the plot, but it is important to remember that they are independent from the other components: we can construct a graphic that can be applied to multiple datasets."
- "Data are what turns an abstract graphic into a concrete graphic."
- Components (SINGLE PASS apart from the first clause): "a default dataset and set of mappings from variables to aesthetics, one or more layers, with each layer having one geometric object, one statistical transformation, one position adjustment, and optionally, one dataset and set of aesthetic mappings, one scale for each aesthetic mapping used, a coordinate system, the facet specification."
Role: the cleanest published sentence that the data are independent of the specification.

4c. Satyanarayan, Moritz, Wongsuphasawat & Heer 2017, "Vega-Lite: A Grammar of Interactive Graphics", IEEE TVCG (Proc. InfoVis). https://idl.cs.washington.edu/files/2017-VegaLite-InfoVis.pdf (abstract: https://idl.uw.edu/papers/vega-lite) Peer-reviewed. STRING-VERIFIED (controls rejected).
- "We present Vega-Lite, a high-level grammar that enables rapid specification of interactive data visualizations."
- "Users specify interactive semantics by composing selections." "In Vega-Lite, a selection is an abstraction that defines input event processing, points of interest, and a predicate function for inclusion testing." "Selections parameterize visual encodings by serving as input data, defining scale extents, or by driving conditional logic."
- §3.1: "A unit specification describes a single Cartesian plot, with a backing data set, a given mark-type, and a set of one or more encoding definitions for visual channels such as position (x, y), color, size, etc." Formal line: "unit := (data, transforms, mark-type, encodings)". The tuple does not itself contain selections; they are defined in §4 as "selection := (name, type, predicate, domain|range, event, init, transforms, resolve)".
- §4: "Selections identify the set of points a user is interested in manipulating."
- §4.3: "Once selections are defined, they parameterize visual encodings to make them interactive — visual encodings are automatically re-evaluated as selections change."
- SINGLE PASS: "Vega-Lite uses a portable JSON (JavaScript Object Notation) syntax that permits generation from a variety of programming languages."
- Vega-Lite docs (https://vega.github.io/vega-lite/docs/spec.html), SINGLE PASS: "Vega-Lite specifications are JSON objects that describe a diverse range of interactive visualizations."

4d. Bostock, Ogievetsky & Heer 2011, "D3: Data-Driven Documents", IEEE TVCG (Proc. InfoVis). https://idl.cs.washington.edu/files/2011-D3-InfoVis.pdf Peer-reviewed. STRING-VERIFIED (control rejected).
- "With D3, designers selectively bind input data to arbitrary document elements, applying dynamic transforms to both generate and modify content."
- §3.2: "The data operator binds input data to selected nodes." "By default, data is joined to elements by index: the first element to the first datum, and so on." "If data or elements are leftover after computing the data join, these are available in the enter and exit subselections, respectively." "The delineation of enter, update and exit allows precise control of the element lifecycle."
- SINGLE PASS: "Operator values are specified either as constants or functions; the latter are evaluated for each element."

The point documented: Wickham makes data independent of the specification. Vega-Lite makes the view a compiled function of (data, transforms, mark, encodings) with encodings re-evaluated "as selections change". sense.us defines the current state as "the settings of filtering, navigation, and visual encoding parameters". Taken together, a state is reproducible from the data version, the specification and the selection values. That last sentence is my synthesis; no single source states it.

==================================================
ITEM 5. MISSING AND WITHHELD DATA ON A CHART
==================================================

5a. Song & Szafir, "Where's My Data? Evaluating Visualizations with Missing Data", IEEE TVCG 25(1): 914–924 (online August 2018). DOI 10.1109/TVCG.2018.2864914. ABSTRACT ONLY, from the OpenAlex record (https://api.openalex.org/works/doi:10.1109/TVCG.2018.2864914), phrase-verified:
- "We conducted a pair of crowdsourced studies to measure how the methods used to impute and visualize missing data may influence analysts' perceptions of data quality and their confidence in their conclusions."
- "Our experiments used different design choices for line graphs and bar charts to estimate averages and trends in incomplete time series datasets."
- "Our results provide preliminary guidance for visualization designers to consider when working with incomplete data in different domains and scenarios."
NOT REACHED: n, the imputation and encoding conditions, and the direction of the findings (which encodings made readers notice missingness and which hid it). No open full text was found. Do not state those findings from memory; the chapter needs the paper itself.

5b. Sarma, Guo, Hoffswell, Rossi, Du, Koh & Kay, "Evaluating the Use of Uncertainty Visualisations for Imputations of Data Missing At Random in Scatterplots", IEEE TVCG (Proc. VIS 2022). https://mucollective.northwestern.edu/files/2022-uncertainty-vis-for-imputations.pdf Peer-reviewed. STRING-VERIFIED (control rejected).
- "Most real-world datasets contain missing values yet most exploratory data analysis (EDA) systems only support visualising data points with complete cases." "This omission may potentially lead the user to biased analyses and insights."
- n: "conduct a crowdsourced study with 202 participants" (abstract). Body (SINGLE PASS): "We recruited a total of 210 participants (35 participants for each between-subjects treatment), using the prolific.co platform, between Oct 10th and Oct 17th 2021."; US residents, all but one with a college degree; datasets with 30% and 50% of observations missing at random.
- Conditions: no imputation (baseline), mean, 95% confidence intervals, probability density plots, gradient intervals, hypothetical outcome plots. Tasks: estimate an average; estimate a trend. Measures: bias, precision, confidence.
- "In the average estimation task, when compared to a baseline of no imputation, we find that all uncertainty representations reduced bias (desirable), but may also reduce precision (undesirable)."
- Abstract: "When estimating averages, uncertainty representations may reduce bias but at the cost of decreasing precision. When estimating trend, only hypothetical outcome plots may lead to a small probability of reducing bias while increasing precision."
- SINGLE PASS: "an average participant will exhibit the greatest magnitude of bias in the no imputation (baseline) condition."; "participants in every uncertainty representation were less certain about their response when compared to the baseline."
Role: showing only complete cases biased readers most. Showing imputed values with uncertainty reduced bias but lowered both precision and confidence.

5c. Andreasson & Riveiro, "Effects of Visualizing Missing Data: An Empirical Evaluation", 18th International Conference on Information Visualisation (iV 2014), pp. 132–138. DOI 10.1109/IV.2014.77. ABSTRACT ONLY (OpenAlex record, phrase-verified; control rejected):
- "A comparison between three visualization techniques: (1) emptiness, (2) fuzziness, and (3) emptiness plus explanation, revealed that the latter technique induced significantly higher degree of decision-confidence than the visualization technique fuzziness."
- "Moreover, emptiness plus explanation yield the highest number of risky choices of the three."
n is not stated in the abstract; full text unreachable.
Role: explaining a gap raised decision confidence relative to blurring it, and also raised risk-taking.

5d. Analysis Function, "Data visualisation: charts" (reader gives 19 May 2022). https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ The URL stands and the rule stands. Government guidance. STRING-VERIFIED (control rejected). Under "Breaks in time series":
- "Breaks in time series can occur due to missing data points and changes in methods." ... "But, it must always be highlighted."
- "Do not join the points either side of the missing data point, even if the line is dotted or dashed."
- "You do not always have to use a line for a time series with a discontinuity. Displaying the data as individual points may be better."

==================================================
ITEM 6. PROVENANCE AND SOURCE CUES: TRUST EVIDENCE
==================================================

6a. Xiong, Padilla, Grayson & Franconeri 2019, "Examining the Components of Trust in Map-Based Visualizations" (EuroVis TrustVis workshop). DOI 10.2312/trvis.20191186. ABSTRACT ONLY (OpenAlex record; PDF unreachable). n is not in the abstract.
- Design per the abstract: four transparency dimensions (accuracy, clarity, disclosure, thoroughness) and a crisis decision task choosing between map applications with less or more information.
- Phrase-verified: "disclosure significantly predicted individuals' selection of a Google Maps-like application with either less or more information"; "Trust in perceived accuracy did not significantly predict which navigation application participants decided to use".
- It is a preliminary workshop paper. It does NOT test source or visual-style cues.

6b. Elhamdadi, Gaba, Kim & Xiong 2022, "How Do We Measure Trust in Visual Data Communication?" (BELIV). https://arxiv.org/pdf/2209.14276 Position/review paper. Abstract SINGLE PASS:
- "Computer science and data visualization researchers have not yet reached a consensus on a trust definition or metric, which are essential to building a comprehensive trust model in human-data interaction." (The reader's text had "humandata"; hyphenation as printed is unconfirmed.)
- "Specifically, we discuss quantitative surveys from social sciences, trust games from behavioral economics, measuring trust through measuring belief updating, and measuring trust through perceptual methods."
Scope: methods only, no new data. It cautions that any single-item "trust" finding rests on an unsettled measure.

6c. Mayr, Hynek, Salisu & Windhager 2019, "Trust in Information Visualization" (EuroVis TrustVis). https://diglib.eg.org/bitstream/handle/10.2312/trvis20191187/025-029.pdf Position paper. STRING-VERIFIED (control rejected).
- "Trust is an important factor that mediates whether a user will rely and build on the information displayed in a visualization." "But they might also use superficial cues as indicators for trust."
- "Trustworthiness, on the one side, refers to the properties of the visualization (and the underlying data) that lead users to trust it." "Trust perception, on the other side, is the user's subjective evaluation of the quality and reliability of the visualized information."
- Factors (SINGLE PASS): "Factors that influence the trustworthiness of information are its accuracy (free from error), currency (up-to-dateness), coverage (completeness), objectivity (unbiasedness and availability of multiple perspectives), as well as its validity and predictability [KFW08]."
- "Disclosure of the underlying data and the designers' decisions about data, representation, and interaction can increase trustworthiness."
- "Also design factors like usability and user experience (such as a positive look and feel) can increase trust [CDHP11]."
- Listed user-side factors (reader summary): prior knowledge and familiarity, coherence, disposition to trust, need for cognition, perceived risk.

6d. Kennedy, Hill, Aiello & Allen 2016, "The work that visualisation conventions do", Information, Communication & Society 19(6): 715–735. Accepted manuscript: https://eprints.whiterose.ac.uk/93521/3/repository20.pdf Peer-reviewed, qualitative/semiotic. STRING-VERIFIED (control rejected).
- "We focus on four conventions which imbue visualisations with a sense of objectivity, transparency and facticity." "These include: a) two-dimensional viewpoints; b) clean layouts; c) geometric shapes and lines; d) the inclusion of data sources."
- "The inclusion of data sources also does other, persuasive work." "It suggests that the designer feels confident that s/he has been truthful to the data, and this in turn suggests that there may be no need for the user to check."
- SINGLE PASS: "the inclusion of data sources performs the rhetorical, persuasive work of ascribing transparency and trustworthiness to visualisations"; "People who are not specialists in data are unlikely to be able make sense of raw data anyway".
- Method (SINGLE PASS): "Skype interviews with 13 visualisations designers" and "detailed social semiotic analysis of 10 visualisations circulating in the media".
Role: the critical counterweight. A source line signals transparency whether or not anyone can follow it.

6e. Peck, Ayuso & El-Etr 2019, "Data is Personal: Attitudes and Perceptions of Data Visualization in Rural Pennsylvania" (CHI 2019). https://arxiv.org/pdf/1901.01920 Peer-reviewed, qualitative. STRING-VERIFIED (control rejected). Read for method and the source finding only.
- "In 42 semi-structured interviews in rural Pennsylvania (USA), we find that a complex set of factors intermix to inform attitudes and perceptions about data visualization" ... "including educational background, political affiliation, and personal experience"
- Sample (SINGLE PASS): "Staff members at a local university (13)"; "Employees at a local construction site (5)"; "Visitors of a local farmers market (24)". Task: rank 10 charts, then re-rank after the sources were revealed.
- "17 of 42 participants changed their rankings after the sources of the data visualizations were revealed." "25 of 42 participants opted to keep their initial rankings."
- "The graphs most commonly ranked higher - C: National Institute on Drug Abuse (NIDA), E: Drexel University, and G: National Vital Statistics System (NVSS) - all came from academic or government sources that were heavily criticized in the first set of rankings."
- "The most recurring theme in our analysis were decisions framed or driven by personal experience."
Role: revealing the source moved rankings for 17 of 42 people and did not for 25. The effect of source varied by person.

6f. Lin & Thornton, preprint posted 17 December 2021 on PsyArXiv, DOI 10.31234/osf.io/dnr9s; current title "Visualization aesthetics influence trust in science, news, and social media". Crossref record: https://api.crossref.org/works/10.31234/osf.io/dnr9s ABSTRACT, STRING-VERIFIED (control rejected). Preprint: Crossref lists no journal version.
- "Across five-preregistered studies (3,405 participants, 1,219 graphs)"
- "graph beauty predicts increased trust in real-world graphs across three important domains: social media, news, and scientific publications"
- "observed that doing so causally increased trust (Study 5)"
- "This effect was fully mediated by people's inferences of the general competence of the graph maker"
- SINGLE PASS: "Visualization aesthetics may vary independent of data quality."
Role: aesthetics raise trust independently of data quality, through inferred competence of the maker. It is the strongest quantitative item in this section, but it is not peer-reviewed as far as the record shows.

==================================================
ITEM 7. MAPS THAT DO NOT STIGMATISE
==================================================

7a. Monmonier, How to Lie with Maps, 3rd edition (University of Chicago Press, April 2018, 256 pp.). https://press.uchicago.edu/ucp/books/book/chicago/H/bo27400568.html Publisher description only. STRING-VERIFIED (control "Maps never lie." rejected).
- "An instant classic when first published in 1991, How to Lie with Maps revealed how the choices mapmakers make—consciously or unconsciously—mean that every map inevitably presents only one of many possible stories about the places it depicts."
- "The principles Mark Monmonier outlined back then remain true today, despite significant technological changes in the making and use of maps."
- Chapter 3 title on the page: "Map Generalization: Little White Lies and Lots of Them".

7b. ColorBrewer scheme definitions (Brewer). https://colorbrewer2.org/learnmore/schemes_full.html Practitioner reference by a cartographic researcher. STRING-VERIFIED (control rejected), except the diverging sentence, where the checker returned NO while quoting the identical sentence back; treat that one as SINGLE PASS.
- "Sequential schemes are suited to ordered data that progress from low to high." "Lightness steps dominate the look of these schemes, with light colors for low data values to dark colors for high data values."
- "Diverging schemes put equal emphasis on mid-range critical values and extremes at both ends of the data range."
- "Qualitative schemes do not imply magnitude differences between legend classes, and hues are used to create the primary visual differences between classes." "Qualitative schemes are best suited to representing nominal or categorical data."

7c. Brewer & Pickle 2002, "Evaluation of Methods for Classifying Epidemiological Data on Choropleth Maps in Series", Annals of the Association of American Geographers 92(4): 662–681. DOI 10.1111/1467-8306.00310. ABSTRACT ONLY (OpenAlex record, phrase-verified; control rejected).
- "We compared seven methods using responses by fifty-six subjects in a two-part experiment involving nine series of U.S. mortality maps."
- "Quantiles and minimum boundary error methods were best suited for these general map-reading tasks."
- "Using matched legends across series (when possible) increased map-comparison accuracy by approximately 28 percent."
- "The advantages of careful optimization procedures in classification seem to offer no benefit over the simpler quantile method for the general map-reading tasks tested in the reported experiment."
- The abstract also puts natural breaks (Jenks) and a hybrid equal-interval method in a second group at "less than 70 percent" as accurate as quantiles. The exact wording of that clause did not verify; do not quote it.

7d. Normalisation rule.
- ONS Service Manual, "Choropleth maps". https://service-manual.ons.gov.uk/data-visualisation/chart-types/choropleth-maps Design system. STRING-VERIFIED (control rejected).
  "Choropleth maps should display data as standardised rates, not absolute values." "For instance, use the unemployment rate (percentage of the population unemployed in each area) rather than the total number of unemployed people in each area." "Using absolute values can be misleading because they are distorted by the size of the area."
  "Typically, use a scale with five discrete colour bands for choropleth maps."
  "The standard method we use for setting breaks is the Jenks natural breaks, which creates an effective visualisation with most datasets."
  "Consider a map if you have data values for geographic areas and the pattern in the data you want to show is primarily geographic"
  "Avoid using a map if you only have data for a few geographic areas, such as the four nations of the UK or the nine regions of England."
  The page says nothing on missing or suppressed areas, hex maps or cartograms.
- Esri ArcGIS Insights documentation. https://doc.arcgis.com/en/insights/latest/create/choropleth-maps.htm Vendor documentation. Verified on the YES/NO pass (control rejected): "Styling your map using graduated colors, like with a choropleth map, can lead to visual misinterpretations, especially when the features on the map are areas of various sizes or populations." "When you normalize data, you take a number, such as total crimes, and divide it by another number, such as total population, to create a proportional value." SINGLE PASS: "In these cases, larger areas will naturally draw your attention, especially if they're styled with darker colors."
- Axis Maps cartography guide. https://www.axismaps.com/guide/choropleth Practitioner. STRING-VERIFIED: use choropleths when data are "standardized to show rates or ratios (never use choropleth with raw data/counts)"; "Above all else the goal of data classification is to put places with similar rates in the same class, and separate places with very different rates into different classes."
- The Analysis Function charts page has no map section (checked).

7e. Area dominance, measured.
- Schiewe 2019, "Empirical Studies on the Visual Perception of Spatial Patterns in Choropleth Maps", KN – Journal of Cartography and Geographic Information 69(3): 217–228; open access (CC BY 4.0). https://link.springer.com/article/10.1007/s42489-019-00026-y Peer-reviewed. STRING-VERIFIED (control rejected).
  "an online study with 260 participants was conducted"
  "the "area-size bias" (i.e., the neglect of small areas, since these are less dominant in perception than larger ones)"
  "On the other hand, the smaller areas had detection rates of only 71.5% (maximum) and 60.0% (minimum)"; large areas were detected at 91.5% and 91.9% (SINGLE PASS).
  "small areas were missed by approximately 30–40% of map users, which is definitively too much."
  "In general, the hypotheses regarding the mentioned effects could be confirmed by statistical analysis."
  Also tested: the "dark-is-more bias". SINGLE PASS: 92.6% and 85.4% correct identification of the maximum from lightness alone, without a legend; 93.1% chose by darkness without questioning the classification.
  On remedies it endorses none. SINGLE PASS: "Much more comparative empirical research is needed to find (sub-)optimal solutions."
- Nusrat, Alam & Kobourov, "Evaluating Cartogram Effectiveness" (IEEE TVCG 2018; arXiv 1504.02218). https://arxiv.org/pdf/1504.02218 Peer-reviewed. STRING-VERIFIED (control rejected).
  n: "Out of 33 participants that took part in the study, 24 were male and 9 female". Four types (contiguous, non-contiguous, rectangular, Dorling); seven tasks (compare, detect change, locate, recognize, find top-k, find adjacency, summarize); time, error and preference measured.
  "Contiguous cartograms more or less preserve localities, region shapes, and adjacencies, and give the best performance for almost all the tasks."
  "Rectangular cartograms are a clear outlier and they should be used carefully."
  SINGLE PASS: "The choice of cartogram type should take into account the expected tasks."; contiguous and Dorling were the most preferred.
  It compares cartograms with each other, not with choropleths.
- Nusrat & Kobourov 2016, "The State of the Art in Cartograms" (arXiv 1605.08485). https://arxiv.org/pdf/1605.08485 Survey; only the first 100,000 characters were read. STRING-VERIFIED for the first quotation (control rejected). On Kaspar et al. 2011, which compared contiguous diffusion cartograms with choropleth plus graduated-circle maps: "The overall results showed that choropleth/graduated circles are more effective (as measured by accurate responses) and more efficient (as measured by faster responses) than the cartograms." SINGLE PASS: "The results seemed to depend on the complexity of the tasks (simple tasks are easier to perform in both maps compared to complex tasks), and the shapes of the polygons." On Sun & Li (SINGLE PASS): "cartograms are more effective in the representation of qualitative data (nominal data, such as, who won - republican or democrats?), but thematic maps are more effective in the representation of quantitative results". These are the survey's reports of other studies, not the originals.
- Dot-density and hexbin/tile-map evaluations: none found by direct URL.
- ONS Census maps' display choice: UNREACHABLE (the page renders only "Loading...").

7f. Colour connotation.
- Bartram, Patra & Stone 2017, "Affective Color in Visualization" (CHI 2017). DOI 10.1145/3025453.3026041. ABSTRACT ONLY (OpenAlex record, single pass; closed access; the Tableau Research PDF link now redirects to a generic page): "We carried out three studies examining how different color properties (lightness, chroma and hue) and palette (combinations and distribution of colors) contribute to different affective interpretations in information visualization". n and the per-affect findings NOT reached.
- Schloss, Lessard, Walmsley et al. 2018, "Color inference in visual communication: the meaning of colors in recycling", Cognitive Research: Principles and Implications (open access). https://link.springer.com/article/10.1186/s41235-018-0090-y SINGLE PASS. Experiment 1 n = 24; Experiment 2 n = 96 (24 per group). Finding: people assign colours to concepts by optimising across the whole set ("global assignment"), which "sometimes resulted in discarding objects in bins whose colors were weakly associated with the object, even when there was a stronger associated option available." Not a red = bad study.
- No measured "red = bad on maps" study was reached. The nearest measured item is Schiewe's dark-is-more result above.

==================================================
UNASKED-FOR FINDINGS
==================================================

1. OWID changed its citation practice in July 2025: cite blocks now point to a dated, immutable archive URL with previous, next and live navigation. This is the most direct working answer to the chapter's question. The archive URL in the citation drops the reader's country and time selection, so the data and text are frozen but the view is not.
2. The UK Government Web Archive says in terms that "Interactive content usually cannot be archived", naming interactive maps. An interactive dashboard therefore falls outside the national archival safety net unless it produces its own static or archived states.
3. ONS guidance and the best experiment disagree on class breaks. The ONS Service Manual's standard is Jenks natural breaks; Brewer & Pickle (n = 56) found quantiles best and natural breaks in a second group, and found that matched legends across a map series raised comparison accuracy by about 28 percent.
4. The DCC guide names three ways to make changing data citable (time slice, full snapshot, partial snapshot) and records that RDA recommends the third, a query result at a time. That maps directly onto "a state a reader reaches".
5. sense.us (CHI 2007) identified a snag with state-in-URL that still applies: different parameter settings give different URLs for the same view, so URL equality is not state equality. Shiny's documentation adds a hard practical limit of about 2,000 characters for URL-encoded state.
6. Sarma et al. show that leaving missing values out (complete cases only) was the most biased condition, and that every uncertainty display lowered readers' confidence. Andreasson & Riveiro's abstract shows that explaining a gap raised confidence and risky choices. Honest display of gaps changes behaviour in more than one direction.
7. Schiewe's 260-person study gives the area-dominance problem numbers (small areas missed by 30 to 40% of readers), but declines to recommend cartograms, citing their drawbacks. The one head-to-head test reported in the Nusrat & Kobourov survey (Kaspar et al.) favoured choropleth plus graduated circles over cartograms.
8. GOV.UK publisher guidance says statistics are "never eligible for history mode", and withdrawn pages stay at the same URL under a dated banner with full change notes. This is a working public convention for keeping the address while marking the content as no longer current.

==================================================
LEFT OUT AND WHY
==================================================

- Song & Szafir's conditions, n and findings: no open full text reachable; abstract only.
- Andreasson & Riveiro's n; Xiong et al.'s n and statistics; Bartram et al.'s n and findings: full texts unreachable.
- Wilkinson 2005 publisher page: refused (429). The 2012 handbook chapter abstract and Wickham 2010 are used instead.
- UK Data Service and ONS dataset-citation guidance: 404s.
- UKGWA "how to cite an archived page": not on the two pages read.
- ONS Census maps design rationale; Vega editor permalinks; Observable: JavaScript-only or 404.
- Kong, Liu & Karahalios 2019 and the UKSA geospatial ethics colour sentences: skipped as instructed.
- Dot-density and hexbin evaluations; a direct "red = bad" map study: not found without search.
- Kaspar et al. 2011 and Sun & Li originals: reported only through the survey.
- All place-specific content on the ONS, UKHSA and GOV.UK pages was ignored; they were read for URL and label conventions only.

==================================================
THREE RICH REFERENCES
==================================================

1. Rauber, Asmi, van Uytvanck & Pröll 2015, RDA "Data Citation of Evolving Data" (4 pages; R1–R14). It is a complete, short specification of what makes a state citable.
2. Gerber & Giattino 2025, OWID "New feature: embed archived versions of our interactive charts in your website", read together with a live grapher page and its archive twin. It shows the three-layer model in production, including the honest trade-off list for live versus frozen.
3. Schiewe 2019 (KN, open access). One 260-person study that measures dark-is-more, area-size bias and legend neglect on choropleths, with explicit caution about remedies.

==================================================
WHAT SURPRISED ME
==================================================

- The Supreme Court figure everyone rounds to "50%" is 49.9% in the body, and the Forum text does not contain the abstract wording commonly quoted.
- OWID's cite block now defaults to an archive URL, yet it silently drops the reader's selection.
- The national web archive states outright that interactive content is usually not archivable.
- ONS's stated default (Jenks) sits against the one controlled experiment in hand (quantiles).
- Three details in the brief did not survive contact with the sources: the Sarma author list, the Lin & Thornton title, and the description of Xiong et al.
- Several of the missing-data and trust papers most cited in this area are closed, so the chapter can only cite their abstracts unless someone obtains the PDFs.
