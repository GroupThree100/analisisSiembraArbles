import pandas as pd
import matplotlib.pyplot as plt

def calcularPromedioArbolesPorNombreComun(dataFrame, rangos, columnaInteres, columnaPromediar, nombreGrafica):
    plt.figure()

    bins = len(rangos) - 1
    dataFrame['Rango'] = pd.cut(dataFrame[columnaInteres], bins=bins, labels=rangos[:-1])

    arbolesPorRango = dataFrame.groupby('Rango')[columnaPromediar].sum()

    arboles = arbolesPorRango.values
    rangosNom = arbolesPorRango.index.astype(str)

    plt.pie(arboles, labels=rangosNom, autopct='%1.1f%%')

    plt.title('Arboles por zonas comunes')
    plt.savefig(f'./assets/img/Bello/{nombreGrafica}.png') 
