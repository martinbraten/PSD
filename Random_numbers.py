import random


class random_num:
    def __init__(self, amount, minRange, maxRange):
        self.amount = amount
        self.minRange = minRange
        self.maxRange = maxRange

    # Generate x amount of digit in the range.
    def myrandom(self):
        mylist = random.sample(range(self.minRange, self.maxRange), self.amount)
        return mylist


# set value
def setvalue(amount):
    return amount


# set minRange
def setminRange(minimum):
    return minimum


# set maxRange
def setmaxRange(maximum):
    maximum += 1
    return maximum


x = setvalue(int(input('Enter amount of random numbers to return:')))
y = setminRange(int(input('Enter starting range of random number:')))
z = setmaxRange(int(input('Enter max number that the random number can be:')))

mycall = random_num(x, y, z)

print(mycall.myrandom(), sep=', ')

# Adding the first change in nano
# Adding the second change in nano
# Adding the third change in nano
