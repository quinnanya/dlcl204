# Part-of-speech tagging for Portuguese
Part-of-speech tagging takes a text and marks grammatical information about all the words (and sometimes associated elements, like punctuation). This is a key step in enabling you to answer questions specific to language use in the text.

## 1. Download the POS tagger
The [Maltparser Universal Tree Bank PT-BR](https://github.com/pedrobalage/Maltparser-Universal-Tree-Bank-PT-BR) combines the [Maltparser](http://www.maltparser.org/) code for doing part-of-speech tagging with the [Universal Dependencies](https://universaldependencies.org/) treebank for Brazilian Portuguese ("GSD" [on this comparative list](https://universaldependencies.org/treebanks/pt-comparison.html)).

On the Github page, click the green "Clone or download" button, then click "Download ZIP". Unzip the file once it downloads.


### Portuguese POS tags
The full set of [Universal Dependencies tags](https://universaldependencies.org/u/pos/) is available here. Unfortunately, there isn't currently a page with Portuguese-specific documentation.


## 2. Prepare your text
To use the segmenter, you need to have the text you're working with saved as a Unicode (UTF-8) text file. You should also name the file without any spaces; e.g. instead of *my example file.txt*, name it *my-example-file.txt*, *my_example_file.txt*, *myexamplefile.txt*. Spaces mean something else when you're working with the command line, and while there's workarounds for using a file with spaces in its name, it's easiest to just avoid it.

It will be simplest for you to run the part-of-speech tagger if you copy your text file into the _Maltparser-Universal-Tree-Bank-PT-BR-master_ folder that you unzipped. If you're comfortable navigating file paths in the command line, you can skip this step.

## 3. Run the tagger
Open a new terminal window, and navigate to the *Maltparser-Universal-Tree-Bank-PT-BR-mastert* folder. Unless you saved it somewhere else, you should be able to enter:
`cd Downloads/Maltparser-Universal-Tree-Bank-PT-BR-master`

Once you're in the folder, you can run `ls` and check for the name of your text file if you want to make sure you moved it into the right folder.

Run the following command, replacing **yourtext.txt** with the name of your text file:

`cat yourtext.txt | ./parse.py`

The results will appear in the terminal window. Unfortunately, there is a Unicode issue in the Python code for this tagger that throws an error when you try to make it save the results as a file. Instead, copy the table out of the terminal window, and paste it in a plain text (.txt) file.

## 4. Look at the output
To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and non-ASCII characters will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with Tint), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

Your text will appear in a series of columns. The most important are:

* column D/E (identical): show the part-of-speech tag
* column H: shows more grammatical information

A blank line separates each sentence. The numbers in column A show the place of the word within its sentence, but there are no unique IDs for any of the words in the text. You can sort your sheet by column D or E to see, for instance, all the nouns in the text. Note, though, that this will lose the original sentence-based structure of the file.