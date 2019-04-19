import requests
from selenium import webdriver
import time

print('自动化查询域名的备案信息开始...')
# TODO:自动化查询域名的备案信息
for domainNum in range(1):
    domainFile = open('.\\OutData\\log\\domain\\md5_domain_%s.txt' %
                      (domainNum + 1), 'rb')
    resultFile = open('.\\OutData\\log\\whois_info\\whois_info_%s.txt' % (
        domainNum + 1), 'w', encoding='utf-8')
    # 模拟浏览器打开
    url = 'http://whois.chinaz.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    for row in domainFile:
        rowInfo = row.decode().strip()
        inputElem = browser.find_element_by_id('DomainName')
        inputElem.send_keys(rowInfo)
        subBtnElem = browser.find_element_by_class_name('search-write-btn')
        subBtnElem.click()
        time.sleep(2)
        resultElem = browser.find_element_by_id('detail_info')
        result = resultElem.text
        resultFile.write(result)
        resultFile.write('\n\n')
        # 模拟返回
        browser.back()
        continue
