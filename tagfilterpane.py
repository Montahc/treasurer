
import tkinter as tk
import random
from style import colors
from filtereditemlist import filtered_table
from tag_grid import tag_grid
from tkinter import messagebox
from loader import loader



class tag_filter_pane(tk.Frame):
    def __init__(self, parent, data):
        self.data = data
        tk.Frame.__init__(self, parent)
        #self.frame = tk.Frame(parent)
        tg = tag_grid(self, data, column_max=10)
        coords = tg.grid_size()
        tg.grid(row = 0, sticky="n")

        item_table = filtered_table(self)
        item_table.grid(row = coords[1], sticky="s")

        coords = tg.grid_size()
        roll_item = tk.Button(tg, text="Roll Item")
        roll_item.bind("<Button-1>", lambda event:item_table.roll(self.data, tg.get_tags()))
        roll_item.grid(row=coords[1]-1, column=coords[0]-1)
        
        print(tg.get_tags())













