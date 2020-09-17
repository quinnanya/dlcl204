# Web scraping with Webscraper.io (adapted from The Data-Sitters Club)

I do a lot of web scraping. When I need to do something simple, quick, and relatively small-scale, I go with webscraper.io, even though it gives you less flexibility in structuring and exporting your results compared to Python. If you need to scrape data from webpages, it's a good place to start if you're not already comfortable with Python.

If your data is complex, or spread across lots of different websites, the Webscraper.io plugin discussed below may not be the right tool for you. One of the things that 

I knew the [Baby-Sitters Club Wiki](https://babysittersclub.fandom.com/wiki/The_Baby-Sitters_Club_Wiki) on Fandom.com had the data I needed, presented as well-structured metadata on each book page. Webscraper.io was going to be a good tool for this job.

Webscraper.io is a plugin for the Chrome browser, so first you need to [install it from the Chrome store](https://webscraper.io/documentation/installation). Next, you need to 1) access it in your browser by opening the *Developer Tools* panel, then 2) choose *Web Scraper* from the tabs at the top of the panel.

![Launching the webscraper plugin](/site/assets/dscm3_launchwebscraper.jpg)

#### Creating a sitemap

Using Webscraper.io's menu, go to *Create new sitemap > Create sitemap*, as shown by arrow 3, above. (Note: if you want to import an existing sitemap, like one of the complete ones that we've posted at the [Data-Sitters Club GitHub repo for this book](https://github.com/datasittersclub/dscm3), you can choose "Import Sitemap" and copy and paste the text from the appropriate sitemap text file into the text field. If you run into trouble with the instructions here, importing one of our sitemaps and playing around with it might help you understand it better.)

The first page is where you put in the start URL of the page you want to scrape. If you're trying to scrape multiple pages of data, and the site uses pagination that involves appending some page number to the end of the URL (e.g. if you go to the second page of results and you see the URL is the same except for something like `?page=2` on the end), you can set a range here, e.g. http://www.somesite.com/results?page=[1-5] if there are 5 pages of results. In our case, though, we have eight *different* web pages we want to scrape for URLs, one for each book (sub-)series.

First, we'll give our scraper a name (it can be almost anything; I went with *bsc_fan_wiki_link_scraper*). For the URL, I just put in the URL for the main book series, <https://babysittersclub.fandom.com/wiki/Category:The_Baby-Sitters_Club_series>. If you have multiple pages (and especially if you're putting in a range), it's often best to start by putting in a single page, setting up the scraper, checking the results, and seeing if you need to make any modifications before you scrape hundreds of pages without capturing what you need. (Trust me -- it's a mistake I've made!)

#### Handling selectors: easy mode

Web scraping is *a lot easier* if you know at least a little bit about HTML, how it's structured, and some common elements. Especially once you get into Python-based web scraping, CSS becomes important, too. I was lucky enough to learn HTML in elementary school (my final project in the 5th grade was a Sailor Moon fan site, complete with starry page background and at least one <blink> element), so it's hard for me to remember not knowing this stuff. But there's lots of tutorials out there, like this one from [W3Schools](https://www.w3schools.com/html/html_intro.asp), that can get you up to speed with the basics and let you play around with it if you're not really comfortable with HTML.

The way we set up a web scraper is related to the way HTML is structured: HTML is made up of nested elements, and if we're doing something complex with our scraper, it'll have a nested structure, too.

For our first scraper, we're *just* trying to get the URLs of all the links on each page.

We'll start by hitting the "Add new selector" button, which takes us to a different interface for choosing the selector. You have to give it a unique ID (I chose *pagelink*), then choose a type from the dropdown menu. For now, we just want *Link* for the type. Under the *Selector* header in this interface, check the "multiple" box (there are multiple links on the page), then click the "Select" button. Now the fun begins! Move your mouse back up to the page, and start clicking on the things you want to capture. After you've clicked on 2-3 of them, the scraper usually gets the idea and highlights the rest. In this case, I started clicking in the "A's", and after two clicks it picked up the rest of the entries filed under that letter, but I had to click in the results for a different letter before it picked up *everything*.

![Selecting links for the scraper](/site/assets/dscm3_selecting_links.jpg)

When everything you want is highlighted in red, click the blue "Done selecting" button. What I then had was `ul:nth-of-type(n+3) a.category-page__member-link`. If you're not comfortable with HTML, you might just be relieved that the computer sorted out all *that* mess. But if you know how to read this, you should be concerned. `<ul>` means "unordered list" (typically, but not always, looks like a bullet point list), and we're grabbing the 3rd &gt;ul&lt; on the page. Which, yes, is what we selected: by starting with A on the [regular book series page](https://babysittersclub.fandom.com/wiki/Category:The_Baby-Sitters_Club_series), we're skipping the list with character-based category pages, and the erroneous list where a wiki page name starts with the number 3. If we were just scraping this one page, it'd be fine: we'd get what we selected, which -- deliberately -- is not *every link on the page*. But what about the Super Specials, Mysteries, Super Mysteries, etc? If we start with the third list, will we be missing things?

Take it from someone who's had to scrape (and re-scrape, and re-re-scrape) a Russian Harry Potter fanfic archive multiple times after not being careful enough: it's almost always better to scrape *too much stuff* and have to do some cleaning later, than to *not scrape enough stuff* and have to re-do it, especially if you don't notice until after you've spent a lot of time cleaning up Ghost Cat data-hairballs.

What to do? Well, `:nth-of-type(n+3)` is a modifier on *ul*, so you can drop it to get ALL THE UNORDERED LISTS. But actually, you can go one step further and even get rid of the *ul* part, because what you're actually grabbing *isn'*t unordered lists, but *links* (in HTML, &lt;a&gt; for anchor) that have the class `category-page__member-link`. The period after the a in the selector indicates a class attribute, which you can see if you switch from the "Web Scraper" tab to the "Elements" tab in the developer toolbar.
	
![HTML page view](/site/assets/dscm3_html_view.jpg)

Each link corresponds to HTML that looks something like: `<a href="/wiki/Abby_and_the_Best_Kid_Ever" title="Abby and the Best Kid Ever" class="category-page__member-link">Abby and the Best Kid Ever</a>`. The text *Abby and the Best Kid Ever* (the one that occurs between `>` and `<`) is the text that actually appears on the page. The rest is the HTML instructions used to make that text into a link. But not just any link: a link with the class category-page__member-link, which *only* appears with links that are part of this list of books in the series corresponding to this wiki page (Regular, Mystery, etc.) Those are the links you want. To select &lt;a&gt; tags with the class category-page_member-link, click in the selector text box that reads ul:nth-of-type(n+3) a.category-page_member-link, and delete everything before the *a*.

One good way to make sure you're generally getting what you want is to click the "Data preview" button once you have something in the selection box. What you should see is all the URLs and link titles on the page, along with a _*followSelectorId* field that has the value of pagelink for all the links (i.e. the name you gave the link selector when you created it). What we actually *need* is just the URLs, so the rest is Ghost Cat hairball, but there's no easy way to get *only* what we need using the Webscraper.io plugin, so we'll take it all and clean it up later.

![Previewing data](/site/assets/dscm3_data_preview.png)

Click the blue *Save selector* button at the bottom of the interface.

#### Scraping and exporting

Now it's time to do the scraping. In the webscraper.io interface, go to *Sitemap bsc_fan_wiki_link_scraper > Scrape*. The window that pops up has two options: Request interval and Page load delay. Request interval means how long to wait before asking the website's server for a new page, assuming there's more than one page. The thing is, if you hammer a server with requests, you're asking to get throttled: having your requests slowed.... way ... waaayyyyyyyy.... down. It's the price you pay for not having good web scraping manners. 5 seconds (5000 ms) is probably a good place to start, but if you're doing scraping at scale (tens or hundreds of pages), you still might be throttled as a bot (which, let's face it, you kinda are) if your delay is the same every time. (We can do more sophisticated things by writing a scraper in Python that can get around some of those issues, but that's a guide for another DSC book.) In this case, though, where we only have a few pages to scrape, the default is fine. As for *Page load delay*, if you have a slow connection, or are scraping a complex site that takes some time to load, you may want to increase this value. If you want to guesstimate how much it should be, time a few page loads (from the new page appearing on your screen, to everything being loaded) by pulling up pages in your browser.

Click the blue "Start scraping" button. A new browser window will pop open with the page(s) that you're scraping; don't close it, it'll close itself when it's done.

When the window closes itself, it'll take you to a page that says "No data scraped"; hit the blue "Refresh" button and your data will appear. Then go to *Sitemap bsc_fan_wiki_link_scraper >  Export data as CSV*. On that page, click the *Download now!* link, and you'll download a CSV file.

![Downloading a CSV](/site/assets/dscm3_download_csv.png)

If you want to edit your scraper to include multiple pages, go to *Sitemap bsc_fan_wiki_link_scraper > Edit metadata*. There's a + button on the right side of the URL field, and you can use it to put in more than one page (e.g. adding the URLs for [Mysteries](https://babysittersclub.fandom.com/wiki/Category:Mystery_books), [Super Specials](https://babysittersclub.fandom.com/wiki/Category:Super_Special_books), [Super Mysteries](https://babysittersclub.fandom.com/wiki/Category:Super_mysteries), [Portrait Collection](https://babysittersclub.fandom.com/wiki/Category:Portrait_Collection_books), [California Diaries](https://babysittersclub.fandom.com/wiki/Category:California_Diaries_series), [Reader Requests](https://babysittersclub.fandom.com/wiki/Category:Readers%27_Request_books), and [Friends Forever](https://babysittersclub.fandom.com/wiki/Category:Friends_Forever_series)). Then, just re-scrape and re-download.

#### Just the URLs

We could import this CSV into OpenRefine, but honestly, it's faster and easier to pull the CSV into Google Docs or Excel, delete the stray rows (e.g. Category:Jessi books), and copy only the *pagelink-href* column (which has the URLs). At this scale (fewer than 300 rows), it probably makes the most sense to just skim and do this cleanup manually, but if you search for "Category" (which will give you links that just take you to sub-categories, like "Mallory Books"), and "Karen" (which is a giveaway for books in the "Baby-Sitter's Little Sister" book series, about Kristy's super-annoying step-sister Karen), that should help you flag the bigger sets of bad results. There's also random pages that accidentally got mis-tagged (e.g. at least as of when I'm writing this, "How to cosplay as Stacey McGill from the BSC"), so you do actually need to read through the list with your eyeballs, and check on any page titles where you're unsure. You should also de-duplicate links as needed, so that you only have one copy of each link (e.g. "Stacey and the Haunted Masquerade" was tagged with both the regular series and mystery, so it appears twice.) Sorting the URLs alphabetically should help make these visible, and most spreadsheet software can easily replace duplicates automatically. (If you're using Google Sheets, you can just go to *Data > Remove* duplicates to take care of it.)

All together, you should have 229 links to scrape.

#### Scraping ALL THE THINGS

You *could* load those 229 pages into Webscraper.io by hitting the + button on the URL field 228 times, and no doubt you may be tempted, especially if you're delegating this work to a research assistant. But resist the tantalizing purr of the Ghost Cat leading you down the path to rote labor: there's an easier way.

What you need is a web page with all the links you want to scrape (as HTML links, not just plain text). The easiest way to get there, as of March 2020, is to use a site like [pastelink.net](https://pastelink.net/), where you can paste the URLs from the spreadsheet you cleaned up in the last step, and it'll give you a link that you can use for Webscraper.io. The site has been around since at least 2015, though it seems at least moderately sketchy (their "news and updates" page mentions a successful purge of child abuse links in 2018 😬), and it can't handle URLs that have an exclamation mark at the end (as more than a couple BSC books do -- along with their corresponding wiki pages), but it's your easiest option if you're not comfortable making an HTML or Markdown page.

A less-dodgy alternative, if you have a GitHub account and are comfortable with Markdown or HTML, is to create a file in a GitHub repo as a place to put the URLs. This approach makes it possible to make all the URLs work, even if they end in an exclamation mark. To make a [Markdown file that you can put on GitHub (like we've done here)](https://github.com/datasittersclub/dscm3/blob/master/bsc_wiki_links.md), try this: if you copy and paste the list of URLs, one URL per line into a plain-text editor that supports regular expressions (which you can [read up on at The Programming Historian](https://programminghistorian.org/en/lessons/understanding-regular-expressions) -- they're basically a fancy find-and-replace syntax), you can search for `^(.*)$` (which translates to "grab all the characters from the beginning of the line to the end of the line") and replace it with `[$1]($1)` ("put what you grabbed between square brackets, then between parentheses"), though you may need to check your text editor documentation for whether its flavor of regular expressions uses $1 or \1 or some other notation for captured groups. If you get this to work, save the results as a .md file, and push that file to a GitHub repo, you can use the URL for that Markdown file in the next step (just like we've done, [using our wiki links Markdown file](https://github.com/datasittersclub/dscm3/blob/master/bsc_wiki_links.md) in our [book metadata scraper](https://github.com/datasittersclub/dscm3/blob/master/bsc_book_metadata.txt)).

However you put your list of links online, the next step is to create a new sitemap in webscraper.io, and put the URL *of the page with all your links*, not any of the individual links. Then, the first selector in the sitemap that you create should be set to have multiple values, and what you're selecting for is each of the links on the page.

![Selecting all the links](/site/assets/dscm3_linkselector.jpg)

Once you've saved that selector, click on it in your sitemap. This takes you *inside* that selector, as Webscraper.io structures things. The new selectors you add aren't selectors for your page of links, they're selectors for the *pages whose URLs are on that page of links*. For that reason, it's going to be very helpful if the links in a single list go to pages that are pretty homogenous: you want the nested selectors to be applicable to most or all of those pages. Not all the selectors I created here work for every book (e.g. the California Diaries and Portrait books don't really have book numbers), but most of the fields are relevant across the board.

As an important side note here, wikis hosted on fandom.com are *unusually well-structured* and pretty remarkable for their use of semantically-inflected markup (i.e. a lot of the HTML elements include a class -- as we've seen above -- that tells you something about the content that you'll find inside). Compare, even, to Wikipedia: even though you have what looks like structured metadata in the sidebar boxes for most articles, if you inspect the HTML, you'll find a table with the class "infobox", and then a bunch of table rows (<tr>) and cells (<td>). What if you were reading the news and wanted to, say, set up a scraper that would go to the Wikipedia page for a bunch of different historical pandemics and extract the death toll? Good luck!

Probably the best you could do is capture the whole sidebar table, and try to (as likely as not, manually) extract the number you're looking for. Having an HTML class that says what it is (e.g. class="death-toll" on a <tr> element) isn't the only setup that would let you scrape the data easily; if every pandemic page had a 100% consistent set of metadata, which was always provided in the same order (and listed as "N/A" or something if there was no known value), you might be able to reliably use something like `tr:nth-of-type(n+3)` in your scraper if you could count on the death toll always being the third element in that sidebar. But in reality, very few websites use either totally consistent metadata, or semantic classes on their elements. In most cases, for the results to be usable, web scraping is just a prelude to lots and lots of data cleaning.

![Wikipedia's fake metadata structure](/site/assets/dscm3_fake_metadata_structure.png)

But fandom.com wikis make our lives easy! Here's the elements I created for all the data I wanted to capture; all of them are *Text* type and only *wikipagetext* (the body text on the wiki page) has the "multiple" boxes selected, because there's usually multiple paragraphs of text on a wiki page:

| Element name | Selector |
|--------------|-----------------------------------|
| booktitle | h1.page-header__title |
| bookseries | [data-source='series'] div |
| booknumber | [data-source='no. in series'] div |
| bookauthor | [data-source='author'] div |
| bookcoverart | [data-source='illustrator'] div |
| booktagline | [data-source='tagline'] div |
| publication | [data-source='date'] div |
| wikipagetext | .mw-content-ltr > p |

Now, if you want to make your life easier, omit the *wikipagetext* element. What I initially wanted to get out of it was the "Dear Reader" section for the books that have it (e.g. what is the wholesome, relatable message at the end of *[Stacey's Big Crush](https://babysittersclub.fandom.com/wiki/Stacey%27s_Big_Crush)*, where she has a crush on a student teacher?), but there's no HTML class to indicate that section, and it's not like the book synopses are reliably 5 paragraphs long, so that you could count on "Dear Reader" being the 6th. But because this element has multiple values, and each one gets saved as its own row in the output file, it's going to be a pretty gross data-hairball.

Once you've set this up, run the scraper, download the results, and you've got a brand new Ghost Cat data-hairball to clean up in OpenRefine... in addition to all those records from the various national libraries.