def getStr(message):
  while(True):
    temp = input(message)
    try:
      temp = int(temp)
      print("That is not the proper value.")
    except:
      break
  return temp
  
def box(loop):
  # starts at 0
  
  length = len(name)
  for i in range(loop, length, 1):
    print(name[i], end = ' ')
  
  
  if loop > 0:
    for j in range(0, loop, 1):
      print(name[j], end = ' ')
  loop += 1
  if loop == length:
    print("")
    print("This name is a mess.")
  else:
    print("")
    box(loop)
name = getStr("What name would you like to turn into a mess? ")
box(0)