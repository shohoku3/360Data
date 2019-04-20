# 360Data

### 相关说明

- 数据脱敏：在一个不可逆转的过程中，敏感数据的真实值被转换成虚构的、但看起来逼真的值，原始值被永久改变且无法恢复。
- MD5
- Base64

### ToDoList 
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
- [x] 对于物理地址在国外的地址进行标识
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
### Config
- 浏览器 chrome 用作模拟浏览器
- 读入的日志文件路径 defaut:.\\PreData\\

### lib
- 使用GeoLite2-City free数据库 查询ip地址

### 文件结构
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
│          2018-12-01.csv //预处理文件
└─__pycache__
        hashCrack.cpython-36.pyc
```
