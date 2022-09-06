'''A recursão nada mais é do que uma função que chame a si mesma.
E a parte mais importante dela é saber identificar o caso base,
 pois ele é o ponto de parada, que garante que a função não execute infinitamente.
 Ficou confuso? Vamos ver com um exemplo que fica mais fácil de entender.'''


def mdc(a, b): # definindo uma função para a recursividade
    if b == 0:
        return a
    return mdc(b, a%b) #retorno esperado da nossa função
   
a = int(input("\nDigite o primeiro número: ")) #usuário insere primeiro número para calculo do MDC
b = int(input("\nDigite o segundo número: ")) #usuário insere segundo número para calculo do MDC
print ("\nO MDC dos números informados é: {}".format(mdc(a,b))) # impressão MDC encontrado


