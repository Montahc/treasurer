import tkinter as tk
from tkinter import ttk
from record import record_display

MAXWIDTH = 51
WRAP = 400
WIDTH = 50
HEIGHT = 5

class filtered_table(ttk.Treeview):

    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent, show='headings', height=25)
        self.data = "null"
        self.activetags = "null"
        self.mode = "null"
        
        
    
    def roll(self, data, activetags, mode="list"):
        self.data = data
        self.activetags = activetags
        self.mode = mode
        for item in self.get_children():
            self.delete(item)

        current_table = filter_table(data, activetags)
                    
        if mode == "table":
            header = headers(data)#["Name", "ID", "Weight", "Source", "Rarity", "Base Items", "Desc", "GP", "Tags"]
            headerAdded = False
            x=0
            for k, v in current_table.items():
                #Set up header row if it has not yet been set
                if not headerAdded:
                    print("header", header)
                    self.config(column=header)
                    
                    j=0
                    for i in header:
                        # self.column("# " + str(j), anchor="w")
                        self.heading(i, text=i, command=lambda _col=i: 
                                    treeview_sort_column(self, _col, False))
                        j += 1

                    headerAdded = True
                text = list(v.values())
                text = list(map(str, text))
                text.insert(0, str(k))
                #add item name as first column in each item
                self.insert('', 'end', text=str(x), values=text, tags=('ttk'))

                x += 1

            self.bind("<Double-1>", self.OnDoubleClick)

    def OnDoubleClick(self, event):
        item = self.selection()[0]
        print("you clicked on", self.item(item,"values")[0])
        record_display(self, self.item(item,"values")[0], self.data)

            
def reroll(self):
    self.roll(self.data, self.activetags, self.mode)

#headers(dict, keyname) -> list
def headers(dict):
    header = ["Name"]
    for k, v in dict.items():
        for s in v:
            if s not in header: header.append(s)

    return header

def filter_table(d, tags):
    c = {}
    for key, value in d.items():
        for t in value["Tags"]:
            if t in tags:
                if value["Tags"][t] and value["Tags"][t] == tags[t]:
                    c[key] = value
                    continue
    
    return c

def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, text=col, command=lambda _col=col: 
                 treeview_sort_column(tv, _col, not reverse))
