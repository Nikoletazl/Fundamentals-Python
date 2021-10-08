population = [int(el) for el in input().split(", ")]
minimum_wealth = int(input())

while True:
    if sum(population) // len(population) < minimum_wealth:
        print("No equal distribution possible")
        break
    current_distribution = minimum_wealth - min(population)
    if max(population) - current_distribution >= minimum_wealth:
        min_wealth_index = population.index(min(population))
        max_wealth_index = population.index(max(population))
        population[min_wealth_index] += current_distribution
        population[max_wealth_index] -= current_distribution

    if min(population) >= minimum_wealth:
        print(population)
        break