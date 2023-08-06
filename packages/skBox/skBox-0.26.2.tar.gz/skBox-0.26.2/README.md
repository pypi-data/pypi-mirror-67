

# skBox使用说明文档

目录

[TOC]

## 一、基本信息

|   版本   |      v0.26.2       |
| :------: | :----------------: |
|   作者   |    Hanmi Cheng     |
| 版本时间 |     2020.02.01     |
| 联系邮箱 | jxmt089659@163.com |

本包致力于为数据科学工作者提供一些辅助性的工具，其原点是数据分析、机器学习建模及其工程化过程中有许多反复造轮子的代码，基本面上许多其他开源工具已经提供了很好的支持，但总有一些使用不方便的问题。有许多的常见、常用函数也需要进行反复造轮子，代码其实非常容易如根据时间计算年龄之类的，所以本项目致力于以下几个方面:

- 一些基本模块的简化封装以及底层问题的解决
- 常用的计算逻辑，但又不耦合与业务的部分的封装
- pandas dataframe及其周围衍生包的常用函数封装以及开发额外的功能

## 二、工具介绍

### 1. skBox.DfTool： pd.DataFrame工具

提供pandas的一些简化的代码操作封装

```python
from skBox.DfTool import DataFrameDf

dfd = DataFrameDf(df=df)
# 重新获取df
df = dfd.df
```

#### 1.1 数据列base64解码与编码

```python
# 对指定列进行base64解码
dfd.base64_decoder(names=['col1', 'col2'])
# 对指定列进行base64编码
dfd.base64_encoder(names=['col1', 'col2'])
```

#### 1.2 常规操作

```python
dfd.drop(name=['col1', 'col2'])
dfd.rename(rename_dict={'改名前': '改名后'})
```

#### 1.3 自动对列中的json格式数据进行递归拆解行转列

目前只做到对单列进行拆解。对于最后{k: v}格式数据 ，如果为list, 且list内数据不再包含另一个dict, 则数据不会进行继续拆分，防止数据从数据意义上做了没有必要的行转列。对于json格式内，一个dict内平级包含2个value为列表的数据，数据直接会计算笛卡尔积，可能造成错误，请尽量避免这种情况发生。如·``'{"一年一班": [{"姓名": "张三"}, {"姓名": "李四"}],"一年二班":[{"姓名": "张三"}, {"姓名": "李四"}]}'``

```python
dfd.json_sep_entance(ex_col='RESP_MSG')
```

### 2. skBox.DocxApi：python写word文档

提供对python-docx的封装，利用python快速生产word文档(当然，内容得自己写)

```python
from skBox.DocxApi import Docxer

doc = Docxer()
```

#### 2.1 增加标题

```python
doc.add_heading("我是谁")
```

#### 2.2 增加段落

```python
doc.add_paragraph("今天我去哪了", alignment='居中') # 目前只做了默认靠左和居中，其他还没写
```

#### 2.3 根据pandas的df创建表格

```
df = pd.DataFrame({"aa": range(10), "bb":range(10, 20)}, index=range(-10, 0))
df.index.name = '我是索引'
doc.add_table(df, index=True)
```

#### 2.4 插入图片

```python
add_picture("e:/temp/test.jpg", width=6, height=None) # 目前支持单位 英尺（Inches)
```

### 3. 邮件发送模块

目前只支持腾讯企业邮箱，其他还没做，要做的话可能API会改. 目前代码结构还是有点问题的。

#### 3.1. 一键使用方式

```
from skBox.MailTool import ExMail
mail = ExMail(user=user, passwd=passwd)
mail.send_email(self, to_list, cc_list, tag=None, body=None, doc=None, subtype=None):
```

### 4. skBox.skLogger：日志记录模块

skLogger为魔改封装版logging模块。提供一键默认配置，多进程日志打印，自定义日志格式，格式内自定义输出等功能。

#### 4.1 线程安全的日志打印(功能最强)

```python
from skBox.Toolbox import get_logger_prod, LoggerAdapter
# 快速初始化
logger = get_logger(log_file_name, level="info", log_dir=None, daily_handler=False, keep=1095, compress=True)

# 进阶用法，自定义Fomatter的参数，并且overwrite Logger类中的extra属性
logger = get_logger_prod('requestQualifier',
                         daily_handler=True,
                         level='debug',
                         log_fmt='%(asctime)s File \"%(filename)s\" [%(thread)d-%(reqId)s] %(levelname)s: %(message)s')
logger = LoggerAdapter(logger, extra={'reqId': 2333})
logger.info("我可以")
```

#### 4.2 多进程下日志打印

##### 4.2.1 多进程日志会有什么问题?

​       logging模块是线程安全的，但大多数python脚本都是cpu密集型运算。意味着在GIL机制下，python并不能有效利用多线程这种机制，需要开启多进程才能真正利用多核CPU。这一限制带来了许多问题，日志打印就是其中之一。

​        以 TimedRotatingFileHandler 这个类的问题作为例子。这个Handler本来的作用是：按天切割日志文件。（当天的文件是xxxx.log 昨天的文件是xxxx.log.2016-06-01）。这样的好处是，一来可以按天来查找日志，二来可以让日志文件不至于非常大, 过期日志也可以按天删除。在每一个日志stream进行打印的时候logger会进行判断，是否需要rotation。以按天rotation为例子，如果Process-1在00:01收到一条日志记录请求，会判断当前时间是否满足routation条件，即logger类的rolloverAt属性所代表的时间，如果满足条件就会进行rotation，所以你会发现被rotated的日志文件的最后修改时间是在rolloverAt之后的第一条日志请求的时间点。

​       阅读源码会发现，rotation的时候会先判断是否有目标文件，如果有则进行删除，然后重命名(没有rotater的情况下). 但是问题来了，如果是用多进程来输出日志，每个进程在何时收到日志请求并不确定。假设process1在00:00:01进行了rotation,  process2在00:01:01进行了rotation。最终结果会是process2删除了前一天所有的日志，并且把process1创建的当前日志文件重命名为昨天的时间戳，其日志内容为 process1 在00:00:01-00:01:00之间打印的日志内容。

关于其他实现，参考 https://www.jianshu.com/p/d615bf01e37b，但本实现并没有完美解决多进程日志问题，在多个进程同时进行rotation的时候会因为文件被锁无法重命名导致一系列问题。文中提到的加文件锁的方法，确实暂时没有找到同时可以在Window,Linux平台下同时可以实现的办法，且实现复杂。

##### 4.2.2 同一个主进程下多进程安全日志打印

总体思想是利用multiprocessing模块中的Queue进行进程间通讯，再利用一个独立的进程进行日志接受与打印工作，保证了日志的唯一性。功能同4.2类似

实现参考了官方logging文档进行了封装加工 https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes。

```python
from skBox.skLogger import get_sender_logger, log_listener
import multiprocessing
import time

class LogTest(object):
    def __init__(self, ilogger, process_no):
        self.logger = ilogger
        self.process_no = process_no

    def run_test(self):
        for i in range(100):
            self.logger.info("count %s, process %s" % (i, self.process_no))
            time.sleep(0.5)


def work_starter(queue, no):
    logger = get_sender_logger(queue, "test_worker")
    LT = LogTest(ilogger=logger, process_no=no)
    LT.run_test()


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    # 启动监听logger进程
    listener = multiprocessing.Process(target=log_listener,
                                       args=(queue, "test_listener"),
                                       kwargs={'log_dir': r'E:\code_work\skBox\temp\temp_log',                                                'daily_handler': True})
    listener.start()
    for i in range(3):
        p = multiprocessing.Process(target=work_starter, args=(queue, i, ))
        p.start()
```

##### 4.2.3 多个独立进程下的多进程日志打印

multiprocessing的队列对于多个独立进程下的日志打印就束手无策了，针对这个问题，写了一个在此种情况下安全的日志打印功能。

但由于用的是直接寻找当前输出文件目录的办法，无法进行原来logging模块意义上的rotation和压缩，因为每个进程不会去判断是否应该rotation,而是直接去正确的文件打印日志（不关心其他进程在干嘛）。如果对于日志压缩有需求，目前想到的优化是，单独做一个定时日志压缩的服务来解决这个问题。且本模块，目前只支持俺天进行日志分割（本质上不会进行分割). 日志会被记录到log_dir/name_log.current_date文件下

```python
from skBox.skLogger import get_save_daily_logger
logger = get_save_daily_logger(name, level='info', log_dir="/home/test/log", log_fmt=None)
logger.info("测试") # 在/home/test/log.{current_date} 文件下打印日志
```

#### 4.3 小小的计时器？

目前是个玩具功能，一个简单的装饰器来记录类下函数的运行时间。

```python
from skBox.skLogger import logger_time_it, get_logger_prod
import time

class Test(object):
    def __init__(self):
        self.logger = get_logger_prod("test_log")
        
    def my_test_func(self):
        time.sleep(20)

if __name__ == '__main__':  
    t = Test()
    t.my_test_func()
```

### 5. 杂项工具

一些常用的计算函数

```python
from skBox.Toolbox import *
```

#### 5.1 获得本机IP(内外网)

```python
ip = get_host_ip(inner=True)
```

#### 5.2 根据生日计算年龄

```python
# born为出生日期,字符串 yyyyMMdd、yyyy-MM-dd、yyyy/MM/dd
# 默认用当前时间计算年龄，也可输入end_date=datetime.today()，支持同上的字符串以及datetime格式
# 小于1周年=0岁
age = calculate_age(born)
```

#### 5.3 从二代身份证中抽取年龄和性别信息

首先会进行身份证合规性校验，如果不合规会返回None.

```python
IE = IdnExtractor()
age = IE.extract_age(card_no)
gender = IE.extract_gender(card_no) # 1男，女
```

#### 5.4 检查手机号合规性

如果合规返回手机号，不然返回空。可选在合规情况下返回运营商。目前可能会有覆盖不全的问题

```python
PC = PhoneCheck()
phone = PC.check(phone)
```

#### 5.5 根据时间起止与时间间隔创造时间列表

输入为字符串格式时间，开始和结束时间必须抱持格式一致。

```python
date_list = create_assist_date(datestart=None, dateend=None,
                               infmt='%Y-%m-%d', ofmt='%Y-%m-%d',
                               unit='days', interval=1):
```

#### 5.6 字符串全半角相互转换

```python
res = strQ2B(ister) # 全角转半角
res = strB2Q(ister) # 半角转全角
```

