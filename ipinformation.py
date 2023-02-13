#!/usr/bin/env python
# coding: utf-8
import json
import requests
import sys
import time
import os
import os

os.system('cd logo  &&  logo.py')

print('在txt中输入ip获取目标信息(可批量获取)')
print('最后结果保存在ipinformation.txt')
os.system('cd url  &&  ip.txt')

data_ip = open(r'url/ip.txt')
data_ip


def get_ip_location(ip):
    url = f"http://ip.taobao.com/outGetIpInfo?ip={ip}&accessKey=alibaba-inc"
    r = requests.get(url)
    data = json.loads(r.text)
    queryIp, country, region, city, isp = (
        data['data']['queryIp'],
        data['data']['country'],
        data['data']['region'],
        data['data']['city'],
        data['data']['isp'],
    )
    return queryIp, country, region, city, isp


def output_data(data):
    ret = "%-10s\t%-4s\t%-4s\t%-4s\t%-4s\n" % ("queryIp", "country", "region", "city", "isp")
    ret += "%-10s\t%-4s\t%-4s\t%-4s\t%-4s" % data
    print(ret)
    return (ret)


data1 = data_ip.readlines()
ipresult = open(r'report/ipinformation.txt', 'w')
for i in data1:
    ret = get_ip_location(i)
    time.sleep(0.01)
    ipdata = output_data(ret)
    ipresult.write(ipdata + '\n')
ipresult.close()