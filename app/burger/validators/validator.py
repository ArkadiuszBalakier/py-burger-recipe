from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.protected_name = self.validate(name)

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.protected_name)

    @abstractmethod
    def validate(self, value):
        pass