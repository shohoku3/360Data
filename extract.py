import csv
import base64
import urllib.parse



for csvNum in range(1):
	print('正在生成hash_value_%s.txt ...' %(csvNum+1))
	print('正在生成base64_post_%s.txt ...' %(csvNum+1))
	LogFile = open('.\\PreData\\log\\2018-12-0%s.csv' % (csvNum + 1), encoding='UTF-8')
	LogReader = csv.reader(LogFile)
	resultCol2File = open('.\\OutData\\log\\hashvalue\\hash_value_%s.txt' % (csvNum + 1), 'w', encoding='UTF-8')
	resultCol4File = open('.\\OutData\\log\\base64\\base64_post_%s.txt' % (csvNum + 1), 'w', encoding='UTF-8')
	for row in LogReader:
		#第三列域名MD5散列值提取程序
		decodecol2 = row[2].split('.')
		try:
			if len(decodecol2)==4:
				resultCol2 = str(decodecol2[1])
				resultCol2File.write(resultCol2)
				resultCol2File.write('\n')
			elif len(decodecol2)==3:
				if len(str(decodecol2[1]))<4:
					resultCol2=str(decodecol2[0])
					resultCol2File.write(resultCol2)
					resultCol2File.write('\n')
				else:
					resultCol2=str(decodecol2[1])
					resultCol2File.write(resultCol2)
					resultCol2File.write('\n')
			elif len(decodecol2)==2:
				resultCol2=str(decodecol2[0])
				resultCol2File.write(resultCol2)
				resultCol2File.write('\n')
			else :
				resultCol2=str(decodecol2[0])
				resultCol2File.write(resultCol2)
				resultCol2File.write('\n')	
		except Exception as e:
			print('list index out of range')
		#第五列提取并处理程序	
		decodeCol4 = base64.standard_b64decode(row[4])
		resultCol4 = urllib.parse.unquote(str(decodeCol4))
		resultCol4File.write(resultCol4)
		resultCol4File.write('\n\n')
	resultCol2File.close()
	resultCol4File.close()

