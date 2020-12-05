from Naked.toolshed.shell import execute_js
import sys
sys.path.append("..")
import nameInterface

class PreferredName:
    def __init__(self):
        self.infoblock = {
            "name": "", # SHOULD BE FULL NAME, NOT JUST FIRST
            "rcsid": "",
            "pword": ""
        }
    def takeInformation(self, name: str, rcsid: str, pword: str) -> bool:
        """
            Overrides NameInterface.take_information()
            If any required fields are blank, return False, otherwise, return True
        """
        if (name == "" or rcsid == "" or pword == ""):
            return False
        self.infoblock = {
            "name": name,
            "rcsid": rcsid, 
            "pword": pword
        }
        return True
    
    def submitNameChange(self) -> list:
        """
            Calls relevant name change functions
            Return [] if successful, and the function number(s) that failed otherwise
        """
        failed = []
        if not changeCas(self.infoblock["name"], self.infoblock["rcsid"], 
                            self.infoblock["pword"]):
            failed.append(1)
        if not changeRoundcube(self.infoblock["name"], self.infoblock["rcsid"], 
                                self.infoblock["pword"]):
            failed.append(2)
        if not changeSubmitty(self.infoblock["name"], self.infoblock["rcsid"], 
                                self.infoblock["pword"]):
            failed.append(3)
        if not changeWebex(self.infoblock["name"], self.infoblock["rcsid"], 
                            self.infoblock["pword"]):
            failed.append(4)
        return failed


def changeCas(name: str, cas_uname: str, cas_pword: str) -> bool:
    name = name.split()[0]
    return execute_js('casChange.js --uname ' + cas_uname + ' --pword ' + cas_pword + ' --pname ' + name);

def changeRoundcube(name: str, cas_uname: str, cas_pword: str) -> bool:
    return execute_js('roundcubeChange.js --uname ' + cas_uname + ' --pword ' + cas_pword + ' --pname ' + name);

def changeSubmitty(name: str, submitty_uname: str, submitty_pword: str) -> bool:
    return execute_js('submittyChange.js --uname ' + submitty_uname + ' --pword ' + submitty_pword + ' --pname ' + name);

def changeWebex(name: str, webex_uname: str, webex_pword: str) -> bool:
    return execute_js('webexChange.js --uname ' + webex_uname + ' --pword ' + webex_pword + ' --pname ' + name);
