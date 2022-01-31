from tabnanny import filename_only
from loader import loader
import asyncio
import random
from tagfilterpane import tag_filter_pane
import tkinter as tk
from record import record_display
from tkinter import messagebox

filename = 'item_superlist.json'

data = loader.loaddata(filename)

"""""
choice = random.choice(list(data))
print(choice)
window = record_display(choice, data)


def on_closing():
    response = messagebox.askyesnocancel("Save and Quit?", "Do you want to save changes before you quit?")
    if response is None:
        pass
    elif response:
        # save
        print("save")
        record_display.save_record(data, window.get_info_widgets())
        loader.writedata(data, filename)
        window.destroy()
    else:
        # nosave
        print("nosave")
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)
"""

window = tk.Tk()
window.title("Treasurer")
top_frame = tag_filter_pane(window, data)
top_frame.grid(row=0, column=0)


def on_closing():
    response = messagebox.askyesnocancel("Save and Quit?", "Do you want to save changes before you quit?")
    if response is None:
        pass
    elif response:
        # save
        print("save")
        loader.writedata(data, filename)
        window.destroy()
    else:
        # nosave
        print("nosave")
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
