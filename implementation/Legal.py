import smtplib,ssl,string,getpass, email, sys, re
import nameInterface
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import ascii_letters, digits
sys.path.append(".")


class LegalName:
    def __init__(self):
        self.name = ""
        self.username = ""
        self.password = ""
        self.phone = ""
        self.document = ""


    def takeInformation(self, name: str, username: str, pword: str, phone: str, document: str) -> bool:
        """
            Overrides NameInterface.take_information()
            If any required fields are blank, return False, otherwise, return True
        """
        if (name == "" or username == "" or pword == ""  ):
            return False
        self.name = name
        self.username = username
        self.password = pword
        self.phone = phone
        self.document = document

        return True

    def submitNameChange(self):

        rin = input("Enter student rin then press enter: ")
        list_of_option = ["DotCio", "Webex", "Health", "Card", "Registrar", "All", "Hao", "Jiang"]

        for num, option in enumerate(list_of_option):
            print(num, option)

        choice = input("What department do you want to email? (input number) -->  ")

        while (not choice.isdigit()):
            choice = input("What department do you want to email? (input number) -->  ")

        mode = list_of_option[int(choice)]



        EmailAll(self.name, self.username,self.password, self.document, self.phone, rin, mode)




def CheckSymbols(name):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(name) == None):
        return False
    else:
        return True


def EmailAll(name, username, password, document, phoneNumber, rin, mode):
    name_has_digit = any(map(str.isdigit, name))
    if (name_has_digit == True):
        return ("Invalid name has digits!")
    elif (CheckSymbols(name)):
        return ("Invalid name has special characters!")
    elif (len(phoneNumber) > 10 or len(phoneNumber) < 10):
        return ("Invalid length of the phone number!")
    elif (len(rin) > 9 or len(rin) < 9):
        return ("Invalid length of student rin!")

    sendtohealth = "healthcenter@rpi.edu"
    sendtoregistrar = "registrar@rpi.edu"
    sendtodotcio = "itssc@support.rpi.edu"
    sendtowebex = "itssc@support.rpi.edu"
    sendtoemailcard = "campuscard@rpi.edu"
    sendto = sendtohealth + "," + sendtoregistrar + "," + sendtodotcio + "," + sendtowebex + "," + sendtoemailcard
    sendto1 = "jianghao98@yahoo.com," + "jiang10901@gmail.com"

    smtp_server = "mail.rpi.edu"
    smtp_port = 587
    subject = "Name changing"
    body = "Hi my name is {} and my rin is {}. Here are my documents to change my name.".format(name, rin)

    message = MIMEMultipart()
    message["From"] = username + "@rpi.edu"
    message["Subject"] = subject
    # message["Bcc"] = sendto
    if (mode == "DotCio"):
        message["To"] = sendtodotcio
    elif (mode == "Webex"):
        message["To"] = sendtowebex
    elif (mode == "Health"):
        message["To"] = sendtohealth
    elif (mode == "Card"):
        message["To"] = sendtoemailcard
    elif (mode == "Registrar"):
        message["To"] = sendtoregistrar
    elif (mode == "All"):
        message["To"] = sendto1


    # Add body to email
    message.attach(MIMEText(body, "plain"))

    file_name = document  # In same directory as script

    open_file = open(file_name, 'rb')  # Open the file as binary mode
    attach_pdf = MIMEBase('application', 'octate-stream')
    attach_pdf.set_payload((open_file).read())
    encoders.encode_base64(attach_pdf)  # encode the attachment
    attach_pdf.add_header('Content-Disposition', 'attachment', filename=file_name)
    message.attach(attach_pdf)

    # Encode file in ASCII characters to send by email
    # encoders.encode_base64(part)



    text = message.as_string()

    context = ssl.create_default_context()

    try:

        server = smtplib.SMTP(host=smtp_server, port=smtp_port)
        server.set_debuglevel(True)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        if (mode == "DotCio"):
            server.sendmail(username + "@rpi.edu", sendtodotcio, text)
        elif (mode == "Webex"):
            server.sendmail(username + "@rpi.edu", sendtowebex, text)
        elif (mode == "Health"):
            server.sendmail(username + "@rpi.edu", sendtohealth, text)
        elif (mode == "Card"):
            server.sendmail(username + "@rpi.edu", sendtoemailcard, text)
        elif (mode == "Registrar"):
            server.sendmail(username + "@rpi.edu", sendtoregistrar, text)
        elif (mode == "All"):
            server.sendmail(username + "@rpi.edu", sendto1.split(","), text)
    finally:
        server.quit()









if __name__ == "__main__":


    tmp = LegalName()
    tmp.name = "Hao Jiang"
    tmp.username = "Jiangh6"
    tmp.password = "Zoo1738*"
    tmp.phone = "9176289861"
    tmp.document = "diploma_reorder_form.pdf"
    tmp.submitNameChange()


