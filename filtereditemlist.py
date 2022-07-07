import tkinter as tk
from record import record_display

MAXWIDTH = 51
WRAP = 400
WIDTH = 50
HEIGHT = 5

class filtered_table(tk.Canvas):

    def __init__(self, parent):
        tk.Canvas.__init__(self, parent)
        self.data = "null"
        self.activetags = "null"
        self.mode = "null"
        
        
    
    def roll(self, data, activetags, mode="list"):
        self.data = data
        self.activetags = activetags
        self.mode = mode
        for widget in self.winfo_children():
            widget.destroy()
        current_table = {}
        scrollbar = tk.Scrollbar(self, command=self.yview)
        self.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for key, value in data.items():
            for t in value["Tags"]:
                if t in activetags:
                    if value["Tags"][t] and value["Tags"][t] == activetags[t]:
                        current_table[key] = value
                        continue
        
        if mode == "list":
            x, y = 0, 0
            for k, v in current_table.items():
                l = tk.Label(self, text=k)
                l.bind("<Button-1>", lambda event:record_display(self, event.widget.cget("text"), data))
                l.grid(row=y, column=x, sticky="ew")
                if x < 4:
                    x+=1
                else:
                    y+=1
                    x=0
                    
        elif mode == "table":
            x, y = 0, 0
            rows = []
            header = headers(data, "Name")#["Name", "ID", "Weight", "Source", "Rarity", "Base Items", "Desc", "GP", "Tags"]
            headerAdded = False
            for k, v in current_table.items():
                #Set up header row if it has not yet been set
                if not headerAdded:
                    rows.append(tk.Frame(self, relief="groove"))
                    for i, n in header.items():
                        if i == "Tags":
                            continue
                        l = tk.Label(rows[y], text=i, anchor="nw", relief="raised", width=n)
                        l.grid(row=0, column=x, sticky="ew", pady=2, padx=1)
                        x+=1
                    rows[y].pack()
                    y+=1
                    x=0
                    headerAdded = True

                #add item name as first column in each item
                rows.append(tk.Frame(self, relief="groove"))
                l = tk.Label(rows[y], text=k, width=header["Name"], height=HEIGHT, anchor="nw",relief="groove")
                l.bind("<Button-1>", lambda event:record_display(self, event.widget.cget("text"), data))
                l.grid(row=0, column=x, sticky="nw", pady=2)
                x+=1

                #add remaining elements
                for s in v:
                    text = str(v[s])
                    if text == "": text = "-"
                    if s == "Tags":
                        continue
                    if len(text) > header[s]:
                        l = tk.Label(rows[y], text=text, width=header[s], wraplength=WRAP, height=HEIGHT, anchor="nw", relief="groove")
                        l.grid(row=0, column=x, sticky="nw", pady=2)
                    else:
                        l = tk.Label(rows[y], text=text, width=header[s], anchor="nw",relief="groove")
                        l.grid(row=0, column=x, sticky="nw", pady=2)
                    x+=1
                rows[y].pack()
                y+=1
                x=0
    def reroll(self):
        self.roll(self.data, self.activetags, self.mode)


def headers(dict, keyname):
    header = {}
    header[keyname] = len(keyname)
    for k, v in dict.items():
        if MAXWIDTH > len(k) > header[keyname]: 
            header[keyname] = len(k)
        for s in v:
            if s not in header: header[s] = len(str(v[s]))
            if MAXWIDTH > len(str(v[s])) > header[s]: 
                header[s] = len(str(v[s]))

    return header

