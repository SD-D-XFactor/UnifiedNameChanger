import requests
import name_interface

class PreferredNew:
    def __init__(self):
        self.infoblock = {
            "name": "",
            "cas_uname": "",
            "cas_pword": "",
            "submitty_uname": "",
            "submitty_pword": "",
            "webex_uname": "",
            "webex_pword": ""
        }
    def take_information(self, name: str, cas_uname: str, cas_pword: str,
                         submitty_uname: str, submitty_pword: str,
                         webex_uname: str, webex_pword: str) -> bool:
        """
            Overrides NameInterface.take_information()
            If any required fields are blank, return False, otherwise, return True
        """
        if (name == "" or cas_uname == "" or cas_pword == "" or submitty_uname == "" 
            or submitty_pword == "" or webex_uname == "" or webex_pword == ""):
            return False
        self.infoblock = {
            "name": name, 
            "cas_uname": cas_uname, 
            "cas_pword": cas_pword, 
            "submitty_uname": submitty_uname, 
            "submitty_pword": submitty_pword, 
            "webex_uname": webex_uname, 
            "webex_pword": webex_pword
        }
        return True
    
    def submit_name_change(self) -> int:
        """
            Calls relevant name change functions
            Return 0 if successful, and the function number that failed otherwise
        """
        if not change_cas(self.infoblock["name"], self.infoblock["cas_uname"], 
                          self.infoblock["cas_pword"]):
            return 1
        if not change_roundcube(self.infoblock["name"], self.infoblock["cas_uname"], 
                                self.infoblock["cas_pword"]):
            return 2
        if not change_submitty(self.infoblock["name"], self.infoblock["submitty_uname"], 
                               self.infoblock["submitty_pword"]):
            return 3
        if not change_webex(self.infoblock["name"], self.infoblock["webex_uname"], 
                               self.infoblock["webex_pword"]):
            return 4
        return 0


def change_cas(name: str, cas_uname: str, cas_pword: str) -> bool:
    return True

def change_roundcube(name: str, cas_uname: str, cas_pword: str) -> bool:
    return True

def change_submitty(name: str, submitty_uname: str, submitty_pword: str) -> bool:
    return True

def change_webex(name: str, webex_uname: str, webex_pword: str) -> bool:
    return True