#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. Définition de la classe Part
class Part:
    def __init__(self, name, material):
        """
        Initialise une pièce avec un nom (ex: "Mât") et un matériau (ex: "Bois")
        """
        self.name = name
        self.material = material

    def change_material(self, new_material):
        """
        Change le matériau de la pièce
        """
        self.material = new_material

    def __str__(self):
        """
        Retourne une chaîne de caractères décrivant la pièce
        """
        return f"Pièce : {self.name} | Matériau : {self.material}"


# 2. Définition de la classe Ship
class Ship:
    def __init__(self, name):
        """
        Initialise un navire avec un nom et un dictionnaire privé de pièces.
        Un historique des modifications est également conservé.
        """
        self.name = name
        self.__parts = {}  # dictionnaire privé des pièces ; les clés sont les noms des pièces
        self.history = []  # liste des modifications effectuées sur le navire

    def add_part(self, part):
        """
        Ajoute une pièce au navire.
        """
        self.__parts[part.name] = part

    def display_state(self):
        """
        Affiche l'état du navire en listant l'ensemble de ses pièces.
        """
        print(f"\n=== État du navire '{self.name}' ===")
        if not self.__parts:
            print("Aucune pièce n'a encore été ajoutée.")
        else:
            for part in self.__parts.values():
                print(part)
        print("=" * 30)

    def replace_part(self, part_name, new_part):
        """
        Remplace une pièce existante par une nouvelle pièce.
        Ajoute l'opération à l'historique.
        """
        if part_name in self.__parts:
            old_part = self.__parts[part_name]
            self.__parts[part_name] = new_part
            self.history.append(
                f"Remplacement de la pièce '{old_part.name}' (ancien matériau: {old_part.material}) par '{new_part.material}'"
            )
            print(f"La pièce '{part_name}' a été remplacée.")
        else:
            print(f"Erreur : la pièce '{part_name}' n'existe pas sur le navire.")

    def change_part(self, part_name, new_material):
        """
        Modifie directement le matériau d'une pièce existante (passage par référence).
        On montre ainsi que l'objet Part est modifié directement en mémoire.
        Ajoute l'opération à l'historique.
        """
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
            self.history.append(
                f"Modification du matériau de la pièce '{part_name}' en '{new_material}'"
            )
            print(f"Le matériau de la pièce '{part_name}' a été modifié.")
        else:
            print(f"Erreur : la pièce '{part_name}' n'existe pas sur le navire.")

    def display_history(self):
        """
        Affiche l'historique des modifications du navire.
        """
        print("\n--- Historique des modifications ---")
        if not self.history:
            print("Aucune modification n'a encore été effectuée.")
        else:
            for event in self.history:
                print(event)
        print("-" * 40)

    # Optionnel : méthode pour accéder aux pièces (utile pour d'autres traitements)
    def get_parts(self):
        return self.__parts


# 4. Définition de la classe RacingShip (héritage de Ship)
class RacingShip(Ship):
    def __init__(self, name, max_speed):
        """
        Initialise un RacingShip avec un nom, une vitesse maximale, et hérite des caractéristiques de Ship.
        """
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        """
        Affiche la vitesse maximale du RacingShip.
        """
        print(f"Vitesse maximale de '{self.name}' : {self.max_speed} km/h")


# 5. Interaction et personnalisation via un menu interactif
def main():
    print("=== Bienvenue dans la simulation du bateau de Thésée ===")

    # Création d'un navire et ajout de quelques pièces de base
    ship = Ship("Thésée")
    ship.add_part(Part("Mât", "Bois"))
    ship.add_part(Part("Coque", "Bois"))
    ship.add_part(Part("Voiles", "Tissu"))
    
    # Création d'un RacingShip pour démontrer l'héritage et l'attribut supplémentaire
    racing_ship = RacingShip("Thésée Racing", max_speed=80)

    # Boucle du menu interactif
    while True:
        print("\n--- Menu ---")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Afficher la vitesse maximale du RacingShip")
        print("6. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("Entrez le nom de la pièce à remplacer : ")
            new_material = input("Entrez le matériau de la nouvelle pièce : ")
            # Pour simplifier, on garde le même nom pour la nouvelle pièce.
            new_part = Part(part_name, new_material)
            ship.replace_part(part_name, new_part)
        elif choix == "3":
            part_name = input("Entrez le nom de la pièce à modifier : ")
            new_material = input("Entrez le nouveau matériau : ")
            ship.change_part(part_name, new_material)
        elif choix == "4":
            ship.display_history()
        elif choix == "5":
            racing_ship.display_speed()
        elif choix == "6":
            print("Au revoir !")
            break
        else:
            print("Option non valide. Veuillez réessayer.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
