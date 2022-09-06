while True:
    print()
    num_1 = input('digite um numero: ')
    num_2 = input('digite outro numero: ')
    operador = input('digite um operador: ')
    sair = input('deseja sair? [s]sim ou [n]nao: ')

    if sair == 's':
        print('Obrigado por usar nossa calculadora! ')
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('voce precisa digitar um numero.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)

    else:
        print('operador invalido')