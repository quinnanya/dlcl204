# Part-of-speech tagging for Japanese
Part-of-speech tagging takes a text and marks grammatical information about all the words (and sometimes associated elements, like punctuation). This is a key step in enabling you to answer questions specific to language use in the text.

The current gold standard for Japanese NLP seems to be [MeCab](http://taku910.github.io/mecab/).

I ran into problems I couldn't overcome with an *input-buffer overflow. The line is split* error. There's [a blog post about how to fix this](https://blog.keinos.com/20180304_3591) that I tried with the help of Google Translate, but wasn't able to get it to work.

If you have MeCab installed and working, you should use that instead, using the documentation on the MeCab website. If you can't install or run MeCab, you can try Rakuten MA instead.

##1.  Japanese POS tags
The source of the model Rakuten MA uses isn't clearly documented, so it's hard to tell how good a fit it is going to be for any given text. There are [instructions for training a new model](https://github.com/rakuten-nlp/rakutenma#training-your-own-analysis-model-from-scratch). The tags used are:

| Tag | Original JA name | English |
| ---- | ---- | ---- |
| A-c | 形容詞-一般 | Adjective-Common |
| A-dp | 形容詞-非自立可能 | Adjective-Dependent |
| C | 接続詞 | Conjunction |
| D | 代名詞 | Pronoun |
| E | 英単語 | English word |
| F | 副詞 | Adverb |
| I-c | 感動詞-一般 | Interjection-Common |
| J-c | 形状詞-一般 | Adjectival Noun-Common |
| J-tari | 形状詞-タリ | Adjectival Noun-Tari |
| J-xs | 形状詞-助動詞語幹 | Adjectival Noun-AuxVerb stem |
| M-aa | 補助記号-AA | Auxiliary sign-AA |
| M-c | 補助記号-一般 | Auxiliary sign-Common |
| M-cp | 補助記号-括弧閉 | Auxiliary sign-Open Parenthesis |
| M-op | 補助記号-括弧開 | Auxiliary sign-Close Parenthesis |
| M-p | 補助記号-句点 | Auxiliary sign-Period |
| N-n | 名詞-名詞的 | Noun-Noun |
| N-nc | 名詞-普通名詞 | Noun-Common Noun |
| N-pn | 名詞-固有名詞 | Noun-Proper Noun |
| N-xs | 名詞-助動詞語幹 | Noun-AuxVerb stem |
| O | その他 | Others |
| P | 接頭辞 | Prefix |
| P-fj | 助詞-副助詞 | Particle-Adverbial |
| P-jj | 助詞-準体助詞 | Particle-Phrasal |
| P-k | 助詞-格助詞 | Particle-Case Marking |
| P-rj | 助詞-係助詞 | Particle-Binding |
| P-sj | 助詞-接続助詞 | Particle-Conjunctive |
| Q-a | 接尾辞-形容詞的 | Suffix-Adjective |
| Q-j | 接尾辞-形状詞的 | Suffix-Adjectival Noun |
| Q-n | 接尾辞-名詞的 | Suffix-Noun |
| Q-v | 接尾辞-動詞的 | Suffix-Verb |
| R | 連体詞 | Adnominal adjective |
| S-c | 記号-一般 | Sign-Common |
| S-l | 記号-文字 | Sign-Letter |
| U | URL | URL |
| V-c | 動詞-一般 | Verb-Common |
| V-dp | 動詞-非自立可能 | Verb-Dependent |
| W | 空白 | Whitespace |
| X | 助動詞 | AuxVerb |


## 2. Use Rakuten MA
Go to the [Rakuten MA Demo Page](http://rakuten-nlp.github.io/rakutenma/); it may take a moment to load the first time. 

Paste your text into the box, and select "Japanese". Then click the "Analyze" button. Select all the text that appears in the box below.


## 3. Clean up the output
Install [Atom text editor](https://atom.io/), and open a new plain text file. Paste in the text from Rakuten MA.

Using the menu bar at top, go to *Find > Find in buffer*. This will open a toolbar at the bottom where you can do find-and-replace.

Click on the button in the upper right of the find-and-replace toolbar that looks like a period with a star next to it. This turns on the feature for using regular expressions (regex), a powerful specialized syntax for find-and-replace.

To make the results show up in columns in Excel, we need to use a tab character between the words and their annotations, and a new line (line break) character between words.

* In the "find" box, type **\|** (copy and paste this), and in the "replace" box, type **\n** (if you have regex turned on, it should appear in blue)
* Hit the "Replace All" button
* Clear out the "find" box, then type one space character (i.e. hit the space bar one time); in the "replace" box, type **\t**
* Hit the "Replace All" button

Save your file.


## 4. Look at the output
You can open the output in a plain text editor, which will display two columns: one with the words, and one with the part-of-speech tags. 

To be able to sort the results more easily, you can use Excel -- but don't try to open the file directly in Excel, because Excel will mess up the encoding and the text will be jibberish.

Instead, open a new, blank document in Excel. Using hte top navigation bar, go to *Data > Get eternal data > Import text file*. Select the output (look in the folder with Tint), and in the "File origin" dropdown, choose *Unicode (UTF-8)*. Your text should become readable in the preview. The rest of the default settings are fine, so click *Finish*.

When it asks where to put the data, choose the top left column (selected by default) and hit *OK*.

You can sort your sheet by column B to see, for instance, all the nouns in the text. Note, though, that this will lose the original sentence-based structure of the file.

If you want to be able to get back to the original order, you can go to a blank column to the right of your part-of-speech tags (column C), and type 1 in the first row, 2 in the second, etc. until you have 3-4 values. Then, highlight those values that you've entered, and you can drag the lower-right corner of the lowest cell to fill that whole column with ordinal numbers