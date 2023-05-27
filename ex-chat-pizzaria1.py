print("Bem-vindo(a) à Pizzaria Delícia!")

#  dados pessoais do cliente (nome e telefone)
name = input("Digite o seu nome:\n")
phone = input(f"Boa noite, {name}! Digite o número do seu telefone:\n")

#  confirmação dos dados
print(f'{name}, o telefone {phone} está correto?')
confirmacao = input('"sim" ou "não"\n')

#  escolher o tamanho da pizza
if confirmacao.lower() == "sim":
    print('Ok. Escolha o tamanho da sua pizza:')
    print("1 - brotinho\n2 - média\n3 - grande")
    pizza_tamanho = input('Digite o número referente ao tamanho da sua pizza:\n')

    if pizza_tamanho == "1":
        print("Você escolheu o tamanho brotinho")
    elif pizza_tamanho == "2":
        print("Você escolheu o tamanho médio")
    elif pizza_tamanho == "3":
        print("Você escolheu o tamanho grande")
    else:
        print('Escolha uma opção válida.')
else:
    print('Por favor, verifique as informações inseridas. Reinicie o processo se necessário.')

#  escolher o sabor da pizza
print("Escolha o sabor da sua pizza:\n 1 - mussarela\n 2 - calabreza\n 3 - frango")
sabores = input('Digite o sabor que você escolheu: ')

if sabores == "1":
    print("Você escolheu o sabor mussarela")
elif sabores == "2":
    print("Você escolheu o sabor calabreza")
elif sabores == "3":
    print("Você escolheu o sabor frango")
else:
    print('Escolha uma opção válida.')

#  informar o endereço da entrega
endereco_entrega = input(f"{name}, digite o endereço para entrega: ")

#  escolher a forma de pagamento
forma_pgto = input('A forma de pagamento será'
                   '\n1 - dinheiro\n2 - débito\n3 - crédito\n')


if forma_pgto == "1":
    print("Você escolheu o pagamento em dinheiro")
elif forma_pgto == "2":
    print("Você escolheu o pagamento em débito")
elif forma_pgto == "3":
    print("Você escolheu o pagamento em crédito")
else:
    print('Escolha uma opção válida.')

#  confirmação do pedido e do tempo de entrega.
print("O seu pedido está confirmado. A sua pizza será entregue em até 30 minutos. Agradecemos a preferência.")



