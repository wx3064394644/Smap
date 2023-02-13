import os

os.system('cd logo  &&  logo.py')

print('如果访问成功那么证明目录泄露了')
ip = input('输入ip或域名:')
port = input('输入端口(80 or 443):')
print('可选默认日志目录(输入对应数字即可)')
print('1 /Application/Runtime/Logs/Admin')
print('2 /Runtime/Logs/Admin')
path = input('输入日志目录:')

if port == "80" and path == "1":

    os.system('start http://{}/Application/Runtime/Logs/Admin'.format(ip))

elif port == "443" and path == "1":

    os.system('start https://{}/Application/Runtime/Logs/Admin'.format(ip))

elif port == "80" and path == "2":

    os.system('start http://{}/Runtime/Logs/Admin'.format(ip))

elif port == "443" and path == "2":

    os.system('start https://{}/Runtime/Logs/Admin'.format(ip))

elif port == "80":

    os.system('start http://{IP}/{MULU}'.format(IP=ip,MULU=path))

elif port == "443":

    os.system('start https://{IP}/{MULU}'.format(IP=ip, MULU=path))

