# -------------------------------------------------------------------------
# - Trabajar con fronteras de USA con México en el año 2018,2019

# 0.- Generar un dataframe com "State","PortName","Measure","Value","Date"
# 1.- Generar una gráfica de Linea para cada estado, sin detalle de puertas
#     que muestre como ha crecido o decrecido el paso peatonal de "Personal
#     Vehicles" a lo largo del Tiempo
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
df_mask=dfFronteras['Measure']=="Personal Vehicles"
dfPersonlVehicles = dfFronteras[df_mask]

# Sumarizamos por Estado 
dfPorEstado = dfPersonlVehicles.groupby(by=['State']).sum().groupby(level=[0]).cumsum()

#Creamos los ejes x,y
x = dfPorEstado.index
y = dfPorEstado.values
plt.plot(x,y)
plt.show()


