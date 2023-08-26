'''
Шаблон Singleton:
Реализуйте паттерн Singleton на языке Python для 
класса Logger, который будет использоваться для 
логирования информации в приложении. Гарантируйте, 
что только один экземпляр класса Logger будет создан.
'''

class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance

    def log(self, message):
        print(message)



logger1 = Logger()
logger2 = Logger()

logger1.log("Сообщение")  
logger2.log("Другое сообщение")  

print(logger1 is logger2)  