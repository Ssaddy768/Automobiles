class Car:

    def __init__(self, brand, model, cost, power, max_speed):
        self.__brand = brand
        self.__model = model
        self.__cost = cost
        self.__power = power
        self.__max_speed = max_speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, __brand):
        self.__brand = __brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, __model):
        self.__model = __model

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, __cost):
        self.__cost = __cost

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, __power):
        self.__power = __power

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, __max_speed):
        self.__max_speed = __max_speed

    def __str__(self):
        return f"Brand: {self.__brand}, " \
               f"Model: {self.__model}, " \
               f"Cost: {self.__cost}, " \
               f"Power: {self.__power}, " \
               f"Max speed: {self.__max_speed}. "

    # def __del__(self):
    #     print("Объект удален!")


class RarityCar(Car):

    def __init__(self, brand, model, cost, power, max_speed, year, count, eco):
        super().__init__(brand, model, cost, power, max_speed)
        self.__year = year
        self.__count = count
        self.__eco = eco

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, __year):
        self.__year = __year

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, __count):
        self.__year = __count

    @property
    def eco(self):
        return self.__eco

    @eco.setter
    def eco(self, __eco):
        self.__eco = __eco


    def __str__(self):
        return "Rarity car: " \
               f"Brand: {self.brand}, " \
               f"Model: {self.model}, " \
               f"Cost: {self.cost}, " \
               f"Power: {self.power}, " \
               f"Max speed: {self.max_speed}, " \
               f"Year: {self.year}. " \
               f"Count in world: {self.count}. " \
               f"Eco : {self.eco}. "


