"""
Pytest configuration for PySide6 testing.
"""

import sys
import pytest
from PySide6.QtWidgets import QApplication


def pytest_configure(config):
    """Create QApplication before running tests."""
    if not QApplication.instance():
        QApplication(sys.argv)


@pytest.fixture(scope="session")
def qapp_instance():
    """Provide QApplication instance."""
    return QApplication.instance()
