from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.show_register_window)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        # اینجا می‌توانید اعتبارسنجی لاگین را انجام دهید.

        print(f"Login: Username={username}, Password={password}")

    def show_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register Page")
        self.setGeometry(100, 100, 300, 200)

        self.first_name_label = QLabel("First Name:")
        self.first_name_entry = QLineEdit()

        self.last_name_label = QLabel("Last Name:")
        self.last_name_entry = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_entry = QLineEdit()

        self.phone_number_label = QLabel("Phone Number:")
        self.phone_number_entry = QLineEdit()

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_entry)
        layout.addWidget(self.last_name_label)
        layout.addWidget(self.last_name_entry)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_entry)
        layout.addWidget(self.phone_number_label)
        layout.addWidget(self.phone_number_entry)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        first_name = self.first_name_entry.text()
        last_name = self.last_name_entry.text()
        email = self.email_entry.text()
        phone_number = self.phone_number_entry.text()

        # اینجا می‌توانید اعتبارسنجی ثبت نام را انجام دهید.

        print(f"Register: First Name={first_name}, Last Name={last_name}, Email={email}, Phone Number={phone_number}")


if __name__ == "__main__":
    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec_()
