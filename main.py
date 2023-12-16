class Machine:
    def __init__(self, productivity, price, avg_price):
        self.productivity = productivity
        self.price = price
        self.avg_price = avg_price

    def payback(self):
        return f"Примерное время окупаемости обычного станка в часах: {self.price/self.avg_price}"


class Miller(Machine):
    def __init__(self, productivity, price, avg_price, service_life):
        super().__init__(productivity, price, avg_price)
        self.service_life = service_life

    def time_payback(self):
        return f"Время окупаемости фрезерного станок в часах: {self.price / (self.productivity * fix_price)}"


class CNCMachine(Machine):
    def __init__(self, productivity, price, avg_price, power):
        super().__init__(productivity, price, avg_price)
        self.power = power

    def time_payback(self):
        return f"Время окупаемости ЧПУ станка в часах: {self.price /(self.productivity * fix_price)}"


fix_price = int(input("Введите стоимость детали:"))
print(Machine(2, 4500, 6).payback())
print(Miller(3, 6000, 2, 30).time_payback())
print(CNCMachine(6, 9000, 5, 300).time_payback())
