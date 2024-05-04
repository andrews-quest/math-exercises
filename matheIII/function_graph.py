from manim import *

class ExampleFunctionGraph(Scene):
    d = 100
    x = 400
    y_edges = []

    def draw_curved(self, range_val, diff, axes):
        prev_q_y = -100
        for q_x in range(0, range_val, diff):
            q_y = -((self.d**3) / ((q_x**2) + (self.d**2)))

            dot1 = Dot(axes.c2p(q_x, q_y), radius=0.04)
            dot2 = Dot(axes.c2p(-q_x, q_y), radius=0.04)
            line6 = Line(start=axes.c2p(q_x-diff, prev_q_y), end=axes.c2p(q_x, q_y), color=ORANGE)
            line7 = Line(start=axes.c2p(-(q_x-diff), prev_q_y), end=axes.c2p(-q_x, q_y), color=ORANGE)

            line1 = Line(start=ORIGIN, end=axes.c2p(q_x, -self.d), color=WHITE)
            line2 = Line(start=axes.c2p(q_x, 0), end=axes.c2p(q_x, -100), color=YELLOW)
            line3 = axes.plot(lambda x: q_y, color=BLUE)
            line4 = Line(start=ORIGIN, end=axes.c2p(-q_x, -self.d), color=WHITE)
            line5 = Line(start=axes.c2p(-q_x, 0), end=axes.c2p(-q_x, -100), color=YELLOW)
            area = axes.get_area(graph=line3, x_range=(-self.x, self.x), color=BLUE, opacity=0.5)

            prev_q_y = q_y
            self.play(Create(dot1, run_time=0.1))
            self.play(Create(dot2, run_time=0.1))
            self.add(line1)
            self.add(line2)
            self.add(line3)
            self.add(line4)
            self.add(line5)
            self.add(area)
            self.add(line6)
            self.add(line7)
            self.wait(4 / diff)
            self.remove(line1)
            self.remove(line2)
            self.remove(line3)
            self.remove(line4)
            self.remove(line5)
            self.remove(area)
            self.add(line6)
            self.add(line7)

    def construct(self):


        axes = Axes(y_range=(-150, 150, 50),
                    x_range=(-400, 400, 100),
                    y_length=3,
                    x_length=22,
                    ).add_coordinates()

        self.play(Create(axes))

        line1 = Line(start=LEFT*10+DOWN, end=RIGHT*10+DOWN, color=RED)
        line2 = Line(start=LEFT*10, end=RIGHT*10, color=RED)
        self.play(Create(line1))
        self.play(Create(line2))

        circle = Circle(color=GREEN, radius=0.5).shift(DOWN*0.5)
        self.play(Create(circle))

        self.draw_curved(self.x, 10, axes)

        self.wait(5)
