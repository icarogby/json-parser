from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QListWidget

class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()

        # Passo 1
        title_label = QLabel("Passo 1:\nAbrir arquivo .json", self)
        title_label.move(20, 20)
        title_label.resize(200, 30)

        # Botão de abrir arquivo
        send_button = QPushButton("Enviar", self)
        send_button.move(620, 360)
        send_button.resize(80, 30)
        send_button.clicked.connect(self.send_button_clicked)

        # Passo 2
        title_label = QLabel("Passo 2:\nAnálise léxica", self)
        title_label.move(20, 360)
        title_label.resize(200, 30)

        # Lista de tokens
        self.msg_list = QListWidget(self)
        self.msg_list.move(20, 20)
        self.msg_list.resize(680, 330)

        # Passo 3
        title_label = QLabel("Passo 1:\nAnálise sintática", self)
        title_label.move(20, 360)
        title_label.resize(200, 30)

        # Arvore sintática
        self.msg_list = QListWidget(self)
        self.msg_list.move(20, 20)
        self.msg_list.resize(680, 330)

        # Resultado
        title_label = QLabel("Passo 1:\nAbrir arquivo .json", self)
        title_label.move(20, 360)
        title_label.resize(200, 30)

        self.setGeometry(100, 100, 1080, 540)
        self.setWindowTitle("GUI Chat")
        self.show()

    def send_button_clicked(self):
        self.conec.enviar(self.send_line.text(), self)
        self.send_line.setText("")

    def receive(self, msg):
        self.msg_list.addItem(msg)