def ajouter_tache(taches, prochain_numero):
    titre = input("Titre de la tâche : ").strip()

    while titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        titre = input("Titre de la tâche : ").strip()

    taches.append({"numero": prochain_numero, "titre": titre})
    print("Tâche ajoutée avec succès.")
    return prochain_numero + 1


def afficher_taches(taches):
    if len(taches) == 0:
        print("La liste des tâches est vide.")
    else:
        print("\n--- LISTE DES TÂCHES ---")
        for tache in taches:
            print(str(tache["numero"]) + " - " + tache["titre"])


def rechercher_tache(taches):
    mot_cle = input("Mot-clé à rechercher : ").strip()
    if mot_cle == "":
        print("Erreur : le mot-clé ne peut pas être vide.")
        return

    resultats = []
    for tache in taches:
        if mot_cle.lower() in tache["titre"].lower():
            resultats.append(tache)

    if len(resultats) == 0:
        print("Aucune tâche ne correspond à votre recherche.")
    else:
        print("\n--- RÉSULTATS DE LA RECHERCHE ---")
        for tache in resultats:
            print(str(tache["numero"]) + " - " + tache["titre"])


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")


def main():
    taches = []
    prochain_numero = 1
    choix = ""

    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            prochain_numero = ajouter_tache(taches, prochain_numero)
        elif choix == "2":
            afficher_taches(taches)
        elif choix == "3":
            rechercher_tache(taches)
        elif choix == "0":
            print("Fermeture du programme. Au revoir !")
        else:
            print("Erreur : option invalide. Veuillez choisir 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()

