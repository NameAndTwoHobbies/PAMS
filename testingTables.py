from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from uiMainWindow import Ui_MainWindow
from db import *
from ErrorBoxes import *
from MyWidgets import Table


# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'FrontDeskDashcjvnfN.ui'
#
# Created by: Qt User Interface Compiler version 6.10.1
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QRect
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox,
                            QLabel, QLineEdit, QPushButton,
                            QTableWidget, QTableWidgetItem, QWidget)


class Ui_Form(QWidget):
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

        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
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




class mainScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PAMS")
        self.setMaximumSize(self.size())

        # Testing Page
        self.TestingPage.testBtn1.clicked.connect(lambda: self.getTenantsTable())
        self.TestingPage.testBtn2.clicked.connect(lambda: self.getLocationsTable())
        # self.TestingPage.testBtn3.clicked.connect(lambda : )
        # self.TestingPage.testBtn4.clicked.connect(lambda : )



    def switchTestingPage(self):
        self.stackedView.setCurrentIndex(5)
    # endregion

    def getTenantsTable(self):
        records = GetTenants()
        headers = GetHeaders("tenants")
        table = Table(records, headers)
        return table

    def getLocationsTable(self):
        records = GetLocations()
        headers = GetHeaders("locations")
        self.table = Table(records, headers)
        self.table.show()


# region App
app = QApplication()

# Creates a main window and places the ui created in designer onto it
mainWindow = mainScreen()

records = GetTenants()
headers = GetHeaders("tenants")
test = Ui_Form()
test.tenantTable.setColumnCount(len(headers))
test.tenantTable.setHorizontalHeaderLabels(headers)
test.tenantTable.setRowCount(len(records))
for rowIndex, rowData in enumerate(records):
    for colIndex, value in enumerate(rowData):
        item = QTableWidgetItem(str(value))
        test.tenantTable.setItem(rowIndex, colIndex, item)


mainWindow.stackedView.addWidget(test)
mainWindow.stackedView.setCurrentIndex(7)
mainWindow.show()

app.exec()

# endregion
