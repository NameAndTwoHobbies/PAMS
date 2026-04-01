"""
Unit tests for PAMS dashboard widgets. Tests ensure all widgets are properly
initialized and visible.
"""

import pytest
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit
from PySide6.QtCore import Qt
from components.MyWidgets import (
    WelcomePage,
    CustomerLoginPage,
    SignUpPage,
    AdminLoginPage,
    Dashboard,
    DetailedSignUpPage,
    FrontDeskDashboard,
    FinanceDashboard,
    Table,
)
from models.Entities import IEntity


@pytest.fixture(scope="session")
def qapp():
    """Create QApplication instance for all tests."""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app


@pytest.fixture
def widget(qtbot):
    """Base widget for testing."""
    return QWidget()


class TestWelcomePage:
    """Tests for WelcomePage widget."""

    def test_welcome_page_creation(self, qtbot):
        """Test WelcomePage is created successfully."""
        page = WelcomePage()
        qtbot.addWidget(page)
        assert page is not None
        assert isinstance(page, QWidget)

    def test_welcome_page_visible(self, qtbot):
        """Test WelcomePage is visible by default."""
        page = WelcomePage()
        qtbot.addWidget(page)
        page.show()
        assert page.isVisible()

    def test_welcome_page_has_title(self, qtbot):
        """Test WelcomePage has title label."""
        page = WelcomePage()
        qtbot.addWidget(page)
        assert hasattr(page, "title")
        assert isinstance(page.title, QLabel)

    def test_welcome_page_title_visible(self, qtbot):
        """Test WelcomePage title is visible."""
        page = WelcomePage()
        qtbot.addWidget(page)
        page.show()
        assert page.title.isVisible()

    def test_welcome_page_has_login_buttons(self, qtbot):
        """Test WelcomePage has login buttons."""
        page = WelcomePage()
        qtbot.addWidget(page)
        assert hasattr(page, "loginCustomerBtn")
        assert hasattr(page, "loginAdminBtn")
        assert isinstance(page.loginCustomerBtn, QPushButton)
        assert isinstance(page.loginAdminBtn, QPushButton)

    def test_welcome_page_buttons_visible(self, qtbot):
        """Test WelcomePage buttons are visible."""
        page = WelcomePage()
        qtbot.addWidget(page)
        page.show()
        assert page.loginCustomerBtn.isVisible()
        assert page.loginAdminBtn.isVisible()

    def test_welcome_page_buttons_enabled(self, qtbot):
        """Test WelcomePage buttons are enabled."""
        page = WelcomePage()
        qtbot.addWidget(page)
        assert page.loginCustomerBtn.isEnabled()
        assert page.loginAdminBtn.isEnabled()


class TestCustomerLoginPage:
    """Tests for CustomerLoginPage widget."""

    def test_customer_login_page_creation(self, qtbot):
        """Test CustomerLoginPage is created successfully."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        assert page is not None
        assert isinstance(page, QWidget)

    def test_customer_login_page_visible(self, qtbot):
        """Test CustomerLoginPage is visible."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.isVisible()

    def test_customer_login_has_email_input(self, qtbot):
        """Test CustomerLoginPage has email input."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "emailInput")
        assert isinstance(page.emailInput, QTextEdit)

    def test_customer_login_email_input_visible(self, qtbot):
        """Test CustomerLoginPage email input is visible."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.emailInput.isVisible()

    def test_customer_login_has_password_input(self, qtbot):
        """Test CustomerLoginPage has password input."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "passwordInput")
        assert isinstance(page.passwordInput, QTextEdit)

    def test_customer_login_password_input_visible(self, qtbot):
        """Test CustomerLoginPage password input is visible."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.passwordInput.isVisible()

    def test_customer_login_has_login_button(self, qtbot):
        """Test CustomerLoginPage has login button."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "loginBtn")
        assert isinstance(page.loginBtn, QPushButton)

    def test_customer_login_button_visible(self, qtbot):
        """Test CustomerLoginPage login button is visible."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.loginBtn.isVisible()

    def test_customer_login_has_signup_button(self, qtbot):
        """Test CustomerLoginPage has sign up button."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "signUpBtn")
        assert isinstance(page.signUpBtn, QPushButton)

    def test_customer_login_signup_button_visible(self, qtbot):
        """Test CustomerLoginPage sign up button is visible."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.signUpBtn.isVisible()

    def test_customer_login_has_title(self, qtbot):
        """Test CustomerLoginPage has title."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "title")
        assert isinstance(page.title, QLabel)

    def test_customer_login_title_visible(self, qtbot):
        """Test CustomerLoginPage title is visible."""
        page = CustomerLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.title.isVisible()


class TestAdminLoginPage:
    """Tests for AdminLoginPage widget."""

    def test_admin_login_page_creation(self, qtbot):
        """Test AdminLoginPage is created successfully."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        assert page is not None
        assert isinstance(page, QWidget)

    def test_admin_login_page_visible(self, qtbot):
        """Test AdminLoginPage is visible."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.isVisible()

    def test_admin_login_has_email_input(self, qtbot):
        """Test AdminLoginPage has email input."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "emailInput")
        assert isinstance(page.emailInput, QTextEdit)

    def test_admin_login_email_input_visible(self, qtbot):
        """Test AdminLoginPage email input is visible."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.emailInput.isVisible()

    def test_admin_login_has_password_input(self, qtbot):
        """Test AdminLoginPage has password input."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "passwordInput")
        assert isinstance(page.passwordInput, QTextEdit)

    def test_admin_login_password_input_visible(self, qtbot):
        """Test AdminLoginPage password input is visible."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.passwordInput.isVisible()

    def test_admin_login_has_login_button(self, qtbot):
        """Test AdminLoginPage has login button."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "loginBtn")
        assert isinstance(page.loginBtn, QPushButton)

    def test_admin_login_button_visible(self, qtbot):
        """Test AdminLoginPage login button is visible."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.loginBtn.isVisible()

    def test_admin_login_has_title(self, qtbot):
        """Test AdminLoginPage has title."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        assert hasattr(page, "title")
        assert isinstance(page.title, QLabel)

    def test_admin_login_title_visible(self, qtbot):
        """Test AdminLoginPage title is visible."""
        page = AdminLoginPage()
        qtbot.addWidget(page)
        page.show()
        assert page.title.isVisible()


class TestSignUpPage:
    """Tests for SignUpPage widget."""

    def test_signup_page_creation(self, qtbot):
        """Test SignUpPage is created successfully."""
        page = SignUpPage()
        qtbot.addWidget(page)
        assert page is not None
        assert isinstance(page, QWidget)

    def test_signup_page_visible(self, qtbot):
        """Test SignUpPage is visible."""
        page = SignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.isVisible()

    def test_signup_page_has_title(self, qtbot):
        """Test SignUpPage has title."""
        page = SignUpPage()
        qtbot.addWidget(page)
        assert hasattr(page, "title")
        assert isinstance(page.title, QLabel)

    def test_signup_page_title_visible(self, qtbot):
        """Test SignUpPage title is visible."""
        page = SignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.title.isVisible()

    def test_signup_page_has_email_input(self, qtbot):
        """Test SignUpPage has email input."""
        page = SignUpPage()
        qtbot.addWidget(page)
        assert hasattr(page, "emailInput")

    def test_signup_page_email_input_visible(self, qtbot):
        """Test SignUpPage email input is visible."""
        page = SignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.emailInput.isVisible()

    def test_signup_page_has_submit_button(self, qtbot):
        """Test SignUpPage has submit button."""
        page = SignUpPage()
        qtbot.addWidget(page)
        assert hasattr(page, "submitBtn")
        assert isinstance(page.submitBtn, QPushButton)

    def test_signup_page_submit_button_visible(self, qtbot):
        """Test SignUpPage submit button is visible."""
        page = SignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.submitBtn.isVisible()

    def test_signup_page_submit_button_enabled(self, qtbot):
        """Test SignUpPage submit button is enabled."""
        page = SignUpPage()
        qtbot.addWidget(page)
        assert page.submitBtn.isEnabled()


class TestDetailedSignUpPage:
    """Tests for DetailedSignUpPage widget."""

    def test_detailed_signup_creation(self, qtbot):
        """Test DetailedSignUpPage is created successfully."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        assert page is not None
        assert isinstance(page, QWidget)

    def test_detailed_signup_visible(self, qtbot):
        """Test DetailedSignUpPage is visible."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.isVisible()

    def test_detailed_signup_has_title(self, qtbot):
        """Test DetailedSignUpPage has title."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        assert hasattr(page, "title")
        assert isinstance(page.title, QLabel)

    def test_detailed_signup_title_visible(self, qtbot):
        """Test DetailedSignUpPage title is visible."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.title.isVisible()

    def test_detailed_signup_has_email_input(self, qtbot):
        """Test DetailedSignUpPage has email input."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        assert hasattr(page, "emailInput")

    def test_detailed_signup_email_input_visible(self, qtbot):
        """Test DetailedSignUpPage email input is visible."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.emailInput.isVisible()

    def test_detailed_signup_has_first_name_input(self, qtbot):
        """Test DetailedSignUpPage has first name input."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        assert hasattr(page, "firstNameInput")

    def test_detailed_signup_first_name_visible(self, qtbot):
        """Test DetailedSignUpPage first name input is visible."""
        page = DetailedSignUpPage()
        qtbot.addWidget(page)
        page.show()
        assert page.firstNameInput.isVisible()


class TestDashboard:
    """Tests for customer Dashboard widget."""

    def test_dashboard_creation(self, qtbot):
        """Test Dashboard is created successfully."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert dashboard is not None
        assert isinstance(dashboard, QWidget)

    def test_dashboard_visible(self, qtbot):
        """Test Dashboard is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.isVisible()

    def test_dashboard_has_stacked_widget(self, qtbot):
        """Test Dashboard has stacked widget."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "stackedWidget")

    def test_dashboard_stacked_widget_visible(self, qtbot):
        """Test Dashboard stacked widget is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.stackedWidget.isVisible()

    def test_dashboard_has_sidebar(self, qtbot):
        """Test Dashboard has sidebar."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "sideBar")

    def test_dashboard_sidebar_visible(self, qtbot):
        """Test Dashboard sidebar is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.sideBar.isVisible()

    def test_dashboard_has_account_button(self, qtbot):
        """Test Dashboard has account button."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "accountBtn")
        assert isinstance(dashboard.accountBtn, QPushButton)

    def test_dashboard_account_button_visible(self, qtbot):
        """Test Dashboard account button is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.accountBtn.isVisible()

    def test_dashboard_has_lease_button(self, qtbot):
        """Test Dashboard has lease button."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "leaseBtn")
        assert isinstance(dashboard.leaseBtn, QPushButton)

    def test_dashboard_lease_button_visible(self, qtbot):
        """Test Dashboard lease button is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.leaseBtn.isVisible()

    def test_dashboard_has_payments_button(self, qtbot):
        """Test Dashboard has payments button."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "paymentsBtn")
        assert isinstance(dashboard.paymentsBtn, QPushButton)

    def test_dashboard_payments_button_visible(self, qtbot):
        """Test Dashboard payments button is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.paymentsBtn.isVisible()

    def test_dashboard_has_complaints_button(self, qtbot):
        """Test Dashboard has complaints button."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "complaintsBtn")
        assert isinstance(dashboard.complaintsBtn, QPushButton)

    def test_dashboard_complaints_button_visible(self, qtbot):
        """Test Dashboard complaints button is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.complaintsBtn.isVisible()

    def test_dashboard_buttons_enabled(self, qtbot):
        """Test Dashboard sidebar buttons are enabled."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert dashboard.accountBtn.isEnabled()
        assert dashboard.leaseBtn.isEnabled()
        assert dashboard.paymentsBtn.isEnabled()
        assert dashboard.complaintsBtn.isEnabled()

    def test_dashboard_has_default_page(self, qtbot):
        """Test Dashboard has default page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "defaultPage")

    def test_dashboard_default_page_visible(self, qtbot):
        """Test Dashboard default page is visible."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.defaultPage.isVisible()

    def test_dashboard_has_account_page(self, qtbot):
        """Test Dashboard has account page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "accountPage")

    def test_dashboard_has_lease_page(self, qtbot):
        """Test Dashboard has lease page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "leasePage")

    def test_dashboard_has_payment_page(self, qtbot):
        """Test Dashboard has payment page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "paymentPage")

    def test_dashboard_has_complaints_page(self, qtbot):
        """Test Dashboard has complaints page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "complaintsPage")

    def test_dashboard_switch_account_page(self, qtbot):
        """Test Dashboard can switch to account page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.switchAccountPage()
        assert dashboard.stackedWidget.currentIndex() == 1

    def test_dashboard_switch_lease_page(self, qtbot):
        """Test Dashboard can switch to lease page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.switchLeasePage()
        assert dashboard.stackedWidget.currentIndex() == 2

    def test_dashboard_switch_payments_page(self, qtbot):
        """Test Dashboard can switch to payments page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.switchPaymentsPage()
        assert dashboard.stackedWidget.currentIndex() == 3

    def test_dashboard_switch_complaints_page(self, qtbot):
        """Test Dashboard can switch to complaints page."""
        dashboard = Dashboard()
        qtbot.addWidget(dashboard)
        dashboard.switchComplaintsPage()
        assert dashboard.stackedWidget.currentIndex() == 4


class TestFrontDeskDashboard:
    """Tests for FrontDeskDashboard widget."""

    def test_front_desk_dashboard_creation(self, qtbot):
        """Test FrontDeskDashboard is created successfully."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        assert dashboard is not None
        assert isinstance(dashboard, QWidget)

    def test_front_desk_dashboard_visible(self, qtbot):
        """Test FrontDeskDashboard is visible."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.isVisible()

    def test_front_desk_dashboard_has_title(self, qtbot):
        """Test FrontDeskDashboard has title."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "title")

    def test_front_desk_dashboard_title_visible(self, qtbot):
        """Test FrontDeskDashboard title is visible."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.title.isVisible()

    def test_front_desk_dashboard_has_tenant_table(self, qtbot):
        """Test FrontDeskDashboard has tenant table."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "tenantTable")

    def test_front_desk_dashboard_tenant_table_visible(self, qtbot):
        """Test FrontDeskDashboard tenant table is visible."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.tenantTable.isVisible()

    def test_front_desk_dashboard_has_search_bar(self, qtbot):
        """Test FrontDeskDashboard has search bar."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "searchBar")

    def test_front_desk_dashboard_search_bar_visible(self, qtbot):
        """Test FrontDeskDashboard search bar is visible."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.searchBar.isVisible()

    def test_front_desk_dashboard_has_submit_button(self, qtbot):
        """Test FrontDeskDashboard has submit button."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "submitButton")
        assert isinstance(dashboard.submitButton, QPushButton)

    def test_front_desk_dashboard_submit_button_visible(self, qtbot):
        """Test FrontDeskDashboard submit button is visible."""
        dashboard = FrontDeskDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.submitButton.isVisible()


class TestFinanceDashboard:
    """Tests for FinanceDashboard widget."""

    def test_finance_dashboard_creation(self, qtbot):
        """Test FinanceDashboard is created successfully."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        assert dashboard is not None
        assert isinstance(dashboard, QWidget)

    def test_finance_dashboard_visible(self, qtbot):
        """Test FinanceDashboard is visible."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.isVisible()

    def test_finance_dashboard_has_title(self, qtbot):
        """Test FinanceDashboard has title."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        assert hasattr(dashboard, "title")

    def test_finance_dashboard_title_visible(self, qtbot):
        """Test FinanceDashboard title is visible."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert dashboard.title.isVisible()

    def test_finance_dashboard_has_layout(self, qtbot):
        """Test FinanceDashboard is properly initialized."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        assert dashboard is not None

    def test_finance_dashboard_can_create_occupancy_levels(self, qtbot):
        """Test FinanceDashboard can create occupancy levels."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert hasattr(dashboard, "CreateOccupancyLevels")

    def test_finance_dashboard_can_create_maintenance(self, qtbot):
        """Test FinanceDashboard can create maintenance."""
        dashboard = FinanceDashboard()
        qtbot.addWidget(dashboard)
        dashboard.show()
        assert hasattr(dashboard, "CreateMaintenance")


class TestWidgetIntegration:
    """Integration tests for all widgets."""

    def test_all_widgets_can_be_created(self, qtbot):
        """Test all dashboard widgets can be created."""
        widgets = [
            WelcomePage(),
            CustomerLoginPage(),
            SignUpPage(),
            AdminLoginPage(),
            Dashboard(),
            DetailedSignUpPage(),
            FrontDeskDashboard(),
            FinanceDashboard(),
        ]

        for widget in widgets:
            qtbot.addWidget(widget)
            assert widget is not None
            assert isinstance(widget, QWidget)

    def test_all_widgets_can_be_shown(self, qtbot):
        """Test all dashboard widgets can be shown."""
        widgets = [
            WelcomePage(),
            CustomerLoginPage(),
            SignUpPage(),
            AdminLoginPage(),
            Dashboard(),
            DetailedSignUpPage(),
            FrontDeskDashboard(),
            FinanceDashboard(),
        ]

        for widget in widgets:
            qtbot.addWidget(widget)
            widget.show()
            assert widget.isVisible()

    def test_widget_sizes_reasonable(self, qtbot):
        """Test all widgets have reasonable sizes."""
        widgets = [
            WelcomePage(),
            CustomerLoginPage(),
            SignUpPage(),
            AdminLoginPage(),
            Dashboard(),
            DetailedSignUpPage(),
            FrontDeskDashboard(),
            FinanceDashboard(),
        ]

        for widget in widgets:
            qtbot.addWidget(widget)
            widget.show()
            size = widget.size()
            assert size.width() > 0
            assert size.height() > 0
