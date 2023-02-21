#port scanner 
import socket
import threading
import queue

ip = '192.168.1.7'

q = queue.Queue()
for i in range(1000):
    q.put(i)

def scan():
    while not q.empty():
        port = q.get()
        with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
            try:
                s.connect(ip , port)
                print('port {} is open'.format(port))
            except:
                pass 
        q.task_done()
        
for i in range(30):
    t = threading.Thread(target=scan , daemon=True)
    t.start()
    
q.join()
print('finished')