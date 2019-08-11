from tkinter import ttk
from baboonpdf.gui.screens.template import ScreenTemplate


class ImagesToPDFScreen(ScreenTemplate):

    def __init__(self, parent):
        super().__init__(parent, input_type='image', multiple_input=True, output_type='file', run_command=self.__convert)

    def __convert(self):
        # TODO: call function of core
        print("running: ", "ImagesToPDFScreen")
        print("input: ", self.input)
        print("output: ", self.output)
