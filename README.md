## Usage

### Initialization

To create your address book, create a `AddressBook` instance like below:

```python
myAddressBook = AddressBook()
```

### Creating contacts

Call `BookContact(ContactName)` to create an instance of `BookContact` which stores information for an individual contact.

```python
myContact = BookContact("John Doe")
```

#### Adding information to contacts

To add additional information to the contact you must call `addInformation(Name, Value)`

> [!TIP]
> The `Value` parameter is not limited to strings, it can be integers, objects, or even other library data structures!

```python
myContact.addInformation("Address", "123 Main Street")
```

#### Retrieving information from contacts

To retrieve information from the contact, call `getInformation(Name)`.

```python
someVariable = myContact.getInformation("Address")
```

### Adding contacts

To add a contact to the address book, call `addContact(contact)`

Below is an example:

```python
newContact = BookContact("John Doe")

myAddressBook.addContact(newContact)
```

### Saving/Loading your address book
To save your address book, call `save(filePath)`

```python
myAddressBook.save(filePath)
```

To load your address book, call the `AddressBook.load(fileName)` function

```python
myAddressBook.load(fileName)
```
