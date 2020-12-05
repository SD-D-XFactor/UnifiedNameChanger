import io
import datetime
import pdfrw

'''
Function will assume data is present unless otherwise stated

Data keys:
first - First name (string)
middle - Middle name / Initial (string, will assume none if not included)
last - Last name (string)
degree - Name of degree (string)
curriculum - Name of curriculum (string)
dateDegree - Date degree was issued (datetime.date)
identificationTail - Last 4 digits of SSN or RIN (string)
birthDate - Date of birth (datetime.date)
dates - A series of dates, assumed to be in pairs representing the beginning and end of periods of attendance, or a string (list of datetime.date, or a string)
email - Email adress (string)
phone - Phone number (string)
description - What happened to the diploma (will default to "I have changed my name and would like it to be represented on my diploma" if not included)
returned - Is the user returning their diploma (boolean)
payment - Unclear (string, will put nothing if missing)
address - Adress to return diploma to (string)
'''

def CreatePdf(data):
    form = pdfrw.PdfReader('diploma_reorder_form.pdf')
    form.Root.Pages.Kids[0].Annots[0].update(pdfrw.PdfDict(V=data['first']))
    form.Root.Pages.Kids[0].Annots[1].update(pdfrw.PdfDict(V=data['middle']))
    form.Root.Pages.Kids[0].Annots[2].update(pdfrw.PdfDict(V=data['last']))
    form.Root.Pages.Kids[0].Annots[3].update(pdfrw.PdfDict(V=data['degree']))
    form.Root.Pages.Kids[0].Annots[4].update(pdfrw.PdfDict(V=data['curriculum']))
    form.Root.Pages.Kids[0].Annots[5].update(pdfrw.PdfDict(V=data['dateDegree']))
    form.Root.Pages.Kids[0].Annots[6].update(pdfrw.PdfDict(V=data['identificationTail']))
    form.Root.Pages.Kids[0].Annots[7].update(pdfrw.PdfDict(V=data['birthDate']))
    form.Root.Pages.Kids[0].Annots[8].update(pdfrw.PdfDict(V=data['dates']))
    form.Root.Pages.Kids[0].Annots[9].update(pdfrw.PdfDict(V=data['email']))
    form.Root.Pages.Kids[0].Annots[10].update(pdfrw.PdfDict(V=data['phone']))
    form.Root.Pages.Kids[0].Annots[12].update(pdfrw.PdfDict(V=data['description']))
    if (data['returned']):
        form.Root.Pages.Kids[0].Annots[13].update(pdfrw.PdfDict(V='*'))
    else:
        form.Root.Pages.Kids[0].Annots[14].update(pdfrw.PdfDict(V='*'))
    form.Root.Pages.Kids[0].Annots[15].update(pdfrw.PdfDict(V=data['payment']))
    form.Root.Pages.Kids[0].Annots[17].update(pdfrw.PdfDict(V=data['address']))
    pdfrw.PdfWriter().write('filled.pdf', form)
    
'''
if __name__ == '__main__':
    data = {'first': "first",
    'middle': "middle",
    'last': "last",
    'degree': "degree",
    'curriculum': "curriculum",
    'dateDegree': "dateDegree",
    'identificationTail': "identificationTail",
    'birthDate': "birthDate",
    'dates': "dates",
    'email': "email",
    'phone': "phone",
    'description': "description",
    'returned': True,
    'payment': "payment",
    'address': "address"}
    CreatePdf(data)'''
