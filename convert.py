from without import without

fail = False
options = ['Text', 'desimal', 'Binary', 'Octal', 'Hexadecimal']


#                   filter input
def filterBin(input = str):
  for notnumBin in range(2,10):
      if str(notnumBin) in input:
        return True

def filterOct(input = str):
  for notnumOct in range(8,10):
      if str(notnumOct) in input:
        return True

def filterHex(input = str):
  for notnumHex in without(0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'):
      if str(notnumHex) in input:
        return True

def filterFrom(input = str):
  From = ['Text']
  
  # filterNumber
  if input.isnumeric() :
    From.append('desimal')
    
    # filterbinary
    if not(filterBin(input)):
      From.append('Binary')
      
    # filteroctal
    if not(filterOct(input)):
      From.append('Octal')

  # filterhexadesimal    
  if not(filterHex(input)):
    From.append('Hexadecimal')
    
  return From
#               end filter input

def filterFroms(input = list):
  From = []
  allvalFilterFrom = []
  
  for inp in input:
    valFilter = filterFrom(inp)
    allvalFilterFrom.append(valFilter)
  
  for ops in options:
    add = True
    for valFilter in allvalFilterFrom:
      if ops in valFilter:
        pass
      else:
        add = False
        
    if add :
      From.append(ops)
  
  return From


#                     To Desimal
# Text
def fromText(n = str):
  return ord(n)

# Biner
def fromBin(n = list):
  value = 0
  for i in range(len(n)):
    digit = n.pop()
    if digit == '1':
      value = value + pow(2, i)
    else :
      fail = True
  return value


# Octal
def fromOct(n = list):
  value = 0
  for i in range(len(n)):
    digit = n.pop()
    if digit == '0':
      value = value + (0*pow(8, i))
    elif digit == '1':
      value = value + (1*pow(8, i))
    elif digit == '2':
      value = value + (2*pow(8, i))
    elif digit == '3':
      value = value + (3*pow(8, i))
    elif digit == '4':
      value = value + (4*pow(8, i))
    elif digit == '5':
      value = value + (5*pow(8, i))
    elif digit == '6':
      value = value + (6*pow(8, i))
    elif digit == '7':
      value = value + (7*pow(8, i))
    else:
      fail = True 
      
  return value

# Hexadecimal
def fromHex(n = list):
  value = 0
  for i in range(len(n)):
    digit = n.pop()
    if digit == '0':
      value = value + (0*pow(16, i))
    elif digit == '1':
      value = value + (1*pow(16, i))
    elif digit == '2':
      value = value + (2*pow(16, i))
    elif digit == '3':
      value = value + (3*pow(16, i))
    elif digit == '4':
      value = value + (4*pow(16, i))
    elif digit == '5':
      value = value + (5*pow(16, i))
    elif digit == '6':
      value = value + (6*pow(16, i))
    elif digit == '7':
      value = value + (7*pow(16, i))
    elif digit == '8':
      value = value + (8*pow(16, i))
    elif digit == '9':
      value = value + (9*pow(16, i))
    elif digit == 'a':
      value = value + (10*pow(16, i))
    elif digit == 'b':
      value = value + (11*pow(16, i))
    elif digit == 'c':
      value = value + (12*pow(16, i))
    elif digit == 'd':
      value = value + (13*pow(16, i))
    elif digit == 'e':
      value = value + (14*pow(16, i))
    elif digit == 'f':
      value = value + (15*pow(16, i))
    else:
      fail = True 


  return value
#               end To Decimal



#                   To Value
# Text
def toText(n = int):
  return chr(n)

# Biner
def toBin(n = int):
  return bin(n).replace("0b", "").zfill(8)


# Octal
def toOct(n = int):
  return oct(n).replace("0o", "")
  

# Hexadecimal
def toHex(n = int):
  return hex(n).replace("0x", "")
#               end To Value
