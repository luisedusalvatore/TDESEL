from funcoes import *
inteiros = ['1','2','3','4','5']
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
contador = 0
conta_dados = 1
viaveis = ['0','1','2','3','4']
while contador < 12:
    lista_cartela = []
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    acao = input('>')
    if acao in viaveis:
        if acao == '0':
            print('Digite a combinação desejada:')
            categoria = input(">")
            opcoes = ['cinco_iguais', 'full_house', 'quadra', 'sem_combinacao', 'sequencia_alta', 'sequencia_baixa','1','2','3','4','5','6']
            if categoria not in opcoes:
                print('Combinação inválida. Tente novamente.')
            else:
                if compara_cartela(dados,categoria,cartela) == False:
                    print('"Essa combinação já foi utilizada."')
                elif compara_cartela(dados,categoria,cartela) == True:    
                    cartela = faz_jogada(dados,categoria,cartela)
                    contador +=1
                    conta_dados=1
        elif acao == '1':
            print(f'Digite o índice do dado a ser guardado (0 a {len(dados)-1}):')
            guardar =input('>')
            while guardar not in viavel(dados):
                print("Opção inválida. Tente novamente.")
                guardar = input('>')
            guardar = int(guardar)
            f1 = guardar_dado(dados, guardados, guardar)
            dados = f1[0]
            guardados = f1[1]
            print(f'Dados Rolados: {dados}')
            print(f'Dados guardados: {guardados}')
        if acao == '2':
            print(f'Digite o índice do dado a ser removido (0 a {len(dados)-1}):')
            remover = (input('>'))
            while remover not in viavel(guardar):
                print("Opção inválida. Tente novamente.")
                remover = (input('>'))
            f2 = remover_dado(dados,guardados,remover)
            dados = f2[0]
            guardados = f2[1]
            print(f'Dados Rolados: {dados}')
            print(f'Dados guardados: {guardados}')
        if acao == '3'and conta_dados < 3:
            dados = rolar_dados(5 - len(guardados))
            conta_dados += 1
            print(f'Dados Rolados: {dados}')
            print(f'Dados guardados: {guardados}')
        elif acao == '3' and conta_dados >= 3:
            print("Você já usou todas as rerrolagens.")
        if acao == '4':
            imprime_cartela(cartela)
        for regra in cartela.values():
            for ponto in regra.values():
                lista_cartela.append(ponto)
    else:
        print('Opção inválida. Tente novamente.')
print(cartela)
soma = 0
for valor in lista_cartela:
    soma += valor
print(f"Pontuação total: {soma}")