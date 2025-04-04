def commander_kebab():
    print("=== Bonjour et bienvenue chez Kebaumann ===")

    choix = []

    print("Choisissez vos crudités:")
    crudites = ["Tomates", "Salade", "Oignon"]
    for crudite in crudites:
        reponse = input(f"Voulez-vous du/de la {crudite}? (o/n): ").lower()
        if reponse == 'o' or reponse == 'oui':
            choix.append(crudite)

    print("\nChoisissez votre viande:")
    viandes = ["Poulet", "Boeuf", "Agneau"]
    for viande in viandes:
        reponse = input(f"Voulez-vous du {viande}? (o/n): ").lower()
        if reponse == 'o' or reponse == 'oui':
            choix.append(viande)

    print("\nChoisissez vos compléments:")
    complements = ["Oeufs", "Fromage"]
    for complement in complements:
        reponse = input(f"Voulez-vous du/de la {complement}? (o/n): ").lower()
        if reponse == 'o' or reponse == 'oui':
            choix.append(complement)

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