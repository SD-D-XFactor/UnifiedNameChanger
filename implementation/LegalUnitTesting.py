import unittest
from emails import EmailAll



class TestEmails(unittest.TestCase):

    ''' test to check if the user input name has
        numbers in the name which will be invalid
    '''
    def test_NameDigit(self):
        name = "Alex1 Junes"
        username = "jiangh6"
        password = "12345"
        document = "pdf"
        phoneNumber = "0000000000"
        rin = "661000000"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertEqual(result,"Invalid name has digits!")
    
    ''' test to check if the user input name has
        any invalid sybmols which are not allowed
    '''
    def test_NameSymbols(self):
        name = "Alex@ Junes@"
        username = "jiangh6"
        password = "12345"
        document = "pdf"
        phoneNumber = "0000000000"
        rin = "661000000"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertEqual(result,"Invalid name has special characters!")
        
    ''' test to check if the user input username is the
        correct one that he/she has to login to the system
    '''
    def test_EmailUsername(self):
        name = "Hao Jiang"
        username = "jiangh829"
        password = "12345"
        document = "pdf"
        phoneNumber = "0000000000"
        rin = "661000000"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertEqual(result,"smtplib.SMTPAuthenticationError: (535, b'5.7.8 Error: authentication failed: UGFzc3dvcmQ6')")
    
    ''' test to check if the user input password is the
        correct one that he/she has to login to the system
    '''
    def test_EmailPassword(self):
        name = "Alex Junes"
        username = "jiangh6"
        password = "12345"
        document = "pdf"
        phoneNumber = "0000000000"
        rin = "661000000"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertEqual(result,"smtplib.SMTPAuthenticationError: (535, b'5.7.8 Error: authentication failed: UGFzc3dvcmQ6')")
        
    ''' test to check if the user input phone
        number is thecorrect length
    '''
    def test_PhoneNumber(self):
        name = "Alex Junes"
        username = "jiangh6"
        password = "12345"
        document = "pdf"
        phoneNumber = "123456789012"
        rin = "661000000"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertEqual(result,"Invalid length of the phone number!")
        
    ''' test to check if the user input rin
        is the correct length
    '''
    def test_Rin(self):
        name = "Alex Junes"
        username = "jiangh6"
        password = "12345"
        document = "pdf"
        phoneNumber = "1234567890"
        rin = "661000000123"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertEqual(result,"Invalid length of student rin!")
    
    ''' test to check if with the correct inputs in
        all the fields then the program would be true
        and valid. Although this case might be error because
        I don't wanna share my RCSID password! So you can try with yours!
    '''
    def test_EmailAll(self):
        name = "Hao Jiang"
        username = "jiangh6"
        #correct passwords
        password = "12345"
        document = "pdf"
        phoneNumber = "0000000000"
        rin = "661000000"
        sendtoemail = "Hao"
        result = EmailAll(name,username,password,document,phoneNumber,rin,sendtoemail)
        self.assertTrue(result)




if __name__ == '__main__':
    unittest.main()
