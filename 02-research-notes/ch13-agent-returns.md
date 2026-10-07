# Chapter 13 — research agent returns (6 October 2026)

*Four agents, dispatched in one message with web search rationed to thirty calls each; returns kept whole. Marks: STRING-VERIFIED / SINGLE PASS / ABSTRACT as the agents reported them.*


---

## Agent A

AGENT A REPORT — THE W3C DOCUMENTS (all fetches 6 October 2026)

READ THIS FIRST — reach and labelling
- The fetch tool cuts long single-page specs. Not reachable at /TR/: the WCAG 2.2 conformance section and glossary (page cut after SC 2.5.8), ARIA 1.2 role sections after the 5.4 role list, COGA Note after pattern 4.3.3, Media Queries 5 after section 6, EN 301 549 clause 9 in the ETSI PDFs.
- Workarounds used: W3C "Understanding" pages (which reproduce each criterion and the Key Terms), the WAI supplemental-guidance pattern pages (COGA patterns), and Accessibility Standards Canada's HTML of EN 301 549:2021 (identical adoption).
- Labels: STRING-VERIFIED (SV) = a second fetch with a YES/NO presence prompt confirmed the exact string; every verification batch carried a false control string, and all controls were rejected. SINGLE PASS (SP) = seen once, or twice without a presence check.
- The reader did invent text once: a first pass on ARIA 1.2 returned plausible but false role definitions (e.g. table as "A widget that contains non-interactive tabular data..."). Nothing from that pass is used.
- U/ below = https://www.w3.org/WAI/WCAG22/Understanding/

=====================================================================
A1. WCAG 2.2 CONFORMANCE MODEL
What it is: W3C Recommendation (normative), read through the W3C Understanding page (informative, reproduces the normative text). Role: the hard line on "alternate version" versus "primary version".

Status and dates
- «W3C Recommendation 12 December 2024» — SV, https://www.w3.org/TR/WCAG22/. This version: https://www.w3.org/TR/2024/REC-WCAG22-20241212/ (SP).
- First Recommendation 5 October 2023 (SP, https://www.w3.org/standards/history/WCAG22/). The 12 December 2024 text is a republished Recommendation.
- SP from the Status section: "The publication of WCAG 2.2 does not deprecate or supersede WCAG 2.0 or WCAG 2.1."; "Content that conforms to WCAG 2.2 also conforms to WCAG 2.0 and WCAG 2.1."; "WCAG 2.2 has removed one success criterion, 4.1.1 Parsing."
- WCAG 2.1: «W3C Recommendation 06 May 2025» — SV, https://www.w3.org/TR/WCAG21/ (this version https://www.w3.org/TR/2025/REC-WCAG21-20250506/, SV). History (SP, https://www.w3.org/standards/history/WCAG21/): Recommendation 5 June 2018, republished 21 September 2023, 12 December 2024, 6 May 2025. The current 2.1 status line is therefore not 2018 or 2023.

The five conformance requirements (U/conformance)
1. Conformance Level: «One of the following levels of conformance is met in full.» SV. Level AA: «satisfies all the Level A and Level AA success criteria, or a Level AA conforming alternate version is provided» SV; the reader gave the lead-in as "For Level AA conformance, the web page" (SP). Note: «It is not recommended that Level AAA conformance be required as a general policy for entire sites because it is not possible to satisfy all Level AAA success criteria for some content» SV.
2. Full pages: «Conformance (and conformance level) is for full web page(s) only, and cannot be achieved if part of a web page is excluded.» SV. Note: «alternatives to part of a page's content are considered part of the page when the alternatives can be obtained directly from the page» SV, continuing "e.g., a long description or an alternative presentation of a video" (SP). Note: «A full page includes each variation of the page that is automatically presented by the page for various screen sizes» SV.
3. Complete processes: «When a web page is one of a series of web pages presenting a process» SV … "(i.e., a sequence of steps that need to be completed in order to accomplish an activity)" SP … «all web pages in the process conform at the specified level or better» SV.
4. Only Accessibility-Supported Ways of Using Technologies: «Only accessibility-supported ways of using technologies are relied upon to satisfy the success criteria.» SV. «Any information or functionality that is provided in a way that is not accessibility supported is also available in a way that is accessibility supported.» SV.
5. Non-Interference: "If technologies are used in a way that is not accessibility supported, or if they are used in a non-conforming way," (SP) «then they do not block the ability of users to access the rest of the page.» SV. The four criteria that apply to all content: «1.4.2 - Audio Control, 2.1.2 - No Keyboard Trap, 2.3.1 - Three Flashes or Below Threshold, and 2.2.2 - Pause, Stop, Hide» SV.
A control string "Conformance at Level AA is the minimum level that W3C recommends for all public websites" was reported absent.

"Conforming alternate version" (definition as reproduced on U/conformance)
"version that
1. conforms at the designated level, and" (SP)
2. «provides all of the same information and functionality in the same human language, and» SV
3. «is as up to date as the non-conforming content, and» SV
"4. for which at least one of the following is true: 1. the conforming version can be reached from the non-conforming page via an accessibility-supported mechanism, or 2. the non-conforming version can only be reached from the conforming version, or 3. the non-conforming version can only be reached from a conforming page that also provides a mechanism to reach the conforming version" (SP, identical in two extractions).
Notes:
- «Each version should be as conformant as possible» SV, followed by "One version would need to be fully conformant in order to meet conformance requirement 1." (SP)
- «Alternate versions should not be confused with supplementary content, which support the original page and enhance comprehension» SV.
- SP: "The alternate version does not need to be matched page for page with the original (e.g., the conforming alternate version may consist of multiple pages)."
- SP: "The conforming alternative version does not need to reside within the scope of conformance, or even on the same website, as long as it is as freely available as the non-conforming version."
- SP: "Setting user preferences within the content to produce a conforming version is an acceptable mechanism for reaching another version as long as the method used to set the preferences is accessibility supported."

W3C on when alternate versions are appropriate, and its caution (U/conformance, "Why permit alternate versions?")
- "LAST RESORT" IS NOT THE W3C'S WORDING. The phrase does not appear on the page (direct question plus a rejected control). The actual sentence, SV in two fragments: «Note that providing an alternate version is a fallback option for conformance to WCAG» «and the preferred method of conformance is to make all content directly accessible».
- «Authors relying on conforming alternate versions must make end users aware that a conforming alternate version is available» SV.
- Reasons given: new technologies not yet accessibility supported (SP); content that cannot be modified for legal or historical reasons (SP); «Sometimes, the best experience for users with certain types of disabilities is provided by tailoring a web page specifically to accommodate that disability» SV; legacy documents (SP).
- On print-first organisations: "...they still retain a paper mindset and" «often insist on formats designed for hard copy as the "primary" version» SV. «Although the Working Group feels these approaches should be deprecated» «it does not feel they can be forbidden so long as accessible versions are readily available» SV.
- SP: "A concern when permitting web pages that do not satisfy the success criteria is that people with disabilities will encounter these non-conforming pages, not be able to access their content, and not be able to find the 'conforming alternate version.'"
- Techniques listed (SP): G136, G190, C29, SCR38, SVR2, SVR3, SVR4; failure F19 "...due to not providing a method for the user to find the alternative conforming version of a non-conforming web page".

"Essential": «if removed, would fundamentally change the information or functionality of the content, and information and functionality cannot be achieved in another way that would conform» — SV, Key Terms on U/animation-from-interactions. The Understanding Conformance page does not define it.

"Accessibility supported": «supported by users' assistive technologies as well as the accessibility features in browsers and other user agents» SV. SP notes: "The Accessibility Guidelines Working Group and the W3C do not specify which or how much support by assistive technologies there must be for a particular use of a web technology in order for it to be classified as accessibility supported."

Partial conformance, third-party content (U/conformance): "However, if the page does not conform to WCAG only for reasons that are legitimately outside the author's control" (SP) «then the author can make a claim of partial conformance» SV. «It is important to recognize that this is a statement of non-conformance» SV. SP: "When an author makes a decision to use a third party implementation, they should choose products that meet WCAG requirements."; "If it is not possible to monitor and repair the third party content, it is necessary to identify the non-conforming parts of the page for users."

=====================================================================
A2. CRITERIA THAT BITE ON AN INTERACTIVE DATA DISPLAY
What it is: normative sentence as reproduced on each Understanding page, plus one informative intent sentence. All SV unless marked.

1.3.2 Meaningful Sequence (A) — U/meaningful-sequence
«When the sequence in which content is presented affects its meaning, a correct reading sequence can be programmatically determined.»
Intent: «to enable a user agent to provide an alternative presentation of content while preserving the reading order needed to understand the meaning»; «may confuse or disorient users when assistive technology reads the content in the wrong order». Technique «C27: Making the DOM order match the visual order».

1.3.3 Sensory Characteristics (A) — U/sensory-characteristics
«Instructions provided for understanding and operating content do not rely solely on sensory characteristics of components such as shape, color, size, visual location, orientation, or sound.»
Intent: «to ensure that all users can access instructions for using the content, even when they cannot perceive shape or size or use information about spatial location or orientation». Also: «Providing information using shape and/or location, however, is an effective method for many users including those with cognitive limitations.» «This provision should not discourage those types of cues as long as the information is also provided in other ways.» Failing example: «The instructions rely on color and shape only and result in a failure of this criterion».

1.4.4 Resize Text (AA) — U/resize-text
«Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality.»
Intent: «to ensure that visually rendered text, including controls and labels using text, can be made larger» «so that it can be read more easily by people with milder visual impairments, without requiring the use of assistive technology». Also: «Images of text do not scale as well as text because they tend to pixelate, and therefore we suggest using text wherever possible.» «It is also harder to change foreground and background contrast and color combinations for images of text, which are necessary for some users.»

1.4.5 Images of Text (AA) — in full under A3.

1.4.12 Text Spacing (AA) — U/text-spacing
«In content implemented using markup languages that support the following text style properties, no loss of content or functionality occurs by setting all of the following and by changing no other style property:» «Line height (line spacing) to at least 1.5 times the font size;» «Spacing following paragraphs to at least 2 times the font size;» «Letter spacing (tracking) to at least 0.12 times the font size;» «Word spacing to at least 0.16 times the font size.»
Intent: «to ensure that when people override author-specified text spacing to improve their reading experience, content is still readable and operable». Relevant: «For this SC, canvas implementations of text are considered to be images of text.» «Currently, this SC does not apply to PDF, as the portable document format is not implemented using markup.» The page does not mention SVG at all.

2.1.2 No Keyboard Trap (A) — U/no-keyboard-trap
«If keyboard focus can be moved to a component of the page using a keyboard interface, then focus can be moved away from that component using only a keyboard interface,» «and, if it requires more than unmodified arrow or tab keys or other standard exit methods, the user is advised of the method for moving focus away.»
Intent: «to ensure that content does not "trap" keyboard focus within subsections of content on a web page»; cause named: «or when custom components and widgets are not implemented with keyboard users in mind».

2.2.2 Pause, Stop, Hide (A) — U/pause-stop-hide
«For moving, blinking, scrolling, or auto-updating information, all of the following are true:»
«For any moving, blinking or scrolling information that (1) starts automatically, (2) lasts more than five seconds, and (3) is presented in parallel with other content,» «there is a mechanism for the user to pause, stop, or hide it unless the movement, blinking, or scrolling is part of an activity where it is essential; and»
«For any auto-updating information that (1) starts automatically and (2) is presented in parallel with other content,» «there is a mechanism for the user to pause, stop, or hide it or to control the frequency of the update unless the auto-updating is part of an activity where it is essential.»
Intent: «The intent of this success criterion is to avoid distracting users during their interaction with a web page.» «Five seconds was chosen because it is long enough to get a user's attention, but not so long that a user cannot wait out the distraction if necessary to use the page.» «Certain groups, particularly those with attention deficit disorders, find blinking content distracting». Note 4: «An animation that occurs as part of a preload phase or similar situation can be considered essential» (continues, SP, "if interaction cannot occur during that phase for all users and if not indicating progress could confuse users..."). SP: '"starts automatically" broadly refers to animations/updates that are not the direct result of a user's intentional activation'; "Pausing and jumping to current display (when pause is released) is better for information that is real-time or 'status' in nature."

2.3.1 Three Flashes or Below Threshold (A) — U/three-flashes-or-below-threshold
«Web pages do not contain anything that flashes more than three times in any one second period, or the flash is below the general flash and red flash thresholds.»
Intent: «to allow users to access the full content of a site without inducing seizures due to photosensitivity».

2.3.3 Animation from Interactions (AAA) — U/animation-from-interactions
«Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed.»
Intent: «The intent of this success criterion is to allow users to prevent animation from being displayed on web pages.» «Some users experience distraction or nausea from animated content.»
Vestibular sentences: «Vestibular (inner ear) disorder reactions include dizziness, nausea and headaches.» «The impact of animation on people with vestibular disorders can be quite severe.» «Triggered reactions include nausea, migraine headaches, and potentially needing bed rest to recover.» «People with vestibular disorders need control over movement triggered by interactions.»
Boundary with 2.2.2: «In contrast, 2.2.2 Pause, Stop, Hide applies when the web page initiates animation» (continues, SP, "'automatically' that is not in response to an intentional user activation").
Definition, motion animation: «addition of steps between conditions to create the illusion of movement or to give a sense of a smooth transition»; note (SP): "Motion animation does not include changes of color, blurring, or opacity which do not change the perceived size, shape, or position of the element."

2.4.3 Focus Order (A) — U/focus-order
«If a web page can be navigated sequentially and the navigation sequences affect meaning or operation, focusable components receive focus in an order that preserves meaning and operability.»
Intent: «to ensure that when users navigate sequentially through content, they encounter information in an order that is consistent with the meaning of the content and can be operated from the keyboard». «This reduces confusion by letting users form a consistent mental model of the content.» Arrow-key navigation is out of scope: «using arrow key navigation to traverse a tree component». SP: "Focus order does not necessarily need to follow the visual layout of the web page, as long as the order in which elements receive focus is logical."

2.4.7 Focus Visible (AA) — U/focus-visible
«Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible.»
Intent: «The purpose of this success criterion is to help a person know which element has the keyboard focus.» «Authors are responsible for providing at least one mode of operation where the focus is visible.»

2.4.11 Focus Not Obscured (Minimum) (AA) — U/focus-not-obscured-minimum
«When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content.»
Intent (SP; the presence check answered NO but returned the identical sentence as "closest"): "The intent of this success criterion is to ensure that the item receiving keyboard focus is always partially visible in the user's viewport." «Typical types of content that can overlap focused items are sticky footers, sticky headers, and non-modal dialogs.» «Where users cannot see the item with focus, they may not know how to proceed, or may even think the system has become unresponsive.» SP Note 2: "Content opened by the user may obscure the component receiving focus. If the user can reveal the focused component without advancing the keyboard focus, the component with focus is not considered visually hidden due to author-created content."

2.4.13 Focus Appearance (AAA) — U/focus-appearance
«When the keyboard focus indicator is visible, an area of the focus indicator meets all the following:» «is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component or sub-component, and» «has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states.» Exceptions: «The focus indicator is determined by the user agent and cannot be adjusted by the author, or» «The focus indicator and the indicator's background color are not modified by the author.»
Purpose (SP; same NO-with-identical-sentence quirk): "The purpose of this success criterion is to ensure a keyboard focus indicator is clearly visible and discernible." Note: «Examples of sub-components that may receive a focus indicator are menu items in an opened drop-down menu, or focusable cells in a grid.»

2.5.2 Pointer Cancellation (A) — U/pointer-cancellation
«For functionality that can be operated using a single pointer, at least one of the following is true:» No Down-Event: «The down-event of the pointer is not used to execute any part of the function;» Abort or Undo: «Completion of the function is on the up-event, and a mechanism is available to abort the function before completion or to undo the function after completion;» Up Reversal: «The up-event reverses any outcome of the preceding down-event;» Essential: «Completing the function on the down-event is essential.»
Intent: «The intent of this success criterion is to make it easier for users to prevent accidental or erroneous pointer input.»

3.2.1 On Focus (A) — U/on-focus
«When any user interface component receives focus, it does not initiate a change of context.»
Intent: «to ensure that functionality is predictable as visitors navigate their way through a document».
"Changes of context": «major changes that, if made without user awareness, can disorient users who are not able to view the entire page simultaneously»; list includes «content that changes the meaning of the web page»; «A change of content is not always a change of context.» «Changes in content, such as an expanding outline, dynamic menu, or a tab control do not necessarily change the context, unless they also change one of the above (e.g., focus).»

3.2.2 On Input (A) — U/on-input
«Changing the setting of any user interface component does not automatically cause a change of context unless the user has been advised of the behavior before using the component.»
Intent: «The intent of this success criterion is to ensure that entering data or selecting a form control has predictable effects.» «Changes in context can confuse users who do not easily perceive the change or are easily distracted by changes.» «Changes of context are appropriate only when it is clear that such a change will happen in response to the user's action.»
Example closest to a filter (a select that reveals fields): «Because only parts of the entry change and the overall structure remains the same, the basic context remains for the user.» SP techniques: G80, G13, H32, H84, "SCR19: Using an onchange event on a select element without causing a change of context".

3.3.2 Labels or Instructions (A) — U/labels-or-instructions (the only 3.3.x read)
«Labels or instructions are provided when content requires user input.» «In the case of radio buttons, checkboxes, comboboxes, or similar controls that provide users with options, each option must have an appropriate label so that users know what they are actually selecting.» «Too much information or instruction can be just as harmful as too little.»

4.1.2 Name, Role, Value (A) — U/name-role-value
«For all user interface components (including but not limited to: form elements, links and components generated by scripts), the name and role can be programmatically determined;» «states, properties, and values that can be set by the user can be programmatically set;» «and notification of changes to these items is available to user agents, including assistive technologies.» Note: «This success criterion is primarily for web authors who develop or script their own user interface components.»
Intent: «to ensure that Assistive Technologies (AT) can gather appropriate information about, activate (or set) and keep up to date on the status of user interface controls in the content». «If custom controls are created, however, or interface elements are programmed (in code or script) to have a different role and/or function than usual,» (continues, SP, "then additional measures need to be taken...").

4.1.3 Status Messages (AA) — U/status-messages. Governs how a filter's result is announced.
«In content implemented using markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.»
Definition: «change in content that is not a change of context, and that provides information to the user on the success or results of an action, on the waiting state of an application, on the progress of a process, or on the existence of errors».
Intent: «to make users aware of important changes in content that are not given focus, and to do so in a way that doesn't unnecessarily interrupt their work». «The intended beneficiaries are blind and low vision users of assistive technologies with screen reader capabilities.»
The distinction that matters for a filter: «For example, the list of results obtained from a search are not considered a status update and thus are not covered by this success criterion.» But brief messages about the search «such as "Searching...", "18 results returned" or "No results returned" would be status updates if they do not take focus or cause a page refresh».
Example: «The change to content also includes the message "5 results returned" near the top of this new content.» «A screen reader announces, "Five results returned".»
Not status messages: «Content is exposed or hidden when a user interacts with a user interface component, for example expanding components such as a menu, select, accordion or tree, or selecting a different tab item in a tablist.»
Cautions: «However, there is a risk of making an application too "chatty" for a screen reader user.» «User testing should be carried out to ensure the appropriate level of feedback is achieved.» «The purpose of this success criterion is not to force authors to generate new status messages.»
Other examples, SP: shopping cart "5 items"; "Invalid entry"; busy icon announced "application busy"; progress bar; "Your form was successfully submitted."; "5 errors on page". On partial updates, SP: "where only the number in this string was coded as an updated chunk of content, the resulting experience for screen reader users could be to only hear 'three'".
Techniques listed, SP: ARIA22, ARIA19, ARIA23, ARIA25, ARIA27, G199.

1.1.1 Understanding, charts — U/non-text-content
Example "A data chart", four sentences, all SV: «A bar chart compares how many widgets were sold in June, July, and August.» «The short label says, "Figure one - Sales in June, July and August."» «The longer description identifies the type of chart, provides a high-level summary of the data, trends and implications comparable to those available from the chart.» «Where possible and practical, the actual data is provided in a table.»
Situation B: «If a short description can not serve the same purpose and present the same information as the non-text content (e.g., a chart or diagram)». «Short and long text alternatives can be used as needed to convey the information in the non-text content.» The phrase "complex images" was not returned from this page; it is the tutorial's term (A5).

1.4.11 Understanding, charts — U/non-text-contrast
- «and the important parts of a more complex diagram such as each line in a graph» (definition of "graphical object").
- «Not every graphical object needs to contrast with its surroundings - only those that are required for a user to understand what the graphic is conveying.»
- «If a person needs to perceive a graphic, or part of a graphic (a graphical object) in order to understand the content it should have sufficient contrast.» «However, that is not a requirement when:» «A graphic with text embedded or overlaid conveys the same information, such as labels and values on a chart.» / «The information is available in another form, such as in a table that follows the graph, which becomes visible when a "Long Description" button is pressed.» / SP "The graphic's presentation falls under the essential exception". Also SP in that list: "Text within a graphic must meet 1.4.3 Contrast (Minimum)".
- Essential examples: «Color gradients that represent a measurement, such as heat maps.»
- «Pie charts make a good case study for the graphical objects part of this success criterion». Fail: labels present but «the contrast between the slices is not 3:1 or greater». Not applicable: «The pie chart has visible labels and values that convey equivalent information to the graphical objects (the pie slices).» Pass (SP): "visible labels, and sufficient contrast around and between the slices".
- «The graphical objects are the lines in the graph, including the background lines for the values, and the colored lines with shapes.»

=====================================================================
A3. IMAGES OF TEXT, SPECIFICALLY (quotation only)
Sources: U/images-of-text and U/images-of-text-no-exception (informative, carrying normative text); Techniques C22 and C30 (informative).

1.4.5 Images of Text (Level AA), normative, SV (also seen on the /TR/ page, SP):
«If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except for the following:»
Customizable: «The image of text can be visually customized to the user's requirements;»
Essential: «A particular presentation of text is essential to the information being conveyed.»
Note: «Logotypes (text that is part of a logo or brand name) are considered essential.»

Definitions, SV:
- image of text: «text that has been rendered in a non-text form (e.g., an image) in order to achieve a particular visual effect». Note: «This does not include text that is part of a picture that contains significant other visual content.» Example: «A person's name on a nametag in a photograph.»
- visually customized: «the font, size, color, and background can be set».
- SP, text: "sequence of characters that can be programmatically determined, where the sequence is expressing something in human language".

Stated intent, SV: «to encourage authors, who are using technologies which are capable of achieving their desired default visual presentation,» «to enable people who require a particular visual presentation of text to be able to adjust the text presentation as needed». «This includes people who require the text in a particular font size, foreground and background color, font family, line spacing or alignment.» «If authors can use text to achieve the same visual effect, they should present the information as text rather than using an image.» Essential examples: «such as type samples, logotypes, branding, etc.» In Brief: «People cannot alter how text looks in images.»

The sentences that bear on provenance text inside a chart image — all SV, Intent section of U/images-of-text:
(a) The Intent restates the definition's note and adds: «Examples of such pictures include graphs, screenshots, and diagrams which visually convey important information through more than just text.»
(b) «The success criterion is intended to address situations where images of text are used rather than text.»
(c) «Where images of text are used in addition to text to convey the same information, and where both are presented to the user, this success criterion is met.»
(d) «This allows authors to convey content using any styling they desire, while also presenting the information in text, which can then be manipulated by users to make it more distinguishable.»
Example on the same page, SV: title «The text in an image is also provided as text»; «The site's CMS (content management system) is limited, and won't allow them to create a custom HTML/CSS/SVG recreation of the poster.» … «so they post both the poster and the text contained in the image» … «This text is shown next to the poster image on the site's calendar page.»

What the text does not say: no sentence on this page concerns downloadable images or charts as such (controls "A downloadable chart image must never contain a title" and "Text inside a chart image always fails..." both absent). The page lists no Failure techniques. The SV condition in (c) is «and where both are presented to the user».

Examples offered for the exceptions (SP): Styled Headings; Dynamically Generated Images; A quote; Navigation items; A logo containing text; Representation of a font family; A representation of a letter; Symbolic text characters; Customizable font settings in images of text; The text in an image is also provided as text. No chart example.
Benefits: «People with cognitive disabilities that affect reading can change and restyle the text to suit their specific needs.» SV.

Techniques
- «C22: Using CSS to control visual presentation of text» SV — Sufficient for 1.4.5 and 1.4.9 (SP). SP: "Text within images has several accessibility problems, including the inability to: be scaled according to settings in the browser; be displayed in colors specified by settings in the browser or rules in user-defined style sheets; honor operating system settings, such as high contrast".
- «C30: Using CSS to replace text with images of text and providing user interface controls to switch» SV — Sufficient for 1.4.5 and 1.4.9 (SP). The technique can be used to meet either criterion «if a presentation that does not include images of text is available» SV. «Where possible, authors should deliver the presentation that does not include images of text as the default presentation.» SV. «In addition, the control used to switch should be located near the beginning of the page.» SV. Test: «Check that when the control is activated the resulting page includes text (programmatically determined text) wherever images of text had been used.» SV.
- Also listed, SP: G140, PDF7.

1.4.9 Images of Text (No Exception) (Level AAA) — for contrast:
«Images of text are only used for pure decoration or where a particular presentation of text is essential to the information being conveyed.» SV. Intent: «to enable people who require a particular visual presentation of text to be able to adjust the text presentation as required» SV; «Using images of text is an example of an implementation that does not allow users to alter the presentation of the text within it.» SV. The 1.4.9 page also carries «Examples of such pictures include graphs, screenshots, and diagrams which visually convey important information through more than just text.» SV. It does NOT carry sentence (c): that string was reported absent from the 1.4.9 page.

Neighbouring text on the same question: 1.4.4 «Except for captions and images of text...»; 1.4.12 «canvas implementations of text are considered to be images of text»; 1.4.11 «A graphic with text embedded or overlaid conveys the same information, such as labels and values on a chart.» and (SP) "Text within a graphic must meet 1.4.3 Contrast (Minimum)". WAI tutorial "Images of Text" (https://www.w3.org/WAI/tutorials/images/textual/, "Status: Updated 12 April 2017", SP): «Genuine text is much more flexible than images: It can be resized without losing clarity, and background and text colors can be modified to suit the reading preferences of users.» SV; «In those rare situations where images of text must be used, the text alternative must contain the same text presented in the image.» SV.

The requested "note on images of text within the definition of text alternative": no such note exists.
- "text alternative" (Key Terms, U/non-text-content): «Text that is programmatically associated with non-text content or referred to from text that is programmatically associated with non-text content.» «Programmatically associated text is text whose location can be programmatically determined from the non-text content.» SV. Its only note is "Refer to Understanding Text Alternatives for more information." (SP). Its example is a chart: «An image of a chart is described in text in the paragraph after the chart. The short text alternative for the chart indicates that a description follows.» SV.
- The images-of-text mention is in the "non-text content" note: «This includes ASCII art (which is a pattern of characters), emoticons, leetspeak (which uses character substitution), and images representing text» SV.

=====================================================================
A4. WAI-ARIA 1.2, APG, GRAPHICS MODULE, ARIA 1.3

WAI-ARIA 1.2 — W3C Recommendation 06 June 2023 (SP on https://www.w3.org/TR/wai-aria-1.2/; same date SP on the history page). Normative. Role definitions SV from the section 5.4 role list:
- alert: «A type of live region with important, and usually time-sensitive, information.»
- status: «A type of live region whose content is advisory information for the user but is not important enough to justify an alert, often but not necessarily presented as a status bar.»
- log: "A type of live region where new information is added in meaningful order and old information may disappear" (SP; the reader corrected my "can" to "may").
- table: «A section containing data arranged in rows and columns.»
- grid: «A composite widget containing a collection of one or more rows with one or more cells where some or all cells in the grid are focusable by using methods of two-dimensional navigation, such as directional arrow keys.»
- treegrid: «A grid whose rows can be expanded and collapsed in the same manner as for a tree.»
- figure: «A perceivable section of content that typically contains a graphical document, images, code snippets, or example text.»
- img: «A container for a collection of elements that form an image.»
- document: «An element containing content that assistive technology users may want to browse in a reading mode.»
- application: «A structure containing one or more focusable elements requiring user input, such as keyboard or gesture events, that do not follow a standard interaction pattern supported by a widget role.»
- No role named chart or graph in the list.
- The aria-live property definition and its off/polite/assertive value table were NOT reachable (truncation).

Politeness, from WCAG Techniques instead (informative):
- ARIA22 «Using role=status to present status messages» (https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22): «The aria live region role of status has an implicit aria-live value of polite, which allows a user to be notified via AT (such as a screen reader) when status messages are added.» SV. «The role of status also has a default aria-atomic value of true» SV. «The content of the aria-live container is automatically read by the AT, without the AT having to focus on the place where the text is displayed.» SV. Example 1 "Including a search results message" with <div role="status" aria-atomic="true">5 results returned.</div> (SP).
- ARIA19 «Using ARIA role=alert or Live Regions to Identify Errors» SV (https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA19): "The following example uses role=alert which is equivalent to using aria-live=assertive." (SP).
- ARIA27 «Using ariaNotify to convey the status of a progress bar» SV: «As of April 2026, ariaNotify is still an experimental feature in web browsers and assistive technologies.» SV; «only use ariaNotify as a progressive enhancement in combination with other more reliable techniques» SV.

ARIA Authoring Practices Guide — informative WAI resource. The three earlier Authoring Practices documents are listed "Retired" on the ARIA WG publications page (SP).
- Read Me First (https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/): «No ARIA is better than Bad ARIA»; «A role is a promise»; «Incorrect ARIA misrepresents visual experiences, with potentially devastating effects on their corresponding non-visual experiences.»; «ARIA roles do not cause browsers to provide keyboard behaviors or styling.»; «Testing assistive technology interoperability is essential before using code from this guide in production.» All SV. SP: "the purpose of this guide is to illustrate appropriate use of ARIA 1.2 as defined in the ARIA specification."
- Table pattern (https://www.w3.org/WAI/ARIA/apg/patterns/table/): «Like an HTML table element, a WAI-ARIA table is a static tabular structure containing one or more rows that each contain one or more cells; it is not an interactive widget.» «Thus, its cells are not focusable or selectable.» «The grid pattern is used to make an interactive widget that has a tabular structure.» «authors are strongly encouraged to use a native HTML table element whenever possible» «It is thus advisable to test implementations thoroughly with each browser and assistive technology combination that could be used by the target audience.» All SV.
- Grid pattern (https://www.w3.org/WAI/ARIA/apg/patterns/grid/): «A grid widget is a container that enables users to navigate the information or interactive elements it contains using directional navigation keys, such as arrow keys, Home, and End.» «It can be used for purposes as simple as grouping a collection of checkboxes or navigation links or as complex as creating a full-featured spreadsheet application.» «A grid can be used to present tabular information that has column titles, row titles, or both.» «The grid pattern is particularly useful if the tabular information is editable or interactive.» «Only one of the focusable elements contained by the grid is included in the page tab sequence.» All SV. SP: "Uses of the grid pattern broadly fall into two categories: presenting tabular information (data grids) and grouping other widgets (layout grids)."; "While in application mode, a screen reader user hears only focusable elements and content that labels focusable elements."
- Alert pattern (https://www.w3.org/WAI/ARIA/apg/patterns/alert/): «An alert is an element that displays a brief, important message in a way that attracts the user's attention without interrupting the user's task.» «it is crucial they do not affect keyboard focus» «It is also important to avoid designing alerts that disappear automatically.» «Another critical design consideration is the frequency of interruption caused by alerts.» «Frequent interruptions inhibit usability for people with visual and cognitive disabilities» All SV.
- Names and descriptions (https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/): «Providing elements with accessible names, and where appropriate, accessible descriptions, is one of the most important responsibilities authors have when developing accessible web experiences.» SV. On aria-describedby: «Descriptions are reduced to text strings.» «For example, if the description contains an HTML img element, a text equivalent of the image is computed.» SV. «Rule 2: Prefer Visible Text» SV. SP: "An accessible name is a short string, typically 1 to 3 words..."; "Like with table elements, if a figure is not named using aria-label or aria-labelledby, the content of the figcaption element will be used as the accessible name." The page does not mention aria-details.
- APG has NO practice page on live regions and NO pattern or practice for charts, graphs, images, figures or data visualisation (SP, pattern and practice index pages).

WAI-ARIA Graphics Module 1.0 — it is a RECOMMENDATION, not a Working Draft: «W3C Recommendation 02 October 2018» SV (https://www.w3.org/TR/graphics-aria-1.0/). First Public Working Draft 3 December 2015 (SP, history page). Graphics Accessibility API Mappings: Recommendation 2 October 2018 (SP). Role definitions, SV:
- graphics-document: «A type of document in which the visual appearance or layout of content conveys meaning.» Superclass document; accessible name required: true (SP). SP fragment: authors SHOULD use it "for structured graphics such as charts, maps, diagrams, technical drawing, blue prints and instructional graphics".
- graphics-object: «A section of a graphics-document that represents a distinct object or sub-component with semantic meaning.»
- graphics-symbol: «A graphical object used to convey a simple meaning or category, where the meaning is more important than the particular visual appearance.» Superclass img; children presentational: true (SP).
- Its own statement of what it lacks: «Future work will expand on this framework to enable more detailed annotation of data-rich graphics such as charts or maps.» SV.

WAI-ARIA 1.3 — «W3C Working Draft 04 June 2026» SV (https://www.w3.org/TR/wai-aria-1.3/; this version https://www.w3.org/TR/2026/WD-wai-aria-1.3-20260604/ SV). First Public Working Draft 23 January 2024 (SP). The words sectionheader and ariaNotify are present (SV). No chart, graph or data-visualisation role in the visible text (SP; role sections truncated).

=====================================================================
A5. WAI TUTORIAL: COMPLEX IMAGES
https://www.w3.org/WAI/tutorials/images/complex/ — informative WAI tutorial. Status line «Updated 08 April 2026» SV. THE PAGE HAS CHANGED FROM THE VERSION USUALLY CITED.

Two-part rule, all SV: «Complex images contain substantial information – more than can be conveyed in a short phrase or sentence.» List includes «graphs and charts, including flow charts and organizational charts;» and «maps showing locations or other information such as weather systems.» «In these cases, a two-part text alternative is required.» «The first part is the short description to identify the image and, where appropriate, indicate the location of the long description.» «The second part is the long description – a textual representation of the essential information conveyed by the image.»

"Long descriptions" section, all SV: «Complex images can be difficult to understand by many people – especially those with low vision, learning disabilities, and limited subject-matter experience.» «Make long descriptions available to everyone to reach a wider audience with your content.» «It is also good practice to refer to and summarize more complex images from the accompanying text.»

Approaches — there are now THREE, not four, under "Example 1: Description containing structured information":
- «Approach 1: A text link to the long description adjacent to the image» SV. «All web browsers and assistive technologies support this approach.» SV. «However, the link is not associated with the image in a semantic way.» SV. A sub-heading "Semantic association of long description link to the image" (figure/figcaption, role="group") — SP.
- «Approach 2: Describing the location of the long description in the alt attribute» SV.
- «Approach 3: Structurally associating the image and its adjacent long description (HTML5)» SV. «The long description (presented as headings, text, and a table) is wrapped in the figcaption element.» SV.
- No Approach 4. The word "longdesc" does not appear anywhere on the page (direct question plus rejected control).
"Example 2: Description containing textual information" uses aria-describedby, with a warning, SV: «The element referenced by aria-describedby is treated as one continuous paragraph of text.» «Screen readers and other assistive technology do not have access to structural information, such as any headings and tables.» «As a result, this approach only works for long descriptions that are text-only».

The chart example: alt text «Bar chart showing monthly and total visitors for the first quarter 2025 for sites 1 to 3» SV (the year is now 2025). «The long description provides detailed information, including scales, values, relationships and trends that are represented visually.» SV. SP: "For example, the long description can point out the declining values for site 1, consistent values for site 2, and increasing values for site 3 that are encoded in the bar chart."

Does it say the long description should include the data table? The tutorial has no normative "should include a table" sentence (control "The long description must always be a data table" absent). But its worked long description DOES contain one. https://www.w3.org/WAI/tutorials/images/examples/long-description/ has three sub-headings — Overview, Values, Presentation (SP). «The chart shows the website hits for the first quarter of 2025.» SV. «Numerical values presented on the image:» SV, followed by a table captioned "2025 First Quarter visitors per site (in thousands)" (SP). «The bar chart represents both the number of visitors per month for each website, and the total number of visitors per website for the entire quarter.» SV.
Elsewhere W3C says more: Understanding 1.1.1 «Where possible and practical, the actual data is provided in a table.» SV; Technique G92 (https://www.w3.org/WAI/WCAG22/Techniques/general/G92, Sufficient for 1.1.1) Example 2 «The long description includes the data table that was used to generate the line graph.» SV. G92 also, SV: «Combined with the short text alternative, the long description should be able to substitute for the non-text content.» «The short alternative identifies the non-text content; the long alternative provides the information.» «If the non-text content were removed from the page and substituted with the short and long descriptions, the page would still provide the same function and information.» Example 1 is a description without a table: «The primary use of the chart is to show leaders, so the description is in sales order.» SV.
The tutorial's "Related WCAG resources" list returned only C22 (SP; probably incomplete).

=====================================================================
A6. COGA — MAKING CONTENT USABLE
Status: «W3C Working Group Note 29 April 2021» SV (https://www.w3.org/TR/coga-usable/). No later version: the history page lists the Note of 29 April 2021 as the latest entry (SP), and /TR/coga-usable-2/ returns 404. WAI's "What We're Working On" (Updated 28 August 2026, SP) says: "We're updating several documents to better address the needs of people with cognitive and learning disabilities."
The document's own statement of status, SV: «This document was published by the Cognitive and Learning Disabilities Accessibility Task Force» … «The objectives and patterns presented here provide supplemental guidance beyond the requirements of WCAG.» «Following this guidance is not required for conformance to WCAG.» «Publication as a Working Group Note does not imply endorsement by the W3C Membership.» «This is a draft document and may be updated, replaced or obsoleted by other documents at any time.» Also «They address accessibility barriers that were not included in the normative WCAG 2.x» (continues, SP, "and may not otherwise be addressed"). Abstract, SV: «This document is for people who make web content (web pages) and web applications.» «It gives advice on how to make content usable for people with cognitive and learning disabilities.»
Pattern text below is from WAI's supplemental-guidance pages, which carry the Note's patterns ("Content first published 29 April 2021; user interface posted January 2022" — SP; banner "Additional ways to improve accessibility, not required to meet WCAG" — SP). Base: https://www.w3.org/WAI/WCAG2/supplemental/patterns/ . All strings SV unless marked.

Provide Alternatives for Numerical Concepts (o3p13-numerical-alternatives/)
User need: «I need words rather than numbers and numerical concepts.»
What to do: «Provide alternatives for numbers and numerical concepts.»
How it helps: «Not all people can understand numbers and numerical concepts.» «For example, a user with dyscalculia may have difficulty processing temperature data when presented only in a numeric format.» «However, if non-numeric alternatives are provided (cold, warm, hot etc.) then they are able to understand the content.» «Numeracy issues can occur due to a range of disabilities, the most severe being the inability to read or understand numbers.» «Other people have challenges with any calculations such as relative sizes or times.» «For example, a user may understand the concept of 90cms as a length but find it hard to cope with the fact that 0.9m and 900mm are the same length.» SP: the train-timetable example ("The user cannot calculate when the next train leaves from their location.").
More details: «Reinforce numbers with non-numerical concepts, e.g., very cold, cold, cool, mild, warm, hot, very hot.» Lead-ins (SP): "Where an understanding of mathematics is not a primary requirement for using this content use one of the following:" and "Where some math skills are essential for the content:". SP bullets: "Move towards digital math that can be extended (not numbers in images)."; "Enable replacing math sections with words or summaries for users who prefer this."
Examples — Use (SP list): "Extra support for numerical content such as: sizes, quantity, distance, time, date, temperature, positive/negative, calculations, sequencing, percentages." then «For the above, there is a description or representation of what the number means as a concept.» Avoid: «Numerical content without extra support.»
User story in the Note: «Math Concepts (User Story)» — «As a user who does not understand numerical concepts, I need content to be usable without understanding math concepts.» «I need content that provides alternatives like a non-math textual explanation.»

Do Not Rely on Users Calculations or Memorizing Information (o6p05-low-cognition/)
User need: «I need navigation and processes that do not rely on memory.»
What to do: lead-in "Create a process that does not require:" (SP), items include "remembering digits to select for a short time" (SP), «performing calculations», and «When going through multiple steps, each step in a process must contain the information needed to allow a user to proceed.» «They must not rely on memory from prior steps.» «Instructions and labels should be located before a call to action or activation mechanism.» «When appropriate, provide a summary of information from previous steps, and a mechanism for traversing the process.»
How it helps: «Many users have an impaired working memory.» «They cannot remember many details at the same time.»
More details: «Each step in a process should contain the information necessary to allow a user to proceed.»
Avoid: «Requiring the user remember a code or a category from a previous step.»
NOTE ON THE ITEM NAMED IN THE BRIEF: no pattern is titled "Ensure Each Step in a Process Includes the Information Needed to Complete It" in the Note's contents list. The wording lives inside this pattern. The nearest titled patterns are below.

Make Each Step Clear (o1p04-clear-steps/)
User need: «I need to recognize where I am in the architecture of the web site, application, or multi-step process, even after I get distracted.» What to do: «Provide breadcrumbs, a "how I got here" button, or heading to help the user orientate themselves inside a site or task.» SP: "In a multi-step process, this includes showing: the steps completed, the current step, the steps pending, and any important choices." How it helps: «Clearly indicating the current location and progress helps the user continue after they lose focus without reading a great deal of content or restarting.» Avoid: «Completed steps and choices that are hard to find and check.»

Provide Information So a User Can Complete and Prepare for a Task (o5p04-task-expectations/) — all SP: user need "I need to know how to start a task, and what is involved."; estimate of "the time it might take," "details of any resources needed to perform the task, and" "overview of the process and next step."

Use Clear Words (o3p01-clear-words/)
User need: «I need to understand the language used, including vocabulary, syntax, tense, and other aspects of language.»
What to do: «Use common and clear words in all content.» «Look at the most common 1500 words or phrases.» «These are the terms that people with severe language impairments are most likely to know.» «Remove unnecessary or vague words (such as: "and so forth").» «Remove or explain uncommon acronyms, abbreviations, and jargon.» «Do not invent new words or give words new meanings in your application.» «If you must create new terms, make sure the user has access to an explanation within one click or event.»
How it helps: «Using uncommon words can make text and media difficult to understand.» «People with language impairments often have a reduced vocabulary.» Example: «The menu item for selecting heat or air conditioning is labeled "mode".» «This type of design has caused emergencies such as hypothermia.»
SP: explain uncommon words by "adding a simple language term in brackets next to it," "providing a pop up definition, or" supported markup; the landlord/security-deposit example.

Provide Summary of Long Documents and Media (o3p08-summary-provided/)
User need: «I need an easy to understand, short summary for long pieces of content or an option for an Easy to Understand version.»
What to do: «Provide a brief summary for a long document and media.» «Emphasize any important keywords to help people understand the purpose and content of the document, and determine if it might contain information they need.» «Summaries should use common words, short sentences, and be written in an easy to understand style and tense.»
How it helps: «Providing an easy to understand summary helps many people to quickly decide if the content is relevant to them and their current goal.» «A high level outline in a few sentences or bullet points is most effective.» «Abstracts and executive summaries are usually much longer and more detailed as they are designed to summarize the entire document.»
More details: «Provide a text summary that can be understood by people with lower secondary education level reading ability.» «In pieces of content with less than 300 words, headings can act as a summary.»
Use: «Short summaries with bullet points that clearly state the main points.» Avoid: «Long texts, documents, or media without summaries.»

Make the Purpose of Your Page Clear (o1p01-clear-purpose/)
User need: «I need to know the context and purpose of the page.»
What to do: «Help the user know the purpose of the content.» Use «a clear title or heading that summarizes the purpose of a page, or» «other clear signposts that have been tested by users with cognitive and learning disabilities».
Use: «Page headings that tell the user where they are.»
SP: "A clear heading at the top of each page shows clearly what the page is about and what they are doing."; "Headings clarify the purpose of this specific page."

Make It Easy to Find Help and Give Feedback (o7p05-findable-support/) — note the full title.
User need: «I need to get help and give feedback easily from every place where I get stuck.»
What to do: «Make it easy for the user to ask for help or report issues at any point in a process.»
How it helps: «If users cannot give feedback easily, problems will continue to exist without the site owner being aware of the problems.»
More details: «Providing multiple methods for gathering feedback is recommended.» Use: «Simple feedback mechanisms that are available on each screen.» Avoid: «A single way to give feedback that not everyone can use.» SP: "Note that chat bots may not be appropriate for this particular type of feedback other than to start the feedback process."

On data, graphs and visual presentation — Provide Alternative Content for Complex Information and Tasks (o7p02-alternative-content/)
User need: «I need contextually-relevant graphs and pictures to supplement text.» — the user need asks FOR graphs.
What to do: «Provide content that helps users understand complex information.» SP list includes "tables and charts", "pictures and informational graphics, and alternatives for numeric content".
How it helps: «The use of complex information, long documents, and complex data formats can present significant barriers». «The way information is presented, such as a graph, diagram, or table, may make it more complex for some users» «a supporting description and guided interpretation will highlight the key features the user needs to understand» (the reader gave the second sentence as beginning "Here,"). Examples of help: «A supporting chart or graph to illuminate text content.» «A supplemental table, that is not complex.»
More details: «Charts or graphics are provided where they aid the comprehension of complex information» «Tables are provided where they aid the comprehension of information».
Avoid: «Complex information and numeric information without extra support.» For example: «A long text and data table of sales figures is shown without any explanation of the key features».

Also read, SP only: Use Familiar Metrics and Units (o4p12; "The Eiffel Tower is 1,063 feet (324 meters) tall, including the antenna at the top."); Let Users Control When the Content Moves or Changes (o8p01; user need "I need to know where things are. Controls and content do not move unexpectedly as I am using them.").

=====================================================================
A7. WCAG 3.0
- Latest draft: «W3C Working Draft 10 September 2026» SV (https://www.w3.org/TR/wcag-3.0/; this version https://www.w3.org/TR/2026/WD-wcag-3.0-20260910/ SP). Earlier 2026 draft: 3 March 2026 (SP, history page). First Public Working Draft 21 January 2021 (SP).
- Status, SV: «It is inappropriate to cite this document as other than a work in progress.» «This is an update to W3C Accessibility Guidelines (WCAG) 3.0» (continues, SP: "It includes all requirements that have reached the developing status." "Requirements and assertions at the Exploratory status are not included in this Working Draft.").
- Abstract, SV: «W3C Accessibility Guidelines (WCAG) 3.0 will provide a wide range of recommendations for making web content more accessible to users with disabilities.»
- Relation to WCAG 2, SV: «but does not deprecate WCAG 2» (full sentence as returned: "WCAG 3 is a successor to Web Content Accessibility Guidelines 2.2 [WCAG22] and previous versions, but does not deprecate WCAG 2."); «WCAG 2 is used around the world and will still be required by different countries for a long time to come»; «Content that conforms to WCAG 2.2 Level A and Level AA is expected to meet most of the minimum conformance level of this new standard».
- Image alternatives ("Images and Media"): guideline «Users have equivalent alternatives for images.» SV. Requirements: «Text alternatives are available for non-decorative images.» SV; «Text alternatives for non-decorative images convey the equivalent purpose to the image.» SV; «Decorative images are programmatically hidden.» SV; "Non-decorative images are detectable." (SP). All labelled Developing (SP).
- Data visualisation, images of text, long description: in the text I could see (truncated inside "Text and Wording"), zero occurrences of graph, visualization, diagram, map, image(s) of text, long description, complex (SP). One occurrence of "chart", in a list about descriptive transcripts: "actions, charts or informative visuals, scene changes, on-screen text" (SP). I cannot report on the unread remainder.
- W3C's statement that WCAG 2 remains the standard to meet (https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/, "Updated: 25 September 2026" SP), all SV: «Many aspects of W3C Accessibility Guidelines (WCAG) 3 Draft are in an exploratory or developing phase and will change substantially.» «The final requirements in WCAG 3 will be different from this draft.» «WCAG 3 is not expected to be a completed W3C standard for a few more years.» «WCAG 3 will not supersede WCAG 2 and WCAG 2 will not be deprecated for several years after WCAG 3 is finalized.» «The best way to prepare for WCAG 3 in the future, is to meet WCAG 2.2 success criteria now.»

=====================================================================
A8. MOTION
- Media Queries Level 5: «W3C Working Draft, 19 February 2026» SV (https://www.w3.org/TR/mediaqueries-5/; this version https://www.w3.org/TR/2026/WD-mediaqueries-5-20260219/ SV). Contents entry «Detecting the desire for less motion on the page: the prefers-reduced-motion feature» SV, section 12.1 (SP).
- THE DEFINITION TEXT WAS NOT REACHABLE AT SOURCE. Tried the TR page, the 2020 First Public Working Draft, the CSSWG editor's draft and the raw GitHub source; all cut before the section. I quote nothing from the spec's definition. It needs a human read of section 12.1.
- Second-hand only: w3c/csswg-drafts issue #5594 (https://github.com/w3c/csswg-drafts/issues/5594, closed). The issue quotes the then-current prose «The prefers-reduced-motion media feature is used to detect if the user has requested the system minimize the amount of animation or motion it uses.» SV as present in the issue. It proposes «Indicates that user has notified the system that they prefer an interface that removes or replaces the types of motion-based animation that trigger discomfort for those with vestibular motion disorders.» SV as present in the issue. Editor's closing comment «I've included the rephrasings suggested by / discussed with @cookiecrook» SV. This is an issue thread quoting and proposing spec text, not the spec; the old "reduce" value wording did not string-verify and is not given.
- WCAG's handling: Technique «C39: Using the CSS prefers-reduced-motion query to prevent motion» SV, Sufficient for «2.3.3 Animation from Interactions» SV (https://www.w3.org/WAI/WCAG22/Techniques/css/C39). «Some users experience distraction or nausea from animated content.» SV. «Media queries that selectively enable/disable CSS-driven animations based on operating system or user agent preferences allow users to avoid those triggers.» SV. Also SCR40 "Using the CSS prefers-reduced-motion query in JavaScript to prevent motion" (SP). The C39 page states techniques "are not required to meet WCAG" (SP).
- 2.2.2 exceptions (five seconds; essential; preload note) and 2.3.3 text: see A2.
- No dedicated WAI page on animation or motion was found beyond these and COGA pattern o8p01.

=====================================================================
A9. EN 301 549
What it is: European Standard by CEN, CENELEC and ETSI; harmonised standard under the Web Accessibility Directive.

V3.2.1 — the version currently carrying legal effect
- Cover: "EN 301 549 V3.2.1 (2021-03) HARMONISED EUROPEAN STANDARD", "Accessibility requirements for ICT products and services" (SP, ETSI PDF https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf, cut at clause 5).
- ETSI page (https://www.etsi.org/human-factors-accessibility/en-301-549-v3-the-harmonized-european-standard-for-ict-accessibility): «EN 301 549 is a harmonised standard» SV (continues, SP, "that supports the European Directive 2016/2102 on the accessibility of the websites and mobile applications of public sector bodies"); «The latest version of EN 301 549 V3.2.1 was published in 2021» SV (continues, SP, "and officially supports the Web Accessibility Directive since August 2021"); «Commission Implementing Decision (EU) 2021/1339» SV. The page is stale: it still says "EN 301 549 will be revised with the aim to publish V4.1.1 in 2025" (SP).
- Foreword, SP: "...prepared under the Commission's standardisation request C(2017)2585 final to provide...one voluntary means of conforming to the essential requirements of Directive 2016/2102".
- Clause 9 (Web), read via Accessibility Standards Canada's HTML of CAN/ASC - EN 301 549:2024 (EN 301 549:2021, IDT) — https://accessible.canada.ca/standards-and-technical-guides/standards-and-technical-guides-database/can-asc-en-301-5492024-accessibility-requirements-ict-products-and-services-en-301-5492021-idt/9-web . Secondary host of the identical text:
 9.0 General (informative): «Requirements in clause 9 apply to web pages (as defined in clause 3.1)» SV. «Conformance with W3C Web Content Accessibility Guidelines (WCAG 2.1) Level AA is equivalent to conforming with all of clauses 9.1 to 9.4 and the conformance requirements of clause 9.6» SV. «When evaluating web sites they are evaluated as individual web pages.» SV. «It is not recommended that Level AAA conformance be required as a general policy for entire sites» SV.
 9.6 WCAG conformance requirements: «Where ICT is a web page, it shall satisfy all the following five WCAG 2.1 conformance requirements at Level AA» SV. Note 1, SP: "A Web page that meets all of requirements 9.1 to 9.4, or where a Level AA conforming alternate version (as defined in WCAG 2.1) is provided, will meet conformance requirement 1."
 Incorporation pattern: «Where ICT is a web page, it shall satisfy WCAG 2.1 Success Criterion 1.4.5 Images of Text» SV. No WCAG 2.2 criteria in V3.2.1 (the control for 2.5.8 was absent).

V4.1.1 — exists; published September 2026
- ETSI PDF https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf : «EN 301 549 V4.1.1 (2026-09)» SV; «HARMONISED EUROPEAN STANDARD» SV; «Directive (EU) 2019/882» SV; «C(2022) 6456 final» SV; «M/587» SV; «WCAG 2.2» SV; «24 August 2026» SV (date of adoption). SP Foreword: "The present document has been prepared under the Commission's standardisation request C(2022) 6456 final [i.28] to provide one voluntary means of conforming to the essential requirements of Directive (EU) 2019/882 on the accessibility requirements for products and services"; "the requirements of clauses 9, 10 and 11 have all been updated to align with the WCAG 2.2 recommendation"; presumption wording «a presumption of conformity with the corresponding essential requirements» SV. SP transposition table: latest announcement 30 November 2026; latest publication or endorsement 31 May 2027; withdrawal of conflicting national standards 31 May 2028. SP contents list: "9.5 WCAG 2.2 AAA Success Criteria (informative)", "9.6 WCAG conformance requirements", "9.7 User preferences for web pages". Clause 9 body text not reachable.
- Legal status as of the AccessibleEU notice dated «7 September 2026» SV (https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en; AccessibleEU, a European Commission initiative): «A new version of the European accessibility standard, EN 301 549 v4.1.1, was published in September 2026.» SV. «The new version is not yet the legal reference standard for demonstrating compliance with the European Accessibility Act (EAA) or the EU Web Accessibility Directive (WAD).» SV. "Until the European Commission formally cites EN 301 549 v4.1.1 in the Official Journal of the European Union," «the current reference remains EN 301 549 v3.2.1 (2021)» SV ", which is based on WCAG 2.1 Level AA." «it adopts WCAG 2.2 as the accessibility benchmark» SV. I did not check the Official Journal for a citation after 7 September 2026.
- UK position: not researched (Agent B). The EN's own text is EU-facing and says nothing about the UK.
- W3C on the link (press release 21 October 2025, https://www.w3.org/press-releases/2025/wcag22-iso-pas/): «ISO/IEC 40500:2025 is the October 2023 version of WCAG 2.2» SV; next sentence SP: "W3C is working to get ISO/IEC 40500 and EN 301 549 updated with the latest version of WCAG 2.2."

=====================================================================
A10. W3C DATA-VISUALISATION EFFORTS
Plainly: THERE IS NO W3C RECOMMENDATION, NOTE OR WAI GUIDANCE DOCUMENT ON CHARTS OR DATA VISUALISATION. What exists:
- Accessible Infographics Community Group (https://www.w3.org/groups/cg/infographics/): «The goal of the Accessible Infographics CG is to make information graphics, like bar charts and maps, as accessible as possible to all.» SV; plan included «to devise and propose additions to SVG that improve accessible options for data in that and other graphics formats» SV. Status: "The Accessible Infographics Community Group was closed on 7 April 2023." (sentence SP; «7 April 2023» and «closed» SV). No published report found. Call for participation dated 6 December 2011 (from URL only).
- Data Visualization Community Group (https://www.w3.org/groups/cg/datavis/): «The mission of this group is to provide a unified data model for data visualization» SV; "The Data Visualization Community Group was closed on 7 December 2023." (sentence SP; «7 December 2023» SV). The word "accessibility" does not appear in its description. The "closed 2023" memory in the brief matches both groups; only the Infographics group was about accessibility. No group named "Visualization Accessibility Community Group" was found.
- The chart-role proposal: W3C wiki "SVG Accessibility/ARIA roles for charts" (https://www.w3.org/wiki/SVG_Accessibility/ARIA_roles_for_charts): «A proposed system of roles and properties for using ARIA to annotate charts, graphs, and maps.» «Builds upon the basic ARIA roles for graphics.» SV. Proposed roles include «graphics-datachart», «graphics-axis», «graphics-legend», «graphics-dataunit» (SV); also graphics-map, graphics-network, graphics-datagroup, graphics-dataline, graphics-dataregion, graphics-connector, graphics-tick (SP). graphics-datachart, as the reader returned it on verification: "A data chart is a type of graphical document in which graphical features (layout, color, shape, etc.) reflect values in a data set." (SP for the parenthesis). Footer «This page was last edited on 11 September 2015» SV. Parent wiki page last edited 24 March 2017 (SP).
- Its fate: only the three generic roles reached Recommendation (Graphics Module, 2 October 2018), which says «Future work will expand on this framework to enable more detailed annotation of data-rich graphics such as charts or maps.» SV. A November 2019 list message from a student, Christopher-A. Kopel (https://lists.w3.org/Archives/Public/public-svga11y/2019Nov/0000.html, SP), calls it "the proposed system 'ARIA Roles for Charts' - still only a Wiki since 2015" and asks "Is it still meant to become a standard, or has it been dismissed in the meantime?" I did not find a W3C reply.
- Current ARIA Working Group charter (https://www.w3.org/WAI/ARIA/charter): start «12 December 2024», end «1 January 2027» SV. Lists the Graphics Module («This specification defines a WAI-ARIA 1.1 module of core roles specific to web graphics.» SV), Graphics Accessibility API Mappings, and «SVG Accessibility API Mappings» SV (Working Draft, joint with the SVG Working Group, SP). The words "chart" and "data visualization" do not appear in the charter (both reported absent). ARIA WG publications page (SP): SVG Accessibility API Mappings Working Draft 27 August 2026.
- WAI: no "Accessible Data Visualization" page. The Images Tutorial index lists only Informative, Decorative, Functional, Images of Text, Complex Images, Groups of Images, Image Maps, a decision tree and tips (SP). "What We're Working On" (updated 28 August 2026) does not mention charts, graphs, maps or data visualisation (SP).

=====================================================================
UNDERSTANDING PAGES THAT MENTION MAPS (beyond 1.4.10 and 2.5.8)
- 1.4.10 Reflow: «Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content.» SV. «A section of content that requires two-dimensional layout for understanding or functionality, such as a table or map, has an exception to this success criterion.» SV. «Graphics and video are by their nature two-dimensional.» SV. Limit on the exception: «Other content that is related to the table or grid, such as a preceding heading, a search field, or an accompanying pagination to load different sets of data are not excepted from meeting Reflow.» SV. SP: "Slicing up a graphic (photograph, drawing, graph, etc.) and stacking the blocks would make the graphic difficult to understand, if not rendering it unintelligible."
- 2.5.8 Target Size (Minimum): «It is essential to show the pins at the correct map location, therefore the Essential exception applies.» SV. «A similar example is an interactive data visualization where targets are necessarily dense.» SV — the one Understanding sentence found that names "data visualization". SP: "If the size and spacing of the targets is fundamental to the information being conveyed, the 'Essential' exception applies."
- 2.5.7 Dragging Movements: «A map allows users to drag the view of the map around, and the map has up/down/left/right buttons to move the view as well.» SV.
- 1.4.11: «Color gradients that represent a measurement, such as heat maps.» SV.
- 2.5.1 Pointer Gestures: no sentence with map, chart or graph (SP).
- 1.4.1 Use of Color: "A legend shows the color and number for each type of element." (SP); technique "G111: Using color and pattern" (SP).
- 2.1.1 Keyboard: no map mention; SP "Free hand drawing, or watercolor painting require path dependent input."
- 1.1.1: "image maps" only as a control type (SP).

=====================================================================
UNASKED THREADS
1. WCAG 2.2 is now an ISO standard: «W3C Web Content Accessibility Guidelines 2.2 approved as ISO/IEC international standard», «21 October 2025», «ISO/IEC 40500:2025» — all SV. It is the October 2023 text, not the December 2024 republication.
2. The Complex Images tutorial was revised («Updated 08 April 2026»): three approaches, no longdesc, example year 2025. Earlier chapters citing "four approaches" or longdesc are citing a superseded page.
3. Understanding 1.4.5 states that image text duplicated as real text, «where both are presented to the user», meets the criterion. The AAA 1.4.9 page has no such sentence.
4. COGA is not anti-chart: one of its user needs is «I need contextually-relevant graphs and pictures to supplement text.» Its "Avoid" example is a data table with no explanation.
5. G92 gives two worked long descriptions for charts: one prose-only, ordered by the chart's purpose; one that «includes the data table that was used to generate the line graph».
6. ariaNotify: a sufficient technique for 4.1.3 (ARIA27) exists but is self-described as experimental «As of April 2026».
7. 4.1.3 excludes the results themselves; only the brief message about them is a status message. The same page warns against "chatty" live regions and says to user-test.
8. 1.4.12 treats canvas text as images of text and does not mention SVG; it does not apply to PDF.

LEFT OUT (and why)
- The normative aria-live value table, ARIA 1.2 role body text, COGA Note sections after 4.3.3, WCAG 3.0 beyond "Text and Wording", EN 301 549 V4.1.1 clause 9 body, and the prefers-reduced-motion definition — all cut by the fetch tool. None is quoted.
- WCAG 2.2 normative text direct from /TR/ for criteria after 2.5.8 (3.2.1, 3.2.2, 3.3.2, 4.1.2, 4.1.3) and for the conformance section and glossary — taken from Understanding pages.
- 3.3.1, 3.3.3 and 3.3.7 — judged not relevant to a filter form.
- Official Journal check for a V4.1.1 citation; EUR-Lex text of Decision (EU) 2021/1339; the UK position (Agent B).
- Graphics-AAM and SVG-AAM content; SVG a11y task force minutes (2014–2015).
- C22 description sentences are SP only.

RICH REFERENCES
1. Understanding SC 1.4.5 Images of Text — https://www.w3.org/WAI/WCAG22/Understanding/images-of-text — the Intent's last paragraphs decide the chart-image question in W3C's own words.
2. Understanding Conformance, "Why permit alternate versions?" — https://www.w3.org/WAI/WCAG22/Understanding/conformance — the «fallback option» sentence and the passage on a hard-copy format treated as the "primary" version.
3. COGA pattern "Provide Alternative Content for Complex Information and Tasks" — https://www.w3.org/WAI/WCAG2/supplemental/patterns/o7p02-alternative-content/ — read with G92 (https://www.w3.org/WAI/WCAG22/Techniques/general/G92).

SURPRISED
- "Last resort" is not W3C's phrase. The page says «fallback option» and «preferred method».
- The Graphics Module has been a full Recommendation since 2 October 2018, and still says chart annotation is «Future work». The chart-roles wiki has not been edited since 11 September 2015. Both W3C community groups in this area closed in 2023.
- EN 301 549 V4.1.1 (2026-09) is published and aligned to WCAG 2.2, but per AccessibleEU on 7 September 2026 it is not yet the legal reference; V3.2.1 with WCAG 2.1 still is.
- WCAG 2.1's current status line is 06 May 2025.
- WAI's own long-description example appears to contain an arithmetic slip: the table (read twice, SP) gives Site 3 as Jan 92, Feb 99, March 126, Qtr total 308; those months sum to 317. Check by eye before using it.
- The reader fabricated ARIA role definitions on a first pass when the section was outside its window; presence checks caught it.

WEBSEARCH CALLS USED: 7 (of 30).

---

## Agent B

AGENT B REPORT — THE UK LEGAL FRAME FOR WEB ACCESSIBILITY
All fetches made 6 October 2026. WebSearch calls used: 15 of 30. Marking: SV = STRING-VERIFIED (second fetch with YES/NO presence prompt, false controls included and correctly rejected); SP = SINGLE PASS. Law is reported as written; nothing here is advice.

CORRECTION TO THE BRIEF'S NUMBERING (matters for citation). In S.I. 2018/952 as it stands: reg 1 citation/commencement; reg 2 REVOCATION (of S.I. 2018/852); reg 3 Interpretation (definitions); reg 4 Application (body exemptions 4(1), content exemptions 4(2), definitions 4(3) — there is no 4(4)); reg 5 Application of Part 2 (the dates); reg 6 the duty; reg 7 disproportionate burden; reg 8 accessibility statement; reg 9 presumed conformity; reg 10 monitoring/reporting; reg 11 enforcement bodies; reg 12 "Failure to make a reasonable adjustment"; reg 13 notification; reg 14 statement enforcement. "Harmonised standards" no longer appears anywhere in the text.

B1. THE 2018 (No. 2) REGULATIONS, S.I. 2018/952
Source: https://www.legislation.gov.uk/uksi/2018/952/regulation/N (each reg fetched separately). Version shown: "Latest available (Revised)"; regs 3, 10, 13, 14 show version date 3.6.2025. Banner on every page: "There are currently no known outstanding effects for The Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018" (SP, consistent across 14 pages). Extent marker "U.K." Type: law (secondary legislation).

Reg 1(2): "These Regulations come into force on 23rd September 2018." (SP)
Reg 3 defined terms now are only: accessibility requirement; accessibility statement; bodies governed by public law; mobile application; model accessibility statement; public sector body; time-based media. NOT defined: "website", "non-governmental organisation" (SV: both absent).
- "“accessibility requirement” means the requirement to make a website or mobile application accessible by making it perceivable, operable, understandable and robust" (SV)
- "“public sector body” means— (a) the State; (b) regional or local authorities; (c) bodies governed by public law; or (d) associations formed by one or more of the authorities in paragraph (b) or one or more of the bodies in paragraph (c), if those associations are established for the specific purpose of meeting needs in the general interest, not having an industrial or commercial character" (SV for opening, (a), (b), (d); (c) SP)
- "bodies governed by public law" = bodies with ALL of: "(a) they are established for the specific purpose of meeting needs in the general interest, not having an industrial or commercial character; (b) they have legal personality; and (c) they have any of the following characteristics— (i) they are financed, for the most part, by the State, regional or local authorities, or by other bodies governed by public law; (ii) they are subject to management supervision by those authorities or bodies; (iii) they have an administrative, managerial or supervisory board, more than half of whose members are appointed by the State, regional or local authorities, or by other bodies governed by public law" (SV for (a), (b), (c)(i); (ii)–(iii) SP). This "financed, for the most part" limb is the only "funded" route by which a private body enters the definition; there is no separate NGO limb in the definition — the NGO wording is an exemption in reg 4(1)(b).
- "“mobile application” means application software designed and developed by or on behalf of a public sector body for use by the general public on mobile devices such as smartphones and tablets" (SV)
- "“model accessibility statement” means an accessibility statement [F2 published electronically by the [F3 Secretary of State]]" (SV, with amendment markers)

Reg 4(1) (SV all limbs): "These Regulations apply to a website or mobile application of a public sector body, except a website or mobile application of— (a) public service broadcasters and their subsidiaries, and of other bodies or their subsidiaries fulfilling a public service broadcasting remit; (b) non-governmental organisations, unless they provide services that— (i) are essential to the public; or (ii) specifically address the needs of, or are meant for, persons with disabilities; and (c) schools or nurseries, except for the content of their websites or mobile applications relating to essential online administrative functions."
Reg 4(2) — EVERY content exemption (SV all): "These Regulations do not apply to the following content of a website or mobile application of a public sector body—
(a) office file formats published before 23rd September 2018, unless such content is needed for active administrative processes relating to the tasks performed by the public sector body;
(b) pre-recorded time-based media published before 23rd September 2020;
(c) live time-based media;
(d) online maps and mapping services, as long as essential information is provided in an accessible digital manner for maps intended for navigational use;
(e) third-party content that is neither funded nor developed by, nor under the control of, the public sector body;
(f) reproductions of items in heritage collections that cannot be made fully accessible because of either— (i) the incompatibility of the accessibility requirement with either the preservation of the item concerned or the authenticity of the reproduction; or (ii) the unavailability of automated and cost-efficient solutions that would easily extract the text of manuscripts or other items in heritage collections and transform it into content compatible with the accessibility requirement; [(f)(i)–(ii) SP]
(g) content of extranets and intranets published before 23rd September 2019, until such websites undergo a substantial revision; and
(h) content of websites and mobile applications qualifying as archives."
The third-party exemption is letter (e) and its exact wording is "third-party content that is neither funded nor developed by, nor under the control of, the public sector body" (SV). The brief's wording "content of third parties that is…" does NOT appear (SV negative). No amendment annotations on reg 4.
Reg 4(3)(a): "“archives” means a website or mobile application which— (i) only contains content that is not needed for active administrative processes; and (ii) is not updated or edited after 23rd September 2019" (SV). 4(3)(b)–(d) define extranets/intranets, items in heritage collections, office file formats (SP).

Reg 5 (SV): "This Part applies as follows— (a) for a website of a public sector body published on or after 23rd September 2018, after 22nd September 2019; (b) for any other website of a public sector body, after 22nd September 2020; and (c) for a mobile application of a public sector body, after 22nd June 2021." (i.e. from 23 Sept 2019 / 23 Sept 2020 / 23 June 2021.)
Reg 6 (SV): "Subject to regulation 7, public sector bodies must comply with the accessibility requirement."
Reg 7 (SV for (1), (2), (3)(a), (3)(b), (4)(a); (4)(b) SP): "(1) Regulation 6 does not require a public sector body to comply with the accessibility requirement if doing so would impose a disproportionate burden on the public sector body. (2) A public sector body must perform an assessment of the extent to which compliance with the accessibility requirement imposes a disproportionate burden. (3) In undertaking such an assessment, a public sector body must take account of relevant circumstances, including— (a) the size, resources and nature of the public sector body; and (b) the estimated costs and benefits for the public sector body in relation to the estimated benefits for persons with disabilities, taking into account the frequency and duration of use of the specific website or mobile application. (4) If, following the assessment, a public sector body determines that compliance with the accessibility requirement would impose a disproportionate burden, it must— (a) explain in its accessibility statement the parts of the accessibility requirement that could not be complied with; and (b) where appropriate, provide accessible alternatives to documents held by that public sector body that are not available on their website or mobile application." ("lack of priority, time or knowledge" is NOT in the regulation — SV negative; it is guidance, see B2.)
Reg 8 (SV for (1), (4)(a), (b), (c)(ii), (d)): "(1) A public sector body must provide an accessibility statement in accordance with the model accessibility statement, and keep that statement under regular review." "(4) The accessibility statement must include— (a) an explanation of those parts of the content that are not accessible and the reasons why; (b) where appropriate, a description of any accessible alternatives provided; (c) a description of, and a link to, a contact form which enables a person to— (i) notify the public sector body of any failure of its website or mobile application to comply with the accessibility requirement; and (ii) request details of the information excluded under regulation 4(2) and regulation 7(4); and (d) a link to the enforcement procedure set out in Part 5 of these Regulations to which recourse may be had in the event of an unsatisfactory response to the notification or the request." No annual-update wording in the regulation (SV negative).
Reg 9 (Part 3, presumed conformity; substituted 26.10.2022) (SV): "A website or mobile application of a public sector body will be presumed to be in conformity with the accessibility requirement to the extent that the website or mobile application conforms to Level A and AA Success Criteria as set out in the Web Content Accessibility Guidelines recommended by the World Wide Web Consortium, as amended from time to time." No version number ("2.1"/"2.2"), no "EN 301 549", no "harmonised standards" in the text (SV negatives). Annotation: "Reg. 9 substituted (26.10.2022) by The Public Sector Bodies (Websites and Mobile Applications) Accessibility (Amendment) (EU Exit) Regulations 2022 (S.I. 2022/1097), regs. 1(2), 4" (SV).
Reg 10 (SP, with markers): "(1) The [F1 Secretary of State] must monitor the compliance by public sector bodies of their websites and mobile applications with the accessibility requirement, on the basis of the monitoring methodology." "(2) By no later than 23rd December [F2 2024], and every three years thereafter, the [F3 Secretary of State] must [F4 publish a report] on the outcome of the monitoring referred to in paragraph (1), including the measurement data." "(5) … “monitoring methodology” means a methodology [F6 published by the [F7 Secretary of State] and as amended from time to time]." Para (3) omitted 26.10.2022.
Reg 11 (SV): "Subject to regulation 14, the enforcement bodies are— (a) for a website or mobile application of a public sector body that is required to comply with the Equality Act 2010, the Equality and Human Rights Commission; (b) for a website or mobile application of a public sector body that is required to comply with the Disability Discrimination Act 1995, the Equality Commission for Northern Ireland."
Reg 12 "Failure to make a reasonable adjustment" — the link to the Equality Act (SV all): "(1) A failure by a public sector body to comply with the accessibility requirement is to be treated as a failure to make a reasonable adjustment. (2) A failure by a public sector body to provide a satisfactory response to a request to provide information in an accessible format, pursuant to regulation 13(2) (right to request information in an accessible format), is to be treated as a failure to make a reasonable adjustment. (3) A “failure to make a reasonable adjustment” in this regulation means a failure to make a reasonable adjustment for the purposes of— (a) sections 20, 21 and 29 of the Equality Act 2010; or (b) sections 19 to 21 and 21B to 21E of the Disability Discrimination Act 1995." The phrase "a failure to comply with a duty under" the Equality Act is NOT the wording; the mechanism is "is to be treated as a failure to make a reasonable adjustment".
Reg 13 (SV (1)–(4)): "(2) A person may request information in an accessible format that has been excluded from a website or mobile application of a public sector body pursuant to regulation 4(2) or regulation 7(4)." "(3) A public sector body must provide a response … within a reasonable period of time." "(4) … that person may complain to the applicable enforcement body."
Reg 14 (SP): statement compliance is assessed by the Secretary of State, who "must publish the name of the public sector body and the determination of the Secretary of State electronically" if a non-compliance determination is upheld (14(12)).

Amending instruments:
(i) S.I. 2022/1097, The Public Sector Bodies (Websites and Mobile Applications) Accessibility (Amendment) (EU Exit) Regulations 2022. "Made 25th October 2022"; "Coming into force 26th October 2022" (SV). https://www.legislation.gov.uk/uksi/2022/1097/made. It: omitted definitions of "the Directive", "European standard", "harmonised standard", "Official Journal", "standard"; made the model statement one "published electronically by the Minister for the Cabinet Office" (SV); substituted reg 9; in reg 10(2) "For “2021” substitute “2024”" and replaced "submit a report to the European Commission" with "publish a report" (SV); omitted reg 10(3); "Omit the Schedule to the 2018 Regulations" (SV); revoked Commission Implementing Decisions 2018/1523, 2018/1524, 2018/2048 (SP). Explanatory Note: "Regulation 4 substitutes for the European accessibility standard (EN 301 549) the international web accessibility standard as the standard that a public sector body's website or mobile application must meet to be presumed to be in conformity with the accessibility requirement." (SP)
(ii) NOT IN THE BRIEF: The Transfer of Functions (Digital Government) Order 2025 (S.I. 2025/557), arts. 1(2), 9 — from 3.6.2025 substituted "Secretary of State" for the Minister for the Cabinet Office in regs 3, 10, 14 (annotations SP on reg 10; consistent on regs 3, 14).
Explanatory Memorandum to S.I. 2018/952 (https://www.legislation.gov.uk/uksi/2018/952/pdfs/uksiem_20180952_en.pdf): the No. 2 Regulations revoke S.I. 2018/852 "due to drafting errors in that instrument" (SV, para 2.2); "The territorial extent of this instrument is the United Kingdom." (SV, para 4.1); the EM does not explain what "funded" means in the third-party exemption (checked).
Origin of reg 4(2)(e): Directive (EU) 2016/2102 Art 1(4)(e) "third-party content that is neither funded nor developed by, nor under the control of, the public sector body concerned" (SV) and recital 30 — see B9.
Role: the hard line for public bodies; a private studio is not a "public sector body" unless it meets the reg 3 "body governed by public law" test.

B2. GOV.UK GUIDANCE AND MONITORING
(a) "Understanding accessibility requirements for public sector bodies", GDS and CDDO, published 9 May 2018, "Last updated: 30 September 2024" (SV; no later date present). https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps. Type: government guidance. Update note: "30 September 2024 Section about when GDS is monitoring the new success criteria in WCAG 2.2 and some references to 2018 for accessibility regulations has been removed." (SP). The string "October 2024" does not appear on this page (SV negative).
- WCAG version: "Your website or mobile app will meet the legal requirements if you:" / "meet the Web Content Accessibility Guidelines (WCAG) 2.2 AA accessibility standard - although there may be valid legal reasons for not meeting accessibility standards" / "publish an accessibility statement that explains how accessible your website or mobile app is" (SV for the two WCAG fragments).
- Third-party content, under "Things you might not need to fix": "third party content that's under someone else's control if you did not pay for it or develop it yourself - for example, social media 'like' buttons" (SV). This is the "content you pay for" sentence. Followed by: "You'll need to explain in your accessibility statement that you've not made things like this accessible because they are exempt." (SV). Maps: "maps - but you'll need to provide essential information in an accessible format like an address" (SV).
- Who: "All public sector bodies have to meet the requirements, unless they are exempt." "Public sector bodies include: central government and local government organisations; some charities and other non-government organisations" (SP). "All UK service providers have a legal obligation to make reasonable adjustments under the Equality Act 2010 or the Disability Discrimination Act 1995 (in Northern Ireland)." (SP). Exempt: "non-government organisations like charities - unless they are mostly financed by public funding, provide services that are essential to the public or aimed at disabled people" (SV). "Partially exempt organisations would need to publish an accessibility statement on their website or mobile app." (SV)
- Disproportionate burden: "You need to think about disproportionate burden in the context of what's reasonable to do right now." (SP) "If you want to declare that making particular things accessible is a disproportionate burden, you're legally required to carry out an assessment." (SP) "You cannot take things like lack of time or knowledge into account in your assessment - or argue that making things accessible is a disproportionate burden because you've not given it priority." (SV first clause)
- Outsourcing/procurement: "If you've outsourced some or all of your website or app to a supplier, you'll need to work together to make sure your website or app meets the accessibility regulations." "make meeting accessibility standards in procurement part of the request for quotation (RFQ)"; "include accessibility as part of the contract evaluation" (SP).
- Convergence sentence useful to the chapter: "Accessible websites usually work better for everyone." (SV) "They are often faster, easier to use and appear higher in search engine rankings." (SP)
- Enforcement: "Organisations that do not meet the accessibility requirement or fail to provide a satisfactory response to a request to produce information in an accessible format, will be failing to make reasonable adjustments." "The EHRC and ECNI can therefore use their legal powers against offending organisations, including investigations, unlawful act notices and court action." (SP). Page still says GDS monitors "on behalf of the Minister for the Cabinet Office" (SP) — out of step with S.I. 2025/557.
(b) "Public sector website and mobile application accessibility monitoring", GDS, published 20 Aug 2020, last updated 30 Sept 2024 (SV). https://www.gov.uk/guidance/public-sector-website-and-mobile-application-accessibility-monitoring
- "The technical standard for websites and mobile apps is level AA of the Web Content Accessibility Guidelines (WCAG) version 2.2." (SV)
- Section "Third party content" in full (SV all three): "If you have funded, developed or are in control of third party content, it is your responsibility to make sure that it is accessible." "We understand that third party content may be harder to change." "You should make sure your accessibility statement is updated to include any issues users may experience when using third party content on your website."
- Method: "We test pages using an automated accessibility tool called Axe." (SV) "Automated testing does not find all accessibility issues." (SV) Manual tests: "tabbing through each page without a mouse"; "viewing the page at different zoom settings"; "simulating viewing the page on a small device like a mobile phone" (SP). "Manual tests can find issues with keyboard functionality, visibility of keyboard focus and reflow. These are common barriers to users with accessibility needs and are unlikely to be found using automated testing." (SP) "Simplified tests do not show every accessibility error and only a sample of pages is tested." (SV) Simplified: "we choose some core pages, like the home page, alongside a sample of other pages chosen from across the site. The number will vary depending on the size of the website." (SP — no fixed sample size is stated.) Detailed: "They test against the full range of WCAG success criteria up to level AA. Assistive technology is used to check compliance as well as the automated and manual methods used in simplified testing." (SP) "fix accessibility issues within 12 weeks" (SV). Disproportionate burden: "The assessment is a financial cost/benefit exercise and should consider things like:" (SV) including "if the site or service is procured or outsourced, how long the third party supplier is contracted for, and how much it would cost to re-tender or renegotiate the contract to fix accessibility issues" (SP).
(c) Latest monitoring report: "Accessibility monitoring of public sector websites and mobile apps from 2022 to 2024", GDS, "Published 17 December 2024" (SV). https://www.gov.uk/government/publications/accessibility-monitoring-of-public-sector-websites-and-mobile-apps-from-2022-to-2024/accessibility-monitoring-of-public-sector-websites-and-mobile-apps-from-2022-to-2024. Type: official practice/monitoring data. Period January 2022 to September 2024.
- "We have monitored 1,203 websites and 21 mobile apps during this monitoring period." (SV) (1,151 simplified + 52 detailed — SP.)
- "Accessibility issues were found on nearly all tested websites and apps, similar to the previous monitoring period." (SV) "We found no accessibility issues for 10 websites." (SV, of 1,151 simplified)
- "We found 29,787 accessibility issues across monitored websites and apps." (SV) "Of these, 16,482 (55.3%) were fixed by the public sector organisations during the monitoring." "3,693 issues (12.4%) were not fixed when we retested the website or app." (SP)
- "68% had fixed the issues found or had short-term plans for when the remaining issues would be fixed. This is a slight increase from the previous monitoring period (59%)." (SP)
- Commonest failures, simplified tests, share of issues: 2.4.7 Focus Visible 13.3%; 1.4.3 Contrast (minimum) 13.0% (both SV); 2.1.1 Keyboard 10.8%; 1.4.10 Reflow 9.2%; 4.1.2 Name, Role, Value 8.6%; 1.3.1 6.4%; 2.4.4 6.2%; 1.4.4 5.5%; 2.4.3 4.0%; 1.1.1 3.0% (SP). "The 5 most common criteria account for 55% of the total issues, and the 10 most common criteria account for 80%." (SV) Detailed tests top three: 1.4.3 13.8%; 4.1.2 10.8%; 1.3.1 10.8% (SP).
- Executive-summary wording: "The main issues we found during monitoring were: not enough colour contrast between text and the background…; lack of visible focus…; problems using a site or app with a keyboard…; sites that do not adjust to the shape and size of the browser or device (known as 'reflow')…" (SP)
- WCAG 2.2 date (Appendix A): "WCAG 2.2 was published on 5 October 2023 and became the legal technical standard for the accessibility regulations. Our team has been monitoring for this standard since October 2024." (SV second sentence; first SP)
- Automated coverage (Appendix C): "Automated checkers are believed to detect approximately 30-40% of accessibility issues." (SV)
- Statements: "85% of websites and mobile apps had published an accessibility statement when initially monitored." (SP) "After the monitoring process, 97% had published a statement and 65% included all necessary information detailed in the model accessibility statement template." (SV for 65% clause) "many accessibility statements are now out-of-date and have not been reviewed in the last 12 months" (SP).
- Disproportionate burden claims at closure (table): Simplified 17%; Detailed 37%; Mobile app 57% (SV as table figures).
- Third parties: "We also test end-to-end services in depth. These are often provided by third parties and not within an organisation's direct control." (SV, section 6)
- Enforcement: "640 (70% of completed cases) websites were passed to the equality bodies with a recommendation of no further action." (SV) "276 (30%) had a recommendation for equality bodies to consider whether further enforcement was appropriate." (SP) "To date, of the 93 public sector bodies in England and Wales that the EHRC has sent initial letters to since 1 January 2022, compliance was secured with 66, without the need for enforcement, with the remaining matters ongoing." (SV) "The EHRC has a two staged approach to enforcement." (SV) "…this may include entering into a binding agreement to comply with the regulations, or conducting an investigation into the failure to make reasonable adjustments to ensure website accessibility." (SP) "No complaints were received through ECNI" (SP). No fines are mentioned (SV negative).
(d) GDS accessibility blog, Chris Heathcote, 9 December 2022 (https://accessibility.blog.gov.uk/2022/12/09/some-changes-to-the-public-sector-digital-accessibility-regulations/): on WCAG 2.2, "The legislation change means that this will automatically become the standard that is expected for public sector websites and mobile apps." (SV) "The applicability, exemptions and enforcement process all remain the same." (SV) "If you rely on third party code or frameworks, for example the GOV.UK Design System, or have outsourced parts of your websites or apps, you should start a conversation with your providers about what their plans are to support WCAG 2.2." (SV)
(e) Sample accessibility statement — see B7.

B3. EQUALITY ACT 2010 (legislation.gov.uk, "Latest available (Revised)")
Banner (s.29, Sch 2, Sch 25, SV): "Equality Act 2010, Section 29 is up to date with all changes known to be in force on or before 05 October 2026. There are changes that may be brought into force at a future date. Changes that have been made appear in the content and are referenced with annotations." Other pages show the same form with dates 01–05 October 2026. Pending effects listed are from "2025 c. 36" and (per the page) affect ss.40, 40B, 78, 153, 154, 208 — not ss.6, 20, 21, 29 (SP). No textual amendments on ss.6, 20, 21, 29.
s.6(1) (SV): "A person (P) has a disability if— (a) P has a physical or mental impairment, and (b) the impairment has a substantial and long-term adverse effect on P's ability to carry out normal day-to-day activities." https://www.legislation.gov.uk/ukpga/2010/15/section/6
s.212(1): "“substantial” means more than minor or trivial" (SV).
s.20 (https://www.legislation.gov.uk/ukpga/2010/15/section/20): "(2) The duty comprises the following three requirements." (SV) "(3) The first requirement is a requirement, where a provision, criterion or practice of A's puts a disabled person at a substantial disadvantage in relation to a relevant matter in comparison with persons who are not disabled, to take such steps as it is reasonable to have to take to avoid the disadvantage." (SV in fragments) "(4) The second requirement is a requirement, where a physical feature puts a disabled person at a substantial disadvantage … to take such steps as it is reasonable to have to take to avoid the disadvantage." (SP) "(5) The third requirement is a requirement, where a disabled person would, but for the provision of an auxiliary aid, be put at a substantial disadvantage in relation to a relevant matter in comparison with persons who are not disabled, to take such steps as it is reasonable to have to take to provide the auxiliary aid." (SV opening) "(6) Where the first or third requirement relates to the provision of information, the steps which it is reasonable for A to have to take include steps for ensuring that in the circumstances concerned the information is provided in an accessible format." (SV) "(7) A person (A) who is subject to a duty to make reasonable adjustments is not (subject to express provision to the contrary) entitled to require a disabled person … to pay to any extent A's costs of complying with the duty." (SP) "(11) A reference in this section, section 21 or 22 or an applicable Schedule to an auxiliary aid includes a reference to an auxiliary service." (SV)
s.21 (SV all): "(1) A failure to comply with the first, second or third requirement is a failure to comply with a duty to make reasonable adjustments. (2) A discriminates against a disabled person if A fails to comply with that duty in relation to that person." (3) "…a failure to comply is, accordingly, not actionable by virtue of another provision of this Act or otherwise."
s.29(1) (SV): "A person (a “service-provider”) concerned with the provision of a service to the public or a section of the public (for payment or not) must not discriminate against a person requiring the service by not providing the person with the service." s.29(7) (SV): "A duty to make reasonable adjustments applies to— (a) a service-provider (and see also section 55(7)); (b) a person who exercises a public function that is not the provision of a service to the public or a section of the public." s.31(2): "A reference to the provision of a service includes a reference to the provision of goods or facilities." (SP) s.31(6): "A reference to a person requiring a service includes a reference to a person who is seeking to obtain or use the service." (SP)
Schedule 2 para 2 (https://www.legislation.gov.uk/ukpga/2010/15/schedule/2): "(1) A must comply with the first, second and third requirements. (2) For the purposes of this paragraph, the reference in section 20(3), (4) or (5) to a disabled person is to disabled persons generally." (SV both) "(4) In relation to each requirement, the relevant matter is the provision of the service, or the exercise of the function, by A." (SV) "(7) If A is a service-provider, nothing in this paragraph requires A to take a step which would fundamentally alter— (a) the nature of the service, or (b) the nature of A's trade or profession." (SV) "(8) If A exercises a public function, nothing in this paragraph requires A to take a step which A has no power to take." (SP) The word "anticipatory" does NOT appear in Schedule 2 (SV negative); the statutory hook is "disabled persons generally".
Explanatory Notes, Schedule 2, para 676 (https://www.legislation.gov.uk/ukpga/2010/15/notes/division/3/16/19; EN are not law): "This Schedule explains how the duty to make reasonable adjustments in section 20 applies to a service provider or person exercising a public function where a disabled person is placed at a substantial disadvantage. It includes definitions of “substantial disadvantage” and “physical features” and stipulates that the duty does not require fundamental changes to the nature of the service. As the duty is owed to disabled persons generally, it is an anticipatory duty which means service providers and people exercising public functions must anticipate the needs of disabled people and make appropriate reasonable adjustments." (SV for the last sentence from "it is an anticipatory duty"; rest SP.) The word "website" does not appear on that EN page (SV negative).
Role: the duty that reaches a private, non-commercial provider of a service to the public "(for payment or not)".

B4. THE EHRC
MAJOR STATUS FINDING: the 2011 Services Code is no longer in force. GOV.UK publication page "Equality Act 2010: Code of Practice for services, public functions and associations, 2026" (Office for Equality and Opportunity; EHRC), published 21 May 2026, last updated 5 August 2026: "The Code came into force on 5th August 2026." "The 2011 Code of Practice for Services, Public Functions and Associations (ISBN: 9780108509728) was revoked on the same date." (both SV) https://www.gov.uk/government/publications/equality-act-2010-code-of-practice-for-services-public-functions-and-associations-2026. EHRC "next steps" page dated 14 July 2026: "On 21 May 2026, the Minister for Women and Equalities laid our updated draft code of practice for services, public functions and associations before Parliament." "The 40-day parliamentary scrutiny period ended on 9 July." (SP) https://www.equalityhumanrights.com/code-practice-services-public-functions-and-associations-next-steps
Status of the 2026 Code (GOV.UK HTML, SP): para 1.5 "It is a statutory Code."; para 1.6 "The Code does not impose legal obligations. Nor is it an authoritative statement of the law: only the courts and tribunals can provide such authority." "Courts and tribunals must consider any part of the Code that appears relevant to any questions arising in such proceedings."
2026 Code on websites:
- Para 3.6 (SP): "Part 3 of the Act imposes obligations on those concerned with the provision of services to the public, or to a section of the public, whether in the private, public or voluntary sectors. It does not matter if services are provided free of charge, such as access to a shopping mall, or in return for payment, such as a meal in a restaurant. The obligation also applies to the provision of services on a website (section 29)."
- Chapter 11, "Remote provision of goods and services", paras 11.73–11.81 (EHRC page, published/updated 5 August 2026, https://www.equalityhumanrights.com/guidance/codes-practice/code-practice-services-public-functions-and-associations/chapter-eleven). Para 11.73: "Some goods and services are provided remotely through mediums like websites or apps, for example, where they are delivering information, products or entertainment to the public." (SV) Para 11.76: an ISSP is any service provided "normally for remuneration; at a distance; by electronic means; at the individual request of a recipient of services"; "A service being provided 'normally for remuneration' means the service is usually, but not necessarily, for payment." (SP; "normally for remuneration" SV) Para 11.80: "Following the UK's withdrawal from the European Union, these rules about ISSPs may be subject to further changes and service providers should review the position regularly." (SP) The 2011 Code's sentence "Websites provide access to services and goods, and may in themselves constitute a service" does NOT appear in the 2026 chapter (SV negative). "WCAG"/"Web Content Accessibility Guidelines" do not appear anywhere in Chapter 11 (SV negative).
- Chapter 7 (anticipatory duty): the EHRC chapter-seven page returned HTTP 403 on every attempt and the GOV.UK HTML/PDF are truncated by the fetch tool before Chapter 7, so NOTHING is quoted at source. Secondary only (stammeringlaw.org.uk, "part update 19th August, 2026", presenting these as 2026 Code quotations — SP, SECONDARY): para 7.20 "In relation to services and public functions, the duty to make reasonable adjustments is owed to disabled people generally"; para 7.22 "The duty is anticipatory. This means that service providers, those exercising public functions and associations must proactively consider the barriers that disabled people could face"; para 7.23 "…should not wait until a disabled person wants to use a service"; para 7.27 "…are not expected to anticipate the needs of every individual"; para 7.31 "There are two components to the duty to make reasonable adjustments: the duty to make anticipatory adjustments for a class of people, as well as the continuing duty to make adjustments in individual cases"; para 7.32 "The duty to make reasonable adjustments is a continuing duty." These need verifying against the Code before use. Whether Chapter 7 mentions websites or WCAG: not established.
- The 2011 Code's own paragraphs: not retrieved at source (revoked; not quoted).
EHRC web guidance (non-statutory), "Websites and Internet services", "Last updated: 19 Feb 2019" (SV), https://www.equalityhumanrights.com/en/multipage-guide/websites-and-internet-services: "If someone provides services through a website – such as online shopping, direct marketing or advertising – they are known as an Information Society Service Provider (ISSP)." (SP) "This applies if they have a one-page website which they maintain themselves." (SV) An ISSP must make sure (bullet) "That it makes reasonable adjustments to make sure that its website is accessible to disabled people." (SV as bullet) "Where this is a reasonable adjustment (and, as with other written information, it is likely to be), a website must be accessible to all users – this will include people with visual impairments, who use text-to-speech software, people with manual dexterity impairments, who cannot use a mouse, people with dyslexia and learning difficulties." (SV to "all users"; rest SP) "In making reasonable adjustments, a service provider is not allowed to wait until a disabled person wants to use their services. They must think in advance about what people with a range of impairments might reasonably need." (SV both)
WCAG as benchmark of reasonableness: NO such EHRC statement was found. "WCAG", "Web Content Accessibility Guidelines" and "W3C" are absent from the EHRC websites guidance page (SV negative) and from 2026 Code Chapter 11 (SV negative). The only EHRC page found pointing to a standard is "General web accessibility guidance" ("Last Updated: 03 Apr 2014"), which says "BS 8878 is consistent with the Equality Act 2010 and is referenced in the UK government's e-Accessibility Action Plan…" (SP). Scope (charity, 2021, modified 19 May 2025) asserts "if you meet these requirements (and follow WCAG 2.1) you will also be meeting The Equality Act" (SP) — that is a charity's statement, not the regulator's.
EHRC/ECNI role under the Regulations: reg 11 (B1) and the GDS report passages (B2(c)).

B5. REPORTED UK CASES ON WEBSITE ACCESSIBILITY
Plainly: I found NO reported UK judgment deciding a website-accessibility claim under the Equality Act 2010 or DDA 1995. What is public is settlements and commenced proceedings:
- RNIB v bmibaby: Civil Society, 30 Jan 2012: "RNIB has now served bmibaby with legal proceedings as the website remains inaccessible to those using screen readers or those who cannot use a mouse." (SP) https://www.civilsociety.co.uk/news/rnib-launches-legal-action-over-accessibility-of-bmibaby-website.html. No judgment; Scope describes it as settled out of court (SP, secondary).
- Government Analysis Function, "Accessibility legislation: what you need to know" (published 29 October 2020; official guidance summarising press reports) https://analysisfunction.civilservice.gov.uk/policy-store/accessibility-legislation-what-you-need-to-know/ : "Inaccessible content can result in legal action." (SV) "In March 2023 BBC News reported on the £3,000 settlement awarded to a blind man over inaccessible content." (SV) "Stephen Campbell was unable to access the Health and Social Care Northern Ireland (HSCNI) website to apply for promotion." (SP) "In 2021 The York Press reported on a blind student from York who won £5,000 in a settlement against the Student Loans Company (SLC)." (SV for the sum/party) RNIB/DHSC inaccessible COVID letters: "The case was settled out of court and the DHSC agreed to address the issues." (SV) The BBC source itself was blocked to the fetch tool; not quoted. Same page: "The regulations do not specifically mention the Web Content Accessibility Guidelines (WCAG) 2.2." (SV)
- Scope for business: "Despite this, there have been no UK web accessibility court cases to date." (SP; page modified 19 May 2025)
- Adjacent county-court material listed by reasonableaccess.org.uk (SP, secondary, not website cases): Tse v Aviva Life Services (Slough County Court, 2 April 2019; accessible correspondence formats; £3,300); Maynard v ITV PLC (Salisbury County Court, 30 April 2019; subtitles; struck out).
- A search hit, [2026] EWCC 14 (Birmingham County Court), was checked and is NOT an accessibility case.
- GDS report 2022–24: EHRC sent initial letters to 93 bodies, compliance secured with 66 without enforcement (B2(c)); no court action reported there.

B6. EUROPEAN ACCESSIBILITY ACT, DIRECTIVE (EU) 2019/882 (EUR-Lex, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019L0882; EU law, not UK law)
- Art 31: "Member States shall adopt and publish, by 28 June 2022, the laws, regulations and administrative provisions necessary to comply with this Directive." "They shall apply those measures from 28 June 2025." (SP) Done at Strasbourg, 17 April 2019 (SP).
- Art 2(1) chapeau: "This Directive applies to the following products placed on the market after 28 June 2025:" (SP). Art 2(2) chapeau: "Without prejudice to Article 32, this Directive applies to the following services provided to consumers after 28 June 2025:" (SV) — (a) electronic communications services; (b) services providing access to audiovisual media services; (c) elements of air, bus, rail and waterborne passenger transport services (websites, mobile device-based services, electronic tickets, transport information, self-service terminals); (d) "consumer banking services"; (e) "e-books and dedicated software"; (f) "e-commerce services" (list SP; (f) SV).
- Art 2(4): "This Directive does not apply to the following content of websites and mobile applications:" … "(c) online maps and mapping services, if essential information is provided in an accessible digital manner for maps intended for navigational use; (d) third-party content that is neither funded, developed by, or under the control of, the economic operator concerned;" (SV both, letters confirmed) plus pre-recorded time-based media and office file formats published before 28 June 2025, and archives (SP).
- Art 3 (point 30, SP for the number): "'e-commerce services' means services provided at a distance, through websites and mobile device-based services by electronic means and at the individual request of a consumer with a view to concluding a consumer contract". Recital 43: "The e-commerce services accessibility obligations of this Directive should apply to the online sale of any product or service…" (SV). Art 3(3): "'service' means a service as defined in point 1 of Article 4 of Directive 2006/123/EC…" (SV); Directive 2006/123/EC Art 4(1): "'service' means any self-employed economic activity, normally provided for remuneration, as referred to in Article 50 of the Treaty" (SV). Art 3(4): "'service provider' means any natural or legal person who provides a service on the Union market or makes offers to provide such a service to consumers in the Union" (SV). Art 3(22) consumer; Art 3(23): "'microenterprise' means an enterprise which employs fewer than 10 persons and which has an annual turnover not exceeding EUR 2 million or an annual balance sheet total not exceeding EUR 2 million" (SV).
- Art 4(5): "Microenterprises providing services shall be exempt from complying with the accessibility requirements referred to in paragraph 3 of this Article and any obligations relating to the compliance with those requirements." (SV) Recital 70: "…should therefore not apply to microenterprises providing services within the scope of this Directive." (SV)
- Free public information website: no category in Art 2(2) is "websites" as such; "website" is not a defined term (SV negative); the strings "information websites", "non-commercial", "This Directive applies to all websites" do not appear (SV negatives). The text reaches websites through the listed services, e-commerce being defined by "with a view to concluding a consumer contract".
- UK position: Written Question UIN 6505, tabled 4 Oct 2024, answered 10 October 2024 by Mr Douglas Alexander (DBT): "The European Accessibility Act (EAA) will not directly apply to the UK and, as such, there are no immediate plans within His Majesty's Government (HMG) to transpose this EU legislation." "However, UK companies offering in-scope products or services in the EU will need to comply with its provisions…" (SV both) https://questions-statements.parliament.uk/written-questions/detail/2024-10-04/6505
- Northern Ireland: ECNI written evidence RGD0004 to the Lords Sub-Committee on the Windsor Framework (1 December 2023), para 2.3: "Such EU laws, if introduced, will need to be implemented in law in Ireland, but NI law will not be required to keep pace with them pursuant to the Windsor Framework. Such EU laws include, for example, the Work-life Balance Directive, and the European Accessibility Act." (SV last sentence; preceding SP) https://committees.parliament.uk/writtenevidence/126911/pdf/

B7. PROCESS STANDARDS AND THE STATEMENT TEMPLATE
- BS 8878:2010 "Web accessibility. Code of practice". BSI Knowledge page (https://knowledge.bsigroup.com/products/web-accessibility-code-of-practice) as read today shows Status "Current", Published "30 Nov 2010", Committee ICT/2; the words "Withdrawn", "Superseded", "30071" do NOT appear on the page (SV negative, checked twice). Scope: "It provides guidance for all sectors on meeting the requirements of the Equality Act 2010" (SV); "The standard also focuses on processes rather than technical or design issues" (SV). The widely repeated statement "On 28 May 2019, BS 8878 was superseded by ISO 30071-1" was found only on Wikipedia (SP, secondary); neither BSI page for BS 8878 nor for BS ISO/IEC 30071-1:2019 (Status "Current", Published "30 Jun 2019", no mention of BS 8878 — SP) nor the ISO page confirms it. Treat supersession as UNCONFIRMED at source.
- ISO/IEC 30071-1:2019, "Information technology — Development of user interface accessibility — Part 1: Code of practice for creating accessible ICT products and services", Edition 1, "Publication date: 2019-05", stage "90.93 2024-09-17 International Standard confirmed" (SV), ISO/IEC JTC 1/SC 35, 50 pages (SP). Abstract: "This document takes a holistic approach to the accessibility of information and communications technology (ICT)…" (SV); "…gives guidelines for building and maintaining ICT systems (including products and services) that are accessible to diverse users (including users with disabilities and older people)" (SV). https://www.iso.org/standard/70913.html
- Accessibility statement template: "Sample accessibility statement (for a fictional public sector website)", GDS/CDDO, published 17 May 2019, last updated 30 September 2024 (SP). https://www.gov.uk/government/publications/sample-accessibility-statement/sample-accessibility-statement-for-a-fictional-public-sector-website. Headings (SP): How accessible this website is; Feedback and contact information; Enforcement procedure; Technical information about this website's accessibility; Compliance status; Non-accessible content [Non-compliance with the accessibility regulations; Disproportionate burden; Content that's not within the scope of the accessibility regulations]; What we're doing to improve accessibility; Preparation of this accessibility statement. Compliance options (SP): "This website is fully compliant with the Web Content Accessibility Guidelines version 2.2 AA standard." / "…partially compliant … due to [insert one of the following: 'the non-compliances', 'the exemptions' or 'the non-compliances and exemptions'] listed below." / "…not compliant…". "The Equality and Human Rights Commission (EHRC) is responsible for enforcing the Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018 (the 'accessibility regulations')." (SP) Related guidance: "The sample statement is based on the model accessibility statement, which details what information you must put in an accessibility statement." (SP). The "model accessibility statement" URL I guessed returned 404; not located.

B8. SCOTLAND / WALES / NORTHERN IRELAND
The Regulations carry the "U.K." extent marker on each provision and the EM states "The territorial extent of this instrument is the United Kingdom." (SV). The difference is the parent discrimination statute and the enforcer: reg 11 gives the EHRC for bodies "required to comply with the Equality Act 2010" and the ECNI for bodies "required to comply with the Disability Discrimination Act 1995" (SV); reg 12(3)(b) refers to "sections 19 to 21 and 21B to 21E of the Disability Discrimination Act 1995" (SV). In Northern Ireland the DDA test is differently worded — s.21(1): "Where a provider of services has a practice, policy or procedure which makes it impossible or unreasonably difficult for disabled persons to make use of a service which he provides…" (SV); the phrase "substantial disadvantage" does not appear in s.21 (SV negative); extent note: "Following the repeal of this Act for E.W.S. by the Equality Act 2010, this section now extends to N.I. only." (SV) https://www.legislation.gov.uk/ukpga/1995/50/section/21. Wales adds a language duty on bodies subject to the Welsh Language Standards (No. 1) Regulations 2015 (2015 No. 996 (W. 68)), Schedule 1, "Standards relating to a body's websites and on-line services": Standard 52 "You must ensure that— (a) the text of each page of your website is available in Welsh, (b) every Welsh language page on your website is fully functional, and (c) the Welsh language is not treated less favourably than the English language on your website." (SV); Standard 56 "You must provide the interface and menus on every page of your website in Welsh." (SV); Standard 57 "All apps that you publish must function fully in Welsh…" (SV). Which standards bind a given body depends on its compliance notice (not researched). Nothing Scotland-specific was found in the Regulations; Scottish specific duties under the PSED were not researched.

B9. PUBLIC BODIES EMBEDDING THIRD-PARTY CONTENT
Text chain: reg 4(2)(e) (B1) → GDS guidance "if you did not pay for it or develop it yourself" (B2(a)) → GDS monitoring page "If you have funded, developed or are in control of third party content, it is your responsibility to make sure that it is accessible." and "You should make sure your accessibility statement is updated to include any issues users may experience when using third party content on your website." (B2(b), SV).
Source of the wording, Directive (EU) 2016/2102 recital 30 (EU text; no longer UK law but the origin of reg 4(2)(e)) — all SV: "Embedded content, such as embedded images or videos, should be covered by this Directive." "Such third-party content, provided that it is neither funded nor developed by the public sector body concerned nor under its control, should be excluded from the scope of this Directive." "Such content should, in principle, not be used if it hinders or decreases the functionality of the public service offered on the website or mobile application concerned." Also "…that content cannot be considered as third-party content and should therefore be accessible" (consultations/forums). Recital 25 on NGOs: "In order to avoid imposing a disproportionate burden on such NGOs, this Directive should not apply to them." (SV) https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016L2102
Real statements (official practice):
(1) ONS, https://www.ons.gov.uk/help/accessibility — "This statement was prepared on 19 September 2020." "It was last reviewed and updated in December 2025." "…last tested in March 2024 following a test completed by the Digital Accessibility Centre (DAC)." (SP) Under "Non-compliance with the accessibility regulations" (heading placement SV): "The interactive pop-up polls we use to collect feedback on some pages of the ONS website are not fully accessible." "These are provided by a third party." (SV both) — listed with failures against 1.3.1, 4.1.2, 3.3.1, 3.3.2, 2.4.3, 1.3.2, 2.4.6, 1.4.12 (SP). On its own embeds: "Many pages on the site include embedded data visualisation content." (SP) "Embedded content is a window on a page that includes content published on a different web page." (SV) "In all instances, the underlying data are accessible through other formats, such as the accompanying dataset files and the surrounding commentary on the HTML web page." (SV) Disproportionate burden: "We have looked at the resources required to make all historical data visualisations on the website accessible compared with their use and believe that this would be a disproportionate burden." (SV for final clause) "This website is partially compliant with the Web Content Accessibility Guidelines (WCAG) version 2.2 AA standard…" (SP)
(2) Manchester City Council, https://www.manchester.gov.uk/accessibility-statement — "It was last reviewed on 25 March 2026." (SP) Heading "Census content on Microsoft Power BI": "This is a third-party app used to compare census data between years and wards." (SV) followed by "We've provided accessible summaries of the census data" (SP). "Intelligence Hub": "This is a third-party platform containing data about Manchester on a range of topics…" (SP) "Due to the graphical and geographical nature of the data shown, some users may require data in alternative accessible formats." (SV) Maps: "As these issues lie within Google's coding, we cannot change them." (SV) Flickr: "The code used to embed an image or album can create non-compliant elements." (SV)
(3) Kent County Council, https://www.kent.gov.uk/about-the-council/about-the-website/accessibility-statement — "It was last reviewed on 9 June 2026." (SP) Under "Platform specific issues": "We use GovService, a third party platform, to create and host forms." (SV) Section "Third party content": "Our website contains third party content. We do not have control over and are not responsible for the accessibility of this content, but we endeavour to work with the third party to improve its accessibility." (SV) "content or functionality on our website that we do not control, develop, or fund" (SV). "We are not responsible for the accessibility of the YouTube or Vimeo platforms." (SV)
What the examples show: bodies handle embeds three different ways — listing them as their own non-compliance (ONS polls; Kent's commissioned platforms), listing them with an accessible alternative (Manchester Power BI), or disclaiming them (Kent "do not control, develop, or fund").

PROCUREMENT (asked under "Also report")
- Procurement Act 2023 s.56 "Technical specifications" (https://www.legislation.gov.uk/ukpga/2023/54/section/56; banner "There are currently no known outstanding effects for the Procurement Act 2023, Section 56."): the words "accessibility", "disabled", "disabilities" do not appear in the section (SP full-text read; single check).
- Public Contracts Regulations 2015 reg 42 (which carried the accessibility-criteria wording) is shown as revoked: page title "The Public Contracts Regulations 2015 (revoked)", text replaced by dots, revoked 24 February 2025 (SP). Its former paras (8)–(9) could not be quoted.
- Cabinet Office "Guidance: Technical Specifications" (published 24 May 2024, last updated 13 July 2026), para 7: "Other legal obligations (outside of the Act) may apply when drawing up technical specifications… technical specifications will need to be drawn up to take account of the needs of people with disabilities, with disability accessibility and broader considerations covered by the public sector equality duty under section 149 of the Equality Act 2010." (SV for the s.149 clause; sentence opening SP.) Neither "WCAG" nor the 2018 Regulations is mentioned (SV negative). https://www.gov.uk/government/publications/procurement-act-2023-guidance-documents-define-phase/guidance-technical-specifications-html
- Technology Code of Practice point 2, "Make things accessible and inclusive" (GDS/CDDO; "Last updated: 5 October 2023"): "All suppliers to government have a legal duty to make their technology and services accessible to all, especially people with disabilities." (SV, corrected wording) "Legally, public sector websites and apps must meet accessibility standards." (SV) Under "How to supply accessible technology": "You must meet the WCAG 2.2 AA standard as a minimum." (SV) "If you're supplying a technology product to the public sector, you might need to make a statement about how that product meets accessibility standards." (SV) https://www.gov.uk/guidance/make-things-accessible
- Does commissioning trigger the Regulations? The texts that bear on it: reg 4(2)(e) excludes only third-party content "neither funded nor developed by, nor under the control of" the body; the GDS reading is "if you did not pay for it or develop it yourself" and "If you have funded, developed or are in control of third party content, it is your responsibility". No PPN on accessibility was found (one search).
- s.149(1) Equality Act (PSED): "A public authority must, in the exercise of its functions, have due regard to the need to— (a) eliminate discrimination, harassment, victimisation and any other conduct that is prohibited by or under this Act; (b) advance equality of opportunity…; (c) foster good relations…" (SP); s.149(4): "The steps involved in meeting the needs of disabled persons that are different from the needs of persons who are not disabled include, in particular, steps to take account of disabled persons' disabilities." (SP)

UNASKED THREADS
1. The 2011 Services Code was revoked and replaced on 5 August 2026 — any chapter text citing "the 2011 Code" or its "may in themselves constitute a service" sentence is now citing a revoked document; the 2026 Code's equivalent is para 11.73 and para 3.6.
2. S.I. 2025/557 moved the monitoring/statement functions to the "Secretary of State" from 3.6.2025; GOV.UK guidance (last updated Sept 2024) still names the Minister for the Cabinet Office and CDDO.
3. Reg 9 is a dynamic reference ("as amended from time to time") with no version number; WCAG 2.2 AA arrives via GDS's statement that it "will automatically become the standard", and GDS "has been monitoring for this standard since October 2024".
4. Equality Act Schedule 25 (information society services), relevant to a GB studio with EEA users: para 1(2) "This Act applies to anything done by the person in an EEA state (other than the United Kingdom) in providing the service as this Act would apply if the act in question were done by the person in Great Britain."; para 2(2) (EEA-established provider) "This Act does not apply to anything done by the person in providing the service." (SP) Para 7(2)(b) definition: "any service normally provided for remuneration, at a distance, by means of electronic equipment… and at the individual request of a recipient of a service" (SP). The 2026 Code glosses "normally for remuneration" as "usually, but not necessarily, for payment".
5. The EAA's content exclusions (Art 2(4)(c), (d)) reuse the 2016 Directive's maps and third-party wording almost word for word — the same two carve-outs sit in UK public-sector law and EU private-sector law.
6. GDS's own figure that automated checkers detect "approximately 30-40%" of issues, and that the top failures (focus visible, contrast, keyboard, reflow) are largely those automated tests miss.
7. Disproportionate-burden claims rise with depth of test: 17% simplified, 37% detailed, 57% mobile app.
8. The ONS statement treats "the surrounding commentary" and "accompanying dataset files" as the accessible route to an embedded visualisation — official practice directly on the chapter's question.

LEFT OUT (and why)
- 2026 Code Chapter 7 at source and the 2011 Code text: EHRC chapter-seven page 403 on four attempts; GOV.UK HTML/PDF truncated by the tool at about 130–138k characters (reaches only Chapter 5). Secondary quotations flagged above.
- EHRC news page "Services Code of Practice comes into force": 403 twice; the in-force date is taken from GOV.UK instead.
- BBC and Bird & Bird sources (blocked/402); the York Press and RNIB originals for the settlements (reported only via the Analysis Function page).
- PCR 2015 reg 42(8)–(9) historical wording (revoked page shows no text).
- The S.I. 2025/557 Order text itself (only its annotations on the 2018 Regulations were read).
- Model accessibility statement page (guessed URL 404); the 2020–21 monitoring report; Welsh compliance notices; Scottish specific duties; Online Safety Act (excluded by the brief).
- Explanatory Notes for s.29 and case law on the anticipatory duty generally (Roads v Central Trains, Paulley, Rowley etc. are listed by stammeringlaw but none concerns websites and none was read).

RICH REFERENCES
1. GDS, "Accessibility monitoring of public sector websites and mobile apps from 2022 to 2024" (17 December 2024) — the only official UK dataset on what fails, what gets fixed, burden claims and enforcement outcomes.
2. EHRC, Code of Practice for services, public functions and associations (2026), Chapters 3, 7 and 11 — in force 5 August 2026; Chapter 7 still needs reading at source.
3. Directive (EU) 2016/2102 recital 30 together with reg 4(2)(e) and the GDS monitoring page's "Third party content" section — the full textual chain on embeds. (A possible fourth: Lawson and Orchard, "The anticipatory reasonable adjustment duty: removing the blockages?", Cambridge Law Journal 2021 — surfaced in search, not read.)

SURPRISED
- The 2011 Code is gone: a new statutory Code came into force two months ago, and its website paragraph is new wording.
- The brief's regulation numbers were one or more out throughout (reg 2 is a revocation), and the Equality Act link is "treated as a failure to make a reasonable adjustment", not a "failure to comply with a duty under" the Act.
- The word "anticipatory" appears nowhere in the Act or Schedule 2; it is Explanatory Note and Code language resting on "disabled persons generally".
- The BSI page shows BS 8878:2010 as "Current", with no withdrawal or supersession notice; the supersession claim traces only to Wikipedia in what I could reach.
- No EHRC text names WCAG at all, in the Code chapter on remote services or in its websites guidance.
- Fourteen years after bmibaby, still no reported UK judgment on a website; the public record is settlements of £3,000 and £5,000 and EHRC letters.
- The Procurement Act 2023's technical-specifications section contains no accessibility wording; guidance routes it through s.149.

WebSearch calls used: 15.

---

## Agent C

AGENT C REPORT — THE EVIDENCE (disabled readers and data displays; convergence)
All sources fetched 6 October 2026. WebSearch calls used: 26 of 30.
Labels: STRING-VERIFIED = confirmed on a second YES/NO presence fetch (false control strings were included in most checks and were all rejected). SINGLE PASS = seen on one fetch only. ABSTRACT = only the abstract was reachable. Where the checker answered "NO" only because my string lacked the sentence's opening words, I say "verified as substring".

Corrections to the brief, up front:
- FRS 2023/24 figure is 16.8 million (25%), not 16.1 million.
- Sharif 2021 figures are 61.48% less accurate and 210.96% more time ("62%" is wrong; "211%" is the authors' own later rounding).
- Chartability: the paper analysis produced 45 groupings and previews 10 critical heuristics; the current site (v2) states 50 heuristics, 14 critical.
- Olli is an IEEE VIS 2022 poster, not UIST.
- Marriott et al. 2021 is in ACM Interactions 28(3), not CG&A.
- The WebAIM Million now has a February 2026 edition; both 2025 and 2026 are given.
- WebAIM Screen Reader Survey #10 has no overlay question; the overlay finding is in the Practitioners Survey #3 (2021).
- GOV.UK writing guidance has moved domain and its "clear language" page no longer contains the phrase "reading age".

C1. Lundgard & Satyanarayan 2022 (IEEE TVCG / InfoVis) — peer-reviewed evidence
URLs: https://arxiv.org/abs/2110.04406 ; http://vis.csail.mit.edu/pubs/vis-text-model/ ; https://ar5iv.labs.arxiv.org/html/2110.04406
- Level names, STRING-VERIFIED: "Elemental and Encoded Properties"; "Statistical Concepts and Relations"; "Perceptual and Cognitive Phenomena"; "Contextual and Domain-Specific Insights".
- Level glosses, SINGLE PASS: L1 "chart type, encoding channels, title, axis ranges, labels, colors"; L2 "descriptive statistics, extrema, outliers, correlations, point-wise comparisons"; L3 "complex trends, pattern synthesis, exceptions, commonplace concepts"; L4 "domain-specific insights, current events, social and political context, explanations".
- Model basis, STRING-VERIFIED: "2,147 sentences" (grounded theory).
- Sample, STRING-VERIFIED: "30 blind and 90 sighted readers".
- Design: each reader ranked the usefulness of four descriptions (one per level) per chart. STRING-VERIFIED fragments: "we asked each blind participant to rank all 15 visualizations"; "we asked each participant to rank only 5 of the 15 visualizations at a time" (sighted).
- Recruitment and pay, SINGLE PASS: sighted via Prolific, "$10-12 per hour, for an approximately 20-minute task"; blind readers screen-reader proficient, "$50 per hour, for an approximately 1-hour task".
- Central finding, STRING-VERIFIED (substring): "while both groups generally prefer mid-level semantic content, they sharply diverge in their rankings of both the lowest and highest levels of our model."
- STRING-VERIFIED: "In particular, blind readers rank content and Levels 2 and 3 as most useful (Region 4.C)" (the tool twice returned "and Levels"; possibly "at Levels" in the source) and "semantic content at Levels 1 and 4 as least useful".
- Sighted readers, STRING-VERIFIED: "Levels 3 and 4 are found to be most useful".
- Level 4, STRING-VERIFIED: "A majority of blind readers (63%, n=19) were emphatic that descriptions should not include domain-specific explanations at Level 4".
- Level 1 nuance, STRING-VERIFIED: "ranked 'most useful' in 101 and 87 instances by blind and sighted readers".
- Abstract conclusion, SINGLE PASS: "captions for blind readers should aim to convey a chart's trends and statistics, rather than solely detailing its low-level design elements or high-level insights."
- Limits, SINGLE PASS: model "focuses on English sentences and canonical chart types"; descriptions were curated by the authors; the outcome is a usefulness ranking, not comprehension. The Friedman p-value was dropped by the reader tool and is not reported here.
- Role: the only large-sample evidence that blind and sighted readers want different content from a chart description; a caution against putting interpretation into the alt text.

C2. Zong, Lee, Lundgard, Jang, Hajas & Satyanarayan 2022 (CGF / EuroVis) — peer-reviewed evidence; and Olli
URLs: https://arxiv.org/abs/2205.04917 ; https://ar5iv.labs.arxiv.org/html/2205.04917
- Three dimensions (abstract, SINGLE PASS for the full sentence): "structure, or how chart entities should be organized for a screen reader to traverse; navigation, or the structural, spatial, and targeted operations a user might perform to step through the structure; and, description, or the semantic content, composition, and verbosity of the screen reader's narration."
- n, STRING-VERIFIED: "13 blind and low vision". Breakdown SINGLE PASS: 7 totally blind, 4 light perception, 2 low vision.
- Task, STRING-VERIFIED: "Participants were asked to explore three prototype accessible screen reader experiences, shown one after another each with a different dataset." Prototypes (SINGLE PASS): table (standard HTML table, the control), multi-view (faceted bar chart), target (scatterplot with targeted navigation).
- Tables, STRING-VERIFIED: "participants overwhelmingly reported the same problems: they are ill-suited for processing large amounts of data and impose high cognitive load as users must remember previous lines".
- Quantified result, STRING-VERIFIED: "A Friedman test found a significant rating difference for the ease-of-use of the prototypes χ2(2,N=13)=15.05,p<0.01, with a large effect size (Kendall's W=0.58)." and "Follow-up Nemenyi tests revealed that multi-view was more difficult to use than table with statistical significance (p<0.01)".
- So the cognitive-load claim against tables is qualitative, and the only significant quantitative result is that the table was easier to use than one of the richer prototypes. There is no quantified cognitive-load reduction (control string «reduced cognitive load by 40%» rejected).
- Prototype: "implemented on top of Vega-Lite" (SINGLE PASS as an exact phrase).
- Co-design, STRING-VERIFIED: "we intentionally acknowledge Hajas as both co-designer and co-author."
- Limits, SINGLE PASS: needs "differ substantially for users who are totally blind compared to those with low-vision"; only text-to-speech considered.
- Olli. https://vis.csail.mit.edu/pubs/olli/ — Blanco, Zong & Satyanarayan, "Olli: An Extensible Visualization Library for Screen Reader Accessibility", IEEE VIS Posters 2022 (SINGLE PASS). Abstract, SINGLE PASS: "Olli renders a chart as an accessible tree view following the HTML Accessible Rich Internet Applications (ARIA) standard." Repository has moved to https://github.com/umwelt-data/olli. README STRING-VERIFIED: "Olli is a library for converting data representations into accessible text structures for screen reader users." Adapters line STRING-VERIFIED: "olli-adapters Vega, Vega-Lite, Observable Plot, Bluefish → specs" (no Highcharts).
- Role: the source for "navigable structure" as a route, and the honest footnote that the flat table still won on ease of use.

C3. Kim, Joyner, Riegelhuth & Kim 2021; Marriott et al. 2021
Kim et al., CGF 40(3), 173–188, June 2021 (Crossref metadata). https://diglib.eg.org/bitstream/handle/10.1111/cgf14298/v40i3pp173-188.pdf — peer-reviewed survey.
- Corpus, STRING-VERIFIED: "resulting in a total of 56 papers"; "an initial corpus of 413 publications"; papers "published since 1999".
- Dimensions, STRING-VERIFIED: "seven dimensions: user group, literacy task, chart type, interaction, information granularity, sensory modality, assistive technology."
- STRING-VERIFIED: "The reading task groups all tasks corresponding to the ability to understand the meaning of visualizations (44/56), while creating refers to tasks requiring the ability to construct visualizations on their own (12/56)."
- Modalities, SINGLE PASS (returned on the verification pass): "speech (40/56) and sonification (16/56)"; "tactile graphics such as embossed prints and physical visualization (19/56), haptic feedback such as forced vibrations (15/56), and braille for texts (7/56)."
- State of evidence, SINGLE PASS: "Most research in our collection did not consider various types of visual impairment."; "A few studies briefly discuss low-vision or involve low-vision participants but do not address the specific needs of this population."; "Most studies do not go beyond basic statistical plots such as bar charts, line charts, pie charts, and scatter plots that take up around 80% of all charts."
Marriott, Lee, Butler, Cutrell, Ellis, Goncu, Hearst, McCoy & Szafir 2021, ACM Interactions 28(3). https://interactions.acm.org/archive/view/may-june-2021/inclusive-data-visualization-for-people-with-disabilities — position paper.
- STRING-VERIFIED: "A 2011 report from the WHO estimates that more than 1 billion people—15 percent of the world's population—live with some form of disability, of whom about one-fifth experience significant difficulties in functioning." (the article quoting WHO)
- STRING-VERIFIED: "The visualization research community, however, has not paid enough attention to the needs of people with disabilities."
- STRING-VERIFIED: "There are three main kinds of disability that may affect access to visualizations: visual, cognitive, and motor impairments."
- SINGLE PASS: "they currently lack evidence-based guidelines and tools that encourage and facilitate the creation of more accessible content."; "In practice, however, alt text is frequently missing or inadequate."; "Currently, design recommendations for CALD-accessible visualizations are not informed by research, remaining largely heuristic." (I did not confirm what "CALD" abbreviates.)
- Role: the field's own admission that the evidence is narrow (blind readers, reading tasks, basic charts) and guidelines are largely heuristic.

C4. VoxLens and Sharif et al. 2021 — peer-reviewed evidence
VoxLens (CHI 2022). https://wildlab.cs.washington.edu/Publications_files/Sharif_CHI2022.pdf (dl.acm.org returned 403)
- STRING-VERIFIED: "Through task-based experiments with 21 screen-reader users"; "by 122% and 36%, respectively".
- STRING-VERIFIED: "with VoxLens users achieving 75% accuracy (SD = 18.0%) and non-VoxLens users achieving only 34% accuracy (SD = 20.1%)."
- STRING-VERIFIED: "the average IT for non-VoxLens users was 84.6 seconds (SD=75.2). For VoxLens users, it was 54.1 seconds (SD=21.9)."
- Baseline, STRING-VERIFIED: "we used prior work's data [69] (N=36) as a baseline for comparison." So the comparison is between studies, not a within-study control.
- Limit, STRING-VERIFIED: "Currently, VoxLens only supports two-dimensional single-series data."
- SINGLE PASS: three modes (question-and-answer by voice, summary, sonification); supports Google Charts, D3, ChartJS; fully functional only in Chrome; one of the 21 excluded from analysis.
Sharif, Chintalapati, Wobbrock & Reinecke, ASSETS 2021. https://wildlab.cs.washington.edu/Publications_files/Sharif_ASSETS2021.pdf
- STRING-VERIFIED: "(1) A qualitative study with nine screen-reader users, and (2) a quantitative study with 36 screen-reader and 36 non-screen-reader users".
- STRING-VERIFIED: "screen-reader users extract information 61.48% less accurately and spend 210.96% more time interacting with online data visualizations compared to non-screen-reader users."
- STRING-VERIFIED: "The study was conducted online, without supervision."
- SINGLE PASS: bar, scatter and line charts in Google Charts, ChartJS and D3; multiple-choice tasks (maximum/minimum, comparison of two points, value retrieval, trend, correlation). Recommendation SINGLE PASS: "many visualizations are indetectable to screen readers."
- Role: the headline measured gap, and one measured remedy, with the caveat about its baseline.

C5. Siu et al. 2022; Fan et al. 2023; Thompson et al. 2023; Jung et al. 2022 — peer-reviewed evidence
Siu et al., CHI 2022. https://hci.stanford.edu/publications/2022/siu2022datanarratives.pdf
- STRING-VERIFIED: "We evaluate our approach with 16 screen reader users."; "Four co-designers were recruited through snowball sampling".
- Compared: description interleaved with sonified segments ("Narrative") versus all description first then one sonification ("Control"). No table condition (verified NO).
- STRING-VERIFIED: "The average number of insights is higher in the Narrative condition (x̄ = 15.4, SD = 6.5) compared to the Control condition (x̄ = 12.4, SD = 6.3)."; "we expect to have a rate 1.24 times greater in the number of insights provided."
- SINGLE PASS: p = 0.0013; proportion of inferred insights 0.33 vs 0.21; single-variable time series only; high cognitive load in both conditions.
Fan et al., ACM TACCESS 2023. https://shape.stanford.edu/research/DataAccessibility/Fan2023_TheAccessibilityOfDataVisualizationsOnTheWeb.pdf
- STRING-VERIFIED (substrings): "an accessibility audit of 87 data visualizations on the web"; "an online survey of 127 screen reader users"; "a remote contextual inquiry with 12 of the survey respondents".
- STRING-VERIFIED: "82% (9/11) of Born Accessible visualizations were rated as very or extremely accessible, while only 14% (11/76) of Top Results visualizations achieved the same ratings."
- STRING-VERIFIED: "21% (3/14) of line graphs, 18% (3/17) of bar graphs, and 7% (1/15) of maps were rated moderately to extremely accessible."
- STRING-VERIFIED: "tables (n = 13) were the only type of representation in which the majority of visualization were rated moderately to extremely accessible (54%, 7/13)."
- STRING-VERIFIED: "None of the audited maps in both groups directly conveyed complexity in the data".
- STRING-VERIFIED: "the most frequently indicated method was through tactile graphics (n = 50), followed by Braille (n = 25), then audio (n = 15), screen reader (n = 7), and sighted assistance (n = 4)." (preferred method of accessing data)
- SINGLE PASS: "65% of respondents reported encountering data-driven media regularly"; "73% of respondents did not agree that data-driven media encountered was typically accessible"; "94% (117/125) agreed they have concerns about accessing accurate information in a timely manner"; "Auditors on average spent 25 minutes per visualization and 78 minutes per website." (one pass returned "78 hours"; the second "78 minutes" — treat the unit as unconfirmed).
- The project page (https://shape.stanford.edu/research/DataAccessibility) gives "16%" very/extremely accessible and "71%" slightly/not at all; I could not confirm these in the PDF.
- Limits, SINGLE PASS: judgement sampling; two of the auditors sighted; mixed screen readers and browsers.
Thompson, Martinez, Sarikaya, Cutrell & Lee, CHI 2023. https://www.microsoft.com/en-us/research/wp-content/uploads/2023/04/ChartReader-CHI2023.pdf
- STRING-VERIFIED: "we partnered with 10 BLV screen reader users".
- SINGLE PASS: "over a continuous period of five months"; "three one-hour sessions"; dimensions "structure, navigation, and description, as well as non-speech audio (e.g., sonification, earcons) and focus"; supports single- and multi-series line charts and stacked bar charts.
- SINGLE PASS: "providing tabular representations is a lossy exchange, as raw data is devoid of the design decisions and communicative intent of the author".
- SINGLE PASS limit: "Our design almost exclusively focuses on audio representation with little supplementary visuals."
Jung, Mehta, Kulkarni, Zhao & Kim, IEEE TVCG 2022. https://arxiv.org/pdf/2108.03657
- STRING-VERIFIED: "we interviewed 22 people with visual impairments"; "reference the underlying data instead of visual elements"; "construct an image of visualizations in their head".
- SINGLE PASS (returned on the verification pass): "We collected total of 2,278 publications (VIS&TVCG:723, ASSETS:95, CHI:1,460) with 7,493 figures"; "Among those figures, 40% contained alternative text descriptions"; "The length suggested by the majority of participants ranges from 2 to 8 sentences."; "All participants favored having access to the underlying data of the visualization."; "Use plain language instead of visualization-specific language (e.g., shade vs. gradient) to enhance accessibility."
- SINGLE PASS: 21 blind, 1 low vision; recommendations to open with chart type, describe axes and range, give trends, put data-table access last.
- Role: together these say what a description should hold, that tables rated best in a real audit, and that survey respondents' first preference was tactile, not screen-reader, access.

C6. Chartability; Data Navigator
Elavsky, Bennett & Moritz 2022 (EuroVis). Paper in HTML: https://www.frank.computer/chartability/ ; workbook: https://chartability.github.io/POUR-CAF/ — peer-reviewed heuristic framework plus living practitioner resource.
- Paper, STRING-VERIFIED: "I then adjusted each of the 45 groupings that resulted from the qualitative analysis into phrasing that could be verified."; "The current version of Chartability (v2) has a total of 50 heuristics."; "10 critical heuristics (these were determined top priorities through user feedback) are previewed in Table 1".
- Site, STRING-VERIFIED: "The following section contains Chartability's 7 principles and 50 heuristics, 14 of which are considered *critical*."
- Seven principles (SINGLE PASS): Perceivable, Operable, Understandable, Robust, Compromising, Assistive, Flexible. Paper SINGLE PASS: "26 heuristics fit neatly back into Perceivable, Operable, Understandable, or Robust"; "19 remaining heuristics with complex codes".
- Site's 14 critical titles, SINGLE PASS: Low contrast; Content is only visual; Small text size; Visual presents seizure risk; Interaction modality only has one input type; No interaction cues or instructions; Controls override AT controls; No explanation for purpose or for how to read; No title, summary, or caption; Reading level inappropriate; No table; Data density is inappropriate; Navigation and interaction is tedious; User style change not respected.
- Time, STRING-VERIFIED on both pages: "those new to auditing may take anywhere between 2 and 8 hours to complete a full pass of Chartability." SINGLE PASS: a highly trained auditor "in as little as 30 minutes".
- Evaluation, STRING-VERIFIED: "I worked with 19 total participants across 8 environment spaces."; "I can publish interview results from 6 participants and discuss the details of 4 audit environments."
- SINGLE PASS: "All novice accessibility practitioners became more confident after using Chartability and believed auditing data visualizations for accessibility to be less difficult."
- Scope sentence, SINGLE PASS: "evaluate data-driven visualizations and interfaces for visual, motor, vestibular, neurological, and cognitive accessibility."
- Version: the site names "Chartability_Worksheet_V2"; no date or changelog on the page. The checker read only the first 100,000 of 109,527 characters of the paper page.
Elavsky, Nadolskis & Moritz 2023 (IEEE VIS 2023 / TVCG). https://arxiv.org/pdf/2308.08475
- STRING-VERIFIED: "We present 3 case examples with Data Navigator"; "Data Navigator supports a wide range of input modalities: screen reader, keyboard, speech, gesture detection, and even fabricated assistive devices."; "Data Navigator is a step towards making accessible data visualizations easier to design and implement."
- Evaluation, STRING-VERIFIED: "a critical next step for future work is to conduct separate studies with both practitioners and end users to evaluate Data Navigator's affordances." No user study.
- SINGLE PASS: "Authors Frank Elavsky (sighted) and Lucas Nadolskis (blind)".
- Role: the audit instrument is evaluated on auditors' confidence, not on disabled readers' outcomes; the navigation toolkit is unevaluated with users.

C7. Alt text practice
Chintalapati, Bragg & Wang, ASSETS 2022. https://arxiv.org/pdf/2209.13718 — peer-reviewed.
- STRING-VERIFIED: "only 50% of alt texts in our sample contain information about extrema or outliers"; "only 31% contain information about major trends or comparisons".
- STRING-VERIFIED: "Only 897 (4.6%) of these converted documents contain at least one piece of valid alt text." This is a share of papers, not of figures. Denominator SINGLE PASS: 19,500 PDFs converted out of "25218 total paper PDFs".
- STRING-VERIFIED: "547 figure alt texts (consisting of 2127 sentences)". Coverage SINGLE PASS: CHI and ASSETS, 2010–2020. SINGLE PASS: "the vast majority of alt text contain level 1 information".
Mack, Cutrell, Lee & Morris, ASSETS 2021. https://www.microsoft.com/en-us/research/wp-content/uploads/2021/08/Mack-ASSETS21__Alt-Text-in-Slides.pdf (PDF text has lost ligatures)
- STRING-VERIFIED as printed: "Finally, authors crafted signifcantly lower quality alt text when starting from the automatic alt text compared to starting from a blank box."
- STRING-VERIFIED: "the average alt text quality rating when starting from a blank text box (M = 2.96, SD = .81) was higher than that when starting from the automatic alt text (M = 2.38, SD = .50)."
- SINGLE PASS: 12 authors and six screen-reader users; "Five participants preferred the free-form interface, all but one of whom had experience writing alt text, and four preferred the template interface"; PowerPoint only.
News and government charts: I found no audit of news charts. Closest:
- Jung et al. (above): 40% of 7,493 figures in VIS/TVCG, CHI and ASSETS papers had alt text (SINGLE PASS).
- Cassidy, Reuters Institute fellowship paper, 17 January 2023 (journalism, not peer-reviewed). https://reutersinstitute.politics.ox.ac.uk/blind-news-audiences-are-being-left-behind-data-visualisation-revolution-heres-how-we-fix — STRING-VERIFIED (substring): "of 55 government agencies disseminating health information about COVID-19, only 12 had included any meaningful alt-text for their visual data." This is Cassidy reporting a Carnegie Mellon analysis of Twitter (linked DOI 10.1145/3373625.3417023), which I did not open. STRING-VERIFIED, Alan Smith of the FT quoted: "you produce something like 20,000 charts a year."

C8. Sonification and audio graphs
Apple. https://developer.apple.com/documentation/accessibility/audio-graphs.md (raw markdown returned identically on two fetches) — vendor documentation.
- STRING-VERIFIED: "Define an accessible representation of your chart for VoiceOver to generate an audio graph."
- STRING-VERIFIED: "Use the audio graphs API to provide all the information that VoiceOver needs to construct an audible representation of the data in your charts and graphs, making the data accessible to people who are blind or have low vision."
- STRING-VERIFIED: "Typically, the audio graph represents the x-axis as time, and the y-axis as pitch."
- AXChart: "A protocol that declares the minimum interface necessary for an accessibility element to act as a chart." AXChartDescriptor: "An object that contains all the semantic information about an accessible chart." The page links WWDC21 session 10122 and states no OS version.
Highcharts. https://www.highcharts.com/docs/sonification/getting-started
- STRING-VERIFIED: "Scientifically speaking, sonification is a collective term for conveying information or perceptualizing data using non-speech audio."; "In Highcharts, we provide a sonification module to allow you full control of playing your data using sound." The getting-started page states no specific default mapping.
Flowers 2005: UNREACHABLE (icad.org robots.txt timed out twice; a guessed Georgia Tech mirror did not resolve). Nothing quoted.
Walker & Nees, "Theory of Sonification" — Georgia Tech author copy http://sonify.psych.gatech.edu/~ben/references/nees_theory_of_sonification.pdf (the sonification.de handbook PDF was unreachable). Walker's publication list gives: The Sonification Handbook, 2011, pp. 9–39. Book chapter.
- STRING-VERIFIED: "Walker and Nees (2005b) further demonstrated that a brief training period (around 20 min) can reduce performance error by 50% on a point estimation sonification task."
- STRING-VERIFIED: "research has generally found weak to non-existent correlations between musical experience and performance with auditory displays."
- STRING-VERIFIED: "the field as a whole continues to exist in a virtual theoretical vacuum".
- SINGLE PASS: "Performance is actually impacted with polarities that do not match listener expectancies."; "Surprisingly little is known about the impact of between- and within-individual differences on auditory display outcomes."
Comparisons with blind users:
- Zhao, Plaisant, Shneiderman & Lazar 2008, ACM TOCHI 15(1), iSonic. https://www.cs.umd.edu/~ben/papers/Zhao2008Data.pdf — case studies, not a controlled experiment. STRING-VERIFIED: "Our in-depth case studies with 7 blind users during 42 hours of data collection"; "successfully completed 90% of the tasks on the next day in a different context without any help."; "For tasks that did not require geographical knowledge, the average testing success rates were similar for iSonic and Excel, both at 86%". For geography tasks in Excel with a screen reader, SINGLE PASS: participants without geographic knowledge "resulting in an average success rate of 20%"; the "95% in iSonic" figure was returned once and not confirmed. Authors' caveat SINGLE PASS: "The participants might have made favorable comments because they wanted to please the experimenters."
- Sharif, Krishnaswamy, Aitharaju & Wobbrock, W4A 2025. https://faculty.washington.edu/wobbrock/pubs/w4a-25.01.pdf — STRING-VERIFIED: "we conducted a need-finding survey of 106 screen-reader users"; "in-depth interviews with 12 screen-reader users"; "has limited value in comprehending complex visualizations and exploring data granularly"; "63% (N=67) of respondents had never encountered sonification in online data visualizations." Abstract (SINGLE PASS on exact punctuation): "only half of respondents found sonification to be at least 'somewhat beneficial.'" SINGLE PASS: not useful "especially for complex visualizations (e.g., multi-dimensional datasets, multi-series visualizations, or geospatial maps)."
- Chundury, Jordan, Reyazuddin, Elmqvist & Lazar, ACM TACCESS 19(1), March 2026. https://par.nsf.gov/biblio/10683608 — ABSTRACT, STRING-VERIFIED against the record: "Ten blind participants completed data analysis tasks involving bar charts, pie charts, line charts, and scatterplots"; systems "a screen-reader-based chart description interface (Olli), a tablet-based audio-tactile system (TactualPlot), and a multi-line refreshable tactile display (Monarch)"; "task accuracy did not differ significantly across systems, while completion time varied substantially"; "with participants completing tasks fastest on the refreshable tactile display."
- Siu et al. 2022 and VoxLens: see C5 and C4.
BBC R&D: one search found no BBC R&D page on sonification.
Role: audio has evidence for overview and trend with training, weak evidence for detail, and no evidence that it replaces a table.

C9. Maps
Froehlich, Brock, Caspi, Guerreiro, Hara, Kirkham, Schöning & Tannert 2019, Interactions XXVI.2, p. 78. https://makeabilitylab.cs.washington.edu/media/publications/Froehlich_GrandChallengesInAccessibleMaps_2019.pdf — position paper from a CHI 2018 SIG.
- Headings, STRING-VERIFIED: "GRAND CHALLENGE ONE: DATA COLLECTION"; "GRAND CHALLENGE TWO: DATA MANAGEMENT AND OPEN STANDARDS"; "GRAND CHALLENGE THREE: MODELING NEEDS AND ABILITIES"; "GRAND CHALLENGE FOUR: ACCESSIBLE MAPS AND APPLICATION"; "GRAND CHALLENGE FIVE: USER FOCI".
- STRING-VERIFIED: "Digital maps are inherently graphical and rely on gestures or mouse inputs for interactivity, which limit their use."
- The word "choropleth" does not appear (verified NO). The paper is mostly about physical-accessibility data in maps, not thematic maps.
Evaluated screen-reader maps (Audiom, Smith-Kettlewell):
- Biggs, Toth, Stockman, Coughlan & Walker, ICAD 2022. https://www.ski.org/publication/evaluation-of-a-non-visual-auditory-choropleth-and-travel-map-viewer/ — ABSTRACT (truncated on the page). STRING-VERIFIED: "was evaluated by thirteen blind participants"; "A dynamic choropleth map of state-level US COVID-19 data". Results not reachable (PMC behind reCAPTCHA).
- Biggs, Toth, Coughlan & Walker 2026, arXiv:2605.07849 (preprint). https://arxiv.org/pdf/2605.07849 — STRING-VERIFIED: "Digital maps are used to communicate generalized spatial information and relationships, yet are commonly made "accessible" using tables that lack geographic information."; "Twenty sighted and 20 blind and low-vision individuals (BLVIs) performed tasks designed to compare visual maps, ITMs, and tables." (ITM = interactive text map, Audiom).
  Blind participants, geographic questions, STRING-VERIFIED: "substantially higher accuracy when using the ITM (M = 0.44, SD = 0.50) compared to the table (M = 0.23, SD = 0.42)."
  Sighted, STRING-VERIFIED: visual map "(M = 0.82, SD = 0.39)", ITM "(M = 0.72, SD = 0.45) compared to the table (M = 0.32, SD = 0.47)".
  Workload, STRING-VERIFIED: "Blind participants reported lower cognitive workload when using the table (M = 27.40, SD = 8.74) compared to the ITM (M = 34.10, SD = 7.69)."
  Conclusion, SINGLE PASS: "Tables should no longer be considered an acceptable alternative to a geographic map."
  Limits, SINGLE PASS: "All participants were first-time Audiom users with only 15 minutes of training"; a 2-minute timeout for blind participants only; blind group older (M=41.2 vs 20.3); numeric questions showed no significant condition effect. The first author is Audiom's developer.
- Biggs, Sloan, Oppegaard, Giudice, Coughlan & Walker 2026, Journal on Technology and Persons with Disabilities 14. https://www.ski.org/publication/17244/ — ABSTRACT. STRING-VERIFIED: "Digital geographic maps remain largely inaccessible to blind and low-vision individuals (BLVIs), despite global legislation adopting the Web Content Accessibility Guidelines (WCAG)"; "Results show that legacy methods such as tables and turn-by-turn directions fail to meet the MEP Framework criteria, while Audiom Maps, Multi-user Domain (MUD) Maps, and Audio Descriptions meet the criteria."; "15 measurable criteria".
Leaflet. https://leafletjs.com/examples/accessibility/ — SINGLE PASS: "The map container and markers are keyboard operable by default"; "The best way to discover accessibility issues is to test your maps using only a keyboard, as well as using a screen reader." Mapbox not checked.
Tactile/haptic, one line: Gorlewicz et al. 2020, ACM TACCESS 13(3). https://umaine.edu/vemi/publication/design-guidelines-and-recommendations-for-multimodal-touchscreen-based-graphics/ — ABSTRACT, SINGLE PASS: "We then present a formal user study with 22 participants with visual impairments, comparing learning performance on using touchscreen-rendered graphics to embossed graphics." The abstract states no result.
Choropleths least accessible: not stated in those words anywhere I read. Nearest measured statements: Fan et al., maps 7% (1/15) moderately-to-extremely accessible, the lowest of the main types (C5); Sharif 2025, sonification not useful for geospatial maps (C8).

C10. Populations and prevalence
Family Resources Survey 2023/24 (DWP official statistics). https://www.gov.uk/government/statistics/family-resources-survey-financial-year-2023-to-2024/family-resources-survey-financial-year-2023-to-2024 — first published 27 March 2025, "Updated 15 January 2026" (page metadata, SINGLE PASS).
- STRING-VERIFIED: "The number of disabled people rose from 11.9 million (19%) in 2013 to 2014 to 16.8 million (25%) in the most recent survey year, an increase of 4.9 million people." This is all people, not adults only.
- SINGLE PASS: "In 2023 to 2024, one in four people were disabled"; "For working-age adults, the proportion of disabled people rose from 16% in 2013 to 2014 to 24% in 2023 to 2024. The proportion of disabled State Pension age adults has remained between 42% and 46% in every year of the past decade."; children 12%.
- Definition, SINGLE PASS: "A person is considered to have a disability if they have a physical or mental impairment that has 'substantial' and 'long term' negative effects on their ability to do normal daily activities."
- Coverage, SINGLE PASS: "representative of all private households in the UK."
- Impairment types among disabled people, SINGLE PASS: working-age mental health 48%, mobility 42%, stamina/breathing/fatigue 35%; State Pension age mobility 69%, stamina 45%, dexterity 34%. Vision and hearing shares were not retrieved.
Colour vision deficiency. https://www.colourblindawareness.org/colour-blindness/ (charity; cites no source) — STRING-VERIFIED: "Colour (color) blindness (colour vision deficiency, or CVD) affects approximately 1 in 12 men (8%) and 1 in 200 women."; "approximately 3 million colour blind people (about 4.5% of the entire population)". The NHS page (last reviewed 17 March 2023) gives no prevalence. Birch 2012 unreachable (PubMed behind reCAPTCHA).
Dyslexia. https://www.bdadyslexia.org.uk/dyslexia — STRING-VERIFIED: "Ten percent of the population are believed to be dyslexic, but it is still often poorly understood." No source or date; note "believed".
Vestibular. NIDCD https://www.nidcd.nih.gov/health/balance-disorders (last updated March 6, 2018) — STRING-VERIFIED: "About 15 percent of American adults (33 million) had a balance or dizziness problem in 2008." VeDA https://vestibular.org/article/what-is-vestibular/about-vestibular-disorders/ — STRING-VERIFIED: "One large epidemiological study estimates that as many as 35% adults aged 40 years or older in the United States—approximately 69 million Americans—have experienced some form of vestibular dysfunction." (citing Agrawal et al., Arch Intern Med 2009;169(10):938-944). Both US; no UK figure found.
Sight loss, UK. RNIB statistics page UNREACHABLE (script-rendered, two attempts). House of Commons Library, CDP-2022-0238, 9 December 2022, https://commonslibrary.parliament.uk/research-briefings/cdp-2022-0238/ — STRING-VERIFIED: "The NHS has estimated that more than 2 million people are living with sight loss in the UK."; "Of these, around 340,000 are registered as blind or partially sighted." No definition of "sight loss" retrieved.
WebAIM Screen Reader User Survey #10. https://webaim.org/projects/screenreadersurvey10/ — self-selected survey.
- STRING-VERIFIED: "In December 2023 and January 2024, WebAIM surveyed preferences of screen reader users. We received 1539 valid responses."
- Primary screen reader, STRING-VERIFIED: JAWS 40.5%, NVDA 37.7%, VoiceOver 9.7%. Commonly used, STRING-VERIFIED: NVDA 65.6%, JAWS 60.5%.
- Browser, SINGLE PASS: Chrome 52.3%, Edge 19.3%, Firefox 16.0%, Safari 8.0%.
- STRING-VERIFIED: "91.3% of respondents report using a screen reader on a mobile device." Mobile platform SINGLE PASS: iOS 70.6%, Android 27.6%.
- Finding information on a long page, STRING-VERIFIED: "Navigate through the headings on the page" 71.6%. Others SINGLE PASS: Find 13.6%, read through 6.4%, links 4.8%, landmarks 3.7%.
- SINGLE PASS: heading levels "88.8% of respondents find them very or somewhat useful"; 89.9% use a screen reader because of a disability; respondents 47.2% North America, 30.7% Europe; CAPTCHA top of the problematic-items list.
- Overlays: the word does not appear in Survey #10 (verified NO). WebAIM Survey of Web Accessibility Practitioners #3, https://webaim.org/projects/practitionersurvey3/ — STRING-VERIFIED: "In January 2021, WebAIM conducted a survey of web accessibility practitioners. We received 758 valid responses to this survey."; "A strong majority (67%) of respondents rate these tools as not at all or not very effective. Respondents with disabilities were even less favorable with 72% rating them not at all or not very effective, and only 2.4% rating them as very effective."
WebAIM Million (automated WAVE scan of one million home pages).
- 2025, https://webaim.org/projects/million/2025 — STRING-VERIFIED: "94.8% of home pages had detected WCAG 2 failures." SINGLE PASS: "50,960,288 distinct accessibility errors were detected—an average of 51 errors per page."; low contrast text 79.1%, missing alternative text 55.5%, missing form input labels 48.2%, empty links 45.4%, empty buttons 29.6%, missing document language 15.8%; "96% of all errors detected fall into these six categories."; "an average of 1257 elements per home page in February 2025."
- 2026 (current page), https://webaim.org/projects/million/ — "Results below are from February 2026". STRING-VERIFIED: "95.9% of home pages had detected WCAG 2 failures."; "Across the one million home pages, 56,114,377 distinct accessibility errors were detected—an average of 56.1 errors per page."; "96% of all errors detected fall into these six categories."; six values confirmed: low contrast 83.9%, missing alt text 53.1%, missing form labels 51%, empty links 46.3%, empty buttons 30.6%, missing document language 13.5%; "Home pages with ARIA present had significantly more errors (59.1 on average) than pages without ARIA (42 on average)."

C11. Convergence — does accessible design help non-disabled readers?
Schmutz, Sonderegger & Sauer 2016, Human Factors 58(4), 611–629. https://journals.sagepub.com/doi/10.1177/0018720816640962 — ABSTRACT, all STRING-VERIFIED:
- "Sixty-one nondisabled participants used one of three Web sites differing in levels of accessibility (high, low, and very low)"
- "A high level of Web accessibility led to better performance (i.e., task completion time and task completion rate) than low or very low accessibility"
- "Likewise, high Web accessibility improved user ratings (i.e., perceived usability, aesthetics, workload, and trustworthiness) compared to low or very low Web accessibility."
- "may provide benefits to users without disabilities"
- No effect sizes in the abstract.
Schmutz, Sonderegger & Sauer 2017, Human Factors 59(6), 956–972. https://journals.sagepub.com/doi/10.1177/0018720817708397 — ABSTRACT, STRING-VERIFIED:
- "Participants from two matched samples, comprising 55 participants with visual impairments and 55 without impairments, took part in a synchronous remote testing of a Web site."
- "Each participant was randomly assigned to one of three Web sites, which differed in the level of accessibility (very low, low, and high) according to recommendations of the well-established Web Content Accessibility Guidelines 2.0 (WCAG 2.0)."
- "Higher conformance to Web accessibility guidelines resulted in increased performance and more positive user ratings (e.g., perceived usability or aesthetics) for both user groups."
- "Higher conformance to WCAG 2.0 may result in benefits for nondisabled users and users with visual impairments alike."
Schmutz, Sonderegger & Sauer 2018, Ergonomics 61(5), 697–709 (online 24 November 2017; Crossref metadata). Abstract UNREACHABLE (Taylor & Francis 403; Crossref and Semantic Scholar hold no abstract). Nothing quoted.
Counter-finding: Schmutz, Sonderegger & Sauer 2019, Applied Ergonomics 74, 97–106, "Easy-to-Read Language in Disability-Friendly Web Sites: Effects on Nondisabled Users" (citation from https://www.unifr.ch/psycho/en/research/cogerg/publication.html). Source unreachable (ScienceDirect robots; PubMed reCAPTCHA). Secondary only: González-Sordé 2025, Universal Access in the Information Society, https://link.springer.com/article/10.1007/s10209-024-01129-8 quotes it — STRING-VERIFIED in that article: "but also to increased reading time, decreased text liking and reduced intention to revisit the web site". So the same lab found a cost to non-disabled users from easy-to-read language. Needs checking at source.
Ekin, Krejtz, Duarte, Pereira, Marcus-Quinn & Krejtz, PLOS ONE 20(7) e0328552, 30 July 2025. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0328552 — STRING-VERIFIED: "The study involved 20 participants reading news websites"; "cognitive engagement declined over time when no accessibility enhancements were present". Small sample; SINGLE PASS "Twenty non-native English-speaking participants were recruited".
Captions:
- Ofcom, "Television Access Services: Review of the Code and Guidance", consultation, "Publication date: 23 March 2006". https://www.ofcom.org.uk/siteassets/resources/documents/consultations/uncategorised/8639-accessservs/summary/access.pdf?v=321957 — STRING-VERIFIED, paragraph 1.9: "On the basis of the quantative research, the researchers concluded that most people were aware of subtitles, and about 7.5 million people had used them to watch television, of whom about 6 million did not have a hearing impairment." ("quantative" as printed). Note the verb is "had used", not "use". SINGLE PASS: "a nationally representative random sample of 4,365 adults (aged 15 and over) throughout the UK". The research is Ipsos MORI for Ofcom; my two passes disagreed on the footnote number and on March 2005 versus March 2006, so that detail is unconfirmed.
- Stagetext, 15 March 2023. https://www.stagetext.org/news/yougov-survey-supports-stagetexts-findings/ — STRING-VERIFIED: "A survey Stagetext commissioned in 2021 found that 80% of 18- to 24-year-olds 'use subtitles some or all of the time watching TV on any device'."; "In the case of Stagetext's survey, 10% of the 80% of 18- to 24-year-olds told us that they were deaf, deafened or hard of hearing."; "The result was 61% of 18- to 24-year-olds said they had 'subtitles on'." (YouGov, February 2023). The age band is 18–24 on Stagetext's own page; "18-25" appears only in a Stagetext social post title seen in search results. Sapio Research is not named on any page I fetched. Secondary (Limping Chicken, 15 November 2021, SINGLE PASS): "The representative poll of 2,003 people, commissioned by Stagetext". BBC News article blocked.
- Gernsbacher 2015, Policy Insights from the Behavioral and Brain Sciences 2(1), 195–202. https://journals.sagepub.com/doi/10.1177/2372732215602130 — ABSTRACT, STRING-VERIFIED: "benefit everyone who watches videos (children, adolescents, college students, and adults)"; "More than 100 empirical studies document that captioning a video improves comprehension of, attention to, and memory for the video". A review, not a meta-analysis.
Plain language:
- GOV.UK guidance has moved: gov.uk/guidance/content-design/writing-for-gov-uk now redirects to https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/clear-language/ ("Use clear language"; no date on page). STRING-VERIFIED there: "people with higher levels of literacy prefer plain English because it allows them to understand the information as quickly as possible"; "80% of people preferred sentences written in clear English"; "Plain English is mandatory for all of GOV.UK."; "1 in 6 adults in England have very poor literacy skills". "Reading age", "5,000" and "age 9" do not appear on that page (verified NO), and the section index lists no "how people read" page.
- Its sources: GDS blog guest post, Mark Morris, 17 February 2014, https://gds.blog.gov.uk/2014/02/17/guest-post-clarity-is-king-the-evidence-that-reveals-the-desperate-need-to-re-think-the-way-we-write/ — STRING-VERIFIED: "First, when given a choice, 80% of people preferred sentences written in clear English (for example, 97% preferred 'among other things' over the more traditional Latin phrase 'inter alia')"; "the more educated the person, the more specialist their knowledge, the greater their preference for plain English". Underlying study: Trudeau, "The Public Speaks: An Empirical Study of Legal Communication", 14 Scribes J. Leg. Writing 121 (2011-2012), https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1843415 — ABSTRACT, STRING-VERIFIED: "analyzes the 376 responses to the survey". The 80% is a preference in a US legal-writing survey of 376 responses; it is not a comprehension measure and does not appear in the SSRN abstract.
Role: convergence is measured for WCAG conformance (two experiments, one lab, n = 61 and 110) and asserted for captions; it is not measured for charts or dashboards anywhere I found, and one study from the same lab suggests a cost for easy-to-read text.

C12. Dyslexia and typography
BDA "Dyslexia Style Guide 2023". https://www.bdadyslexia.org.uk/advice/employers/creating-a-dyslexia-friendly-workplace/dyslexia-friendly-style-guide — charity guidance; no evidence cited on the page. All STRING-VERIFIED:
- "Use sans serif fonts, such as Arial and Comic Sans, as letters can appear less crowded"
- "Font size should be 12-14 point or equivalent (e.g. 1-1.2em / 16-19 px)"
- line spacing: "It should be proportional to inter-word spacing; 1.5/150% is preferable."
- "Left align text, without justification"
- "Use dark coloured text on a light (not white) background"; "White can appear too dazzling"
- "Write short simple sentences: 60 to 70 characters is optimal." (as printed this is about sentences, not line length)
- "Avoid green and red/pink, as these colours are difficult for those who have colour vision deficiencies (colour blindness)."
- "Adopting these principles for dyslexic readers has the advantage of making all written communication easier on the eye for everyone."
- The guide does not mention OpenDyslexic or Dyslexie (verified NO).
- SINGLE PASS: "Avoid underlining and italics as this can make the text appear to run together and cause crowding. Use bold for emphasis."; headings "at least 20% larger than the normal text"; letter spacing "ideally around 35% of the average letter width".
Rello & Baeza-Yates, ASSETS 2013. http://dyslexiahelp.umich.edu/sites/default/files/good_fonts_for_dyslexia_study.pdf — peer-reviewed; Spanish texts.
- STRING-VERIFIED: "Using a within-subject design, 48 subjects with dyslexia read 12 texts with 12 different fonts."
- STRING-VERIFIED: "Sans serif, monospaced and roman font styles significantly improved the reading performance over serif, proportional and italic fonts."
- STRING-VERIFIED: "The fonts designed specifically for dyslexia, OpenDys and OpenDys It., did not lead to a better or worse readability. As in [21], OpenDys did not lead to a faster reading."
- STRING-VERIFIED: "In particular, Arial It. should be avoided since it significantly decreases readability."
- STRING-VERIFIED: "Good fonts for people with dyslexia are Helvetica, Courier, Arial, Verdana and CMU, taking into consideration both, reading performance and subjective preferences."
- Comprehension was a control variable, not an outcome.
Rello & Baeza-Yates, ACM TACCESS 8(4), Article 15, 2016. https://www.superarladislexia.org/pdf/2016-Luz%20Rello-Fonts-taccess.pdf
- STRING-VERIFIED: "97 subjects (48 with dyslexia) read 12 texts with 12 different fonts"; "Font types have an impact on readability for people with and without dyslexia"; "For the tested fonts, sans serif, monospaced, and roman font styles significantly improved the reading performance over serif, proportional, and italic fonts."; "The fonts that are more readable for people with dyslexia are also beneficial for people without dyslexia."; "The fonts designed specifically for dyslexia, OpenDys and OpenDys It., did not lead to better or worse readability."
- This is a direct convergence finding for typeface.
Rello, Pielot & Marcos, CHI 2016, "Make It Big!". https://pielot.org/pubs/Rello2016-Fontsize.pdf — participants did not have dyslexia.
- STRING-VERIFIED: "We report from an eye-tracking experiment with 104 participants"; "On the basis of our results, we recommend to use at least 18-point font size for the text body of websites."; "For line spacing, we found marginal effects, suggesting that the two tested extremes (0.8 and 1.8) impair readability."
- SINGLE PASS: "we replicated this experimental setting with smaller group of 28 people who were diagnosed dyslexia and found similar effects of font size."
- This sits above the BDA's 12–14 point.
Kuster, van Weerdenburg, Gompel & Bosman 2018, Annals of Dyslexia (open access). https://link.springer.com/article/10.1007/s11881-017-0154-6 — all STRING-VERIFIED:
- "In Experiment 1, children with dyslexia (n = 170) did not read text written in Dyslexie font faster or more accurately than in Arial font."
- "In Experiment 2, children with (n = 102) and without dyslexia (n = 45) read word lists in three different font types (Dyslexie, Arial, Times New Roman)."
- "Words written in Dyslexie font were not read faster or more accurately."
- "These experiments clearly justify the conclusion that the Dyslexie font neither benefits nor impedes the reading process of children with and without dyslexia."
Wery & Diliberto 2017, Annals of Dyslexia 67(2), 114–127. ERIC record https://eric.ed.gov/?id=EJ1156546 — ABSTRACT, STRING-VERIFIED: "A single-subject alternating treatment design was used"; "Results from this alternating treatment experiment show no improvement in reading rate or accuracy for individual students with dyslexia, as well as the group as a whole."; "None of the participants reported preferring to read material presented in that font." The abstract gives no n.

Also asked
- Screen-reader time on a table versus a chart description: no study measuring this directly was found. Nearest: Sharif 2021 (210.96% more time than sighted users on charts); VoxLens (84.6 s versus 54.1 s); Zong 2022 (table easier than multi-view, with reported memory load); Biggs 2026 (table lower workload but lower geographic accuracy); Chundury 2026 (accuracy equal, time varied by device); Fan 2023 (auditors 25 minutes per visualization). Wang, Jung, Wang & Kim, CHI 2022, "What makes web data tables accessible?" (https://pages.cs.wisc.edu/~yeaseulkim/assets/papers/2022_make_table_accessible.pdf, SINGLE PASS): 13 interviewees, 5 evaluators, no timing or accuracy measures.
- "Text-only" or separate accessible versions being worse maintained or less used: no empirical study found in one search. What is written:
  W3C, Understanding Conformance, https://www.w3.org/WAI/WCAG22/Understanding/conformance — STRING-VERIFIED: "Note that providing an alternate version is a fallback option for conformance to WCAG and the preferred method of conformance is to make all content directly accessible."; the definition requires that the alternate "is as up to date as the non-conforming content". The page says nothing about alternate versions being out of date in practice (verified NO).
  US Department of Justice fact sheet on the ADA Title II web rule, April 08, 2024 (US, not UK), https://www.ada.gov/resources/2024-03-08-web-rule/ — STRING-VERIFIED: "Under the rule, state and local governments may use conforming alternate versions as an alternative to inaccessible content only in very limited circumstances."; "Usually state and local governments should not have a main web page that is inaccessible and a separate accessible version of the same content, because people with disabilities should get equal access to that content on the same page."
- ISO/IEC 30071-1:2019. https://www.iso.org/standard/70913.html — title SINGLE PASS: "Information technology — Development of user interface accessibility — Part 1: Code of practice for creating accessible ICT products and services". STRING-VERIFIED: "This document takes a holistic approach to the accessibility of information and communications technology (ICT) by combining guidance on implementing" (first fragment of the abstract). Status SINGLE PASS: "90.93 2024-09-17 International Standard confirmed"; "This publication was last reviewed and confirmed in 2024."

Unasked threads
1. A 2026 preprint tests the "table as the accessible map" assumption directly (Biggs et al., arXiv:2605.07849, C9): blind participants answered geographic questions at 0.44 with an interactive text map versus 0.23 with a table, though the table cost less workload and numeric questions showed no difference.
2. In Fan et al.'s survey of 127 screen-reader users, the most frequently preferred way to access data was tactile graphics (n = 50), ahead of Braille (25), audio (15) and screen reader (7).
3. Half of 106 screen-reader users in Sharif et al. 2025 were unfamiliar with sonification and 63% had never met it on the web; only about half found it at least somewhat beneficial.
4. Mack et al. 2021: authors wrote significantly worse alt text when started from machine-generated alt text (2.38 versus 2.96).
5. The WebAIM Million worsened between 2025 and 2026: 94.8% to 95.9% of home pages with detected failures, 51 to 56.1 errors per page, low-contrast text 79.1% to 83.9%.
6. GOV.UK's content guidance has moved to guidance.publishing.service.gov.uk and the "reading age" rationale is not on the replacement "Use clear language" page; anything citing "reading age of 9" to GOV.UK needs a live source.
7. Chartability's site lists "No table" and "Reading level inappropriate" among its 14 critical failures, alongside contrast and keyboard issues.
8. The Stagetext figure usually quoted as "four in five 18–25s" is "80% of 18- to 24-year-olds" on Stagetext's own page, and Stagetext says a tenth of that 80% were deaf, deafened or hard of hearing.

Left out
- Flowers 2005: unreachable (icad.org).
- RNIB statistics page: script-rendered; House of Commons Library used instead.
- Birch 2012 and the NHS for colour vision prevalence: PubMed blocked; NHS page has no figure.
- Schmutz 2018 (Ergonomics) abstract and Schmutz 2019 (Applied Ergonomics) at source: publishers blocked.
- Biggs 2022 ICAD results beyond the truncated abstract.
- Holloway et al. "Infosonics", Mapbox accessibility documentation, any US plain-language comprehension trial, and BBC R&D: not pursued or not found within the ration.
- Departures from the two-attempt rule, disclosed: for Wery & Diliberto (PMC and Europe PMC failed) I used a third host, ERIC, found by search; for Biggs 2022 (PMC and Semantic Scholar failed) a third host, ski.org; for Schmutz 2018 three hosts were tried without success.
- I tried three guessed arXiv IDs that were wrong (discarded), and the arXiv API and curl were blocked, so discovery relied on WebSearch.

Rich references
1. Fan et al. 2023, ACM TACCESS — audit of 87 visualizations, survey of 127 screen-reader users, contextual inquiry with 12; per-chart-type accessibility ratings, including maps and tables. https://shape.stanford.edu/research/DataAccessibility/Fan2023_TheAccessibilityOfDataVisualizationsOnTheWeb.pdf
2. Lundgard & Satyanarayan 2022, accessible HTML version — the four-level model and the blind/sighted ranking divergence. http://vis.csail.mit.edu/pubs/vis-text-model/
3. Schmutz, Sonderegger & Sauer 2017, Human Factors 59(6) — the only matched disabled/non-disabled experiment on WCAG conformance found; read with their 2019 easy-to-read paper for the counter-case. https://journals.sagepub.com/doi/10.1177/0018720817708397

Surprised
- The best-known "rich screen reader" paper's only significant quantitative result favours the plain table on ease of use; the case against tables there is qualitative.
- VoxLens's 122% improvement is measured against a different study's participants, not a control group.
- The convergence claim rests on very little: two experiments from one Swiss lab for WCAG, a typeface study for dyslexia, and reviews for captions; the same lab reports a cost for easy-to-read language. Nothing measures convergence for charts.
- No source reviewed says "choropleths are the least accessible form"; the evidence is about "maps" generally (1 of 15 rated accessible).
- The Ofcom caption figure is real and traceable (2006, paragraph 1.9), but it says people "had used" subtitles, from a survey of 4,365 adults — weaker than the "7.5 million use subtitles" it is usually turned into.
- The BDA's dyslexia prevalence is worded "believed to be" and unsourced, and its style guide's 12–14 point sits below the "at least 18-point" recommended by the one large eye-tracking study.

WebSearch calls used: 26.

---

## Agent D

AGENT D REPORT — OFFICIAL AND NEWSROOM PRACTICE (Chapter 13)

All sources fetched 6 October 2026. WebSearch calls used: 25 of 30.

Method note. Direct download (curl) is blocked by the proxy, so every check was a second WebFetch pass with a YES/NO presence prompt and false control strings. STRING-VERIFIED therefore means "confirmed present on a second, separate read by the fetch reader", not a byte-level grep. SINGLE PASS means read once, or reproduced identically on two reads without a presence check. The reader did invent sentences on first pass in at least two places (Service Standard point 5; the ONS statement); both were caught and are corrected below.

---------------------------------------------------------------
D1. ONS SERVICE MANUAL
---------------------------------------------------------------

The sentence is not the ONS's. "Dashboards rarely meet full accessibility requirements" does not appear in the ONS service manual; the word "rarely" is absent from its dashboards page (control-checked). It belongs to the Analysis Function (see D2). The chapter should re-attribute it.

ONS dashboards page — https://service-manual.ons.gov.uk/data-visualisation/guidance/dashboards (official practice; no date on page)
- Under "Disadvantages of dashboards", in the list introduced by "Dashboards can be problematic, as they:" — «are difficult to make accessible and responsive for different devices» STRING-VERIFIED
- «In most cases it is better to use charts that provide users with specific insights» STRING-VERIFIED
- «they put the burden of interpreting and understanding data onto the user» STRING-VERIFIED
- Under "Tips for creating a dashboard": «always make sure any dashboard design meets accessibility standards» STRING-VERIFIED
- Role: the ONS's true wording is "difficult to make accessible", a weaker admission than the Analysis Function's.

ONS interactive charts — https://service-manual.ons.gov.uk/data-visualisation/guidance/interactive-charts-and-animations (no date)
- «Only consider using an interactive chart where the most important information for the user cannot be clearly shown through a non-interactive chart.» STRING-VERIFIED
- Disadvantages include «hide the main messages from users» STRING-VERIFIED
- «Expert users will be able to download and explore the data.» STRING-VERIFIED
- «Never make an animation the only way to get the information.» STRING-VERIFIED
- «This does not include charts where the only interactive element is a tooltip.» and «A tooltip displays data values when the user hovers over or selects part of a chart.» SINGLE PASS
- Tip: «consider starting your visualisation from a view that either shows the main message without needing any interaction, or helps users navigate the chart» SINGLE PASS
- The page states no accessibility rule for interactive charts: the reader found no occurrence of "keyboard", "screen reader", "text alternative" or "mobile".

ONS on alt text — https://service-manual.ons.gov.uk/data-visualisation/guidance/chart-text
The brief's guess is the wrong way round: the ONS requires alt text, in a fixed formula. It is the Analysis Function that prefers body text over the alt attribute.
- «Chart alternative text (alt text) is an accessible text description of a chart on a page.» SINGLE PASS (identical on two reads)
- «Use chart alt text to provide a specific description of the type of chart and the main trend that it is showing.» SINGLE PASS
- «A chart alt text sentence should be between 100 and 200 characters and always end with a full stop.» STRING-VERIFIED
- «Use the format "A [chart type] showing that [chart title]."» SINGLE PASS (two reads)
- Control «Do not use alt text for charts» — absent.
- «Each chart must include the source of the data directly after the chart.» SINGLE PASS
- Interactive tools: «For some interactive tools, it may not be possible or useful to provide a title that describes a trend.» SINGLE PASS

ONS chart component — https://service-manual.ons.gov.uk/design-system/components/bar-chart-component
- Parameter "description", required: «A textual description of the chart for screen readers» STRING-VERIFIED
- «Use the Tab key to move focus into the chart. Once inside, use the arrow keys to navigate between data points.» STRING-VERIFIED
- Download formats include «Image (PNG format, 25KB)» STRING-VERIFIED; XLSX and CSV options SINGLE PASS
- The reader reports the component is built on Highcharts (a "data-highcharts-config" attribute) and that no sonification is mentioned. Both are the reader's reading, not quotations.

ons.gov.uk accessibility statement — https://www.ons.gov.uk/help/accessibility-statement (same content at /help/accessibility)
- «This website is partially compliant with the Web Content Accessibility Guidelines (WCAG) version 2.2 AA standard» STRING-VERIFIED; continues «, because of the non-compliances and the exemptions listed in this statement.» SINGLE PASS
- «some of our previously accessible data visualisations published since 23 September 2020 may not be fully accessible» STRING-VERIFIED (context: WCAG 2.2 criterion 2.5.8 target size)
- «Some of our data visualisations may not load or function correctly for users who have JavaScript disabled.» STRING-VERIFIED
- «This is particularly the case for our more advanced interactive tools such as Explore local statistics, Build a custom area profile and Census maps, which use dynamic user interactions as a core function of the product.» Fragment «which use dynamic user interactions» STRING-VERIFIED; rest SINGLE PASS
- «In all instances, the underlying data are accessible through other formats, such as the accompanying dataset files and the surrounding commentary on the HTML web page.» STRING-VERIFIED
- Disproportionate burden: «There are many historical data visualisations on the site published between 23 September 2018 and 23 September 2020 that may not be compliant with WCAG 2.2 level AA standards.» SINGLE PASS. Fragment «we believe that this would be a disproportionate burden» confirmed on second pass; the full sentence wording is not settled.
- «We will be introducing a new website platform and content management system in 2026 and are currently in the Discovery phase for data visualisations.» SINGLE PASS
- Dates (SINGLE PASS, two reads): prepared 19 September 2020; last reviewed December 2025; last tested March 2024 by Digital Accessibility Centre (DAC).

"Accessible charts" page: none exists. The sitemap lists only "Accessibility statement", "Accessible PDF design" and "Accessible text formatting"; /accessibility returns 404.

---------------------------------------------------------------
D2. ANALYSIS FUNCTION
---------------------------------------------------------------

(i) Dashboards — https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-building-and-managing-dashboards/ (page gives 6 February 2026, SINGLE PASS)
- Under "What we mean by 'dashboard'": «Dashboards rarely meet full accessibility requirements.» STRING-VERIFIED
- Followed by "This means you should:" «not publish a dashboard without the data being available in another form» STRING-VERIFIED and «consider a statistical bulletin to accompany your dashboard» SINGLE PASS
- No tool is named on this page.

(ii) Dashboard software — https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-dashboard-software/ (6 February 2026, SINGLE PASS), section "Accessibility"
- «External dashboards must meet WCAG 2.2 guidelines» STRING-VERIFIED
- «Open-source languages (such as R, and Python) will give greater control over accessibility» STRING-VERIFIED
- «Out-of-the-box options (such as Power BI) come with some accessibility features built in, but they can be difficult to customise» STRING-VERIFIED
- «accessibility features are available but are not always used by analysts in a way that meets the WCAG 2.2 requirements» STRING-VERIFIED
- «users who are reliant on keyboards or assistive software can find it difficult to interact with these dashboards» STRING-VERIFIED
- Power BI limitation: «has a limited Accessibility Checker which does not cover all possible issues» STRING-VERIFIED
- Tableau is not mentioned. Control «Power BI is fully compliant with WCAG 2.2» absent.

(iii) DataConnect22 Q&A — https://analysisfunction.civilservice.gov.uk/support/making-charts-accessible-dataconnect22 (reader gives September 2022; unnamed answerer)
- «It is hard to make dynamic charts and dashboards fully accessible.» STRING-VERIFIED
- «I have been looking into it but I am yet to find a fully accessible dashboard.» STRING-VERIFIED
- Tip: «Be up front about the lack of accessibility – make sure your accessibility statement says what is and is not accessible» SINGLE PASS
- «If you have a text alternative to the chart you should not need to repeat it.» STRING-VERIFIED
- On per-chart downloads: «But it is not necessary for accessibility, unless you are relying on the data download as the text alternative.» STRING-VERIFIED

(iv) Making analytical publications accessible — https://analysisfunction.civilservice.gov.uk/policy-store/making-analytical-publications-accessible/ (29 October 2020, SINGLE PASS)
- «Alternative text is often thought of as the text that sits in the code behind an image, but really it refers to any text that describes non-text content.» SINGLE PASS (two reads)
- Charts can meet 1.1.1 by a table or «a text description of the message the chart is presenting» STRING-VERIFIED
- «Which you choose should depend on what you would expect a non-disabled user to get from the chart.» STRING-VERIFIED
- «We advise that it should live in the body text rather than in the alt attribute.» STRING-VERIFIED
- «The text description should never be in both the alt attribute and the body text» + «as this causes auditory clutter for screen reader users» STRING-VERIFIED
- «It should also never be in a caption as screen readers do not always pick up on these.» STRING-VERIFIED
- «The text description should provide the same level of understanding a user would get if they looked at the chart.» SINGLE PASS (two reads)
- «It should not: be a literal description of the chart; outline every data point shown» confirmed on two reads
- «There is no specific character limit for the text description of a chart as charts can be complex.» STRING-VERIFIED
- «It is best practice to provide the data displayed in each chart as an accessible data download.» STRING-VERIFIED
- Text in images: «The accessibility success criteria state that images of text should only be used when essential or when the image can be customised.» SINGLE PASS. «This means titles should be in the body of the page or document, as opposed to within an image.» STRING-VERIFIED
- The cost it admits: «This does mean an image of a chart can be taken out of context if it is copied and pasted elsewhere.» SINGLE PASS. «Therefore, we prioritise accessibility and advise for the title and subtitle to be in the body text.» STRING-VERIFIED
- «Chart labels and annotations can be considered essential images of text» STRING-VERIFIED
- HTML first: «If the website you publish on has the functionality to build charts with HTML code and this is known to meet accessibility standards, you should use it.» STRING-VERIFIED
- «Using the SVG format is not explicitly mentioned in the accessibility guidelines but we consider it the most accessible option for images of charts.» STRING-VERIFIED
- Alternative versions are allowed, for spreadsheets only: «If your current spreadsheet document does not meet the accessibility guidelines but you feel that it does assist your users, you can publish two versions of the same document.» «One that meets the accessibility guidelines and one that does not.» Both STRING-VERIFIED. The reader reports these two sentences are the whole section.

(v) Data visualisation: charts — https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/ (19 May 2022, SINGLE PASS)
- «Many of the success criterion relevant to publishing charts are related to colour contrast.» STRING-VERIFIED
- «It means all text related to the chart should be in the body text of the webpage unless it is essential for it to be in the image.» STRING-VERIFIED
- «In this situation the image of the chart should be marked as decorative and therefore hidden from screen reader software.» STRING-VERIFIED
- «This is because legends use colour to match labels to data. This fails accessibility success criterion 1.4.1.» STRING-VERIFIED
- «In general, we should not rely on colour as the only way to match labels to data.» STRING-VERIFIED
- «when writing the chart's alternative text you should incorporate any messages given by annotation» STRING-VERIFIED
- «You should link to a data download underneath each chart.» SINGLE PASS
- No section on interactive charts, tooltips or keyboard appears in the heading list.

(vi) Releasing statistics in spreadsheets — https://analysisfunction.civilservice.gov.uk/policy-store/releasing-statistics-in-spreadsheets/ (30 June 2021, SINGLE PASS). All STRING-VERIFIED:
- «It is best practice to have one table per worksheet»
- «Restructure your tables so there are no split cells, merged cells or nested tables.»
- «Remove all blank rows and blank columns within tables.»
- «Ensure all tables in your spreadsheet are 'marked up' as a table»
- «Colour is never used as the only way to communicate a message.»
- «No columns or rows are hidden from view.»
SINGLE PASS: «Images within spreadsheets should be avoided. Generally the best place for any analysis or data visualisations is in HTML.»

---------------------------------------------------------------
D3. WHAT OFFICIAL DASHBOARDS DECLARE THEY DO NOT MEET
---------------------------------------------------------------

(a) UKHSA data dashboard — https://ukhsa-dashboard.data.gov.uk/accessibility-statement
- «This website is partially compliant with the Web Content Accessibility Guidelines version 2.2 AA standard, due to the non-compliances listed below.» STRING-VERIFIED
- «some charts present on the dashboards use colour alone to differentiate between lines on the chart. This may make some chart content particularly difficult for some colourblind users to interpret. This fails WCAG 1.4.1 Use of Colour (A).» SINGLE PASS
- The other listed failures concern the API page (reflow, resize, heading structure) — paraphrase, SINGLE PASS.
- «At this time, we have made no claims of disproportionate burden.» STRING-VERIFIED
- «This statement was prepared on Tuesday, 19 December 2023. It was last reviewed on Tuesday, 19 December 2023.» Date and «All Able Ltd» STRING-VERIFIED; last tested 12 December 2023 SINGLE PASS.
- Nothing on maps, alt text or tabular views. No review is shown since December 2023.

(b), (c) ONS Census maps and Explore Local Statistics. No separate statement was reachable (the Census maps page renders only "Loading..."; the beta Explore Local Statistics statement URL is 404). Both are named in the ons.gov.uk statement quoted in D1, which is the official admission for them.

(d) OHID Fingertips — https://fingertips.phe.org.uk/profile/guidance/supporting-information/site-accessibility-statement
- «This website is partially compliant with the Web Content Accessibility Guidelines version 2.1 AA standard» STRING-VERIFIED (still 2.1)
- «Interactive elements within data tables are not keyboard operable» (2.1.1) STRING-VERIFIED
- «Relationship between information in data table cells is not always clear to those using a screen reader» (1.3.1) STRING-VERIFIED
- «Colour is the only method used for conveying information within some tables» (1.4.1) STRING-VERIFIED
- SINGLE PASS: contrast 1.4.3; no visible focus 2.4.7; no skip link 2.4.1; form labels 1.3.1; Parsing 4.1.1.
- The reader found no mention of charts or maps, no dates, no tester, no disproportionate burden claim.

(e) Public Health Scotland — https://publichealthscotland.scot/accessibility-statement-for-public-health-scotland/ (the richest list found)
- «This website is partially compliant with the Web Content Accessibility Guidelines version 2.2 AA standard» STRING-VERIFIED
- «The R dashboards currently published on this website have a range of accessibility issues and fail the following WCAG 2.2 success criteria» STRING-VERIFIED
- R dashboard items, STRING-VERIFIED: «Title of the graph is not communicated to screen reader users as it is an image of text.» (1.3.1, 1.4.5); «The graph is not announced by screen reader.» (1.1.1, 1.4.5); «Slider widget is inoperable with screen reader activated.» (2.1.1)
- R dashboard items, SINGLE PASS: «Dropdown menu is inoperable using standard keyboard gestures.»; «Dynamic content is not announced.» (4.1.3); «No visible focus indicator.»; «Use of colour alone.» (1.4.1); «Content overlapping at 400% browser zoom.» (1.4.10); «Downloadable files are not announced by the screen reader.» The reader returned 32 bullets.
- «The Tableau dashboards currently published on this website have a range of accessibility issues» STRING-VERIFIED
- Tableau items: «Screen reader users do not have access to tooltip information.» STRING-VERIFIED. SINGLE PASS: «Content is not announced by screen reader.»; «Text spacing cannot be applied to the interactive application on the Tableau dashboard.» (1.4.12); «Use of colour alone to convey content.»; «Insufficient page title.»
- «This statement was prepared on 18 May 2026.» and «This website was last tested on 29 July 2025.» STRING-VERIFIED. Tested by «our User-centred Design team» SINGLE PASS.
- No disproportionate burden claim. One bullet still carries «aiming to fix by 31 May 2023» (SINGLE PASS).
- ScotPHO's own statement: unreachable (two scotpho.org.uk URLs 404; the Shiny app is not readable).

(f) Council Power BI examples
Scottish Borders Council — https://www.scotborders.gov.uk/access-information/accessibility-statement/1 (all STRING-VERIFIED)
- «This site uses Microsoft Power BI dashboards to visualise data and move through different areas of interest.»
- «Visitors using screen reader software or a keyboard will not be able to interact with them in the same way.»
- Mapping and zoom features «do not have an equivalent for keyboard only or screen reader users»
- «Some graphs and charts within PowerBI dashboards rely solely on colour to convey information.»
- «We do however describe trends in associated research reports or consider alternative format requests.»
- Prepared «29 May 2025»; tested by «Shaw Trust Accessibility Services» (test date 7 January 2025 SINGLE PASS). Disproportionate burden: «We have not identified any content that meets the criteria for disproportionate burden.» SINGLE PASS
Kingston Data (Royal Borough of Kingston upon Thames) — https://data.kingston.gov.uk/accessibility-statement
- «This website is partially compliant with the Web Content Accessibility Guidelines version 2.2 AA standard» STRING-VERIFIED
- «Power BI has known accessibility limitations which will be kept under review» SINGLE PASS
- «longer strings of alternative text may be cut off when using a screen reader» (1.1.1) STRING-VERIFIED
- «The frame does not reflow when zoomed in at high levels.» (1.4.10) STRING-VERIFIED
- «Dashboard titles do not appear in the window title bar or as browser tab names.» (2.4.2) STRING-VERIFIED
- «Whilst the dashboards can be navigated using just a keyboard, this functionality can be complex when interacting with certain user interface components.» SINGLE PASS
- «We currently are not claiming disproportionate burden on any area of the Kingston Data Website.» STRING-VERIFIED. Prepared 03/07/2023; reviewed and tested 18/02/2026 by the council's own team (SINGLE PASS).

Pattern across the set: every statement says "partially compliant". The only disproportionate-burden claim touching visualisation is the ONS's, for the 2018–2020 back catalogue. The fallback offered is always "the data in another form". None claims the interactive view itself is accessible.

---------------------------------------------------------------
D4. GOV.UK DESIGN SYSTEM, SERVICE MANUAL, SERVICE STANDARD, NHS
---------------------------------------------------------------

Design System accessibility strategy — https://design-system.service.gov.uk/accessibility/accessibility-strategy/
- «Using the GOV.UK Design System in a service does not immediately make that service accessible.» STRING-VERIFIED
- «WCAG does not cover all aspects of accessibility» STRING-VERIFIED
- «released version 5.0.0 of GOV.UK Frontend with WCAG 2.2 AA compliant components» STRING-VERIFIED (dated December 2023 on the page, SINGLE PASS)
- Testing access: «screen readers through Assistiv Labs and macOS» STRING-VERIFIED; magnifiers, display modes and speech recognition lines SINGLE PASS
- «To ensure services are accessible, user research must include disabled people» STRING-VERIFIED
- The strategy page names no product: JAWS, NVDA, VoiceOver, Dragon, ZoomText and TalkBack do not appear (reader's check).

Design System accessibility statement — https://design-system.service.gov.uk/accessibility-statement/
- «is fully compliant with the Web Content Accessibility Guidelines (WCAG) version 2.2 AA standard» STRING-VERIFIED
- «There is currently no known non-compliant content» STRING-VERIFIED
- «including screen magnifiers, screen readers and speech recognition tools» STRING-VERIFIED
- «listen to most of the website using a screen reader (including the most recent versions of JAWS, NVDA, TalkBack and VoiceOver)» SINGLE PASS
- «The details component does not work well with Dragon and older versions of VoiceOver.» SINGLE PASS
- «It was last reviewed and updated on 18 December 2024» STRING-VERIFIED
- ZoomText is not named (control absent). The Service Manual's "Testing with assistive technologies" page, which holds the exact product list, returned 404 twice — not quoted.
- Basis for the list: the 2016 GOV.UK assistive technology survey, https://accessibility.blog.gov.uk/2016/11/01/results-of-the-2016-gov-uk-assistive-technology-survey/ (Chris Moore, 1 November 2016). 712 completed surveys from GOV.UK users of assistive technology, over six weeks, self-selected. Screen magnifier 30%, screen reader 29%, speech recognition 18%; JAWS 38.5% of screen-reader users. Figures STRING-VERIFIED.

Service Manual
- "Making your service accessible: an introduction" (last updated 17 December 2025, SINGLE PASS): no sentence on separate accessible versions, text-only versions, overlays or charts.
- "Understanding WCAG 2.2" (last updated 29 October 2024, SINGLE PASS): «not use images of text»; «not use colour as the only way to explain or distinguish something» — both SINGLE PASS. Nothing on charts or alternative versions.
- So the current GOV.UK manual states no position on parallel accessible versions. The nearest GDS statement found is the 2013 comment in D9.

Service Standard point 5 — https://www.gov.uk/service-manual/service-standard/point-5-make-sure-everyone-can-use-the-service (last updated 30 May 2022, SINGLE PASS). All STRING-VERIFIED:
- Title: "5. Make sure everyone can use the service"
- «Provide a service that everyone can use, including disabled people and people with other legally protected characteristics.» «And people who do not have access to the internet or lack the skills or confidence to use it.»
- «Government services must work for everyone who needs to use them.»
- «Public sector organisations have a legal duty to consider everyone's needs when they're designing and delivering services.»
- «Inclusive, accessible services are better for everyone.»
- «For example, using simple words helps people who are in a hurry as well as people who have a learning disability.»
- «meet accessibility standards, including both online and offline parts»

NHS digital service manual
- Charts appear once, in the alt-text rule. https://service-manual.nhs.uk/accessibility/content (Updated: February 2025): «Keep alt-text to a sentence or 2 and ideally under 125 characters including spaces.» STRING-VERIFIED. «If there's important information that you cannot fit in 125 characters (for example, you're describing a complex chart or image), include this information in the alt-text or consider linking to more information for screen reader users.» SINGLE PASS (two reads).
- https://service-manual.nhs.uk/accessibility/design (Updated: February 2025): «Do not include text in graphical (raster) formats like PNG, JPEG or GIF.» STRING-VERIFIED, then «They do not work well when users zoom in. Instead put text in HTML (styled with CSS) or use SVG. This does not apply to logos.» SINGLE PASS. «Do not rely on colour to convey meaning, for example, an instruction.» STRING-VERIFIED
- Reading age — https://service-manual.nhs.uk/content/how-we-write (Updated: August 2019): «We aim for a reading age of 9 to 11 years old.» STRING-VERIFIED. «In this case, try to make sure that an 11 to 14-year old will understand.» STRING-VERIFIED. No source is given for the 9-to-11 target. The only citation on the page (the 2014 GDS guest post, see D5) supports a different claim, the preference for plain English.
- https://service-manual.nhs.uk/content/health-literacy (October 2023, SINGLE PASS): «more than 4 in 10 adults struggle with health content for the public» and «more than 6 in 10 adults struggle with health content that includes numbers and statistics» — both STRING-VERIFIED, introduced by "Research shows that:" with no source named on the page.

---------------------------------------------------------------
D5. READING-AGE GUIDANCE
---------------------------------------------------------------

- GOV.UK has dropped the "9 years old" claim from its live guidance. The old "Writing for GOV.UK" URL now redirects (302) to https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/. On its "Use clear language" page (/clear-language/) the strings «reading age» and «9 years old» are absent on a presence check. The old wording could not be recovered (archive.org blocked) and is not quoted here.
- Councils still cite it. Surrey County Council: «We aim for a reading age of 9 to match GOV.UK standards» SINGLE PASS — https://www.surreycc.gov.uk/website/writing-guide/reading-levels-for-web-pages
- What GOV.UK now rests on: «Plain English is mandatory for all of GOV.UK.» STRING-VERIFIED; a list headed by a link to the National Literacy Trust including «1 in 6 adults in England have very poor literacy skills» SINGLE PASS; «80% of people preferred sentences written in clear English» STRING-VERIFIED, linked to SSRN abstract 1843415 and the GDS guest post; «Try to split up sentences that are over 25 words long.» SINGLE PASS.
- The GDS guest post — https://gds.blog.gov.uk/2014/02/17/guest-post-clarity-is-king-the-evidence-that-reveals-the-desperate-need-to-re-think-the-way-we-write/ (Mark Morris, Department of Health, 17 February 2014). It reports Christopher Trudeau's 2012 study of legal language (Thomas M Cooley Law School). Sample size and method are not in the post; the study itself was not read. SINGLE PASS; this is a source quoting a source.
- National Literacy Trust — https://literacytrust.org.uk/parents-and-families/adult-literacy/: «1 in 6 (18% / 6.6 million people) adults aged 16 to 65 in England have very poor literacy skills» STRING-VERIFIED, sourced to the Survey of Adult Skills 2023 national report for England. The older "16.4% / 7.1 million" is gone (control absent). «This is also known as being functionally illiterate.» STRING-VERIFIED. Scotland «1 in 4 (26.7% / 931,000 people)» STRING-VERIFIED, source given as Adult Literacies Scotland 2009; Wales 1 in 8 (12%), 2010; Northern Ireland 1 in 5 (17.4%), OECD 2012 — SINGLE PASS.
- Readability Guidelines (Content Design London): the site redirects to contentdesign.london. The 2018–19 wiki (http://readabilityguidelines.wikidot.com/home, last edited 30 April 2019) holds "reading age 9" only as an open research question. SINGLE PASS.
- Net: neither the NHS nor the old GOV.UK reading-age figure is tied on the page to a measured study. The literacy figures rest on the Survey of Adult Skills 2023.

---------------------------------------------------------------
D6. THE BBC
---------------------------------------------------------------

bbc.co.uk and bbc.com are blocked to the fetch tool. The Mobile Accessibility Guidelines, BBC R&D pages and any subtitles figure were unreachable; nothing is quoted from them. No R&D sonification project was found.

Reachable: the BBC GEL technical guide "Infographics" — https://bbc.github.io/gel/components/infographics/ (version 0.1.0; footer "Copyright © 2021 BBC"). All STRING-VERIFIED:
- Alternative text: «Describes what is in the infographic; a literal interpretation of its form»
- Caption: «Explains what the infographic says; an editorial summary of its salient points»
- «Multi-dimensional data that can be represented as a chart or graph should also be provided as a data table.»
- «It's recommended that colour is only added to your infographics as a progressive enhancement.» «Design it monochrome to begin with, and only add colour where desirable.»
- «In most cases, you should avoid creating interactive visualisations» «and instead use the recommended combination of alternative text, caption, and supplementary data table/source»
SINGLE PASS: one stated reason is «Sighted screen reader users are liable to be confused by what appears to be a graph being announced (and behaving) as a table or other semantic structure.»
Role: a broadcaster's own three-part rule (hidden literal alt text, visible editorial caption, data table) and a default against interactivity.

---------------------------------------------------------------
D7. NEWSROOMS AND PLATFORMS
---------------------------------------------------------------

- Financial Times, Guardian: sites blocked. No public FT alt-text policy was found by search. NYT and Reuters not attempted.
- Datawrapper — https://www.datawrapper.de/accessibility (reader gives "Updated 2025-05-05"): «The elements of all your Datawrapper charts, maps, and tables can be navigated using only the keyboard.» STRING-VERIFIED; alt text «to let screen readers read out what your chart, map, or table is about» STRING-VERIFIED; «semantically correct, descriptive markup» STRING-VERIFIED; a "Get the data" link STRING-VERIFIED; an automatic colourblind check SINGLE PASS. The page mentions no WCAG level, VPAT or conformance report. The Academy article on accessibility is robots-blocked.
- Flourish — https://flourish.studio/accessibility/: «the final accessibility level also depends on user choices like color palettes, descriptive titles, and clear annotations» STRING-VERIFIED; «That's why instead of a blanket WCAG AA certification, we focus on enabling and guiding users to create accessible visualizations.» SINGLE PASS; «Ongoing WCAG 2.2 AA improvements» and «EAA-ready» STRING-VERIFIED. No conformance claim.
- Highcharts — https://www.highcharts.com/accessibility/: «users can navigate and interact with chart by keyboard only» confirmed on two reads; «Screen reader users can explore the chart and its data point by point.» STRING-VERIFIED; «With the Highcharts Sonification module enabled, you can turn data into sound.» STRING-VERIFIED; «Highcharts has teamed up with the Sonification Lab at Georgia Institute of Technology» STRING-VERIFIED. No WCAG claim on the page. Docs (https://www.highcharts.com/docs/sonification/getting-started): «Sonification is a collective term for conveying information or perceptualizing data using non-speech audio.» STRING-VERIFIED; «many blind or low vision users find sonification helpful for getting an overview of the data» STRING-VERIFIED. This is a vendor's assertion, not a study.
- Vega-Lite — https://vega.github.io/vega-lite/docs/mark.html: «A boolean flag indicating if ARIA attributes should be included (SVG output only).» «A text description of the mark item for ARIA accessibility (SVG output only).» «If specified, this property determines the "aria-label" attribute.» All STRING-VERIFIED.
- Observable Plot — https://observablehq.github.io/plot/features/accessibility: «Marks automatically generate an aria-label attribute on the rendered SVG G element; this attribute includes the mark's type, such as "dot".» SINGLE PASS
- Our World in Data: no accessibility statement found (/accessibility is 404; the FAQ page and its footer mention none).
- Tableau — https://help.tableau.com/current/pro/desktop/en-us/accessibility_overview.htm: «You can use Tableau to create dashboards that conform to the Web Content Accessibility guidelines (WCAG 2.2 AA).» STRING-VERIFIED. The claim is about what an author can build. No VPAT wording was reached.
- Power BI — https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-accessibility-creating-reports (reader gives 2026-08-31): «Power BI has accessibility features built into the product, but as the report author, it's up to you to incorporate that capability into your reports.» SINGLE PASS; «All Power BI visuals support keyboard navigation.» STRING-VERIFIED; «The Alt Text textbox has a limit of 250 characters.» STRING-VERIFIED; «The accessibility features have a few known problems and limitations.» STRING-VERIFIED. Conformance reports are deferred to Microsoft's conformance portal; no "not fully conformant" line was found.

---------------------------------------------------------------
D8. OVERLAY WIDGETS
---------------------------------------------------------------

- Overlay Fact Sheet — https://overlayfactsheet.com/en/. All STRING-VERIFIED: «Overlays are a broad term for technologies that aim to improve the accessibility of a website.»; «full compliance cannot be achieved with an overlay»; «We will never advocate, recommend, or integrate an overlay which deceptively markets itself as providing automated compliance with laws or standards»; «We will always advocate for the remediation of accessibility issues at the source of the original error». SINGLE PASS: «Overlay widgets are unnecessary and are poorly placed in the technology stack.»
- Signatory count: the page states no total. The reader reports the numbered list ending at entry 1048 on this date. Treat as a reader's count.
- WebAIM Survey of Web Accessibility Practitioners #3 — https://webaim.org/projects/practitionersurvey3/ (January 2021; 758 valid responses; practitioners, self-selected). «A strong majority (67%) of respondents rate these tools as not at all or not very effective.» «Respondents with disabilities were even less favorable with 72% rating them not at all or not very effective, and only 2.4% rating them as very effective.» Both STRING-VERIFIED.
- EDF and IAAP joint statement, 17 May 2023 — https://www.edf-feph.org/accessibility-overlays-dont-guarantee-compliance-with-european-legislation/. «Overlays do not make the website accessible or compliant with European accessibility legislation.» «They do not constitute an acceptable alternative or a substitute for fixing the website itself.» Both STRING-VERIFIED. Advocacy and professional bodies, not a regulator.
- UK regulator: none found. The GDS monitoring report for 2022–2024 and the GOV.UK public-sector requirements guidance do not mention overlays (reader's check).
- FTC and accessiBe: the year is 2025, not 2023. Proposed order announced January 3, 2025 (https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-order-requires-online-marketer-pay-1-million-deceptive-claims-its-ai-product-could-make-websites): «The order would require accessiBe to pay the FTC $1 million that may be used to provide refunds to consumers.» STRING-VERIFIED; «despite the company's claims, accessWidget did not make all user websites WCAG-compliant» SINGLE PASS; vote 5-0. Final order April 22, 2025 (https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million): «The order prohibits accessiBe from making misleading claims and requires the company to pay $1 million.» SINGLE PASS; vote 3-0. These are allegations settled by consent order.

---------------------------------------------------------------
D9. TEXT-ONLY VERSIONS
---------------------------------------------------------------

- GDS — https://gds.blog.gov.uk/2012/01/20/user-testing-accessibility/. In a comment reply dated 23 July 2013 beneath his own post, Joshua Marshall wrote: «I'd rather we didn't build a separate 'accessible' site for users who may need a little extra assistance» «I'd much prefer that we try and make our core experience as useful and usable as we can» and «We've tried to avoid using the typical font resizing or contrast widgets that you tend to see on sites.» All STRING-VERIFIED. A staff comment, not policy. No formal GOV.UK statement on why text-only sites were dropped was found.
- BBC Betsie — https://lists.w3.org/Archives/Public/w3c-wai-ig/2001JanMar/0655.html (Wayne Myers, wayne.myers@bbc.co.uk, 16 February 2001, subject "RE: 'Text-Only' Versions Considered Harmful"). Betsie «provides an on-the-fly text-only view of the BBC website and others» STRING-VERIFIED. He argues the target should be «poorly implemented text only versions of sites» STRING-VERIFIED. «A text-only view need not be a 'ghetto'» is the corrected wording, SINGLE PASS. Betsie's retirement could not be sourced (bbc.co.uk blocked, Wikipedia not fetchable).
- WebAIM — https://webaim.org/articles/design/textonly (last updated Sep 25, 2020). All STRING-VERIFIED: «Text-only versions do not accomplish the goal of accessibility.»; «They accommodate users with some disabilities but neglect other types of disabilities.»; «Updates may not be reflected on the text-only version, and the information can quickly become outdated and inaccurate.»; «Text-only versions should be used only when other methods are not sufficient.»
- Evidence that parallel versions are less maintained: none measured. WebAIM cites no audit. A 2006 book chapter at http://www.uiaccess.com/myth-textonly.html (author not named on the page) says «When there are two versions of a website, invariably, the text-only version doesn't get updated as frequently as the main version.» STRING-VERIFIED, supported by one anecdote: «In one such implementation that I reviewed, ... the text-only version was missing promotional material.» SINGLE PASS. The claim is practitioner consensus, not a finding. One search for an empirical audit found none.

---------------------------------------------------------------
D10. AUDIO AND WRITTEN ROUTES IN OFFICIAL STATISTICS
---------------------------------------------------------------

- ONS: no audio or sonification experiment found (one search). The chart component docs mention none, though the reader identifies the component as Highcharts, whose sonification module exists.
- Government of Canada Digital Accessibility Toolkit — https://a11y.canada.ca/en/alternative-text-and-long-description-best-practices/ (Date modified 2025-09-19). Government-wide, not Statistics Canada's own. STRING-VERIFIED: «You must provide a long description if you can't describe the content and function of the image in less than 140 characters.»; «A long description usually goes right below the image.»; «the long description can be presented as a table»; «If a detailed and equivalent explanation of the image appears in the text immediately before or after a complex image, you don't have to provide a long description.» SINGLE PASS: chart alt text should give «The chart or graph type», «Type of data», «Brief description of the chart or graph». A Statistics Canada-specific rule was not found.
- Eurostat accessibility statement — https://ec.europa.eu/eurostat/help/accessibility. STRING-VERIFIED: «This website is partially compliant with technical standard EN 301 549 v.3.2.1 and the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA»; «The interactive tools and visualisations on this site do not always have text alternatives.»; «Interactive maps are not always accessible to blind users and users who rely on keyboard navigation». SINGLE PASS: «However, all visualisations provide a direct link to the source dataset to display the data in table format.»; «The website was last tested on 22 November 2022.»; «This statement was revised on 12 February 2026.»
- EU data visualisation guide (data.europa.eu; footer "© 2023, eu | academy") — https://data.europa.eu/apps/data-visualisation-guide/alt-text. It gives Amy Cesal's formula: «Chart type of type of data where reason for including chart» SINGLE PASS. Its sonification page says «Highchart's sonification module is still experimental, and doesn't work in all browsers.» SINGLE PASS, and cites an FT yield-curve sonification (2019) as a newsroom example.
- US Census Bureau Data Visualization Standards — https://xdgov.github.io/data-design-standards/components/colors. «Use text elements to label data directly to rely less on color.» and «text and interactive elements should have a color contrast ratio of at least 4.5:1» — both STRING-VERIFIED. No alt-text rule was found in these standards.
- Statistics Netherlands: not attempted.

---------------------------------------------------------------
D11. TITLE AND SOURCE INSIDE THE IMAGE — PRACTICE
---------------------------------------------------------------

- Analysis Function: title in the body text, and it names the cost (quotations in D2 iv). The image can be taken out of context; accessibility is prioritised anyway.
- ONS: the component takes title, subtitle and caption as separate parameters («The main title of the chart.», «A subtitle that appears under the main title.», «A caption providing additional context for the chart.» — SINGLE PASS), and the reader reports they sit outside the chart container in the HTML. A PNG download is offered. Whether that PNG carries title and source could not be established from the docs.
- Datawrapper — https://www.datawrapper.de/academy/how-to-download-your-chart-as-a-pdf: «you can decide if you want to download your chart with title, description, source, and byline» with options «Full header and footer» and «Just chart» — all STRING-VERIFIED. The PNG article (published January 20, 2022; updated February 24, 2026, SINGLE PASS) says «The last option is if you just want to import the chart, or the full header and footer» STRING-VERIFIED. Neither article states the default; "by default" is not verified.
- Financial Times: ft.com blocked. The FT's open library https://github.com/Financial-Times/g-chartframe («FT styled frames for D3 graphics», SINGLE PASS) has title, subtitle and source as properties of the SVG frame, which shows the tooling is built to draw them inside the graphic. Its README has no accessibility mention (reader's check). FT published charts were not observed.
- BBC GEL: the editorial summary is a visible caption outside the graphic, plus hidden alt text (D6).
- Our World in Data: the FAQ covers PNG/SVG download but does not say what the image contains.
- A live cost of title-in-image: Public Health Scotland lists as a WCAG failure of its R dashboards «Title of the graph is not communicated to screen reader users as it is an image of text.» (1.3.1, 1.4.5) STRING-VERIFIED.
- Net: official UK guidance and the ONS and BBC components keep title and source outside the image. Datawrapper offers both. The FT's tooling is built for the opposite. The house's departure has commercial and newsroom precedent but runs against the Analysis Function, and one official statement names the resulting failure.

---------------------------------------------------------------
UNASKED THREADS
---------------------------------------------------------------

1. The "rarely meet" sentence belongs to the Analysis Function (February 2026), not the ONS, and its Q&A page goes further: «I am yet to find a fully accessible dashboard.»
2. Public Health Scotland's statement is a ready-made catalogue of what Shiny and Tableau dashboards fail, criterion by criterion — roughly 32 and 16 items.
3. GOV.UK has moved its content guidance to guidance.publishing.service.gov.uk and no longer states a reading age there; councils still cite "GOV.UK's reading age of 9".
4. The National Literacy Trust's England figure is now 18% / 6.6 million (Survey of Adult Skills 2023), replacing 16.4% / 7.1 million.
5. GDS monitoring report 2022–2024 (published 17 December 2024) — https://www.gov.uk/government/publications/accessibility-monitoring-of-public-sector-websites-and-mobile-apps-from-2022-to-2024/accessibility-monitoring-of-public-sector-websites-and-mobile-apps-from-2022-to-2024: «We have monitored 1,203 websites and 21 mobile apps during this monitoring period.» and «Accessibility issues were found on nearly all tested websites and apps» — both STRING-VERIFIED. SINGLE PASS: «At the time of each detailed test, none of the 52 websites were fully compliant.»; most common failures 2.4.7 (13.3%), 1.4.3 (13.0%), 2.1.1 (10.8%), 1.4.10 (9.2%), 4.1.2 (8.6%).
6. Disproportionate burden as written in GOV.UK guidance (last updated 30 September 2024, SINGLE PASS): «You cannot take things like lack of time or knowledge into account in your assessment - or argue that making things accessible is a disproportionate burden because you've not given it priority.» The maps exemption reads «maps - but you'll need to provide essential information in an accessible format like an address». https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
7. NISRA publishes a separate accessibility statement for its visualisations (https://datavis.nisra.gov.uk/dissemination/accessibility-statement-visualisations.html). Unreadable to the fetch tool in two attempts; worth a manual read.
8. The GCS/GDS guidance "Planning, creating and publishing accessible website content" defers to the ONS for charts: «The Office for National Statistics (ONS) also publishes information about how to publish accessible charts, tables and other diagrams.» SINGLE PASS — https://www.communications.gov.uk/guidance/digital-communication/planning-creating-and-publishing-accessible-website-content/

---------------------------------------------------------------
LEFT OUT
---------------------------------------------------------------

- BBC Mobile Accessibility Guidelines, BBC R&D, BBC subtitles figure; FT and Guardian accessibility pages: domains blocked.
- ScotPHO's own statement; standalone Census maps and Explore Local Statistics statements; NISRA visualisation statement: unreachable or unreadable.
- GOV.UK "Testing with assistive technologies" page (404 twice), so the exact product-and-browser list is not quoted.
- The old GOV.UK "9 years old" sentence: page redirected, archive blocked.
- Tableau and Power BI VPAT/ACR documents; Datawrapper Academy accessibility article (robots-blocked).
- NYT, Reuters, Statistics Netherlands, a Statistics Canada-specific rule, a US Census alt-text rule.
- The Trudeau study and the source of the NHS "4 in 10" figure were not read at source.
- W3C alternate-version text and the WebAIM screen reader survey belong to Agents A and C.

---------------------------------------------------------------
RICH REFERENCES
---------------------------------------------------------------

1. Public Health Scotland accessibility statement — https://publichealthscotland.scot/accessibility-statement-for-public-health-scotland/ — the most specific official list of what R and Tableau dashboards cannot yet do.
2. Analysis Function, "Data visualisation: dashboard software" with "building and managing dashboards" (both February 2026) — the current cross-government position on dashboards, tools and WCAG 2.2.
3. BBC GEL technical guide "Infographics" — https://bbc.github.io/gel/components/infographics/ — a compact three-part rule and a default against interactive visualisations.

---------------------------------------------------------------
SURPRISED
---------------------------------------------------------------

- The chapter's anchor sentence is misattributed, and the true owner also says in print that it has yet to find a fully accessible dashboard.
- The ONS and the Analysis Function disagree on where the chart description lives: the ONS mandates a 100–200 character alt attribute in a fixed formula; the Analysis Function says body text, not the alt attribute, never both, never a caption.
- Not one official dashboard statement claims the interactive view is accessible; all fall back on data in another form. The UKHSA statement has not been reviewed since December 2023.
- The Design System declares itself "fully compliant" and in the same strategy says using it «does not immediately make that service accessible».
- GOV.UK quietly dropped the reading-age figure, and the NHS's 9-to-11 target has no source on its page.
- No UK regulator statement on overlays could be found; the hard fact is a US consumer-protection order, dated 2025.
- The "text-only versions go stale" claim, repeated everywhere, rests on practitioner assertion and one anecdote.