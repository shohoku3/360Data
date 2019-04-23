import csv
f=open('.\\OutData\\log\\result\\result_1.txt','r',encoding='utf-8')
outputFile=open('.\\OutData\\LOG\\output_1.csv','w',newline='',encoding='utf-8-sig')
outputWrite=csv.writer(outputFile)
outputWrite.writerow(['域名','CNAME解析地址','服务提供商','A解析地址','物理地址','域名类别','记录类别','错误日志','错误对应域名'])
for row in f:
	print (row.split(','))
	outputWrite.writerow(row.split(','))
