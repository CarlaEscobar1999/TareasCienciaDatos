# -------------------------------------------------------------------------
# 40 - Trabajar con fronteras de USA con México en el año 2018,2019

# 0.- Generar un dataframe com "State","PortName","Measure","Value","Date"

# 4.- Obtener un histograma de "Bus Passengers" para todos los estados por 
#     los 2 años  
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

# Filtramos los registros que contienen "Personal Vehicles"
df_mask=dfFronteras['Measure']=="Bus Passengers"
dfBusPassengers = dfFronteras[df_mask]

# Sumarizamos por Estado 
dfPorEstado = dfBusPassengers.groupby(by=['State']).sum().groupby(level=[0]).cumsum()

# Imprimimos
#print (dfPorEstado.values)
#input ("Espera")

#Creamos los ejes x,y
datos = dfPorEstado.values

# Crea el Histrograma
plt.title('Bus Passenger para todos los Estados')
plt.hist(datos, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
plt.grid(True)
plt.show()
plt.clf()
