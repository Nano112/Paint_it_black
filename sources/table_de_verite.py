def affichage(liste):
    for i in range(len(liste[0])):
        print('| ',end='')
        for j in range(len(liste)):
            print(str(liste[j][i])+' |',end='')
        print()

def tableV(entier):
    liste=[]
    deuxn=2**entier
    div=2
    nb=0
    boole=False
    for i in range(entier):
        boole=False
        nb=0
        liste.append([])
        alt=deuxn/div
        for j in range(deuxn):
            if boole:
                liste[i].append(0)
                nb-=1
            else:
                liste[i].append(1)
                nb+=1
            if nb==alt:
                boole=True
            elif nb==0:
                boole=False
        div*=2

    return liste


def xOr(entier):
    liste=tableV(entier)
    for i in range(len(liste[0])):
        som=0
        ligne='| '
        for j in range(len(liste)):
            ligne+=str(liste[j][i])+' |'
            som+=liste[j][i]
        if som==1:
            print(ligne+str(1)+' |')
    
def linetostr(liste):
    ligne='| '
    for i in range(len(liste)):
        ligne+=str(liste[i])+' |'
    return ligne
    
def nombrecase(nb,affich=False,FNCbool=False):
    liste=tableV(9)
    tab=[]
    for i in range(len(liste[0])):
        tab.append([])
        som=0
        ligne=[]
        for j in range(len(liste)):
            ligne.append(liste[j][i])
            som+=liste[j][i]
        if FNCbool==False:
            if som==nb:
                tab.append(ligne)
                if affich:
                    print(linetostr(ligne))
        else:
            if som!=nb:
                tab.append(ligne)
                if affich:
                    print(linetostr(ligne))
    i=len(tab)-1
    while i!=-1:
        if tab[i]==[]:
            tab.pop(i)
        i-=1
    return tab


def FND(liste):
    n=0
    for i in range(len(liste)):
        var=1
        n+=1
        print('(',end='')
        for j in range(len(liste[i])):
            if liste[i][j]==1:
                print(' '+str(var),end=' ')
            else:
                print(' ¬'+str(var),end=' ')
            if j!=len(liste[i])-1:
                print('Ʌ',end='')
            var+=1
        print(')',end='')
        if i!=len(liste)-1:
            print('V')
    print()
    print(n)

def FNDXOR(nb):
    FND(nombrecase(nb))


def FNC(liste):
    n=0
    for i in range(len(liste)):
        var=1
        n+=1
        print('(',end='')
        for j in range(len(liste[i])):
            if liste[i][j]==1:
                print(' ¬'+str(var),end=' ')
            else:
                print('  '+str(var),end=' ')
            if j!=len(liste[i])-1:
                print('V',end='')
            var+=1
        print(')',end='')
        if i!=len(liste)-1:
            print('Ʌ')
    print()
    print(n)

def FNCXOR(nb):
    FNC(nombrecase(nb,False,True))
