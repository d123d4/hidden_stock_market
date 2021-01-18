from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
SCREEN_WEIGHT = 1920
SCREEN_HEIGHT = 1080
WINDOW_WEIGHT = 500
WINDOW_HEIGHT = 100


class KeywordUI(QWidget):

    def __init__(self):
        self.moved = False
        super().__init__()
        self.initUI()

    def initUI(self):

        # 初始化窗口大小
        # 创建输入文本框
        # 创建一个垂直布局 和 输出文本框
        # 并将其加入到主界面之中

        self.resize(500, 100)
        self.left_close = QPushButton("")

        # self.inputTextEdit = QTextEdit()
        self.outputTextEdit = QTextEdit()

        self.mainLayout = QGridLayout()
        self.mainLayout.setSpacing(8)

        self.mainLayout.addWidget(self.left_close, 1, 0, 1, 6)
        # self.mainLayout.addWidget(self.inputTextEdit, 2, 0, 4, 6)
        self.mainLayout.addWidget(self.outputTextEdit, 6, 0, 4, 6)

        self.setLayout(self.mainLayout)

        self.left_close.setFixedSize(15, 15)
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')

        self.setStyleSheet(
            '''QTextEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
                    color:#555555;
                    font-size:13px;
            }
            '''
        )
        self.setWindowOpacity(0.5)  # 设置窗口透明度
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #         self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag = False
    #     self.setCursor(QCursor(Qt.ArrowCursor))

    def enterEvent(self, event):
        self.hide_or_show('show', event)

    def leaveEvent(self, event):
        self.hide_or_show('hide', event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry(
            ).topLeft()
            QApplication.postEvent(self, QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            try:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
            except:pass

    def hide_or_show(self, mode, event):
        pos = self.frameGeometry().topLeft()
        if mode == 'show' and self.moved:
            if pos.x() + WINDOW_WEIGHT >= SCREEN_WEIGHT:  # 右侧显示
                self.startAnimation(SCREEN_WEIGHT - WINDOW_WEIGHT + 2, pos.y())
                event.accept()
                self.moved = False
            elif pos.x() <= 0:  # 左侧显示
                self.startAnimation(0,pos.y())
                event.accept()
                self.moved = False
            elif pos.y() <= 0: # 顶层显示
                self.startAnimation(pos.x(),0)
                event.accept()
                self.moved = False
        elif mode == 'hide':
            if pos.x() + WINDOW_WEIGHT >= SCREEN_WEIGHT:  # 右侧隐藏
                self.startAnimation(SCREEN_WEIGHT - 2,pos.y())
                event.accept()
                self.moved = True
            elif pos.x() <= 2:  # 左侧隐藏
                self.startAnimation(2 - WINDOW_WEIGHT,pos.y())
                event.accept()
                self.moved = True
            elif pos.y() <= 2: # 顶层隐藏
                self.startAnimation(pos.x(),2 - WINDOW_HEIGHT)
                event.accept()
                self.moved = True

    def startAnimation(self,width,height):
        animation = QPropertyAnimation(self,b"geometry",self)
        startpos = self.geometry()
        animation.setDuration(200)
        newpos = QRect(width,height,startpos.width(),startpos.height())
        animation.setEndValue(newpos)
        animation.start()
