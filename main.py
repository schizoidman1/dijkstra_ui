from user_interface import QApplication, DijkstraGraphApp
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DijkstraGraphApp()
    window.show()
    sys.exit(app.exec())