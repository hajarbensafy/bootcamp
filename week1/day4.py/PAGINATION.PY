class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []  # Liste des éléments à paginer
        self.pageSize = int(pageSize)  # Taille de chaque page (converti en entier)
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)  # Nombre total de pages
        self.currentPage = 1  # Page actuelle (commence à 1)

    def getVisibleItems(self):
        """Retourne les éléments visibles sur la page actuelle."""
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        """Passe à la page précédente."""
        self.currentPage = max(1, self.currentPage - 1)
        return self  # Permet le chaînage des méthodes

    def nextPage(self):
        """Passe à la page suivante."""
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self  # Permet le chaînage des méthodes

    def firstPage(self):
        """Passe à la première page."""
        self.currentPage = 1
        return self  # Permet le chaînage des méthodes

    def lastPage(self):
        """Passe à la dernière page."""
        self.currentPage = self.totalPages
        return self  # Permet le chaînage des méthodes

    def goToPage(self, pageNum):
        """Passe à une page spécifique."""
        pageNum = int(pageNum)  # Convertit en entier
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self  # Permet le chaînage des méthodes


# Exemple d'utilisation
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")

    # Initialisation de la pagination avec 4 éléments par page
    p = Pagination(alphabetList, 4)

    # Affichage des éléments de la page actuelle
    print("Page 1:", p.getVisibleItems())  # ["a", "b", "c", "d"]

    # Passage à la page suivante
    p.nextPage()
    print("Page 2:", p.getVisibleItems())  # ["e", "f", "g", "h"]

    # Passage à la dernière page
    p.lastPage()
    print("Dernière page:", p.getVisibleItems())  # ["y", "z"]

    # Retour à la première page
    p.firstPage()
    print("Première page:", p.getVisibleItems())  # ["a", "b", "c", "d"]

    # Aller à une page spécifique
    p.goToPage(3)
    print("Page 3:", p.getVisibleItems())  # ["i", "j", "k", "l"]

    # Chaînage des méthodes
    p.nextPage().nextPage()
    print("Page 5 après chaînage:", p.getVisibleItems())  # ["q", "r", "s", "t"]

    # Test avec une page en dehors des limites
    p.goToPage(10)
    print("Page 10 (hors limites):", p.getVisibleItems())  # ["y", "z"]