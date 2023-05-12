grammar json;

init: 'hello' nomes;
nomes: NOME (',' NOME)*;
NOME: [a-z]+;
WS: [ \t\r\n] -> skip;