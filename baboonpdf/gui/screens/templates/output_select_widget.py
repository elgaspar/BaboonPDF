import tkinter
from tkinter import ttk, filedialog
import baboonpdf.gui.screens.templates as templates


class OutputSelectWidget(ttk.Frame):

    def __init__(self, parent, output_type):
        if output_type not in templates.VALID_OUTPUT_TYPES:
            msg = "Invalid value for argument 'output_type'. Valid values: %s" % str(templates.VALID_OUTPUT_TYPES)[1:-1]
            raise Exception(msg)

        super().__init__(parent)
        self.parent = parent
        self.output_type = output_type

        label = ttk.Label(self, text='Output:')
        label.grid(row=0, column=0, sticky='w')

        self.selected_path = tkinter.StringVar()
        self.output = ttk.Entry(self, textvariable=self.selected_path, state=tkinter.DISABLED)
        self.output.grid(row=1, column=0, sticky='we', padx=(0, 5))

        self.grid_columnconfigure(0, weight=1)

        self.browse_button = ttk.Button(self, text='Browse', command=self.__browse)
        self.browse_button.grid(row=1, column=1)

    def __browse(self):
        if self.output_type == 'file':
            path = filedialog.asksaveasfilename(parent=self.parent,
                                                filetypes=[('PDF files', '.pdf')],
                                                defaultextension='.pdf')
        elif self.output_type == 'dir':
            path = filedialog.askdirectory(parent=self.parent)
        self.selected_path.set(path)

    @property
    def value(self):
        return self.selected_path.get()
