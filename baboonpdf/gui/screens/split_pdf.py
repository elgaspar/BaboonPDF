from tkinter import ttk
from baboonpdf.gui.screens.templates import ScreenTemplate


class SplitPDFScreen(ScreenTemplate):

    def __init__(self, parent):
        super().__init__(parent, input_type='pdf', multiple_input=False, output_type='dir', run_command=self.__convert)

        # TODO: add content
        ttk.Label(self.settings_frame, text="TODO (settings of split)").pack()

    def __convert(self):
        # TODO: call function of core
        print("running: ", "SplitPDFScreen")
        print("input: ", self.input)
        print("output: ", self.output)
