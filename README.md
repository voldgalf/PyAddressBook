## Usage

### Initialization

To create your address book, create a `AddressBook` instance like below:

```python
myAddressBook = AddressBook()
```

### Adding contacts
The `BookRecord` class stores all the contact information

The contact's full name is required to initialize 

```python
myContact = BookRecord("John Doe")
```

#### Adding Info

To add additional information to the contact you must call `addInformation(Name, Value)`
```python
myContact.addInformation("Address", "123 Main Street")
```

#### Retrieving Info

To retrieve information from the contact, call `getInformation(Name)`.

```python
someVariable = myContact.getInformation("Address")
```

### Saving/Loading
To save your address book, call `save(filePath)`

```python
myAddressBook.save(filePath)
```

To load your address book, call the `AddressBook.load(fileName)` function

```python
myAddressBook.load(FileName)
```
