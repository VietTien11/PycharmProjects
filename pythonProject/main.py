from function import *

if __name__ == '__main__':
    f = int(input("Saisir le numéreo de la fonction voulu : \n"))
    if f == 1:
        recuperer_noms_presidents(fichier)
    elif f == 2:
        prenoms_president()
    elif f == 3:
        minuscule(fichier)
    elif f == 4:
        occurence(phrase, i)
    elif f == 5:
        mots_pas_importants(matrice)
    elif f == 6:
        calcul_idf(directory)
    elif f == 7 :
        calcul_tf(text)
    elif f == 8:
        calcul_matrice_tf_idf(fichier)
    else :
        print('indice incorrect')


