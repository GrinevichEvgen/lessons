'''Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A),
а на втором название масти (Hearts, Diamonds, Clubs, Spades).'''



import random

nominal =['6','7','8','9','10','J','D','K','A']
masti =['Hearts', 'Diamonds', 'Clubs', 'Spades']
print (random.choice(nominal) ,  random.choice(masti))

