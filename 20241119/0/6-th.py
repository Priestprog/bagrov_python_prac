class C:
    @property
    def age(self):
        if self.a == 42:
            print("Secret")
            return -1
        return self.a

    @age.setter
    def age(self, value):
        if value > 128:
            raise ValueError("Too old")
        self.a = value

c = C()
c.age = 43
print(c.age)
c.age = 130
