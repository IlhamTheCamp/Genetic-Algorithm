# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import numpy as np
import random
import math

def decode_chromosome(chromosome):

    c1 = int(chromosome/2)
    dc1 = np.zeros(chromosome)
    dc1[0: c1] = 1
    np.random.shuffle(dc1)
    return(dc1)

def create_population(individu, pchromosome):
    population = np.zeros((individu, pchromosome))
    for p in range(individu):
        #random angka
        pop = random.randint(0, pchromosome)
        population[p, 0:pop] = 1
        np.random.shuffle(population[p])
    return(population)

def func(x1, x2):
    f_hasil = 0
    if x1 >= -1 and x1 <= 2 and x2 >= 1 and x2 <= 1 :
        f_hasil = np.cos(x1)*np.sin(x2) - (x1 / ((x2 ** 2) + 1))

    return(f_hasil)

def fitness(func, x1, x2):
    #nilai a untuk menghindari pembagian dengan nol
    a = 0.2

    h = func(x1, x2)
    f = 1 / (h + a)
    return(f)

def main():
    chromosome = decode_chromosome(20)
    print ("Hasil Chromosome: \n", chromosome)
    population = create_population(4, 20)
    print("\nHasil Populasi: \n", population)
    hasil_fitness = fitness(func, chromosome, population)
    print("\n Fitness Terbaik dari fungsi yang diberikan: \n",hasil_fitness)



if __name__ == '__main__':
    main()
