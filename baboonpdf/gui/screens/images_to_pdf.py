from tkinter import ttk
from baboonpdf.gui.screens.templates import ScreenTemplate


class ImagesToPDFScreen(ScreenTemplate):

    def __init__(self, parent):
        super().__init__(parent, input_type='image', multiple_input=True, output_type='file', run_command=self.__convert)

        # TODO: add content
        ttk.Label(self.settings_frame, text="TODO (settings of images to pdf)").pack()

    def __convert(self):
        # TODO: call function of core
        print("running: ", "ImagesToPDFScreen")
        print("input: ", self.input)
        print("output: ", self.output)
