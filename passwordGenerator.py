import string
import random   

print('Random Password Generator')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*(),.1234567890'

length = input('Input Your Password Length: ')
length = int(length)

print('\nhere is your password: ')
for pwd in range(length):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)