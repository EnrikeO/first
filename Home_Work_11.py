class Fighter:
    def __init__(self, name, health=100, rang=1, power=1, money=0):
        self.name = name
        self.health = health
        self.rang = rang
        self.money = money
        if 0 <= power <= (self.health * 0.1):
            self.power = power
        else:
            print(self.name, 'have a limit of power. Power will be set', (self.health * 0.1))
            self.power = int((self.health * 0.1))

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if 0 <= value <= 100:
            self.__health = int(value)
        else:
            if value > 100:
                print(f'{self.name}`s {value} health is impossible. Health will be set 100')
                self.__health = 100
            elif value < 0:
                self.__health = 0

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

    def hit(self, name):
        if name.health >= 5:
            name.health = round(name.health - self.power, 1)
            name.power = round(name.power - (self.power * 0.1), 1)
            if name.health < 5:
                print(f'{name.name} won and takes {name.money} coins')
                self.money = self.money + name.money
                name.money = 0
        else:
            print(self.name, "you can't beat the weak", name.name)


class Wizard(Fighter):
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)

    def heal(self, name):
        while name.health < 100 and name.money > 0:
            name.health = name.health + 1
            name.power = round(name.power + 0.1, 1)
            name.money = name.money - 1
            self.money = self.money + 1


priest = Wizard('Priest', 100, 1, 1, 10)
johnyy = Fighter('Johnyy', 100, 1, 8, 30)
michael = Fighter('Michael', 100, 1, 10, 50)

print(johnyy.name, 'health =', johnyy.health, 'rang =', johnyy.rang, 'power =', johnyy.power, 'money =', johnyy.money)
print(michael.name, 'health =', michael.health, 'rang =', michael.rang, 'power =', michael.power, 'money =', michael.money)
print(priest.name, 'health =', priest.health, 'rang =', priest.rang, 'power =', priest.power, 'money =', priest.money)
print('!!!!!!!!!!!!!!!!!!!!!!')
johnyy.hit(michael)
johnyy.hit(michael)
johnyy.hit(michael)
michael.hit(johnyy)

print(johnyy.name, 'health =', johnyy.health, 'rang =', johnyy.rang, 'power =', johnyy.power, 'money =', johnyy.money)
print(michael.name, 'health =', michael.health, 'rang =', michael.rang, 'power =', michael.power, 'money =', michael.money)
print('!!!!!!!!!!!!!!!!!!!!!!')
priest.heal(michael)
priest.heal(johnyy)
print(michael.name, 'health =', michael.health, 'rang =', michael.rang, 'power =', michael.power, 'money =', michael.money)
print(johnyy.name, 'health =', johnyy.health, 'rang =', johnyy.rang, 'power =', johnyy.power, 'money =', johnyy.money)
print(priest.name, 'health =', priest.health, 'rang =', priest.rang, 'power =', priest.power, 'money =', priest.money)
