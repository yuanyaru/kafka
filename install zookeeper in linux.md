### 安装条件
想要安装 zookeeper ，必须先在 linux 中安装好 jdk 。安装步骤见：
[https://github.com/yuanyaru/cassandra/blob/master/install%20java%20and%20run%20a%20java%20code%20in%20linux.txt](https://github.com/yuanyaru/cassandra/blob/master/install%20java%20and%20run%20a%20java%20code%20in%20linux.txt)

### 下载并解压 zookeeper 压缩包
下载链接：
[http://mirror.bit.edu.cn/apache/zookeeper](http://mirror.bit.edu.cn/apache/zookeeper)
``` bash
mkdir -p /usr/local/zookeeper
tar zxvf zookeeper-3.4.14.tar.gz -C /usr/local/zookeeper/
```

### 编辑配置文件
1.  进入 conf 目录：
``` bash
cd zookeeper/zookeeper-3.4.14/conf
```
2.  将 zoo_sample.cfg 这个文件复制为 zoo.cfg (必须是这个文件名)
``` bash
cp zoo_sample.cfg zoo.cfg
```
3.  进入 zoo.cfg 文件进行编辑
``` bash
vi zoo.cfg   
dataDir=/tmp/zookeeper/data
dataLogDir=/tmp/zookeeper/log
```
4.  在 tmp 目录创建目录
``` bash
mkdir /tmp/zookeeper
mkdir /tmp/zookeeper/data
mkdir /tmp/zookeeper/log
```

### 配置环境变量
``` bash
vi /etc/profile
# zookeeper
export ZOOKEEPER_INSTALL=/usr/local/zookeeper-3.4.14
export PATH=$PATH:$ZOOKEEPER_INSTALL/bin
```

### 启动 zookeeper
1.进入 bin 目录，并启动 zookeep。
``` bash
cd /usr/local/zookeeper/zookeeper-3.4.14/bin/
./zkServer.sh start
# 其他常用操作
./zkServer.sh stop
./zkServer.sh restart
```
启动成功效果如下：
``` bash
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/zookeeper-3.4.14/bin/../conf/zoo.cfg
Starting zookeeper ...STARTED
```
2.zookeeper 的服务端启动后，还需要启动 zookeeper 的客户端：
``` bash
./zkCli.sh
```
启动成功效果如下：
``` bash
Connecting to localhost:2181
......
......
......
Welcome to ZooKeeper!
2019-09-04 09:48:49,079 [myid:] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1025] - Opening socket connection to server localhost/127.0.0.1:2181. Will not attempt to authenticate using SASL (unknown error)
JLine support is enabled
2019-09-04 09:48:49,173 [myid:] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@879] - Socket connection established to localhost/127.0.0.1:2181, initiating session
2019-09-04 09:48:49,190 [myid:] - INFO  [main-SendThread(localhost:2181):ClientCnxn$SendThread@1299] - Session establishment complete on server localhost/127.0.0.1:2181, sessionid = 0x100015ef7930001, negotiated timeout = 30000

WATCHER::

WatchedEvent state:SyncConnected type:None path:null
[zk: localhost:2181(CONNECTED) 0]
```
3.查看状态
``` bash
./zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/zookeeper-3.4.14/bin/../conf/zoo.cfg
Mode: standalone
```
遇到问题怎么解决？
* zookeeper 的出错日志会记录在 zookeeper.out。
* 当前处于哪个目录，执行完 zkServer.sh start 命令， zookeeper.out 就会写在哪个目录。
* vi zookeeper.out 可以查看报错信息。然后再搜索解决。

例如：这是一个端口占用，导致 zookeeper 启动失败的问题
``` bash
[root@kube-node1 bin]# ./zkServer.sh status
ZooKeeper JMX enabled by default
Using config: /usr/local/zookeeper/zookeeper-3.4.14/bin/../conf/zoo.cfg
Error contacting service. It is probably not running.
[root@kube-node1 bin]# netstat -apn | grep 2181
tcp        0      0 0.0.0.0:2181            0.0.0.0:*               LISTEN      15274/java          
[root@kube-node1 bin]# kill 15274
[root@kube-node1 bin]# ./zkServer.sh restart
```

### zookeeper 使用
通过 ./zkCli.sh 进入客户端后，就可以使用命令来操作zookeeper了。

1.创建节点

使用 create 命令，可以创建一个 zookeeper 节点。

create [-s]   [-e]  path  data  acl

其中 -s 表示顺序节点，-e 表示临时节点。默认情况下，创建的是持久节点。

path是节点路径，data 是节点数据，acl 是用来进行权限控制的。

如下：

创建一个叫做 /zk-test 的节点，内容是 "yyr-123"
``` bash
[zk: localhost:2181(CONNECTED) 0] create /zk-test yyr-123
Created /zk-test
```
创建 /zk-test 的子节点 yuan，内容是 "yyr-123-456"
``` bash
[zk: localhost:2181(CONNECTED) 1] create /zk-test/yuan yyr-123-456
Created /zk-test/yuan
```
2.查看节点内容

使用 get 命令，可以获取 zookeeper 指定节点的内容和属性信息。

如下：
``` bash
[zk: localhost:2181(CONNECTED) 2] get /zk-test
yyr-123
cZxid = 0x2
ctime = Tue Sep 03 16:45:42 CST 2019
mZxid = 0x2
mtime = Tue Sep 03 16:45:42 CST 2019
pZxid = 0x3
cversion = 1
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 7
numChildren = 1
```
3.查看子节点

使用 ls 命令可以查看指定节点下的所有子节点

下查看根目录下的所有子节点：
``` bash
[zk: localhost:2181(CONNECTED) 4] ls /
[zk-test, zookeeper]
```
查看zk-test节点的子节点：
``` bash
[zk: localhost:2181(CONNECTED) 5] ls /zk-test
[yuan]
```
4.更新节点内容

使用 set 命令，更新节点内容。格式为：

set   path  data 

其中的 data 就是要更新的新内容。
``` bash
[zk: localhost:2181(CONNECTED) 6] set /zk-test yyr-321
cZxid = 0x2
ctime = Tue Sep 03 16:45:42 CST 2019
mZxid = 0x4
mtime = Tue Sep 03 16:53:10 CST 2019
pZxid = 0x3
cversion = 1
dataVersion = 1
aclVersion = 0
ephemeralOwner = 0x0
dataLength = 7
numChildren = 1
```
在输出的信息中，可以发现，dataVersion 的值由原来的 0 变成了 1 ，这是因为刚才的更新操作导致该节点的数据版本也发生变更。

6.删除节点

使用 delete 命令来删除节点，如下：
``` bash
[zk: localhost:2181(CONNECTED) 7] delete /zk-test
Node not empty: /zk-test
```
可以发现，一个节点存在子节点时，无法删除该节点。

先删除子节点 /zk-test/yuan ，再删除父节点，如下：
``` bash
[zk: localhost:2181(CONNECTED) 8] delete /zk-test/yuan
[zk: localhost:2181(CONNECTED) 9] delete /zk-test     
[zk: localhost:2181(CONNECTED) 10] ls /
[zookeeper]
```
删除成功。