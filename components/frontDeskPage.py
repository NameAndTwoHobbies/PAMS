from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication, QDate, QRect
from datetime import datetime, time

from models import domain_models

class AssignDialog(QDialog):
    def __init__(self, maintenance_service, current_user, request_id, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Assign Worker")

        self.maintenance_service = maintenance_service
        self.current_user = current_user
        self.request_id = request_id

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate.currentDate())
        self.calendar.setMaximumDate(QDate.currentDate().addDays(14))
        self.calendar.clicked.connect(self.load_workers)

        self.worker_combo = QComboBox()

        self.assign_btn = QPushButton("Assign")
        self.assign_btn.clicked.connect(self.assign_worker)
        self.assign_btn.setEnabled(False)

        layout.addWidget(QLabel("Select Date"))
        layout.addWidget(self.calendar)
        layout.addWidget(QLabel("Available Workers"))
        layout.addWidget(self.worker_combo)
        layout.addWidget(self.assign_btn)

        self.setLayout(layout)

    def load_workers(self):
        date = self.calendar.selectedDate().toPython()
        start = datetime.combine(date, time(hour=9, minute=0))
        end = datetime.combine(date, time(hour=17, minute=0))

        try:
            workers = self.maintenance_service.get_available_workers(
                start, end, self.current_user
            )

            self.worker_combo.clear()

            if not workers:
                self.worker_combo.addItem("No available workers", None)
                self.assign_btn.setEnabled(False)
                return

            for w in workers:
                self.worker_combo.addItem(f"{w['firstName']} {w['lastName']}", w['user_id'])

            self.assign_btn.setEnabled(True)

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            print(e)

    def assign_worker(self):
        worker_id = self.worker_combo.currentData()

        if worker_id is None:
            QMessageBox.warning(self, "Error", "Select a worker")
            return

        date = self.calendar.selectedDate().toPython()
        start = datetime.combine(date, time(hour=9, minute=0))
        end = datetime.combine(date, time(hour=17, minute=0))

        try:
            self.maintenance_service.assign_worker_to_request(
                self.request_id,
                worker_id,
                start,
                end,
            )

            self.accept()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            print(e)


class FrontDeskPendingMaintenance(QWidget):
    def __init__(self, maintenance_service):
        super().__init__()

        self.maintenance_service = maintenance_service
        self.current_user = None
        
        self.init_ui()

    def setUser(self, user):
        self.current_user = user
        self.load_pending_requests

    def init_ui(self):
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "ID", "Description", "Priority", "Action"
        ])

        layout.addWidget(QLabel("Pending Requests"))
        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_pending_requests(self):
        if (self.current_user == None):
            return

        requests = self.maintenance_service.get_pending_requests(self.current_user)

        self.table.setRowCount(len(requests))

        for row, req in enumerate(requests):
            self.table.setItem(row, 0, QTableWidgetItem(str(req['request_id'])))
            self.table.setItem(row, 1, QTableWidgetItem(req['description']))
            self.table.setItem(row, 2, QTableWidgetItem(str(req['priority'])))            

            btn = QPushButton("Assign")
            btn.clicked.connect(lambda _, r=req: self.open_assign_dialog(r['request_id']))
            self.table.setCellWidget(row, 3, btn)

    def open_assign_dialog(self, request_id):
        dialog = AssignDialog(
            self.maintenance_service,
            self.current_user,
            request_id,
            self
        )

        if dialog.exec():
            self.load_pending_requests()

class RequestDetailsDialog(QDialog):
    def __init__(self, request, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Request Details")
        self.resize(400, 300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"Request ID: {request['request_id']}"))
        layout.addWidget(QLabel(f"Description: {request['description']}"))
        layout.addWidget(QLabel(f"Priority: {request['priority']}"))
        layout.addWidget(QLabel(f"Status: {request['status']}"))

        if "scheduled_start" in request:
            layout.addWidget(QLabel(f"Start: {request['scheduled_start']}"))
        if "scheduled_end" in request:
            layout.addWidget(QLabel(f"End: {request['scheduled_end']}"))
        if "worker_name" in request:
            layout.addWidget(QLabel(f"Worker: {request['worker_name']}"))

        self.setLayout(layout)


class RescheduleDialog(QDialog):
    def __init__(self, maintenance_service, current_user, request, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Reschedule Request")

        self.maintenance_service = maintenance_service
        self.current_user = current_user
        self.request = request

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate.currentDate())
        self.calendar.setMaximumDate(QDate.currentDate().addDays(14))
        self.calendar.clicked.connect(self.load_workers)

        self.worker_combo = QComboBox()

        self.reschedule_btn = QPushButton("Reschedule")
        self.reschedule_btn.clicked.connect(self.reschedule)
        self.reschedule_btn.setEnabled(False)

        layout.addWidget(QLabel("Select New Date"))
        layout.addWidget(self.calendar)
        layout.addWidget(QLabel("Available Workers"))
        layout.addWidget(self.worker_combo)
        layout.addWidget(self.reschedule_btn)

        self.setLayout(layout)

    def load_workers(self):
        date = self.calendar.selectedDate().toPython()
        start = datetime.combine(date, time(hour=9, minute=0))
        end = datetime.combine(date, time(hour=17, minute=0))

        workers = self.maintenance_service.get_available_workers(start, end, self.current_user)

        self.worker_combo.clear()

        if not workers:
            self.worker_combo.addItem("No available workers", None)
            self.reschedule_btn.setEnabled(False)
            return

        for w in workers:
            self.worker_combo.addItem(f"{w['firstName']} {w['lastName']}", w['user_id'])

        self.reschedule_btn.setEnabled(True)

    def reschedule(self):
        worker_id = self.worker_combo.currentData()

        if worker_id is None:
            QMessageBox.warning(self, "Error", "Select a worker")
            return

        date = self.calendar.selectedDate().toPython()
        start = datetime.combine(date, time(hour=9, minute=0))
        end = datetime.combine(date, time(hour=17, minute=0))

        try:
            self.maintenance_service.reschedule_request(
                self.request.request_id,
                worker_id,
                start,
                end,
                self.current_user
            )
            self.accept()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))


class FrontDeskScheduledMaintenance(QWidget):
    def __init__(self, maintenance_service):
        super().__init__()

        self.maintenance_service = maintenance_service
        self.current_user = None
        self.requests = []

        self.init_ui()

    def setUser(self, user):
        self.current_user = user
        self.load_scheduled_requests

    def init_ui(self):
        layout = QVBoxLayout()

        filter_layout = QHBoxLayout()
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["All", "Today", "This Week"])
        self.filter_combo.currentIndexChanged.connect(self.apply_filter)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_scheduled_requests)

        filter_layout.addWidget(QLabel("Filter:"))
        filter_layout.addWidget(self.filter_combo)
        filter_layout.addStretch()
        filter_layout.addWidget(refresh_btn)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Description", "Priority", "Worker", "Start", "Details", "Reschedule", "Cancel"
        ])

        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        layout.addLayout(filter_layout)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def load_scheduled_requests(self):
        if self.current_user == None: 
            return print("no user")
        try:
            self.requests = self.maintenance_service.see_scheduled_requests(self.current_user.location.location_id)
            self.populate_table(self.requests)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            print(e)

    def populate_table(self, requests):
        self.table.setRowCount(len(requests))

        for row, req in enumerate(requests):
            self.table.setItem(row, 0, QTableWidgetItem(str(req['request_id'])))
            self.table.setItem(row, 1, QTableWidgetItem(req['description']))
            self.table.setItem(row, 2, QTableWidgetItem(str(req['priority'])))

            worker = req.get("firstName") + " " + req.get("lastName") if req.get("firstName") and req.get("lastName") else "-"
            start = req.get("scheduled_start")

            # format datetime nicely
            if start:
                start = start.strftime("%Y-%m-%d %H:%M") if hasattr(start, "strftime") else str(start)
            else:
                start = "-"

            self.table.setItem(row, 3, QTableWidgetItem(worker))
            self.table.setItem(row, 4, QTableWidgetItem(start))

            details_btn = QPushButton("Details")
            details_btn.clicked.connect(lambda _, r=req: self.show_details(r))
            self.table.setCellWidget(row, 5, details_btn)

            reschedule_btn = QPushButton("Reschedule")
            reschedule_btn.clicked.connect(lambda _, r=req: self.open_reschedule(r))
            self.table.setCellWidget(row, 6, reschedule_btn)

            cancel_btn = QPushButton("Cancel")
            cancel_btn.clicked.connect(lambda _, r=req: self.cancel_request(r))
            self.table.setCellWidget(row, 7, cancel_btn)

    def apply_filter(self):
        option = self.filter_combo.currentText()

        today = datetime.today().date()
        this_week = today.isocalendar()[1]

        if option == "All":
            filtered = self.requests

        elif option == "Today":
            filtered = [
                r for r in self.requests
                if r.get("scheduled_start")
                and r["scheduled_start"].date() == today
            ]

        else:
            filtered = [
                r for r in self.requests
                if r.get("scheduled_start")
                and r["scheduled_start"].isocalendar()[1] == this_week
            ]

        self.populate_table(filtered)

    def show_details(self, request):
        dialog = RequestDetailsDialog(request, self)
        dialog.exec()

    def open_reschedule(self, request):
        dialog = RescheduleDialog(self.maintenance_service, self.current_user, request, self)
        if dialog.exec():
            self.load_scheduled_requests()

    def cancel_request(self, request):
        confirm = QMessageBox.question(self, "Confirm Cancellation", f"Cancel request {request['request_id']}?")

        if confirm != QMessageBox.Yes:
            return

        try:
            self.maintenance_service.cancel_scheduled_request(request['request_id'])
            QMessageBox.information(self, "Success", "Request cancelled successfully")
            self.load_scheduled_requests()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

class FrontDeskManageTenants(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        from components.MyWidgets import Table


        # Main layout for whole widget
        mainLayout = QVBoxLayout(self)

        # Register Tenants Section
        self.registerTenants = QGroupBox("Register Tenants")
        self.registerTenants.setStyleSheet("font-size: 14px;")
        registerLayout = QGridLayout()

        self.firstNameInput = QLineEdit()
        self.firstNameInput.setPlaceholderText("First Name")

        self.lastNameInput = QLineEdit()
        self.lastNameInput.setPlaceholderText("Last Name")

        self.emailInput = QLineEdit()
        self.emailInput.setPlaceholderText("Email")

        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Password")

        self.nationalInsuranceInput = QLineEdit()
        self.nationalInsuranceInput.setPlaceholderText("National Insurance Number")

        self.phoneNumberInput = QLineEdit()
        self.phoneNumberInput.setPlaceholderText("Phone Number")

        self.occupationDropdown = QComboBox()
        self.occupationDropdown.addItems(["Student", "Unemployed", "Employed", "Part-Time"])

        self.submitButton = QPushButton("Submit")

        registerLayout.addWidget(self.firstNameInput, 0, 0)
        registerLayout.addWidget(self.lastNameInput, 1, 0)
        registerLayout.addWidget(self.emailInput, 2, 0)
        registerLayout.addWidget(self.passwordInput, 3, 0)

        registerLayout.addWidget(self.nationalInsuranceInput, 0, 1)
        registerLayout.addWidget(self.phoneNumberInput, 1, 1)
        registerLayout.addWidget(self.occupationDropdown, 2, 1)
        registerLayout.addWidget(self.submitButton, 3, 1)

        self.registerTenants.setLayout(registerLayout)

        # Manage Tenants Section
        self.manageTenants = QGroupBox()
        manageLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()
        self.manageTitle = QLabel("Manage Tenants")
        self.manageTitle.setStyleSheet("font-size: 14px;")
        headerLayout.addWidget(self.manageTitle)
        headerLayout.addStretch()
        
        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Search")
        self.searchBar.setMaximumWidth(200)

        headerLayout.addWidget(self.searchBar)

        # Table
        self.tenantTable = Table([], [])

        manageLayout.addLayout(headerLayout)
        manageLayout.addWidget(self.tenantTable)

        self.manageTenants.setLayout(manageLayout)

        # Add to main layout
        mainLayout.addWidget(self.registerTenants)
        mainLayout.addWidget(self.manageTenants)

        # Connections
        self.searchBar.textChanged.connect(
            lambda: self.tenantTable.search(self.searchBar.text())
        )

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
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

    def Submit(self):
        fName = self.firstNameInput.text()
        lName = self.lastNameInput.text()
        email = self.emailInput.text()
        password = self.passwordInput.text()
        phoneNumber = self.phoneNumberInput.text() #TODO phonenumber checking is valid phone number
        nationalInsurance = self.nationalInsuranceInput.text()
        occupation = self.occupationDropdown.currentText()
        references = ""
        tenant = domain_models.Tenant(-1,fName,lName,email,password,phoneNumber,nationalInsurance,occupation ,references )
        self.firstNameInput.clear()
        self.lastNameInput.clear()
        self.emailInput.clear()
        self.passwordInput.clear()
        self.phoneNumberInput.clear()
        self.nationalInsuranceInput.clear()
        self.occupationDropdown.setCurrentIndex(0)
        return tenant
    
class FrontDeskSendNotifications(QWidget):
    def __init__(self, maintenance_service):
        super().__init__()
        self.maintenance_service = maintenance_service
        current_user = None
        self.init_ui()

    def setUser(self, user):
        current_user = user

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
