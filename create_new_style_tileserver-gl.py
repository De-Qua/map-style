import pdb
import json
import os
import sys
import re
import argparse


PATHS = {
    "glyphs": "{fontstack}/{range}.pbf",
    "sprite": "sprite",
    "source": "mbtiles://{dequa_tiles}"
}

BASE_TEMPLATE = 'template/style.json'

OUTPUT = "attempts"
PREFIX = "style_"


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '_', s)
    return s.lower()


def main():
    # This is the file you get from maputnik
    MAPUTNIK_STYLE = None
    # CHANGE THIS
    NAME = None

    parser = argparse.ArgumentParser()
    parser.add_argument("style", nargs="?", help="The path of the Maputnik style")
    parser.add_argument("name", nargs="?", help="The name of the new style")
    parser.add_argument("-s", "--style", help="The path of the Maputnik style")
    parser.add_argument("-n", "--name", help="The name of the new style")
    parser.add_argument("-id", "--id", help="The id of the new style (default: the given name)")
    parser.add_argument("-o", "--output", help=f"The output folder of the new style (default: {OUTPUT})", default=OUTPUT)
    parser.add_argument("-p", "--prefix", help=f"The prefix of the new style (default: {PREFIX})", default=PREFIX)

    args = parser.parse_args()

    # check style
    if args.style and os.path.exists(args.style):
        MAPUTNIK_STYLE = args.style
    else:
        while MAPUTNIK_STYLE is None:
            new_style = input("Write the path of the style: ")
            try:
                if os.path.exists(new_style):
                    MAPUTNIK_STYLE = new_style
                else:
                    raise ValueError()
            except Exception:
                print(f"The path '{new_style}' does not exist... Please retry!")
                MAPUTNIK_STYLE = None
        print(f"Path correctly set! I will use the file '{MAPUTNIK_STYLE}'")

    # check name
    if args.name and urlify(args.name):
        NAME = args.name
    else:
        while NAME is None:
            new_name = input("Write the new name: ")
            try:
                if new_name and urlify(new_name):
                    NAME = new_name
                else:
                    raise ValueError()
            except Exception:
                print(f"The name '{new_name}' is bad formatted... Please retry!")
        print(f"Name correctly set! I will use the name '{NAME}'")

    # check id
    if args.id and urlify(args.id):
        ID = urlify(args.id)
    else:
        ID = urlify(NAME)

    # output
    if args.output and os.path.exists(args.output):
        output_folder = args.output
    else:
        output_folder = OUTPUT
        print(f"The given output was not valid. The output folder has been changed to {output_folder}")

    # prefix
    if args.prefix and urlify(args.prefix):
        file_prefix = args.prefix
    else:
        file_prefix = PREFIX
        print(f"The given prefix was not valid. The prefix has been changed to {file_prefix}")

    # let's start
    with open(BASE_TEMPLATE) as json_basic:
        basic_data = json.load(json_basic)

    with open(MAPUTNIK_STYLE) as json_dequa:
        dequa_data = json.load(json_dequa)

    dequa_correct_data = [layer for layer in dequa_data['layers'] if layer['id']
                          != "natural_earth_shaded_relief" or layer['id'] != "natural_earth"]
    basic_data['layers'] = dequa_correct_data
    basic_data['name'] = NAME
    basic_data['id'] = ID
    basic_data['glyphs'] = PATHS["glyphs"]
    # Does it remain the same?
    # In the server, the files are in the sprites folder (not inside the styles/dequa_2022 folder)
    # but it seems to work
    basic_data['sprite'] = PATHS["sprite"]
    # the json for the tiles should also not change, afaiu
    basic_data['sources']['openmaptiles']['url'] = PATHS["source"]

    output_file = os.path.join(output_folder, f"{file_prefix}{ID}.json")

    with open(output_file, 'w') as json_new:
        json.dump(basic_data, json_new, separators=(",", ":"))

    print(
        f"WARNING: output saved in {output_file}, if final version, move it to final")


if __name__ == '__main__':
    main()
