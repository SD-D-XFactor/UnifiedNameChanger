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

    def getName(self):
        return self.name

class LegalChangeInfo():
    def __init__(self):
        self.name=""
        self.email=""
        self.password=""
    def setName(self, name):
        self.name = name
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
        self.legal_model = LegalChangeInfo()
        #add more models here

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(10, weight=3)
        container.grid_columnconfigure(10, weight=3)

        self.frames = {}
        for F in (StartPage, LegalFrame, PrefFrame, DiplomaFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("StartPage", "")

    def showFrame(self, page_name, model):
        '''Show a frame for the given page name'''
        self.model = model
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

        self.next_button = tk.Button(self, text="Next >", state= "disabled", command= lambda: controller.showFrame(self.type_radio.get(), controller.model))
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

        self.controller.legal_model.setName(self.controller.model.getName())

        label = tk.Label(self, text="Legal Name Change")
        label_direction = tk.Label(self, text="Please Enter Your Email and Password")

        self.email = tk.StringVar()
        self.password = tk.StringVar()

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self, textvariable = self.email)
        self.email.trace_add("write", lambda x, y, z: self.setEmail(self.email))

        
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show = "*", textvariable = self.password)
        self.password.trace_add("write", lambda x, y, z: self.setPassword(self.password))
        

        self.email_label.grid(column = 0, row = 2, padx=5)
        self.email_entry.grid(column=1, row = 2)
        
        self.password_label.grid(column = 0, row = 3, padx=5)
        self.password_entry.grid(column=1, row = 3)
        
        label.grid(column = 1, row = 0)
        label_direction.grid(column = 1, row = 1)

        back_button = tk.Button(self, text="< Back", command = lambda: controller.showFrame("StartPage", controller.model))
        back_button.grid(column = 4, row = 2, padx=(0,10))

        
        enter_button = tk.Button(self, text="Enter >")
        enter_button.grid(column=4, row = 3, padx = (0, 10))
        #NOTE: THIS IS WHERE THE INFO WOULD BE PASSED TO HAO'S MODULE, EMAIL AND PASSWORD ARE STORED IN self.controller.legal_model.email
        #enter_button.grid(column=4, row = 3, padx= (0, 10), command = ???)
    
    def setEmail(self, email):
        self.controller.legal_model.setEmail(email.get())
        print(self.controller.legal_model.email)

    def setPassword(self, password):
        self.controller.legal_model.setPassword(password.get())
        print(self.controller.legal_model.password)
    


class PrefFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Preferred Name Change")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.showFrame("StartPage", controller.model))
        button.pack()

class DiplomaFrame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Diploma Info")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                           command=lambda: controller.showFrame("StartPage", controller.model))
        button.pack()

if __name__ == "__main__":
    model = NameChangeInfo()
    app = nameChanger(model)
    app.mainloop()