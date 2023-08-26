'''
Шаблон Наблюдатель:
Реализуйте паттерн Наблюдатель на языке Python для 
системы уведомлений. Создайте класс 
NotificationSystem (наблюдаемый объект), который будет 
иметь методы для добавления наблюдателей и уведомления 
о событиях. Создайте несколько наблюдателей, 
реагирующих на уведомления.
'''

class NotificationSystem:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

class EmailNotif(NotificationSystem):
    def update(self, message):
        print("Recerved message:",message)
    
class Observer:
    def update(self, message):
        pass

class SmsNotif(NotificationSystem):
    def update(self, message):
        print("Recerved message:",message)


subject = NotificationSystem()

em_not = EmailNotif()
sms_not = SmsNotif()

subject.add_observer(em_not)
subject.add_observer(sms_not)

subject.notify_observers("Сообщение")