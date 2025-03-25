from os import *
from ioStuff import *
from client import * 
from dbStuff import Database

class Menu:
  def __init__(self):
    self.breadcrumb = ""
    self.pageName = ""
    self.minMenuVal = 0
    self.maxMenuVal = 0
    self.menuOptions = []

  def displayPage(self):
    clearScreen()
    print(self.pageName)
    print("---------------------------")
    for option in self.menuOptions:
      print(option)
    print("")

  #======================================

  def displayDashboard(self):
    self.pageName = "Dashboard"
    self.breadcrumb = ">"
    self.minMenuVal = 1
    self.maxMenuVal = 5
    self.menuOptions.clear()
    self.menuOptions.append("1. properties")
    self.menuOptions.append("2. clients")
    self.menuOptions.append("3. Messages")
    self.menuOptions.append("4. Reports")
    self.menuOptions.append("5. Staff availabilty")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.properties()
    elif choice == 2:
      self.clients()
      
    def displayClients(self):
      self.pagename = "Clients:"
      self.breadcrumb = "Dashboard / Clients>"
      self.minMenuVal = 1
      self.maxMenuVal = 2
      self.menuOptions.clear()
      self.menuOptions.append("1. Display clients")
      self.menuOptions.append("2. Back")
      self.displayPage()
      choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
      if choice == 1:
        self.displayClients()
      elif choice == 2:
        self.displayDashboard()
    
    def editClient(self):
      self.pageName = "Edit a client"
      self.breadcrumb = "Dashboard / Edit a client>"
      self.minMenuVal = 1
      self.maxMenuVal = 2
      
  #======================================

  def properties(self):
    self.pageName = "Display properties"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()    
    self.menuOptions.append("1. New properties")
    self.menuOptions.append("2. Display properties (day view)")
    self.menuOptions.append("3. Display properties (week view)")
    self.menuOptions.append("4. Back")  
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.newproperties()
    elif choice == 2:
      self.displayDayViewproperties()
    elif choice == 3:
      self.displayWeekViewproperties()
    elif choice == 4:
      self.displayDashboard()

  def newproperties(self):
    self.pageName = "New properties"
    self.breadcrumb = "Dashboard / New properties>"
    self.minMenuVal = 1
    self.maxMenuVal = 2
    
  #======================================

  def clients(self):
    self.pageName = "clients"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()    
    self.menuOptions.append("1. New client")
    self.menuOptions.append("2. Remove client")
    self.menuOptions.append("3. Display clients")
    self.menuOptions.append("4. Back")  
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    def client():
      return 0
    if choice == 1:
      tmpNewclient = client()
      self.newclient(tmpNewclient)
    elif choice == 2:
      self.removeclient
    elif choice == 3:
      self.displayClients()
    elif choice == 4:
      self.displayDashboard()


  
  def newclient(self, tmpNewclient):
    self.firstName = ""
    self.lastName = ""
    self.dob = ""
    
    
    self.pageName = "New client"
    self.breadcrumb = "Dashboard / New client>"
    self.minMenuVal = 1
    self.maxMenuVal = 9
    self.menuOptions.clear()
    self.menuOptions.append("1. First name: " + self.firstName)
    self.menuOptions.append("2. Last name: " + self.lastName)
    self.menuOptions.append("3. Date of birth: " + self.dob)
    self.menuOptions.append("8. Submit new client to database")
    self.menuOptions.append("9. Back")
    self.displayPage()
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    
    if choice == 1:
      choice = getString("First name: ", minLen=1, maxLen=20)
      self.firstName = choice
      self.newclient(tmpNewclient)
      
    elif choice == 2:
      choice = getString("Last name: ", minLen=1, maxLen=20)
      self.lastName = choice
      self.newclient(tmpNewclient)
  
    elif choice == 3:
      choice = getDate("Date of birth (dd/mm/yyyy): ", minLen=1, maxLen=10)
      self.dob = choice
      self.newclient(tmpNewclient)

    elif choice == 4:
      choice = getGender("Gender: (m/f)")
      self.gender = choice
      self.newclient(tmpNewclient)

    elif choice == 5:
      choice = getString("Address", 1, 50)
      self.address = choice
      self.newclient(tmpNewclient)

    elif choice == 6:
      choice = getPhoneNumber("Phone number:")
      self.phone = choice
      self.newclient(tmpNewclient)

    elif choice == 7:
      choice = getEmail("eMail:")
      self.email = choice
      self.newclient(tmpNewclient)

    elif choice == 8:
      if getYesNo("Are you sure you want to submit this client?") == "y":
        Database.addClientToDB(self, self.firstName, self.lastName, self.dob)
        self.displayDashboard()
      else:
        self.newclient(tmpNewclient)
      
    elif choice == 9:
      self.displayDashboard()
      

  def displayproperties(self):
    self.pageName = "Displayproperties"
    self.breadcrumb = "Dashboard>"
    self.minMenuVal = 1
    self.maxMenuVal = 4
    self.menuOptions.clear()
    self.menuOptions.append("1. Display properties (day view)")
    self.menuOptions.append("2. Display properties (week view)")
    self.menuOptions.append("3. Back")
    self.displayPage()
    
    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.displayDayViewproperties()
    elif choice == 2:
      self.displayWeekViewproperties()
    elif choice == 3:
      self.displayDashboard()

  def displayDayViewproperties(self):
    self.pageName = "Display properties (day view)"
    self.breadcrumb = "Dashboard / Display properties (day view)>"
    self.minMenuVal = 1
    self.maxMenuVal = 2

    self.menuOptions.clear()
    self.menuOptions.append("1. Display properties for today")
    self.menuOptions.append("2. Back")
    self.displayPage()

    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.displayDayViewproperties()
    elif choice == 2:
      self.displayDashboard()

  def displayWeekViewproperties(self):
    self.pageName = "Display properties (week view)"
    self.breadcrumb = "Dashboard / Display properties (week view)>"
    self.minMenuVal = 1
    self.maxMenuVal = 2

    self.menuOptions.clear()
    self.menuOptions.append("1. Display properties for this week")
    self.menuOptions.append("2. Back")
    self.displayPage()

    choice = getNumber(self.breadcrumb, self.minMenuVal, self.maxMenuVal)
    if choice == 1:
      self.displayWeekViewproperties()
    elif choice == 2:
      self.displayDashboard()
