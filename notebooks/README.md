# Jupyter notebooks for multilingual DH

## Text acquisition

* [Extracting burned-in subtitles from videos](subtitle_extraction.ipynb)

## Text enrichment

### Lemmatizers
Lemmatizing (replacing inflected word forms with their dictionary form) is an important step in preparing texts in many languages for computational methods that involve some form of counting words.

* [French lemmatizer](dlcl204-french-lemmatizer.ipynb) using spaCy
* [German lemmatizer](dlcl204-german-lemmatizer.ipynb) using spaCy
* [Italian lemmatizer](dlcl204-italian-lemmatizer.ipynb) using spaCy
* [Portuguese lemmatizer](dlcl204-portuguese-lemmatizer.ipynb) using spaCy
* [Russian lemmatizer](dlcl204-russian-lemmatizer.ipynb) using pymystem
* [Spanish lemmatizer](dlcl204-spanish-lemmatizer.ipynb) using spaCy
* Vietnamese doesn't need a lemmatizer, because the words in the text are the same as the root form

### Segmenters
Segmenting (artificially inserting spaces between words) is an important step in preparing texts for computational methods, for languages that don't use spaces in the same way as English.
* [Chinese segmenter](dlcl204-chinese-segmenter.ipynb) using jieba
* [Japanese segmenter](https://github.com/quinnanya/japanese-segmenter) using RakutenMA