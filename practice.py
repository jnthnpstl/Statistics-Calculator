import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Statistics Calculator")
        self.geometry("750x500")
        self.resizable(False, False)

        menu = CalculatorView(self)
        menu.add_page(text="Descriptive", page=Descriptive)
        menu.add_page(text="Probability", page=Probability)
        menu.show_frame(Descriptive.__name__)
        menu.pack(expand=True, fill=tk.BOTH)

        self.mainloop()


class CalculatorView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.create_frame_treeview().grid(row=0, column=0, sticky="esn")
        self.create_frame_page().grid(row=0, column=1)
        self.frames = {}

    def create_frame_treeview(self) -> ttk.Frame:
        self.frame_treeview = ttk.Frame(self)
        self.treeview_menu = MenuTreeView(self.frame_treeview)
        self.treeview_menu.bind("<<TreeviewSelect>>", self.on_treeview_selection_changed)
        self.treeview_menu.pack(fill=tk.BOTH, expand=True)
        return self.frame_treeview


    def on_treeview_selection_changed(self, event):
        selected_item = self.treeview_menu.focus()
        page_name = self.treeview_menu.item(selected_item)['text']
        self.show_frame(page_name=page_name)

    
    def create_frame_page(self) -> ttk.Frame:
        self.frame_page = ttk.Frame(self)
        return self.frame_page


    def add_page(self, text, page):
        self.treeview_menu.add_menu(section_text=text)

        
        # Make frames stack on each other
        page_name = page.__name__
        page_frame = page(self.frame_page)
        self.frames[page_name] = page_frame
        page_frame.grid(row=0, column=0, stick="nsew")
    
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    


class MenuTreeView(ttk.Treeview):
    def __init__(self, master):
        super().__init__(master=master)
        self.heading("#0", text="Menu")
    
    def add_menu(self, section_text:str):
        self.insert(parent="",index=tk.END, text=section_text)



class Descriptive(ttk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)
    
    def create_frame_content(self) ->ttk.Frame:
        self.frame_content = ttk.Frame(self)
        lbl_content = ttk.Label(self.frame_content, text="This is Desciptive Statistic Page")
        lbl_content.pack()
        return self.frame_content



class Probability(ttk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.create_frame_content().pack(fill=tk.BOTH, expand=True)
    
    def create_frame_content(self) ->ttk.Frame:
        self.frame_content = ttk.Frame(self)
        lbl_content = ttk.Label(self.frame_content, text="This is Probability Statistic Page")
        lbl_content.pack()
        return self.frame_content


print('baka earnest and jonathan yan')

if __name__ == "__main__":
    App()