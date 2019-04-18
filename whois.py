import os
import requests
from selenium import webdriver

#TODO:读取数据从之前处理的数据中
for domainNum in range(2):
	domainFile=open('.\\OutData\\log\\domain\\result_col2_%s.txt' %(domainNum),'rb')
	for row in domainFile:
		print(row)