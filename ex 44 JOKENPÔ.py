#JOKENPÔ feito por Roberto Pedro

import random
from time import sleep
print('JOKENPÔ Roberto Pedro')
escolha = int(input('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Make your choice:'''))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)
joken = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(joken)

print('-='*20)
if escolha == 1 and computador == 'TESOURA':
    print('''JOGADOR VENCEU !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('PEDRA',computador))
elif escolha == 1 and computador == 'PAPEL':
    print('''COMPUTADOR VENCEU !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('PEDRA',computador))
elif escolha == 1 and computador == 'PEDRA':
    print('''EMPATE !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('PEDRA',computador))

elif escolha == 2 and computador == 'PEDRA':
    print('''JOGADOR VENCEU !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('PAPEL',computador))
elif escolha == 2 and computador == 'PAPEL':
    print('''EMPATE !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('PAPEL',computador))
elif escolha == 2 and computador == 'TESOURA':
    print('''COMPUTADOR VENCEU !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('PAPEL',computador))

elif escolha == 3 and computador == 'PEDRA':
    print('''COMPUTADOR VENCEU !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('TESOURA',computador))
elif escolha == 3 and computador == 'PAPEL':
    print('''JOGADOR VENCEU !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('TESOURA',computador))
elif escolha == 3 and computador == 'TESOURA':
    print('''EMPATE !!! 
JOGADOR escolheu {}
COMPUTADOR escolheu {}'''.format('TESOURA',computador))

print('-='*20)