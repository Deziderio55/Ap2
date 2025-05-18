import Ap2.grafos as g
import maiordistancia as md

garfos = [g.retornaTeste1(), g.retornaTeste2(), g.retornaTeste3()]

for i in garfos:
    print(md.maior_distancia(i))