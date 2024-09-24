# Contact Management System
## Overview
This project is a Contact Management System implemented in Python. The system allows users to manage their contacts by adding, viewing, editing, and deleting contact information (name, phone number, and email). The project also includes unit tests written using the pytest framework.

## Features
1. **Add Contact:** Add a new contact with a name, phone number, and email address.
2. **View Contacts:** Display all saved contacts in a formatted list.
3. **Edit Contact:** Update the details of an existing contact.
4. **Delete Contact:** Remove a contact from the list.
5. **Save Contacts:** Automatically save contacts to a JSON file after changes.

## Installation and Setup
### Prerequisites
* Python 3.x
* pytest (for running tests)

### Steps
1. Clone the repository:

```
git clone https://github.com/Wise-deldu/PRODIGY_SD_03.git
cd PRODIGY_SD_03
```

2. Install dependencies:
Install the required packages for running tests by creating a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

Install pytest:

```
pip install pytest
```

Install pycodestyle:

```
pip install pytest pycodestyle
```

3. Run the application:

```
python3 contact_man_sys.py
```

4. Run tests:

```
pytest contact_man_sys.py 
pytest test_contactMngSys.py
```

### Usage
Once you run the application, you will be presented with a menu of options:

```
Contact Management System
1. Add Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Exit
```

# Author
* [Wise D. Duho](https://github.com/Wise-deldu)
* Contact: delduwise@gmail.com
