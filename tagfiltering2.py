
import tkinter as tk
import random
from record import RecordDisplay as rd
from style import colors

class tag_filter_pane(tk.Frame):
    def __init__(self, parent, data):
        self.data = data
        #super(tk.Frame, self).__init__()
        self.frame = tk.Frame(parent)
        self.tags = []
        self.activetags = {}
        self.labels = []
        self.taglabels = []
        tag_filter_pane.tagprep(self)
        tag_filter_pane.labelsetup(self)


    def tagprep(self):
        for key, value in self.data.items():
            for k, v in value[0]["Tags"].items():
                if k not in self.tags:
                    self.tags.append(k)

        for t in self.tags:
            self.activetags[t] = False   

    def labelsetup(self):
        def change_color(event):
            if event.widget.cget("bg") == colors["ashley_green"]:
                event.widget.config(bg= colors["no_red"])
                self.activetags[event.widget.cget("text")] = False
            else:
                event.widget.config(bg=colors["ashley_green"])
                self.activetags[event.widget.cget("text")] = True
            
        x, y = 0, 0
        for t in self.tags:
            l = tk.Label(self, text=str(t), bg=colors["no_red"], fg="black")
            l.bind("<Button-1>", lambda event:change_color(event),)
            l.grid(row=y, column=x, sticky="ew")
            if x < 4:
                x+=1
            else:
                y+=1
                x=0
            self.taglabels.append(l)
        def all_true(event): 
            for t in self.taglabels:
                t.config(bg=colors["ashley_green"])
                self.activetags[t.cget("text")] = True

        def all_false(event): 
            for t in self.taglabels:
                t.config(bg=colors["no_red"])
                self.activetags[t.cget("text")] = False
        all_on = tk.Label(self, text="all")
        all_on.bind("<Button-1>", lambda event:all_true(event))
        all_off = tk.Label(self, text="none")
        all_off.bind("<Button-1>", lambda event:all_false(event))
        all_on.grid(row=y, column=x)
        all_off.grid(row=y, column=x+1)










