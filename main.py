import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from dashboard import DashBoard


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = DashBoard()
    #window.showMaximized()
    window.show()
    
    sys.exit(app.exec())
    