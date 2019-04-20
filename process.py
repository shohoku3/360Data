import hashCrack
import eventlet
import time

eventlet.monkey_patch()
hashFile=open('.\\OutData\\log\\hashvalue\\hash_value_1.txt','r')
f=open('.\\OutData\\log\\domain\\md5_1.txt','w',encoding='utf-8')
for row in hashFile:
	try:
		hashval=row[0:-1]
		with eventlet.Timeout(10,False):
			demd5 = hashCrack.crack(hashval)
			print(demd5.ljust(10),'破解成功'.rjust(10),file=f)
			continue
		print('破解超时'.rjust(10),file=f)
	except Exception as e:
		print('破解失败'.rjust(10),file=f)