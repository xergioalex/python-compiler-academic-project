#-------------------------------------------------------------------------------
# Nombre:       Deus Ex Machine
# Autores:      Sergio Aleander Florez Galeano
#               Camilo Fernandez Bernal
# Descripcion:  Analizador Lexico de nuestro Compilador
#-------------------------------------------------------------------------------

import os
import sys
import DeuxExMachinaLexico
import ply.yacc as yacc
sys.path.insert(0,"../..")

# Obtener mapa de tokens
tokens = DeuxExMachinaLexico.tokens

#  ---------------------------------------------------------------
#  GRAMATICAS BNF
#  ---------------------------------------------------------------




#Programa
def p_programa(token):
    'programa : CIERRELINEA NICK CIERRELINEA DOSPUNTOS restoprograma'
    pass

def p_restoprograma(token):
    '''restoprograma : principal
    | importarlibrerias prototipos constantes principal
    | importarlibrerias prototipos constantes global principal
    | importarlibrerias prototipos constantes global principal funciones
    | importarlibrerias prototipos principal
    | importarlibrerias principal
    | prototipos constantes global principal funciones
    | constantes global principal funciones
    | prototipos global principal funciones
    | prototipos constantes principal funciones
    | prototipos constantes global principal
    | importarlibrerias constantes global principal funciones
    | importarlibrerias global principal funciones
    | importarlibrerias principal funciones
    | importarlibrerias prototipos global principal funciones
    | importarlibrerias prototipos principal funciones
    | importarlibrerias prototipos constantes principal funciones '''
    pass

#Importar  Libreria &
def p_importarlibrerias(token):
    '''importarlibrerias : IMPORTAR CADVALOR CIERRELINEA
        | IMPORTAR CADVALOR CIERRELINEA importarlibrerias'''
    pass

#Prototipos de funciones
def p_prototipos(token):
    '''prototipos : prototipofuncion
        | prototipos prototipofuncion '''
    pass

def p_prototipofuncion(token):
    '''prototipofuncion : tipodato  MACRO NICK IZQPAREN DERPAREN
        | tipodato  MACRO NICK IZQPAREN declaracionparametros  DERPAREN'''
    pass

#Constantes
def p_constantes(token):
    '''constantes : CONSTANTE tipodato  ASIGNAR NICK dato  CIERRELINEA
        | CONSTANTE tipodato  ASIGNAR NICK dato  CIERRELINEA constantes'''
    pass

#Variables y Arreglos Globales y Estructuras
def p_global(token):
    '''global : declaraciones
        | global declaraciones '''
    pass

def p_declaraciones(token):
    '''declaraciones : declaracion
        | declaracionestructura'''
    pass

#Funcion Principal
def p_principal(token):
    'principal : VACIO MACRO PRINCIPAL IZQPAREN DERPAREN IZQLLAVE bloque  DERLLAVE'
    pass

#Funciones
def p_funciones(token):
    '''funciones : declaracionfuncion
        | funciones declaracionfuncion  '''
    pass

#Tipos de dato
def p_tipodato(token):
    '''tipodato : ENTERO
        | REAL
        | CARACTER
        | CADENA
        | BOOLEANO'''
    pass

#Expresiones
def p_expresion(token):
    '''expresion : dato
        | operador expresion
        | operador expresion expresion
        | IZQPAREN expresion  DERPAREN '''
    pass

#Datos
def p_dato(token):
    '''dato : NICK
        | ENTVALOR
        | REALVALOR
        | CARVALOR
        | CADVALOR
        | BOOLVALOR
        | datoarreglo
        | datosarreglo
        | datofuncion
        | operadorternario '''
    pass

def p_datoarreglo(token):
    '''datoarreglo : NICK indicearreglo'''
    pass

def p_indicearreglo(token):
    '''indicearreglo : IZQCORCHET dato  DERCORCHET
        | indicearreglo IZQCORCHET dato DERCORCHET '''
    pass

def p_datosarreglo(token):
    '''datosarreglo : IZQCORCHET restoarreglo  DERCORCHET
        | IZQCORCHET datosarreglo COMA IZQCORCHET restoarreglo  DERCORCHET DERCORCHET'''
    pass

def p_restoarreglo(token):
    '''restoarreglo : dato
        | restoarreglo COMA dato '''
    pass

def p_datofuncion(token):
    'datofuncion : NICK IZQPAREN parametros  DERPAREN'
    pass

def p_parametros(token):
    '''parametros : dato
        | dato COMA parametros'''
    pass

#Operador ternario
def p_operadorternario(token):
    'operadorternario : IZQPAREN  expresion  DERPAREN TERNARIO dato DOSPUNTOS dato '
    pass

#Operadores
def p_operador(token):
    '''operador : SUMA
        | MENOS
        | MASMAS
        | MENOSMENOS
        | MULT
        | DIV
        | MODULO
        | EXP
        | Y
        | O
        | NEGAR
        | MENOR
        | MAYOR
        | MENORIGUAL
        | MAYORIGUAL
        | IGUAL
        | DIFERENTE'''
    pass


def p_operadorasignacion(token):
    '''operadorasignacion : IGUAL
        | SUMAIGUAL
        | MENOSIGUAL
        | MULTIGUAL
        | DIVIGUAL'''
    pass

#Bloque
def p_bloque(token):
    '''bloque : sentencia
        | sentencia  bloque'''
    pass

#Sentencias
def p_sentencia(token):
    '''sentencia : asignacion
        | declaracion
        | sentenciasalto
        | sentencialeer
        | sentenciaescribir
        | ciclohacer
        | ciclomientras
        | ciclopara
        | selector
        | condicionalsi'''
    pass

def p_sentenciasalto(token):
    'sentenciasalto : tokensalto  CIERRELINEA'
    pass

def p_tokensalto(token):
    '''tokensalto : ROMPER
        | CONTINUE
        | RETORNO'''
    pass

def p_sentencialeer(token):
    'sentencialeer : LEER IZQPAREN DERPAREN'
    pass

def p_sentenciaescribir(token):
    'sentenciaescribir : IMPRIMIR IZQPAREN info  DERPAREN CIERRELINEA'
    pass

def p_info(token):
    '''info : dato
        | dato  COMA dato'''
    pass


#Declaracion de variables y arreglos
def p_declaracion(token):
    'declaracion : tipodato  restodeclaracion  CIERRELINEA'
    pass

def p_restodeclaracion(token):
    '''restodeclaracion : NICK
        | ASIGNAR NICK dato
        | corchetes  NICK
        | corchetes  ASIGNAR NICK tipodato  tamanoarreglo
        | corchetes  ASIGNAR NICK datosarreglo'''
    pass

def p_corchetes(token):
    '''corchetes : IZQCORCHET DERCORCHET
        | IZQCORCHET DERCORCHET corchetes'''
    pass

def p_tamanoarreglo(token):
    '''tamanoarreglo : IZQCORCHET dato  DERCORCHET
        | tamanoarreglo IZQCORCHET dato  DERCORCHET '''
    pass

#Declaracion de funciones
def p_declaracionfuncion(token):
    '''declaracionfuncion : VACIO MACRO NICK IZQPAREN DERPAREN IZQLLAVE bloque  DERLLAVE
        | tipodato  MACRO NICK IZQPAREN DERPAREN IZQLLAVE bloque  DERLLAVE
        | tipodato  MACRO NICK IZQPAREN declaracionparametros  DERPAREN IZQLLAVE bloque  DERLLAVE'''
    pass

def p_declaracionparametros(token):
    '''declaracionparametros : nuevoparametro
        | declaracionparametros nuevoparametro '''
    pass

def p_nuevoparametro(token):
    '''nuevoparametro : tipodato  NICK
        | tipodato  corchetes  NICK'''
    pass

#Declaracion de funciones
def p_declaracionestructura(token):
    'declaracionestructura : ESTRUCTURA NICK IZQPAREN declaraciones DERPAREN'
    pass

#Asignacion
def p_asignacion(token):
    '''asignacion : ASIGNAR NICK dato  CIERRELINEA
    	| ASIGNAR NICK NULO CIERRELINEA
        | operadorasignacion  NICK dato  CIERRELINEA'''
    pass

#Estructuras De Control

#Condicional si
def p_condicionalsi(token):
    '''condicionalsi : SI IZQPAREN expresion  DERPAREN  accion
	   | SI IZQPAREN expresion  DERPAREN accion  SINO accion'''
    pass

def p_accion(token):
    '''accion : sentencia
        | IZQLLAVE bloque DERLLAVE'''
    pass

#Ciclo hacer
def p_ciclohacer(token):
    'ciclohacer : HACER IZQLLAVE bloque DERLLAVE MIENTRAS IZQPAREN expresion  DERPAREN'
    pass

#Ciclo mientras
def p_ciclomientras(token):
    'ciclomientras : MIENTRAS IZQPAREN expresion  DERPAREN accion'
    pass

#Ciclo para
def p_ciclopara(token):
    'ciclopara : PARA IZQPAREN declaracion DOSPUNTOS expresion DOSPUNTOS asignacion  DERPAREN'
    pass

#Estructura Selector
def p_selector(token):
    'selector : SELECTOR IZQPAREN variablecontrol  DERPAREN IZQLLAVE casos  DERLLAVE'
    pass

def p_variablecontrol(token):
    '''variablecontrol : NICK
        | datoarreglo
        | datofuncion'''
    pass

def p_casos(token):
    '''casos : casoselector
        | casoselector  casoespecial'''
    pass

def p_casoselector(token):
    '''casoselector : CASO valorcontrol  DOSPUNTOS  bloque
        |  casoselector CASO valorcontrol  DOSPUNTOS  bloque  '''
    pass

def p_valorcontrol(token):
    '''valorcontrol : ENTVALOR
        | CARVALOR'''
    pass

def p_casoespecial(token):
    'casoespecial : DEFECTO DOSPUNTOS bloque'
    pass




#  ---------------------------------------------------------------
#  ERROR
#  ---------------------------------------------------------------
##def p_error(t):
##    if p is not None:
##        print "Error de Sintaxis" + str(p.lexer.lineno) + "Token desconocido "+ str(p.value)
##    else:
##        print "Error de sintaxis en la linea " + str(lenguaje_simple.lexer.lineno)

def p_error(t):
    print "Usted tiene un error de sintaxis en alguna parte de su codigo."
    print "Este puede estar cerca de la linea %d." % t.lineno,
    print "Buena suerte encontrandolo."
    raise ParseError()

#  ---------------------------------------------------------------
#  CONSTRUIR GRAMATICA
#  ---------------------------------------------------------------

#parser = yacc.yacc()

parser = yacc.yacc(method="LALR",debug=1)

##try:
##    fle = sys.argv[1]
##    f= open(fle)
##    dato= f.read()
##    f.close()
##except EOFError:
##    sys.exit()


