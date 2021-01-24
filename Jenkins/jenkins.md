+ 相关配置

  + 安装openjdk

  + 生成ssh key, 

    ```
    ssh-keygen -t rsa -P ''
    ```

  + 用ssh-copy-id将ssh key命令复制到其他机子

    ```
    ssh-copy-id root@spider-003
    ```

  + 安装与开发环境版本一致的nodejs, 参考 [Centos7 安装Nodejs](https://www.jianshu.com/p/7d3f3fa056e8)

  + 安装与开发环境版本一致的python, 使用miniconda, pip源改成清华, 并且软连接到`/usr/bin/python3` 和 `/usr/bin/pip3`, 并根据项目创建不同的虚拟环境

  + github项目上

    ```
    setting -- Webhooks -- Add webhook
    Payload URL: 填入: http://39.104.123.143:7777/github-webhook/  
    Content type: 选择 application/json
    点击 Add webhook
    跳转后的页面出现绿色对号说明配置成功
    ```
    
    
    
    

+ 安装并配置, 参考 [CentOS 7 安装 Jenkins](https://www.cnblogs.com/stulzq/p/9291237.html)

  + 找到最新版本的rpm文件, `https://pkg.jenkins.io/`

  + 下载并安装

    ```
    wget https://pkg.jenkins.io/redhat-stable/jenkins-2.164.1-1.1.noarch.rpm
    rpm -ivh jenkins-2.164.1-1.1.noarch.rpm
    ```

  + 配置文件

    ```
    vim /etc/sysconfig/jenkins
    修改jenkins的home文件夹
    ```

  + 修改权限

    ```
    /etc/sysconfig/jenkins #配置文件中
    ENKINS_USER="root"
    # 修改文件夹的权限
    chown -R root:root /var/cache/jenkins
    chown -R root:root /var/log/jenkins
    
    ```

  + 启动

    ```
    service jenkins start
    ```

+ 浏览器登录`http://server:8080` , 根据提示一步一步进行, 最后是生成管理员账号

+ 配置邮箱通知

  ```
  系统管理 -- 系统设置 -- Jenkins Location
  ```

  ```
  系统管理员邮件地址: 填入相应管理员的邮箱地址, 这个邮箱与下面填写的smtp的服务器的一致
  ```

  ```
  系统管理 -- 系统设置 -- 邮件通知
  ```

  ```
  SMTP服务器: smtp.163.com
  用户默认邮件后缀: 	
  使用SMTP认证: 勾选
  用户名: boeing737
  密码: 163邮箱的客户端授权码
  使用SSL协议: 勾选
  SMTP端口: 465
  通过发送测试邮件测试配置: 勾选,
  Test e-mail recipient: 随便输入一个邮箱地址
  Test configuration: 点击 后, 查看邮箱是否能够收到测试邮件
  ```

  

+ 安装ssh并配置所有需要部署的服务器的ssh remote参数

  ```
  系统管理 -- 插件管理 -- 可选插件
  ```

  搜索 `ssh` 勾选后直接安装

  ```
  系统管理 -- 系统设置 -- SSH remote hosts
  ```

  点击 `新增` , 

  ```
  hostname填入相应的ip, 
  port 填入22
  Credentials 点击添加, 弹出窗口, 类型选择 SSH Username with private key
                  id 填入 类似 ssh-spider-003
                  描述 填入 ssh登录spider-003的凭证
                  username 填入root
                  勾选Private Key, 填入前面生成的本机的ssh Private Key.
                  点击添加
  			选择刚刚生成的ssh凭证
  点击 Check connection, 验证是否能 connection 成功
  ```

  点击 最下面的 `保存`

+ 安装git插件并配置git服务器

  ```
  系统管理 -- 插件管理 -- 可选插件
  搜索 git 勾选后直接安装
  ```

  ```
  系统管理 -- 系统设置 -- Github 服务器	
  ```

  点击 `添加 Github 服务器`

  ```
  名称: 填入个人姓名
  凭据: 点击添加, 在弹出的窗口中, 类型选择 Select text, 
           Secret: 填入 前面github生成的token
           ID: 填入 github-token-姓名拼音
           描述: 填入 具体姓名的github的token
           点击添加
       选择刚刚生成的github凭证
  勾选`管理 Hook`
  ```

  点击 最下面的 `保存`

+ 非必须, 安装node插件并配置node命令执行路径, 参考 [Jenkins使用NodeJS插件完成Vue的可持续集成](https://www.chenchen.org/2018/01/16/Jenkins_NodeJs_Vue_CI.html)

  ```
  系统管理 -- 插件管理 -- 可选插件
  搜索 nodejs 勾选后直接安装
  ```

  ```
  系统管理 -- 全局工具配置 -- NodeJS
  ```

  点击`新增 NodeJS`

  ```
  别名: 填入 nodejs
  勾选 自动安装
  version 选择 前面 安装的版本, 也就是与开发环境相同的版本
  ```

  点击 最下面的 `保存`

+ 安装python插件并配置python命令的执行路径

  ```
  
  ```

+ 新建任务并构建

  + 创建任务

    ```
    新建任务
    填入任务名称
    选择 构建一个自由风格的软件项目
    点击确定
    ```

  + 配置任务

    ```
    通用:
        描述: 填入相应的描述
        勾选 github, 
        项目url: 填入 类似 https://github.com/playbear/Jenkins
    源码管理:
    	勾选 git
    	Repository URL: 填入类似 https://github.com/playbear/Jenkins.git
    	Credentials: 点击 添加, 弹出的窗口中, 
    						类型: Username with password
    						用户名和密码: 填入github的用户名和密码
    						ID: github-姓名拼音
    						描述: 具体姓名的github的用户名和密码凭证
    						点击添加
    				 选择刚刚添加的github凭证
    构建触发器:
    	勾选 GitHub hook trigger for GITScm polling
    	勾选 轮询SCM 设置为 H/2 * * * * 
    		表示: 每两分钟轮询一次仓库代码是否变更
        
    构建环境:
    	勾选 Execute shell script on remote host using ssh
    		SSH site: 选择要部署机子的ip和端口
            Post build script: 如果是前端html, 填入 nginx -s reload
            				   如果是后端, 填入 supervisorctl restart xxproject
    构建:
    	点击 增加构建步骤, 选择 执行 shell
    		命令: 如果是前端填入
    			 
    			 npm config set registry https://registry.npm.taobao.org &&
                 npm install &&
                 rm -rf dist &&
                 npm run build &&
                 rsync -azI --delete dist/ root@172.24.42.202:/usr/share/nginx/html	
                 如果是后端填入
    		     rsync -azI --delete ./ spider@172.24.42.201:/home/spider/jenkins
    		     # rsync 远程同步删除文件时候, 不能用./* 这种方法表示同步本地文件夹
    		     	-a 表示 -rlptgoD, -r: 递归, -l: 软连接, -p: 保持权限, -t: 只能源和目标文				  件匹配, -g: 保持文件的组属性 -o: 保持文件的ower属性, -D: 保持设备文件的信息
    ```

    点击 最下面的 `保存`

    点击左侧的`立即构建` 检查是否构建部署成功.

    rsync 参考 [rsync 的使用方法](https://segmentfault.com/a/1190000015669114), [使用rsync同步目录](https://www.cnblogs.com/MikeZhang/p/rsyncExample_20160818.html), [关于Rsync的一点经验](http://gunner.me/archives/439)

+ python 项目 构建的 shell 语法

  ```
  export PATH=/root/miniconda3/bin:$PATH &&
  #source activate mark-test &&
  #pip install -r requirement.txt &&
  #pip install mock nose coverage &&
  nosetests --with-xunit --all-modules --traverse-namespace --with-coverage --cover-inclusive && coverage xml &&
  rsync -azI --delete -exclude=coverage.xml -exclude=nosetests.xml ./ spider@172.24.42.201:/home/spider/jenkins
  ```

+ js项目 构建的shell语法

  ```
  export PATH=/opt/node-v10.12.0-linux-x64/bin:$PATH
  npm config set registry https://registry.npm.taobao.org &&
  npm install &&
  rm -rf dist &&
  npm run build &&
  rsync -azI --delete  ./dist/ root@172.24.42.202:/usr/share/nginx/html/
  ```

+ 生产环境的项目,自动部署, 不自动启动

+ 测试环境的项目, 自动部署, 并设置自动启动

  























