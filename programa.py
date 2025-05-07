from funcoes import *

inteiros = ['1', '2', '3', '4', '5']
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house':-1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
dados = []
guardados = []
imprime_cartela(cartela)
dados = rolar_dados(5 - len(guardados))
print(f'Dados Rolados: {dados}')
print(f'Dados guardados: {guardados}')
contador = 0
conta_dados = 0
viaveis = ['0', '1', '2', '3', '4']
while contador < 12:
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    acao = input('>')
    if acao in viaveis:
        if acao == '0':
            valid_combinacao = False
            while not valid_combinacao:
                print('Digite a combinação desejada:')
                categoria = input(">")
                opcoes = ['cinco_iguais', 'full_house', 'quadra', 'sem_combinacao', 'sequencia_alta', 'sequencia_baixa', '1', '2', '3', '4', '5', '6']
                if categoria not in opcoes:
                    print('Combinação inválida. Tente novamente.')
                elif compara_cartela(dados + guardados, categoria, cartela) == False:
                    print('"Essa combinação já foi utilizada."')
                else:
                    cartela = faz_jogada(dados + guardados, categoria, cartela)
                    contador += 1
                    conta_dados = 0
                    dados = rolar_dados(5)  # Resetar dados
                    guardados = []  # Limpar guardados
                    print(f'Dados Rolados: {dados}')
                    print(f'Dados guardados: {guardados}')
                    valid_combinacao = True
        elif acao == '1':
            if not dados:
                print("Não há dados para guardar.")
            else:
                print(f'Digite o índice do dado a ser guardado (0 a {len(dados)-1}):')
                guardar = input('>')
                if guardar not in viavel(len(dados)):
                    print("Opção inválida. Tente novamente.")
                    continue
                guardar = int(guardar)
                f1 = guardar_dado(dados, guardados, guardar)
                dados = f1[0]
                guardados = f1[1]
                print(f'Dados Rolados: {dados}')
                print(f'Dados guardados: {guardados}')
        elif acao == '2':
            if not guardados:
                print("Não há dados guardados para remover.")
            else:
                print(f'Digite o índice do dado a ser removido (0 a {len(guardados)-1}):')
                remover = input('>')
                if remover not in viavel(len(guardados)):
                    print("Opção inválida. Tente novamente.")
                    continue
                remover = int(remover)
                f2 = remover_dado(dados, guardados, remover)
                dados = f2[0]
                guardados = f2[1]
                print(f'Dados Rolados: {dados}')
                print(f'Dados guardados: {guardados}')
        elif acao == '3' and conta_dados < 2:
            if not dados:
                print("Não há dados para rerrolar. Todos os dados estão guardados.")
            else:
                dados = rolar_dados(5 - len(guardados))
                conta_dados += 1
                print(f'Dados Rolados: {dados}')
                print(f'Dados guardados: {guardados}')
        elif acao == '3' and conta_dados >= 2:
            print("Você já usou todas as rerrolagens.")
        elif acao == '4':
            imprime_cartela(cartela)
    else:
        print('Opção inválida. Tente novamente.')
print(cartela)
soma = 0
pontuacao_simples = 0
for ponto in cartela['regra_simples'].values():
    if ponto >= 0:
        pontuacao_simples += ponto
for ponto in cartela['regra_avancada'].values():
    if ponto >= 0:
        soma += ponto
soma += pontuacao_simples
if pontuacao_simples >= 63:
    soma += 35
print(f"Pontuação total: {soma}")