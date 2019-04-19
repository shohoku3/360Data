import csv
import base64
import urllib.parse

# TODO：自动化解密base64获得post行为
print('自动化解密base64数据开始...')
for csvNum in range(1):
    LogFile = open('.\\PreData\\log\\2018-12-0%s.csv' %
                   (csvNum + 1), encoding='UTF-8')
    LogReader = csv.reader(LogFile)
    resultCol4File = open('.\\OutData\\log\\base64\\base64_post_%s.txt' % (
        csvNum + 1), 'w', encoding='UTF-8')
    for row in LogReader:
        decodeCol4 = base64.standard_b64decode(row[4])
        resultCol4 = urllib.parse.unquote(str(decodeCol4))  # 将html编码转换成字符串
        resultCol4File.write(resultCol4)
        resultCol4File.write('\n\n')
