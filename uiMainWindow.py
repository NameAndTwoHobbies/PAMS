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
        self.stackedView = QStackedWidget(self.View)
        self.stackedView.setObjectName(u"stackedView")
        self.stackedView.setGeometry(QRect(10, -2, 831, 581))
        self.stackedView.setMouseTracking(False)
        self.stackedView.setFrameShadow(QFrame.Shadow.Plain)
        self.stackedView.setLineWidth(0)

        #region Page 1 Welcome
        self.Welcome = WelcomePage()
        self.stackedView.addWidget(self.Welcome)
        #endregion

        #region Page 2 Customer Login
        self.CustLogin = CustomerLoginPage()
        self.stackedView.addWidget(self.CustLogin)
        #endregion

        #region Page 3 Admin
        self.AdminLogin = AdminLoginPage()
        self.stackedView.addWidget(self.AdminLogin)
        #endregion

        #region Page 4 Customer Dashboard
        self.CustDash = Dashboard()
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
        self.DetailedSignUp = DetailedSignUpPage()
        self.stackedView.addWidget(self.DetailedSignUp)
        #end region

        
        MainWindow.setCentralWidget(self.View)

        self.retranslateUi(MainWindow)

        self.stackedView.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        #retranslate ui for the pages
        self.Welcome.retranslateUi()

        self.CustLogin.retranslateUi()

        self.AdminLogin.retranslateUi()

        self.CustDash.retranslateUi()

        self.CustSignUp.retranslateUi()

        self.TestingPage.retranslateUi()

        self.DetailedSignUp.retranslateUi()

    # retranslateUi

