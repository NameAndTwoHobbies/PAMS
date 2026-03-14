import sys
import random
from wsgiref import headers
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from uiMainWindow import Ui_MainWindow
from db import *
from ErrorBoxes import *
from MyWidgets import *
from Entities import Tenant

class mainScreen(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PAMS")
        self.setMaximumSize(self.size())
    #region Testing Section
    #This section is used test functionality, quick testing and debugging. 

        #Testing Page
        self.TestingPage.testBtn1.clicked.connect(lambda : self.MakePieChartUnoccupied("Madrid"))
        self.TestingPage.testBtn2.clicked.connect(lambda : self.MakePieChartUnoccupied("London"))
        self.TestingPage.testBtn3.clicked.connect(lambda : self.MakeMaintanenceRequestsPieChart("London"))
        #self.TestingPage.testBtn4.clicked.connect(lambda : )

    #endregion

#region Connecting Interactivity 
# This region is responsible for connecting the buttons to the front end to the functionailty in the back end.
        #Welcome Page

        self.Welcome.loginCustomerBtn.clicked.connect(lambda : self.switchCustomerLoginPage())
        self.Welcome.loginAdminBtn.clicked.connect(lambda : self.switchAdminLoginPage())

        #Customer Page

        self.CustLogin.loginBtn.clicked.connect(lambda : self.LoginTenantBTN(self.CustLogin.emailInput.toPlainText(),self.CustLogin.passwordInput.toPlainText()))
        self.AdminLogin.loginBtn.clicked.connect(lambda : self.switchToFinanceDashboard())

        self.CustLogin.signUpBtn.clicked.connect(lambda : self.switchCustomerSignUp())
        self.CustSignUp.submitBtn.clicked.connect(lambda : self.SignUpUser(self.CustSignUp.emailInput.toPlainText()))

        

        #Front Desk Page
        self.FrontDeskDash.submitButton.clicked.connect(lambda : self.RegisterTenant(self.FrontDeskDash.Submit()))
        #endregion

        #Admin Dashboard
        #self.AdminDash.userLocationDropdown.currentIndexChanged.connect(lambda : self.AdminDash.userTable.UpdateTable(GetTenants(),GetHeaders("tenants")))
        self.AdminDash.userRefreshBtn.clicked.connect(lambda : self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),[], []))
#region Page Functions
# This section is responsible for the functions that switch the pages and that load the data into these pages.
    def switchWelcomePage(self):
        self.stackedView.setCurrentIndex(0)
    
    def switchCustomerLoginPage(self):
        self.stackedView.setCurrentIndex(1)
    
    def switchAdminLoginPage(self):
        self.stackedView.setCurrentIndex(2)
    
    def switchCustomerView(self):
        #Change when page is implemented to customer dashboard
        self.stackedView.setCurrentIndex(3)

    def switchAdminView(self):
        #Change when page is implemented to customer dashboard
        self.stackedView.setCurrentIndex(9)
        self.AdminDash.GetLocations(GetLocations())
        #TODO make a table thart changes due to location
        #TODO add a dropdown for the reports page for locations
        self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),[], [])    
    def switchCustomerSignUp(self):
        self.stackedView.setCurrentIndex(4)


    def switchTestingPage(self):
        self.stackedView.setCurrentIndex(5)
    
    def switchCustomerSignUpDetailed(self, email : str):
        self.stackedView.setCurrentIndex(6)
        self.DetailedSignUp.emailInput.setText(email)
    
    def switchFrontDeskDashboard(self):
        self.stackedView.setCurrentIndex(7)
        self.FrontDeskDash.tenantTable.UpdateTable(GetTenants(), GetHeaders("tenants"))
        self.FrontDeskDash.searchBar.textChanged.connect(lambda : self.FrontDeskDash.tenantTable.search(self.FrontDeskDash.searchBar.text()))
    def switchToFinanceDashboard(self):
        self.stackedView.setCurrentIndex(8)
        self.FinanceDash.paymentTable.UpdateTable()
        self.FinanceDash.CreateOccupancyLevels(self.MakePieChartUnoccupied("London")) # Add specifc location for the user
        self.FinanceDash.CreateMaintenance(self.MakeMaintanenceRequestsPieChart("London")) # Add specifc location for the user
#endregion

#region Interaction Functions
# This section is responsible for the functions that implement the database interactions and interactivity with the data
    
    # Checks if the email is valid by checking if it already exists in the database
    # It will produce a popup error if the email is already registered.
    # If the email is valid it switches to the detailed sign up page and inputs the email into the email box
    def SignUpUser(self, email : str):
        if CheckEmailIsValid(email) == False:
            #Must be set to self to allow for this box to be made
            title = "Tenant Already Exists"
            description = "This email has already been used to sign up a user. Please try a different email."
            error = ErrorMessage(title, description)
            self.errorBox = ErrorBox(error)
            self.errorBox.show()
        else: 
            #Changes the page to the detailed sign up
            self.switchCustomerSignUpDetailed(email)

    # Creates a new tenant and prepares the data to be inputed into the database.
    # If the credentials are already in use it will produce a popup error box.
    # If the credentials are valid it will input the data into the database and refresh the page
    def RegisterTenant(self, tenant : Tenant):
        if CheckEmailIsValid(tenant.email) == False:
            title = "Tenant Already Exists"
            description = "This email has already been used to sign up a user. Please try a different email."
            error = ErrorMessage(title, description)
            self.errorBox = ErrorBox(error)
            self.errorBox.show()
        else: 
            SignUpUser(tenant)
            self.switchFrontDeskDashboard()

    # Not functioning 
    def LoginTenantBTN(self, email: str, password : str):
        user = LoginUser(email,password)

        if user is None:
            self.errorBox = ErrorBox(ErrorMessage("No User Found", "The credentials do not match any known user"))
            self.errorBox.show()

    # Returns a table with all tenants in the database
    def getTenantsTable(self):
        records = GetTenants()
        headers = GetHeaders("tenants")
        return Table(records,headers)

    # Returns a table with all locations in the database
    def getLocationsTable(self):
        records = GetLocations()
        headers = GetHeaders("locations")
        self.table = Table(records,headers)
        self.table.show()
    
    
    # Creates a pie chart showing the Occupancy levels in a location. Right now it produces a piechart on a new page.
    def MakePieChartUnoccupied(self, locationName : str):
        location = GetLocation(locationName)
        if location is None:
            self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
            self.error.show() #Change to ann error manager
        else:
            apartments = GetApartmentsFromLocation(location.id)
            if apartments != None:
                total = len(apartments)
                unoccupied = GetUnoccupiedApartmentsForLocation(location.id)
                if unoccupied is None:
                    self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
                    self.error.show() #Change to ann error manager
                else:
                    unoccupied = len(unoccupied)
                    pie = PieChart(("Occupied","Unoccupied") , (total - unoccupied, unoccupied) , "Occupied vs Unoccupied of " + locationName)
                    return pie
        print("Done")
    # Creates a pie chart that shows the number of maintanence requests in a given location compared to the apartments that are functional.
    def MakeMaintanenceRequestsPieChart(self, locationName : str):
        location = GetLocation(locationName)
        if location is None:
            self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
            self.error.show() #Change to ann error manager
        else:
            requests = GetMainanenceRequestsForLocation(location.id)
            apartments = GetApartmentsFromLocation(location.id)
            print(len(requests))
            print(len(apartments))
            pie = PieChart(labels= ("Repairs In Progress", "Functional"),numData= ((len(requests)), len(apartments) - len(requests)) ,title= "Repairs in progress vs functional rooms")
            return pie
        print("Done")
#endregion

#region App

app = QApplication()

#Creates a main window and places the ui created in designer onto it 
mainWindow = mainScreen()

mainWindow.show()

app.exec()

#endregion




#TODO Have a look over and see if you can swap around how the mainwindow works its a tad inconsisitent