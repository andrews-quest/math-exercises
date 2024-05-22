import schemdraw
from schemdraw import logic

with schemdraw.Drawing() as d:
    d.config(unit=0.5)
    and1 = logic.And(inputs=2)
    and2 = logic.And(inputs=3)
    and3 = logic.And(inputs=3)


