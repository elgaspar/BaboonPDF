import tkinter
from tkinter import ttk, filedialog
import os
import re
import baboonpdf.gui.screens.templates as templates


class SingleInput(ttk.Frame):

    def __init__(self, parent, input_type):
        if input_type not in templates.VALID_INPUT_TYPES:
            msg = "Invalid value for argument 'input_type'. Valid values: %s" % str(templates.VALID_INPUT_TYPES)[1:-1]
            raise Exception(msg)

        super().__init__(parent)
        self.parent = parent
        self.input_type = input_type

        ttk.Label(self, text='TODO (SingleInput)').pack()  # TODO

    @property
    def value(self):
        return 'TODO'  # TODO
