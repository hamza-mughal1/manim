from manim import *


class Intro1(Scene):
    def construct(self):
        font_of_text1 = "Edwardian Script ITC"
        fontSize = 70
        part1 = Text(" Created by. ", font_size=fontSize,font=font_of_text1)
        part2 = Text("Hamza Mughal", font_size=fontSize,font=font_of_text1, color=YELLOW)
        text1 = VGroup(part1, part2).arrange(RIGHT)
        self.play(Write(text1), run_time = 3)
        self.wait()
        self.play(FadeOut(text1),run_time = 2)
        self.wait()

class Intro2(Scene):
    def construct(self):
        font_of_text1 = "Times New Roman"
        part1 = Text("\" Mathematics ", font=font_of_text1)
        part2 = Text("discovers", font=font_of_text1, color=BLUE)
        part3 = Text(", it does not ", font=font_of_text1)
        part4 = Text("invent", font=font_of_text1, color=RED)
        part5 = Text(" \"", font=font_of_text1)
        text2 = Text("-Carl Friedrich Gauss",font_size=35,font=font_of_text1,color=YELLOW).shift(UP)
        text1 = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT)
        text1.shift(2*UP)
        self.play(FadeIn(text1), run_time = 2)
        self.play(text1.animate.scale(0.8))
        self.wait(2)
        self.play(Write(text2), run_time = 5)
        self.wait()

        self.play(FadeOut(text1),FadeOut(text2),run_time = 2)

        self.wait(2)

class WhatIsDerivative(Scene):
    def construct(self):
        font_of_text1 = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        """heading"""
        part1 = Text("what is ", font_size=heading_font_size,font=font_of_text1)
        part2 = Text("derivative", font_size=heading_font_size,font=font_of_text1, color=BLUE)
        part3 = Text("?", font_size=heading_font_size,font=font_of_text1)
        text1 = VGroup(part1, part2, part3).arrange(RIGHT)
        self.play(Write(text1), run_time = 2)
        self.wait(5)
        self.play(text1.animate.shift(3*UP))

        """question text"""
        part1 = Text("It is not about", font_size=normal_font_size,font=font_of_text1)
        part2 = Text("'how'", font_size=normal_font_size,font=font_of_text1, color=ORANGE)
        part3 = Text(",", font_size=normal_font_size,font=font_of_text1)
        part4 = Text("it is about", font_size=normal_font_size,font=font_of_text1)
        part5 = Text("'what'", font_size=normal_font_size,font=font_of_text1, color=GREEN)
        part6 = Text("and", font_size=normal_font_size,font=font_of_text1)
        part7 = Text("'why'", font_size=normal_font_size,font=font_of_text1, color=BLUE)
        part8 = Text(".", font_size=normal_font_size,font=font_of_text1)
        group1 = VGroup(part1, part2, part3, part4 ).arrange(RIGHT)
        group2 = VGroup(part5, part6, part7, part8).arrange(RIGHT)
        text2 = VGroup(group1, group2).arrange(DOWN, aligned_edge = LEFT)
        self.play(Write(text2), run_time = 4)
        self.play(text2.animate.shift(UP/2))
        self.wait(5)

        """removing first slide"""
        self.play(FadeOut(text1),FadeOut(text2),run_time = 1)
        self.wait()

        """Moving onto functions"""
        part1 = Text("Let's first look at", font_size=heading_font_size,font=font_of_text1)
        part2 = Text("'Functions'", font_size=heading_font_size,font=font_of_text1, color = YELLOW)
        part3 = Text(".", font_size=heading_font_size,font=font_of_text1)
        text3 = VGroup(part1, part2, part3).arrange(RIGHT)
        self.play(Write(text3), run_time = 2)
        self.play(text3.animate.shift(UP))
        self.wait(3)

        """removing second slide"""
        self.play(Unwrite(text3),run_time = 2)
        self.wait()

class Function(ThreeDScene):
    def construct(self):
        font_of_text1 = "Times New Roman"
        font_of_text = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        """heading"""
        part1 = Text("Think of a", font_size=heading_font_size,font=font_of_text1)
        part2 = Text("'function'", font_size=heading_font_size,font=font_of_text1, color=BLUE)
        part3 = Text("as a box", font_size=heading_font_size,font=font_of_text1)
        text1 = VGroup(part1, part2, part3).arrange(RIGHT).scale(0.5).to_edge(UP)

        """heading 2"""
        part1 = Text("A", font_size=heading_font_size,font=font_of_text1)
        part2 = Text("'box'", font_size=heading_font_size,font=font_of_text1, color=BLUE)
        part3 = Text("with two hole in it", font_size=heading_font_size,font=font_of_text1)
        text2 = VGroup(part1, part2, part3).arrange(RIGHT).scale(0.5).to_edge(UP)

        """normal text"""
        part1 = Text("Now imagine when we enter anything in", font_size=normal_font_size,font=font_of_text1)
        part2 = Text("'blue'", font_size=normal_font_size,font=font_of_text1, color=BLUE)
        part3 = Text("hole it comes out from", font_size=normal_font_size,font=font_of_text1)
        part4 = Text("'orange'", font_size=normal_font_size,font=font_of_text1, color=ORANGE)
        part5 = Text("hole. But", font_size=normal_font_size,font=font_of_text1)
        part6 = Text("it get's bigger by the magic of the box.", font_size=normal_font_size,font=font_of_text1)
        group1 = VGroup(part1, part2).arrange(RIGHT)
        group2 = VGroup(part3, part4, part5,).arrange(RIGHT)
        text3 = VGroup(group1, group2, part6).arrange(DOWN, aligned_edge = LEFT).scale(0.5).to_edge(UP)

        """normal text"""
        part1 = Text("Now we can see our ", font_size=normal_font_size,font=font_of_text1)
        part2 = Text("'sphere'", font_size=normal_font_size,font=font_of_text1, color=BLUE)
        part3 = Text("got bigger by the", font_size=normal_font_size,font=font_of_text1)
        part4 = Text("'magic'", font_size=normal_font_size,font=font_of_text1, color=RED)
        part5 = Text("of the box.", font_size=normal_font_size,font=font_of_text1)
        group1 = VGroup(part1, part2, part3).arrange(RIGHT)
        group2 = VGroup(part4, part5,).arrange(RIGHT)
        text4 = VGroup(group1, group2).arrange(DOWN, aligned_edge = LEFT).scale(0.5).to_edge(UP)

        """labels"""
        text5 = Text("INPUT", font_size=normal_font_size - 20, font=font_of_text, color=BLUE).shift(LEFT )
        text6 = Text("OUTPUT", font_size=normal_font_size - 20, font=font_of_text, color=ORANGE).shift(RIGHT *2).shift(UP)
        

        cube = Cube(side_length=3, fill_opacity= 0,  stroke_width=1, stroke_color = WHITE).rotate(PI/2, axis= UP)

        circle1 = Circle(radius=0.5, color=BLUE).move_to(cube.get_top()).rotate(PI/2, axis=RIGHT) 
        circle2 = Circle(radius=0.5, color=ORANGE).move_to(cube.get_bottom()).rotate(PI/2, axis=RIGHT)       
        group = VGroup(cube, circle1, circle2)
        self.play(Write(text1), run_time=2)
        self.play(Create(cube), run_time = 2)
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(Write(text2), run_time=2)
        self.play(Create(circle1),Create(circle2), run_time = 2)

        group.save_state()

        self.play(Rotate(group, PI/3, axis= RIGHT), run_time = 2)
        self.play(Rotate(group, PI/3, axis= DOWN), run_time = 2)
        self.play(Rotate(group, PI/3, axis= IN), run_time = 2)

        self.play(Restore(group), run_time=1)
        self.wait()

        self.play(FadeOut(text2), run_time = 1)
        self.play(Write(text3), run_time = 4)

        self.play(group.animate.shift(DOWN).scale(0.7))


        sphere = Sphere(radius=0.5, color = WHITE, fill_opacity = 1).move_to(cube.get_top()*3).scale(0.3).shift(UP)
        

        self.play(Create(sphere))
        self.bring_to_back(sphere)
        self.play(sphere.animate.move_to(cube.get_bottom()*1.5).scale(2), run_time = 2)

        self.play(FadeOut(text3), run_time = 1)
        self.play(Write(text4), run_time = 4)

        self.play(FadeOut(group), FadeOut(sphere), run_time = 1)

        sphere2 = Sphere(radius=0.5, color = BLUE, fill_opacity = 1).scale(0.6).shift(LEFT).shift(DOWN)
        sphere3 = Sphere(radius=0.5, color = ORANGE, fill_opacity = 1).scale(0.6)
        sphere3 = sphere3.scale(2).shift(RIGHT).shift(DOWN)

        

        arrow1 = Arrow(start=text5.get_bottom(), end=sphere2.get_top(), buff=0.1)
        arrow2 = Arrow(start=text6.get_bottom(), end=sphere3.get_top(), buff=0.1) 

        self.play(Write(text5), Write(text6), Create(sphere2), Create(sphere3), Create(arrow1),
                  Create(arrow2), run_time = 2)


        self.wait(3)

class Function2(Scene):
    def construct(self):
        font_of_text = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        """heading"""
        part1 = Text("Think that this box does some", font_size=heading_font_size - 25, font=font_of_text)
        part2 = Text("'Magic'", font_size=heading_font_size - 25, font=font_of_text, color=RED)
        part3 = Text("when we put some", font_size=heading_font_size - 25, font=font_of_text)
        part4 = Text("'input'", font_size=heading_font_size - 25, font=font_of_text, color=BLUE)
        part5 = Text("it does some", font_size=heading_font_size - 25, font=font_of_text)
        part6 = Text("'magic'", font_size=heading_font_size - 25, font=font_of_text, color=RED) 
        part7 = Text("and gives us", font_size=heading_font_size - 25, font=font_of_text)
        part8 = Text("'output'.", font_size=heading_font_size - 25, font=font_of_text, color=ORANGE) 
        group1 = VGroup(part1, part2).arrange(RIGHT)
        group2 = VGroup(part3, part4, part5).arrange(RIGHT)
        group3 = VGroup(part6, part7, part8).arrange(RIGHT)
        heading_text = VGroup(group1, group2, group3).arrange(DOWN, aligned_edge = LEFT).to_edge(UP)
        self.play(Write(heading_text), run_time = 6)
        
        """bottom portion"""
        sq = Square(side_length=3, color=BLUE, fill_opacity=0).to_edge(DOWN).scale(0.5)
        
        text1 = Text("INPUT", font_size=normal_font_size - 20, font=font_of_text, color=BLUE).shift(DL * 2).shift(LEFT * 3)
        text2 = Text("OUTPUT", font_size=normal_font_size - 20, font=font_of_text, color=ORANGE).shift(DR * 2).shift(RIGHT * 3)
        text3 = Text("MAGIC", font_size=normal_font_size - 25, font=font_of_text, color=RED).shift(sq.get_center())

        
        arrow1 = Arrow(start=text1.get_right(), end=sq.get_left(), buff=0.3)
        arrow2 = Arrow(start=sq.get_right(), end=text2.get_left(), buff=0.3)

        self.play(Create(sq), Write(text3), Write(text1), Write(text2), Create(arrow1), Create(arrow2), run_time = 3)
        self.wait(3)

        self.play(FadeOut(heading_text))

        """heading 2"""
        part1 = Text("Now let's think that the", font_size=heading_font_size - 25, font=font_of_text)
        part2 = Text("'Magic'", font_size=heading_font_size - 25, font=font_of_text, color=RED)
        part3 = Text("of the function is mathematical", font_size=heading_font_size - 25, font=font_of_text)
        part4 = Text("'equation'.", font_size=heading_font_size - 25, font=font_of_text, color=BLUE)
        group1 = VGroup(part1, part2).arrange(RIGHT)
        group2 = VGroup(part3, part4).arrange(RIGHT)
        heading_text = VGroup(group1, group2).arrange(DOWN, aligned_edge = LEFT).to_edge(UP)
        equation_text = Text("EQUATION", font_size=normal_font_size - 35, font=font_of_text, color=RED).shift(sq.get_center())
        self.play(Write(heading_text), run_time = 6)
        self.wait()
        self.play(FadeOut(text3), Write(equation_text))
        self.wait(2)

        self.play(FadeOut(heading_text),FadeOut(equation_text),
                  FadeOut(arrow1),FadeOut(arrow2),
                  FadeOut(text1),FadeOut(text2),FadeOut(sq))

class Function3(Scene):
    def construct(self):
        font_of_text = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        """heading"""
        part1 = Text("Let's see how this", font_size=heading_font_size, font=font_of_text)
        part2 = Text("'box'", font_size=heading_font_size, font=font_of_text, color=BLUE)
        part3 = Text("is related to", font_size=heading_font_size, font=font_of_text)
        part4 = Text("'functions'.", font_size=heading_font_size, font=font_of_text, color=YELLOW)
        
        group1 = VGroup(part1, part2).arrange(RIGHT)
        group2 = VGroup(part3, part4).arrange(RIGHT)
        heading_text = VGroup(group1, group2).arrange(DOWN, aligned_edge = LEFT)
        self.play(Write(heading_text), run_time = 3)
        self.wait(3)
        self.play(Unwrite(heading_text))

class Function4(Scene):
    def construct(self):
        font_of_text = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        part1 = Text("Let's say we have this", font=font_of_text, font_size=heading_font_size - 20)
        part2 = Text("'function'", font=font_of_text, font_size=heading_font_size - 20, color = YELLOW)
        part3 = Text("here:", font=font_of_text, font_size=heading_font_size - 20)
        text1 = VGroup(part1, part2, part3).arrange(RIGHT).shift(UP)
        self.play(Write(text1), run_time = 2)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("x", color = BLUE).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("2x", color = BLUE).scale(2)
        fn_eq = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT).scale(0.8)
        self.play(Write(fn_eq), text1.animate.shift(UP*2), run_time = 2)
        self.wait(3)

        text2 = Text("INPUT", font_size=normal_font_size - 20, font=font_of_text, color=BLUE).shift(LEFT)
        text3 = Text("OUTPUT", font_size=normal_font_size - 20, font=font_of_text, color=ORANGE).shift(RIGHT*5).shift(DOWN*2)
        text4 = Text("EQUATION", font_size=normal_font_size - 20, font=font_of_text, color=RED).shift(RIGHT*2)

        self.play(fn_eq.animate.shift(DOWN*2), run_time = 1)

        arrow1 = Arrow(start=text2.get_bottom(), end=part2.get_top(), buff=0.1)
        arrow2 = Arrow(start=text3.get_left(), end=part5.get_right(), buff=0.1)
        arrow3 = Arrow(start=text4.get_bottom(), end=part5.get_top(), buff=0.1)

        self.play( Write(text2),
                  Write(text3),Write(text4), Create(arrow1),
                  Create(arrow2), Create(arrow3), run_time = 3)
        

        self.play(FadeOut(text1), run_time = 1)

        part1 = Text("Let's put some input in this", font=font_of_text, font_size=heading_font_size - 20)
        part2 = Text("'function'", font=font_of_text, font_size=heading_font_size - 20, color = YELLOW)
        part3 = Text(".", font=font_of_text, font_size=heading_font_size - 20)
        text1 = VGroup(part1, part2, part3).arrange(RIGHT).shift(UP*3)
        self.play(Write(text1), run_time = 2)

        part1 = Text("E.G.", font=font_of_text, font_size=normal_font_size - 10)
        part2 = Text("'x'", font=font_of_text, font_size=normal_font_size - 10, color = BLUE)
        part3 = Text("=", font=font_of_text, font_size=normal_font_size - 10)
        part4 = Text("'2'", font=font_of_text, font_size=normal_font_size - 10, color = GREEN)
        text5 = VGroup(part1, part2, part3, part4).arrange(RIGHT).to_edge(LEFT).shift(UP)
        self.play(Write(text5), run_time = 2)
        self.wait(1)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("2", color = GREEN).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("2", color = BLUE).scale(2)
        part6 = Tex("(").scale(2)
        part7 = Tex("2", color = GREEN).scale(2)
        part8 = Tex(")").scale(2)
        fn_eq2 = VGroup(part1, part2, part3, part4, part5,
                       part6, part7, part8).arrange(RIGHT).scale(0.8).shift(DOWN*2)
        
        arrow4 = Arrow(start=text2.get_bottom(), end=part2.get_top(), buff=0.1)
        arrow5 = Arrow(start=text3.get_left(), end=part8.get_right(), buff=0.1)
        arrow6 = Arrow(start=text4.get_bottom(), end=part7.get_top(), buff=0.1)
        
        self.play(Transform(fn_eq, fn_eq2), 
                  Transform(arrow1,arrow4),
                  Transform(arrow2,arrow5),
                  Transform(arrow3,arrow6), run_time = 2)
        
        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("2", color = GREEN).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("2", color = BLUE).scale(2)
        part6 = Tex("(").scale(2)
        part7 = Tex("2", color = GREEN).scale(2)
        part8 = Tex(") = 4").scale(2)
        fn_eq3 = VGroup(part1, part2, part3, part4, part5,
                       part6, part7, part8).arrange(RIGHT).scale(0.8).shift(DOWN*2)
        
        arrow7 = Arrow(start=text2.get_bottom(), end=part2.get_top(), buff=0.1)
        arrow8 = Arrow(start=text3.get_left(), end=part8.get_right(), buff=0.1)
        arrow9 = Arrow(start=text4.get_bottom(), end=part7.get_top(), buff=0.1)
        
        self.play(Transform(fn_eq, fn_eq3), 
                  Transform(arrow1,arrow7),
                  Transform(arrow2,arrow8),
                  Transform(arrow3,arrow9), run_time = 2)
        

        self.play(FadeOut(text1), FadeOut(text5), run_time = 0.5)

        part1 = Text("As we can see here our", font=font_of_text, font_size=heading_font_size - 20)
        part2 = Text("'input'", font=font_of_text, font_size=heading_font_size - 20, color = BLUE)
        part3 = Text("got bigger/multiplied just", font=font_of_text, font_size=heading_font_size - 20)
        part4 = Text("like our", font=font_of_text, font_size=heading_font_size - 20)
        part5 = Text("'sphere'.", font=font_of_text, font_size=heading_font_size - 20, color = BLUE)
        

        group1 = VGroup(part1, part2).arrange(RIGHT)
        group2 = VGroup(part4, part5).arrange(RIGHT)
        text1 = VGroup(group1, part3, group2).arrange(DOWN, aligned_edge = LEFT).shift(UP*2)
        self.play(Write(text1), run_time = 4)

        self.play(FadeOut(text1), FadeOut(text2),
                  FadeOut(text3), FadeOut(text4),
                  FadeOut(arrow1), FadeOut(arrow2),
                  FadeOut(arrow3), FadeOut(fn_eq))

        self.wait(1)

class Function5(Scene):
    def construct(self):
        font_of_text = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        """heading"""
        part1 = Text("'Functions'", font_size=heading_font_size - 15, font=font_of_text, color = YELLOW)
        part2 = Text("can perform any functionality", font_size=heading_font_size - 15, font=font_of_text)
        part3 = Text("on given", font_size=heading_font_size - 15, font=font_of_text)
        part4 = Text("'input'", font_size=heading_font_size - 15, font=font_of_text, color = BLUE)
        part5 = Text("not just", font_size=heading_font_size - 15, font=font_of_text)
        part6 = Text("'multiplication'", font_size=heading_font_size - 15, font=font_of_text, color = GREEN)
        part7 = Text(".", font_size=heading_font_size - 15, font=font_of_text)

        group1 = VGroup(part1, part2).arrange(RIGHT)
        group2 = VGroup(part3, part4, part5, part6, part7).arrange(RIGHT)
        text1 = VGroup(group1, group2).arrange(DOWN, aligned_edge = LEFT)

        """normal text"""
        text2 = Text("E.G.", font_size=normal_font_size - 15, font=font_of_text).to_edge(LEFT).shift(UP)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("x", color = BLUE).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("3x", color = BLUE).scale(2)
        fn_eq = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT).scale(0.5).shift(UP)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("x", color = BLUE).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("x", color = BLUE).scale(2)

        fn_eq2 = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT).scale(0.5)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("x", color = BLUE).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex(r"$\sqrt[2]{x}$", color = BLUE).scale(2)

        fn_eq3 = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT).scale(0.5).shift(DOWN)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("x", color = BLUE).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("x/2", color = BLUE).scale(2)

        fn_eq4 = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT).scale(0.5).shift(DOWN*2)

        part1 = Tex("f(", color = YELLOW).scale(2)
        part2 = Tex("x", color = BLUE).scale(2)
        part3 = Tex(")", color = YELLOW).scale(2)
        part4 = Tex("=",).scale(2)
        part5 = Tex("1/x", color = BLUE).scale(2)
        fn_eq5 = VGroup(part1, part2, part3, part4, part5).arrange(RIGHT).scale(0.5).shift(DOWN*3)

        self.play(Write(text1), run_time = 6)
        self.play(text1.animate.shift(UP*3).scale(0.8))
        self.wait(1)

        self.play(Write(fn_eq),Write(fn_eq2),
                  Write(fn_eq3),Write(fn_eq4),
                   Write(fn_eq5), Write(text2), run_time = 3)

        
        

        self.wait(3)

        self.play(FadeOut(text1) , FadeOut(text2),
                  FadeOut(fn_eq),FadeOut(fn_eq2),
                  FadeOut(fn_eq3),FadeOut(fn_eq4),
                   FadeOut(fn_eq5), run_time = 2)
        
class Function6(Scene):
    def construct(self):
        font_of_text = "Times New Roman"
        heading_font_size = 70
        normal_font_size = 50

        part1 = Text("In a nutshell", font_size=heading_font_size - 15, font=font_of_text)
        part2 = Text("'functions'", font_size=heading_font_size - 15, font=font_of_text, color = YELLOW)
        part3 = Text("are just like a", font_size=heading_font_size - 15, font=font_of_text)
        part4 = Text("'machine'", font_size=heading_font_size - 15, font=font_of_text, color = PURPLE)
        part5 = Text("which can perform some", font_size=heading_font_size - 15, font=font_of_text)
        part6 = Text("'functionality'", font_size=heading_font_size - 15, font=font_of_text, color = YELLOW_B)
        part7 = Text("/", font_size=heading_font_size - 15, font=font_of_text)
        part8 = Text("'transformation'", font_size=heading_font_size - 15, font=font_of_text, color = YELLOW_B)
        part9 = Text("on a given", font_size=heading_font_size - 15, font=font_of_text)
        part10 = Text("'input'", font_size=heading_font_size - 15, font=font_of_text, color = BLUE)
        part11 = Text("and returns us", font_size=heading_font_size - 15, font=font_of_text)
        part12 = Text("'output'", font_size=heading_font_size - 15, font=font_of_text, color = ORANGE)
        part13 = Text(".", font_size=heading_font_size - 15, font=font_of_text)

        group1 = VGroup(part1, part2, part3).arrange(RIGHT)
        group2 = VGroup(part4, part5).arrange(RIGHT)
        group3 = VGroup(part6, part7, part8, part9).arrange(RIGHT)
        group4 = VGroup(part10, part11, part12, part13).arrange(RIGHT)

        text1 = VGroup(group1, group2, group3,
                       group4).arrange(DOWN, aligned_edge = LEFT)
        
        self.play(Write(text1), run_time = 6)
        self.play(text1.animate.shift(UP))

        self.wait(3)

        self.play(FadeOut(text1))
