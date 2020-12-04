import tkinter as tk

   
class NameChangeInfo():
    def __init__(self):
        self.name = ""
        self.type = ""
    def setName(self, name):
        if (name.isalpha):
            self.name = name
            return True
        else: 
            return False
    def setType(self, type):
        self.type = type

class LegalChangeInfo():
    def __init__(self):
        self.name=""
        self.email=""
        self.password=""
    def setEmail(self, email):
        self.email = email
    def setPassword(self, password):
        self.password = password

class PrefChangInfo():
    def __init(self):
        self.name=""
        self.cas_uname = ""
        self.cas_pword = ""
        self.submitty_uname=""
        self.submitty_pword=""
        self.webex_uname=""
        self.webex_pword=""
    
    def setName(self, name):
        self.name = name
    
    def setCas(self, uname, pword):
        self.cas_uname = uname
        self.cas_pword = pword
    
    def setSubmitty(self, uname, pword):
        self.submitty_uname = uname
        self.submitty_pword = pword

    def setWebex(self, uname, pword):
        self.webex_uname = uname
        self.webex_uname = pword
    
    def getName(self):
        return self.name
    
    def getCas(self):
        return (self.cas_uname, self.cas_pword)
    
    def getSubmitty(self):
        return (self.submitty_uname, self.submitty_pword)
    
    def getWebex(self):
        return (self.webex_uname, self.webex_pword)


class nameChanger(tk.Tk):
    
    def __init__(self, model, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.model = model
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LegalFrame, PrefFrame, DiplomaFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("StartPage")

    def showFrame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.name_inputted = False
        self.type_inputted = False
        
        self.new_name = tk.StringVar()
        self.name_entry = tk.Entry(self, textvariable = self.new_name)
        self.name_label = tk.Label(self, text="Please enter your name")
        
        self.new_name.trace_add("write", lambda x, y, z: self.setName())
        # self.name_entry.bind('<Return>', lambda _: self.setName())

        self.name_label.pack(side="top")
        self.name_entry.pack(side="top")
        self.label = tk.Label(self, text="Please choose the type of name change")
        self.label.pack(side="top", fill="x")

        self.type_radio = tk.StringVar()

        self.radio_pref = tk.Radiobutton(self, text="Preferred", variable=self.type_radio, value='PrefFrame', command= lambda: self.checkInfo())
        self.radio_pref.pack(side = "left", fill="x", pady=0)
        self.radio_legal = tk.Radiobutton(self, text="Legal", variable=self.type_radio, value='LegalFrame', command= lambda: self.checkInfo())
        self.radio_legal.pack(side = "left", fill="x", pady=0)
        self.radio_dip = tk.Radiobutton(self, text="Diploma Request", variable=self.type_radio, value='DiplomaFrame', command= lambda: self.checkInfo())
        self.radio_dip.pack(side = "left", fill="x", pady=0)

        self.next_button = tk.Button(self, text="Next >", state= "disabled", command= lambda: controller.showFrame(self.type_radio.get()))
        self.next_button.pack(side="bottom",pady=10)

        #this will just set name = to entry.get(), if name is not valid, will set name_inputted to false, otherwise true
    def setName(self):
        if (self.name_entry.get()).isalpha():
            self.name_inputted = True
            self.new_name = self.name_entry
        else: 
            self.name_inputted = False
        
        if (self.name_inputted and self.type_inputted):
            self.next_button["state"] = "normal"
        else:
            self.next_button["state"] = "disabled"

    def checkInfo(self):
        self.type_inputted = True
        # print(self.new_name.get())
        # print(self.name_inputted)
        if (self.name_inputted and self.type_inputted):
            self.next_button["state"] = "normal"
        else:
            self.next_button["state"] = "disabled" 


    
class LegalFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Legal Name Change")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.showFrame("StartPage"))
        button.pack()


class PrefFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Preferred Name Change")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.showFrame("StartPage"))
        button.pack()

class DiplomaFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Diploma Info")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.showFrame("StartPage"))
        button.pack()

if __name__ == "__main__":
    model = NameChangeInfo
    app = nameChanger(model)
    app.mainloop()