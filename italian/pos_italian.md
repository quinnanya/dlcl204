# Part-of-speech tagging for Italian
Part-of-speech tagging takes a text and marks grammatical information about all the words (and sometimes associated elements, like punctuation). This is a key step in enabling you to answer questions specific to language use in the text.

## 1. Download the POS tagger
[TINT (The Italian NLP Tool)](http://tint.fbk.eu/) is based on [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/) but includes training data for Italian.

The current stable build (v0.2) is no longer compatible with Stanford CoreNLP, and throws errors when you try to run it. Instead, go to the [TINT downloads page](http://tint.fbk.eu/download.html) and download *tint-runner-1.0-SNAPSHOT-bin.tar.gz (latest nightly build, tar.gz)*. Save the file, and unzip it.

### Italian POS tags
TINT is [built using the ISTD (Italian Stanford Dependency Treebank)](http://tint.fbk.eu/pos.html), and uses the following tags.

| Value | Description | Examples | Contexts of use |
| ----------- | ----------- | ----------- | ----------- |
| A | adjective | *bello, buono, pauroso, ottimo* | una **bella** passeggiata\ un **ottimo** attaccante\ una persona **paurosa** |
| AP | possessive adjective | *mio, tuo, nostro, loro* | a **mio** parere\ il **tuo** libro |
| B | adverb | *bene, fortemente, malissimo, domani* | arrivo **domani**\ sto **bene** |
| BN | negative adverb | *no, non, nemmeno* | **non** arrivo **nemmeno** domani\ **non** sto bene |
| CC | coordinate conjunction | *e, o, ma* | i libri **e** i quaderni |
| CS | subordinate conjunction | *mentre, quando* | **quando** ho finito vengo |
| DD | demonstrative determiner | *questo, codesto, quello* | **questo** denaro\ **quella** famiglia |
| DE | exclamative determiner | *che, quale, quanto* | **che** disastro!\ **quale** catastrofe! |
| DI | indefinite determiner | *alcuno, certo, tale, parecchio, qualsiasi* | **alcune** telefonate\ **parecchi** giornali\ **qualsiasi** persona |
| DR | relative determiner | *cui, quale* | i **cui** libri |
| DQ | interrogative determiner | *che, quale, quanto* | **che** cosa\ **quanta** strada\ **quale** formazione |
| E | preposition | *di, a, da, in, su, attraverso, verso, di* | **a** casa del poeta\ prima **di** giorno\ **verso** sera |
| EA | articulated preposition | *del, alla, dal* | a casa **del** poeta\ **all'** alba |
| FB | balanced punctuation | *( ) -* | frutta **(**pere e banane**)** |
| FC | clause boundary punctuation | *, ;* | mele, pere e banane**.** |
| FF | comma | *, -* | mele**,** pere e banane |
| FS | sentence boundary punctuation | *; . ? !* | cosa vuoi**?** |
| I | interjection | *ahimè, beh, ecco, grazie* | **Beh**, che vuoi? |
| N | cardinal number | *uno, due, cento, mille, 28, 2000* | **due** partite\ **28** anni |
| NO | ordinal number | *primo, secondo, centesimo* | **secondo** posto |
| PC | clitic pronoun | *ci, vi, ne* | **vi** piace? |
| PD | demonstrative pronoun | *questo, quello, costui* | **quello** di Roma\ **costui** uccide |
| PE | personal pronoun | stressed: *io, tu, egli, lui, noi, voi, essi*\ unstressed: *lo, la, mi, ci, vi* | **io** parto\ **lo** mangio |
| PI | indefinite pronoun | *chiunque, ognuno, molto* | **chiunque** venga\ i diritti di **ognuno** |
| PP | possessive pronoun | *mio, tuo, suo, loro, proprio* | il **mio**è qui\ più bella della **loro** |
| PR | relative pronoun | *che, cui, quale* | **ciò** che dice\ il **quale** afferma\ a **cui** parlo |
| PQ | interrogative pronoun | *che, chi, quanto* | non so **chi** parta\ **quanto** costa?\ **che** ha fatto ieri? |
| RD | determinative article | *il, lo, la, i, gli, le* | **il** libro\ **i** gatti |
| RI | indeterminative article | *uno, un, una* | **un** amico\ **una** bambina |
| S | common noun | *amico, insegnante, verità* | l'**amico**\ la **verità** |
| SP | proper noun | *Monica, Pisa, Fiat, Sardegna* | **Monica** scrive |
| SW | foreign noun | *fazenda, mulieris dignitatem, weekend* | una **fazenda** in Brasile\ il prossimo **weekend** |
| T | predeterminer | *tutti i giorni* | **tutti** i giorni\ **entrambi** i genitori |
| V | verb | *mangio, avere, passato* | il tempo **passa**\ le **scriverò** una lettera\ **vengo** domani |
| VA | auxiliary verb | *sono stato, ho mangiato* | il peggio **è** passato\ **ho scritto** una lettera |
| VM | modal verb | *posso, devono* | il peggio **deve** venire\ **dovrò** scriverle una lettera |
| X | residual class: it includes formulae,\ unclassified words, alphabetic symbols\ and the like |  distanziare di piacce |


## 2. Prepare your text
To use the segmenter, you need to have the text you're working with saved as a Unicode (UTF-8) text file. An example text file you can use for this exercise is [a few lines from "Una questione privata" by  Beppe Fenoglio](questione.txt).

You should also name the file without any spaces; e.g. instead of *my example file.txt*, name it *my-example-file.txt*, *my_example_file.txt*, *myexamplefile.txt*. Spaces mean something else when you're working with the command line, and while there's workarounds for using a file with spaces in its name, it's easiest to just avoid it.

It will be simplest for you to run the part-of-speech tagger if you copy your text file into the _tint_ folder that you unzipped. If you're comfortable navigating file paths in the command line, you can skip this step.

## 3. Run the tagger
**On a Mac**
Open a new terminal window, and navigate to the *tint* folder. Unless you saved it somewhere else, you should be able to enter:
`cd Downloads/tint`

Once you're in the folder, you can run `ls` and check for the name of your text file if you want to make sure you moved it into the right folder.

Run the following command, replacing **yourtext.txt** with the name of your text file:

`cat yourtext.txt | ./tint.sh -o yourposoutput.txt -f textpro`

A few lines of text should appear, ending with *Tint is ready*, before returning you to the command line. If everything worked correctly, you should see a new file, *yourposoutput.txt*, in the directory.

- [Sample text annotated](questione-pos.txt)

## 4. Look at the output
You can open the output in a plain text editor, which will display a series of columns. 

To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and non-ASCII characters will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with Tint), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

Your text will appear in a series of columns. The most important are:

* tokenid: this gives a unique ID to each word or piece of punctuation
* parserid: this gives an ID number indicating order within a sentence
* pos: the part of speech, using the tags described above
* entity: indicates whether the word has been flagged as a named entity (PER for person, LOC for location)
* deprel: [universal dependency relation](https://universaldependencies.org/u/dep/index.html), further linguistic information about the word

You can sort your sheet by *pos* (column E) to see, for instance, all the nouns in the text. Note, though, that this will lose the original sentence-based structure of the file -- although you can always restore this by sorting by *tokenid* (column A).