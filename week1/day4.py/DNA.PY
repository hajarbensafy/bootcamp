import random

class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])  # Initialise le gène à 0 ou 1 aléatoirement

    def mutate(self):
        """Fait muter le gène en inversant sa valeur (0 -> 1 ou 1 -> 0)."""
        self.value = 1 if self.value == 0 else 0

    def __str__(self):
        return str(self.value)


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]  # Un chromosome est composé de 10 gènes

    def mutate(self):
        """Fait muter le chromosome en inversant aléatoirement certains gènes."""
        for gene in self.genes:
            if random.random() < 0.5:  # 1/2 chance de muter chaque gène
                gene.mutate()

    def is_all_ones(self):
        """Vérifie si tous les gènes du chromosome sont égaux à 1."""
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return "".join(str(gene) for gene in self.genes)


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]  # Un ADN est composé de 10 chromosomes

    def mutate(self):
        """Fait muter l'ADN en inversant aléatoirement certains chromosomes."""
        for chromosome in self.chromosomes:
            if random.random() < 0.5:  # 1/2 chance de muter chaque chromosome
                chromosome.mutate()

    def is_all_ones(self):
        """Vérifie si tous les chromosomes de l'ADN sont composés uniquement de 1."""
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __str__(self):
        return "\n".join(str(chromosome) for chromosome in self.chromosomes)


class Organism:
    def __init__(self, dna, mutation_probability):
        self.dna = dna  # ADN de l'organisme
        self.mutation_probability = mutation_probability  # Probabilité de mutation

    def mutate(self):
        """Fait muter l'ADN de l'organisme avec une certaine probabilité."""
        if random.random() < self.mutation_probability:
            self.dna.mutate()

    def has_perfect_dna(self):
        """Vérifie si l'ADN de l'organisme est composé uniquement de 1."""
        return self.dna.is_all_ones()

    def __str__(self):
        return f"Organisme avec ADN :\n{self.dna}"


# Simulation
def simulate_evolution(num_organisms, mutation_probability):
    # Crée une liste d'organismes
    organisms = [Organism(DNA(), mutation_probability) for _ in range(num_organisms)]

    generation = 0
    while True:
        generation += 1
        print(f"Génération {generation}")

        # Fait muter chaque organisme
        for organism in organisms:
            organism.mutate()

            # Vérifie si un organisme a un ADN parfait
            if organism.has_perfect_dna():
                print("Un organisme a atteint un ADN parfait !")
                print(organism)
                return generation  # Retourne le nombre de générations nécessaires


# Exemple d'utilisation
if __name__ == "__main__":
    num_organisms = 10  # Nombre d'organismes dans la simulation
    mutation_probability = 0.1  # Probabilité de mutation

    generations = simulate_evolution(num_organisms, mutation_probability)
    print(f"Nombre de générations nécessaires : {generations}")