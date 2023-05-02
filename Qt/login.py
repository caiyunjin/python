from PySide6.QtWidgets import QWidget, QMessageBox
from UI.login_ui import Ui_Form


class LoginWindow(QWidget):
    def __init__(self, mainWindow):
        super(LoginWindow, self).__init__()
        # 保存好父窗口，用于登录后显示父窗口
        self.parent = mainWindow
        # 创建ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 显示自己
        self.show()
        self.ui.pushButton.clicked.connect(self.btn1)

    # 注意这里名称与界面中设定的一致
    def btn1(self):
        uname = self.ui.lineEdit.text()
        pw = self.ui.lineEdit_2.text()
        if uname == "1" and pw == "1":
            self.close()
            self.parent.show()
        else:
            QMessageBox.warning(self, "信息提示", "用户名或密码错误！")
