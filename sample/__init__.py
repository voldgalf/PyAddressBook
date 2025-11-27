import pickle
import os

REGULAR_PROPERTIES = ["First Name", "Last Name", "Address", "Phone"]

class AddressContact:
    
    def __init__(self, fullName):
        self.info = {}
        
        self.addInformation("First Name", fullName.split()[0])
        
        self.addInformation("Last Name", fullName.split()[1])
    
    def addInformation(self, infoName, infoValue) -> None:
            
        self.info[infoName] = infoValue
        
    def getInformation(self, propertyName):
        
        return (self.info.get(propertyName))
        
    def getAllInformation(self) -> list:
        
        return(list(self.info.keys()))
            
class AddressBook:
    
    def __init__(self):
        
        self.contacts: List[BookContact] = []
    def getContacts(self):
        return self.contacts
    def addContact(self, BookContact):
        
        self.contacts.append(BookContact)
        
    def load(self, filePath) -> bool:
        if os.path.exists(filePath):

            with open(filePath, 'rb') as f:
                self.contacts = pickle.load(f)
            return True;
        else:
            return False
    def save(self, filePath):
        with open(filePath, 'wb') as f:
            pickle.dump(self.contacts, f)  
