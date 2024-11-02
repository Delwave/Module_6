class Horse:                 # Создаётся класс лошадь
    def __init__(self):      # Конструктор лошади
        super().__init__()
        self.x_distance = 0  # Пройденное расстояние
        self.sound = "Frr"   # Звук лошади

    def run(self, dx):   # Метод лошади, который изменяет расстояние
        self.x_distance += dx   # Увеличивает пройденное расстояние на dx
        return self.x_distance   # Возвращает текущее пройденное расстояние



class Eagle:    # Создаётся класс орла
    def __init__(self):  # Конструктор орла
        super().__init__()   # Вызывает конструктор родительского класса
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repear'   # Звук орла

    def fly(self, dy):    # Метод орла, который изменяет расстояние
        self.y_distance += dy  # Увеличивает пройденное расстояние на dy
        return self.y_distance   # Возвращает текущее пройденное расстояние


class Pegasus(Horse, Eagle):   # Создаётся класс пегаса, наследуется от Horse и Eagle
    def __init__(self):  # Конструктор пегаса
        super().__init__()   # Вызывает конструктор родительского класса
        Eagle.__init__(self)  # Вызывает конструктор Eagle

    def move(self, dx, dy):   # Метод пегаса, который изменяет расстояние
        super().run(dx)    # Вызывает run из родительского класса
        super().fly(dy)    # Вызывает fly из родительского класса

    def get_pos(self):          # Метод пегаса, который возвращает текущее положение
        return self.x_distance, self.y_distance   # Возвращает текущее положение пегаса

    def voice(self):    # Метод пегаса, который выводит звук
        print(self.sound)    # Выводит звук пегаса





p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()


