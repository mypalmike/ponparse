import ply.yacc as yacc

from .ponlex import tokens


def p_value(p):
    '''value : INTEGER
             | STRING
             | BOOLEAN
             | NONE
             | FLOAT
             | dict
             | list
             | tuple'''
    p[0] = p[1]


# def p_value_set(p):
#     'value : set'
#     p[0] = p[1]


def p_dict_dictentries(p):
    'dict : LBRACE dictentries RBRACE'
    p[0] = p[2]

def p_dictentries_comma(p):
    'dictentries : dictentry COMMA dictentries'
    p[0] = p[1]  # TODO: Copy?
    p[0].update(p[3])

def p_dictentries_dictentry(p):
    'dictentries : dictentry'
    p[0] = p[1]

def p_dictentries_empty(p):
    'dictentries : empty'
    p[0] = {}

def p_dictentry_colon(p):
    'dictentry : value COLON value'
    p[0] = {p[1]: p[3]}

def p_list_elements(p):
    'list : LBRACKET listelements RBRACKET'
    p[0] = p[2]

def p_listelements_comma(p):
    'listelements : value COMMA listelements'
    p[0] = [p[1]] + p[3]

def p_listelements_value(p):
    'listelements : value'
    p[0] = [p[1]]

def p_listelements_empty(p):
    'listelements : empty'
    p[0] = []


def p_tuple_elements(p):
    'tuple : LPAREN tupleelements RPAREN'
    p[0] = p[2]


def p_tupleelements_comma(p):
    'tupleelements : value COMMA tupleelements'
    p[0] = (p[1],) + p[3]


def p_tupleelements_value(p):
    'tupleelements : value'
    p[0] = (p[1],)


def p_tupleelements_empty(p):
    'tupleelements : empty'
    p[0] = ()


def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()


def main():
    while True:
        try:
            s = input('ponparse > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(f'type is : {type(result)}')
        print(result)

if __name__ == '__main__':
    main()
