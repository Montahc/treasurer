import tkinter as tk
from tkinter import ttk
from record import record_display
import misctools as MT

MAXWIDTH = 51
WRAP = 400
WIDTH = 50
HEIGHT = 5

ITEMS = 40


class filtered_table(ttk.Treeview):

    def __init__(self, parent):
        ttk.Treeview.__init__(self, parent, show='headings', height=0)
        self.data = "null"
        self.activetags = "null"
        self.mode = "null"

    def roll(self, data, whitelist, mode="list"):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ROLL      @@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.data = data
        self.whitelist = whitelist
        print("whitelist" + str(self.whitelist))
        self.mode = mode
        for item in self.get_children():
            self.delete(item)

        current_table = filter_table(data, whitelist)

        ##Display the new table in the selected layout mode
        self.config(height=min(ITEMS, len(current_table)))
        if mode == "table":
            # ["Name", "ID", "Weight", "Source", "Rarity", "Base Items", "Desc", "GP", "Tags"]
            header = headers(current_table)
            headerAdded = False
            x = 0
            for k, v in current_table.items():
                # Set up header row if it has not yet been set
                if not headerAdded:
                    ##print("header", header)
                    self.config(column=header)

                    j = 0
                    for i in header:
                        # self.column("# " + str(j), anchor="w")
                        self.heading(i, text=i, command=lambda _col=i:
                                     treeview_sort_column(self, _col, False))
                        j += 1

                    headerAdded = True
                text = list(v.values())
                text = list(map(str, text))
                text.insert(0, str(k))
                # add item name as first column in each item
                self.insert('', 'end', text=str(x), values=text, tags=('ttk'))

                ##self.bind("<ButtonRelease-1>", lambda event:print(self.focus_get()))
                self.bind("<Double-ButtonRelease-1>", lambda event:record_display(self.parent, 
                                                                    self.item(self.focus())["values"][0],
                                                                    current_table))
                x += 1


def oldroll(self, data, activetags, mode="list"):
        self.data = data
        self.activetags = activetags
        self.mode = mode
        for item in self.get_children():
            self.delete(item)

        current_table = filter_table(data, activetags)
        self.config(height=min(ITEMS, len(current_table)))
        if mode == "table":
            # ["Name", "ID", "Weight", "Source", "Rarity", "Base Items", "Desc", "GP", "Tags"]
            header = headers(data)
            headerAdded = False
            x = 0
            for k, v in current_table.items():
                # Set up header row if it has not yet been set
                if not headerAdded:
                    ##print("header", header)
                    self.config(column=header)

                    j = 0
                    for i in header:
                        # self.column("# " + str(j), anchor="w")
                        self.heading(i, text=i, command=lambda _col=i:
                                     treeview_sort_column(self, _col, False))
                        j += 1

                    headerAdded = True
                text = list(v.values())
                text = list(map(str, text))
                text.insert(0, str(k))
                # add item name as first column in each item
                self.insert('', 'end', text=str(x), values=text, tags=('ttk'))

                x += 1

            self.bind("<Double-1>", self.OnDoubleClick)

def OnDoubleClick(self, event):
        item = self.selection()[0]
        print("you clicked on", self.item(item, "values")[0])
        record_display(self, self.item(item, "values")[0], self.data)


def reroll(self):
    self.roll(self.data, self.activetags, self.mode)

# headers(dict, keyname) -> list


def headers(dict):
    header = ["Name"]
    for k, v in dict.items():
        for s in v:
            if s not in header:
                header.append(s)

    return header


def filter_table(d, wl):
    c = {}
    for key, value in d.items():
        #print("Starting " + key)
        #print(str(value))

        include = None
        for v in value["Tags"]:
            ##print(value["Tags"][v])

            if value["Tags"][v]:
                ##print(key + "has tag" + v + ", continuing.")
                evaluate = wl.get(v, -1)
                if evaluate == -1:
                    break
                elif evaluate:
                    ##print(v + " is whitelisted")
                    if value["Tags"][v]:
                        ##print(key + " has whitelisted Tag, including")
                        include = True
                elif evaluate is False and value["Tags"][v] is True:
                    include = False
                elif evaluate is None:
                    pass
                else:
                    print("filtered_table, this should never happen")

                ##print(include)
                if include:
                    ##print(key + " added to C by WL")
                    c[key] = value
                elif include is None:
                    ##print(key + " added to C by default")
                    c[key] = value
                else:
                    pass
            else:
                #print(key + " does not have tag, breaking")
                continue
    return c

def oldfilter_table(d, tags):
    c = {}
    for key, value in d.items():
        for t in value["Tags"]:
            if t in tags:
                if value["Tags"][t] and value["Tags"][t] == tags[t]:
                    c[key] = value
                    continue

    return c


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, text=col, command=lambda _col=col:
               treeview_sort_column(tv, _col, not reverse))
