import numpy as np
from manim import *

class scene1(Scene):
    def construct(self):

        e = ValueTracker(0)

        axes1 = Axes(x_range = [0,5,1], y_range = [0,20,4], x_length = 4, y_length = 7,
                     axis_config = {"include_tip" : True, "numbers_to_exclude" : [0]}
                     ).add_coordinates()
        label1 = axes1.get_axis_labels(x_label = "x", y_label = "y")
        graph1 = axes1.plot(lambda x : x ** 2, x_range = [0,4], color = YELLOW)

        tangent = always_redraw(lambda: TangentLine(graph1, alpha=e.get_value()/4, length=4, color=TEAL))
        dot1 = always_redraw(lambda: Dot(fill_color=TEAL, fill_opacity=0.8).scale(1).move_to(tangent.get_center()))
        text1 = always_redraw(lambda : Tex(f"slope = {(e.get_value()*2):.2f}", color = WHITE).move_to(axes1, UR))
        axes1_stuff = Group(axes1, label1, graph1, dot1, tangent, text1)
        axes1_stuff.shift(LEFT*3)

        axes2 = Axes(x_range = [0,5,1], y_range = [0,20,4], x_length = 4, y_length = 7,
                     axis_config = {"include_tip" : True, "numbers_to_exclude" : [0]}
                     ).add_coordinates()
        label2 = axes2.get_axis_labels(x_label = "x", y_label = "y")
        graph2 = axes2.plot(lambda x: 2*x, x_range = [0,4],color = YELLOW)
        dot2 = always_redraw(lambda: Dot(fill_color=TEAL, fill_opacity=0.8).scale(1).move_to(axes2.c2p(e.get_value(),(e.get_value())*2)))
        text2 = always_redraw(lambda : Tex(f"y = {(e.get_value()*2):.2f}", color = WHITE).move_to(axes2, UR))
        axes2_stuff = Group(axes2, label2, graph2, dot2, text2)
        axes2_stuff.shift(RIGHT*3)


        self.add(axes1_stuff, axes2_stuff)
        self.play(e.animate.set_value(3), run_time=5,rate_func=linear)
        self.wait()