grammar gramatica;

start: texto;

texto: (SIMB*|PAL+) (SIMB* PAL+| PAL* SIMB+)*;

PAL: [a-záàâãäéèêëíìîïóòôõöúùûüçA-ZÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ0-9]+;
SIMB:[,."':;?!(){}<>_+=-] |'[' | ']' |'/' | '\\'|'&'|'ª'|'$'|'#'|'%'|'*';
WS: [ \t\r\n]+ -> skip;

/*((SIMB|COLCHETE|BARRA)*|PAL+) ((SIMB|COLCHETE|BARRA)* PAL+| PAL* SIMB+)*;