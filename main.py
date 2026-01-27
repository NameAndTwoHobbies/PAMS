import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from uiMainWindow import Ui_MainWindow
from db import *
from ErrorBoxes import *


class mainScreen(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PAMS")


        #Default Values
        self.stackedView.setCurrentIndex(0)


        #Menu Bar




        #Welcome Page

        self.Welcome.loginCustomerBtn.clicked.connect(lambda : self.switchCustomerLoginPage())
        self.Welcome.loginAdminBtn.clicked.connect(lambda : self.switchAdminLoginPage())

        #Customer Page

        self.CustLogin.loginBtn.clicked.connect(lambda : self.switchCustomerView())
        self.AdminLogin.loginBtn.clicked.connect(lambda : self.switchAdminView())

        self.CustLogin.signUpBtn.clicked.connect(lambda : self.switchCustomerSignUp())
        self.CustSignUp.submitBtn.clicked.connect(lambda : self.SignUpUser(self.CustSignUp.emailInput.toPlainText()))



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

    def switchCustomerSignUpDetailed(self, email :str):
        self.stackedView.setCurrentIndex(5)

    def SignUpUser(self, email : str):
        print(email)
        error = CheckEmailIsValid(email)
        if error is not None:
            #Must be set to self to allow for this box to be made
            self.errorBox = ErrorBox(error)
            self.errorBox.show()
        else: 
            ## TODO Add a Detailed signup page with the email from this function already being entered
            #self.switchCustomerSignUpDetailed(email)
            pass



    def buttonTestTenant(self):
        TestTenant()


#region App
app = QApplication()

#Creates a main window and places the ui created in designer onto it 
mainWindow = mainScreen()

mainWindow.show()

app.exec()

#endregion


