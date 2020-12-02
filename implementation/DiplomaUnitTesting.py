import unittest
import io
import datetime
import pdfrw

class TestDiploma(unittest.TestCase):
    def test_DataEntry(self):
        data = {'first': "John",
        'middle': "D.",
        'last': "Doe",
        'degree': "Bachelors",
        'curriculum': "Computer Science",
        'dateDegree': datetime.date(2016, 1, 1),
        'identificationTail': "0000",
        'birthDate': datetime.date(2000, 1, 1),
        'dates': [datetime.date(2012, 1, 1),datetime.date(2012, 1, 2)],
        'email': "doej@rpi.edu",
        'phone': "(000)-000-0000",
        'description': "Name has Changed",
        'returned': True,
        'payment': "Cash",
        'adress': "95 High St, Limestone, ME 04750"}
        CreatePdf(data)
        form = pdfrw.PdfReader('filled.pdf')
        self.assertEqual(form.Root.Pages.Kids[0].Annots[0]['first'], "John")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[1]['middle'], "D.")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[2]['last'], "Doe")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[3]['degree'], "Bachelors")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[4]['curriculum'], "Computer Science")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[5]['dateDegree'], "1/1/2016")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[6]['identificationTail'], "0000")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[7]['birthDate'], "1/1/2000")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[8]['dates'], "1/1/2012-1/2/2012")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[9]['email'], "doej@rpi.edu")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[10]['phone'], "(000)-000-0000")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[12]['description'], "Name has Changed")
        self.assertTrue(form.Root.Pages.Kids[0].Annots[13]['*'])
        self.assertEqual(form.Root.Pages.Kids[0].Annots[15]['payment'], "Cash")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[17]['adress'], "95 High St, Limestone, ME 04750")

    def test_AlternateValues(self):
        data = {'first': "John",
        'last': "Doe",
        'degree': "Bachelors",
        'curriculum': "Computer Science",
        'dateDegree': datetime.date(2016, 1, 1),
        'identificationTail': "0000",
        'birthDate': datetime.date(2000, 1, 1),
        'dates': "The first day of the year 2012",
        'email': "doej@rpi.edu",
        'phone': "(000)-000-0000",
        'returned': True,
        'payment': "Cash",
        'adress': "95 High St, Limestone, ME 04750"}
        CreatePdf(data)
        form = pdfrw.PdfReader('filled.pdf')
        self.assertEqual(form.Root.Pages.Kids[0].Annots[0]['/V'], "John")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[1]['/V'], "")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[2]['/V'], "Doe")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[3]['/V'], "Bachelors")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[4]['/V'], "Computer Science")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[5]['/V'], "1/1/2016")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[6]['/V'], "0000")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[7]['/V'], "1/1/2000")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[8]['/V'], "The first day of the year 2012")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[9]['/V'], "doej@rpi.edu")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[10]['/V'], "(000)-000-0000")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[12]['/V'], "I have changed my name and would like it to be represented on my diploma")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[13]["/V"], "*")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[15]['/V'], "")
        self.assertEqual(form.Root.Pages.Kids[0].Annots[17]['/V'], "95 High St, Limestone, ME 04750")

if __name__ == '__main__':
    unittest.main()
