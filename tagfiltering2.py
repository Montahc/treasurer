
from tkinter import *
import random
from record import RecordDisplay as rd
from style import colors

class tag_filter_pane:
    def __init__(self, parent, data):
        self.data = data
        self.frame = Frame(parent)
        self.tags = []
        self.activetags = {}
        self.labels = []
        self.taglabels = []
        self.tagprep(self.data, self.tags, self.activetags)
        self.labelsetup(self.tags, self.activetags, self.frame, self.taglabels)


    def tagprep(self, data, tags, activetags):
        for key, value in data.items():
            for k, v in value[0]["Tags"].items():
                if k not in tags:
                    tags.append(k)

        for t in tags:
            activetags[t] = False   

    def labelsetup(self, tags, activetags, taglabels, frame):
        def change_color(event):
            if event.widget.cget("bg") == colors["ashley_green"]:
                event.widget.config(bg= colors["no_red"])
                activetags[event.widget.cget("text")] = False
            else:
                event.widget.config(bg=colors["ashley_green"])
                activetags[event.widget.cget("text")] = True
            
        x, y = 0, 0
        for t in tags:
            l = Label(frame, text=str(t), bg=colors["no_red"], fg="black")
            l.bind("<Button-1>", lambda event:change_color(event),)
            l.grid(row=y, column=x, sticky="ew")
            if x < 4:
                x+=1
            else:
                y+=1
                x=0
            taglabels.append(l)

            all_on = Label(frame, text="all")
            all_on.bind("<Button-1>", lambda event:all_true(event))
            all_off = Label(frame, text="none")
            all_off.bind("<Button-1>", lambda event:all_false(event))
            all_on.grid(row=y, column=x)
            all_off.grid(row=y, column=x+1)


        def all_true(event): 
            for t in taglabels:
                t.config(bg=colors["ashley_green"])
                activetags[t.cget("text")] = True

        def all_false(event): 
            for t in taglabels:
                t.config(bg=colors["no_red"])
                activetags[t.cget("text")] = False







