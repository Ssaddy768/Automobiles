class Convertor:

    @staticmethod
    def convert_to_str(cars):
        s = ""
        if isinstance(cars, list):
            for car in cars:
                s += str(car) + "\n"

        return s
