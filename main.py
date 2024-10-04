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
def d(event):
    print(event)
    #print(event.width,event.height)
    for c in window.winfo_children():
        c.pack()

window.bind('<Configure>',d)
window.geometry("1280x720")
window.maxsize(1920,1017)
tag_filter_pane(window, data)


def on_closing():
    response = messagebox.askyesnocancel("Save and Quit?", "Do you want to save changes before you quit?")
    if response is None:
          pass
    elif response:
         # save
         print("saved on exit")
         loader.writedata(data, filename)
         window.destroy()
         exit()
    else:
         # nosave
         print("no save on exit")
         window.destroy()
         exit()


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
