import json
import os


class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
        self.next_index = max(map(int, self.contacts.keys()), default=0) + 1

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}
    
    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        self.contacts[str(self.next_index)] = {"name": name, "phone": phone, "email": email}
        print(f"Contact '{name}' added successfully with index {self.next_index}.")
        self.next_index += 1

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, info in self.contacts.items():
                print(f"Index: {index}")
                print(f"Name: {info['name']}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print("=" * 30)

    def edit_contact(self):
        index = input("Enter the index of the contact to edit: ")
        if index in self.contacts:
            print(f"Editing contact: {self.contacts[index]['name']}")
            name = input("Enter new name (press Enter to keep current): ")
            phone = input("Enter new phone number (press Enter to keep current): ")
            email = input("Enter new email address (press Enter to keep current): ")
            if name:
                self.contacts[index]["name"] = name
            if phone:
                self.contacts[index]["phone"] = phone
            if email:
                self.contacts[index]["email"] = email
            print(f"Contact with index {index} updated successfully.")
        else:
            print(f"Contact with index {index} not found.")

    def delete_contact(self):
        index = input("Enter the index of the contact to delete: ")
        if index in self.contacts:
            name = self.contacts[index]["name"]
            del self.contacts[index]
            print(f"Contact '{name}' with index {index} deleted successfully.")
        else:
            print(f"Contact with index {index} not found.")

    def run(self):
        while True:
            print("\nContact Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.edit_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.save_contacts()
                print("Contacts saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    manager = ContactManager()
    manager.run()

if __name__ == "__main__":
    main()
