def menu():
    print("=== Bonjour et bienvenue chez Kebaumann ===")
    choix = 0
    arret = 1
    ingredients = []

    ingredients = choisir_kebab()
    while arret == 1:
        recap(ingredients)
        print("\nSouhaitez-vous effectuer l'une de ces actions ? ")
        actions = ["Doubler le fromage", "Retirer les oignons", "Ajouter un supplément", "Confirmer la commande"]
        for i, action in enumerate(actions, 1):
            print(f"{i}- {action}")

        selection_actions = input("Votre sélection: ")
        for char in selection_actions:
            if char.isdigit() and 1 <= int(char) <= len(actions):
                index = int(char)
                choix = index

        if choix == 1:
            doubler_fromage(ingredients)
        elif choix == 2:
            retirer_oignons(ingredients)
        elif choix == 3:
            ajouter_supplement(ingredients)
        else:
            confirmer_commande()
            arret = 0

def choisir_kebab():
    choixKebab = []
    choix = []

    print("Choisissez quel type de kebab vous souhaitez: ")
    kebabs = ["Classique", "Fromage", "Personnalisé"]
    for i, kebab in enumerate(kebabs, 1):
        print(f"{i}- {kebab}")

    selection_kebab = input("Votre sélection: ")
    list = selection_kebab.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(kebabs):
            index = int(char) - 1
            choixKebab.append(kebabs[index])

    if choixKebab[0] == kebabs[2]:
        choix = commander_kebab_personnalise()
        return choix
    elif choixKebab[0] == kebabs[1]:
        choix = ["Salade", "Fromage", "Viande"]
        print("Vous avez choisi le kebab Fromage")
        return choix
    else:
        choix = ["Tomates", "Salade", "Oignons", "Viande"]
        print("Vous avez choisi le kebab Classique")
        return choix

def recap(choix):
    print("\n=== Récapitulatif de votre commande ===")

    print("Ingrédients sélectionnés:")
    for ingredient in choix:
        print(f"- {ingredient}")

    if not choix:
        print("Vous n'avez sélectionné aucun ingrédient!")
        return

def doubler_fromage(choix):
    confirmation = input("\nVoulez vous doubler le fromage ? (o/n): ").lower()
    if confirmation == "o" or confirmation == "oui":
        i = 0
        while i < len(choix):
            if choix[i] == "Fromage":
                choix.insert(i + 1, "Fromage")
                i += 1
            i += 1

    return choix

def retirer_oignons(choix):
    confirmation = input("\nVoulez vous retirer les oignons ? (o/n): ").lower()
    if confirmation == "o" or confirmation == "oui":
        for ingredient in choix:
            if ingredient == "Oignons":
                choix.remove(ingredient)

    return choix

def ajouter_supplement(choix):
    choixSupplement = ["Fromage", "Oignons", "Salade", "Maïs", "Sauce blanche", "Sauce Algérienne"]
    for i, supplement in enumerate(choixSupplement, 1):
        print(f"{i}- {supplement}")

    selection_supplement = input("Votre sélection: ")
    list = selection_supplement.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(choixSupplement):
            index = int(char) - 1
            choix.append(choixSupplement[index])

def confirmer_commande():
    confirmation = input("\nÊtes vous bien sûrs de vouloir confirmer votre commande ? (o/n): ").lower()
    if confirmation == "o" or confirmation == "oui":
        print("Votre commande a été validée et sera prête dans 10 minutes.")
    else:
        print("Commande annulée !")

def commander_kebab_personnalise():
    choix = []

    print(
        "\nChoisissez vos crudités (tapez les numéros correspondants, il est possible d'avoir plusieurs ingrédients) - veillez à bien mettre un espace entre chaque ingrédient:")
    crudites = ["Tomates", "Salade", "Oignons", "Patates", "Carottes", "Oignons rouge", "Courgettes", "Radis", "Choux",
                "Coleslaw"]
    for i, crudite in enumerate(crudites, 1):
        print(f"{i}- {crudite}")

    selection_crudites = input("Votre sélection: ")
    list = selection_crudites.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(crudites):
            index = int(char) - 1
            choix.append(crudites[index])

    print(
        "\nChoisissez votre viande (tapez les numéros correspondants, il est possible d'avoir plusieurs ingrédients) - veillez à bien mettre un espace entre chaque ingrédient:")
    viandes = ["Poulet", "Boeuf", "Agneau"]
    for i, viande in enumerate(viandes, 1):
        print(f"{i}- {viande}")

    selection_viandes = input("Votre sélection: ")
    list = selection_viandes.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(viandes):
            index = int(char) - 1
            choix.append(viandes[index])

    print(
        "\nChoisissez votre poisson (tapez les numéros correspondants, il est possible d'avoir plusieurs ingrédients) - veillez à bien mettre un espace entre chaque ingrédient:")
    poissons = ["Thon", "Saumon", "Cabillaud"]
    for i, poisson in enumerate(poissons, 1):
        print(f"{i}- {poisson}")

    selection_poissons = input("Votre sélection: ")
    list = selection_poissons.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(poissons):
            index = int(char) - 1
            choix.append(poissons[index])

    print(
        "\nChoisissez vos compléments (tapez les numéros correspondants, il est possible d'avoir plusieurs ingrédients) - veillez à bien mettre un espace entre chaque ingrédient:")
    complements = ["Oeufs", "Fromage"]
    for i, complement in enumerate(complements, 1):
        print(f"{i}- {complement}")

    selection_complements = input("Votre sélection: ")
    list = selection_complements.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(complements):
            index = int(char) - 1
            choix.append(complements[index])

    print(
        "\nChoisissez vos sauces (tapez les numéros correspondants, il est possible d'avoir plusieurs ingrédients) - veillez à bien mettre un espace entre chaque ingrédient:")
    sauces = ["Blanche", "Samouraï", "Algérienne", "Ketchup", "Harissa"]
    for i, sauce in enumerate(sauces, 1):
        print(f"{i}- {sauce}")

    selection_sauces = input("Votre sélection: ")
    list = selection_sauces.split(" ")
    for char in list:
        if char.isdigit() and 1 <= int(char) <= len(sauces):
            index = int(char) - 1
            choix.append(sauces[index])

    is_vegetarien = not any(viande in choix for viande in viandes) and not any(poisson in choix for poisson in poissons)
    is_pescetarien = any(poisson in choix for poisson in poissons) and not any(viande in choix for viande in viandes)

    print(
        f"\nVotre kebab est {'végétarien' if is_vegetarien else 'avec viande ou poisson, donc il n\'est pas végétarien'}.")
    print(
        f"\nVotre kebab est {'péscétarien' if is_pescetarien else 'sans poisson ou avec viande, donc il n\'est pas péscétarien'}.")

    confirmation = input("\nConfirmez-vous votre commande? (o/n): ").lower()
    if confirmation == 'o' or confirmation == 'oui':
        print("\nVotre kebab personnalisé est validé")

    return choix

if __name__ == "__main__":
    menu()