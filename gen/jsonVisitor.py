# Generated from C:/Users/icaro/OneDrive/Documentos/GitHub/json-parser\json.g4 by ANTLR 4.12.0
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


    # Visit a parse tree produced by jsonParser#value.
    def visitValue(self, ctx:jsonParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#obj.
    def visitObj(self, ctx:jsonParser.ObjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#data.
    def visitData(self, ctx:jsonParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#key.
    def visitKey(self, ctx:jsonParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#num.
    def visitNum(self, ctx:jsonParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by jsonParser#arr.
    def visitArr(self, ctx:jsonParser.ArrContext):
        return self.visitChildren(ctx)



del jsonParser