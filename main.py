import entity.manager
import utile.creator
import utile.convertor

if __name__ == '__main__':

    cars = utile.creator.Creator().create_car(20)
    s = utile.convertor.Convertor().convert_to_str(cars)
    print(s)

    brand = input("Enter brand: ")
    result = entity.manager.Manager().search_brand(brand, cars)
    s = utile.convertor.Convertor().convert_to_str(result)
    print(s)

    ls = entity.manager.Manager().the_most_expensive_car(cars)
    s = utile.convertor.Convertor().convert_to_str(ls)
    print("The most expensive car: \n", s)

    cost = entity.manager.Manager().all_cost(cars)
    print("Total value car showroom: ", cost)

    cost = int(input("\nEnter price: "))
    ls = entity.manager.Manager().cars_in_cost(cars, cost)
    s = utile.convertor.Convertor().convert_to_str(ls)

    print("\nCars in your price: \n", s)




