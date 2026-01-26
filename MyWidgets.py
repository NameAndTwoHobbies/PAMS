import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import * 

#region Fonts

font1 = QFont()
font1.setFamilies([u"Arial"])
font1.setPointSize(18)

font2 = QFont()
font2.setFamilies([u"Arial"])
font2.setPointSize(18)



font3 = QFont()
font3.setFamilies([u"Arial"])
font3.setPointSize(40)
font3.setBold(True)

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
        self.title.setFont(font3)

       

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
            

            self.loginGroup.setFont(font1)
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

            self.passwordInput.setFont(font2)

            self.customerPassword = QLabel(self.loginGroup)
            self.customerPassword.setObjectName(u"password")
            self.customerPassword.setGeometry(QRect(360, 270, 93, 30))


            #title
            self.title = QLabel(self.loginGroup)
            self.title.setObjectName(u"title")
            self.title.setGeometry(QRect(240, 90, 297, 53))
            
            self.title.setFont(font3)

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


#region Admin Login

class AdminLoginPage(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setObjectName(u"AdminLogin")

        # Group Box
        self.adminGroup = QGroupBox(self)
        self.adminGroup.setObjectName(u"adminGroup")
        self.adminGroup.setGeometry(QRect(10, 10, 811, 561))

        
        self.adminGroup.setFont(font1)
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
        
        self.passwordInput.setFont(font1)

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


        self.title.setFont(font3)

        
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

