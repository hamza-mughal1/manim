from manim import *

class Test(Scene):
    def construct(self):
        title = Tex(r"HELLO")
        end_scene = Tex(r"Thanks for watching :) see you soon!")
        circle = Circle()
        triangle = Triangle()
        square = Square()
        square.flip(LEFT)

        self.play(
            Write(title),
        )
        self.play(
            Unwrite(title),
        )
        self.play(Create(square))
        square.save_state()
        self.play(Transform(square, circle))
        self.play(Transform(square, triangle))
        square.generate_target()
        square.target.move_to(2*UP)
        self.play(MoveToTarget(square))
        self.play(Transform(square,circle))
        self.play(Restore(square))
        self.play(Uncreate(square))

        self.play(
            Write(end_scene),
        )
        self.play(
            Unwrite(end_scene),
        )



