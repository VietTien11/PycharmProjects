import os
import math
import re

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def recuperer_noms_presidents(fichier):
    noms_presidents = {}
    liste = r"Nomination_(.*?)\d*\.txt"
    for file in os.listdir(fichier):
        chemin = os.path.join(fichier, file)
        if os.path.isfile(chemin) and fichier.endswith(".txt"):
            match = re.search(liste, file)
        if match:
            nom_complet = math.group(1)
            noms = nom_complet.split(" ")
            nom_famille = noms[-1]
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


def lower_letter(file_name):
    contentV1 = ""  # Initialisation of content V1 because we have to change all upper letter by lower letter
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()  # Here it's all the text of the speech store in the variable content
    for i in content:
        if ord(i) > 64 and ord(i) < 91:  # It's the interval of the upper letter in ASCII
            contentV1 = contentV1 + chr(ord(i) + 32)  # +32 in order to change upper letter into lower letter
        else:
            contentV1 = contentV1 + i
    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]}", "w",
              encoding="utf-8") as f:  # Create a New file with the New content
        f.write(contentV1)
    contentV2 = ""  # let's initialize a new variable in oder to change again and only have lower letter and nothing else
    for i in contentV1:
        if i == "-" or i == "'" or i == "." or i == "\n":
            contentV2 = contentV2 + " "
        elif ord(i) > 95 and ord(i) < 123 or ord(i) == 32 or i in "ùàéèôûîÉâêçŒœ" and not (i in ";:!?'"):
            contentV2 = contentV2 + i
    with open(f"Cleaned/{file_name.split('.')[0].split('/')[-1]}",
              "w", encoding="utf-8") as f:  # change the file with the New content
        f.write(contentV2)

#fonction qui prend en argument une phrase et renvoyant le nombre d'occurence des mots présents dans la phrase
def occurence(phrase : str, i):
    l = liste_TF[i]
    for mot in phrase.split():
        if mot in l.keys():
            l[mot] += 1
        else:
            l[mot] = 1
liste_TF = ({},{},{},{},{},{},{},{})


#fonction prenant en argument une matrice et renvoyant les mots
def mots_pas_importants(matrice):
    liste_mots = []
    n = len(matrice)
    m = len(cleanned_file)
    for i in range(n):
        moy = 0
        occ = 0
        for j in range(m):
            if matrice[i][j]
                occ += 1
    moy /= occ
    if moy <= 0.5 :
        mots = list(IDF.keys())
        mot = mots[i]
        liste_mot.append(mot)
    return liste_mots

def calculate_idf(directory):
    idf_dict = {}
    total_documents = len(os.listdir(directory))
    word_document_count = {}
    for file in os.listdir(directory):
        with open(f"{directory}/{file}", 'r', encoding='utf-8') as file:
            content = set(file.read().split())
            for mot in content:
                word_document_count[mot] = word_document_count.get(mot, 0) + 1
    for mot, count in word_document_count.items():
        idf_dict[mot] = math.log10(total_documents / count)
    return idf_dict


def calculate_tfidf_matrix(directory):
    idf_dict = calculate_idf(directory)
    tfidf_matrix = {}
    all_words = set()

    for file in os.listdir(directory):
        with open(f"{directory}/{file}", 'r', encoding='utf-8') as file:
            all_words.update(file.read().split())

    for file in os.listdir(directory):
        with open(f"{directory}/{file}", 'r', encoding='utf-8') as file:
            tf_dict = calculate_tf(file.read())
            for word in all_words:
                tfidf = tf_dict.get(word, 0) * idf_dict.get(word, 0)
                if word not in tfidf_matrix:
                    tfidf_matrix[word] = []
                tfidf_matrix[word].append(tfidf)

    return tfidf_matrix












