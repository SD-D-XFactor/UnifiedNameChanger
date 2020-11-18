import abc

class NameInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'submit_name_change') and 
                callable(subclass.submit_name_change) and 
                hasattr(subclass, 'take_information') and
                callable(subclass.take_information))

# see preferred_backend.py for example of implementation