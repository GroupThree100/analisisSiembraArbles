import matplotlib.pyplot as plt


def graficarVeredaMarinillo(dataFrame, campoX, campoY, nombreGrafica):
    colores=['magenta', 'cyan', 'red', 'yellow'] 
    veredaMarinillo = dataFrame.groupby(campoX)[campoY].mean() 

    plt.bar(veredaMarinillo.index, veredaMarinillo, color=colores)

    plt.title("Vereda Marinillo") 
    plt.xlabel("Hectareas de Zonas Comunes")
    plt.ylabel("Siembra")

    plt.savefig(f'./assets/img/Yarumal/{nombreGrafica}.png') 