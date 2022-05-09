import pandas as pd
import re
from Fridge import Fridge
from Recipe import Recipe


def main():

    McCarty = Fridge("McCarty 273")
    Baked_Speghetti = Recipe("BakedSpeg.txt")
    
    
    McCarty.add_item("spaghetti", 16)
    McCarty.add_item("ground chuck", 1)
    McCarty.add_item("onion", 1)
    McCarty.add_item("garlic", 3)
    McCarty.add_item("marinara sauce", 24)
    McCarty.add_item("basil", 2)
    McCarty.add_item("mozzarella", 1)


    Baked_Speghetti.good_to_make(McCarty)








if __name__ == "__main__":
    main()