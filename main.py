from antlr4 import *
from gen.gramaticaLexer import gramaticaLexer
from gen.gramaticaParser import gramaticaParser

if __name__ == '__main__':
    #data = FileStream()
    data = FileStream("test-schema.json")
    lexer = gramaticaLexer(data)

    for tok in lexer.getAllTokens():
        print(tok.text, tok.type)
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.start()
    print(tree.toStringTree())