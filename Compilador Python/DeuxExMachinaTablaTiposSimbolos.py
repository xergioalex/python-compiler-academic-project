#-------------------------------------------------------------------------------
# Nombre:       Deus Ex Machine
# Autores:      Sergio Aleander Florez Galeano
#               Camilo Fernandez Bernal
# Descripcion:  Analizador Lexico de nuestro Compilador
#-------------------------------------------------------------------------------

import DeuxExMachinaTipos as tipo
import DeuxExMachinaSimbolos as simbolo

class Tabla:
    def __init__(self):
        self.tablatipos={}
        self.tablasimbolos={}
        #Tipo(nombre,tipobase,padre,dimension,minimo,maximo)
        self.tablatipos['entero'] = tipo.Tipo('entero',-1,-1,1,-1,-1)
        self.tablatipos['real'] = tipo.Tipo('real',-1,-1,1,-1,-1)
        self.tablatipos['caracter'] = tipo.Tipo('caracter',-1,-1,1,-1,-1)
        self.tablatipos['cadena'] = tipo.Tipo('cadena',-1,-1,1,-1,-1)
        self.tablatipos['booleano'] = tipo.Tipo('booleano',-1,-1,1,-1,-1)
        #Simbolo(nombre,categoria,tipo,numeroparametros,listaparametros,direccion)
        #self.tablasimbolos['entero'] = simbolo.Simbolo('hola','variable','entero',-1,[],5)
        #self.tablatipos['hola'] = tipo.Tipo('hola',-1,-1,1,-1,-1)


    def imprimir(self):
        print "********************* TABLA DE TIPOS *********************"
        for k,v in self.tablatipos.iteritems():
            v.imprimir()
        print "**********************************************************"
        print "******************* TABLA DE SIMBOLOS ********************"
        for k,v in self.tablasimbolos.iteritems():
            v.imprimir()
        print "**********************************************************"

    def getTablaTipos(self):
        return self.tablatipos

    def getTablaSimbolos(self):
        return self.tablasimbolos

    def countSimbolos(self):
        return self.tablaSimbolos.count()

    def countTipos(self):
        return self.tablaTipos.count()


    def addSimbolo(self, nombre,categoria,tipo,numeroparametros,listaparametros,direccion):
        self.tablasimbolos[nombre] = simbolo.Simbolo(nombre, categoria, tipo, numeroparametros, listaparametros, direccion)

    def addTipo(self,nombre,tipobase,padre,dimension,minimo,maximo):
        self.tablatipos[nombre] = tipo.Tipo(nombre,tipobase,padre,dimension,minimo,maximo)

    def existeTipo(self,nombre):
        return self.tablatipos.__contains__(nombre)

    #Asigna el atributo tipo en la tabla de simbolos y tipos
    def setTipoTablas(self,nombre,tipo):
        temp=self.tablatipos[nombre]
        temp.setTipoBase(tipo)
        temp=self.tablasimbolos[nombre]
        temp.setTipo(tipo)

##nuevatabla = Tabla()
##nuevatabla.setTipoTablas('entero','b')
##nuevatabla.imprimir()
##nuevatabla.imprimir()
##print(nuevatabla.existeTipo('sergio'))

##
##	boolean existeCampoRegistro(String id) {
##		//Como el tipo base de un registro es -1,
##		//eso nos va a indicar cuando hemos llegado al tipo base
##		boolean retorno = false;
##		int i = countTipos()-1;
##		while(i>=0) {
##			Tipo t = getTipo(i);
##			if(t.getTipoBase()<0) {
##				break;
##			} else {
##				if(t.getId().equals(id)) {
##					retorno = true;
##					break;
##				}
##			}
##			i--;
##		}
##		return retorno;
##	}
##
##	int posicionCampoRegistro(int t, String id) {
##		int pos = -1;
##		for(int i = t+1;i<countTipos();i++) {
##			if(getTipo(i).getPadre()>-1) {
##				if(getTipo(i).getId().equals(id)) {
##					pos = i-t-1;
##					break;
##				}
##			} else {
##				break;
##			}
##		}
##		return pos;
##	}
##
##	void addTipoCampo(String id) {
##		addTipo(id);
##		Tipo t = getTipo(id);
##		t.setDimension(1);
##		t.setTipoBase(0);
##		//Como el tipo base de un registro es -1,
##		//eso nos va a indicar cuando hemos llegado al tipo base
##		int i = countTipos()-1;
##		while(i>=0) {
##			Tipo j = getTipo(i);
##			if(j.getTipoBase()<0) {
##				j.setDimension(j.getDimension()+1);
##				t.setPadre(i);
##				break;
##			}
##			i--;
##		}
##	}
##
##	void addSimbolo(String id) {
##		tablaSimbolos.add(new Simbolo(countSimbolos(),id));
##	}
##
##	void addTipo(String id) {
##		tablaTipos.add(new Tipo(countTipos(),id));
##	}

##	void addTipo(Tipo t) {
##		tablaTipos.add(t);
##	}
##
##	void addTipo(String id, int e) {
##		Tipo t = new Tipo(countTipos(),id);
##		t.setTipoBase(0);
##		t.setDimension(e+1);
##		t.setMaximo(e);
##		tablaTipos.addElement(t);
##	}
##

##
##	Simbolo getSimbolo(int pos) {
##		return (Simbolo)tablaSimbolos.elementAt(pos);
##	}
##
##	Tipo getTipo(int pos) {
##		return (Tipo)tablaTipos.elementAt(pos);
##	}
##
##	Simbolo getSimbolo(String id) {
##		Simbolo simbolo = null;
##		//La busqueda comienza desde el final hacia el principio
##		//Esto se hace asi para cuando tengamos variables locales
##		//declaradas con el mismo nombre que las globales. Se
##		//buscara primero la local, es decir la ultima en la tabla
##		for(int i=countSimbolos()-1;i>=0;i--) {
##			simbolo = getSimbolo(i);
##			if(simbolo.getId().equals(id)) {
##				break;
##			} else {
##				simbolo = null;
##			}
##		}
##		return simbolo;
##	}
##
##	Tipo getTipo(String id) {
##		Tipo tipo = null;
##		for(int i=0;i<countTipos();i++) {
##			tipo = getTipo(i);
##			if(tipo.getId().equals(id)) {
##				break;
##			} else {
##				tipo = null;
##			}
##		}
##		return tipo;
##	}
##
##	boolean existeSimbolo(String id) {
##		if(getSimbolo(id)!=null) {
##			return true;
##		} else {
##			return false;
##		}
##	}
##
##	boolean existeSimboloAmbito(String id, int a) {
##		boolean retorno = false;
##		for(int i=countSimbolos()-1;i>=0;i--) {
##			Simbolo s = getSimbolo(i);
##			if(s.getId().equals(id) && s.getAmbito()==a) {
##				retorno = true;
##				break;
##			}
##		}
##		return retorno;
##	}
##
##
##	boolean existeTipo(String id) {
##		boolean retorno = false;
##		for(int i=countTipos()-1;i>=0;i--) {
##			Tipo t = getTipo(i);
##			if(t.getId().equals(id) && t.getPadre()<0) {
##				retorno = true;
##				break;
##			}
##		}
##		return retorno;
##	}
##
##	void setSimbolo(Simbolo s) {
##		int cod = s.getCod();
##		tablaSimbolos.setElementAt(s,cod);
##	}
##
##	void setDireccionSimbolo(String id,int d) {
##		Simbolo simbolo = getSimbolo(id);
##		simbolo.setDireccion(d);
##		setSimbolo(simbolo);
##	}
##
##	void setTipoSimbolo(String id,int t) {
##		Simbolo simbolo = getSimbolo(id);
##		simbolo.setTipo(t);
##		setSimbolo(simbolo);
##	}
##
##	void setCategoriaSimbolo(String id,String c) {
##		Simbolo simbolo = getSimbolo(id);
##		simbolo.setCategoria(c);
##		setSimbolo(simbolo);
##	}
##
##	void setCategoriaUltimoSimbolo(String c) {
##		Simbolo simbolo = getSimbolo(countSimbolos()-1);
##		simbolo.setCategoria(c);
##		setSimbolo(simbolo);
##	}
##
##	void setAmbitoSimbolo(String id, int a) {
##		for(int i=countSimbolos()-1;i>=0;i--) {
##			Simbolo s = getSimbolo(i);
##			if(s.getId().equals(id)) {
##				s.setAmbito(a);
##				setSimbolo(s);
##				break;
##			}
##		}
##	}
##
##	void eliminarAmbito(int a) {
##		int i = countSimbolos()-1;
##		while(i>0) {
##			Simbolo s = getSimbolo(i);
##			if(s.getAmbito()>=a) {
##				tablaSimbolos.removeElementAt(i);
##				i--;
##			} else {
##				break;
##			}
##		}
##	}
##
##	Simbolo getUltimoSubprograma() {
##		Simbolo s = null;
##		for(int i=countSimbolos()-1;i>=0;i--) {
##			s = getSimbolo(i);
##			if(s.getCategoria().equals("funcion") || s.getCategoria().equals("procedimiento")) {
##				break;
##			} else {
##				s = null;
##			}
##		}
##		return s;
##	}
##
##	void setParametroUltimoSubprograma(Tipo tp) {
##		Simbolo s = getUltimoSubprograma();
##		s.setNumeroParametros(s.getNumeroParametros()+1);
##		s.addParametro(tp.getCod());
##	}
##
##	int getTipoFuncion() {
##		int retorno = -1;
##		Simbolo s;
##		for(int i=countSimbolos()-1;i>=0;i--) {
##			s = getSimbolo(i);
##			if(s.getAmbito()==0) {
##				retorno = s.getTipo();
##				break;
##			}
##		}
##		return retorno;
##	}
##
##	String getIdFuncion() {
##		String retorno = "";
##		Simbolo s;
##		for(int i=countSimbolos()-1;i>=0;i--) {
##			s = getSimbolo(i);
##			if(s.getAmbito()==0) {
##				retorno = s.getId();
##				break;
##			}
##		}
##		return retorno;
##	}
##
##	int getDimensionParametros(String id) {
##		Simbolo s = getSimbolo(id);
##		int suma = 0;
##		for(int i=0;i<s.getNumeroParametros()-1;i++) {
##			suma = suma + getTipo(s.getParametro(i)).getDimension();
##		}
##		return suma;
##	}
##}

