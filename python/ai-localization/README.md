# AI-assisted UI Translation in Open Source apps

This directory explores ways to improve app UI translation proces while leveraging AI
(Artificial Intelligence).

## Motivation

The manual UI translation process in general is error-prone and time-consuming process.
Small apps contain ~100. More complex apps have more than 1000 strings. To translate apps
to local languases is costly and/or requires many volunteers. The translation quality
differs between translations. Also when apps are updated then the translations are quickly outdated.

AI could improve the translation process by making it faster and also improve the quality of the
translations.

## Use Case
For my experiments I chose a small opne source Android app Power Ampache 2. For this project
I created the Czech translation in the past. It needed some updates.

- open source project: [PowerAmpache 2](https://power.ampache.dev/)
- description: Android client for playing own audio collections stored in cloud-file services like Nextcloud.
- UI strings count: 155 (simple small app)
- text format: standard Android string definition in xml format. e.g.
```
<resources>
    <string name="coming_soon">Coming Soon</string>
    <string name="playlistItem_songCount">%s Songs</string>
    <string name="main_tab_title_albums">Albums</string>
</resources>
```

## Metrics
Features to check:
- czech lang support
- customization - ability to set context-specific info - This is necessary for updating existing translation - use existing translated string and translate in a similar way
- accuracy
- style guides
- automation - API available?
- file translation
- price/limitation

## A bit of Translation/Localization Theory

### Terminology
- **translation**: Convert text from one lang to another, translation is part of localization.
- **localization** The entire process of adapting a product or content to a specific location or market.
- **machine translation**: The use of computational techniques to translate text/speech from one lang to another.
- **translation memory**: A database of strings that were previously translated by a human. It aids human translators.
- **AI localization**: Integrate AI technologies into the localization process.
- **web-based translation platform**: Whole management platform for app localization lifecycle. Services like transifex.com and weblate.org are widely used by open source projects. The services provide free translation hosting for open source projects. I used transifex.com in the past.
- **back translation**: The process of re-translating a translation back to its original language. Nice and handy quality control method for translation. Ideally a different translator should perform the translation to original language.

### Machine Translations
PROS: fast, cost-efficient for large volumes, reduced time to market, adaptable, programmable, developer-friendly

CONS: lack of context (inability translate local phrases/slang/nuances, culturally releavant phrases), difficult to transindustry-specific terms, predicting/correcting specific grammar errors

4 ways of machin translation (Translation tools usually use combination of them.):

1. statistical - relies on human, analyzes databases to pick the best translation
2. neural networks (also called Artifical Intelligence) - e.g. google translate
3. syntax based - translates syntax instead of just words
4. rule based - relies on context - linguistic/grammatical rules

### AI Localization
- Traditional translation: Human does the content translation.
- It refines translation outputs, speeds up review process. Also leverages advanced machine learning algorithms and natural language processing
- helps with managing localization projects of any scale and automate repetitive tasks, optimizing workflows, providing predictive analytics for better decision-making.
- Uses: translation memories, glossaries, and feedback loops, historical data and continuous learning to improve translation over time
- Benefits: speed/efficiency, accuracy/consistency, cost-effective, scalability, collaboration/integration
- Content is translated and also culturally and contextually adapted.
- AI localization tools are designed to complement human expertise. Professionals may focus more on strategic, creative, and culturally nuanced aspects of translaton.

Translation Best Practices:
1. define clear objectives
2. select appropriate tools
3. balance automation with human insight
4. monitor/refine continuously

### AI misconceptions in Localization
- **AI replaces human translators** NO, it complements it. AI serves as a tool to improve and assist the whole process.
- **AI is flawless** - NO, it still needs humans for quality control and providing context. particularly for content that involves deep cultural understanding or specialized industry knowledge.

## AI Backends
There are many services providing AI capabilities. I tried to pick those
well known. Translation management platform usually integrates with various
AI backends.

### Comparison Process
1. Pick up AI backend for testing
2. Find Python programming library
3. Create cli tool to submit UI strings for translation and get it back
4. Compare the machine-translated string with previously manually translated

### Backend - DeepL
- After some blogpost reading and internet research DeepL is recommended as being one with best translation accuracy.
- PROS:
  - many customization options: translation formality level, own glossary, html/xml tag detections, provide text for context (text in target language and DeepL should translate it similarly)
  - official Python library, which is easy to use, well documented API, examples
  - Free web services for small translations and for writing styles
  - Czech support
  - able to detect xml/html tags, those are not translated, xml/html detection is much better than Google Translate. (The tags are present in translated text unchanged)
  - For PowerAmpache2 UI translation it translated some strings better than I did manually. It excels in longer strings 
    and making better with simple phrasing
    - `This is a required field` - manual `Toto políčko je poovinné` machine `Toto je povinné pole`
    - `More Albums` - manual `Více albumů` - machine `Další alba`
- CONS:
  - less language support when compared to Google Translate
  - not all customization features supported by all languages (e.g. formality level and glossaries not supported for Czech)
  - free service limits to 5000 characters, xml/html tags not counted
  - sometimes it does not translate simple words - e.g. in the PowerAmpache2 translation - not translated 14 string of 155. E.g.
    simple words, special terms, like "home", "comming soon", "auth token", dark, light,

### Backend - Google Translate
- Common service used to translate something. Google translate also uses neural network models for machine translation.
- PROS:
    - translate to/from many languages than other services
    - ability to translate text with html/xml tags and keep the tags in translated output. However there were some issues
      when trying to translate PowerAmpache2 UI strings.
- CONS
    - not much customization options, no writing-style assistant
    - free service limits to 5000 characters
    - for automation and larger volumes - required prepaid service and google cloud api key
    - free service unusable for automation - no API
 
### Backend - OpenAI
- NOTE: I did not have much time to explore this backend. It is probably more capable than others but the learning path
  is more complex.
- AI backed for the chatbot Chatgpt. This one being the most famous.
- PROS
  - more capabilities than other backends not just machine translation
- CONS
  - free service limits translation to 4000 characters
  - harder to learn and use programatically

## Results
- In regards to using AI-assisted machine translation for user interface it is great for:

  1. *Fast initial UI translation* - it helps human translator to get quickly started or where translation quality is less important.
  2. *Review UI translation by human* - improve wording/grammer/phrasing, unify style

- It is less usable for:
  1. *updating existing translation* - the AI translation might not respect the context and style of the translation. Then at least manual review of the updated strings is still required.
  2. *industry- and cultural-specific content* - quality of translation differs among AI backends. Also the ability customize translation is different.

- I tend to agree that from the translation quality aspect the best results were achieved with *DeepL* backend. Mostly because it has the best customization options:
  1. It allows to specify context text in target language how the text should look like when translated from original language
  2. For some languages it allows specify if the text should be translated as more formal or less formal. (Not available for Czech)
  3. For some languages define glossaries - how some words should be translated. (Not available for Czech)
  4. Best detection of html/xml tags in text. It does translate xml/html tags. Google Translate had some issues with html/xml tags in text.
  5. For some languages it has also [writing-style assistant](https://www.deepl.com/en/write). This assistant helps you tune the writing style - not just grammar errors.

### Visible Artifacts

During my mini-research I created:

- Python code with translation experiments: https://github.com/matysek/matysek-code-library/tree/master/python/ai-localization
- Updated Czech UI translation of an android app: https://github.com/icefields/Power-Ampache-2/pull/163
- Set up translation service for that android app: https://app.transifex.com/matysek/powerampache2/dashboard/


### Conclusion
- Artificial Intelligence really improves the quality of machine-translated texts and speeds up translation process significantly.

- AI works very well for general text and large volumes of data. It has issues with text where more context is needed. For example
  with industry and cultural specific content.

- Based on my mini-research I agree with the following statements:
  1. *Machine translation tools won't replace human translation. They fine for large volumes, bad at cultural and slang nuances.*
  2. *Machine translation tools are good starting point for translating UI*

- AI backends differ a lot in customization, number of supported languages and ease of use.

- In general the AI services are costly. Free service is limited to 4-5 thousands characters. Being able to translate more at once
requires some form of subscription. Then monthly quota is assigned how many characters per month the user is allowed to translate.
Being able to use translation API requires API key. Even Google Translate does not have direct API and requires using Google cloud translation
API with subscription.

- There are no free subscription plans for open source projects that could improve the adoption of AI tools in open source world.

## Resource Links
- Blogposts:
    - [Top 7 AI-translation tools](https://www.transifex.com/blog/2024/ai-translation-tool/)
    - [Machine translation](https://www.transifex.com/blog/2021/what-is-machine-translation/)
    - [AI Localization](https://www.transifex.com/blog/2024/ai-localization/)
    - [AI transforms localization](https://www.transifex.com/blog/2024/ai-transforms-localization/)
    - [Transifex AI](https://www.transifex.com/blog/2023/introducing-transifex-ai/)
    - [Guide to SW localization](https://www.transifex.com/blog/2024/software-localization-guide-examples/)
    - [What is Back Translation](https://www.transifex.com/blog/2023/what-is-back-translation/)
- Tools:
    - [Transifex](https://www.transifex.com/): proprietary web-based translation platfomr, many open source projects uses it
    - [Weblate](https://weblate.org/en/): another, open source, web-based translation platform, also used a lot by open source projects
    - [LibreTranslate](https://cs.libretranslate.com/): opensource online/offline machine translation tool
    - [PowerAmpache 2](https://power.ampache.dev/): Android client for playing own audio collections stored in cloud-file services like Nextcloud.
    - [DeepL](https://www.deepl.com/en/translator): - AI translation service most praised for its accuracy, customization and recpecting translation context
    - [Google Translate](https://translate.google.com/): Google translation service incorporates AI into translations
    - [OpenAI](https://openai.com/): Backend used by ChatGPT - most famous AI chatbot.
- Python Libraries:
    - [deepl library](https://pypi.org/project/deepl/)
    - [gooletrans-modified library](https://pypi.org/project/googletrans-modified/)
    - [openai library](https://pypi.org/project/openai/)
