import random

class Game:
    def __init__(self):
        # Liste pour valider les saisies du jeu
        self.items = ["pierre", "feuille", "ciseaux"]

    def get_user_item(self) -> str:
        """Demande à l'utilisateur de choisir un élément avec validation."""
        while True:
            choice = input("Faites votre choix (pierre/feuille/ciseaux) : ").strip().lower()
            if choice in self.items:
                return choice
            print("❌ Choix invalide. Veuillez recommencer.")

    def get_computer_item(self) -> str:
        """Sélectionne aléatoirement pierre, feuille ou ciseaux pour l'ordinateur."""
        return random.choice(self.items)

    def get_game_result(self, user_item: str, computer_item: str) -> str:
        """Détermine le résultat de la partie du point de vue de l'utilisateur.
        
        Renvoie 'victoire', 'match nul' ou 'défaite'.
        """
        if user_item == computer_item:
            return "match nul"
        
        # Logique des règles (la clé gagne contre la valeur)
        rules = {
            "pierre": "ciseaux",
            "feuille": "pierre",
            "ciseaux": "feuille"
        }
        
        if rules[user_item] == computer_item:
            return "victoire"
        else:
            return "défaite"

    def play(self) -> str:
        """Exécute une manche complète et renvoie le résultat."""
        # 1. Récupération et mémorisation du choix de l'utilisateur
        user_choice = self.get_user_item()
        
        # 2. Tirage et mémorisation du choix de l'ordinateur
        computer_choice = self.get_computer_item()
        
        # 3. Détermination du résultat
        result = self.get_game_result(user_choice, computer_choice)
        
        # Affichage textuel obligatoire du résultat de la manche
        if result == "match nul":
            print(f"Vous avez choisi {user_choice}. L’ordinateur a choisi {computer_choice}. Vous avez fait match nul !")
        elif result == "victoire":
            print(f"Vous avez choisi {user_choice}. L’ordinateur a choisi {computer_choice}. Vous avez gagné !")
        else:
            print(f"Vous avez choisi {user_choice}. L’ordinateur a choisi {computer_choice}. Vous avez perdu")
            
        return result
