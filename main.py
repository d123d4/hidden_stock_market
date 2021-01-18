from KeywordTransformationMethod import KeywordMethod
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)
    keywordRun = KeywordMethod()
    keywordRun.show()
    sys.exit(app.exec_())
