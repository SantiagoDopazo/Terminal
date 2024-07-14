import sys
from utils import *

def main():
    while True:
      sys.stdout.write("$ ")
      sys.stdout.flush()
      builtinCommands = ["echo", "exit", "type"]
      # Wait for user input
      command = input()
      if(command == "exit 0"):
        sys.exit(0)
      elif(startWith(command, "echo")):
        print(f"{deletePrefix(command, "echo")}")
      elif(startWith(command, "type")):
          if deletePrefix(command, "type") in builtinCommands:
            print(f"{deletePrefix(command, "type")} is a shell builtin")
          else:
            print(f"{deletePrefix(command, "type")}: not found")
      else:
        print(f"{command}: command not found")

    


if __name__ == "__main__":
    main()
