import dataclasses
import json


class loader:
    def loaddata(filename):
        with open(filename, encoding="Latin-1") as json_file:
            d = json.load(json_file)
            print("Type:", type(d))
            return d

    def writedata(json_string, filename):
        with open(filename, 'w', encoding="Latin-1") as outfile:
            json.dump(json_string, outfile)
