import pandas as pd
from helpers.santa_Fe_De_Antioquia.crearTablas import crearTabla
from helpers.caucasia.crearBarras import graficarEstadisticas as graficarEstadisticasCaucasia
from helpers.belmira.la_salazar.crearBarras import graficarEstadisticas as graficarEstadisticasLaSalazar
from helpers.belmira.rio_arriba.crearBarras import graficarEstadisticas as graficarEstadisticasRioArriba

siembras=pd.read_csv("./data/Siembras.csv")

cantidadArboles=siembras.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia" ')
datosGeneralesCaucasia=siembras.query('Ciudad == "Caucasia" ')
datosGeneralesBelmiraLaSalazar=siembras.query('Ciudad == "Belmira" and Vereda == "La Salazar"')
datosGeneralesBelmiraRioArriba=siembras.query('Ciudad == "Belmira" and Vereda == "Rio Arriba"')

crearTabla(cantidadArboles, "cantidad_Arboles")
graficarEstadisticasCaucasia(datosGeneralesCaucasia, 'Vereda', 'Arboles', 'grafica_arboles_caucasia')
graficarEstadisticasLaSalazar(datosGeneralesBelmiraLaSalazar, 'Vereda', 'Arboles', 'grafica_vereda_la_salazar')
graficarEstadisticasRioArriba(datosGeneralesBelmiraRioArriba, 'Vereda', 'Arboles', 'grafica_vereda_rio_arriba')