import tkinter as tk
import datetime
from tkinter import filedialog
from tkcalendar import Calendar, DateEntry

#EVERYTHING IS STORED IN THE MODELS (LEGALCHANGEINFO, PREFCHANGEINFO, DIPLOMACHANGEINFO)
#access the information by calling self.controller.(pref_model/Legal_model/dip_model).getName/getEmail/getCas IN the frames
#information needs to be grabbed from the models in nameChanger

#Model for the NameChange interface. It contains the name that the user has inputted and passes to the other model
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

#Model for the LegalChange frame. It holds the legal info that the user has inputted
class LegalChangeInfo():
    def __init__(self):
        self.name=""
        self.email=""
        self.password=""
        self.filename=""
    def setName(self, name):
        self.name = name
    def setEmail(self, email):
        self.email = email
    def setPassword(self, password):
        self.password = password
    def setFilename(self, file):
        self.file = file
#Model for the LegalChange frame. It holds the legal info that the user has inputted
class PrefChangeInfo():
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
    
    def setCasUName(self, uname):
        self.cas_uname = uname

    def setCasPWord(self, pword):
        self.cas_pword = pword
    
    def setSubmittyUName(self, uname):
        self.cas_uname = uname
    
    def setSubmittyPWord(self, pword):
        self.submitty_pword = pword

    def setWebexUName(self, uname):
        self.webex_uname = uname
    
    def setWebexPWord(self, pword):
        self.webex_uname = pword
    
    def getName(self):
        return self.name
    
    def getCas(self):
        return (self.cas_uname, self.cas_pword)
    
    def getSubmitty(self):
        return (self.submitty_uname, self.submitty_pword)
    
    def getWebex(self):
        return (self.webex_uname, self.webex_pword)

#Model for the DiplomaChange frame. It holds all the diploma info that the user has inputted
class DipChangeInfo():
    def __init__(self):
        # dipDict = {'first': "", 'middle': "", 'last': "", 'degree': "", 'curriculum': "", 'dateDegree': "", 'identificationTail': "",
        # 'birthDate': "",'birth_date': "", 'attend_date': "", 'email': "", 'phone': "", 'description': "", 'returned': "", 'payment': "", 'address':""}
        self.dipDict = {}
    def setInfo(self, dict):
        self.dipDict = dict

class nameChanger(tk.Tk):
    #"root" class. Holds all the models, and handles changing of the frames
    def __init__(self, model, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.model = model
        self.legal_model = LegalChangeInfo()
        self.pref_model = PrefChangeInfo()
        self.dip_model = DipChangeInfo()
        #add more models here

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1, weight=0)
        container.grid_columnconfigure(1, weight=0)

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

        for frame in self.frames.values():
            frame.grid_remove()

        self.model = model
        frame = self.frames[page_name]
        frame.grid()

        if page_name == "StartPage":
            self.geometry("380x120")

        if page_name == "PrefFrame":
            self.geometry("400x220")
        
        elif page_name == "LegalFrame":
                self.geometry("430x145")
        
        elif page_name == "DiplomaFrame":
                self.geometry("420x650")
        
        else: 
            self.geometry("380x120")
        
        frame.tkraise()

class StartPage(tk.Frame):
    #start page for namechange, will allow user to choose the type of change and takes in a name to pass to models
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 400)
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
        self.next_button.pack(side="top", fill = "x",pady=10)

    #this will just set name = to entry.get(), if name is not valid, will set name_inputted to false, otherwise true
    #basically will switch to the frame specified by the radio button 
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
    
    #enables next button if both entry and radio button are selected/written
    def checkInfo(self):
        self.type_inputted = True
        # print(self.new_name.get())
        # print(self.name_inputted)
        if (self.name_inputted and self.type_inputted):
            self.next_button["state"] = "normal"
        else:
            self.next_button["state"] = "disabled" 
    
class LegalFrame(tk.Frame):
    #allows entering of info for legal_model
    #all info is passed to legal_model
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

        upload_button = tk.Button (self, text = "Upload", command = lambda: self.setUpload())
        upload_button.grid(column = 1, row = 4, padx = (0, 10))


        back_button = tk.Button(self, text="< Back", command = lambda: controller.showFrame("StartPage", controller.model))
        back_button.grid(column = 4, row = 2, padx=(0,10))

        
        enter_button = tk.Button(self, text="Enter >")
        enter_button.grid(column=4, row = 3, padx = (0, 10))
        #NOTE: THIS IS WHERE THE INFO WOULD BE PASSED TO HAO'S MODULE, EMAIL AND PASSWORD ARE STORED IN self.controller.legal_model.email
        #enter_button.grid(column=4, row = 3, padx= (0, 10), command = ???)
    
    def setEmail(self, email):
        self.controller.legal_model.setEmail(email.get())
        # print(self.controller.legal_model.email)

    def setPassword(self, password):
        self.controller.legal_model.setPassword(password.get())
        # print(self.controller.legal_model.password)
    
    #passes filename to legal model
    def setUpload(self, event = None):
        filename = filedialog.askopenfile()
        self.controller.legal_model.setFilename(filename)

class PrefFrame(tk.Frame):
    #this holds all the info for pref name changes
    #passes all info to pref_model as it is entered
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        
        label = tk.Label(self, text="Preferred Name Change")
        label.grid(column = 2, row = 0)
        button = tk.Button(self, text="Go back", command=lambda: controller.showFrame("StartPage", controller.model))
        button.grid(column = 1, row = 8, pady = 10)

        self.controller.pref_model.setName(self.controller.model.getName())

        self.cas_uname = tk.StringVar()
        self.cas_pword = tk.StringVar()

        self.submitty_uname = tk.StringVar()
        self.submitty_pword = tk.StringVar()

        self.webex_uname = tk.StringVar()
        self.webex_pword = tk.StringVar()
        
        self.cas_uname_label = tk.Label(self, text="CAS Username:")
        self.cas_uname_entry = tk.Entry(self, textvariable = self.cas_uname)
        self.cas_uname.trace_add("write", lambda x, y, z: self.setCasUName(self.cas_uname))

        self.cas_pword_label = tk.Label(self, text="CAS Password:")
        self.cas_pword_entry = tk.Entry(self, show="*", textvariable = self.cas_pword)
        self.cas_pword.trace_add("write", lambda x, y, z: self.setCasPWord(self.cas_pword))

        self.cas_uname_label.grid(column = 1, row = 2, padx=5)
        self.cas_uname_entry.grid(column=2, row = 2)
        
        self.cas_pword_label.grid(column = 1, row = 3, padx=5)
        self.cas_pword_entry.grid(column=2, row = 3)

        #submitty
        self.submitty_uname_label = tk.Label(self, text="Submitty Username:")
        self.submitty_uname_entry = tk.Entry(self, textvariable = self.submitty_uname)
        self.submitty_uname.trace_add("write", lambda x, y, z: self.setSubmittyUName(self.submitty_uname))

        self.submitty_pword_label = tk.Label(self, text="Submitty Password:")
        self.submitty_pword_entry = tk.Entry(self, show="*", textvariable = self.submitty_pword)
        self.submitty_pword.trace_add("write", lambda x, y, z: self.setSubmittyPWord(self.submitty_pword))

        self.submitty_uname_label.grid(column = 1, row = 4, padx=5)
        self.submitty_uname_entry.grid(column=2, row = 4)
        
        self.submitty_pword_label.grid(column = 1, row = 5, padx=5)
        self.submitty_pword_entry.grid(column=2, row = 5)

        #webex
        self.webex_uname_label = tk.Label(self, text="Webex Username:")
        self.webex_uname_entry = tk.Entry(self, textvariable = self.webex_uname)
        self.webex_uname.trace_add("write", lambda x, y, z: self.setWebexUName(self.webex_uname))

        self.webex_pword_label = tk.Label(self, text="Webex Password:")
        self.webex_pword_entry = tk.Entry(self, show = "*", textvariable = self.webex_pword)
        self.webex_pword.trace_add("write", lambda x, y, z: self.setWebexPWord(self.webex_pword))

        self.webex_uname_label.grid(column = 1, row = 6, padx=5)
        self.webex_uname_entry.grid(column=2, row = 6)
        
        self.webex_pword_label.grid(column = 1, row = 7, padx=5)
        self.webex_pword_entry.grid(column=2, row = 7)
      
        button = tk.Button(self, text="Enter >")
        button.grid(column = 2, row = 8, pady = 10)



    def setCasUName(self, cas_uname):
        self.controller.pref_model.setCasUName(cas_uname.get())

    def setCasPWord(self, cas_pword):
        self.controller.pref_model.setCasPWord(cas_pword.get())

    def setSubmittyUName(self, submitty_uname):
            self.controller.pref_model.setSubmittyUName(submitty_uname.get())

    def setSubmittyPWord(self, submitty_pword):
        self.controller.pref_model.setSubmittyPWord(submitty_pword.get())

    def setWebexUName(self, webex_uname):
        self.controller.pref_model.setWebexUName(webex_uname.get())

    def setWebexPWord(self, webex_pword):
        self.controller.pref_model.setWebexPWord(webex_pword.get())

class DiplomaFrame(tk.Frame):
    
    #this holds the info needed for the diploma, it holds all info for the diploma in a map
    #this frame will pass all the info onto the dip_model
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Diploma Info")
        label.grid(column = 2, row = 0)
        button = tk.Button(self, text="< Back",
                           command=lambda: controller.showFrame("StartPage", controller.model))
        button.grid(column = 1, row = 19)

        dipDict = {'first': "", 'middle': "", 'last': "", 'degree': "", 'curriculum': "", 'dateDegree': "", 'identificationTail': ""
        ,'birth_date': "", 'attend_date': "", 'email': "", 'phone': "", 'description': "", 'returned': "", 'payment': "", 'address':""}

        self.first_name = tk.StringVar()
        self.middle_name = tk.StringVar()
        self.last_name = tk.StringVar()

        self.degree = tk.StringVar()
        self.curriculum = tk.StringVar()
        self.date_degree = datetime.date(2000, 1, 1)
        self.id_tail = tk.StringVar()
        self.birth_date = datetime.date(2000, 1, 1)
        self.start_date = datetime.date(2000, 1, 1)
        self.end_date = datetime.date(2000, 1, 1)
        self.email = tk.StringVar()
        self.phone = tk.StringVar()
        self.description = tk.StringVar()
        self.dip_returned = bool
        self.payment = tk.StringVar()
        self.address = tk.StringVar()

        self.first_name_label = tk.Label(self, text="First Name:", anchor = "w")
        self.first_name_entry = tk.Entry(self, textvariable = self.first_name)
        self.first_name_label.grid(column = 1, row = 2, padx=(10,5))
        self.first_name_entry.grid(column=2, row = 2)

        self.middle_name_label = tk.Label(self, text="Middle Name:")
        self.middle_name_entry = tk.Entry(self, textvariable = self.middle_name)
        self.middle_name_label.grid(column = 1, row = 3, padx=(10,5))
        self.middle_name_entry.grid(column=2, row = 3)

        self.last_name_label = tk.Label(self, text="Last Name:")
        self.last_name_entry = tk.Entry(self, textvariable = self.last_name)
        self.last_name_label.grid(column = 1, row = 4, padx=(10,5))
        self.last_name_entry.grid(column=2, row = 4)

        self.degree_label = tk.Label(self, text="Degree:")
        self.degree_entry = tk.Entry(self, textvariable = self.degree)
        self.degree_label.grid(column = 1, row = 5, padx=(10,5))
        self.degree_entry.grid(column=2, row = 5)

        self.curriculum_label = tk.Label(self, text="Curriculum:")
        self.curriculum_entry = tk.Entry(self, textvariable = self.curriculum)
        self.curriculum_label.grid(column = 1, row = 6, padx=(10,5))
        self.curriculum_entry.grid(column=2, row = 6)

        self.date_degree_label = tk.Label(self, text="Date of Degree:")
        self.date_degree_cal = DateEntry(self)
        self.date_degree_cal.bind("<<DateEntrySelected>>", self.setDateDegree())
        self.date_degree_label.grid(column=1, row = 7)
        self.date_degree_cal.grid(column = 2, row = 7)

        self.id_label_1 = tk.Label(self, text="Last 4 Digits of SSN:")
        self.id_label_2 = tk.Label(self, text = "or Student ID#")
        self.id_entry = tk.Entry(self, textvariable = self.id_tail)
        self.id_label_1.grid(column = 1, row = 8, padx=(10,5))
        self.id_label_2.grid(column = 1, row = 9)
        self.id_entry.grid(column=2, row = 8)

        self.birth_date_label = tk.Label(self, text="Date of Birth:")
        self.birth_date_cal = DateEntry(self)
        self.birth_date_cal.bind("<<DateEntrySelected>>", self.setBirthDate())
        self.birth_date_label.grid(column=1, row = 10)
        self.birth_date_cal.grid(column = 2, row = 10)

        self.start_date_label = tk.Label(self, text="Attendance Start Date")
        self.start_date_cal = DateEntry(self, width = 12)
        self.start_date_cal.bind("<<DateEntrySelected>>", self.setStartDate())
        self.start_date_label.grid(column=1, row = 11)
        self.start_date_cal.grid(column = 2, row = 11)

        self.end_date_label = tk.Label(self, text="Attendance End Date")
        self.end_date_cal = DateEntry(self, width = 12)
        self.end_date_cal.bind("<<DateEntrySelected>>", self.setEndDate())
        self.end_date_label.grid(column=1, row = 12)
        self.end_date_cal.grid(column = 2, row = 12)

        self.email_label = tk.Label(self, text="Email:")
        self.email_entry = tk.Entry(self, textvariable = self.email)
        self.email_label.grid(column = 1, row = 13, padx=(10,5))
        self.email_entry.grid(column=2, row = 13)
        
        self.phone_label = tk.Label(self, text="Phone #:")
        self.phone_entry = tk.Entry(self, textvariable = self.phone)
        self.phone_label.grid(column = 1, row = 14, padx=(10,5))
        self.phone_entry.grid(column=2, row = 14)

        self.description_label = tk.Label(self, text="Reason for Request:")
        self.description_entry = tk.Entry(self, textvariable = self.description)
        self.description_label.grid(column = 1, row = 15, padx=(10,5))
        self.description_entry.grid(column=2, row = 15)

        self.temp_int = tk.IntVar()

        self.returned_label = tk.Label(self, text= "Diploma returned?")
        self.returned_label.grid(column = 1, row = 16)
        self.return_true_dip = tk.Radiobutton(self, text="Yes", value=1, variable=self.temp_int, command = self.setReturned())
        self.return_false_dip = tk.Radiobutton(self, text="No", value=0,  variable=self.temp_int, command = self.setReturned())
        self.return_true_dip.grid(column = 2, row = 16)
        self.return_false_dip.grid(column = 3, row = 16)

        self.pay_label = tk.Label(self, text="Payment Type ($50):")
        self.pay_entry = tk.Entry(self, textvariable = self.payment)
        self.pay_label.grid(column = 1, row = 17, padx=(10,5))
        self.pay_entry.grid(column=2, row = 17)

        self.address_label = tk.Label(self, text="Address:")
        self.address_entry = tk.Entry(self, textvariable = self.address)
        self.address_label.grid(column = 1, row = 18, padx=(10,5))
        self.address_entry.grid(column=2, row = 18)

        self.enter_button = tk.Button(self, text="Enter >",
                           command=lambda: self.updateDipModel(dipDict))
        self.enter_button.grid(column = 2, row = 19)

    def setDateDegree(self):
        self.date_degree = self.date_degree_cal.get_date()
        print (self.date_degree)

    def setBirthDate(self):
        self.birth_date = self.birth_date_cal.get_date()

    def setStartDate(self):
        self.start_date = self.start_date_cal.get_date()
    
    def setEndDate(self):
        self.end_date = self.end_date_cal.get_date()

    def setReturned(self):
        if self.temp_int == 1:
            self.dip_returned = True
        else:
            self.dip_returned = False
 
    def updateDipModel(self, dict):

        dict['first'] = self.first_name.get()
        dict['middle'] = self.middle_name.get()
        dict['last'] = self.last_name.get()
        dict['degree'] = self.degree.get()
        dict['curriculum'] = self.curriculum.get()
        dict['dateDegree'] = self.date_degree_cal.get()
        dict['identificationTail'] = self.id_tail.get()
        dict['birth_date'] = self.birth_date_cal.get()
        dict['attend_date'] = [self.start_date_cal.get(), self.end_date_cal.get()]
        dict['email'] = self.email.get()
        dict['phone'] = self.phone.get()
        dict['description'] = self.description.get()
        dict['returned'] = self.dip_returned
        dict['payment'] = self.payment.get()
        dict['address'] = self.address.get()

        self.controller.dip_model.setInfo(dict)

        # print(dict)


if __name__ == "__main__":
    model = NameChangeInfo()
    app = nameChanger(model)
    app.mainloop()