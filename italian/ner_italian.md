# Named entity recognition for Italian
Named entity recognition (NER) attempts to identify proper names (and sometimes other things, like money and time) in your text. What you do with those entities depends on what they are, and what your research question is. People's names could be used (in conjunction with other information) to map networks of relationships. Locations can be geocoded and placed on a map. Time can be organized chronologically, etc.

For this tutorial, we'll be focusing on location names. The end point of this tutorial will be a CSV (comma-separated values) spreadsheet file that you can use as the input of the Geocoding and Palladio Mapping tutorial.

## 1. Download TINT

[TINT (The Italian NLP Tool)](http://tint.fbk.eu/) is based on [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) but includes training data for Italian.

The current stable build (v0.2) is no longer compatible with Stanford CoreNLP, and throws errors when you try to run it. Instead, go to the [TINT downloads page](http://tint.fbk.eu/download.html) and download *tint-runner-1.0-SNAPSHOT-bin.tar.gz (latest nightly build, tar.gz)*. Save the file, and unzip it.


## 2. Prepare your text
To do named entity recognition, you need to have the text you're working with saved as a Unicode (UTF-8) text file.

You should also name the file without any spaces; e.g. instead of *my example file.txt*, name it *my-example-file.txt*, *my_example_file.txt*, *myexamplefile.txt*. Spaces mean something else when you're working with the command line, and while there's workarounds for using a file with spaces in its name, it's easiest to just avoid it.

It will be simplest for you to run the part-of-speech tagger if you copy your text file into the _tint_ folder that you unzipped. If you're comfortable navigating file paths in the command line, you can skip this step.

For an example text that includes many place names, you can use the [Italian-language Wikipedia article on Seattle](seattle-it.txt)

## 3. Run the annotator
**On a Mac**
Open a new terminal window, and navigate to the *tint* folder. Unless you saved it somewhere else, you should be able to enter:
`cd Downloads/tint`

Once you're in the folder, you can run `ls` and check for the name of your text file if you want to make sure you moved it into the right folder.

Run the following command, replacing **yourtext.txt** with the name of your text file:

`cat yourtext.txt | ./tint.sh -o yourneroutput.txt -f textpro -properties tokenize,ssplit,pos,lemma,ner`

A few lines of text should appear. One of them might be *ERROR StatusLogger No log4j2 configuration file found. Using default configuration: logging only errors to the console.* but this shouldn't pose a problem. Eventually you should see *Tint is ready*, and it will return you you to the command line. If everything worked correctly, you should see a new file, *yourneroutput.txt*, in the directory.

## 4. Look at the output
You can open the output in a plain text editor, which will display a series of columns. 

To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and non-ASCII characters will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with Tint), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

Your text will appear in a series of columns. The two that matter here are:

* token: the word itself
* entity: indicates whether the word has been flagged as a named entity (PER for person, LOC for location)

## 5. Clean up the output
Delete all the columns except for *token* and *entity*.

Select all the data in the two remaining columns, and sort by the *entity* column. You'll see the following types of entities:

* LOC: location
* O: not an entity
* ORG: organization
* PER: person

Select all the words that have been annotated with *LOC*, and paste them into a new spreadsheet. You shouldn't copy the annotations, just the words themselves.

At this point, you might want to clean up the data, for instance, putting multi-word location names that have been split across multiple rows into a single cell (e.g. Stati Uniti).

Don't remove duplicate listings, though: these duplicates will have a purpose once we start mapping with Palladio.

## 6. Save your list of places
Once you're done cleaning the data as described above, save your data (which should be just a single column of place names) as **places.csv**. If you name the file something else, or use different capitalization, etc., you'll have to change the Python code that does the coordinate lookup. It's easier to just name it **places.csv**.

## 7. Move on to Geocoding and Palladio Mapping Tutorial
You're done with the language-specific part! Next, move on to the [Geocoding and Palladio Mapping Tutorial](/palladio/geocoding_palladio_mapping.md).
