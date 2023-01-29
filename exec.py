"""Main file for the application."""
import sys
from PyQt6.QtWidgets import QApplication
from src.views.login import LoginFormWindow

app = QApplication(sys.argv)
Login = LoginFormWindow()
sys.exit(app.exec())
