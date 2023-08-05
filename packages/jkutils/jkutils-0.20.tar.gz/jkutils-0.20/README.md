# 介绍

常用工具整理

* 统一的 JSON 日志输出方式的 Logger
* 环境变量、zk 配置读取 (需要 kazoo==2.5.0 库)
* 通过服务名称获取服务地址 (需要 requests==2.19.1 库)
* 服务告警 (需要 requests 库)
* 生成业务流水号
* rabbit MQ 消息推送 (需要 pika==1.1.0)
* kafka 消息推送 (需要 kafka-python==1.4.4)

# 日志

``` python
from jkutils.logger import JKLogger

logger = JKLogger("jk_utils")

logger.debug("debug")
logger.info("info")
# 设置默认字段，后面的log都会带上默认字段
logger.set_default_fields(log_id=logger.log_id, default_id="000000000")
logger.warning("warning")
logger.warn("warn")
logger.error("error")
# 移除默认字段 可以传任意个 key
logger.remove_default_field("default_id", "test_id")
logger.critical("critical")
# 带上额外字段
logger.info("dict", uid=123, phone="12774147414")
# 移除所有默认字段
logger.remove_default_all_fields()
logging.info("logging info")

```

在 **flask** 中使用时，如果你设置的默认字段生命周期只在同一次请求时，请在创建对象时设置 `default_fileds_obj` 为：

``` python
from jkutils.logger import JKLogger, FlaskGStorage
logger = JKLogger("jk_utils", default_fileds_obj=FlaskGStorage())

```

在 **多线程** 中使用时，如果你设置的默认字段生命周期只在同一线程内时，请在创建对象时设置 `default_fileds_obj` 为：

``` python
from jkutils.logger import JKLogger, ThreadLocalStorage
logger = JKLogger("jk_utils", default_fileds_obj=ThreadLocalStorage())

```

结果类似

``` json
{"msg": "info", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:12", "level": "INFO", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
{"log_id": "48c1fc3068d748fa9b100f68d679cf3e", "default_id": "000000000", "msg": "warning", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:14", "level": "WARNING", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
{"log_id": "48c1fc3068d748fa9b100f68d679cf3e", "default_id": "000000000", "msg": "warn", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:15", "level": "WARNING", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
{"log_id": "48c1fc3068d748fa9b100f68d679cf3e", "default_id": "000000000", "msg": "error", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:16", "level": "ERROR", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
{"log_id": "48c1fc3068d748fa9b100f68d679cf3e", "msg": "critical", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:18", "level": "CRITICAL", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
{"uid": 123, "phone": "12774147414", "log_id": "48c1fc3068d748fa9b100f68d679cf3e", "msg": "dict", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:19", "level": "INFO", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
{"msg": "logging info", "funcname": "test_log", "file": "/home/jianshijiuyou/python_code/xwjk-base/tests/test_log.py:21", "level": "INFO", "project": "jk_utils", "time": "2019-03-03 11:26:37"}
```

注意原生 `logging` 也被修改了的，如果不需要

``` python
logger = JKLogger("jk_utils", native=False)
```

设置日志级别、时间格式

``` python
logger = JKLogger("jk_utils", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S", native=True)

```

# 读取环境变量/zk（<=0.11）

``` python
from jkutils.env import EnvZk

ez = EnvZk("111.230.231.xx:port,111.230.231.xx:port,111.230.231.xx:port", "server_name", "服务注册地址")

CUR_ENV = ez.init_conf("CUR_ENV", force=True)
CHAOS_DB = ez.init_conf("test_bool",default="true", conftype=bool, force=False)

# init_conf 的签名为
# def init_conf(self, name, default=None, conftype=None,
#               force=False, hash_log=None):


```

# 读取环境变量/zk（>=0.14）
``` python
from jkutils.env import EnvZk

ez = env_zk = EnvZk(zk_servers=conf_servers, service_name=service_name,config_path="/entry/config/service")

# init_conf 的签名为
# def init_conf(self, name, default=None, conftype=None,
#               force=False, hash_log=None):


```


以上是初始化获取参数的方式

还可以动态获取参数，但是动态获取的参数必须是之前初始化过的

``` python
report_exc_url =  ez["REPORT_EXC_URL"]
```

参数读取顺序为

```
读取顺序: 环境变量 > zk > default
```

## 监听配置变化

``` python
def test(config):
    print(config)

ez = EnvZk(...)
ez.add_listener(test)
# 添加多个监听器请设置 key
ez.add_listener(test, key="other")
# 删除监听器只需要将对应 key 的 func 设置为 None
ez.add_listener(None)
# or
ez.add_listener(None, key="other")
```

# 获取服务地址

``` python
from jkutils.get_host_ip import get_host_ip

chaos_host = get_host_ip(url, "chaos")

```

# 服务告警

``` python
from jkutils.report_exception import AbnormalReport

ar = AbnormalReport("chaos", "bank", report_url)
# 设置告警级别 code
ar.set_err_code(1001, 1002, 1003)

# 告警
ar.report("title", "出 bug 啦～～～")
```

支持参数

``` python
AbnormalReport(project_name, env_flag, url=None, timeout=15):

report(self, title, content, cid=AbnormalReport.GENERAL_ERROR):
```

# 获取当前 git commit id（如果存在）

``` python
from jkutils.git import git_revision_hash
commit_id = git_revision_hash()
```

# 生成业务流水号

``` python
from jkutils.env import EnvZk
from jkutils.ids import serial_number

ez = EnvZk("127.0.0.1:2181", "chaos", "localhost:12345")
# ez.zk_node_number 获取 zk node 节点名称后 7 位数字
sn = serial_number("1020", ez.zk_node_number, "00001")
print("=====sn=======", sn) # 10200000012000013178922453168129
```

# rabbit MQ 消息推送

``` python
from jkutils.rabbitmq import MQPublisher

p = MQPublisher("amqp://xxx:xxx@127.0.0.1:111/")
p.publish(exchange="test", exchange_type="topic", durable=True, routing_key="teddy", msg="xxx",properties={"delivery_mode":2})

```

# rabbit MQ Topic消息消费者

``` python
from jkutils.rabbitmq import MqConsumer
from pika.channel import Channel

def call(ch: Channel, method, properties, body):
    """接收到消息后回调方法"""
    print("{}:{}:{}:{}".format(ch, method.routing_key, properties, body))

def mq_error_func(msg):
    """消费发生异常时候回调方法[用途：告警or失败处理]"""
    print("[call]:{}".format(msg))

p = MqConsumer("amqp://guest:guest@127.0.0.1:5672/", mq_error_func)
p.topic_consumer(
    exchange="test_topic",
    queue_name="test",
    callback=call_backic_ack,
    binding_key="a.*",
    exception_sleep_time=5,
    prefetch_count=1,
    auto_ack=False,
    arguments={
        "x-dead-letter-exchange": "test_topic",
        "x-dead-letter-routing-key": "a.*",
        "x-message-ttl": 1 * 1000,
    },
)
```

# jkkafka

## kafka消息推送
``` python
from jkutils.jkafka import JKKafka

kafka_server = "127.0.0.1:9092"

client = JKKafka(bootstrap_servers=kafka_server)
res = client.send(topic_name="public_to_elk_dev", data="{}".encode("utf-8"))
```

## kafka消息消费
``` python
from kafka.consumer.fetcher import ConsumerRecord

from jkutils.jkafka import JKkafkaConsumer

def callback_func(msg: ConsumerRecord):
    print(f"[callback]:{msg.value}")


def mq_error_func(msg: ConsumerRecord):
    print(f"[mq_error_func]:{msg.offset}")

kafka_server = "127.0.0.1:9092"

consumer = JKkafkaConsumer(kafka_server, "test-001", mq_error_func)
consumer.subscribe(["test"])
consumer.consume_data(callback_func)
consumer.close()
```


# jk_decrypt.py 金科核心接口加解密（私钥加密公钥解密方式）
```
    a = CoreCrypt()
    body = {"data": {'certType': '01',
                     'certNo': '522623198706237606',
                     'address': '云南省曲靖市南苑小区',
                     'custName': '李明',
                     'loanAmount': '1000000',
                     'mobile': '18623451234',
                     'creditLimit': '1000000',
                     'businessNo': '10080000353100873225489139797243',
                     'applyNo': '6b2879e627cb11eaac87787b8ae13052',
                     'register_mobile': '18623451234'
                     },
            "mchtNo": "00000000",
            "version": "1.0",
            "reqTime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            }
    new_body = a.run(body, "data", "./sn_test_encrypt.pem")
    print(new_body)
    # 解密 私钥解密
    res = {"returnCode": "0", "returnMsg": "成功", "respTime": "2019-12-31 16:55:00",
           "sign": "OGJjZjYzZTI4ZTYzNjVjZGM2NDJkZTM4OTI3MjkyZjAxY2FkMzhiYTM2ZWEwZTBiZjM4MGVmYmRhY2M0ZDIyZQ==",
           "data": "X+KM6s3r+tJq7PiUDO7YSnBkVzXamF9BGIAueVkXSBs1XiZWNkYHeYmWNOOePk+X",
           "randomKey": "dl8UuU15g9FNOmNf4s021ulenEmIu0MkOemxhhoFmhB6rxkfi25KnJdZ8dA4UWUBsMFLNWQsIV54l7GdPr+AtyV8M0wX3N7+iSK/SFPQchWMreSo0w6xRXBOFEUcge03pA6BkKPX2M7vcA5UNKEtSZ0P/BgqmV5VawypjFD5DscuCaflpxggyS+dtmu+aKH8EMIU3OXykZqyqvONCP5sA7HnpT6z8Z5Eiw5UvmzTln/SevC7LJxM5RUoUrvN3MnIzgUR8ugwv1rJghQcemtf0L8UHMnZrS8r1RMl2EqTEKQ80JrvUUk+hK2Hmfq6vimL39l8bgAKY20uih++njQfEg=="}
    a = CoreCrypt()
    data = a.decrypt_private("./sn_test_encrypt.pem", res["randomKey"], res["data"], res["sign"], res)
    print(data)
    
    # 解密 公钥解密
    res = {"returnCode": "0", "returnMsg": "成功", "respTime": "2019-12-31 16:56:11",
           "sign": "NDY4NjliYzRhNGY4MjhmNDJlNzBiMDJiMDc2YWRjMGNhYWFhNWRlNmI1OTI1OWMyYTY4MWQzYjg4NWMxMjMzZQ==",
           "data": "K2A1+yf0JXXjGhyT5RfeyRD+cYEjbMHXv0OcmYo9UEQJB9MKXEA8iRhobm19iEE3",
           "randomKey": "W2UhXxG9qzU12aRUbXR/q04TaFQPrs4pUzJFm1kcMvIGxnnDBQoyCfX67CcUChKmdtrb2hoKYARl9hZLjPWkt/VxRqxzAuo+tdlyJcEzzy+wgfWjzgfQRiWzMDh2tVLkgXsamgr1s7IX4MsyPmrO6SaCY7Iq0GSoj9NLhIm44JZT0g/AKjygaLLgLLFmqdM8CcpXpf8CuMfu9OTRz42RFNl2MpuLjiLkT0Mwd7vVmNXell2+flj8O5Xn2uNRqMrfYEJRJJBZtip/CL2UcqfNT52YSBEPTB8j+abOl6YGBQPRkeaqhOlHRW5i6WYvTcJk7MrTiSI7AkhLnC+pmfQw8g=="}
    a = CoreCrypt()
    data = a.decrypt_public("./sn_test_public.pem", res["randomKey"], res["data"], res["sign"], res)
    print(data)
```