# DLCL 204 - Winter 2023 overview

What tools, methods, and topics did we cover in DLCL 204 in winter 2023 that you might be able to use in the future? Here's a handy guide!

## Values of DH

Lisa Spiro's "['This is Why We Fight: Defining the Values of Digital Humanities](https://dhdebates.gc.cuny.edu/read/untitled-88c11800-9446-469b-a3be-3fdb36bfbd1e/section/9e014167-c688-43ab-8b12-0f6746095335)" (2012) looks to define shared values as a way to find common ground within the (still ongoing) debates about what DH is.


## Copyright law and the DMCA

[Data-Sitters Club #7: The DSC and Mean Copyright Law](https://datasittersclub.github.io/site/dsc7.html) and [Data-Sitters Club #14: Hello, DMCA Exemption](https://datasittersclub.github.io/site/dsc14.html) cover the legal landscape and recent developments around how you can use encrypted ebooks for research.

We also talked a little about the copyright implications for AI, with this [point-counterpoint piece](http://www.stablediffusionfrivolous.com/) on the lawsuit that's been filed over image generation models.


## (Collaborative) note-taking and markdown
We tried to do collaborative note-taking on readings using [Obsidian](https://obsidian.md/), where notes are stored on your own computer in plain-text [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) format, and syncing it to a shared repository using [GitHub Desktop](https://desktop.github.com/). We learned that Windows machines break a lot with this workflow, and can't handle notes that have any special characters (like punctuation) in the filenames. We also learned that we needed to exclude some of the Obsidian-specific files to avoid weird conflicts when people uploaded their own notes. The idea would be that this process would generate some kind of collaborative knowledge graph visualization that maybe could be part of people's final project / publication (I was hoping developers would make more progress on something like [Flowershow](https://flowershow.app/) to generate pretty webpages from Obsidian notes), but all in all it didn't work out.

## Paths for text acquisition
We looked through various [paths for text acquisition](https://quinndombrowski.com/dlcl204-adventure/dlcl204-text-acquisition.html) based on the last session of DLCL 204.


## Unicode
We did a deep dive on Unicode: what is it? How does it work? How do things get added to it? And we talked a bit about the [Script Encoding Initiative](https://dh-stanford.github.io/sei/) that advocates for the representation of more writing systems in Unicode.

## Playful exploratory text analysis with Voyant
We explored [Voyant](https://voyant-tools.org/) and read some of the introduction to "[Hermeneutica](https://searchworks.stanford.edu/view/13347297)" and the [Data-Sitters Club Book on Voyant](https://datasittersclub.github.io/site/dsc6.html) and on [Stéfan Sinclair](https://datasittersclub.github.io/site/dsc13.html#stefan-sinclair). We [filed an issue on the GitHub repo](https://github.com/voyanttools/VoyantServer/issues/31) to ask how distinctive words are calculated (TF-IDF), and also asked about Chinese pre-processing which was acting weird ([it's a known issue](https://github.com/voyanttools/VoyantServer/issues/32)).

We looked at Voyant's stopword lists (which are extremely hit-or-miss depending on the languages) and worked on improving them to be useful for our own research use cases.


## DH conferences
I tried to convince you all to apply for the [ACH 2023 conference](https://ach2023.ach.org/en/cfp/), which, I swear, continues to be one of the most newcomer-friendly, welcoming DH conferences out there.

## Lemmatization & other text pre-processing
We talked about [text pre-processing for non-English languages](https://www.modernlanguagesopen.org/articles/10.3828/mlo.v0i0.294/), creating derivative files that will make it easier for the computer to do its thing (like counting words, especially in languages where "words" can appear in many different forms). 

We then tried this out using [Jupyter notebooks](https://programminghistorian.org/en/lessons/jupyter-notebooks) and Google Colab (you can add Colab to your Google Drive following the [instructions at the top here](https://github.com/multilingual-dh/russian-starter-kit)).

We used [spaCy](https://spacy.io/) for our natural language processing work, including lemmatization (and segmentation for Chinese, though it didn't perform amazingly). Here's the Colab notebooks for each language:

* [Chinese](https://colab.research.google.com/drive/1a2OjoCs_CXpzX1hTeQ2-NBVaWfgFyFqu?usp=sharing)
* [English](https://colab.research.google.com/drive/14tPao1XtHktYnWpHwPogCCV2gcyI2UF5?usp=sharing)
* [French](https://colab.research.google.com/drive/1E-XuTF3NAdK_NMa_mbCIDpvsf6VkdoW7?usp=sharing)
* [Spanish](https://colab.research.google.com/drive/1FR6rsFXkzcy7kg6v_SUQwBW_-w5waKDG?usp=sharing)
* [Russian](https://colab.research.google.com/drive/1iTbQcHVcC4vdZkVBrNvOhH0d3Cuch6ep?usp=sharing)

(You could adapt these for any other language supported by spaCy by subbing in the name of the [model for that language](https://spacy.io/models) in a couple places at the top.)

## Named entity recognition

After we did lemmatization / segmentation, I updated the same set of notebooks to include code for pulling out *named entities* (e.g. people, places) in your texts. All that code is in the same Colab notebook linked above. Unsurprisingly, [English performed better than the other languages](https://datasittersclub.github.io/site/dscm2.html).

## Finding grammatical subjects

We used the same Colab notebooks again to find the grammatical subject of sentences in your texts, with the [caveat that this may work less well for non-English languages](https://datasittersclub.github.io/site/dscm5.html).


## Finding words in a text
We again used the same Colab notebooks to identify all occurrences of a particular word or word(s) in the text. For languages where lemmatization is important, we used the lemmatized version of the text to search for words.


## HathiTrust data capsules
We took an extended trip down the rabbit hole of HathiTrust data capsules, following the instructions in [The Data-Sitters HathiTrust Mistake](https://datasittersclub.github.io/site/dsc18.html). We installed [AntConc](https://datasittersclub.github.io/site/dsc4.html) in the data capsules, but then discovered we couldn't type accented characters. (Typing, in general, was moderately torturous.) No one managed to get the sort of cool results in the end that [Ted Underwood regularly does with HathiTrust](https://tedunderwood.com/2016/12/28/the-gender-balance-of-fiction-1800-2007/), but if your research questions align reasonably well with what HathiTrust has in its collection and you have a lot of patience and are up for jumping through a lot of hoops, it is, in principle, possible to persist and overcome all the obstacles and come up with some interesting findings.

##  Topic modeling
We used the [Topic Modeling Tool](https://github.com/senderle/topic-modeling-tool) to experiment with topic modeling, after reading about applications of topic modeling as depicted in Matt Jockers' [Macroanalysis & related work](http://digitalhumanities.org:8081/dhq/vol/10/2/000250/000250.html), and as described through an extended metaphor in his [LDA Buffet](https://www.matthewjockers.net/macroanalysisbook/lda/). We also read about the limits of topic modelign through Ben Schmidt's [Words Alone](https://journalofdigitalhumanities.org/2-1/words-alone-by-benjamin-m-schmidt/). We also talked a little about [Scott Enderle](https://datasittersclub.github.io/site/dsc13.html#scott-enderle) (RIP), the developer of the Topic Modeling Tool.

## Text comparison
We looked at various methods for text comparison -- including different [similarity measures](https://programminghistorian.org/en/lessons/common-similarity-measures). We read about my screw-up with word *frequencies* vs word *counts* in [Text-Comparison Algorithm Crazy Quinn](https://datasittersclub.github.io/site/dsc8.html) and used a [Colab notebook with code for doing different kinds of text comparison and generating heatmaps](https://colab.research.google.com/drive/1wflDgTxFRflB6fKqPQj1t0vzbbiA4qfI?authuser=1#scrollTo=b9KsOrxbxOHe). We also used this to try out TF-IDF to find words that are particularly characteristic of individual texts.


## Networks & maps
We read Scott Weingart's [Demystifying Networks, Part I and II](https://journalofdigitalhumanities.org/1-1/demystifying-networks-by-scott-weingart/) for a basic introduction to network analysis, and the fact that the network metrics only really work on a *unipartite* network (i.e. a network between the same kinds of thing -- like people and people), and we can't use those metrics on a *bipartite* network (a network between two different kinds of things, like people and books).

We tried out both networks and maps using [Palladio](https://hdlab.stanford.edu/palladio-app/#/upload), and did some quick geocoding on a very small data set just by sticking places into Google Maps and looking at the URL to find the latitude and longitude, which we added to the data set that we uploaded to Palladio. (Remember: you need to give Palladio latitude and longitude as part of your data set if you want to use maps.)


## Principal component analysis
Finally, we also did [principal component analysis](https://datasittersclub.github.io/site/dsc10.html) (arranging texts in a 2-dimensional visualization based on their usage of the top (some number) of nouns (or words).) We used [R in a Colab notebook for PCA](colab.research.google.com/drive/15Ptvvc0Y7vC-P9_YFhxD-PEgzTO9SbH0?usp=sharing
), and used [Tableau](https://www.tableau.com/academic/students) (for which you can get a student license for free) to visualize the results. We also expanded the notebook to create a biplot that shows which words play the biggest role in positioning a text in one quadrant or another.

**Important note:** the code used in the Data-Sitters Club piece and in the Colab notebook includes a cleaning function that deletes *all non-ASCII characters*, which is a huge problem if your text is in the Cyrillic alphabet or Chinese characters. That function has to be disabled for this to work at all, but the results are then a little messy.


## Shifterator
We also tried [Shifterator](https://github.com/ryanjgallagher/shifterator) for looking at what words are characteristic of one text vs. another. In the process, we discovered that Shifterator's output visualization uses a font that won't render Chinese characters and [filed an issue on GitHub](https://github.com/ryanjgallagher/shifterator/issues/38) asking for a fix.


## OpenRefine
A few people met for a crash course on [OpenRefine](https://openrefine.org/) which is great for cleaning up and bulk-editing tabular data. 