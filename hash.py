import hashlib ## import hash library to utilize sha256 hash
import os
from os.path import join, getsize
from os.stat import os.stat_result
import glob
unauthorized = ["/proc/", "/dev/", "/run/", "/sys/", "/tmp/", "/var/lib/", "/var/run/"] ## list of directories that should be skipped when iterating through the directories
fileList = []



def main(): ## this function will iterate through the directories, call the hashing function, and store the filename and path in a tuple in a list
  for root, dirs, files in os.walk(top, topdown=false): ##returns 3-tuple (dirpath, dirnames, filenames)
    for x in dirs:
      if x in unauthorized:
        dirs.remove(x) 
    for filename in files:
      file_path = os.path.join(root, filename)
      fileList.append((filename,file_path))
      hashing(filename)
  compare_files()
   

def hashing(file): ## this function will hash each file and add file hash, filename, and file path into a log file 
  fileInfo = []
  hash_object = hashlib.new('sha256')
  with open(file, 'rb') as f:
    contents = f.read()
    hash_object.update(contents)
    with open("log"+str(os.stat_result(st_mtime)+".txt", 'wb') as g:
      for pair in fileList:
        fileInfo.append((hash_object.hexidigest(),pair[0],pair[1]))
      g.write(fileInfo)
      
def compare_files(): ## this function will compare the most recent file, with the second most recent file, and print out summary information INCOMPLETE
  summaryInfo = ""
  newList = sorted(glob.glob("log*.txt")):
   with open(newList[-1], 'rb') as file1:
     with open(newList[-2], 'rb') as file2:
       for x in file1.readlines():
         for y in file2.readlines():
           if x != y:
              summaryInfo += str(x[1])
              os.stat_result(
             
              
              
              
              
   


    
if __name__=="__main__":
  main()
  
## RESOURCES USED FOR THIS LAB: 
## riptutorial.com/python/example/9666/file-hashing
## docs.python.org/3/library/os.html#files-and-directories
## pythontutorial.net/python-basic/python-dictionary
    
      
   
