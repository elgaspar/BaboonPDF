import tkinter
from tkinter import ttk, filedialog


class OutputSelectWidget(ttk.Frame):

    def __init__(self, parent, output_type):
        if output_type != 'file' and output_type != 'dir':
            raise Exception("Invalid value for argument 'output_type'. Use 'file' or 'dir' instead.")

        super().__init__(parent)
        self.parent = parent
        self.output_type = output_type

        label = ttk.Label(self, text='Output:')
        label.grid(row=0, column=0, sticky='w')

        self.filename = tkinter.StringVar()
        self.output = ttk.Entry(self, textvariable=self.filename, state=tkinter.DISABLED)
        self.output.grid(row=1, column=0, sticky='we', padx=(0, 5))

        self.grid_columnconfigure(0, weight=1)

        self.browse_button = ttk.Button(self, text='Browse', command=self.__browse)
        self.browse_button.grid(row=1, column=1)

    def __browse(self):
        # TODO: run fiiledialog depending on output_type
        path = filedialog.asksaveasfilename(parent=self.parent,
                                            filetypes=[('PDF files', '.pdf')],
                                            defaultextension='.pdf')
        self.filename.set(path)
