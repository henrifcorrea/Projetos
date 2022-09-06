def dec(numero_decimal):  # Definindo uma função para nossa recursividade decimal para binário
    if numero_decimal == 0:  # se 0 retornar 0
        return 0
    else:
        return (numero_decimal % 2 + 10 *
                dec(int(numero_decimal // 2)))  # caso seja maior que 1 cálculo de conversão binária


# Inserindo o número para conversão e realizando a impressão
numero_decimal = int(input(
    "\nDigite o número decimal que deseja converter para binário: "))  # usuário insere o número que deseja converter em binário
print("\nO número convertido em binário é: {}".format(
    dec(numero_decimal)))  # impressão do número decimal convertido em binário