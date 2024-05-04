from manim import *

class ExampleFunctionGraph(Scene):
    d = 100
    x = 1000
    y_edges = []

    def construct(self):


        axes = Axes(y_range=(-400, 10, 10), x_range=(-200, 400, 10))
        self.play(Create(axes))

        for q_x in range(0, self.x, 20):
            q_y = -((self.d**3) / ((q_x**2) + (self.d**2)))
            dot = Dot(axes.c2p(q_x, q_y))
            self.play(Create(dot, run_time=0.1))


        self.wait(5)
