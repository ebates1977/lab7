lower = "abcdefghijklmnopqrstuvwxyz"
sentence = input("please enter a sentence: ")
shift =  int(input("please enter your shift: "))

def encrypt(shift):
  global sentence
  encrypted = ""
  for letter in sentence.lower():

    if letter in lower:
      
      pos = lower.find(letter)
      encrypted = encrypted + lower[(pos+shift) % len(lower)]

    else:
      encrypted = encrypted + letter

  sentence = encrypted
  print(encrypted)

  running()

def decrypt(shift):
  global sentence
  decrypted = ""
  
  for letter in sentence.lower():

    if letter in lower:
      
      pos = lower.find(letter)
      decrypted = decrypted + lower[(pos-shift) % len(lower)]

    else:
      decrypted = decrypted + letter
      
  sentence = decrypted
  print(decrypted)
  running()

def running():
  ask = int(input("would you like to \n1. Encrypt \n2. Decrypt\n3. Quit?\n"))
  
  if ask == 1:
    encrypt(shift)

  elif ask == 2:
    decrypt(shift)

  elif ask == 3:
    print("okay, have a good day!")
    exit()
    
  else:
    print("enter 1, 2, or 3.")
    running()


running()