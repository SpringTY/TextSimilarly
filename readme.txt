# 部署相关
#### 数据库结构 textsimilarity.sql
#### docker启动相关 redis.sh mysql.sh
#### 在docker 启动相关的错误
1.运行失败,找不到镜像(image),更改sh文件中的镜像名为你的镜像名字
2.运行后自动退出,采用docker logs <containername> 查看你容器的日志,会提示原因,
    常见的原因有挂载目录结构与虚拟环境中所期待的不同(如mysql中少一个conf.d文件夹)
请查阅相关文档.
#### mysql用户创建,并授予远程访问权限
create user 'similarity'@'%' identified by 'similarity@insis.bjtu';
grant ALL ON textsimilarity.* TO 'similarity'@'%'
#### conda相关命令
创建环境(若存在不需要创建):conda create -n Django3 python=3.6.2
激活环境:source activate Django3
安装依赖:pip install -r requirements.txt
注意:在安装pymysql的时候可能会报错,因此需要删除requirements中的mysql相关,手动安装
注意:如果conda命令找不到,则需要配置一下anaconda环境变量在个人目录下的.profile
注意:linux 环境变量是用:分割,
例如:ANACONDA_PATH=/.../bin
export PATH="$PATH:$ANACONDA_PATH"
#### 启动
python manager.py runserver 0.0.0.0:8001
注意:127.0.0.1是本地访问,要让局域网内其他人能够访问 设置成回路(0.0.0.0)


# 由于客户端断开连接，所以任务执行完成没法相应，服务器报错
不影响使用，如果需要改进，则需要MQ进行异步处理数据
----------------------------------------
Exception happened during processing of request from ('127.0.0.1', 52788)
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\socketserver.py", line 650, in process_request_thread
    self.finish_request(request, client_address)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\socketserver.py", line 360, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\socketserver.py", line 720, in __init__
    self.handle()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\servers\basehttp.py", line 174, in handle
    self.handle_one_request()
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\site-packages\django\core\servers\basehttp.py", line 182, in handle_one_request
    self.raw_requestline = self.rfile.readline(65537)
  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python37\lib\socket.py", line 589, in readinto
    return self._sock.recv_into(b)
ConnectionAbortedError: [WinError 10053] 你的主机中的软件中止了一个已建立的连接。

