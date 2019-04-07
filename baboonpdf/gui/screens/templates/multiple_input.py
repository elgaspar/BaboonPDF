import tkinter
from tkinter import ttk, filedialog
import os
import re
import baboonpdf.gui.screens.templates as templates


class MultipleInput(ttk.Frame):

    def __init__(self, parent, input_type):
        if input_type not in templates.VALID_INPUT_TYPES:
            msg = "Invalid value for argument 'input_type'. Valid values: %s" % str(templates.VALID_INPUT_TYPES)[1:-1]
            raise Exception(msg)

        super().__init__(parent, height=5)
        self.parent = parent
        self.input_type = input_type

        self.__add_tree()
        self.__add_tree_scrollbar()
        self.__add_top_buttons()
        self.__add_bottom_button()

    def __add_tree(self):
        self.tree = ttk.Treeview(self, height=10)

        self.tree['columns'] = ('#', 'filename', 'pages', 'size', 'path')
        self.tree.column('#', width=25, minwidth=25, stretch=tkinter.NO)
        self.tree.column('filename', width=100, minwidth=60, stretch=tkinter.NO)
        if self.input_type == 'pdf':
            self.tree.column('pages', width=50, minwidth=40, stretch=tkinter.NO)
        self.tree.column('size', width=50, minwidth=40, stretch=tkinter.NO)
        self.tree.column('path', width=50, minwidth=40)

        self.tree.heading('#', text='#', anchor=tkinter.W)
        self.tree.heading('filename', text='Filename', anchor=tkinter.W)
        if self.input_type == 'pdf':
            self.tree.heading('pages', text='Pages', anchor=tkinter.W)
        self.tree.heading('size', text='Size', anchor=tkinter.W)
        self.tree.heading('path', text='Path', anchor=tkinter.W)

        self.tree['show'] = 'headings'

        self.tree.grid(row=1, column=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)

    def __add_tree_scrollbar(self):
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=1, sticky='nsew')
        self.tree.configure(yscrollcommand=scrollbar.set)

    def __add_top_buttons(self):
        self.buttons_frame = ttk.Frame(self)

        self.move_up_button = ttk.Button(self.buttons_frame, text="Move Up", command=self.__move_up)
        self.move_up_button.grid(row=0, column=0, padx=(0, 5), pady=5)

        self.move_down_button = ttk.Button(self.buttons_frame, text="Move Down", command=self.__move_down)
        self.move_down_button.grid(row=0, column=1, padx=(0, 5), pady=5)

        self.remove_button = ttk.Button(self.buttons_frame, text="Remove", command=self.__remove_selected)
        self.remove_button.grid(row=0, column=2, padx=(0, 5), pady=5)

        self.remove_all_button = ttk.Button(self.buttons_frame, text="Remove All", command=self.__remove_all)
        self.remove_all_button.grid(row=0, column=3, padx=(0, 5), pady=5)

        self.buttons_frame.grid(row=0, column=0, sticky='w')

    def __add_bottom_button(self):
        self.add_button = ttk.Button(self, text="Add File(s)", command=self.__add)
        self.add_button.grid(row=2, column=0, columnspan=2, sticky='e', pady=5)

    def __move_up(self):
        # TODO
        print('__move_up')
        pass

    def __move_down(self):
        # TODO
        print('__move_down')
        pass

    def __remove_selected(self):
        selected_items = self.tree.selection()
        self.tree.delete(*selected_items)
        self.__recalculate_indices()

    def __recalculate_indices(self):
        index = 1
        for item_id in self.tree.get_children(''):
            values = self.tree.item(item_id)['values']
            values[0] = index
            self.tree.item(item_id, values=values)
            index += 1

    def __remove_all(self):
        items = self.tree.get_children('')
        for index in items:
            self.tree.delete(index)

    def __add(self):
        if self.input_type == 'pdf':
            valid_filetypes = [('PDF files', '.pdf')]
        elif self.input_type == 'image':
            valid_filetypes = [('Image files', ('.jpg', '.bmp', '.png', '.jpeg', '.tif'))]  # TODO: Do all these formats work with my function?
        files = filedialog.askopenfilenames(parent=self.parent,
                                            title="Please select one or more files:",
                                            filetypes=valid_filetypes)
        index = self.__get_row_count() + 1
        for filepath in files:
            filename = os.path.basename(filepath)
            size = self.__generate_size_string(os.path.getsize(filepath))
            if self.input_type == 'pdf':
                pages_count = self.__get_pdf_page_count(filepath)
                values = (index, filename, pages_count, size, filepath)
            elif self.input_type == 'image':
                values = (index, filename, size, filepath)
            self.tree.insert('', 'end', values=values)
            index += 1

    #  TODO: move to utility/helper module
    def __generate_size_string(self, size_in_bytes):
        kb = size_in_bytes/1024
        mb = (size_in_bytes/1024)/1024
        if mb >= 1:
            return "%.2f MB" % mb
        else:
            return "%d KB" % round(kb)

    #  TODO: move to utility/helper module
    #  TODO: do it using a better/faster way.
    #  TODO: IMPORTANT: it doesnt work for some PDF files
    def __get_pdf_page_count(self, filepath):
        rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE | re.DOTALL)
        data = open(filepath, "rb").read()
        return len(rxcountpages.findall(str(data)))

    def __get_row_count(self):
        return len(self.get_filepaths())

    def get_filepaths(self):
        filepaths = list()
        for item_id in self.tree.get_children(''):
            if self.input_type == 'pdf':
                i = 4
            elif self.input_type == 'image':
                i = 3
            filepaths.append(self.tree.item(item_id)['values'][i])
        return filepaths

    @property
    def value(self):
        return self.get_filepaths()
