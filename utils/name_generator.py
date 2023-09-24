from random import randrange

def generate_name():
  size = randrange(5,20)

  name = []
  for i in range(0, size):
    char = chr(randrange(0,26) + 97)
    name.append(char)

  return ''.join(name)
