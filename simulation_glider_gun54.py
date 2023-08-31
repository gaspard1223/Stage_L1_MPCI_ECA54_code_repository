from glider_class import Ether
from rules import rule54


from glider_class import Glider


Y = Glider(100, 0, 25, 0, 0, "c")
glider_list = [Y]


p = 25
periodic_list = []

ether = Ether(500, (0, 200), glider_list, rule54, periodic_list)
ether.affichage()

for i in range(500):
    ether.update_ether()
    ether.affichage()
