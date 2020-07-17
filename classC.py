import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class classC(QTabWidget):
    update_temp1 = pyqtSignal(float)
    update_temp2 = pyqtSignal(float)
    update_temp3 = pyqtSignal(str)
    def __init__(self, self1):
        self.self1 = self1
        super(classC, self).__init__()
        self.setWindowTitle("Setup")
        # self.setGeometry(900, 400, 220, 130)

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, "温度")
        self.addTab(self.tab2, "其他")

        self.tab1UI()

    def tab1UI(self):

        self.label0 = QLabel("芯片温度（℃）")
        self.label1 = QLabel("M02_A")
        self.label2 = QLabel("M02_B")
        self.label3 = QLabel("")
        self.label4 = QLabel("批次")
        self.label5 = QLabel("片号")
        self.lineEdit1 = QLineEdit()
        self.qdouble1 = QDoubleValidator()
        self.lineEdit1.setValidator(self.qdouble1)
        self.lineEdit2 = QLineEdit()
        self.qdouble2 = QDoubleValidator()
        self.lineEdit2.setValidator(self.qdouble2)
        self.lineEdit4 = QLineEdit()
        self.spinBox5 = QSpinBox()
        self.spinBox5.setMaximum(10000)
        self.pushButton1 = QPushButton()
        self.pushButton1.setText("加载")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("加载")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("加载")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)

        self.layout1 = QHBoxLayout()
        self.layout1.addWidget(self.label0)

        self.layout2 = QGridLayout()
        self.layout2.addWidget(self.label1, 0, 0, 1, 1)
        self.layout2.addWidget(self.label2, 1, 0, 1, 1)
        self.layout2.addWidget(self.lineEdit1, 0, 1, 1, 1)
        self.layout2.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.layout2.addWidget(self.pushButton1, 0, 2, 1, 1)
        self.layout2.addWidget(self.pushButton2, 1, 2, 1, 1)

        self.layout3 = QHBoxLayout()
        self.layout3.addWidget(self.label3)

        self.layout4 = QGridLayout()
        self.layout4.addWidget(self.label4, 0, 0, 1, 1)
        self.layout4.addWidget(self.label5, 1, 0, 1, 1)
        self.layout4.addWidget(self.lineEdit4, 0, 1, 1, 1)
        self.layout4.addWidget(self.spinBox5, 1, 1, 1, 1)
        self.layout4.addWidget(self.pushButton3, 0, 2, 2, 1)

        self.layout0 = QVBoxLayout()
        self.layout0.addLayout(self.layout1)
        self.layout0.addLayout(self.layout2)
        self.layout0.addLayout(self.layout3)
        self.layout0.addLayout(self.layout4)

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

    def pushButton3Clicked(self):
        if self.lineEdit4.text() == '' or self.spinBox5.text() == '0':
            QMessageBox.critical(self, '错误', '请输入正确的批次和芯片号', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        print(f"{self.lineEdit4.text()}{self.spinBox5.text():>04}")
        self.update_temp3.emit(f"{self.lineEdit4.text()}{self.spinBox5.text():>04}")
        QMessageBox.information(self, "正确", "信息加载完成", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = classC(1)
    main.show()
    sys.exit(app.exec_())