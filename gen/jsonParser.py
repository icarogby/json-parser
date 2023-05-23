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
        4,1,3,47,2,0,7,0,2,1,7,1,1,0,1,0,1,1,5,1,8,8,1,10,1,12,1,11,9,1,
        1,1,4,1,14,8,1,11,1,12,1,15,3,1,18,8,1,1,1,5,1,21,8,1,10,1,12,1,
        24,9,1,1,1,4,1,27,8,1,11,1,12,1,28,1,1,5,1,32,8,1,10,1,12,1,35,9,
        1,1,1,4,1,38,8,1,11,1,12,1,39,5,1,42,8,1,10,1,12,1,45,9,1,1,1,0,
        0,2,0,2,0,0,53,0,4,1,0,0,0,2,17,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,0,
        6,8,5,2,0,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,
        18,1,0,0,0,11,9,1,0,0,0,12,14,5,1,0,0,13,12,1,0,0,0,14,15,1,0,0,
        0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,9,1,0,0,0,17,13,1,
        0,0,0,18,43,1,0,0,0,19,21,5,2,0,0,20,19,1,0,0,0,21,24,1,0,0,0,22,
        20,1,0,0,0,22,23,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,25,27,5,1,0,
        0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,42,
        1,0,0,0,30,32,5,1,0,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,
        33,34,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,36,38,5,2,0,0,37,36,1,
        0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,
        22,1,0,0,0,41,33,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,
        0,44,3,1,0,0,0,45,43,1,0,0,0,9,9,15,17,22,28,33,39,41,43
    ]

class jsonParser ( Parser ):

    grammarFileName = "json.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PAL", "SIMB", "WS" ]

    RULE_init = 0
    RULE_texto = 1

    ruleNames =  [ "init", "texto" ]

    EOF = Token.EOF
    PAL=1
    SIMB=2
    WS=3

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

        def texto(self):
            return self.getTypedRuleContext(jsonParser.TextoContext,0)


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
            self.texto()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMB(self, i:int=None):
            if i is None:
                return self.getTokens(jsonParser.SIMB)
            else:
                return self.getToken(jsonParser.SIMB, i)

        def PAL(self, i:int=None):
            if i is None:
                return self.getTokens(jsonParser.PAL)
            else:
                return self.getToken(jsonParser.PAL, i)

        def getRuleIndex(self):
            return jsonParser.RULE_texto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTexto" ):
                listener.enterTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTexto" ):
                listener.exitTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTexto" ):
                return visitor.visitTexto(self)
            else:
                return visitor.visitChildren(self)




    def texto(self):

        localctx = jsonParser.TextoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_texto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 9
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 6
                        self.match(jsonParser.SIMB) 
                    self.state = 11
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 2:
                self.state = 13 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 12
                        self.match(jsonParser.PAL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 15 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass


            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 41
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==2:
                        self.state = 19
                        self.match(jsonParser.SIMB)
                        self.state = 24
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 26 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 25
                            self.match(jsonParser.PAL)

                        else:
                            raise NoViableAltException(self)
                        self.state = 28 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                    pass

                elif la_ == 2:
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 30
                        self.match(jsonParser.PAL)
                        self.state = 35
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 37 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 36
                            self.match(jsonParser.SIMB)

                        else:
                            raise NoViableAltException(self)
                        self.state = 39 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                    pass


                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





