import matplotlib.pyplot as plt

def graficarEstadisticas(dataFrame, campoX, campoY, nombreGrafica):
    colores = ['g', 'r', 'b', 'y', 'c', 'm', 'k']
    data = dataFrame.groupby(campoX)[campoY].sum()

    plt.figure(figsize=(4, 4))

    #Generar gráfica
    plt.bar(data.index, data, color=colores)

    plt.title("Belmira - La Salazar")
    plt.xlabel("Vereda")
    plt.ylabel("Cantidad de Árboles")

    #plt.xticks(rotation=90)

    plt.subplots_adjust(left=0.2)

    plt.savefig(f'./assets/img/Belmira/la_salazar/{nombreGrafica}.png')
    #plt.show()