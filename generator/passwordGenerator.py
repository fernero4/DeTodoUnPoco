##hacer interfaz

import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits="0123456789"
symbols="()[]{},;:.-/\\?+*# "

upper, lower, nums, syms= True,True, True, True
# upper=bool(input("letras mayusculas \nTrue False"))
# lower=bool(input("letras minusculas \nTrue False"))
# nums=bool(input("numeros? \nTrue False"))
# syms=bool(input("simbolos \nTrue False"))


password=""

all=""

if upper:
    all+=uppercase_letters
if lower:
    all+=lowercase_letters
if nums:
    all+=digits
if syms:
    all+=symbols

#l=int(input("length"))
#amo=int(input("amount"))

length=10
amount=1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
