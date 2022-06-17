# -*- coding: utf-8 -*-
"""
@author: Abhishek
"""
import random
from collections import namedtuple
from matplotlib import pyplot as plt

Point = namedtuple('Point', ['generation', 'avg_fit', 'max_fit'])

sys_random = random.SystemRandom()

# Plot graph for each value of 4, 6, 8
POPULATION_SIZE = 8
MIN_RANGE = 0
MAX_RANGE = 15
MAX_GENERATIONS = 100


def f(x):
    # 0 <= x <= 15
    return int((64 - (x**2))**2)


def fitness(x):
    ans = f(x)
    if ans == 0:
        # return sys.maxsize  # 9223372036854775807
        return 1

    return abs(1/ans)


def generate_solutions():
    solutions = []
    for i in range(POPULATION_SIZE):
        solutions.append(sys_random.randint(MIN_RANGE, MAX_RANGE))

    return solutions


def selection_function(population):
    # Assume population to be already sorted in descending order
    return population[:2]


def mutate(num):
    # Mutation of an element by bit flipping
    # Genome of length 6 is taken as per the question (0 to 6)
    idx = sys_random.randint(0, 6)
    num ^= (1 << idx)
    return num


def simple_genetic_algorithm():
    solutions = generate_solutions()
    #points = []

    for i in range(MAX_GENERATIONS):
        rankedsolutions = []
        #fitnesses = []

        for s in solutions:
            fit = fitness(s)
            rankedsolutions.append((fit, s))
            # fitnesses.append(fit)

        rankedsolutions.sort(reverse=True)

        print(f"=== Generation {i+1} best solution ===")
        print(rankedsolutions[0])
        # print(len(rankedsolutions))

        # avg_fit = sum(fitnesses)/len(fitnesses)  # Average fitness
        # max_fit = max(fitnesses)  # Maximum fitness
        #points.append(Point(i+1, avg_fit, max_fit))

        if rankedsolutions[0][0] == 1:
            break

        bestsolutions = selection_function(rankedsolutions)

        elements = []

        for sol in bestsolutions:
            elements.append(sol[1])

        new_generation = []
        for _ in range(POPULATION_SIZE):
            e1 = sys_random.choice(elements)
            # e2 = random.choice(elements)

            new_generation.append(mutate(e1))

        solutions = new_generation

    # return points


def plot(points):
    # Plot average fitness
    X = []
    Y1 = []  # Average fitness for each generation
    Y2 = []  # Max fitness for each generation

    for point in points:
        X.append(point.generation)
        Y1.append(point.avg_fit)
        Y2.append(point.max_fit)

    plt.title(f"Population size : {POPULATION_SIZE}")
    plt.xlabel("Generation")
    plt.scatter(X, Y1, color='k')
    plt.scatter(X, Y2, color='g')
    plt.legend(["avg_fit", "max_fit"], bbox_to_anchor=(1, 1))
    plt.show(block=False)


simple_genetic_algorithm()
#points = simple_genetic_algorithm()
# plot(points)
