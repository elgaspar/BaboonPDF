from tkinter import ttk
from baboonpdf.gui.screens.multiple_file_input import MultipleFileInput
from baboonpdf.gui.screens.output_select_widget import OutputSelectWidget
from baboonpdf.gui.screens.run_widget import RunWidget


class MergePDFScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)

        self.file_input = MultipleFileInput(self, 'pdf')
        self.file_input.grid(row=0, sticky='we')

        self.output = OutputSelectWidget(self, 'file')
        self.output.grid(row=1, sticky='we')

        self.grid_rowconfigure(2, minsize=20)

        self.run = RunWidget(self, self.__merge)
        self.run.grid(row=3, sticky='we')

        self.grid_rowconfigure(4, minsize=5)

    def __merge(self):
        # TODO: call merge function of core
        print("TODO")
        pass
