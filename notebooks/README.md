# Jupyter notebooks for multilingual DH

## Text acquisition

* [Extracting burned-in subtitles from videos](subtitle_extraction.ipynb)

## Text enrichment

### Lemmatizers
Lemmatizing (replacing inflected word forms with their dictionary form) is an important step in preparing texts in many languages for computational methods that involve some form of counting words.

* [French lemmatizer](dlcl204-french-lemmatizer.ipynb) using [spaCy](https://spacy.io/models)
* [German lemmatizer](dlcl204-german-lemmatizer.ipynb) using [spaCy](https://spacy.io/models)
* [Italian lemmatizer](dlcl204-italian-lemmatizer.ipynb) using [spaCy](https://spacy.io/models)
* [Portuguese lemmatizer](dlcl204-portuguese-lemmatizer.ipynb) using [spaCy](https://spacy.io/models)
* [Russian lemmatizer](dlcl204-russian-lemmatizer.ipynb) using [pymystem](https://github.com/nlpub/pymystem3)
* [Spanish lemmatizer](dlcl204-spanish-lemmatizer.ipynb) using [spaCy](https://spacy.io/models)
* [Turkish lemmatizer](dlcl204-turkish-lemmatizer.ipynb) using [zeyrek](https://zeyrek.readthedocs.io/en/latest/)
* Vietnamese doesn't need a lemmatizer, because the words in the text are the same as the root form

### Stemmers
Stemming removes prefixes and suffixes, leaving a kind of "root form" for each word (which may or may not be the linguistically correct root of the word). It's computationally easier than lemmatizing, and stemmers exist for many languages that don't have lemmatizers.

* [Arabic stemmer](dlcl204-arabic-stemmer.ipynb) using [farasapy](https://pypi.org/project/farasapy/)

### Segmenters
Segmenting (artificially inserting spaces between words) is an important step in preparing texts for computational methods, for languages that don't use spaces in the same way as English.
* [Chinese segmenter](dlcl204-chinese-segmenter.ipynb) using [jieba](https://pypi.org/project/jieba/)
* [Japanese segmenter](https://github.com/quinnanya/japanese-segmenter) using RakutenMA

## Analysis
* [Creating word vectors](dlcl204_word_vectors.ipynb) using gensim