import numbers
import random   

print('Random Password Generator')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*(),.1234567890'
number = input('Amount of Passwords to Generate: ')
number = int(number)

length = input('Input Your Password Length: ')
length = int(length)

print('\nhere are your passwords: ')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
print(passwords)