import os
import sys
import datetime

def del_older_files(req_path):
  N=30
  if not os.path.exists(req_path):
    print("Please provide valid path, where ur files are located : ")
    sys.exit(1)
    
  if os.path.isfile(req_path):
    print("Please provide dictionary path : ")
    sys.exit(2)
    
  today=datetime.datetime.now()
  
  
  for each_file in os.listdir(req_path):
    each_file_path=os.path.join(req_path,each_file)
    
    if os.path.isfile(each_file_path):
      file_cre_date=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
      dif_days=(today-file_cre_date).days
      
      if dif_days > N:
        os.remove(each_file_path)
        print(each_file_path,dif_days)
        
req_path=input("Enter your path: ")

del_older_files(req_path)
