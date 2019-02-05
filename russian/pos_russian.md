# Part-of-speech tagging for Spanish
Part-of-speech tagging takes a text and marks grammatical information about all the words (and sometimes associated elements, like punctuation). This is a key step in enabling you to answer questions specific to language use in the text.

## 1. Download the POS tagger
[MyStem](https://tech.yandex.ru/mystem/) from Yandex ("Russian Google") is the best natural language processing toolkit for Russian. The documentation link on the MyStem homepage is broken, but the [documentation is here](https://tech.yandex.ru/mystem/doc/index-docpage/).

[Download the latest version of MyStem](https://tech.yandex.ru/mystem/) for your operating system. Unzip it. It will unpack a file you can execute from the command line.

### Russian POS tags
MyStem has [documentation about all the POS tags they use](https://tech.yandex.ru/mystem/doc/grammemes-values-docpage/).


## 2. Prepare your text
To use the tagger, you need to have the text you're working with saved as a Unicode (UTF-8) text file. An example text file you can use for this exercise is [the prologue to "The Compromise" by Sergei Dovlatov](kompromiss.txt).

You should also name the file without any spaces; e.g. instead of *my example file.txt*, name it *my-example-file.txt*, *my_example_file.txt*, *myexamplefile.txt*. Spaces mean something else when you're working with the command line, and while there's workarounds for using a file with spaces in its name, it's easiest to just avoid it.

Put your text file in the same place that you unzipped MyStem (i.e. probably in your Downloads folder). If you're comfortable navigating file paths in the command line, you can skip this step.

## 3. Run the tagger
Open a new terminal window and use it to navigate to the directory where you unzipped MyStem (probably Downloads): `cd Downloads`.

Run the following, but substitute your text file name for **yourfile.txt**. You can also choose another name for your output file.

`./mystem -i yourfile.txt yourposoutput.txt`

This will create a new file, **yourposoutput.txt** (if you haven't named it something else) in that same folder.


## 4. Clean up the output
You can try to look at the output file in any plain text editor, but it will probably start making your head hurt very quickly. To be able to browse the output more easily in Excel, we need to reformat it slightly.

Install [Atom text editor](https://atom.io/), and open your output text file.

Using the menu bar at top, go to *Find > Find in buffer*. This will open a toolbar at the bottom where you can do find-and-replace.

Click on the button in the upper right of the find-and-replace toolbar that looks like a period with a star next to it. This turns on the feature for using regular expressions (regex), a powerful specialized syntax for find-and-replace.

To make the results show up in columns in Excel, we need to use a tab character between the words and their annotations, and a new line (line break) character between words.

* In the "find" box, type **{**, and in the "replace" box, type **\t** (if you have regex turned on, it should appear in blue)
* Hit the "Replace All" button
* Clear out the "find" box, then type **}**, and in the "replace" box, type **\n** (if you have regex turned on, it should appear in blue)
* Hit the "Replace All" button

Save your file.


## 4. Look at the output


You can open the output in a plain text editor, which will display two columns: one with the Spanish words, and one with the part-of-speech tags.

To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and the characters will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with the POS tagger), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

Your text will appear in two columns, with one word per row in the first column, and set of grammatical annotations in the second column. One of the challenges of the MyStem package is that it gives you all possible annotations for a word -- and with words like и and я, the result is a very long string of annotations that's hard to wade through.

