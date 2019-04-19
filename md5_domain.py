import csv
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

print('自动化在线md5解密域名开始...')
# TODO：自动化进行在线md5解密域名
for csvNum in range(2):
    LogFile = open('.\\PreData\\log\\2018-12-0%s.csv' %
                   (csvNum + 1), encoding='UTF-8')
    LogReader = csv.reader(LogFile)
    resultCol2File = open('.\\OutData\\log\\domain\\md5_domain_%s.txt' % (
        csvNum + 1), 'w', encoding='UTF-8')
    resultCol2File.write('\n')
    # TODO 模拟浏览器并提交数据
    url = 'https://www.cmd5.com/'
    brower = webdriver.Chrome()
    brower.get(url)
    # TODO:模拟登录
    loginBtnElem = brower.find_element_by_link_text('qq一键登录')
    loginBtnElem.click()
    # 切换iframe
    brower.switch_to_frame('ptlogin_iframe')
    qqLoginBtnElem = brower.find_element_by_link_text('帐号密码登录')
    qqLoginBtnElem.click()
    qqInputElem = brower.find_element_by_id('u')
    qqInputElem.send_keys('2812845017')
    qqPsdInputElem = brower.find_element_by_id('p')
    qqPsdInputElem.send_keys('syf199610021016')
    qqBtnElem = brower.find_element_by_id('login_button')
    qqBtnElem.click()
    # 强制暂停timeout 等待页面加载 根据网速做适当调整
    time.sleep(3)
    for row in LogReader:
            # TODO: 在线查询MD5
                    # TODO:将待处理的MD5数据切片
        decodecol2 = row[2].split('.')
        resultCol2 = str(decodecol2[1])
        print(decodecol2)
        # TODO:模拟提交表单
        inputElem = brower.find_element_by_id(
            'ctl00_ContentPlaceHolder1_TextBoxInput')
        inputElem.clear()
        inputElem.send_keys(resultCol2)
        selectElm = Select(brower.find_element_by_id(
            'ctl00_ContentPlaceHolder1_InputHashType'))
        selectElm.select_by_value('md5(md5($pass))')
        btnElem = brower.find_element_by_id(
            'ctl00_ContentPlaceHolder1_Button1')
        btnElem.click()
        answerElem = brower.find_element_by_id('LabelAnswer').text
        if answerElem!='验证错误，如有问题 请更换浏览器断开vpn等再试一次':
        # TODO 内容写入文本
            resultCol2File.write('www.' + answerElem + '.' +str(decodecol2[2])+str(decodecol2[3]))
            resultCol2File.write('\n')
        else:
            brower.quit()