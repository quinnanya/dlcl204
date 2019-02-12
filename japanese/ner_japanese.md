# Named entity recognition for Japanese
Named entity recognition (NER) attempts to identify proper names (and sometimes other things, like money and time) in your text. What you do with those entities depends on what they are, and what your research question is. People's names could be used (in conjunction with other information) to map networks of relationships. Locations can be geocoded and placed on a map. Time can be organized chronologically, etc.

For this tutorial, we'll be focusing on location names. The end point of this tutorial will be a CSV (comma-separated values) spreadsheet file that you can use as the input of the Geocoding and Palladio Mapping tutorial.

## 1. Install OpenNLP

Go to the [Apache OpenNLP website](https://opennlp.apache.org/) and click the red download button to go to the downloads. Click on *apache-opennlp-1.9.1-bin.zip* to download that file. Unzip it after you've downloaded it. This will give you a folder called *apache-opennlp-1.9.1*.

Now, go to the [Rondhuit website](https://www.rondhuit.com/apache-opennlp-1-9-0-ja-ner.html) and scroll down until you see a link to download *rondhuit-ja-ner-1.0.0.zip*. Click on it, and unzip it when it's downloaded. This will give you a folder called *rondhuit-ja-ner-1.0.1*. Open that folder, and move the *rondhuit-ja-ner-1.0.0.bin* file into your *apache-opennlp-1.9.1* folder.

## 2. Prepare your text
To do named entity recognition, you need to have the text you're working with available as plain Unicode (UTF-8) text. You will also need to ensure that the text has been *segmented* using a tool like [MeCab](http://taku910.github.io/mecab/).


For an example text that includes many place names, you can use this excerpt from the [Japanese-language Wikipedia article on Seattle](seattle-jp-segmented.txt).

## 3. Run the annotator
**On a Mac**
Open a new terminal window, and navigate to the *apache-opennlp-1.9.1* folder.

Type:
`./bin/opennlp TokenNameFinder rondhuit-ja-ner-1.0.0.bin`

and press "Enter". 

You should see a message: *Loading Token Name Finder model ... done (0.427s)*

Open the text you're working with in a plain-text editor, and copy and paste it into your terminal and press "Enter".

It will scroll through the terminal and show your text, annotated with named entities.

Copy your annotated text from the terminal window and paste it into a plain text file.

## 4. Clean up the output
Open the plain text output file in a plain text editor. [Atom](https://atom.io/) is recommended here because you'll need to clean up the output.

Using the Atom menu bar, go to *Find > Replace in buffer*. This will open a find-and-replace toolbar at the bottom of the screen.

While there are a few different kinds of annotations, the ones we're interested in are the locations.

Click the little button in the upper right of the find-and-replace toolbar with _.*_ on it. This will enable you to use *regular expressions*, a powerful syntax for pattern matching, in your queries.

In the "find" field, enter `<START:LOCATION>(.*)<END>`

Click the "find" button, and scroll through the locations identified by the script.

Select the text between *<START:LOCATION>* and *<END>* and paste each location into a new plain text document, one location per line.

## 5. Save your list of places
Once you're done cleaning the data as described above, save your data (which should be just a single column of place names) as **places.csv**. If you name the file something else, or use different capitalization, etc., you'll have to change the Python code that does the coordinate lookup. It's easier to just name it **places.csv**.

## 7. Move on to Geocoding and Palladio Mapping Tutorial
You're done with the language-specific part! Next, move on to the [Geocoding and Palladio Mapping Tutorial](/palladio/geocoding_palladio_mapping.md).
