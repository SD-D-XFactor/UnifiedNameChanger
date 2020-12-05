# Team Logistics and Evaluation

## Team Name

The X Factor

## Changes in Logistics from Team Deliverable 3

There are no changes in logistics from Team Deliverable 3

# Project Status Reports

## Current State

Slightly behind, however, catching up. We are making sure we know where to go with our project.

## Issues Encountered

1. Implementation issues with the preferred-name backend

Python didn't have an easy-to-import headless browser, so we needed to add Node.js to the mix in order to properly do the preferred name change. This slowed development slightly.

## Work Distribution

All team members have split work fairly evenly, with everyone working on all parts of the deliverables. In terms of implementation, Brooke is working on the preferred name backend, Hao is working on the legal name backend, Brass is working on the diploma reorder backend, Ryan is doing the GUI, and Leke is integration testing to make sure that all the parts work together.

# System Test Plan

## `TEST-1`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-5`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits enter/next

### Expected Outputs

Student has different name in LMS

### Expected Side Effects

N/A

## `TEST-2`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-6`, `REQ-7`. 

### Use Case 

`UC-2`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits enter/next

### Expected Outputs

Student has different name in RPI Directory

### Expected Side Effects

N/A

## `TEST-3`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-7`. 

### Use Case 

`UC-3`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits enter/next

### Expected Outputs

Student has different name in RPI's Housing System

### Expected Side Effects

N/A

## `TEST-4`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-5`. 

### Use Case 

`UC-4`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits enter/next

### Expected Outputs

Student has different name in Submitty

### Expected Side Effects

N/A

## `TEST-5`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-8`. 

### Use Case 

`UC-5`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits enter/next

### Expected Outputs

Student has different name in WebEx System

### Expected Side Effects

N/A

## `TEST-6`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-9`. 

### Use Case 

`UC-6`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits enter/next

### Expected Outputs

Student has different name in RPI Mail System

### Expected Side Effects

N/A

## `TEST-7`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-4`, `REQ-10`. 

### Use Case 

`UC-7`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses legal name change
3. User enters RCSID and password
4. User uploads relevant documentation
5. User hits enter/next

### Expected Outputs

The registrar is emailed a completed name change request

### Expected Side Effects

Registrar updates student's name

## `TEST-8`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-4`, `REQ-11`. 

### Use Case 

`UC-8`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses legal name change
3. User enters RCSID and password
4. User uploads relevant documentation
5. User hits enter/next

### Expected Outputs

Card Campus Office is prompted to issue a new ID with the newly changed name to the student

### Expected Side Effects

Student is issued a new ID

## `TEST-9`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-4`, `REQ-12`. 

### Use Case 

`UC-9`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses legal name change
3. User enters RCSID and password
4. User uploads relevant documentation
5. User hits enter/next

### Expected Outputs

The Health Center is emailed a completed name change request.

### Expected Side Effects

The Health Center updates student's CDPHP insurance information.

CDPHP is prompted to issue a new insurance card.

Student is issued a new insurance card.

## `TEST-10`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-4`, `REQ-13`. 

### Use Case 

`UC-10`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses legal name change
3. User enters RCSID and password
4. User uploads relevant documentation
5. User enters phone number
6. User hits enter/next

### Expected Outputs

A DotCIO ticket is generated requesting a name change in DotCIO ticketing system

### Expected Side Effects

Student's name is changed in DotCIO ticketing system.

## `TEST-11`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-4`, `REQ-14`. 

### Use Case 

`UC-11`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses legal name change
3. User enters RCSID and password
4. User uploads relevant documentation
5. User enters phone number
6. User hits enter/next

### Expected Outputs

A DotCIO ticket is generated requesting a name change in WebEx

### Expected Side Effects

Student's name is changed in WebEx.

## `TEST-12`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-4`, `REQ-15`

### Use Case 

`UC-12`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses diploma
3. User fills out information form
4. User hits enter/next

### Expected Outputs

User is provided a partially filled PDF

### Expected Side Effects

N/A

## `TEST-13`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-1`, `UC-2`, `UC-3`, `UC-4`, `UC-5`, `UC-6`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name with invalid symbols
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-14`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-1`, `UC-2`, `UC-3`, `UC-4`, `UC-5`, `UC-6`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name that has numbers
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-15`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-1`, `UC-2`, `UC-3`, `UC-4`, `UC-5`, `UC-6`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User does not input any name
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told to enter a name

### Expected Side Effects

User is prompted to enter a different name

## `TEST-16`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-1`, `UC-2`, `UC-3`, `UC-4`, `UC-5`, `UC-6`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs a name over 50 characters
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told to enter a shorter name

### Expected Side Effects

User is prompted to enter a different name

## `TEST-17`

### Requirements 

`REQ-2`, `REQ-3`, `REQ-4`. 

### Use Case 

`UC-7`, `UC-8`, `UC-9`, `UC-10`, `UC-11`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name with invalid symbols
2. User chooses legal name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-18`

### Requirements 

`REQ-2`, `REQ-3`, `REQ-4`. 

### Use Case 

`UC-7`, `UC-8`, `UC-9`, `UC-10`, `UC-11`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name that has numbers
2. User chooses legal name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-19`

### Requirements 

`REQ-2`, `REQ-3`, `REQ-4`. 

### Use Case 

`UC-7`, `UC-8`, `UC-9`, `UC-10`, `UC-11`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User does not input any name
2. User chooses legal name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told to enter a name

### Expected Side Effects

User is prompted to enter a name

## `TEST-20`

### Requirements 

`REQ-2`, `REQ-3`, `REQ-4`. 

### Use Case 

`UC-7`, `UC-8`, `UC-9`, `UC-10`, `UC-11`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name with over 50 characters
2. User chooses legal name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-21`

### Requirements 

`REQ-1`, `REQ-2`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`. 

### Use Case 

`UC-1`, `UC-2`, `UC-3`, `UC-4`, `UC-5`, `UC-6`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name on list of prohibited names
2. User chooses preferred name change
3. User enters RCSID and password
4. User hits next

### Expected Outputs

User is told that chosen name is prohibited

### Expected Side Effects

User is prompted to enter a different name

## `TEST-22`

### Requirements 

`REQ-2`, `REQ-3`, `REQ-4`. 

### Use Case 

`UC-10`, `UC-11`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses legal name change
3. User inputs invalid phone number
4. User enters RCSID and password
5. User hits next

### Expected Outputs

User is told that phone number is invalid

### Expected Side Effects

User is prompted to enter a valid phone number

## `TEST-23`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-12`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name with invalid symbols
2. User chooses diploma
3. User fills out information form
4. User hits enter/next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-24`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-12`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name that has numbers
2. User chooses diploma
3. User fills out information form
4. User hits enter/next

### Expected Outputs

User is told that name is invalid

### Expected Side Effects

User is prompted to enter a different name

## `TEST-25`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-12`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User does not input name
2. User chooses diploma
3. User fills out information form
4. User hits enter/next

### Expected Outputs

User is told to enter name

### Expected Side Effects

User is prompted to enter a name

## `TEST-26`

### Requirements 

`REQ-2`, `REQ-3`. 

### Use Case 

`UC-12`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name over 50 characters
2. User chooses diploma
3. User fills out information form
4. User hits enter/next

### Expected Outputs

User is told to enter a shorter name

### Expected Side Effects

User is prompted to enter a different name

## `TEST-27`

### Requirements 

`REQ-1`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`, `REQ-9`, `REQ-10`, `REQ-11`, `REQ-12`, `REQ-13`, `REQ-14`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters incorrect RCSID and password
4. User hits enter/next

### Expected Outputs

User is told that RCSID/Password is invalid

### Expected Side Effects

User is taken back to input RCSID and password

## `TEST-28`

### Requirements 

`REQ-1`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`, `REQ-9`, `REQ-10`, `REQ-11`, `REQ-12`, `REQ-13`, `REQ-14`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters correct RCSID but incorrect password for LMS
4. User hits enter/next

### Expected Outputs

User is told that RCSID/Password is invalid

### Expected Side Effects

User is taken back to input RCSID and password

## `TEST-29`

### Requirements 

`REQ-1`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`, `REQ-9`, `REQ-10`, `REQ-11`, `REQ-12`, `REQ-13`, `REQ-14`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters correct RCSID but incorrect password for RPI Directory
4. User hits enter/next

### Expected Outputs

User is told that RCSID/Password is invalid

### Expected Side Effects

User is taken back to input RCSID and password

## `TEST-30`

### Requirements 

`REQ-1`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`, `REQ-9`, `REQ-10`, `REQ-11`, `REQ-12`, `REQ-13`, `REQ-14`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters correct RCSID but incorrect password for Housing System
4. User hits enter/next

### Expected Outputs

User is told that RCSID/Password is invalid

### Expected Side Effects

User is taken back to input RCSID and password

## `TEST-31`

### Requirements 

`REQ-1`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`, `REQ-9`, `REQ-10`, `REQ-11`, `REQ-12`, `REQ-13`, `REQ-14`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters correct RCSID but incorrect password for WebEx
4. User hits enter/next

### Expected Outputs

User is told that RCSID/Password is invalid

### Expected Side Effects

User is taken back to input RCSID and password


## `TEST-32`

### Requirements 

`REQ-1`, `REQ-3`, `REQ-5`, `REQ-6`, `REQ-7`, `REQ-8`, `REQ-9`, `REQ-10`, `REQ-11`, `REQ-12`, `REQ-13`, `REQ-14`. 

### Use Case 

`UC-1`.

### Initial Setup

User opens up interface

### Steps/Inputs

1. User inputs name
2. User chooses preferred name change
3. User enters correct RCSID but incorrect password for email
4. User hits enter/next

### Expected Outputs

User is told that RCSID/Password is invalid

### Expected Side Effects

User is taken back to input RCSID and password

# Implementation Plan

We will mainly be using Python for the interface, LegalName, DiplomaHandler, and PreferredName. However, for the preferred name backend, Node.JS was also used, because a headless browser was needed, and the chrome devs wrote a library for Node (`puppeteer`) allowing for easy usage.

We have chosen Python as it has many useful libraries, and is simple to use. This allows for quick implementation and testing, at the cost of performance. However, this is not a concern as the tasks being performed are computationally simplistic.

We are using Node.JS for the preferred name backend, as it has the simplest headless browser interface available (Chrome, which most users likely have installed) which allows for a less bloated package, as most users will not have to install another browser.

For the python backends, we will be following the pythonic standard, and for function definitions, functions are defined in the following format: `def func([self], var: type) -> return_type:`, where `[self]` is included in a class function.

As Brooke is the only developer for Node.JS, the team hasn’t defined an agreed upon coding standard. Brooke will be following the best practices as outlined by Node.JS developers.

As Python does not require compilation, we have no compilation requirements for python. In terms of build requirements, all team members should have the packages and languages listed in `README.md` in the implementation

Brooke is following the best practices for compilation as outlined by Node.JS developers for the Node.JS modules.

# Unit Tests

Preferred Name:

```python
import unittest
import preferredBackend

class PreferredTestCase(unittest.TestCase):
    def test_fail_cas(self):
        result = preferredBackend.changeCas("Brooke Baer", "baerb", "fakePass")
        self.assertEqual(result, False)
    
    def test_fail_roundcube(self):
        result = preferredBackend.changeRoundcube("Brooke Baer", "baerb", "fakePass")
        self.assertEqual(result, False)
    
    def test_fail_submitty(self):
        result = preferredBackend.changeSubmitty("Brooke Baer", "baerb", "fakePass")
        self.assertEqual(result, False)
    
    def test_fail_webex(self):
        result = preferredBackend.changeWebex("Brooke Baer", "baerb", "fakePass")
        self.assertEqual(result, False)
    
    def test_fail_all(self):
        change = preferredBackend.PreferredName()
        change.takeInformation("Brooke Baer", "baerb", "fakePass", "baerb", "fakePass", "baerb", "fakePass")
        result = change.submitNameChange()
        self.assertEqual(result, [1, 2, 3, 4])

"""
There is no way to unit-test success without revealing my log-in information.
Unfortunately, this is the only thing I can test.
"""
```

Legal Name:

```python
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
```

Diploma:

```python

```