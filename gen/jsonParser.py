# Generated from C:/Users/icaro/PycharmProjects/json-parser\json.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,4,16,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,5,1,11,8,1,10,1,
        12,1,14,9,1,1,1,0,0,2,0,2,0,0,14,0,4,1,0,0,0,2,7,1,0,0,0,4,5,5,1,
        0,0,5,6,3,2,1,0,6,1,1,0,0,0,7,12,5,3,0,0,8,9,5,2,0,0,9,11,5,3,0,
        0,10,8,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,3,1,
        0,0,0,14,12,1,0,0,0,1,12
    ]

class jsonParser ( Parser ):

    grammarFileName = "json.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'hello'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NOME", "WS" ]

    RULE_init = 0
    RULE_nomes = 1

    ruleNames =  [ "init", "nomes" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NOME=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nomes(self):
            return self.getTypedRuleContext(jsonParser.NomesContext,0)


        def getRuleIndex(self):
            return jsonParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = jsonParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(jsonParser.T__0)
            self.state = 5
            self.nomes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NomesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOME(self, i:int=None):
            if i is None:
                return self.getTokens(jsonParser.NOME)
            else:
                return self.getToken(jsonParser.NOME, i)

        def getRuleIndex(self):
            return jsonParser.RULE_nomes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNomes" ):
                listener.enterNomes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNomes" ):
                listener.exitNomes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNomes" ):
                return visitor.visitNomes(self)
            else:
                return visitor.visitChildren(self)




    def nomes(self):

        localctx = jsonParser.NomesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nomes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(jsonParser.NOME)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 8
                self.match(jsonParser.T__1)
                self.state = 9
                self.match(jsonParser.NOME)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





