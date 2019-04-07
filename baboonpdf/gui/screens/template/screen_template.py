from tkinter import ttk
from baboonpdf.gui.screens.template.multiple_input import MultipleInput
from baboonpdf.gui.screens.template.single_input import SingleInput
from baboonpdf.gui.screens.template.output_select_widget import OutputSelectWidget
from baboonpdf.gui.screens.template.run_widget import RunWidget


class ScreenTemplate(ttk.Frame):

    def __init__(self, parent, input_type, multiple_input, output_type, run_command):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=1)

        self.__add_input_widget(input_type, multiple_input)
        self.__add_output_widget(output_type)
        self.__add_settings_empty_frame()
        self.__add_run_widget(run_command)

    def __add_input_widget(self, input_type, multiple_input):
        if multiple_input:
            self.__input = MultipleInput(self, input_type)
        else:
            self.__input = SingleInput(self, input_type)

        self.__input.grid(row=0, sticky='we')

    def __add_settings_empty_frame(self):
        self.settings_frame = ttk.Frame(self)
        self.settings_frame.grid(row=1, sticky='we')

    def __add_output_widget(self, output_type):
        self.__output = OutputSelectWidget(self, output_type)
        self.__output.grid(row=2, sticky='we')

    def __add_run_widget(self, run_command):
        self.grid_rowconfigure(3, minsize=20)

        self.__run = RunWidget(self, run_command)
        self.__run.grid(row=4, sticky='we')

        self.grid_rowconfigure(5, minsize=5)

    @property
    def input(self):
        return self.__input.value

    @property
    def output(self):
        return self.__output.value
