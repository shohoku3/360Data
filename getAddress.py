import geoip2.database
import re

print('自动化获取域名的物理地址')
reader = geoip2.database.Reader('.\\lib\\GeoLite2-City.mmdb')
refile=open('.\\OutData\\log\\address\\address_1.txt','w',encoding='utf-8')
def getAddress(ip):
    response = reader.city(ip)
    country = response.country.name
    city = response.city.names.get('zh-CN', '')
    return country, city

reader = geoip2.database.Reader('.\\lib\\GeoLite2-City.mmdb')
hostlist = open('.\\OutData\\log\\dns_parse\\dns_parse_1.txt','r',encoding='utf-8')
for host in hostlist:
    if host[-2] == '1':
        hostRegex=re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
        result=hostRegex.findall(host)
        res=' '.join(result)
        address=' '.join(getAddress(res))
        print(str(res).ljust(20),str(address).ljust(20),file=refile)