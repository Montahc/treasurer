from loader import loader
import asyncio
from tagfilterpane import tag_filter_pane
import tkinter as tk

data = loader.loaddata('item_superlist.json')


window = tk.Tk()
top_frame = tag_filter_pane(window, data)
top_frame.grid(row=0, column=0)




window.mainloop()