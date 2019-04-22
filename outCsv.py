import csv
f=open('.\\OutData\\log\\result\\result_1.txt','r',encoding='utf-8')
outputFile=open('.\\OutData\\LOG\\output_1.csv','w',newline='',encoding='utf-8')
outputWrite=csv.writer(outputFile)
for row in f:
	print (row.split(','))
	outputWrite.writerow(row.split(','))