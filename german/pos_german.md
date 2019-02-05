# Part-of-speech tagging for German
Part-of-speech tagging takes a text and marks grammatical information about all the words (and sometimes associated elements, like punctuation). This is a key step in enabling you to answer questions specific to language use in the text.

## 1. Download the POS tagger
The [Stanford part-of-speech tagger](https://nlp.stanford.edu/static/software/tagger.shtml) includes code for performing part-of-speech tagging, along with a number of language-specific models that have been trained on different kinds or quantities of texts, and that use different sets of grammatical tags.

Go to the ["Downloads" section of the page](https://nlp.stanford.edu/static/software/tagger.shtml#Download) and click on "Download full Stanford Tagger version 3.6.0 [124 MB]" (the available version number may vary.)

Save the zip file to your computer, and unzip it when it's done downloading.

### German POS tags
As described in the Stanford NLP readme file, the default tagger is trained on the first 80% of the [Negra corpus](http://www.coli.uni-saarland.de/projects/sfb378/negra-corpus/negra-corpus.html) (which is based on German newspaper text). It uses the Stuttgart-Tübingen Tagset (STTS), a set of 54 tags for annotating German text corpora with part-of-speech labels.
	  ADJA    attributives Adjektiv                   [das] große [Haus]
      ADJD    adverbiales oder                        [er fährt] schnell
              prädikatives Adjektiv                   [er ist] schnell

      ADV     Adverb                                  schon, bald, doch

      APPR    Präposition; Zirkumposition links       in [der Stadt], ohne [mich]
      APPRART Präposition mit Artikel                 im [Haus], zur [Sache]
      APPO    Postposition                            [ihm] zufolge, [der Sache] wegen
      APZR    Zirkumposition rechts                   [von jetzt] an

      ART     bestimmter oder                         der, die, das,
              unbestimmter Artikel                    ein, eine, ...

      CARD    Kardinalzahl                            zwei [Männer], [im Jahre] 1994
              (Ordinalzahlen sind als ADJA getaggt)

      FM      Fremdsprachliches Material              [Er hat das mit ``]
                                                      A big fish ['' übersetzt]

      ITJ     Interjektion                            mhm, ach, tja

      KOUI    unterordnende Konjunktion               um [zu leben],
              mit ``zu'' und Infinitiv                anstatt [zu fragen]
      KOUS    unterordnende Konjunktion               weil, daß, damit,
              mit Satz                                wenn, ob
      KON     nebenordnende Konjunktion               und, oder, aber
      KOKOM   Vergleichskonjunktion                   als, wie

      NN      normales Nomen                          Tisch, Herr, [das] Reisen
      NE      Eigennamen                              Hans, Hamburg, HSV

      PDS     substituierendes Demonstrativ-          dieser, jener
              pronomen
      PDAT    attribuierendes Demonstrativ-           jener [Mensch]
              pronomen

      PIS     substituierendes Indefinit-             keiner, viele, man, niemand
              pronomen
      PIAT    attribuierendes Indefinit-              kein [Mensch],
              pronomen ohne Determiner                irgendein [Glas]
      PIDAT   attribuierendes Indefinit-              [ein] wenig [Wasser],
              pronomen mit Determiner                 [die] beiden [Brüder]

      PPER    irreflexives Personalpronomen           ich, er, ihm, mich, dir

      PPOSS   substituierendes Possessiv-             meins, deiner
              pronomen
      PPOSAT  attribuierendes Possessivpronomen       mein [Buch], deine [Mutter]

      PRELS   substituierendes Relativpronomen        [der Hund ,] der
      PRELAT  attribuierendes Relativpronomen         [der Mann ,] dessen [Hund]

      PRF     reflexives Personalpronomen             sich, einander, dich, mir

      PWS     substituierendes                        wer, was
              Interrogativpronomen
      PWAT    attribuierendes                         welche [Farbe],
              Interrogativpronomen                    wessen [Hut]
      PWAV    adverbiales Interrogativ-               warum, wo, wann,
              oder Relativpronomen                    worüber, wobei

      PAV     Pronominaladverb                        dafür, dabei, deswegen, trotzdem

      PTKZU   ``zu'' vor Infinitiv                    zu [gehen]
      PTKNEG  Negationspartikel                       nicht
      PTKVZ   abgetrennter Verbzusatz                 [er kommt] an, [er fährt] rad
      PTKANT  Antwortpartikel                         ja, nein, danke, bitte
      PTKA    Partikel bei Adjektiv                   am [schönsten],
              oder Adverb                             zu [schnell]

      TRUNC   Kompositions-Erstglied                  An- [und Abreise]

      VVFIN   finites Verb, voll                      [du] gehst, [wir] kommen [an]
      VVIMP   Imperativ, voll                         komm [!]
      VVINF   Infinitiv, voll                         gehen, ankommen
      VVIZU   Infinitiv mit ``zu'', voll              anzukommen, loszulassen
      VVPP    Partizip Perfekt, voll                  gegangen, angekommen
      VAFIN   finites Verb, aux                       [du] bist, [wir] werden
      VAIMP   Imperativ, aux                          sei [ruhig !]
      VAINF   Infinitiv, aux                          werden, sein
      VAPP    Partizip Perfekt, aux                   gewesen
      VMFIN   finites Verb, modal                     dürfen
      VMINF   Infinitiv, modal                        wollen
      VMPP    Partizip Perfekt, modal                 gekonnt, [er hat gehen] können

      XY      Nichtwort, Sonderzeichen                3:7, H2O,
              enthaltend                              D2XW3

      $,      Komma                                   ,
      $.      Satzbeendende Interpunktion             . ? ! ; :
      $(      sonstige Satzzeichen; satzintern        - [,]()

### German Universal Dependencies tags
Alternately, you can choose to use the German tagger that draws on the [Universal Dependencies](https://universaldependencies.org/) tag set. It's not totally clear which UD treebank(s) it's drawing from but here's a [comparison of the UD treebanks](https://universaldependencies.org/treebanks/de-comparison.html).

You can read more about [how the Universal Dependencies tags are used for German](https://universaldependencies.org/de/index.html).


## 2. Prepare your text
To use the tagger, you need to have the text you're working with saved as a Unicode (UTF-8) text file. You should also name the file without any spaces; e.g. instead of *my example file.txt*, name it *my-example-file.txt*, *my_example_file.txt*, *myexamplefile.txt*. Spaces mean something else when you're working with the command line, and while there's workarounds for using a file with spaces in its name, it's easiest to just avoid it.

It will be simplest for you to run the part-of-speech tagger if you copy your text file into the _stanford-postagger-full-2018-10-16_ folder that you unzipped. If you're comfortable navigating file paths in the command line, you can skip this step.

## 3. Run the tagger
**On a Mac**
Open a new terminal window, and navigate to the POS tagger folder. Unless you saved it somewhere else, you should be able to enter:
`cd Downloads/stanford-postagger-full-2018-10-16`

Once you're in the folder, you can run `ls` and check for the name of your text file if you want to make sure you moved it into the right folder.

Run the following command, replacing **yourtext.txt** with the name of your text file:

`java -cp "*" edu.stanford.nlp.tagger.maxent.MaxentTagger -model models/german-hgc.tagger -textFile yourtext.txt -outputFormat tsv -outputFile yourposoutput.txt`

A few lines of text should appear, concluding with a message along the lines of *Tagged 768 words at 864.86 words per second.* (where the numbers will vary based on your text and your computer)

If you want to try the universal dependencies tagger, you can replace *german-hgc.tagger* with **german-ud.tagger**.

## 4. Look at the output
You can open the output in a plain text editor, which will display two columns: one with the German words, and one with the part-of-speech tags.

To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and non-ASCII characters will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with the POS tagger), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

Your text will appear in two columns, with one word per row in the first column, and one tag per row in the second column. A blank row will exist to indicate a new line in your original text. (For instance, if your original text is poetry, each line of the poem will be separated by a blank row.)

You can sort your sheet by column B to see, for instance, all the nouns in the text. Note, though, that this will lose the original sentence-based structure of the file.

If you want to count, for instance, at the average number of nouns per sentence, you'll need to use a different output format from the part-of-speech tagger. In the code above where you ran the POS tagger, you could replace **txt** with **xml** to get an output file with a format that supports queries that depend on text structure.

