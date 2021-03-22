# -------------------------------------------------------------------------
#  Trabajar con fronteras de USA con México en el año 2018,2019

# 0.- Generar un dataframe com "State","PortName","Measure","Value","Date"

# 2.- Elaborar una gráfica de puntos, que muestre el comportamiento de
#     "Pedestrians". Que sea una gráfica por cada estado-año y con detalle de
#     puertas en la horizontal
# -------------------------------------------------------------------------

# Importamos librería
import pandas as pd
import matplotlib.pyplot as plt

# Creamos el DataFrame con todos los datos
dfFronteras = pd.read_csv("fronteras.csv")

# Filtramos Frontera de usa con Mexico 
Border = dfFronteras["Border"] == "US-Mexico Border"
dfFronteras = dfFronteras[Border]

# 0.- Eliminamos las columnas excedentes
del(dfFronteras['Port Code'])
del(dfFronteras['Border'])

# Filtramos los registros que contienen "Pedestrians"
df_mask=dfFronteras['Measure']=="Pedestrians"
dfPedestrians = dfFronteras[df_mask]
#print(dfPedestrians.index)

# Diccionario Vario para los datos
dicEstadoAño = {}

# Ciclo para procesar los datos por Estado y Año
for i in dfPedestrians.index: 

      # Creamos la llave del diccionario
      llave = dfPedestrians["State"][i]
      fecha = dfPedestrians["Date"][i]
      valor = dfPedestrians["Value"][i]
      
      # Verifica si la fecha es del 2020
      if (fecha.find("2019")>=0):
         llave = llave+"-2019"
      elif (fecha.find("2018")>=0):
         llave = llave+"-2018"      
      else:
         # Cualquier otro año es ignorado  
         llave =""
         
      # Verifica que sea llave correcta
      if (llave!=""):
         #Verifica si ya existe la llave en el diccionario
         if (dicEstadoAño.get(llave)==None):
            # lo agrega porque no existe
            dicEstadoAño[llave] = valor
         else:
            # Actualiza 
            valorActual = dicEstadoAño.get(llave)
            valorActual = valorActual + valor
            dicEstadoAño[llave] = valorActual  

# Coloca los datos para graficar
x = dicEstadoAño.values()
y = dicEstadoAño.keys()
plt.scatter(x,y)
plt.show()

print("Programa Terminado")
