### 安装条件
确保 zookeeper 已经安装成功。zookeeper 安装过程见：
https://github.com/yuanyaru/kafka/blob/master/install%20zookeeper%20in%20linux.md

1.下载 kafka 
进入Apache官网 [http://kafka.apache.org/downloads.html](http://kafka.apache.org/downloads.html) 选择版本进行下载

2.解压下载的 kafka
``` bash
mkdir /usr/local/kafka
tar zxvf kafka_2.11-2.3.0.tgz -C /usr/local/kafka/
```

3.启动服务

* 启动 zookeeper
启动zk有两种方式，第一种是使用 kafka 自己带的一个 zk。
``` bash
bin/zookeeper-server-start.sh  config/zookeeper.properties 
```
另一种是使用其它的 zookeeper ，可以位于本机也可以位于其它地址。

这种情况需要修改 config 下面的 server.properties 里面的 zookeeper 地址 。例如 zookeeper.connect=192.168.100.71:2181

成功启动 zookeeper 后才可以启动 kafka 。
* 启动 kafka
``` bash
 bin/kafka-server-start.sh config/server.properties
```

4.创建 topic
``` bash
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```
创建一个名为 test 的 topic ，只有一个副本，一个分区。

通过 list 命令查看刚刚创建的 topic
``` bash
bin/kafka-topics.sh -list -zookeeper localhost:2181
```

5.启动 producer 并发送消息
``` bash
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
```
启动之后就可以发送消息了

6.然后在另一个终端中，启动 consumer

以下是旧版本的命令：
``` bash
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning
```
报错：``` bash consumer zookeeper is not a recognized option ```
发现在启动的时候说使用 --zookeeper 是一个过时的方法，最新的版本中命令如下：
``` bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```
启动 consumer 之后就可以在 console 中看到 producer 发送的消息了

可以开启两个终端，一个发送消息，一个接受消息。
