#-------------------------------------------------------------------------------
# Nombre:       Deus Ex Machine
# Autores:      Sergio Aleander Florez Galeano
#               Camilo Fernandez Bernal
# Descripcion:  Analizador Lexico de nuestro Compilador
#-------------------------------------------------------------------------------

import os
import sys
sys.path.insert(0,"../..")

import ply.lex as lex

#  ---------------------------------------------------------------
#  TOKENS DEL ANALIZADOR LEXICO
#  ---------------------------------------------------------------
tokens = (
    #-----PALABRAS RESERVADAS-------#

    #Estructuras de control
    'PRINCIPAL',    #principal
    'IMPORTAR',     #importar
    'CONSTANTE',    #constante
    'HACER',        #hacer
    'MIENTRAS',     #mientras
    'PARA',         #para
    'SI',           #si
    'SINO',         #sino
    'SELECTOR',     #selector
    'CASO',         #caso
    'DEFECTO',      #defecto
    'MACRO',        #macro

    #Sentencias de salto
    'ROMPER',       #romper
    'CONTINUE',     #continue
    'RETORNO',      #retorno

    #Tipos de dato
    'ESTRUCTURA',    #estructura
    'CARACTER',     #caracter
    'CADENA',       #cadena
    'ENTERO',       #entero
    'REAL',         #real
    'BOOLEANO',     #booleano
    'VACIO',        #vacio

    #Entrada/salida de datos
    'IMPRIMIR',     #print
    'LEER',         #read

    #-------------------------------#

    #Identificadores y Constantes
    'NICK',         #Identificador
    'ENTVALOR',     #Constante entera
    'REALVALOR',    #Constante entera
    'CARVALOR',     #Constante caracter
    'CADVALOR',     #Constate Cadena
    'BOOLVALOR',    #Constate Booleana

    # OPERADORES
    #Aritmeticos
    'SUMA',         #+
    'MENOS',        #-
    'MULT',         #*
    'DIV',          #/
    'MODULO',       #%
    "EXP",          #^

    #logicos
    'O',            #|
    'Y',            #&
    'NEGAR',        #~

    #Relacionales
    'MENOR',        #<
    'MENORIGUAL',   #<=
    'MAYOR',        #>
    'MAYORIGUAL',   #>=
    'IGUAL',        #==
    'DIFERENTE',    #~=

    # Asignaciones
    'ASIGNAR',      #=
    'SUMAIGUAL',    #+=
    'MENOSIGUAL',   #-=
    'MULTIGUAL',    #*=
    'DIVIGUAL',     #/=

    # Incrementos/Decrementos (++,--)
    'MASMAS',       #++
    'MENOSMENOS',   #--

    # Operador ternario
    'TERNARIO',     #?

    # Delimitadores
    'IZQPAREN',     #(
    'DERPAREN',     #)
    'IZQCORCHET',   #[
    'DERCORCHET',   #]
    'IZQLLAVE',     #:/
    'DERLLAVE',     #\:
    'COMA',         #,
    'DOSPUNTOS',    #:
    'CIERRELINEA',  # #

    )

#  ---------------------------------------------------------------
#  MAPA DE PALABRAS RESERVADAS
#  ---------------------------------------------------------------
palabras_reservadas = {
    #Estructuras de control
    'principal' : 'PRINCIPAL',
    'constante' : 'CONSTANTE',
    'importar'  : 'IMPORTAR',
    'hacer'     : 'HACER',
    'mientras'  : 'MIENTRAS',
    'para'      : 'PARA',
    'si'        : 'SI',
    'sino'      : 'SINO',
    'selector'  : 'SELECTOR',
    'caso'      : 'CASO',
    'defecto'   : 'DEFECTO',

    #Sentencias de salto
    'romper'    : 'ROMPER',
    'continue'  : 'CONTINUE',
    'retorno'   : 'RETORNO',

    #Tipos de dato
    'estructura': 'ESTRUCTURA',
    'caracter'  : 'CARACTER',
    'cadena'    : 'CADENA',
    'doble'     : 'DOBLE',
    'entero'    : 'ENTERO',
    'real'      : 'REAL',
    'booleano'  : 'BOOLEANO',
    'vacio'     : 'VACIO',

    #funciones
    'macro'     : 'MACRO',

    #Entrada/salida de datos
    'imprimir'  : 'IMPRIMIR',
    'leer'      : 'LEER'
}

#  ---------------------------------------------------------------
#  SIMBOLOS COMPLEJOS
#  ---------------------------------------------------------------

# Identificadores y palabras reservadas
def t_NICK(token):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if palabras_reservadas.has_key(token.value):
	    token.type = palabras_reservadas[token.value]
    return token

# Constante Entera
t_ENTVALOR = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Constante Real
t_REALVALOR = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# Constante Cadena
t_CADVALOR = r'\"([^\\\n]|(\\.))*?\"'

# Constante Caracter
t_CARVALOR = r'(L)?\'([^\\\n]|(\\.))*?\''

# Constante Caracter
t_BOOLVALOR = r'"verdadero"|"mentira"'

#  ---------------------------------------------------------------
#  SIMBOLOS IGNORADOS
#  ---------------------------------------------------------------

# Espacios, tabuladores
t_ignore = ' \t\x0c'

# Salto de linea
def t_newline(token):
    r'\n+'
    token.lexer.lineno += token.value.count("\n")

# Comentarios
def t_comment(token):
    r'(<<<(.|\n)*?>>>)'
    token.lexer.lineno += token.value.count('\n')

#  ---------------------------------------------------------------
#  OPERADORES
#  ---------------------------------------------------------------

# Operadores Aritmeticos
t_SUMA               = r'\+'
t_MENOS              = r'-'
t_MULT               = r'\*'
t_DIV                = r'/'
t_MODULO             = r'%'
t_EXP                = r'\^'
t_O                  = r'\|'
t_Y                  = r'&'
t_NEGAR              = r'~'
t_MENOR              = r'<'
t_MAYOR              = r'>'
t_MENORIGUAL         = r'<='
t_MAYORIGUAL         = r'>='
t_IGUAL              = r'=='
t_DIFERENTE          = r'~='

# Operadores de asignacion
t_ASIGNAR            = r'='
t_SUMAIGUAL          = r'\+='
t_MENOSIGUAL         = r'-='
t_MULTIGUAL          = r'\*='
t_DIVIGUAL           = r'/='

# Incremento / Decremento
t_MASMAS             = r'\+\+'
t_MENOSMENOS         = r'--'

# ?
t_TERNARIO           = r'\?'

# Delimitadores
t_IZQPAREN           = r'\('
t_DERPAREN           = r'\)'
t_IZQCORCHET         = r'\['
t_DERCORCHET         = r'\]'
t_IZQLLAVE           = r':/'
t_DERLLAVE           = r'\\:'
t_COMA               = r','
t_DOSPUNTOS          = r':'
t_CIERRELINEA        = r'\#'


#  ---------------------------------------------------------------
#  ERROR
#  ---------------------------------------------------------------
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

#  ---------------------------------------------------------------
#  CONSTRUIR LEXICO
#  ---------------------------------------------------------------
lexer = lex.lex()

##if __name__ == '__main__':
##    lex.runmain()

#  ---------------------------------------------------------------
#  LEXICO FUNCIONAL
#  ---------------------------------------------------------------

##archivo = open("archivoslenguaje/ejemplo_1.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_2.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_3.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_4.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_5.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_6.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_7.txt", "r")
###archivo = open("archivoslenguaje/ejemplo_8.txt", "r")
##
##lenguaje = archivo.read()
##
##lexer.input(lenguaje)
##
### Tokenizer
##for tok in lexer:
##    print tok
