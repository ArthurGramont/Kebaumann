def commander_kebab():
    print("=== Bonjour et bienvenue chez Kebaumann ===")

    choix = []

    print("\nChoisissez vos crudités (tapez les numéros correspondants):")
    crudites = ["Tomates", "Salade", "Oignon"]
    for i, crudite in enumerate(crudites, 1):
        print(f"{i}- {crudite}")

    selection_crudites = input("Votre sélection: ")
    for char in selection_crudites:
        if char.isdigit() and 1 <= int(char) <= len(crudites):
            index = int(char) - 1
            choix.append(crudites[index])

    print("\nChoisissez votre viande (tapez les numéros correspondants):")
    viandes = ["Poulet", "Boeuf", "Agneau"]
    for i, viande in enumerate(viandes, 1):
        print(f"{i}- {viande}")

    selection_viandes = input("Votre sélection: ")
    for char in selection_viandes:
        if char.isdigit() and 1 <= int(char) <= len(viandes):
            index = int(char) - 1
            choix.append(viandes[index])

    print("\nChoisissez vos compléments (tapez les numéros correspondants):")
    complements = ["Oeufs", "Fromage"]
    for i, complement in enumerate(complements, 1):
        print(f"{i}- {complement}")

    selection_complements = input("Votre sélection: ")
    for char in selection_complements:
        if char.isdigit() and 1 <= int(char) <= len(complements):
            index = int(char) - 1
            choix.append(complements[index])

    print("\nChoisissez vos sauces (tapez les numéros correspondants):")
    sauces = ["Blanche", "Samouraï", "Algérienne", "Ketchup", "Harissa"]
    for i, sauce in enumerate(sauces, 1):
        print(f"{i}- {sauce}")

    selection_sauces = input("Votre sélection: ")
    for char in selection_sauces:
        if char.isdigit() and 1 <= int(char) <= len(sauces):
            index = int(char) - 1
            choix.append(sauces[index])

    is_vegetarien = not any(viande in choix for viande in viandes)

    print("\n=== Récapitulatif de votre commande ===")

    if not choix:
        print("Vous n'avez sélectionné aucun ingrédient!")
        return

    print("Ingrédients sélectionnés:")
    for ingredient in choix:
        print(f"- {ingredient}")

    print(f"\nVotre kebab est {'végétarien' if is_vegetarien else 'avec viande, donc il n\'est pas végétarien'}.")

    confirmation = input("\nConfirmez-vous votre commande? (o/n): ").lower()
    if confirmation == 'o' or confirmation == 'oui':
        print("\nVotre commande a été confirmée et sera prête dans 10 minutes!")
    else:
        print("\nVotre commande a été annulée.")


if __name__ == "__main__":
    commander_kebab()