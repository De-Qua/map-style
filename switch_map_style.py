import pdb
import json

print("*" * 50)
print("WARNING: old version for openmaptiles - for tileserver use create_new_style_tileserver-gl.py")
print("*" * 50)

with open('template/style.json') as json_basic:
    basic_data = json.load(json_basic)

with open('dequa2022.json') as json_dequa:
    dequa_data = json.load(json_dequa)

dequa_correct_data = [layer for layer in dequa_data['layers'] if layer['id']
                      is not "natural_earth_shaded_relief" or layer['id'] is not "natural_earth"]
basic_data['layers'] = dequa_correct_data
### CHANGE THESE
NAME = 'mappa_dequa'
basic_data['name'] = NAME
basic_data['glyphs'] = "https://tiles.dequa.it/api/fonts/{fontstack}/{range}.pbf"
basic_data['sprite'] = f"https://tiles.dequa.it/api/maps/{NAME}/sprite"

with open(f"style_{NAME}.json", 'w') as json_new:
    json.dump(basic_data, json_new)
