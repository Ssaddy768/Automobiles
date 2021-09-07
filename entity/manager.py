class Manager:

    @staticmethod
    def search_brand(brand, cars):

        if isinstance(cars, list):
            ls = []
            for car in cars:
                if brand == car.brand:
                    ls.append(car)

            return ls

    @staticmethod
    def the_most_expensive_cost(cars):

        if isinstance(cars, list):
            max_cost = 0
            for car in cars:
                if max_cost < car.cost:
                    max_cost = car.cost
            return max_cost

    def the_most_expensive_car(self, cars):

        if isinstance(cars, list):
            ls = []
            cost = self.the_most_expensive_cost(cars)
            for car in cars:
                if cost == car.cost:
                    ls.append(car)
            return ls

    @staticmethod
    def all_cost(cars):

        if isinstance(cars, list):
            cost = 0
            for car in cars:
                cost += car.cost

            return cost

    @staticmethod
    def cars_in_cost(cars, cost1):
        if isinstance(cars, list):
            ls = []
            for car in cars:
                if car.cost <= cost1:
                    ls.append(car)

            return ls



