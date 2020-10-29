
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

