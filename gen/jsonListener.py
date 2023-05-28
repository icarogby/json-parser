# Generated from C:/Users/icaro/OneDrive/Documentos/GitHub/json-parser\json.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .jsonParser import jsonParser
else:
    from jsonParser import jsonParser

# This class defines a complete listener for a parse tree produced by jsonParser.
class jsonListener(ParseTreeListener):

    # Enter a parse tree produced by jsonParser#init.
    def enterInit(self, ctx:jsonParser.InitContext):
        pass

    # Exit a parse tree produced by jsonParser#init.
    def exitInit(self, ctx:jsonParser.InitContext):
        pass


    # Enter a parse tree produced by jsonParser#value.
    def enterValue(self, ctx:jsonParser.ValueContext):
        pass

    # Exit a parse tree produced by jsonParser#value.
    def exitValue(self, ctx:jsonParser.ValueContext):
        pass


    # Enter a parse tree produced by jsonParser#obj.
    def enterObj(self, ctx:jsonParser.ObjContext):
        pass

    # Exit a parse tree produced by jsonParser#obj.
    def exitObj(self, ctx:jsonParser.ObjContext):
        pass


    # Enter a parse tree produced by jsonParser#data.
    def enterData(self, ctx:jsonParser.DataContext):
        pass

    # Exit a parse tree produced by jsonParser#data.
    def exitData(self, ctx:jsonParser.DataContext):
        pass


    # Enter a parse tree produced by jsonParser#key.
    def enterKey(self, ctx:jsonParser.KeyContext):
        pass

    # Exit a parse tree produced by jsonParser#key.
    def exitKey(self, ctx:jsonParser.KeyContext):
        pass


    # Enter a parse tree produced by jsonParser#num.
    def enterNum(self, ctx:jsonParser.NumContext):
        pass

    # Exit a parse tree produced by jsonParser#num.
    def exitNum(self, ctx:jsonParser.NumContext):
        pass


    # Enter a parse tree produced by jsonParser#arr.
    def enterArr(self, ctx:jsonParser.ArrContext):
        pass

    # Exit a parse tree produced by jsonParser#arr.
    def exitArr(self, ctx:jsonParser.ArrContext):
        pass



del jsonParser