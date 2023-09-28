# import library

import string
import random

# print massage and length fix that password

print("Welcome to password Generator")
len = int(input("Enter the length of password: "))

# generating random characters

low = string.ascii_lowercase
upr = string.ascii_uppercase
dig = string.digits
smbl = string.punctuation

# combining the pasword

pasword = low+upr+dig+smbl

#generate the random according to length

gen = random.sample(pasword,len)
pasword = "".join(gen)

#print the pasword

print(pasword)
