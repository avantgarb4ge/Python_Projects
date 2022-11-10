

class Cheetos():
    def __init__(self):
        self._x = "protected"
        self.__y = "sacred"

    def getPrivate(self):
        return self.__y
    
    def setPrivate(self,private):
        self.__y = private
        
    
obj = Cheetos()

print("This member of Cheetos is {}.".format(obj._x))
# returning private value
# this method will not return bc it is PRIVATE
# print(obj.__y)
# this is the way around it, but it is frowned upon
print(obj._Cheetos__y)
# this would be the proper method
# print(obj.getPrivate())


