from schemdraw import logic
import schemdraw
from schemdraw.parsing.logic_parser import logicparse

l = logicparse('(not $x_3$ and $x_1$) or ($x_2$ and $x_1$ and $x_0$) or (not $x_3$ and $x_2$ and $x_0$)', outlabel='y')
l.config(unit=2)
l.save('1.png')


with schemdraw.Drawing() as d:
    d.config(unit=0.5)
    S = logic.Xor().label('S', 'right')
    logic.Line().left(d.unit*2).at(S.in1).idot().label('A', 'left')
    B = logic.Line().left().at(S.in2).dot()
    logic.Line().left().label('B', 'left')
    logic.Line().down(d.unit*3).at(S.in1)
    C = logic.And().right().anchor('in1').label('C', 'right')
    logic.Wire('|-').at(B.end).to(C.in2)

d.save('2.png')