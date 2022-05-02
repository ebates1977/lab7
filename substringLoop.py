def substr(word, index, length):
  if index > 0 and length >= 0:
    for i in range (length):
      print(word[i], end ="")

  else:
    return (" ")

def get_word():
  try: 
    word = input("enter a word: ")
    return word
  except ValueError:
    print("please enter a word.")
    get_word()
    
def get_index():
  try: 
    index = int(input("please enter an index: "))
    return index
  except ValueError:
    print("Please enter an int.")
    get_index()

def get_length():
  try: 
    length = int(input("Please enter a length: "))
    if length >= 0:
      return length
    else:
      print("no, enter a number bigger then 0.")
      get_length()
  except ValueError:
    print("Please enter an int.")
    get_length()

word = get_word()
index = get_index()
length = get_length()


substr(word, index, length)