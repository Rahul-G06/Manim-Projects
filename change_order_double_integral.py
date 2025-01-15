from manim import *

class Scene1(Scene):
    def construct(self):
        # Display the double integral
        double_integral = MathTex(r"\int_{0}^\infty \int_{x}^\infty \frac{e^{-y}}{y} \, dy \, dx").scale(1.5)
        
        self.play(Write(double_integral))
        self.wait(2)
        
        double_integral_small = double_integral.copy().scale(0.6).to_corner(UL)
        self.play(Transform(double_integral, double_integral_small))
        self.wait(1)

        double_integral_copy = double_integral.copy()
        double_integral_copy.move_to(double_integral)

        self.play(double_integral_copy.animate.next_to(double_integral, DOWN).to_edge(LEFT))
        self.wait(2)

        step1 = MathTex(r"= \int_{0}^\infty \left[ -\frac{e^{-y}}{y} - \int \frac{e^{-y}}{y^2} \, dy \right]_{x}^{\infty} \, dx"
        ).scale(0.8).next_to(double_integral, DOWN).to_edge(LEFT)
        
        self.play(Transform(double_integral_copy, step1))
        self.wait(2)

        step1_copy = step1.copy()
        step1_copy.move_to(step1)

        self.add(step1_copy)
        self.play(step1_copy.animate.next_to(step1, DOWN).to_edge(LEFT))
        self.wait(2)

        step2 = MathTex(r"= \int_{0}^\infty \left[ -\frac{e^{-y}}{y} + \frac{e^{-y}}{y^2} + 2 \int \frac{e^{-y}}{y^3} \, dy \right]_{x}^{\infty} \, dx"
        ).scale(0.8).next_to(step1, DOWN).to_edge(LEFT)

        self.play(Transform(step1_copy, step2))
        self.wait(2)

        step2_copy = step2.copy()
        step2_copy.move_to(step2)

        self.add(step2_copy)
        self.play(step2_copy.animate.next_to(step2, DOWN).to_edge(LEFT))
        self.wait(2)

        step3 = MathTex(r"= \int_{0}^\infty \left[ -\frac{e^{-y}}{y} + \frac{e^{-y}}{y^2} - \frac{2e^{-y}}{y^3} - 6 \int \frac{e^{-y}}{y^4} \, dy \right]_{x}^{\infty} \, dx"
        ).scale(0.8).next_to(step2, DOWN).to_edge(LEFT)

        self.play(Transform(step2_copy, step3))
        self.wait(2)
        
        step3_copy = step3.copy()
        step3_copy.move_to(step3)

        self.add(step3_copy)
        self.play(step3_copy.animate.next_to(step3, DOWN).to_edge(LEFT))
        self.wait(2)

        step4 = MathTex(
            r"= \int_{0}^\infty \left[ -\frac{e^{-y}}{y} + \frac{e^{-y}}{y^2} - \frac{2e^{-y}}{y^3} + \frac{6e^{-y}}{y^4} + 24 \int \frac{e^{-y}}{y^5} \, dy \right]_{x}^{\infty} \, dx"
        ).scale(0.8).next_to(step3, DOWN).to_edge(LEFT)

        self.play(Transform(step3_copy, step4))
        self.wait(2)

        step5 = MathTex(
            r"\int_{0}^\infty \left[ -\frac{e^{-x}}{x} + \frac{e^{-x}}{x^2} - \frac{2e^{-x}}{x^3} + \frac{6e^{-x}}{x^4} - \frac{24e^{-x}}{x^5}   ... \right] \, dx"
        ).scale(0.8).move_to(step4)

        self.play(Transform(step3_copy, step5))
        self.wait(2)

class Scene2(Scene):
    def construct(self):

        question = MathTex(r"\int_{0}^\infty \int_{x}^\infty \frac{e^{-y}}{y} \, dy \, dx").scale(0.8).to_corner(UL)

        self.play(Write(question))
        self.wait(2)

        question_copy = question.copy()
        question_copy.move_to(question)

        self.play(question_copy.animate.next_to(question, DOWN).to_edge(LEFT))
        self.wait(2)

        step1 = MathTex(
            r"= \int_{0}^\infty \int_{0}^y \frac{e^{-y}}{y} \, dx \, dy"
        ).scale(0.8).next_to(question_copy, RIGHT, buff = 0.5)
        self.play(Write(step1))
        self.wait(2)

        self.play(FadeOut(question_copy))
        self.play(step1.animate.to_edge(LEFT))

        step2 = MathTex(
            r"= \int_{0}^\infty \frac{e^{-y}}{y} \int_{0}^y 1 \, dx \, dy"
        ).scale(0.8).next_to(step1, DOWN, aligned_edge=LEFT)
        self.play(Write(step2))
        self.wait(4)

        step3 = MathTex(
            r"= \int_{0}^\infty \frac{e^{-y}}{y} \cdot y \, dy"
        ).scale(0.8).next_to(step2, DOWN, aligned_edge=LEFT)
        self.play(Write(step3))
        self.wait(4)

        step4 = MathTex(
            r"= \int_{0}^\infty e^{-y} \, dy"
        ).scale(0.8).next_to(step3, DOWN, aligned_edge=LEFT)
        self.play(Write(step4))
        self.wait(4)

        solution = MathTex(
            r"= \left[ -e^{-y} \right]_0^\infty = 1"
        ).scale(0.8).next_to(step4, DOWN, aligned_edge=LEFT)
        self.play(Write(solution))
        self.wait(4)

        # End scene
        self.play(FadeOut(question, step1, step2, step3, step4, solution))
        self.wait(1)

class Scene3(Scene):
    def construct(self):

        question = MathTex(r"\int_{0}^\infty \int_{x}^\infty \frac{e^{-y}}{y} \, dy \, dx").scale(0.8).to_corner(UL)
        new_question = MathTex(r"= \int_{0}^\infty \int_{0}^y \frac{e^{-y}}{y} \, dx \, dy").scale(1.2)
        axes = Axes(x_range = [0,5,1], y_range = [0,5,1],x_length = 5, y_length = 5, axis_config = {"include_tip" : True, "numbers_to_exclude" : [0]}
                     ).add_coordinates()
        label = axes.get_axis_labels(x_label = "x", y_label = "y")
        line1 = axes.plot(lambda x: x, x_range = [0,4], color = YELLOW)
        line2 = axes.plot(lambda x: x, x_range = [0,4.5], color = YELLOW)
        def riemann_above(x, y_upper):
            return Rectangle(
                width=0.07,
                height=y_upper - x,
                fill_opacity=0.5,
                color=BLUE,
                stroke_width=0,
            ).move_to(
                axes.c2p(x + 0.05, x + (y_upper - x) / 2))
        

        def riemann_across(y):
            return Rectangle(
                width= y,
                height= 0.07,
                fill_opacity=0.5,
                color=BLUE,
                stroke_width=0,
            ).move_to(
                axes.c2p((y/2),y))

        rectangles1 = VGroup(
            *[
                riemann_above(x, 4.5)
                for x in np.arange(0, 4, 0.1)
            ]
        )

        rectangles2 = VGroup(
            *[
                riemann_across(y)
                for y in np.arange(0, 4.5, 0.1)
            ]
        )
            
        self.play(Write(question))
        self.wait(2)
        self.play(Create(axes), Create(label), Create(line1), run_time = 3)
        self.play(Create(rectangles1), run_time = 5)
        self.wait(3)

        self.play(FadeOut(axes, label, line1, rectangles1))
        self.play(question.animate.move_to(ORIGIN).scale(1.5))
        self.wait(2)

        self.play(Transform(question, new_question))
        self.wait(2)
        self.play(question.animate.to_corner(UL).scale(0.6))
        self.wait(2)
        self.play(Create(axes), Create(label), Create(line2), run_time = 3)
        self.play(Create(rectangles2), run_time = 5)
        self.wait(5)




        