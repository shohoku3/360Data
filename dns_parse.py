from dns.resolver import *
import re
print('dns解析开始...')
for domainFileNum in range(1):
    hostlist = open('.\\OutData\\log\\domain\\md5_domain_%s.txt' %(domainFileNum+1),'r', encoding='utf-8')
    for host in hostlist:
        try:
            host = host.split('\n')[0]
            if 'gov.cn' in host:
                attr = 'gov'
            elif 'edu' in host:
                attr = 'edu'
            else:
                attr = 'other'  
#查询A记录、CNAME记录 #ID 0:CNAME 1:A记录
            a = query(host)
            for dns in a.response.answer:
                if 'CNAME' in str(dns):
                    id = 0
                elif 'A' in str(dns):
                    id = 1
                for dns in dns.items:
                    f = open('.\\OutData\\log\\dns_parse\\dns_parse_%s.txt' %(domainFileNum+1), 'a',encoding='utf-8')
                    print(host.ljust(40), (str(dns)).ljust(40), attr.ljust(5), id, file=f)
#泛解析查询
            host = 'sanshibuing.'+ host
            b=query(host)
            for dns in b.response.answer:
                for dns in dns.items:
                    pass 
                    id=2
                    f = open('.\\OutData\\log\\dns_parse\\dns_parse_%s.txt' %(domainFileNum+1), 'a',encoding='utf-8')
                    print(host.ljust(40),(str(dns)).ljust(40),attr.ljust(5),id,file=f)
        except Exception as e:
            pass
            print(host.ljust(40),'Connet Error', file=f)
