# Chapter 14 — agent returns (assembled 6 October 2026)

Four research agents, dispatched in one message; common brief in the research log, Entry 14. Returns reproduced as received, in full. These are working notes, not the chapter; quotations here carry the agents' own verification marks.



---

## Agent A

AGENT A REPORT — THEORY AND CRITICISM OF EXPRESSIVE DATA VISUALISATION
All fetches 6 October 2026. Marks: STRING-VERIFIED (SV) = re-fetched with a YES/NO presence check, false controls included and rejected; SINGLE PASS (SP) = returned by the reader but not separately presence-checked; ABSTRACT = only abstract reachable; SECONDARY = a reachable source quoting or describing an unreachable one. Quote marks inside quotations may be typographic in the original; the reader normalises them. WebSearch calls used: 24 of 30.

Read these first:
- The Fragapane/MoMA claim is true: three works including "Noise Pollution" have MoMA records (A7b).
- Kennedy et al. 2016 is not a focus-group study. It is 13 designer interviews plus semiotic analysis of 10 visualisations. The focus groups (9 groups, 46 people) belong to a sister paper (A4).
- Viégas & Wattenberg 2007 contains no discussion of the sublime or of scale. The sublime is Kosara's (A2).
- Kosara never uses the word "continuum"; his phrase is "opposite ends of the sublimity scale".
- Not reachable at source: Lau & Vande Moere full text, Vande Moere & Purchase full text, Kostelnick 2008, Munzner's textbook, Tufte. What I could get for each is marked ABSTRACT or SECONDARY.

---------------------------------------------------------------
A1. EXPRESSIVENESS / EFFECTIVENESS; NESTED MODEL

Mackinlay 1986, ACM TOG 5(2), April 1986, pp. 110–141 (bibliographic line SP). Scanned copy: http://vis.arc.vt.edu/~npolys/projects/safas/p110-mackinlay.pdf. Peer-reviewed theory paper; foundational.

Expressiveness
- "Expressiveness criteria determine whether a graphical language can express the desired information." SV (abstract)
- "The difficulty with this intuition is that the sentence may encode additional incorrect facts." SV
- "A set of facts is expressible in a language if it contains a sentence that (1) encodes all the facts in the set, (2) encodes only the facts in the set." SV in three fragments (the whole-string check returned NO with an identical "closest" sentence, so probably a line break in the scan).
- Bar-chart example of an unintended fact: "Most people perceive the lengths of the bars as an encoding of an ordered or quantitative set." SP (returned identically on two passes).

Effectiveness
- "Effectiveness criteria determine whether a graphical language exploits the capabilities of the output medium and the human visual system." SV (abstract)
- "Effectiveness criteria can be based on a number of different factors." SV
- "a design can be judged effective when it can be interpreted accurately or quickly, when it has visual impact, or when it can be rendered in a cost-effective manner" SV
- "Since some perceptual tasks are accomplished more accurately than others, effectiveness criteria can be based on the comparison of the perceptual tasks required by alternative graphical languages" SV

Ranking of perceptual tasks
- "The core of this conjectural theory is an observation, made by Cleveland and McGill" / "people accomplish the perceptual tasks associated with the interpretation of graphical presentations with different degrees of accuracy" SV (both fragments)
- Fig. 14 caption: "Accuracy ranking of quantitative perceptual tasks." "Higher tasks are accomplished more accurately than lower tasks." "Cleveland and McGill empirically verified the basic properties of this ranking" — all SV.
- Fig. 15 caption: "Ranking of perceptual tasks. The tasks shown in the gray boxes are not relevant to these types of data" SV.
- "Although this extension was developed using existing psychophysical results and various analyses of the different perceptual tasks, it has not been empirically verified." SV
- "Principle of Importance Ordering: Encode more important information more effectively." SV
- The contents of Figures 14 and 15 (the ordered lists under Quantitative / Ordinal / Nominal) could not be read reliably. Three passes gave three different orders and the reader finally answered "CANNOT READ RELIABLY". I quote no list; take it from the printed figure.

Role: the formal name for the tier test. The "only the facts" clause is the removal test stated in 1986. Mackinlay himself calls the effectiveness ranking "conjectural" and its extension beyond quantitative data unverified.

Munzner 2009, "A Nested Model for Visualization Design and Validation", IEEE TVCG. Author copy: https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf. The copy prints "Manuscript received 31 March 2009; accepted 27 July 2009; posted online 11 October 2009" (SP); volume and pages are not printed on it.
- Four levels (abstract): "characterize the task and data in the vocabulary of the problem domain, abstract into operations and data types, design visual encoding and interaction techniques, and create algorithms to execute techniques efficiently" SV
- "an upstream error inevitably cascades to all downstream levels" SV
- "This model provides prescriptive guidance for determining appropriate evaluation approaches by identifying threats to validity unique to each level" SV
- Encoding level: "the threat is that the chosen design is not effective at communicating the desired abstraction to the person using the system" SV; "One immediate validation approach is to justify the design with respect to known perceptual and cognitive principles" SV
- "The immediate validations only offer partial evidence of success" SV; continuation "none of them are sufficient to demonstrate that the threat to validity at that level has been addressed" SP (consistent on two passes).
- "If a poor choice was made in the abstraction stage, then even perfect visual encoding and algorithm design will not create a visualization system that solves the intended problem." SP
Role: where the evidence/expression boundary sits (abstraction vs encoding), and why an encoding-level check cannot repair an upstream error.

Munzner, Visualization Analysis and Design (2014): book text not reachable; https://www.cs.ubc.ca/~tmm/vadbook/ links no full text.
- Her own slides (City University London, 3 February 2015, https://www.cs.ubc.ca/~tmm/talks/minicourse14/vad15london.pdf): "effectiveness principle – encode most important attributes with highest ranked channels"; "expressiveness principle – match channel and data characteristics"; "validation is necessary, but tricky". All SV.
- SECONDARY, two independent course pages: "Visual encoding should express all of, and only, the information in the dataset attributes" and "[The] importance of the attribute should match the salience of the channel". Present (SV on those pages) at https://teaching.vda.univie.ac.at/vis/23s/LectureNotes/04_visual_encoding_principles.pdf (L. Koesten, Univ. Vienna, "based on © Munzner/Möller et al.") and https://www.math.csi.cuny.edu/~mvj/GC-DataViz-S23/lectures/L5.html. Neither gives a book page; check against the book before quoting as Munzner's. The Vienna slide pairs expressiveness with Tufte's "Lie factor" and effectiveness with "Data-ink ratio".

---------------------------------------------------------------
A2. ART / DESIGN / PRAGMATIC FRAMEWORKS

Kosara 2007, "Visualization Criticism – The Missing Link Between Information Visualization and Art" (IV 2007). https://media.eagereyes.org/papers/2007/Kosara-IV-2007.pdf (kosara.net returns 403). Conference position paper; pages not printed on the copy.

Abstract: "Classifications of visualization are often based on technical criteria, and leave out artistic ways of visualizing information" SV. "Visualization criticism bridges the gap between design, art, and technical/pragmatic information visualization" SV.

Three criteria for what counts as visualization (heads SV; bodies as marked):
- "It is based on (non-visual) data." SV
- "It produces an image." SV. Body, SP: "…the visual must be the primary means of communicating the data. Other media can be part of a visualization, but the visualization must be able to stand on its own."
- "The result is readable and recognizable." SV. "Visualization images must also be recognizable as such, and not appear to be something else." SV. "The use of additional elements (or even "eye candy") is certainly possible, but must not take precedence over the communication goals of the visualization" SV.

The sublime (section 4.1):
- "One aesthetic criterion of particular interest is the sublime" SV
- "The sublime can be understood as that which inspires awe, grandeur, and evokes a deep emotional and/or intellectual response" SV
- "They are thus designed to remove any sublimity, and instead foster immediate understanding" SV
- "while the classical technical information visualization is entirely anti-sublime, artistic visualizations are primarily sublime" SV
- "The sublime subsumes the two criteria of readability and recognizability, since for a work of art to be sublime, it cannot be easily readable (or user friendly)" SV
- "It must present enough of an enigma to keep an audience interested without being easy to solve" SV

Pragmatic and artistic:
- "Pragmatic visualization is what we term the technical application of visualization techniques to analyze data" SV
- "The goal of artistic visualization is usually to communicate a concern, rather than to show data" SV
- "It also provides a proof that the concern in question is, in fact, real." (present; the check tripped only on the final full stop)
- "Visual efficiency does not play a role in artistic visualization, quite the contrary" SV
- Not a "continuum": "The fact that artistic and pragmatic visualizations are on opposite ends of the sublimity scale" … "and thus theoretically impossible to reconcile, should not deter us from trying, though" SV (two fragments). "We therefore propose a third way of doing information visualization" SV.

Criticism:
- "Visualization criticism is an organized and well-defined channel to discuss work in visualization" SV; "Visualization criticism is critical thinking about visualization" SV
- Four rules (section 5.1), headed Neutral voice / Facts / No self-promotion / Clear goal: "Criticism must be expressed in a way that states the facts and presents them in the most balanced possible light" SV; "Every statement must be backed up by facts that can be independently checked" SV; "A critique must serve a goal" SV; "The critics' own work can only be cited as an example if there are also other examples, and cannot be used as the gold standard." SP
Role: gives the chapter a published rule set for reading expressive works, and a published "eye candy must not take precedence" line.

Viégas & Wattenberg 2007, "Artistic Data Visualization: Beyond Visual Analytics", in D. Schuler (ed.), Online Communities and Social Computing, HCII 2007, LNCS 4564, pp. 182–191. https://link.springer.com/content/pdf/10.1007/978-3-540-73257-0_21.pdf (hint.fm unreachable). Short survey/position paper.
- "Artistic visualizations are visualizations of data done by artists with the intent of making art" SV
- "This definition may seem like a tautology, but in fact it specifies a coherent and interesting class of work" SV
- "First, the artworks must be based on actual data, rather than the metaphors or surface appearance of visualization" SV
- "we do not contend that beautiful scientific visualizations are automatically artistic, or that visualization art must be pretty" SV
- "Each embodies a forceful point of view" SV. Next sentence, SP: "In a sense, the artworks derive their power from the fact that the artists are committing various sins of visual analytics."
- "traditional analytic visualization tools have sought to minimize distortions, since these may interfere with dispassionate analysis" SV
- "Is it possible that this focus on minimizing "point of view" is misguided?" SV
- "to choose which perspective is the right one for a given analytic task" SV (fragment)
- "A more radical change in attitude would be to embrace the fact that visualizations can be used to persuade as well as analyze" SV
- "Should data visualization researchers investigate ways to support making a point, as well as disinterested analysis?" SV
- The word "sublime" does not appear (checked); no sentences on "scale", "vast" or "overwhelming" were found.

Lau & Vande Moere 2007, "Towards a Model of Information Aesthetics in Information Visualization" (IV 2007, pp. 87–92). Full text unreachable (infoscape.org down, designersinteractifs 403, IEEE/CSDL blank, KU Leuven timeout). ABSTRACT via a third-party mirror, https://eurekamag.com/research/098/232/098232892.php, SV on that page:
- "This paper proposes a model of information aesthetics in the context of information visualization"
- "The proposed model is based on analysing existing visualization techniques by their interpretative intent and data mapping inspiration"
- "It reveals information aesthetics as the conceptual link between information visualization and visualization art, and includes the fields of social and ambient visualization"
- "This model is unique in its focus on aesthetics as the artistic influence on the technical implementation and intended purpose of a visualization technique, rather than subjective aesthetic judgments of the visualization outcome"
The axis definitions (data focus intrinsic–extrinsic; mapping technique direct–interpretive) are not in the abstract and I could not verify them at source. SECONDARY, J. C. Roberts, "Engaging Data-Art" (IEEE EduVis 2024), https://arxiv.org/pdf/2408.04750, SV there: "Andrea and Vande Moere [11] likewise focus on aesthetics, presenting a two-dimensional model of intrinsic ("cognitively effective visual mapping") to extrinsic (to facilitate communication of meaning, underpinned by the data) and on the horizontal axis: direct to interpretive." and "Where information visualisation is considered as being direct and intrinsic, whereas visualisation art is extrinsic and interpretative". Roberts misnames the first author ("Andrea" for Andrea Lau). Do not print the axis definitions as Lau & Vande Moere's words without the paper.

Vande Moere & Purchase 2011, "On the role of design in information visualization", Information Visualization 10(4), pp. 356–371, October 2011. Full text closed. ABSTRACT, SV at https://research.monash.edu/en/publications/on-the-role-of-design-in-information-visualization/ (the Glasgow record gives 2012 for the year):
- "balancing the three requirements of utility, soundness and attractiveness within given constraints"
- "In presenting a model of three potential roles for design in information visualization"
- "visualizations produced as part of commercial practice or artistic exploration"
- "a paradigm shift in the way we value, teach and conduct information visualization research"
The triangle and the sentences placing "design" are not reachable; nothing quoted. One sentence of theirs as quoted by Quispel et al. 2018 (SECONDARY, SP): "(…) complex and socially relevant issues might best be communicated to a large audience through popular media using an artistic and engaging visualization (even if its designer knows that such a method is not the most effective or efficient)."

Pousman, Stasko & Mateas 2007, "Casual Information Visualization: Depictions of Data in Everyday Life", IEEE TVCG 13(6). Author copy: https://faculty.cc.gatech.edu/~john.stasko/papers/infovis07-casual.pdf (no volume or pages printed; the reader invented a page range on the first pass). Peer-reviewed framework.
- Definition: "Casual Infovis is the use of computer mediated tools to depict personally meaningful information in visual ways that support everyday users in both everyday work and non-work situations" SV
- User Population: "The user population is enlarged to include a wide spectrum of users from experts to novices" SV
- Usage Pattern: "Systems are intended for usage that is momentary and repeatable (over weeks and months), or contemplative" SV, followed by "(a long moment at an art gallery)" SV
- Data Type: "The data is typically personally important and relevant, as opposed to work-motivated" SV
- Insight: "We propose that the kinds of insight that Casual Infovis may support are different from more traditional systems." SP
- Analytic: "Analytic insight is the most traditional sense of insight that we find supported in visualization systems" SV
- Awareness: "Awareness insight is the insight that comes from maintaining awareness of a particular data stream" SV
- Social: both "Social insight is insight about social networks, social situations, and social life" SV and "Social insight is the sense of understanding of a social group and one's place in it" SV
- Reflective: "Reflective insight is insight about oneself, the world, and one's place in it" SV
- Evaluation: "are not tied to productivity metrics like efficiency and effectiveness" SV (fragment)
- Artistic infovis, SP: "Yet another emerging area of information visualization work are systems that are works of data-driven art."

---------------------------------------------------------------
A3. CRITICAL AND FEMINIST VISUALISATION

Dörk, Feng, Collins & Carpendale 2013, "Critical InfoVis: Exploring the Politics of Visualization", CHI 2013 Extended Abstracts (alt.chi), Paris. https://mariandoerk.de/criticalinfovis/altchi2013.pdf. Argument paper, no data.
- "So far the research community has not given sufficient thought to how values and assumptions pervade information visualization" SV
- "we outline a critical approach that promotes disclosure, plurality, contingency, and empowerment" SV
- Disclosure: "Creating visualizations involves a range of decisions about data, representation, and interaction." (SP, same on two passes) "Disclosing some of these decisions is a way to establish trust between visualization creators and viewers" SV
- Plurality: "exposing multiple facets and enabling a variety of interpretations is preferable to limited views and singular readings" SV (the sentence opens "Since no one visualization can capture all perspectives on a phenomenon,")
- Contingency: "tools should provide for a range of possible ways viewers experience a visualization" SV (opens "Instead of pre-determined conclusions to be drawn from a visualization,")
- Empowerment: "Empowering visualizations should also allow viewers to question visual representations, utilize them to tell their own story" SV, continuing "and shift from awareness to action" (SP)
- "These principles do not provide checklist-criteria to deem visualizations good or bad" SV
- Under Plurality, SP: "There may be situations in which the visualization designer deliberatively chooses to advocate a specific standpoint instead of offering a nuanced set of perspectives."

D'Ignazio & Klein 2020, Data Feminism (MIT Press), chapter 3, "On Rational, Scientific, Objective Viewpoints from Mythical, Imaginary, Impossible Standpoints". https://data-feminism.mitpress.mit.edu/pub/5evfe9yd. Scholarly monograph; argument, not experiment.
- Principle: "Elevate Emotion and Embodiment" — "Data feminism teaches us to value multiple forms of knowledge, including the knowledge that comes from people as living, feeling bodies in the world" SV
- Rhetoric: "Any communicating object that reflects choices about the selection and representation of reality is a rhetorical object" SV
- "This includes visualizations that do not deliberately intend to persuade people of a certain message" SV; "It especially and definitively includes those so-called neutral visualizations that do not appear to have an editorial hand" SV; "In fact, those might even be the most perniciously persuasive visualizations of all!" SV
- Plain style: "The more plain, the more neutral; the more neutral, the more objective; and the more objective, the more true" SV (the sentence ends "—or so this line of reasoning goes", SP)
- "So if plain, "unemotional" visualizations are not neutral, but are actually extremely persuasive, then what does this mean for the concept of neutrality in general?" SV. It begins "So if", not "But if"; the first pass got this wrong.
- "Clarity without persuasion" SV — this is D&K quoting Guardian workshop leaders. "persuasion is everywhere, even in spreadsheets" SV
- God trick: "the god trick of seeing everything from nowhere" SV (D&K quoting Haraway); "The view from nowhere—from a distance, from up above, like a god—may be data visualization's most signature feature" SV; "The god trick and its underlying assumptions about neutrality and truth are baked into today's best practices for data visualization" SV
- Periscopic: "Periscopic's work is framed around an emotion: loss" SV; "Once we embrace the idea of leveraging emotion in data visualization, we can truly appreciate what sets Periscopic's" SV (fragment); "leads with loss, grief, and mourning" SV; "emotion and visual minimalism are not incompatible here" SV
- Cairo's objection, as quoted by D&K: "Is it clear to a general audience that what they see is the work of professionals who actively shape data to support a cause, and not the product of automated processes?" SV
- On Kennedy et al.: "four conventions of data visualization reinforce people's perceptions of its factual basis" SV; "The layout is "clean," meaning minimal and lacking embellishment beyond what is necessary to communicate the data" SV; "These conventions contribute to the perception of data visualization as objective, scientific, and neutral" SV. D&K list the fourth convention as "the inclusion of data sources at the bottom" (SP); "at the bottom" is their gloss, not Kennedy's wording.
- They also concede: "there are also good reasons to use the god trick as a form of recuperation, contestation, or empowerment" (SP), under the subheading "Don't Never Do a God Trick" (SP).
- Last sentence: "All design fields, including visualization and data communication, are fields of possibility" SV
- Empirical claim, SP: "Scientific researchers are now proving by experiment what designers and artists have known through practice: activating emotion, leveraging embodiment, and creating novel presentation forms help people grasp and learn more from data-driven arguments, as well as remember them more fully." This is stronger than the experiments I found support (A8; Unasked 1–2).

---------------------------------------------------------------
A4. THE CONVENTIONS OF OBJECTIVITY

Kennedy, Hill, Aiello & Allen 2016, "The work that visualisation conventions do", Information, Communication & Society 19(6), 715–735, DOI 10.1080/1369118X.2016.1153126. Accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/93521/3/repository20.pdf, cross-checked on a second White Rose copy (eprint 95186). The T&F page returns 403. Peer-reviewed, qualitative, social-semiotic.

Method: "Skype interviews with 13 visualisations designers" SV and "detailed social semiotic analysis of 10 visualisations circulating in the media" SV. SP details: "Three were women and 10 were men"; "Four of these 10 visualisations were produced by interviewees." The phrase "focus group" does not appear (checked on both copies). No reader was tested, so the claim that conventions make readers perceive objectivity is an interpretive argument.

- "This paper argues that visualisation conventions work to make the data represented within visualisations seem objective, that is, transparent and factual" SV
- "We focus on four conventions which imbue visualisations with a sense of objectivity, transparency and facticity" SV; "a) two-dimensional viewpoints; b) clean layouts; c) geometric shapes and lines; d) the inclusion of data sources" SV
- "It is not visualisation designers who are creating this sense of objectivity, we propose, but rather the conventions on which they necessarily draw in producing visualisations" SV
- "Two-dimensional viewpoints look objective even though they are not" SV; "Two-dimensional viewpoints create the illusion of objectivity by disguising perspective" SV
- "The use of clean layouts to present data in visualisations creates an aura of clarity and simplicity" SV; "This aura of simplicity 'rubs off' on the data" SV
- Geometric shapes, SP: "The use of geometrical shapes and lines therefore results in the dramatic and systematic simplification of data by highlighting only some of their characteristics."
- "Thus the inclusion of data sources performs the rhetorical, persuasive work of ascribing transparency and trustworthiness to visualisations" SV. Preceding sentence, SP: "It suggests that the designer feels confident that s/he has been truthful to the data, and this in turn suggests that there may be no need for the user to check."
- "Visualisation conventions sometimes work to undermine the good intentions of visualisers, by imbuing data with a sense of objectivity" SV
- Funding, SP: Seeing Data, AHRC Grant No. AH/L009986/1.
Role: the conventions of objectivity are themselves a rhetoric, including source citation, which the house treats as plain evidence practice.

The focus-group paper is Kennedy, Hill, Allen & Kirk 2016, "Engaging with (big) data visualizations: Factors that affect engagement and resulting new definitions of effectiveness", First Monday 21(11), 3 November 2016. https://firstmonday.org/ojs/index.php/fm/article/view/6389 (full text via /download/6389/5652).
- "We carried out nine focus groups with a total of 46 participants" SV; "Twenty-seven participants were female and 19 male" SV; "ages ranged from 11 to 70" SV
- Eight visualisations were evaluated; the exact sentence is unsettled (the check gave "we asked participants to look at each visualisation" as the closest text).
- Diary follow-up: "Seven participants agreed to do this" SV
- Six factors (abstract, SP): "subject matter; source/media location; beliefs and opinions; time; emotions; and confidence and skills"
- "What constitutes effectiveness is fluid" SV; "no single definition will apply across all engagements with visualizations" SV; "should be seen as dimensions of effectiveness" SV
- SP: "This type of visualization was new to many of our participants who therefore did not like it."
Kennedy & Hill 2018 (Sociology) returned 403; Kennedy & Engebretsen 2020 not attempted.

---------------------------------------------------------------
A5. ETHICS, MANIPULATION, THE LOOK OF NEUTRALITY

Correll 2019, "Ethical Dimensions of Visualization Research" (CHI 2019). https://arxiv.org/pdf/1811.07271 (no venue line on the arXiv copy). Peer-reviewed essay.
- Abstract: "it is not clear how this power connects to ethical duties" SV; "propose a set of additional moral obligations that we have as designers, builders, and researchers of visualizations" SV
- The three categories appear in one sentence, SP on two passes: "In the following subsections I will present three ethical challenges of visualization work, related to visibility, privacy, and power."
- The three section headings are imperatives: "Make the Invisible Visible", "Collect Data With Empathy", "Challenge Structures of Power" (all SV).
- Nine principles, each a bolded "We ought to…" lead-in (all SV): "We ought to visualize hidden labor"; "We ought to visualize hidden uncertainty"; "We ought to visualize hidden impacts"; "We ought to encourage "small data.""; "We ought to anthropomorphize data"; "We ought to obfuscate data to protect privacy"; "We ought to support data "due process.""; "We ought to act as data advocates"; "We ought to pressure or slow unethical analytical behavior".
- "All visualization research, no matter how superficially apolitical or trivial, has a moral character" SV
- "All visualizations are rhetorical, and have the power to potentially persuade" SV (citing Pandey et al. 2014)
- "The clean lines and structured layouts of traditional visualizations communicate authority and certainty in implicit but measurable ways" SV (citing Kennedy et al. 2016)
- "Visualizations have rhetorical strength and political power" SV
- Under his own anthropomorphise principle, SP: "Proposed solutions to recenter human beings in data visualizations using person-shaped glyphs has not been shown to produce any additional empathic response [16]."

Correll & Heer 2017, "Black Hat Visualization" (DECISIVe workshop, IEEE VIS 2017; the venue is not printed on the PDF). https://idl.cs.washington.edu/files/2017-BlackHatVis-DECISIVe.pdf. Workshop paper.
- "People lie, mislead, and bullshit in a myriad of ways" SV
- "we use the language of computer security to expand the space of ways that unscrupulous people (black hats) can manipulate visualizations for nefarious ends" SV
- "visualizations which have fidelity to the underlying data" SV — the framing that matters: faithful to the data, still harmful.
- "are well-situated to perform "man in the middle" attacks" SV
- Example: "By choosing how to aggregate and normalize the same data, the designer of the visualization can control the message of the chart" SV
- "We encourage designers to think defensively and comprehensively about how their visual designs can result in data being misinterpreted" SV
- The word "exploit" does not appear in the paper.

Kostelnick 2008, "The Visual Rhetoric of Data Displays: The Conundrum of Clarity", IEEE TPC 51(1), 116–130: unreachable (Semantic Scholar 403 twice, IEEE blank, ResearchGate blocked). Nothing quoted from it. SECONDARY: Prantl, Möller & Koesten, "Untangling Rhetoric, Pathos, and Aesthetics in Data Visualization", https://arxiv.org/pdf/2304.10540 (venue and year not confirmed). SV there:
- "Kostelnick sees an explanation of this avoidance of pathos in the rise of a new modernist minimalism" (this cites Kostelnick's 2016 Technical Communication article, not the 2008 one)
- "ultimately promoting Tufte's minimalist approach as "the way to truth""
- "data or data visualizations are often considered apolitical and ethically neutral, as data itself are seemingly objective"
- "Drawing from Campbell's seven circumstances, we illustrate how pathos is being used as a rhetorical device in data visualizations today, at times inadvertently"
The strongest reachable primary statements that "clean" is a rhetorical style are Kennedy et al. (A4), D&K ch. 3 (A3) and Correll's sentence above.

---------------------------------------------------------------
A6. DATA HUMANISM AS PRACTICE (practitioner manifesto, not evidence)

Lupi, "Data Humanism: The Revolutionary Future of Data Visualization", PrintMag, 30 January 2017 (date SP). https://www.printmag.com/article/data-humanism-future-of-data-visualization/. Also on her site as "Data Humanism — The Revolution will be Visualized", marked "Originally published on PrintMag", undated: https://giorgialupi.com/data-humanism-my-manifesto-for-a-new-data-wold.

The four headings differ between the two versions:
- PrintMag (SV, checked in lower-case form): "Embrace Complexity" / "Move Beyond Standards" / "Sneak Context In (Always)" / "Remember That Data is Flawed (As We Are)"
- giorgialupi.com (SV): "EMBRACE COMPLEXITY" / "MOVE BEYOND STANDARDS" / "SNEAK CONTEXT IN. (ALWAYS)" / "FINALLY, REMEMBER THAT DATA IS IMPERFECT. (AS WE ARE)"
- "Data is people" appears on neither page (checked). "small data" and "data is never neutral" are absent from her site page. The Visual Manifesto image on her site has no extractable text, so its word pairs cannot be quoted.

Sentences (PrintMag, SV unless marked):
- "We are ready to question the impersonality of a merely technical approach to data, and to begin designing ways to connect numbers to what they really stand for: knowledge, behaviors, people"
- "Data represents real life. It is a snapshot of the world in the same way that a picture catches a small moment in time"
- ""Data-driven" doesn't mean "unmistakably true," and it never did"
- "Data is a tool that filters reality in a highly subjective way"
- "One size does not fit all"; "A dataset might lead to many stories"; "Let's stop thinking data is perfect"
- "Data visualization should embrace imperfection and approximation"
- "peak infographics" (in "Now that we are past what we can call peak infographics…", SP)
- Hand-drawing as method, SP: "What I always do when I start a new data project is to move away from the screen and start drawing."; "Sketching with data—in a way, removing technology from the equation before bringing it back to finalize the design with digital tools—introduces novel ways of thinking"
- Dear Data: "Can you get to know another human being through data only?" SV. The PrintMag page prints the start date as "Sept. 1, 2004" (the check found "September 1, 2004" present and "2014" absent). This looks like a typo on PrintMag, since MoMA dates the cards 2014–2015. Do not reproduce it.

Dear Data, in the makers' words:
- https://www.dear-data.com/theproject: "Dear Data is a year-long, analog data drawing project by Giorgia Lupi and Stefanie Posavec" SV; "Each week, and for a year, we collected and measured a particular type of data about our lives" SV; "Over the fifty-two weeks, the collecting of data about our lives became a kind of ritual" (SP; the digit form "52 weeks" is absent); "We prefer to approach data in a slower, more analogue way" SV; "we argue we can use data to become more humane and to connect with ourselves and others at a deeper level" SV; "Instead of using data just to become more efficient" SV. No mention of MoMA on that page.
- https://www.stefanieposavec.com/dear-data-about: "Dear Data is a year-long, analogue data drawing project between myself and Giorgia Lupi" SV; "104 unique esoteric datasets and visualisation methods" SV; "slow data" SV; "The 104 postcards and accompanying preliminary sketchbooks for this project are now held in the permanent collection of the Museum of Modern Art, New York" SV. No acquisition year is stated.

---------------------------------------------------------------
A7. MUSEUM RECORDS — VERIFIED AT THE RECORD

(a) Wind Map. https://www.moma.org/collection/works/163892
- Artist "Fernanda Bertini Viégas, Martin Wattenberg"; title "Wind Map"; date 2012; medium "Interactive software"; credit "Gift of the designers"; object number "1751.2012"; Department of Architecture and Design (all SV except the department, SP). "Not on view" SP. The record does not say purchased.
- Exhibitions as printed (SP for the list; the Applied Design dates were confirmed on a second pass): Applied Design, Mar 2, 2013–Jan 20, 2014; A Collection of Ideas, Feb 15, 2014–Jan 11, 2015; This Is for Everyone: Design Experiments for the Common Good, Feb 14, 2015–Jan 18, 2016; Energy, Oct 21, 2019–Jan 26, 2020; Never Alone: Video Games and Other Interactive Design, Sep 10, 2022–Jul 16, 2023; Pirouette: Turning Points in Design, January 26, 2025–November 15, 2025.
- Date discrepancy: MoMA's press release of 14 February 2013 (https://www.moma.org/documents/moma_press-release_386891.pdf, SP) gives Applied Design as "March 2, 2013–January 31, 2014"; the record gives Jan 20, 2014.
- Label text: "to create a "living portrait" of the wind landscape over the United States" SV; "The result is an intricate pattern of swirling currents" SV (Pirouette label); "Wind Map's patterns serve as useful data visualizations and, as we consider alternative energy sources, a reminder of the power of wind" SV (Never Alone label); the designers' words, "An invisible, ancient source of energy surrounds us, energy that powered the first explorations of the world, and that may be a key to the future" SV.
- Press-release checklist, SP: "Wind Map 2012 Interactive software Gift of the designers 1751.2012".

(b) Federica Fragapane — the claim is true. Artist page https://www.moma.org/artists/136154-federica-fragapane ("Italian, born 1988", SP) lists three works:
- "Noise Pollution (Data visualization for La Lettura)", 2020, "Digital image", "Gift of the designer", object number "98.2023", Architecture and Design, "Not on view" — all SV. https://www.moma.org/collection/works/447623. This record carries no gallery label and no exhibition; "Pirouette" is absent from it (checked).
- "Land Defenders (Data visualization for Atmos)", 2021, "Digital image", "Gift of the designer", "97.2023" (SV). https://www.moma.org/collection/works/447622. Shown in Pirouette: Turning Points in Design.
- "Space Junk (Data visualization for BBC Science Focus)", 2019, "Digital image", "Gift of the designer", "96.2023" (SP). https://www.moma.org/collection/works/447620.
- Label shared by Land Defenders and Space Junk: "Information design often goes beyond mere description to become an expressive interpretation of reality." (first 70 characters SV; remainder SP, identical on two records). It continues, SP: "Designers like Fragapane analyze and describe all sorts of phenomena and data—from literary history facts to urgent social, political, and ecological issues—by sometimes also designing their own datasets. Land Defenders illustrates Brazil's deforestation rates in correlation with the deaths of environmental defenders, represented by blood-red leaves."
- What the records do not say: no acquisition date beyond the ".2023" accession suffix, no purchase, no dimensions, and nothing about Noise Pollution having been exhibited.

(c) Dear Data. Each week has its own record. Example, https://www.moma.org/collection/works/216731: "Giorgia Lupi, Stefanie Posavec. Dear Data: Week 6 (Don't Touch Me Now / A Week of Physical Contact). 2014"; ".a: Ink, marker, and pencil on paper" (SV for the medium string); credit "Committee on Architecture and Design Funds" (SV; "Gift of the designers" is absent, so this was bought with committee funds); object number "962.2016.6a-b" SV; "Not on view" SV; exhibition "Search Engines", "Nov 14, 2020–Jun 1, 2023".
- Label ("Gallery label from 2020"), SP except "hand-drawn" SV: "Imagine getting to know someone halfway across the world through postcards sent by snail mail—but instead of a picture and a brief message, these postcards are covered with hand-drawn symbols representing patterns from daily life. … While information design today is typically associated with digital data, Posavec and Lupi focused on analog design to tell stories about ordinary events and small intrigues."
- Lupi's artist page (https://www.moma.org/artists/67122-giorgia-lupi): "53 works online" SV, "Italian, born 1981" SV. Every title shown begins "Dear Data: Week" and no sketchbook title is visible, though only the first rows could be read.
- The record nowhere states "acquired 2016"; the year is carried only by the accession number 962.2016. I found no separate MoMA acquisition statement.

(d) Other holdings with records
- MoMA, Aaron Koblin, "Flight Patterns", 2005, "Video (color)", "Gift of the designer", object number "SC529.2008.1-2" (all SV). https://www.moma.org/collection/works/110268. Shown in Design and the Elastic Mind, "Feb 24, 2008–May 12, 2008" SV. Label: "Flight Patterns is a "flat" corollary to an installation combining science, statistics, and art designed to be shown in a planetarium" SV. The number carries an "SC" prefix; the page does not print "Study Collection" and I do not interpret it.
- MoMA, Jonathan Harris and Sep Kamvar, "I Want You To Want Me", 2007, credit "Commissioned by The Museum of Modern Art on the occasion of the exhibition Design and the Elastic Mind", object number SC527.2008 (SP). https://www.moma.org/collection/works/110269.
- V&A, Aaron Koblin, "Flight Patterns", accession "E.1185-2012", "Prints, Drawings & Paintings Collection", "Not on display", credit "Courtesy of the artist" (all SV). Dated "2009 (made)" with a brief description giving "2005 - 2009" (SP). Label, SP with "205,000" and "12 August 2008" SV: "Koblin specialises in taking unreadable computational data and making visualisations with it. … He sourced data from the Federal Aviation Administration on 205,000 flights on 12 August 2008." https://collections.vam.ac.uk/item/O1247173/flight-patterns-digital-art-aaron-koblin/
- Art Institute of Chicago, Koblin, "Flight Patterns", date field 2011, "Animation", "Funds provided by the Architecture & Design Society", reference "2011.275" (all SV). Description: "a time-lapse animation that employs data visualization and processing" SV; "140,000 airplanes" (number SV). https://www.artic.edu/artworks/213139/flight-patterns
- The same named work is held by three museums under three dates (2005 / 2009 / 2011) and two flight counts (205,000 / 140,000). A data work is a versioned thing; a record's date is the version's.
- Not checked: Ars Electronica archive, Cooper Hewitt, Design Museum.
- A caution for anyone re-checking: MoMA's collection search URL (?q=…) returns the same default set whatever the query. Records have to be reached by ID.

---------------------------------------------------------------
A8. EMPIRICAL EVALUATION OF "ARTISTIC" / EXPRESSIVE VISUALISATION WITH READERS

Little exists. I found no controlled study that takes museum-grade data art and measures what viewers correctly take from it against a conventional chart of the same data. What exists:

1. Arunkumar, Padilla, Bae & Bryan 2023, "Image or Information? Examining the Nature and Impact of Visualization Perceptual Classification", IEEE TVCG / VIS 2023. https://arxiv.org/pdf/2307.10571. The nearest thing to the test the chapter wants.
- "we annotated 500 visualizations" SV; "analyzed the responses of 250 online participants" SV (methods say 265 were recruited on Prolific, SP); "in-person study (n = 101)" SV, free recall; college-aged and older adults (SP).
- Task: rate each visualisation on a scale from image to information, then recall.
- "Image-rated visualizations were perceived as more aesthetically appealing, enjoyable, and pleasing" SV
- "visualizations internalized as images are less effective in conveying trends and messages, though they elicit a more positive emotional judgment" SV
- SP (abstract): "We discuss the implications of this dissociation between aesthetic pleasure and perceived ease of use in visualization design."
- Strength: one paper, a real-world corpus, correlational on design features.

2. Vande Moere, Tomitsch, Wimmer, Boesch & Grechenig 2012, "Evaluating the Effect of Style in Information Visualization", IEEE TVCG 18(12), 2739–2748. Primary unreachable; n not obtained. SECONDARY, Lan et al. 2025 (SV there): "compared analytical, magazine, and artistic visualization styles, noting that analytical styles enhance the discovery of analytical insights, while the other two induce more meaning-based insights".

3. Cawthon & Vande Moere 2007, "The Effect of Aesthetic on the Usability of Data Visualization" (IV 2007, pp. 637–648). Primary unreachable. SECONDARY, Lan et al. 2025 (SV there): "asked participants to rank eleven visualization types on an aesthetic scale from "ugly" to "beautiful"".

4. Lan, Wu, Chen & Cao 2023, "The Chart Excites Me! Exploring How Data Visualization Design Influences Affective Arousal", IEEE TVCG. https://arxiv.org/pdf/2211.03296. "We collected a corpus of 265 data visualizations and conducted a crowdsourcing study with 184 participants" SV; "all texts were blurred to exclude the influence of semantics" SV; "we finally identified four design features (e.g., colorfulness, the number of different visual channels) cross-validated as important features correlated with affective arousal" SV. Measures arousal only; comprehension was not measured, and the authors limit the findings to "correlations rather than causal effects" (SP).

5. Lan, Wang, Peng & Ma 2025, "More Than Beautiful: Exploring Design Features, Practical Perspectives, and Implications of Artistic Data Visualization", IEEE TVCG. https://arxiv.org/pdf/2502.04940. "we analyzed 220 data artworks" SV (IEEE VISAP: "a total of 231 non-duplicate artworks" SV; minus 36 inaccessible, plus 25 by snowballing, SP); "in-depth interviews with twelve data artists" SV ("including 5 females and 7 males" SV); "artistic data visualization is deeply rooted in art discourse" SV. No viewer study. Their second future direction is "Enriching evaluation metrics": "art often enables open-ended interpretation and repeated contemplation" SV; "Therefore, it is also crucial to assess long-term user experience beyond capturing immediate responses" SV. The field's own 2025 review treats evaluation as unbuilt.

6. Saket, Endert & Stasko 2016, "Beyond Usability and Performance: A Review of User Experience-focused Evaluations in Visualization" (BELIV '16). https://faculty.cc.gatech.edu/~stasko/papers/beliv16-ux.pdf. Review of studies measuring "memorability, engagement, enjoyment and fun" (abstract, SP); such goals "appear to be more difficult to define, much less to measure" (SP).

7. Qualitative reader evidence: Kennedy, Hill, Allen & Kirk 2016 (A4; 9 focus groups, 46 participants).

---------------------------------------------------------------
INFORMATION IS BEAUTIFUL AWARDS — JUDGING CRITERIA

There is no "truthful, insightful, beautiful" formula on either page checked.
- https://www.informationisbeautifulawards.com/about (SV): "has been celebrating excellence & beauty in data visualization, infographics, interactives & information art since 2012"; "Our judges review each entrant for how well it suits the medium (infographic, interactive, data visualization and more) & how well it illuminates the topic"; "The Awards are judged by a panel of experts & a public vote". The word "truthful" does not appear. The page says the Awards are now presented by the Data Visualization Society (SP).
- https://www.datavisualizationsociety.org/iib-awards-faqs (the page refers to the 2024 Awards, SP): "This year, judges will consider the following criteria when reviewing submissions" SV. Eight criteria: impactful; engaging; clarity; innovative and creative; inclusive; accessible; effective; beautiful. SV wording: "Is the work impactful?"; "Does the work display clarity of analysis, including clear guidance that makes the visual usable?"; "Is the work innovative and creative, celebrating novel formats and design approaches?"; "Is the work effective, achieving its goals and connecting an audience to the underlying data – which may mean valuing simplicity over complexity?"; "Is the work beautiful, celebrating aesthetic beauty and design broadly?". Longlisting: "each submission was reviewed by at least three people based on the judging criteria outlined above" SV.
- No criterion addresses accuracy, truth or data integrity; the reader's explicit check returned none.

TUFTE, "smallest effective difference" (Visual Explanations): not reachable at source. The edwardtufte.com book page does not contain the phrase; only third-party blogs do. Skipped; nothing quoted.

---------------------------------------------------------------
UNASKED THREADS

1. Boy, Pandey, Emerson, Satterthwaite, Nov & Bertini 2017, "Showing People Behind Data: Does Anthropomorphizing Visualizations Elicit More Empathy for Human Rights Data?" (CHI 2017). ABSTRACT at https://nyuscholars.nyu.edu/en/publications/showing-people-behind-data-does-anthropomorphizing-visualizations: "Contrary to our expectations, we consistently find that anthropomorphized data graphics and standard charts have very similar effects on empathy and prosocial behavior" SV; experiments "conducted on Amazon Mechanical Turk" (SP). The number of experiments and the n are not in the abstract. This bears directly on the Periscopic example and on D&K's "proving by experiment" sentence.

2. Morais, Jansen, Andrade & Dragicevic 2021, "Can Anthropographics Promote Prosociality? A Review and Large-Sample Study" (CHI 2021): exists, but HAL was blocked. A blog reports 786 participants and a small positive effect; this is not verified at source and should not be used without the paper.

3. Correll's own caveat under "We ought to anthropomorphize data" (A5): person-shaped glyphs have "not been shown to produce any additional empathic response". The ethics paper most cited for humanising data concedes the evidence gap.

4. Quispel, Maes & Schilperoord 2018, "Aesthetics and Clarity in Information Visualization: The Designer's Perspective", Arts 7(4):72, open access. https://www.mdpi.com/2076-0752/7/4/72. Interviews with 10 professional designers plus a review of 26 information design handbooks (SP). "Results show that, according to the information designers, clarity and aesthetics are the main criteria, with clarity being the most important. They aim to objectively inform the public, rather than conveying personal opinions." (SP) It tests, and contradicts, the scientists' assumption that designers put attractiveness first.

5. Börner, Maltese, Balliet & Heimlich, "Investigating aspects of data visualization literacy using 20 information visualizations and 273 science museum visitors", Information Visualization. https://cns.iu.edu/docs/publications/2015-borner-investigating.pdf. Abstract, SP: "a total of 273 visitors were shown 5 out of 20 different visualizations"; three US science museums; "many have a hard time naming and interpreting visualizations"; "most participants pointed to superficial features such as color, lines, or text as important to developing understanding". A public-audience constraint on unfamiliar forms.

6. Kosara's second criterion — "the visualization must be able to stand on its own" (SP) — together with the eye-candy sentence (SV) is a published near-statement of the removal test from inside the field.

7. The MoMA Fragapane label is an institutional statement of the chapter's subject: "Information design often goes beyond mere description to become an expressive interpretation of reality."

8. Source hygiene: Lupi's fourth heading reads "Flawed" on PrintMag and "Imperfect" on her site; PrintMag prints Dear Data's start as 2004; MoMA gives two end dates for Applied Design; D&K add "at the bottom" to Kennedy's fourth convention. Quote each from the version cited.

LEFT OUT, AND WHY
- Lau & Vande Moere axis definitions, and the Vande Moere & Purchase triangle and "design" sentences: full texts unreachable; abstracts only.
- Kostelnick 2008: unreachable; only a secondary characterisation, which cites his 2016 article.
- Munzner 2014 book text: not open; slides and two secondary course pages only.
- Mackinlay's Figure 14/15 lists: scan not machine-readable.
- Tufte: not online at source.
- Vande Moere et al. 2012 and Cawthon & Vande Moere 2007 primaries: unreachable; n not obtained.
- Kennedy & Hill 2018, and Kennedy & Engebretsen 2020: 403 / not attempted.
- Ars Electronica, Cooper Hewitt, Design Museum records: not checked.
- Correll, Bertini & Franconeri 2020 and Pandey et al. 2015: skipped as instructed.
- Venue and year of Prantl et al., and the CHI venue line for Correll 2019: not printed on the copies read.

RICH REFERENCES
1. Kennedy, Hill, Aiello & Allen 2016, accepted manuscript — https://eprints.whiterose.ac.uk/id/eprint/93521/3/repository20.pdf. The four conventions, the designers' own words, and a method section that shows how far the claim reaches.
2. D'Ignazio & Klein 2020, chapter 3 — https://data-feminism.mitpress.mit.edu/pub/5evfe9yd. Makes the case against neutral plainness and also concedes "Don't Never Do a God Trick".
3. Arunkumar, Padilla, Bae & Bryan 2023 — https://arxiv.org/pdf/2307.10571. The one reader study that separates aesthetic pleasure from conveying the message.
(Mackinlay 1986 is the formal anchor for A1.)

SURPRISED
- The Fragapane/MoMA claim held up: three records, all "Gift of the designer", accession 96–98.2023, none on view. "Noise Pollution" is the one of the three with no label and no exhibition on its record.
- Mackinlay calls his own effectiveness theory "conjectural" and its extended ranking "not been empirically verified", in a paper usually cited as settled ground.
- The conventions paper tested no readers, and D&K's "sociological analysis" summary can be read as stronger than the method supports.
- Viégas & Wattenberg's paper has no "sublime"; the common pairing of them with the sublime comes from Kosara and Sack.
- The Information is Beautiful Awards' published criteria have eight heads and none of them is accuracy or truth.
- Dear Data was bought with committee funds, while Wind Map, Flight Patterns and the Fragapane works were gifts of the designers.
- The fetch reader invented or mis-shaped text several times: a page range for Pousman, three different orders for Mackinlay's figure, "But if" for "So if" in Data Feminism, and sentences without the search word when asked for "leverag". The presence checks caught each.

WebSearch calls used: 24.


---

## Agent B

AGENT B REPORT — AFFECT AND PERCEPTION EVIDENCE (Chapter 14)
All sources fetched 6 October 2026. WebSearch calls used: 30 of 30.
Marks: STRING-VERIFIED = passed a second-fetch YES/NO presence check (false control strings were included and correctly rejected); SINGLE PASS = one reading only; ABSTRACT = only the abstract was reachable.
Access notes: HAL (all portals), PubMed/PMC, dl.acm.org, Semantic Scholar, ScienceDirect and OSF were blocked or empty; Europe PMC was proxy-refused; ResearchGate rate-limited after two successful reads. Several n values could therefore not be reached and are flagged, not guessed.

FOUR CORRECTIONS TO THE BRIEF'S CITATIONS
- Nothelfer, Gleicher & Franconeri 2017 is in Journal of Experimental Psychology: Human Perception and Performance 43(9), 1667–1676, not TVCG 23(1). (STRING-VERIFIED «Vol. 43, No. 9, 1667–1676»)
- Anderson & Robinson is TVCG 28(8), 2867–2878, 2022 per Penn State Pure (early access 2021). (SINGLE PASS)
- Garvey, Pietrucha & Meeker 1997 is a Clearview-font study; its abstract says nothing about mixed case versus capitals, despite the title.
- Lazard & Atkinson 2015 measured issue-relevant thinking (elaboration), not perceived credibility.

B1. ANTHROPOGRAPHICS

Boy, Pandey, Emerson, Satterthwaite, Nov & Bertini 2017 (CHI). Peer-reviewed crowdsourced experiments.
URL: https://www.researchgate.net/publication/312166759 (full text rendered there; the visualizingrights.org PDF failed on a certificate error).
- Design: seven experiments on Amazon Mechanical Turk, 50 participants recruited for each. STRING-VERIFIED: «seven experiments»; «we recruited 50 participants». SINGLE PASS: "we contribute the results of seven experiments as an initial assessment"; "We recruited 50 participants on AMT who had not participated in our pre-study"; "We recruited 50 new participants for each".
- Measures (SINGLE PASS): "We measured participants' empathic concern, personal distress, perception of story-protagonists' responsibility, and perception of justice of donating for each HR narrative on 7-point scales", plus donation likelihood and allocation.
- Finding, STRING-VERIFIED: "Contrary to our expectations, we consistently find that anthropomorphized data graphics and standard charts have very similar effects on empathy and prosocial behavior."
- STRING-VERIFIED fragments: «anthropographics are neither truly beneficial, nor detrimental»; «they can afford to be abstract».
- Retained n per experiment (48, 46, 48) came from the reader's paraphrase only; unverified.
- Role: the first direct test of humanised marks against plain charts found no difference in feeling or giving.

Morais, Jansen, Andrade & Dragicevic 2020 (TVCG), design space. Practitioner/analytic framework. Paper itself unreachable; dimensions confirmed from two independent sources.
- Via Sorapure 2022, Big Data & Society 9(1), https://journals.sagepub.com/doi/full/10.1177/20539517221098414 (Sorapure describing Morais), STRING-VERIFIED: «consisting of seven dimensions in two broad categories: what is shown and how it is shown»; «the four dimensions are granularity, specificity, coverage, and authenticity»; «the three dimensions are realism, physicality, and situatedness».
- Authors' own catalogue, https://luizaugustomm.github.io/anthropographics/ (SINGLE PASS), levels: Granularity low/intermediate/maximum; Specificity low/intermediate/high; Coverage minimum/partial/full; Authenticity partial/full; Realism low/intermediate/high; Physicality low/intermediate/maximum; Situatedness low/intermediate/high/maximum.
- Corpus, from the authors' VISU 2021 summary (https://journee-visu.github.io/2021/documents/moraiz.pdf, SINGLE PASS): "an analysis of 115 visualizations collected from newspapers, websites, and research papers".
- Role: a vocabulary for what "humanising" varies; it is not evidence of effect.

Morais, Jansen, Andrade & Dragicevic 2021 (CHI). Peer-reviewed, preregistered, crowdsourced; hypothetical money.
Abstract at https://anthropographics.github.io/ (SINGLE PASS, non-leading sentence listing):
- "Empirical studies have recently examined whether anthropographics indeed promote empathy, compassion, or the likelihood of prosocial behavior, but findings have been inconclusive so far."
- "We tested an information-rich anthropographic against a simple bar chart, asking participants to allocate hypothetical money in a crowdsourcing study."
- "We found that the anthropographic had, at best, a small effect on money allocation."
- "Such a small effect may be relevant for large-scale donation campaigns, but the large sample sizes required to observe an effect and the noise involved in measuring it make it very difficult to study in more depth."
Numbers from the authors' published analysis pages (not the paper PDF, which was unreachable):
- Experiment 1, https://anthropographics.github.io/exp1/planned-analysis.html. STRING-VERIFIED: «Total sample size: 128» (64 rich-first, 64 poor-first); primary effect «3.8, 95% CI [-1.7, 9.3]»; personal-donation effect «-1.8, 95% CI [-7.1, 3.1]». Standardised (SINGLE PASS): "Cohen's d : 0.12, 95% CI [-0.13, 0.37]".
- Experiment 2, https://anthropographics.github.io/exp2/planned-analysis.html. STRING-VERIFIED: «786» total (Anonymous & Rich 196, Anonymous & Poor 207, Named & Rich 195, Named & Poor 188); information-richness effect «3.4, 95% CI [0.021, 6.8]» on a 0–100 allocation scale; anonymisation «0.14, 95% CI [-3.3, 3.5]». Standardised, STRING-VERIFIED: «0.14, 95% CI [-0.0011, 0.28]»; probability of superiority «0.54, 95% CI [0.5, 0.58]».
- Review conclusion, as quoted by Sorapure 2022 (fragment STRING-VERIFIED in Sorapure): "the overall inconclusive results from the range of experiments [about anthropographics] conducted by researchers so far call for some skepticism."
- Authors' later summary (VISU 2021, SINGLE PASS, grammar as printed): "The results from our studies call for caution in the belief that current design strategies for anthropographics are substantially effective than using other charts."
- Role: the largest test puts the effect at about 3 points in 100 (d ≈ 0.14), with an interval touching zero.

Campbell & Offenhuber 2019, Information Design Journal 25(1), 71–86. ABSTRACT only; n not reachable.
URL: https://benjamins.com/catalog/idj.25.1.06cam
- STRING-VERIFIED fragments: «appeals to emotion through proximity techniques – the contextual framing of a visualization»; «people feel greater interest towards a topic when the visualized data are more relevant to them»; «data representing events closer in time are more affecting».
- Role: framing by relevance and recency moved interest and affect; that is a content choice, not a mark-styling one.

B2. AFFECTIVE VISUALISATION DESIGN

Lan, Shi, Wu, Jiao & Cao 2021, "Smile or Scowl?" (TVCG). Crowdsourced labelling plus qualitative coding; correlational.
URL: https://idvxlab.com/papers/2021TVCG_Smile_Lan.pdf
- Corpus and samples, STRING-VERIFIED: «We identified 976 of the 1526 infographics»; «We recruited 490 participants from MTurk»; «resulting in 117,120 ratings in total»; «identify 12 infographic-associated affective responses»; «We evaluated the design heuristics with 15 designers». SINGLE PASS: "We conducted a crowdsourcing study with 245 participants" (first study).
- The 12 responses (SINGLE PASS): happy, surprised, excited, content, awestruck, hopeful; sad, concerned, shocked, overwhelmed, bored, annoyed.
- Factors: STRING-VERIFIED «two categories: Usability, and Expressiveness». Usability: accessibility, readability, messaging, credibility. Expressiveness: embodiment, narrative, uniqueness (factor names SINGLE PASS).
- STRING-VERIFIED: negative responses «are mainly caused by poor usability (H1), especially low accessibility (H1-1), small font size».
- SINGLE PASS: "Positive affects such as happy and content may occur when infographics present a comprehensible data visualization (H1-1-1), a clear layout (H1-1-3), and detailed explanations (H1-3-3) to the audience."
- Role: in this corpus, bad feeling tracks unreadability and good feeling tracks comprehensibility, so affect and legibility were not opposed.

Lan, Shi, Zhang & Cao 2021, Kineticharts (TVCG/VIS). Two user studies.
URL: https://idvxlab.com/papers/2021VIS_Charts_Lan.pdf
- Scheme (SINGLE PASS): "an animation design scheme for creating charts that express five positive affects: joy, amusement, surprise, tenderness, and excitement"; STRING-VERIFIED «resulting in 60 animated charts for the five affects».
- Study I, STRING-VERIFIED: «We recruited 80 college students (55 females), aged from 18 to 41»; measured affect recognition.
- Study II, STRING-VERIFIED: «We recruited 197 participants who speak English as their first language from Prolific»; measured expressiveness, engagement, and four comprehension questions.
- Comprehension result (SINGLE PASS, full sentence): "Mann-Whitney U tests showed that Kineticharts earned similar scores in people's comprehension of the story subject (M = 2.92), data categories and values (M = 2.22), and trend (M = 2.85) with the baseline (M = 2.90, 2.18, 2.90, respectively), and the differences were not significant (p = .737, .257, .348, respectively)."
- Abstract claim (SINGLE PASS; the fragment «without hindering data comprehension» was confirmed present): Kineticharts "can accurately convey affects, and improve the expressiveness of data stories, as well as enhance user engagement without hindering data comprehension compared to the animation design from DataClips".
- Caveats: positive affects only; the baseline was another animation, not a static chart; non-significance is not demonstrated equivalence.
- Role: expressive motion added feeling with no detected comprehension loss in one study.

Lan, Wu & Cao 2023, "Affective Visualization Design" (TVCG). Literature review and design space.
URLs: https://arxiv.org/abs/2308.02831 and https://arxiv.org/html/2308.02831v2
- Corpus, STRING-VERIFIED: «kept 109 papers»; «identified 61 projects».
- Design space (abstract, SINGLE PASS): "three dimensions, including design fields (where), design tasks (what), and design methods (how)". Tasks listed (SINGLE PASS): inform, engage, experiment, provoke, advocate, socialize, heal, empower, commemorate, archive. Methods: six genres plus four strategies, STRING-VERIFIED «sensation, narrative, behavior, and context».
- Five justifications for emotion (SINGLE PASS): application, usefulness, rhetoric, sociology, humanism.
- Affect versus accuracy, the key sentence (fragment STRING-VERIFIED; full sentence SINGLE PASS): "In several user studies [44, 47], researchers indeed observed that affective visualization design was not at odds with data comprehension."
- STRING-VERIFIED fragments: «no data visualization is truly objective»; «emotion is not separate from, but is a huge part of rationality»; «the power of emotion may be exploited by people with malevolent intents».
- Role: the field's own survey rests the "no conflict" claim on two studies and names manipulation as the open ethical problem.

Lee-Robbins & Adar 2022 (TVCG). Interview study and taxonomy.
URLs: https://arxiv.org/abs/2208.04078 and https://arxiv.org/pdf/2208.04078
- Sample, STRING-VERIFIED: «we invited 17 people to participate in an interview, of which 12 accepted».
- Taxonomy, STRING-VERIFIED: verbs «observe, position, strengthen, connect, and behave». Nouns (SINGLE PASS): "we redefined the lower levels of the nouns as appraisal and attitude, while maintaining the upper levels of value and value system." Template (SINGLE PASS): "The viewer will [verb] [noun]".
- Under-served point (abstract, SINGLE PASS): "We pay less attention to affective intents--those that seek to influence or leverage the audience's opinions, attitudes, or values in some way." And: "Because such goals are often considered a violation of perceived 'neutrality' or are 'political,' designers may resist or be unable to describe these intents, let alone formalize them as learning objectives." And: "visualization designers rarely acknowledge or formalize affective objectives."
- Role: gives a way to declare an affective intent so it can be checked, rather than left implicit.

B3. AFFECTIVE COLOUR, CONGRUENCE, DISPLAY POLARITY

Bartram, Patra & Stone 2017 (CHI). Three studies.
URL: https://www.tableau.com/sites/default/files/2023-01/Affective%20Color%20CHI%202017.pdf
- Samples, STRING-VERIFIED: «we analyzed the palettes of 8608 images» (Study 1, image corpus); «76 persons, roughly distributed by gender» (Study 2, choosing 5-colour palettes for a bar chart or map); «38 users (and an additional 2 with incomplete data) participated» (Study 3, best/worst palette per affect).
- Affects (SINGLE PASS): core Calm, Exciting, Positive, Negative; "We added 4 'pragmatic' affects: Serious, Playful, Trustworthy and Disturbing."
- Colour properties, STRING-VERIFIED: «Calm, Playful and Positive were much lighter than Disturbing, Serious and Negative»; «Calm was the least saturated of the affects»; Calm «makes strong use of cool colors (blues and greens) and is overall high lightness and low chroma»; «Trustworthy showed very little structure».
- SINGLE PASS: "Exciting emphasizes warmer and higher chroma colors: more reds and yellows." "Negative, as anticipated, has more browns, dark reds, and greys." "Serious shared the greys of Negative but used more blue". "Trustworthy also has blues, purples and some greens." "highly saturated light colors will NOT be appropriate for Serious or Trust, or Calm".
- Role: small data palettes carry mood reliably through lightness and chroma; "trustworthy" had no clear colour signature.

Anderson & Robinson (TVCG 28(8), 2022). ABSTRACT only; n and the objective-measure statistics not reachable.
URL: https://pure.psu.edu/en/publications/affective-congruence-in-visualization-design-influences-on-readin/
- STRING-VERIFIED: «We report both objective (pattern detection; area comparison) and subjective (affective quality; appropriateness; preference) measures»; «affectively congruent colors amplify perceptions of the affective qualities of maps with emotive topics, affective incongruence may cause confusion»; «affective congruence is particularly influential in maps of positive-leaning data topics».
- The abstract reports amplified affect and possible confusion; it does not claim an accuracy or time gain from congruence. Whether accuracy changed is unverified.
- Role: congruent colour demonstrably changes how the topic feels; a reading benefit is not claimed in the abstract.

Piepenbrock, Mayr, Mund & Buchner 2013, Ergonomics 56(7). Lab experiment.
URL: https://www.psychologie.hhu.de/.../Publikationen/2013/Piepenbrock-2013-Positive_display_polarity_is_.pdf (full path as returned by search)
- STRING-VERIFIED: «Participants were 85 older and 84 younger adults»; «A positive polarity advantage was found for both age groups»; «The presentation in positive polarity is recommended for all ages»; «Dark characters on light background lead to better legibility and are strongly recommended independent of observer».
- Ages (SINGLE PASS): older 60–85, younger 18–33. Tasks: Landolt C acuity, and proofreading 250-word texts in 10 point Helvetica.
- Effect sizes for the acuity comparison, STRING-VERIFIED as printed: younger «d ¼ 2.17», older «d ¼ 0.58» (¼ is the PDF's rendering of "=").
- Mechanism (SINGLE PASS): "The brighter display leads to a greater pupillary contraction that, in turn, reduces the effects of spherical aberrations and increases the depth of field".
- Role: the measured cost of a dark ground for small text, at all ages.

Buchner & Baumgartner 2007, Ergonomics 50(7), 1036–1063. ABSTRACT (via https://eurekamag.com/research/013/854/013854254.php); n not given.
- STRING-VERIFIED: «proofreading performance was consistently better with positive polarity»; «This positive polarity advantage was independent of ambient lighting»; «colour contrast ( red text on green background) could not compensate for a lack of luminance contrast».

Dobres, Chahine & Reimer 2017, Applied Ergonomics 60. ABSTRACT, SINGLE PASS (ResearchGate, then rate-limited); n not reachable.
- "legibility thresholds, quantified as the amount of time needed to read a word accurately, were highest for the negative polarity configurations under dark ambient illumination, indicated worse performance."
- "Conversely, the positive polarity conditions under dark ambient illumination and all conditions under bright illumination demonstrated significantly reduced thresholds, indicating greater legibility."
- Role: at a glance, the dark-ground penalty appears in a dark room and disappears in daylight-like light.

B4. REDUNDANCY AND THE PRECISE TWIN

Nothelfer, Gleicher & Franconeri 2017 (JEP:HPP 43(9)). Lab experiments.
URL: https://graphics.cs.wisc.edu/Papers/2017/NGF17/ (PDF linked there)
- n (SINGLE PASS except Exp. 3): Exp. 1a 12 subjects; 1b and 1c 16; Exp. 2a 15; 2b 16; Exp. 3 STRING-VERIFIED «We recruited 17 Northwestern University students and community members».
- STRING-VERIFIED: redundant coding «may carry costs, and there is no direct evidence for a benefit» (the prior state); «this practice can indeed yield a large benefit for rapidly segmenting objects within a dense display».
- Limit (SINGLE PASS): "when one dimension, such as color, is more easily discriminable, adding shape differences will likely not yield a redundancy advantage."
- Role: evidence that saying the same thing in two channels helps segmentation, with a stated boundary.

Dual presentation (same data, two forms). No toggle study of "expressive form plus plain twin" was found. Nearest evidence:
- Ottley, Kaszowska, Crouser & Peck 2019 (EuroVis short), https://diglib.eg.org/bitstream/handle/10.2312/evs20191181/121-125.pdf. Eye-tracking, Bayesian reasoning problem. STRING-VERIFIED: «32 participants took part in the study» (29 analysed, SINGLE PASS); «We found no significant effect of presentation on accuracy»; «Text = 55/87 correct, Vis = 56/87 correct, Text +Vis = 59/87 correct». Abstract (SINGLE PASS): "These tendencies persist even when text and visualization are presented together, indicating that users do not integrate information well across the two representation types." Role: showing both forms does not by itself make readers use both.
- Stokes, Setlur, Cogley, Satyanarayan & Hearst 2022 (TVCG), https://arxiv.org/abs/2208.01780, ABSTRACT, SINGLE PASS: "302 participants ranked univariate line charts containing varying amounts of text"; "We find that heavily annotated charts were not penalized." Role: plain-language text on the chart was preferred, not punished.

Hullman, Adar & Shah 2011 (TVCG). Position/synthesis paper, not an experiment.
URL: https://mucollective.northwestern.edu/files/2011-VisualDifficulties-InfoVis.pdf
- Thesis, STRING-VERIFIED fragments: «non-efficient visual elements may benefit comprehension and recall on the part of users»; «providing a counterpoint to efficiency-based design theory with guidelines that describe how visual difficulties can be introduced»; «We characterize effective graph design as a trade-off between efficiency and learning difficulties».
- Own caution, STRING-VERIFIED fragment: «may induce unproductive levels of frustration».
- "Desirable difficulties" appears as a borrowed term (SINGLE PASS): "psychologists have applied the term desirable difficulties to a class of techniques that hinge on 'going against one's intuitions'…"
- Later tests: no direct visualisation test was found. The underlying perceptual-disfluency effect has not held up: Xie, Zhou & Liu 2018, Educational Psychology Review 30(3), 745–771, https://link.springer.com/article/10.1007/s10648-018-9442-x, STRING-VERIFIED: «based on 25 empirical articles involving 3135 participants»; «there was no effect of perceptual disfluency on recall (d = − 0.01) or transfer (d = 0.03)»; it did «reduce participants' judgments of learning (d = − 0.43) and increase learning time (d = 0.52)». A preregistered replication (Weissgerber, Terhorst & Rummer 2024, Metacognition and Learning 19, N = 96; ABSTRACT, SINGLE PASS) reports "null results for disfluency, WMC, and their interaction for all learning outcomes."
- Practitioner rebuttal: Stephen Few 2011, https://perceptualedge.com/articles/visual_business_intelligence/visual_difficulties.pdf (SINGLE PASS): "Making visualizations of data unnecessarily difficult to read and interpret leads to unnecessary cognitive effort, without benefit."
- Role: "harder to read is better remembered" is not a licence; the meta-analysis shows it costs time and confidence for no recall gain.

B5. PHYSICALISATION AND GLANCEABILITY

Jansen, Dragicevic & Fekete 2013 (CHI). Lab experiment.
URL: https://www.aviz.fr/phys (abstract); n from the authors' re-analysis, https://idl.uw.edu/living-papers-paper/multiverse/index.pdf
- Abstract, STRING-VERIFIED: «We present the first infovis study comparing physical to on-screen visualizations»; «moving visualizations to the physical world can improve users' efficiency at information retrieval tasks»; «augmenting on-screen visualizations with stereoscopic rendering alone or with prop-based manipulation was of limited help»; «such as their ability to be touched and their perfect visual realism».
- n = 16 confirmed, STRING-VERIFIED in Dragicevic & Jansen 2018: «Sixteen participants were recruited». Re-analysis STRING-VERIFIED: «The study's findings appear to be robust to choices in statistical analysis». No ratio for the size of the speed gain was reachable.
- Role: the gain was for 3D bar charts made physical versus the same charts on screen; it is not evidence for physical over flat 2D.

Blascheck, Besançon, Bezerianos, Lee & Isenberg 2019 (TVCG 25(1)). Two perception studies.
URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2018/08/GlanceableVis-InfoVis2018.pdf
- n: 18 in each study (SINGLE PASS: "We recruited 18 participants (7 female, 11 male; 10 researchers, 8 students)"; "We recruited 18 new participants"). The reader's breakdown for Study 2 did not add up; treat only the totals as reported.
- Task (SINGLE PASS): "Participants' task was to select the larger of the two targets." Charts: bar, donut, radial bar; 7, 12 and 24 values.
- STRING-VERIFIED: «< 300 ms for the bar chart, < 220 ms for the donut chart, and in < 1780 ms for the radial bar chart»; «a vast majority of smartwatch interactions last under 5 s»; «Thresholds in the second study per chart type were on average 1.14–1.35× higher than in the first study».
- Limit (SINGLE PASS): "our thresholds should also be considered as a lower bound because we used a static watch."
- Role: one two-value comparison can be made in a fraction of a second from a conventional form; the unusual radial form took about six times longer.

B6. READING AT A DISTANCE AND IN MOTION

Garvey, Pietrucha & Meeker 1997, Transportation Research Record 1605, 73–79. ABSTRACT. Field experiments.
URL: https://trid.trb.org/view.aspx?id=475144
- STRING-VERIFIED: «exposed 48 older drivers to high-brightness guide signs displaying either the current or the Clearview font»; «nighttime recognition distances 16% greater than those allowed by the Standard Highway Series E(M) font»; «without increasing overall sign dimensions».
- The abstract is silent on case (checked explicitly). The mixed-case result is reachable only second-hand:
  - Tejero, Royo & Roca 2024 (Human Factors), as rendered on a ResearchGate page, SINGLE PASS and second-hand: "No support for differences in the legibility distance between titledcase and all-uppercase was found, whereas the recognition distance was significantly longer with titled-case".
  - USSC guideline (below), SINGLE PASS: "the 15 percent increase in letter height required when all upper case letters (all caps) are used instead of upper and lower case letters with initial caps, a difference in recognition distance documented in earlier studies".

Garvey, Eie & Klena 2016, Interdisciplinary Journal of Signage and Wayfinding 1(1). Peer-reviewed threshold-legibility study.
URL: https://journals.shareok.org/ijsw/article/download/3/1
- STRING-VERIFIED: «Sixty-four subjects from 19-87 years of age viewed 64 displays using 33 fonts»; «with uppercase often performing significantly better than lowercase»; «For all the 31 fonts that had upper and lowercase conditions, the uppercase words had higher mean LIs than the lower»; «In 22 of the cases, that difference was statistically significant»; «research has shown that using lowercase words can improve recognition distance over all-uppercase words».
- Authors' reconciliation (SINGLE PASS): "in recognition tasks, the reader knows what word he or she is looking for and merely has to match a mental image of that word with the word on the display… In a legibility task, the reader does not know what the display will say and therefore has to read all or most of the individual letters to build the word."
- Also (abstract, SINGLE PASS): "The choice of serif versus sans-serif alone does not have an important effect on display legibility."

Legibility index. Practitioner standard built on test-track research.
URL: https://usscfoundation.org/wp-content/uploads/2018/03/USSC-Guideline-Standards-for-On-Premise-Signs-2018.pdf (Bertucci & Crawford, Best Practice Standards for On-Premise Signs, 2015)
- STRING-VERIFIED: «representing the distance in feet for every inch of capital letter height at which a sign may be read»; «an average Legibility Index value of 30 may be used»; «signs displaying four to eight words in simple typography can be comfortably read and comprehended in approximately four seconds»; «one-tenth of a second per letter».
- Bullough 2017 review (IJSW 1(2), https://journals.shareok.org/ijsw/article/download/9/8) records 30, 35, 40 and 50 ft/in from different sources; the 50 ft/in figure is tied to Forbes et al. 1965 (SINGLE PASS).

UK guidance. Standard.
URL: https://assets.publishing.service.gov.uk/media/5c78f8c7e5274a0ebfec719c/traffic-signs-manual-chapter-07.pdf (Traffic Signs Manual Chapter 7, TSO)
- STRING-VERIFIED: «The size of an alphabet is specified in terms of its x-height»; «The overall size of a sign is determined by the chosen x-height»; «This will depend on the type of sign and, in most cases, the 85th percentile speed»; «should not indicate more than three directions as the sign would then become difficult to read».
- The x-height-by-speed table (Appendix A) and any stated distance ratio were not extractable; no ratio string was found in the text.

Words per glance.
- Bullough 2017, annotating Forbes, Snyder & Pain 1965, STRING-VERIFIED (it is Bullough's summary sentence, not Forbes's own words): «Only 3-4 short, familiar words can be read in a single glance at a sign».
- "Seven words" is trade practice with no cited study. Lamar (https://lamar.com/en/advertising-resources/design-tips, SINGLE PASS): "exposure time is typically four to five seconds"; "say it in seven words or less". Clear Channel Outdoor blog (SINGLE PASS): "the average viewer has only about six seconds"; "Stick to seven words or less". Neither page cites a source. An OAAA primary document was not found.

Museum labels. Bitgood 2000, Journal of Interpretation Research 5(2), is a review, not a study.
URL: https://www.academia.edu/54595991
- STRING-VERIFIED: «three principles of attention are used to organize what we know about interpretive label design» (the principles, SINGLE PASS: selectivity, motivated focusing, limited capacity).
- Figures belong to the studies it cites: Borun & Miller 1980, STRING-VERIFIED «Adult visitors were found to read an average of only 18 percent of the labels» and SINGLE PASS "they did read 68 percent of the printed material on the exhibits at which they chose to spend a longer amount of time"; Serrell 1998, STRING-VERIFIED «the median was 8 minutes» (mean total exhibition time 11 minutes; median stops 34%, SINGLE PASS); Bitgood & Patterson 1993, SINGLE PASS "breaking down a long label into three smaller ones (chunks), resulted in increased reading."
- The page also contains «visitors read an average of 200 words per label» (present, attribution not established); do not use without checking.
- No word-count thresholds or words-per-minute rates were found in this paper.
- Role for B6 overall: the only quantified rules for text read in passing are a letter-height ratio (about 30 ft per inch as a planning average), about half a second per word, and three or four words per glance; the popular "seven words" has no traceable study.

B7. ANIMATION AS FEEL VERSUS INFORMATION

Chevalier, Riche, Plaisant, Chalbi & Hurter 2016 (AVI, pp. 280–287). Review plus practitioner interviews; taxonomy, not an experiment. ABSTRACT (project page http://animations.recherche.enac.fr/).
- STRING-VERIFIED: «From bouncing icons that catch attention, to transitions helping with orientation, to tutorials, animations can serve numerous purposes»; roles «for keeping in context, teaching, improving user experience, data encoding and visual discourse».
- SINGLE PASS: "We reviewed academic publications and commercial systems, and interviewed professionals of various backgrounds."
- The individual role list and its count were not reachable.
- Role: separates animation that encodes data from animation that serves experience or discourse, which is the distinction a removal test needs.
Kineticharts (B2) is the only reachable study that measured affect and comprehension together. Shi et al. 2021 was not reachable.

B8. TRUST AND THE PROFESSIONAL LOOK

Boukhelifa, Bezerianos, Isenberg & Fekete 2012, TVCG 18(12), 2769–2778. ABSTRACT, SINGLE PASS (https://tobias.isenberg.cc/p/Boukhelifa2012ESV; PDF blocked by robots.txt); n not reachable.
- "Our results show that sketchiness is a viable alternative for the visualization of uncertainty in lines and is as intuitive as blur; although people subjectively prefer dashing style over blur, grayscale and sketchiness."
- It tests sketchiness as an uncertainty signal for lines; it is not a credibility study.
- Role: a hand-drawn look is read as imprecision, so it says something about the data whether intended or not.

Lazard & Atkinson 2015, Science Communication 37(1), 6–33. ABSTRACT (Sage; full text paywalled; n not reachable).
- STRING-VERIFIED: «Relying on two experiments»; «individuals engage in greater levels of issue-relevant thinking when shown infographics compared to messages that rely just on text or just on illustration».
- No credibility claim appears in the abstract.

Li & Moacdieh 2014, Proceedings of the HFES Annual Meeting 58(1), 1516–1520. ABSTRACT; n and the direction of the recall effect not stated there.
URL: https://journals.sagepub.com/doi/abs/10.1177/1541931214581316
- STRING-VERIFIED: «larger data sets (10 or more data points)»; «the presence of a time limit affected comprehension and short-term recall performance, while the type of chart significantly affected short-term recall»; «Participants found Holmes charts more attractive and memorable».
- Role: extends Bateman to denser charts under time pressure; time limits hurt comprehension, and embellishment's standing under time pressure is not settled by the abstract.
Wood et al. 2012: noted only, as instructed.

UNASKED THREADS
1. While & Sarvghad 2024 (IEEE VIS short), https://arxiv.org/html/2409.10841v2. Dark versus light mode for charts, not text. STRING-VERIFIED: «the contrast polarity that led to better performance did not always match their preferred polarity»; «resulting in an average percent difference of around 36%»; «making visualizations available in both contrast polarities». Abstract (SINGLE PASS): "the polarity that led to better performance and the resulting amount of improvement varied on an individual basis, with each polarity benefiting comparable proportions of participants." The abstract says «134 participants (69 below age 60, 66 aged 60 and above)», which sums to 135; the body reportedly says 135 recruited and 52 + 52 analysed (SINGLE PASS).
2. Budiu 2020, Nielsen Norman Group, https://www.nngroup.com/articles/dark-mode/ (practitioner synthesis, SINGLE PASS): "In people with normal vision (or corrected-to-normal vision), visual performance tends to be better with light mode, whereas some people with cataract and related disorders may perform better with dark mode." It recommends letting users switch.
3. Blair, Wang & Perin 2024 (TVCG), https://arxiv.org/html/2407.18427 (SINGLE PASS): five crowdsourced experiments, 50 participants reported for each of four; "certain data characteristics influence the emotion of viewers even when the data has no meaning"; "The effect of color palette on emotion (for both arousal and valence) is larger than that of data trend".
4. Lan, Wu and colleagues, "The Chart Excites Me!", https://arxiv.org/abs/2211.03296 (ABSTRACT, SINGLE PASS): "a corpus of 265 data visualizations and … a crowdsourcing study with 184 participants"; texts blurred; four features including colourfulness and number of visual channels correlated with arousal.
5. Xie, Zhou & Liu 2018 disfluency meta-analysis (in B4).
6. Garvey, Eie & Klena 2016 on capitals at threshold (in B6).
7. Morais's own reading, in a trade interview (builtin.com, SINGLE PASS, journalist-reported): "It seems that anthropographics might slightly increase empathy but not compassion. But the effect is not as large as practitioners expected."
8. Dragicevic & Jansen 2018 multiverse re-analysis of the physical-visualisation study (in B5): a model of showing a finding survives 56 analysis choices.

LEFT OUT, AND WHY
- n for Campbell & Offenhuber, Anderson & Robinson, Dobres et al., Buchner & Baumgartner, Boukhelifa et al., Lazard & Atkinson, Li & Moacdieh: full texts blocked or paywalled. Nothing guessed.
- Morais 2020 and Morais 2021 paper PDFs (HAL and ACM blocked): dimensions and numbers taken from Sorapure 2022 and the authors' own catalogue and analysis pages instead.
- Garvey 1997 full text; Tejero et al. 2024 at source (Sage 403).
- Traffic Signs Manual Appendix A x-height table; any TRL report.
- OAAA primary guidance; Shi et al. 2021; Chevalier's full role list.
- Piepenbrock, Mayr & Buchner 2014 (small character sizes): seen only in NN/g's summary, not fetched.

RICH REFERENCES
1. Morais, Jansen, Andrade & Dragicevic 2021 with its open analysis site (https://anthropographics.github.io/): review, two preregistered experiments, and every estimate with intervals. The best single source on whether humanising data moves action.
2. Lan, Wu & Cao 2023 (https://arxiv.org/html/2308.02831v2): 109 papers, 61 projects, five arguments for emotion, and a frank ethics section. The map of the affective-design field.
3. Bullough 2017, "Factors Affecting Sign Visibility, Conspicuity and Legibility: Review and Annotated Bibliography" (IJSW 1(2)): one annotated route into sixty years of distance-reading research, with legibility-index values by source.

SURPRISED
- The humanising evidence is weaker than its reputation: seven null experiments (Boy), then a best case of about 3 points in 100 at n = 786 with the interval's lower bound at 0.021.
- Capitals beat lower case in all 31 fonts in an unprimed threshold-legibility test; the familiar mixed-case advantage is for recognising a word you are already looking for.
- "Seven words" has no source on the pages that repeat it; the nearest research statement is three to four short words per glance, itself a reviewer's summary of a 1965 report.
- The disfluency effect behind "visual difficulties" is null on recall across 3,135 participants, while making readers slower and less confident.
- Showing text and chart together did not raise accuracy, and eye-tracking suggested readers did not integrate them; a plain twin beside an expressive form cannot be assumed to be read.
- For charts, as opposed to text, dark versus light polarity helped different individuals in roughly equal proportion, and preference did not predict which.
- The fetch reader twice answered YES to a string that was only a paraphrase of the real sentence (Kineticharts, Ottley); where that happened I have quoted the longer real sentence and marked it SINGLE PASS.


---

## Agent C

AGENT C — THE GALLERY, audited live. All fetches 6 October 2026.

HOW TO READ THIS
- Tooling limit: only the text-reader fetch worked (raw curl is refused by the proxy). I could not see pixels, so colour, decoration, hover behaviour and keyboard operability are NOT observable unless the page says so in words. "n/d" = not determinable.
- Blocked at source (quote nothing): bbc.co.uk, bbc.com, the web.archive.org copy of the BBC page, nytimes.com, theguardian.com, reuters.com, ft.com (all SITE_BLOCKED); washingtonpost.com (403); osf.io and sciencedirect.com (robots); github.com tree pages (robots; raw.githubusercontent.com works).
- One page I must flag: arXiv 2607.01593 ("Made to Feel: How Designers Bring Emotions into Affective Visualization", surfaced by a search on Halloran) returned HTTP 429 with an instruction not to retry. Unread.
- Marks: SV = STRING-VERIFIED (YES/NO re-fetch, with a false control string that correctly returned NO). SP = SINGLE PASS.

C1. THE PUDDING
"This is a teenager" — https://pudding.cool/2024/03/teenagers/ (script-rendered; text layer readable)
(i) Leads with written sentences, no input demanded. SV: «This is a teenager», «by Alvin Chang», «We'll call him Alex.», «Keep scrolling ↓». Control «Enter your age to begin» = NO.
(ii) Provenance is inline, not on the first screen. SP: «They're among the thousands of kids who are part of the National Longitudinal Survey of Youth.»; chart-level lines «Source: National Center for Education Statistics», «Source: General Social Survey», «Source: National Center for Education Statistics, College Board, US Census». No heading "Methodology"/"Data and methods" (both NO); the words GitHub, Methods, Notes, weights do not appear in the fetched text. Caveat: a methods note inside a script-only element would be invisible to me.
(iii) Scroll is required; click is optional (SV «(Click a kid to see details)»); a linear alternative is offered (SV «Don't feel like scrolling? Watch the video instead!»). The essay ends in an "Explore the data" section (SP «Select other factors to sort these people using the pulldown option on the top.»). Keyboard: n/d.
(iv) No separate method statement found. (v) No published evaluation found. Award only: Gold, People, Language & Identity, IIB Awards 2024 (SP).
"Is the love song dying?" — https://pudding.cool/2024/11/love-songs/ — script-rendered; two attempts returned only the title and meta description: «We categorized songs in the Billboard Top 10 to see if love songs are on the decline.» (SP, same string on its IIB showcase page). Credits on IIB: David Mora and Michelle Jia. Gold (Arts, Entertainment & Culture) and "Most Beautiful", IIB 2024. Nothing else reportable.
How they work — https://pudding.cool/about/ — SV: «The Pudding explains ideas debated in culture with visual essays.»; «We're not chasing current events or clickbait.»; «Visual essays are an emerging form of journalism.»; «Each team member can do every step: research and reporting, data analysis, design, writing, and code.»; «There are no deadlines because we are not tied to news events.». Control «Every essay is peer reviewed before publication.» = NO. The about page contains no sentence with "method", "open", "GitHub", "correct" or "transparen" (SP).
https://pudding.cool/pitch/ — SV: «Is it an argument, or just a topic?»; «Why is this uniquely a visual data story?»; «Do you have the receipts?»; «a rough data roadmap»; «custom data analysis and visual design are absolutely essential». SP: «If the data is a mystery, the pitch is a no-go.»
Role: practitioner case. The method gate is at commissioning, not printed on the piece.

C2. OUR WORLD IN DATA — https://ourworldindata.org/grapher/life-expectancy
(i) Order in the static page: heading, subtitle «Long-run data», a one-sentence definition of the indicator, the source/date block, then key-point bullets. The chart exists in static HTML only as a PNG fallback; the interactive is script-rendered. No input demanded.
(ii) SV fragment: «with major processing by Our World in Data». Full line (SP; three of four passes placed it under the title): «Data source: Riley (2005); Zijdeman et al. (2015); HMD (2025); UN WPP (2024) – with major processing by Our World in Data». Labels with values (SP, consistent across passes): «Last updated» 2025-10-22; «Next expected update» 2026-10-22 (SV label); «Date range» 1543-2023; unit «years».
«Learn more about this data» — NOT in the fetched text (NO; closest «Read about our data pipeline»). It presumably sits in the script-rendered chart footer; I could not confirm it. «What you should know about this indicator» also NO; the static heading is «Frequently asked questions».
Headings in order (SP): Frequently asked questions / How did Our World in Data process this data? / Notes on our processing step for this indicator / Data sources (one sub-heading per source) / How to cite / How to cite this page (SV) / How to cite this data / Related research and writing / Related charts / Download / Quick download / Data API.
SP: «Download the data shown in this chart as a ZIP file containing a CSV file, metadata in JSON format, and a README.»; «If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation».
(iii) n/d. (iv) Method is on the same page as the chart. (v) No evaluation searched for or found. Decorative treatment: none evident in text; not verifiable visually.

C3. ONS
Explore Local Statistics — explore-local-statistics.beta.ons.gov.uk now 302-redirects to https://www.ons.gov.uk/explore-local-statistics/; the word "beta" does not appear on the page (SP).
(i) Headline, one sentence, then an input; no chart, map or statistic precedes the search box (SP). SV: «Find, compare and visualise statistics about places in the United Kingdom.»; «Find an area»; «Search for a postcode, local authority, region, parliamentary constituency or other named area.». Control «Enter your postcode to see your personalised dashboard» = NO.
(ii) SV fragment «quality and methodology information (QMI) report»; SV «We value your feedback on these statistics.». SP: «You can download all of the data available on the Explore Local Statistics service in an XLSX, CSV, CSVW or JSON-Stat format.». SP only: «Explore 116 indicators, including household income, further education participation and life satisfaction.» (two passes agreed, but the YES/NO check answered NO while giving the identical string — treat the number as unconfirmed).
Census 2021 template — https://www.ons.gov.uk/visualisations/censusareachanges/
Landing demands a choice (SP): «Choose a local authority area to find out what Census 2021 tells us about how people's lives have changed over 10 years.». Dates (SP): «These articles were first published on 8 December 2022…» and «They were updated on 19 January 2023…».
One area page opened for furniture only (URL pattern …/censusareachanges/[code]/). Headline template «How life has changed in [area]: Census 2021». First element after the headline is a written sentence about the area, not a selector or chart. SV: «Source: Office for National Statistics – 2011 Census and Census 2021»; «Download the data (CSV)»; «Save as image (PNG)»; «Show embed code»; «About the data»; the word «semi-automated». Full sentences SP: «The articles have been written and semi-automated by our data journalists and are a new publishing format for the Office for National Statistics.»; «Topics are chosen and ordered automatically based on how relevant they are for each area, however all data are checked before publishing.». Control «Hover over the chart to see values» = NO. No «Published:» label; the date is printed bare.
(v) Not searched (Chapter 11 has it).

C4. BBC POSTCODE INTERACTIVES — BLOCKED. bbc.co.uk/news/health-59549800 (a tracker-type piece), the bbc.com mirror and the Wayback copy all returned SITE_BLOCKED. I quote nothing from the BBC and cannot report first screen, furniture or interaction.
Method description only:
- Data Journalism Handbook, "Data Journalism at the BBC", Andrew Leimdorfer — https://datajournalism.com/read/handbook/one/in-the-newsroom/data-journalism-at-the-bbc (year not printed on the page). SV: «Enable a reader to discover information that is personally relevant»; «Reveal a story that is remarkable and previously unknown»; «Help the reader to better understand a complex issue»; «Readers can find local schools by entering a postcode, and compare them on a range of indicators.»; «The ability to easily share a 'personal' fact is something we have begun to incorporate as standard.». Control (user-testing claim) = NO.
- Applied Works, "How we built the BBC's most shared data tool" (Medium, April 11, 2023, about the 2013 class calculator — an input-first tool, not a postcode one). SV: «It wasn't just a black box that spat out a result at the end.»; «We tested it on people to ensure not only that the algorithm worked, but also that it was fun and easy to use»; «the most shared BBC page ever».
- BBC Shared Data Unit GitHub org (https://github.com/BBC-Data-Unit) is reachable: "10 of 317 repositories", latest update January 2026 (SP). No general method statement on the org page.
(v) No evaluation found.

C5. GAPMINDER
Home — https://www.gapminder.org/ — SV: «You are probably wrong about»; «Upgrade your worldview»; «Gapminder is an independent educational non-profit fighting global misconceptions.». SP: «Learn about the 17 UN Goals in this 18 Question Quiz.». The door is a challenge and an invitation to a quiz; no input is forced (control «Take the test before you read on.» = NO).
Upgrader — https://upgrader.gapminder.org/ — first five lines (SP): "Welcome to" / "The Worldview Upgrader" / «We can predict what you are wrong about.» / «We have asked thousands of important fact-questions to lots of people and identified the most common misconceptions.» / "Search". The two sentences and the title are SV.
Dollar Street — https://www.gapminder.org/dollar-street — shows content at once; no input required (SP). First elements: "Dollar Street" / "Families" / "Families in The World" / «The World by income per month» / "Poor" / "Rich". SV: «photos as data to kill country stereotypes»; «Dollar Street is a Gapminder project - free for anyone to use.». Method at /dollar-street/about — SV: «Imagine the world as a street ordered by income.»; «Everyone lives somewhere on the street.»; «taking photos of up to 135 objects»; «tries to measure consumption rather than salary or income». SP: «Since the cost of living can vary a lot between countries, we use dollars adjusted for purchasing power parity (PPP).». No sentence there contains "estimate", "approximate" or "rough" (SP). The about page and the landing page give different family/country counts.
Tools — gapminder.org/tools: "Too many redirects" twice. Unreachable.
Ignorance Project — https://www.gapminder.org/ignorance/ — SV: «The mission of Gapminder Foundation is to fight devastating ignorance» + «with a fact-based worldview that everyone can understand»; «We use surveys to ask representative groups of people simple questions» + «about key-aspects of global development»; «Novus Group International AB»; «the chimpanzee would score 2.5 correct answers». Control «All surveys were preregistered» = NO.
Evaluation method (Gapminder's own pages, not peer-reviewed):
- 2017 study, /ignorance/gms/ — SV: «The surveys were commissioned to Novus and Ipsos MORI»; «online panels with representative samples of the general public»; «Every question had three alternative choices: A, B or C.»; «Chimpanzees picking answers randomly would get one third correct, on average.». 14 countries, 12 questions (SV on the studies index). No respondent count on the page.
- 2019 study, /ignorance/studies/global-misconception-study-2019/ — SP: «We asked a total of 15500 people in 31 different countries…»; «The surveys were conducted in October 2019 using Ipsos MORI survey platform.». 18 questions, 31 countries (SV on the index).
Role: the baseline is random guessing, not a control group; an audience-knowledge survey, not an evaluation of the display.

C6. MoMA COLLECTION RECORDS
MoMA's search pages are script-rendered: q=Wind+Map, q=Dear+Data and q=Lupi returned no results in static HTML. Records were found by web search and opened directly.
- Wind Map — EXISTS. https://www.moma.org/collection/works/163892. SV: «Fernanda Bertini Viégas, Martin Wattenberg» / «Wind Map» / 2012 / medium «Interactive software» / credit «Gift of the designers» / object number «1751.2012». Department Architecture and Design; "Not on view" (SP).
- Fragapane — THREE RECORDS EXIST (artist page /artists/136154-federica-fragapane lists 3).
 «Land Defenders (Data visualization for Atmos)», 2021, «Digital image», «Gift of the designer», «97.2023» — all SV — /works/447622.
 "Space Junk (Data visualization for BBC Science Focus)", 2019, Digital image, Gift of the designer, 96.2023 — SP — /works/447620.
 "Noise Pollution (Data visualization for La Lettura)", 2020, Digital image, Gift of the designer, 98.2023 — SP — /works/447623.
 Gallery label on these records (SP, returned independently on two record pages), attributed "Gallery label from Pirouette: Turning Points in Design, January 26, 2025–November 15, 2025": «Information design often goes beyond mere description to become an expressive interpretation of reality.»
- Dear Data — EXISTS, bought not gifted. /works/215813. SV: «Giorgia Lupi, Stefanie Posavec» / "Dear Data" / 2015 / medium «8 moleskin sketchbooks» (spelling as printed) / credit «Committee on Architecture and Design Funds» / object number «963.2016.1-8». Control «Gift of the designers» = NO. Weekly postcards are separate records, e.g. /works/216726, SV: «Dear Data: Week 1 (What's the Time / A Week of Clocks)», 2014, «Ink and pencil on paper», «Committee on Architecture and Design Funds», «962.2016.1a-b».
- Lupi — artist page /artists/67122-giorgia-lupi. SV: «53 works online». SP: "Italian, born 1981". Every Lupi work shown on the fetched page is a Dear Data item; I found NO Lupi record outside Dear Data, but the page paginates so I cannot exclude one.
(iv)/(v) None; a museum record is custody, not evaluation.

C7. MONA CHALABI
Pulitzer — https://www.pulitzer.org/winners/mona-chalabi-contributor-new-york-times — 2023, «Illustrated Reporting and Commentary», «Mona Chalabi, contributor, The New York Times» (SV). Citation, SV in two fragments: «For striking illustrations that combine statistical reporting with keen analysis to help readers understand the immense wealth and economic power of Amazon founder Jeff Bezos.» Winning work (SP): "9 Ways to Imagine Jeff Bezos' Wealth", April 7, 2022.
A published piece: NOT SEEN. NYT and Guardian are blocked; her own listing (https://monachalabi.com/projects/data-visualisation) returned filters but no items, with a meta description "Under construction" (SP). I therefore cannot say whether her pieces carry a source line. Homepage SV: «Mona Chalabi is an award-winning writer and illustrator who uses data as the foundation for her work.»
Her method in her own words — each is an interview quoting her:
- Dezeen, Jennifer Hahn, 16 Nov 2023 (https://www.dezeen.com/2023/11/16/mona-chalabi-pulitzer-prize-winner/). SV fragments: «Then I load the charts into Photoshop»; «to line up pixel-for-pixel with the computer-generated graphics»; «so they're as accurate as any computer graph that you're going to see anywhere else»; «I try to produce journalism where I'm explaining my methods to you.»; «Every single word that you add to an image reduces engagement». Control «I never use a computer to make my charts.» = NO.
- It's Nice That, Bryony Stone, 8 March 2018. SV: «computer-generated images overstate certainty»; «my hand-drawn graphics show the real margin of error»; «remind people that a human was responsible for the data gathering and analysis»; «It's transparent about its lack of certainty.»; «that's a mistaken understanding of objectivity».
- Nightingale (Medium), 1 Nov 2019. SV: «You'll never see decimal places on my illustrations»; «They're just trying to communicate the imprecision of the data that underlies it.»; «an overstatement of accuracy».
The word "source" appears in none of the three interviews (SP).
(v) No evaluation found.
Role: her stated method is a drawn layer registered to a computed chart — the removal-test structure, as testimony not observation.

C8. NEIL HALLORAN, "The Fallen of World War II" — fallen.io 302-redirects to https://www.neilfilms.com/ww2/
(i) First text elements (SP): "Neil Halloran" / "English" / "The Fallen of World War II" / "Interactive" / «Best experienced on a computer.» (SV) / "YouTube" / "Interactive Mode". A mode choice leads; no data input.
(iii) SV in two fragments: «The film follows a linear narration but pauses at key moments, letting viewers step into the charts and explore the numbers themselves.». Exploration is optional; the linear YouTube version is the stated fallback. Keyboard: n/d.
(ii) Sources are in prose below, not on the first screen. SV fragments: «Much of the underlying data draws from sources similar to those listed in the» [World War II Casualties Wikipedia article]; «Post-WWII statistics were sourced from the» [Uppsala Conflict Data Program (UCDP)]. SV: «Written, directed, coded, and narrated by Neil Halloran». Control «All figures have been independently audited» = NO. No sentence on estimates, uncertainty or disputed figures (SP).
(iv) None beyond the two source sentences. (v) No empirical evaluation found in two searches. A critical essay appears in search results only ("A Critical Inquiry on Data Visualization Based Interactive Documentary: 'The Fallen of World War II' as an example", on Academia/ResearchGate) — not fetched.

C9. RAWORTH'S DOUGHNUT
https://www.kateraworth.com/doughnut/ — SV: «The environmental ceiling consists of nine planetary boundaries, as set out by Rockstrom et al»; «The twelve dimensions of the social foundation are derived from internationally agreed minimum social standards»; «Between social and planetary boundaries lies an environmentally safe and socially just space in which humanity can thrive.». SP: «it acts as a compass for human progress this century.». The image is labelled as the 2017 version (SP).
https://doughnuteconomics.org/about-doughnut-economics — SV fragments: «At its conceptual core, the Doughnut consists of two concentric rings»; «a social foundation, to ensure that no one is left falling short on life's essentials»; «an ecological ceiling, to ensure that humanity does not destabilise the life-supporting systems»; «offers a visual monitor of progress».
Method paper: Fanning & Raworth, "Doughnut of social and planetary boundaries monitors a world out of balance", Nature 646, 47–56, 1 Oct 2025 — https://www.nature.com/articles/s41586-025-09385-1. SV «a revised set of 35 indicators». SP: 21 dimensions; 22 social and 13 ecological indicators; 2000–2022. SP: «The grey wedge indicates missing data.»
Critique as a display — the strongest one is the authors' own, in the Figure 1 caption. SV in fragments: «Values are proportional to the length of each wedge, which leads to a quadratic scaling of wedge area that may lead some readers to perceive small changes as more significant than they are.» and «bar-chart representation that avoids this quadratic scaling issue» (full second sentence SP: «To address this limitation, we provide Fig. 2 with a bar-chart representation that avoids this quadratic scaling issue.»). Control «Values are proportional to the area of each wedge» = NO.
External critique: "Deconstructing the Doughnut" (ScienceDirect S1877343524000381) is robots-blocked — title only. A Substack piece I fetched is not a display critique.
(v) No user evaluation found.

C10. "I WANT A BETTER CATASTROPHE" FLOWCHART — the claim mostly checks out, with three qualifications.
Paper: Jona Pomerance, Andrew Boyd, Marian Dörk, "Navigating and Narrating Interactive Flowcharts", Journal of Visualization and Interaction 1(1), published Apr 10, 2026 (SV metadata 2026-04-10), doi 10.54337/jovi.v1i1.8418, CC BY-SA 4.0 (SP) — https://journals.aau.dk/index.php/jovi/article/view/8418. Peer-reviewed, and the review is public: the article page carries "Round 1 Reviews", "Round 2 Reviews" and an «Open Practices Review» (SV label). It is listed on Dörk's publication page.
Display (from the paper; the live site flowchart.bettercatastrophe.com is script-rendered). SV: «visitors are greeted with an introductory panel suggesting two viewing options» / «listening to the narration or exploring the chart on their own»; «the case study flowchart contains 330 nodes and the narration spans over 52 minutes of audio». A mode choice leads. The paper has no sentence on transcript, captions, keyboard or mobile (SP).
Evaluation — observational field data, no control:
- Survey: SV «to which we received 177 responses». Self-selected visitors; six questions that appear open-ended; learning self-reported (SP).
- Logs: SV «29,112 such logs were collected» / «of which we will use 23,346 for further analysis» / «ignoring sessions without any interaction with the flowchart». A log is one page load with a random identifier (SP).
- Findings: SV «20% of all analyzed sessions reach the flowchart's final node». SV «a slight overall preference for narration (40%)», followed by both modes (34%) and exploring alone (26%) (SP). In the logs, by contrast, time went mostly to one mode: exploration 54%, narration 39% (SP), and SV «the 'balanced' use of both modes is noticeably rarer (7%)». SP: about 4.6% reach a narration time of at least 52:12; mean nodes visited 61, median 30; about 7% of respondents did not notice the audio narration.
- Authoring: SV «created 13 interactive flowchart projects» (one-week course, first-year design students).
- Limits: SV «the asynchronous and anonymous nature of these sources also limits the study of engagement». No comparison with the static flowchart (control strings for random assignment and a 48-person experiment = NO).
Qualifications on "released evaluation data":
1. Materials are on OSF (https://osf.io/5usfm; the "Research Materials" link redirects there). I could not open OSF.
2. Raw survey submissions are withheld. SP: «The complete submissions to the feedback survey (see subsection 5.1) are not shared publicly, as participants were not asked to consent to their responses being shared with others, and the data entered by some survey respondents contains personal information such as names, affiliations, and email addresses.»
3. The published Open Practices Review found the evaluation component unreachable at review time. SV strings «currently archiving», «license.txt», «survey data, log data»; SP sentence: «It looks like the Evaluation Materials component is unreachable and marked as 'currently archiving'.»
Also: Gold, Places, Spaces & Environment, IIB 2024 (SV title and category on the showcase page).

C11. INFORMATION IS BEAUTIFUL AWARDS
Status — https://datavisualizationsociety.org/iib-awards/ — SV: «The IIB Awards is currently on hiatus and will resume in 2027.»; «Submissions are now closed.». The latest completed cycle is the one the awards site calls "2024" (presented June 2025). There is no separate 2025 winners list; informationisbeautiful.net's call for the same cycle is titled "Enter the Information is Beautiful Awards 2025".
Judging criteria — https://www.datavisualizationsociety.org/iib-awards-faqs — eight, in page order (emphasis as printed; SV except where marked):
«Is the work impactful?»
«Is the work engaging?»
«Does the work display clarity of analysis, including clear guidance that makes the visual usable?»
«Is the work innovative and creative, celebrating novel formats and design approaches?»
«Is the work inclusive, including using inclusive language, and considering representations of equity appropriately?» (SP continuation: «Does the design single out or leave out data resulting in a viz that is not inclusive?»)
«Is the work accessible, including design decisions to support interaction from all users?» (SP continuation: «…Consider color contrast, color blindness, and alt text where applicable.…»)
«Is the work effective, achieving its goals and connecting an audience to the underlying data» (SP continuation: «– which may mean valuing simplicity over complexity?»)
«Is the work beautiful, celebrating aesthetic beauty and design broadly?»
There is NO criterion on accuracy, sourcing or data integrity (control «Is the work accurate, with sources cited and verified by judges?» = NO).
Process: SV «each submission was reviewed by at least three people»; SP «If a submission got at least two votes to be longlisted, then it made the longlist.»; SP «Both the works themselves (links and/or images) and your descriptions will be considered in the judging process.»
Winners post (https://www.informationisbeautifulawards.com/news/680-announcing-the-2024-winners), SV fragments: «Chosen by a panel of expert judges from nearly a thousand global submissions» … «their impact, innovation, and clarity».
Categories (nine; three sources agree bar punctuation): Arts, Entertainment & Culture; Business Analytics; Current Affairs & Politics; Humanitarian; Leisure, Games & Sport; People, Language & Identity; Places, Spaces & Environment; Science, Technology & Health; Unusual. Special awards (seven): Most Beautiful, Community Vote, Outstanding Studio, Impressive Individual, Rising Star, Test of Time, Impactful Community Leader.
Source-page discrepancies: the FAQ timeline says «ten open Awards categories» (SP) against nine listed; informationisbeautiful.net prints «Any work created between Sep 1st 2023 and Dec 31st 2023 is eligible.» (SV) while the awards site says to December 31, 2024 (SP).
Winners read for method: "This is a Teenager" (C1); "I Want a Better Catastrophe" (C10); ABC's burger piece, Silver, Business Analytics (C13); "Is the Love Song Dying?" (script-rendered). Showcase pages carry title, credits, a one-paragraph description and a link — no method or source field (SP).

C12. INCUMBENTS (display method only)
Thriving Places Index — thrivingplacesindex.org 302-redirects to https://www.centreforthrivingplaces.org/thriving-places-index/about-the-thriving-places-index/. Dashboard: https://www.centreforthrivingplaces.org/thriving-places-index/
(i) Heading «Thriving Places Dashboard» (SV), explanatory text, then an embedded Power BI iframe (app.powerbi.com) (SP). It is select-first inside the embed: SV «Select the name of the local authority using the drop-down in the top corner».
Scale statement, all SV: «< 3.5 = very low compared to the England average»; «3.5-4.5 = below the England average»; «4.5-5.5 = close to the England average»; «5.5-6.5 = above the England average»; «> 6.5 = very high compared to the England average»; «The Index scores are between 0 and 10.»; «A high score indicates better performance relative to other places.»
Colour statement, SV: «Colour coding is applied to make it easy to see how your place compares to other Local Authorities.» The page text does NOT say which colour means which band (SP; control «Green means good and red means bad.» = NO).
(ii) Methodology link «Full methodology (8mb PDF)» (SV) on the dashboard page and «Methodology (8mb PDF)» (SV) on the about page — https://www.centreforthrivingplaces.org/wp-content/uploads/2024/09/TPI-2024-Methodology-1.pdf. The PDF returned no machine-readable text, so I cannot quote it. No «Last updated:» label (NO). The edition appears only in prose (SP: «The 2024 TPI uses the same general methodology as previous editions from 2019 onwards.»); footer "© 2023 Centre for Thriving Places"; page metadata modified 2025-02-26 (SP).
(v) Not searched.
London Night Time Data Observatory — LIVE at https://data.london.gov.uk/night-time-observatory/
Landing, SV: «Welcome to the Night Time Data Observatory.»; «This webpage contains a range of research and data on London at night.»; fragment «over 30 data sources». «Last updated» = NO.
The landing shows NO dated contents: 0 dataset entries and 0 dataset dates. It links to four theme pages.
Counts on the theme pages (SP each): 6, 8, 5 and 5 entries = 24, of which about 19–20 carry a stamp (one page gave 5 of 6 on first count and 6 of 6 on recount). Stamps are relative, not dates ("Updated almost 6 years ago"); most read five to seven years, one "Updated over 2 years ago", one "Updated 3 months ago". No theme page has a page-level date. The landing's "over 30" exceeds the 24 I counted.
Creative Footprint: not researched, as instructed.

C13. NEWSROOM PIECES AND THE FT VISUAL VOCABULARY
ABC News (Australia), "What's driving up burger prices?" — https://www.abc.net.au/news/2024-08-05/cost-of-living-interest-rates-burgers/104156654 — Silver, Business Analytics, IIB 2024. Byline Julian Fell, Teresa Tan and Matt Liddy; posted 5 Aug 2024 (SP).
(i) Leads with a written sentence, then photography and charts; no input.
(ii) Sources are given ONCE, at the end, under «About the story» (SV heading); individual charts carry no source line (SP). SV: «Big Mac prices were sourced from The Economist's Big Mac Index data.»; «(The exact price at individual stores across Australia can vary.)»; «Reporting and development: Julian Fell»; «Design, photography and illustration: Teresa Tan». Control «All charts were independently verified by the ABS.» = NO.
(iii) n/d. (iv) Only the end note. (v) None found.
Reuters (Gold, Humanitarian) and the Washington Post (Silver, Current Affairs & Politics) are both blocked; not described.
FT Visual Vocabulary — ft.com/vocabulary blocked; read from https://raw.githubusercontent.com/Financial-Times/chart-doctor/main/visual-vocabulary/README.md. SV: «to assist designers and journalists to select the optimal symbology for data visualisations»; «by the Financial Times Visual Journalism Team»; «The FT Visual Vocabulary is at the core of a newsroom-wide training session aimed at improving chart literacy.»; «This learning resource is inspired by the Graphic Continuum by Jon Schwabish and Severino Ribecca.»; «Copyright © The Financial Times Limited, all rights reserved.». SP: «This is not an attempt to teach everyone how to make charts, but how to recognise the opportunities to use them effectively alongside words.». Category headings (SP): Deviation, Correlation, Ranking, Distribution, Change over Time, Part-to-whole, Magnitude, Spatial, Flow. Control «This vocabulary has been validated in a user study.» = NO. A training artefact, not evidence.

SUMMARY TABLE (Y / N / n/d = not determinable by text reader / blk = blocked)
| Entry | Leads with written sentence | Leads with an input | Source line on first screen | Hover required for any value | Publishes method | Publishes evaluation |
|---|---|---|---|---|---|---|
| C1 Teenager | Y | N (scroll) | N (inline, later) | n/d (click optional) | Partial (inline sources; no methods section found) | N |
| C1 Love song | n/d (script) | n/d | n/d | n/d | n/d | N |
| C2 OWID grapher | Y (title, subtitle, definition) | N | Y (under the title, with dates) | n/d | Y (same page) | N |
| C3 ONS ELS landing | Y (one sentence) | Y (search follows at once) | N (nothing shown yet) | n/a | Y (QMI link) | N |
| C3 Census landing / area page | Y / Y | Y (choose area) / N | N / Y (per chart) | — / N (CSV per chart; no hover instruction) | Y ("About the data") | N |
| C4 BBC | blk | blk | blk | blk | blk | N found |
| C5 Gapminder home / Upgrader | Y (a challenge) | N (quiz invited) | N | n/a | Partial (polling prose) | Own surveys (n=15,500 in 2019); not peer-reviewed |
| C5 Dollar Street | N (photos and income strip) | N | N | n/d | Y (about page) | N |
| C6 MoMA records | n/a | n/a | n/a | n/a | n/a | N |
| C7 Chalabi | not seen | not seen | not seen | n/a (static images) | Y in interviews only | N |
| C8 Halloran | N (title and mode choice) | N (mode choice) | N (sources in prose below) | n/d | Minimal (two sentences) | N found |
| C9 Doughnut | n/a (diagram) | N | n/a | N (static) | Y (Nature 2025) | No user study; authors' own perceptual caveat |
| C10 Flowchart | N (intro panel, two options) | N (mode choice) | n/d | n/d | Y (JoVI paper, template) | Y (survey n=177; 23,346 sessions; no control; raw survey withheld) |
| C11 IIB Awards | n/a | n/a | n/a | n/a | Y (eight criteria; none on accuracy) | N |
| C12 TPI dashboard | Y (explanatory text) | Y inside the embed (select) | N (sources in prose; no date label) | n/d (Power BI) | Y (image-only PDF) | N |
| C12 London NTDO landing | Y | N | N (no dates on landing) | n/a | Guidance linked | N |
| C13 ABC burger | Y | N | N (sources once, at end) | n/d | End note only | N |
| C13 FT Visual Vocabulary | n/a | n/a | n/a | n/a | It is the method artefact | N |

UNASKED THREADS
1. The field's main prize does not score truth. The eight IIB criteria include beauty, engagement, inclusion and accessibility but nothing on accuracy or sourcing, and the description text is judged alongside the work. The awards are on hiatus until 2027.
2. A removal test printed by the authors. Fanning & Raworth's 2025 caption admits the wedge area misleads and supplies a bar chart of the same values.
3. Chalabi's "pixel-for-pixel" statement: the drawn layer is registered to a computed chart. Paired with "computer-generated images overstate certainty", it is the clearest practitioner statement I found of expression carrying an evidential claim (uncertainty) rather than decorating one.
4. Stated versus logged behaviour diverge in the flowchart study: 40% say they prefer narration, but logs show 54% of sessions mostly exploring and only 7% balanced. Self-report about an expressive display is weak evidence.
5. JoVI publishes its review rounds and an Open Practices Review beside the article, and that review records that the evaluation materials could not be opened. "Released data" needs checking at the repository.
6. A MoMA gallery label (Pirouette, 2025) states institutionally that information design is «an expressive interpretation of reality» — on records whose medium is "Digital image", gifted by the designer.
7. Gomasta et al., "Investigating How Music Affects Persuasion, Engagement, and Emotion in Data Videos", arXiv 2601.17893, 25 Jan 2026 — ABSTRACT only. Preregistered; one data video shown with no music, default music and custom music. The abstract says default music made the video more persuasive, music did not increase engagement, and participants reported more intense emotions without music. No n in the abstract.
8. Morini et al., "Critical Interactivity: Exploration and Narration in Data Visualization", IEEE CG&A 2025, doi 10.1109/MCG.2025.3544684 — abstract (SP) frames interactivity as «the negotiation of authority and agency». Also from the same lab: Garretón et al., "Data Stories of Water", CGF/EuroVis 2023, an interpretive framework over 17 data stories (SP) — a content analysis, not a reader study.
Housekeeping: both incumbents have drifted. TPI's old domain now redirects and its dashboard is a Power BI iframe with an image-only methodology PDF; the Observatory's landing still calls itself "the first iteration".

LEFT OUT (and why)
- Everything on BBC, NYT, Guardian, Reuters, WaPo and ft.com: blocked. No BBC postcode interactive was audited.
- "Is the love song dying?" body; Gapminder Tools; the live flowchart: script-rendered or redirect loops, two attempts each.
- OSF contents, "Deconstructing the Doughnut", TPI methodology PDF text: unreadable.
- arXiv 2607.01593: rate-limited, not retried.
- Visual properties (colour, decoration, hover, keyboard): not observable.
- Creative Footprint: excluded by brief. No findings about any place or population are reported; one fetch returned a place statistic, which I discarded.
- Not done: the live Wind Map site, Posavec's artist page, the 2020/2023 Gapminder study pages, any search for evaluations of OWID, ONS, TPI or the FT vocabulary.

RICH REFERENCES
1. Fanning, A. L. & Raworth, K. (2025). Doughnut of social and planetary boundaries monitors a world out of balance. Nature 646, 47–56. https://www.nature.com/articles/s41586-025-09385-1 — the Figure 1 caption.
2. Pomerance, J., Boyd, A. & Dörk, M. (2026). Navigating and Narrating Interactive Flowcharts. Journal of Visualization and Interaction 1(1). https://doi.org/10.54337/jovi.v1i1.8418 — with its published reviews and Open Practices Review.
3. Data Visualization Society, Information Is Beautiful Awards FAQ — https://www.datavisualizationsociety.org/iib-awards-faqs. (Near miss: the Dezeen interview with Chalabi, 16 Nov 2023.)

SURPRISED
- The flowchart claim held: a 2026 peer-reviewed paper with a real field evaluation exists. But it has no control, and its open-practices reviewer could not open the evaluation data.
- The awards rubric has no accuracy criterion.
- The Doughnut's authors publish the perceptual defect of their own diagram in the caption.
- Chalabi's hand-drawn work is, by her account, traced onto computed charts.
- Neither Pudding piece's readable text contains a methods section or data link, though the commissioning rule demands "the receipts".
- OWID's «Learn more about this data» is not in the static page text; it lives, if anywhere, in the script-rendered chart.
- ONS Explore Local Statistics has left its beta host and opens with a sentence and a search box — no number or chart before input.
- MoMA records Dear Data as a purchase and Wind Map and the Fragapane works as designers' gifts.

WebSearch calls used: 11 of 30.


---

## Agent D

AGENT D REPORT — THE OFFICIAL AND NEWSROOM LINE ON DECORATION
All fetches made 6 October 2026 with WebFetch. Direct curl is blocked by the proxy, so STRING-VERIFIED means: the reader confirmed the exact string on a second, separate presence prompt, and every false control string I planted was rejected. SINGLE PASS means one non-leading extraction only (I note where two extractions agreed). WebSearch calls used: 14 of 30.

======================================================================
D1. ANALYSIS FUNCTION: INFOGRAPHICS, DECORATION, COLOUR
======================================================================

D1a. "Data visualisation: infographics" — official guidance (Government Analysis Function), published 17 August 2022; names WCAG 2.2.
URL: https://analysisfunction.civilservice.gov.uk/policy-store/infographics/ (the /data-visualisation-infographics/ URL is a 404)

STRING-VERIFIED:
- "Infographics use charts, timelines, maps or other visualisations to provide engaging explanations of data."
- "They should tell users the story without needing lots of extra information."
- "Infographics can be effective but can be difficult to do well."
- "For example a simple chart with some explanatory text could be clearer and more accessible for your users."
- "If you have lots of information to communicate, an infographic is probably not the best choice."
- "If the design is not done correctly, it could result in a poor or misleading infographic that could potentially damage the reputation of your department."
- "Infographics are normally produced as PDF or image files. Generally, these are not accessible."
- "The content within the infographic should also be available in an accessible format."
- "For infographics published on webpages, a good way to do this is to provide a plain text version on the same webpage."
- "provide a plain text alternative explaining all the information within the infographic"
- "Longer infographics can be used to share a large quantity of complex information in a visually appealing way."
- "You should ensure they do not become too cluttered and the content within them is concise."
- Bullet under "Use appropriate visualisations": "avoid visual clutter"
- Summary bullets: "Let the data lead the story"; "Keep the infographic as simple as possible"; "Test your infographic with users – do they understand the story without explanation?"

SINGLE PASS: "When used well, infographics: help to explain difficult messages / make stories more memorable / promote your work / are likely to be shared and re-used"; "High-quality infographics need a team of people to produce them, including analysts, designers and press office colleagues."; summary bullets "Avoid visual clutter", "Provide a plain text version of the content", "Publish as an SVG format".

NEGATIVE FINDING (checked explicitly): the words "pictogram", "icon", "3D" and "decorative" do not appear anywhere on the infographics page.
Role: the official infographic rule is a removal test in miniature — the content must also exist as plain text, and the story must be understood "without explanation".

D1b. "Data visualisation: charts" — official guidance, published 19 May 2022, no last-updated date shown.
URL: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/

- Under "Formatting charts", sub-heading "Keep it simple", then "Avoid:" with seven bullets: "shaded backgrounds" / "unnecessary borders" / "boxes around legends and other content" / "patterns, textures and shadows" / "3D shapes" / "unnecessary data markers on line charts" / "thick or dark gridlines". The bullets "3D shapes" and "patterns, textures and shadows" are STRING-VERIFIED; the whole list came out identically on two passes.
- STRING-VERIFIED: "In this situation the image of the chart should be marked as decorative and therefore hidden from screen reader software." Surrounding paragraph (SINGLE PASS): "If you use a text description, our advice is that this should live in the body of the page, directly underneath the chart. … This is usually done by leaving the 'alt attribute' blank but sometimes there will be a box to tick."
- Titles (SINGLE PASS, two passes agree): "All charts need at least one title, but it is considered best practice to give them two." / "The headline title should communicate the headline message of the chart." / "The statistical subtitle should say what the data is, the geography the data relates to and the time period shown."
- Axis (SINGLE PASS): "For example, breaking the numerical axis on a bar chart is problematic and highly controversial." / "In bar charts you perceive the bars being proportional to each other – breaking the numerical axis distorts these relative proportions." / "If starting the numerical axis at zero stops you from telling the story clearly, consider an alternative chart, such as a Cleveland dot plot."
- NEGATIVE FINDINGS (checked): no "pictogram", no "icon", no "chart junk"/"chartjunk". "cluttered" appears only about more than four categories or lines. The introduction says the guidance "does not cover interactive visualisations" (SINGLE PASS).

D1c. "Charts: a checklist" — official, published 2 May 2023.
URL: https://analysisfunction.civilservice.gov.uk/policy-store/charts-a-checklist/
STRING-VERIFIED:
- Item "Remove chart clutter": "Avoid shaded backgrounds, unnecessary borders, patterns, textures, shadows, 3D shapes, unnecessary data markers and thick or dark gridlines."
- Item "Mark images of charts as decorative": "Marking images of charts as decorative means they have nothing in the alt attribute. This means a screen reader user will skip directly from the chart title to the text alternative (which should be directly underneath the chart)."
- "If a point is followed by (E) it means we have deemed it essential to meet the Web Content Accessibility Guidelines 2.2." ("Remove chart clutter" carries no (E); it is advice, not a legal minimum.)
- Item "Do not break the numerical axis – it should always start at zero": "Even if a break in the axis is clearly signposted, the relative size of bars is still displayed very strongly on bar charts."
Role: the official list of forbidden decoration. Note the odd usage: here "decorative" is a technical status given to the chart image itself once its text alternative sits beside it.

D1d. "Data visualisation: colours in charts" — official, published 23 November 2021, last updated 12 February 2026.
URL: https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/

STRING-VERIFIED:
- "Limiting the number of colours you use in a chart makes them stand out."
- "You should only use different colours when they show helpful differences in the data."
- "When you have categorical data that cannot be grouped, use a single colour."
- "If your colours suggest meanings that are not there the user will waste time and effort trying to understand them." (two non-leading passes give first word "If"; one YES/NO pass echoed "When" — treat the first word as probable, not certain)
- "Never use an image as a background."
- "We recommend using white as a background colour."
- "All our palettes are designed to be used with a white background."
- "Some users may find a white background difficult to look at because of glare or the high contrast of colours against it."
- "Doing it this way means you are using colour for emphasis." (RAG section)
- Categorical palette, in order: Dark blue #12436D, Turquoise #28A197, Dark pink #801650, Orange #F46A25, Dark grey #3D3D3D, Light purple #A285D1.

SINGLE PASS:
- "Think carefully before you introduce additional colours into a graph." / "Do you really need the colours?" / "Do they make your message clearer?"
- "Use a plain background", full run: "Never use an image as a background." / "This can make charts difficult to see." / "Charts that use an image as a background are also likely to fail the accessibility legislation." / "We recommend using white as a background colour." / "All our suggested colour palettes are based on this." / "There are some accessibility issues with using white as a background colour." / [glare sentence] / "On the other hand, other users prefer a white background because they need the high level of contrast it provides." / "A perfect solution would be to have data visualisations that can be fully customised to meet specific user needs." / "As this is not possible at the moment we recommend a white background because it provides a helpful 'anchor' in general."
- "Consider colour associations": "People link certain colours to certain things." … "Colours can also have cultural associations." / "We may react to these consciously or unconsciously." / "These associations vary across countries and groups." / "Consider whether your colours are appropriate."
- "Ideally, use just the first four": "We recommend a limit of four categories as best practice for basic data visualisations." / "The dark grey and light purple have been added to this palette due to demand for extra colours." / "But these should only be used when essential."
- "Focus charts are charts which use colour to highlight specific elements to help users understand the information." Focus palette: Dark blue #12436D, Grey #BFBFBF.
- Sequential palette: #092135, #12436D, #2073BC, #6BACE6, #ADD1F1, #F2F2F2; "A sequential colour palette should only be used when absolutely necessary for the type of data you are presenting and there are no alternate methods."
- Branded palettes: "If you need to use a certain branded colour palette but you do not think it meets the accessibility legislation, there are things you can do to help make data visualisations as accessible as possible:" then bullets beginning "Wherever possible ensure colours presented next to each other have the required amount of contrast" / "Avoid colour being the only way to communicate a message – for example, label lines or sections directly instead of using legends" / "Make sure to provide text alternatives to the data visualisations…"

NEGATIVE FINDING (checked): no sentence on the colours page contains "decorat". The rule on decorative colour is implicit in "only use different colours when they show helpful differences in the data".
Role: colour is licensed for meaning and emphasis only; background is plain white; brand palettes are tolerated subject to the same tests.

D1e. "Making analytical publications accessible" — official, published 29 October 2020.
URL: https://analysisfunction.civilservice.gov.uk/policy-store/making-analytical-publications-accessible/
- STRING-VERIFIED, under the sub-heading "Simplify" (Word/Excel documents): "Do not use lots of colourful diagrams and logos unless they are strictly necessary." Preceded by "Strip out any content that is not necessary." (SINGLE PASS).
- SINGLE PASS: "Images in Word documents should have appropriate alt text in the properties of the image, unless they are only decorative, in which case they should have two double quotation marks ("")." / "See our guidance on infographics and our tips for dashboards for general advice."

D1f. Pictograms or icons of people: no Analysis Function rule exists on any of the five pages I checked (charts, checklist, colours, infographics, accessibility). The e-learning landing page shows only module titles. Nearest official rules are in D2 (GOV.UK) and D4 (FT, GLA).

======================================================================
D2. GOV.UK, NHS AND ONS ON IMAGES, DECORATION, ICONS
======================================================================

D2a. GOV.UK content and publishing guidance, "Images" — official standard; no date displayed.
URL: https://guidance.publishing.service.gov.uk/formatting-content/images/ (redirect target of gov.uk/guidance/content-design/image-copyright-standards-for-gov-uk)
STRING-VERIFIED:
- "Decorative images are generic images which do not give any additional information to the content."
- "For example, an image of laptops in a blog post about technology, or featured content on organisation pages."
- "Informative images can help users understand the written text in a different way."
- "do not use images alone to provide information - it will exclude users who cannot see or access the image"
- "do not use the alt text field" (a bullet under "For both types of image")
- "An infographic is an image which usually displays data, graphs, charts or text to explain a complex process or overview of a subject."
- "Infographics can be hard to make accessible if they're too complicated."
- "If you do use an infographic you should provide a plain text version of the content."
- "All charts should have two titles - a headline title and a statistical title." / "The headline title of the chart should summarise the main message of the chart."
NEGATIVE: "Do not use decorative images." does NOT appear. GOV.UK content guidance defines decorative images and permits them; it does not ban them. Section heading: "Informative or decorative images".

D2b. GOV.UK Design System, "Images" — official design-system rule; page notes a March 2023 update.
URL: https://design-system.service.gov.uk/styles/images/
STRING-VERIFIED:
- "Avoid using images for unnecessary decoration." / "Only use images if there's a real user need."
- "However, images should only be visual aids – written content must contain all the information the user needs to complete the service."
- "Do not use photography to represent abstract concepts, such as to convey an impression or emotion to the user."
- "Use as few visual elements as possible to communicate your message."
- "Use flat blocks of colour. Avoid using shadows or gradients, except when needed to show a distinctive feature of an object or to communicate layering or depth."
- "Avoid depicting people in illustrations." / "If you need to show people, think carefully about how you represent the people that use your service" [– do not only show one kind of person.] / "only depicting people of a particular age, gender or ethnicity can exclude people and reinforce negative stereotypes."
- "Avoid using icons in most cases." / "People can understand a single icon to mean different things, so they can be confusing."
- "However, make sure the image actually benefits the user and is not just for decoration."
- "Remember to avoid using images for unnecessary decoration, even if it's an 'image of text'."
- "All images should include the alt attribute, even if it's left empty without alt text (alt="")"
- Empty-alt case: "a decorative image that does not include important content"
The page does not mention dark mode or dark backgrounds (checked).
Role: the strongest official sentence against affective imagery ("an impression or emotion") — written for transactional services, not for publications.

D2c. NHS digital service manual.
- Icons, updated June 2026. URL: https://service-manual.nhs.uk/design-system/styles/icons
 STRING-VERIFIED: "Use icons sparingly, and not for decoration." / "Use this small set of icons that we know our users need and understand to help them identify and navigate content more quickly." / "We tested them in context – not on their own, but in components on a full page."
 NEGATIVE: "Do not use icons alone." does NOT appear.
- Images, updated January 2025. URL: https://service-manual.nhs.uk/design-system/components/images
 STRING-VERIFIED: "Use images only if there is a real user need. Avoid unnecessary decoration." / "But having unnecessary or decorative images can frustrate users, especially on information pages or transactional journeys."
 SINGLE PASS: "Images help them orient themselves and they separate out the content." / "We've also found users with some access needs (such as dyslexia) navigate health information through images."

D2d. ONS service manual.
- Data visualisation principles. URL: https://service-manual.ons.gov.uk/data-visualisation/guidance/principles (guidance added November 2023 per the "About" page)
 STRING-VERIFIED:
 "Avoid using charts or maps to show information that is unimportant, or supplementary to the main findings."
 "Do not use charts to introduce concepts or data that are not discussed in the main text of your release."
 "Aim to make your chart as simple as possible while still giving users the necessary context to understand the data."
 "Only include the data that are needed to show the important trends clearly and accurately."
 "Data visualisations should not be used to share your entire dataset."
 "Data visualisations often attract users' attention."
 "Plotting values on a chart alone does not guarantee the trends will be clear to the user."
 "If the trend you are showing is not immediately clear to the user, reconsider your chart choices."
 Aims list: "accessible to all users / accurate / intuitive to use / engaging / simple and clear to understand / consistent" — note that "engaging" is an official aim.
- Chart elements (build specification). URL: https://service-manual.ons.gov.uk/data-visualisation/build-specifications/chart-elements
 STRING-VERIFIED: "Do not add any other chart decoration, such as borders or backgrounds, as these distract users from the data and message."
 SINGLE PASS (preceding sentence): "It is important to stay consistent with these styles to maximise legibility of the charts and brand recognition."
- Using colours in charts. URL: https://service-manual.ons.gov.uk/data-visualisation/colours/using-colours-in-charts
 STRING-VERIFIED: "using colour in a way that is intuitive and helps to convey the meaning of the data"
 SINGLE PASS: "At the Office for National Statistics (ONS), we use Ocean blue when only one colour is needed." / "For charts with a single main colour, use a different colour to highlight a category or interesting data point." / "Always use five colours or fewer in your data visualisations to help users perceive the differences between colours" / "In charts created in other tools, use grey to show less important categories and use Ocean blue or other colours from our standard category colour palette to highlight important data"
- Interactive charts and animations. URL: https://service-manual.ons.gov.uk/data-visualisation/guidance/interactive-charts-and-animations
 STRING-VERIFIED: "never make an animation the only way to get the information" / "make sure there is a way for the user to control the animation, for example, to pause or reset and navigate through the frames" / "keep the animated elements to a minimum, as using too many can be distracting and make it difficult to understand what the chart is showing" / "Only consider using an interactive chart where the most important information for the user cannot be clearly shown through a non-interactive chart."
- Dashboards. URL: https://service-manual.ons.gov.uk/data-visualisation/guidance/dashboards
 STRING-VERIFIED: "A dashboard is a visual tool that shows different views of data to provide an overview of a specific topic." / "Only use a dashboard if you have clear justification for doing so." / "are not well-suited to highlighting important findings; they put the burden of interpreting and understanding data onto the user" / "are difficult to make accessible and responsive for different devices" / "use written content to provide context and use accompanying articles to highlight current trends and priorities"
- Design System "Image" component. URL: https://service-manual.ons.gov.uk/design-system/components/image
 STRING-VERIFIED: "If the image is decorative and does not convey important information, do not add an alt tag." / "This will then be hidden from screen reader users."
- Brand guidelines, Iconography. URL: https://service-manual.ons.gov.uk/brand-guidelines/iconography
 STRING-VERIFIED: "Icons should be used to support content, not replace it." / "They should not be used in isolation, as the meaning can be interpreted in different ways by different people." / listed use: "increase the impact of our messaging on social media" / "Our icons use simple geometric shapes and rounded corners to convey trustworthiness and professionalism, but with a friendly feel."
Role: ONS states both sides in one manual — charts carry no decoration; icons and brand carry affect ("friendly", "impact") but never information on their own.

======================================================================
D3. WCAG 2.2 AUDIO CRITERIA AND THE DEFINITION OF DECORATION (standard; W3C Understanding pages)
======================================================================
All normative sentences STRING-VERIFIED unless marked.

1.2.1 Audio-only and Video-only (Prerecorded), Level A
URL: https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html
- "For prerecorded audio-only and prerecorded video-only media, the following are true, except when the audio or video is a media alternative for text and is clearly labeled as such:"
- Prerecorded Audio-only: "An alternative for time-based media is provided that presents equivalent information for prerecorded audio-only content."
- Prerecorded Video-only (SINGLE PASS): "Either an alternative for time-based media or an audio track is provided that presents equivalent information for prerecorded video-only content."
- Definition, "alternative for time-based media": "document including correctly sequenced text descriptions of time-based visual and auditory information and providing a means for achieving the outcomes of any time-based interaction"
- Definition, "audio-only": "a time-based presentation that contains only audio (no video and no interaction)"
- Intent: "The intent of this success criterion is to make information conveyed by prerecorded audio-only and prerecorded video-only content available to all users." / "Alternatives for time-based media that are text based make information accessible because text can be rendered through any sensory modality (for example, visual, auditory or tactile) to match the needs of the user."
- Benefit (SINGLE PASS): "People who are deaf, are hard of hearing, or who are having trouble understanding audio information for any reason can read the text presentation."
- The word "transcript" appears only in examples (SINGLE PASS), e.g. "The link to a text transcript is provided immediately after the link to the audio clip." The normative requirement is the "alternative for time-based media"; the page states no exemption for music (control rejected).

1.2.2 Captions (Prerecorded), Level A
URL: https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html
- "Captions are provided for all prerecorded audio content in synchronized media, except when the media is a media alternative for text and is clearly labeled as such."
- Intent: "The intent of this success criterion is to enable people who are deaf or hard of hearing to watch synchronized media presentations." / "Captions not only include dialogue, but identify who is speaking and include non-speech information conveyed through sound, including meaningful sound effects."
- Definition of captions (SINGLE PASS): "synchronized visual and/or text alternative for both speech and non-speech audio information needed to understand the media content"; Note 1: "Captions convey not only spoken dialogue but also equivalents for non-dialogue audio information, including sound effects, music, laughter, speaker identification and location."

1.2.3 Audio Description or Media Alternative (Prerecorded), Level A
URL: https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html
- "An alternative for time-based media or audio description of the prerecorded video content is provided for synchronized media, except when the media is a media alternative for text and is clearly labeled as such."
- Intent: "The intent of this success criterion is to provide people who are blind or visually impaired access to the visual information in a synchronized media presentation" [in the same human language as the video or page on which it appears.]

1.2.5 Audio Description (Prerecorded), Level AA
URL: https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html
- "Audio description is provided for all prerecorded video content in synchronized media."
- Intent: "During existing pauses in dialogue, audio description provides information about actions, characters, scene changes, and on-screen text that are important and are not described or spoken in the main sound track."

1.4.2 Audio Control, Level A
URL: https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html
- "If any audio on a web page plays automatically for more than 3 seconds, either a mechanism is available to pause or stop the audio, or a mechanism is available to control audio volume independently from the overall system volume level."
- Note (SINGLE PASS, two passes agree): "Since any content that does not meet this success criterion can interfere with a user's ability to use the whole page, all content on the web page (whether or not it is used to meet other success criteria) must meet this success criterion."
- Intent: "Individuals who use screen reading software can find it hard to hear the speech output if there is other audio playing at the same time." / "Therefore, it is important that the user be able to turn off the background sound."
- SINGLE PASS: "Therefore, we discourage the practice of automatically starting sounds (especially if they last more than 3 seconds), and encourage that the sound be started by an action initiated by the user after they reach the page, rather than requiring that the sound be stopped by an action of the user after they land on the page."

Definition of decoration and 1.1.1's clause
URL: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html
- 1.1.1 clause: "If non-text content is pure decoration, is used only for visual formatting, or is not presented to users, then it is implemented in a way that it can be ignored by assistive technology."
- "pure decoration": "serving only an aesthetic purpose, providing no information, and having no functionality"
- Note: "Text is only purely decorative if the words can be rearranged or substituted without changing their purpose."
- Example: "The cover page of a dictionary has random words in very light text in the background."
Role: a dashboard about sound owes a deaf reader a text document equivalent to every audio-only item (A), captions that include non-speech sound where audio accompanies video (A), and no audio that starts by itself for more than three seconds without a stop control (A). WCAG's own decoration test is itself a removal test: decoration is what can be "rearranged or substituted without changing" purpose.

======================================================================
D4. NEWSROOM AND PLATFORM STYLE
======================================================================

(a) FT Visual Vocabulary — practitioner framework; README (github tree URL is robots-disallowed; raw file reachable).
URL: https://raw.githubusercontent.com/Financial-Times/chart-doctor/main/visual-vocabulary/README.md
STRING-VERIFIED:
- Purpose: "to assist designers and journalists to select the optimal symbology for data visualisations"
- "The FT Visual Vocabulary is at the core of a newsroom-wide training session aimed at improving chart literacy."
- "This learning resource is inspired by the Graphic Continuum by Jon Schwabish and Severino Ribecca."
- "This is not an attempt to teach everyone how to make charts, but how to recognise the opportunities to use them effectively alongside words."
- Under Magnitude: "Isotype (pictogram): Excellent solution in some instances – use only with whole numbers (do not slice off an arm to represent a decimal)."
- Spatial: "Used only when precise locations or geographical patterns in data are more important to the reader than anything else."
The README has no rule on decoration or chartjunk (control rejected). The FT's line is drawn through form selection, plus one explicit licence for pictograms.

(b) Datawrapper — platform/practitioner blog (Lisa Charlotte Muth).
- "Emphasize what you want readers to see with color", July 24th, 2023. URL: https://www.datawrapper.de/blog/emphasize-with-color-in-data-visualizations
 STRING-VERIFIED: "Color is our most powerful tool to control where the reader looks." / "If a category is as important as other, colorful ones, don't make it gray."
 SINGLE PASS: "Another hue will communicate 'this is a separate category,' not 'these are less important.'" (The heading "Make everything else gray" failed verification — do not quote it.)
- "What to consider when choosing colors for data visualization", May 29th, 2018. URL: https://www.datawrapper.de/blog/colors
 STRING-VERIFIED with full wording from the verifier: "Using grey for less important elements in your chart makes your highlight colors (which should be reserved for your most important data points) stick out even more." / "Grey is also helpful for general context data, less important annotations, to show what's unselected by the user, or to calm down the overall visual impression of your charts."
- No Datawrapper article specifically on chartjunk, decoration, or icons/images in charts was found in the "Data vis do's & don'ts" index (32 titles) or by site search; datawrapper.de/blog/chartjunk is a 404. Its Tufte book-club post (July 18th, 2018) takes no position (SINGLE PASS).

(c) The Economist, Sarah Leo, "Mistakes, we've drawn a few", March 27, 2019 — a newsroom's own boundary statement.
URL: https://medium.com/the-economist/mistakes-weve-drawn-a-few-8cdd8a42d368 (medium.economist.com and archive.org are blocked)
STRING-VERIFIED:
- "I grouped our crimes against data visualisation into three categories: charts that are (1) misleading, (2) confusing and (3) failing to make a point."
- "At The Economist, we take data visualisation seriously." / "Every week we publish around 40 charts across print, the website and our apps."
- "Best practices in data visualisation are evolving fast: what may be acceptable today can be frowned upon tomorrow."
SINGLE PASS (two passes agree): section headings "Misleading charts" / "Confusing charts" / "Charts that conceal their point". The third heading differs from the sentence's third category.
SINGLE PASS: "Mistake:" headings — "Truncating the scale"; "Forcing a relationship by cherry-picking scales"; "Choosing the wrong visualisation method"; "Taking the "mind-stretch" a little too far"; "Confusing use of colour"; "Including too much detail"; "Lots of data, not enough space". Also: "The visualiser (me!) ignored the fact that a change of colour often implies a categorical change."
No category of mistake is "decoration". Nieman Lab (April 9, 2019) reproduces the category sentence with US spelling.

(d) Reuters Graphics / NYT: no public style guidance found. reuters-graphics.github.io/style-guide/ is a 404; one search found no NYT guide. The Economist's chart style guide PDF (design-system.economist.com) is blocked. BBC R cookbook (https://bbc.github.io/rcookbook/), SINGLE PASS only: "finalise_plot(), the second function of the bbplot package, will left-align the title, subtitle and add the footer with a source and an image in the bottom right corner of your plot." — a tooling fact, not a rule on decoration.

(f) Urban Institute Data Visualization Style Guide — practitioner house style; page shows "LAST UPDATED ON AUGUST 27, 2025" (SINGLE PASS).
URL: https://urbaninstitute.github.io/graphics-styleguide/
STRING-VERIFIED:
- "Stay away from 3-D." / "There is no need to add a superfluous third dimension to your chart, particularly when you don't have a third value." / "The 3-D effect available in many software tools actually distorts the data values because the effect is not actually 3-D but rather a perspective rendering of 3-D."
- "Keep it simple. Don't try to stuff every data value into a single graph."
- "Urban charts posted on the web also include an Urban tagline/logo in the lower-right corner of the figure so that when others copy and paste our charts, Urban is identified as the source."
NEGATIVE: "chartjunk" does not appear; nothing on pictograms. (The reader saw the first 100,000 of 101,709 characters.)

(g) ProPublica Data Style Guide (Scott Klein) — newsroom rule.
URL: https://raw.githubusercontent.com/propublica/guides/master/news-apps.md
STRING-VERIFIED: "Avoid 3-D charts at all costs." / "Humans have enough problem perceiving area accurately." / "Avoid pie charts, with one exception: Use them to show the relationship between part and whole."
SINGLE PASS: "Asking them to perceive 3-D volume makes matters worse." / "Avoid donut charts at all costs." / "Don't show interpolated or predicted data without saying you're doing so."
Sunlight Foundation: the PDF guide was unreachable in two attempts (binary). Blog post by Amy Cesal, March 12, 2014, URL: https://sunlightfoundation.com/2014/03/12/datavizguide/ — STRING-VERIFIED: "Charts that are well designed and professional are taken more seriously because it conveys an attention to detail that implies that similar care was taken with the data." / "In our guide I've included not just where to put the logo (top right across from the title), but how far apart things should be spaced"

Role of D4: practising newsrooms forbid 3-D and distortion by name; they do not forbid decoration by name; the FT explicitly permits pictograms under a truth condition (whole units).

======================================================================
D5. TUFTE'S RULES AS PRINTED
======================================================================
No scan of the books was reachable; everything below is a secondary quotation, verified only at the secondary source. Treat as "as quoted by".

- Chartjunk passage (VDQI 1983), as quoted on Wikipedia "Chartjunk" (no page number given). URL: https://en.wikipedia.org/wiki/Chartjunk. STRING-VERIFIED at Wikipedia: "The interior decoration of graphics generates a lot of ink that does not tell the viewer anything new." / "The purpose of decoration varies—to make the graphic appear more scientific and precise, to enliven the display, to give the designer an opportunity to exercise artistic skills." / "Regardless of its cause, it is all non-data-ink or redundant data-ink, and it is often chartjunk."
- Data-ink (VDQI 1983), as quoted on InfoVis-Wiki. URL: https://infovis-wiki.net/wiki/Data-Ink_Ratio. STRING-VERIFIED at the wiki: "A large share of ink on a graphic should present data-information, the ink changing as the data change." / "Data-ink is the non-erasable core of a graphic, the non-redundant ink arranged in response to variation in the numbers represented." / "Above all else show the data"
- Data-ink ratio definition and "erase" rules: NOT quotable as printed. John Stasko's Georgia Tech slides (https://faculty.cc.gatech.edu/~stasko/7450/11s/Talks/tufte.pdf, SINGLE PASS) give "Data ink ratio = Data ink / Total ink used in graphic = proportion of graphic's ink devoted to the non-redundant display of data-information" and "Maximize the data-ink ratio" / "Erase non-data-ink" / "Erase redundant data-ink" / "Revise and edit" — all without "within reason". No reachable source carries "Erase non-data-ink, within reason" verbatim. The EU guide (below) only paraphrases: "According to Tufte, non-data-ink is chart junk and should be removed, within reason." Skip, or quote from the physical book.
- Lie Factor: formula as given on InfoVis-Wiki and Stasko's slides (SINGLE PASS each): "Lie Factor = (size of effect shown in graphic) / (size of effect in data)". The accompanying principle is quoted two different ways by two secondary sources ("…directly proportional to the quantities represented" on InfoVis-Wiki; "…directly proportional to the numerical quantities represented" on guypursey.com). Do not quote without the book.
- Smallest effective difference (Visual Explanations 1997), as quoted by Dan Brown, Boxes and Arrows, November 24, 2002. URL: https://boxesandarrows.com/three-lessons-from-tufte-special-deliverable-6/. STRING-VERIFIED at that source with its citations: "Make all visual distinctions as subtle as possible, but still clear and effective" (Explanations 73); "Muting … secondary elements will often reduce visual clutter – and thus help to clarify the primary information" (Explanations 74).
- Tufte in his own words, on his own site (forum post dated March 6, 2006). URL: https://www.edwardtufte.com/notebook/analytical-design-and-human-factors/. STRING-VERIFIED: "If possible, design architectures should be spare, straightforward, conventional, and self-effacing; AND the evidence presented should be rich, complex, multivariate, causal." Following sentences (SINGLE PASS): "The idea is to maximize the viewer's content reasoning time, and to minimize the design figuring out time and to reduce impediments to content reasoning." / "This theme runs through the first 3 books, with increasing elaborations over time: the 'data-ink ratio' in The Visual Display of Quantitative Information (1983, 2001); micro/macro designs, and layering and separation in Envisioning Information (1990); and the 'smallest effective difference' in Visual Explanations (1997)."
- The "duck" sentence, as quoted in the EU data.europa.eu guide (see Unasked 4). STRING-VERIFIED at that source in two fragments: "When a graphic is taken over by decorative forms or computer debris, when the data measures and structures become Design Elements, when the overall design purveys Graphical Style rather than quantitative information, then that graphic may be called a duck in honor of the duck-form store" [, "Big Duck"]. Also: "graphics do not become attractive and interesting through the addition of ornamental hatching and false perspective to a few bars".
Few: skipped as instructed; no one-line boundary statement was sought.
Role: the 2006 sentence is Tufte's own two-layer statement — self-effacing design, rich evidence — and the only one I could verify in his own hand.

======================================================================
D6. DESIGN SYSTEMS' TIER LANGUAGE: "DECORATIVE" VERSUS "INFORMATIVE"
======================================================================
Yes: the two-tier distinction is a named rule category in several public systems.

- W3C WAI Images Tutorial (the root precedent). Categories, in order: Informative images / Decorative images / Functional images / Images of text / Complex images / Groups of images / Image maps. URL: https://www.w3.org/WAI/tutorials/images/ (shows "Updated: 08 April 2026", SINGLE PASS) and https://www.w3.org/WAI/tutorials/images/decorative/ (shows "Updated: 27 July 2019", SINGLE PASS).
 STRING-VERIFIED: "Decorative images don't add information to the content of a page." / "For example, the information provided by the image might already be given using adjacent text, or the image might be included to make the website more visually attractive." / "Whether to treat an image as decorative or informative is a judgment that only the author can make, based on the reason for including the image on the page." / bullet "Illustrative of adjacent text but not contributing information ("eye-candy");" / Informative: "Images that graphically represent concepts and information, typically pictures, photos, and illustrations." / Decorative: "Provide a null text alternative (alt="") when the only purpose of an image is to add visual decoration to the page, rather than to convey information that is important to understanding the page." / Complex: "such as graphs and diagrams: To convey data or detailed information, provide a complete text equivalent of the data or information provided in the image as the text alternative."
- GOV.UK content guidance: section headed "Informative or decorative images", with the definition quoted in D2a.
- GOV.UK Design System: empty alt for "a decorative image that does not include important content" (D2b).
- ONS Design System: "If the image is decorative and does not convey important information, do not add an alt tag." (D2d).
- NHS: "unnecessary or decorative images" (D2c).
- Material Design (archived version 1; Material 2 and 3 pages need JavaScript and were unreachable in two attempts). URL: https://m1.material.io/usability/accessibility.html. STRING-VERIFIED: heading "Logos and decorative elements"; "While decorative elements (such as logos or illustrations) don't have to meet contrast ratios, they should be distinguishable if they possess important functionality." / "Decorative logos that are distinguishable don't have to meet contrast ratios." SINGLE PASS, Sound section: "Give visual alternatives to sound, and vice versa."
- Carbon (IBM): no "decorative" wording found on the icon usage or accessibility pages (SINGLE PASS). Carbon instead tiers "productive" versus "expressive" — see Unasked 7.
- USWDS icon component: no decorative/informative sentence found (SINGLE PASS). Polaris: the URL now redirects to shopify.dev; not pursued.
Role: a "Decorative tier" has direct public precedent, with a consistent meaning — carries no information, may be ignored by assistive technology, and (W3C) is the author's judgment to make.

======================================================================
D7. OFFICIAL STATISTICS: BRANDING VERSUS CHART CLARITY
======================================================================
- Logos: Analysis Function, "Do not use lots of colourful diagrams and logos unless they are strictly necessary." (D1e, STRING-VERIFIED). No AF or ONS rule on a logo inside a chart was found. ONS logo page (https://service-manual.ons.gov.uk/brand-guidelines/logo, SINGLE PASS) covers the logo only; its "do not" list includes "apply any effects, such as a stroke or shadow". Contrast Urban Institute, where the logo on a chart is a provenance device (D4f).
- Chart titles as headlines: AF and GOV.UK both require a headline title plus a statistical title (D1b, D2a). ONS chart text (https://service-manual.ons.gov.uk/data-visualisation/guidance/chart-text), STRING-VERIFIED: "The chart title should describe the main trend you want the chart to show to the user." / "Your chart title should complement but not repeat your section heading." SINGLE PASS: "All charts must have a title that is:" front-loaded / in the active voice / in sentence case / as concise as possible / 15 words or fewer; and "For some interactive tools, it may not be possible or useful to provide a title that describes a trend. In this case, give the chart a title that prompts the user on how to use the tool." A control string requiring neutral, descriptive-only titles was rejected: official UK guidance requires the message in the title.
- House palettes used for meaning: AF branded-palette passage (D1d). ONS brand colours page (https://service-manual.ons.gov.uk/brand-guidelines/colours, SINGLE PASS): "Our core brand colours should be used across all products to build familiarity and recognition."; the page directs data visualisations to the separate chart-colour guidance (reader paraphrase, not quotable); "This palette is for people illustrations only and should not be used in other contexts."
- "Images that mislead": no page titled "Communicating statistics" with such a section was found. The nearest is Analysis Function, "Advice for policy professionals using statistics and analysis", published 3 February 2022, section "10. Presentation really matters". URL: https://analysisfunction.civilservice.gov.uk/policy-store/advice-for-policy-professionals-using-statistics/
 STRING-VERIFIED: "Poorly chosen presentation methods can hide things or mislead and confuse people." / "Good statistical graphics, based on accurate statistics, help you to tell the stories in the numbers." / "Statistical graphics in government are increasingly self-contained." / "In 2014, the Department for Work and Pensions press office published an infographic with a press release." / "It is much larger than the house on the right which represents 50,000 households." / "The positive message from the press release was lost in discussions about inappropriate use of graphics." / "Even worse was the suggestion that the government were trying to mislead the public on purpose." / "An innocent explanation for the size of the houses might be that one is bigger than the other because it has more writing on it." / "But the authors had not thought about how people might interpret the image."
 SINGLE PASS: "Secondly, the house on the left represents 12,000 households." / "This example shows how important it is to get graphics right." / "This will help to reduce the risk of publishing a graphic that people might think is misleading."
 UNRESOLVED: the sentence naming the newspaper team ("ampp3d") came back three different ways; do not quote it.
Role: the official case of a decorative container read as an encoding — size chosen to fit the words, read as size of the number.

======================================================================
D8. OSR ON PRESENTATION THAT MISLEADS
======================================================================
Code of Practice for Statistics, edition 3.0 — regulatory standard. Web version shows "Publication Date: 3 November 2025", "Last Updated: 11 August 2026" (SINGLE PASS); the PDF says "Published: Autumn 2025" (SINGLE PASS).
URLs: https://osr.statisticsauthority.gov.uk/publications/the-code-of-practice-for-statistics/pages/3/ (principles), /pages/5/ (Standards for Official Statistics with practices), /pages/7/ (Standards for the Public Use…)

STRING-VERIFIED:
- Standard 9 "Be clear": "Producers must clearly present the statistics to support appropriate interpretation" [, collaborating with other producers and experts…]
- 9.2: "Communicate the statistics in a way that helps users understand issues and support them to make appropriately informed decisions." "Provide a clear description of the main messages with suitable data visualisations" — the only practice on the page containing "visualisation" (checked).
- 9.5: "Aid understanding by highlighting potential misinterpretations."
- 9.8: "Consider new ways to present data where appropriate." "Improve ways of disseminating and presenting the statistics."
- Principle 9 "Be clear", the don't: "present too much information" / "use confusing colours or jargon" (both fragments verified; full line SINGLE PASS: "Don't present too much information, use confusing colours or jargon or present insufficient information to enable appropriate interpretation or use").
- Public Use standard "Supporting Understanding": "Public bodies should use statistics, data and wider analysis with integrity and communicate them with clarity and accuracy so that the public can easily understand the basis for claims and decisions made" / "Do not use statistics, data or wider analysis in a misleading way." / "This includes not cherry-picking figures, taking figures out of context or placing undue certainty on them." / "Take proactive steps to prevent or minimise the risk of misinterpretation or misuse."
- NEGATIVE (checked): no practice in the Public Use standards mentions charts, graphs, visuals, images or infographics. The Code has no practice on decoration.
SINGLE PASS: 10.3: "Account for the needs of disabled people, using accessible communication formats and means which should work with commonly used assistive technologies and be in line with accessibility legislation". Short guide to Standard Nine (29 October 2025, https://osr.statisticsauthority.gov.uk/guidance/short-guide-to-code-of-practice-standard-nine-be-clear/): "Clear communication involves effective data presentation and visualisation, key information about what the numbers mean, appropriate context to support interpretation, and an openness to consider the receiver of the information and to strive to better meet their needs."

OSR casework and statements:
- Ed Humpherson to David Pares (HM Treasury), 27 February 2023, "HM Treasury Chart on inflation". URL: https://osr.statisticsauthority.gov.uk/correspondence/ed-humpherson-to-david-pares-treasury-inflation-infographic/
 STRING-VERIFIED: "We consider that the way the tweet presents this data to be misleading." / "The graph gives a misleading impression of the scale of the deceleration in inflation, due to the y-axis beginning at 8%." / "This would still be the case had the axis been labelled clearly with a break to signify the gap." / "An important role of data visualisation is to aid understanding of trends in data by showing them in their relevant policy context." / "It remains important that communications teams within departments consult their Heads of Profession for Statistics before publishing high-profile numbers or data visualisations of this sort."
 The letter quotes the Analysis Function as saying "when presenting data on a bar chart, the y-axis should always start at zero." (the source quoting another; that exact string is NOT on the current AF charts page — checked).
- "Statement on the presentation of political support statistics" (no date displayed; opens "Since the start of the 2024 UK general election campaign…"). URL: https://osr.statisticsauthority.gov.uk/news/statement-on-the-presentation-of-political-support-statistics/
 STRING-VERIFIED: "Starting the vertical axis for such charts at zero for each party is generally advisable in this regard."
 SINGLE PASS: "Second, polling or election results data should be visualized in a way that does not mislead the average reader about the relative support for different parties. In general, the size of the bars in charts of this sort should directly and accurately reflect the number or proportion of votes being cast or the opinion poll support being registered, rather than exaggerating the closeness or distance between the support for particular parties."
- OSR blog, "Is a picture really worth a thousand words?", by "Kirsty" (Head of Private Office and Casework Manager), 24 May 2024. URL: https://osr.statisticsauthority.gov.uk/blog/is-a-picture-really-worth-a-thousand-words/
 STRING-VERIFIED: "It is defined as a visual representation of information or data as a chart or diagram." / "Many social media platforms thrive on simplified, engaging content – which can often take the form of data visualisation." / "The y axis on this infographic was not labelled and it also didn't start at 0." / "the lines appear to suggest a bigger relative increase in pay for newly qualified nurses than the data justify."
 SINGLE PASS: "This infographic has no identifiable source, meaning that it fails our first principle of intelligent transparency as you do not have access to the data."
- OSR blog, Ed Humpherson, 30 August 2024, "Whose line is it anyway? Why the misleading presentation of statistics cannot be dismissed as just a matter of opinion". URL: https://osr.statisticsauthority.gov.uk/blog/whose-line-is-it-anyway-why-the-misleading-presentation-of-statistics-cannot-be-dismissed-as-just-a-matter-of-opinion/
 STRING-VERIFIED: "Statistics may be used to provoke and to challenge the status quo; but Ofcom is entitled to insist – in the public interest – that they should not be misused so as to mislead" — this is the blog quoting a High Court judgment (introduced, SINGLE PASS, as "Not our words but the words of a recent High Court Judgement following an intervention by Ofcom…").
 SINGLE PASS: "The misleading presentation of statistics cannot be dismissed as just a matter of opinion."
- OSR "Regulatory guidance: Dashboards" (21 August 2025) contains no sentence on visual design (SINGLE PASS).
Role: the regulator's line is about encodings (axis, bar size, source, context) and never about ornament; the Code requires "suitable" visualisations and forbids "confusing colours", and stops there.

DARK MODE AND DARK BACKGROUNDS — what UK public bodies publish
- Analysis Function: recommends white ("We recommend using white as a background colour." / "All our palettes are designed to be used with a white background."), acknowledges glare, and says full customisation "is not possible at the moment" (D1d). No dark-mode rule.
- ONS data-visualisation pages: no dark-background sentence found; "backgrounds" are listed as chart decoration to avoid (D2d). ONS brand pattern (SINGLE PASS): "The pattern can be applied on dark or light backgrounds, using full colours or one of the tints in the ONS palette."
- GOV.UK Design System: Images page silent (checked). GitHub backlog issue "Dark Mode" #177, opened December 3, 2018, still open (SINGLE PASS, https://github.com/alphagov/govuk-design-system-backlog/issues/177); team member, July 21, 2023: "Dark Mode hasn't been prioritised by the community as a big need, so it's not part of our plans to work on soon, but we're doing a strategic discovery in October that may reconfigure priorities based on emergent needs."
- Greater London Authority, "City Intelligence Data Design: Data Visualisation and Information Design Guidelines", version 2.0, May 2019. URL: https://data.london.gov.uk/download/e6wyz/00556d0a-9a1f-414f-8f04-ce050133ee96/Intelligence-Data-Styleguide_v2_0.pdf — the one UK public body found that publishes palettes for dark backgrounds. Two passes agree on: "Remove decoration and effects. Get rid of any unnecessary key lines around shapes, drop shadows and bevelling effects." (p. 7); "Minimise use of colour. Remove colour encoding of data that is there only for context or comparison."; "Avoid poor quality icons or pictograms that don't lend clear meaning to your design or might appear trite or cliched." (p. 9); heading "Remove the noise, highlight the signal" (p. 6); "Good design is as little design as possible. Less, but better." (p. 6, attributed in the document to Dieter Rams). SINGLE PASS: "All colours work on a dark background" (p. 13); "Darker categorical colour palette on a dark application background" (p. 18); "For data on dark backgrounds and maps" (p. 27). It does not say when a dark background should be used.
- Not UK: data.europa.eu guide, "Dark mode" (SINGLE PASS, https://data.europa.eu/apps/data-visualisation-guide/dark-mode): "Datawrapper changes the colours of all elements on the chart in dark mode to ensure a high enough contrast ratio with the dark background."

ICONS OR PICTOGRAMS OF PEOPLE: no Analysis Function rule. Related rules found: GOV.UK Design System "Avoid depicting people in illustrations." (D2b); FT's Isotype line (D4a); GLA's icon/pictogram line above.

======================================================================
UNASKED THREADS
======================================================================
1. WCAG has a third category between information and decoration: "specific sensory experience". STRING-VERIFIED (same Understanding page as 1.1.1): "If non-text content is primarily intended to create a specific sensory experience, then text alternatives at least provide descriptive identification of the non-text content." Definition: "a sensory experience that is not purely decorative and does not primarily convey important information or perform a function"; "Examples include a performance of a flute solo, works of visual art etc." Intent (SINGLE PASS): "Sometimes content is primarily intended to create a specific sensory experience that words cannot fully capture." This is the standard's own slot for expressive content: it must be identified and described, not ignored.

2. ONS brand guidelines license decoration, and derive it from data, in the same manual that bans chart decoration. Pattern page, URL: https://service-manual.ons.gov.uk/brand-guidelines/pattern. STRING-VERIFIED: "We are taking the most basic representation of data, a dot, and turning it into an identity fit for the Office for National Statistics (ONS)." / "A grid of dots that uses scale to represent numbers 0 to 15 in binary to produce a seemingly random pattern that still feels structured." / "Basing the pattern on data ties in with our purpose of producing and presenting statistics." / bullet "background decoration" / "positive emotional messages (circles seem softer and more welcoming than harshly angled shapes such as triangles)" / "multicolour solid – used in cuts of the pattern to add visual interest to artwork (do not use more than five colours)". The page says nothing about applying the pattern to charts (checked).

3. Tufte's own two-layer sentence (D5): "spare, straightforward, conventional, and self-effacing; AND the evidence presented should be rich, complex, multivariate, causal."

4. An EU public body states the continuum. data.europa.eu Data Visualisation Guide (footer "(c) 2023, eu | academy"; no author credited on the pages). URLs: https://data.europa.eu/apps/data-visualisation-guide/chart-junk-and-data-ink-origins and …/chart-junk-and-data-ink-minimalistic-vs-rich-design. STRING-VERIFIED: "A sane way of looking at the Tufte versus Holmes is to see them as two extremes of a continuum." / "How much ink you can and should spend on non-data elements in your designs depends on the medium, the audience, the topic and also of your own taste and style." / "If you are after readable values, effective comparisons, and a scientifical look: go towards minimalistic." / "If you want engagement, some humour and memorability, go more for the Nigel Holmes style." / "What the 2010 study showed is that a lot of chart junk is actually harmless: the message of the chart survives the embellishments and decorations." / "Non-data ink or non-data pixels that are harmful junk, should best be removed from your designs." SINGLE PASS: "But an area where Tufte's rules probably hold is in what visualisation researcher Robert Kosara calls "harmfull junk": the kind of chart junk that actively interferes with the reading and understanding of a visualization or infographic." It leans on the 2010 study (Bateman et al., already settled) and concedes: "However, what the researchers did not study, was how well people were able to read data values from both kind of charts." (SINGLE PASS).

5. OSR treats misleading presentation as a matter of fact, not taste, and relays a High Court sentence to that effect (D8).

6. The DWP "two houses" infographic (D7): the government's own teaching case of decoration accidentally becoming an encoding.

7. Carbon's "productive" versus "expressive" tiers — a commercial design system's formal two-register rule. STRING-VERIFIED (https://carbondesignsystem.com/elements/motion/overview/): "Productive motion creates a sense of efficiency and responsiveness, while remaining subtle and out of the way." / "Productive motion is appropriate for moments when the user needs to focus on completing tasks." / "Expressive motion delivers enthusiastic, vibrant, and highly visible movement." / "Reserve expressive motion for occasional, important moments, to better capture the user's attention and offer a rhythmic break to the productive experience." STRING-VERIFIED (https://carbondesignsystem.com/elements/pictograms/usage/): "Productive and expressive pictograms are two distinct types of artwork that work best in different contexts." / "Due to their visual complexity, expressive pictograms should be used selectively and only in scenarios that call for a graphic with strong presence." / "Don't overuse expressive pictograms. They should be used sparingly." Also Carbon accessibility, Deaf and hard-of-hearing users: "Find an alternative way to convey information exclusively with sound." (STRING-VERIFIED; the sentence is oddly worded at source) and (SINGLE PASS) "Transcribe and caption all videos and animations that have meaningful audio."

8. ONS on animation (D2d): "never make an animation the only way to get the information" — an official removal test for motion.

======================================================================
LEFT OUT
======================================================================
- Stephen Few: skipped as instructed.
- BBC GEL infographics: Chapter 13's.
- The Economist chart style guide PDF, medium.economist.com, archive.org: blocked.
- Sunlight Foundation PDF: unreadable (binary) in two attempts; only the launch blog is quoted.
- Material Design 2/3, Polaris: JavaScript-only or redirected; only archived Material 1 quoted.
- Reuters and NYT: no public guide found; not pursued beyond one fetch and one search.
- Tufte's books themselves: no reliable scan reachable. The data-ink ratio formula, "Erase non-data-ink, within reason", and the Lie Factor principle should be taken from the physical books; secondary sources disagree in wording.
- Analysis Function e-learning module content (only module titles visible) and the new AF dashboards page ("Data visualisation: building and managing dashboards", published 6 February 2026 — governance and lifecycle; no design sentences on a keyword pass).
- The UK Statistics Authority Chair's earlier letter referred to in the Treasury letter; the Code 3.0 guidance on the Public Use standards beyond three sentences.
- ONS Illustration, Photography and Videography brand pages (the Illustration landing page is three sentences of introduction).
- ONS "Notion" chart guidance (external; not fetched).

======================================================================
RICH REFERENCES
======================================================================
1. Analysis Function, "Advice for policy professionals using statistics and analysis", section 10 "Presentation really matters" — the DWP two-houses case told by government against itself.
2. data.europa.eu Data Visualisation Guide, the two "Chart junk and data ink" pages — a public body's plain statement of the Tufte–Holmes continuum, with "harmless" and "harmful" junk separated.
3. OSR's trio: the Treasury inflation chart letter (27 February 2023), the 2024 election bar-chart statement, and "Is a picture really worth a thousand words?" (24 May 2024) — the regulator's working test applied to real graphics.

======================================================================
SURPRISED
======================================================================
- The Analysis Function's infographics guidance contains no rule at all on pictograms, icons, 3D or decoration; it governs infographics through user need, "avoid visual clutter", and the plain-text alternative.
- GOV.UK content guidance does not ban decorative images; it defines them and regulates them. The ban-like wording ("Avoid using images for unnecessary decoration") belongs to the Design System, which is for services.
- "Decorative" has two unrelated official senses: ornament, and the technical status given to a chart image whose content is carried by adjacent text. Under the second, the Analysis Function advises marking the chart itself as decorative.
- The Code of Practice 3.0 mentions data visualisation in exactly one practice (9.2) and colour in one principle line ("confusing colours"); the Public Use standards never mention charts or images. The regulator's line on visuals lives in casework, not in the Code.
- OSR's letter quotes Analysis Function guidance in words that are not on the current guidance page.
- Official UK guidance requires a message-bearing chart title (AF, GOV.UK, ONS); a control string demanding neutral titles was rejected at ONS.
- No UK statistical body publishes a dark-mode chart rule; the Analysis Function recommends white and calls it an "anchor". Only the GLA guide publishes dark-background palettes, without saying when to use them.
- ONS lists "engaging" among its aims for charts, and its brand pages openly reason about emotion ("softer and more welcoming"), while its chart specification forbids "chart decoration".
- None of the newsroom documents reached forbids decoration by name; they forbid 3-D and distortion. The FT explicitly allows pictograms on a whole-number condition.

WebSearch calls used: 14.