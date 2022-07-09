""" Modulo Ciclos
    Funciones para practicas con ciclos
    Oscar Franco-Bedoya
    Abril-2022 """


# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#El Floid Veersion 10.000.0
 # el iniwalable ya tu sae







#Muevete!

def simulador_movimiento():
  #ingresar el valor
 velocidad = float(input('\nIngresa la velocidad en KM:'))
 opciones = str(input('indique si fue en minutos u horas:\nIngrese solamente H o M: '))
    #horas


  
 if opciones == 'h':
  horas = int(input('\nDurante cuanto tiempo: '))
  tiempo = horas * 60
  segundos = tiempo * 60
  desplazamiento = 1000/velocidad
  print('\nsu desplazamiento es:',desplazamiento,'\nEl tiempo ingresado es: ',horas,' Horas','\nSu tiempo en Minutos es:',tiempo,'\nSu tiempo en segundos es: ',segundos)



   
 elif opciones == 'm' or opciones == 'M':
  minutos = int(input('\nDurante cuantos minutos: '))
  segundos = minutos * 60
  horas = minutos / 60
  desplazamiento = 1000/velocidad
  
  print('\nsu desplazamiento es:',desplazamiento,'\nEl tiempo ingresado es: ',minutos,' Minutos','\nLos minutos Equivalen a: ',horas,'Horas','\nSus minutos equivalen a : ',segundos,'Segundos')
 else:
  print ('opcion no valida')






#Series y no las de Netflix

Serie = int(input('ingrese su numero entero: '))
desde = 1 
hasta = 15 

for f in range(desde, hasta + 1):
	print(f'{Serie} + {f}  =  {Serie * f}')


#Triangulares
n = int(input("¿Cuántas filas quieres?")) #filas que quiere el usuario  
x=1 #Fila actual que es el mismo número que el número de columnas que tiene que tener esa fila  
y=1 #Número que hay que imprimir  
z=1 #número de columnas que hay en la fila  

frase = ''  
for x in range(1,n+1):  
   for z in range(1,x+1): #z recorre de 1 hasta x. Ejemplo en la 4 (x=4 z=1,2,3,4)  
     frase+=(str(y)+(' '))  
     y+=1  
   print(frase)  
   frase =''  





  
  
    #TODO Comentar código
    #TODO Implementar la función


#def calculador_series(n):
#TODO Comentar código
#TODO Implementar la función
#  return "No implementada aún"

#def constructor_triangulos(pisos):
#TODO Comentar código
#TODO Implementar la función
#  return "No implementada aún"
#Muevete!
  
#def simulador_movimiento():
  #ingresar el valor
   # velocidad = float(input('\tHola Bienvenid@\n\nIngresa la velocidad en KM:'))
   # horas = int(input('\nDurante cuanto tiempo: '))
   # tiempo = horas * 60
   # segundos = tiempo * 60
   # desplazamiento = 1000/velocidad
   # print('\nsu desplazamiento es:',desplazamiento,'\nEl tiempo ingresado es: ',horas,' Horas','\nSu tiempo en Minutos es:',tiempo,'\nSu tiempo en segundos es: ',segundos)
  
    











#n = int(input("¿Cuántas filas quieres?")) #filas que quiere el usuario  
#x=1 #Fila actual que es el mismo número que el número de columnas que tiene que tener esa fila  
#y=1 #Número que hay que imprimir  
#z=1 #número de columnas que hay en la fila  
#frase = ''  
#for x in range(1,n+1):  
#   for z in range(1,x+1): #z recorre de 1 hasta x. Ejemplo en la 4 (x=4 z=1,2,3,4)  
#     frase+=(str(y)+(' '))  
#     y+=1  
#   print(frase)  
#   frase =''  



#for i in range (ElFloid-1,0-1):
# for j in range (1,i+1):
#  print (j,end = " ")
#  print (" ")








#Series y no las de Netflix

#serie = int (input ('\tHola Bienvenid@\nIngrese el numero entero positvo de su serie: '))
#resultado =  0
#for i in range (1,serie+1):
# resultado += (1/i)
# print ('el resultado de su serie es:',resultado)



#Muevete!

#def simulador_movimiento():
  #ingresar el valor
 #velocidad = float(input('\nIngresa la velocidad en KM:'))
 #opciones = str(input('indique si fue en minutos u horas:\nIngrese solamente H o M: '))
    #horas


  
 #if opciones == 'h':
 # horas = int(input('\nDurante cuanto tiempo: '))
 # tiempo = horas * 60
 # segundos = tiempo * 60
 # desplazamiento = 1000/velocidad
 # print('\nsu desplazamiento es:',desplazamiento,'\nEl tiempo ingresado es: ',horas,' Horas','\nSu tiempo en Minutos es:',tiempo,'\nSu tiempo en segundos es: ',segundos)



   
 #elif opciones == 'm' or opciones == 'M':
 # minutos = int(input('\nDurante cuantos minutos: '))
 # segundos = minutos * 60
 # horas = minutos / 60
 # desplazamiento = 1000/velocidad
  
 # print('\nsu desplazamiento es:',desplazamiento,'\nEl tiempo ingresado es: ',minutos,' Minutos','\nLos minutos Equivalen a: ',horas,'Horas','\nSus minutos equivalen a : ',segundos,'Segundos')
 #else:
  #print ('opcion no valida')












   


#def printPattern(n):
 
    # Printing upper part 
 #   for i in range(n+1):
 
  #      for j in range(1,i+1):
    
  #print(i,end="")
   #     print("")
 
    # printing lower part 
   # for i in range(n - 1,0,-1):
 
    #    for j in range(i,0,-1):
     #       print(i,end="")
     #   print("")
 
# driver code
#n = 8
#printPattern(n)












#def pyramid( n ):
 
    # outer loop to handle number
    # of rows n in this case
#    for i in range(n, 0, -1):
 
        # inner loop to create right triangle
        # gaps on left side of pyramid
 #       for gap in range(n-1, i-1, -1):
  #          print(" ", end = '')
   #         print(" ", end = '')
 
        # initializing value corresponding
        # to 'A' ASCII value
    #    num = ord('A')
 
        # loop to print characters on
        # left side of pyramid
   #     for j in range(1, i+1):
    #        print(chr(num), end = ' ')
     #       num += 1
 
        # loop to print characters on
        # right side of pyramid
      #  for j in range(i - 1, -1, -1):
       #     num -= 1
        #    print(chr(num), end = ' ')
 
#        print("\n", end = '')
 
#n = 9
#pyramid(n)




#Series y no las de Netflix

#Serie = int(input('ingrese su numero entero: '))
#desde = 1 
#hasta = 15 

#for f in range(desde, hasta + 1):
#	print(f'{Serie} + {f}  =  {Serie * f}')

  
    #TODO Comentar código
    #TODO Implementar la función


#def calculador_series(n):
#TODO Comentar código
#TODO Implementar la función
#  return "No implementada aún"

#def constructor_triangulos(pisos):
#TODO Comentar código
#TODO Implementar la función
#  return "No implementada aún"
#Muevete!
  
#def simulador_movimiento():
  #ingresar el valor
   # velocidad = float(input('\tHola Bienvenid@\n\nIngresa la velocidad en KM:'))
   # horas = int(input('\nDurante cuanto tiempo: '))
   # tiempo = horas * 60
   # segundos = tiempo * 60
   # desplazamiento = 1000/velocidad
   # print('\nsu desplazamiento es:',desplazamiento,'\nEl tiempo ingresado es: ',horas,' Horas','\nSu tiempo en Minutos es:',tiempo,'\nSu tiempo en segundos es: ',segundos)
  
    