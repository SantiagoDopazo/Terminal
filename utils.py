def startWith(string, prefix):
  if len(prefix) > len (string):
    return False
  for i in range(len(prefix)):
    if(string[i] != prefix[i]):
      return False
  return True

def deletePrefix(string, prefix):
  if(startWith(string, prefix)):
    return string[len(prefix):]
  else:
    return string
