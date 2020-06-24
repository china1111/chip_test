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

class classA(QMainWindow):
    def __init__(self):
        super(classA, self).__init__()

        self.initUI()
        self.setWindowTitle("测试")
        self.setWindowIcon(QIcon(r"./images/logo1.png"))
        self.backend = classAback(self)

    def initUI(self):
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("2019-2020 SOLFIR-X.Corp")
        self.statusright = QLabel("江苏金羿智芯科技有限公司 版权所有")
        self.statusBar.addPermanentWidget(self.statusright)
        self.setStatusBar(self.statusBar)

        self.sb0 = QLabel()
        self.sb0.setText("M02 TEST Platfrorm V1.0.1")
        self.sb0.setFont(QFont("Arial", 15))
        self.sb0.setAlignment(Qt.AlignLeft)
        self.sb1 = QLabel()
        self.sb1.setAlignment(Qt.AlignRight)
        self.sb1.setPixmap(QPixmap(r"./images/logo1.png"))
        self.sb2 = QLabel("POWER")
        self.sb3 = QLabel("Voltage")
        self.sb4 = QLabel("Current")
        self.sb5 = QTableWidgetItem("M02_A")
        self.sb6 = QTableWidgetItem("INT")
        self.sb7 = QTableWidgetItem("DRAM")
        self.sb8 = QTableWidgetItem("IO")
        self.sb9 = QTableWidgetItem("3V3")
        self.sb10 = QTableWidgetItem("M02_B")
        self.sb11 = QTableWidgetItem("INT")
        self.sb12 = QTableWidgetItem("DRAM")
        self.sb13 = QTableWidgetItem("IO")
        self.sb14 = QTableWidgetItem("3V3")
        self.sb37 = QTableWidgetItem("MAIN")
        self.sb38 = QTableWidgetItem("PWR")
        self.sb15 = QLineEdit()
        self.sb15.setDisabled(True)
        self.sb15.setFixedWidth(70)
        self.sb15.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb16 = QLineEdit()
        self.sb16.setDisabled(True)
        self.sb16.setFixedWidth(70)
        self.sb16.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb17 = QLineEdit()
        self.sb17.setDisabled(True)
        self.sb17.setFixedWidth(70)
        self.sb17.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb18 = QLineEdit()
        self.sb18.setDisabled(True)
        self.sb18.setFixedWidth(70)
        self.sb18.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb19 = QLineEdit()
        self.sb19.setDisabled(True)
        self.sb19.setFixedWidth(70)
        self.sb19.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb20 = QLineEdit()
        self.sb20.setDisabled(True)
        self.sb20.setFixedWidth(70)
        self.sb20.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb21 = QLineEdit()
        self.sb21.setDisabled(True)
        self.sb21.setFixedWidth(70)
        self.sb21.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb22 = QLineEdit()
        self.sb22.setDisabled(True)
        self.sb22.setFixedWidth(70)
        self.sb22.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb23 = QLineEdit()
        self.sb23.setDisabled(True)
        self.sb23.setFixedWidth(70)
        self.sb23.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb24 = QLineEdit()
        self.sb24.setDisabled(True)
        self.sb24.setFixedWidth(70)
        self.sb24.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb25 = QLineEdit()
        self.sb25.setDisabled(True)
        self.sb25.setFixedWidth(70)
        self.sb25.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb26 = QLineEdit()
        self.sb26.setDisabled(True)
        self.sb26.setFixedWidth(70)
        self.sb26.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb27 = QLineEdit()
        self.sb27.setDisabled(True)
        self.sb27.setFixedWidth(70)
        self.sb27.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb28 = QLineEdit()
        self.sb28.setDisabled(True)
        self.sb28.setFixedWidth(70)
        self.sb28.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb29 = QLineEdit()
        self.sb29.setDisabled(True)
        self.sb29.setFixedWidth(70)
        self.sb29.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb30 = QLineEdit()
        self.sb30.setDisabled(True)
        self.sb30.setFixedWidth(70)
        self.sb30.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb31 = QLineEdit()
        self.sb31.setDisabled(True)
        self.sb31.setFixedWidth(70)
        self.sb31.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb32 = QLineEdit()
        self.sb32.setDisabled(True)
        self.sb32.setFixedWidth(70)
        self.sb32.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb33 = QLabel("LOG")
        self.sb33.setDisabled(True)
        self.sb33.setFixedWidth(70)
        self.sb33.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb34 = QTextEdit()
        self.sb34.setDisabled(True)
        # self.sb34.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb34.setFixedHeight(272)
        # self.sb34.setFixedWidth(234)

        self.sb35 = QHBoxLayout()
        self.sb35.addSpacing(5)
        self.sb35.addWidget(self.sb2)
        self.sb35.addSpacing(36)
        self.sb35.addWidget(self.sb3)
        self.sb35.addSpacing(7)
        self.sb35.addWidget(self.sb4)

        self.sb36 = QTableWidget()
        self.sb36.setDisabled(True)
        self.sb36.setRowCount(9)
        self.sb36.setColumnCount(4)
        self.sb36.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sb36.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sb36.horizontalHeader().setVisible(False)
        self.sb36.verticalHeader().setVisible(False)
        self.sb36.setFixedWidth(264)
        self.sb36.setFixedHeight(272)
        self.sb36.setItem(0, 0, self.sb37)
        self.sb37.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(0, 1, self.sb38)
        self.sb38.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(1, 0, self.sb5)
        self.sb5.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(1, 1, self.sb6)
        self.sb6.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(2, 1, self.sb7)
        self.sb7.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(3, 1, self.sb8)
        self.sb8.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(4, 1, self.sb9)
        self.sb9.setTextAlignment(Qt.AlignCenter)
        self.sb36.setSpan(1, 0, 4, 1)
        self.sb36.setCellWidget(0, 2, self.sb15)
        self.sb36.setCellWidget(0, 3, self.sb16)
        self.sb36.setCellWidget(1, 2, self.sb17)
        self.sb36.setCellWidget(1, 3, self.sb18)
        self.sb36.setCellWidget(2, 2, self.sb19)
        self.sb36.setCellWidget(2, 3, self.sb20)
        self.sb36.setCellWidget(3, 2, self.sb21)
        self.sb36.setCellWidget(3, 3, self.sb22)
        self.sb36.setCellWidget(4, 2, self.sb23)
        self.sb36.setCellWidget(4, 3, self.sb24)

        self.sb36.setItem(5, 0, self.sb10)
        self.sb10.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(5, 1, self.sb11)
        self.sb11.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(6, 1, self.sb12)
        self.sb12.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(7, 1, self.sb13)
        self.sb13.setTextAlignment(Qt.AlignCenter)
        self.sb36.setItem(8, 1, self.sb14)
        self.sb14.setTextAlignment(Qt.AlignCenter)
        self.sb36.setSpan(5, 0, 4, 1)
        self.sb36.setCellWidget(5, 2, self.sb25)
        self.sb36.setCellWidget(5, 3, self.sb26)
        self.sb36.setCellWidget(6, 2, self.sb27)
        self.sb36.setCellWidget(6, 3, self.sb28)
        self.sb36.setCellWidget(7, 2, self.sb29)
        self.sb36.setCellWidget(7, 3, self.sb30)
        self.sb36.setCellWidget(8, 2, self.sb31)
        self.sb36.setCellWidget(8, 3, self.sb32)
        self.sb36.resizeColumnsToContents()
        self.sb36.setColumnWidth(0, 60)
        self.sb36.setColumnWidth(1, 60)

        self.sb39 = QHBoxLayout()
        self.sb39.addWidget(self.sb0)
        self.sb39.addWidget(self.sb1)

        self.sb40 = QVBoxLayout()
        self.sb40.addWidget(self.sb36)


        self.sb42 = QVBoxLayout()
        self.sb42.addLayout(self.sb35)
        self.sb42.addLayout(self.sb40)


        self.sb43 = QVBoxLayout()
        self.sb43.addWidget(self.sb33)
        self.sb43.addWidget(self.sb34)

        self.sb44 = QHBoxLayout()
        self.sb44.addLayout(self.sb42)
        self.sb44.addLayout(self.sb43)




        self.sb45 = QProgressBar()
        self.sb46 = 0
        self.sb45.setValue(self.sb46)

        self.sb47 = QVBoxLayout()
        self.sb48 = QLineEdit("Hello world")
        self.sb48.setFixedHeight(20)
        self.sb48.setDisabled(True)
        self.sb48.setFixedWidth(100)
        self.sb48.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb47.addWidget(self.sb48)
        self.sb47.addWidget(self.sb45)

        self.sb49 = QPushButton("Setup")
        self.sb50 = QPushButton("Start")
        self.sb50.clicked.connect(self.startchecked)
        self.sb51 = QPushButton("Stop")
        self.sb52 = QHBoxLayout()
        self.sb52.addWidget(self.sb49)
        self.sb52.addSpacing(350)
        self.sb52.addWidget(self.sb50)
        self.sb52.addWidget(self.sb51)

        self.sb53 = QVBoxLayout()
        self.sb53.addLayout(self.sb39)
        self.sb53.addLayout(self.sb44)
        self.sb53.addLayout(self.sb47)
        self.sb53.addLayout(self.sb52)

        self.sb54 = QWidget()
        self.sb54.setLayout(self.sb53)
        self.setCentralWidget(self.sb54)
        self.setFixedSize(660, 440)
        # self.setFixedSize(498, 440)
        print("width = " + str(self.width()))
        print("height = " + str(self.height()))

    def startchecked(self):
        self.sb50.setDisabled(True)
        self.backend.update_date.connect(self.showPOWER)
        self.backend.update_date1.connect(self.showPROGRESSBAR)
        self.backend.start()

    def endchecked(self):
        pass

    def setupchecked(self):
        pass

    def showPROGRESSBAR(self, l1):
        print("显示进度条")
        self.sb46 = 100 * int(l1[-14:-12], 16) / int(l1[20:22], 16)
        print(self.sb46)
        self.sb45.setValue(self.sb46)


    def showPOWER(self, l1):
        print(l1)
        self.POWERstr = [l1[16:-12][i:i + 4] for i in range(0, len(l1[16:-12]), 4)]
        print(self.POWERstr)
        print(str(int(self.POWERstr[0], 16) / 1000) + 'V')
        print(type(str(int(self.POWERstr[0], 16) / 1000) + 'V'))
        self.sb15.setText('{:.3f}'.format(int(self.POWERstr[0], 16) / 1000) + 'V')
        self.sb16.setText('{:.3f}'.format(int(self.POWERstr[1], 16) / 1000) + 'A')
        self.sb17.setText('{:.3f}'.format(int(self.POWERstr[2], 16) / 1000) + 'V')
        self.sb18.setText('{:.3f}'.format(int(self.POWERstr[3], 16) / 1000) + 'A')
        self.sb19.setText('{:.3f}'.format(int(self.POWERstr[4], 16) / 1000) + 'V')
        self.sb20.setText('{:.3f}'.format(int(self.POWERstr[5], 16) / 1000) + 'A')
        self.sb21.setText('{:.3f}'.format(int(self.POWERstr[6], 16) / 1000) + 'V')
        self.sb22.setText('{:.3f}'.format(int(self.POWERstr[7], 16) / 1000) + 'A')
        self.sb23.setText('{:.3f}'.format(int(self.POWERstr[14], 16) / 1000) + 'V')
        self.sb24.setText('{:.3f}'.format(int(self.POWERstr[15], 16) / 1000) + 'A')
        self.sb25.setText('{:.3f}'.format(int(self.POWERstr[8], 16) / 1000) + 'V')
        self.sb26.setText('{:.3f}'.format(int(self.POWERstr[9], 16) / 1000) + 'A')
        self.sb27.setText('{:.3f}'.format(int(self.POWERstr[10], 16) / 1000) + 'V')
        self.sb28.setText('{:.3f}'.format(int(self.POWERstr[11], 16) / 1000) + 'A')
        self.sb29.setText('{:.3f}'.format(int(self.POWERstr[12], 16) / 1000) + 'V')
        self.sb30.setText('{:.3f}'.format(int(self.POWERstr[13], 16) / 1000) + 'A')
        self.sb31.setText('{:.3f}'.format(int(self.POWERstr[14], 16) / 1000) + 'V')
        self.sb32.setText('{:.3f}'.format(int(self.POWERstr[15], 16) / 1000) + 'A')
        # self.sb15.setText(str(int(self.POWERstr[0], 16) / 1000) + 'V')
        # self.sb16.setText(str(int(self.POWERstr[1], 16) / 1000) + 'A')
        # self.sb17.setText(str(int(self.POWERstr[2], 16) / 1000) + 'V')
        # self.sb18.setText(str(int(self.POWERstr[3], 16) / 1000) + 'A')
        # self.sb19.setText(str(int(self.POWERstr[4], 16) / 1000) + 'V')
        # self.sb20.setText(str(int(self.POWERstr[5], 16) / 1000) + 'A')
        # self.sb21.setText(str(int(self.POWERstr[6], 16) / 1000) + 'V')
        # self.sb22.setText(str(int(self.POWERstr[7], 16) / 1000) + 'A')
        # self.sb23.setText(str(int(self.POWERstr[14], 16) / 1000) + 'V')
        # self.sb24.setText(str(int(self.POWERstr[15], 16) / 1000) + 'A')
        # self.sb25.setText(str(int(self.POWERstr[8], 16) / 1000) + 'V')
        # self.sb26.setText(str(int(self.POWERstr[9], 16) / 1000) + 'A')
        # self.sb27.setText(str(int(self.POWERstr[10], 16) / 1000) + 'V')
        # self.sb28.setText(str(int(self.POWERstr[11], 16) / 1000) + 'A')
        # self.sb29.setText(str(int(self.POWERstr[12], 16) / 1000) + 'V')
        # self.sb30.setText(str(int(self.POWERstr[13], 16) / 1000) + 'A')
        # self.sb31.setText(str(int(self.POWERstr[14], 16) / 1000) + 'V')
        # self.sb32.setText(str(int(self.POWERstr[15], 16) / 1000) + 'A')



class classAback(QThread):
    update_date = pyqtSignal(str)
    update_date1 = pyqtSignal(str)

    def __init__(self, self1):
        print("classAback")
        self.self1 = self1
        super(classAback, self).__init__()
        with open("order_dict.json", 'r') as f:
            self.order_dict = json.load(f)
        print("self.order_dict")
        print(self.order_dict)
        self.order_dict0 = {}
        for k, v in self.order_dict.items():
            self.order_dict0[k] = binascii.a2b_hex(v)
        self.order_dict = copy.deepcopy(self.order_dict0)
        print("打印字典完成")
        self.connectDSP(conf.IP1_ADDR, conf.IP1_PORT)

    def connectDSP(self, ipaddr, port):
        print("开始connectDSP")
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
                print(self.order_dict['getMAC'])
                self.sock.send(self.order_dict['getMAC'])
                # self.sock.send(self.order_dict['getMAC'].encode())
                self.recv = self.sock.recv(1024)
                print(self.recv)
                self.mac = binascii.b2a_hex(self.recv).decode()
                print(self.mac)
                print(self.crc(self.mac[4:-12]))
                print(self.mac[-12:-4])
                if self.crc(self.mac[4:-12]) == self.mac[-12:-4]:
                    break
            # except Exception as e:
            except socket.error as e:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((ipaddr, port))

        self.idfirst = '000101' + self.mac[18:-12]
        print("semf.mac")
        print(self.mac)
        print(self.idfirst)

    def crc(self, l1):
        self.l2 = binascii.a2b_hex(l1)
        print(self.l2)
        self.c = zlib.crc32(self.l2)
        return hex(self.c)[2:] if len(hex(self.c)[2:]) == 8 else '0'*(8-len(hex(self.c)[2:]))+hex(self.c)[2:]

    def ordercreate(self, l1, l2, l3):
        return 'aa55' + l1 + '{:04x}'.format(int(len(l2) / 2)) + l2 + l3 + '33cc'

    def run(self):
        print("开始run")
        self.update_date1.emit('55aa00020007000300006c8000dd699d1a33cc')
        self.time = time.localtime()
        self.id = self.idfirst + '{:04x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(self.time.tm_year, self.time.tm_mon,
                                                                               self.time.tm_mday, self.time.tm_hour,
                                                                               self.time.tm_min, self.time.tm_sec)
        self.sendid = self.ordercreate('0001', self.id,
                                       self.crc('0001' + '{:04x}'.format(int(len(self.id) / 2)) + self.id))
        print("self.sendid")
        print(self.sendid)
        self.sendid = binascii.a2b_hex(self.sendid)
        print("self.sendid")
        print(self.sendid)
        self.sendord1 = [self.sendid, self.order_dict['getSTATE']]
        while True:
            for i in self.sendord1:
                while True:
                    try:
                        print("self.socket.send('self.sendid')")
                        print(i)
                        print("这里对不对")
                        # time.sleep(1)
                        # self.sock.send(i.encode())
                        self.sock.send(i)
                        print('sock getSTATE OK')

                        self.recv = self.sock.recv(1024)
                        print(self.recv)
                    except Exception as e:
                        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.sock.connect((conf.IP1_ADDR, conf.IP1_PORT))
                    self.recv = binascii.b2a_hex(self.recv)
                    print(self.recv)
                    self.recv = self.recv.decode()
                    print(self.recv)
                    print('hello world1')
                    print(self.recv[4:-12])
                    print(self.crc(self.recv[4:-12]))
                    print(self.recv[-12:-4])
                    if i is self.sendord1[1] and int(self.recv[8:12], 16) != 5:
                        self.update_date1.emit(self.recv)
                    if self.crc(self.recv[4:-12]) == self.recv[-12:-4]:
                        print(self.recv[12:20])
                        if self.recv[12:20] != ['00010001', '00010101', '00010201']:
                            break

            print('hello world')
            while self.recv[12:18] in ['00030001', '00030101', '00030201']:
                self.sock.send(self.order_dict['getSTATEagain'])
                self.recv = self.sock.recv(1024)
                print(self.recv)
                self.recv = binascii.b2a_hex(self.recv).decode()
                print(self.recv)

            print("hello world 2!!!!!")
            while True:
                print('我操你大爷！长度到底是多少！')
                print(len(self.recv))
                if int(self.recv[20:22], 16) == int(self.recv[-14:-12], 16) and len(self.recv) > 34:
                    print("测试完成")
                    self.self1.sb50.setDisabled(False)
                    return
                # time.sleep(1)
                self.sock.send(self.order_dict['getSTATE'])
                self.recv = self.sock.recv(1024)
                self.recv = binascii.b2a_hex(self.recv).decode()
                print("开始读取状态")
                print(self.recv)
                if int(self.recv[8:12], 16) != 5:
                    self.update_date1.emit(self.recv)
                print("查看校验：")
                print('self.sss', self.sss)
                print('死活都不对')
                print(self.crc(self.recv[4:-12]))
                print(self.recv[-12:-4])
                while self.crc(self.recv[4:-12]) != self.recv[-12:-4] or self.recv[12:18] in ['00030001', '00030101',
                                                                                              '00030201']:
                    print("发送getSTATEagain")
                    self.sock.send(self.order_dict['getSTATEagain'])
                    self.recv = self.sock.recv(1024)
                    self.recv = binascii.b2a_hex(self.recv).decode()
                    print('你大爷的！', self.recv)

                    # 处理电压电流
                if self.sss == 2:
                    self.sock.send(self.order_dict['getPOWER'])
                    self.recvPOWER = binascii.b2a_hex(self.sock.recv(1024))
                    print("电压：")
                    print(self.recvPOWER)
                    # 处理电压电流
                    # self.showPOWER(self.recv.decode())
                    self.update_date.emit(self.recvPOWER.decode())
                    print('电压显示完成')
                    self.sss = 0
                self.sss += 1
            break
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = classA()
    main.show()
    sys.exit(app.exec_())
