from tkinter import ttk
from functools import partial
import baboonpdf.gui.screens as screens


class HomeScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid_columnconfigure(0, weight=1)
        ttk.Style().configure("home_screen_style.TButton", width=14)

        self.__add_button(0, screens.MERGE_SCREEN)
        self.__add_button(1, screens.SPLIT_SCREEN)
        self.__add_button(2, screens.REMOVE_PAGES_SCREEN)
        self.grid_rowconfigure(3, minsize=20)
        self.__add_button(4, screens.DOC_TO_PDF_SCREEN)
        self.__add_button(5, screens.IMAGES_TO_PDF_SCREEN)
        self.grid_rowconfigure(6, minsize=20)
        self.__add_button(7, screens.ABOUT_SCREEN)

    def __add_button(self, row_number, screen):
        func = partial(self.parent.show_screen, screen)
        button = ttk.Button(self, text=screen, command=func, style="home_screen_style.TButton")
        button.grid(row=row_number)
