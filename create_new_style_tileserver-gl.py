import pdb
import json
import os
import sys

## This is the file you get from maputnik
MAPUNTIK_STYLE = 'final/base_piedi_battello.json'
if not os.path.exists(MAPUNTIK_STYLE):
    print(
        f"Which file should we use? Could not find '{MAPUNTIK_STYLE}' - please change name (line 7)")
else:

    ### CHANGE THIS
    NAME = 'mappa_luca_08Feb'
    if len(sys.argv) > 1:
        NAME = sys.argv[1]

    with open('template/style.json') as json_basic:
        basic_data = json.load(json_basic)

    with open(MAPUNTIK_STYLE) as json_dequa:
        dequa_data = json.load(json_dequa)

    dequa_correct_data = [layer for layer in dequa_data['layers'] if layer['id']
                          is not "natural_earth_shaded_relief" or layer['id'] is not "natural_earth"]
    basic_data['layers'] = dequa_correct_data
    basic_data['name'] = NAME
    basic_data['id'] = NAME
    basic_data['glyphs'] = "https://tiles.dequa.it/fonts/{fontstack}/{range}.pbf"
    # Does it remain the same?
    # In the server, the files are in the sprites folder (not inside the styles/dequa_2022 folder)
    # but it seems to work
    basic_data['sprite'] = "https://tiles.dequa.it/styles/dequa_2022/sprite"
    # the json for the tiles should also not change, afaiu
    basic_data['sources']['openmaptiles']['url'] = "https://tiles.dequa.it/data/dequa_tiles.json"

    with open(f"attempts/style_{NAME}.json", 'w') as json_new:
        json.dump(basic_data, json_new, separators=(",", ":"))

    print(
        f"WARNING: output saved in attempts/style_{NAME}.json, if final version, move it to final")
