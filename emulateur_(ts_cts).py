from tag_systems import TagSystem, CyclicTagSystem

ap = {"a": "bb", "b": "ac", "c": "abc"}
m = 2
ts = TagSystem("abc", m, ap)

def encodeur(TS):
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
    return L, str


def emulateur(TS):
    L = encodeur(TS)[0]
    str = encodeur(TS)[1]
    CTS = CyclicTagSystem(str, L)
    return CTS


cts = emulateur(ts)
assert isinstance(cts, CyclicTagSystem)
print(ts.str)
print(cts.str)
for i in range(20):
    cts.actualisation()
    print(cts.str)
for i in range(20):
    ts.actualisation()
    print(ts.str)
