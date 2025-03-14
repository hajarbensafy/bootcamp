import copy
import os
import time

class Cell:
    def __init__(self, alive=False):
        self.alive = alive  # État de la cellule : vivante (True) ou morte (False)

    def __str__(self):
        return "O" if self.alive else "."  # Représentation visuelle de la cellule

    def toggle(self):
        """Inverse l'état de la cellule (vivante -> morte, morte -> vivante)."""
        self.alive = not self.alive


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows  # Nombre de lignes
        self.cols = cols  # Nombre de colonnes
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]  # Grille de cellules

    def __str__(self):
        """Représentation visuelle de la grille."""
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)

    def set_initial_state(self, initial_state):
        """Définit l'état initial de la grille."""
        for (row, col) in initial_state:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid[row][col].toggle()

    def count_live_neighbors(self, row, col):
        """Compte le nombre de voisins vivants pour une cellule donnée."""
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:  # Ignorer la cellule elle-même
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    if self.grid[new_row][new_col].alive:
                        live_neighbors += 1
        return live_neighbors

    def update(self):
        """Met à jour la grille pour la prochaine génération."""
        new_grid = copy.deepcopy(self.grid)  # Crée une copie de la grille actuelle

        for row in range(self.rows):
            for col in range(self.cols):
                live_neighbors = self.count_live_neighbors(row, col)
                cell = self.grid[row][col]

                # Règles du Jeu de la Vie
                if cell.alive:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row][col].alive = False  # Sous-population ou surpopulation
                else:
                    if live_neighbors == 3:
                        new_grid[row][col].alive = True  # Reproduction

        self.grid = new_grid  # Met à jour la grille


class GameOfLife:
    def __init__(self, rows, cols, initial_state):
        self.grid = Grid(rows, cols)
        self.grid.set_initial_state(initial_state)

    def run(self, generations, delay=0.5):
        """Exécute le jeu pour un nombre donné de générations."""
        for generation in range(generations):
            os.system("cls" if os.name == "nt" else "clear")  # Efface l'écran
            print(f"Generation {generation + 1}:\n")
            print(self.grid)
            self.grid.update()
            time.sleep(delay)  # Délai entre les générations


# Exemple d'utilisation
if __name__ == "__main__":
    # Définir l'état initial (liste de coordonnées (row, col) des cellules vivantes)
    initial_state = [
        (1, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    ]

    # Créer une instance du jeu
    game = GameOfLife(rows=10, cols=10, initial_state=initial_state)

    # Exécuter le jeu pour 20 générations avec un délai de 0.5 seconde entre chaque génération
    game.run(generations=20, delay=0.5)