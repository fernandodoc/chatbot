print()
print("Bem-vindo(a) à Pizzaria Delícia!")
print()

#  dados pessoais do cliente (nome e telefone)
name = input("Digite o seu nome: ")

while True:
    print(f'{name}, boa noite.')
    phone = input('Digite o telefone com ddd: ')
    
    if phone.isnumeric() is True:
        print()
        print(f'{name}, o número {phone} será usado para contato.')
        break
            
    else:
        print('Os dados digitados não são válidos. Digite o número do seu telefone com ddd sem espaço.')
        continue      

#  escolher o tamanho da pizza
print()
print('Escolha o tamanho da sua pizza:\n'
'1 - Pizza Brotinho\n2 - Pizza Média\n3 - Pizza Grande')

tamanho_da_pizza = input()

while True:

    if tamanho_da_pizza == '1':
        print('Você escolheu uma pizza brotinho')
        break

    elif tamanho_da_pizza == '2':
        print('Você escolheu uma pizza média')
        break

    elif tamanho_da_pizza == '3':
        print('Você escolheu uma pizza grande')
        break

    else:
        print('Escolha uma opção válida')
        break

#  escolher a massa da pizza
print()
print('Escolha a massa da sua pizza:\n'
'1 - Massa tradicional\n2 - Massa Pan\n3 - Massa Integral') 

massa_da_pizza = input()

while True:

    if massa_da_pizza == '1':
        print('Você escolheu a massa tradicional.')
        break

    elif massa_da_pizza == '2':
        print('Você escolheu a massa pan.')
        break
    
    elif massa_da_pizza == '3':
        print('Você escolheu a massa integral.')
        break

    else:
        print('Escolha uma opção válida.')

#  escolher o tipo da pizza
print()
print('Escolha o tipo da pizza:')
print()
print('1 - Pizza Tradicional\n'
      '(Margherita, Pepperoni, Calabresa, Quatro Queijos, Frango com Catupiry)')
print()
print('2 - Pizza Especial\n'
      '(Portuguesa, Calabresa Especial, Vegetariana, Carne Seca com Catupiry, Margherita Especial)')
print()
print('3 - Pizza Doce\n'
      '(Chocolate com Morango, Romeu e Julieta, Banana com Canela)')

tipo_da_pizza = input()

while True:

    if tipo_da_pizza == '1':
        print('Você escolheu uma pizza tradicional.')
        break
    
    elif tipo_da_pizza == '2':
        print('Você escolheu uma pizza especial')
        break

    elif tipo_da_pizza == '3':
        print('Você escolheu uma pizza doce.')
        break

    else:
        print('Escolha uma opção válida.')
        continue

#  escolher uma pizza inteira ou com dois sabores

print('A pizza será inteira ou com dois sabores?')
pizza = input('\n1 - Inteira\n2 - Meia-a-meia: ')

#  escolher uma pizza inteira e o sabor dela
while True:

    if pizza == '1':
        print('Você escolheu uma pizza inteira.')
        print('Escolha um sabor')

        print('1 - Margherita\n2 - Pepperoni\n3 - Calabresa\n4 - Quatro queijos\n5 - Frango com catupiry')

        sabor_escolhido1 = input('')

        if sabor_escolhido1 == '1':
            print('Você escolheu o sabor margherita')
            break
                        
        elif sabor_escolhido1 == '2':
            print('Você escolheu o sabor pepperoni')
            break
                                        
        elif sabor_escolhido1 == '3':
            print('Você escolheu o sabor calabresa')
            break
                        
        elif sabor_escolhido1 == '4':
            print('Você escolheu o sabor quatro queijos')
            break
                        
        elif sabor_escolhido1 == '5':
            print('Você escolheu o sabor frango com catupiry')
            break
                                
        else:
            print('Escolha uma opção válida.')
            break

#  escolher uma pizza dois sabores ! continuar desenvolvendo o código daqui

    if pizza == '2':
        print('Você escolheu dois sabores')
        print('Escolha o primeiro sabor')
        print('1 - Margherita\n2 - Pepperoni\n3 - Calabresa\n4 - Quatro queijos\n5 - Frango com catupiry')
        sabor_escolhido1 = input('')
        sabor_escolhido2 = input('')
        break

    elif sabor_escolhido2 == '1':
        print('Você escolheu metade Margherita.')
        print('Escolha a outra metade.')
        print('1 - Margherita\n2 - Pepperoni\n3 - Calabresa\n4 - Quatro queijos\n5 - Frango com catupiry')
        sabor_escolhido2 = input('')

sabor_tradicional1 = 'Margherita'
sabor_tradicional2 = 'Pepperoni'
sabor_tradicional3 = 'Calabresa'
sabor_tradicional4 = 'Quatro queijos'
sabor_tradicional5 = 'Frango com catupiry'



    











# pizzas_tradicionais = 'Margherita', 'Pepperoni', 'Calabresa', 'Quatro Queijos', 'Frango com Catupiry'

# pizzas_especiais = 'Portuguesa', 'Calabresa Especial', 'Vegetariana', 'Carne Seca com Catupiry', \
# 'Margherita Especial'

# pizzas_doces = 'Chocolate com Morango', 'Romeu e Julieta', 'Banana com Canela'

# opcoes_de_massa = 'Massa tradicional', 'Massa Pan', 'Massa Integral'

# tamanho_da_pizza = 'Pizza Brotinho', 'Pizza Média', 'Pizza Grande'

# bebidas = 'Refrigerantes', 'Água mineral', 'Sucos naturais', 'Cervejas', 'Vinhos'

# sobremesas = 'Brownie com sorvete', 'Petit Gateau', 'Torta de limão', 'Sorvetes'

# ingredientes_comuns = 'Molho de tomate, mussarela, tomate, azeitona preta'

# else:
#     print(f'{name}, você não digitou um número válido. Tente novamente.')

