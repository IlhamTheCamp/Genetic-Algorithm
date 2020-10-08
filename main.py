# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random
import math
import time

def create_kromosom(banyakKromosom):
    kromosom = []
    for x in range(banyakKromosom):
        kromosom.append(random.randint(0,1))
    return kromosom

def create_populasi(banyakPopulasi):
    populasi = []
    for x in range(banyakPopulasi):
        populasi.append(create_kromosom(10))
    return populasi

def decode_kromosom(kromosom):
    x1 = -1 + ((3 / (2**-1 + 2**-2 + 2**-3 + 2**-4 + 2**-5)) * ((kromosom[0]*2**-1)+(kromosom[1]*2**-2)+(kromosom[2]*2**-3)+(kromosom[3]*2**-4)+(kromosom[4]*2**-5)))
    x2 = -1 + ((2 / (2**-1 + 2**-2 + 2**-3 + 2**-4 + 2**-5)) * ((kromosom[5]*2**-1)+(kromosom[6]*2**-2)+(kromosom[7]*2**-3)+(kromosom[8]*2**-4)+(kromosom[9]*2**-5)))
    return [x1,x2]

def calculate_fitness(kromosom):
    k = decode_kromosom(kromosom)
    fitness = -1 * ((math.cos(k[0]) * math.sin(k[1])) - (k[0] / (k[1]**2 + 1)))
    return fitness

def calculate_all_fitness(populasi, banyakPopulasi):
    all_fitness = []
    for x in range(banyakPopulasi):
        all_fitness.append(calculate_fitness(populasi[x]))
    return all_fitness

def tournament_parent(pop, banyakPopulasi, banyakTourney):
    best = []
    for x in range(banyakTourney):
        kromosom = pop[random.randint(0, banyakPopulasi-1)]
        if (best == []) or calculate_fitness(kromosom) > calculate_fitness(best):
            best = kromosom
    return best

def crossover(parent1, parent2, probCros):
    k = random.random()
    if k < probCros:
        pointCross = random.randint(0,9)
        for i in range(pointCross):
            parent1[i], parent2[i] = parent2[i], parent1[1]
    return parent1, parent2

def mutasi(child1, child2, probMuta):
    k = random.random()
    c1 = random.randint(0, 9)
    c2 = random.randint(0, 9)
    if k < probMuta:
        if child1[c1] == 0:
            child1[c1] = 1
        else:
            child1[c1] = 0
        if child2[c2] == 0:
            child2[c2] = 1
        else:
            child2[c2] = 0
    return child1, child2

def get_elitisme(fitnessAll):
    return fitnessAll.index(max(fitnessAll))

def get_lowest(fitnessAll):
    return fitnessAll.index(min(fitnessAll))

def steady_state(populasi, banyakPopulasi, child):
    fitness = calculate_all_fitness(populasi, banyakPopulasi)
    low1 = get_lowest(fitness)
    fitness[low1] = 9999
    low2 = get_lowest(fitness)
    populasi[low1] = child[0]
    populasi[low2] = child[1]
    return populasi

def main():
    banyakPopulasi = 100
    banyakTourney = 10
    probCros = 0.65
    probMuta = 0.13
    timeout = time.time() + 60*2

    populasi = create_populasi(banyakPopulasi)
    while True:
        parent1 = tournament_parent(populasi, banyakPopulasi, banyakTourney)
        parent2 = tournament_parent(populasi, banyakPopulasi, banyakTourney)
        while parent1 == parent2 :
            parent2 = tournament_parent(populasi, banyakPopulasi, banyakTourney)
        child = crossover(parent1, parent2, probCros)
        child = mutasi(child[0], child[1], probMuta)
        populasi = steady_state(populasi, banyakPopulasi, child)
        if time.time() > timeout:
            break

    fitness = calculate_all_fitness(populasi, banyakPopulasi)
    bestKromosom = get_elitisme(fitness)
    print("Hasil Minimasi Fungsi : ")
    print("Kromosom Terbaik : ", populasi[bestKromosom])
    print("Fitness Terbaik : ", calculate_fitness(populasi[bestKromosom]))
    print("Decode Kromosom : ", decode_kromosom(populasi[bestKromosom]))

if __name__ == '__main__':
    main()
