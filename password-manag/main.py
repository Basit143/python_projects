# Import the necessary libraries:
import os
import random
import secrets
import json
import string

# Define a function to generate a random password

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Create a class to store password data

class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

# Define functions to add, view, and delete password entries

def add_entry(entries):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = generate_password()
    entries.append(PasswordEntry(website, username, password))
    print(f"Password for {website} generated: {password}")

def view_entries(entries):
    for entry in entries:
        print(f"Website: {entry.website}")
        print(f"Username: {entry.username}")
        print(f"Password: {entry.password}")

def delete_entry(entries):
    website = input("Enter website to delete: ")
    for i, entry in enumerate(entries):
        if entry.website == website:
            del entries[i]
            print(f"Entry for {website} deleted.")
            return
    print(f"Entry for {website} not found.")

# Load and save password data to a file

def load_data(filename="passwords.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save_data(entries, filename="passwords.json"):
    with open(filename, "w") as f:
        json.dump([entry.__dict__ for entry in entries], f)

def main():
    entries = load_data()

    while True:
        print("\nChoose an option:")
        print("1. Add new entry")
        print("2. View entries")
        print("3. Delete entry")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            delete_entry(entries)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

    save_data(entries)

if __name__ == "__main__":
    main()

