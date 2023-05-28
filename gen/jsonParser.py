# Generated from C:/Users/icaro/OneDrive/Documentos/GitHub/json-parser\json.g4 by ANTLR 4.12.0
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
        4,1,15,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,2,5,2,
        29,8,2,10,2,12,2,32,9,2,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,1,
        3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,5,6,52,8,6,10,6,12,6,55,9,6,1,
        6,1,6,1,6,1,6,3,6,61,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,8,9,64,
        0,14,1,0,0,0,2,22,1,0,0,0,4,37,1,0,0,0,6,39,1,0,0,0,8,43,1,0,0,0,
        10,45,1,0,0,0,12,60,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,23,5,14,
        0,0,17,23,3,10,5,0,18,23,5,12,0,0,19,23,5,13,0,0,20,23,3,12,6,0,
        21,23,3,4,2,0,22,16,1,0,0,0,22,17,1,0,0,0,22,18,1,0,0,0,22,19,1,
        0,0,0,22,20,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,1,0,0,25,
        30,3,6,3,0,26,27,5,2,0,0,27,29,3,6,3,0,28,26,1,0,0,0,29,32,1,0,0,
        0,30,28,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,
        5,3,0,0,34,38,1,0,0,0,35,36,5,1,0,0,36,38,5,3,0,0,37,24,1,0,0,0,
        37,35,1,0,0,0,38,5,1,0,0,0,39,40,3,8,4,0,40,41,5,4,0,0,41,42,3,2,
        1,0,42,7,1,0,0,0,43,44,5,14,0,0,44,9,1,0,0,0,45,46,7,0,0,0,46,11,
        1,0,0,0,47,48,5,5,0,0,48,53,3,2,1,0,49,50,5,2,0,0,50,52,3,2,1,0,
        51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,
        0,0,0,55,53,1,0,0,0,56,57,5,6,0,0,57,61,1,0,0,0,58,59,5,5,0,0,59,
        61,5,6,0,0,60,47,1,0,0,0,60,58,1,0,0,0,61,13,1,0,0,0,5,22,30,37,
        53,60
    ]

class jsonParser ( Parser ):

    grammarFileName = "json.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "INT", 
                      "FLOAT", "EXP", "ALTINT", "BOOL", "NULL", "STR", "CHAR" ]

    RULE_init = 0
    RULE_value = 1
    RULE_obj = 2
    RULE_data = 3
    RULE_key = 4
    RULE_num = 5
    RULE_arr = 6

    ruleNames =  [ "init", "value", "obj", "data", "key", "num", "arr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    WS=7
    INT=8
    FLOAT=9
    EXP=10
    ALTINT=11
    BOOL=12
    NULL=13
    STR=14
    CHAR=15

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

        def value(self):
            return self.getTypedRuleContext(jsonParser.ValueContext,0)


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
            self.state = 14
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(jsonParser.STR, 0)

        def num(self):
            return self.getTypedRuleContext(jsonParser.NumContext,0)


        def BOOL(self):
            return self.getToken(jsonParser.BOOL, 0)

        def NULL(self):
            return self.getToken(jsonParser.NULL, 0)

        def arr(self):
            return self.getTypedRuleContext(jsonParser.ArrContext,0)


        def obj(self):
            return self.getTypedRuleContext(jsonParser.ObjContext,0)


        def getRuleIndex(self):
            return jsonParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = jsonParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(jsonParser.STR)
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.num()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(jsonParser.BOOL)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.match(jsonParser.NULL)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 20
                self.arr()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 6)
                self.state = 21
                self.obj()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsonParser.DataContext)
            else:
                return self.getTypedRuleContext(jsonParser.DataContext,i)


        def getRuleIndex(self):
            return jsonParser.RULE_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj" ):
                listener.enterObj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj" ):
                listener.exitObj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj" ):
                return visitor.visitObj(self)
            else:
                return visitor.visitChildren(self)




    def obj(self):

        localctx = jsonParser.ObjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_obj)
        self._la = 0 # Token type
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(jsonParser.T__0)
                self.state = 25
                self.data()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 26
                    self.match(jsonParser.T__1)
                    self.state = 27
                    self.data()
                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 33
                self.match(jsonParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(jsonParser.T__0)
                self.state = 36
                self.match(jsonParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(jsonParser.KeyContext,0)


        def value(self):
            return self.getTypedRuleContext(jsonParser.ValueContext,0)


        def getRuleIndex(self):
            return jsonParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = jsonParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.key()
            self.state = 40
            self.match(jsonParser.T__3)
            self.state = 41
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(jsonParser.STR, 0)

        def getRuleIndex(self):
            return jsonParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = jsonParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(jsonParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(jsonParser.INT, 0)

        def FLOAT(self):
            return self.getToken(jsonParser.FLOAT, 0)

        def getRuleIndex(self):
            return jsonParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = jsonParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(jsonParser.ValueContext)
            else:
                return self.getTypedRuleContext(jsonParser.ValueContext,i)


        def getRuleIndex(self):
            return jsonParser.RULE_arr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr" ):
                listener.enterArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr" ):
                listener.exitArr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr" ):
                return visitor.visitArr(self)
            else:
                return visitor.visitChildren(self)




    def arr(self):

        localctx = jsonParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arr)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(jsonParser.T__4)
                self.state = 48
                self.value()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 49
                    self.match(jsonParser.T__1)
                    self.state = 50
                    self.value()
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 56
                self.match(jsonParser.T__5)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(jsonParser.T__4)
                self.state = 59
                self.match(jsonParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





