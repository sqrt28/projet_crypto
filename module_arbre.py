# Partie1

# 1,2 implémentation arbre
class Sommet(object):
    # chaque objet un sommet

    def __init__(self, lettre, frequence):
        self.lettre = lettre
        self.frequence = frequence

    def get_lettre(self):
        return self.lettre

    def get_frequence(self):
        return self.frequence

    def set_lettre(self, nv_lettre):
        self.lettre = nv_lettre


class ArbreB(Sommet):
    # chaque objet un arbre

    def __init__(self):
        self.racine = None
        self.fils_gauche = None
        self.fils_droit = None

    def get_racine(self):
        return self.racine

    def get_fils_gauche(self):
        return self.fils_gauche

    def get_fils_droit(self):
        return self.fils_droit

    def recherche(self, sommet):
        if sommet.get_lettre() == self.fils_gauche.get_lettre():
            return True
        if sommet.get_lettre() == self.fils_droit.get_lettre():
            return True

    def insertion(self, nouveau_sommet):
        if self.fils_gauche == None:
            self.fils_gauche = nouveau_sommet
        elif self.fils_droit == None:
            self.fils_droit = nouveau_sommet
        #else:
           # nouveau_sommet = ArbreB()

        if self.fils_gauche != None and self.fils_droit != None:
            self.racine = Sommet(self.fils_gauche.get_lettre()+self.fils_droit.get_lettre(
            ), self.fils_gauche.get_frequence()+self.fils_droit.get_frequence())

    def suppression(self, sommet):
        if sommet == self.racine:
            self.racine = None

        elif sommet == self.fils_gauche:
            self.fils_gauche = None

        elif sommet == self.fils_droit:
            self.fils_droit = None


    def fusion(arbre1,arbre2):
        fusion_arbre = ArbreB()
        fusion_arbre.fils_gauche = arbre1.get_racine().get_lettre()
        fusion_arbre.fils_droit = arbre2.get_racine().get_lettre()
        fusion_arbre.racine = Sommet(arbre1.get_racine().get_lettre()+arbre2.get_racine().get_lettre(),arbre1.get_racine().get_frequence()+arbre2.get_racine().get_frequence())
        return fusion_arbre

    def decomposition():
        pass

    def affichage(self):
        print("L'arbre a pour racine {0}, son fils gauche est {1} et sont fils droit est {2}".format(
            self.racine, self.fils_gauche, self.fils_droit))



# 3 test abre
s1 = Sommet("a", 2)
s2 = Sommet("e", 3)
s3 = Sommet("i", 7)
s4 = Sommet("u", 5)
a1 = ArbreB()
a2 = ArbreB()
a1.insertion(s1)
a1.insertion(s2)
a2.insertion(s3)
a2.insertion(s4)
arbre_fusion = ArbreB.fusion(a2,a1)
print(arbre_fusion.get_racine().get_lettre())





# 4 interface graphique (voir interface_graphique.py)
