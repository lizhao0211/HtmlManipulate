import sys
import MainWinHorLayout
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    mainWindow = QMainWindow()
    ui = MainWinHorLayout.UI_MainWindow
    ui.setupUi(mainWindow)
    mainWindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())