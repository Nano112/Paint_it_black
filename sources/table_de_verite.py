##case_actuel=lng*i+(j+1)

def listeVersVariable(liste):
    retour = []
    for x in range(0, len(liste)):
        for y in range(0, len(liste[0])):
            if liste[x][y]:
                retour.append(x * len(liste) + y)
    return retour


def liste_to_dimacs(liste, defin=[], sattrois=True):

    defini = listeVersVariable(defin)
    print(defini)
    fnc = list_to_fnc(liste, defini)
    nbvar = len(liste) * len(liste[0])

    if sattrois:
        fnc, nbvar = fnc_to_3fnc(fnc, nbvar)
    fnc_to_dimacs(fnc, nbvar)

def position_adjacente(p, largeur, hauteur):
    adj = []
    adj.append(p-1-largeur)
    adj.append(p-largeur)
    adj.append(p+1-largeur)
    adj.append(p-1)
    adj.append(p)
    adj.append(p+1)
    adj.append(p - 1 + largeur)
    adj.append(p + largeur)
    adj.append(p + 1 + largeur)
    for i in range(0,len(adj)):
        if adj[i]<0 | adj[i]>(largeur*hauteur):
            adj.remove(i)
    return adj





def cote(i, j, lng):
    retourne = ''

    if i == 0:
        if j == 0:
            return 'coin'  ##haut gauche
        elif j == lng - 1:
            return 'coin'  ##haut droit
        return 'bord'  ##haut
    elif i == lng - 1:
        if j == 0:
            return 'coin'  ##bas gauche
        elif j == lng - 1:
            return 'coin'  ##bas droit
        return 'bord'  ##bas
    elif j == 0:  ## gauche
        return 'bord'
    elif j == lng - 1:  ## droit
        return 'bord'
    else:
        return 'milieu'  ## milieu


def certain(liste, fnc, i, j, lng):
    if i > 0:  # ligne 1
        if j > 0:
            fnc.append([(i - 1) * lng + j])
        fnc.append([(i - 1) * lng + j + 1])
        if j < lng - 1:
            fnc.append([(i - 1) * lng + j + 2])

    if j > 0:  # ligne 2
        fnc.append([i * lng + j])
    fnc.append([i * lng + j + 1])
    if j < lng - 1:
        fnc.append([i * lng + j + 2])

    if i < lng - 1:  # ligne 3
        if j > 0:
            fnc.append([(i + 1) * lng + j])
        fnc.append([(i + 1) * lng + j + 1])
        if j < lng - 1:
            fnc.append([(i + 1) * lng + j + 2])


def nul(liste, fnc, i, j, lng):
    if i > 0:  # ligne 1
        if j > 0:
            fnc.append([-((i - 1) * lng + j)])
        fnc.append([-((i - 1) * lng + j + 1)])
        if j < lng - 1:
            fnc.append([-((i - 1) * lng + j + 2)])

    if j > 0:  # ligne 2
        fnc.append([-(i * lng + j)])
    fnc.append([-(i * lng + j + 1)])
    if j < lng - 1:
        fnc.append([-(i * lng + j + 2)])

    if i < lng - 1:  # ligne 3
        if j > 0:
            fnc.append([(-(i + 1) * lng + j)])
        fnc.append([-((i + 1) * lng + j + 1)])
        if j < lng - 1:
            fnc.append([-((i + 1) * lng + j + 2)])


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
    lng = len(liste)
    for ligne in range(len(liste)):
        for colonne in range(len(liste)):
            nb = liste[ligne][colonne]
            if nb != -1:
                if nb == 9 or ( (
                        ((cote(ligne, colonne, lng) == 'bord') and nb == 6) or (
                        (cote(ligne, colonne, lng) == 'coin') and nb == 4))):  # cas certain non nul
                    certain(liste, fnc, ligne, colonne, lng)

                elif nb == 0:  # cas certain nul
                    nul(liste, fnc, ligne, colonne, lng)
                else:  # cas incertain

                    chiffres = []  ##definition des chiffres couverts
                    if ligne > 0:  # ligne 1
                        if colonne > 0:
                            chiffres.append(((ligne - 1) * lng + colonne))
                        chiffres.append(((ligne - 1) * lng + colonne + 1))
                        if colonne < lng - 1:
                            chiffres.append(((ligne - 1) * lng + colonne + 2))
                    if colonne > 0:  # ligne 2
                        chiffres.append((ligne * lng + colonne))
                    chiffres.append((ligne * lng + colonne + 1))
                    if colonne < lng - 1:
                        chiffres.append((ligne * lng + colonne + 2))
                    if ligne < lng - 1:  # ligne 3
                        if colonne > 0:
                            chiffres.append(((ligne + 1) * lng + colonne))
                        chiffres.append(((ligne + 1) * lng + colonne + 1))
                        if colonne < lng - 1:
                            chiffres.append(((ligne + 1) * lng + colonne + 2))

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



