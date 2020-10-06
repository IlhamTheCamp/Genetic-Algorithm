# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random
import math

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

def tournament_parent(pop, banyakPopulasi, banyakTourney):
    best = []
    for x in range(banyakTourney):
        kromosom = pop[random.randint(1, banyakPopulasi)]
        if (best == []) or calculate_fitness(kromosom) > calculate_fitness(best):
            best = kromosom
    return best

def main():
    # Tanya kenapa ada fungsi fitnessAll
    # Tanya maksud dari ukuran Tourney
    banyakPopulasi = 100
    banyakTourney = 10

    populasi = create_populasi(banyakPopulasi)
    print("Contoh Populasi : ", populasi)
    print("Hasil Dekode : ", decode_kromosom(populasi[2]))
    print("Hasil Fitness : ", calculate_fitness(populasi[2]))

    #tesTournament
    parent1 = tournament_parent(populasi, banyakPopulasi, banyakTourney)
    parent2 = tournament_parent(populasi, banyakPopulasi, banyakTourney)
    print("Kromosom Orang Tua : ")
    print(parent1)
    print(parent2)

if __name__ == '__main__':
    main()
