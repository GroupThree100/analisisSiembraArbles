import matplotlib.pyplot as plt

def graficarEstadisticas(dataFrame, campoX, campoY, nombreGrafica):
    colores = ['green', 'red', 'blue']
    data = dataFrame.groupby(campoX)[campoY].sum()

    plt.figure(figsize=(4, 4))

    #Generar gráfica
    plt.bar(data.index, data, color=colores)

    plt.title("Cantidad de Árboles por vereda")
    plt.xlabel("Vereda")
    plt.ylabel("Cantidad de Árboles")

    #plt.xticks(rotation=90)

    plt.subplots_adjust(left=0.2)

    plt.savefig(f'./assets/img/belmira/la_salazar/{nombreGrafica}.png')
    #plt.show()