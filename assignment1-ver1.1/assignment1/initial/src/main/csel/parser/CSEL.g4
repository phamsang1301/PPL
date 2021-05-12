grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
    language=Python3;
}

program  : (vardecl  | functiondecl )*  EOF ;

iden: ID_SIGN | ID_NOT_SIGN;

ID_SIGN:    (DOL | [a-z]) ([a-zA-Z_0-9])*;

ID_NOT_SIGN:    [a-z]([a-zA-Z_0-9])*;

vardecl: LET elem (CM elem)*  SM;

elem:   (iden (COLON type_arr)? (EQUAL (literals | expression))?)| array_decl | json_decl | constantdecl;

array_decl: id_array (COLON type_arr)? (EQUAL array_lit)?;

id_array:   iden LSQ (literals | call_stmt) (CM (literals | call_stmt))? RSQ;

json_decl: iden EQUAL json_lit;

functiondecl: FUNCTION iden parameters LS body RS;

parameters: LCC parameter (CM parameter)* RCC;

parameter: (iden | expression6)?;

body: ( vardecl* stmt+ ) | ( vardecl+ stmt* );

stmt:   assign_stmt
        | if_stmt
        | while_stmt
        | for_stmt
        | return_stmt
        | break_stmt
        | continue_stmt
        | call_stmt;

assign_stmt: (iden | id_array) EQUAL expression SM;

if_stmt: IF condi stmt_list (ELIF condi stmt_list)* (ELSE stmt_list)?;

condi: LCC expression RCC;

stmt_list: LS stmt* RS;

for_stmt: for_of | for_in;

for_in: FOR iden IN (iden | array_lit) stmt_list;

for_of: FOR iden OF iden stmt_list;

while_stmt: WHILE condi stmt_list;

break_stmt: BREAK SM;

continue_stmt:  CONTINUE SM;

call_stmt:  function_call SM;

return_stmt:    RETURN (expression |call_stmt )? SM;

/* 4 Type and value */

array_boolean: boolean_lit (CM boolean_lit)*;

array_num: NUMBER_LIT (CM NUMBER_LIT)*;

array_str: STRING_LIT (CM STRING_LIT)*;

array_json: json_lit (CM json_lit)*;

array_arr: array_lit (CM array_lit)*;

// array_real: REAL_LIT (CM REAL_LIT)*;

// SET NEW VALUE
new_val: iden LSQ STRING_LIT RSQ EQUAL expression SM;
//get value

/* 5  */
// 5.1 variable fragment

// CONSTANT

constantdecl: CONSTANT DOL ID_NOT_SIGN (COLON type_arr)? (EQUAL expression)?;//note

/*6 EXPRESSION */

booleanexp: (boolean_lit | iden) (NOT | OR | AND) (boolean_lit | iden);

stringexp: (STRING_LIT | iden ) (CAT | COM) (STRING_LIT | iden) ;

numexp: (NUMBER_LIT | iden) (ADD | MOD | MUL | DIV | SUB | ASS | DIF | BGT | LGT | BGZ | LGZ) (NUMBER_LIT | iden);

// realexp: (REAL_LIT | iden) (ADD | MUL | DIV | SUB | ASS | DIF | BGT | LGT | BGZ | LGZ) (REAL_LIT | iden);

function_call: CALL LCC iden CM LSQ (expression | function_call_el | function_call )? RSQ RCC;
function_call_el:    NUMBER_LIT (CM NUMBER_LIT)*;
expression:     expression relational expression | expression9; // relational
expression9:    expression9 stri expression9 | expression1;
expression1:    expression1 logical expression2 | expression2;  // logical
expression2:    expression2 adding expression3 | expression3;  // adding
expression3:    expression3 multiplying expression4 | expression4;// multiplying
expression4:    NOT expression4 | expression5;   // logical not
expression5:    SUB expression5 | expression6;   // sign
expression6:    expression6 LSQ expression RSQ | expression7; // index
expression7:    function_call_el | expression8; //functioncall
expression8:    literals| id_array | iden | LCC expression RCC ; //
/*Lexer Declaretion */


// indentifers

//ID_SMALL: [a-z] [a-zA-Z_0-9]*;

// 3.literals

literals:    NUMBER_LIT
            | STRING_LIT 
            | boolean_lit
            | json_lit
            | array_lit;

// DOMAIN VALUES
// REAL_LIT:     INTEGER_LIT+ DOT? (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
//             | INTEGER_LIT* DOT DIGIT+ EXPONENT? // (1).5(e-4)
//             | INTEGER_LIT+ EXPONENT // 12e-5  
//             ;

// INTEGER_LIT:    
fragment INT_L: ('0' | NDIGIT) DIGIT*;
NUMBER_LIT: ('0' | NDIGIT) DIGIT*
            |INT_L+ DOT? (DIGIT | EXPONENT)* 
            | INT_L* DOT DIGIT+ EXPONENT? 
            | INT_L+ EXPONENT;


boolean_lit: TRUE | FALSE;

json_lit: LS elem_json (CM elem_json)* RS;

elem_json: iden COLON ( NUMBER_LIT | json_lit  | STRING_LIT | boolean_lit | array_lit);

array_lit: LSQ (array_boolean | array_num | array_json | array_str | array_arr) RSQ;

// block comment

BLOCK_COMMENT: ('##' .*? '##') -> skip ;

// key word

BREAK:       'Break';
CONTINUE:    'Continue';
IF:          'If';
ELIF:        'Elif';
ELSE:        'Else';
WHILE:       'While';
FOR:         'For';
OF:          'Of';
IN:          'In';
FUNCTION:    'Function';
LET:         'Let';
TRUE:        'True';
FALSE:       'False';
CALL:        'Call';
RETURN:      'Return';
NUMBER:      'Number';
BOOLEAN:     'Boolean';
STRING:      'String';
JSON:        'Json';
ARRAY:       'Array';
CONSTANT:    'Constant';
// uliti
type_arr:       NUMBER | STRING | JSON | BOOLEAN;
adding:        ADD | SUB;
multiplying:    MUL | DIV | MOD;
logical:        AND | OR;
relational:     ASS | DIF | BGT | BGZ | LGT | LGZ;
stri:            CAT | COM;
// operators
fragment EXPONENT:    [eE] [+-]? DIGIT+;
ADD:     '+';
SUB:     '-';
MUL:     '*';
DIV:     '/';
MOD:     '%';
NOT:     '!';
AMP:     '&';
AND:     '&&';
OR:      '||';
EQUAL:   '=';
ASS:     '==';
DIF:     '!=';
BGT:     '>';
LGT:     '<';
BGZ:     '>=';
LGZ:     '<=';
COM:     '==.';
CAT:     '+.';

// seperators

RCC:     ')';
LCC:     '(';
RSQ:     ']';
LSQ:     '[';
LS:      '{';
RS:      '}';
SM:      ';';
DOT:     '.';
COLON:   ':';
CM:      ',';
DOL:     '$'; 
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// then more

//fragment CHAR_STR:   ~[\b\t\n\f\r"'\\];
fragment DIGIT:      [0-9];
fragment NDIGIT:     [1-9];
fragment SIGN:       [+-];

// string
// STRING_LIT: '"' ('\'"' | '\\' ['bfrnt\\] | ~['"\n\\])* '"';
STRING_LIT:  ["] (~[\b\f\r\n\t\\'"] | '\\' [bfrnt'\\] | '\'"')* ["]{
    temp = str(self.text)
    self.text = temp[1:-1]
};
// { super().emit().text = super().emit().text[1:][:-1]

// };

UNCLOSE_STRING: '"' (~[\b\f\r\n\t\\'"] | '\\' [bfrnt'\\] | '\'"')*  ([\b\f\r\n\t\\] | EOF) {
    legalescape = ['\b', '\t', '\n', '\f', '\r', '\\', "\'"]
    tempstr = str(self.text)
    if tempstr[-1] in legalescape:
        raise UncloseString(tempstr[1:-1])
    else :
        raise UncloseString(tempstr[1:])
};
ILLEGAL_ESCAPE:
    '"'(~[\b\f\r\n\t\\'"] | '\\' [bfrnt'\\] | '\'"')* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

	
fragment ESC_ILLEGAL: ('\\' ~[btnfr'\\]) | (['] ~["]);


// UNCLOSE_STRING: '"' ('\'"' | '\\' ['bfrnt\\] | ~['"\n\\])*;
UNTERMINATED_COMMENT: '#' .?;

ID: [a-z][a-zA-Z0-9_]*;
ERROR_CHAR: .;