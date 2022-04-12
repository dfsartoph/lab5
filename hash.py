import hashlib
import strings
import os
from os.path import join, getsize
from os.stat import os.stat_result
import glob
unauthorized = ["/proc/", "/dev/", "/run/", "/sys/", "/tmp/", "/var/lib/", "/var/run/"]
fileList = []



def main():
  for root, dirs, files in os.walk(top, topdown=false): ##returns 3-tuple (dirpath, dirnames, filenames)
    for x in dirs:
      if x in unauthorized:
        dirs.remove(x) 
    for filename in files:
      file_path = os.path.join(root, filename)
      fileList.append((filename,file_path))
      hashing(filename)
  compare_files()
   

def hashing(file):
  fileInfo = ""
  hash_object = hashlib.new('sha256')
  with open(file, 'rb') as f:
    contents = f.read()
    hash_object.update(contents)
    with open("log"+str(os.stat_result(st_mtime)+".txt", 'wb') as g:
      for pair in fileList:
        fileInfo += hash_object.hexidigest() + "," + pair[0] + "," + pair[1] + "\n"
      g.write(fileInfo)
      
##def compare_files():
  ## newList = sorted(glob.glob("log*.txt")):
   ##with open(newList[-1], 'rb') as file1:
     ## with open(newList[-2], 'rb') as file2:
       ##    for x in file1.readlines():
         ##     for y in file2.readlines():
           ##     os.stat_result(
             
              
              
              
              
   


    
if __name__=="__main__":
  main()
  
  
## riptutorial.com/python/example/9666/file-hashing
## docs.python.org/3/library/os.html#files-and-directories
## pythontutorial.net/python-basic/python-dictionary
    
      
   
