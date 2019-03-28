import tkinter
from tkinter import ttk
from functools import partial
import baboonpdf.gui.screens as screens


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.__add_window_properties()
        self.__add_top_frame()
        self.__add_screens()
        self.show_screen(screens.HOME_SCREEN)

    def __add_window_properties(self):
        self.title("BaboonPDF")
        self.geometry("400x500")  # TODO: set proper size
        self.resizable(0, 0)
        # TODO: add icon
        self.grid_columnconfigure(0, weight=1)

    def __add_top_frame(self):
        top_frame = ttk.Frame(self)

        func = partial(self.show_screen, screens.HOME_SCREEN)
        self.back_button = ttk.Button(self, text="back", command=func, width=7)
        self.back_button.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        ttk.Style().configure("title.TLabel", font=('Sans', '14', 'bold'))

        self.title_label = ttk.Label(self, style='title.TLabel')
        self.title_label.grid(row=0, column=0, columnspan=2, padx=11, pady=11)

        top_frame.grid(row=0, sticky="nsew")

    def __add_screens(self):
        self.screens = dict()
        self.screens[screens.HOME_SCREEN] = screens.HomeScreen(self)
        self.screens[screens.MERGE_SCREEN] = screens.MergeScreen(self)
        self.screens[screens.SPLIT_SCREEN] = screens.SplitScreen(self)
        self.screens[screens.ABOUT_SCREEN] = screens.AboutScreen(self)

        for screen in self.screens.values():
            screen.grid(row=1, sticky="nsew")

    def show_screen(self, name):
        if name == screens.HOME_SCREEN:
            self.back_button.grid_remove()
        else:
            self.back_button.grid()
        self.title_label['text'] = name
        self.screens[name].tkraise()


if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()
