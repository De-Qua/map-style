# map-style
A repository to work on our json file for the map style with Maputnik

## Maputnik
A tool to graphically change map layouts

## Instructions
To work on these files:
- Download the release for your system [here](https://github.com/maputnik/editor/releases)
- Move the file (unpack it, it should be one file called maputnik) in this folder (it is .gitignored)
- Make it executable if it's not yet (`chmod +x maputnik`)
- Launch Maputnik (`./maputnik`)

To choose the json style file, either pass it as a parameter `./maputnik --file dequa_barca.json` or choose "open" from the GUI when it starts.

Add `--watch true` to change in real time the json file via an editor.

Using default info maputnik exposes itself on the port 8000, but you should be able to change with `--port something_else`.

## Fonts
Install Inter Font (Google Font)

## Files
We will have:
- a file for the pedestrian navigation (dequa_pedestrian.json)
- a file for the water navigation (dequa_water.json)
- a file for the public transportation (dequa_transport.json) (not done yet)
- a base file? (dequa_base.json)

osm_libery.json was the initial file I used to start.
