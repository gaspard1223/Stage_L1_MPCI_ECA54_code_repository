class TagSystem:
    def __init__(self, str, m, ap):
        self.str = str
        self.m = m
        self.ap = ap

    def actualisation(self):
        if len(self.str) >= self.m:
            self.str = self.str[(self.m) :] + self.ap[self.str[0]]
        else:
            print("Terminé")


class CyclicTagSystem:
    def __init__(self, str, L):
        self.str = str
        self.L = L
        self.i = 0

    def actualisation(self):
        if len(self.str) > 0:
            if self.str[0] == "1":
                self.str = self.str[1:] + self.L[self.i]
            else:
                self.str = self.str[1:]
            self.i = (self.i + 1) % len(self.L)
        else:
            print("Terminé")
