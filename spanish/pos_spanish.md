# Part-of-speech tagging for Spanish
Part-of-speech tagging takes a text and marks grammatical information about all the words (and sometimes associated elements, like punctuation). This is a key step in enabling you to answer questions specific to language use in the text.

## 1. Download the POS tagger
The [Stanford part-of-speech tagger](https://nlp.stanford.edu/static/software/tagger.shtml) includes code for performing part-of-speech tagging, along with a number of language-specific models that have been trained on different kinds or quantities of texts, and that use different sets of grammatical tags.

Go to the ["Downloads" section of the page](https://nlp.stanford.edu/static/software/tagger.shtml#Download) and click on "Download full Stanford Tagger version 3.6.0 [124 MB]" (the available version number may vary.)

Save the zip file to your computer, and unzip it when it's done downloading.

### Spanish POS tags
The Spanish tagger uses an abbreviated set of 85 tags, derived from the [AnCora 3.0 corpus](http://clic.ub.edu/corpus/en) (Spanish newswire from Spain plus an older balanced Castilian Spanish corpus), and [DEFT Spanish Treebank](https://catalog.ldc.upenn.edu/LDC2018T01) (which consists of newswire and discussion fora). The tags are less transparent than many. There's further background on the source corpora and methodology on the [Stanford NLP Spanish FAQ page](https://nlp.stanford.edu/software/spanish-faq.shtml).

| Tag | Description | Example(s) |
| --- | --- | --- |
| Adjectives |
| `ao0000` | Adjective (ordinal) | *primera*, *segundo*, *últimos* |
| `aq0000` | Adjective (descriptive) | *populares*, *elegido*, *emocionada*, *andaluz* |
| Conjunctions |
| `cc` | Conjunction (coordinating) | *y*, *o*, *pero* |
| `cs` | Conjunction (subordinating) | *que*, *como*, *mientras* |
| Determiners |
| `da0000` | Article (definite) | *el*, *la*, *los*, *las* |
| `dd0000` | Demonstrative | *este*, *esta*, *esos* |
| `de0000` | "Exclamative" (TODO) | *qué* (*¡Qué pobre!*) |
| `di0000` | Article (indefinite) | *un*, *muchos*, *todos*, *otros* |
| `dn0000` | Numeral | *tres*, *doscientas* |
| `do0000` | Numeral (ordinal) | *el **65** aniversario* |
| `dp0000` | Possessive | *sus*, *mi* |
| `dt0000` | Interrogative | *cuántos*, *qué*, *cuál* |
| Punctuation |
| `f0` | Other | *&*, *@* |
| `faa` | Inverted exclamation mark | *¡* |
| `fat` | Exclamation mark | *!* |
| `fc` | Comma | *,* |
| `fca` | Left bracket | *[* |
| `fct` | Right bracket | *]* |
| `fd` | Colon | *:* |
| `fe` | Double quote | *"* |
| `fg` | Hyphen | *-* |
| `fh` | Forward slash | */* |
| `fia` | Inverted question mark | *¿* |
| `fit` | Question mark | *?* |
| `fp` | Period / full-stop | *.* |
| `fpa` | Left parenthesis | *(* |
| `fpt` | Right parenthesis | *)* |
| `fra` | Left guillemet / angle quote | *«* |
| `frc` | Right guillemet / angle quote | *»* |
| `fs` | Ellipsis | *...*, *etcétera* |
| `ft` | Percent sign | *%* |
| `fx` | Semicolon | *;* |
| `fz` | Single quote | *'* |
| Interjections |
| `i` | Interjection | *ay*, *ojalá*, *hola* |
| Nouns |
| `nc00000` | Unknown common noun (neologism, loanword) | *minidisc*, *hooligans*, *re-flotamiento* |
| `nc0n000` | Common noun (invariant number) | *hipótesis*, *campus*, *golf* |
| `nc0p000` | Common noun (plural) | *años*, *elecciones* |
| `nc0s000` | Common noun (singular) | *lista*, *hotel*, *partido* |
| `np00000` | Proper noun | *Málaga*, *Parlamento*, *UFINSA* |
| Pronouns |
| `p0000000` | Impersonal *se* | *se* |
| `pd000000` | Demonstrative pronoun | *éste*, *eso*, *aquellas* |
| `pe000000` | "Exclamative" pronoun | *qué* |
| `pi000000` | Indefinite pronoun | *muchos*, *uno*, *tanto*, *nadie* |
| `pn000000` | Numeral pronoun | *dos* *miles*, *ambos* |
| `pp000000` | Personal pronoun | *ellos*, *lo*, *la*, *nos* |
| `pr000000` | Relative pronoun | *que*, *quien*, *donde*, *cuales* |
| `pt000000` | Interrogative pronoun | *cómo*, *cuánto*, *qué* |
| `px000000` | Possessive pronoun | *tuyo*, *nuestra* |
| Adverbs |
| `rg` | Adverb (general) | *siempre*, *más*, *personalmente* |
| `rn` | Adverb (negating) | *no* |
| Prepositions |
| `sp000` | Preposition | *en*, *de*, *entre* |
| Verbs |
| `va00000` | Verb (unknown) | *should* |
| `vag0000` | Verb (auxiliary, gerund) | *habiendo* |
| `vaic000` | Verb (auxiliary, indicative, conditional) | *habría*, *habríamos* |
| `vaif000` | Verb (auxiliary, indicative, future) | *habrá*, *habremos* |
| `vaii000` | Verb (auxiliary, indicative, imperfect) | *había*, *habíamos* |
| `vaip000` | Verb (auxiliary, indicative, present) | *ha*, *hemos* |
| `vais000` | Verb (auxiliary, indicative, preterite) | *hubo*, *hubimos* |
| `vam0000` | Verb (auxiliary, imperative) | *haya* |
| `van0000` | Verb (auxiliary, infinitive) | *haber* |
| `vap0000` | Verb (auxiliary, participle) | *habido* |
| `vasi000` | Verb (auxiliary, subjunctive, imperfect) | *hubiera*, *hubiéramos*, *hubiese* |
| `vasp000` | Verb (auxiliary, subjunctive, present) | *haya*, *hayamos* |
| `vmg0000` | Verb (main, gerund) | *dando*, *trabajando* |
| `vmic000` | Verb (main, indicative, conditional) | *daría*, *trabajaríamos* |
| `vmif000` | Verb (main, indicative, future) | *dará*, *trabajaremos* |
| `vmii000` | Verb (main, indicative, imperfect) | *daba*, *trabajábamos* |
| `vmip000` | Verb (main, indicative, present) | *da*, *trabajamos* |
| `vmis000` | Verb (main, indicative, preterite) | *dio*, *trabajamos* |
| `vmm0000` | Verb (main, imperative) | *da*, *dé*, *trabaja*, *trabajes*, *trabajemos* |
| `vmn0000` | Verb (main, infinitive) | *dar*, *trabjar* |
| `vmp0000` | Verb (main, participle) | *dado*, *trabajado* |
| `vmsi000` | Verb (main, subjunctive, imperfect) | *diera*, *diese*, *trabajáramos*, *trabajésemos* |
| `vmsp000` | Verb (main, subjunctive, present) | *dé*, *trabajemos* |
| `vsg0000` | Verb (semiauxiliary, gerund) | *siendo* |
| `vsic000` | Verb (semiauxiliary, indicative, conditional) | *sería*, *serían* |
| `vsif000` | Verb (semiauxiliary, indicative, future) | *será*, *seremos* |
| `vsii000` | Verb (semiauxiliary, indicative, imperfect) | *era*, *éramos* |
| `vsip000` | Verb (semiauxiliary, indicative, present) | *es*, *son* |
| `vsis000` | Verb (semiauxiliary, indicative, preterite) | *fue*, *fuiste* |
| `vsm0000` | Verb (semiauxiliary, imperative) | *sea*, *sé* |
| `vsn0000` | Verb (semiauxiliary, infinitive) | *ser* |
| `vsp0000` | Verb (semiauxiliary, participle) | *sido* |
| `vssf000` | Verb (semiauxiliary, subjunctive, future) | *fuere* |
| `vssi000` | Verb (semiauxiliary, subjunctive, imperfect) | *fuera*, *fuese*, *fuéramos* |
| `vssp000` | Verb (semiauxiliary, subjunctive, present) | *sea*, *seamos* |
| Dates |
| `w` | Date | *octubre*, *jueves*, *2002* |
| Numerals |
| `z0` | Numeral | *547.000*, *04*, *52,52* |
| `zm` | Numeral qualifier (currency) | *dólares*, *euros* |
| `zu` | Numeral qualifier (other units) | *km*, *cc* |
| Other |
| `word` | Emoticon or other symbol | *:)*, *®* |

### Spanish Universal Dependencies tags
Alternately, you can choose to use the Spanish tagger that draws on the [Universal Dependencies](https://universaldependencies.org/) tag set, which draws on the AnCora corpus described above, as well as some treebanks that were developed specifically for Universal Dependencies. Here's a [comparison of the treebanks](https://universaldependencies.org/treebanks/es-comparison.html).

You can read more about [how the Universal Dependencies tags are used for Spanish](https://universaldependencies.org/es/index.html).


## 2. Prepare your text
To use the tagger, you need to have the text you're working with saved as a Unicode (UTF-8) text file. An example text file you can use for this exercise is [a few lines from "Muerte de Narciso" by José Lezama Lima](muerte_de_narciso.txt).

It will be simplest for you to run the part-of-speech tagger if you copy your text file into the _stanford-postagger-full-2018-10-16_ folder that you unzipped. If you're comfortable navigating file paths in the command line, you can skip this step.

## 3. Run the tagger
**On a Mac**
Open a new terminal window, and navigate to the POS tagger folder. Unless you saved it somewhere else, you should be able to enter:
`cd Downloads/stanford-postagger-full-2018-10-16`

Once you're in the folder, you can run `ls` and check for the name of your text file if you want to make sure you moved it into the right folder.

Run the following command, replacing **yourtext.txt** with the name of your text file:

`java -cp "*" edu.stanford.nlp.tagger.maxent.MaxentTagger -model models/spanish-distsim.tagger -textFile yourtext.txt -outputFormat tsv -outputFile yourposoutput.txt`

A few lines of text should appear, concluding with a message along the lines of *Tagged 768 words at 864.86 words per second.* (where the numbers will vary based on your text and your computer)

If you want to try the universal dependencies tagger, you can replace *spanish-distsim.tagger* with **spanish-ud.tagger**.

- [Sample text annotated using spanish-distsim tags](muerte-distsim.txt)
- [Sample text annotated with Universal Dependencies tags](muerte-ud.txt)

## 4. Look at the output
You can open the output in a plain text editor, which will display two columns: one with the Spanish words, and one with the part-of-speech tags.

To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and non-ASCII characters will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with the POS tagger), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

Your text will appear in two columns, with one word per row in the first column, and one tag per row in the second column. A blank row will exist to indicate a new line in your original text. (For instance, if your original text is poetry, each line of the poem will be separated by a blank row.)

You can sort your sheet by column B to see, for instance, all the nouns in the text. Note, though, that this will lose the original sentence-based structure of the file.

If you want to count, for instance, at the average number of nouns per sentence, you'll need to use a different output format from the part-of-speech tagger. In the code above where you ran the POS tagger, you could replace **txt** with **xml** to get an output file with a format that supports queries that depend on text structure.

- [Sample text annotated with Universal Depdencies tags, in XML format](muerte-ud.xml)

