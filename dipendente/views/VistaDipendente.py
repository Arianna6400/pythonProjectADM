from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Codice Fiscale: {}".format(self.controller.get_cf_dipendente())))
        v_layout.addWidget(self.get_info("Data Nascita: {}".format(self.controller.get_data_nascita_dipendente())))
        v_layout.addWidget(self.get_info("Luogo Nascita: {}".format(self.controller.get_luogo_nascita_dipendente())))
        v_layout.addWidget(self.get_info("Telefono: {}".format(self.controller.get_telefono_dipendente())))
        v_layout.addWidget(self.get_info("Ruolo: {}".format(self.controller.get_ruolo_dipendente())))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        delete_button = QPushButton("Elimina")
        delete_button.clicked.connect(self.elimina_dipendente)
        v_layout.addWidget(delete_button)

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_nome_dipendente())

    def get_info(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label

    def elimina_dipendente(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()