# Criação do Menu
def exibe_menu():
    print('-' * 41)
    print('[1] Adicionar pizza no cardapio')
    print('[2] Consultar pizza')
    print('[3] Alterar pizza do cardapio')
    print('[4] Excluir pizza do cardapio')
    print('[5] Exibir cardápio completo')
    print('[6] Exportar cardápio para arquivo texto')
    print('[7] SAIR')
    print('-' * 41)
    while True:
        try:
            opcao = int(input('Escolha uma Opção:'))
            if opcao >= 0 and opcao <= 7:
                return opcao
            else:
                print("Opção inválido, favor digitar entre 0 e 7")
        except ValueError:
            print("Opção inválido, favor digitar entre 0 e 7")

# [1] Adicionar pizza no cardapio


def cardapio_cadastrar():
    # captando os dados gravando os dados no item que é dicionário em seguida no cardapio que é lista
    item = {}
    while True:
        try:
            item['id'] = int(input('Informe o código da Pizza.......:'))
            break
        except:
            print('Informe um numero inteiro!!')
    item['nome'] = input('Informe o nome da pizza.........:')
    ingred = []
    ingred = input("Informe os ingredientes da Pizza:")
    item['ingredientes'] = ingred
    item['preco'] = float(input('Informe o Preço da Pizza........:'))
    cardapio.append(item)
    cardapio_exibir()

# [2] Consultar pizza


def cardapio_consulta():
    busca = int(input('Informe o código da Pizza:'))
    for x in range(0, int(len(cardapio))):
        if busca == cardapio[x]['id']:
            print(
                f'Pizza consta no cardapio segue informações e seu indice é {x}')
            print(cardapio[x])
            return
    print('Pizza não consta no cardápio!!!')


# [3] Alterar pizza do cardapio
def cardapio_alterar():
    busca = int(input('Informe o código da Pizza que deseja Alterar:'))
    for x in range(0, int(len(cardapio))):
        if busca == cardapio[x]['id']:
            print(cardapio[x])
            print(f'Pizza localizada providencie as alterações abaixo')
            while True:
                try:
                    cardapio[x]['id'] = int(
                        input('Informe o código da Pizza.......:'))
                    break
                except:
                    print('Informe um numero inteiro!!')
            cardapio[x]['nome'] = input('Informe o nome da pizza.........:')
            cardapio[x]['ingredientes'] = input(
                "Informe os ingredientes da Pizza:")
            cardapio[x]['preco'] = float(
                input('Informe o Preço da Pizza........:'))
            print('Pizza alterada com sucesso!!!')
            print(cardapio[x])
            return
    print('Pizza não consta no cardápio!!!')
    return

# [4] Excluir pizza do cardapio


def cardapio_remover():
    busca = int(input('Informe o código da Pizza:'))
    for x in range(0, int(len(cardapio))):
        if busca == cardapio[x]['id']:
            print(cardapio[x])
            while True:
                SN = input(
                    'Tem certeza que deseja excluir a Pizza (S/N)?').upper()[0]
                if SN in "SN":
                    break
                else:
                    print('Erro! Por favor Digite apenas S ou N')
            if SN == 'S':
                cardapio.pop((x))
                cardapio_exibir()
                print(f"Ok Pizza {busca} removida!!!")
            return
    print('Pizza não consta no cardápio!!!')


# [5] Exibir cardápio completo
def cardapio_exibir():
    for x in range(0, int(len(cardapio))):
        print(cardapio[x])

# [6] Exportar cardápio para arquivo texto


def cardapio_salvar():
    # visualisando em tela para conferencia
    cardapio_exibir()

    # Exportação
    print('Exportando para o arquivo: Exporta_Cardapio.txt')
    arquivo = open('Exporta_Cardapio.txt', 'w')
    for ttt in range(0, int(len(cardapio))):
        item = cardapio[ttt]
        linha = str(item["id"]) + ";" + str(item["nome"]) + ";" + \
            str(item["ingredientes"]) + ";" + str(item["preco"])
        arquivo.write(f"{linha}\n")
    arquivo.close()
    return


if __name__ == "__main__":
    # Importando o método para limpar a tela
    import os
    os.system('cls') or None

    cardapio = []
    ## item =  {'id': 0, 'nome': 'Calabresa', 'ingredientes': ['queijo','tomate', 'manjericão'], 'preco': 20.50 }

    # populando o cardapio somente para testes
    item = {'id': 10, 'nome': 'Calabresa', 'ingredientes': [
        'queijo', 'tomate', 'oregano', 'calabresa'], 'preco': 40.00}
    cardapio.append(item)
    item = {'id': 20, 'nome': 'Portuguesa', 'ingredientes': [
        'queijo', 'presunto', 'tomate', 'manjericão', 'ovos'], 'preco': 50.00}
    cardapio.append(item)
    item = {'id': 30, 'nome': 'Marguerita', 'ingredientes': [
        'queijo', 'tomate', 'manjericão', 'queijo prato'], 'preco': 60.00}
    cardapio.append(item)
    # ate aqui

    while True:
        op = exibe_menu()
        if op == 1:
            cardapio_cadastrar()
        elif op == 2:
            cardapio_consulta()
        elif op == 3:
            cardapio_alterar()
        elif op == 4:
            cardapio_remover()
        elif op == 5:
            cardapio_exibir()
        elif op == 6:
            cardapio_salvar()
        elif op == 7:
            print('Encerrando!!!')
            break
