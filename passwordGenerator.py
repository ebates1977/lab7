import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*(),.<>[]{}\|")

def generate_random_password():
  length = int(input("Enter password length: "))
  if length < 8:
    print("Please enter a number bigger then 8.")
    generate_random_password()
    
  random.shuffle(characters)
  password = []
  
  for i in range(length):
    password.append(random.choice(characters))
    
  random.shuffle(password)
  print("".join(password))

generate_random_password()