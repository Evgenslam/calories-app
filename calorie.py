from temperature import Temperature


class Calorie:
    """
    Reprepsents the amount of calories calculated with formula
    """
    def __init__(self, weight, height, age, temperature):
        self.weight = int(weight)
        self.height = int(height)
        self.age = int(age)
        self.temperature = temperature


    def calculate(self):
        result = 10*self.weight + 6.25*self.height - 5*self.age + 5 - 10*self.temperature
        return result
    

if __name__ == '__main__':
    temperature = Temperature(country='Japan', city='Naha').get()
    calorie = Calorie(weight=87, height=175, age=37, temperature=temperature)
    print(temperature)
    print(calorie.calculate())
