# Author@ Lucas V.
# Mede o tempo e a quantidade de tentativas necessárias
# para se acertar um numero de dezenas em determinado
# sorteio!

from random import randrange
from datetime import datetime


def sorteio(num_dezenas, dezenas_ate):
    lista = []
    i = 1
    while i <= num_dezenas:
        k = 1
        j = randrange(1, dezenas_ate + 1)
        while k:
            if j in lista:
                j = randrange(1, dezenas_ate + 1)
            else:
                k = 0
        lista.append(j)
        i += 1
    return sorted(lista)


def tentativas(sorteios, num_dezenas, dezenas_ate):
    ini = datetime.now()
    numeros = sorteio(num_dezenas, dezenas_ate)
    dezenas = sorteio(num_dezenas, dezenas_ate)
    i = 0
    while numeros != dezenas and i <= sorteios:
        i += 1
        dezenas = sorteio(num_dezenas, dezenas_ate)
        print('----- Tentativa {}: -----'.format(i))
        print('Desejada: {}  -  {} :Sorteada'.format(numeros, dezenas))
    fim = datetime.now()
    if i <= sorteios:
        print('\nParabens você acertou após {} tentativas !!!'.format(i))
    else:
        print('\nQue pena mesmo após {} tentativas Você não conseguiu :('.format(i))
    print('Tempo de execução: ', end='')
    print(fim - ini)


print(sorteio(3, 60))