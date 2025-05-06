from funcoes import *
cartela = {
    'regra_simples':  {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0
    },
    'regra_avancada' : {
        'sem_combinacao':0,
        'quadra': 0,
        'full_house':0,
        'sequencia_baixa': 0,
        'sequencia_alta': 0,
        'cinco_iguais': 0
    }
}
dados = []
guardados = []
imprime_cartela(cartela)
dados = rolar_dados(5 - len(guardados))
print(f'Dados Rolados: {dados}')
print(f'Dados guardados: {guardados}')
lista_cartela = []
for regra in cartela.values():
    for ponto in regra.values():
        lista_cartela.append(ponto)
print(lista_cartela)
while 0 in lista_cartela:
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    acao = int(input('>'))
    if acao == 1:
        print(f'Digite o índice do dado a ser guardado (0 a {len(dados)-1}):')
        guardar = int(input('>'))
        f1 = guardar_dado(dados, guardados, guardar)
        dados = f1[0]
        guardados = f1[1]
        print(f'Dados Rolados: {dados}')
        print(f'Dados guardados: {guardados}')
    if acao == 2:
        print(f'Digite o índice do dado a ser removido (0 a {len(dados)-1}):')
        remover = int(input('>'))
        f2 = remover_dado(dados,guardados,remover)
        dados = f2[0]
        guardados = f2[1]
        print(f'Dados Rolados: {dados}')
        print(f'Dados guardados: {guardados}')
