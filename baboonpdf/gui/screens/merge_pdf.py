from tkinter import ttk
from baboonpdf.gui.screens.multiple_file_input import MultipleFileInput
from baboonpdf.gui.screens.output_select_widget import OutputSelectWidget


class MergePDFScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.file_input = MultipleFileInput(self, 'pdf')
        self.file_input.pack(fill='x')

        self.output = OutputSelectWidget(self, 'file')
        self.output.pack(fill='x')

        # TODO: add content

        # self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="TODO (merge)").pack()
