#!/usr/bin/python
#-*- coding: utf-8 -*-
import time
import json
from netmiko import ConnectHandler
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
with open('ip_lab5.json') as f:
        devices = json.load(f)
for device in devices:
        with ConnectHandler(**device['connection']) as connect:
                hostname = device['connection'].get('host')
                print("已经成功登陆交换机:" + hostname)
                print("开始执行命令")
                output1 = connect.send_command('display ip interface', use_textfsm=True)       # 通过use_textfsm=Ture,调用textfsm，textfsm输出结果是list
                output2 = connect.send_command('display ip routing-table', use_textfsm=True)
                log = open(hostname + '-' + LogTime + '.txt', 'w')
                log.write(json.dumps(output1, indent=2)+json.dumps(output2, indent=2))        # dumps()可以将输出结果转换成json格式的字符串。
                log.close()
                print('设备中UP的接口如下：')
                for interface in output1:
                        f = interface.get('line_status')                                       # 使用dict的get()方法获取key对应的vaules
                        if f != 'DOWN':                                                        # 对vaules进行判断
                                print(interface.get('intf'))                                   # 打印接口名称
                                print('-link-status:', interface.get('line_status'))           # 打印链路状态
                                print('-ip_address:', interface.get('ipaddr'))                 # 打印设备IP地址
                net_count, static_count, direct_count, ospf_count=0, 0, 0, 0
                for net in output2:
                        f = net.get('protocal')                                               # 判断protocal对应的vaule
                        if f == 'Static':                                                     # 判断vaule内容
                                static_count += 1                                             # 静态+1
                        if f == 'Direct':
                                direct_count += 1                                             # 直连+1
                        if f == 'Ospf':
                                ospf_count += 1                                               # ospf+1
                        net_count += 1                                                        # 总体加1
                print('设备中路由统计信息：')
                print('-静态路由条目总计:', static_count)
                print('-直连路由条目总计:', direct_count)
                print('-ospf路由条目总计:', ospf_count)
                print('-路由条目总计:', net_count)
