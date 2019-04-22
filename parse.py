from dns.resolver import *
import geoip2.database
import re

#该程序为解析程序 负责查询物理地址 查询云服务提供商 dns解析
print('自动化解析...')
reader = geoip2.database.Reader('.\\lib\\GeoLite2-City.mmdb')
#查询物理地址
def getAddress(ip):
    response = reader.city(ip)
    country = response.country.name
    #city = response.city.names.get('zh-CN', '')
    if country=='China':
        city=response.city.names.get('zh-CN','')
    else:
        city=response.city.names.get('en','')
    return country ,city

for domainFileNum in range(1):
    hostlist = open('.\\OutData\\log\\col3_%s.txt' %(domainFileNum+1),'r', encoding='utf-8')
    f = open('.\\OutData\\log\\result\\result_%s.txt' %(domainFileNum+1), 'w',encoding='utf-8')
    for host in hostlist:
        try:
            host = host.split('\n')[0]
            if 'gov.cn' in host:
                attr = 'gov'
            elif 'edu' in host:
                attr = 'edu'
            elif 'org' in host:
                attr = 'org'
            else:
                attr='other'         
            #查询A记录、CNAME记录 #ID 0:CNAME 1:A记录
            a = query(host)
            FLAG=0
            for dns in a.response.answer:
                if 'CNAME' in str(dns):
                    cdnRegex=re.compile(r'[a-z0-9]{5,}\.[a-z0-9]{5,}\.com')
                    cdnre=cdnRegex.findall(str(dns))
                    cdnhost=''.join(cdnre)
                    if '360cloudwaf' in cdnhost  or '360safeedns.com' in cdnhost:
                        cdn='360云服务'
                    elif 'powercdn.cn' in cdnhost:
                        cdn='动力在线'
                    f.write(host+','+cdnhost+','+cdn)
                    FLAG=1
                elif 'A' in str(dns):
                    if FLAG==1:
                        record='A and CNAME'
                        hostRegex=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
                        result=hostRegex.findall(str(dns))
                        res=' '.join(result)
                        address=' '.join(getAddress(res))
                        f.write(','+res+','+address+','+attr+','+record+',')
                        FLAG=0
                    else:
                        cdnhost='Null'
                        record='A'
                        hostRegex=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
                        result=hostRegex.findall(str(dns))
                        res=' '.join(result)
                        address=' '.join(getAddress(res))
                        cdn='Null'
                        f.write(host+','+cdnhost+','+cdn+','+res+','+address+','+attr+','+record+',')
#泛解析查询
            host = 'sanshibuing.'+ host
            b=query(host)
            if b: 
                f.write('已经开启泛解析'+','+'\n')
        except Exception as e:
            pass
            f.write(str(e)+','+'\n')
