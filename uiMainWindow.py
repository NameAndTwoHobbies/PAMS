# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMJOjaG.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
from MyWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(843, 634)
        self.View = QWidget(MainWindow)
        self.View.setObjectName(u"View")
        self.frame = QFrame(self.View)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 843, 634))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBar = QFrame(self.frame)
        self.toolBar.setObjectName(u"toolBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMaximumSize(QSize(843, 53))
        self.toolBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.toolBar.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.toolBar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(740, 0, 79, 24))

        self.verticalLayout.addWidget(self.toolBar)

        self.content = QFrame(self.frame)
        self.content.setObjectName(u"content")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy1)
        self.content.setMaximumSize(QSize(16777215, 581))
        self.content.setFrameShape(QFrame.Shape.StyledPanel)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedView = QStackedWidget(self.content)
        self.stackedView.setObjectName(u"stackedView")
        self.stackedView.setGeometry(QRect(0, 0, 823, 581))
        sizePolicy.setHeightForWidth(self.stackedView.sizePolicy().hasHeightForWidth())
        self.stackedView.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.content)
        

        #region Page 1 Welcome
        self.Welcome = WelcomePage()
        self.stackedView.addWidget(self.Welcome)
        #endregion

        #region Page 2 Customer Login
        self.CustLogin = CustomerLoginPage()
        self.stackedView.addWidget(self.CustLogin)
        #endregion

        #region Page 3 Admin
        self.StaffLogin = AdminLoginPage()
        self.stackedView.addWidget(self.StaffLogin)
        #endregion

        #region Page 4 Customer Dashboard
        self.CustDash = TenantDashboard()
        self.stackedView.addWidget(self.CustDash)

        #endregion

        #region Page 5 Sign Up Customer
        self.CustSignUp = SignUpPage()
        self.stackedView.addWidget(self.CustSignUp)
        #end region
       
        #region Page 6 Testing Page
        self.TestingPage = TestPage()
        self.stackedView.addWidget(self.TestingPage)
        #end region

        
        #region Page 7 Detailed Sign Up Customer
        self.DetailedSignUp = SignUpDetailed()
        self.stackedView.addWidget(self.DetailedSignUp)
        #end region
        
        #region Page 8 Front Desk Dashboard
        self.FrontDeskDash = FrontDeskDashboard()
        self.stackedView.addWidget(self.FrontDeskDash)
        #endregion
        
        #region Page 9 Finance Dashboard
        self.FinanceDash = FinanceDashboard()
        self.stackedView.addWidget(self.FinanceDash)
        #endregion

        #region Page 10 Admin Dashboard
        self.AdminDash = AdminDashboard()
        self.stackedView.addWidget(self.AdminDash)
        #endregion

        #region Page 11 Manager Dashboard
        self.ManagerDash = ManagerDashboard()
        self.stackedView.addWidget(self.ManagerDash)
        #endregion
        
        MainWindow.setCentralWidget(self.View)

        self.retranslateUi(MainWindow)

        self.stackedView.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))

        #retranslate ui for the pages
        self.Welcome.retranslateUi()

        self.CustLogin.retranslateUi()

        self.StaffLogin.retranslateUi()

        self.CustDash.retranslateUi()

        self.CustSignUp.retranslateUi()

        self.TestingPage.retranslateUi()

        self.DetailedSignUp.retranslateUi()
        
        self.FrontDeskDash.retranslateUi()

        self.FinanceDash.retranslateUi()

        self.AdminDash.retranslateUi()
    # retranslateUi

