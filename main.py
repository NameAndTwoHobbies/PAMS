from PySide6.QtWidgets import * #the asterisks mean import everything
from PySide6.QtGui import *
from PySide6.QtCore import * 
from components.uiMainWindow import Ui_MainWindow
from database.db import *
from components.ErrorBoxes import *
from components.MyWidgets import *
from models.Entities import *
from repositories import *

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
        self.TestingPage.testBtn3.clicked.connect(lambda : self.MakeMaintenanceRequestsPieChart("London"))
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
        self.FrontDeskDash.manageTenants.submitButton.clicked.connect(lambda : self.RegisterTenant(self.FrontDeskDash.manageTenants.Submit()))
        #endregion

        #Admin Dashboard
        self.AdminDash.userLocationDropdown.currentIndexChanged.connect(lambda : self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),GetTenantsFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("tenants")))
        self.AdminDash.userRefreshBtn.clicked.connect(lambda : self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),GetTenantsFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("tenants")))
        self.AdminDash.apartmentLocationDropdown.currentIndexChanged.connect(lambda : self.AdminDash.CreateApartmentTable(GetApartmentsFromLocation(GetLocation(self.AdminDash.apartmentLocationDropdown.currentText()).GetID()), GetHeaders("apartments")))
        self.AdminDash.apartmentRefresh.clicked.connect(lambda : self.AdminDash.CreateApartmentTable(GetApartmentsFromLocation(GetLocation(self.AdminDash.apartmentLocationDropdown.currentText()).GetID()), GetHeaders("apartments")))
        self.AdminDash.ReportPage.reportLocationDropdown.currentIndexChanged.connect(lambda : self.AdminDash.ReportPage.CreatePieCharts(self.MakePieChartUnoccupied(self.AdminDash.ReportPage.reportLocationDropdown.currentText()),self.MakePieChartPaymentInsights(self.AdminDash.ReportPage.reportLocationDropdown.currentText()),self.MakeMaintenanceRequestsPieChart(self.AdminDash.ReportPage.reportLocationDropdown.currentText())))
        
        #Sign Up Customer Page
        self.DetailedSignUp.submitBtn.clicked.connect(lambda : SignUpTenant(Tenant("", self.DetailedSignUp.firstNameInput.text(),self.DetailedSignUp.lastNameInput.text(),self.DetailedSignUp.nationalNumInput.text(),self.DetailedSignUp.emailInput.text(),self.DetailedSignUp.passwordInput.text(),self.DetailedSignUp.phoneNumInput.text(),self.DetailedSignUp.occupationComboBox.currentText(),"")))
        self.DetailedSignUp.submitBtn.clicked.connect(lambda : self.switchCustomerView(Tenant("", self.DetailedSignUp.firstNameInput.text(),self.DetailedSignUp.lastNameInput.text(),self.DetailedSignUp.nationalNumInput.text(),self.DetailedSignUp.emailInput.text(),self.DetailedSignUp.passwordInput.text(),self.DetailedSignUp.phoneNumInput.text(),self.DetailedSignUp.occupationComboBox.currentText(),"")))

        #Customer Page
        self.CustDash.OverviewPage.logoutBtn.clicked.connect(lambda : self.logoutTenant())
        self.CustDash.PaymentsPage.payNowBtn.clicked.connect(lambda : self.Pay(self.CustDash.contract))
        self.CustDash.AccountPage.submitReqsBtn.clicked.connect(lambda : self.CreateTenantRequirement(self.CustDash.AccountPage.locationComboBox.currentText(),self.CustDash.tenant.GetID(),self.CustDash.AccountPage.SubmitRequirements()))
        self.CustDash.AccountPage.submitBtn.clicked.connect(lambda : self.UpdateTenant(self.CustDash.tenant, self.CustDash.SubmitUserInfo()))
        self.CustDash.OverviewPage.leaveTenancyBtn.clicked.connect(lambda : self.LeaveTenancyEarly())

        #Maintenance rquest Page
        self.CustDash.MaintenanceReq.submitBtn.clicked.connect(lambda: self.SubmitMaintenanceRequest())
        self.CustDash.MaintenanceReq.backBtn.clicked.connect(lambda: self.switchCustomerView()) #DONT worry
        #endregion

        #Manager Page
        self.ManagerDash.LocationPage.locationCreateBtn.clicked.connect(lambda : self.CreateLocation(self.ManagerDash.LocationPage.SubmitLocation()))
        self.ManagerDash.LocationPage.managerCreationBtn.clicked.connect(lambda : self.CreateLocationManager(self.ManagerDash.LocationPage.SubmitLocationManager(), self.ManagerDash.LocationPage.managerLocationComboBox.currentText()))
        
        self.ManagerDash.ApartmentPage.apartmentCreateBtn.clicked.connect(lambda  : self.CreateApartments(self.ManagerDash.ApartmentPage.Submit() , self.ManagerDash.ApartmentPage.locationComboBox.currentText()))
        self.ManagerDash.ReportPage.reportLocationDropdown.currentIndexChanged.connect(lambda : self.ManagerDash.ReportPage.CreatePieCharts(self.MakePieChartUnoccupied(self.ManagerDash.ReportPage.reportLocationDropdown.currentText()) , self.MakePieChartPaymentInsights(self.ManagerDash.ReportPage.reportLocationDropdown.currentText()), self.MakeMaintanenceRequestsPieChart(self.ManagerDash.ReportPage.reportLocationDropdown.currentText())))

        #Finance Page
        self.FinanceDash.refreshBtn.clicked.connect(lambda: self.FinanceDash.paymentTable.UpdateTable(GetAllPaymentsFromLocation(self.FinanceDash.user.location_id), GetHeaders("payments")))
        self.FinanceDash.issueRentBtn.clicked.connect(lambda : IssueRentPayments(self.FinanceDash.user.location_id))
        self.FinanceDash.submitInvoiceBtn.clicked.connect(lambda: self.CreateInvoice(self.FinanceDash.SubmitInvoice()))

        #Maintenance Page


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
        self.stackedView.setCurrentWidget(self.CustDash)
        contract = GetContract(tenant.GetID())
        if contract is None:
            self.CustDash.setUser(tenant , Contract("","","","","","",""), Apartment("","","","","","",True))
            self.CustDash.switchToAccountPage()
            self.CustDash.accountBtn.setEnabled(False)
            self.CustDash.overviewBtn.setEnabled(False)
            self.CustDash.paymentsBtn.setEnabled(False)
            self.CustDash.maintenanceBtn.setEnabled(False)
            self.CustDash.notifcationsBtn.setEnabled(False)
            self.CustDash.AddPageDetail(GetLocations(),[],"")
        else: 
            apartment = GetApartment(contract.apartment_id)
            self.CustDash.setUser(tenant,contract,apartment)
            print(apartment.GetDataBaseFormat())
            self.CustDash.notificationsPage.setTenant(tenant, apartment.location_id)
            paymentHistory = GetTenantPaymentHistory(tenant.GetID())
            totalToPay = 0
            for payment in paymentHistory:
                if payment.payment_status == 'Unpaid':
                    totalToPay = totalToPay + payment.amount_paid
                self.CustDash.PaymentsPage.CurrentDue.setText("£" + str(totalToPay))

            self.CustDash.PaymentsPage.paymentHistory.UpdateTable(paymentHistory, GetHeaders("payments"))
            date = QDate.currentDate()
            dueDate = QDate(date.year(), date.month(),date.daysInMonth())
            self.CustDash.AddPageDetail(GetLocations(),[],dueDate.toString())
    
    def switchAdminView(self, admin : User):
        #Change when page is implemented to customer dashboard
        self.stackedView.setCurrentIndex(9)
        self.AdminDash.setUser(admin)
        self.setWindowTitle(admin.firstName)
        self.AdminDash.GetLocations(GetLocations())
        self.AdminDash.ReportPage.CreatePieCharts(self.MakePieChartUnoccupied(self.AdminDash.ReportPage.reportLocationDropdown.currentText()),self.MakePieChartPaymentInsights(self.AdminDash.ReportPage.reportLocationDropdown.currentText()),self.MakeMaintenanceRequestsPieChart(self.AdminDash.ReportPage.reportLocationDropdown.currentText()))
        self.AdminDash.CreateUserTable(GetUsersFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("users"),GetTenantsFromLocation(self.AdminDash.userLocationDropdown.currentText()),GetHeaders("tenants")) 
        self.AdminDash.CreateApartmentTable(GetApartmentsFromLocation(GetLocation(self.AdminDash.apartmentLocationDropdown.currentText()).GetID()), GetHeaders("apartments"))
    
    
    def switchFrontDeskDashboard(self , frontDesk: User):
        self.FrontDeskDash.setUser(frontDesk)
        self.stackedView.setCurrentWidget(self.FrontDeskDash)
        self.setWindowTitle(frontDesk.firstName)
    
    def switchToFinanceDashboard(self, finance : User):
        self.stackedView.setCurrentIndex(8)
        self.FinanceDash.setUser(finance)
        self.setWindowTitle(finance.firstName)
        print(GetHeaders("payments"))
        self.FinanceDash.paymentTable.UpdateTable(GetAllPaymentsFromLocation(self.FinanceDash.user.location_id), GetHeaders("payments"))
        self.FinanceDash.ReportPage.CreatePieCharts(self.MakePieChartUnoccupied(GetLocationFromID(finance.location_id).location_name), self.MakePieChartPaymentInsights(GetLocationFromID(finance.location_id).location_name),self.MakeMaintenanceRequestsPieChart(GetLocationFromID(finance.location_id).location_name) )
        
    def switchToManagerDashboard(self, manager : User):
        self.ManagerDash.setUser(manager)
        self.ManagerDash.GetLocations(GetLocations())
        self.ManagerDash.ReportPage.CreatePieCharts(self.MakePieChartUnoccupied(GetLocationFromID(manager.location_id).location_name),self.MakePieChartPaymentInsights(GetLocationFromID(manager.location_id).location_name), self.MakeMaintenanceRequestsPieChart(GetLocationFromID(manager.location_id).location_name))
        self.stackedView.setCurrentIndex(10)
  
    def switchTestingPage(self):
        self.stackedView.setCurrentIndex(5)

    def switchMaintenancePage(self, maintenance :User):
        self.stackedView.setCurrentIndex(11)


        requests = GetMaintenanceRequestsForMaintenanceTeam(maintenance)
        headers  = ["request_id", "scheduled_start", "description" ,"maintenance_notes", "priority" ,"cost" , "Details"]
        self.MaintenanceDash.table.clear()
        lenHeader = len(headers)
        lenRecords = len(requests)
        self.MaintenanceDash.table.setColumnCount(lenHeader)
        self.MaintenanceDash.table.setRowCount(lenRecords)
        self.MaintenanceDash.table.verticalHeader().setVisible(False)
        for header in range(0,lenHeader):
            self.MaintenanceDash.table.setHorizontalHeaderItem(header,QTableWidgetItem(str(headers[header])))
        
        # Converts the database format of the records into table
        for x in range(len(requests)):
            record = requests[x]
            for y in range(0,len(record)):
                self.MaintenanceDash.table.setItem(x,y,QTableWidgetItem(str(record[y])))
        

        self.MaintenanceDash.setUser(maintenance)

        self.MaintenanceDash.table.selectColumn(self.MaintenanceDash.table.columnCount()-1)

        for column in self.MaintenanceDash.table.selectedItems():
            btn = QPushButton("Details")
            index = column.row()
            btn.clicked.connect(lambda : self.MaintenanceDash.CreateDialogBox(self.MaintenanceDash.table.item(index,1),self.MaintenanceDash.table.item(index,3),self.MaintenanceDash.table.item(index,5)))
            self.MaintenanceDash.table.setCellWidget(column.row(),column.column(),btn)



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
            self.switchFrontDeskDashboard(frontDesk=self.FrontDeskDash.user)

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
                    self.switchToManagerDashboard(staff)
                case "Finance":
                    self.switchToFinanceDashboard(staff)
                case "Maintenance":
                    self.switchMaintenancePage(staff)
                case "Admin":
                    self.switchAdminView(staff)
                
                case _: 
                    self.errorBox = ErrorBox(ErrorMessage("Role Error", "Something went wrong, please contact your administrator"))
                    self.errorBox.show()
    def logoutTenant(self):
        self.CustDash.clearUser()
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
                unoccupied : list[Apartment] = []
                for apartment in apartments:
                    if apartment.occupancy_status == False:
                        unoccupied.append(apartment)
                if unoccupied is None:
                    self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
                    self.error.show() #Change to ann error manager
                else:
                    unoccupied = len(unoccupied)
                    pie = PieChart(("Occupied","Unoccupied") , (total - unoccupied, unoccupied) , "Occupied vs Unoccupied of " + locationName)
                    return pie
        print("Done")
    def MakePieChartPaymentInsights(self, locationName : str):
        location = GetLocation(locationName)
        if location is None:
            self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
            self.error.show() #Change to ann error manager
        else:
            payments = GetAllPaymentsFromLocation(location.id)
            if payments != None:
                total = len(payments)
                unpaid : list[Payment] = []
                for payment in payments:
                    if payment.payment_status == "Unpaid":
                        unpaid.append(payment)
                if unpaid is None:
                    self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
                    self.error.show() #Change to ann error manager
                else:
                    unpaid = len(unpaid)
                    pie = PieChart(("Paid","Outstanding") , (total - unpaid, unpaid) , "Paid vs Outstanding payments of " + locationName)
                    return pie
        print("Done")

    # Creates a pie chart that shows the number of maintanence requests in a given location compared to the apartments that are functional.
    def MakeMaintenanceRequestsPieChart(self, locationName : str):
        location = GetLocation(locationName)
        if location is None:
            self.error = ErrorBox(ErrorMessage("No Data", "There is no location by this name"))
            self.error.show() #Change to ann error manager
        else:
            requests = GetMaintenanceRequestsForLocation(location.id)
            apartments = GetApartmentsFromLocation(location.id)
            print(len(requests))
            print(len(apartments))
            pie = PieChart(labels= ("Repairs In Progress", "Functional"),numData= ((len(requests)), len(apartments) - len(requests)) ,title= "Repairs in progress vs functional rooms")
            return pie
        print("Done")

    def CreateLocation(self, newLocation : Location):
        location = GetLocation(newLocation.location_name)

        if location is not None:
            self.errorBox = ErrorBox(ErrorMessage("Location Already Exists", "A location already exists under this name"))
            self.errorBox.show()
        else:
            AddLocation(newLocation)
            self.ManagerDash.GetLocations(GetLocations())

    def CreateLocationManager(self, newManager : User, locationName : str):
        location = GetLocation(locationName) # Can only be the locations in the database as the combo box stores locations directly pulled from the database
        newManager.location_id = location.id
        added = AddStaff(newManager)
        if added != True:
            self.errorBox = ErrorBox(ErrorMessage("User Already Exists", "A User already exists under these credentials"))
            self.errorBox.show()

    def CreateApartments(self, apartments : list[Apartment] , locationName : str):
        location = GetLocation(locationName) # Can only be the locations in the database as the combo box stores locations directly pulled from the database


        if apartments == []:
            self.errorBox = ErrorBox(ErrorMessage("No Apartments To Add", "No Apartments have been created"))
            self.errorBox.show()
        else: 
            for apartment in apartments:
                apartment.location_id = location.id
                AddApartment(apartment)
    def CreateTenantRequirement(self,location_id,tenant_id: str, reqs : Requirements):
        reqs.tenant_id = tenant_id
        reqs.location_id =  GetLocation(location_id).GetID() # AT THAT time it is the name of the location
        print(reqs.GetDataBaseFormat())
        AddRequirements(reqs)
    def CreateInvoice(self, invoiceInfo :tuple[str,str,str,str]):
        contract = GetContract(invoiceInfo[0])
        if contract is None:
            self.errorBox = ErrorBox(ErrorMessage("Tenant Doesn't Exists", "No Tenants with this ID"))
            self.errorBox.show()
        else:
            CreateInvoice(Payment("", contract.id,'NULL',invoiceInfo[1],invoiceInfo[2],'Unpaid','DirectDebit', invoiceInfo[3]))

    def Pay(self, contract: Contract):
        MakePayment(self.CustDash.contract)
        self.switchCustomerView(self.CustDash.tenant)
    def UpdateTenant(self, currentTenant: Tenant, changeTenant: Tenant):
        changeTenant.references = currentTenant.references
        validTenant = True
        for field in changeTenant.GetDataBaseFormat():
            print(field)
            if field == "":
                validTenant = False
        if validTenant == True:
            if changeTenant.email != currentTenant.email:
                if CheckEmailIsValid(changeTenant.email):
                    changeTenant.id = currentTenant.id
                else:
                    self.errorBox = ErrorBox(ErrorMessage("Invalid Email", "This email is already in use please re-enter"))
                    self.errorBox.show()
            UpdateTenant(changeTenant)
            self.switchCustomerView(changeTenant)
        else:
            self.errorBox = ErrorBox(ErrorMessage("Invalid Tenant", "Please Re-enter"))
            self.errorBox.show()

    def SubmitMaintenanceRequest(self):
        request = self.CustDash.SubmitRequest()
        SubmitMaintenanceRequest(request.tenant_id, request.apartment_id,request.description,request.priority)

    def LeaveTenancyEarly(self):
        contract = self.CustDash.contract

    # Guard: if no contract is loaded yet, do nothing
        if not contract.id:
            ErrorBox("No active contract found.")
            return

    # Open the calendar dialog, passing the current contract so it
    # knows the end_date boundary
        dialog = EarlyLeaveDateDialog(contract, parent=self)

        if dialog.exec() == QDialog.DialogCode.Accepted:
            chosen_date = dialog.GetSelectedDate()          # "YYYY-MM-DD"
            UpdateContractEarlyLeave(contract.id, chosen_date)

        # Update the in-memory contract so the UI stays consistent
        # without needing a full re-login
            self.CustDash.contract.end_date = chosen_date
            self.CustDash.contract.early_leave = True

            QMessageBox.information(
                self,
                "Early Leave Confirmed",
                f"Your tenancy has been updated.\n"
                f"Your new move-out date is {chosen_date}."
            )

#endregion

#region App

app = QApplication()

#Creates a main window and places the ui created in designer onto it 
mainWindow = mainScreen()
mainWindow.show()

app.exec()

#endregion




#TODO Have a look over and see if you can swap around how the mainwindow works its a tad inconsisitent

#TODO MAKE CHECKS FOR ANY EMPTY ENTRIES
