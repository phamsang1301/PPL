//1813810
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


program:  decllist EOF;
//--------------------program---------------------------

decllist: var_decl* func_decl*;
var_decl: glo_constant_decl | var_glo_decl;

var_glo_decl: LET list_var SM;
var_loc_decl: LET list_var SM;
glo_constant_decl: CONSTANT list_var SM;
loc_constant_decl: CONSTANT list_var SM;
list_var: ID CM list_var 
        | ID ASSIGN (literal | exp) CM list_var
        | ID CL primitive_types ASSIGN (literal | exp) CM list_var
        | ID CL primitive_types ASSIGN (literal | exp)
        | ID CL primitive_types | CM list_var
        | ID CL primitive_types
        | ID ASSIGN (literal | exp)
        | ID LSB list_index RSB ASSIGN (literal | exp) CM list_var
        | ID LSB list_index RSB ASSIGN(literal | exp)
        | ID LSB list_index RSB
        | ID LSB list_index RSB CM list_var
        | ID;
list_index: NUMBER_LITERAL CM list_index | NUMBER_LITERAL; 


// Function 
func_decl: 
          FUNCTION ID  LP (list_parameters)? RP  LCB body? RCB;

list_parameters: parameter CM list_parameters
              
              |  parameter;
parameter: ID |  ID LSB NUMBER_LITERAL ( CM NUMBER_LITERAL)* RSB;

body: bodystmt; 
bodystmt: stmtList;

stmtList: (stmt | var_loc_decl | loc_constant_decl) stmtList | stmt
         | var_loc_decl
         | loc_constant_decl;
stmt: if_Stmt
    | assign_Stmt
    | forIn_Stmt
    | forOf_Stmt
    | while_Stmt
    | break_Stmt
    | continue_Stmt
    | call_Stmt
    | return_Stmt;
if_Stmt: IF LP exp RP LCB stmtList? RCB
      |  IF LP exp RP LCB stmtList? RCB (list_elif | else_Stmt)
      |  IF LP exp RP LCB stmtList? RCB list_elif else_Stmt;

list_elif: ELIF LP exp RP LCB stmtList? RCB list_elif
    | ELIF LP exp RP LCB stmtList? RCB;

else_Stmt: ELSE LCB stmtList? RCB; 

assign_Stmt: lhs ASSIGN exp SM;
forIn_Stmt: FOR ID IN (array_literal | ID) LCB stmtList? RCB;
forOf_Stmt: FOR ID OF (json_literal  | ID) LCB stmtList? RCB;
while_Stmt: WHILE LP exp RP LCB stmtList? RCB;
break_Stmt: BREAK SM;
continue_Stmt: CONTINUE SM;
call_Stmt: CALL LP ID CM LSB list_exp? RSB RP SM;
list_exp: exp CM list_exp | exp;
return_Stmt: RETURN exp SM | RETURN SM;
lhs: ID | index_exp;

exp: exp1 (EQ | NOT_EQ | LESS_T | GREAT_T | LESS_E | GREAT_E | COMPARE_STR) exp1 | exp1;
exp1: exp1 (AND | OR) exp2 | exp2;
exp2: exp2 (ADD | SUB | ADD_STR) exp3 | exp3;
exp3: exp3 (MUL | DIV | MOD) exp4 | exp4;
exp4: NOT exp4 | exp5;
exp5: SUB exp5 | index_exp;
index_exp: exp7 (LSB exp (CM exp)* RSB)*;
exp7: operands;

operands: literal | ID | funcCall | LP exp RP;
funcCall: CALL LP ID CM LSB list_exp? RSB RP;

//fragment
fragment DOLLAR: '$';
fragment DIGIT: [0-9];
fragment LOWCASE: [a-z];
fragment UPCASE: [A-Z];
fragment LETTER: LOWCASE | UPCASE;
fragment UNDERSCORE: '_';


//--------------------------- Lexer-----------------------------------
//Skip

WS : [ \t\r\n\f]+ -> skip ;  // skip spaces, tabs, newlines 

// Comment
COMMENT: '##' .*? '##' -> skip;

//Identifiers

ID: (DOLLAR | LOWCASE)(LETTER | UNDERSCORE | DIGIT)*;

// Literals 
literal: NUMBER_LITERAL 
        | BOOLEAN_LITERAL 
        | STRING_LITERAL 
        | array_literal 
        | json_literal;  

//---------Number
// fragment EXPONENT: ;
fragment SIGN:  '+' | '-';
fragment INT_PART:  [0-9][0-9]* ;
fragment DEC_PART: '.' [0-9]+;
fragment EXPONENT_PART: [eE][+-]?[0-9]+;

NUMBER_LITERAL: [SIGN]? INT_PART ('.'? | (DEC_PART EXPONENT_PART?)?)
              | [SIGN]? INT_PART ('.'?  EXPONENT_PART?);

// NUMBER_LITERAL: SIGN? [1-9]DIGIT* (DOT DIGIT (EXPONENT DIGIT)?)?
//               | '0';
  //-------Boolean
BOOLEAN_LITERAL: TRUE | FALSE;

  //-------String
fragment ESC: '\\' [bfrnt'\\];
fragment DOUBLE_QUOTE: '\'"';
fragment CHARACTER: ~[\b\f\r\n\t\\'"] | ESC | DOUBLE_QUOTE;
STRING_LITERAL: ["] CHARACTER* ["]{
    temp = str(self.text)
    self.text = temp[1:-1]
};


//---------Array
// list_literals: LSB ((literal CM list_literals) | literal) RSB; 
// array_literal:  LSB literal CM list_literals RSB;

array_literal: LSB ( literal ( CM literal)*) RSB
              | LSB RSB;

//--------- JSON

element: ID CL literal;
list_elements: element CM list_elements | element;
json_literal: LCB list_elements RCB
              | LCB RCB;

primitive_types: NUMBER | BOOLEAN | STRING | ARRAY | JSON;

//Keywords
BREAK: 'Break';
CONTINUE:'Continue';
IF: 'If';
ELIF: 'Elif';
ELSE: 'Else';
WHILE: 'While';
FOR: 'For';
OF: 'Of';
IN: 'In';
FUNCTION: 'Function';
LET: 'Let';
TRUE: 'True';
FALSE: 'False';
CALL: 'Call';
RETURN: 'Return';
NUMBER: 'Number';
BOOLEAN: 'Boolean';  
STRING: 'String';
JSON: 'JSON';
ARRAY: 'Array';
CONSTANT: 'Constant';



// Operator
   // --------Arithmetic
ADD: '+';
SUB: '-';
DIV: '/';
MOD: '%';
MUL: '*';
ASSIGN: '=';

  // --------Relational
EQ: '==';
NOT_EQ: '!=';
LESS_T: '<';
GREAT_T: '>';
LESS_E: '<=';
GREAT_E: '>=';

  //--------Boolean
NOT: '!';
AND: '&&';
OR: '||';

  // --------String
ADD_STR: '+.';
COMPARE_STR: '==.';

// --------Seperators
LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';

SM: ';';
CM: ',';
CL: ':';
DOT: '.';

// //Reference
// REF: '&';

// coercions
// STR2NUM: 'str2num';
// NUM2STR: 'num2str';
// STR2BOOL: 'str2bool';
// BOOL2STR: 'bool2str';



UNCLOSE_STRING: '"' CHARACTER* ([\b\f\r\n\t\\] | EOF) {
    legalescape = ['\b', '\t', '\n', '\f', '\r', '\\', "\'"]
    tempstr = str(self.text)
    if tempstr[-1] in legalescape:
        raise UncloseString(tempstr[1:-1])
    else :
        raise UncloseString(tempstr[1:])
};
ILLEGAL_ESCAPE:
	'"' CHARACTER* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
fragment ESC_ILLEGAL: ('\\' ~[btnfr'\\]) | (['] ~["]);
UNTERMINATED_COMMENT:
	'##' (~'#' | '#' ~'#')? {
		raise UnterminatedComment()
	};
ERROR_CHAR: .;

