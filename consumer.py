# !/usr/bin/python
# -*- encoding:utf-8 -*-

from kafka import KafkaConsumer

# 消费者接收消息
consumer = KafkaConsumer('test', bootstrap_servers=['192.168.100.71:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print recv
