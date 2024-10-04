
import tkinter as tk
from tkinter import ttk
from style import colors
from filtereditemlist import filtered_table
from tag_grid import tag_grid
from modules.tagdata import tag_categories

class tag_filter_pane(tk.Frame):
    def __init__(self, parent, data):
        self.data = data
        tk.Frame.__init__(self, parent, bg='black')
        tabControl = ttk.Notebook(self)
        tg = tag_grid(tabControl, data, "all", column_max="dynamic")
        tabControl.add(tg, text="all")

        for category in tag_categories:
            tg = tag_grid(tabControl, data, tag_categories[category], column_max="dynamic", )
            tabControl.add(tg, text = category)
        
        self.pack(side="left")
        tabControl.pack(side="top")
        roll_item = tk.Button(self, text="Roll Items")
        roll_item.pack(fill="x", side="top", pady=10, padx=10)

        item_table = filtered_table(self)
        item_table.pack(side="bottom")

        roll_item.bind("<Button-1>", lambda event:item_table.roll(self.data, tabControl.nametowidget(tabControl.select()).get_whitelist(), mode="table"))













