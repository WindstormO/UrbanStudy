class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
        
    def go_to(new_floor):
        if new_floor > self.number_of_floors:
            print("нет такого этажа")
        else:
            for floor in new_floor:
                print(floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
#h2.go_to(10)                
