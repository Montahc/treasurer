import dataclasses
import json
import tkinter as tk
from tkinter import *
import random

class loader:
    def loaddata(filename):
        with open(filename, encoding="Latin-1") as json_file:
            d = json.load(json_file)
            print("Type:", type(d))
            return d

colors = {"ashley_green":"#88b04b", "no_red":"#c86d42", "maybe_blue":"#7979ce", "med_pink": "#c85a9b", "teal":"#4ba77f"}


data = loader.loaddata('item_superlist.json')
choice = "Weapon"#input("What tag would you like to list?")
options = []
tags = []
for key, value in data.items():
    for k, v in value[0]["Tags"].items():
        if k not in tags:
            tags.append(k)
    if value[0]["Tags"][choice] == True: 
        options.append(key)
activetags = {}
for t in tags:
    activetags[t] = True



window = tk.Tk(baseName="Report Window")
top_frame = Frame(window)
top_frame.grid(row=0, column=0)
bot_frame = Frame(window)
bot_frame.grid(row=1, column=0)
labels = []
taglabels = []
def all_true(event): 
    print("alltrue")
    for t in taglabels:
        t.config(bg=colors["ashley_green"])
        activetags[t.cget("text")] = True

def all_false(event): 
    print("allfalse")
    for t in taglabels:
        t.config(bg=colors["no_red"])
        activetags[t.cget("text")] = False

all_on = tk.Label(top_frame, text="all")
all_on.bind("<Button-1>", lambda event:all_true(event))
all_off = tk.Label(top_frame, text="none")
all_off.bind("<Button-1>", lambda event:all_false(event))


def change_color(event):
    if event.widget.cget("bg") == colors["ashley_green"]:
        event.widget.config(bg= colors["no_red"])
        activetags[event.widget.cget("text")] = False
    else:
        event.widget.config(bg=colors["ashley_green"])
        activetags[event.widget.cget("text")] = True
    


x = 0
y = 0
for t in tags:
    l = tk.Label(top_frame, text=str(t), bg=colors["ashley_green"], fg="black")
    l.bind("<Button-1>", lambda event:change_color(event),)
    l.grid(row=y, column=x, sticky="ew")
    print(str(x) + " " + str(y))
    if x < 4:
        x+=1
    else:
        y+=1
        x=0
    taglabels.append(l)
all_on.grid(row=y, column=x)
all_off.grid(row=y, column=x+1)



def roll(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    filtered_table = []
    for key, value in data.items():
        for t in value[0]["Tags"]:
            if value[0]["Tags"][t] and value[0]["Tags"][t] == activetags[t]:
                filtered_table.append(key)
                continue
    x, y = 0, 0
    for f in filtered_table:
        l = tk.Label(bot_frame, text=f)
        l.grid(row=y, column=x, sticky="ew")
        print(str(x) + " " + str(y))
        if x < 4:
            x+=1
        else:
            y+=1
            x=0
    print (filtered_table)
    return filtered_table


roll_item = tk.Button(top_frame, text="Roll Item")
roll_item.bind("<Button-1>", lambda event:roll(bot_frame))
roll_item.grid(row=y, column=x+2)
"""for o in options:
    l = tk.Label(text=str(o))
    l.pack()
    labels.append(l)
"""
window.mainloop()