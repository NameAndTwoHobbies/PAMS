import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from uiMainWindow import Ui_MainWindow
from db import *
from ErrorBoxes import *
from MyWidgets import Table

class mainScreen(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PAMS")


        #self.switchTestingPage()



        #Welcome Page

        self.Welcome.loginCustomerBtn.clicked.connect(lambda : self.switchCustomerLoginPage())
        self.Welcome.loginAdminBtn.clicked.connect(lambda : self.switchAdminLoginPage())

        #Customer Page

        self.CustLogin.loginBtn.clicked.connect(lambda : self.switchCustomerView())
        self.AdminLogin.loginBtn.clicked.connect(lambda : self.switchAdminView())

        self.CustLogin.signUpBtn.clicked.connect(lambda : self.switchCustomerSignUp())
        self.CustSignUp.submitBtn.clicked.connect(lambda : self.SignUpUser(self.CustSignUp.emailInput.toPlainText()))

        #Testing Page
        self.TestingPage.testBtn1.clicked.connect(lambda : self.getTenantsTable())
        self.TestingPage.testBtn2.clicked.connect(lambda : self.getLocationsTable())
        #self.TestingPage.testBtn3.clicked.connect(lambda : )
        #self.TestingPage.testBtn4.clicked.connect(lambda : )


    #region Page Switching Functions
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
        self.switchWelcomePage()
    
    def switchCustomerSignUp(self):
        self.stackedView.setCurrentIndex(4)


    def switchTestingPage(self):
        self.stackedView.setCurrentIndex(5)
    
    def switchCustomerSignUpDetailed(self, email : str):
        self.stackedView.setCurrentIndex(6)
        self.DetailedSignUp.emailInput.setText(email)
    
    #endregion

    def SignUpUser(self, email : str):
        error = CheckEmailIsValid(email)
        if error is not None:
            #Must be set to self to allow for this box to be made
            self.errorBox = ErrorBox(error)
            self.errorBox.show()
        else: 
            #Changes the page to the detailed sign up
            self.switchCustomerSignUpDetailed(email)


    def getTenantsTable(self):
        records = GetTenants()
        headers = GetHeaders("tenants")
        self.table = Table(records,headers)
        self.table.show()

    def getLocationsTable(self):
        records = GetLocations()
        headers = GetHeaders("locations")
        self.table = Table(records,headers)
        self.table.show()


#region App
app = QApplication()

#Creates a main window and places the ui created in designer onto it 
mainWindow = mainScreen()

mainWindow.show()

app.exec()

#endregion


