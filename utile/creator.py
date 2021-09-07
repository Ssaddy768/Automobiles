import random
import entity.cars


class Creator:
    BRANDS = ("Mercedes", "BMW", "Opel", "Ford", "Mazda", "Skoda", "Toyota")

    MAX_COST = 100000
    MIN_COST = 5000

    MAX_POWER = 1000
    MIN_POWER = 100

    MAX_SPEED = 300
    MIN_SPEED = 180

    MAX_YEAR = 1900
    MIN_YEAR = 1600

    MAX_ECO = 5
    MIN_ECO = 1

    MAX_COUNT = 100
    MIN_COUNT = 1



    def create_car(self, size):

        RARITY_LIST = tuple(map(int, [random.randint(0, size) for _ in range(5)]))

        cars = []

        while size:

            brand = random.choice(self.BRANDS)
            model = chr(random.randint(ord('A'), ord('Z')))
            cost = random.randrange(self.MIN_COST, self.MAX_COST, 100)
            power = random.randint(self.MIN_POWER, self.MAX_POWER)
            max_speed = random.randrange(self.MIN_SPEED, self.MAX_SPEED, 10)
            car = entity.cars.Car(brand, model, cost, power, max_speed)

            if RARITY_LIST.count(size):
                year = random.randrange(self.MIN_YEAR, self.MAX_YEAR, 10)
                count = random.randrange(self.MIN_COUNT, self.MAX_COUNT, 10)
                eco = random.randrange(self.MIN_ECO, self.MAX_ECO,1)
                car = entity.cars.RarityCar(brand, model, cost, power, max_speed, year, count, eco)

            cars.append(car)
            size -= 1

        return cars
