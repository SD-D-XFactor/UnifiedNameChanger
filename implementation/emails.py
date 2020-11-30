import smtplib,ssl,string,getpass, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def email_all1(name,username,password1,document,phoneNumber,rin,mode):
    sendtohealth = "healthcenter@rpi.edu"
    sendtoregistrar = "registrar@rpi.edu"
    sendtodotcio = "itssc@support.rpi.edu"
    sendtowebex = ""
    sendtoemailcard = ""
    sendto = sendtohealth + "," + sendtoregistrar + "," + sendtodotcio + "," + sendtowebex + "," + sendtoemailcard
    sendto1 = "jianghao98@yahoo.com," + "jiang10901@gmail.com"
    
    

    smtp_server = "mail.rpi.edu"
    smtp_port = 587
    subject = "Name changing"
    body = "Hi my name is {} and my rin is {}. Here are my documents to change my name.".format(name,rin)


    message = MIMEMultipart()
    message["From"] = username + "@rpi.edu"
    message["Subject"] = subject
    #message["Bcc"] = sendto
    if(mode == "DotCio"):
        message["To"] = sendtodotcio
    elif(mode == "Webex"):
        message["To"] = sendtowebex
    elif(mode == "Health"):
        message["To"] = sendtohealth
    elif(mode == "Card"):
        message["To"] = sendtoemailcard
    elif(mode == "Registrar"):
        message["To"] = sendtoregistrar
    elif(mode == "All"):
        message["To"] = sendto1

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    file_name = "Midterm.pdf"  # In same directory as script

    open_file = open(file_name, 'rb') # Open the file as binary mode
    attach_pdf = MIMEBase('application', 'octate-stream')
    attach_pdf.set_payload((open_file).read())
    encoders.encode_base64(attach_pdf) #encode the attachment
    attach_pdf.add_header('Content-Disposition', 'attachment', filename = file_name)
    message.attach(attach_pdf)

    # Encode file in ASCII characters to send by email
    #encoders.encode_base64(part)



    text = message.as_string()

    context = ssl.create_default_context()
    
    try :

        server = smtplib.SMTP(host=smtp_server, port=smtp_port)
        server.set_debuglevel(True)
        server.ehlo()
        server.starttls(context = context)
        server.ehlo()
        server.login(username, password)
        if(mode == "DotCio"):
            server.sendmail(username+"@rpi.edu",sendtodotcio,text)
        elif(mode == "Webex"):
            server.sendmail(username+"@rpi.edu",sendtowebex,text)
        elif(mode == "Health"):
            server.sendmail(username+"@rpi.edu",sendtohealth,text)
        elif(mode == "Card"):
            server.sendmail(username+"@rpi.edu",sendtoemailcard,text)
        elif(mode == "Registrar"):
            server.sendmail(username+"@rpi.edu",sendtoregistrar,text)
        elif(mode == "All"):
            server.sendmail(username+"@rpi.edu",sendto1.split(","),text)
    finally:
        server.quit()

#seperate functions or just one function with modes to check the places to send emails to?
def email_dotcio(name,username,password1,document,phoneNumber,rin):
    sendto = "itssc@support.rpi.edu"
    smtp_server = "mail.rpi.edu"
    smtp_port = 587
    
    subject = "Name changing"
    body = "Hi my name is {} and my rin is {}. Here are my documents to change my name.".format(name,rin)


    message = MIMEMultipart()
    message["From"] = username + "@rpi.edu"
    message["To"] = sendto
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    file_name = "Midterm.pdf"  # In same directory as script

    open_file = open(file_name, 'rb') # Open the file as binary mode
    attach_pdf = MIMEBase('application', 'octate-stream')
    attach_pdf.set_payload((open_file).read())
    encoders.encode_base64(attach_pdf) #encode the attachment
    attach_pdf.add_header('Content-Disposition', 'attachment', filename = file_name)
    message.attach(attach_pdf)

    text = message.as_string()
    context = ssl.create_default_context()

    try :

        server = smtplib.SMTP(host=smtp_server, port=smtp_port)
        server.set_debuglevel(True)
        server.ehlo()
        server.starttls(context = context)
        server.ehlo()
        server.login(username, password)
        server.sendmail(username+"@rpi.edu",sendto,text)
    finally:
        server.quit()



if __name__ == "__main__":
    name = input("Enter your full name then press enter: ").strip()
    username = input("Enter your RCS ID (without the @rpi.edu) then press enter: ").replace(" ","")
    
    print("Enter password to rpi email: ")
    password = getpass.getpass()
    document = "pdf"
    phoneNumber = input("Enter phone number then press enter:")
    rin = input("Enter student rin then press enter: ")
    list_of_option = ["DotCio","Webex","Health","Card","Registrar","All","Hao","Jiang"]
    
    for num,option in enumerate(list_of_option):
        print(num,option)
        
    choice = input("What department do you want to email? (input number) -->  ")
    
    while(not choice.isdigit()):
        choice = input("What department do you want to email? (input number) -->  ")
    
    mode = list_of_option[int(choice)]
    
    
    email_all1(name,username,password,document,phoneNumber,rin,mode)

