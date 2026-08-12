from manim import *

class lesson1(Scene):
    def construct(self):

        ## Intro Card ##
        # 0:00.000 - 0:04.972
        greeting = Text("Hello!").scale(3)
        greeting.to_edge(UP, 2)
        lessonname = Text("Lesson 1.1: Analyzing categorical data")
        lessonname.to_edge(DOWN, 2)
        self.add_sound("U1_ExploringData\\1.1\\speech1.1.wav")
        self.play(Write(greeting, run_time=.64));self.wait(.7)
        self.play(Write(lessonname, run_time=2)) ## Finishes 3.34 seconds in
        self.wait(0.932)  ## Finishes 4.272 seconds in
        self.play(Unwrite(lessonname, run_time=0.7), Unwrite(greeting, run_time=0.7))

        ## Learning target ##
        # 0:04.972 - 
        lt1 = Text("1. Explore collected data")
        lt2 = Text("2. Categorial or quantitative?")
        lt3 = Text("3. Check out some basic graphs")
        lt4 = Text("4. Fixing misleading graphs")

        learningtargets = VGroup(lt1, lt2, lt3, lt4).arrange(direction=DOWN).set_submobject_colors_by_gradient(RED, BLUE)

        self.play(Write(learningtargets, lag_ratio=0.5, run_time=0.524))
        self.play(Indicate(learningtargets[0], run_time=1.641));self.wait(1.033)
        self.play(Indicate(learningtargets[1], run_time=2.570));self.wait(0.834)
        self.play(Indicate(learningtargets[2], run_time=3.959));self.wait(0.05) ## end at 15.583
        self.play(Indicate(learningtargets[3], run_time=2.605));self.wait(0.978) ## end at 19.275
        self.wait(1.155)
        self.play(Unwrite(learningtargets, run_time=5.982))


