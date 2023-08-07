import tkinter as tk
import tkinter.ttk as ttk

class free_hand_drawing(tk.Tk):
    def __int__(self):
        super().__init__()
        self.title("Free Hand Drawing Tool")
        self._xold = None
        self._yold = None
        self.canvas = None
        self.color = "Black"
        self.thickness = 1
        self.tag = ["tag", "0"]
        self._create_widget()






free_hand_drawing().mainloop()