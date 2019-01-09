#-------------------------------------------------------------------------------
# Nombre:       Deus Ex Machine
# Autores:      Sergio Aleander Florez Galeano
#               Camilo Fernandez Bernal
# Descripcion:  Analizador Lexico de nuestro Compilador
#-------------------------------------------------------------------------------

class Tipo:
    def __init__(self,nombre,tipobase,padre,dimension,minimo,maximo):
        self.nombre = nombre
        self.tipobase = tipobase
        self.padre = padre
        self.dimension = dimension
        self.minimo = minimo
        self.maximo = maximo


    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setTipoBase(self,tipobase):
        self.tipobase = tipobase

    def getTipoBase(self):
        return self.tipobase

    def setDimension(self,dimension):
        self.dimension = dimension

    def getDimension(self):
        return self.dimension

    def setMinimo(self,minimo):
        self.minimo = minimo

    def getMinimo(self):
        return self.minimo

    def setMaximo(self,maximo):
        self.maximo = maximo

    def getMaximo(self):
        return self.maximo

    def setPadre(self,padre):
        self.padre = padre

    def getPadre(self):
        return self.padre

    def imprimir(self):
        print self.getNombre(),"=> [TB=",self.getTipoBase()," Pd=",self.getPadre()," Dim=",self.getDimension()," Min=",self.getMinimo()," Max=",self.getMaximo(),"]"


