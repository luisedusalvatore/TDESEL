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

def remover_dado(rolados, estoque, remover):
    lista = []
    rolados.append(estoque[remover])
    del estoque[remover]
    lista.append(rolados)
    lista.append(estoque)
    return lista

def calcula_pontos_regra_simples(lista):
    dicio = {1:0,2:0,3:0,4:0,5:0,6:0}
    for numero in lista:
        dicio[numero]+=numero
    return dicio
def calcula_pontos_soma(lista):
    soma = 0
    for pontos in lista:
        soma += pontos
    return soma