import tkinter as tk
from style import colors
from loader import loader


class tag_grid(tk.Frame):
    def __init__(self, parent, data, filter="all", column_max = None, editable=True, chosen=None):
        self.data = data
        tk.Frame.__init__(self, parent)
        self.tags = {}
        self.taglabels = []
        ##print(chosen)
        if chosen:
            self.chosen = chosen
        else:
            self.chosen = False
        self.editable = editable
        self.filter = filter
        
        self.tagprep()
        self.labelsetup("dynamic")



    def set_editable(self, state):
        self.editable = state

    # tagprep creates lists of the tags and their active state
    def tagprep(self):
        if self.chosen:
            for k, v in self.chosen["Tags"].items():
                self.tags[k] = v
        else:
            for key, value in self.data.items():
                for k, v in value["Tags"].items():
                    if k not in self.tags and (self.filter == "all" or k in self.filter):
                        self.tags[k] = False

    def labelsetup(self, column_max=None):
        if column_max == "dynamic":
            column_max = 1920//100
        else:
            column_max -= 1
        def change_color(event):
            if self.editable:
                if event.widget.cget("bg") == colors["ashley_green"]:
                    event.widget.config(bg= colors["no_red"])
                    self.tags[event.widget.cget("text")] = False
                    print("Green>Red")
                elif event.widget.cget("bg") == colors["no_red"]:
                    event.widget.config(bg= colors["neut_gray"])
                    self.tags[event.widget.cget("text")] = None
                    print("Red>White")
                else:
                    event.widget.config(bg=colors["ashley_green"])
                    self.tags[event.widget.cget("text")] = True
                    print("White>Green")
            
        x, y = 0, 0
        for t in list(self.tags):
            l = tk.Label(self, text=str(t), bg=colors["no_red"], fg="black")
            if self.tags[t]:
                l.config(bg=colors["ashley_green"])
            else:
                self.tags[t] = None
                l.config(bg=colors["neut_gray"])
            l.bind("<Button-1>", lambda event:change_color(event),)
            l.grid(row=y, column=x, sticky="ew")
            if x < column_max:
                x+=1
            else:
                y+=1
                x=0
            self.taglabels.append(l)

        def all_true(event): 
            for t in self.taglabels:
                t.config(bg=colors["ashley_green"])
                self.tags[t.cget("text")] = True

        def all_false(event): 
            for t in self.taglabels:
                t.config(bg=colors["no_red"])
                self.tags[t.cget("text")] = False
                ##print("all_false " + t.cget("text") + str(self.tags[t.cget("text")]))
        
        def all_reset(event): 
            for t in self.taglabels:
                t.config(bg=colors["neut_gray"])
                self.tags[t.cget("text")] = None


        all_on = tk.Label(self, text="WL All")
        all_on.bind("<Button-1>", lambda event:all_true(event))
        all_on.grid(row=y, column=x)

        all_off = tk.Label(self, text="BL All")
        all_off.bind("<Button-1>", lambda event:all_false(event))
        all_off.grid(row=y, column=x+1)

        all_none = tk.Label(self, text="Reset All")
        all_none.bind("<Button-1>", lambda event:all_reset(event))
        all_none.grid(row=y, column=x+2)

    def get_whitelist(self):
        return self.tags

