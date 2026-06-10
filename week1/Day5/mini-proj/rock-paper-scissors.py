from game import Game

def get_user_menu_choice():
    """Affiche le menu et récupère le choix de l'utilisateur."""
    print("--- MENU PRINCIPAL ---")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores")
    print("q. Quitter")
    
    choice = input("Votre choix : ").strip().lower()
    return choice

def print_results(results):
    """Affiche le récapitulatif des scores de manière conviviale."""
    print("\n=======================")
    print("      RÉSULTATS        ")
    print("=======================")
    print(f"Victoires : {results['win']}")
    print(f"Défaites  : {results['loss']}")
    print(f"Matchs nuls : {results['draw']}")
    print("=======================")
    print("Merci d'avoir joué ! À bientôt.\n")

def main():
    """Fonction principale pour orchestrer le jeu."""
    # Initialisation du dictionnaire des scores selon le format requis
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            # Création d'une nouvelle instance de match
            match = Game()
            game_result = match.play()
            
            # Mise à jour du dictionnaire de scores
            if game_result == "victoire":
                scores["win"] += 1
            elif game_result == "défaite":
                scores["loss"] += 1
            elif game_result == "match nul":
                scores["draw"] += 1
                
        elif choice == "2":
            # Option bonus pour voir le score sans quitter
            print(f"\nScores actuels -> Victoires: {scores['win']}, Défaites: {scores['loss']}, Nuls: {scores['draw']}\n")
            
        elif choice in ["q", "x"]:
            # Fin du programme et affichage final
            print_results(scores)
            break
        else:
            print("Option indisponible. Veuillez choisir 1, 2 ou q.\n")

if __name__ == "__main__":
    main()
