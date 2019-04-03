import tkinter
from tkinter import ttk, filedialog


class RunWidget(ttk.Frame):

    def __init__(self, parent, command):
        super().__init__(parent)
        self.parent = parent
        self.command = command

        self.run_button = ttk.Button(self, text='Run', command=self.run)
        self.run_button.grid(row=0, column=0)

        self.progress_bar = ttk.Progressbar(self)
        self.progress_bar.grid(row=0, column=1, sticky='we', padx=(5, 0))

        self.grid_columnconfigure(1, weight=1)

    def run(self):
        self.progress_bar.configure(mode='indeterminate')
        self.progress_bar.start(20)
        self.command()

        # TODO: disable all
        # TODO: enable all after finished

        # self.progress_bar.configure(mode='determinate')
