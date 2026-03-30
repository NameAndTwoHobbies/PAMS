import sys
import random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtCharts import *
from components.ErrorBoxes import ErrorBox
from models import domain_models
from models.domain_models import *
import controllers.inboxController as inboxController

class TenantOverviewPage(QWidget):
    def __init__(self):

        super().__init__()
        self.setObjectName(u"OverviewPage")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        #Quick info section
        self.quickInfoSection = QFrame()
        self.quickInfoSection.setObjectName(u"quickInfoSection")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHeightForWidth(self.quickInfoSection.sizePolicy().hasHeightForWidth())
        self.quickInfoSection.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.apartmentInfo.sizePolicy().hasHeightForWidth())
        self.apartmentInfo.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHeightForWidth(self.userManagementSection.sizePolicy().hasHeightForWidth())
        self.userManagementSection.setSizePolicy(sizePolicy1)
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
    
    def UpdateTenantInfomation(self,userName : str, price: str, dueDate: str , numRequests: str, nameApartment : str, nameLocation : str):
        self.userName.setText(userName)
        self.priceNextRent.setText(price)
        self.dueDate.setText(dueDate)
        self.numRequests.setText(numRequests)
        self.apartmentInfoTitle.setText(nameApartment + " " + nameLocation)

        
class TenantPaymentsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName(u"paymentsPage")
        self.horizontalLayout_6 = QHBoxLayout(self)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pageSection = QFrame(self)
        self.pageSection.setObjectName(u"pageSection")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pageSection.sizePolicy().hasHeightForWidth())
        self.pageSection.setSizePolicy(sizePolicy2)
        self.pageSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.pageSection.setFrameShadow(QFrame.Shadow.Raised)
        self.searchBarSection = QFrame(self.pageSection)
        self.searchBarSection.setObjectName(u"searchBarSection")
        self.searchBarSection.setGeometry(QRect(0, 0, 791, 36))
        self.searchBarSection.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchBarSection.setFrameShadow(QFrame.Shadow.Raised)
        self.paymentLabel = QLabel(self.searchBarSection)
        self.paymentLabel.setObjectName(u"paymentLabel")
        self.paymentLabel.setGeometry(QRect(10, 10, 127, 16))
        self.payementHistoryTable = QWidget(self.pageSection)
        self.payementHistoryTable.setObjectName(u"payementHistoryTable")
        self.payementHistoryTable.setGeometry(QRect(0, 40, 781, 581))

        self.horizontalLayout_6.addWidget(self.pageSection)
    def retranslateUi(self):
        self.paymentLabel.setText(QCoreApplication.translate("Form", u"Previous Rent Payments", None))

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
    
    def setTenant(self, tenant: domain_models.Tenant):
        self.currentTenant = tenant
        if self.controller is None:
            self.controller = inboxController.InboxController(self, tenant.tenant_id, tenant.get_location().location_id)

#endregion
