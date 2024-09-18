class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            floor_list = [int(x) for x in range(1, new_floor+1)]
            for i in floor_list:
                print(i)

    def __eq__(self, other):
        if isinstance(other, House) and self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, House) and self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        if isinstance(other, House) and self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, House) and self.number_of_floors > other.number_of_floors:
                return True
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, House) and self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House) and self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return h1


    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print("eq: ", h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print("eq: ", h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print("gt: ", h1 > h2)
print("ge: ", h1 >= h2)
print("lt: ", h1 < h2)
print("le: ", h1 <= h2)
print("ne: ", h1 != h2)
