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

#云服务提供商
def searchCdn(host):
    if '360cloudwaf' in host or '360safeedns.com' in host:
        product='360云服务'
    if 'powercdn.cn' in host:
        product='动力在线'
    if 'yunjiasu-cdn' in host:
        product='百度云加速'
    if 'cname.365cyd.cn' in host or 'cdn.jiashule.' in host:
        product='创宇云服务'
    return product

for domainFileNum in range(1):
    hostlist = open('.\\OutData\\log\\col2_%s.txt' %(domainFileNum+1),'r', encoding='utf-8')
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
            for dns in a.response.answer:
                if 'CNAME' in str(dns):
                    record='CANME'
                    cdn=searchCdn(str(dns))
                    address=''
                elif 'A' in str(dns):
                    record='A'
                    cdn=''
                    hostRegex=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
                    result=hostRegex.findall(str(dns))
                    res=' '.join(result)
                    address=' '.join(getAddress(res))
                for dns in dns.items:
                    f = open('.\\OutData\\log\\result\\result_%s.txt' %(domainFileNum+1), 'a',encoding='utf-8')
                    print(host.ljust(40), (str(dns)).ljust(40),cdn.ljust(10),address.ljust(10),attr.ljust(10),record.ljust(10), file=f)
#泛解析查询
            host = 'sanshibuing.'+ host
            b=query(host)
            for dns in b.response.answer:
                for dns in dns.items:
                    pass 
                    id=2
                    f = open('.\\OutData\\log\\result\\result_%s.txt' %(domainFileNum+1), 'a',encoding='utf-8')
                    print(host.ljust(40),(str(dns)).ljust(40),attr.ljust(10),id,file=f)
        except Exception as e:
            pass
            f = open('.\\OutData\\log\\result\\result_%s.txt' %(domainFileNum+1), 'a',encoding='utf-8')
            print(host.ljust(40),'Connet Error', file=f)
