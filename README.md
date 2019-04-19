# 360Data

### 相关说明

- 数据脱敏：在一个不可逆转的过程中，敏感数据的真实值被转换成虚构的、但看起来逼真的值，原始值被永久改变且无法恢复。
- MD5
- Base64

### ToDoList 4-18
- [x] python 实现 base64 自动化转码
- [x] python 模拟浏览器实现 自动化在线MD5解密
- [ ] 无法突破在线查询限制 
- [x] 进行whois查询
- [x] 进行DNS解析 查看CNAME,A
- [x] 解析ip地址的物理地址
- [x] 查看网站是否开启CDN 云服务

### Config
- 修改浏览器 default chrome
- 修改读取日志文件路径 defaut:.\\PreData
- 修改中间数据及最终数据

### lib
- 使用GeoLite2-City free数据库 查询ip地址

### 文件结
```
E:.
│  .gitignore							//
│  base64_post.py 						//base64解密自动化
│  cname_extract.py 					//CNAME提取程序
│  dns_parse.py 						//域名解析自动化程序
│  geckodriver.log 						//浏览器驱动日志
│  getAddress.py 						//获取物理地址的程序
│  md5_domain.py 						//破解MD5的自动化程序
│  README.md  							//使用说明
│  whois_domain.py 						//whois 自动化程序
│
├─lib									//查询域名物理地址的所需的数据库文件
│      COPYRIGHT.txt
│      GeoLite2-City.mmdb
│      LICENSE.txt
│      README.txt
│
├─OutData								//输出数据文件夹
│  └─log
│      ├─address						//域名物理地址的文件夹
│      │      address_1.txt
│      │
│      ├─base64							//解密base64的文件夹
│      │      base64_post_1.txt
│      │
│      ├─dns_parse						//DNS解析的文件夹
│      │      dns_parse_1.txt
│      │
│      ├─domain							//解密MD5的域名文件夹
│      │      md5_domain_1.txt
│      │
│      └─whois_info						//生成whois信息的文件夹
│              whois_info_1.txt
│
└─PreData								//预处理数据的文件夹
    └─log
            2018-12-01.csv
```