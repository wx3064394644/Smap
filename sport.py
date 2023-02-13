import socket
import threading
import time
import os

os.system('cd logo  &&  logo.py')

def scan_port(host,port):
    sk = socket.socket()
    sk.settimeout(0.5)
    conn_result = sk.connect_ex((host, port))
    if conn_result == 0:
        print(f'{port} is open')
    sk.close()

start_time = time.time()
host = input('输入ip:')
thread_list = []
for port in range(0, 65536):
    t = threading.Thread(target=scan_port, args=(host, port))
    thread_list.append(t)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

end_time = time.time()
print(f'耗时:{end_time-start_time}')