# Generated from C:/Users/icaro/PycharmProjects/json-parser\json.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,26,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,2,4,2,19,8,2,11,2,12,2,20,1,3,1,3,1,3,1,3,0,0,4,
        1,1,3,2,5,3,7,4,1,0,2,1,0,97,122,3,0,9,10,13,13,32,32,26,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,0,0,3,15,1,0,0,0,
        5,18,1,0,0,0,7,22,1,0,0,0,9,10,5,104,0,0,10,11,5,101,0,0,11,12,5,
        108,0,0,12,13,5,108,0,0,13,14,5,111,0,0,14,2,1,0,0,0,15,16,5,44,
        0,0,16,4,1,0,0,0,17,19,7,0,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,
        1,0,0,0,20,21,1,0,0,0,21,6,1,0,0,0,22,23,7,1,0,0,23,24,1,0,0,0,24,
        25,6,3,0,0,25,8,1,0,0,0,2,0,20,1,6,0,0
    ]

class jsonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NOME = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hello'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NOME", "WS" ]

    ruleNames = [ "T__0", "T__1", "NOME", "WS" ]

    grammarFileName = "json.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


