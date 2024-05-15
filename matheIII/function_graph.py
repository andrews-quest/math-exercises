from manim import *

class Graph(Scene):
    d = 100
    x = 400
    y_edges = []
    all_area = d * x * 2
    allowed_area = 0

    def draw_curved(self, axes):
        prev_q_y = -100
        diff = 10
        q_y_text = Text(text="Aktuelles y: ",
                        font_size=18,
                        font="Arial").shift(LEFT * 4.8 + UP * 1.2)
        allowed_area_text = Text(text="Der erlaubte Anteil der Fläche: ",
                                 font_size=18,
                                 font="Arial").shift(LEFT * 3.7 + UP * 0.9)
        self.play(Create(q_y_text))
        self.play(Create(allowed_area_text))
        for q_x in range(0, self.x, diff):
            q_y = -((self.d**3) / ((q_x**2) + (self.d**2)))
            self.allowed_area -= q_y * 2 * diff
            allowed_area_value_text = Text(text=str(int(self.allowed_area)), font_size=18, font="Arial").next_to(allowed_area_text)
            q_y_value_text = Text(text=str(int(q_y)), font_size=18, font="Arial").next_to(q_y_text)

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
            self.add(q_y_value_text)
            self.add(allowed_area_value_text)
            self.wait(4 / diff)
            self.remove(line1)
            self.remove(line2)
            self.remove(line3)
            self.remove(line4)
            self.remove(line5)
            self.remove(area)
            if q_x >= self.x - diff:
                self.wait(5)
            self.remove(q_y_value_text)
            self.remove(allowed_area_value_text)

    def construct(self):


        axes = Axes(y_range=(-150, 150, 50),
                    x_range=(-400, 400, 50),
                    y_length=9,
                    x_length=24,
                    ).add_coordinates()

        self.play(Create(axes))

        line1 = Line(start=LEFT*10+DOWN*3, end=RIGHT*10+DOWN*3, color=RED)
        line2 = Line(start=LEFT*10, end=RIGHT*10, color=RED)
        rectangle = Rectangle(height=0.5, width=1, color=BLUE, fill_color=BLUE, fill_opacity=0.5).shift(UP*2, LEFT*5)
        text = Text(text="Das Bereich\nder erlaubten Punkten", font_size=18, font="Arial").next_to(rectangle)
        all_area_text = Text(text="Die Gesamtfläche:  " + str(self.all_area), font_size=18, font="Arial").shift(UP*1.5, LEFT*4)
        self.play(Create(line1))
        self.play(Create(line2))

        circle = Circle(color=GREEN, radius=1.5).shift(DOWN*1.5)
        self.play(Create(circle))
        self.play(DrawBorderThenFill(rectangle))
        self.play(Create(text))
        self.play(Create(all_area_text))

        self.draw_curved(axes)
