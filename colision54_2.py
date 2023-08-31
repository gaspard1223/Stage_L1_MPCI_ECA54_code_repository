from glider_class import Ether
from rules import rule54


from glider_class import Glider


W = Glider(94, 1, 0, 0, 0, "W")
w = Glider(105, -1, 0, 0, 0, "w")
glider_list = [W, w]


p = 25
periodic_list = []

ether = Ether(500, (0, 200), glider_list, rule54, periodic_list)
ether.affichage()

for i in range(500):
    ether.update_ether()
    ether.affichage()
