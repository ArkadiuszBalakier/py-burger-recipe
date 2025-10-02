from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.protected_name = "_" + name

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        getattr(instance, self.protected_name)

    @abstractmethod
    def validate(self, value):
        pass