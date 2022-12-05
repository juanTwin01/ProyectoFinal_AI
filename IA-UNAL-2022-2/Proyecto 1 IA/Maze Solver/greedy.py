def h(p1,p2):
  x1=p1[0]
  y1=p1[1]
  x2=p2[0]
  y2=p2[1]
  return abs(x1-x2)+abs(y1-y2)

def greedy(matriz,punto_inicial,objetivo,dimension):
  
  ## Mis elementos recorridos
  recorrido=[]
  
  #Empiezo por mi punto inicial
  
  x=punto_inicial[0]
  y=punto_inicial[1]
  recorrido.append(punto_inicial)
  
  mejor_opcion=(punto_inicial,h(punto_inicial,objetivo))
  
  #Mientras que no encuentre mi objetivo estare iterando
  while(mejor_opcion[0] != objetivo):  
     #Tomo mi elemento inicial
     #Miro las mejores opciones de mis vecindades siempre y cuando no sea un muro y tampoco sea un elemento recorrido y tomo la mejor opcion
    if(x+1<dimension):
      
      if(matriz[x+1][y] == "C" and matriz[x+1][y]  not in recorrido):
        if(mejor_opcion[1] > h((x+1,y),objetivo)):
          mejor_opcion=((x+1,y),h((x+1,y),objetivo))

    if(y+1<dimension):
      
      if(matriz[x][y+1] == "C" and matriz[x][y+1]  not in recorrido):
        if(mejor_opcion[1] > h((x,y+1),objetivo)):
          mejor_opcion=((x,y+1),h((x,y+1),objetivo))

    if(y-1>=0):
      
      if(matriz[x][y-1] == "C" and matriz[x][y-1]  not in recorrido):
        if(mejor_opcion[1] > h((x,y-1),objetivo)):
          mejor_opcion=((x,y-1),h((x,y-1),objetivo) )   

    if(x-1>=0):
      
      if(matriz[x-1][y] == "C" and matriz[x-1][y]  not in recorrido):
        if(mejor_opcion[1] > h((x,y-1),objetivo)):
          mejor_opcion=((x,y-1),h((x,y-1),objetivo))          
    x=mejor_opcion[0][0]
    y=mejor_opcion[0][1]
    recorrido.append(mejor_opcion[0])

  return(recorrido)