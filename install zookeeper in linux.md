### 安装条件

想要安装zookeeper，必须先在linux中安装好jdk。安装步骤见：
[https://github.com/yuanyaru/cassandra/blob/master/install%20java%20and%20run%20a%20java%20code%20in%20linux.txt](https://github.com/yuanyaru/cassandra/blob/master/install%20java%20and%20run%20a%20java%20code%20in%20linux.txt)

### 下载并解压zookeeper压缩包

下载链接：
[http://mirror.bit.edu.cn/apache/zookeeper](http://mirror.bit.edu.cn/apache/zookeeper)

    mkdir -<span class="hljs-tag">p</span> /usr/local/zookeeper
    tar zxvf zookeeper-<span class="hljs-number">3.4</span>.<span class="hljs-number">14</span><span class="hljs-class">.tar</span><span class="hljs-class">.gz</span> -C /usr/local/zookeeper/
    `</pre>

    ### 编辑配置文件

1.  进入conf目录：<pre>`<span class="hljs-keyword">cd</span> zookeeper/zookeeper-<span class="hljs-number">3.4</span>.<span class="hljs-number">14</span>/<span class="hljs-keyword">conf</span>
    `</pre>
2.  将zoo_sample.cfg这个文件复制为zoo.cfg (必须是这个文件名)<pre>`cp zoo_sample<span class="hljs-class">.cfg</span> zoo.cfg
    `</pre>
3.  进入zoo.cfg文件进行编辑<pre>`vi zoo.cfg    dataDir=<span class="hljs-regexp">/tmp/</span>zookeeper/data
    dataLogDir=<span class="hljs-regexp">/tmp/</span>zookeeper/log
    `</pre>
4.  在tmp目录创建目录<pre>`<span class="hljs-keyword">mkdir</span> /tmp/zookeeper
    <span class="hljs-keyword">mkdir</span> /tmp/zookeeper/data
    <span class="hljs-keyword">mkdir</span> /tmp/zookeeper/<span class="hljs-keyword">log</span>
    `</pre>

    ### 配置环境变量

    <pre>`vi /etc/profile
    <span class="hljs-comment"># zookeeper</span>
    <span class="hljs-keyword">export</span> ZOOKEEPER_INSTALL=/usr/local/zookeeper-<span class="hljs-number">3.4</span>.<span class="hljs-number">14</span>
    <span class="hljs-keyword">export</span> PATH=<span class="hljs-variable">$PATH</span>:<span class="hljs-variable">$ZOOKEEPER_INSTALL</span>/bin
    `</pre>

    ### 启动zookeeper

    1.进入bin目录，并启动zookeep。

    <pre>`cd <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/zookeeper/</span>zookeeper-<span class="hljs-number">3.4</span>.<span class="hljs-number">14</span><span class="hljs-regexp">/bin/</span>
    .<span class="hljs-regexp">/zkServer.sh start</span>
    `</pre>

    2.启动成功效果如下：

    <pre>`ZooKeeper JMX enabled by <span class="hljs-keyword">default</span>
    Using <span class="hljs-string">config:</span> <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/zookeeper/</span>zookeeper-<span class="hljs-number">3.4</span><span class="hljs-number">.14</span><span class="hljs-regexp">/bin/</span>..<span class="hljs-regexp">/conf/</span>zoo.cfg
    Starting zookeeper ...STARTED
    `</pre>

    3.zookeeper的服务端启动后，还需要启动zookeeper的客户端：

    <pre>`./zkCli.<span class="hljs-keyword">sh</span>
    `</pre>

    启动成功效果如下：

    <pre>`Connecting to <span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>
    ......
    ......
    ......
    Welcome to ZooKeeper!
    <span class="hljs-number">2019</span>-<span class="hljs-number">09</span>-<span class="hljs-number">03</span> <span class="hljs-number">16</span>:<span class="hljs-number">41</span>:<span class="hljs-number">52</span>,<span class="hljs-number">978</span> [<span class="hljs-string">myid:</span>] - INFO  [main-SendThread(<span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>):ClientCnxn$SendThread@<span class="hljs-number">1025</span>] - Opening socket connection to server localhost/<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>:<span class="hljs-number">2181.</span> Will not attempt to authenticate using SASL (unknown error)
    JLine support is enabled
    <span class="hljs-number">2019</span>-<span class="hljs-number">09</span>-<span class="hljs-number">03</span> <span class="hljs-number">16</span>:<span class="hljs-number">41</span>:<span class="hljs-number">53</span>,<span class="hljs-number">074</span> [<span class="hljs-string">myid:</span>] - INFO  [main-SendThread(<span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>):ClientCnxn$SendThread@<span class="hljs-number">879</span>] - Socket connection established to localhost/<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>:<span class="hljs-number">2181</span>, initiating session
    <span class="hljs-number">2019</span>-<span class="hljs-number">09</span>-<span class="hljs-number">03</span> <span class="hljs-number">16</span>:<span class="hljs-number">41</span>:<span class="hljs-number">53</span>,<span class="hljs-number">117</span> [<span class="hljs-string">myid:</span>] - INFO  [main-SendThread(<span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>):ClientCnxn$SendThread@<span class="hljs-number">1299</span>] - Session establishment complete on server localhost/<span class="hljs-number">127.0</span><span class="hljs-number">.0</span><span class="hljs-number">.1</span>:<span class="hljs-number">2181</span>, sessionid = <span class="hljs-number">0x100015ef7930000</span>, negotiated timeout = <span class="hljs-number">30000</span>
    <span class="hljs-label">
    WATCHER:</span>:

    WatchedEvent <span class="hljs-string">state:</span>SyncConnected <span class="hljs-string">type:</span>None <span class="hljs-string">path:</span><span class="hljs-literal">null</span>
    [<span class="hljs-string">zk:</span> <span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>(CONNECTED) <span class="hljs-number">0</span>]
    `</pre>

    4.查看状态

    <pre>`./zkServer.sh status
    ZooKeeper JMX enabled by <span class="hljs-keyword">default</span>
    Using <span class="hljs-string">config:</span> <span class="hljs-regexp">/usr/</span>local<span class="hljs-regexp">/zookeeper/</span>zookeeper-<span class="hljs-number">3.4</span><span class="hljs-number">.14</span><span class="hljs-regexp">/bin/</span>..<span class="hljs-regexp">/conf/</span>zoo.cfg
    <span class="hljs-string">Mode:</span> standalone
    `</pre>

    遇到问题怎么解决？

    zookeeper的出错日志会记录在 zookeeper.out。

    当前处于哪个目录，执行完zkServer.sh start命令， zookeeper.out就会写在哪个目录。

    vim zookeeper.out 可以查看报错信息。然后再搜索解决。

    ### zookeeper使用

    通过 ./zkCli.sh 进入客户端后，就可以使用命令来操作zookeeper了。
    1.创建节点

    使用create命令，可以创建一个zookeeper节点。

    create [-s]   [-e]  path  data  acl

    其中-s表示顺序节点，-e表示临时节点。默认情况下，创建的是持久节点。

    path是节点路径，data是节点数据，acl是用来进行权限控制的。

    如下：

    创建一个叫做/zk-test的节点，内容是"yyr-123"

    <pre>`<span class="hljs-list">[<span class="hljs-keyword">zk:</span> localhost:2181<span class="hljs-list">(<span class="hljs-keyword">CONNECTED</span>)</span> <span class="hljs-number">0</span>] create /zk-test yyr-123

    Created /zk-test</span>
    `</pre>

    创建/zk-test的子节点yuan，内容是"yyr-123-456"

    <pre>`[<span class="hljs-string">zk:</span> <span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>(CONNECTED) <span class="hljs-number">1</span>] create <span class="hljs-regexp">/zk-test/</span>yuan yyr-<span class="hljs-number">123</span>-<span class="hljs-number">456</span>

    Created <span class="hljs-regexp">/zk-test/</span>yuan
    `</pre>

    2.查看节点内容

    使用get命令，可以获取zookeeper指定节点的内容和属性信息。

    如下：

    <pre>`[zk: localhost:2181(CONNECTED) 2] get /zk-test
    yyr-123
    <span class="hljs-constant">cZxid</span> = 0x2
    <span class="hljs-constant">ctime</span> = Tue Sep 03 16:45:42 CST 2019
    <span class="hljs-constant">mZxid</span> = 0x2
    <span class="hljs-constant">mtime</span> = Tue Sep 03 16:45:42 CST 2019
    <span class="hljs-constant">pZxid</span> = 0x3
    <span class="hljs-constant">cversion</span> = 1
    <span class="hljs-constant">dataVersion</span> = 0
    <span class="hljs-constant">aclVersion</span> = 0
    <span class="hljs-constant">ephemeralOwner</span> = 0x0
    <span class="hljs-constant">dataLength</span> = 7
    <span class="hljs-constant">numChildren</span> = 1
    `</pre>

    3.查看子节点

    使用ls命令可以查看指定节点下的所有子节点

    以下查看根目录下的所有子节点：

    <pre>`<span class="hljs-list">[<span class="hljs-keyword">zk:</span> localhost:2181<span class="hljs-list">(<span class="hljs-keyword">CONNECTED</span>)</span> <span class="hljs-number">4</span>] ls /

    <span class="hljs-list">[<span class="hljs-keyword">zk-test</span>, zookeeper]</span></span>
    `</pre>

    查看zk-test节点的子节点：

    <pre>`<span class="hljs-list">[<span class="hljs-keyword">zk:</span> localhost:2181<span class="hljs-list">(<span class="hljs-keyword">CONNECTED</span>)</span> <span class="hljs-number">5</span>] ls /zk-test

    <span class="hljs-list">[<span class="hljs-keyword">yuan</span>]</span></span>
    `</pre>

    4.更新节点内容

    使用set命令，更新节点内容。格式为：

    set   path  data 

    其中的data就是要更新的新内容。

    <pre>`[zk: localhost:2181(CONNECTED) 6] set /zk-test yyr-321
    <span class="hljs-constant">cZxid</span> = 0x2
    <span class="hljs-constant">ctime</span> = Tue Sep 03 16:45:42 CST 2019
    <span class="hljs-constant">mZxid</span> = 0x4
    <span class="hljs-constant">mtime</span> = Tue Sep 03 16:53:10 CST 2019
    <span class="hljs-constant">pZxid</span> = 0x3
    <span class="hljs-constant">cversion</span> = 1
    <span class="hljs-constant">dataVersion</span> = 1
    <span class="hljs-constant">aclVersion</span> = 0
    <span class="hljs-constant">ephemeralOwner</span> = 0x0
    <span class="hljs-constant">dataLength</span> = 7
    <span class="hljs-constant">numChildren</span> = 1
    `</pre>

    在输出的信息中，可以发现，dataVersion的值由原来的 0 变成了 1 ，这是因为刚才的更新操作导致该节点的数据版本也发生变更。

    6.删除节点

    使用delete命令来删除节点，如下：

    <pre>`[<span class="hljs-string">zk:</span> <span class="hljs-string">localhost:</span><span class="hljs-number">2181</span>(CONNECTED) <span class="hljs-number">7</span>] delete /zk-test

    Node not <span class="hljs-string">empty:</span> /zk-test
    `</pre>

    可以发现，一个节点存在子节点时，无法删除该节点。

    先删除子节点/zk-test/yuan，再删除父节点，如下：

    <pre>`<span class="hljs-list">[<span class="hljs-keyword">zk:</span> localhost:2181<span class="hljs-list">(<span class="hljs-keyword">CONNECTED</span>)</span> <span class="hljs-number">8</span>] delete /zk-test/yuan
    <span class="hljs-list">[<span class="hljs-keyword">zk:</span> localhost:2181<span class="hljs-list">(<span class="hljs-keyword">CONNECTED</span>)</span> <span class="hljs-number">9</span>] delete /zk-test     
    <span class="hljs-list">[<span class="hljs-keyword">zk:</span> localhost:2181<span class="hljs-list">(<span class="hljs-keyword">CONNECTED</span>)</span> <span class="hljs-number">10</span>] ls /
    <span class="hljs-list">[<span class="hljs-keyword">zookeeper</span>]</span></span></span></span>

删除成功。