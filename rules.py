import copy
from glider_class import Glider


def obo(b):
    if b.vitesse != 0:
        if b.phase < b.nb_phases:
            return copy.deepcopy(b)
        else:
            return None
    else:
        return copy.deepcopy(b)


###Cette fonction correspond à la règle de transition qui permet de simuler le SG idéal###
def ideal_rules(i, grille):
    if i == 0:
        a = None
        b = grille[i]
        c = grille[i + 1]
    elif i == len(grille) - 1:
        a = grille[i - 1]
        b = grille[i]
        c = None
    else:
        a = grille[i - 1]
        b = grille[i]
        c = grille[i + 1]
    if (a, b, c) == (None, None, None):  # Règle vide
        return None
    elif (a, b, c) == (None, b, None):  # Règle obo
        if isinstance(b, Glider):
            return obo(b)
        elif b == 1 or b == 6 or b == 7:
            return Glider(i, 0, 0, 0, 0, "Y")
        elif b == 2 or b == 9 or b == 10:
            return Glider(i, 0, 0, 0, 0, "N")
        elif b == 3 or b == 4 or b == 5:
            return None

    elif (a, b, c) == (None, None, c):  # Règle ooc
        if isinstance(c, Glider):
            if c.vitesse < 0 and c.phase == c.nb_phases:
                return copy.deepcopy(c)
            else:
                return None
        elif c == 3 or c == 6 or c == 9:
            return Glider(i, -1, 0, 0, 0, "y")
        elif c == 4 or c == 7 or c == 10:
            return Glider(i, -1, 0, 0, 0, "n")
        elif c == 5:
            return None
    elif (a, b, c) == (a, None, None):  # Règle aoo
        if isinstance(a, Glider):
            if a.vitesse > 0 and a.phase == a.nb_phases:
                return copy.deepcopy(a)
            else:
                return copy.deepcopy(b)
        elif a == 3 or a == 4 or a == 5:
            return Glider(i, 1, 0, 0, 0, "A")
        elif a == 6 or a == 7 or a == 9 or a == 10:
            return None
        elif a == 8:
            return Glider(i, 1, 0, 0, 0, "R")
    elif (a, b, c) == (a, None, c):  # Règle aoc
        if isinstance(a, Glider) and isinstance(c, Glider):
            if a.vitesse > 0 and c.vitesse < 0:
                if a.phase == a.nb_phases and c.phase == c.nb_phases:
                    if a.symbol == "O":
                        if c.symbol == "y":
                            return 1
                        elif c.symbol == "n":
                            return 2
                    elif a.symbol == "A":
                        if c.symbol == "y":
                            return 3
                        elif c.symbol == "n":
                            return 4
                        elif c.symbol == "L":
                            return copy.deepcopy(c)
                    elif a.symbol == "R":
                        if c.symbol == "L":
                            return copy.deepcopy(c)
                        else:
                            return copy.deepcopy(a)
                elif a.phase == a.nb_phases:
                    return copy.deepcopy(a)
                elif c.phase == c.nb_phases:
                    return copy.deepcopy(c)
            elif c.vitesse < 0:
                if c.phase == c.nb_phases:
                    return copy.deepcopy(c)
    elif (a, b, c) == (a, b, None):  # Règle abo
        if isinstance(a, Glider):
            if a.vitesse <= 0:
                if isinstance(b, Glider):
                    return obo(b)
            else:
                if a.phase == a.nb_phases and b.phase != b.nb_phases:
                    if a.symbol == "O":
                        if b.symbol == "y":
                            return 1
                        elif b.symbol == "n":
                            return 2
                    elif a.symbol == "A":
                        if b.symbol == "y":
                            return 3
                        elif b.symbol == "n":
                            return 4
                        elif b.symbol == "L":
                            return copy.deepcopy(b)
                    elif a.symbol == "R":
                        if b.symbol == "L":
                            return copy.deepcopy(b)
                        else:
                            return copy.deepcopy(a)
                else:
                    return obo(b)
    elif (a, b, c) == (None, b, c):  # Règle obc
        if isinstance(c, Glider):
            if c.vitesse >= 0:
                if isinstance(b, Glider):
                    return obo(b)
            else:
                if c.phase == c.nb_phases:
                    if b.symbol == "O":
                        if c.symbol == "y":
                            return 1
                        elif c.symbol == "n":
                            return 2
                    elif b.symbol == "A":
                        if c.symbol == "y":
                            return 3
                        elif c.symbol == "n":
                            return 4
                        elif c.symbol == "L":
                            return copy.deepcopy(c)
                    elif b.symbol == "R":
                        if c.symbol == "L":
                            return copy.deepcopy(c)
                        else:
                            return copy.deepcopy(b)
                    elif b.symbol == "Y":
                        if c.symbol == "L":
                            return 5
                        elif c.symbol == "y":
                            return 6
                        elif c.symbol == "n":
                            return 7
                    elif b.symbol == "N":
                        if c.symbol == "L":
                            return 8
                        elif c.symbol == "y":
                            return 9
                        elif c.symbol == "n":
                            return 10
                else:
                    return obo(b)


##Cette fonction, qui n'est pas encore terminée, correspond à la règle de transition qui permet de simuler les glider de l'ECA 54##

#w W c g G#
def rule54(i, grille):
    if i == 0:
        a = None
        b = grille[i]
        c = grille[i + 1]
    elif i == len(grille) - 1:
        a = grille[i - 1]
        b = grille[i]
        c = None
    else:
        a = grille[i - 1]
        b = grille[i]
        c = grille[i + 1]
    if (a, b, c) == (None, None, None):  # Règle vide
        return None
    elif (a, b, c) == (None, b, None):  # Règle obo
        if isinstance(b, Glider):
            return obo(b)
        

    elif (a, b, c) == (None, None, c):  # Règle ooc
        if isinstance(c, Glider):
            if c.vitesse < 0 and c.phase == c.nb_phases:
                return copy.deepcopy(c)
            elif c.symbol==c and c.phase == or c.phase == or c.phase == :
                return Glider(i, -1, 0, 0, 0, "w")
            else:
                return None

    elif (a, b, c) == (a, None, None):  # Règle aoo
        if isinstance(a, Glider):
            if a.vitesse > 0 and a.phase == a.nb_phases:
                return copy.deepcopy(a)
            else:
                return None#############################################################################################################################
        elif a == 3 or a == 4 or a == 5:
            return Glider(i, 1, 0, 0, 0, "A")
        elif a == 6 or a == 7 or a == 9 or a == 10:
            return None
        elif a == 8:
            return Glider(i, 1, 0, 0, 0, "R")
    elif (a, b, c) == (a, None, c):  # Règle aoc
        if isinstance(a, Glider) and isinstance(c, Glider):
            if a.vitesse > 0 and c.vitesse < 0:
                if a.phase == a.nb_phases and c.phase == c.nb_phases:
                    if a.symbol == "O":
                        if c.symbol == "y":
                            return 1
                        elif c.symbol == "n":
                            return 2
                    elif a.symbol == "A":
                        if c.symbol == "y":
                            return 3
                        elif c.symbol == "n":
                            return 4
                        elif c.symbol == "L":
                            return copy.deepcopy(c)
                    elif a.symbol == "R":
                        if c.symbol == "L":
                            return copy.deepcopy(c)
                        else:
                            return copy.deepcopy(a)
                elif a.phase == a.nb_phases:
                    return copy.deepcopy(a)
                elif c.phase == c.nb_phases:
                    return copy.deepcopy(c)
            elif c.vitesse < 0:
                if c.phase == c.nb_phases:
                    return copy.deepcopy(c)
    elif (a, b, c) == (a, b, None):  # Règle abo
        if isinstance(a, Glider):
            if a.vitesse <= 0:
                if isinstance(b, Glider):
                    return obo(b)
            else:
                if a.phase == a.nb_phases and b.phase != b.nb_phases:
                    if a.symbol == "O":
                        if b.symbol == "y":
                            return 1
                        elif b.symbol == "n":
                            return 2
                    elif a.symbol == "A":
                        if b.symbol == "y":
                            return 3
                        elif b.symbol == "n":
                            return 4
                        elif b.symbol == "L":
                            return copy.deepcopy(b)
                    elif a.symbol == "R":
                        if b.symbol == "L":
                            return copy.deepcopy(b)
                        else:
                            return copy.deepcopy(a)
                else:
                    return obo(b)
    elif (a, b, c) == (None, b, c):  # Règle obc
        if isinstance(c, Glider):
            if c.vitesse >= 0:
                if isinstance(b, Glider):
                    return obo(b)
            else:
                if c.phase == c.nb_phases:
                    if b.symbol == "O":
                        if c.symbol == "y":
                            return 1
                        elif c.symbol == "n":
                            return 2
                    elif b.symbol == "A":
                        if c.symbol == "y":
                            return 3
                        elif c.symbol == "n":
                            return 4
                        elif c.symbol == "L":
                            return copy.deepcopy(c)
                    elif b.symbol == "R":
                        if c.symbol == "L":
                            return copy.deepcopy(c)
                        else:
                            return copy.deepcopy(b)
                    elif b.symbol == "Y":
                        if c.symbol == "L":
                            return 5
                        elif c.symbol == "y":
                            return 6
                        elif c.symbol == "n":
                            return 7
                    elif b.symbol == "N":
                        if c.symbol == "L":
                            return 8
                        elif c.symbol == "y":
                            return 9
                        elif c.symbol == "n":
                            return 10
                else:
                    return obo(b)
