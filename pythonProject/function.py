import os
import math
import re



def call_list_of_files():
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    return files_names




def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names




#cette fonction prend un argument un dossier fichier en renvoyant un dictionnaire avec les noms des présidents de chaque discours
def recuperer_noms_presidents(directory):
    motif = r"Nomination_(.*?)\d*\.txt"
    noms_presidents = {}
    for speeches in os.listdir(directory):
        chemin = os.path.join(directory, speeches)
        if os.path.isfile(chemin) and speeches.endswith(".txt"):
            correspondance = re.search(motif, speeches)
            if correspondance:
                nom_complet = correspondance.group(1)
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
        return("l'indice est invalide")
    else:
        print("Nom :", noms[n-1], "", "Prénom : ", prenoms[n-1])




#Fonction qui s'assure qu'un répertoire nommé "cleaned" existe à l'emplacement spécifié. S'il n'existe pas, elle le crée, et si ce répertoire est déjà présent, elle ne fait rien.
def clean_directory():
    directory = "cleaned"
    parent_directory = r"C:\Users\giang\OneDrive\Bureau\Travail VietTien\L1\projet python\PycharmProjects\pythonProject"
    path = os.path.join(parent_directory, directory)
    if not os.path.exists(path):
        os.mkdir(path)




#fonction qui prend en argument un fichier texte en renvoyant un fichier ayant transformé tout le fichier texte en lettre minsucule
fichier = "speeches/"
def cleaned(fichier):
    with open("speeches/" + fichier, "r") as f1, open("clean/" + fichier.strip(".txt") + "_clean.txt", "w") as f2:
        lignes = f1.readlines()
        caracteres_speciaux = [",", ";", ":", ".", "!", "?", "-", "'", "_"]

        for ligne in lignes:
            for caractere in ligne:
                if caractere in caracteres_speciaux:
                    caractere = " "
                    f2.write(caractere)
                elif 65 <= ord(caractere) <= 90:  # Vérifie si le caractère est une lettre majuscule
                    caractere = chr(ord(caractere) + 32)  # Convertit la lettre majuscule en lettre minuscule
                    f2.write(caractere)
                else:
                    f2.write(caractere)

#Fonction qui permet de clean un fichier en appelant la fonction call_list_of files
def call_clean_files():
    files_names = call_list_of_files()
    for noms in files_names:
        clean_files(noms)



#Fonction qui permet d'appeler les fichiers clean
def call_list_of_cleaned_files():
    directory = "./cleaned"
    files_names = list_of_files(directory, "txt")
    return files_names



#fonction qui prend en argument une phrase et renvoyant le nombre d'occurence des mots présents dans la phrase
def occurence(phrase , str, i):
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
    m = len(cleaned_file)
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


directory = "./speeches"
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
text = "messieurs les présidents mesdames messieurs en ce jour où je prends la responsabilité assumer la plus haute charge de etat je me sens dépositaire une espérance élection présidentielle a pas vu la victoire une france contre une autre une idéologie contre une autre elle a vu la victoire une france qui veut se donner les moyens entrer forte et unie dans le troisième millénaire le 7 mai le peuple français a exprimé sa volonté de changement je suis décidé à placer le septennat qui commence sous le signe de la dignité de la simplicité de la fidélité aux valeurs essentielles de notre république je aurai autre ambition que de rendre les français plus unis plus égaux et la france plus allante forte de son histoire comme de ses atouts je ferai tout pour qun etat impartial assumant pleinement ses missions de souveraineté et de solidarité soit pour les citoyens le garant de leurs droits et le protecteur de leurs libertés je ferai tout pour que notre démocratie soit affermie et mieux équilibrée par un juste partage des compétences entre exécutif et le législatif ainsi que avait voulu le général de gaulle fondateur de la vème république le président arbitrera fixera les grandes orientations assurera unité de la nation préservera son indépendance le gouvernement conduira la politique de la nation le parlement fera la loi et contrôlera action gouvernementale telles sont les voies à suivre je veillerai à ce qune justice indépendante soit dotée des moyens supplémentaires nécessaires à accomplissement de sa tâche surtout engagerai toutes mes forces pour restaurer la cohésion de la france et renouer le pacte républicain entre les français emploi sera ma préoccupation de tous les instants la campagne qui achève a permis à notre pays de se découvrir tel qil est avec ses cicatrices ses fractures ses inégalités ses exclus mais aussi avec son ardeur sa générosité son désir de rêver et de faire du rêve une réalité la france est un vieux pays mais aussi une nation jeune enthousiaste prête à libérer le meilleur elle même pour peu qon lui montre horizon et non étroitesse de murs clos le président françois mitterrand a marqué de son empreinte les quatorze ans qui viennent de écouler un nouveau septennat commence je voudrais qà issue de mon mandat les français constatent que le changement espéré a été réalisé je voudrais que plus assurés de leur avenir personnel tous nos compatriotes se sentent partie prenante un destin collectif je voudrais que ces années lourdes enjeux mais ouvertes à tous les possibles les voient devenir plus confiants plus solidaires plus patriotes et en même temps plus européens car la force intérieure est toujours la source un élan vers extérieur avec aide des hommes et des femmes de bonne volonté conformément à esprit et à la lettre de nos institutions et aussi à idée que je me fais de ma mission je serai auprès des français garant du bien public en charge des intérêts supérieurs de la france dans le monde et de universalité de son message vive la république vive la france"



#cette fonction prend en agrument un fichier en renvoyant une matrice
def calcul_tfidf(directory):
    matrice_tfidf = {}
    idf_dict = calcul_idf(directory)
    liste_mots = []

    for fichier in os.listdir(directory):
        with open(f"{directory}/{fichier}", 'r', encoding='utf-8') as fichier_ouvert:
            liste_mots.extend(fichier_ouvert.read().split())

    for fichier in os.listdir(directory):
        with open(f"{directory}/{fichier}", 'r', encoding='utf-8') as fichier_ouvert:
            tf_dict = calcul_tf(fichier_ouvert.read())
            for mot in set(liste_mots):
                tfidf = tf_dict.get(mot, 0) * idf_dict.get(mot, 0)
                if mot not in matrice_tfidf:
                    matrice_tfidf[mot] = []
                matrice_tfidf[mot].append(tfidf)

    return matrice_tfidf




directory = "./speeches"
#Fonction qui indique le(s) nom(s) du (des) président(s) qui a (ont) parlé de la " Nation " et celui qui a répété ce mot le plus de fois
def president_parlant_de_la_nation(directory):
    frequences_nation = {}
    frequence_max = 0
    president_max = ""
    for speeches in os.listdir(directory):
        with open(f"{directory}/{speeches}", 'r', encoding='utf-8') as contenu_fichier:
            contenu = contenu_fichier.read()
            compte = contenu.count("nation")
            if compte > 0:
                president = re.match(r"Nomination_([a-zA-Z\s]+)(\d*)\.txt", speeches).group(1)
                frequences_nation[president] = frequences_nation.get(president, 0) + compte
                if frequences_nation[president] > frequence_max:
                    frequence_max = frequences_nation[president]
                    president_max = president

    return frequences_nation, president_max



directory = "./speeches"
#Cette fonction parcourt les fichiers et vérifie la présence des mots "climat" ou "écologie" dans chaque fichier.
def premier_president_ecologie(directory):
    for speeches in sorted(os.listdir(directory)):
        with open(f"{directory}/{speeches}", 'r', encoding='utf-8') as contenu_fichier:
            contenu = contenu_fichier.read()
            if "climat" in contenu or "écologie" in contenu:
                return re.match(r"Nomination_([a-zA-Z\s]+)(\d*)\.txt", speeches).group(1)
    return None



matrice_tfidf = calcul_tfidf("cleaned")
directory = "./speeches"
#cette fonction extrait les mots les plus fréquemment utilisés dans tous les fichiers d'un répertoire donné, en filtrant les mots non importants et en les classant par fréquence d'apparition totale.
def mots_cités_par_tout_le_monde(directory, matrice_tfidf):
    mots_non_importants = mots_pas_importants(matrice_tfidf)
    texte_complet = ""

    for fichier in os.listdir(directory):
        with open(f"{directory}/{fichier}", 'r', encoding='utf-8') as fichier_ouvert:
            texte_complet += fichier_ouvert.read() + " "
    tf_tous = {}
    for fichier in os.listdir(directory):
        with open(f"{directory}/{fichier}", 'r', encoding='utf-8') as fichier_ouvert:
            tf_dict = calcul_tf(fichier_ouvert.read())
            for mot, tf in tf_dict.items():
                if mot not in texte_complet:
                    continue
                if mot not in tf_tous:
                    tf_tous[mot] = 0
                tf_tous[mot] += tf
    mots_filtres = {}
    for mot, compteur in tf_tous.items():
        if mot not in mots_pas_importants:
            mots_filtres[mot] = compteur
    mots_tries = sorted(mots_filtres.items(), key=lambda x: x[1], reverse=True)
    return mots_tries





###########################################################################################
##################################### PARTIE 2 ############################################
###########################################################################################



#Fonction qui clean la question
def question_tokenisation(question):
    question = question.lower()
    question = re.sub(r"\w[’']", '', question)
    question = re.sub(r"-", ' ', question)
    question = re.sub(r"[^\w\s]", '', question)
    question = re.sub(r"\s+", ' ', question).strip()
    return question

question = ''
question = question_tokenisation(question)

#Fonction qui calcule le score idf d'une question
def calculer_idf_question(question, repertoire):
    compte_mot_document = {}
    idf_corpus = calcul_idf(repertoire)
    print(idf_corpus)
    contenu_question = set(question.split())
    for mot in contenu_question:
        if mot in contenu_question:
            if mot not in idf_corpus:
                compte_mot_document[mot] = 0
            else:
                compte_mot_document[mot] = idf_corpus[mot]
    return compte_mot_document

idf_question = calculer_idf_question(question, "cleaned")

#Fonction qui calcule le score TF-IDF pour chaque mot présent dans une question donnée, en utilisant un dictionnaire des scores IDF préalablement calculés.
def calculer_tfidf(question, calculer_idf):
    mots_dans_question = question.split()
    tfidf_question = {}
    for mot in set(mots_dans_question):
        tf = mots_dans_question.count(mot)
        idf = calculer_idf.get(mot, 0)
        tfidf_question[mot] = tf * idf
    return tfidf_question

tfidf_question = calculer_tfidf(question, idf_question)


#Fonction qui calcule le produit scaleire de deux vecteurs saisie en argument
def produit_scalaire(vecteursA,vecteursB):
    resultat = 0
    for i in range(len(vectorsA)):
        resultat += vecteursA[i] * vecteursB[i]
    return resultat


#Fonction qui calcule la norme d'un vecteur mis en argument
def calculer_norme(vecteursA):
    norme = math.sqrt(sum(x ** 2 for x in vecteursA)) # Calcul de la norme euclidienne du vecteur A
    return norme

def similarite(vecteursA,vecteursB):
    score=(produit_scalaire(vecteursA,vecteursB))/(calculer_norme(vecteursA)*calculer_norme(vecteursB))
    return score

#Fonction prenant en argument une matric et renvoie le nom du fichier correspondant à l'indice de la plus grande similarité.
def document_le_plus_pertinent(matrice_similarite):
    name_of_files = real_list_of_file("./speeches")
    maximum = similarite(matrice_similarite[0], matrice_similarite[len(matrice_similarite) - 1])
    for i in range(len(matrice_similarite) - 1):
        similaire = similarite(matrice_similarite[i], matrice_similarite[len(matrice_similarite) - 1])
        if maximum < similaire:
            maximum = similaire
            indice_maximum = i
    return name_of_files[indice_maximum]


#Fonction qui prend en argument le chemin d'un dossier et un mot, renvoyant la phrase contenant ce mot dans le fichier mis en argument
def extraire_phrase_avec_mot(chemin_document, mot):
    with open(chemin_document, 'r', encoding='utf-8') as fichier:
        texte = fichier.read()
        phrases = texte.split(".")
        for phrase in phrases:
            if mot in phrase.lower():
                return phrase.strip() + '.'
    return "Le mot n'a pas été trouvé dans le document."
