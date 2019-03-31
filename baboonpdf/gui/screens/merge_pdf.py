from tkinter import ttk
from baboonpdf.gui.screens.multiple_file_input import MultipleFileInput


class MergePDFScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.filelist_frame = MultipleFileInput(self, 'pdf')
        self.filelist_frame.pack(fill='x')

        # TODO: add content

        # self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="TODO (merge)").pack()
