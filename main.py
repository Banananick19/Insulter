import tkinter as tk
from tkinter import messagebox
from utils import *
import random

class Window(tk.Frame):

    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self.lines = get_lines()
        self.pack(expand=True, fill=tk.BOTH)
        self.make_widgets()

    def make_widgets(self):
        for key in BUTTONS:
            if hasattr(self, BUTTONS[key]):
                tk.Button(self, text=key, command=eval('self.'+ BUTTONS[key])).pack()

    def on_show_insult(self):
        line = random.choice(self.lines)
        messagebox.showinfo('Оскорбление', line)

def main():
    root = tk.Tk()
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()