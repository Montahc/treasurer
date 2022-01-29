from loader import loader
import asyncio
from tagfiltering2 import tag_filter_pane
import tkinter as tk

data = loader.loaddata('item_superlist.json')


window = tk.Tk()
top_frame = tag_filter_pane(window, data)
top_frame.frame.grid(row=0, column=0)
#bot_frame = Frame(window)
#bot_frame.grid(row=1, column=0)



window.mainloop()