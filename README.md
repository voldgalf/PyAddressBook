## Usage

### Initialization

To create your address book, create a `AddressBook` instance like below:

```python
myAddressBook = AddressBook()
```

### Creating contacts
The `BookRecord` class stores all the contact information.

It is called as `BookRecord(ContactName)`

```python
myContact = BookRecord("John Doe")
```
#### Adding Info

To add additional information to the contact you must call `addInformation(Name, Value)`

> [!TIP]
> The `Value` paramter can be numbers, string, or objects

```python
myContact.addInformation("Address", "123 Main Street")
```

#### Retrieving Info

To retrieve information from the contact, call `getInformation(Name)`.

```python
someVariable = myContact.getInformation("Address")
```

### Adding contacts

To add a contact to the address book, call `addContact(contact)`

Below is an example:

```python
myAddressBook = AddressBook()

newContact = BookRecord("John Doe")

myAddressBook.addContact(newContact)
```

### Saving/Loading your address book
To save your address book, call `save(filePath)`

```python
myAddressBook.save(filePath)
```

To load your address book, call the `AddressBook.load(fileName)` function

```python
myAddressBook.load(FileName)
```
