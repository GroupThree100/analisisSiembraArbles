import matplotlib.pyplot as plt

def graficarEstadisticas(dataFrame, campoX, campoY, nombreGrafica):
    colores = ['g', 'r', 'b', 'y', 'c', 'm', 'k']
    data = dataFrame.groupby(campoX)[campoY].sum()

    plt.figure(figsize=(4, 4))

    #Generar gráfica
    plt.bar(data.index, data, color=colores)

    plt.title("Caucasia", pad=20)
    plt.xlabel("Vereda")
    plt.ylabel("Cantidad de Árboles", labelpad=10)

    plt.xticks(rotation=90)

    plt.subplots_adjust(left=0.3, bottom=0.3)

    plt.savefig(f'./assets/img/Caucasia/{nombreGrafica}.png')
    plt.show()