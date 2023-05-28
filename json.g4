grammar json;

init: value;
value:  STR | num | BOOL | NULL | arr |obj ;

obj: '{' data (',' data)* '}' | '{' '}';
data: key ':' value;
key: STR;

num: INT | FLOAT;
arr: '[' value (',' value)* ']' | '[' ']';

WS: [ \t\r\n]+ -> skip;
INT: '-'? '0' EXP?| '-'? [1-9][0-9]* EXP?;
FLOAT: '-'? '0.'[0-9]+ EXP? | '-'? [1-9][0-9]*'.'[0-9]+ EXP?;
EXP: 'e'ALTINT;
ALTINT: [+-]? [0-9]+;
BOOL: 'true' | 'false';
NULL: 'null';
STR: '"' CHAR+ '"' | '"' '"';
CHAR: [a-záàâãäéèêëíìîïóòôõöúùûüçA-ZÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ 0-9_,.:;/|] | '[' | ']' | '\\' | '\'';
