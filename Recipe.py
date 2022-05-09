import pandas as pd
from Fridge import Fridge

class Recipe:
    def __init__ (self, filename):
        self._name = filename
        self._recipe_list = {}
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(",")
                if line[0] in self._recipe_list:
                    self._recipe_list[line[0]] += line[1].strip()
                else:
                    self._recipe_list[line[0]] = line[1].strip()
                    
    def get_items(self):
        for k, v in self._recipe_list.items():
            print("You need:", v, k+"(s)")
            
    def good_to_make(self, Fridge):
        counter = 0
        for k, v in self._recipe_list.items():
            if k not in Fridge.get_keys():
                counter += 1
            if int(v) != Fridge.get_count_item(k):
                counter += 1
        if counter == 0:
            print("Can make dish!")
        else:
            print("Cannot make it")