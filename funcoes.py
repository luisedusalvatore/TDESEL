import random
def rolar_dados(n):
    lista = []
    for i in range(n):
        dado = random.randint(1,6)
        lista.append(dado)
    return lista

def guardar_dado(rolados, estoque, guardar):
    lista = []
    estoque.append(rolados[guardar])
    del rolados[guardar]
    lista.append(rolados)
    lista.append(estoque)
    return lista

