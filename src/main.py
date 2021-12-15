import sys
from helper import print_directories, print_help_message
from directory import check_directory, delete_directories


def main():
  args = sys.argv
  delete = False
  path = ""
  
  if len(args) < 2:
    print_help_message()
    return
  
  if args[1] == "-d":
    if len(args) != 3:
      print_help_message()
      return
    
    delete = True
    path = args[2]
  else:
    path = args[1]
  
  dirs = check_directory(path)
  
  print(dirs)
  
  if len(dirs) == 0:
    print("No empty directories found")
    return
  
  if delete:
    delete_directories(dirs)
    
    print("Deleted the following directories")
    print_directories(dirs)
  else:
    print_directories(dirs)
    
if __name__ == "__main__":
  main()
