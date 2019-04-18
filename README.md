# 360Data

### 相关说明

- 数据脱敏：在一个不可逆转的过程中，敏感数据的真实值被转换成虚构的、但看起来逼真的值，原始值被永久改变且无法恢复。
- MD5
- Base64

### ToDoList
- [x] python 实现 base64 转码模块
- [x] python 模拟浏览器实现在线MD5解密
- [ ] 无法突破在线查询限制

### 项目结构
E:.
│  .gitignore
│  geckodriver.log
│  log.py
│  README.md
│
├─OutData
│  └─log
│      ├─base64
│      │      result_col4_*.txt
│      │
│      └─domain
│              result_col2_*.txt
│
└─PreData
    └─log
            2018-12-**.csv