import pandas as pd
from helpers.Santa_Fe_De_Antioquia.crearTablas import crearTabla as graficarTablaStaFe
from helpers.Santa_Fe_De_Antioquia.crearBarras import graficarEstadisticas as graficarBarrasStaFe
from helpers.Belmira.la_salazar.crearTablas import crearTabla as graficarTablaLaSalazar
from helpers.Belmira.rio_arriba.crearTablas import crearTabla as graficarTablaRioArriba
from helpers.Belmira.la_salazar.crearBarras import graficarEstadisticas as graficarBarrasLaSalazar
from helpers.Belmira.rio_arriba.crearBarras import graficarEstadisticas as graficarBarrasRioArriba
from helpers.Caucasia.crearTablas import crearTabla as graficarTablaCaucasia
from helpers.Caucasia.crearBarras import graficarEstadisticas as graficarBarrasCaucasia
from helpers.Bello.crearTablaHtml import crearTablaBelloQuitasol
from helpers.Bello.crearBarras import graficarVeredasQuitasol
from helpers.Bello.crearTorta import calcularPromedioArbolesPorNombreComun
from helpers.Caramanta.crearTablaHtml import crearTablaCaramanta
from helpers.Caramanta.crearBarras import graficarSiembraCaramanta
from helpers.Yarumal.crearBarras import graficarVeredaMarinillo
from helpers.Yarumal.crearTablaHtml import crearTablaVeredaMarinillo


siembras=pd.read_csv("./data/Siembras.csv")

cantidadArboles=siembras.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia" ')
datosGeneralesBelmiraLaSalazar=siembras.query('Ciudad == "Belmira" and Vereda == "La Salazar"')
datosGeneralesBelmiraRioArriba=siembras.query('Ciudad == "Belmira" and Vereda == "Rio Arriba"')
datosGeneralesCaucasia=siembras.query('Ciudad == "Caucasia" ')

# ----------------- Santa_Fe_De_Antioquia
graficarTablaStaFe(cantidadArboles, 'Tabla_Santa_Fe_De_Antioquia')
graficarBarrasStaFe(cantidadArboles, 'Hectareas', 'Arboles', 'Barras_Santa_Fe_De_Antioquia')

# ----------------- Belmira
graficarTablaLaSalazar(datosGeneralesBelmiraLaSalazar, 'Tabla_La_Salazar')
graficarTablaRioArriba(datosGeneralesBelmiraRioArriba, 'Tabla_Rio_Arriba')
graficarBarrasLaSalazar(datosGeneralesBelmiraLaSalazar, 'Hectareas', 'Arboles', 'Barras_La_Salazar')
graficarBarrasRioArriba(datosGeneralesBelmiraRioArriba, 'Hectareas', 'Arboles', 'Barras_Rio_Arriba')

# ----------------- Caucasia
graficarTablaCaucasia(datosGeneralesCaucasia, 'Tabla_Caucasia')
graficarBarrasCaucasia(datosGeneralesCaucasia, 'Hectareas', 'Arboles', 'Barras_Caucasia')



tablaBDsiembras = pd.read_csv('./data/Siembras.csv')

# ----------------- Caramanta
siembraCaramanta = tablaBDsiembras.query('Arboles > 100 and Ciudad == "Caramanta" ')

crearTablaCaramanta(siembraCaramanta, "siembraCaramanta")
graficarSiembraCaramanta(siembraCaramanta, ['Cabecera Municipal', 'El Balso', 'La Unión', 'Olibales', 'Olibales'], 'Arboles', 'graficarSiembraCaramanta')


# ----------------- Yarumal
veredaMallarino = tablaBDsiembras.query('Vereda == "Mallarino" and Ciudad == "Yarumal" ')

graficarVeredaMarinillo(veredaMallarino, 'Hectareas', 'Arboles', 'graficarVeredaMarinillo')
crearTablaVeredaMarinillo(veredaMallarino, "veredaMallarino")

print(veredaMallarino[['Nombre comun']])

# ----------------- Bello
BelloveredasQuitasol = tablaBDsiembras[['Nombre comun','Ciudad','Vereda','Arboles','Hectareas']].query('Vereda == "Quitasol" and Ciudad == "Bello" ')
graficarVeredasQuitasol(BelloveredasQuitasol, 'Hectareas', 'Arboles', 'MediabelloVeredasQuitasol')

crearTablaBelloQuitasol(BelloveredasQuitasol, "belloVeredasQuitasol")
calcularPromedioArbolesPorNombreComun(BelloveredasQuitasol,['Almendra', 'misperos', 'casco de vaca', 'ceiba', 'pino' 'vela'], 'Hectareas', 'Arboles','Distribución_Árboles_Hectáreas')









