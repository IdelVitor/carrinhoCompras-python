compras = []

def pergunta():
    while True:
        resposta = input('Você gostaria de (i)inserir, (a)apagar, (l)listar ou (s)sair? ').strip().upper()
        if len(resposta) != 1 or resposta not in ['I', 'A', 'L', 'S']:
            print('Dado inválido, digite novamente.')
        else:
            return resposta

def acao(resposta):
    if resposta == 'I':
        while True:
            item = input('Me fale que item quer inserir: ')
            compras.append(item)
            mais = input('Você quer inserir mais itens? (s/n): ').strip().lower()
            if mais != 's':
                break  
    elif resposta == 'A':
        item = input('Me fale que item quer apagar: ')
        if item in compras:
            compras.remove(item)
        else:
            print('Item não encontrado.')
    elif resposta == 'L':
        if compras:
            print('Lista de compras:')
            for i, item in enumerate(compras, 1):
                print(f'{i}. {item}')
        else:
            print('A lista está vazia.')
    elif resposta == 'S':
        print('Saindo do programa...')
        return False  
    return True  

while True:
    resposta = pergunta()
    if not acao(resposta):
        break 