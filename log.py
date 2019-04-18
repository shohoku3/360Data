import csv,base64
import urllib.parse
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#TODO：reader csv file
for csvNum in range(10):
	LogFile=open('.\\PreData\\log\\2018-12-0%s.csv' %(csvNum+1),encoding='UTF-8')
	LogReader=csv.reader(LogFile)
	resultCol2File=open('.\\OutData\\log\\domain\\result_col2_%s.txt' %(csvNum+1),'w',encoding='UTF-8')
	resultCol2File.write('log 2018-12-0%s 解码后的域名'.center(50,'=') %(csvNum+1))
	resultCol2File.write('\n')
	resultCol4File=open('.\\OutData\\log\\base64\\result_col4_%s.txt' %(csvNum+1),'w',encoding='UTF-8')
	resultCol4File.write('log 2018-12-0%s 解码后的post请求'.center(50,'=') %(csvNum+1))
	resultCol4File.write('\n')
	#TODO 模拟浏览器并提交数据
	url='https://www.cmd5.com/'
	brower=webdriver.Chrome()
	brower.get(url)
	#TODO:模拟登录
	loginBtnElem=brower.find_element_by_link_text('qq一键登录')
	loginBtnElem.click()
		#切换iframe
	brower.switch_to_frame('ptlogin_iframe')
	qqLoginBtnElem=brower.find_element_by_link_text('帐号密码登录')
	qqLoginBtnElem.click()
	qqInputElem=brower.find_element_by_id('u')
	qqInputElem.send_keys('2812845017')
	qqPsdInputElem=brower.find_element_by_id('p')
	qqPsdInputElem.send_keys('syf199610021016')
	qqBtnElem=brower.find_element_by_id('login_button')
	qqBtnElem.click()
	time.sleep(5)
	for row in LogReader:	#TODO: IP

		#TODO: 在线查询MD5
			#TODO:将待处理的MD5数据切片
		decodecol2=row[2].split('.')
		resultCol2=str(decodecol2[1])
			#TODO:模拟提交表单
		inputElem=brower.find_element_by_id('ctl00_ContentPlaceHolder1_TextBoxInput')
		inputElem.send_keys(resultCol2)
		selectElm = Select(brower.find_element_by_id('ctl00_ContentPlaceHolder1_InputHashType'))
		selectElm.select_by_value('md5(md5($pass))')  
		btnElem=brower.find_element_by_id('ctl00_ContentPlaceHolder1_Button1')
		btnElem.click()
		answerElem=brower.find_element_by_id('LabelAnswer').text
			#抓取的内容进行在线查询 获取信息
			#TODO 内容写入文本
		resultCol2File.write('www.'+answerElem+'.'+str(decodecol2[2])+'.com')
		resultCol2File.write('\n')

		#TODO: decode base64 and write in resultCol4
		decodeCol4=base64.standard_b64decode(row[4])
		resultCol4=urllib.parse.unquote(str(decodeCol4))
		resultCol4File.write(resultCol4)

		#TODO: