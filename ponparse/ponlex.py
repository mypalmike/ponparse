import ply.lex as lex
from ply.lex import TOKEN

# Stupid stuff to consider
# OK! nan (float)
# OK! inf (float)
# OK! -inf (float)
# OK! 2.52e+5 (float)
# OK! 2.52e-5 (float)
# OK! None
# XX! string escapes (\x08, \t, \r, \n)
# XX? string unicode (Some works. Need more testing.)
# XX! double-quotes (python outputs this for strings containing single quotes but not double quotes like e.g. "'")

tokens = (
    'INTEGER',
    'FLOAT',
    'BOOLEAN',
    'STRING',
    'NONE',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'COLON',
    'COMMA',
)


t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_COMMA = r','


def t_STRING(t):
    r'(\'.*?\'|\".*?\")'
    t.value = t.value[1:-1]  # Remove outer quotes.
    return t


float_exp = r'-?[0-9](\.[0-9]+)?e(\+|-)[0-9]+'
float_normal = r'-?[0-9]+\.[0-9]+'
float_special = r'(nan|inf|-inf)'
float_any = r'(' + float_exp + r'|' + float_normal + r'|' + float_special + r')'

@TOKEN(float_any)
def t_FLOAT(t):
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t


def t_BOOLEAN(t):
    r'(True|False)'
    t.value = (t.value == 'True')
    return t


def t_NONE(t):
    r'None'
    t.value = None
    return t



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'


def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# def main():
#     data = '''
#     { 'blahΔ\t\r' :
#             True, -123: -1.528e+53,
#             2.3: ('a', -inf)}
#     '''
#     # data = '123.45'
#     lexer.input(data)
#     # Tokenize
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break      # No more input
#         print(tok)


# if __name__ == '__main__':
#     main()