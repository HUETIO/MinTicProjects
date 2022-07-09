import pandas as pd
from collections import namedtuple

def tabla_goleadores(tabla):
  
  lista_goleadores = []
  lista_goles = []
  goleador = namedtuple("goleador", "PAIS NOMBRE PARTIDOS GOLES")
  
  tabla_resultado = tabla.parse("RESULTADOS")
  tabla_goleador = tabla.parse("GOLEADORES")
  
  goleadores = pd.DataFrame(tabla_goleador)
  goles = pd.DataFrame(tabla_resultado)
  
  goleadores_pais = goleadores.iloc[:, 0]
  goleadores_nombre = goleadores.iloc[:, 1]
  goles_equipo1 = goles.iloc[:, 1]
  goles_equipo2 = goles.iloc[:, 3]
  pais_equipo1 = goles.iloc[:, 0]
  pais_equipo2 = goles.iloc[:, 2]

  for i in range(len(goleadores_pais)):
    gol = 0
    pais = goleadores_pais[i]
    if pais == pais_equipo1[i]:
      gol += goles_equipo1[i]
    elif pais == pais_equipo2[i]:
      gol += goles_equipo2[i]
    lista_goles.append(int(gol))
  
  for i in range(len(goleadores_nombre)):
    
    jugador = goleador(goleadores_pais[i], goleadores_nombre[i], 3, lista_goles[i])
    lista_goleadores.append(jugador)
  
  print("\nTABLA DE GOLEADORES\n")
  jugadores = pd.DataFrame(lista_goleadores)
  print(jugadores)











def tabla_posiciones(tabla):
  lista_ganadores = []
  lista_perdedores = []
  lista_empatados = []
  
  tabla2 = tabla.parse("RESULTADOS")
  
  mostrar = pd.DataFrame(tabla2)
  goles1_grupoA = mostrar.iloc[:5, 1]
  goles2_grupoA = mostrar.iloc[:5, 3]
  pais1_grupoA = mostrar.iloc[:5, 0]
  pais2_grupoA = mostrar.iloc[:5, 2]
  #print(mostrar)
  
  
  for i in range(len(goles1_grupoA)):
    if goles1_grupoA[i] > goles2_grupoA[i]:
      #print(pais1_grupoA[i])
      lista_ganadores.append(pais1_grupoA[i])
      lista_perdedores.append(pais2_grupoA[i])
    elif goles1_grupoA[i] == goles2_grupoA[i]:
      lista_empatados.append(pais1_grupoA[i])
      lista_empatados.append(pais2_grupoA[i])
    else:
      #print(pais2_grupoA[i])
      lista_ganadores.append(pais2_grupoA[i])
      lista_perdedores.append(pais1_grupoA[i])
  
  print("\nLista ganadores:\n")
  print(lista_ganadores)
  
  diccionario_ganadores = {}
  diccionario_perdedores = {}
  diccionario_empatados = {}
  
  # iterating over the list
  for item in lista_ganadores:
  # checking the element in dictionary
    if item in diccionario_ganadores:
    # incrementing the counr
      diccionario_ganadores[item] += 1
    else:
    # initializing the count
      diccionario_ganadores[item] = 1
  
  print("\nGANADORES\n")
  print(diccionario_ganadores)
  
  
  df = pd.DataFrame([[key, diccionario_ganadores[key]] for key in diccionario_ganadores.keys()], columns=['PAIS', 'PG'])
  print("\nTABLA DE PUNTUACIÓN GRUPO A\n")
  print(df)