import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCharts import *
from ErrorBoxes import ErrorBox
from Entities import *
from Table import Table
from tenantPage import *

#region Fonts

text = QFont()
text.setFamilies([u"Arial"])
text.setPointSize(18)




title = QFont()
title.setFamilies([u"Arial"])
title.setPointSize(40)
title.setBold(True)

heading = QFont()
heading.setFamilies([u"Calibri"])
heading.setPointSize(22)
heading.setBold(True)

heading2 = QFont()
heading2.setFamilies([u"Calibri"])
heading2.setPointSize(18)

class userPage(QWidget):
    def __init__(self):
        super().__init__()
        self.user = None
    def setUser(self, user: IEntity):
        self.user = user
    def logoutUser(self):
        self.setUser(None)
    def loadUserData(self):
        pass
        # Each page that invokes the loadable interface takes a list of elements to load to the specific page
        #the idea is that at the time of logging in the user all the infomation directly loaded into the page through this function

#endregion

#In order to have an efficient and scalable app pages will be seperated into individual widgets
#This prevents accidental variable changes and makes the application easier to debug and develop

#region Welcome Page

# The welcome page consists of a title and buttons that lead to the tenant and staff portals respectively
class WelcomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"Welcome")

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setLayout(self.verticalLayout)

        self.title = QLabel()
        self.title.setObjectName(u"title")
        self.title.setFont(title)

       

        self.loginCustomerBtn = QPushButton()
        self.loginCustomerBtn.setObjectName(u"loginCustomerBtn")


        self.loginAdminBtn = QPushButton()
        self.loginAdminBtn.setObjectName(u"loginAdminBtn")


        self.verticalLayout.addWidget(self.title)
        self.verticalLayout.addWidget(self.loginAdminBtn)
        self.verticalLayout.addWidget(self.loginCustomerBtn)


    def retranslateUi(self):
        self.title.setText(QCoreApplication.translate("MainWindow", u"Paragon Apartment Mangement System", None))
        self.loginCustomerBtn.setText(QCoreApplication.translate("MainWindow", u"Customer Login Portal", None))
        self.loginAdminBtn.setText(QCoreApplication.translate("MainWindow", u"Admin Login Portal", None))

#endregion



#region Customer Login
# The customer login page contains a email and password input section and a submit button
class CustomerLoginPage(QWidget):
        def __init__(self):
            super().__init__()

            self.setObjectName(u"CustomerLogin")

            # Group Box
            self.loginGroup = QGroupBox(self)
            self.loginGroup.setObjectName(u"loginGroup")
            self.loginGroup.setGeometry(QRect(9, 10, 811, 561))
            

            self.loginGroup.setFont(text)
            self.loginGroup.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
            self.loginGroup.setFlat(True)
            
            # Email
            self.emailLabel = QLabel(self.loginGroup)
            self.emailLabel.setObjectName(u"emailLabel")
            self.emailLabel.setGeometry(QRect(380, 170, 54, 30))

            self.emailInput = QTextEdit(self.loginGroup)
            self.emailInput.setObjectName(u"emailInput")
            self.emailInput.setGeometry(QRect(180, 200, 461, 41))

            #Password 
            self.passwordInput = QTextEdit(self.loginGroup)
            self.passwordInput.setObjectName(u"passwordInput")
            self.passwordInput.setGeometry(QRect(180, 300, 461, 41))

            self.passwordInput.setFont(text)

            self.customerPassword = QLabel(self.loginGroup)
            self.customerPassword.setObjectName(u"password")
            self.customerPassword.setGeometry(QRect(360, 270, 93, 30))


            #title
            self.title = QLabel(self.loginGroup)
            self.title.setObjectName(u"title")
            self.title.setGeometry(QRect(240, 90, 297, 53))
            
            self.title.setFont(title)

            #Buttons
            self.loginBtn = QPushButton(self.loginGroup)
            self.loginBtn.setObjectName(u"loginBtn")
            self.loginBtn.setGeometry(QRect(340, 400, 129, 40))

            self.signUpBtn = QPushButton(self.loginGroup)
            self.signUpBtn.setObjectName(u"signUpBtn")
            self.signUpBtn.setGeometry(QRect(340, 350, 129, 40))

        def retranslateUi(self):
            self.loginGroup.setTitle("")
            self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
            self.emailInput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "hr { height: 1px; border-width: 0; }\n"
    "li.unchecked::marker { content: \"\\2610\"; }\n"
    "li.checked::marker { content: \"\\2612\"; }\n"
    "</style></head><body style=\" font-family:'Calibri'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
            self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. paragon@gmail.com ", None))
            self.passwordInput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "hr { height: 1px; border-width: 0; }\n"
    "li.unchecked::marker { content: \"\\2610\"; }\n"
    "li.checked::marker { content: \"\\2612\"; }\n"
    "</style></head><body style=\" font-family:'Bookshelf Symbol 7'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
            self.passwordInput.setPlaceholderText("")
            self.customerPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
            self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
            self.signUpBtn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
            self.title.setText(QCoreApplication.translate("MainWindow", u"Customer Login", None))

#endregion

#region Sign Up Page

# The Sign Up Page consists of a title and a email input. It also has a submit button
class SignUpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(160, 40, 503, 36))
        self.title.setFont(heading)
        self.title.setScaledContents(False)
        self.signUpForm = QWidget(self)
        self.signUpForm.setObjectName(u"signUpForm")
        self.signUpForm.setGeometry(QRect(240, 150, 311, 261))
        self.submitBtn = QPushButton(self.signUpForm)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(100, 150, 110, 24))
        self.formTitle = QLabel(self.signUpForm)
        self.formTitle.setObjectName(u"formTitle")
        self.formTitle.setGeometry(QRect(60, 70, 181, 30))
        self.formTitle.setFont(text)
        self.emailInput = QTextEdit(self.signUpForm)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(20, 120, 281, 21))
        self.emailInput.setMouseTracking(True)
        self.emailInput.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.emailInput.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.prompt = QLabel(self.signUpForm)
        self.prompt.setObjectName(u"prompt")
        self.prompt.setGeometry(QRect(50, 100, 205, 16))
    # setupUi

    def retranslateUi(self):
        self.title.setText(QCoreApplication.translate("signUpPage", u"<html><head/><body><p>Paragon Apartment Management System</p></body></html>", None))
        self.submitBtn.setText(QCoreApplication.translate("signUpPage", u"Sign up with email", None))
        self.formTitle.setText(QCoreApplication.translate("signUpPage", u"Create an Account", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("signUpPage", u"email@domain.com", None))
        self.prompt.setText(QCoreApplication.translate("signUpPage", u"Enter your email to sign up for this app", None))
    # retranslateUi
    
        




#endregion


#region Admin Login

class AdminLoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.staff = User("","", "", "" , "" ,"", "")
        self.setObjectName(u"AdminLogin")

        # Group Box
        self.adminGroup = QGroupBox(self)
        self.adminGroup.setObjectName(u"adminGroup")
        self.adminGroup.setGeometry(QRect(10, 10, 811, 561))

        
        self.adminGroup.setFont(text)
        self.adminGroup.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.adminGroup.setFlat(True)

        #Email 

        self.emailLabel = QLabel(self.adminGroup)
        self.emailLabel.setObjectName(u"adminEmailLabel")
        self.emailLabel.setGeometry(QRect(380, 170, 54, 30))

        self.emailInput = QTextEdit(self.adminGroup)
        self.emailInput.setObjectName(u"adminEmailInput")
        self.emailInput.setGeometry(QRect(180, 200, 461, 41))

        #Password

        self.passwordInput = QTextEdit(self.adminGroup)
        self.passwordInput.setObjectName(u"adminPasswordInput")
        self.passwordInput.setGeometry(QRect(180, 300, 461, 41))
        

        self.passwordLabel = QLabel(self.adminGroup)
        self.passwordLabel.setObjectName(u"adminPasswordLabel")
        self.passwordLabel.setGeometry(QRect(360, 270, 93, 30))

        #Login Button

        self.loginBtn = QPushButton(self.adminGroup)
        self.loginBtn.setObjectName(u"adminLoginBtn")
        self.loginBtn.setGeometry(QRect(340, 370, 129, 40))

        #Title

        self.title = QLabel(self.adminGroup)
        self.title.setObjectName(u"adminLoginLabel")
        self.title.setGeometry(QRect(290, 90, 234, 53))


        self.title.setFont(title)

        
    def retranslateUi(self):
        self.adminGroup.setTitle("")
        self.emailLabel.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.emailInput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Calibri'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. paragon@gmail.com ", None))
        self.passwordInput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Bookshelf Symbol 7'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.passwordInput.setPlaceholderText("")
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Admin Login", None))

        def setAdmin(self, admin : User):
            self.staff = admin
#endregion 

#I have put my code in this spot, this file it very different to the one I worked on

#region Maintenance Request Page

# This page lets a tenant describe a problem in their apartment and submit it.
# QWidget is the base "blank canvas" class everything is built on.
class MaintenanceRequestPage(QWidget):
    def __init__(self):
        super().__init__()        # Always call the parent class constructor first
        self.resize(831, 581)

        # QLabel is just a text label — it doesn't do anything, it just displays text
        self.title = QLabel(self)
        self.title.setGeometry(QRect(290, 30, 250, 40))   # (x, y, width, height)
        self.title.setFont(heading)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # QGroupBox draws a box with a title around a group of related widgets
        self.formGroup = QGroupBox(self)
        self.formGroup.setGeometry(QRect(150, 90, 530, 400))

        #QLabel for the description field
        self.descriptionLabel = QLabel(self.formGroup)
        self.descriptionLabel.setGeometry(QRect(20, 30, 120, 20))

        # QTextEdit is a multi-line text input box — good for longer descriptions
        self.descriptionInput = QTextEdit(self.formGroup)
        self.descriptionInput.setGeometry(QRect(20, 55, 490, 100))
        self.descriptionInput.setPlaceholderText("Describe the issue in detail...")

        # QLabel for the priority dropdown
        self.priorityLabel = QLabel(self.formGroup)
        self.priorityLabel.setGeometry(QRect(20, 175, 120, 20))

        # QComboBox is a dropdown menu — you add the options with addItem()
        self.priorityDropdown = QComboBox(self.formGroup)
        self.priorityDropdown.setGeometry(QRect(20, 200, 200, 26))
        self.priorityDropdown.addItem("Low")
        self.priorityDropdown.addItem("Medium")
        self.priorityDropdown.addItem("High")

        # QPushButton is a clickable button
        # The actual click action is connected later in main.py — not here
        self.submitBtn = QPushButton(self.formGroup)
        self.submitBtn.setGeometry(QRect(380, 340, 110, 32))

        # A back button so the tenant can return to their dashboard
        self.backBtn = QPushButton(self)
        self.backBtn.setGeometry(QRect(20, 20, 80, 30))

        self.retranslateUi()

    # retranslateUi sets all the visible text separately from the layout.
    # This is a Qt convention — it makes it easier to support multiple languages later.
    def retranslateUi(self):
        self.title.setText("Submit a Maintenance Request")
        self.formGroup.setTitle("Request Details")
        self.descriptionLabel.setText("Description of Issue")
        self.priorityLabel.setText("Priority Level")
        self.submitBtn.setText("Submit")
        self.backBtn.setText("< Back")


#endregion

#region Client Dashboard

#Previous iteration of the client dashbaord
# The client dashboard contains a side bar that controls a stackwidget that switches the sections currently being looked at.
# The default page - what the user is greeted with after they login
# The Account Page - Where the user will view and edit their personal infomation
# The Lease Page - Where the user can track their lease agreement
# The Payment Page - Where the user will make any outstanding payments
# The complaint Page - Where the user will submit complaints
# The buttons are automatically connected so no need to connect them at run time 

# class Dashboard(userPage):
#         def __init__(self):
#             super().__init__()
#             self.resize(805, 581)
#             #StackWidget / Dashboard Content
#             self.stackedWidget = QStackedWidget(self)
#             self.stackedWidget.setObjectName(u"stackedWidget")
#             self.stackedWidget.setGeometry(QRect(110, 70, 681, 501))
#             self.stackedWidget.setStyleSheet("background-color: green;")

#             #Default Page
#             self.defaultPage = QWidget()
#             self.defaultPage.setObjectName(u"defaultPage")
#             self.defaultTitle = QLabel(self.defaultPage)
#             self.defaultTitle.setObjectName(u"defaultTitle")
#             self.defaultTitle.setGeometry(QRect(270, 220, 44, 16))
#             self.stackedWidget.addWidget(self.defaultPage)
            


#             #Account Page
#             self.accountPage = QWidget()
#             self.accountPage.setObjectName(u"accountPage")
#             self.label_2 = QLabel(self.accountPage)
#             self.label_2.setObjectName(u"label_2")
#             self.label_2.setGeometry(QRect(270, 220, 44, 16))
#             self.stackedWidget.addWidget(self.accountPage)

#             #Lease Page
#             self.leasePage = QWidget()
#             self.leasePage.setObjectName(u"leasePage")
#             self.label_3 = QLabel(self.leasePage)
#             self.label_3.setObjectName(u"label_3")
#             self.label_3.setGeometry(QRect(250, 250, 30, 16))
#             self.stackedWidget.addWidget(self.leasePage)

#             #Payment Page
#             self.paymentPage = QWidget()
#             self.paymentPage.setObjectName(u"paymentPage")
#             self.label_4 = QLabel(self.paymentPage)
#             self.label_4.setObjectName(u"label_4")
#             self.label_4.setGeometry(QRect(280, 240, 52, 16))
#             self.stackedWidget.addWidget(self.paymentPage)

#             #Complaints Page
#             self.complaintsPage = QWidget()
#             self.complaintsPage.setObjectName(u"complaintsPage")
#             self.label = QLabel(self.complaintsPage)
#             self.label.setObjectName(u"label")
#             self.label.setGeometry(QRect(270, 190, 58, 16))
#             self.stackedWidget.addWidget(self.complaintsPage)


#             #Sidebar

#             self.sideBar = QWidget(self)
#             self.sideBar.setObjectName(u"sideBar")
#             self.sideBar.setGeometry(QRect(10, 10, 91, 561))
#             self.sideBar.setStyleSheet("background-color: green;")

#             self.gridLayout = QGridLayout(self.sideBar)
#             self.gridLayout.setObjectName(u"gridLayout")


#             #Account Button
#             self.accountBtn = QPushButton(self.sideBar)
#             self.accountBtn.setObjectName(u"accountBtn")
#             self.accountBtn.setCheckable(True)
#             self.accountBtn.setAutoExclusive(True)
#             self.accountBtn.clicked.connect(self.switchAccountPage)

#             #Lease Button
#             self.leaseBtn = QPushButton(self.sideBar)
#             self.leaseBtn.setObjectName(u"leaseBtn")
#             self.leaseBtn.setCheckable(True)
#             self.leaseBtn.setAutoExclusive(True)
#             self.leaseBtn.clicked.connect(self.switchLeasePage)


#             #Payment Button
#             self.paymentsBtn = QPushButton(self.sideBar)
#             self.paymentsBtn.setObjectName(u"paymentsBtn")
#             self.paymentsBtn.setCheckable(True)
#             self.paymentsBtn.setAutoExclusive(True)
#             self.paymentsBtn.clicked.connect(self.switchPaymentsPage)


#             #Complaints Button
#             self.complaintsBtn = QPushButton(self.sideBar)
#             self.complaintsBtn.setObjectName(u"complaintsBtn")
#             self.complaintsBtn.setCheckable(True)
#             self.complaintsBtn.setAutoExclusive(True)
#             self.complaintsBtn.clicked.connect(self.switchComplaintsPage)


#             #Adding to Layout
#             self.gridLayout.addWidget(self.accountBtn, 0, 0, 1, 1)
#             self.gridLayout.addWidget(self.leaseBtn, 1, 0, 1, 1)
#             self.gridLayout.addWidget(self.paymentsBtn, 2, 0, 1, 1)
#             self.gridLayout.addWidget(self.complaintsBtn, 3, 0, 1, 1)

#             self.stackedWidget.setCurrentIndex(0)


#         def retranslateUi(self):
#             self.leaseBtn.setText(QCoreApplication.translate("dashboard", u"Lease", None))
#             self.paymentsBtn.setText(QCoreApplication.translate("dashboard", u"Payments", None))
#             self.accountBtn.setText(QCoreApplication.translate("dashboard", u"Account", None))
#             self.complaintsBtn.setText(QCoreApplication.translate("dashboard", u"Complaints", None))
#             self.defaultTitle.setText(QCoreApplication.translate("dashboard", u"Default", None))
#             self.label_2.setText(QCoreApplication.translate("dashboard", u"Account", None))
#             self.label_3.setText(QCoreApplication.translate("dashboard", u"Lease", None))
#             self.label_4.setText(QCoreApplication.translate("dashboard", u"payments", None))
#             self.label.setText(QCoreApplication.translate("dashboard", u"complaints", None))
#         # retranslateUi

#         def switchAccountPage(self):
#             self.stackedWidget.setCurrentIndex(1)

#         def switchLeasePage(self):
#             self.stackedWidget.setCurrentIndex(2)

#         def switchPaymentsPage(self):
#             self.stackedWidget.setCurrentIndex(3)
        
#         def switchComplaintsPage(self):
#             self.stackedWidget.setCurrentIndex(4)
    


class TenantDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.tenant = Tenant("","","", "", "", "", "", "","")
        self.contract = Contract("","","","","","","")
        self.apartment = Apartment("","","","","","",True)
        self.resize(831, 758)

        #Title Section
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0,0,0,0)
        self.titleSection = QFrame(self)
        self.titleSection.setObjectName(u"titleSection")
        self.titleSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleSection.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleSection)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.title = QLabel(self.titleSection)
        self.title.setObjectName(u"title")
        self.horizontalLayout_2.addWidget(self.title, 0, Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addWidget(self.titleSection)

        #Tabs
        self.tabSection = QFrame(self)
        self.tabSection.setObjectName(u"tabSection")
        self.tabSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.tabSection.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.tabSection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.overviewBtn = QPushButton(self.tabSection)
        self.overviewBtn.setObjectName(u"overviewBtn")
        self.horizontalLayout.addWidget(self.overviewBtn)

        self.accountBtn = QPushButton(self.tabSection)
        self.accountBtn.setObjectName(u"accountBtn")
        self.horizontalLayout.addWidget(self.accountBtn)

        self.paymentsBtn = QPushButton(self.tabSection)
        self.paymentsBtn.setObjectName(u"paymentsBtn")
        self.horizontalLayout.addWidget(self.paymentsBtn)

        self.maintanenceBtn = QPushButton(self.tabSection)
        self.maintanenceBtn.setObjectName(u"maintanenceBtn")
        self.horizontalLayout.addWidget(self.maintanenceBtn)

        self.horizontalSpacer = QSpacerItem(533, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        self.verticalLayout_2.addWidget(self.tabSection)


        #Main Content
        self.mainSection = QStackedWidget(self)
        self.mainSection.setObjectName(u"mainSection")
        self.mainSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainSection.setFrameShadow(QFrame.Shadow.Raised)
        self.mainSection.resize(811,621)

        #Overview Page
        self.OverviewPage = TenantOverviewPage()
        self.mainSection.addWidget(self.OverviewPage)
                
        self.PaymentsPage = TenantPaymentsPage()
        self.PaymentsPage.setObjectName(u"paymentsPage")
        self.mainSection.addWidget(self.PaymentsPage)
    

        self.verticalLayout_2.addWidget(self.mainSection)

        #Account Page

        self.AccountPage = TenantAccountPage()
        self.mainSection.addWidget(self.AccountPage)

        #Maintenance Page 
        
        self.MaintenanceReq = MaintenanceRequestPage()
        self.mainSection.addWidget(self.MaintenanceReq)

        #Connections

        self.overviewBtn.clicked.connect(lambda: self.switchToOverviewPage())
        self.paymentsBtn.clicked.connect(lambda: self.switchToPaymentsPage())
        self.accountBtn.clicked.connect(lambda : self.switchToAccountPage())
        self.maintanenceBtn.clicked.connect(lambda : self.switchToMaintenence())

        self.mainSection.setCurrentIndex(0)
        self.retranslateUi()

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Tenant Dashboard", None))
        self.overviewBtn.setText(QCoreApplication.translate("Form", u"Overview", None))
        self.paymentsBtn.setText(QCoreApplication.translate("Form", u"Payments", None))
        self.maintanenceBtn.setText(QCoreApplication.translate("Form", u"Maintanence", None))
        self.accountBtn.setText(QCoreApplication.translate("Form", u"Account", None))
        self.OverviewPage.retranslateUi()
        self.PaymentsPage.retranslateUi()
       
    # retranslateUi

    def setUser(self, tenant : Tenant, contract : Contract, apartment : Apartment):
        self.tenant = tenant
        self.contract = contract
        self.apartment = apartment
    def clearUser(self):
        self.tenant = Tenant("","","", "", "", "", "", "","")
        self.contract = Contract("","","","","","","")
        self.apartment = Apartment("","","","","","",True)
        self.retranslateUi()
        self.OverviewPage.retranslateUi()
        self.PaymentsPage.retranslateUi()
        self.AccountPage.retranslateUi()


    def switchToPaymentsPage(self):
        self.mainSection.setCurrentIndex(1)
    def switchToOverviewPage(self):
        self.mainSection.setCurrentIndex(0)
    def switchToAccountPage(self):
        self.mainSection.setCurrentIndex(2)
    def switchToMaintenence(self):
        self.mainSection.setCurrentIndex(3)
        
    def AddPageDetail(self,locations : list[Location], OutstandingMaintence : list[MaintenanceRequest], dueDate: str):
        for location in locations:
            if location.id == self.apartment.location_id:
                locationName = location.location_name
        
        self.OverviewPage.AddPageDetail(self.tenant.first_name,self.apartment.monthly_rent,dueDate,len(OutstandingMaintence),self.apartment.id,self.apartment.location_id)
        self.AccountPage.GetLocations(locations)
        self.AccountPage.AddPageDetail(self.tenant.first_name,self.tenant.last_name,self.tenant.email,self.tenant.national_insurance,self.tenant.phone_number)

    def SubmitUserInfo(self):
        info = self.AccountPage.SubmitNewUserInfo()
        NewTenant = Tenant(self.tenant.id ,info.first_name, info.last_name,info.national_insurance,info.email,info.password,info.phone_number,info.occupation,info.references)
        return NewTenant

    def SubmitRequest(self):
        return MaintenanceRequest("",self.tenant.id, self.apartment.id, self.MaintenanceReq.descriptionInput.toPlainText(),self.MaintenanceReq.priorityDropdown.currentText(), '', "","","","","")
#endregion


#region Testing Page
# This page has 4 buttons on it that are asssigned to functions that are being developed currently
# This page makes testing much quicker while not interferring with the project
class TestPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.testBtn1 = QPushButton(self)
        self.testBtn1.setObjectName(u"testBtn1")

        self.gridLayout.addWidget(self.testBtn1, 0, 0, 1, 1)

        self.testBtn2 = QPushButton(self)
        self.testBtn2.setObjectName(u"testBtn2")

        self.gridLayout.addWidget(self.testBtn2, 0, 1, 1, 1)

        self.testBtn3 = QPushButton(self)
        self.testBtn3.setObjectName(u"testBtn3")

        self.gridLayout.addWidget(self.testBtn3, 1, 0, 1, 1)

        self.testBtn4 = QPushButton(self)
        self.testBtn4.setObjectName(u"testBtn4")

        self.gridLayout.addWidget(self.testBtn4, 1, 1, 1, 1)


    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("testPage", u"Form", None))
        self.testBtn1.setText(QCoreApplication.translate("testPage", u"Test 1", None))
        self.testBtn2.setText(QCoreApplication.translate("testPage", u"Test 2", None))
        self.testBtn3.setText(QCoreApplication.translate("testPage", u"Test 3", None))
        self.testBtn4.setText(QCoreApplication.translate("testPage", u"Test 4", None))
    # retranslateUi



#endregion


#region Detailed Sign Up Page
class SignUpDetailed(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        self.content = QFrame(self)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(0, 0, 831, 581))
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(25, 50, 25, 50)
        self.form = QFrame(self.content)
        self.form.setObjectName(u"form")
        self.form.setFrameShape(QFrame.Shape.Box)
        self.form.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_7 = QVBoxLayout(self.form)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.title = QLabel(self.form)
        self.title.setObjectName(u"title")

        self.verticalLayout_7.addWidget(self.title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.signInFrame = QFrame(self.form)
        self.signInFrame.setObjectName(u"signInFrame")
        self.signInFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.signInFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout = QVBoxLayout(self.signInFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nameFrame = QFrame(self.signInFrame)
        self.nameFrame.setObjectName(u"nameFrame")
        self.nameFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.nameFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.nameFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.firstNamePrompt = QLabel(self.nameFrame)
        self.firstNamePrompt.setObjectName(u"firstNamePrompt")

        self.verticalLayout_3.addWidget(self.firstNamePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.firstNameInput = QLineEdit(self.nameFrame)
        self.firstNameInput.setObjectName(u"firstNameInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstNameInput.sizePolicy().hasHeightForWidth())
        self.firstNameInput.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.firstNameInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lastNamePrompt = QLabel(self.nameFrame)
        self.lastNamePrompt.setObjectName(u"lastNamePrompt")

        self.verticalLayout_3.addWidget(self.lastNamePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lastNameInput = QLineEdit(self.nameFrame)
        self.lastNameInput.setObjectName(u"lastNameInput")
        sizePolicy.setHeightForWidth(self.lastNameInput.sizePolicy().hasHeightForWidth())
        self.lastNameInput.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.lastNameInput, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.nameFrame)

        self.emailPrompt = QLabel(self.signInFrame)
        self.emailPrompt.setObjectName(u"emailPrompt")

        self.verticalLayout.addWidget(self.emailPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.emailInput = QLineEdit(self.signInFrame)
        self.emailInput.setObjectName(u"emailInput")
        sizePolicy.setHeightForWidth(self.emailInput.sizePolicy().hasHeightForWidth())
        self.emailInput.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.emailInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.passwordPrompt = QLabel(self.signInFrame)
        self.passwordPrompt.setObjectName(u"passwordPrompt")

        self.verticalLayout.addWidget(self.passwordPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.passwordInput = QLineEdit(self.signInFrame)
        self.passwordInput.setObjectName(u"passwordInput")
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.passwordInput, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addWidget(self.signInFrame)

        self.signInFrame_2 = QFrame(self.form)
        self.signInFrame_2.setObjectName(u"signInFrame_2")
        self.signInFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.signInFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.signInFrame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.nationalNumPrompt = QLabel(self.signInFrame_2)
        self.nationalNumPrompt.setObjectName(u"nationalNumPrompt")

        self.verticalLayout_6.addWidget(self.nationalNumPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.nationalNumInput = QLineEdit(self.signInFrame_2)
        self.nationalNumInput.setObjectName(u"nationalNumInput")
        sizePolicy.setHeightForWidth(self.nationalNumInput.sizePolicy().hasHeightForWidth())
        self.nationalNumInput.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.nationalNumInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.phoneNumPrompt = QLabel(self.signInFrame_2)
        self.phoneNumPrompt.setObjectName(u"phoneNumPrompt")

        self.verticalLayout_6.addWidget(self.phoneNumPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.phoneNumInput = QLineEdit(self.signInFrame_2)
        self.phoneNumInput.setObjectName(u"phoneNumInput")
        sizePolicy.setHeightForWidth(self.phoneNumInput.sizePolicy().hasHeightForWidth())
        self.phoneNumInput.setSizePolicy(sizePolicy)

        self.verticalLayout_6.addWidget(self.phoneNumInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.occupationPrompt = QLabel(self.signInFrame_2)
        self.occupationPrompt.setObjectName(u"occupationPrompt")

        self.verticalLayout_6.addWidget(self.occupationPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.occupationComboBox = QComboBox(self.signInFrame_2)
        self.occupationComboBox.addItem("")
        self.occupationComboBox.addItem("")
        self.occupationComboBox.addItem("")
        self.occupationComboBox.addItem("")
        self.occupationComboBox.setObjectName(u"occupationComboBox")
        sizePolicy.setHeightForWidth(self.occupationComboBox.sizePolicy().hasHeightForWidth())
        self.occupationComboBox.setSizePolicy(sizePolicy)
        self.occupationComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.verticalLayout_6.addWidget(self.occupationComboBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addWidget(self.signInFrame_2)

        self.submitBtn = QPushButton(self.form)
        self.submitBtn.setObjectName(u"submitBtn")
        sizePolicy.setHeightForWidth(self.submitBtn.sizePolicy().hasHeightForWidth())
        self.submitBtn.setSizePolicy(sizePolicy)

        self.verticalLayout_7.addWidget(self.submitBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.form)


        self.retranslateUi()

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("SignUpDetailed", u"Form", None))
        self.title.setText(QCoreApplication.translate("SignUpDetailed", u"Welcome New User", None))
        self.firstNamePrompt.setText(QCoreApplication.translate("SignUpDetailed", u"First Name", None))
        self.lastNamePrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Last Name", None))
        self.emailPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Email", None))
        self.passwordPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Password", None))
        self.nationalNumPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"National Insurance Number", None))
        self.phoneNumPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Phone Number", None))
        self.occupationPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Occupation", None))
        self.occupationComboBox.setItemText(0, QCoreApplication.translate("SignUpDetailed", u"Employed", None))
        self.occupationComboBox.setItemText(1, QCoreApplication.translate("SignUpDetailed", u"Student", None))
        self.occupationComboBox.setItemText(2, QCoreApplication.translate("SignUpDetailed", u"Part-Time", None))
        self.occupationComboBox.setItemText(3, QCoreApplication.translate("SignUpDetailed", u"Unemployed", None))

        self.submitBtn.setText(QCoreApplication.translate("SignUpDetailed", u"Submit", None))
    # retranslateUi

#endregion

#region Front Desk Dashboard

# The Front Desk Dashboard contains all the widgets needed for the staff to operate their task.
# The top section is for registering new tenants, the bottom section is for managing existing tenants.

class FrontDeskDashboard(userPage):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(350, 20, 118, 16))

        # Managing tenants section
        self.manageTenants = QGroupBox(self)
        self.manageTenants.setObjectName(u"manageTenants")
        self.manageTenants.setGeometry(QRect(40, 320, 731, 241))


        #Tenant Table and Search Bar
        self.tenantTable = Table([],[])
        self.tenantTable.setParent(self.manageTenants)
        self.tenantTable.setObjectName(u"tenantTable")
        self.tenantTable.setGeometry(QRect(10, 30, 711, 201))
        self.searchBar = QLineEdit(self.manageTenants)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(610, 10, 113, 22))



        #Registering tenants section
        self.registerTenants = QGroupBox(self)
        self.registerTenants.setObjectName(u"registerTenants")
        self.registerTenants.setGeometry(QRect(40, 50, 731, 241))
        self.firstNameInput = QLineEdit(self.registerTenants)
        self.firstNameInput.setObjectName(u"firstNameInput")
        self.firstNameInput.setGeometry(QRect(20, 40, 113, 21))
        self.lastNameInput = QLineEdit(self.registerTenants)
        self.lastNameInput.setObjectName(u"lastNameInput")
        self.lastNameInput.setGeometry(QRect(20, 80, 113, 21))
        self.emailInput = QLineEdit(self.registerTenants)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(20, 120, 113, 21))
        self.nationalInsuranceInput = QLineEdit(self.registerTenants)
        self.nationalInsuranceInput.setObjectName(u"nationalInsuranceInput")
        self.nationalInsuranceInput.setGeometry(QRect(410, 50, 161, 21))
        self.phoneNumberInput = QLineEdit(self.registerTenants)
        self.phoneNumberInput.setObjectName(u"phoneNumberInput")
        self.phoneNumberInput.setGeometry(QRect(410, 110, 161, 21))
        self.occupationDropdown = QComboBox(self.registerTenants)
        self.occupationDropdown.addItem("")
        self.occupationDropdown.addItem("")
        self.occupationDropdown.addItem("")
        self.occupationDropdown.addItem("")
        self.occupationDropdown.setObjectName(u"occupationDropdown")
        self.occupationDropdown.setGeometry(QRect(410, 170, 171, 26))
        self.submitButton = QPushButton(self.registerTenants)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(600, 200, 81, 26))
        self.passwordInput = QLineEdit(self.registerTenants)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(20, 170, 113, 21))


        #Connections

        self.searchBar.textChanged.connect(lambda : self.tenantTable.search(self.searchBar.text()))

        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Front Desk Dashboard", None))
        self.manageTenants.setTitle(QCoreApplication.translate("Form", u"Manage Tenants", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.registerTenants.setTitle(QCoreApplication.translate("Form", u"Register Tenants", None))
        self.firstNameInput.setPlaceholderText(QCoreApplication.translate("Form", u"First Name", None))
        self.lastNameInput.setText("")
        self.lastNameInput.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name", None))
        self.emailInput.setText("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.nationalInsuranceInput.setText("")
        self.nationalInsuranceInput.setPlaceholderText(QCoreApplication.translate("Form", u"National Insurance Number", None))
        self.phoneNumberInput.setText("")
        self.phoneNumberInput.setPlaceholderText(QCoreApplication.translate("Form", u"Phone Number", None))
        self.occupationDropdown.setItemText(0, QCoreApplication.translate("Form", u"Student", None))
        self.occupationDropdown.setItemText(1, QCoreApplication.translate("Form", u"Unemployed", None))
        self.occupationDropdown.setItemText(2, QCoreApplication.translate("Form", u"Employed", None))
        self.occupationDropdown.setItemText(3, QCoreApplication.translate("Form", u"Part-Time", None))

        self.occupationDropdown.setPlaceholderText(QCoreApplication.translate("Form", u"Occupation", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
    # retranslateUi


        
    def Submit(self):
        fName = self.firstNameInput.text()
        lName = self.lastNameInput.text()
        email = self.emailInput.text()
        password = self.passwordInput.text()
        phoneNumber = self.phoneNumberInput.text() #TODO phonenumber checking is valid phone number
        nationalInsurance = self.nationalInsuranceInput.text()
        occupation = self.occupationDropdown.currentText()
        references = ""
        tenant = Tenant(-1,fName,lName,email,password,phoneNumber,nationalInsurance,occupation ,references )
        self.firstNameInput.clear()
        self.lastNameInput.clear()
        self.emailInput.clear()
        self.passwordInput.clear()
        self.phoneNumberInput.clear()
        self.nationalInsuranceInput.clear()
        self.occupationDropdown.setCurrentIndex(0)
        return tenant
    

#endregion



#region Graph Generation

class BarChart(QBarSeries):
    def __init__(self):
        super().__init__()

#endregion

#Labels contains the names of the different type of data and numData contains the number of entrys for each label
class PieChart(QChartView):
    def __init__(self, labels : tuple , numData : tuple , title : str):
        super().__init__()
        chart = QChart()
        self.pieChart = QPieSeries()
        for i in range(0, len(labels)):
            self.pieChart.append(labels[i],numData[i])
        chart.addSeries(self.pieChart)
        chart.setTitle(title)

        self.setChart(chart)
        

#Pie for occupancy levels vs unoccupied in aprtment and then in city

#Pie of oustandinf payments vs collected

#entension add a prediction method

#TODO CREATE A PIE GRAPH FOR OUTSTANDING VERSES COLLECTED PAYMENTS 
#TODO CREATE A LINE GRAPH FOR THE EPENSES PER WEEK/ MONTH / YEAR FROM MAINTANENCE

#region Finance Dashboard



class FinanceDashboard(userPage):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)

        #region Title
        self.titleFrame = QFrame(self)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(0, 10, 831, 91))
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.titleFrame)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2.addWidget(self.label)
        #endregion


        #region Main Content
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 110, 811, 461))
        #endregion


        #region Tabs
        self.tabs = QFrame(self)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(0, 100, 831, 41))
        self.tabs.setFrameShape(QFrame.Shape.StyledPanel)
        self.tabs.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.tabs)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        # Payment Tab Button
        self.paymentsBtn = QPushButton(self.tabs)
        self.paymentsBtn.setObjectName(u"paymentsBtn")
        self.horizontalLayout_8.addWidget(self.paymentsBtn)

        # Invoice Tab Button
        self.invoicesBtn = QPushButton(self.tabs)
        self.invoicesBtn.setObjectName(u"invoicesBtn")
        self.horizontalLayout_8.addWidget(self.invoicesBtn)

        # Report Tab Button
        self.reportBtn = QPushButton(self.tabs)
        self.reportBtn.setObjectName(u"reportBtn")
        self.horizontalLayout_8.addWidget(self.reportBtn)
        #endregion

        #region Pages
        #region Report Page
        self.ReportPage = ReportPage()
        self.ReportPage.setObjectName(u"ReportPage")
        
        
        self.stackedWidget.addWidget(self.ReportPage)
        #endregion
        
        #region Invoice Page
        self.InvoicePage = QWidget()
        self.InvoicePage.setObjectName(u"InvoicePage")
        

        #Title
        self.invoiceFrame = QFrame(self.InvoicePage)
        self.invoiceFrame.setObjectName(u"invoiceFrame")
        self.invoiceFrame.setGeometry(QRect(10, 20, 791, 431))
        self.invoiceFrame.setFrameShape(QFrame.Shape.StyledPanel)

        self.invoiceTitleBar = QFrame(self.invoiceFrame)
        self.invoiceTitleBar.setObjectName(u"invoiceTitleBar")
        self.invoiceTitleBar.setGeometry(QRect(5, 5, 781, 51))
        self.invoiceTitleBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.invoiceTitleBar.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7 = QHBoxLayout(self.invoiceTitleBar)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.invoiceTitle = QLabel(self.invoiceTitleBar)
        self.invoiceTitle.setObjectName(u"label_3")
        self.invoiceTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_7.addWidget(self.invoiceTitle)

        self.content = QFrame(self.invoiceFrame)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(10, 65, 771, 361))
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Form = QFrame(self.content)
        self.Form.setObjectName(u"Form")
        self.Form.setFrameShape(QFrame.Shape.StyledPanel)
        self.Form.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.issueRentBtn = QPushButton(self.Form)
        self.issueRentBtn.setObjectName(u"issueRentBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.issueRentBtn.sizePolicy().hasHeightForWidth())
        self.issueRentBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.issueRentBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.tenantIDPrompt = QLabel(self.Form)
        self.tenantIDPrompt.setObjectName(u"tenantIDPrompt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tenantIDPrompt.sizePolicy().hasHeightForWidth())
        self.tenantIDPrompt.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.tenantIDPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tenantIDInput = QSpinBox(self.Form)
        self.tenantIDInput.setObjectName(u"tenantIDInput")
        self.tenantIDInput.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tenantIDInput.setMaximum(999)

        self.verticalLayout.addWidget(self.tenantIDInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.dueDatePrompt = QLabel(self.Form)
        self.dueDatePrompt.setObjectName(u"dueDatePrompt")
        sizePolicy1.setHeightForWidth(self.dueDatePrompt.sizePolicy().hasHeightForWidth())
        self.dueDatePrompt.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.dueDatePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.dueDateInput = QDateEdit(self.Form)
        self.dueDateInput.setObjectName(u"dueDateInput")
        self.dueDateInput.setDateTime(QDateTime.currentDateTime())
        self.dueDateInput.setDateRange(QDateTime.currentDateTime().date(), QDate(QDate.currentDate().addMonths(3)))

        self.verticalLayout.addWidget(self.dueDateInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.amountPrompt = QLabel(self.Form)
        self.amountPrompt.setObjectName(u"amountPrompt")
        sizePolicy1.setHeightForWidth(self.amountPrompt.sizePolicy().hasHeightForWidth())
        self.amountPrompt.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.amountPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.amountInput = QDoubleSpinBox(self.Form)
        self.amountInput.setObjectName(u"amountInput")

        self.verticalLayout.addWidget(self.amountInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.referencePrompt = QLabel(self.Form)
        self.referencePrompt.setObjectName(u"referencePrompt")
        sizePolicy1.setHeightForWidth(self.referencePrompt.sizePolicy().hasHeightForWidth())
        self.referencePrompt.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.referencePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.referenceInput = QLineEdit(self.Form)
        self.referenceInput.setObjectName(u"referenceInput")
        self.referenceInput.setMaxLength(255)

        self.verticalLayout.addWidget(self.referenceInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.submitInvoiceBtn = QPushButton(self.Form)
        self.submitInvoiceBtn.setObjectName(u"submitInvoiceBtn")

        self.verticalLayout.addWidget(self.submitInvoiceBtn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout.addWidget(self.Form)

        self.stackedWidget.addWidget(self.InvoicePage)
        #endregion
        
        #region Payment Page
        self.PaymentPage = QWidget()
        self.PaymentPage.setObjectName(u"PaymentPage")
        
        
        
        self.managePayments = QGroupBox(self.PaymentPage)
        self.managePayments.setObjectName(u"managePayments")
        self.managePayments.setGeometry(QRect(20, 30, 771, 431))

        #Table
        self.paymentTable = Table([],[])
        self.paymentTable.setParent(self.managePayments)
        self.paymentTable.setObjectName(u"tenantTable")
        self.paymentTable.setGeometry(QRect(10, 50, 751, 371))
        self.tableBar = QFrame(self.managePayments)
        self.tableBar.setObjectName(u"tableBar")
        self.tableBar.setGeometry(QRect(10, 5, 751, 46))
        self.tableBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.tableBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableTitle = QFrame(self.tableBar)
        self.tableTitle.setObjectName(u"tableTitle")
        self.tableTitle.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableTitle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.tableTitle)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.title = QLabel(self.tableTitle)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.title)
        self.horizontalLayout_4.addWidget(self.tableTitle)


        #Tool Bar
        self.toolBar = QFrame(self.tableBar)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.toolBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.toolBar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.latePaymentsBtn = QPushButton(self.toolBar)
        self.latePaymentsBtn.setObjectName(u"latePaymentsBtn")
        self.latePaymentsBtn.setCheckable(True)
        self.latePaymentsBtn.setChecked(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.latePaymentsBtn.sizePolicy().hasHeightForWidth())
        self.latePaymentsBtn.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5.addWidget(self.latePaymentsBtn)

        self.refreshBtn = QPushButton(self.toolBar)
        self.refreshBtn.setObjectName(u"refreshBtn")
        sizePolicy1.setHeightForWidth(self.refreshBtn.sizePolicy().hasHeightForWidth())
        self.refreshBtn.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Wingdings 3"])
        self.refreshBtn.setFont(font)

        self.horizontalLayout_5.addWidget(self.refreshBtn)

        self.searchBar_2 = QLineEdit(self.toolBar)
        self.searchBar_2.setObjectName(u"searchBar_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.searchBar_2.sizePolicy().hasHeightForWidth())
        self.searchBar_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.searchBar_2)

        self.horizontalLayout_4.addWidget(self.toolBar)

        self.stackedWidget.addWidget(self.PaymentPage)
        #endregion
        #endregion
        
        #Connections
        self.invoicesBtn.clicked.connect(lambda : self.switchToInvoices())
        self.paymentsBtn.clicked.connect(lambda : self.switchToPayments())
        self.reportBtn.clicked.connect(lambda : self.switchToReport())
        self.searchBar_2.textChanged.connect(lambda : self.paymentTable.search(self.searchBar_2.text()))


        self.latePaymentsBtn.clicked.connect(lambda : self.ToggleLatePayments())
        self.stackedWidget.setCurrentIndex(2)
        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Finance Dashboard", None))
        self.invoiceTitle.setText(QCoreApplication.translate("Form", u"Issue Invoices", None))
        self.managePayments.setTitle("")
        self.title.setText(QCoreApplication.translate("Form", u"Payments", None))
        self.latePaymentsBtn.setText(QCoreApplication.translate("Form", u"Late Payments", None))
        self.refreshBtn.setText(QCoreApplication.translate("Form", u"P", None))
        self.searchBar_2.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.paymentsBtn.setText(QCoreApplication.translate("Form", u"Payments", None))
        self.invoicesBtn.setText(QCoreApplication.translate("Form", u"Invoices", None))
        self.reportBtn.setText(QCoreApplication.translate("Form", u"Report", None))
        self.issueRentBtn.setText(QCoreApplication.translate("InvoicePage", u"Issue All Monthlty Payments", None))
        self.tenantIDPrompt.setText(QCoreApplication.translate("InvoicePage", u"Tenant ID", None))
        self.dueDatePrompt.setText(QCoreApplication.translate("InvoicePage", u"Due Date", None))
        self.amountPrompt.setText(QCoreApplication.translate("InvoicePage", u"Amount", None))
        self.amountInput.setPrefix(QCoreApplication.translate("InvoicePage", u"\u00a3", None))
        self.referencePrompt.setText(QCoreApplication.translate("InvoicePage", u"Reference", None))
        self.submitInvoiceBtn.setText(QCoreApplication.translate("InvoicePage", u"Send Invoice", None))
        
    # retranslateUi

    def ToggleLatePayments(self):
        if self.latePaymentsBtn.isChecked():
            self.ShowLatePayments()
        else:
            self.ShowAllPayments()

    def ShowLatePayments(self):
     # STATUS of payment 5
        self.paymentTable.selectColumn(5)
        for item in self.paymentTable.selectedItems():
            if item.text() == 'Paid':
                self.paymentTable.hideRow(item.row())
        self.paymentTable.clearSelection()
        
    def ShowAllPayments(self):
        for row in range(0,self.paymentTable.rowCount()):
            self.paymentTable.showRow(row) 

    def switchToInvoices(self):
        self.stackedWidget.setCurrentIndex(1)
    def switchToPayments(self):
        self.stackedWidget.setCurrentIndex(2)
    def switchToReport(self):
        self.stackedWidget.setCurrentIndex(0)

    def SubmitInvoice(self):
        
        dueDate = self.dueDateInput.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        return (self.tenantIDInput.text(), dueDate, self.amountInput.cleanText(), self.referenceInput.text())

#endregion



#region Admin Dashboard
class AdminDashboard(userPage):
    def __init__(self):
        super().__init__()
        self.resize(832, 591)

        #Title
        self.titleFrame = QFrame(self)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(0, 10, 831, 91))
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.titleFrame)
        self.label.setObjectName(u"label")
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2.addWidget(self.label)

        #region Main Content
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 110, 811, 461))
        #endregion

        #region Tabs
        self.tabs = QFrame(self)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setGeometry(QRect(0, 100, 831, 41))
        self.tabs.setFrameShape(QFrame.Shape.StyledPanel)
        self.tabs.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.tabs)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.userBtn = QPushButton(self.tabs)
        self.userBtn.setObjectName(u"userBtn")

        self.horizontalLayout_8.addWidget(self.userBtn)

        self.apartmentBtn = QPushButton(self.tabs)
        self.apartmentBtn.setObjectName(u"apartmentBtn")

        self.horizontalLayout_8.addWidget(self.apartmentBtn)

        self.reportBtn = QPushButton(self.tabs)
        self.reportBtn.setObjectName(u"reportBtn")

        self.horizontalLayout_8.addWidget(self.reportBtn)
        #endregion



        #region Report Page
        self.ReportPage = ReportPageWithAllLocations()
        self.ReportPage.setObjectName(u"ReportPage")
        self.stackedWidget.addWidget(self.ReportPage)
        #endregion
        

        #region Apartments Page
        self.Apartments = QWidget()
        self.Apartments.setObjectName(u"Apartments")
        self.apartmentManage = QGroupBox(self.Apartments)
        self.apartmentManage.setObjectName(u"apartmentManage")
        self.apartmentManage.setGeometry(QRect(20, 30, 771, 431))

        #region Apartment Table
        self.apartmentTable = Table([],[])
        self.apartmentTable.setObjectName(u"apartmentTable")
        self.apartmentTable.setGeometry(QRect(10, 50, 751, 371))
        self.apartmentTable.setParent(self.apartmentManage)

        self.apartmentTableBar = QFrame(self.apartmentManage)
        self.apartmentTableBar.setObjectName(u"apartmentTableBar")
        self.apartmentTableBar.setGeometry(QRect(10, 5, 751, 46))
        self.apartmentTableBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.apartmentTableBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.apartmentTableBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)


        self.apartmentTitle = QFrame(self.apartmentTableBar)
        self.apartmentTitle.setObjectName(u"apartmentTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apartmentTitle.sizePolicy().hasHeightForWidth())

        self.apartmentTitle.setSizePolicy(sizePolicy)
        self.apartmentTitle.setFrameShape(QFrame.Shape.StyledPanel)
        self.apartmentTitle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.apartmentTitle)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.title_2 = QLabel(self.apartmentTitle)
        self.title_2.setObjectName(u"title_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_2.sizePolicy().hasHeightForWidth())
        self.title_2.setSizePolicy(sizePolicy1)
        self.title_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.title_2)
        self.horizontalLayout_7.addWidget(self.apartmentTitle)


        #Apartment Table Tool Bar
        self.apartmentToolBar = QFrame(self.apartmentTableBar)
        self.apartmentToolBar.setObjectName(u"apartmentToolBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHeightForWidth(self.apartmentToolBar.sizePolicy().hasHeightForWidth())
        self.apartmentToolBar.setSizePolicy(sizePolicy2)
        self.apartmentToolBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.apartmentToolBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.apartmentToolBar)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        #Apartment Location Dropdown
        self.apartmentLocationDropdown = QComboBox(self.apartmentToolBar)
        self.apartmentLocationDropdown.setObjectName(u"apartmentLocationDropdown")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHeightForWidth(self.apartmentLocationDropdown.sizePolicy().hasHeightForWidth())
        self.apartmentLocationDropdown.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10.addWidget(self.apartmentLocationDropdown)

        #Apartment Refresh Button
        self.apartmentRefresh = QPushButton(self.apartmentToolBar)
        self.apartmentRefresh.setObjectName(u"apartmentRefresh")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHeightForWidth(self.apartmentRefresh.sizePolicy().hasHeightForWidth())
        self.apartmentRefresh.setSizePolicy(sizePolicy4)
        self.apartmentRefresh.setMinimumSize(QSize(16, 16))
        self.apartmentRefresh.setBaseSize(QSize(0, 16))
        font = QFont()
        font.setFamilies([u"Wingdings 3"])
        self.apartmentRefresh.setFont(font)
        self.horizontalLayout_10.addWidget(self.apartmentRefresh)

        #Apartment Search Bar
        self.apartmentSearchBar = QLineEdit(self.apartmentToolBar)
        self.apartmentSearchBar.setObjectName(u"apartmentSearchBar")
        sizePolicy3.setHeightForWidth(self.apartmentSearchBar.sizePolicy().hasHeightForWidth())
        self.apartmentSearchBar.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10.addWidget(self.apartmentSearchBar)


        self.horizontalLayout_7.addWidget(self.apartmentToolBar)
        #endregion
        self.stackedWidget.addWidget(self.Apartments)

        #endregion

        #region User Page
        self.UserPage = QWidget()
        self.UserPage.setObjectName(u"UserPage")
        self.manageUsers = QGroupBox(self.UserPage)
        self.manageUsers.setObjectName(u"manageUsers")
        self.manageUsers.setGeometry(QRect(20, 30, 771, 431))

        #region User Table
        self.staffTable = Table((),())
        self.staffTable.setObjectName(u"staffTable")
        self.staffTable.setGeometry(QRect(10, 50, 751, 371))
        
        #Tenant Table
        self.tenantTable = Table((),())
        self.tenantTable.setObjectName(u"tenantTable")
        self.tenantTable.setGeometry(QRect(10, 50, 751, 371))
        

        self.userTableBar = QFrame(self.manageUsers)
        self.userTableBar.setObjectName(u"userTableBar")
        self.userTableBar.setGeometry(QRect(10, 5, 751, 46))
        self.userTableBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.userTableBar.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4 = QHBoxLayout(self.userTableBar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        #Table Title
        self.tableTitle = QFrame(self.userTableBar)
        self.tableTitle.setObjectName(u"tableTitle")
        sizePolicy.setHeightForWidth(self.tableTitle.sizePolicy().hasHeightForWidth())
        self.tableTitle.setSizePolicy(sizePolicy)
        self.tableTitle.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableTitle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.tableTitle)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.title = QLabel(self.tableTitle)
        self.title.setObjectName(u"title")
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_6.addWidget(self.title)
        self.horizontalLayout_4.addWidget(self.tableTitle)

        #User Table Tool Bar
        self.userToolBar = QFrame(self.userTableBar)
        self.userToolBar.setObjectName(u"userToolBar")
        sizePolicy2.setHeightForWidth(self.userToolBar.sizePolicy().hasHeightForWidth())
        self.userToolBar.setSizePolicy(sizePolicy2)
        self.userToolBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.userToolBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.userToolBar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.userBtnGroup = QWidget(self.userToolBar)
        self.userBtnGroup.setObjectName(u"userBtnGroup")
        self.horizontalLayout_3 = QHBoxLayout(self.userBtnGroup)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        #Show Tenants Button
        self.tenantsBtn = QPushButton(self.userBtnGroup)
        self.tenantsBtn.setObjectName(u"tenantsBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHeightForWidth(self.tenantsBtn.sizePolicy().hasHeightForWidth())
        self.tenantsBtn.setSizePolicy(sizePolicy5)
        self.tenantsBtn.setCheckable(True)
        self.tenantsBtn.setChecked(True)
        self.horizontalLayout_3.addWidget(self.tenantsBtn)

        #Show Staff Button
        self.staffBtn = QPushButton(self.userBtnGroup)
        self.staffBtn.setObjectName(u"staffBtn")
        self.staffBtn.setCheckable(True)
        self.horizontalLayout_3.addWidget(self.staffBtn)
        self.horizontalLayout_5.addWidget(self.userBtnGroup)

        #User Location Dropdown
        self.userLocationDropdown = QComboBox(self.userToolBar)
        self.userLocationDropdown.setObjectName(u"userLocationDropdown")
        sizePolicy3.setHeightForWidth(self.userLocationDropdown.sizePolicy().hasHeightForWidth())
        self.userLocationDropdown.setSizePolicy(sizePolicy3)
        self.horizontalLayout_5.addWidget(self.userLocationDropdown)

        #User Table Refresh Button
        self.userRefreshBtn = QPushButton(self.userToolBar)
        self.userRefreshBtn.setObjectName(u"userRefreshBtn")
        sizePolicy4.setHeightForWidth(self.userRefreshBtn.sizePolicy().hasHeightForWidth())
        self.userRefreshBtn.setSizePolicy(sizePolicy4)
        self.userRefreshBtn.setMinimumSize(QSize(16, 16))
        self.userRefreshBtn.setBaseSize(QSize(0, 16))
        self.userRefreshBtn.setFont(font)
        self.horizontalLayout_5.addWidget(self.userRefreshBtn)

        #User Table Search Bar
        self.userSearchBar = QLineEdit(self.userToolBar)
        self.userSearchBar.setObjectName(u"userSearchBar")
        sizePolicy3.setHeightForWidth(self.userSearchBar.sizePolicy().hasHeightForWidth())
        self.userSearchBar.setSizePolicy(sizePolicy3)
        self.horizontalLayout_5.addWidget(self.userSearchBar)

        self.horizontalLayout_4.addWidget(self.userToolBar)
        #endregion

        self.stackedWidget.addWidget(self.UserPage)
        #endregion



        #region Connections
        self.userBtn.clicked.connect(lambda : self.switchToUserPage())
        self.apartmentBtn.clicked.connect(lambda : self.switchToApartmentsPage())
        self.reportBtn.clicked.connect(lambda : self.switchToReportsPage())
        self.staffBtn.clicked.connect(lambda: self.switchToStaffTable())
        self.tenantsBtn.clicked.connect(lambda: self.switchToTenantTable())
        self.apartmentSearchBar.textChanged.connect(lambda : self.apartmentTable.search(self.apartmentSearchBar.text()))
        self.userSearchBar.textChanged.connect(lambda : self.staffTable.search(self.userSearchBar.text()))
        self.userSearchBar.textChanged.connect(lambda : self.tenantTable.search(self.userSearchBar.text()))
        #endregion

        self.retranslateUi()

        self.stackedWidget.setCurrentIndex(2)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Administration Dashboard", None))
        #self.occupancyBtn.setText(QCoreApplication.translate("Form", u"Occupancy Levels", None))
        #self.collectionBtn.setText(QCoreApplication.translate("Form", u"Collection Rate", None))
        #self.maintenanceBtn.setText(QCoreApplication.translate("Form", u"Maintenance", None))
        self.apartmentManage.setTitle("")
        self.title_2.setText(QCoreApplication.translate("Form", u"Apartments", None))
        self.apartmentRefresh.setText(QCoreApplication.translate("Form", u"P", None))
        self.apartmentSearchBar.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.manageUsers.setTitle("")
        self.title.setText(QCoreApplication.translate("Form", u"Users", None))
        self.tenantsBtn.setText(QCoreApplication.translate("Form", u"Tenants", None))
        self.staffBtn.setText(QCoreApplication.translate("Form", u"Staff", None))
        self.userRefreshBtn.setText(QCoreApplication.translate("Form", u"P", None))
        self.userSearchBar.setPlaceholderText(QCoreApplication.translate("Form", u"Search", None))
        self.userBtn.setText(QCoreApplication.translate("Form", u"Users", None))
        self.apartmentBtn.setText(QCoreApplication.translate("Form", u"Apartments", None))
        self.reportBtn.setText(QCoreApplication.translate("Form", u"Report", None))
    # retranslateUi

    def switchToUserPage(self):
        self.stackedWidget.setCurrentIndex(2)
    def switchToApartmentsPage(self):
        self.stackedWidget.setCurrentIndex(1)
    def switchToReportsPage(self):
        self.stackedWidget.setCurrentIndex(0)


    #User Table Switching
    def switchToStaffTable(self):
        self.tenantsBtn.setChecked(False)
        self.staffBtn.setChecked(True)
        self.staffTable.show()
        self.tenantTable.hide()
    
    def switchToTenantTable(self):
        self.staffBtn.setChecked(False)
        self.tenantsBtn.setChecked(True)
        self.tenantTable.show()
        self.staffTable.hide()
    
    #Dropdown menu
    def GetLocations(self, locations : list[Location]):
        self.userLocationDropdown.clear()
        self.ReportPage.GetLocations(locations)

        for location in locations:
            self.userLocationDropdown.addItem(location.location_name)
            self.apartmentLocationDropdown.addItem(location.location_name)
    
    def CreateUserTable(self, staffRecords, staffHeaders, tenantRecords : list[Tenant], tenantHeaders ):
        self.staffBtn.setChecked(True)
        self.tenantsBtn.setChecked(False)


        self.staffTable.UpdateTable(staffRecords , staffHeaders)
        self.staffTable.setParent(self.manageUsers)

        self.tenantTable.UpdateTable(tenantRecords,tenantHeaders)
        for tenant in tenantRecords:
            print(tenant.GetDataBaseFormat())
            print("")
        print(tenantHeaders)
        self.tenantTable.setParent(self.manageUsers)   

        self.switchToStaffTable()

    def CreateApartmentTable(self, apartments : list[Apartment], apartmentHeaders : list[str]):
        self.apartmentTable.UpdateTable(apartments, apartmentHeaders)
        self.apartmentTable.setParent(self.apartmentManage)

    #TODO Add Tenant table
    #TODO Make faster for db requests
    #TODO MAKE IT EASIER TOP MAKE REQUIRE TABLES AND NOT REUSE CODE

#endregion


#region Manager Page

class ManagerDashboard(userPage):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        self.titleFrame = QFrame(self)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setGeometry(QRect(0, 0, 831, 61))
        self.titleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.titleFrame)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.contentFrame = QFrame(self)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setGeometry(QRect(0, 60, 831, 521))
        self.contentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.toolBarFrame = QFrame(self.contentFrame)
        self.toolBarFrame.setObjectName(u"toolBarFrame")
        self.toolBarFrame.setGeometry(QRect(0, 0, 831, 48))
        self.toolBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.toolBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toolBarFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.locationBtn = QPushButton(self.toolBarFrame)
        self.locationBtn.setObjectName(u"locationBtn")

        self.horizontalLayout_2.addWidget(self.locationBtn)

        self.apartmentBtn = QPushButton(self.toolBarFrame)
        self.apartmentBtn.setObjectName(u"apartmentBtn")

        self.horizontalLayout_2.addWidget(self.apartmentBtn)

        self.reportsBtn = QPushButton(self.toolBarFrame)
        self.reportsBtn.setObjectName(u"reportsBtn")

        self.horizontalLayout_2.addWidget(self.reportsBtn)

        self.horizontalSpacer = QSpacerItem(545, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.mainStackedWidget = QStackedWidget(self.contentFrame)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.mainStackedWidget.setGeometry(QRect(10, 50, 811, 461))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainStackedWidget.sizePolicy().hasHeightForWidth())
        self.mainStackedWidget.setSizePolicy(sizePolicy)



        self.LocationPage = ManagerLocationPage()
        self.LocationPage.setObjectName(u"LocationPage")
        self.mainStackedWidget.addWidget(self.LocationPage)

        self.ApartmentPage = ManagerApartmentPage()
        self.ApartmentPage.setObjectName(u"ApartmentPage")
        self.mainStackedWidget.addWidget(self.ApartmentPage)


        self.ReportPage = ReportPageWithAllLocations()
        self.ReportPage.setObjectName(u"ReportPage")
        self.mainStackedWidget.addWidget(self.ReportPage)


        self.locationBtn.clicked.connect(lambda : self.switchToLocationPage())
        
        self.apartmentBtn.clicked.connect(lambda : self.switchToApartmentPage())
        
        self.reportsBtn.clicked.connect(lambda : self.switchToReportsPage())

        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Manager", u"Form", None))
        self.title.setText(QCoreApplication.translate("Manager", u"Manager Dashboard", None))
        self.locationBtn.setText(QCoreApplication.translate("Manager", u"Locations", None))
        self.apartmentBtn.setText(QCoreApplication.translate("Manager", u"Apartments", None))
        self.reportsBtn.setText(QCoreApplication.translate("Manager", u"Reports", None))
    # retranslateUi
    def switchToLocationPage(self):
        self.mainStackedWidget.setCurrentIndex(0)

    def switchToApartmentPage(self):
        self.mainStackedWidget.setCurrentIndex(1)

    def switchToReportsPage(self):
        self.mainStackedWidget.setCurrentIndex(2)

    def GetLocations(self, locations : list[Location]):
        self.LocationPage.GetLocations(locations)
        self.ApartmentPage.GetLocations(locations)
        self.ReportPage.GetLocations(locations)


#region Manager Report


#endregion

#region Manager Apartment
class ManagerApartmentPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(811, 463)
        self.ApartmentMainFrame = QFrame(self)
        self.ApartmentMainFrame.setObjectName(u"ApartmentMainFrame")
        self.ApartmentMainFrame.setGeometry(QRect(0, 0, 811, 451))
        self.ApartmentMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ApartmentMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.apartmentCreateFrame = QFrame(self.ApartmentMainFrame)
        self.apartmentCreateFrame.setObjectName(u"apartmentCreateFrame")
        self.apartmentCreateFrame.setGeometry(QRect(280, 2, 303, 441))
        self.apartmentCreateFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.apartmentCreateFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.apartmentCreateFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.apartmentCreateFrame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.locationPrompt = QLabel(self.apartmentCreateFrame)
        self.locationPrompt.setObjectName(u"locationPrompt")

        self.verticalLayout.addWidget(self.locationPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.locationComboBox = QComboBox(self.apartmentCreateFrame)
        self.locationComboBox.setObjectName(u"locationComboBox")

        self.verticalLayout.addWidget(self.locationComboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.roomTypePrompt = QLabel(self.apartmentCreateFrame)
        self.roomTypePrompt.setObjectName(u"roomTypePrompt")

        self.verticalLayout.addWidget(self.roomTypePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.roomTypeComboBox = QComboBox(self.apartmentCreateFrame)
        self.roomTypeComboBox.addItem("")
        self.roomTypeComboBox.addItem("")
        self.roomTypeComboBox.addItem("")
        self.roomTypeComboBox.addItem("")
        self.roomTypeComboBox.setObjectName(u"roomTypeComboBox")

        self.verticalLayout.addWidget(self.roomTypeComboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.monthlyRentPrompt = QLabel(self.apartmentCreateFrame)
        self.monthlyRentPrompt.setObjectName(u"monthlyRentPrompt")

        self.verticalLayout.addWidget(self.monthlyRentPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.monthlyRentInput = QDoubleSpinBox(self.apartmentCreateFrame)
        self.monthlyRentInput.setObjectName(u"monthlyRentInput")
        self.monthlyRentInput.setMaximum(9999999999.989999771118164)
        self.monthlyRentInput.setSingleStep(50.000000000000000)

        self.verticalLayout.addWidget(self.monthlyRentInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.numBedroomsPrompt = QLabel(self.apartmentCreateFrame)
        self.numBedroomsPrompt.setObjectName(u"numBedroomsPrompt")

        self.verticalLayout.addWidget(self.numBedroomsPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.numBedroomsInput = QSpinBox(self.apartmentCreateFrame)
        self.numBedroomsInput.setObjectName(u"numBedroomsInput")
        self.numBedroomsInput.setMinimum(1)
        self.numBedroomsInput.setMaximum(3)

        self.verticalLayout.addWidget(self.numBedroomsInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.numBathroomsPrompt = QLabel(self.apartmentCreateFrame)
        self.numBathroomsPrompt.setObjectName(u"numBathroomsPrompt")

        self.verticalLayout.addWidget(self.numBathroomsPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.numBathroomsInput = QSpinBox(self.apartmentCreateFrame)
        self.numBathroomsInput.setObjectName(u"numBathroomsInput")
        self.numBathroomsInput.setMinimum(1)
        self.numBathroomsInput.setMaximum(3)

        self.verticalLayout.addWidget(self.numBathroomsInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.numApartmentsPrompt = QLabel(self.apartmentCreateFrame)
        self.numApartmentsPrompt.setObjectName(u"numApartmentsPrompt")

        self.verticalLayout.addWidget(self.numApartmentsPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.numApartmentsInput = QSpinBox(self.apartmentCreateFrame)
        self.numApartmentsInput.setObjectName(u"numApartmentsInput")
        self.numApartmentsInput.setMinimum(1)

        self.verticalLayout.addWidget(self.numApartmentsInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.apartmentCreateBtn = QPushButton(self.apartmentCreateFrame)
        self.apartmentCreateBtn.setObjectName(u"apartmentCreateBtn")

        self.verticalLayout.addWidget(self.apartmentCreateBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("ApartmentPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("ApartmentPage", u"Create Apartments", None))
        self.locationPrompt.setText(QCoreApplication.translate("ApartmentPage", u"Location", None))
        self.roomTypePrompt.setText(QCoreApplication.translate("ApartmentPage", u"Room Type", None))
        self.roomTypeComboBox.setItemText(0, QCoreApplication.translate("ApartmentPage", u"Single", None))
        self.roomTypeComboBox.setItemText(1, QCoreApplication.translate("ApartmentPage", u"Double", None))
        self.roomTypeComboBox.setItemText(2, QCoreApplication.translate("ApartmentPage", u"Studio", None))
        self.roomTypeComboBox.setItemText(3, QCoreApplication.translate("ApartmentPage", u"Penthouse", None))

        self.monthlyRentPrompt.setText(QCoreApplication.translate("ApartmentPage", u"Monthly Rent", None))
        self.monthlyRentInput.setPrefix(QCoreApplication.translate("ApartmentPage", u"\u00a3", None))
        self.numBedroomsPrompt.setText(QCoreApplication.translate("ApartmentPage", u"Number of Bedrooms", None))
        self.numBathroomsPrompt.setText(QCoreApplication.translate("ApartmentPage", u"Number Of Bathrooms", None))
        self.numApartmentsPrompt.setText(QCoreApplication.translate("ApartmentPage", u"How many of these apartments would you like to add", None))
        self.numApartmentsInput.setSuffix("")
        self.apartmentCreateBtn.setText(QCoreApplication.translate("ApartmentPage", u"Create", None))
    # retranslateUi
    def GetLocations(self,locations : list[Location]):
        self.locationComboBox.clear()
        for location in locations:
            self.locationComboBox.addItem(location.location_name)
    def Submit(self):
        apartments = []
        #Creates a list of apartments to add depending on the number of apartments requested 
        for i in range(0,int(self.numApartmentsInput.text())):
            apartments.append(Apartment("", "",self.roomTypeComboBox.currentText(),str(self.monthlyRentInput.value()),self.numBedroomsInput.text(),self.numBathroomsInput.text() , False))
        self.monthlyRentInput.setValue(0.000000)
        self.numBedroomsInput.setValue(1)
        self.numBathroomsInput.setValue(1)
        self.numApartmentsInput.setValue(1)
        return apartments
    
#endregion

#region Manager Location 

class ManagerLocationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(811, 461)
        self.locationMainFrame = QFrame(self)
        self.locationMainFrame.setObjectName(u"locationMainFrame")
        self.locationMainFrame.setGeometry(QRect(0, 0, 811, 451))
        self.locationMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.locationMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.locationCreationFrame = QFrame(self.locationMainFrame)
        self.locationCreationFrame.setObjectName(u"locationCreationFrame")
        self.locationCreationFrame.setGeometry(QRect(120, 130, 181, 141))
        self.locationCreationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.locationCreationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.locationCreationFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.locationCreateTitle = QLabel(self.locationCreationFrame)
        self.locationCreateTitle.setObjectName(u"locationCreateTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locationCreateTitle.sizePolicy().hasHeightForWidth())
        self.locationCreateTitle.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.locationCreateTitle)

        self.locationPrompt = QLabel(self.locationCreationFrame)
        self.locationPrompt.setObjectName(u"locationPrompt")
        sizePolicy.setHeightForWidth(self.locationPrompt.sizePolicy().hasHeightForWidth())
        self.locationPrompt.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.locationPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.locationNameInput = QLineEdit(self.locationCreationFrame)
        self.locationNameInput.setObjectName(u"locationNameInput")
        sizePolicy.setHeightForWidth(self.locationNameInput.sizePolicy().hasHeightForWidth())
        self.locationNameInput.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.locationNameInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.locationCreateBtn = QPushButton(self.locationCreationFrame)
        self.locationCreateBtn.setObjectName(u"locationCreateBtn")
        sizePolicy.setHeightForWidth(self.locationCreateBtn.sizePolicy().hasHeightForWidth())
        self.locationCreateBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.locationCreateBtn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.locationManagerCreationFrame = QFrame(self.locationMainFrame)
        self.locationManagerCreationFrame.setObjectName(u"locationManagerCreationFrame")
        self.locationManagerCreationFrame.setGeometry(QRect(490, 70, 156, 340))
        self.locationManagerCreationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.locationManagerCreationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.locationManagerCreationFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.managerCreationTitle = QLabel(self.locationManagerCreationFrame)
        self.managerCreationTitle.setObjectName(u"managerCreationTitle")

        self.verticalLayout_2.addWidget(self.managerCreationTitle)

        self.managerFirstPrompt = QLabel(self.locationManagerCreationFrame)
        self.managerFirstPrompt.setObjectName(u"managerFirstPrompt")

        self.verticalLayout_2.addWidget(self.managerFirstPrompt)

        self.managerFirstInput = QLineEdit(self.locationManagerCreationFrame)
        self.managerFirstInput.setObjectName(u"managerFirstInput")

        self.verticalLayout_2.addWidget(self.managerFirstInput)

        self.managerLastPrompt = QLabel(self.locationManagerCreationFrame)
        self.managerLastPrompt.setObjectName(u"managerLastPrompt")

        self.verticalLayout_2.addWidget(self.managerLastPrompt)

        self.managerLastInput = QLineEdit(self.locationManagerCreationFrame)
        self.managerLastInput.setObjectName(u"managerLastInput")

        self.verticalLayout_2.addWidget(self.managerLastInput)

        self.managerEmailPrompt = QLabel(self.locationManagerCreationFrame)
        self.managerEmailPrompt.setObjectName(u"managerEmailPrompt")

        self.verticalLayout_2.addWidget(self.managerEmailPrompt)

        self.managerEmailInput = QLineEdit(self.locationManagerCreationFrame)
        self.managerEmailInput.setObjectName(u"managerEmailInput")

        self.verticalLayout_2.addWidget(self.managerEmailInput)

        self.managerPasswordPrompt = QLabel(self.locationManagerCreationFrame)
        self.managerPasswordPrompt.setObjectName(u"managerPasswordPrompt")

        self.verticalLayout_2.addWidget(self.managerPasswordPrompt)

        self.managerPasswordInput = QLineEdit(self.locationManagerCreationFrame)
        self.managerPasswordInput.setObjectName(u"managerPasswordInput")

        self.verticalLayout_2.addWidget(self.managerPasswordInput)

        self.managerLocationPrompt = QLabel(self.locationManagerCreationFrame)
        self.managerLocationPrompt.setObjectName(u"managerLocationPrompt")

        self.verticalLayout_2.addWidget(self.managerLocationPrompt)

        self.managerLocationComboBox = QComboBox(self.locationManagerCreationFrame)
        self.managerLocationComboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.managerLocationComboBox)

        self.managerCreationBtn = QPushButton(self.locationManagerCreationFrame)
        self.managerCreationBtn.setObjectName(u"managerCreationBtn")

        self.verticalLayout_2.addWidget(self.managerCreationBtn)


        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("LocationPage", u"Form", None))
        self.locationCreateTitle.setText(QCoreApplication.translate("LocationPage", u"Add New Location", None))
        self.locationPrompt.setText(QCoreApplication.translate("LocationPage", u"Location Name", None))
        self.locationCreateBtn.setText(QCoreApplication.translate("LocationPage", u"Create", None))
        self.managerCreationTitle.setText(QCoreApplication.translate("LocationPage", u"Create Location Manager", None))
        self.managerFirstPrompt.setText(QCoreApplication.translate("LocationPage", u"First Name", None))
        self.managerLastPrompt.setText(QCoreApplication.translate("LocationPage", u"Last Name", None))
        self.managerEmailPrompt.setText(QCoreApplication.translate("LocationPage", u"Email", None))
        self.managerPasswordPrompt.setText(QCoreApplication.translate("LocationPage", u"Password", None))
        self.managerLocationPrompt.setText(QCoreApplication.translate("LocationPage", u"Location", None))
        self.managerCreationBtn.setText(QCoreApplication.translate("LocationPage", u"Add Manager", None))
    # retranslateUi

    def SubmitLocation(self):
        newLocation = Location("", self.locationNameInput.text(), "")
        self.locationNameInput.clear()
        return newLocation
    def SubmitLocationManager(self):
        manager = User("",self.managerFirstInput.text(),self.managerLastInput.text(),self.managerEmailInput.text(),self.managerPasswordInput.text(),"Manager","") #Does not have an ID as must be requested from the main to maintain the level of abstraction
        self.managerFirstInput.clear()
        self.managerLastInput.clear()
        self.managerEmailInput.clear()
        self.managerPasswordInput.clear()
        return manager
    def GetLocations(self,locations : list[Location]):
        self.managerLocationComboBox.clear()
        for location in locations:
            self.managerLocationComboBox.addItem(location.location_name)

#endregion
#endregion

#region Report Pages
class ReportPage(QWidget):
    def __init__(self):
        super().__init__()

        self.Graphs = QFrame(self)
        self.Graphs.setObjectName(u"Graphs")
        self.Graphs.setGeometry(QRect(180, 50, 411, 361))
        self.Graphs.setFrameShape(QFrame.Shape.StyledPanel)
        self.Graphs.setFrameShadow(QFrame.Shadow.Raised)
        self.graphsStackedWidget = QStackedWidget(self.Graphs)
        self.graphsStackedWidget.setObjectName(u"graphsStackedWidget")
        self.graphsStackedWidget.setGeometry(QRect(10, 60, 391, 291))
        self.Occupancy = PieChart((),(), "Occupancy Levels")
        self.Occupancy.setObjectName(u"Occupancy")
        self.graphsStackedWidget.addWidget(self.Occupancy)
        self.MaintenceCost = PieChart((),(), "Maintenance Costs")
        self.MaintenceCost.setObjectName(u"MaintenceCost")
        self.graphsStackedWidget.addWidget(self.MaintenceCost)
        self.CollectionRate = PieChart((),(), "Collection Rates")
        self.CollectionRate.setObjectName(u"CollectionRate")
        self.graphsStackedWidget.addWidget(self.CollectionRate)
        self.btnGroup = QFrame(self.Graphs)
        self.btnGroup.setObjectName(u"btnGroup")
        self.btnGroup.setGeometry(QRect(10, 10, 391, 44))
        self.btnGroup.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnGroup.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnGroup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.occupancyBtn = QPushButton(self.btnGroup)
        self.occupancyBtn.setObjectName(u"occupancyBtn")

        self.horizontalLayout.addWidget(self.occupancyBtn)

        self.collectionBtn = QPushButton(self.btnGroup)
        self.collectionBtn.setObjectName(u"collectionBtn")
        self.horizontalLayout.addWidget(self.collectionBtn)

        self.maintenanceBtn = QPushButton(self.btnGroup)
        self.maintenanceBtn.setObjectName(u"maintenanceBtn")

        self.horizontalLayout.addWidget(self.maintenanceBtn)

        #Connections
        self.occupancyBtn.clicked.connect( lambda : self.switchToOccupanyLevels())
        self.collectionBtn.clicked.connect( lambda : self.switchToCollectionRate())
        self.maintenanceBtn.clicked.connect( lambda : self.switchToMaintenance())

        self.retranslate()
    
    def retranslate(self):
        self.occupancyBtn.setText(QCoreApplication.translate("Form", u"Occupancy Levels", None))
        self.collectionBtn.setText(QCoreApplication.translate("Form", u"Collection Rate", None))
        self.maintenanceBtn.setText(QCoreApplication.translate("Form", u"Maintenance", None))


    def switchToOccupanyLevels(self):
        self.graphsStackedWidget.setCurrentIndex(0)

    def switchToCollectionRate(self):
        self.graphsStackedWidget.setCurrentIndex(2)

    def switchToMaintenance(self):
        self.graphsStackedWidget.setCurrentIndex(1)

    def CreatePieCharts(self,occupancy : PieChart , collection : PieChart, maintenance : PieChart):
        self.CreateOccupancyLevels(occupancy)
        self.CreateMaintenance(maintenance)
        self.CreateCollectionRates(collection)

    def CreateOccupancyLevels(self, pie :PieChart):
        self.Occupancy.setChart(pie.chart())
        self.Occupancy.setGeometry(QRect(10, 60, 391, 291))
        self.Occupancy.setParent(self.graphsStackedWidget)
        print("Created Occupancy Pie")

    def CreateCollectionRates(self, pie :PieChart):
        self.CollectionRate.setChart(pie.chart())
        self.CollectionRate.setGeometry(QRect(10, 60, 391, 291))
        self.CollectionRate.setParent(self.graphsStackedWidget)
        print("Created Collection Pie")

    def CreateMaintenance(self, pie :PieChart):
        self.MaintenceCost.setChart(pie.chart())
        self.MaintenceCost.setGeometry(QRect(10, 60, 391, 291))
        self.MaintenceCost.setParent(self.graphsStackedWidget)
        print("Created Maintenence Pie")



class ReportPageWithAllLocations(QWidget):
        def __init__(self):
            super().__init__()
            self.Graphs = QFrame(self)
            self.Graphs.setObjectName(u"Graphs")
            self.Graphs.setGeometry(QRect(180, 50, 411, 361))
            self.Graphs.setFrameShape(QFrame.Shape.StyledPanel)
            self.Graphs.setFrameShadow(QFrame.Shadow.Raised)
            self.graphsStackedWidget = QStackedWidget(self.Graphs)
            self.graphsStackedWidget.setObjectName(u"graphsStackedWidget")
            self.graphsStackedWidget.setGeometry(QRect(10, 60, 391, 291))
            self.Occupancy = PieChart((),(), "Occupancy Levels")
            self.Occupancy.setObjectName(u"Occupancy")
            self.graphsStackedWidget.addWidget(self.Occupancy)
            self.MaintenceCost = PieChart((),(), "Maintenance Costs")
            self.MaintenceCost.setObjectName(u"MaintenceCost")
            self.graphsStackedWidget.addWidget(self.MaintenceCost)
            self.CollectionRate = PieChart((),(), "Collection Rates")
            self.CollectionRate.setObjectName(u"CollectionRate")
            self.graphsStackedWidget.addWidget(self.CollectionRate)
            self.btnGroup = QFrame(self.Graphs)
            self.btnGroup.setObjectName(u"btnGroup")
            self.btnGroup.setGeometry(QRect(10, 10, 391, 44))
            self.btnGroup.setFrameShape(QFrame.Shape.StyledPanel)
            self.btnGroup.setFrameShadow(QFrame.Shadow.Raised)
            self.horizontalLayout = QHBoxLayout(self.btnGroup)
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.occupancyBtn = QPushButton(self.btnGroup)
            self.occupancyBtn.setObjectName(u"occupancyBtn")

            self.horizontalLayout.addWidget(self.occupancyBtn)

            self.collectionBtn = QPushButton(self.btnGroup)
            self.collectionBtn.setObjectName(u"collectionBtn")

            self.horizontalLayout.addWidget(self.collectionBtn)

            self.maintenanceBtn = QPushButton(self.btnGroup)
            self.maintenanceBtn.setObjectName(u"maintenanceBtn")

            self.horizontalLayout.addWidget(self.maintenanceBtn)

            self.reportLocationDropdown = QComboBox(self.btnGroup)
            self.reportLocationDropdown.setObjectName(u"reportLocationDropdown")
            self.horizontalLayout.addWidget(self.reportLocationDropdown)
            #Connections
            self.occupancyBtn.clicked.connect(lambda : self.switchToOccupanyLevels())
            self.collectionBtn.clicked.connect(lambda : self.switchToCollectionRate())
            self.maintenanceBtn.clicked.connect(lambda : self.switchToMaintenance())

            self.retranslate()
        def retranslate(self):
            self.occupancyBtn.setText(QCoreApplication.translate("Form", u"Occupancy Levels", None))
            self.collectionBtn.setText(QCoreApplication.translate("Form", u"Collection Rate", None))
            self.maintenanceBtn.setText(QCoreApplication.translate("Form", u"Maintenance", None))


        def switchToOccupanyLevels(self):
            self.graphsStackedWidget.setCurrentIndex(0)

        def switchToCollectionRate(self):
            self.graphsStackedWidget.setCurrentIndex(2)

        def switchToMaintenance(self):
            self.graphsStackedWidget.setCurrentIndex(1)


        
        def CreatePieCharts(self,occupancy : PieChart , collection : PieChart, maintenance : PieChart):
            self.CreateOccupancyLevels(occupancy)
            self.CreateMaintenance(maintenance)
            self.CreateCollectionRates(collection)

        def CreateOccupancyLevels(self, pie :PieChart):
                self.Occupancy.setChart(pie.chart())
                self.Occupancy.setGeometry(QRect(10, 60, 391, 291))
                self.Occupancy.setParent(self.graphsStackedWidget)
                print("Created Occupancy Pie")

        def CreateCollectionRates(self, pie :PieChart):
            self.CollectionRate.setChart(pie.chart())
            self.CollectionRate.setGeometry(QRect(10, 60, 391, 291))
            self.CollectionRate.setParent(self.graphsStackedWidget)
            print("Created Collection Pie")

        def CreateMaintenance(self, pie :PieChart):
            self.MaintenceCost.setChart(pie.chart())
            self.MaintenceCost.setGeometry(QRect(10, 60, 391, 291))
            self.MaintenceCost.setParent(self.graphsStackedWidget)
            print("Created Maintenence Pie")

        def GetLocations(self,locations : list[Location]):
                self.reportLocationDropdown.clear()
                for location in locations:
                    self.reportLocationDropdown.addItem(location.location_name)

#endregion



#region Maintenance Dashboard

class MaintenanceDashboard(userPage):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        
        self.Main = QFrame(self)
        self.Main.setObjectName(u"Main")
        self.Main.setGeometry(QRect(0, 80, 831, 501))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main.sizePolicy().hasHeightForWidth())
        self.Main.setSizePolicy(sizePolicy)
        self.Main.setFrameShape(QFrame.Shape.StyledPanel)
        self.Main.setFrameShadow(QFrame.Shadow.Raised)



        self.tableToolBar = QFrame(self.Main)
        self.tableToolBar.setObjectName(u"tableToolBar")
        self.tableToolBar.setGeometry(QRect(0, 0, 831, 71))
        sizePolicy.setHeightForWidth(self.tableToolBar.sizePolicy().hasHeightForWidth())
        self.tableToolBar.setSizePolicy(sizePolicy)
        self.tableToolBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableToolBar.setFrameShadow(QFrame.Shadow.Raised)
        self.titleBar = QFrame(self)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 831, 81))




        self.tableFrame = QFrame(self.Main)
        self.tableFrame.setObjectName(u"tableFrame")
        self.tableFrame.setGeometry(QRect(0, 70, 831, 431))
        self.tableFrame.setFrameShadow(QFrame.Shadow.Raised)
        sizePolicy.setHeightForWidth(self.tableFrame.sizePolicy().hasHeightForWidth())
        self.tableFrame.setSizePolicy(sizePolicy)
        self.tableFrame.setFrameShape(QFrame.Shape.StyledPanel)

        self.table = Table([],[])
        self.table.setParent(self.tableFrame)
        self.table.setObjectName(u"tenantTable")
        self.table.setGeometry(QRect(10, 30, 821, 430))


        self.searchBar = QLineEdit(self.tableToolBar)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setGeometry(QRect(610, 10, 113, 22))

        
        sizePolicy.setHeightForWidth(self.titleBar.sizePolicy().hasHeightForWidth())
        self.titleBar.setSizePolicy(sizePolicy)
        self.titleBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(self.titleBar)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi()

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MaintenanceDashboard", u"Form", None))
        self.title.setText(QCoreApplication.translate("MaintenanceDashboard", u"Maintenance Dashboard", None))
    # retranslateUi


class MaintenanceDialogBox(QDialog):
    def __init__(self, startedDate : str, currentMaintenanceNotes : str , costRepair : int):
        super().__init__()
        self.resize(400, 300)
        self.startedDate = startedDate
        self.currentMaintenanceNotes = currentMaintenanceNotes
        self.currentCostRepair = costRepair

        self.wizardFrame = QFrame(self)
        self.wizardFrame.setObjectName(u"wizardFrame")
        self.wizardFrame.setGeometry(QRect(0, 0, 450, 400))
        self.wizardFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.wizardFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.wizardFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QLabel(self.wizardFrame)
        self.title.setObjectName(u"title")

        self.verticalLayout_3.addWidget(self.title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame = QFrame(self.wizardFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maintenanceNotesInput = QTextEdit(self.frame)
        self.maintenanceNotesInput.setObjectName(u"maintenanceNotesInput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintenanceNotesInput.sizePolicy().hasHeightForWidth())
        self.maintenanceNotesInput.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.maintenanceNotesInput)

        self.addNotesBtn = QPushButton(self.frame)
        self.addNotesBtn.setObjectName(u"addNotesBtn")

        self.verticalLayout.addWidget(self.addNotesBtn)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.wizardFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.costPrompt = QLabel(self.frame_2)
        self.costPrompt.setObjectName(u"costPrompt")

        self.verticalLayout_2.addWidget(self.costPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.costInput = QDoubleSpinBox(self.frame_2)
        self.costInput.setObjectName(u"costInput")
        self.costInput.setMaximum(99999.000000000000000)
        self.costInput.setMinimum(self.currentCostRepair)

        self.verticalLayout_2.addWidget(self.costInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.buttonsFrame = QFrame(self.wizardFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy1)
        self.buttonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.completeRequestBtn = QPushButton(self.buttonsFrame)
        self.completeRequestBtn.setObjectName(u"completeRequestBtn")

        self.horizontalLayout.addWidget(self.completeRequestBtn)


        self.verticalLayout_3.addWidget(self.buttonsFrame)


        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Maintenance Wizard", None))
        self.maintenanceNotesInput.setDocumentTitle(QCoreApplication.translate("Dialog", u"Maitenance Notes", None))
        self.maintenanceNotesInput.setPlaceholderText(QCoreApplication.translate("Dialog", u"Please add maintenance notes", None))
        if self.currentMaintenanceNotes != "":
            self.maintenanceNotesInput.setText(self.currentMaintenanceNotes)
        self.addNotesBtn.setText(QCoreApplication.translate("Dialog", u"Add Notes", None))
        self.costPrompt.setText(QCoreApplication.translate("Dialog", u"Cost Of Request", None))
        self.costInput.setPrefix(QCoreApplication.translate("Dialog", u"\u00a3", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add Cost", None))
        self.completeRequestBtn.setText(QCoreApplication.translate("Dialog", u"Complete Request", None))
    # retranslateUi

    def AddNotes(self):
        if self.currentMaintenanceNotes != self.maintenanceNotesInput.toPlainText():
            self.currentMaintenanceNotes == self.maintenanceNotesInput.toPlainText()
            return self.currentMaintenanceNotes
        
    def AddCost(self):
        if self.currentCostRepair > float(self.costInput.cleanText()): 
            return float(self.costInput.cleanText())

         

        
#endregion