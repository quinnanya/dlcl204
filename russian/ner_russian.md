# Named entity recognition for Russian
Named entity recognition (NER) attempts to identify proper names (and sometimes other things, like money and time) in your text. What you do with those entities depends on what they are, and what your research question is. People's names could be used (in conjunction with other information) to map networks of relationships. Locations can be geocoded and placed on a map. Time can be organized chronologically, etc.

For this tutorial, we'll be focusing on location names. The end point of this tutorial will be a CSV (comma-separated values) spreadsheet file that you can use as the input of the Geocoding and Palladio Mapping tutorial.

## 1. Install natasha

[Natasha](https://github.com/natasha/natasha) is a Python module (code) that does named entity recognition for Russian.

**On a Mac**
Open a new terminal window. Type:
`python -m pip install natasha`

You'll see it scroll through various lines of text, downloading and installing dependencies for the *natasha* module.

If you're returned to the command line without any errors, then you've installed *natasha* successfully.


## 2. Download and edit Python script
Download [russian_ner.py](russian_ner.py). This is the script that calls the *natasha* module to do the named-entity recognition for locations. (Note: if you want to use it to do named entity extraction for personal names, you can open it in a plain text editor and replace *LocationExtractor* with *NamesExtractor*. Be sure to do this towards the top, and towards the bottom of the file -- there are two places where it occurs.)

This script includes the text of the Russian-language Wikipedia article on Seattle, which has many place names.

If you want to use your own text, open *russian_ner.py* in a plain text editor (like [Atom](https://atom.io/), which is cross-platform).

You can delete all the text after *text = '''* (line 6) and before the closing *'''* (line 289) and replace it with your own text.

Save the Python script when you've replaced the sample text with your own.

## 3. Run the annotator
**On a Mac**
Open a new terminal window, and navigate to where you've saved the *russian_ner.py* script.

Type:
`python russian_ner.py > ner_output.txt`

and press "Enter". The command prompt will disappear while it's processing, and it may take a few seconds before it reappears. When it does, you should have a new text file, *ner_output.txt*, in the same folder as the Python script.

## 4. Clean up the output
Open *ner_output.txt* in a plain text editor. [Atom](https://atom.io/) is recommended here because you'll need to clean up the output.

You should see a bunch of lines that look like:
[203, 212) Location(name='вашингтон')
[253, 259) Location(name='сиэтл')

All we want is the place names in between the quotes.

Using the Atom menu bar, go to *Find > Replace in buffer*. This will open a find-and-replace toolbar at the bottom of the screen.

- In the "find" field, type `Location(name='` and replace it with nothing
- In the "find" field, type `')` and replace it with nothing
- Click the little button in the upper right of the find-and-replace toolbar with _.*_ on it. This will enable you to use *regular expressions*, a powerful syntax for pattern matching, in your queries.
- In the "find" field, type `[0-9]*` and replace it with nothing.
- Click on the _.*_ button again to turn off regular expressions.
- In the "find" field, type `[, ) ` and replace it with nothing. (Don't forget to put a space at the end after the parenthesis.)

This should leave you with a list of place names.

## 5. Save your list of places
Once you're done cleaning the data as described above, save your data (which should be just a single column of place names) as **places.csv**. If you name the file something else, or use different capitalization, etc., you'll have to change the Python code that does the coordinate lookup. It's easier to just name it **places.csv**.

## 7. Move on to Geocoding and Palladio Mapping Tutorial
You're done with the language-specific part! Next, move on to the [Geocoding and Palladio Mapping Tutorial](/palladio/geocoding_palladio_mapping.md).
