def display_board(board):
    """Affiche le plateau de jeu."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def player_input(board, player):
    """Demande au joueur de saisir sa position."""
    while True:
        try:
            row = int(input(f"Joueur {player}, entrez la ligne (1-3) : ")) - 1
            col = int(input(f"Joueur {player}, entrez la colonne (1-3) : ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Position invalide ou déjà occupée. Réessayez.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def check_win(board, player):
    """Vérifie si le joueur actuel a gagné."""
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Lignes
            return True
        if all([board[j][i] == player for j in range(3)]):  # Colonnes
            return True
    if all([board[i][i] == player for i in range(3)]):  # Diagonale principale
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Diagonale secondaire
        return True
    return False


def is_board_full(board):
    """Vérifie si le plateau est plein (match nul)."""
    return all([cell != " " for row in board for cell in row])


def play():
    """Fonction principale pour exécuter le jeu."""
    # Initialisation du plateau
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # Joueur X commence

    print("Bienvenue dans le jeu Tic Tac Toe !")
    display_board(board)

    while True:
        # Demande au joueur de faire un mouvement
        row, col = player_input(board, current_player)
        board[row][col] = current_player
        display_board(board)

        # Vérifie si le joueur actuel a gagné
        if check_win(board, current_player):
            print(f"Félicitations, Joueur {current_player} a gagné !")
            break

        # Vérifie si le plateau est plein (match nul)
        if is_board_full(board):
            print("Match nul !")
            break

        # Change de joueur
        current_player = "O" if current_player == "X" else "X"


# Démarrer le jeu
if __name__ == "__main__":
    play()