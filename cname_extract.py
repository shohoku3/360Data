#TODO:从CNAME中提取使用CDN、云防护
import re


print('自动化实现CDN云防护分析')

def searchCdn(host):
	if '360cloudwaf' in host or '360safeedns.com' in host:
		product='360云服务'
		f=open('.\\OutData\\log\\cdn\\cdn_1.txt','a',encoding='utf-8')
		print(host.ljust(60),product,file=f)
	if 'powercdn.cn' in host:
		product='动力在线'
		f=open('.\\OutData\\log\\CDN\\cdn_1.txt','a',encoding='utf-8')
		print(host.ljust(60),product,file=f)
	if 'yunjiasu-cdn' in host:
		product='百度云加速'
		f=open('.\\OutData\\log\\CDN\\cdn_1.txt','a',encoding='utf-8')
		print(host.ljust(60),product,file=f)
	if 'cname.365cyd.cn' in host or 'cdn.jiashule.' in host:
		product='创宇云服务'
		f=open('.\\OutData\\log\\CDN\\cdn_1.txt','a',encoding='utf-8')
		print(host.ljust(60),product,file=f)


hostlist = open('.\\OutData\\log\\dns_parse\\dns_parse_1.txt','r',encoding='utf-8')
for host in hostlist:
    if host[-2] == '0':
    	searchCdn(host)

