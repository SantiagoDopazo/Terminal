import sys
from utils import *

def main():
    while True:
      sys.stdout.write("$ ")
      sys.stdout.flush()

      # Wait for user input
      command = input()
      if(command == "exit 0"):
        sys.exit(0)
      elif(startWith(command, "echo")):
        print(f"{deletePrefix(command, "echo")}")
      else:
        print(f"{command}: command not found")

    


if __name__ == "__main__":
    main()
