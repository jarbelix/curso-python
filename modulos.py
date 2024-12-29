import math
print(math.sqrt(81))

from math import sqrt, sin
print(sqrt(81))

import math as m
print(m.sqrt(99))

# É perigoso pois outros módulos importado podem conflitar
from math import *
print(sqrt(45))


import mod_func as mf
if __name__ == "__main__":
    mf.mensagem()

    num = int(input("Digite um número inteiro positivo: "))

    print(f'\nCalcular fatorial do número:')
    fat = mf.fatorial(num)
    print(f'O fatorial é {fat}')

    print(f'\nCalcular sequencia de fibonacci:')
    fib = mf.fibo(num)
    print(f'O fatorial é {fib}')