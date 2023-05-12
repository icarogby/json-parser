from antlr4 import *
from gen.jsonLexer import jsonLexer
from gen.jsonParser import jsonParser

if __name__ == '__main__':
    data = FileStream('input.txt')
    lexer = jsonLexer(data)

    for tok in lexer.getAllTokens():
        print(tok.text, tok.type)

    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = jsonParser(stream)

    tree = parser.init()
    print(tree.toStringTree())
