import abc
import hashlib

class Person(object):
    __metaclass__ = abc.ABCMeta
    @property
    def Id(self):
        pass
    @Id.setter
    def Id(self, id):
        pass 
    @property
    def Name(self):
        pass
    @Name.setter
    def Name(self, name):
        pass
    @property
    def Email(self):
        pass
    @Email.setter
    def Email(self, email):
        pass