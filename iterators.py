class Houses:
    def __init__(self, collections=None):
        self.houses = {}
        if collections:
            for k,v in collections.items():
                self.add_house(k,v)

    def __str__(self):
        result = ""
        for key, value in self.houses.items():
            r = ""
            for i in value:
                r += i + ", "
            result += "House: " + key + "; Residents: " + r + "\n"
        return result

    def __iter__(self):
        def generator():
            for k in self.houses:
                yield k
        return generator()

    def __len__(self):
        return len(self.houses.keys())

    def __eq__(self, other):
        return self.houses.keys() == other.houses.keys()

    def __getitem__(self, house):
        if not self.houses[house]:
            raise KeyError
        return self.houses[house]

    def add_house(self, house, residents):
        self.houses[house] = residents

    def add_residents(self, house, residents):
        for resident in residents:
            if resident not in self.houses[house]:
                self.houses[house].append(resident)

if __name__ == '__main__':
    # data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"], "HuntedHouse":["Morticia", "Wednesday", "Gomez"]}
    # houses = Houses(data)
    #
    # #__str__
    # print(houses)
    #
    # #__iter__
    # for h in houses:
    #     print(h)
    #
    # #__len__
    # print(len(houses))
    # # houses.add_house("12345house", ["Joy", "Henry", "Tim"])
    # # print(len(houses))
    #
    # #__eq__
    # new_data = {"Hogwarts": [""], "Hell Kichen": [""],
    #         "HuntedHouse": [""]}
    # another_house = Houses(new_data)
    # print(houses == another_house)