#Ce fichier contient les fonctions permettant de construire à partir d'un Systême de Tague un Système de Tague cyclique ayant le même comportement.


from tag_systems import TagSystem, CyclicTagSystem

ap = {"a": "bb", "b": "ac", "c": "abc"}
m = 2
ts = TagSystem("abc", m, ap)

def emulateur(TS):
    #cette fonction prend en entrée un Tag System et renvoie L la liste des suffixes du Cyclic tag system correspondant
    encodage = {}
    alphabet = []
    L = []
    for x in TS.ap.keys():
        alphabet.append(x)
    squelette = "0" * (len(alphabet) - 1)
    for i in range(len(alphabet)):
        encodage[alphabet[i]] = squelette[:i] + "1" + squelette[i:]
    for x in TS.ap.values():
        char = ""
        for y in x:
            char += encodage[y]
        L.append(char)
    while len(L) < len(alphabet) * TS.m:
        L.append("")
    str = ""
    for x in TS.str:
        str += encodage[x]
    return CyclicTagSystem(str, L)


#EXEMPLE : le programme suivant entraine la création du Cyclic Tag System simulant le 2-Tague system d'alphabet [a,b,c] de mot initial abc et de fonction de transition : f(a)=bb, f(b)=ac, f(c)=abc
Foncton_de_transition = {"a": "bb", "b": "ac", "c": "abc"}
m = 2
ts = TagSystem("abc", m, ap)
cts = emulateur(ts)
assert isinstance(cts, CyclicTagSystem)
print("Execution du Cyclic tag system")
print(cts.str)
for i in range(20):
    cts.actualisation()
    print(cts.str)
print("Execution du tag system")
print(ts.str)
for i in range(20):
    ts.actualisation()
    print(ts.str)
