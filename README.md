# map-style
A repository to work on our JSON file for the map style with Maputnik

## [Maputnik](https://maputnik.github.io/)
A tool to graphically change map layouts and see changes in real time.

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
Use the `create_new_style_tileserver-gl.py`
```
usage: create_new_style_tileserver-gl.py [-h] [-s STYLE] [-n NAME] [-id ID] [-o OUTPUT] [-p PREFIX] [style] [name]

positional arguments:
  style                 The path of the Maputnik style
  name                  The name of the new style

optional arguments:
  -h, --help            show this help message and exit
  -s STYLE, --style STYLE
                        The path of the Maputnik style
  -n NAME, --name NAME  The name of the new style
  -id ID, --id ID       The id of the new style (default: the given name)
  -o OUTPUT, --output OUTPUT
                        The output folder of the new style (default: attempts)
  -p PREFIX, --prefix PREFIX
                        The prefix of the new style (default: style_)
```
It can accept as positional arguments the style file and the new name of the style.
These arguments can also be passed as optional arguments with the key/values pairs, if they are not given the program will ask for them.
Other optional arguments are the id, which default is the given name (already cleaned by spaces and weird characters), the output folder and the prefix of the new file.
The new generated file is saved in the output folder as {PREFIX}{ID}.json

## Fonts
Install Inter Font (Google Font) by [downloading from their web page](https://fonts.google.com/specimen/Inter) or via command line if you are on Linux with the command
```
sudo apt-get install fonts-inter
```
[it may need `sudo apt update` before](https://www.devmanuals.net/install/ubuntu/ubuntu-20-04-focal-fossa/installing-fonts-inter-on-ubuntu20-04.html).
## Files
Files are divided in three folders:
- **attempts** (all the tests we did and we will do)
- **template** (one file which work, which we use as a template for basic information and formatting which should not change)
- **final** (here the final versions should be saved)
