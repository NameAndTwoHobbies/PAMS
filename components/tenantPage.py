import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCharts import *
from components.ErrorBoxes import ErrorBox
from models import Entities, domain_models
from models.domain_models import *
import controllers.inboxController as inboxController
from Table import Table

expandingPolicy      = QSizePolicy(QSizePolicy.Policy.Expanding,       QSizePolicy.Policy.Expanding)
expandingFixedPolicy      = QSizePolicy(QSizePolicy.Policy.Expanding,       QSizePolicy.Policy.Fixed)
preferredPolicy = QSizePolicy(QSizePolicy.Policy.Preferred,       QSizePolicy.Policy.Preferred)
preferredFixedPolicy = QSizePolicy(QSizePolicy.Policy.Preferred,       QSizePolicy.Policy.Fixed)
fixedPolicy          = QSizePolicy(QSizePolicy.Policy.Fixed,           QSizePolicy.Policy.Fixed)
minExpandingPolicy   = QSizePolicy(QSizePolicy.Policy.MinimumExpanding,QSizePolicy.Policy.Preferred)

class TenantPage(QWidget):
    def __init__(self):
        super().__init__()
    
    def AddPageDetail():
        pass

class TenantOverviewPage(TenantPage):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"OverviewPage")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        #Quick info section
        self.quickInfoSection = QFrame()
        self.quickInfoSection.setObjectName(u"quickInfoSection")
        #self.quickInfoSection.setSizePolicy(expandingPolicy)
        self.quickInfoSection.setMinimumSize(QSize(0, 0))
        self.quickInfoSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.quickInfoSection.setFrameShadow(QFrame.Shadow.Raised)

        #Greeting Section
        self.greetingSection = QFrame(self.quickInfoSection)
        self.greetingSection.setObjectName(u"greetingSection")
        self.greetingSection.setGeometry(QRect(10, 10, 254, 266))
        self.greetingSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.greetingSection.setFrameShadow(QFrame.Shadow.Raised)
        self.greeting = QLabel(self.greetingSection)
        self.greeting.setObjectName(u"greeting")
        self.greeting.setGeometry(QRect(10, 10, 91, 16))
        self.userName = QLabel(self.greetingSection) 
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(10, 30, 181, 31))
        self.userName.setScaledContents(False)

        #Next Rent Section
        self.nextRentSection = QFrame(self.quickInfoSection)
        self.nextRentSection.setObjectName(u"nextRentSection")
        self.nextRentSection.setGeometry(QRect(270, 10, 253, 266))
        self.nextRentSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.nextRentSection.setFrameShadow(QFrame.Shadow.Raised)
        self.nextRentTitle = QLabel(self.nextRentSection)
        self.nextRentTitle.setObjectName(u"nextRentTitle")
        self.nextRentTitle.setGeometry(QRect(10, 10, 101, 16))
        self.priceNextRent = QLabel(self.nextRentSection) 
        self.priceNextRent.setObjectName(u"priceNextRent")
        self.priceNextRent.setGeometry(QRect(10, 30, 181, 31))
        self.priceNextRent.setMinimumSize(QSize(181, 31))
        self.priceNextRent.setMaximumSize(QSize(181, 31))
        self.dueDate = QLabel(self.nextRentSection) 
        self.dueDate.setObjectName(u"dueDate")
        self.dueDate.setGeometry(QRect(10, 70, 231, 16))
        self.dueDate.setMinimumSize(QSize(191, 16))

        #Outstanding Maintenance Section
        self.outstandingMaintenanceSection = QFrame(self.quickInfoSection)
        self.outstandingMaintenanceSection.setObjectName(u"outstandingMaintenanceSection")
        self.outstandingMaintenanceSection.setGeometry(QRect(529, 10, 254, 266))
        self.outstandingMaintenanceSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.outstandingMaintenanceSection.setFrameShadow(QFrame.Shadow.Raised)
        self.outstandingTitle = QLabel(self.outstandingMaintenanceSection)
        self.outstandingTitle.setObjectName(u"outstandingTitle")
        self.outstandingTitle.setGeometry(QRect(10, 10, 188, 16))
        self.numRequests = QLabel(self.outstandingMaintenanceSection)
        self.numRequests.setObjectName(u"numRequests")
        self.numRequests.setGeometry(QRect(10, 30, 181, 31))
        self.numRequests.setMinimumSize(QSize(181, 31))
        self.numRequests.setMaximumSize(QSize(181, 31))

        self.verticalLayout.addWidget(self.quickInfoSection)

        self.tenancyInfoSection = QFrame()
        self.tenancyInfoSection.setObjectName(u"tenancyInfoSection")
        self.tenancyInfoSection.setMinimumSize(QSize(0, 0))
        self.tenancyInfoSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.tenancyInfoSection.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.tenancyInfoSection)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.apartmentInfo = QFrame(self.tenancyInfoSection)
        self.apartmentInfo.setObjectName(u"apartmentInfo")
        #self.apartmentInfo.setSizePolicy(expandingPolicy)
        self.apartmentInfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.apartmentInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.apartmentInfoTitle = QLabel(self.apartmentInfo)
        self.apartmentInfoTitle.setObjectName(u"apartmentInfoTitle")
        self.apartmentInfoTitle.setGeometry(QRect(10, 0, 164, 16))
        self.image = QWidget(self.apartmentInfo)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(10, 20, 341, 151))

        self.horizontalLayout_4.addWidget(self.apartmentInfo)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.notifications = QFrame(self.tenancyInfoSection)
        self.notifications.setObjectName(u"helpInfo")
        self.notifications.setFrameShape(QFrame.Shape.StyledPanel)
        self.notifications.setFrameShadow(QFrame.Shadow.Raised)
        self.notificationTable = QWidget(self.notifications)
        self.notificationTable.setObjectName(u"contactsTable")
        self.notificationTable.setGeometry(QRect(10, 20, 341, 151))
        self.helpLabel = QLabel(self.notifications)
        self.helpLabel.setObjectName(u"helpLabel")
        self.helpLabel.setGeometry(QRect(10, 0, 164, 16))

        self.horizontalLayout_4.addWidget(self.notifications)


        self.verticalLayout.addWidget(self.tenancyInfoSection)

        self.userManagementSection = QFrame()
        self.userManagementSection.setObjectName(u"userManagementSection")
        #self.userManagementSection.setSizePolicy(preferredFixedPolicy)
        self.userManagementSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.userManagementSection.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5 = QHBoxLayout(self.userManagementSection)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.logoutBtn = QPushButton(self.userManagementSection)
        self.logoutBtn.setObjectName(u"pushButton_2")


        self.leaveTenancyBtn = QPushButton(self.userManagementSection)
        self.leaveTenancyBtn.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.logoutBtn)
        self.horizontalLayout_5.addWidget(self.leaveTenancyBtn)


        self.verticalLayout.addWidget(self.userManagementSection)

        self.setLayout(self.verticalLayout)

    def retranslateUi(self):
        self.greeting.setText(QCoreApplication.translate("Form", u"Welcome back,", None))
        self.userName.setText(QCoreApplication.translate("Form", u"UserName", None))
        self.nextRentTitle.setText(QCoreApplication.translate("Form", u"Next Rent Payment", None))
        self.priceNextRent.setText(QCoreApplication.translate("Form", u"Price in pounds", None))
        self.dueDate.setText(QCoreApplication.translate("Form", u"Due Date", None))
        self.outstandingTitle.setText(QCoreApplication.translate("Form", u"Outstanding Maintenance Requests", None))
        self.numRequests.setText(QCoreApplication.translate("Form", u"Number Requests", None))
        self.apartmentInfoTitle.setText(QCoreApplication.translate("Form", u"Apartment Name and Location", None))
        self.helpLabel.setText(QCoreApplication.translate("Form", u"Notifications", None))
        self.logoutBtn.setText(QCoreApplication.translate("Form", u"Log Out", None))
        self.leaveTenancyBtn.setText(QCoreApplication.translate("Form", u"Leave Tenancy", None))
    
    def AddPageDetail(self,userName : str, price: str, dueDate: str , numRequests: str, nameApartment : str, nameLocation : str):
        self.userName.setText(userName)
        self.priceNextRent.setText(str(price))
        self.dueDate.setText(dueDate)
        self.numRequests.setText(str(numRequests))
        self.apartmentInfoTitle.setText("Location: " + str(nameLocation) + " In Apartment: "  + str(nameApartment))
    

class TenantPaymentsPage(TenantPage):
    def __init__(self):
        super().__init__()
        self.resize(809, 622)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.setLayout(self.horizontalLayout)
        self.prevPayments = QGroupBox(self)
        self.prevPayments.setObjectName(u"prevPayments")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.prevPayments.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.prevPayments)
        self.verticalLayout_2 = QVBoxLayout(self.prevPayments)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        
        self.paymentHistory = Table([],[])
        self.paymentHistory.setParent(self.prevPayments)
        self.paymentHistory.setObjectName(u"paymentHistory")


        self.verticalLayout_2.addWidget(self.paymentHistory)



        self.paymentsNow = QGroupBox(self)
        self.paymentsNow.setObjectName(u"paymentsNow")
        self.horizontalLayout.addWidget(self.paymentsNow)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.paymentHistory.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.paymentsNow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.currentDueLabel = QLabel(self.paymentsNow)
        self.currentDueLabel.setObjectName(u"currentDueLabel")

        self.verticalLayout.addWidget(self.currentDueLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.CurrentDue = QLabel(self.paymentsNow)
        self.CurrentDue.setObjectName(u"CurrentDue")

        self.verticalLayout.addWidget(self.CurrentDue, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cardNumPrompt = QLabel(self.paymentsNow)
        self.cardNumPrompt.setObjectName(u"cardNumPrompt")

        self.verticalLayout.addWidget(self.cardNumPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cardNumInput = QLineEdit(self.paymentsNow)
        self.cardNumInput.setObjectName(u"cardNumInput")
        self.cardNumInput.setMaxLength(16)

        self.verticalLayout.addWidget(self.cardNumInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.cvvPrompt = QLabel(self.paymentsNow)
        self.cvvPrompt.setObjectName(u"cvvPrompt")

        self.verticalLayout.addWidget(self.cvvPrompt, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.cvvInput = QLineEdit(self.paymentsNow)
        self.cvvInput.setObjectName(u"cvvInput")
        self.cvvInput.setMaxLength(3)

        self.verticalLayout.addWidget(self.cvvInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.expDatePrompt = QLabel(self.paymentsNow)
        self.expDatePrompt.setObjectName(u"expDatePrompt")

        self.verticalLayout.addWidget(self.expDatePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

        self.expDateInput = QDateEdit(self.paymentsNow)
        self.expDateInput.setObjectName(u"expDateInput")

        self.verticalLayout.addWidget(self.expDateInput, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.payNowBtn = QPushButton(self.paymentsNow)
        self.payNowBtn.setObjectName(u"payNowBtn")

        self.verticalLayout.addWidget(self.payNowBtn, 0, Qt.AlignmentFlag.AlignHCenter)



        self.retranslateUi()
    # setupUi

    def retranslateUi(self):
        self.prevPayments.setTitle(QCoreApplication.translate("PaymentsPage", u"Previous Payments", None))
        self.paymentsNow.setTitle(QCoreApplication.translate("PaymentsPage", u"PayNow", None))
        self.currentDueLabel.setText(QCoreApplication.translate("PaymentsPage", u"Current Amount Due", None))
        self.CurrentDue.setText(QCoreApplication.translate("PaymentsPage", u"CURRENT AMOUNT", None))
        self.cardNumPrompt.setText(QCoreApplication.translate("PaymentsPage", u"Card Number", None))
        self.cardNumInput.setInputMask("")
        self.cardNumInput.setPlaceholderText("")
        self.cvvPrompt.setText(QCoreApplication.translate("PaymentsPage", u"CVV", None))
        self.expDatePrompt.setText(QCoreApplication.translate("PaymentsPage", u"Expiry Date", None))
        self.expDateInput.setDisplayFormat(QCoreApplication.translate("PaymentsPage", u"MM/yyyy", None))
        self.payNowBtn.setText(QCoreApplication.translate("PaymentsPage", u"Pay", None))
    # retranslateUi

    def SubmitPayment(self):
        if self.CurrentDue.text() != "£0":
            self.cardNumInput
            self.expDateInput
            self.cvvInput
            return self.cardNumInput.text(),self.expDateInput.text(),self.cvvInput.text()

class TenantAccountPage(TenantPage):
        def __init__(self):
            super().__init__()
            self.resize(811,621)

            self.horizontalLayout_3 = QHBoxLayout(self)
            self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
            self.UserInfo = QFrame(self)
            self.UserInfo.setObjectName(u"UserInfo")
            self.UserInfo.setFrameShape(QFrame.Shape.Box)
            self.UserInfo.setFrameShadow(QFrame.Shadow.Plain)
            #self.UserInfo.setSizePolicy(expandingPolicy)
            self.verticalLayout_7 = QVBoxLayout(self.UserInfo)
            self.verticalLayout_7.setObjectName(u"verticalLayout_7")
            self.formTitle = QLabel(self.UserInfo)
            self.formTitle.setObjectName(u"formTitle")
            #self.formTitle.setSizePolicy(preferredFixedPolicy)

            self.verticalLayout_7.addWidget(self.formTitle, 0, Qt.AlignmentFlag.AlignHCenter)

            self.signInForm = QFrame(self.UserInfo)
            self.signInForm.setObjectName(u"signInForm")
            self.signInForm.setFrameShape(QFrame.Shape.NoFrame)
            self.signInForm.setFrameShadow(QFrame.Shadow.Raised)
            self.verticalLayout_3 = QVBoxLayout(self.signInForm)
            self.verticalLayout_3.setObjectName(u"verticalLayout_3")
            self.firstNamePrompt = QLabel(self.signInForm)
            self.firstNamePrompt.setObjectName(u"firstNamePrompt")

            self.verticalLayout_3.addWidget(self.firstNamePrompt)

            self.firstNameInput = QLineEdit(self.signInForm)
            self.firstNameInput.setObjectName(u"firstNameInput")
            #self.firstNameInput.setSizePolicy(preferredPolicy)

            self.verticalLayout_3.addWidget(self.firstNameInput)

            self.lastNamePrompt = QLabel(self.signInForm)
            self.lastNamePrompt.setObjectName(u"lastNamePrompt")

            self.verticalLayout_3.addWidget(self.lastNamePrompt)

            self.lastNameInput = QLineEdit(self.signInForm)
            self.lastNameInput.setObjectName(u"lastNameInput")
            #self.lastNameInput.setSizePolicy(expandingPolicy)

            self.verticalLayout_3.addWidget(self.lastNameInput)

            self.emailPrompt = QLabel(self.signInForm)
            self.emailPrompt.setObjectName(u"emailPrompt")

            self.verticalLayout_3.addWidget(self.emailPrompt)

            self.emailInput = QLineEdit(self.signInForm)
            self.emailInput.setObjectName(u"emailInput")
            #self.emailInput.setSizePolicy(expandingPolicy)

            self.verticalLayout_3.addWidget(self.emailInput)

            self.passwordPrompt = QLabel(self.signInForm)
            self.passwordPrompt.setObjectName(u"passwordPrompt")

            self.verticalLayout_3.addWidget(self.passwordPrompt)

            self.passwordInput = QLineEdit(self.signInForm)
            self.passwordInput.setObjectName(u"passwordInput")
            #self.passwordInput.setSizePolicy(expandingPolicy)

            self.verticalLayout_3.addWidget(self.passwordInput)

            self.nationalNumPrompt = QLabel(self.signInForm)
            self.nationalNumPrompt.setObjectName(u"nationalNumPrompt")

            self.verticalLayout_3.addWidget(self.nationalNumPrompt)

            self.nationalNumInput = QLineEdit(self.signInForm)
            self.nationalNumInput.setObjectName(u"nationalNumInput")
            #self.nationalNumInput.setSizePolicy(expandingPolicy)

            self.verticalLayout_3.addWidget(self.nationalNumInput)

            self.phoneNumPrompt = QLabel(self.signInForm)
            self.phoneNumPrompt.setObjectName(u"phoneNumPrompt")

            self.verticalLayout_3.addWidget(self.phoneNumPrompt)

            self.phoneNumInput = QLineEdit(self.signInForm)
            self.phoneNumInput.setObjectName(u"phoneNumInput")
            #self.phoneNumInput.setSizePolicy(expandingPolicy)

            self.verticalLayout_3.addWidget(self.phoneNumInput)

            self.occupationPrompt = QLabel(self.signInForm)
            self.occupationPrompt.setObjectName(u"occupationPrompt")

            self.verticalLayout_3.addWidget(self.occupationPrompt)

            self.occupationComboBox = QComboBox(self.signInForm)
            self.occupationComboBox.addItem("")
            self.occupationComboBox.addItem("")
            self.occupationComboBox.addItem("")
            self.occupationComboBox.addItem("")
            self.occupationComboBox.setObjectName(u"occupationComboBox")
            #self.occupationComboBox.setSizePolicy(expandingPolicy)
            #self.occupationComboBox.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

            self.verticalLayout_3.addWidget(self.occupationComboBox)


            self.verticalLayout_7.addWidget(self.signInForm, 0, Qt.AlignmentFlag.AlignHCenter)

            self.submitBtn = QPushButton(self.UserInfo)
            self.submitBtn.setObjectName(u"submitBtn")

            self.verticalLayout_7.addWidget(self.submitBtn, 0, Qt.AlignmentFlag.AlignHCenter)


            self.horizontalLayout_3.addWidget(self.UserInfo)

            self.requirements = QFrame(self)
            self.requirements.setObjectName(u"requirements")
            self.requirements.setFrameShape(QFrame.Shape.Box)
            self.requirements.setFrameShadow(QFrame.Shadow.Plain)
            #self.requirements.setSizePolicy(expandingPolicy)
            self.verticalLayout_8 = QVBoxLayout(self.requirements)
            self.verticalLayout_8.setSpacing(0)
            self.verticalLayout_8.setObjectName(u"verticalLayout_8")
            self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.requirementsLabel = QLabel(self.requirements)
            self.requirementsLabel.setObjectName(u"requirementsLabel")
            #self.requirementsLabel.setSizePolicy(preferredPolicy)

            self.verticalLayout_8.addWidget(self.requirementsLabel, 0, Qt.AlignmentFlag.AlignHCenter)

            self.reqForm = QFrame(self.requirements)
            self.reqForm.setObjectName(u"reqForm")
            #self.reqForm.setSizePolicy(preferredPolicy)
            self.reqForm.setFrameShape(QFrame.Shape.NoFrame)
            self.reqForm.setFrameShadow(QFrame.Shadow.Plain)
            self.verticalLayout_5 = QVBoxLayout(self.reqForm)
            self.verticalLayout_5.setObjectName(u"verticalLayout_5")
            self.locationPrompt = QLabel(self.reqForm)
            #self.locationPrompt.setSizePolicy(preferredFixedPolicy)

            self.verticalLayout_5.addWidget(self.locationPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

            self.locationComboBox = QComboBox(self.reqForm)
            self.locationComboBox.setObjectName(u"locationComboBox")
            #self.locationComboBox.setSizePolicy(expandingPolicy)

            self.verticalLayout_5.addWidget(self.locationComboBox, 0, Qt.AlignmentFlag.AlignHCenter)

            self.roomTypePrompt = QLabel(self.reqForm)
            self.roomTypePrompt.setObjectName(u"roomTypePrompt")
            #self.roomTypePrompt.setSizePolicy(preferredFixedPolicy)

            self.verticalLayout_5.addWidget(self.roomTypePrompt, 0, Qt.AlignmentFlag.AlignHCenter)

            self.roomTypeComboBox = QComboBox(self.reqForm)
            self.roomTypeComboBox.addItem("")
            self.roomTypeComboBox.addItem("")
            self.roomTypeComboBox.addItem("")
            self.roomTypeComboBox.addItem("")
            self.roomTypeComboBox.setObjectName(u"roomTypeComboBox")
            sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
            sizePolicy5.setHorizontalStretch(0)
            sizePolicy5.setVerticalStretch(0)
            #self.roomTypeComboBox.setSizePolicy(sizePolicy5)

            self.verticalLayout_5.addWidget(self.roomTypeComboBox, 0, Qt.AlignmentFlag.AlignHCenter)

            self.maxRentPrompt = QLabel(self.reqForm)
            self.maxRentPrompt.setObjectName(u"maxRentPrompt")
            #self.maxRentPrompt.setSizePolicy(preferredFixedPolicy)

            self.verticalLayout_5.addWidget(self.maxRentPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

            self.maxRentInput = QSpinBox(self.reqForm)
            self.maxRentInput.setObjectName(u"maxRentInput")
            #self.maxRentInput.setSizePolicy(expandingPolicy)
            self.maxRentInput.setWrapping(False)
            self.maxRentInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.maxRentInput.setProperty(u"showGroupSeparator", False)
            self.maxRentInput.setMaximum(2000)
            self.maxRentInput.setSingleStep(100)

            self.verticalLayout_5.addWidget(self.maxRentInput, 0, Qt.AlignmentFlag.AlignHCenter)

            self.numRoomsPrompt = QLabel(self.reqForm)
            self.numRoomsPrompt.setObjectName(u"numRoomsPrompt")
            #self.numRoomsPrompt.setSizePolicy(preferredFixedPolicy)

            self.verticalLayout_5.addWidget(self.numRoomsPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

            self.numRoomsInput = QSpinBox(self.reqForm)
            self.numRoomsInput.setObjectName(u"numRoomsInput")
            #self.numRoomsInput.setSizePolicy(expandingPolicy)
            self.numRoomsInput.setMinimum(1)
            self.numRoomsInput.setMaximum(3)

            self.verticalLayout_5.addWidget(self.numRoomsInput, 0, Qt.AlignmentFlag.AlignHCenter)

            self.numBathroomsPrompt = QLabel(self.reqForm)
            self.numBathroomsPrompt.setObjectName(u"numBathroomsPrompt")
            #self.numBathroomsPrompt.setSizePolicy(preferredFixedPolicy)

            self.verticalLayout_5.addWidget(self.numBathroomsPrompt, 0, Qt.AlignmentFlag.AlignHCenter)

            self.numBathroomsInput = QSpinBox(self.reqForm)
            self.numBathroomsInput.setObjectName(u"numBathroomsInput")
            #self.numBathroomsInput.setSizePolicy(expandingPolicy)
            self.numBathroomsInput.setMinimum(1)
            self.numBathroomsInput.setMaximum(4)

            self.verticalLayout_5.addWidget(self.numBathroomsInput, 0, Qt.AlignmentFlag.AlignHCenter)


            self.verticalLayout_8.addWidget(self.reqForm)

            self.submitReqsBtn = QPushButton(self.requirements)
            self.submitReqsBtn.setObjectName(u"submitReqs")


            self.verticalLayout_8.addWidget(self.submitReqsBtn, 0, Qt.AlignmentFlag.AlignHCenter)


            self.horizontalLayout_3.addWidget(self.requirements)

            self.retranslateUi()
        def retranslateUi(self):
            

            self.formTitle.setText(QCoreApplication.translate("Form", u"Change User Info", None))
            self.firstNamePrompt.setText(QCoreApplication.translate("Form", u"First Name", None))
            self.lastNamePrompt.setText(QCoreApplication.translate("Form", u"Last Name", None))
            self.emailPrompt.setText(QCoreApplication.translate("Form", u"Email", None))
            self.passwordPrompt.setText(QCoreApplication.translate("Form", u"Password", None))
            self.nationalNumPrompt.setText(QCoreApplication.translate("Form", u"National Insurance Number", None))
            self.phoneNumPrompt.setText(QCoreApplication.translate("Form", u"Phone Number", None))
            self.occupationPrompt.setText(QCoreApplication.translate("Form", u"Occupation", None))
            self.occupationComboBox.setItemText(0, QCoreApplication.translate("Form", u"Employed", None))
            self.occupationComboBox.setItemText(1, QCoreApplication.translate("Form", u"Student", None))
            self.occupationComboBox.setItemText(2, QCoreApplication.translate("Form", u"Part-Time", None))
            self.occupationComboBox.setItemText(3, QCoreApplication.translate("Form", u"Unemployed", None))

            self.submitBtn.setText(QCoreApplication.translate("Form", u"Change", None))
            self.requirementsLabel.setText(QCoreApplication.translate("Form", u"Set Requirements", None))
            self.locationPrompt.setText(QCoreApplication.translate("Form", u"Location", None))
            self.roomTypePrompt.setText(QCoreApplication.translate("Form", u"Room Type", None))
            self.roomTypeComboBox.setItemText(0, QCoreApplication.translate("Form", u"Single", None))
            self.roomTypeComboBox.setItemText(1, QCoreApplication.translate("Form", u"Double", None))
            self.roomTypeComboBox.setItemText(2, QCoreApplication.translate("Form", u"Studio", None))
            self.roomTypeComboBox.setItemText(3, QCoreApplication.translate("Form", u"Penthouse", None))

            self.maxRentPrompt.setText(QCoreApplication.translate("Form", u"Maximum Rent", None))
            self.maxRentInput.setPrefix(QCoreApplication.translate("Form", u"\u00a3", None))
            self.numRoomsPrompt.setText(QCoreApplication.translate("Form", u"Number of Rooms", None))
            self.numBathroomsPrompt.setText(QCoreApplication.translate("Form", u"Number of Bathrooms", None))
            self.submitReqsBtn.setText(QCoreApplication.translate("Form", u"Set", None))
        # retranslateUi

        def SubmitRequirements(self):
            reqs = Entities.Requirements("","", "", self.roomTypeComboBox.currentText(), self.maxRentInput.cleanText(), self.numRoomsInput.text(),self.numBathroomsInput.text())
            self.locationComboBox.setCurrentIndex(0)
            self.roomTypeComboBox.setCurrentIndex(0)
            self.maxRentInput.setValue(0.000000)
            self.numRoomsInput.setValue(1)
            self.numBathroomsInput.setValue(1)
            return reqs
        
        def GetLocations(self,locations : list[Location]):
            self.locationComboBox.clear()


            for location in locations:
                self.locationComboBox.addItem(location.location_name)
        
        def SubmitNewUserInfo(self):
            return Entities.Tenant("",self.firstNameInput.text(),self.lastNameInput.text(), self.nationalNumInput.text(),self.emailInput.text(), self.passwordInput.text() ,self.phoneNumInput.text(),self.occupationComboBox.currentText(), 'Null')
        
        def AddPageDetail(self,firstName, lastName,email,national, phone):
            self.firstNameInput.setText(firstName)
            self.lastNameInput.setText(lastName)
            self.emailInput.setText(email)
            self.nationalNumInput.setText(national)
            self.phoneNumInput.setText(phone)

class EarlyLeaveDateDialog(QDialog):
    def __init__(self, contract: Contract, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Early Leave Date")
        self.setMinimumWidth(400)

        # ── Work out the date boundaries ──────────────────────────────────────
        # Earliest allowed: strictly more than one month away
        self._min_date = QDate.currentDate().addMonths(1).addDays(1)

        # Latest allowed: the contract end_date.
        # The DB driver returns end_date as a Python datetime/date object,
        # so we convert to string "YYYY-MM-DD" then parse into QDate.
        end_str = str(contract.end_date)[:10]          # keeps "YYYY-MM-DD"
        self._max_date = QDate.fromString(end_str, "yyyy-MM-dd")

        # ── Build the UI ───────────────────────────────────────────────────────
        layout = QVBoxLayout(self)

        # Explanatory label
        info = QLabel(
            f"Choose your move-out date.\n"
            f"It must be after {self._min_date.toString('dd MMM yyyy')} "
            f"and no later than {self._max_date.toString('dd MMM yyyy')}."
        )
        info.setWordWrap(True)
        layout.addWidget(info)

        # The calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(self._min_date)
        self.calendar.setMaximumDate(self._max_date)
        self.calendar.setSelectedDate(self._min_date)   # sensible default
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)

        # Selected date readout
        self._selected_label = QLabel(
            f"Selected: {self._min_date.toString('dd MMM yyyy')}"
        )
        layout.addWidget(self._selected_label)

        # Update the label whenever the user clicks a different date
        self.calendar.selectionChanged.connect(self._on_date_changed)

        # Confirm / Cancel buttons
        btn_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    # ── Slot: keep the label in sync with the calendar ────────────────────────
    def _on_date_changed(self):
        date = self.calendar.selectedDate()
        self._selected_label.setText(f"Selected: {date.toString('dd MMM yyyy')}")

    # ── Public helper: returns the chosen date as "YYYY-MM-DD" string ─────────
    def GetSelectedDate(self) -> str:
        return self.calendar.selectedDate().toString("yyyy-MM-dd")
#region Notifications Dashboard

class TenantNotificationsDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("NotificationsDashboard")
        self.resize(831, 487)

        self.controller = None
        self.currentTenant = None

        # Inbox List
        self.previewList = QScrollArea(self)
        self.previewList.setGeometry(QRect(20, 90, 171, 381))
        self.previewList.setWidgetResizable(True)

        self.inbox = QWidget()
        self.inboxLayout = QVBoxLayout(self.inbox)
        self.inboxLayout.setContentsMargins(5, 5, 5, 5)
        self.inboxLayout.setSpacing(5)
        self.inboxLayout.addStretch()  # keeps items at top
        self.previewList.setWidget(self.inbox)

        # Message View
        self.expandedMessage = QScrollArea(self)
        self.expandedMessage.setGeometry(QRect(220, 90, 581, 381))
        self.expandedMessage.setWidgetResizable(True)

        self.message = QWidget()
        self.messageLayout = QVBoxLayout(self.message)
        self.messageLayout.setContentsMargins(10, 10, 10, 10)

        self.messageBody = QLabel("")
        self.messageBody.setWordWrap(True)
        self.messageLayout.addWidget(self.messageBody)

        self.expandedMessage.setWidget(self.message)

        # Header
        self.header = QGroupBox(self)
        self.header.setGeometry(QRect(20, 0, 781, 80))

        self.personal = QCheckBox(self.header)
        self.personal.setGeometry(QRect(90, 50, 85, 20))
        self.personal.setText("Personal")
        self.personal.setChecked(True)

        self.public = QCheckBox(self.header)
        self.public.setGeometry(QRect(10, 50, 85, 20))
        self.public.setText("Public")
        self.public.setChecked(True)

        self.label = QLabel(self.header)
        self.label.setGeometry(QRect(10, 10, 200, 31))
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("Your Inbox")

        self.subject = QLabel(self.header)
        self.subject.setGeometry(QRect(200, 50, 511, 20))
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.subject.setFont(font1)
        self.subject.setText("Message Subject")

        self.setWindowTitle(
            QCoreApplication.translate(
                "NotificationsDashboard", "Notifications", None
            )
        )

        QMetaObject.connectSlotsByName(self)
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("NotificationsDashboard", "Notifications", None))
        self.personal.setText(QCoreApplication.translate("NotificationsDashboard", "Personal", None))
        self.public.setText(QCoreApplication.translate("NotificationsDashboard", "Public", None))
        self.label.setText(QCoreApplication.translate("NotificationsDashboard", "Your Inbox", None))
        self.subject.setText(QCoreApplication.translate("NotificationsDashboard", "Message Subject", None))
    
    def setTenant(self, tenant: Entities.Tenant):
        self.currentTenant = tenant
        if self.controller is None:
            self.controller = inboxController.InboxController(self, tenant.id, location_id=1)

#endregion
