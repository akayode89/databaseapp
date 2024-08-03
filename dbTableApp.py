from database.table import DBTable
from vehicles.fourwheelers.hector import Hector

if __name__ == "__main__":
    h1 = Hector()
    h1.speed_up(40)

    h2 = Hector()
    h2.speed_up(20)

    h3 = Hector()
    h3.speed_up(60)

    h4 = Hector()
    h4.speed_up(90)

    cars_table = DBTable("CARS", "C:/Users/*****/database/my-cars")
    cars_table1 = DBTable("TRUCKS", "C/Users/*****/database/my-cars")
    cars_table.insert("h1", h1)
    cars_table.insert("h2", h2)
    cars_table.insert("h3", h3)
    cars_table.insert("h4", h4)
    cars_table1.insert("h1", h1)
    print(cars_table.db)
    cars_table.save()
    cars_table1.save()
    print(cars_table.select("h4"))
