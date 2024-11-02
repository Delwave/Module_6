class Animal:

    def __init__(self, name):
        self.name = name    # Аттрибуты, общие для всех животных (имя)
        self.alive = True # Аттрибуты, общие для всех животных (живой/мертвый)
        self.fed = False    # Аттрибуты, общие для всех животных (едят/недоедят)

    def eat(self,food):    # Метод, общий для всех млекопитающих
        if food.edible:    # Если еда сьедобна
            print(f'{self.name} ест {food.name}')  # Выводится сообщение о еде
            self.fed = True     # Метод меняет состояние "едят"
        else:
            print(f'{self.name} не может есть {food.name}')
            self.alive = False


class Plant:
    def __init__(self, name):
        self.name = name    # Аттрибуты, общие для всех растений (имя)
        self.edible = False # Аттрибуты, общие для всех растений (недоеденный)




class Mammal(Animal):      # Класс Млекопитающее наследует от Animal
    pass

class Predator(Mammal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)