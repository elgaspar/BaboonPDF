from tkinter import ttk


class SplitScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # TODO: add content
        ttk.Label(self, text="TODO (split)").pack()
