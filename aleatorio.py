import random

num_bytes = random.randbytes(5)
print(num_bytes)

num_inteiro = random.randint(1, 60)
print(num_inteiro)

n = random.random()
print(n)

import secrets

numero = secrets.choice(range(0,100))
print(numero)

print(secrets.token_bytes(10))
print(secrets.token_hex(10))
print(secrets.token_urlsafe(10))
