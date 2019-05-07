##case_actuel=largeur*i+(j+1)

def listeVersVariable(liste):
    retour = []
    for x in range(0, len(liste)):
        for y in range(0, len(liste[0])):
            if liste[x][y]:
                retour.append(x * len(liste[0]) + y+1)
    return retour


def liste_to_dimacs(liste, defin=[], sattrois=True):

    defini = listeVersVariable(defin)
    fnc = list_to_fnc(liste, defini)
    nbvar = len(liste) * len(liste[0])

    if sattrois:
        fnc, nbvar = fnc_to_3fnc(fnc, nbvar)
    fnc_to_dimacs(fnc, nbvar)

def position_adjacente(p, largeur, hauteur):
    adj = [p - largeur, p, p + largeur]
    if p % largeur != 1:
        adj.append(p - 1 - largeur)
        adj.append(p - 1)
        adj.append(p - 1 + largeur)
    if p % largeur != 0:
        adj.append(p + 1 + largeur)
        adj.append(p + 1 - largeur)
        adj.append(p + 1)
    for i in range(len(adj)-1, 0-1, -1):
        if adj[i] <= 0:
            adj.pop(i)
            continue
        if adj[i] > (largeur*hauteur):
            adj.pop(i)
    return adj
position_adjacente(1,3,3)





def cote(i, j ,largeur,hauteur):
    retourne = ''

    if i == 0:
        if j == 0:
            return 'coin'  ##haut gauche
        elif j == largeur - 1:
            return 'coin'  ##haut droit
        return 'bord'  ##haut
    elif i == hauteur - 1:
        if j == 0:
            return 'coin'  ##bas gauche
        elif j == largeur - 1:
            return 'coin'  ##bas droit
        return 'bord'  ##bas
    elif j == 0:  ## gauche
        return 'bord'
    elif j == largeur - 1:  ## droit
        return 'bord'
    else:
        return 'milieu'  ## milieu


def certain(liste, fnc, i, j, largeur, hauteur):
    listecase=position_adjacente(largeur*i+(j+1),largeur,hauteur)
    for n in listecase:
        fnc.append([n])


def nul(liste, fnc, i, j, largeur,hauteur):
    listecase=position_adjacente(largeur*i+(j+1),largeur,hauteur)
    for n in listecase:
        fnc.append([-n])


def combinliste(seq, k):
    p = []
    imax = 2 ** len(seq)
    for i in range(imax):
        s = []
        jmax = len(seq)
        for j in range(jmax):
            if (i >> j) & 1 == 1:
                s.append(seq[j])
        if len(s) == k:
            p.append(s)
    return p


def clauses(chiffre, i):
    n = len(chiffre)
    chiffrenegatif = []
    for j in chiffre:
        chiffrenegatif.append(-j)
    positif = n - (i - 1)  ##nombre de variables dans les clauses "positives"
    negatif = i + 1  ##nombre de variables dans les clauses "negatives"
    clausepositive = combinliste(chiffre, positif)
    clausenegative = combinliste(chiffrenegatif, negatif)

    return (clausepositive, clausenegative)


def list_to_fnc(liste, defini = []):
    fnc = []
    for i in defini:
        fnc.append([i])
    hauteur = len(liste)
    largeur = len(liste[0])
    for ligne in range(len(liste)):
        for colonne in range(len(liste[0])):
            nb = liste[ligne][colonne]
            if nb != -1:
                if nb == 9 or ( (
                        ((cote(ligne, colonne, largeur, hauteur) == 'bord') and nb == 6) or (
                        (cote(ligne, colonne, largeur,hauteur) == 'coin') and nb == 4))):  # cas certain non nul
                    certain(liste, fnc, ligne, colonne, largeur, hauteur)

                elif nb == 0:  # cas certain nul
                    nul(liste, fnc, ligne, colonne, largeur,hauteur)
                else:  # cas incertain

                    chiffres = position_adjacente(largeur*ligne+(colonne+1),largeur,hauteur)

                    clausepositive, clausenegative = clauses(chiffres, nb)
                    for clp in clausepositive:
                        fnc.append(clp)
                    for cln in clausenegative:
                        fnc.append(cln)
    return fnc


def fnc_to_3fnc(fnc, nbvar):
    tfnc = []
    for i in fnc:
        while len(i) > 3:
            nbvar += 1
            partieun = []
            for j in range(2):
                partieun.append(i.pop(0))
            partieun.append(nbvar)
            i.insert(0, -nbvar)
            tfnc.append(partieun)
        tfnc.append(i)
    return tfnc,nbvar


def fnc_to_dimacs(fnc, nbvar):
    long = len(fnc)
    f = open("DIMACS.cnf", "w")
    f.write("p cnf " + str(nbvar) + " " + str(long) + "\n")
    for i in fnc:
        ligne = ''
        for j in i:
            ligne += str(j) + " "
        ligne += "0\n"
        f.write(ligne)
    f.close()



