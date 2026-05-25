# Dans main.py
from circle import Circle  # Importe la classe depuis le fichier circle.py

def main():
    # 1. Création de cercles
    c1 = Circle(10)
    c2 = Circle(20)
    
    # 2. Test des méthodes magiques
    print(f"Cercle 1 : {c1}")
    print(f"Cercle 2 : {c2}")
    
    c3 = c1 + c2
    print(f"Cercle additionné (c1 + c2) : {c3}")
    print(f"Est-ce que c1 > c2 ? {c1 > c2}")

if __name__ == "__main__":
    main()
