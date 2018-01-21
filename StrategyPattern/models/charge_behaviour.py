import abc

class Charge_Behaviour(metaclass=abc.ABCMeta):
    """This is the charge behaviour abstract class"""
    @abc.abstractmethod
    def charge(self):
        raise NotImlementError()
