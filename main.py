import numpy as np
import random

kardano = np.zeros((8,8))
a = [0, 0, 0, 0, 0, 0, 0, 0]
print("Нажмите на ENTER, чтобы продолжить")
input()
count = 0
while count != 16:
    k = random.randint(0, 63)
    i = int(k//8)
    j = k % 8
    if kardano[i, j] == 0:
        kardano[i, j] = 1
        kardano[j, 7 - i] = 2
        kardano[7 - i, 7 - j] = 2
        kardano[7 - j, i] = 2
        count += 1
#print(kardano)
for i in range(0, 8):
    for j in range(0, 8):
        if kardano[i, j] == 2:
            kardano[i, j] = 0
print(kardano)
print("Введите сообщение для шифрования(до 64 символов)")
message = input()
message_x = ''
z = len(message)
ind = 0
r = 0
for i in range(0, 64):
    if i < len(message):
        message_x += message[i]
        ind += 1
    elif r == 0:
        message_x += '\n'
        r = 1
        #ind += 1
    else:
        message_x += ' '

print(message_x)

kardano1 = np.zeros((8, 8))
kardano2 = np.zeros((8, 8))
kardano3 = np.zeros((8, 8))
kardano4 = np.zeros((8, 8))
for i in range(0, 8):
    for j in range(0, 8):
        kardano1[i, j] = kardano[7 - j, i]
        kardano2[i, j] = kardano[7 - i, 7 - j]
        kardano3[i, j] = kardano[j, 7 - i]


encrypted = np.array([['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']])
for i in range(0, 8):
    for j in range(0, 8):
        encrypted[i, j] = chr(random.randint(40, 90))
index = 0
for i in range(0, 8):
    for j in range(0, 8):
        if kardano[i, j] == 1 and ind >= 0:
            encrypted[i, j] = message_x[index]
            ind -=1
            index += 1
for i in range(0, 8):
    for j in range(0, 8):
        if kardano1[i, j] == 1 and ind >= 0:
            encrypted[i, j] = message_x[index]
            ind -=1
            index += 1
for i in range(0, 8):
    for j in range(0, 8):
        if kardano2[i, j] == 1 and ind >= 0:
            encrypted[i, j] = message_x[index]
            ind -=1
            index += 1
for i in range(0, 8):
    for j in range(0, 8):
        if kardano3[i, j] == 1 and ind >= 0:
            encrypted[i, j] = message_x[index]
            ind -=1
            index += 1
print(encrypted)


decrypted = ''
for i in range(0, 8):
    for j in range(0, 8):
        if kardano[i, j] == 1:
            decrypted += encrypted[i, j]
for i in range(0, 8):
    for j in range(0, 8):
        if kardano1[i, j] == 1:
            decrypted += encrypted[i, j]
for i in range(0, 8):
    for j in range(0, 8):
        if kardano2[i, j] == 1:
            decrypted += encrypted[i, j]
for i in range(0, 8):
    for j in range(0, 8):
        if kardano3[i, j] == 1:
            decrypted += encrypted[i, j]
print("Изначальное сообщение:\t" + message_x.partition('\n')[0])
print("Полученное сообщение:\t" + decrypted.partition('\n')[0])