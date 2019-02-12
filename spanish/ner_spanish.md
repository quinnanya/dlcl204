# Named entity recognition for Spanish
Named entity recognition (NER) attempts to identify proper names (and sometimes other things, like money and time) in your text. What you do with those entities depends on what they are, and what your research question is. People's names could be used (in conjunction with other information) to map networks of relationships. Locations can be geocoded and placed on a map. Time can be organized chronologically, etc.

For this tutorial, we'll be focusing on location names. The end point of this tutorial will be a TSV (tab-separated values) spreadsheet file that you can use as the input of the Geocoding and Palladio Mapping tutorial.


## 1. Download Stanford Named Entity Recognizer
The [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) includes code for doing named entity recognition, along with models for English.

Go to the ["Downloads" section of the page](https://stanfordnlp.github.io/CoreNLP/index.html#download) and click on the big red "Download CoreNLP 3.9.2".

Save the zip file to your computer, and unzip it when it's done downloading. This will create a folder named *stanford-corenlp-full-2018-10-05*.

Next, you'll need to download the Spanish model file. Further down [in the downloads section of the CoreNLP page](https://stanfordnlp.github.io/CoreNLP/index.html#download), there's a table with other language models. Click the download link next to "Spanish" in the table. This will download the *stanford-spanish-corenlp-2018-10-05-models.jar* file. (Your computer may warn you about this type of file, but don't worry, it's safe.)

**Move** the *stanford-spanish-corenlp-2018-10-05-models.jar* file from where you downloaded it, into the *stanford-corenlp-full-2018-10-05* folder that you unzipped above.


## 2. Prepare your text
To use the tagger, you need to have the text you're working with saved as a Unicode (UTF-8) text file. You should also name the file without any spaces; e.g. instead of *my example file.txt*, name it *my-example-file.txt*, *my_example_file.txt*, *myexamplefile.txt*. Spaces mean something else when you're working with the command line, and while there's workarounds for using a file with spaces in its name, it's easiest to just avoid it.

It will be simplest for you to run the part-of-speech tagger if you copy your text file into the _stanford-corenlp-full-2018-10-05_ folder that you unzipped. If you're comfortable navigating file paths in the command line, you can skip this step.

For an example text that includes many place names, you can use the [Spanish-language Wikipedia article on Seattle](seattle-es.txt)

## 3. Run the tagger
**On a Mac**
Open a new terminal window, and navigate to the *stanford-corenlp-full-2018-10-05* folder. Unless you saved it somewhere else, you should be able to enter:
`cd Downloads/stanford-corenlp-full-2018-10-05`

Once you're in the folder, you can type `ls` and hit enter to check for the name of your text file if you want to make sure you moved it into the right folder.

Run the following command, replacing **yourtext.txt** with the name of your text file:

`java -mx3g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -props StanfordCoreNLP-spanish.properties -annotators tokenize,ssplit,pos,lemma,ner -file yourtext.txt -outputFormat conll -output.columns word,ner`

You'll see multiple lines of text appear, including some warnings like _[main] WARN edu.stanford.nlp.pipeline.TokensRegexNERAnnotator - Number in types column for [anti, psiquiatría] is probably priority: 2_. Don't worry about these.

If it completes successfully, you'll see some statistics (yours may vary, depending on your computer and source file) before you're given a new command prompt:
_Annotation pipeline timing information:_
_TokenizerAnnotator: 0.3 sec._
_WordsToSentencesAnnotator: 0.0 sec._
_POSTaggerAnnotator: 0.6 sec._
_MorphaAnnotator: 0.1 sec._
_NERCombinerAnnotator: 2.5 sec._
_TOTAL: 3.5 sec. for 7063 tokens at 2010.0 tokens/sec._
_Pipeline setup: 4.5 sec._
_Total time for StanfordCoreNLP pipeline: 8.0 sec._

These statistics show all the things that the command you entered did: first it tokenized the text (identified words), then identified the sentences, then did part-of-speech tagging, and then identified the dictionary form of all the words. All of this is a prerequisite for the named entity recognition; if you removed the things besides *ner* from the *-annotators* part of the command, you'd get an error message. Finally, after all this pre-processing, Stanford CoreNLP performed the NER annotation. On my computer, with the sample Spanish-language Wikipedia article on Seattle, the entire pipeline took 8 seconds and 7063 tokens (words) were annotated.

If you look at your *stanford-corenlp-full-2018-10-05* folder, you'll see a new file there, with the same name as your input file except with *.conll* at the end (so **yourtext.txt** will generate **yourtext.txt.conll**.)

## 4. Clean up the output
You can open the .conll file created above in a plain text editor (like [Atom](https://atom.io/), cross-platform, or [TextMate](https://macromates.com/), Mac only), which will display two columns: one with the Spanish words, and one with the named entity recognition annotations.

Open the file, and copy everything in it. Next, go to your favorite spreadsheet program (e.g. Google Docs sheets, Numbers, or Excel) and create a new blank document. Click in the upper left cell of the spreadsheet, and paste all the values. They should arrange themselves in two columns.

Next, select all the data and sort it by column B (the column with the NER annotations). If you don't select all the data, at least in Excel, it stops sorting once it hits a blank line -- and there's a blank line after each sentence.

You'll see multiple different annotations, potentially including:

* Cause of death
* City
* Country
* Date
* Ideology
* Location
* Misc
* Money
* Nationality
* Number
* O (not recognized as a named entity)

Create a new, blank spreadsheet. Copy all rows with *City*, *Country*, or *Location* in the annotation column, and paste them into the new spreadsheet.

You may want to clean up the data in this new spreadsheet (e.g. combining multi-word place names, like *Estados Unidos*, into a single cell). If you don't do this, those places won't be found when we try to look up their coordinates using a geocoder.

Don't remove duplicate listings, though: these duplicates will have a purpose once we start mapping with Palladio.

Once you're done with your cleanup, select all of column B (with the annotations), and delete it, leaving only a single column of place names.

## 5. Save your list of places
Once you're done cleaning the data as described above, save your data (which should be just a single column of place names) as **places.csv**. If you name the file something else, or use different capitalization, etc., you'll have to change the Python code that does the coordinate lookup. It's easier to just name it **places.csv**.

## 6. Move on to Geocoding and Palladio Mapping Tutorial
You're done with the language-specific part! Next, move on to the [Geocoding and Palladio Mapping Tutorial](/palladio/geocoding_palladio_mapping.md).
