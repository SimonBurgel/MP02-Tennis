class joueur():

    def __init__(self):
        self.score = 0
        self.jeux = 0
        self.sets = 0
        self.jeuxTotaux = 0
        self.setsTotaux = 0
        self.victoires = 0

    def affronte(self,adversaire):
        a
    def gainPoint(self,adversaire): #Le joueur gagne un poin contre son adversaire
        if self.score == 0:
            self.score = 15
        else:
            if self.score == 15:
                self.score = 30
            else:
                if self.score == 30:
                    self.score = 40
                else:
                    if self.score == 40 and adversaire.score == 40:
                        self.score = 50
                    else:
                        if self.score == 40 and adversaire.score == 50:
                            adversaire.score == 40
                        else:
                            if self.score == 40 or self.score == 50:
                                self.score = 0
                                adversaire.score = 0
                                self.gainJeu(adversaire)

    def gainJeu(self,adversaire):
                     
                                
    def gainSet(self):
        
    def victoire(self):
        
    
