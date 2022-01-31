from loader import loader
import asyncio
from tagfilterpane import tag_filter_pane
import tkinter as tk
from record import record_display
from tkinter import messagebox

data = loader.loaddata('item_superlist.json')

window = record_display("Karui Sabre", data)

def on_closing():
    response = messagebox.askyesnocancel("Save and Quit?", "Do you want to save changes before you quit?")
    if response == None:
        pass
    elif response:
        #save
        window.save_record(data, window.get_info_widgets(window))
        loader.writedata(data)
        print("save")
        window.destroy()
    else:
        #nosave
        print("nosave")
        window.destroy()
    
window.protocol("WM_DELETE_WINDOW", on_closing)

"""
window = tk.Tk()
window.title("Treasurer")
top_frame = tag_filter_pane(window, data)
top_frame.grid(row=0, column=0)
"""
window.mainloop()