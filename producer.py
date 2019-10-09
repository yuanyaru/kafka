# !/usr/bin/python
# -*- encoding:utf-8 -*-

import json
# pip2 install kafka-python
from kafka import KafkaProducer

# 生产者生产消息
producer = KafkaProducer(bootstrap_servers='192.168.100.71:9092')

msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test",
        "host": "192.168.100.71",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict)
producer.send('test', msg, partition=0)
producer.close()
