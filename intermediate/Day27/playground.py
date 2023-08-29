# '*arg'--> 'unlimited Positional Arguments' : specify a tuple that can enter any arguments inside when using method
def add(*arg):
    for n in arg:
        print(n)

# add(1, 2, 3, 4, 5, 6, 76)


def calculate(n, **kwargs):
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)


calculate(3, add = 3, multiply = 4)