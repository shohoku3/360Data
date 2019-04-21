import csv
import base64
import urllib.parse
import hashCrack
import eventlet

#该程序为提取程序 负责第三列域名MD5散列值提取 第五列提取并处理程序	
eventlet.monkey_patch()
for csvNum in range(1):
	LogFile = open('.\\PreData\\log\\2018-12-0%s.csv' % (csvNum + 1), encoding='UTF-8')
	LogReader = csv.reader(LogFile)
	f = open('.\\OutData\\log\\col2_%s.txt' % (csvNum + 1),'w', encoding='UTF-8')
	col4f = open('.\\OutData\\log\\col4_%s.txt' % (csvNum + 1), 'w', encoding='UTF-8')
	for row in LogReader:
		#第三列域名MD5散列值提取程序
		col2 = row[2].split('.')
		try:
			for i in range(len(col2)):
				if len(str(col2[i]))>3:
					try:
						hashval=col2[i]
						with eventlet.Timeout(30,False):
							demd5 = hashCrack.crack(hashval)
							f.write(demd5+'.')
							continue
						f.write('破解超时.')
					except Exception as e:
						f.write('破解失败.')
				else:
					if i == len(col2)-1:
						f.write(col2[i]+'\n')
					else:
						f.write(col2[i]+'.')
		except Exception as e:
			print('list index out of range')
		#第五列提取并处理程序	
		col3=str(row[3])
		if col3 == 'post':
			col4 = base64.standard_b64decode(row[4])
			resultCol4 = urllib.parse.unquote(str(col4))
			col4f.write(resultCol4[1:])
			col4f.write('\n\n')
		else:
			col4f.write('null')
			col4f.write('\n\n')

