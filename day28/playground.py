def add(*args):
    sm = 0
    for n in args:
        sm += n
    return (sm)


print(add(2, 3, 8))


def calculate(**kwargs):
    print(kwargs)
    for key, val in kwargs.items():
        print(val)


calculate(add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

new_car = Car(make="Mercedes", model = "MD-E0")
print(new_car.make)
