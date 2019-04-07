from tkinter import ttk
from baboonpdf.gui.screens.templates import ScreenTemplate


class DocToPDFScreen(ScreenTemplate):

    def __init__(self, parent):
        super().__init__(parent, input_type='doc', multiple_input=False, output_type='file', run_command=self.__convert)

        # TODO: add content
        ttk.Label(self.settings_frame, text="TODO (settings of doc to pdf)").pack()

    def __convert(self):
        # TODO: call function of core
        print("running: ", "DocToPDFScreen")
        print("input: ", self.input)
        print("output: ", self.output)
