import os
def startWith(string, prefix):
  if len(prefix) > len (string):
    return False
  for i in range(len(prefix)):
    if(string[i] != prefix[i]):
      return False
  return True

def deletePrefix(string, prefix):
  if(startWith(string, prefix)):
    return string[len(prefix)+1:]
  else:
    return string
  
def searchCommand(command, paths):
  for path in paths:
    complete_path = os.path.join(path, command)
    if os.path.exists(complete_path) and os.access(complete_path, os.X_OK):
      return path
    return None
