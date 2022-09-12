from manim import *

class driver(Scene):
    def construct(self):
        
        # DELETE WHEN FINISHED
        #self.camera.background_color=GRAY_E
        
        # Intro
        RED_LOGO = SVGMobject(r".\rMPC.svg", stroke_color=GRAY_E, width=7, fill_color='#C2344E')
        PINK_LOGO= SVGMobject(r".\pMPC.svg", stroke_color=GRAY_E, width=7, fill_color='#F88081')
        RED_LOGO.align_to(PINK_LOGO, LEFT)
        LOGO = VGroup(RED_LOGO, PINK_LOGO)

        self.play(DrawBorderThenFill(LOGO))
        
        lim = Tex(r'\[ \lim_{x\to2} x^3 \]', font_size=144)

        self.play(AnimationGroup(LOGO.animate.shift(UP*8), Write(lim), lag_ratio=1))

        self.play(AnimationGroup(FadeOut(LOGO), lim.animate.shift(UP*8), lag_ratio=0.5))

        plane = Axes(
                x_range=[-10,10,1],
                y_range=[-10,10,1],
                x_length=10,
                y_length=10,
                axis_config={
                    'include_numbers': False,
                    'tick_size': 0.1,
                    'stroke_width' : 4
                    },
                tips=False
                )
        
        xtick = ValueTracker(0)

        bnd = (10)**(1/3)
        func = plane.plot(lambda x : x**3, x_range=[-bnd,bnd], color=TEAL, stroke_width=8)

        xpos = DecimalNumber(0, font_size=144)
        ypos = DecimalNumber(0, font_size=144)

        xlabel = Tex(r'\[x = \]', font_size=144)
        ylabel = Tex(r'\[y = \]', font_size=144)

        table = VGroup(xlabel, xpos, ylabel, ypos)
        ylabel.next_to(xlabel, DOWN*4)
        xpos.next_to(xlabel, RIGHT)
        ypos.next_to(ylabel, RIGHT)
        table.next_to(plane, DOWN*5)

        xpos.add_updater(lambda x: x.set_value(xtick.get_value()))
        ypos.add_updater(lambda y: y.set_value(xtick.get_value()**3))

        pt = Dot(point=plane.c2p(0,0), radius=0.16, color=RED)
        pt.add_updater(lambda p: p.move_to(plane.i2gp(xtick.get_value(), func)))
        self.play(Create(plane), Create(table), Create(func), Create(pt))
        self.wait(2)

        self.play(xtick.animate.move_to(1), run_time=2)
        self.play(xtick.animate.move_to(2), run_time=2)
        self.play(xtick.animate.move_to(-bnd), run_time=2)

        self.play(FadeOut(plane), FadeOut(table), FadeOut(func), FadeOut(pt), FadeOut(lim))

        car = SVGMobject(r".\car.svg", stroke_color=PURE_RED, stroke_width=8, width=4, fill_color=None)
        shop = SVGMobject(r".\shop.svg", stroke_color=PURE_BLUE, stroke_width=8, width=4, fill_color=None)

        car.shift(LEFT*4)
        shop.shift(RIGHT*4)

        self.play(AnimationGroup(Create(shop), Create(car), lag_ratio=0.5))
        self.wait(1)

        self.play(car.animate.shift(RIGHT*3))
        self.wait(2)

        plane = Axes(
                x_range=[-10,10,1],
                y_range=[-10,10,1],
                x_length=8,
                y_length=8,
                axis_config={
                    'include_numbers': False,
                    'tick_size': 0.1,
                    'stroke_width' : 4
                    },
                tips=False
                )

        xtick = ValueTracker(0)

        bnd = (10)**(1/3)
        func = plane.plot(lambda x : x**3, x_range=[-bnd,bnd], color=TEAL, stroke_width=8)

        xpos = DecimalNumber(0, font_size=72)
        ypos = DecimalNumber(0, font_size=72)

        xlabel = Tex(r'\[x = \]', font_size=72)
        ylabel = Tex(r'\[y = \]', font_size=72)

        table = VGroup(xlabel, xpos, ylabel, ypos)
        ylabel.next_to(xlabel, DOWN*2)
        xpos.next_to(xlabel, RIGHT)
        ypos.next_to(ylabel, RIGHT)
        table.next_to(plane, RIGHT*2)

        xpos.add_updater(lambda x: x.set_value(xtick.get_value()))
        ypos.add_updater(lambda y: y.set_value(xtick.get_value()**3))

        pt = Dot(point=plane.c2p(0,0), radius=0.08, color=RED)
        pt.add_updater(lambda p: p.move_to(plane.i2gp(xtick.get_value(), func)))

        VGroup(plane, table, func, pt).shift(LEFT*2)
        
        self.play(
                AnimationGroup(
                    AnimationGroup(
                        car.animate.shift(LEFT*3+UP*8),
                        shop.animate.shift(UP*8)
                        ),
                        
                    FadeIn(VGroup(plane, table, func, pt)),

                    lag_ratio = 0.05
                    )
                )

        self.play(xtick.animate.move_to(2), car.animate.shift(RIGHT*2))

        def tsfm(mobj):
            mobj.scale(1.25)
            mobj.shift(RIGHT*2)
            return mobj

        self.play(
                AnimationGroup(
                    FadeOut(table),
                    ApplyFunction(tsfm, VGroup(plane, func, pt)), 
                    lag_ratio=0.5
                    )
                )
        table.move_to(ORIGIN)
        table.shift(DOWN*7)
        self.play(FadeIn(table), xtick.animate.move_to(0))

        car.set_z_index(10)
        limpt = Dot(point=plane.c2p(2, 8), radius = 0.16, color=PURE_BLUE)
        def tsfm1(mobj):
            mobj.scale(0.3)
            #mobj.next_to(pt, UP+LEFT)
            mobj.set_fill(RED)
            mobj.add_updater(lambda c: c.move_to(plane.i2gp(xtick.get_value(), func)+UP+LEFT))
            return mobj

        def tsfm2(mobj):
            mobj.scale(0.3)
            mobj.set_fill(BLUE)
            mobj.next_to(limpt, RIGHT*2)
            return mobj

        self.play(ApplyFunction(tsfm1, car), ApplyFunction(tsfm2, shop), FadeIn(limpt))

        car.add_updater(lambda c: c.move_to(plane.i2gp(xtick.get_value(), func)+UP+LEFT))
        self.wait(1)

        self.play(xtick.animate.move_to(2), run_time=2)
        self.wait(3)

