# Named entity recognition for Portuguese
Named entity recognition (NER) attempts to identify proper names (and sometimes other things, like money and time) in your text. What you do with those entities depends on what they are, and what your research question is. People's names could be used (in conjunction with other information) to map networks of relationships. Locations can be geocoded and placed on a map. Time can be organized chronologically, etc.

For this tutorial, we'll be focusing on location names. The end point of this tutorial will be a CSV (comma-separated values) spreadsheet file that you can use as the input of the Geocoding and Palladio Mapping tutorial.


## 1. Download Stanford CoreNLP
The [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) includes code for doing named entity recognition, along with models for English.

Go to the ["Downloads" section of the page](https://stanfordnlp.github.io/CoreNLP/index.html#download) and click on the big red "Download CoreNLP 3.9.2".

Save the zip file to your computer, and unzip it when it's done downloading. This will create a folder named *stanford-corenlp-full-2018-10-05*.


## 2. Download Portuguese training data
Next, you'll need to download the Portuguese training data for Stanford CoreNLP.

Go to the [ner-re-pt Github repo](https://github.com/arop/ner-re-pt) and click the green "Clone or download" button in the upper right. Download and unzip the .zip file. This will create a folder called *ner-re-pt-master*.

Open the folder, and then open the *tools* folder, then the *stanford-ner* folder. Select all the files and folders in the *stanford-ner* folder and move them into the *stanford-corenlp-full-2018-10-05* folder you unzipped after downloading Stanford CoreNLP.

## 3. Edit the properties file
Open the *props* folder that you've moved into *stanford-corenlp-full-2018-10-05*. Open *sigarra.prop* in a plain text editor. 

In line 2 and line 6, replace *../../* so that line 2 reads *trainFile = outputs/repeat-3/fold-9/t_filtered_train.txt* and line 6 reads *serializeTo = models/repeat-3/fold-9/filtered-ner-model.ser.gz*.

Save the file and close it. Move *sigarra.prop* from the *properties* folder directly into the *stanford-corenlp-full-2018-10-05*

## 4. Train the annotator
**On a Mac**
Open a new Terminal and navigate to your *stanford-corenlp-full-2018-10-05* folder. For instance, if it's in Downloads, type:

`cd Downloads/stanford-corenlp-full-2018-10-05`

Once you're in the Stanford CoreNLP directory, you can train the tagger. Note: this is a memory-intensive process, and may be more than you can do successfully on your laptop.

To train the annotator, type:
`java -Xms4G -cp "*" edu.stanford.nlp.ie.crf.CRFClassifier -prop sigarra.prop`


## 5. ???
I haven't been able to get past this step yet due to my laptop running out of memory. 

## Acknowledgements
Many thanks to [André Pires](https://github.com/arop) for sharing the code and  [tutorial](https://github.com/arop/ner-re-pt/wiki/Stanford-CoreNLP) from his master's thesis.