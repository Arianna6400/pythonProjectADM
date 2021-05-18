from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listamenu.views.VistaListaMenuCliente import VistaListaMenuCliente


class VistaHomeCliente(QWidget):

    def __init__(self):
        super(VistaHomeCliente, self).__init__()
        grid_layout = QGridLayout()

        button = QPushButton("Visualizza Menu")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.go_vista_menu)
        grid_layout.addWidget(self.button, 0, 0)

        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Vista Cliente")

    def go_vista_menu(self):
        self.vista_menu = VistaListaMenuCliente()
        self.vista_menu.show()