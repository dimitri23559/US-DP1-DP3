def without(*n):
  list_without = []
  for code_ascii in range(128):
    continues = False 
    for x in n:
      if str(x).lower() == chr(code_ascii) or str(x).upper() == chr(code_ascii):
        continues = True
    if continues:
      continue
    list_without.append(chr(code_ascii))
  return list_without