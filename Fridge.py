class Fridge:
    def __init__(self, name):
        self._name = name
        self._items = {}
        
        
    def get_name(self):
        return self._name
        
        
    def add_item(self, item, count):
        if item in self._items:
            self._items[item] += count
        else:
            self._items[item] = count 
         
            
    def get_items(self):
        if len(self._items) == 0: return "No items"
        for k, v in self._items.items():
            print("There are", v, k+"(s)")
    
            
    def get_count_item(self, item):
        if item not in self._items:
            return "Item not in fridge!"
        return self._items[item]
            
    def get_keys(self):
        return self._items.keys()
    