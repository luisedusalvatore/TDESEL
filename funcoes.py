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
def calcula_pontos_sequencia_baixa(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        if lista[i] not in lista2:
            lista2.append(lista[i])
    combinacoes = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
    for combinacao in combinacoes:
            check = True
            for num in combinacao:
                if num not in lista2:
                    check = False
                    break
            if check == True:
                return 15
    return 0
def calcula_pontos_sequencia_alta(lista):
    lista.sort()
    lista2 = []
    for i in range(len(lista)):
        if lista[i] not in lista2:
            lista2.append(lista[i])
    combinacoes = [[1,2,3,4,5],[2,3,4,5,6]]
    for combinacao in combinacoes:
            check = True
            for num in combinacao:
                if num not in lista2:
                    check = False
                    break
            if check == True:
                return 30
    return 0
def calcula_pontos_full_house(lista):
    dicio = {}
    for i in range(len(lista)):
        if lista[i] not in dicio:
            dicio[lista[i]] = 1
        else:
            dicio[lista[i]]+=1
    if len(dicio) != 2:
        return 0
    lista2 = []
    for valor in dicio.values():
        lista2.append(valor)
    if sorted(lista2) != [2,3]:
        return 0
    else:
        resposta = 0
        for dado in lista:
            resposta += dado
        return resposta
def calcula_pontos_quadra(lista):
    dicio = {}
    for i in range(len(lista)):
        if lista[i] not in dicio:
            dicio[lista[i]] = 1
        else:
            dicio[lista[i]]+=1
    resposta = 0
    check = False
    for qtd in dicio.values():
        if qtd > 3:
            check = True
    if check == True:
        resposta = 0
        for dado, qtd in dicio.items():
            resposta += qtd*dado
    return resposta
def calcula_pontos_quina(lista):
    dicio = {}
    for i in range(len(lista)):
        if lista[i] not in dicio:
            dicio[lista[i]] = 1
        else:
            dicio[lista[i]]+=1
    check = False
    for qtd in dicio.values():
        if qtd > 4:
            check = True
    if check == True:
        return 50
    else:
        return 0