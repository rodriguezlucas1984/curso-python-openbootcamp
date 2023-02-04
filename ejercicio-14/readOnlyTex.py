from tkinter import Text


class ReadOnlyTex(Text):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(state='disabled')

    def set_Text(self, textStr=""):
        self.config(state='normal')
        self.delete('1.0', 'end')
        self.insert('1.0', textStr)
        self.config(state='disabled')
