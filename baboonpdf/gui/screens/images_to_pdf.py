from tkinter import ttk
from baboonpdf.gui.screens.multiple_file_input import MultipleFileInput


class ImagesToPDFScreen(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.filelist_frame = MultipleFileInput(self, 'images')
        self.filelist_frame.pack(fill='x')

        # TODO: add content
        ttk.Label(self, text="TODO (images to pdf)").pack()
