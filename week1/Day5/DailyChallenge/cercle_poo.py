import math

class Circle:
    def __init__(self, radius: float):
        """Initialise le cercle avec son rayon."""
        if radius < 0:
            raise ValueError("Le rayon ne peut pas être négatif.")
        self._radius = float(radius)

    # --- DÉCORATEURS / PROPRIÉTÉS (Getters et Setters) ---
    
    @property
    def radius(self) -> float:
        """Permet de récupérer le rayon : cercle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Permet de modifier le rayon : cercle.radius = 10"""
        if value < 0:
            raise ValueError("Le rayon ne peut pas être négatif.")
        self._radius = float(value)

    @property
    def diameter(self) -> float:
        """Calcule et renvoie le diamètre automatiquement : cercle.diameter"""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value: float):
        """Permet de modifier le cercle via son diamètre : cercle.diameter = 20"""
        if value < 0:
            raise ValueError("Le diamètre ne peut pas être négatif.")
        self._radius = float(value) / 2

    @property
    def area(self) -> float:
        """Calcule et renvoie l'aire du cercle : cercle.area"""
        return math.pi * (self._radius ** 2)

    # --- MÉTHODES DUNDER (AFFICHAGE) ---

    def __str__(self) -> str:
        """Affichage convivial pour l'utilisateur final (via print)"""
        return f"Cercle de rayon {self._radius:.2f} (Diamètre: {self.diameter:.2f})"

    def __repr__(self) -> str:
        """Affichage officiel pour le débogage ou les listes"""
        return f"Circle({self._radius})"

    # --- MÉTHODES DUNDER (OPÉRATIONS ARITHMÉTIQUES) ---

    def __add__(self, other):
        """Additionne deux cercles et renvoie un NOUVEAU cercle avec la somme des rayons"""
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self._radius + other._radius)

    # --- MÉTHODES DUNDER (COMPARAISONS) ---

    def __eq__(self, other) -> bool:
        """Vérifie si deux cercles sont égaux (mêmes rayons)"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

    def __lt__(self, other) -> bool:
        """Inférieur à : indispensable pour que la fonction native sort() fonctionne"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius

    def __gt__(self, other) -> bool:
        """Supérieur à : permet l'utilisation de l'opérateur >"""
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius > other._radius


# =====================================================================
# ZONE DE TESTS AUTOMATIQUES (S'exécute uniquement si on lance ce fichier)
# =====================================================================
if __name__ == "__main__":
    print("--- 1. Création et requêtes d'attributs ---")
    c1 = Circle(4)
    print(c1)  # Utilise __str__
    print(f"Rayon initial : {c1.radius}")
    print(f"Diamètre calculé : {c1.diameter}")
    print(f"Aire calculée : {c1.area:.2f}")

    print("\n--- 2. Modification dynamique (via le Diamètre) ---")
    c1.diameter = 10
    print(f"Nouveau diamètre fixé à 10 -> Nouveau rayon calculé : {c1.radius}")
    print(f"Nouvelle aire : {c1.area:.2f}")

    print("\n--- 3. Addition de deux cercles (Dunder __add__) ---")
    c2 = Circle(3)
    c3 = c1 + c2
    print(f"{c1} + {c2} = {c3}")

    print("\n--- 4. Comparaisons (Dunder __eq__, __gt__) ---")
    print(f"Est-ce que {c1} > {c2} ? {c1 > c2}")
    print(f"Est-ce que {c1} == {c2} ? {c1 == c2}")
    
    c_identique = Circle(5)
    print(f"Création d'un clone de c1 (rayon 5). Égaux ? {c1 == c_identique}")

    print("\n--- 5. Stockage et Tri d'une liste de cercles ---")
    liste_cercles = [Circle(9), Circle(2), Circle(5.5), Circle(1)]
    print(f"Liste brute (repr) : {liste_cercles}")
    
    # Utilisation de la méthode native de Python qui s'appuie sur __lt__
    liste_cercles.sort()
    print("Liste triée par ordre croissant de rayon :")
    for c in liste_cercles:
        print(f"  - {c}")

    # =====================================================================
    # BONUS VISUEL : ESSAI DESSIN AVEC TURTLE (Optionnel)
    # =====================================================================
    try:
        import turtle
        print("\n--- 🎁 Défi Bonus : Dessin des cercles avec Turtle ---")
        print("Fermez la fenêtre graphique Turtle pour terminer le script.")
        
        # Configuration de l'écran
        screen = turtle.Screen()
        screen.title("Visualisation des cercles triés")
        screen.setup(width=600, height=400)
        
        pen = turtle.Turtle()
        pen.speed(3)
        pen.width(2)
        
        # Dessiner les cercles triés de la liste
        # Multiplication du rayon par un facteur d'échelle pour la visibilité
        facteur_echelle = 10 
        
        for index, cercle in enumerate(liste_cercles):
            pen.penup()
            # Espacer les cercles horizontalement sur l'écran
            pen.goto(-200 + (index * 120), -50) 
            pen.pendown()
            
            # Aléatoire simple pour la couleur
            couleurs = ["blue", "green", "orange", "red"]
            pen.color(couleurs[index % len(couleurs)])
            
            # Turtle dessine à partir du bas du cercle
            pen.circle(cercle.radius * facteur_echelle)
            
        pen.hideturtle()
        screen.mainloop()
        
    except (ImportError, turtle.Terminator):
        print("\nNote : Le module graphique 'turtle' n'est pas disponible ou l'affichage a été ignoré.")
