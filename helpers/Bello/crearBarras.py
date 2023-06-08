import matplotlib.pyplot as plt

def graficarVeredasQuitasol(dataFrame, campoX, campoY, nombreGrafica):
    colores=['green', 'red', 'blue', 'purple'] 
    arboles = dataFrame.groupby(campoX)[campoY].mean() 

    plt.bar(arboles.index, arboles, color=colores)
    plt.title("Media de Arboles y Hectareas")
    plt.xlabel("Hectareas")
    plt.ylabel("Arboles")

    plt.savefig(f'./assets/img/Bello/{nombreGrafica}.png') 