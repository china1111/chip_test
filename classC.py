import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class classC(QTabWidget):
    update_temp1 = pyqtSignal(float)
    update_temp2 = pyqtSignal(float)
    def __init__(self, self1):
        self.self1 = self1
        super(classC, self).__init__()
        self.setWindowTitle("Setup")
        self.setGeometry(900, 400, 220, 130)

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, "温度")
        self.addTab(self.tab2, "其他")

        self.tab1UI()

    def tab1UI(self):

        self.label0 = QLabel("芯片温度（℃）")
        self.label1 = QLabel("M02_A")
        self.label2 = QLabel("M02_B")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton1 = QPushButton()
        self.pushButton1.setText("加载")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("加载")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)

        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.label0)

        self.layout2 = QGridLayout()
        self.layout2.addWidget(self.label1, 0, 0, 1, 1)
        self.layout2.addWidget(self.label2, 1, 0, 1, 1)
        self.layout2.addWidget(self.lineEdit1, 0, 1, 1, 1)
        self.layout2.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.layout2.addWidget(self.pushButton1, 0, 2, 1, 1)
        self.layout2.addWidget(self.pushButton2, 1, 2, 1, 1)

        self.layout0 = QVBoxLayout()
        self.layout0.addLayout(self.layout1)
        self.layout0.addLayout(self.layout2)

        self.tab1.setLayout(self.layout0)

    def closeEvent(self, event):
        self.self1.setEnabled(True)
        # pass

    def pushButton1Clicked(self):
        if self.lineEdit1.text() == '':
            temp1 = -100
        elif self.lineEdit1.text().isdigit():
            temp1 = float(self.lineEdit1.text())
        else:
            print("数据输入错误！请输入数字")
            return
        self.update_temp1.emit(temp1)

    def pushButton2Clicked(self):
        if self.lineEdit2.text() == '':
            temp2 = -100
        elif self.lineEdit2.text().isdigit():
            temp2 = float(self.lineEdit2.text())
        else:
            print("数据输入错误！请输入数字")
            return
        self.update_temp2.emit(temp2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = classC(1)
    main.show()
    sys.exit(app.exec_())