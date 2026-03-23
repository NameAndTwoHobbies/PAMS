
from PySide6.QtCore import QCoreApplication, QRect, Qt
from PySide6.QtWidgets import (QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QVBoxLayout)


class ErrorMessage():
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description


# Error boxs are pop out dialog boxes used when an error has occurred on when the user needs to be notified urgently
# Error Boxes take a ErrorMessage as an argument and apply styling and layout to the data
class ErrorBox(QDialog):
    def __init__(self, error: ErrorMessage):
        super().__init__()
        self.error = error
        self.resize(400, 300)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)

        self.buttonBox.accepted.connect(self.reject)

        self.buttonBox.rejected.connect(self.reject)

        self.groupBox = QGroupBox(self)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 221))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setFlat(True)

        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.errorTitle = QLabel(self.groupBox)
        self.errorTitle.setObjectName(u"errorTitle")
        self.errorTitle.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.errorTitle)

        self.errorDescription = QLabel(self.groupBox)
        self.errorDescription.setObjectName(u"errorDescription")
        self.errorDescription.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.errorDescription)


        self.retranslateUi(self)
    # setupUi

    def retranslateUi(self, errorBox):
        errorBox.setWindowTitle(QCoreApplication.translate("errorBox", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("errorBox", u"Error", None))
        self.errorTitle.setText(QCoreApplication.translate("errorBox", self.error.title, None))
        self.errorDescription.setText(QCoreApplication.translate("errorBox", self.error.description, None))
    # retranslateUi
