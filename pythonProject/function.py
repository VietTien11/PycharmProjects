import os
import math
import re

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#cette fonction prend un argument un dossier fichier en renvoyant un dictionnaire avec les noms des présidents de chaque discours
def recuperer_noms_presidents(speeches):
    liste = r"Nomination_(.*?)\d*\.txt"
    noms_presidents = {}
    for file in os.listdir(speeches):
        chemin = os.path.join(speeches, file)
        if os.path.isfile(chemin) and speeches.endswith(".txt"):
            match = re.search(liste, file)
        if match:
            nom_complet = math.group(1)
            nom_famille = noms[-1]
            noms = nom_complet.split(" ")
            if nom_famille not in noms_presidents:
                noms_presidents[nom_famille] = noms[:-1]
    return noms_presidents



# Cette fonction permet de déterminer le prénom du président en fonction de l'indice du discours choisi par l'utilisateur
def prenoms_president():
    n = int(input("saisir l'indice du discours voulu :\n"))
    noms = ["Chirac","Chirac", "d'Estaing", "Hollande", "Macron", "Mitterrand","Mitterrand", "Sarkozy"]
    prenoms = ["Jacques","Jacques","Valérie Giscard","François","Emmanuel","François","François","Nicolas"]
    if  n>9 :
        print("l'indice est invalide")
    else:
        print("Nom :", noms[n-1], "", "Prénom : ", prenoms[n-1])

#fonction qui prend en argument un fichier texte en renvoyant un fichier ayant transformé tout le fichier texte en lettre minsucule
def minuscule(speeches):
    file1 = ""
    with open(speeches, "r", encoding="utf-8") as f:
        phrase = f.read()
    for i in phrase:
        if ord(i) > 64 and ord(i) < 91:
            file1 +=  chr(ord(i) + 32)
        else:
            file1 += i
    with open(f"cleaned/{speeches.split('.')[0].split('/')[-1]}", "w",
              encoding="utf-8") as f:
        f.write(file1)
    file2 = ""
    for i in file1:
        if i == "-" or i == "'" or i == "." or i == "\n":
            file2 +=  " "
        elif ord(i) > 95 and ord(i) < 123 or ord(i) == 32 or i in "ùàéèôûîÉâêçŒœ" and not (i in ";:!?'"):
            file2 += i
    with open(f"cleaned/{fichier.split('.')[0].split('/')[-1]}",
              "w", encoding="utf-8") as f:
        f.write(file2)

#fonction qui prend en argument une phrase et renvoyant le nombre d'occurence des mots présents dans la phrase
def occurence(phrase : str, i):
    l = liste_TF[i]
    for mot in phrase.split():
        if mot in l.keys():
            l[mot] += 1
        else:
            l[mot] = 1
liste_TF = ({},{},{},{},{},{},{},{})


#fonction prenant en argument une matrice et renvoyant les mots les moins importants
def mots_pas_importants(matrice):
    liste_mots = []
    n = len(matrice)
    m = len(cleanned_file)
    for i in range(n):
        moy = 0
        occ = 0
        for j in range(m):
            if matrice[i][j]:
                occ += 1
    moy /= occ
    if moy <= 0.5 :
        mots = list(IDF.keys())
        mot = mots[i]
        liste_mot.append(mot)
    return liste_mots


#fonction prenant en argument un fichier texte en renvoyant le score idf
def calcul_idf(directory):
    word_document_count = {}
    score_idf = {}
    total_documents = len(os.listdir(directory))
    for file in os.listdir(directory):
        with open(f"{directory}/{file}", 'r', encoding='utf-8') as file:
            content = set(file.read().split())
            for mot in content:
                word_document_count[mot] = word_document_count.get(mot, 0) + 1
    for mot, count in word_document_count.items():
        score_idf[mot] = math.log10(total_documents / count)
    return score_idf


#fonction prenant en argument un fichier texte en renvoyant le score tf
def calcul_tf(text):
    score_tf = {}
    words = text.split()
    for word in words:
        score_tf[word] = score_tf.get(word, 0) + 1
    return score_tf

#cette fonction prend en agrument un fichier en renvoyant une matrice
def calcul_matrice_tf_idf(fichier):
    tfidf_matrix = {}
    idf_dict = calculate_idf(fichier)
    liste_mots = []
    for file in os.listdir(fichier):
        with open(f"{fichier}/{file}", 'r', encoding='utf-8') as file:
            liste_mots.update(file.read().split())
    for file in os.listdir(fichier):
        with open(f"{fichier}/{file}", 'r', encoding='utf-8') as file:
            tf_dict = calculate_tf(file.read())
            for word in liste_mots:
                tfidf = tf_dict.get(word, 0) * idf_dict.get(word, 0)
                if word not in tfidf_matrix:
                    tfidf_matrix[word] = []
                tfidf_matrix[word].append(tfidf)
    return tfidf_matrix


def all_speech(directory):
    all_speeches = ""
    for filename in os.listdir(directory):
        score_tf_idf = dict()
        with open(f"{directory}/{filename}", "r", encoding="utf-8") as f:
            speech = f.read()
            all_speeches += speech
    return all_speeches



def scalar_product(vectorsA,vectorsB):
    result = 0
    for i in range(len(vectorsA)):
        result += vectorsA[i] * vectorsB[i]
    return result







