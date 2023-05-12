# Generated from C:/Users/icaro/PycharmProjects/json-parser\json.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsonParser import jsonParser
else:
    from jsonParser import jsonParser

# This class defines a complete generic visitor for a parse tree produced by jsonParser.

class jsonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by jsonParser#init.
    def visitInit(self, ctx:jsonParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#nomes.
    def visitNomes(self, ctx:jsonParser.NomesContext):
        return self.visitChildren(ctx)



del jsonParser