from tkinter import ttk
from baboonpdf.gui.screens.templates import ScreenTemplate


class RemovePagesScreen(ScreenTemplate):

    def __init__(self, parent):
        super().__init__(parent, input_type='pdf', multiple_input=False, output_type='file', run_command=self.__convert)

        # TODO: add content
        ttk.Label(self.settings_frame, text="TODO (settings of remove pages)").pack()

    def __convert(self):
        # TODO: call function of core
        print("running: ", "RemovePagesScreen")
        print("input: ", self.input)
        print("output: ", self.output)
