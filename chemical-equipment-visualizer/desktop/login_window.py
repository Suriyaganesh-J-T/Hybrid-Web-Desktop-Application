import requests
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

API_LOGIN = "http://127.0.0.1:8000/api/auth/login/"


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.setFixedSize(420, 260)

        self.setStyleSheet("""
            QWidget { background: #f2f4f6; font-family: Segoe UI; }
            QFrame { background: white; border: 1px solid #d0d0d0; }
            QLabel#title { font-size: 18px; font-weight: bold; }
            QLabel#sub { color: #555; }
            QLineEdit { padding: 6px; border: 1px solid #aaa; }
            QPushButton {
                background: #2563eb;
                color: white;
                padding: 6px;
                border: none;
            }
            QPushButton:hover { background: #1e40af; }
        """)

        outer = QVBoxLayout(self)
        outer.setAlignment(Qt.AlignCenter)

        card = QFrame()
        layout = QVBoxLayout(card)
        layout.setContentsMargins(25, 20, 25, 20)
        layout.setSpacing(10)

        title = QLabel("Sign in")
        title.setObjectName("title")

        sub = QLabel("Chemical Equipment Parameter Visualizer")
        sub.setObjectName("sub")

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login)

        layout.addWidget(title)
        layout.addWidget(sub)
        layout.addSpacing(10)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(login_btn)

        outer.addWidget(card)

    def login(self):
        res = requests.post(API_LOGIN, json={
            "username": self.username.text(),
            "password": self.password.text()
        })

        if res.status_code == 200:
            from dashboard_window import DashboardWindow
            self.dashboard = DashboardWindow(self)
            self.dashboard.show()
            self.hide()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials")
