from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy

from prodotto.controller.ControlloreProdotto import ControlloreProdotto


class VistaProdotto(QWidget):
    def __init__(self, prodotto, parent=None):
        super(VistaProdotto, self).__init__(parent)
        self.controller = ControlloreProdotto(prodotto)

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_prodotto())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(self.get_info("Prodotto: {}".format(self.controller.get_prodotto())))
        v_layout.addWidget(self.get_info("Prezzo: {}€\n".format(self.controller.get_prezzo())))
        v_layout.addWidget(self.get_info("Ingredienti:"))
        for a in self.controller.get_ingredienti():
            v_layout.addWidget(self.get_info("{}".format(a) + ": {}".format(self.controller.get_ingredienti()[a])))
        v_layout.addWidget(self.get_info("\n{}".format(self.controller.get_isDisponibile())))

        self.setLayout(v_layout)
        self.setWindowTitle(self.controller.get_prodotto())

    @staticmethod
    def get_info(text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(17)
        label.setFont(font)
        return label
