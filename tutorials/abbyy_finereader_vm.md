# Using ABBYY FineReader on Stanford's virtual workstations

If you have book scans and want to create a searchable PDF (but need better OCR than what you can get from the library scanner workstations or Adobe Acrobat), you can use the virtual workstation to access ABBYY FineReader. You'll need to have a reasonably stable internet connection to use this.

If you're still working on scanning books for your research, it's ideal to scan in grayscale at around 300 dpi, if you can configure the scanner to do that. Save each book as a PDF, though the file may be quite large. Once you OCR it, you can export as a smaller PDF for ongoing use.

## Moving your data

Before you get started, you'll need to put your images in a place that you can access from the virtual machine. Your personal Google Drive is a good option. (Don't use your Stanford one if it requires you to use CardinalKey; you can't get that set up on the virtual machine.) Any other cloud storage, like Dropbox, is also fine.

## Connecting to a virtual machine

Go to the [Stanford Virtual Desktop](https://virtualdesktop.stanford.edu/), choose _Windows GPU_, then click the blue _Next_ button. Finally, click the blue _Let's Go_ button. This may take you to a page where once again you have to choose the _Windows GPU_ option. This will launch a new browser tab that can take a couple minutes to load. Once it does, you should see a Windows desktop.

## Downloading your images

Oen a web browser, navigate to Google Drive (or whatever cloud storage you're using), and download your images to the virtual machine (e.g. to the Downloads folder, or anywhere else you'd like). There's warning text on the desktop about how you need to keep your file storage to 1 GB or less, but this is not actually enforced.

Your files are also not generally deleted after you log out of the virtual desktop, but **do not rely on this for storage**. Once you've OCR'd files, be sure to upload them back to your cloud storage before you log out.

## ABBYY FineReader

There's an icon for ABBYY FineReader on the desktop. Double-click it to launch the software. Once the interface opens, go to _File > New OCR project_.

![Screenshot showing how to get to 'new OCR project'](/assets/abbyy-new-ocr-project.jpg)

This will open an interface where you can choose the language(s) of the text you're going to OCR using a drop-down at the top of the screen. Once you've chosen the language, open the Windows file manager (the folder icon in the bottom bar of the virtual desktop) and drag your file(s) into the vertical panel on the left side of the ABBYY FineReader interface. The OCR engine will start running immediately.

![Screenshot showing how to drag files to the panel](/assets/abbyy-drag-files.jpg)

You can OCR multiple PDFs at the same time, as long as you use the right export settings to get one output file per original file (as described below under "Exporting".)

Once it's done (which can take anywhere from a minute or two for a few pages, to 45 minutes or more for 1000+ pages with complex layout), you can see the results in the ABBYY FineReader interface. Characters that it's uncertain about are highlighted in bright turquoise in the text box, and if you click on turquoise text, the image window will zoom in on the area in question. If you want to make sure your text is highly accurate, this is the easiest place to do the correction, before you export the results.

![Screenshot showing how to edit results in FineReader](/assets/abbyy-editing.jpg)

If you can't correct everything in one session, you can save the OCR project to return to later, but you may want to export your intermediate results and save them back to cloud storage -- don't trust the virtual machine for storing the only copy of important files.

### Exporting

Go to _File > Save As_, and there are multiple export formats, each with different uses:

- Plain text (.txt): good for doing computational text analysis / DH work
- Searchable PDF: lets you search and highlight and copy text from a PDF, but otherwise interact with the text like a scanned PDF
- HTML: a text format that retains formatting (e.g. font size, italics, etc.), which can be useful information when you're trying to parse texts into constituent data (e.g. for a bibliography). The HTML export will also generate a folder with all the images from the book, which can be helpful for some projects.

Choose the export format you want. In the window where you choose the filename, there are some important things to check:

**File options** (bottom right): if you have multiple PDFs, set this to "Create a separate file for each source file". It will automatically name the output files based on the name of the input files. If you uploaded a bunch of single-page images from a book rather than a PDF, choose "Create a single file for all pages"

![Screenshot showing how to choose the file options](/assets/abbyy-file-options.jpg)

**Options**: these options vary depending on the export format, but choosing to remove headers and footers is helpful.

![Screenshot showing how to choose additional options](/assets/abbyy-more-options.jpg)

## Moving files to cloud storage

Once you've done all your exporting, you should upload those files back to your cloud storage. You don't need to save the OCR project if you've exported everything that you need.

## Data management

As you work on building your research corpus, reasonable data management practices are going to become more and more important. At a minimum, you should have a folder with all your plain text file versions (ideally, with nothing else in it). It's best if the file names for those plain text files have no spaces, and no accented or non-Latin characters (use an underscore or hyphen instead of a space.) I often use a convention of "authorname_book-title.txt" for my own files. You should also make yourself a spreadsheet with the following columns:

- filename of plain text file
- title
- author surname
- author given name
- year of publication
- (other columns with additional metadata as needed)

## For more information

There's a <a href="https://guides.nyu.edu/abbyy">wonderfully detailed ABBYY FineReader tutorial from NYU Libraries</a> with more information about ABBYY FineReader.
