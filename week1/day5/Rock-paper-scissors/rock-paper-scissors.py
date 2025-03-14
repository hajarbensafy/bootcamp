from game import Game

def get_user_menu_choice():
    """Affiche le menu et retourne le choix de l'utilisateur."""
    print("Menu :")
    print("(g) Jouer une nouvelle partie")
    print("(x) Afficher les scores et quitter")
    choice = input(": ").lower()
    while choice not in ['g', 'x']:
        print("Choix invalide. Veuillez réessayer.")
        choice = input(": ").lower()
    return choice

def print_results(results):
    """Affiche les résultats des parties jouées."""
    print("\nRésultats des parties :")
    print(f"Vous avez gagné {results.get('win', 0)} fois.")
    print(f"Vous avez perdu {results.get('loss', 0)} fois.")
    print(f"Vous avez fait match nul {results.get('draw', 0)} fois.")
    print("Merci d'avoir joué !")

def main():
    """Fonction principale du jeu."""
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == 'x':
            print_results(results)
            break

if __name__ == "__main__":
    main()