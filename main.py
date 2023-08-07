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


    def _create_widget(self):
        topframe = tk.Frame(self)
        topframe.grid(row=0, column=0, pady=10)

        self.col_select = tk.StringVar()
        color_list = ttk.Combobox(topframe, textvariable=self.col_select, values=["Black", "Green", "Yellow", "Red", "Blue"],
                                  state="readonly", width=10)
        color_list.current(0)
        self.option_add("*TCombobox*Listbox.selectBackground","skyblue")
        color_list.bind("<<CombovoxSelected>>", self._change_color)
        color_list.grid(row=0, column=0, padx=5)

        self.t_select = tk.StringVar()
        t_list = ttk.Combobox(topframe, textvariable=self.t_select,
                              values=[1, 2, 3, 4, 5, 6, 7], state="readonly", width=3)
        t_list.current(0)
        t_list.bind("<<ComboboxSelected>>", self._change_thickness)
        t_list.grid(row=0, column=1, padx=5)




free_hand_drawing().mainloop()