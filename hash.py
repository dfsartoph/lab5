import hashlib
import os
from os.path import join, getsize
unauthorized = ["/proc/", "/dev/", "/run/", "/sys/", "/tmp/", "/var/lib/", "/var/run/"]
fileDict = {}



def main():
  for root, dirs, files in os.walk(top, topdown=false): ##returns 3-tuple (dirpath, dirnames, filenames)
    for x in dirs:
      if x in unauthorized:
        dirs.remove(x) 
    for filenames in files:
      file_path = os.path.join(root, filename)
      fileDict[filename] = file_path

def hashing(file):
  hash_object = hashlib.new('sha256')
  with open(file, 'rb') as f:
    contents = f.read()
    hash_object.update(contents)
    with open('filelog.txt', 'wb') as g:
      g.write(hash_object.hexidigest())
      
    

    
if __name__=="__main__":
  main()
  
  
## riptutorial.com/python/example/9666/file-hashing
## docs.python.org/3/library/os.html#files-and-directories
    
      
   
