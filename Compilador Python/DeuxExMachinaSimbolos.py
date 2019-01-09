#-------------------------------------------------------------------------------
# Nombre:       Deus Ex Machine
# Autores:      Sergio Aleander Florez Galeano
#               Camilo Fernandez Bernal
# Descripcion:  Analizador Lexico de nuestro Compilador
#-------------------------------------------------------------------------------


class Simbolo:
    def __init__(self, nombre,categoria,tipo,numeroparametros,listaparametros,direccion):
        self.nombre = nombre
        self.categoria = categoria
        self.tipo = tipo
        self.numeroparametros = numeroparametros
        self.listaparametros = listaparametros
        self.direccion = direccion


    def imprimir(self):
    	print self.getNombre(),"=> [Valor=",self.getDireccion()," Ctg=",self.getCategoria()," tipo=",self.getTipo()," nPar=",self.getNumeroParametros()," list=",self.listaparametros,"]"

    def setNombre(self,nombre):
    	self.nombre = nombre

    def getNombre(self):
    	return self.nombre

    def setDireccion(self,direccion):
    	self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setTipo(self,tipo):
    	self.tipo = tipo

    def getTipo(self):
    	return self.tipo

    def setCategoria(self,categoria):
    	self.categoria = categoria;

    def getCategoria(self):
    	return self.categoria;

    def setNumeroParametros(self,numeroparametros):
    	self.numeroparametros = numeroparametros

    def getNumeroParametros(self):
    	return self.numeroparametros

    def addParametro(self,parametro):
    	self.listaparametros.append(parametro)

    def getParametro(self,posicion):
    	return listaparametros[posicion]


##nuevosimbolo = Simbolo(1,"integer")
##nuevosimbolo.imprimir()


