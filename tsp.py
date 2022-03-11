import random
import matplotlib.pyplot as plt


def create_cities(no):
    cities = []
    for x in range(no):
        x = (random.randint(-100, 100), random.randint(-100, 100), random.randint(0, 50))
        cities.append(x)
    return cities


def show_cities(cities):
    x, y, z = zip(*cities)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    plt.show()


if __name__ == '__main__':
    cities = create_cities(5)
    print(cities)
    show_cities(cities)