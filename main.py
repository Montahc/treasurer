import dataclasses
import json
import tkinter as tk

class loader:
    def loaddata(filename):
        with open(filename, encoding="Latin-1") as json_file:
            d = json.load(json_file)
            print("Type:", type(d))
            return d

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
    

print(tags)


window = tk.Tk(baseName="Report Window")
labels = []
taglabels = []

def change_color(event):
    if event.widget.cget("bg") == "gray51":
        event.widget.config(bg= "black", fg= "white")
    else:
        event.widget.config(bg='gray51', fg= "white")

x = 0
y = 0
for t in tags:
    l = tk.Label(text=str(t))
    l.bind("<Button-1>", lambda event:change_color(event),)
    l.grid(row=y, column=x)
    print(str(x) + " " + str(y))
    if x < 4:
        x+=1
    else:
        y+=1
        x=0
    taglabels.append(l)
"""for o in options:
    l = tk.Label(text=str(o))
    l.pack()
    labels.append(l)
"""
window.mainloop()