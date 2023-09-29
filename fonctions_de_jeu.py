import pygame
from variable import *
from importation_images import *

def reaffichage():
    #reaffichage du plateau
    screen.blit(echiquier, (0, 0))

    for p in pieces_noires:
        if p=='pion':
            for k in range (len(pieces_noires[p])):
                c=coordonnées_cases[tab120[pieces_noires[p][k][0]]]
                screen.blit(pion_noir,c[0])
        elif p=='tour':
            for k in range (len(pieces_noires[p])):
                c=coordonnées_cases[tab120[pieces_noires[p][k]]]
                screen.blit(tour_noir,c[0])
        elif p=='cavalier':
            for k in range (len(pieces_noires[p])):
                c=coordonnées_cases[tab120[pieces_noires[p][k]]]
                screen.blit(cavalier_noir,c[0])
        elif p=='fou':
            for k in range (len(pieces_noires[p])):
                c=coordonnées_cases[tab120[pieces_noires[p][k]]]
                screen.blit(fou_noir,c[0])
        elif p=='reine':
            for k in range (len(pieces_noires[p])):
                c=coordonnées_cases[tab120[pieces_noires[p][k]]]
                screen.blit(reine_noir,c[0])
        elif p=='roi':
            for k in range (len(pieces_noires[p])):
                c=coordonnées_cases[tab120[pieces_noires[p][k]]]
                screen.blit(roi_noir,c[0])

    for p in pieces_blanches:
        if p=='pion':
            for k in range (len(pieces_blanches[p])):
                c=coordonnées_cases[tab120[pieces_blanches[p][k][0]]]
                screen.blit(pion_blanc,c[0])
        elif p=='tour':
            for k in range (len(pieces_blanches[p])):
                c=coordonnées_cases[tab120[pieces_blanches[p][k]]]
                screen.blit(tour_blanc,c[0])
        elif p=='cavalier':
            for k in range (len(pieces_blanches[p])):
                c=coordonnées_cases[tab120[pieces_blanches[p][k]]]
                screen.blit(cavalier_blanc,c[0])
        elif p=='fou':
            for k in range (len(pieces_blanches[p])):
                c=coordonnées_cases[tab120[pieces_blanches[p][k]]]
                screen.blit(fou_blanc,c[0])
        elif p=='reine':
            for k in range (len(pieces_blanches[p])):
                c=coordonnées_cases[tab120[pieces_blanches[p][k]]]
                screen.blit(reine_blanc,c[0])
        elif p=='roi':
            for k in range (len(pieces_blanches[p])):
                c=coordonnées_cases[tab120[pieces_blanches[p][k]]]
                screen.blit(roi_blanc,c[0])

    pygame.display.update()


def pion_derniere_ligne(pB,pN):
    pionsB=pB['pion']
    pionsN=pN['pion']
    for i in range (len(pionsN)):
        if pionsN[i][0]==91 or pionsN[i][0]==92 or pionsN[i][0]==93 or pionsN[i][0]==94 or pionsN[i][0]==95 or pionsN[i][0]==96 or pionsN[i][0]==97 or pionsN[i][0]==98:
            return (True,i)
    for i in range (len(pionsB)):
        if pionsB[i][0]==21 or pionsB[i][0]==22 or pionsB[i][0]==23 or pionsB[i][0]==24 or pionsB[i][0]==25 or pionsB[i][0]==26 or pionsB[i][0]==27 or pionsB[i][0]==28:
            return (True,i)
    return (False,-1)

def promotion(coord,i,tour):
    global pieces_blanches
    global pieces_noires

    if tour==True:
        if coord[0]>50 and coord[0]<515 and coord[1]>50 and coord[1]<150:
            if coord[0]>50 and coord[0]<166:
                pieces_blanches['reine'].append(pieces_blanches['pion'][i][0])
            elif coord[0]>=166 and coord[0]<282:
                pieces_blanches['fou'].append(pieces_blanches['pion'][i][0])
            elif coord[0]>=282 and coord[0]<398:
                pieces_blanches['cavalier'].append(pieces_blanches['pion'][i][0])
            else:
                pieces_blanches['tour'].append(pieces_blanches['pion'][i][0])

            del pieces_blanches['pion'][i]

            reaffichage()
            return True

        return False

    else:
        if coord[0]>50 and coord[0]<508 and coord[1]>450 and coord[1]<550:
            if coord[0]>50 and coord[0]<164:
                pieces_noires['reine'].append(pieces_noires['pion'][i][0])
            elif coord[0]>=164 and coord[0]<279:
                pieces_noires['fou'].append(pieces_noires['pion'][i][0])
            elif coord[0]>=279 and coord[0]<393:
                pieces_noires['cavalier'].append(pieces_noires['pion'][i][0])
            else:
                pieces_noires['tour'].append(pieces_noires['pion'][i][0])

            del pieces_noires['pion'][i]

            reaffichage()
            return True

        return False


def initialisation (coord):
    global liste_coup_joué
    global tour
    global petit_roque_blanc,petit_roque_noir,grand_roque_blanc,grand_roque_noir
    global pieces_noires,pieces_blanches

    pieces_noires={
    'pion':[[31,False],[32,False],[33,False],[34,False],[35,False],[36,False],[37,False],[38,False]],#numero de case tab64, possibilité d'être prit en passant (devient true pouur un tour puis ils repassent tous false au debut du tour du joueur
    'tour':[21,28],
    'fou':[23,26],
    'cavalier':[22,27],
    'reine':[24],
    'roi':[25]
    }

    pieces_blanches={
    'pion':[[81,False],[82,False],[83,False],[84,False],[85,False],[86,False],[87,False],[88,False]],#numero de case tab64, possibilité d'être prit en passant (devient true pouur un tour puis ils repassent tous false au debut du tour du joueur
    'tour':[91,98],
    'fou':[93,96],
    'cavalier':[92,97],
    'reine':[94],
    'roi':[95]
    }
    tour=True
    liste_coup_joué=[(pieces_blanches,pieces_noires,tour)]
    petit_roque_blanc,petit_roque_noir=True,True
    grand_roque_blanc,grand_roque_noir=True,True

    screen.blit(tour_noir, coord[0][0])
    screen.blit(tour_noir, coord[7][0])
    screen.blit(cavalier_noir, coord[1][0])
    screen.blit(cavalier_noir, coord[6][0])
    screen.blit(fou_noir, coord[2][0])
    screen.blit(fou_noir, coord[5][0])
    screen.blit(reine_noir, coord[3][0])
    screen.blit(roi_noir, coord[4][0])

    screen.blit(tour_blanc, coord[56][0])
    screen.blit(tour_blanc, coord[63][0])
    screen.blit(cavalier_blanc, coord[57][0])
    screen.blit(cavalier_blanc, coord[62][0])
    screen.blit(fou_blanc, coord[58][0])
    screen.blit(fou_blanc, coord[61][0])
    screen.blit(reine_blanc, coord[59][0])
    screen.blit(roi_blanc, coord[60][0])

    for i in range (8,16):
        screen.blit(pion_noir, coord[i][0])

    for i in range (48,56):
        screen.blit(pion_blanc, coord[i][0])

def selection_piece(coord_p,tour):
    if tour==True:
        for p in pieces_blanches:
            if p=='pion':
                for k in range (len(pieces_blanches[p])):
                    c=coordonnées_cases[tab120[pieces_blanches[p][k][0]]]
                    if c[0][0]<coord_p[0] and coord_p[0]<c[1][0] and c[0][1]<coord_p[1] and coord_p[1]<c[1][1]:
                        return (p,k)
            else:
                for k in range (len(pieces_blanches[p])):
                    c=coordonnées_cases[tab120[pieces_blanches[p][k]]]
                    if c[0][0]<coord_p[0] and coord_p[0]<c[1][0] and c[0][1]<coord_p[1] and coord_p[1]<c[1][1]:
                        return (p,k)
    else:
        for p in pieces_noires:
            if p=='pion':
                for k in range (len(pieces_noires[p])):
                    c=coordonnées_cases[tab120[pieces_noires[p][k][0]]]
                    if c[0][0]<coord_p[0] and coord_p[0]<c[1][0] and c[0][1]<coord_p[1] and coord_p[1]<c[1][1]:
                        return (p,k)
            else:
                for k in range (len(pieces_noires[p])):
                    c=coordonnées_cases[tab120[pieces_noires[p][k]]]
                    if c[0][0]<coord_p[0] and coord_p[0]<c[1][0] and c[0][1]<coord_p[1] and coord_p[1]<c[1][1]:
                        return (p,k)

    return None

def affiche_coups_possibles(coups):
    for i in range (len(coups)):
        coord=coordonnées_cases[tab120[coups[i]]]
        screen.blit(rond, coord[0])

def case(joueur):
    #renvoie la liste des cases sur lesquels sont les pieces du joueur
    L=[]
    if joueur==True:
        for p in pieces_blanches:
            if p=='pion':
                for i in range (len(pieces_blanches[p])):
                    L.append(pieces_blanches[p][i][0])
            else:
                for i in range (len(pieces_blanches[p])):
                    L.append(pieces_blanches[p][i])

    if joueur==False:
        for p in pieces_noires:
            if p=='pion':
                for i in range (len(pieces_noires[p])):
                    L.append(pieces_noires[p][i][0])
            else:
                for i in range (len(pieces_noires[p])):
                    L.append(pieces_noires[p][i])

    return L

def est_en_echec (joueur):

    case_blanche=case(True)
    case_noire=case(False)

    if joueur==True:
        case_roi=pieces_blanches['roi'][0]

        for piece in pieces_noires:
            if piece=='tour':
                for t in pieces_noires[piece]:
                    if t not in case_blanche:
                        for deplacement in deplacements_tour:
                            k=1
                            while t+k*deplacement in tab64:
                                if t+k*deplacement==case_roi:
                                    return True
                                elif t+k*deplacement in case_blanche or t+k*deplacement in case_noire :
                                    break
                                k+=1

            if piece=='fou':
                for t in pieces_noires[piece]:
                    if t not in case_blanche:
                        for deplacement in deplacements_fou:
                            k=t+deplacement
                            while k in tab64 and k not in case_noire:
                                if k==case_roi:
                                    return True
                                elif k in case_blanche:
                                    break
                                k=deplacement+k

            if piece=='cavalier':
                for t in pieces_noires[piece]:
                    if t not in case_blanche:
                        for deplacement in deplacements_cavalier:
                            if t+deplacement==case_roi:
                                return True

            if piece=='reine':
                for t in pieces_noires[piece]:
                    if t not in case_blanche:
                        for deplacement in deplacements_tour:
                            k=1
                            while t+k*deplacement in tab64:
                                if t+k*deplacement==case_roi:
                                    return True
                                elif t+k*deplacement in case_blanche or t+k*deplacement in case_noire:
                                    break
                                k+=1
                        for deplacement in deplacements_fou:
                            k=1
                            while t+k*deplacement in tab64:
                                if t+k*deplacement==case_roi:
                                    return True
                                elif t+k*deplacement in case_blanche or t+k*deplacement in case_noire:
                                    break
                                k+=1

            if piece=='pion':
                for t in pieces_noires[piece]:
                    if t not in case_blanche:
                        if t[0]+9==case_roi:
                            return True
                        elif t[0]+11==case_roi:
                            return True

            if piece=='roi':
                for t in pieces_noires[piece]:
                    if t not in case_blanche:
                        for deplacement in deplacements_fou:
                            if t+deplacement==case_roi:
                                return True
                        for deplacement in deplacements_tour:
                            if t+deplacement==case_roi:
                                return True

        return False

    else:
        case_roi=pieces_noires['roi'][0]


        for piece in pieces_blanches:
            if piece=='tour':
                for t in pieces_blanches[piece]:
                    if t not in case_noire:
                        for deplacement in deplacements_tour:
                            k=1
                            while t+k*deplacement in tab64:
                                if t+k*deplacement==case_roi:
                                    return True
                                if t+k*deplacement in case_blanche or t+k*deplacement in case_noire:
                                    break
                                k+=1

            if piece=='fou':
                for t in pieces_blanches[piece]:
                    if t not in case_noire:
                        for deplacement in deplacements_fou:
                            k=1
                            while t+k*deplacement in tab64 and t+k*deplacement not in case_blanche:
                                if t+k*deplacement==case_roi:
                                    return True
                                if t+k*deplacement in case_noire:
                                    break
                                k=k+1


            if piece=='cavalier':
                for t in pieces_blanches[piece]:
                    if t not in case_noire:
                        for deplacement in deplacements_cavalier:
                            if t+deplacement==case_roi:
                                return True

            if piece=='reine':
                for t in pieces_blanches[piece]:
                    if t not in case_noire:
                        for deplacement in deplacements_tour:
                            k=1
                            while t+k*deplacement in tab64:
                                if t+k*deplacement==case_roi:
                                    return True
                                if t+k*deplacement in case_blanche or t+k*deplacement in case_noire:
                                    break
                                k+=1
                        for deplacement in deplacements_fou:
                            k=1
                            while t+k*deplacement in tab64:
                                if t+k*deplacement==case_roi:
                                    return True
                                if t+k*deplacement in case_blanche or t+k*deplacement in case_noire:
                                    break
                                k+=1

            if piece=='pion':
                for t in pieces_blanches[piece]:
                    if t not in case_noire:
                        if t[0]-9==case_roi:
                            return True
                        if t[0]-11==case_roi:
                            return True

            if piece=='roi':
                for t in pieces_blanches[piece]:
                    if t not in case_noire:
                        for deplacement in deplacements_fou:
                            if t+deplacement==case_roi:
                                return True
                        for deplacement in deplacements_tour:
                            if t+deplacement==case_roi:
                                return True

        return False

def coups_possible(piece,tour):
    coups=[]
    case_blanche=case(True)
    case_noire=case(False)
    global pieces_blanches,pieces_noires

    if tour==True:

        if piece[0]=='pion':
            position=pieces_blanches[piece[0]][piece[1]][0]
        else:
            position=pieces_blanches[piece[0]][piece[1]]

        if piece[0]=='tour':
            for deplacement in deplacements_tour:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_blanche:
                        break
                    elif position+k*deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for j in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_noires[pi][j][1]
                                    del pieces_noires[pi][j]
                                    break
                                elif pieces_noires[pi][j]==position+k*deplacement:
                                    del pieces_noires[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                    k+=1

        if piece[0]=='fou':
            for deplacement in deplacements_fou:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_blanche:
                        break
                    elif position+k*deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for j in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_noires[pi][j][1]
                                    del pieces_noires[pi][j]
                                    break
                                elif pieces_noires[pi][j]==position+k*deplacement:
                                    del pieces_noires[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                    k+=1

        if piece[0]=='reine':
            for deplacement in deplacements_tour:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_blanche:
                        break
                    elif position+k*deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for j in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_noires[pi][j][1]
                                    del pieces_noires[pi][j]
                                    break
                                elif pieces_noires[pi][j]==position+k*deplacement:
                                    del pieces_noires[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                    k+=1
            for deplacement in deplacements_fou:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_blanche:
                        break
                    elif position+k*deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for j in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_noires[pi][j][1]
                                    del pieces_noires[pi][j]
                                    break
                                elif pieces_noires[pi][j]==position+k*deplacement:
                                    del pieces_noires[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(True):
                            coups.append(position+k*deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                    k+=1

        if piece[0]=='cavalier':
            for deplacement in deplacements_cavalier:
                if position+deplacement not in case_blanche and  position+deplacement in tab64:
                    if position+deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for k in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][k][0]==position+deplacement:
                                    p,i,status=pi,k,pieces_noires[pi][k][1]
                                    del pieces_noires[pi][k]
                                    break
                                elif pieces_noires[pi][k]==position+deplacement:
                                    del pieces_noires[pi][k]
                                    p,i=pi,k
                                    break
                        if not est_en_echec(True):
                            coups.append(position+deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+deplacement)
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+deplacement
                        if not est_en_echec(True):
                            coups.append(position+deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position

        if piece[0]=='roi':
            for deplacement in deplacements_fou:
                if position+deplacement not in case_blanche and  position+deplacement in tab64:
                    if position+deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for k in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][k][0]==position+deplacement:
                                    p,i,status=pi,k,pieces_noires[pi][k][1]
                                    del pieces_noires[pi][k]
                                    break
                                elif pieces_noires[pi][k]==position+deplacement:
                                    del pieces_noires[pi][k]
                                    p,i=pi,k
                                    break
                        if not est_en_echec(True):
                            coups.append(position+deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+deplacement)
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+deplacement
                        if not est_en_echec(True):
                            coups.append(position+deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position

            for deplacement in deplacements_tour:
                if position+deplacement not in case_blanche and  position+deplacement in tab64:
                    if position+deplacement in case_noire:
                        pieces_blanches[piece[0]][piece[1]]=position+deplacement
                        p=None
                        i=0
                        for pi in pieces_noires:
                            for k in range (len(pieces_noires[pi])):
                                if pi=='pion' and pieces_noires[pi][k][0]==position+deplacement:
                                    p,i,status=pi,k,pieces_noires[pi][k][1]
                                    del pieces_noires[pi][k]
                                    break
                                elif pieces_noires[pi][k]==position+deplacement:
                                    del pieces_noires[pi][k]
                                    p,i=pi,k
                                    break
                        if not est_en_echec(True):
                            coups.append(position+deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_noires[p].insert(i,[position+deplacement,status])
                            else:
                                pieces_noires[p].insert(i,position+deplacement)
                    else:
                        pieces_blanches[piece[0]][piece[1]]=position+deplacement
                        if not est_en_echec(True):
                            coups.append(position+deplacement)
                        pieces_blanches[piece[0]][piece[1]]=position
            if petit_roque_blanc and position-1 not in case_blanche and position-1 not in case_noire and not est_en_echec(True):
                pieces_blanches[piece[0]][piece[1]]=position-1
                if position-2 not in case_blanche and position-2 not in case_noire and not est_en_echec(True):
                    pieces_blanches[piece[0]][piece[1]]=position-2
                    if not est_en_echec(True):
                        coups.append(position-2)
                pieces_blanches[piece[0]][piece[1]]=position
            if grand_roque_blanc and position+1 not in case_blanche and position+1 not in case_noire and not est_en_echec(True):
                pieces_blanches[piece[0]][piece[1]]=position+1
                if position+2 not in case_blanche and position+2 not in case_noire and not est_en_echec(True):
                    pieces_blanches[piece[0]][piece[1]]=position+2
                    if not est_en_echec(True):
                        coups.append(position+2)
                pieces_blanches[piece[0]][piece[1]]=position

        if piece[0]=='pion':
            if position-9 in case_noire:
                pieces_blanches[piece[0]][piece[1]][0]=position-9
                if not est_en_echec(True):
                    coups.append(position-9)
                pieces_blanches[piece[0]][piece[1]][0]=position
            if position-11 in case_noire :
                pieces_blanches[piece[0]][piece[1]][0]=position-11
                if not est_en_echec(True):
                    coups.append(position-11)
                pieces_blanches[piece[0]][piece[1]][0]=position
            if position//10==8 and position-20 not in case_blanche and position-20 not in case_noire:
                pieces_blanches[piece[0]][piece[1]][0]=position-20
                if not est_en_echec(True):
                    coups.append(position-20)
                pieces_blanches[piece[0]][piece[1]][0]=position
            if position-10 not in case_blanche and position-10 not in case_noire:
                pieces_blanches[piece[0]][piece[1]][0]=position-10
                if not est_en_echec(True):
                    coups.append(position-10)
                pieces_blanches[piece[0]][piece[1]][0]=position
            if position//10==5:
                for pions in pieces_noires['pion']:
                    if pions[0]//10==5 and pions[1]==True:
                        pieces_blanches[piece[0]][piece[1]][0]=pions[0]
                        if not est_en_echec(True):
                            coups.append(pions[0]-10)
                        pieces_blanches[piece[0]][piece[1]][0]=position

    if tour==False:

        if piece[0]=='pion':
            position=pieces_noires[piece[0]][piece[1]][0]
        else:
            position=pieces_noires[piece[0]][piece[1]]

        if piece[0]=='tour':
            for deplacement in deplacements_tour:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_noire:
                        break
                    elif position+k*deplacement in case_blanche :
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for j in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_blanches[pi][j][1]
                                    del pieces_blanches[pi][j]
                                    break
                                elif pieces_blanches[pi][j]==position+k*deplacement:
                                    del pieces_blanches[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                    k+=1

        if piece[0]=='fou':
            for deplacement in deplacements_fou:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_noire:
                        break
                    elif position+k*deplacement in case_blanche :
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for j in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_blanches[pi][j][1]
                                    del pieces_blanches[pi][j]
                                    break
                                elif pieces_blanches[pi][j]==position+k*deplacement:
                                    del pieces_blanches[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                    k+=1

        if piece[0]=='reine':
            for deplacement in deplacements_tour:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_noire:
                        break
                    elif position+k*deplacement in case_blanche :
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for j in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_blanches[pi][j][1]
                                    del pieces_blanches[pi][j]
                                    break
                                elif pieces_blanches[pi][j]==position+k*deplacement:
                                    del pieces_blanches[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                    k+=1
            for deplacement in deplacements_fou:
                k=1
                while position+k*deplacement in tab64:
                    if position+k*deplacement in case_noire:
                        break
                    elif position+k*deplacement in case_blanche :
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for j in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][j][0]==position+k*deplacement:
                                    p,i,status=pi,j,pieces_blanches[pi][j][1]
                                    del pieces_blanches[pi][j]
                                    break
                                elif pieces_blanches[pi][j]==position+k*deplacement:
                                    del pieces_blanches[pi][j]
                                    p,i=pi,j
                                    break
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+k*deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+k*deplacement)
                        break
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+k*deplacement
                        if not est_en_echec(False):
                            coups.append(position+k*deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                    k+=1

        if piece[0]=='cavalier':
            for deplacement in deplacements_cavalier:
                if position+deplacement not in case_noire and position+deplacement in tab64:
                    if position+deplacement in case_blanche:
                        pieces_noires[piece[0]][piece[1]]=position+deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for k in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][k][0]==position+deplacement:
                                    p,i,status=pi,k,pieces_blanches[pi][k][1]
                                    del pieces_blanches[pi][k]
                                    break
                                elif pieces_blanches[pi][k]==position+deplacement:
                                    del pieces_blanches[pi][k]
                                    p,i=pi,k
                                    break
                        if not est_en_echec(False):
                            coups.append(position+deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+deplacement)
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+deplacement
                        if not est_en_echec(False):
                            coups.append(position+deplacement)
                        pieces_noires[piece[0]][piece[1]]=position

        if piece[0]=='roi':
            for deplacement in deplacements_fou:
                if position+deplacement not in case_noire and position+deplacement in tab64:
                    if position+deplacement in case_blanche:
                        pieces_noires[piece[0]][piece[1]]=position+deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for k in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][k][0]==position+deplacement:
                                    p,i,status=pi,k,pieces_blanches[pi][k][1]
                                    del pieces_blanches[pi][k]
                                    break
                                elif pieces_blanches[pi][k]==position+deplacement:
                                    del pieces_blanches[pi][k]
                                    p,i=pi,k
                                    break
                        if not est_en_echec(False):
                            coups.append(position+deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+deplacement)
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+deplacement
                        if not est_en_echec(False):
                            coups.append(position+deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
            for deplacement in deplacements_tour:
                if position+deplacement not in case_noire and  position+deplacement in tab64:
                    if position+deplacement in case_blanche:
                        pieces_noires[piece[0]][piece[1]]=position+deplacement
                        p=None
                        i=0
                        for pi in pieces_blanches:
                            for k in range (len(pieces_blanches[pi])):
                                if pi=='pion' and pieces_blanches[pi][k][0]==position+deplacement:
                                    p,i,status=pi,k,pieces_blanches[pi][k][1]
                                    del pieces_blanches[pi][k]
                                    break
                                elif pieces_blanches[pi][k]==position+deplacement:
                                    del pieces_blanches[pi][k]
                                    p,i=pi,k
                                    break
                        if not est_en_echec(False):
                            coups.append(position+deplacement)
                        pieces_noires[piece[0]][piece[1]]=position
                        if p!=None:
                            if p=='pion':
                                pieces_blanches[p].insert(i,[position+deplacement,status])
                            else:
                                pieces_blanches[p].insert(i,position+deplacement)
                    else:
                        pieces_noires[piece[0]][piece[1]]=position+deplacement
                        if not est_en_echec(False):
                            coups.append(position+deplacement)
                        pieces_noires[piece[0]][piece[1]]=position

            if petit_roque_noir==True and position-1 not in case_noire and position-1 not in case_blanche and not est_en_echec(False):
                pieces_noires[piece[0]][piece[1]]=position-1
                if position-2 not in case_noire and position-2 not in case_blanche and not est_en_echec(False):
                    pieces_noires[piece[0]][piece[1]]=position-2
                    if not est_en_echec(False):
                        coups.append(position-2)
                pieces_noires[piece[0]][piece[1]]=position
            if grand_roque_noir==True and position+1 not in case_noire and position+1 not in case_blanche and not est_en_echec(False):
                pieces_noires[piece[0]][piece[1]]=position+1
                if position+2 not in case_noire and position+2 not in case_blanche and not est_en_echec(False):
                    pieces_noires[piece[0]][piece[1]]=position+2
                    if not est_en_echec(False):
                        coups.append(position+2)
                pieces_noires[piece[0]][piece[1]]=position

        if piece[0]=='pion':
            if position+9 in case_blanche:
                pieces_noires[piece[0]][piece[1]][0]=position+9
                if not est_en_echec(False):
                    coups.append(position+9)
                pieces_noires[piece[0]][piece[1]][0]=position
            if position+11 in case_blanche :
                pieces_noires[piece[0]][piece[1]][0]=position+11
                if not est_en_echec(False):
                    coups.append(position+11)
                pieces_noires[piece[0]][piece[1]][0]=position
            if position//10==3 and position+20 not in case_blanche and position+20 not in case_noire:
                pieces_noires[piece[0]][piece[1]][0]=position+20
                if not est_en_echec(False):
                    coups.append(position+20)
                pieces_noires[piece[0]][piece[1]][0]=position
            if position+10 not in case_blanche and position+10 not in case_noire:
                pieces_noires[piece[0]][piece[1]][0]=position+10
                if not est_en_echec(False):
                    coups.append(position+10)
                pieces_noires[piece[0]][piece[1]][0]=position
            if position//10==6:
                for pions in pieces_blanches['pion']:
                    if pions[0]//10==6 and pions[1]==True:
                        pieces_noires[piece[0]][piece[1]][0]=pions[0]
                        if not est_en_echec(False):
                            coups.append(pions[0]+10)
                        pieces_noires[piece[0]][piece[1]][0]=position

    return coups

def coup_joue(coord,coups_jouables):
    for k in range(len(coups_jouables)):
        coord_coup=coordonnées_cases[tab120[coups_jouables[k]]]
        if coord[0]>coord_coup[0][0] and coord[0]<coord_coup[1][0] and coord[1]>coord_coup[0][1] and coord[1]<coord_coup[1][1]:
            return coups_jouables[k]
    return None

def joue_piece(coord,coups_jouables,piece_jouee,tour):
    global piece_en_cours
    global pieces_blanches
    global pieces_noires
    global petit_roque_blanc,petit_roque_noir,grand_roque_blanc,grand_roque_noir
    coup=coup_joue(coord,coups_jouables)
    if coup==None:
        piece_en_cours=None
        return -1,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
    else:
        if tour==True:
            for i in range (len(pieces_blanches['pion'])):
                pieces_blanches['pion'][i][1]=False

            if piece_jouee[0]=='pion':
                if pieces_blanches[piece_jouee[0]][piece_jouee[1]][0]-20==coup:
                    pieces_blanches[piece_jouee[0]][piece_jouee[1]][1]=True

                pieces_blanches[piece_jouee[0]][piece_jouee[1]][0]=coup
                for p in pieces_noires:
                    for i in range (len(pieces_noires[p])):
                        if p=='pion':
                            if pieces_noires[p][i][0]==coup:
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                            elif coup//10==4 and pieces_noires[p][i][1]==True and pieces_noires[p][i][0]==coup+10:#prise en passant
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        elif p=='tour' and pieces_noires[p][i]==coup:
                            if i==0 and petit_roque_noir:
                                petit_roque_noir=False
                            if i==0 and not petit_roque_noir and grand_roque_noir:
                                grand_roque_noir=False
                            if i==1 and grand_roque_noir:
                                grand_roque_noir=False
                            del pieces_noires[p][i]
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        else:
                            if pieces_noires[p][i]==coup:
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

            if piece_jouee[0]=='roi':
                grand_roque_blanc=False
                petit_roque_blanc=False

                if pieces_blanches[piece_jouee[0]][piece_jouee[1]]+2==coup:#petit roque
                    pieces_blanches[piece_jouee[0]][piece_jouee[1]]=coup
                    for t in range (len(pieces_blanches['tour'])):
                        if pieces_blanches['tour'][t]==98:
                            pieces_blanches['tour'][t]=coup-1
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                elif pieces_blanches[piece_jouee[0]][piece_jouee[1]]-2==coup:#grand roque
                    pieces_blanches[piece_jouee[0]][piece_jouee[1]]=coup
                    for t in range (len(pieces_blanches['tour'])):
                        if pieces_blanches['tour'][t]==91:
                            pieces_blanches['tour'][t]=coup+1
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                else:
                    pieces_blanches[piece_jouee[0]][piece_jouee[1]]=coup
                    for p in pieces_noires:
                        for i in range (len(pieces_noires[p])):
                            if p=='pion':
                                if pieces_noires[p][i][0]==coup:
                                    del pieces_noires[p][i]
                                    piece_en_cours=None
                                    return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                            elif p=='tour' and pieces_noires[p][i]==coup:
                                if i==0 and petit_roque_noir:
                                    petit_roque_noir=False
                                if i==0 and not petit_roque_noir and grand_roque_noir:
                                    grand_roque_noir=False
                                if i==1 and grand_roque_noir:
                                    grand_roque_noir=False
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                            else:
                                if pieces_noires[p][i]==coup:
                                    del pieces_noires[p][i]
                                    piece_en_cours=None
                                    return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

            if piece_jouee[0]=='tour':
                #deroque pour les mouvement des tours
                if piece_jouee[1]==0 and petit_roque_blanc:
                    petit_roque_blanc=False
                if piece_jouee[1]==0 and not petit_roque_blanc and grand_roque_blanc:
                    grand_roque_blanc=False
                if piece_jouee[1]==1 and grand_roque_blanc:
                    grand_roque_blanc=False

                #action de la tour
                pieces_blanches[piece_jouee[0]][piece_jouee[1]]=coup
                for p in pieces_noires:
                    for i in range (len(pieces_noires[p])):
                        if p=='pion':
                            if pieces_noires[p][i][0]==coup:
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        elif p=='tour' and pieces_noires[p][i]==coup:
                            if i==0 and petit_roque_noir:
                                petit_roque_noir=False
                            if i==0 and not petit_roque_noir and grand_roque_noir:
                                grand_roque_noir=False
                            if i==1 and grand_roque_noir:
                                grand_roque_noir=False
                            del pieces_noires[p][i]
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        else:
                            if pieces_noires[p][i]==coup:
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

            else:
                pieces_blanches[piece_jouee[0]][piece_jouee[1]]=coup
                for p in pieces_noires:
                    for i in range (len(pieces_noires[p])):
                        if p=='pion':
                            if pieces_noires[p][i][0]==coup:
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        elif p=='tour' and pieces_noires[p][i]==coup:
                            if i==0 and petit_roque_noir:
                                petit_roque_noir=False
                            if i==0 and not petit_roque_noir and grand_roque_noir:
                                grand_roque_noir=False
                            if i==1 and grand_roque_noir:
                                grand_roque_noir=False
                            del pieces_noires[p][i]
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        else:
                            if pieces_noires[p][i]==coup:
                                del pieces_noires[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

        else:
            for i in range (len(pieces_noires['pion'])):
                pieces_noires['pion'][i][1]=False

            if piece_jouee[0]=='pion':
                if pieces_noires[piece_jouee[0]][piece_jouee[1]][0]+20==coup:
                    pieces_noires[piece_jouee[0]][piece_jouee[1]][1]=True
                pieces_noires[piece_jouee[0]][piece_jouee[1]][0]=coup
                for p in pieces_blanches:
                    for i in range (len(pieces_blanches[p])):
                        if p=='pion':
                            if pieces_blanches[p][i][0]==coup:
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                            elif coup//10==7 and pieces_blanches[p][i][1]==True and pieces_blanches[p][i][0]==coup-10:#prise en passant
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        elif p=='tour' and pieces_blanches[p][i]==coup:
                            if i==0 and petit_roque_blanc:
                                petit_roque_blanc=False
                            if i==0 and not petit_roque_blanc and grand_roque_blanc:
                                grand_roque_blanc=False
                            if i==1 and grand_roque_blanc:
                                grand_roque_blanc=False
                            del pieces_blanches[p][i]
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        else:
                            if pieces_blanches[p][i]==coup:
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

            if piece_jouee[0]=='roi':
                grand_roque_noir=False
                petit_roque_noir=False

                if pieces_noires[piece_jouee[0]][piece_jouee[1]]+2==coup:#petit roque
                    pieces_noires[piece_jouee[0]][piece_jouee[1]]=coup
                    for t in range (len(pieces_noires['tour'])):
                        if pieces_noires['tour'][t]==28:
                            pieces_noires['tour'][t]=coup-1
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                elif pieces_noires[piece_jouee[0]][piece_jouee[1]]-2==coup:#grand roque
                    pieces_noires[piece_jouee[0]][piece_jouee[1]]=coup
                    for t in range (len(pieces_noires['tour'])):
                        if pieces_noires['tour'][t]==21:
                            pieces_noires['tour'][t]=coup+1
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                else:
                    pieces_noires[piece_jouee[0]][piece_jouee[1]]=coup
                    for p in pieces_blanches:
                        for i in range (len(pieces_blanches[p])):
                            if p=='pion':
                                if pieces_blanches[p][i][0]==coup:
                                    del pieces_blanches[p][i]
                                    piece_en_cours=None
                                    return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                            elif p=='tour' and pieces_blanches[p][i]==coup:
                                if i==0 and petit_roque_blanc:
                                    petit_roque_blanc=False
                                if i==0 and not petit_roque_blanc and grand_roque_blanc:
                                    grand_roque_blanc=False
                                if i==1 and grand_roque_blanc:
                                    grand_roque_blanc=False
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                            else:
                                if pieces_blanches[p][i]==coup:
                                    del pieces_blanches[p][i]
                                    piece_en_cours=None
                                    return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

            if piece_jouee[0]=='tour':
                #deroque pour les mouvement des tours
                if piece_jouee[1]==0 and petit_roque_noir:
                    petit_roque_noir=False
                if piece_jouee[1]==0 and not petit_roque_noir and grand_roque_noir:
                    grand_roque_noir=False
                if piece_jouee[1]==1 and grand_roque_noir:
                    grand_roque_noir=False

                #action de la tour
                pieces_noires[piece_jouee[0]][piece_jouee[1]]=coup
                for p in pieces_blanches:
                    for i in range (len(pieces_blanches[p])):
                        if p=='pion':
                            if pieces_blanches[p][i][0]==coup:
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        elif p=='tour' and pieces_blanches[p][i]==coup:
                            if i==0 and petit_roque_blanc:
                                petit_roque_blanc=False
                            if i==0 and not petit_roque_blanc and grand_roque_blanc:
                                grand_roque_blanc=False
                            if i==1 and grand_roque_blanc:
                                grand_roque_blanc=False
                            del pieces_blanches[p][i]
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        else:
                            if pieces_blanches[p][i]==coup:
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

            else:
                pieces_noires[piece_jouee[0]][piece_jouee[1]]=coup
                for p in pieces_blanches:
                    for i in range (len(pieces_blanches[p])):
                        if p=='pion':
                            if pieces_blanches[p][i][0]==coup:
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        elif p=='tour' and pieces_blanches[p][i]==coup:
                            if i==0 and petit_roque_blanc:
                                petit_roque_blanc=False
                            if i==0 and not petit_roque_blanc and grand_roque_blanc:
                                grand_roque_blanc=False
                            if i==1 and grand_roque_blanc:
                                grand_roque_blanc=False
                            del pieces_blanches[p][i]
                            piece_en_cours=None
                            return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours
                        else:
                            if pieces_blanches[p][i]==coup:
                                del pieces_blanches[p][i]
                                piece_en_cours=None
                                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours

                piece_en_cours=None
                return None,pieces_blanches,pieces_noires,petit_roque_blanc,grand_roque_blanc,petit_roque_noir,grand_roque_noir,piece_en_cours


def mat(tour):
    if tour==True:
        for p in pieces_blanches:
            for k in range (len(pieces_blanches[p])):
                if coups_possible((p,k),tour)!=[]:
                    return False
    else:
        for p in pieces_noires:
            for k in range (len(pieces_noires[p])):
                if coups_possible((p,k),tour)!=[]:
                    return False
    return True






