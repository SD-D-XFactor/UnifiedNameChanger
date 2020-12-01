from Naked.toolshed.shell import execute_js
import sys
sys.path.append("..")
import nameInterface

class PreferredName:
    def __init__(self):
        self.infoblock = {
            "name": "", # SHOULD BE FULL NAME, NOT JUST FIRST
            "cas_uname": "",
            "cas_pword": "",
            "submitty_uname": "",
            "submitty_pword": "",
            "webex_uname": "",
            "webex_pword": ""
        }
    def takeInformation(self, name: str, cas_uname: str, cas_pword: str,
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
    
    def submitNameChange(self) -> int:
        """
            Calls relevant name change functions
            Return 0 if successful, and the function number that failed otherwise
        """
        if not changeCas(self.infoblock["name"], self.infoblock["cas_uname"], 
                            self.infoblock["cas_pword"]):
            return 1
        if not changeRoundcube(self.infoblock["name"], self.infoblock["cas_uname"], 
                                self.infoblock["cas_pword"]):
            return 2
        if not changeSubmitty(self.infoblock["name"], self.infoblock["submitty_uname"], 
                                self.infoblock["submitty_pword"]):
            return 3
        if not changeWebex(self.infoblock["name"], self.infoblock["webex_uname"], 
                            self.infoblock["webex_pword"]):
            return 4
        return 0


def changeCas(name: str, cas_uname: str, cas_pword: str) -> bool:
    name = name.split()[0]
    return execute_js('casChange.js --uname ' + cas_uname + ' --pword ' + cas_pword + ' --pname ' + name);

def changeRoundcube(name: str, cas_uname: str, cas_pword: str) -> bool:
    return execute_js('roundcubeChange.js --uname ' + cas_uname + ' --pword ' + cas_pword + ' --pname ' + name);

def changeSubmitty(name: str, submitty_uname: str, submitty_pword: str) -> bool:
    return execute_js('submittyChange.js --uname ' + submitty_uname + ' --pword ' + submitty_pword + ' --pname ' + name);

def changeWebex(name: str, webex_uname: str, webex_pword: str) -> bool:
    return execute_js('webexChange.js --uname ' + webex_uname + ' --pword ' + webex_pword + ' --pname ' + name);
