from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=1)

        square = Square()
        square.set_fill(ORANGE, opacity=1)

        arc = Arc(radius=2, angle=PI, start_angle=100, fill_color=BLUE)

        square.rotate(PI / 2)
        self.play(FadeIn(arc))
        # self.play(Create(circle))
        self.play(Transform(arc, circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.remove(arc)
        self.wait(1)
        self.play(circle.animate(run_time=2).move_to(LEFT * 2).rotate(PI / 2))
        self.wait(1)
        self.play(FadeOut(circle))
        self.wait(1)
