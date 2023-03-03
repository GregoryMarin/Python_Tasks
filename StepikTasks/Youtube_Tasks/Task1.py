class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'age:', self.age, 'isHappy:', self.isHappy)

cat1 = Cat('Borsh', 4, True)
cat2 = Cat('Plov', 3, False)
