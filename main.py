import sys
from PyQt5.QtWidgets import QApplication

from home.views.VistaHome import VistaHome


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    vista_home = VistaHome()
    vista_home.showMaximized()
    sys.exit(app.exec())