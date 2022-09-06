salario = int(input('Digite seu salario fixo: '))
qtd_vendas = int(input('\nQuantos carros voce vendeu? '))
contador = 0
lista = []

while contador != qtd_vendas:
    montadora = input('\nQual a montadora dos carros vendidos:\n 1- Peugeot\n 2- VW\n 3- Fiat\n 4- Renault\n 5- Citroen\n 6- Toyota\n 7- Hyundai\n 8- GM\n 9- Honda\n 10- Nissan\nDigite a montadora de acordo com o numero: ')
    montadora = montadora.isdigit()

    if montadora == 1:
        modelo = input('\nQual modelo do carro? a- 206, b- 207, c- 208\nDigite o modelo de acordo com o opçao: ')
        if modelo == 'a':
            modelo1 = 12500 * (20/100)
            lista.append(modelo1)

        elif modelo == 'b':
            modelo2 = 15000 * (20/100)
            lista.append(modelo2)

        elif modelo == 'c':
            modelo3 = 18500 * (20/100)
            lista.append(modelo3)

        else:
            print('\nDigite uma opçao valida!')
            continue


    elif montadora == 2:
        modelo = input('\nQual modelo do carro? a- Jetta, b- Passat, c- Golf\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo4 = 50250 * (5/100)
            lista.append(modelo4)

        elif modelo == 'b':
            modelo5 = 45200 * (5/100)
            lista.append(modelo5)

        elif modelo == 'c':
            modelo6 = 59650 * (5/100)
            lista.append(modelo6)

        else:
            print('\nDigite uma opçao valida!')
            continue


    elif montadora == 3:
        modelo = input('\nQual modelo do carro? a- Uno , b- 500 , c- Punto \nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo7 = 12300 * (2/100)
            lista.append(modelo7)

        elif modelo == 'b':
            modelo8 = 67850 * (2/100)
            lista.append(modelo8)

        elif modelo == 'c':
            modelo9 = 23500 * (2/100)
            lista.append(modelo9)

        else:
            print('\nDigite uma opçao valida!')
            continue


    elif montadora == 4:
        modelo = input('\nQual modelo do carro? a- Clio, b- Sandero, b- Logan \nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo10 = 17450 * (10/100)
            lista.append(modelo10)

        elif modelo == 'b':
            modelo11 = 32655 * (10/100)
            lista.append(modelo11)

        elif modelo == 'c':
            modelo12 = 33200 * (10/100)
            lista.append(modelo12)

        else:
            print('\nDigite uma opçao valida!')
            continue


    elif montadora == 5:
        modelo = input('\nQual modelo do carro? a- c3, b- c4, c- Xsara\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo13 = 53600 * (15/100)
            lista.append(modelo13)

        elif modelo == 'b':
            modelo14 = 59800 * (15/100)
            lista.append(modelo14)

        elif modelo == 'c':
            modelo15 = 22400 * (15/100)
            lista.append(modelo15)

        else:
            print('\nDigite uma opçao valida!')
            continue


    elif montadora == 6:
        modelo = input('\nQual modelo do carro? a- Corolla, b- Yaris, c- Etios\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo16 = 69500 * (4/100)
            lista.append(modelo16)

        elif modelo == 'b':
            modelo17 = 89700 * (4/100)
            lista.append(modelo17)

        elif modelo == 'c':
            modelo18 = 85000 * (4/100)
            lista.append(modelo18)

        else:
            print('\nDigite uma opçao valida!')
            continue

    elif montadora == 7:
        modelo = input('\nQual modelo do carro? a- hb20, b- i30, c- Azera\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo19 = 36500 * (3/100)
            lista.append(modelo19)

        elif modelo == 'b':
            modelo20 = 64120 * (3/100)
            lista.append(modelo20)

        elif modelo == 'c':
            modelo21 = 80400 * (3/100)
            lista.append(modelo21)

        else:
            print('\nDigite uma opçao valida!')
            continue

    elif montadora == 8:
        modelo = input('\nQual modelo do carro? a- Agile, b- Cobalt, c- Sonic\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo22 = 23200 * (1/100)
            lista.append(modelo22)

        elif modelo == 'b':
            modelo23 = 25600 * (1/100)
            lista.append(modelo23)

        elif modelo == 'c':
            modelo24 = 23690 * (1/100)
            lista.append(modelo24)

        else:
            print('\nDigite uma opçao valida!')
            continue

    elif montadora == 9:
        modelo = input('\nQual modelo do carro? a- Cr-v, b- Fit, c- City\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo25 = 98500 * (4/100)
            lista.append(modelo25)

        elif modelo == 'b':
            modelo26 = 77850 * (4/100)
            lista.append(modelo26)

        elif modelo == 'c':
            modelo27 = 72650 * (4/100)
            lista.append(modelo27)

        else:
            print('\nDigite uma opçao valida!')
            continue

    elif montadora == 10:
        modelo = input('\nQual modelo do carro? a- Sentra, b- Versa, c- Kicks\nDigite o modelo de acordo com a opçao: ')
        if modelo == 'a':
            modelo28 = 63980 * (4/100)
            lista.append(modelo28)

        elif modelo == 'b':
            modelo29 = 74500 * (4/100)
            lista.append(modelo29)

        elif modelo == 'c':
            modelo30 = 87400 * (4/100)
            lista.append(modelo30)

        else:
            print('\nDigite uma opçao valida!')
            continue

    else:
        print('\nDigite um numero valido!')
        continue

    contador += 1

soma = 0
for elem in lista:
    soma = soma + elem

print(f'Seu salario no mês foi de {soma + salario:.2f} R$.')


