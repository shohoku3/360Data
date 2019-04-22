import csv
import hashCrack
import eventlet

#该程序为提取程序 负责第三列域名MD5散列值提取 第五列提取并处理 
#该程序支持断点破解
eventlet.monkey_patch()
for csvNum in range(1):
	LogFile = open('.\\PreData\\log\\2018-12-0%s.csv' % (csvNum + 1), encoding='UTF-8')
	LogReader = csv.reader(LogFile)
	col3f = open('.\\OutData\\log\\col3_%s.txt' % (csvNum + 1),'a', encoding='UTF-8')
	f3=open('.\\OutData\\log\\col3_%s.txt' % (csvNum + 1),'r', encoding='UTF-8')
	lines3 = len(f3.readlines())
	print('程序将于第'+str(lines3+1)+'行开始继续破解')
	num=0
	for row in LogReader:
		num+=1
		#第三列域名MD5散列值提取程序
		if num>lines3:
			col3 = row[2].split('.')
			try:
				for i in range(len(col3)):
					if len(str(col3[i]))>3:
						try:
							hashval=col3[i]
							with eventlet.Timeout(30,False):
								demd5 = hashCrack.crack(hashval)
								col3f.write(demd5+'.')
								continue
							col3f.write('破解超时.')
						except Exception as e:
							col3f.write('破解失败.')
					else:
						if i == len(col3)-1:
							col3f.write(col3[i]+'\n')
							print('The Row '+str(num)+' Success')
						else:
							col3f.write(col3[i]+'.')
			except Exception as e:
				print('error')
