from tkinter import ttk
from baboonpdf.gui.screens.template import ScreenTemplate


class AboutScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # TODO: add content
        ttk.Label(self, text="TODO (about)").pack()
