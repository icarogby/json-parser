from antlr4 import *
from gen.jsonLexer import jsonLexer
from gen.jsonParser import jsonParser

from PyQt5.QtWidgets import QApplication
import sys
import ui

def main():
    app = QApplication(sys.argv)
    window = ui.Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    # data = FileStream('input1.json')
    # lexer = jsonLexer(data)
    #
    # for tok in lexer.getAllTokens():
    #     print(tok.text, tok.type)
    #
    # lexer.reset()
    # stream = CommonTokenStream(lexer)
    # parser = jsonParser(stream)
    #
    # tree = parser.init()
    # print(tree.toStringTree())

    main()
