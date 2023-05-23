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
        4,0,3,24,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,9,8,0,11,0,12,0,10,
        1,1,1,1,1,1,3,1,16,8,1,1,2,4,2,19,8,2,11,2,12,2,20,1,2,1,2,0,0,3,
        1,1,3,2,5,3,1,0,3,22,0,48,57,65,90,97,122,160,164,167,175,178,182,
        185,188,195,195,338,339,352,353,381,381,402,402,710,710,8211,8211,
        8217,8218,8220,8222,8225,8226,8240,8240,8249,8250,8364,8364,8482,
        8482,65533,65533,8,0,33,34,38,41,44,47,58,60,62,63,91,93,123,123,
        125,125,3,0,9,10,13,13,32,32,26,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,1,8,1,0,0,0,3,15,1,0,0,0,5,18,1,0,0,0,7,9,7,0,0,0,8,7,1,0,0,
        0,9,10,1,0,0,0,10,8,1,0,0,0,10,11,1,0,0,0,11,2,1,0,0,0,12,16,7,1,
        0,0,13,14,5,194,0,0,14,16,5,170,0,0,15,12,1,0,0,0,15,13,1,0,0,0,
        16,4,1,0,0,0,17,19,7,2,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,
        0,0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,6,2,0,0,23,6,1,0,0,0,4,0,10,
        15,20,1,6,0,0
    ]

class jsonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PAL = 1
    SIMB = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "PAL", "SIMB", "WS" ]

    ruleNames = [ "PAL", "SIMB", "WS" ]

    grammarFileName = "json.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


