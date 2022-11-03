
class rental:
    # defining attributes of parent class
    sqft = 600
    homeType = 'apartment'
    price = 1250.00

class tenant(rental):
    # defining attributes of child class
    name = 'Jumbo Shrimp'
    email = 'jshrimp@seafood.com'

class landlord(rental):
    # defining attributes of child class
    numOfProp = 4
    lang = 'spanish'    
    
