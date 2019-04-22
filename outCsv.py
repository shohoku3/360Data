import csv
from itertools import islice
outputFile=open('.\\OutData\\log\\Output_1.csv','w',newline='',encoding='utf-8')
outputWrite=csv.writer(outputFile)
outputWrite.writerow(['domain','CDN','type','CNAME'])
with open('.\\OutData\\log\\result\\result_1.txt','r',encoding='utf-8') as f:
    while True:
        next_n_lines = list(islice(f, 3))
        
        if not next_n_lines:
            break