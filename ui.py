from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QListWidget, QFileDialog

from antlr4 import *
from gen.jsonLexer import jsonLexer
def types(tok):
    if tok == 1 or tok == 3:
        return "Chaves"
    elif tok == 2:
        return "Virgula"
    elif tok == 4:
        return "Dois Pontos"
    elif tok == 5 or tok == 6:
        return "Parenteses"
    elif tok == 7:
        return "Espaço"
    elif tok == 8:
        return "Int"
    elif tok == 9:
        return "Float"
    elif tok == 10:
        return "Expoente"
    elif tok == 11:
        return "IntExpoente"
    elif tok == 12:
        return "Boolean"
    elif tok == 13:
        return "Null"
    elif tok == 14:
        return "String"
    elif tok == 15:
        return "Char"
    else:
        return "Tipo Desconhecido"

class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()

        # Passo 1
        title_label = QLabel("Passo 1: Abrir arquivo .json", self)
        title_label.move(20, 20)
        title_label.resize(200, 40)

        # Botão de abrir arquivo
        send_button = QPushButton("Abrir", self)
        send_button.move(20, 80)
        send_button.resize(80, 40)
        send_button.clicked.connect(self.open_button_clicked)

        # Passo 2
        title_label = QLabel("Passo 2: Análise léxica", self)
        title_label.move(20, 140)
        title_label.resize(200, 40)

        # Lista de tokens
        self.msg_list = QListWidget(self)
        self.msg_list.move(20, 200)
        self.msg_list.resize(680, 320)

        # Janela
        self.setGeometry(100, 100, 720, 540)
        self.setWindowTitle("Reconhecedor de tokens para JSON")
        self.show()

    def open_button_clicked(self):
        arquivo = QFileDialog.getOpenFileName()[0]
        data = FileStream(arquivo)
        lexer = jsonLexer(data)

        for tok in lexer.getAllTokens():
            token_type = types(tok.type)
            token = f'Token: {tok.text}\nTipo: {token_type}\n'
            self.msg_list.addItem(token)
