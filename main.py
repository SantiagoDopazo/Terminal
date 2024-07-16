import sys
from utils import *
import os

def main():
    PATH =  os.environ.get("PATH")
    paths =  PATH.split(os.pathsep)
    builtinCommands = ["echo", "exit", "type"]
    #print(f"{PATH}")
    print(f"{paths}")
    while True:
      sys.stdout.write("$ ")
      sys.stdout.flush()
      
      # Wait for user input
      command = input()
      if(command == "exit 0"):
        sys.exit(0)

      if(startWith(command, "echo")):
        print(f"{deletePrefix(command, "echo")}")

      if(startWith(command, "type")):
        cmd = deletePrefix(command, "type")
        if cmd in builtinCommands:
          print(f"{cmd} is a shell builtin")
        else:
          cmd_path = searchCommand(cmd, paths)
          if(cmd_path):
            print(f"{cmd} is {cmd_path}")
          else:
            print(f"{cmd}: not found")
      else:
        print(f"{command}: command not found")

    


if __name__ == "__main__":
    main()
