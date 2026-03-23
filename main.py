import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from uiMainWindow import Ui_MainWindow
from db import *
from ErrorBoxes import *
from MyWidgets import *
from Entities import Tenant
from Table import Table

class mainScreen(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PAMS")
        self.setMaximumSize(self.size())
    #region Testing Section
    #This section is used test functionality, quick testing and debugging. 
        self.LoginTenantBTN("peter@gmail.com", "")
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

        #Customer login page
        self.CustLogin.loginBtn.clicked.connect(lambda : self.LoginTenantBTN(self.CustLogin.emailInput.toPlainText(),self.CustLogin.passwordInput.toPlainText()))

        self.CustLogin.signUpBtn.clicked.connect(lambda : self.switchCustomerSignUp())
        self.CustSignUp.submitBtn.clicked.connect(lambda : self.SignUpUser(self.CustSignUp.emailInput.toPlainText()))

        #Staff LoginPage
        self.StaffLogin.loginBtn.clicked.connect(lambda : self.loginStaffMember(self.StaffLogin.emailInput.toPlainText(), self.StaffLogin.passwordInput.toPlainText()))

        #Front Desk Page
        self.FrontDeskDash.submitButton.clicked.connect(lambda : self.RegisterTenant(self.FrontDeskDash.Submit()))
        #endregion

        #Admin Dashboard
        self.AdminDash.userLocationDropdown.currentIndexChanged.connect(lambda : self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),[], []))
        self.AdminDash.userRefreshBtn.clicked.connect(lambda : self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),[], []))
        self.AdminDash.apartmentLocationDropdown.currentIndexChanged.connect(lambda : self.AdminDash.CreateApartmentTable(GetApartmentsFromLocation(GetLocation(self.AdminDash.apartmentLocationDropdown.currentText()).GetID()), GetHeaders("apartments")))
        self.AdminDash.apartmentRefresh.clicked.connect(lambda : self.AdminDash.CreateApartmentTable(GetApartmentsFromLocation(GetLocation(self.AdminDash.apartmentLocationDropdown.currentText()).GetID()), GetHeaders("apartments")))
        self.AdminDash.reportLocationDropdown.currentIndexChanged.connect(lambda : [self.AdminDash.CreateOccupancyLevels(self.MakePieChartUnoccupied(self.AdminDash.reportLocationDropdown.currentText())), self.AdminDash.CreateMaintenance(self.MakeMaintanenceRequestsPieChart(self.AdminDash.reportLocationDropdown.currentText()))]) #TODO Create a function that updates both graphs at the same time
        
        #Sign Up Customer Page
        self.DetailedSignUp.submitBtn.clicked.connect(lambda : SignUpTenant(Tenant("", self.DetailedSignUp.firstNameInput.text(),self.DetailedSignUp.lastNameInput.text(),self.DetailedSignUp.nationalNumInput.text(),self.DetailedSignUp.emailInput.text(),self.DetailedSignUp.passwordInput.text(),self.DetailedSignUp.phoneNumInput.text(),self.DetailedSignUp.occupationComboBox.currentText(),"")))
        self.DetailedSignUp.submitBtn.clicked.connect(lambda : self.switchCustomerView(Tenant("", self.DetailedSignUp.firstNameInput.text(),self.DetailedSignUp.lastNameInput.text(),self.DetailedSignUp.nationalNumInput.text(),self.DetailedSignUp.emailInput.text(),self.DetailedSignUp.passwordInput.text(),self.DetailedSignUp.phoneNumInput.text(),self.DetailedSignUp.occupationComboBox.currentText(),"")))

        #Customer Page

        self.CustDash.OverviewPage.logoutBtn.clicked.connect(lambda : self.logoutTenant())
#region Page Functions
# This section is responsible for the functions that switch the pages and that load the data into these pages.
    def switchWelcomePage(self):
        self.stackedView.setCurrentIndex(0)
    
    def switchCustomerLoginPage(self):
        self.stackedView.setCurrentIndex(1)
    
    def switchAdminLoginPage(self):
        self.stackedView.setCurrentIndex(2)
    
    def switchCustomerSignUp(self):
        self.stackedView.setCurrentIndex(4)

    def switchCustomerSignUpDetailed(self, email : str):
        self.stackedView.setCurrentIndex(6)
        self.DetailedSignUp.emailInput.setText(email)
    
    def switchCustomerView(self, tenant : Tenant):
        #Change when page is implemented to customer dashboard
        self.stackedView.setCurrentIndex(3)
        self.CustDash.paymentsPage.paymentHistory.UpdateTable(GetTenantPaymentHistory(tenant.GetID()), GetHeaders("payments"))
        self.CustDash.setUser(tenant)

    
    def switchAdminView(self, admin : User):
        #Change when page is implemented to customer dashboard
        self.stackedView.setCurrentIndex(9)
        self.AdminDash.setUser(admin)
        self.setWindowTitle(admin.firstName)
        self.AdminDash.GetLocations(GetLocations())

        self.AdminDash.CreateOccupancyLevels(self.MakePieChartUnoccupied(self.AdminDash.apartmentLocationDropdown.currentText())) #TODO add a dropdown for the reports page for locations
        self.AdminDash.CreateMaintenance(self.MakeMaintanenceRequestsPieChart(self.AdminDash.apartmentLocationDropdown.currentText())) 
        self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),[], []) 
        self.AdminDash.CreateApartmentTable(GetApartmentsFromLocation(GetLocation(self.AdminDash.apartmentLocationDropdown.currentText()).GetID()), GetHeaders("apartments"))
    
    
    def switchFrontDeskDashboard(self , frontDesk: User):
        self.stackedView.setCurrentIndex(7)
        self.FrontDeskDash.setUser(frontDesk)
        self.setWindowTitle(frontDesk.firstName)
        self.FrontDeskDash.tenantTable.UpdateTable(GetTenants(), GetHeaders("tenants"))

    
    def switchToFinanceDashboard(self, finance : User):
        self.stackedView.setCurrentIndex(8)
        self.FinanceDash.setUser(finance)
        self.setWindowTitle(finance.firstName)
        self.FinanceDash.paymentTable.UpdateTable((),())
        self.FinanceDash.CreateOccupancyLevels(self.MakePieChartUnoccupied("London")) # Add specifc location for the user
        self.FinanceDash.CreateMaintenance(self.MakeMaintanenceRequestsPieChart("London")) # Add specifc location for the user

    def switchTestingPage(self):
        self.stackedView.setCurrentIndex(5)

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
            SignUpTenant(tenant)
            self.switchFrontDeskDashboard()

    def LoginTenantBTN(self, email: str, password : str):
        tenant = LoginTenant(email,password)

        if tenant is None:
            self.errorBox = ErrorBox(ErrorMessage("No User Found", "The credentials do not match any known user"))
            self.errorBox.show()
        else:
            self.CustLogin.retranslateUi() # removes  the values input into the page
            self.switchCustomerView(tenant)

    def loginStaffMember(self, email : str, password : str):
        staff = LoginUser(email,password)

        if staff is None:
            self.errorBox = ErrorBox(ErrorMessage("No User Found", "The credentials do not match any known user"))
            self.errorBox.show()
        else:
            self.StaffLogin.retranslateUi() #removes the values stored
            match(staff.role):
                case "FrontDesk":
                    self.switchFrontDeskDashboard(staff)
                case "Manager":
                    #Implement manager
                    self.switchWelcomePage()
                case "Finance":
                    self.switchToFinanceDashboard(staff)
                case "Maintenance":
                    self.switchWelcomePage()
                case "Admin":
                    self.switchAdminView(staff)
                
                case _: 
                    self.errorBox = ErrorBox(ErrorMessage("Role Error", "Something went wrong, please contact your administrator"))
                    self.errorBox.show()
    def logoutTenant(self):
        self.CustDash.setUser(Tenant("","","", "", "", "", "", "",""))
        self.switchWelcomePage()


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