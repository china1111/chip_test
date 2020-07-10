import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import copy
import conf
import binascii
import json
import socket
import zlib
import time
import threading
import os

class classAback(QThread):
    update_date = pyqtSignal(str)
    update_date1 = pyqtSignal(str)
    update_date2 = pyqtSignal(str)
    update_date3 = pyqtSignal(str, str, str, str)
    update_date4 = pyqtSignal(str, str, str)
    update_date5 = pyqtSignal()

    def __init__(self, self1):
        # print("classAback")
        self.self1 = self1
        super(classAback, self).__init__()
        with open("order_dict.json", 'r') as f:
            self.order_dict = json.load(f)
        # print("self.order_dict")
        print(self.order_dict)
        self.order_dict0 = {}
        for k, v in self.order_dict.items():
            self.order_dict0[k] = binascii.a2b_hex(v)
        self.order_dict = copy.deepcopy(self.order_dict0)
        # print("打印字典完成")
        self.connectDSP(conf.IP1_ADDR, conf.IP1_PORT)
        print("socket连接完成")
        self.pidset = 0
        self.lock = threading.Lock()
        self.__flag_pause = threading.Event()
        self.__flag_pause.clear()

    def connectDSP(self, ipaddr, port):
        # print("开始connectDSP")
        self.sss = 0
        self.n = 0
        while self.n < 3:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((ipaddr, port))
            except TimeoutError as e:
                self.n += 1
                continue
            break

        if self.n == 3:
            print("测试版连接失败")
            return
        else:
            print("测试版连接成功")

        while True:
            try:
                # print(self.order_dict['getMAC'])
                self.sock.send(self.order_dict['getMAC'])
                # self.sock.send(self.order_dict['getMAC'].encode())
                self.recv = self.sock.recv(1024)
                # print(self.recv)
                self.mac = binascii.b2a_hex(self.recv).decode()
                # print(self.mac)
                # print(self.crc(self.mac[4:-12]))
                # print(self.mac[-12:-4])
                if self.crc(self.mac[4:-12]) == self.mac[-12:-4]:
                    break
            # except Exception as e:
            except socket.error as e:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((ipaddr, port))

        self.idfirst = '000101' + self.mac[18:-12]
        # print("semf.mac")
        # print(self.mac)
        # print(self.idfirst)

    def crc(self, l1):
        self.l2 = binascii.a2b_hex(l1)
        # print(self.l2)
        self.c = zlib.crc32(self.l2)
        return hex(self.c)[2:] if len(hex(self.c)[2:]) == 8 else '0'*(8-len(hex(self.c)[2:]))+hex(self.c)[2:]

    def ordercreate(self, l1, l2, l3):
        return 'aa55' + l1 + '{:04x}'.format(int(len(l2) / 2)) + l2 + l3 + '33cc'

    def run(self):
        self.pidset = 0
        print("开始run")
        self.recvPOWER = ''
        self.update_date1.emit('55aa00020007000300006c8000dd699d1a33cc')
        self.time = time.localtime()
        self.id = self.idfirst + '{:04x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(self.time.tm_year, self.time.tm_mon,
                                                                               self.time.tm_mday, self.time.tm_hour,
                                                                               self.time.tm_min, self.time.tm_sec)
        self.sendid = self.ordercreate('0001', self.id,
                                       self.crc('0001' + '{:04x}'.format(int(len(self.id) / 2)) + self.id))
        # print("self.sendid")
        # print(self.sendid)
        self.sendid = binascii.a2b_hex(self.sendid)
        # print("self.sendid")
        # print(self.sendid)
        self.sendord1 = [self.sendid, self.order_dict['getSTATE']]
        while True:
            for i in self.sendord1:
                while True:
                    try:
                        # print("self.socket.send('self.sendid')")
                        # print(i)
                        # print("这里对不对")
                        # time.sleep(1)
                        self.sock.send(i)
                        # print('sock getSTATE OK')

                        self.recv = self.sock.recv(1024)
                        # print(self.recv)
                    except Exception as e:
                        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.sock.connect((conf.IP1_ADDR, conf.IP1_PORT))
                    self.recv = binascii.b2a_hex(self.recv).decode()
                    # print(self.recv)
                    # print('hello world1')
                    # print(self.recv[4:-12])
                    # print(self.crc(self.recv[4:-12]))
                    # print(self.recv[-12:-4])
                    if i is self.sendord1[1]:
                        self.sock.send(self.order_dict['getPOWER'])
                        self.recvPOWER = binascii.b2a_hex(self.sock.recv(1024)).decode()
                        self.update_date3.emit(self.id, time.strftime("%Y-%m-%d %H:%M:%S", self.time), self.recv, self.recvPOWER)
                        self.update_date.emit(self.recvPOWER)
                        self.update_date4.emit(self.id, '', self.recvPOWER)

                    if i is self.sendord1[1] and int(self.recv[8:12], 16) != 5:
                        self.update_date1.emit(self.recv)
                        self.update_date2.emit(self.recv)
                        self.update_date4.emit(self.id, self.recv, '')
                    if self.crc(self.recv[4:-12]) == self.recv[-12:-4]:
                        # print(self.recv[12:20])
                        if self.recv[12:20] != ['00010001', '00010101', '00010201']:
                            break



            # print('hello world')
            while self.recv[12:20] in ['00030001', '00030101', '00030201']:
                self.sock.send(self.order_dict['getSTATEagain'])
                self.recv = self.sock.recv(1024)
                # print(self.recv)
                self.recv = binascii.b2a_hex(self.recv).decode()
                # print(self.recv)

            print('self.total', self.recv)
            print("self.total", int(self.recv[18:22], 16))

            # print("hello world 2!!!!!")
            while True:
                # print('我操你大爷！长度到底是多少！')
                # print(len(self.recv))
                print("这里我看看对不对")
                print("self接受到的信息" + self.recv)
                if int(self.recv[20:22], 16) == int(self.recv[-14:-12], 16) and len(self.recv) > 34:
                    print("测试完成")
                    self.self1.sb50.setDisabled(False)
                    print("第一个按键")
                    self.self1.sb56.setDisabled(True)
                    print("第二个按键")
                    self.self1.sb57.setDisabled(True)
                    print("第三个按键")
                    self.update_date5.emit()
                    print("byebye")
                    return
                # time.sleep(1)
                self.sock.send(self.order_dict['getSTATE'])
                self.recv = self.sock.recv(1024)
                self.recv = binascii.b2a_hex(self.recv).decode()
                # print("开始读取状态")
                # print(self.recv)
                if int(self.recv[8:12], 16) != 5:
                    self.update_date1.emit(self.recv)
                    self.update_date2.emit(self.recv)
                # print("查看校验：")
                # print('self.sss', self.sss)
                # print('死活都不对')
                # print(self.crc(self.recv[4:-12]))
                # print(self.recv[-12:-4])
                while self.crc(self.recv[4:-12]) != self.recv[-12:-4] or self.recv[12:18] in ['00030001', '00030101',
                                                                                              '00030201']:
                    # print("发送getSTATEagain")
                    self.sock.send(self.order_dict['getSTATEagain'])
                    self.recv = self.sock.recv(1024)
                    self.recv = binascii.b2a_hex(self.recv).decode()
                    # print('你大爷的！', self.recv)

                    # 处理电压电流
                if self.sss == 1000:
                    self.sock.send(self.order_dict['getPOWER'])
                    self.recvPOWER = binascii.b2a_hex(self.sock.recv(1024)).decode()
                    # print("电压：")
                    # print(self.recvPOWER)
                    # 处理电压电流
                    # self.showPOWER(self.recv.decode())
                    self.update_date.emit(self.recvPOWER)
                    # print('电压显示完成')
                    self.sss = 0
                if self.sss == 0:
                    self.update_date4.emit(self.id, self.recv, self.recvPOWER)
                else:
                    self.update_date4.emit(self.id, self.recv, '')
                self.sss += 1
                print("PIDSET:", self.pidset)

                if self.pidset == 1:
                    self.self1.sb50.setDisabled(False)
                    self.sock.send(self.order_dict['stop'])
                    self.recv = self.sock.recv(1024)
                    self.recv = binascii.b2a_hex(self.recv).decode()
                    while self.crc(self.recv[4:-12]) != self.recv[-12:-4]:
                        self.sock.send(self.order_dict['stop'])
                        self.recv = self.sock.recv(1024)
                        self.recv = binascii.b2a_hex(self.recv).decode()
                    return
                print("是不是这里的事儿")
                if self.__flag_pause.isSet():
                    # 发送暂停命令, 直至生效
                    while True:
                        self.sock.send(self.order_dict['pause'])
                        self.recv = self.sock.recv(1024)
                        self.recv = binascii.b2a_hex(self.recv).decode()
                        print("挂起")
                        print(self.recv)
                        if self.crc(self.recv[4:-12]) == self.recv[-12:-4]:
                            break
                        time.sleep(0.1)
                    while self.__flag_pause.isSet():
                        time.sleep(0.1)
                    # 发送恢复命令, 直至生效
                    while True:
                        self.sock.send(self.order_dict['restore'])
                        self.recv = self.sock.recv(1024)
                        self.recv = binascii.b2a_hex(self.recv).decode()
                        print("恢复")
                        print(self.recv)
                        if self.crc(self.recv[4:-12]) == self.recv[-12:-4]:
                            break
                        time.sleep(0.1)
                time.sleep(conf.ReadResultCycle)
            break
        return 0

    def changepidset(self, pidset):
        self.lock.acquire()
        self.pidset = pidset
        self.lock.release()

    def pausestart(self):
        self.__flag_pause.set()
        print("线程已经暂停")

    def restorestart(self):
        self.__flag_pause.clear()
        print("线程已经恢复")