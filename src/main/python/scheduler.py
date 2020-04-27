from PyQt5.QtWidgets import QDialog, QDateTimeEdit, QVBoxLayout, QHBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate, QDateTime

class Scheduler(QDialog):
    def __init__(self):
        super(Scheduler, self).__init__()
        self.init_ui()
        self.exec_()


    def init_ui(self):
        self.setWindowTitle("Schedule Post")
        self.date_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.date_edit.setDisplayFormat("dd.MM.yyyy hh:mm")

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)

        self.calendar.setMinimumDate(QDate.currentDate())
        self.calendar.setSelectedDate(QDate.currentDate())
        self.calendar.clicked.connect(self.print_date_time)


        vbox = QVBoxLayout(self)
        vbox.addWidget(self.date_edit)
        vbox.addWidget(self.calendar)


    def print_date_time(self, qDate):
        print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        print(f'Day Number of the year: {qDate.dayOfYear()}')
        print(f'Day Number of the week: {qDate.dayOfWeek()}')


