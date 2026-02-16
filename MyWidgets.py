import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 
from ErrorBoxes import ErrorBox

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


#endregion

#In order to have an efficient and scalable app pages will be seperated into individual widgets
#This prevents accidental variable changes and makes the application easier to debug and develop

#region Welcome Page

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
        
        self.passwordInput.setFont(text)

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
#endregion 


#region Client Dashboard

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardXBxFzf.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# Dashboard is a page the client dashboard widgets including the following:
# A side bar with Account, Lease, Payments and Complaints buttons
# A stacked widget that contains the corrosponding pages to these buttons
# The pages inside will have database connectivity to collect the infomation

class Dashboard(QWidget):
        def __init__(self):
            super().__init__()
            self.resize(805, 581)


            #StackWidget / Dashboard Content
            self.stackedWidget = QStackedWidget(self)
            self.stackedWidget.setObjectName(u"stackedWidget")
            self.stackedWidget.setGeometry(QRect(110, 70, 681, 501))
            self.stackedWidget.setStyleSheet("background-color: green;")

            #Default Page
            self.defaultPage = QWidget()
            self.defaultPage.setObjectName(u"defaultPage")
            self.defaultTitle = QLabel(self.defaultPage)
            self.defaultTitle.setObjectName(u"defaultTitle")
            self.defaultTitle.setGeometry(QRect(270, 220, 44, 16))
            self.stackedWidget.addWidget(self.defaultPage)
            


            #Account Page
            self.accountPage = QWidget()
            self.accountPage.setObjectName(u"accountPage")
            self.label_2 = QLabel(self.accountPage)
            self.label_2.setObjectName(u"label_2")
            self.label_2.setGeometry(QRect(270, 220, 44, 16))
            self.stackedWidget.addWidget(self.accountPage)

            #Lease Page
            self.leasePage = QWidget()
            self.leasePage.setObjectName(u"leasePage")
            self.label_3 = QLabel(self.leasePage)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setGeometry(QRect(250, 250, 30, 16))
            self.stackedWidget.addWidget(self.leasePage)

            #Payment Page
            self.paymentPage = QWidget()
            self.paymentPage.setObjectName(u"paymentPage")
            self.label_4 = QLabel(self.paymentPage)
            self.label_4.setObjectName(u"label_4")
            self.label_4.setGeometry(QRect(280, 240, 52, 16))
            self.stackedWidget.addWidget(self.paymentPage)

            #Complaints Page
            self.complaintsPage = QWidget()
            self.complaintsPage.setObjectName(u"complaintsPage")
            self.label = QLabel(self.complaintsPage)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(270, 190, 58, 16))
            self.stackedWidget.addWidget(self.complaintsPage)


            #Sidebar

            self.sideBar = QWidget(self)
            self.sideBar.setObjectName(u"sideBar")
            self.sideBar.setGeometry(QRect(10, 10, 91, 561))
            self.sideBar.setStyleSheet("background-color: green;")

            self.gridLayout = QGridLayout(self.sideBar)
            self.gridLayout.setObjectName(u"gridLayout")


            #Account Button
            self.accountBtn = QPushButton(self.sideBar)
            self.accountBtn.setObjectName(u"accountBtn")
            self.accountBtn.setCheckable(True)
            self.accountBtn.setAutoExclusive(True)
            self.accountBtn.clicked.connect(self.switchAccountPage)

            #Lease Button
            self.leaseBtn = QPushButton(self.sideBar)
            self.leaseBtn.setObjectName(u"leaseBtn")
            self.leaseBtn.setCheckable(True)
            self.leaseBtn.setAutoExclusive(True)
            self.leaseBtn.clicked.connect(self.switchLeasePage)


            #Payment Button
            self.paymentsBtn = QPushButton(self.sideBar)
            self.paymentsBtn.setObjectName(u"paymentsBtn")
            self.paymentsBtn.setCheckable(True)
            self.paymentsBtn.setAutoExclusive(True)
            self.paymentsBtn.clicked.connect(self.switchPaymentsPage)


            #Complaints Button
            self.complaintsBtn = QPushButton(self.sideBar)
            self.complaintsBtn.setObjectName(u"complaintsBtn")
            self.complaintsBtn.setCheckable(True)
            self.complaintsBtn.setAutoExclusive(True)
            self.complaintsBtn.clicked.connect(self.switchComplaintsPage)


            #Adding to Layout
            self.gridLayout.addWidget(self.accountBtn, 0, 0, 1, 1)
            self.gridLayout.addWidget(self.leaseBtn, 1, 0, 1, 1)
            self.gridLayout.addWidget(self.paymentsBtn, 2, 0, 1, 1)
            self.gridLayout.addWidget(self.complaintsBtn, 3, 0, 1, 1)

            self.stackedWidget.setCurrentIndex(0)


        def retranslateUi(self):
            self.leaseBtn.setText(QCoreApplication.translate("dashboard", u"Lease", None))
            self.paymentsBtn.setText(QCoreApplication.translate("dashboard", u"Payments", None))
            self.accountBtn.setText(QCoreApplication.translate("dashboard", u"Account", None))
            self.complaintsBtn.setText(QCoreApplication.translate("dashboard", u"Complaints", None))
            self.defaultTitle.setText(QCoreApplication.translate("dashboard", u"Default", None))
            self.label_2.setText(QCoreApplication.translate("dashboard", u"Account", None))
            self.label_3.setText(QCoreApplication.translate("dashboard", u"Lease", None))
            self.label_4.setText(QCoreApplication.translate("dashboard", u"payments", None))
            self.label.setText(QCoreApplication.translate("dashboard", u"complaints", None))
        # retranslateUi

        def switchAccountPage(self):
            self.stackedWidget.setCurrentIndex(1)

        def switchLeasePage(self):
            self.stackedWidget.setCurrentIndex(2)

        def switchPaymentsPage(self):
            self.stackedWidget.setCurrentIndex(3)
        
        def switchComplaintsPage(self):
            self.stackedWidget.setCurrentIndex(4)
    




#endregion

#region Database Widgets


class Table(QTableWidget):
    def __init__(self, records, headers):
        super().__init__()
        print(len(headers))
        print(len(records))
        lenHeader = len(headers)
        lenRecords = len(records)
        self.setColumnCount(lenHeader)
        self.setRowCount(lenRecords)
        self.verticalHeader().setVisible(False)
        for header in range(0,lenHeader):
            self.setHorizontalHeaderItem(header,QTableWidgetItem(str(headers[header][0])))
        
        for x in range(0, lenRecords):
            for y in range(0,len(records[x])):
                self.setItem(x,y,QTableWidgetItem(str(records[x][y])))
    



        

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

class DetailedSignUpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(817, 587)
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.setGeometry(QRect(0, 10, 812, 571))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(103, 16))
        self.title.setFont(title)
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(164, 16))
        self.label.setFont(heading)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(807, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.emailPrompt = QLabel(self)
        self.emailPrompt.setObjectName(u"emailPrompt")
        self.emailPrompt.setMinimumSize(QSize(29, 16))
        self.emailPrompt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.emailPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emailPrompt.setFont(text)

        self.verticalLayout.addWidget(self.emailPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.emailInput = QLineEdit(self)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setMinimumSize(QSize(150, 22))
        self.emailInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.emailInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.firstNamePrompt = QLabel(self)
        self.firstNamePrompt.setObjectName(u"firstNamePrompt")
        self.firstNamePrompt.setMinimumSize(QSize(57, 16))
        self.firstNamePrompt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.firstNamePrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.firstNamePrompt.setFont(text)

        self.verticalLayout.addWidget(self.firstNamePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.firstNameInput = QLineEdit(self)
        self.firstNameInput.setObjectName(u"firstNameInput")
        self.firstNameInput.setMinimumSize(QSize(116, 22))
        self.firstNameInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.firstNameInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lastNamePrompt = QLabel(self)
        self.lastNamePrompt.setObjectName(u"lastNamePrompt")
        self.lastNamePrompt.setMinimumSize(QSize(56, 16))
        self.lastNamePrompt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lastNamePrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lastNamePrompt.setFont(text)

        self.verticalLayout.addWidget(self.lastNamePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lastNamInput = QLineEdit(self)
        self.lastNamInput.setObjectName(u"lastNamInput")
        self.lastNamInput.setMinimumSize(QSize(116, 22))
        self.lastNamInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lastNamInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.passwordPrompt = QLabel(self)
        self.passwordPrompt.setObjectName(u"passwordPrompt")
        self.passwordPrompt.setMinimumSize(QSize(50, 16))
        self.passwordPrompt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.passwordPrompt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passwordPrompt.setFont(text)

        self.verticalLayout.addWidget(self.passwordPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.passwordInput = QLineEdit(self)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(116, 22))
        self.passwordInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.passwordInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(807, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(79, 24))
        self.pushButton.setFont(text)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

    def retranslateUi(self):
        self.title.setText(QCoreApplication.translate("SignUpDetailed", u"Welcome New User", None))
        self.label.setText(QCoreApplication.translate("SignUpDetailed", u"Please fill in the following form", None))
        self.emailPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Email", None))
        self.emailInput.setText("")
        self.emailInput.setPlaceholderText(QCoreApplication.translate("SignUpDetailed", u"#ADD-EMAIL-HERE#", None))
        self.firstNamePrompt.setText(QCoreApplication.translate("SignUpDetailed", u"First Name", None))
        self.firstNameInput.setPlaceholderText(QCoreApplication.translate("SignUpDetailed", u"eg. Peter", None))
        self.lastNamePrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Last Name", None))
        self.lastNamInput.setText("")
        self.lastNamInput.setPlaceholderText(QCoreApplication.translate("SignUpDetailed", u"eg. Smith", None))
        self.passwordPrompt.setText(QCoreApplication.translate("SignUpDetailed", u"Password", None))
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("SignUpDetailed", u"Sign Up", None))
    # retranslateUi
#endregion

#region Front Desk Dashboard
class FrontDeskDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(831, 581)
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(330, 30, 118, 16))
        self.registerTenants = QGroupBox(self)
        self.registerTenants.setObjectName(u"registerTenants")
        self.registerTenants.setGeometry(QRect(10, 50, 731, 241))
        self.firstNameInput = QLineEdit(self.registerTenants)
        self.firstNameInput.setObjectName(u"firstNameInput")
        self.firstNameInput.setGeometry(QRect(20, 40, 113, 21))
        self.lastNameInput = QLineEdit(self.registerTenants)
        self.lastNameInput.setObjectName(u"lastNameInput")
        self.lastNameInput.setGeometry(QRect(20, 130, 113, 21))
        self.emailInput = QLineEdit(self.registerTenants)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(20, 200, 113, 21))
        self.nationalInsuranceInput = QLineEdit(self.registerTenants)
        self.nationalInsuranceInput.setObjectName(u"nationalInsuranceInput")
        self.nationalInsuranceInput.setGeometry(QRect(270, 40, 161, 21))
        self.phoneNumberInput = QLineEdit(self.registerTenants)
        self.phoneNumberInput.setObjectName(u"phoneNumberInput")
        self.phoneNumberInput.setGeometry(QRect(270, 130, 161, 21))
        self.occupationDropdown = QComboBox(self.registerTenants)
        self.occupationDropdown.addItem("")
        self.occupationDropdown.addItem("")
        self.occupationDropdown.addItem("")
        self.occupationDropdown.addItem("")
        self.occupationDropdown.setObjectName(u"occupationDropdown")
        self.occupationDropdown.setGeometry(QRect(260, 200, 171, 26))
        self.submitButton = QPushButton(self.registerTenants)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(560, 40, 81, 26))
        self.errorMessage = QWidget(self.registerTenants)
        self.errorMessage.setObjectName(u"errorMessage")
        self.errorMessage.setGeometry(QRect(480, 80, 231, 141))
        self.manageTenants = QGroupBox(self)
        self.manageTenants.setObjectName(u"manageTenants")
        self.manageTenants.setGeometry(QRect(10, 320, 731, 241))
        self.errorMessage_2 = QWidget(self.manageTenants)
        self.errorMessage_2.setObjectName(u"errorMessage_2")
        self.errorMessage_2.setGeometry(QRect(480, 80, 231, 141))
        self.tenantTable = QTableWidget(self.manageTenants)
        self.tenantTable.setObjectName(u"tenantTable")
        self.tenantTable.setGeometry(QRect(20, 20, 701, 211))


    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Front Desk Dashboard", None))
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
        self.occupationDropdown.setItemText(2, QCoreApplication.translate("Form", u"Full-Time Employed", None))
        self.occupationDropdown.setItemText(3, QCoreApplication.translate("Form", u"Part-Time Employed", None))

        self.occupationDropdown.setPlaceholderText(QCoreApplication.translate("Form", u"Occupation", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.manageTenants.setTitle(QCoreApplication.translate("Form", u"Manage Tenants", None))
    # retranslateUi

    def UpdateTenants(self, records, headers):
        self.tenantTable = Table(records,headers)
        self.tenantTable.setParent(self.manageTenants)
        self.tenantTable.setObjectName(u"tenantTable")
        self.tenantTable.setGeometry(QRect(20, 20, 701, 211))
        



#endregion
