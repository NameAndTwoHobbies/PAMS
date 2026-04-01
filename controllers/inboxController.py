from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QMessageBox
)
from PySide6.QtCore import QTimer
from services.notificationsService import NotificationService


class InboxController(QWidget):

    def __init__(self, window, tenant_id, location_id):
        super().__init__()

        self.window = window
        self.service = NotificationService(tenant_id, location_id)

        self.setup_connections()
        self.setup_timer()

        self.load_notifications()

    # Setup

    def setup_connections(self):

        self.window.personal.stateChanged.connect(self.load_notifications)
        self.window.public.stateChanged.connect(self.load_notifications)

    def setup_timer(self):

        self.timer = QTimer()
        self.timer.timeout.connect(self.load_notifications)
        self.timer.start(10000)  # 10 seconds


    # Loader

    def load_notifications(self):

        personal = self.window.personal.isChecked()
        public = self.window.public.isChecked()

        notifications = self.service.get_notifications(personal, public)

        self.populate_list(notifications)
        if not personal and not public:
            return

    # Populate

    def populate_list(self, notifications):

        # Clear existing items
        while self.window.inboxLayout.count() > 1:
            item = self.window.inboxLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        for n in notifications:

            btn = QPushButton(n["subject"])
            btn.setStyleSheet("text-align: left; padding: 5px;")
            btn.clicked.connect(lambda checked=False, data=n: self.display_message(data))

            if not n["is_read"]:
                btn.setStyleSheet("text-align: left; padding: 5px; font-weight: bold;")

            self.window.inboxLayout.insertWidget(
                self.window.inboxLayout.count() - 1,
                btn
            )

    # Display Message

    def display_message(self, data):

        self.window.subject.setText(data["subject"])
        self.window.messageBody.setText(data["message"])

        if not data["is_read"]:
            self.service.mark_as_read(data["notification_id"])
            self.load_notifications()