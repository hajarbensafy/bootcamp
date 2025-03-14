import random

class Game:
    def get_user_item(self):
        """Demande à l'utilisateur de choisir pierre, papier ou ciseaux."""
        while True:
            user_input = input("Choisissez (r)ock, (p)aper, ou (s)cissors : ").lower()
            if user_input in ['r', 'p', 's']:
                return {'r': 'rock', 'p': 'paper', 's': 'scissors'}[user_input]
            print("Choix invalide. Veuillez réessayer.")

    def get_computer_item(self):
        """Choisit aléatoirement pierre, papier ou ciseaux pour l'ordinateur."""
        return random.choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, user_item, computer_item):
        """Détermine le résultat du jeu."""
        if user_item == computer_item:
            return 'draw'
        if (user_item == 'rock' and computer_item == 'scissors') or \
           (user_item == 'paper' and computer_item == 'rock') or \
           (user_item == 'scissors' and computer_item == 'paper'):
            return 'win'
        return 'loss'

    def play(self):
        """Joue une partie et retourne le résultat."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"Vous avez choisi : {user_item}. L'ordinateur a choisi : {computer_item}. Résultat : {result}.")
        return result