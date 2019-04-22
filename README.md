# 360Data

## 相关说明
- 数据脱敏：在一个不可逆转的过程中，敏感数据的真实值被转换成虚构的、但看起来逼真的值，原始值被永久改变且无法恢复。
- 这是一个自动化程序 用来解密MD5  并且解析域名
## ToDoList 
##### 4-18
- [x] python 实现 base64 自动化转码
- [x] python 模拟浏览器实现 自动化在线MD5解密
- [ ] 无法突破在线查询限制 测试<50
##### 4-19 
- [x] 进行whois查询
- [x] 进行DNS解析 查看CNAME,A
- [x] 解析ip地址的物理地址
- [x] 查看网站是否开启CDN 云服务
- [x] 修复查询物理地址时外国不显示城市
- [ ] 对于物理地址在国外的地址进行标识
- [x] CNAME 查询那些开启了云服务 云服务厂商是
##### 4-20
- [ ] 尝试将运行测试结果合并
- [x] 尝试利用其它方式破解MD5
- [x] 成功用其他方式替换在线查询
- [x] 解决提取程序问题
- [x] 尝试将提取程序合并
- [x] 解决提取第三列时提取值为空问题
- [x] 超时异常处理
- [x] 超时打印
- [x] 尝试将提取与操作程序合并 
- [x] 合并解析程序 
##### 4-21 
- [x] 尝试进行断点破解
- [ ] 可能存在数据量大无法写入的问题
- [ ] 本地破解md5存在一定的命中失败
#### 4-22
- [ ] 将结果数据导入csv
- [ ] 可能存在断点破解数据写入无法换行
- [x] 尝试将两个破解程序分离 crackcol3 crackcol5


## 可能存在的BUG
- 可能存在数据量大无法写入的问题
- 本地破解md5存在一定的命中失败
- 可能存在断点破解数据写入无法换行
- 可能存在断点破解数据非正常结束时 写入漏行问题

##强烈建议
- 断点破解开始时以整行结束后的新行开始
- 浏览器 chrome 用作模拟浏览器
- 检查lib是否存在

## lib
- csv
- base64
- urllib.parse
- hashCrack
- eventlet
- dns
- geoip2.database
- re

## 文件结构
```
  .gitignore
│  geckodriver.log
│  hashCrack.py  //破解程序
│  index.py  //负责提取数据的主入口
│  parse.py  //负责分析数据
│  README.md //
│  whois_domain.py  //自动化whois查询
│
├─lib //数据库文件
│      COPYRIGHT.txt
│      GeoLite2-City.mmdb
│      LICENSE.txt
│      README.txt
│
├─OutData
│  └─log
│      │  col2_1.txt
│      │  col4_1.txt
│      │
│      ├─result
│      │      result_1.txt
│      │
│      └─whois_info
│              whois_info_1.txt
│
├─PreData
│  └─log
│          2018-12-01.csv //预处理文件放到这里
└─__pycache__
        hashCrack.cpython-36.pyc
```