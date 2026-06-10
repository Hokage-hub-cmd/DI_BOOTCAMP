# Importation de la classe Game depuis le fichier game.py
from game import Game

def get_user_menu_choice() -> str:
    """Affiche le menu simple et recueille le choix de l'utilisateur sans boucle."""
    print("\n--- MENU PRINCIPAL ---")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("3. Quitter")
    
    choice = input("Saisissez votre choix : ").strip()
    return choice

def print_results(results: dict):
    """Affiche de manière conviviale le dictionnaire de résultats complet."""
    print("\n=======================================")
    print("📊 RÉCAPITULATIF DES SCORES DE LA SESSION")
    print("=======================================")
    print(f"🏆 Victoires   (win)  : {results['win']}")
    print(f"💀 Défaites   (loss) : {results['loss']}")
    print(f"🤝 Matchs nuls (draw) : {results['draw']}")
    print("=======================================")
    print("Merci d'avoir participé à ce jeu ! À bientôt ! 👋\n")

def main():
    """Fonction principale de contrôle du flux du programme."""
    # Initialisation du dictionnaire requis : {win: 0, loss: 0, draw: 0}
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        # Récupération du choix du menu
        menu_choice = get_user_menu_choice()
        
        if menu_choice == "1":
            # Création de l'instance de jeu et récupération du résultat retourné par play()
            game_round = Game()
            outcome = game_round.play()
            
            # Incrémentation des compteurs du dictionnaire externe
            if outcome == "victoire":
                results["win"] += 1
            elif outcome == "défaite":
                results["loss"] += 1
            elif outcome == "match nul":
                results["draw"] += 1
                
        elif menu_choice == "2":
            # Affichage rapide des scores intermédiaires
            print(f"\n📈 Scores actuels -> Victoires: {results['win']} | Défaites: {results['loss']} | Nuls: {results['draw']}")
            
        elif menu_choice in ["3", "q", "x", "Q", "X"]:
            # Appel de la fonction d'affichage final et sortie de la boucle
            print_results(results)
            break
        else:
            print("❌ Option invalide du menu. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()
