from function import *

if __name__ == '__main__':

    print("1 - Récupérer le noms des présidents")
    print("2 - Associer le prénom des présidents")
    print("3 - Calculer le nombre d'occurence des mots présents dans une phrase")
    print("4 - Renvoyer les mots les moins importants")
    print("5 - Calculer le score IDF")
    print("6 - Calculer le score TF")
    print("7 - Calculer le score TF-IDF")
    print("8 - Relever le ou les présidents qui ont parlé le plus de la Nation")
    print("9 - Relever les présidents qui ont parlé le plus du climat ou de l'écologie")
    print("10 - Relever les mots utilisés par tous les présidents")

    print("")
    choix = int(input("Votre choix: "))
    print("")

    if choix == 1:
        print(recuperer_noms_presidents(directory))
    if choix == 2:
        print(prenoms_president())
    if choix == 3:
        print(occurence(phrase ,str, i))
    if choix == 4:
        print(mots_pas_importants())
    if choix == 5:
        print(calcul_idf(directory))
    if choix == 6:
        print(calcul_tf(text))
    if choix == 7:
        print(calcul_tfidf(directory))
    if choix == 8:
        print(president_parlant_de_la_nation(directory))
    if choix == 9:
        print("Le premier président à avoir parlé de l'écologie est :",premier_president_ecologie(directory))
    if choix == 10:
        print(mots_cités_par_tout_le_monde(directory, matrice_tfidf))