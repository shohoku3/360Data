import csv
import base64
import urllib.parse

for csvNum in range(1):
	LogFile = open('.\\PreData\\log\\2018-12-0%s.csv' % (csvNum + 1), encoding='UTF-8')
	LogReader = csv.reader(LogFile)
	col5f = open('.\\OutData\\log\\col5_%s.txt' % (csvNum + 1), 'a', encoding='UTF-8')
	f5=open('.\\OutData\\log\\col5_%s.txt' % (csvNum + 1),'r', encoding='UTF-8')
	lines5 = len(f5.readlines())  
	print('程序将于第'+str(lines5+1)+'行开始继续破解')
	num=0
	for row in LogReader:
		num+=1
		#第五列提取并处理程序	
		if num>lines5:
			col3=str(row[3])
			if col3 == 'post':
				col5 = base64.standard_b64decode(row[4])
				resultcol5 = urllib.parse.unquote(str(col5))
				col5f.write(resultcol5[1:])
				col5f.write('\n')
				print('The Row '+str(num)+' Success')
			else:
				col5f.write('null')
				col5f.write('\n')

