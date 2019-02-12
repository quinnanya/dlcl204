# Geocoding and Palladio Mapping Tutorial
One common approach to visualizing a text is mapping the locations in it. The method described here only works for places that can be geocoded (i.e. looked up in a database that provides latitude and logitude for named locations; this would not work if your text referred to "the town pub" and there was no way to tie that to a specific pub in a specific town in the real world). There are also issues with geocoding, which provides a single "dot on a map" usually in the center of entities that are geographically much more disperse (e.g. cities, countries, etc), and whose borders change over time.

With those caveats in mind, it can still be valuable to use this approach to get a sense of which (named, real-world) places appear in the text, with what frequency.

## 1. Prepare your data
To start this tutorial, you should have a plain-text file list of places that appear in the text, organized one place per line. This file should be saved as **places.csv**. The place names can be in any language, and at least some historical *place names are supported.

If you want to name it something else, you can do that, but you'll need to edit the *dlcl204-geocoding.py* file to reflect your file name.

## 2. Download the geocoding code
Go to [dlcl204-geocoding.py](dlcl204-geocoding.py). Click on "raw" in the upper right, and then save (Ctrl + S) when you see the page with just the code on the white screen. Save the file in the same location as your **places.csv** file.

## 3. Get a geonames username
Go to [https://geonames.org](https://geonames.org) and [sign up for a user account](http://www.geonames.org/login).

## 4. Add your username to the geocoding code
Open *dlcl204-geocoding.py* in a plain text editor. In line 6, replace *YOUR-USERNAME-HERE* with your username. (Be sure to keep the '' characters around your username.) Save *dlcl204-geocoding.py*. 

## 5. Run the geocoding code
**On a Mac**
Open a Terminal, and navigate to where your *dlcl204-geocoding.py* and *places.csv* files are. For instance, if they're both in the Downloads folder, you can type:

`cd Downloads`

and press Enter.

Once you're in the directory where both those files are located, run the geocoding code by typing:

`python dlcl204-geocoding.py > geocoded.tsv`

and press Enter.

It may take as much as a few minutes before the command line prompt returns, depending on how long your list of places is, and how busy Geonames is when you submit it. When the command line prompt returns, there should be a new file, *geocoded.tsv*, that appears in the same folder as your *places.csv*.


## 6. Create a Palladio project
Go to [Palladio](http://hdlab.stanford.edu/palladio-app/). The first step is to load in your data -- but for Palladio to work, your data has to have headers.

In the first line of the box that appears on the page, type *City*, press the "tab" key, and type *Coordinates*.

Now, open the *geocoded.tsv* file that the geocoding code created in a plain text editor. Copy all the text (you can leave in the places won't have coordinates -- those just won't appear on the map), and paste it into the big text box on Palladio starting with line 2. Click the *Load* button.

Click on "Provide a title to this project" and give it a name.

## 7. Create a map
Click on the "Map" tab at the top of the screen. In the "Map layers" box in the upper right, click the "New layer" button.

* Name: You can name this "Locations"
* Map type: Use the default "Points"
* Places: Click in the "Select or search" box and choose "Coordinates"
* Tooltip label: Click on it and choose "City"
* Size points: Check the box

After setting up these configuration options, click the "Apply" button. All the locations that were geocoded should appear on the map.

## 8. Saving your Palladio project
If you want to save what you've done with your Palladio project to refer to it or edit it later, click the "Download" button in the upper right. This will download a .json file. Next time you go to the Palladio website, you can choose "Load an existing project" (in the left sidebar), and upload that .json file to resume where you left off.