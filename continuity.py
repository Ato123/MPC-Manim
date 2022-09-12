from manim import *
import numpy as np


class continuity(Scene):
    def construct(self):
        # DELETE WHEN FINISHED
        self.camera.background_color = GRAY_E

        RED_LOGO = SVGMobject(r".\rMPC.svg", stroke_color=GRAY_D, width=7, fill_color='#C2344E')
        PINK_LOGO = SVGMobject(r".\pMPC.svg", stroke_color=GRAY_D, width=7, fill_color='#F88081')
        RED_LOGO.align_to(PINK_LOGO, LEFT)
        LOGO = VGroup(RED_LOGO, PINK_LOGO)

        self.play(DrawBorderThenFill(LOGO), runtime=1)
        self.wait(1)
        self.play(FadeOut(LOGO), runtime=1)

        txt = Text('Continuous?', font_size=92)
        self.play(Write(txt))
        self.wait(1)
        self.play(Unwrite(txt))
        plot = Axes(
            x_range=[-3 * PI / 2, 3 * PI / 2],
            y_range=[-2, 2],
            x_length=12,
            y_length=6,
            axis_config={
                'include_ticks': False,
                'include_tip': False
            }
        )

        self.play(FadeIn(plot), runtime=2)
        sinfunc = plot.plot(lambda x: np.sin(x), x_range=[-3 * PI / 2, 3 * PI / 2], color=TEAL)
        self.play(Create(sinfunc), runtime=1)
        self.play(Uncreate(sinfunc), Uncreate(plot), runtime=1)

        plot = Axes(
            x_range=[-1, 2],
            y_range=[-1, 5],
            x_length=12,
            y_length=6,
            axis_config={
                'include_ticks': False,
                'include_tip': False
            }
        )

        piece1 = plot.plot(lambda x: x ** 2, x_range=[-1, 1], color=TEAL)
        piece2 = plot.plot(lambda x: x ** 3 + 2, x_range=[1, 3 ** (1 / 3)], color=TEAL)
        holes = VGroup(
            Dot(point=plot.c2p(1, 1), radius=0.16, color=RED, fill_color=BLACK, stroke_width=6),
            Dot(point=plot.c2p(1, 3), radius=0.16, color=RED, fill_color=RED),
        )
        holes.set_z_index(2)

        # functxt = Tex(r"$f(x) = $", font_size=72)
        # funcgroup = VGroup(
        #     Tex(r"$x^2 \quad & x<1$", font_size=72).next_to(functxt, RIGHT*2 + UP),
        #     Tex(r"$x^3+2 \quad & 1 \leq x$", font_size=72).next_to(functxt, RIGHT*2 + DOWN)
        # )
        # func = VGroup(
        #     functxt,
        #     Brace(funcgroup, LEFT),
        #     funcgroup
        # ).center().shift(UP*8)

        func = Tex(
            r'$'
            r'f(x)='
            r'  \begin{cases}'
            r'      x^2 & x < 1 \\'
            r'      x^3+2 & 1 \leq x'
            r'  \end{cases}'
            r'$',
            font_size=72
        ).shift(UP * 7)

        self.play(FadeIn(plot), runtime=1)
        self.play(Create(piece1), Write(func), runtime=1)
        self.play(DrawBorderThenFill(holes), Create(piece2), runtime=1)

        self.play(FadeOut(holes), FadeOut(piece1), FadeOut(piece2), FadeOut(plot), FadeOut(func), runtime=1)

        plot = Axes(
            x_range=[-3*PI/2, 3*PI/2],
            y_range=[-2, 5],
            x_length=12,
            y_length=8,
            axis_config={
                'include_ticks': False,
                'include_tip': False
            }
        )

        xtick = ValueTracker(-3*PI/2)

        func = always_redraw(
            lambda:
            plot.plot(lambda x: x + np.sin(x), x_range=[-3*PI/2, xtick.get_value()], color=TEAL)
        )

        dot = always_redraw(
            lambda:
            Dot(radius=0.16, color=RED)
                .move_to(plot.c2p(xtick.get_value(), xtick.get_value() + np.sin(xtick.get_value())))
                .set_z_index(2)
        )

        pencil = always_redraw(
            lambda:
            SVGMobject(r".\pencil.svg", stroke_color=GRAY_D, width=1.5, fill_color='#F88081').next_to(dot, UP+LEFT)
        )

        self.add(func)
        self.play(FadeIn(plot), FadeIn(dot), FadeIn(pencil))
        self.wait(1)
        self.play(xtick.animate.move_to(-3*PI/4), runtime=4)
        self.wait(1)
        self.play(xtick.animate.move_to(0), runtime=4)
        self.wait(1)
        self.play(xtick.animate.move_to(3*PI/2), runtime=1)
        self.wait(3)

        self.play(FadeOut(VGroup(plot, dot, func, pencil)))

        txt = Tex(
            r'$'
            r'\lim\limits_{x \to c} f(x) = f(c)'
            r'$',
            font_size=72
        )

        txt2 = Tex(
            r'$'
            r'\text{for all } c \text{ in the interval}'
            r'$',
            font_size=72
        ).align_to(txt, LEFT).shift(DOWN*2)

        self.play(Write(txt), Write(txt2))
        self.wait(2)

        txt3 = Tex(
            r'$'
            r'\text{for all } c \text{ in the domain}'
            r'$',
            font_size=72
        ).align_to(txt, LEFT).shift(DOWN*2)

        txt4 = Tex(
            r'$'
            r'\text{for all } c \text{ in the}'
            r'$',
            font_size=72
        ).align_to(txt, LEFT).shift(DOWN * 2)

        self.add(txt4)
        self.play(FadeOut(txt2), FadeIn(txt3), runtime=1)
        self.wait(1)
        self.remove(txt4)
        self.play(FadeOut(txt), FadeOut(txt3), runtime=1)
