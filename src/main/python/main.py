from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QDialog, QFileDialog, QLineEdit, QDialogButtonBox, QFormLayout, QLabel, QVBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from instagram_api import InstagramLib
from scheduler import Scheduler


import sys

class IGSuite(QWidget):
    def __init__(self):
        super(IGSuite, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IG Suite")
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.open_login_dialog)
        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_filename_dialog)
        self.caption_label = QLabel("Caption")
        self.caption_box = QPlainTextEdit()
        self.caption_box.setPlaceholderText("#ootd #photooftheday #travel")
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.upload)
        self.scheduled_ul_button = QPushButton("Scheduled Upload")
        self.scheduled_ul_button.clicked.connect(self.set_schedule)
        self.clear_button = QPushButton("Unfollow non-followers")
        self.clear_button.clicked.connect(self.unfollow_unfollowers)

        self.img_view = QLabel(self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.login_button)
        hbox.addWidget(self.open_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.caption_label)
        vbox.addWidget(self.caption_box)
        hbox = QHBoxLayout()
        hbox.addWidget(self.upload_button)
        hbox.addWidget(self.scheduled_ul_button)
        vbox.addLayout(hbox)
        vbox.addWidget(self.clear_button)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.img_view)

        self.setLayout(hbox)
        self.show()


    def open_login_dialog(self):
        self.dialog = QDialog()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout = QFormLayout(self.dialog)
        layout.addRow("Username", self.username)
        layout.addRow("Password", self.password)
        layout.addWidget(button_box)

        button_box.accepted.connect(self.login)
        button_box.rejected.connect(self.dialog.reject)

        self.dialog.exec_()


    def login(self):
        try:
            self.ig = InstagramLib(self.username.text(), self.password.text())
            self.dialog.accept()
        except:
            dlg = QDialog()
            ok = QPushButton("ok", dlg)
            dlg.setWindowTitle("Login failed")
            dlg.setWindowModality(QtCore.Qt.ApplicationModal)
            dlg.exec_()


    def open_filename_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '~')
        self.path = fname[0]
        self.pixmap = QPixmap(self.path)
        self.pixmap = self.pixmap.scaled(1024, 1024, QtCore.Qt.KeepAspectRatio)
        self.img_view.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())


    def upload(self):
        caption = self.caption_box.toPlainText()
        self.ig.upload(self.path, caption)


    def set_schedule(self):
        caption = self.caption_box.toPlainText()
        self.scheduler = Scheduler(self.path, caption, self.ig)


    def unfollow_unfollowers(self):
        self.ig.unfollow_non_followers()


if __name__ == '__main__':
    appctxt = ApplicationContext()
    app = IGSuite()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)