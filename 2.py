'''
ООП Концепции:
Создайте класс Person, который имеет атрибуты name, age и метод introduce(), 
выводящий информацию о человеке. Создайте несколько объектов этого класса и 
вызовите метод introduce() для каждого из них.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Хей, мое имя {self.name} и мой возраст {self.age} лет")

        
person1 = Person("Ирина", 26)
person2 = Person("Катя", 27)

print(person1.name)  
print(person2.age) 

person1.introduce()
person2.introduce()