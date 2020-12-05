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

if __name__ == '__main__':
    unittest.main()
