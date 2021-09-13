class Fighter:
    def __init__(self, name, health, rang, power):
        self.name = name
        self.health = health
        self.rang = rang
        self.power = power

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if 0 <= value <= 100:
            self.__health = value
        else:
            print(f'{self.name}`s {value} health is impossible. Health will be set 100')
            self.__health = 100

    health = property(get_health, set_health)

    def get_rang(self):
        return self.__rang

    def set_rang(self, value):
        if value in range(1, 4):
            self.__rang = value
        else:
            print(f'{self.name}`s {value} rang is impossible. Rang will be set 1')
            self.__rang = 1

    rang = property(get_rang, set_rang)

    def get_power(self):
        return self.__power

    def set_power(self, value):
        if 0 <= value <= (self.health * 0.1):
            self.__power = value
        else:
            print(self.name, 'have a limit of power. Power will be set', (self.health * 0.1))
            self.__power = (self.health * 0.1)

    power = property(get_power, set_power)

    def hit(self, name):
        if name.health >= 5:
            name.health = name.health - self.power
        else:
            print(self.name, "you can't beat the weak", name.name)
        name.set_power()

    def set_power(self):
        if self.power > (self.health * 0.1):
            self.power = (self.health * 0.1)
        else:
            pass


johnyy = Fighter('Johnyy', 120, 1, 1)
michael = Fighter('Michael', 100, 5, 20)
print(johnyy.name, 'health =', johnyy.health, 'rang =', johnyy.rang, 'power =', johnyy.power)
print(michael.name, 'health =', michael.health, 'rang =', michael.rang, 'power =', michael.power)

johnyy.hit(michael)
print(michael.name, 'health =', michael.health, 'rang =', michael.rang, 'power =', michael.power)
