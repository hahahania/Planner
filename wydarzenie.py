
from datetime import datetime

current_date = datetime.now()


class Event():
    # klasa tworząca wydarzenie
    def __init__(self, name='',  execution_date='', execution_time='', priority='', execution_level='', category='', description=''):
        self.execution_time = execution_time
        self.execution_date = execution_date
        self.priority = priority
        self.execution_level = execution_level
        self.category = category
        self.name = name
        self.description = description

        self.date_of_creating = datetime.today().strftime('%Y-%m-%d')
        self.time_of_creating = current_date.strftime("%H:%M")
        self.update_date = None
        self.update_time = None

    # funkcja pozwalająca stworzyć string z klasy
    def __str__(self):
        return (f'Event name : {self.name}\nDate : {self.execution_date}\nTime : {self.execution_time}\nPriority : {self.priority}\nexecution level : {self.execution_level}\nCategory : {self.category}\nDescription : {self.description}')

    # tworzenie listy z wydarzenia
    def creating_list(self):
        return [self.name, self.execution_date, self.execution_time, self.priority, self.execution_level, self.category, self.description, self.date_of_creating, self.time_of_creating, self.update_date, self.update_time]

    # zmienienie daty aktualizacji
    def update(self):
        self.update_date = datetime.today().strftime('%Y-%m-%d')
        self.update_time = current_date.strftime("%H:%M")
