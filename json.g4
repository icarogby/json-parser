grammar json;

init: texto;

texto: (SIMB*|PAL+) (SIMB* PAL+| PAL* SIMB+)*;

PAL: [a-záàâãäéèêëíìîïóòôõöúùûüçA-ZÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ0-9]+;
SIMB:[,."':;?!(){}<>-] |'[' | ']' |'/' | '\\'|'&'|'ª';
WS: [ \t\r\n]+ -> skip;

/*((SIMB|COLCHETE|BARRA)*|PAL+) ((SIMB|COLCHETE|BARRA)* PAL+| PAL* SIMB+)*;