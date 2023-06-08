
import pandas as pd
from helpers.Bello.crearTablaHtml import crearTablaBelloQuitasol
from helpers.Bello.crearBarras import graficarVeredasQuitasol
from helpers.Bello.crearTorta import calcularPromedioArbolesPorNombreComun
from helpers.Caramanta.crearTablaHtml import crearTablaCaramanta
from helpers.Caramanta.crearBarras import graficarSiembraCaramanta
from helpers.Yarumal.crearBarras import graficarVeredaMarinillo
from helpers.Yarumal.crearTablaHtml import crearTablaVeredaMarinillo


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









