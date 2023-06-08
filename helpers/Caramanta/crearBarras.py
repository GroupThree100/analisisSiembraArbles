import matplotlib.pyplot as plt

def graficarSiembraCaramanta(dataFrame, campoX, campoY, nombreGrafica):
    colores=['green', 'orange', 'magenta', 'cyan']
    siembra = dataFrame.groupby(campoX)[campoY].mean() 
    plt.bar(siembra.index, siembra, color=colores)

    plt.title("Siembra de arboles en CaramantaL")
    plt.xlabel("Veredas")
    plt.ylabel("Siembra")

    plt.savefig(f'./assets/img/Caramanta/{nombreGrafica}.png') 