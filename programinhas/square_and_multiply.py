import math

''' Lista 2 Questão 2.c) 
    Nesse script, vamos determinar que M = 2^{32} + 1 não é primo.
    Já vimos pela parte (a) e (b) que sendo M um número de Fermat (2^{2^n} + 1) com n >= 2, 
    qualquer fator primo de M é da forma k*2^{7} + 1. Vamos verificar se algum k baixo funciona.'''

''' Forma rapida de calcular a^exp (mod n)'''
def square_and_multiply(a,exp,mod):
    result = 1
    base = a
    while exp != 0:
        if exp%2 == 1:
            result*=base
        exp//=2
        base = (base*base)%mod
    return result

N = 5 # M = 2^{2^N} + 1
M = 2**(2**N) + 1

MAX_K = 1000 # k máximo que estamos dispostos a tentar
DIV = [] # divisores que achamos

'''
    Note que k*(2**(N+2)) + 1) é divisor  de 2{32} + 1 se, e só se, 2{32} = 1 mod  k*(2**(N+2)) + 1). Portanto podemos acha-los
    da seguinte forma.
'''
for k in range(1,MAX_K):
    if (square_and_multiply(2,2**N, k*(2**(N+2)) + 1) - 1) == 0:
        DIV += [k*(2**(N+2)) + 1]
        print(f"{M} = 2^(2^{N}) + 1 = {DIV[-1]} * {M // DIV[-1]} : {DIV[-1]} = {k}*(2^{N+2}) + 1")

