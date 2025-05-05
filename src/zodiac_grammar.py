from textx import metamodel_from_str

# Define Zodiac language grammar using textX
zodiac_grammar = """
Program:
    statements*=Statement
;

Statement:
    VariableDeclaration |
    InputStatement |
    PrintStatement |
    IfStatement |
    FunctionDeclaration |
    FunctionCall |
    ReturnStatement |
    Block
;

VariableDeclaration:
    'var' name=ID ':' type=Type ('=' expression=Expression)? ';'
;

Type:
    'String' | 'Int' | 'Date' | 'Bool' | 'ZodiacSign'
;

InputStatement:
    name=ID '=' 'input' '(' prompt=STRING ')' ';'
;

PrintStatement:
    'print' '(' expression=Expression ')' ';'
;

IfStatement:
    'if' '(' condition=Expression ')' thenBlock=Block
    ('else' elseBlock=Block)?
;

Block:
    '{' statements*=Statement '}'
;

FunctionDeclaration:
    'func' name=ID '(' params*=Parameter[','] ')' ('->' returnType=Type)? body=Block
;

Parameter:
    name=ID ':' type=Type
;

FunctionCall:
    name=ID '(' args*=Expression[','] ')'
;

ReturnStatement:
    'return' expression=Expression ';'
;

Expression:
    Literal | ID | FunctionCall | BinaryOperation | TemplateString
;

Literal:
    IntLiteral | StringLiteral | BoolLiteral
;

IntLiteral:
    value=INT
;

StringLiteral:
    value=STRING
;

BoolLiteral:
    value=BOOL
;

BinaryOperation:
    left=Expression operator=Operator right=Expression
;

Operator:
    '==' | '!=' | '<' | '>' | '<=' | '>=' | '+' | '-' | '*' | '/' | '&&' | '||'
;

TemplateString:
    '${' expression=Expression '}'
;

Comment:
    /\/\/.*$/
;

BOOL:
    "true" | "false"
;
"""

# Create metamodel from grammar
zodiac_metamodel = metamodel_from_str(zodiac_grammar)