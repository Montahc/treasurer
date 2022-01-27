import dataclasses
import json


class loader:
    def loaddata(filename):
        with open(filename, encoding="Latin-1") as json_file:
            d = json.load(json_file)
            print("Type:", type(d))
            return d


data = loader.loaddata('item_superlist.json')