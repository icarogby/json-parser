from PyQt5.QtWidgets import QApplication
import sys
import ui

def main():
    app = QApplication(sys.argv)
    window = ui.Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


