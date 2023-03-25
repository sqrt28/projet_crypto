import module_arbre
import string

#text_input = input("saississez une phrase:\n")
text_input = "Portez ce vieux whisky au juge blond qui fume sur son île intérieure à côté de l'alcôve ovoïde où les bûches se consument dans l'âtre, ce qui lui permettra de penser à la cænogenèse de l'être dont il est question dans la cause ambiguë entendue à Moÿ, dans un capharnaüm qui, pense-t-il, diminue çà et là la qualité de son jugement."

# création d'un dico avec les lettres du text et leurs fréquences respectives
dico_lettre = dict()
for i in text_input:
    dico_lettre[i] = text_input.count(i)

# trie du dico_lettre
dico_lettre_trie = dict(sorted(dico_lettre.items(), key=lambda x: x[1]))
print(dico_lettre_trie)


# création de sommets
liste_sommets = list()
for key, value in dico_lettre_trie.items():
    liste_sommets.append(module_arbre.Sommet(key, value))
print(liste_sommets)

# affichage sommets
for i in range(len(liste_sommets)):
    print("lettre :", liste_sommets[i].get_lettre(
    ), "frequence:", liste_sommets[i].get_frequence())

liste_sommets_total = list()
for i in range(len(liste_sommets)):
    liste_sommets_total.append([liste_sommets[i].get_frequence(
    ), liste_sommets[i].get_lettre(), liste_sommets[i]])


# création de l'abre
liste_arbre = list()
for i in range(len(liste_sommets)-1):
    liste_arbre.append(module_arbre.ArbreB())


def creation_arbre(liste_des_sommets):
    liste_arbre = list()

    # for i in range(len(liste_sommets)//2):
    # liste_arbre.append(module_arbre.ArbreB())

    for i in range(len(liste_des_sommets)-2):
        liste_arbre.append(module_arbre.ArbreB())
        print(f"étape {i}\n")
        print(liste_des_sommets)
        liste_arbre[i].insertion(liste_des_sommets[0][2])
        liste_arbre[i].insertion(liste_des_sommets[1][2])
        liste_des_sommets.remove(liste_des_sommets[0])
        liste_des_sommets.remove(liste_des_sommets[0])
        liste_des_sommets.append([liste_arbre[i].get_racine().get_frequence(
        ), liste_arbre[i].get_racine().get_lettre(), liste_arbre[i].get_racine()])
        sorted(liste_des_sommets)
        """print(f"étape {i}\n")
        print(liste_des_sommets)"""
    liste_arbre.append(module_arbre.ArbreB())
    liste_arbre[-1].insertion(liste_des_sommets[0][2])
    liste_des_sommets.remove(liste_des_sommets[0])
    liste_arbre[-1].insertion(liste_des_sommets[0][2])
    liste_des_sommets.remove(liste_des_sommets[0])

    return liste_arbre


# affichage arbre
res = creation_arbre(liste_sommets_total)
for i in res:
    print(i.get_racine().get_lettre())


print(len(res))
# récupération code des chaques lettres


def recuperer_code_lettre(lettre):
    code_lettre = ""
    for i in range(len(res)-1, 0-1, -1):
        if lettre not in res[i].racine.get_lettre():
            pass
        if lettre in res[i].get_fils_gauche().get_lettre():
            code_lettre += "0"
        elif lettre == res[i].get_fils_gauche().get_lettre():
            return code_lettre

        if lettre in res[i].get_fils_droit().get_lettre():
            code_lettre += "1"
        elif lettre == res[i].get_fils_droit().get_lettre():
            return code_lettre
    return code_lettre


b = recuperer_code_lettre("b")


dico_lettre_codifie = {}
liste_caracteres = string.ascii_letters + string.punctuation
print(liste_caracteres)
for i in range(len(liste_caracteres)-1):
    dico_lettre_codifie[liste_caracteres[i]
                        ] = recuperer_code_lettre(liste_caracteres[i])
print(dico_lettre_codifie)


# codifier un texte
def crypter_text(texte):
    text_crypte = ""
    for i in texte:
        text_crypte += dico_lettre_codifie[i]
    return text_crypte

# vérifier que le texte à été crypter selon l'arbre binaire précedent


# décrypter le texte
def decrypter_text(text_crypte):
    text_decrypte = ""
    i = 0
    while i != len(text_crypte):
        valeur = text_crypte[i]
        while valeur not in dico_lettre_codifie.values():
            valeur += text_crypte[i+1]
            i += 1
        for key, value in dico_lettre_codifie.items():
            if value == valeur:
                text_decrypte += key
        i += 1
    return text_decrypte
