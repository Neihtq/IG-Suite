from PyQt5.QtWidgets import QDialog, QDateTimeEdit, QVBoxLayout, QHBoxLayout, QCalendarWidget, QPushButton
from PyQt5.QtCore import QDate, QDateTime
from instagram_api import InstagramLib
from datetime import datetime
from threading import Timer


class Scheduler(QDialog):
    def __init__(self, photo, caption, ig):
        super(Scheduler, self).__init__()
        self.photo = photo
        self.caption = caption
        self.ig = ig
        self.init_ui()
        self.exec_()


    def init_ui(self):
        self.setWindowTitle("Schedule Post")
        self.date_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.date_edit.setDisplayFormat("dd.MM.yyyy hh:mm")
        self.date_edit.setMinimumDateTime(QDateTime.currentDateTime())

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)

        self.calendar.setMinimumDate(QDate.currentDate())
        self.calendar.setSelectedDate(QDate.currentDate())
        self.calendar.clicked.connect(self.set_date_time)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.set_schedule)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.calendar)
        vbox.addWidget(self.confirm_button)


    def set_date_time(self, qDate):
        self.date_edit.setDate(qDate)


    def set_schedule(self):
        self.date_time = self.date_edit.dateTime()
        schedule = self.date_time.toPyDateTime()
        now = datetime.now()
        delta_t = schedule - now
        secs = delta_t.seconds + 1

        t = Timer(secs, self.ig.upload, [self.photo, self.caption])
        t.start()

        self.accept()


