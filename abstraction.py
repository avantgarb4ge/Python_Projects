

from abc import ABC, abstractmethod

class Dessert(ABC):
    def toBake(self, temp):
        print("Bake for 30 minutes at ",temp)

    @abstractmethod
    def toServe(self,serving):
        pass

class Cookies(Dessert):
    def toServe(self,serving):
        print('Present {} cookie per person.'.format(serving))


obj = Cookies()
obj.toBake("375")
obj.toServe("one")
