import math

class Circle:
    def __init__(self, radius):
        """Initialise le cercle avec son rayon."""
        self.radius = radius

    @property
    def radius(self):
        """Récupère le rayon du cercle."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Définit le rayon en s'assurant qu'il n'est pas négatif."""
        if value < 0:
            raise ValueError("Le rayon ne peut pas être négatif.")
        self._radius = value

    @property
    def diameter(self):
        """Calcule le diamètre automatiquement."""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """Permet de modifier le diamètre, ce qui ajuste le rayon."""
        self.radius = value / 2

    @property
    def area(self):
        """Calcule l'aire du cercle (π * r²)."""
        return math.pi * (self._radius ** 2)

    # --- MÉTHODES MAGIQUES (DUNDER) ---

    def __str__(self):
        """Affichage propre lors de l'utilisation de print()."""
        return f"Cercle de rayon {self.radius:.2f} (Diamètre: {self.diameter:.2f}, Aire: {self.area:.2f})"

    def __repr__(self):
        """Représentation officielle de l'objet dans une liste."""
        return f"Circle({self.radius})"

    def __add__(self, other):
        """Additionne les rayons de deux cercles (c1 + c2)."""
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        """Vérifie si deux cercles sont égaux (c1 == c2)."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other):
        """Vérifie si un cercle est plus petit qu'un autre (c1 < c2) - Utile pour le tri."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other):
        """Vérifie si un cercle est plus grand qu'un autre (c1 > c2)."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
