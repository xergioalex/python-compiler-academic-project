 #-------------------------------------------------------------------------------
# Nombre:       Deus Ex Machine
# Autores:      Sergio Alexander Florez Galeano
#               Camilo Fernandez Bernal
# Descripcion:  Analizador Semantico de nuestro Compilador
#-------------------------------------------------------------------------------

import sys
import DeuxExMachinaLexico
import ply.yacc as yacc

import DeuxExMachinaTablaTiposSimbolos as tabla

# Obtener mapa de tokens
tokens = DeuxExMachinaLexico.tokens

#  ---------------------------------------------------------------
#  ERRORS
#  ---------------------------------------------------------------

# Clase para Errores Semanticos
class ErrorSemantico(Exception):
     def __init__(self, valor):
         self.valor = valor
     def __str__(self):
         return repr((self.valor))

# Clase para Errores Sintacticos
class  rrorSintactico(Exception):
     def __init__(self, valor):
         self.valor = valor
     def __str__(self):
         return repr((self.valor))

#  ---------------------------------------------------------------
#  PARSER
#  ---------------------------------------------------------------

# Diccionario de Simbolos y Tipos
Tabla= tabla.Tabla()

# Listas Auxiliares
librerias=[]
constantes=[]
tempparametros = []

# Precedencia de Operadores
precedence=(
    ('left','SUMA','MENOS'),
    ('left','MULT','DIV'),
    )

#Programa: Es el no terminal PRINCIPAL que llama toda la gramatica e inicia todo.
def p_programa(p):
    #'programa : CIERRELINEA NICK CIERRELINEA importarlibrerias prototipos constantes global principal funciones'
    '''programa : CIERRELINEA NICK CIERRELINEA importarlibrerias constantes declaraciones prototipos principal funciones
        | CIERRELINEA NICK CIERRELINEA importarlibrerias principal
        | CIERRELINEA NICK CIERRELINEA importarlibrerias declaraciones principal
        | CIERRELINEA NICK CIERRELINEA principal
        | CIERRELINEA NICK CIERRELINEA constantes principal
        | CIERRELINEA NICK CIERRELINEA declaraciones principal
        | CIERRELINEA NICK CIERRELINEA constantes declaraciones principal
        | CIERRELINEA NICK CIERRELINEA importarlibrerias constantes principal
        | CIERRELINEA NICK CIERRELINEA importarlibrerias constantes declaraciones principal
        | CIERRELINEA NICK CIERRELINEA prototipos principal funciones
        | CIERRELINEA NICK CIERRELINEA importarlibrerias prototipos principal funciones
        | CIERRELINEA NICK CIERRELINEA importarlibrerias constantes prototipos principal funciones
        | CIERRELINEA NICK CIERRELINEA constantes prototipos principal funciones
        | CIERRELINEA NICK CIERRELINEA constantes declaraciones prototipos principal funciones
    '''
    pass
##    for i in p:
##        print i

#LISTO
#Importar Libreria
def p_importarlibrerias_1(p):
    '''importarlibrerias : IMPORTAR CADVALOR CIERRELINEA
        | importarlibrerias IMPORTAR CADVALOR CIERRELINEA
    '''
    if(len(p)==4):
        librerias.append(p[2])
    else:
        librerias.append(p[3])
    p[0]=librerias

#Prototipos de funciones
def p_prototipos(p):
    '''prototipos : prototipofuncion
        | prototipos prototipofuncion '''
    pass


def p_prototipofuncion(p):
    '''prototipofuncion : tipodato  MACRO NICK IZQPAREN DERPAREN
        | tipodato  MACRO NICK IZQPAREN declaracionparametros  DERPAREN'''
    pass

def p_declaracionparametros(p):
    '''declaracionparametros : nuevoparametro
        | declaracionparametros COMA nuevoparametro '''
    pass

def p_nuevoparametro(p):
    '''nuevoparametro : tipodato NICK
        | tipodato IZQCORCHET DERCORCHET  NICK'''
    pass

#LISTO
#Tipos de dato
def p_tipodato(p):
    '''tipodato : ENTERO
        | REAL
        | CARACTER
        | CADENA
        | BOOLEANO'''
    p[0]=p[1]

#LISTO
#Constantes
def p_constantes(p):
    '''constantes : CONSTANTE tipodato  ASIGNAR NICK dato  CIERRELINEA
        | constantes CONSTANTE tipodato  ASIGNAR NICK dato  CIERRELINEA'''
    if(len(p)==7):
        if(not(Tabla.existeTipo(p[4])) and p[2]==p[5][1]):
            Tabla.addTipo(p[4],p[2],-1,1,-1,-1)
            Tabla.addSimbolo(p[4],'constante',p[2],-1,[],p[5][0])
            constantes.append(p[4])
        else:
            raise ErrorSemantico("El simbolo '"+p[4]+"' ya existe o los tipos no coinciden")
    else:
        if(not(Tabla.existeTipo(p[5]))  and p[3]==p[6][1]):
            Tabla.addTipo(p[5],p[3],-1,1,-1,-1)
            Tabla.addSimbolo(p[5],'constante',p[3],-1,[],p[6][0])
            constantes.append(p[5])
        else:
            raise ErrorSemantico("El simbolo '"+p[5]+"' ya existe o los tipos no coinciden")
    p[0]=constantes

#LISTO
#Datos
def p_dato_1(p):
    '''dato : ENTVALOR '''
    p[0]=[p[1],"entero"]

#LISTO
def p_dato_2(p):
    '''dato : REALVALOR '''
    p[0]=[p[1],"real"]

#LISTO
def p_dato_3(p):
    '''dato : CARVALOR '''
    p[0]=[p[1],"caracter"]

#LISTO
def p_dato_4(p):
    '''dato : CADVALOR '''
    p[0]=[p[1],"cadena"]

#LISTO
def p_dato_5(p):
    '''dato : BOOLVALOR '''
    p[0]=[p[1],"booleano"]


def p_datofuncion(p):
    'datofuncion : NICK IZQPAREN parametros  DERPAREN'
    pass

def p_parametros(p):
    '''parametros : dato
        | parametros COMA dato
    '''
    if(len(p)==2):
        tempparametros.append(p[1])
    else:
        tempparametros.append(p[3])
    p[0]=tempparametros

def p_datoarreglo(p):
    '''datoarreglo : NICK IZQCORCHET ENTVALOR DERCORCHET '''
    if(Tabla.existeTipo(p[1])):
        aux = int(p[3])
        auxarray=Tabla.getTablaSimbolos()[p[1]]
        auxtipo = auxarray.getTipo()
        temp = [auxarray.getDireccion()[aux],auxtipo]
        p[0]= temp
    else:
        raise ErrorSemantico("El simbolo '"+p[1]+"' no existe")

#Operador ternario
def p_operadorternario(p):
    'operadorternario : IZQPAREN  expresion  DERPAREN TERNARIO expresion DOSPUNTOS expresion '
    pass

def p_expresion(p):
    '''expresion : expresionsimple
        | expresioncompuesta
    '''
    p[0]=p[1]

#Expresiones
def p_expresionsimple_1(p):
    '''expresionsimple : NICK'''
    if(Tabla.existeTipo(p[1])):
        temp=Tabla.getTablaTipos()[p[1]]
        temp1= Tabla.getTablaSimbolos()[p[1]]
        p[0]=[temp1.getDireccion(),temp.getTipoBase()]
    else:
        raise ErrorSemantico("El simbolo '"+p[1]+"' no existe")


def p_expresionsimple_2(p):
    '''expresionsimple : datofuncion'''
    pass

#LISTO
def p_expresionsimple_3(p):
    '''expresionsimple : dato'''
    p[0]=p[1]

def p_expresionsimple_4(p):
    '''expresionsimple : operadorternario'''
    pass

def p_expresionsimple_5(p):
    '''expresionsimple : datoarreglo'''
    p[0] = p[1]

def p_expresioncompuesta(p):
    '''expresioncompuesta :  operador expresion
        | IZQPAREN expresion  DERPAREN
        | operador IZQPAREN expresion DERPAREN IZQPAREN expresion DERPAREN
        | operador IZQPAREN expresion DERPAREN dato
        | operador dato expresion
    '''
    pass

#LISTO
#Operadores
def p_operador(p):
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
    p[0]=p[1]


#Variables y Arreglos Globales y Estructuras
def p_declaraciones(p):
    '''declaraciones : declaracion
        | declaracionestructura
        | declaraciones declaracion
        | declaraciones declaracionestructura
    '''
    pass

#Declaracion de variables y arreglos
def p_declaracion(p):
    '''declaracion : tipodato restodeclaracion  CIERRELINEA'''
    if(len(p[2])==3):
        pass
    elif(len(p[2])==2):
        if(not(p[2][1]==p[1])):
            mensaje =  "Los tipos de dato no coinciden"
            raise ErrorSemantico(mensaje)
    else:
        Tabla.setTipoTablas(p[2],p[1])

#LISTO
def p_restodeclaracion_1(p):
    '''restodeclaracion : NICK
        | IZQCORCHET DERCORCHET  NICK
        | IZQCORCHET DERCORCHET ASIGNAR NICK tipodato IZQCORCHET ENTVALOR DERCORCHET
    '''
    if(len(p)==4):
        if(not(Tabla.existeTipo(p[3]))):
            Tabla.addTipo(p[3],-1,-1,1,-1,-1)
            Tabla.addSimbolo(p[3],'arreglo',-1,-1,[],-1)
            p[0]=p[3]
        else:
            raise ErrorSemantico("El simbolo '"+p[3]+"' ya existe")
    elif(len(p)==9):
        if(not(Tabla.existeTipo(p[4]))):
            aux =int(p[7])-1
            Tabla.addTipo(p[4],p[5],-1,p[7],0,aux)
            Tabla.addSimbolo(p[4],'arreglo',p[5],-1,[],[0]*int(p[7]))
            p[0]=[p[4],p[5]]
        else:
            raise ErrorSemantico("El simbolo '"+p[4]+"' ya existe")
    else:
        if(not(Tabla.existeTipo(p[1]))):
            Tabla.addTipo(p[1],-1,-1,1,-1,-1)
            Tabla.addSimbolo(p[1],'variable',-1,-1,[],-1)
            p[0]=p[1]
        else:
            raise ErrorSemantico("El simbolo '"+p[1]+"' ya existe")

def p_restodeclaracion_2(p):
    '''restodeclaracion : asignacion'''
    #p[1]=[operador,nick,valor,tipo]
    if(p[1][0]=='='):
        if(not(Tabla.existeTipo(p[1][1]))):
            Tabla.addTipo(p[1][1],p[1][3],-1,1,-1,-1)
            Tabla.addSimbolo(p[1][1],'variable',p[1][3],-1,[],p[1][2])
            p[0]=[p[1][1],p[1][3]]
        else:
            raise ErrorSemantico("El simbolo '"+p[1][1]+"' ya existe")
    else:
        raise ErrorSemantico("El operador '"+p[1][0]+"' no se puede usar en una declaracion debe usarse '='")

def p_restodeclaracion_3(p):
    '''restodeclaracion : IZQCORCHET DERCORCHET ASIGNAR NICK IZQCORCHET parametros DERCORCHET'''
    parametros=p[6]
    tempparametros=[]
    tipoaux= parametros[0][1]
    lista = []
    for i in parametros:
        if(tipoaux!=i[1]):
            raise ErrorSemantico("Los tipos del array '"+str(p[6])+"' no coinciden")
        tipoaux=i[1]
        lista.append(i[0])
    if(not(Tabla.existeTipo(p[4]))):
        Tabla.addTipo(p[4],tipoaux,-1,len(p[6]),0,len(p[6])-1)
        Tabla.addSimbolo(p[4],'arreglo',tipoaux,-1,[],lista)
        p[0]=[p[4],tipoaux]
    else:
        raise ErrorSemantico("El simbolo '"+p[4]+"' ya existe")
    #print p[6]

def p_declaracionestructura(p):
    'declaracionestructura : ESTRUCTURA NICK IZQPAREN declaraciones DERPAREN'
    pass

#Funcion Principal
def p_principal(p):
    'principal : VACIO MACRO PRINCIPAL IZQPAREN DERPAREN IZQLLAVE bloque DERLLAVE'
    pass

#Bloque
def p_bloque(p):
    '''bloque : sentencia
        | bloque sentencia '''
    pass

#Sentencias
def p_sentencia(p):
    '''sentencia : asignacion CIERRELINEA
        | sentenciasalto
        | sentencialeer
        | sentenciaescribir
        | condicionalsi
        | ciclohacer
        | ciclomientras
        | ciclopara
        | selector
    '''
    pass

#Estructuras De Control
#Ciclo hacer
def p_ciclohacer(p):
    'ciclohacer : HACER IZQLLAVE bloque DERLLAVE MIENTRAS IZQPAREN expresion  DERPAREN'
    pass

#Ciclo mientras
def p_ciclomientras(p):
    'ciclomientras : MIENTRAS IZQPAREN expresion  DERPAREN IZQLLAVE bloque DERLLAVE'
    pass

#Ciclo para
def p_ciclopara(p):
    'ciclopara : PARA IZQPAREN declaracion DOSPUNTOS expresion DOSPUNTOS asignacion  DERPAREN IZQLLAVE bloque DERLLAVE'
    pass

#Estructura Selector
def p_selector(p):
    'selector : SELECTOR IZQPAREN variablecontrol  DERPAREN IZQLLAVE casos  DERLLAVE'
    pass

def p_variablecontrol(p):
    'variablecontrol : NICK'
    pass

def p_casos(p):
    '''casos : casoselector
        | casoselector  casoespecial'''
    pass

def p_casoselector(p):
    '''casoselector : CASO valorcontrol  DOSPUNTOS  bloque
        |  casoselector CASO valorcontrol  DOSPUNTOS  bloque  '''
    pass

def p_valorcontrol(p):
    '''valorcontrol : ENTVALOR
        | CARVALOR'''
    pass

def p_casoespecial(p):
    'casoespecial : DEFECTO DOSPUNTOS bloque'
    pass

def p_condicionalsi (p):
    '''condicionalsi : SI IZQPAREN expresion DERPAREN  IZQLLAVE bloque DERLLAVE  SINO  IZQLLAVE bloque DERLLAVE
                    | SI IZQPAREN expresion  DERPAREN  IZQLLAVE bloque DERLLAVE'''
    pass

#LISTO
#Sentencia Salto
def p_sentenciasalto(p):
    'sentenciasalto : tokensalto  CIERRELINEA'
    p[0]=p[1]

#LISTO
def p_tokensalto(p):
    '''tokensalto : ROMPER
        | CONTINUE
        | RETORNO'''
    p[0]=p[1]

#LISTO
def p_sentencialeer(p):
    'sentencialeer : LEER IZQPAREN DERPAREN'
    pass

#LISTO
def p_sentenciaescribir(p):
    'sentenciaescribir : IMPRIMIR IZQPAREN info  DERPAREN CIERRELINEA'
    print p[4]

def p_info(p):
    '''info : dato
        | dato  COMA dato'''
    pass

#Asignacion
def p_asignacion_1(p):
    '''asignacion : ASIGNAR NICK expresion'''
    #p[0]=[operador,nick,valor,tipo]
    p[0]=[p[1],p[2],p[3][0],p[3][1]]

def p_asignacion_2(p):
    '''asignacion : operadorasignacion  NICK expresion'''
    #p[0]=[operador,nick,valor,tipo]
    p[0]=[p[1],p[2],p[3][0],p[3][1]]

def p_operadorasignacion(p):
    '''operadorasignacion : SUMAIGUAL
        | MENOSIGUAL
        | MULTIGUAL
        | DIVIGUAL'''
    p[0]=p[1]

#--------------------------------------------------------------------------------

#Funciones
def p_funciones(p):
    '''funciones : declaracionfuncion
        | funciones declaracionfuncion  '''
    pass

#Declaracion de funciones
def p_declaracionfuncion(p):
    '''declaracionfuncion : VACIO MACRO NICK IZQPAREN DERPAREN IZQLLAVE bloque DERLLAVE
        | tipodato  MACRO NICK IZQPAREN DERPAREN IZQLLAVE bloque DERLLAVE
        | tipodato  MACRO NICK IZQPAREN declaracionparametros  DERPAREN IZQLLAVE bloque DERLLAVE'''
    pass

#  ---------------------------------------------------------------
#  ERROR
#  ---------------------------------------------------------------

def p_error(p):
    mensaje = "Usted tiene un error de sintaxis en alguna parte de su codigo. Este puede estar cerca de la linea %d. " % p.lineno+", y esta cerca de '" + str(p.value)+"'. Buena suerte encontrandolo."
    raise ErrorSintactico(mensaje)

#  ---------------------------------------------------------------
#  CONSTRUIR GRAMATICA
#  ---------------------------------------------------------------
import profile

yacc.yacc(method="LALR",debug=1)
#profile.run("yacc.yacc(method='LALR')")
try:
    #fle = sys.argv[1]
    f= open("ejemplo_1.txt","r")
    dato= f.read()
    yacc.parse(dato)
    f.close()
except EOFError:
    sys.exit()

Tabla.imprimir()
