grammar json;

init: obj;
obj: '{' data (',' data)* '}';
data: key ':' value;

key: STR;
value: STR | num | BOOL | NULL | vec | obj;

num: INT | FLOAT;
vec: '[' obj (',' obj)* ']';

STR: '"' [a-záàâãäéèêëíìîïóòôõöúùûüçA-ZÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ 0-9_]+ '"';
INT: [0-9]+ | '-'[0-9]+ ;
FLOAT: [0-9]+'.'[0-9][0-9] | '-'[0-9]+'.'[0-9][0-9];
BOOL: 'true' | 'false';
NULL: 'null';

SIMB:[,."':;?!(){}<>-] |'[' | ']' |'/' | '\\'|'&'|'ª';
WS: [ \t\r\n]+ -> skip;

/*((SIMB|COLCHETE|BARRA)*|PAL+) ((SIMB|COLCHETE|BARRA)* PAL+| PAL* SIMB+)*;