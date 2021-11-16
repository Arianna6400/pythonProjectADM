from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from homeamministratore.views.VistaHomeAmministratore import VistaHomeAmministratore


class LoginAmministratore(QWidget):
	def __init__(self):
		super(LoginAmministratore, self).__init__()
		self.home_amministratore = VistaHomeAmministratore()
		self.setWindowTitle('Login Amministratore')
		self.resize(500, 120)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		self.lineEdit_username.returnPressed.connect(self.check_password)
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setEchoMode(QLineEdit.Password)
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		self.lineEdit_password.returnPressed.connect(self.check_password)
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):  # solo quando i dati inseriti sono corretti viene avviato la vista amministratore
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'a' and self.lineEdit_password.text() == '666':
			self.home_amministratore.show()
			self.close()
		else:
			msg.setText('Password errata')
			msg.setWindowTitle("Attenzione!")
			msg.exec_()
