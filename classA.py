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
import classB
import classC
import inspect
import ctypes

class classA(QMainWindow):
    def __init__(self):
        super(classA, self).__init__()

        self.initUI()
        self.setWindowTitle("测试")
        self.setWindowIcon(QIcon(r"./images/logo1.png"))
        self.backend = -1
        self.tem1 = -100
        self.tem2 = -100

    def initUI(self):
        with open("statuscode.json", 'r') as f:
            self.sb99 = json.load(f)
        # with open("level.json", "r") as f:
        #     self.level = json.load(f)
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("2019-2020 SOLFIR-X.Corp")
        self.statusright = QLabel("江苏金羿智芯科技有限公司 版权所有")
        self.statusBar.addPermanentWidget(self.statusright)
        self.setStatusBar(self.statusBar)
        self.lock = threading.Lock()

        self.sb0 = QLabel()
        self.sb0.setText("M02 TEST Platfrorm V1.0.1")
        self.sb0.setFont(QFont("Arial", 15))
        self.sb0.setAlignment(Qt.AlignLeft)
        self.sb1 = QLabel()
        self.sb1.setAlignment(Qt.AlignRight)
        self.sb1.setPixmap(QPixmap(r"./images/logo1.png"))
        self.sb2 = QLabel("POWER")
        self.sb2.setFixedHeight(20)
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
        # self.sb33.setDisabled(True)
        self.sb33.setFixedWidth(70)
        self.sb33.setFixedHeight(32)
        self.sb33.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb34 = QTextEdit()
        # self.sb34.setDisabled(True)
        # self.sb34.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb34.setFixedHeight(272)
        # self.sb34.setFixedWidth(234)

        self.sb35 = QHBoxLayout()
        self.sb35.addSpacing(15)
        self.sb35.addWidget(self.sb2)
        self.sb35.addSpacing(55)
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
        self.sb58 = QLabel("Result")
        self.sb59 = QLineEdit()
        self.sb59.setDisabled(True)
        self.sb59.setFixedHeight(20)
        self.sb59.setFixedWidth(40)
        self.sb59.setStyleSheet("background:gray")
        self.sb62 = QLabel("Status")
        self.sb63 = QLineEdit()
        self.sb63.setDisabled(True)
        self.sb63.setFixedSize(40, 20)
        self.sb63.setStyleSheet("background:red")
        self.sb60 = QHBoxLayout()
        self.sb60.addSpacing(5)
        self.sb60.addWidget(self.sb33)
        self.sb60.addSpacing(130)
        self.sb60.addWidget(self.sb62)
        self.sb60.addWidget(self.sb63)
        self.sb60.addWidget(self.sb58)
        self.sb60.addWidget(self.sb59)
        self.sb61 = QHBoxLayout()
        self.sb61.addWidget(self.sb34)
        self.sb43.addLayout(self.sb60)
        self.sb43.addLayout(self.sb61)
        # self.sb43.addWidget(self.sb33)
        # self.sb43.addWidget(self.sb34)

        self.sb44 = QHBoxLayout()
        self.sb44.addLayout(self.sb42)
        self.sb44.addLayout(self.sb43)




        self.sb45 = QProgressBar()
        self.sb46 = 0
        self.sb45.setValue(self.sb46)

        self.sb47 = QVBoxLayout()
        self.sb48 = QLineEdit()
        self.sb48.setFixedHeight(20)
        # self.sb48.setDisabled(True)
        self.sb48.setFixedWidth(100)
        self.sb48.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        self.sb47.addWidget(self.sb48)
        self.sb47.addWidget(self.sb45)

        self.sb49 = QPushButton("Setup")
        self.sb49.clicked.connect(self.setupchecked)
        self.sb50 = QPushButton("Start")
        self.sb50.clicked.connect(self.startchecked)
        self.sb56 = QPushButton("Pause")
        self.sb56.setDisabled(True)
        self.sb56.clicked.connect(self.pausechecked)

        self.sb57 = QPushButton("Restore")
        self.sb57.setDisabled(True)
        self.sb57.clicked.connect(self.restorechecked)

        self.sb51 = QPushButton("Stop")
        self.sb51.clicked.connect(self.endchecked)
        self.sb52 = QHBoxLayout()
        self.sb52.addWidget(self.sb49)
        self.sb52.addSpacing(250)
        self.sb52.addWidget(self.sb50)
        self.sb52.addWidget(self.sb56)
        self.sb52.addWidget(self.sb57)
        self.sb52.addWidget(self.sb51)

        self.sb53 = QVBoxLayout()
        self.sb53.addLayout(self.sb39)
        self.sb53.addLayout(self.sb44)
        self.sb53.addLayout(self.sb47)
        self.sb53.addLayout(self.sb52)

        self.sb54 = QWidget()
        self.sb54.setLayout(self.sb53)
        self.setCentralWidget(self.sb54)
        self.setFixedSize(660, 460)

        # 电压记录格式[VDD12V, VDD3V3, VDDINT_A, VDDRAM_A, VDDIO_A, VDDINT_B, VDDRAM_B, VDDIO_B]
        self.sbPOWER = []

        # self.setFixedSize(498, 440)
        # print("width = " + str(self.width()))
        # print("height = " + str(self.height()))

    def startchecked(self):
        self.sb50.setDisabled(True)
        self.sb59.setStyleSheet("background:gray")
        self.sb63.setStyleSheet("background:green")
        self.sb55 = ''
        print("self.sb55:", self.sb55)
        self.sb34.setPlainText(None)
        self.right = 0
        self.wrong = 0
        self.temp = 0
        if self.backend == -1:
            self.backend = classB.classAback(self)
            self.backend.update_date3.connect(self.writetologbegin)
            self.backend.update_date2.connect(self.showLOG)
            self.backend.update_date.connect(self.showPOWER)
            self.backend.update_date1.connect(self.showPROGRESSBAR)
            self.backend.update_date4.connect(self.writetolog)
            self.backend.update_date5.connect(self.writetologend)
            self.backend.restorestart()
        self.backend.start()
        print("backend创建成功")
        self.sb56.setDisabled(False)

    def endchecked(self):
        self.sb59.setStyleSheet("background:gray")
        self.sb63.setStyleSheet("background:red")
        if self.backend == -1:
            return
        self.backend.changepidset(1)
        time.sleep(0.5)
        del self.backend
        self.backend = -1
        self.sb50.setDisabled(False)
        self.sb56.setDisabled(True)
        self.sb57.setDisabled(True)

    def setupchecked(self):
        self.setDisabled(True)
        self.setupobj = classC.classC(self)
        self.setupobj.update_temp1.connect(self.settemp1)
        self.setupobj.update_temp2.connect(self.settemp2)
        self.setupobj.show()

    def settemp1(self, temp1):
        self.tem1 = temp1
        print(self.tem1)

    def settemp2(self, temp2):
        self.tem2 = temp2
        print(self.tem2)

    def pausechecked(self):
        if self.backend == -1:
            return
        self.sb63.setStyleSheet("background:yellow")
        self.sb56.setDisabled(True)
        self.sb57.setDisabled(False)
        self.backend.pausestart()


    def restorechecked(self):
        self.sb63.setStyleSheet("background:green")
        self.sb56.setDisabled(False)
        self.sb57.setDisabled(True)
        self.backend.restorestart()




    def showPROGRESSBAR(self, l1):
        # print("显示进度条")
        self.sb46 = 100 * int(l1[-14:-12], 16) / int(l1[20:22], 16)
        # print(self.sb46)
        self.sb45.setValue(self.sb46)
        # if l1[-14:-12] == l1[20:22]:
        #     self.lock.acquire()
        #     with open(self.id, 'a') as f1:
        #         self.writetolog(f1, right=self.right, wrong=self.wrong)
        #     self.lock.release()


    def showPOWER(self, l1):
        # print(l1)
        self.POWERstr = [l1[16:-12][i:i + 4] for i in range(0, len(l1[16:-12]), 4)]
        # with open(self.id, 'a') as f1:
        #     self.writetolog(f1, *[int(self.POWERstr, 16) / 1000])
        # print(self.POWERstr)
        # print(str(int(self.POWERstr[0], 16) / 1000) + 'V')
        # print(type(str(int(self.POWERstr[0], 16) / 1000) + 'V'))
        # self.sb15.setStyleSheet("color:red")


        keylis = [f"sb{i}" for i in range(15, 33)]
        vallis = [int(i, 16)/1000 for i in self.POWERstr]
        vallis.insert(8, int(self.POWERstr[14], 16) / 1000)
        vallis.insert(9, int(self.POWERstr[15], 16) / 1000)
        prolis = [self.sb15, self.sb16, self.sb17, self.sb18, self.sb19, self.sb20, self.sb21, self.sb22, self.sb23, self.sb24, self.sb25, self.sb26, self.sb27, self.sb28, self.sb29, self.sb30, self.sb31, self.sb32]
        prodic = {keylis[i]:prolis[i] for i in range(len(keylis))}
        showdic = {keylis[i]:vallis[i] for i in range(len(keylis))}
        '''
        for k, v in showdic.items():
            if v > 0.2:
                prodic[k].setStyleSheet("color:red")
            else:
                prodic[k].setStyleSheet("color:black")
        '''
        print("这里咋样")
        '''
        self.leveldic = {'sb15':self.level['VDD12V'][0:2],
                    'sb16':self.level['VDD12V'][2:],
                    'sb17':self.level['VDDINT_A'][0:2],
                    'sb18':self.level['VDDINT_A'][2:],
                    'sb19':self.level['VDDDRM_A'][0:2],
                    'sb20':self.level['VDDDRM_A'][2:],
                    'sb21':self.level['VDDDIO_A'][0:2],
                    'sb22':self.level['VDDDIO_A'][2:],
                    'sb23':self.level['VDDD3V3_A'][0:2],
                    'sb24':self.level['VDDD3V3_A'][2:],
                    'sb25':self.level['VDDINT_B'][0:2],
                    'sb26':self.level['VDDINT_B'][2:],
                    'sb27':self.level['VDDDRM_B'][0:2],
                    'sb28':self.level['VDDDRM_B'][2:],
                    'sb29':self.level['VDDDIO_B'][0:2],
                    'sb30':self.level['VDDDIO_B'][0:2],
                    'sb31':self.level['VDDD3V3_B'][0:2],
                    'sb32':self.level['VDDD3V3_B'][2:],
        }
        '''
        self.leveldic = {'sb15': conf.VDD12V[0:2],
                         'sb16': conf.VDD12V[2:],
                         'sb17': conf.VDDINT_A[0:2],
                         'sb18': conf.VDDINT_A[2:],
                         'sb19': conf.VDDDRM_A[0:2],
                         'sb20': conf.VDDDRM_A[2:],
                         'sb21': conf.VDDDIO_A[0:2],
                         'sb22': conf.VDDDIO_A[2:],
                         'sb23': conf.VDDD3V3_A[0:2],
                         'sb24': conf.VDDD3V3_A[2:],
                         'sb25': conf.VDDINT_B[0:2],
                         'sb26': conf.VDDINT_B[2:],
                         'sb27': conf.VDDDRM_B[0:2],
                         'sb28': conf.VDDDRM_B[2:],
                         'sb29': conf.VDDDIO_B[0:2],
                         'sb30': conf.VDDDIO_B[0:2],
                         'sb31': conf.VDDD3V3_B[0:2],
                         'sb32': conf.VDDD3V3_B[2:],
                         }
        # print(self.leveldic)
        for k, v in showdic.items():
            print(k)
            print(v)
            print(self.leveldic[k])

            if float(self.leveldic[k][0]) < v and v < float(self.leveldic[k][1]):
                prodic[k].setStyleSheet("color:black")
            else:
                prodic[k].setStyleSheet("color:red")






        self.sb15.setText("{:.3f}V".format(int(self.POWERstr[0], 16) / 1000))
        self.sb16.setText('{:.3f}A'.format(int(self.POWERstr[1], 16) / 1000))
        self.sb17.setText('{:.3f}V'.format(int(self.POWERstr[2], 16) / 1000))
        self.sb18.setText('{:.3f}A'.format(int(self.POWERstr[3], 16) / 1000))
        self.sb19.setText('{:.3f}V'.format(int(self.POWERstr[4], 16) / 1000))
        self.sb20.setText('{:.3f}A'.format(int(self.POWERstr[5], 16) / 1000))
        self.sb21.setText('{:.3f}V'.format(int(self.POWERstr[6], 16) / 1000))
        self.sb22.setText('{:.3f}A'.format(int(self.POWERstr[7], 16) / 1000))
        self.sb23.setText('{:.3f}V'.format(int(self.POWERstr[14], 16) / 1000))
        self.sb24.setText('{:.3f}A'.format(int(self.POWERstr[15], 16) / 1000))
        self.sb25.setText('{:.3f}V'.format(int(self.POWERstr[8], 16) / 1000))
        self.sb26.setText('{:.3f}A'.format(int(self.POWERstr[9], 16) / 1000))
        self.sb27.setText('{:.3f}V'.format(int(self.POWERstr[10], 16) / 1000))
        self.sb28.setText('{:.3f}A'.format(int(self.POWERstr[11], 16) / 1000))
        self.sb29.setText('{:.3f}V'.format(int(self.POWERstr[12], 16) / 1000))
        self.sb30.setText('{:.3f}A'.format(int(self.POWERstr[13], 16) / 1000))
        self.sb31.setText('{:.3f}V'.format(int(self.POWERstr[14], 16) / 1000))
        self.sb32.setText('{:.3f}A'.format(int(self.POWERstr[15], 16) / 1000))
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
    def showLOG(self, l1):
        if len(l1) < 34:
            return
        l1 = l1[22:-12]
        self.sb101 = [l1[i:i+4][-2:] for i in range(0, len(l1), 4)]
        self.sb102 = [l1[i:i+4][:2] for i in range(0, len(l1), 4)]
        self.sb48.setText(self.sb99[str(int(self.sb101[-1], 16))])
        for i in range(len(self.sb101)):
            print("进入循环")
            if self.sb102[i] == '00':
                self.right += 1
                print('这里是第一部分循环')
                print(self.sb99)
                c = f"{int(self.sb101[i], 16):<8}" + "{:<20}".format(self.sb99[str(int(self.sb101[i], 16))]) + '\tPASS\n'
                print('正确的c', c)
                # with open(self.id, 'a') as f1:
                #     self.writetolog(f1, test_part=self.sb99[str(int(self.sb101[i], 16))], test_part_status='OK')
            elif self.sb102[i] == '80':
                self.wrong += 1
                c = f"{int(self.sb101[i], 16):<8}" + "{:<20}".format(self.sb99[str(int(self.sb101[i], 16))]) + '\tFAIL\n'
                # with open(self.id, 'a') as f1:
                #     self.writetolog(f1, test_part=self.sb99[str(int(self.sb101[i], 16))], test_part_status="ERROR")
                print('错误的c', c)
            else:
                print("这里有问题")
                c = "这里有问题"
            print("正确的值", self.right)
            print("错误的值", self.wrong)
            self.sb55 += c
        self.sb34.setPlainText(self.sb55)
        self.sb34.verticalScrollBar().setValue(self.sb34.verticalScrollBar().maximum())

        # if self.right + self.wrong == self.tot:
        #     with open(self.id, 'a') as f1:
        #         self.writetolog(f1, right=self.right, wrong=self.wrong)

    # def rememberidandtime(self, id, time, tot):
    #     self.id = id
    #     self.tot = tot
    #     print("我已得到self.tot", self.tot)
        # with open(self.id, 'w') as f1:
        #     self.writetolog(f1, wid=self.id, tot=self.tot, tem1=1, tem2=2, dttime=time)

#     def writetologbegin(self, f1, *args, wid=None, tot=None, tem1=None, tem2=None, test_part=None, test_part_status=None,
#                    dttime=None, right=None, wrong=None):
#         if wid is not None:
#             s1 = f'''
# M02 TEST RECORD
# ID: {wid}
# TOTAL TEST: {tot}
# TEM: TEM_A: {tem1}, TEM_B: {tem2}
# DATA: {dttime}
# '''
#             f1.write(s1)
#         if test_part is not None:
#             s2 = f'''
# {test_part} {test_part_status}
# '''
#             f1.write(s2)
#         if len(args) != 0:
#             s5 = f'''
# POWER:
# VDD12V: {args[0]}, {args[0]}  VDD3V3: {args[0]}, {args[0]}
# VDDINT_A: {args[0]}, {args[0]}    VDDRAM_A: {args[0]}, {args[0]}    VDDIO_A: {args[0]}, {args[0]}
# VDDINT_B: {args[0]}, {args[0]}    VDDRAM_B: {args[0]}, {args[0]}    VDDIO_B: {args[0]}, {args[0]}
# '''
#         if right is not None:
#             if wrong == 0:
#                 s4 = "M02 TEST SUCCESSFUL"
#             else:
#                 s4 = "M02 TEST SAIL"
#             s3 = f'''
# M02 TEST RESULT
# OK: {right}
# ERROR: {wrong}
# {s4}
# DATA:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
# '''
#             f1.write(s3)

    def writetologbegin(self, id, dttime, recv, recv2):
        self.id = id
        self.total = int(recv[18:22], 16)
        sb100 = [int(recv2[16:-12][i:i+4],16)/1000 for i in range(0, len(recv2[16:-12]), 4)]
        print('sb100', sb100)
        s1 = f'''M02 TEST RECORD
ID: {self.id}
TOTAL TEST: {self.total}
TEM: TEM_A: {self.tem1}℃, TEM_B: {self.tem2}℃
VDD12V: {sb100[0]}V, {sb100[1]}A  
VDDINT_A: {sb100[2]}V, {sb100[3]}A    VDDRAM_A: {sb100[4]}V, {sb100[5]}A 
VDDIO_A: {sb100[6]}V, {sb100[7]}A   VDD2V3:{sb100[14]}V, {sb100[15]}A
VDDINT_B: {sb100[8]}V, {sb100[9]}A    VDDRAM_B: {sb100[10]}V, {sb100[11]}A  
VDDIO_B: {sb100[12]}V, {sb100[13]}A   VDD2V3:{sb100[14]}V, {sb100[15]}A
DATA: {dttime}



------------------start test-------------------
'''
        self.sb55 += s1
        print("self.sb55:", self.sb55)
        with open(self.id + ".txt", 'w') as f1:
            f1.write(s1)
    def writetolog(self, id, recv, recv2):
        if recv == '':
            sb103 = [int(recv2[16:-12][i:i + 4], 16) / 1000 for i in range(0, len(recv2[16:-12]), 4)]
            self.sbPOWER.append(sb103)
        if recv2 == '':
            if len(recv) < 34:
                return
            l1 = recv[22:-12]
            sb101 = [l1[i:i+4][-2:] for i in range(0, len(l1), 4)]
            sb102 = [l1[i:i+4][:2] for i in range(0, len(l1), 4)]
            with open(self.id + ".txt", 'a') as f1:
                for i in range(len(sb101)):
                    if sb102[i] == '00':
                        c = f"{int(self.sb101[i], 16):<8}" + "{:<50}".format(self.sb99[str(int(sb101[i], 16))]) + '\tPASS\n'
                        f1.write(c)
                    elif sb102[i] == '80':
                        c = f"{int(self.sb101[i], 16):<8}" + "{:<50}".format(self.sb99[str(int(sb101[i], 16))]) + '\tFAIL\n'
                        f1.write(c)
                    else:
                        c = f"{int(self.sb101[i], 16):<8}" + "{:<50}".format(self.sb99[str(int(sb101[i], 16))]) + '\tbad return\n'
                        f1.write(c)
        else:
            if len(recv) < 34:
                return
            self.temp += 1
            l1 = recv[22:-12]
            sb101 = [l1[i:i + 4][-2:] for i in range(0, len(l1), 4)]
            sb102 = [l1[i:i + 4][:2] for i in range(0, len(l1), 4)]
            sb103 = [int(recv2[16:-12][i:i+4],16)/1000 for i in range(0, len(recv2[16:-12]), 4)]
            # dp = f"VDD12V:{sb103[0]}, {sb103[1]}\tVDD3V3:{sb103[14]}, {sb103[15]}\tVDDINT_A:{sb103[2]}, {sb103[3]}\tVDDRAM_A:{sb103[4]}, {sb103[5]}\tVDDIO_A:{sb103[6]}, {sb103[7]}, VDDINT_B:{sb103[8]}, {sb103[9]}\tVDDRAM_B{sb103[10]}, {sb103[11]}\tVDDIO_B{sb103[12]}, {sb103[13]}"
            self.sbPOWER.append(sb103)
            # print('sb103', sb103)

            with open(self.id + ".txt", 'a') as f1:
                for i in range(len(sb101)-1):
                    if sb102[i] == '00':
                        c = f"{int(self.sb101[i], 16):<8}" + "{:<50}".format(self.sb99[str(int(sb101[i], 16))]) + '\tPASS\t' + '\n'
                        f1.write(c)
                    elif sb102[i] == '80':
                        c = f"{int(self.sb101[i], 16):<8}" + "{:<50}".format(self.sb99[str(int(sb101[i], 16))]) + '\tFAIL\t' + '\n'
                        f1.write(c)
                    else:
                        c = f"{int(self.sb101[i], 16):<8}" + "{:<50}".format(self.sb99[str(int(sb101[i], 16))]) + '\tbad return\t' + '\n'
                        f1.write(c)

            print("进到记录电压里的次数：", self.temp)


    def writetologend(self):
        t1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.sb63.setStyleSheet("background:red")
        if self.right == self.total:
            self.sb59.setStyleSheet("background:green")
            # s4 = "M02 TEST PASS"
            s4 = '''**********           **          ************     ************      
***********         ****         ************     ************  
**       **       **    **       **               **
**       **     **        **     **               **
***********     **        **     ************     ************  
**********      ************     ************     ************  
**              ************               **               **
**              **        **               **               **
**              **        **               **               **
**              **        **     ************     ************   
**              **        **     ************     ************  '''
        else:
            self.sb59.setStyleSheet("background:red")
            # s4 = "M02 TEST FAIL"
            s4 = '''**********          **             **        **     
**********         ****            **        ** 
**               **    **          **        **
**             **        **        **        **
**********     **        **        **        **
**********     ************        **        **
**             ************        **        **
**             **        **        **        **
**             **        **        **        **
**             **        **        **        ***********
**             **        **        **        ***********'''
        s3 = f'''


-----------------end--------------------
M02 TEST RESULT
TEST_TOTAL:{self.total}
OK: {self.right}
ERROR: {self.wrong}
{s4}
DATA:{t1}
'''
        s5 = f'''


-----------------end--------------------
M02 TEST RESULT
TEST_TOTAL:{self.total}
OK: {self.right}
ERROR: {self.wrong}
DATA:{t1}
'''
        self.sb55 += s3
        self.sb34.setPlainText(self.sb55)
        self.sb34.verticalScrollBar().setValue(self.sb34.verticalScrollBar().maximum())

        with open(self.id + ".txt", 'a') as f1:
            f1.write(s5)

        self.write_to_log_power()
        self.write_to_end(s4, t1)

    def write_to_log_power(self):
        l = [sum([self.sbPOWER[i][j] for i in range(len(self.sbPOWER))]) / len(self.sbPOWER) for j in range(len(self.sbPOWER[0]))]
        c = f'''-----------------Power(average)-------------------------
VDD12V: {l[0]:.3f}V, {l[1]:.3f}A  
VDDINT_A: {l[2]:.3f}V, {l[3]:.3f}A    VDDRAM_A: {l[4]:.3f}V, {l[5]:.3f}A 
VDDIO_A: {l[6]:.3f}V, {l[7]:.3f}A   VDD2V3:{l[14]:.3f}V, {l[15]:.3f}A
VDDINT_B: {l[8]:.3f}V, {l[9]:.3f}A    VDDRAM_B: {l[10]:.3f}V, {l[11]:.3f}A  
VDDIO_B: {l[12]:.3f}V, {l[13]:.3f}A   VDD2V3:{l[14]:.3f}V, {l[15]:.3f}A
'''
        with open(self.id + ".txt", 'a') as f1:
            f1.write(c)

        with open(self.id + ".txt", 'a') as f1:
            f1.write("---------------------------Power(abnormal)----------------------------\n")
            for i in self.sbPOWER:
                if i[0] < conf.VDD12V[0] or i[0] > conf.VDD12V[1] or i[1] < conf.VDD12V[2] or i[1] > conf.VDD12V[3]:
                    f1.write(f"VDD12V: {i[0]}V, {i[1]}A\t")
                if i[14] < conf.VDDD3V3_A[0] or i[14] > conf.VDDD3V3_A[1] or i[15] < conf.VDDD3V3_A[2] or i[15] > conf.VDDD3V3_A[3]:
                    f1.write(f"VDD3V3: {i[14]}V, {i[15]}A\t")
                if i[2] < conf.VDDINT_A[0] or i[2] > conf.VDDINT_A[1] or i[3] < conf.VDDINT_A[2] or i[3] > conf.VDDINT_A[3]:
                    f1.write(f"VDDINT_A: {i[2]}V, {i[3]}A\t")
                if i[4] < conf.VDDDRM_A[0] or i[4] > conf.VDDDRM_A[1] or i[5] < conf.VDDDRM_A[2] or i[5] > conf.VDDDRM_A[3]:
                    f1.write(f"VDDDRM_A: {i[4]}V, {i[5]}A\t")
                if i[6] < conf.VDDDIO_A[0] or i[6] > conf.VDDDIO_A[1] or i[7] < conf.VDDDIO_A[2] or i[7] > conf.VDDDIO_A[3]:
                    f1.write(f"VDDDIO_A: {i[6]}V, {i[7]}A\t")
                if i[8] < conf.VDDINT_B[0] or i[8] > conf.VDDINT_B[1] or i[9] < conf.VDDINT_B[2] or i[9] > conf.VDDINT_B[3]:
                    f1.write(f"VDDINT_B: {i[8]}V, {i[9]}A\t")
                if i[10] < conf.VDDDRM_B[0] or i[10] > conf.VDDDRM_B[1] or i[11] < conf.VDDDRM_B[2] or i[11] > conf.VDDDRM_B[3]:
                    f1.write(f"VDDINT_B: {i[8]}V, {i[9]}A\t")
                if i[12] < conf.VDDDIO_B[0] or i[12] > conf.VDDDIO_B[1] or i[13] < conf.VDDDIO_B[2] or i[13] > conf.VDDDIO_B[3]:
                    f1.write(f"VDDINT_B: {i[8]}V, {i[9]}A\n")


    def write_to_end(self, t, t1):
        with open(self.id + ".txt", "a") as f1:
            f1.write("----------------------data------------------------\n")
            f1.write(f"DATA:{t1}\n")
            f1.write("---------------------result------------------------\n")
            f1.write(t)












if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = classA()
    main.show()
    sys.exit(app.exec_())

