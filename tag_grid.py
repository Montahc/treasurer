import tkinter as tk
from style import colors
from loader import loader


class tag_grid(tk.Frame):
    def __init__(self, parent, data, column_max = None, editable=True, chosen=None):
        self.data = data
        tk.Frame.__init__(self, parent)
        self.tags = {}
        #self.labels = []
        self.taglabels = []
        print(chosen)
        if chosen:
            self.chosen = chosen
        else:
            self.chosen = False
        self.editable = editable
        
        self.tagprep()
        self.labelsetup(column_max)



    def set_editable(self, state):
        self.editable = state

    # tagprep creates lists of the tags and their active state
    def tagprep(self):
        if self.chosen:
            for k, v in self.chosen["Tags"].items():
                self.tags[k] = v
        else:
            for key, value in self.data.items():
                for k, v in value[0]["Tags"].items():
                    if k not in self.tags:
                        self.tags[k] = False

    def labelsetup(self, column_max=None):
        if column_max is None:
            column_max = 4
        else:
            column_max -= 1
        def change_color(event):
            if self.editable:
                if event.widget.cget("bg") == colors["ashley_green"]:
                    event.widget.config(bg= colors["no_red"])
                    self.tags[event.widget.cget("text")] = False
                else:
                    event.widget.config(bg=colors["ashley_green"])
                    self.tags[event.widget.cget("text")] = True
            
        x, y = 0, 0
        for t in list(self.tags):
            l = tk.Label(self, text=str(t), bg=colors["no_red"], fg="black")
            if self.tags[t]:
                l.config(bg=colors["ashley_green"])
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


        all_on = tk.Label(self, text="all")
        all_on.bind("<Button-1>", lambda event:all_true(event))
        all_on.grid(row=y, column=x)

        all_off = tk.Label(self, text="none")
        all_off.bind("<Button-1>", lambda event:all_false(event))
        all_off.grid(row=y, column=x+1)

    def get_tags(self):
        return self.tags
