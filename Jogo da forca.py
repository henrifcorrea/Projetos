secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu...')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso nao vale! Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'uhuuul, a letra {letra} existe na palavra segreta.')

    else:
        print(f'affffs, a letra {letra} NAO existe na palavra secreta.')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta

        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Que legal, VOCE GANHOU!!! A palavra secreta era {secreto_temp}')
        break
    else:
        print(f'A palavra secreta é: {secreto_temp}')

    if letra not in secreto:
        chances -= 1
    print(f'Voce ainda tem {chances} chances.')
    print()