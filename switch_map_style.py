import pdb
import json

with open('basic_style.json') as json_basic:
    basic_data = json.load(json_basic)

with open('dequa2022.json') as json_dequa:
    dequa_data = json.load(json_dequa)

dequa_correct_data= [layer for layer in dequa_data['layers'] if layer['id'] is not "natural_earth_shaded_relief" or layer['id'] is not "natural_earth"]
pdb.set_trace()
basic_data['layers'] = dequa_correct_data

with open('style2022.json', 'w') as json_new:
    json.dump(basic_data, json_new)
