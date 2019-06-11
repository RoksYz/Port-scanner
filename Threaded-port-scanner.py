import socket
import threading
import time
from queue import Queue

print_lock = threading.Lock()

target = ''
#ip = socket.gethostbyname(target)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port)
        con.close()
    except:
        pass
# for that always change the numbers while compiling.

def threader():
    while True:
        worker = que.get()

        portscan(worker)

        que.task_done()

que = Queue()

for x in range(30):
    t = threading.Thread(target=threader)

    t.daemon= True

    t.start()

start =time.time()

for worker in range(1,100):
    que.put(worker)

que.join()
