import abc

class NameInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'submitNameChange') and 
                callable(subclass.submitNameChange) and 
                hasattr(subclass, 'takeInformation') and
                callable(subclass.takeInformation))

# see preferred_backend.py for example of implementation
