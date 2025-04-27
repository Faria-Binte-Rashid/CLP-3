import random

def create_individual(k):
    return [random.randint(0, 9) for _ in range(k)]

def fitness(individual, T):
    return abs(T - sum(individual))

def mutate(individual):
    idx = random.randint(0, len(individual) - 1)
    individual[idx] = random.randint(0, 9)

def genetic_algorithm(T, k, max_generations=10000):

    individual = create_individual(k)
    
    for generation in range(max_generations):
        # Check if we have a perfect solution
        if sum(individual) == T:
            print(f"Found in generation {generation}: {individual}")
            return individual

        new_individual = individual[:]
        mutate(new_individual)

        if fitness(new_individual, T) <= fitness(individual, T):
            individual = new_individual
    
    print("No perfect solution found.")
    return individual

T = 7
k = 2
solution = genetic_algorithm(T, k)
print("Case#1 Output:", *solution)

T = 10
k = 3
solution = genetic_algorithm(T, k)
print("Case#2 Output:", *solution)
