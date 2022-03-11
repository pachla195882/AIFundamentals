import random
import matplotlib.pyplot as plt
import numpy as np


def create_cities(no):
    cities = []
    for x in range(no):
        x = np.array((random.randrange(-100, 100), random.randrange(-100, 100), random.randrange(0, 50)))
        cities.append(x)
    return cities


def show_cities(cities):
    x, y, z = cities
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()


def calculate_cost(first_city, second_city, asymmetric):
    cost = np.linalg.norm(first_city - second_city)
    if asymmetric and first_city[2] > second_city[2]:
        cost *= 0.9
    elif asymmetric and first_city[2] < second_city[2]:
        cost *= 1.1
    return cost


if __name__ == '__main__':
    _cities = create_cities(3)
    print(*_cities)
    print(_cities[1])
    print(_cities[1][0])
    _cost = calculate_cost(_cities[0], _cities[1], False)
    print(_cost)
    show_cities(_cities)
