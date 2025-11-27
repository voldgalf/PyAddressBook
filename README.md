# PyAddressBook

PyAddressBook is a simple, structured yet expandable, Python library for address books.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pyaddressbook
```
## Usage

### Creating and Saving Address Books

```python
# Create an AddressBook instance
myAddressBook = AddressBook()

# Create a BookContact instance
myContact = AddressContact("John Doe")

# Add information to BookContact instance
myContact.addInformation("Address", "123 Main Street")

# Add BookContact instance to AddressBook
myAddressBook.addContact(myContact)

# Save current AddressBook to file
myAddressBook.save("myAddressBook.file")
```

### Loading Saved Address Books

```python
# Create an AddressBook instance
myAddressBook = AddressBook()

# Load AddressBook file to AddressBook instance
myAddressBook.load("myAddressBook.file")

# Retrieve all contacts from AddressBook instance
allContacts = myAddressBook.getContacts()

```

## License

[Apache-2.0](LICENSE)
