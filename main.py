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
for i in range(0, 64):
    if i < len(message):
        message_x += message[i]
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
for i in range(0, 8):
    for j in range(0, 8):
        kardano4[i, j] = kardano[i, j] + kardano1[i, j] + kardano2[i, j] + kardano3[i, j]
print(kardano4)

encrypted = np.array([['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '']])
ind = 0
for i in range(0, 8):
    for j in range(0, 8):
        if kardano[i, j] == 1:
            encrypted[i, j] = message_x[ind]
            ind +=1
for i in range(0, 8):
    for j in range(0, 8):
        if kardano1[i, j] == 1:
            encrypted[i, j] = message_x[ind]
            ind +=1
for i in range(0, 8):
    for j in range(0, 8):
        if kardano2[i, j] == 1:
            encrypted[i, j] = message_x[ind]
            ind +=1
for i in range(0, 8):
    for j in range(0, 8):
        if kardano3[i, j] == 1:
            encrypted[i, j] = message_x[ind]
            ind +=1
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
print(message_x)
print(decrypted)