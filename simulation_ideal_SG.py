from glider_class import Ether
from rules import ideal_rules


from glider_class import Glider


A = Glider(100, 0, 3, 0, 1, "A")

B = Glider(110, 1, 3, 0, 1, "B")

O = Glider(120, 1, 2, 0, 1, "O")

y = Glider(134, -1, 0, 0, 10, "y")

a = Glider(140, -1, 1, 0, 0, "L")

L = Glider(152, -1, 3, 0, 0, "n")

Y = Glider(190, 0, 0, 0, 0, "Y")
glider_list = [Y]
for i in range(0, 19):
    glider_list.append(Glider(10 * i, 1, 3, 0, 10, "O"))


p = 25
periodic_list = [
    Glider(0, 1, 3, 0, 40, "O"),
    Glider(205, -1, 0, 0, p, "L"),
    Glider(210, -1, 0, 0, p, "y"),
    Glider(215, -1, 0, 0, p, "y"),
    Glider(220, -1, 0, 0, p, "L"),
    Glider(225, -1, 0, 0, p, "n"),
]

ether = Ether(500, (0, 200), glider_list, ideal_rules, periodic_list)
ether.affichage()

for i in range(500):
    ether.update_ether()
    ether.affichage()
