# -------------------------------------------------------------------------
# 40 - Trabajar con fronteras de USA con México en el año 2018,2019

# 3.- Graficar mediante barras verticales, una para cada estado, la cantidad
#     de "Personal Vehicles" y "Personal Vehicles Passengers", para cada 
#     puerta y acumulado de los 2 años
# -------------------------------------------------------------------------

# Importamos librería
import pandas as pd
import matplotlib.pyplot as plt

# Creamos el DataFrame con todos los datos
dfFronteras = pd.read_csv("fronteras.csv")

# Filtramos Frontera de usa con Mexico 
Border = dfFronteras["Border"] == "US-Mexico Border"
dfFronteras = dfFronteras[Border]

# Diccionario para el Estado y Puerta
dicEstadoPuerta = {}

# Ciclo para procesar los datos por Estado y Año
for i in dfFronteras.index: 
    # Verificamos que sea Personal Vehicles
    if (dfFronteras["Measure"][i]=="Personal Vehicles" or dfFronteras["Measure"][i]=="Personal Vehicles"):
        # Creamos la llave del diccionario
        llave  = dfFronteras["State"][i]
        fecha  = dfFronteras["Date"][i]
        puerta = dfFronteras["Border"][i]        
        valor =  dfFronteras["Value"][i]
        
        # Verifica si la fecha es del 2020
        if (fecha.find("2019")>=0 or fecha.find("2018")>=0):
            llave = llave + "-" +puerta      
        else:
            # Cualquier otro año es ignorado  
            llave =""
            
        # Verifica que sea llave correcta
        if (llave!=""):
            #Verifica si ya existe la llave en el diccionario
            if (dicEstadoPuerta.get(llave)==None):
                # lo agrega porque no existe
                dicEstadoPuerta[llave] = valor
            else:
                # Actualiza 
                valorActual = dicEstadoPuerta.get(llave)
                valorActual = valorActual + valor
                dicEstadoPuerta[llave] = valorActual    


# Para las Etiquetas
listaEtiquetas = []

# Ciclo para navegar en cada valor
for xDato in dicEstadoPuerta.keys():
    listaEtiquetas.append(xDato)

# Para los valores
listaValores = []

# Ciclo para navegar en cada valor
for xDato in dicEstadoPuerta.values():
    listaValores.append(xDato)
 

## Declaramos valores para el eje x
#eje_x = dicEstadoPuerta.keys() // Esto lo acepta pero para la vertical
eje_x = listaEtiquetas
 
# ## Declaramos valores para el eje y
#eje_y = dicEstadoPuerta.values()  // Lo acepta para vertical
eje_y = listaValores
 
## Creamos Gráfica
#plt.bar(eje_x, eje_y) Si la haces vertical se enciman los datos en las etiquteas
plt.barh(eje_x, eje_y)
 
## Legenda en el eje y
#plt.ylabel('Personal Vehicles') // Si la haces vertical
plt.xlabel('Personal Vehicles')
 
## Legenda en el eje x
#plt.xlabel('Estados Puertas') // Si la haces vertical
plt.ylabel('Estados Puertas')

 
## Título de Gráfica
plt.title('Graficas de Estado Puerta 2018-2019')
 
## Mostramos Gráfica
plt.show()


print("Programa Terminado")
