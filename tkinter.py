

import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='darkgray')

        self.varfName = StringVar()
        self.varlName = StringVar()
        
        #calling
        self.txtfName = Entry(self.master, text = self.varfName, font = ("Helvetica", 16), fg = 'black', bg = 'lightblue')
        self.txtfName.pack()

        self.txtlName = Entry(self.master, text = self.varlName, font = ("Helvetica", 16), fg = 'black', bg = 'lightblue')
        self.txtlName.pack()        








if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    # keeping main loop active until user kills it
    root.mainloop()
