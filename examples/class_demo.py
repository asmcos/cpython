class JeapeSite:
    n = "demo"

    def get_name(self):
        return "jeapedu"


a = JeapeSite()
print(a.n)
print(a.get_name())


class JeapeSite1:
    n = "demo"

    def __init__(self):
        self.data = ["1", 2, 3, "456"]

    def get_name(self):
        return "jeapedu"

    def set_name(self, name):
        self.name = name


b = JeapeSite1()
print(b.data)
b.set_name("jeapedu1")
print(b.name)


class JeapeSite2:
    def __init__(self, name):
        self.data = ["1", 2, 3, "456"]
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


c = JeapeSite2("jeapedu2")
print(c.get_name())
c.set_name("2jeapedu")
print(c.get_name())
