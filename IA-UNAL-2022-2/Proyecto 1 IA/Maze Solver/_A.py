

class Nodo():

  def __init__(self):
    self.dato=None
    self.padre=None
    self.valor=None


def h(p1,p2):
  x1=p1[0]
  y1=p1[1]
  x2=p2[0]
  y2=p2[1]
  return abs(x1-x2)+abs(y1-y2)
  
def f(n,objetivo):
  
  return g(n)+h(n,objetivo)
  

def g(n):
  return 1



def A_estrella(matriz,punto_inicial,objetivo,dimension):
  
  open_set=[]
  closed_set=[]
  x=punto_inicial[0]
  y=punto_inicial[1]
  matriz[x][y]=Nodo()
  
  matriz[x][y].dato=punto_inicial
  matriz[x][y].padre=None
  matriz[x][y].valor=f(matriz[x][y].dato,objetivo)

  
  open_set.append(matriz[x][y])
  

  ganador=matriz[x][y]
  #Mientras que no encuentre mi objetivo
  while ganador!=objetivo:
    
    m = min([nodo.valor for nodo in open_set])
    ganador=open_set[[nodo.valor for nodo in open_set].index(m)]

    if(ganador.dato==objetivo):break    
    open_set.remove(ganador)
      
    x=ganador.dato[0]
    y=ganador.dato[1]

    if(x+1<dimension):
      
      if(matriz[x+1][y] == "C" and matriz[x+1][y]  not in closed_set  ):
        matriz[x+1][y]=Nodo()
        matriz[x+1][y].dato=(x+1,y)   
        matriz[x+1][y].padre=matriz[x][y]
       
        matriz[x+1][y].valor=f(matriz[x+1][y].dato,objetivo)
        open_set.append(matriz[x+1][y])
      
       
    
    if(y+1<dimension):
      
      if(matriz[x][y+1] == "C" and matriz[x][y+1]  not in closed_set  ):
        matriz[x][y+1]=Nodo()
        matriz[x][y+1].dato=(x,y+1)
        matriz[x][y+1].padre=matriz[x][y]
        matriz[x][y+1].valor=f(matriz[x][y+1].dato,objetivo)
        open_set.append(matriz[x][y+1])
          

    
    if(x-1>=0):
      
      if(matriz[x-1][y] == "C" and matriz[x-1][y]  not in closed_set ):
        matriz[x-1][y]=Nodo()
        
        matriz[x-1][y].dato=(x-1,y)
     
        matriz[x-1][y].padre=matriz[x][y]
        matriz[x-1][y].valor=f(matriz[x-1][y].dato,objetivo)    
        open_set.append(matriz[x-1][y])

        
    
    if(y-1>=0):
     
      
      if(matriz[x][y-1] == "C" and matriz[x][y-1]  not in closed_set ):
        matriz[x][y-1]=Nodo()
        matriz[x][y-1].dato=(x,y-1)
        matriz[x][y-1].padre=matriz[x][y]
        matriz[x][y-1].valor=f(matriz[x][y-1].dato,objetivo)      
        open_set.append(matriz[x][y-1])
              
  casilla=ganador
  recorrido=[]
  while (casilla!= None):
    recorrido.append(casilla.dato)
    
    casilla=casilla.padre      

  return list(reversed(recorrido))
      
    
    
    
    
  

    
  
  
