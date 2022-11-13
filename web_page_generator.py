

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")

        self.customtext = StringVar()
        
        # instantiaiting label and its properties
        self.lblCustom = Label(self.master,text = "Enter custom text or click the Default HTML page button:")
        self.lblCustom.grid(row=0,column=0,padx=(0,0),pady=(30,0))
        # create entry field
        self.txtCustom = Entry(self.master,text=self.customtext,width=60)
        self.txtCustom.grid(row=1,column=0,padx=(30,0),pady=(30,0))
        # create default HTML Page button
        self.btnDefault = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btnDefault.grid(row=2,column=1,padx=(10,10), pady=(10,10))
        # create custom text button
        self.btnCustom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btnCustom.grid(row=2,column=2,padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        c = self.customtext.get()
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>" + c + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
