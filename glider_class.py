import copy


class Glider:
    def __init__(self, position, vitesse, nb_phases, phase, period, symbol):
        self.position = position
        self.vitesse = vitesse
        self.nb_phases = nb_phases
        self.phase = phase
        self.period = period
        self.symbol = symbol


class Ossifier(Glider):
    def __init__(self, position, period):
        super().__init__(
            position=position,
            nb_phases=0,
            phase=0,
            period=period,
            symbol="O",
        )


class Leader(Glider):
    def __init__(self, position, period):
        super().__init__(
            position=position,
            nb_phases=0,
            phase=0,
            period=period,
            symbol="O",
        )


class Rejecteur(Glider):
    def __init__(self, position, vitesse, period):
        super().__init__(position, vitesse, period, "r")


class Accepteur(Glider):
    def __init__(self, position, vitesse, period):
        super().__init__(position, vitesse, period, "a")


class Y_mobile(Glider):
    def __init__(self, position, vitesse, period):
        super().__init__(position, vitesse, period, "y")


class N_mobile(Glider):
    def __init__(self, position, vitesse, period):
        super().__init__(position, vitesse, period, "n")


class Data_y(Glider):
    def __init__(self, position):
        super().__init__(position, 0, 1, "Y")


class Data_N(Glider):
    def __init__(self, position):
        super().__init__(position, 0, 1, "N")


class Ether:
    def __init__(self, taille, fenetre, glider_list, rules, periodic_list):
        self.grid = [None] * taille
        for glider in glider_list:
            self.add_glider(glider)
        self.rules = rules
        self.time = 0
        self.fenetre = fenetre
        self.periodic_list = periodic_list
        for x in self.periodic_list:
            self.add_glider(x)

    def affichage(self):
        line_list = self.grid[self.fenetre[0] : self.fenetre[1]]
        line = ""
        for x in line_list:
            if isinstance(x, Glider):
                line += x.symbol
            elif x is not None:
                line += str(x)
            else:
                line += " "

        print(line)

    def update_ether(self):
        self.time += 1
        new_grid = []

        for i in range(len(self.grid)):
            new_grid.append(self.rules(i, self.grid))
        self.grid = new_grid
        for x in self.grid:
            if isinstance(x, Glider):
                if x.phase < x.nb_phases:
                    x.phase += 1
                else:
                    x.phase = 0
        for x in self.periodic_list:
            if self.time % x.period == 0:
                self.add_glider(x)

    def add_glider(self, glider):
        g = copy.deepcopy(glider)
        self.grid[g.position] = g
