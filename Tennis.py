from random import randint
class ORDI():

    def __init__(self): #Définir un classe incluant les score d'une partie de Tennis. Le système de point utilisé est le même qui celui d'un match de Tennis classique
        self.score = 0
        self.jeux = 0
        self.sets = 0
        self.etatVictoire = 0

    def gainPoint(self,joueur): # Mise en place du système de point. Au Tennis, les points ne se compte pas de 1 en 1. Voir explications des règles plus haut.
        if self.score == 0:
            self.score = 15 #Le joueur ne gagne pas 1, mais 15 points lorsqu'il marque un premier point.
        else:
            if self.score == 15:
                self.score = 30 #Son score est de 30 s'il en gagne un deuxième...
                
            else:
                if self.score == 30:
                    self.score = 40 #...de 40 s'il en marque un 3ème
                else:
                    if self.score == 40 and joueur.score == 40: #Lorsqu'il y a 40A, il faut gagner l'avantage puis un autre point pour gagner le jeu
                        self.score = 50
                    else:
                        if self.score == 40 and joueur.score == 50: #
                            joueur.score = 40
                        else:
                            if self.score == 40 or self.score == 50:
                                self.score = 0
                                joueur.score = 0
                                self.jeux = self.jeux + 1 #Un jeu de plus pour le joueur qui remporte les points nécessaires au gain d'un jeu
                                self.gainJeu(joueur)
    def gainJeu(self,joueur):
        if self.jeux >= 6 and joueur.jeux <= self.jeux - 2:
            self.sets = self.sets + 1
            self.jeux, joueur.jeux = 0, 0
            self.gainSet(joueur)
        else:
            if self.jeux == joueur.jeux and self.jeux == 6:
                self.jeux, joueur.jeux = 0, 0
                joueur.tieBreak()
            else:
                if self.jeux >= 25:
                    self.gainSet(joueur)
    def gainSet(self,joueur):
        if self.sets  == 2:
            self.score, joueur.score = 0, 0
            self.jeux, joueur.jeux = 0, 0
            self.sets, joueur.sets = 0, 0
            self.etatVictoire = 1
            
    def finpartie(self):
        self.score = 0
        self.jeux = 0
        self.sets = 0

class JOUEURIA():

    def __init__(self):
        self.score = 0
        self.jeux = 0
        self.sets = 0
        self.victoires = 0
        self.etatVictoire = 0
        self.nom = self

    def affronte(self):
        while self.etatVictoire == 0 and ordi.etatVictoire == 0:
            balle = randint(0,1)
            if balle == 0:
                ordi.gainPoint(self)
            else:
                self.gainPoint()
        if self.etatVictoire == 1:
            self.etatVictoire = 0
            self.victoires = self.victoires + 1
        else:
            if ordi.etatVictoire == 1:
                ordi.etatVictoire = 0

            
    def gainPoint(self):
        if self.score == 0:
            self.score = 15
        else:
            if self.score == 15:
                self.score = 30
            else:
                if self.score == 30:
                    self.score = 40
                else:
                    if self.score == 40 and ordi.score == 40:
                        self.score = 50
                    else:
                        if self.score == 40 and ordi.score == 50:
                            self.score = 40
                        else:
                            if self.score == 40 or self.score == 50:
                                self.score = 0
                                ordi.score = 0
                                self.jeux = self.jeux + 1
                                self.gainJeu()

    def gainJeu(self):
        if self.jeux >= 6 and ordi.jeux <= self.jeux - 2:
            self.jeux = 0
            ordi.jeux = 0
            self.sets = self.sets + 1
            self.gainSet()
        else:
            if self.jeux == ordi.jeux and self.jeux == 6:
                self.jeux, ordi.jeux = 0, 0
                self.tieBreak()
            else:
                if self.jeux >= 25:
                    self.gainSet()
    def tieBreak(self):
        while self.score  < 7 and ordi.score < 7:
            balle = randint(0,1)
            if balle == 0:
                self.score = self.score + 1
            else:
                ordi.score = ordi.score + 1
        if ordi.score == 7:
            ordi.score = 0
            self.score = 0
            ordi.gainSet(self)
        if self.score == 7:
            ordi.score = 0
            self.score = 0
            self.gainSet()
                                
    def gainSet(self):
        if self.sets  == 2:
            self.score, ordi.score = 0, 0
            self.jeux, ordi.jeux = 0, 0
            self.sets, ordi.sets = 0, 0
            self.etatVictoire = 1
        
def genJoueurs(nombreJoueurs):
    Joueur = []
    for i in range (nombreJoueurs):        
        Joueur.append("Joueur{0}".format(i))
        Joueur[i] = JOUEURIA()
    return Joueur
def Lancement():
    for i in range(100):
        for i in range(len(listeJoueurs)):            
            joueurEnCours = listeJoueurs[i]
            joueurEnCours.affronte()
            listeJoueurs[i] = joueurEnCours
ordi = ORDI()
        
    
