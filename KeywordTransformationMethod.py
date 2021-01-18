from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from KeywordTransformationUI import KeywordUI
timer =QTimer()

class KeywordMethod(KeywordUI):

    def __init__(self):

        super().__init__()
        self.initMethod()

    def initMethod(self):

        # self.inputTextEdit.textChanged.connect(self.transformationButtonMethod)
        # 注册函数到定时器
        timer.timeout.connect(self.transformationButtonMethod)
        # 设置计时器间隔并启动
        timer.start(1000)
        self.left_close.clicked.connect(self.closeMethod)

    def closeMethod(self):

        self.close()

    def transformationButtonMethod(self):

        # inputKeywords = self.inputTextEdit.toPlainText()
        # outputKeywords = ""

        fileOperate = open('temp1.txt', 'r')
        my_str = fileOperate.read()
        fileOperate.close()

        # 这里的转化算法可以优化,判断顺序的优化

        # for input_chr in inputKeywords:
        #
        #     if input_chr == ",":
        #
        #         outputKeywords += " "
        #
        #     elif input_chr == " ":
        #
        #         outputKeywords += ","
        #
        #     else:
        #
        #         outputKeywords += input_chr

        self.outputTextEdit.setText(my_str)
