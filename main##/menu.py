from os import *
from ioStuff import *
from client import * 
from dbStuff import Database

class Menu:
    def __init__(self):
        self.db = Database("estates")

    def displayDashboard(self):
        while True:
            print("\nDashboard")
            print("---------------------------")
            print("1. Clients")
            print("2. Properties")
            print("3. Exit")
            
            choice = input("Select an option: ")
            
            if choice == "1":
                self.clientsMenu()
            elif choice == "2":
                self.propertiesMenu()
            elif choice == "3":
                break
            else:
                print("Invalid option")

    def clientsMenu(self):
        while True:
            print("\nClients")
            print("---------------------------")
            print("1. New client")
            print("2. Remove client")
            print("3. Display clients")
            print("4. Back")
            
            choice = input("Select an option: ")
            
            if choice == "1":
                self.addNewClient()
            elif choice == "2":
                self.removeClient()
            elif choice == "3":
                self.db.displayClients()
            elif choice == "4":
                break
            else:
                print("Invalid option")

    def addNewClient(self):
        print("\nAdd New Client")
        username = input("Enter username: ")
        name = input("Enter full name: ")
        
        if self.db.addClient(username, name):
            print("Client added successfully")
        else:
            print("Failed to add client. Username might already exist.")

    def removeClient(self):
        username = input("\nEnter username to remove: ")
        if self.db.deleteClient(username):
            print("Client removed successfully")
        else:
            print("Failed to remove client")
