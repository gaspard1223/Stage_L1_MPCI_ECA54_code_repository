from test_glider import glider_list, periodic_list
from glider_class import Ether
from rules import ideal_rules


ether = Ether(500, (0, 200), glider_list, ideal_rules, periodic_list)
ether.affichage()

for i in range(500):
    ether.update_ether()
    ether.affichage()
