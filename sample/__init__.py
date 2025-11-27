import pickle
import os

REGULAR_PROPERTIES = ["First Name", "Last Name", "Address", "Phone"]

class BookContact:
    
    def __init__(self, fullName):
        """Class docstrings go here."""
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
        
        self.records: List[BookRecord] = []
    def getContacts(self):
        return self.records
    def addContact(self, BookRecord):
        
        self.records.append(BookRecord)
        
    def load(self, filePath) -> bool:
        if os.path.exists(filePath):

            with open(filePath, 'rb') as f:
                self.records = pickle.load(f)
            return True;
        else:
            return False
    def save(self, fileName):
        with open(fileName, 'wb') as f:
            pickle.dump(self.records, f)  
            
FileName = "myAddress.book"

myAddressBook = AddressBook()

if(not myAddressBook.load(FileName)):
    print(f"{FileName} does not exist... creating new address book")
    myAddressBook = AddressBook()
    John = BookRecord("John McClane")
    John.addInformation("Address", "New York")
    John.addInformation("Phone", "123-456-7891")

    myAddressBook.addRecord(John)

    myAddressBook.save(FileName)

    print(John.printAllInformation())
else:
    print(f"{FileName} Loaded")
    for record in myAddressBook.getRecords():
        record.printAllInformation()
