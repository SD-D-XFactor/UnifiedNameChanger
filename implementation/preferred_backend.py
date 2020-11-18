import requests
import name_interface
from collections import namedtuple
preferred_struct = namedtuple("preferred_struct", "name cas_uname cas_pword" + 
                              " submitty_uname submitty_pword webex_uname" +
                              " webex_pword")

class PreferredNew:
    def __init__(self):
        self.infoblock = ()

    """Change Preferred Name"""
    def submit_name_change(self) -> bool:
        """Overrides NameInterface.submit_name_change()"""
        return True

    def take_information(self, name: str, cas_uname: str, cas_pword: str,
                         submitty_uname: str, submitty_pword: str,
                         webex_uname: str, webex_pword: str) -> bool:
        """Overrides NameInterface.take_information()"""
        self.infoblock = preferred_struct(name, cas_uname, cas_pword, submitty_uname,
                                          submitty_pword, webex_uname, webex_pword)
        print(self.infoblock)
        return True


def change_cas_roundcube(self, name: str, cas_uname: str, cas_pword: str) -> bool:
    pass

def change_submitty(self, name: str, submitty_uname: str, submitty_pword: str) -> bool:
    pass

def change_webex(self, name: str, webex_uname: str, webex_pword: str) -> bool:
    pass

x = PreferredNew()