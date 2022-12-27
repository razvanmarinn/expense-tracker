from PyQt6.QtWidgets import QApplication
import sys
from templates.Login import LoginFormWindow




app = QApplication(sys.argv)
Login = LoginFormWindow()
sys.exit(app.exec())


