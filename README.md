# map-style
A repository to work on our JSON file for the map style with Maputnik

## What is Maputnik?
A tool to graphically change map layouts

## Instructions
To work on these files:
- Download the release for your system [here](https://github.com/maputnik/editor/releases)
- Move the file (unpack it, it should be one file called maputnik) in this folder (it is .gitignored)
- Make it executable if it's not yet (`chmod +x maputnik`)
- Launch Maputnik (`./maputnik`) - if you already have a file to start with, add it! Read below

Alternatively, you can use [maputnik in your browser](https://maputnik.github.io/editor/), even [pointing already to a 3D view of Venice](https://maputnik.github.io/editor/#16.31/45.437168/12.332744/-10.4/60). In this case you need to use the GUI to open your file and cannot change the JSON file via editor

#### Using a preexisting file:
To choose the JSON style file, either pass it as a parameter `./maputnik --file dequa_barca.json` or choose "open" from the GUI when it starts.

Add `--watch true` to change in real time the JSON file via an editor.

Using default info maputnik exposes itself on the port 8000, but you should be able to change with `--port something_else`.

## Saving
Once you are done changing styles on maputnik, export the JSON file via GUI and download it.

## Prepare for tileserver-gl
Use the `create_new_style_tileserver-gl.py`. It can accept as input the name you want to give to the file (which will be used to set the `id` and `name` keys in the JSON).
Plus you need to modify the python file to use the JSON file you just exported (line 7).
Use the python code, we had problem using a normal editor for some formatting.

It is easier than changing by hand and it avoids adding spaces or formatting in weird ways, which can cause problems.

## Fonts
Install Inter Font (Google Font)

## Files
Files are divided in three folders:
- **attempts** (all the tests we did and we will do)
- **template** (one file which work, which we use as a template for basic information and formatting which should not change)
- **final** (here the final versions should be saved)
