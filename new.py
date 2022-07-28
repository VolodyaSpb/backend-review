from math import *
import itertools

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def Cal_sqr_Root(tale):
    """ Вычисляет квадратный корень"""

    return sqrt(tale)


def calc(your_number):
    if your_number <= 0:
        return

    print(f"Мы вычислили корень квадратный из введенного вами числа. Это будет: {Cal_sqr_Root(your_number)}")


print(message)
calc(25.5)
