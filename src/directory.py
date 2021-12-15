import os
from pathlib import Path

def check_directory(path):
  result = []
  empty_dirs = []
  
  p = Path(path)
  
  dirs = [x for x in p.iterdir() if x.is_dir()]
  files = [x for x in p.iterdir() if not x.is_dir()]
  
  if len(files) == 0 and len(dirs) == 0:
    result.append(path)
    return result
  
  for dir in dirs:
      empty_dirs = check_directory(dir.as_posix())
      result = result + empty_dirs
      
  if len(empty_dirs) == len(dirs) and len(files) == 0:
    result.append(path)
  
  return result

def delete_directories(dirs):
  for dir in dirs:
    os.rmdir(dir)
