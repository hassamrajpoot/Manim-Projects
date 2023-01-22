from manim import *
from manim.utils.color import Colors

class PartTwo(Scene):
    def construct(self):
        dot = Dot(color=YELLOW).move_to([0,0,0])
        self.play(FadeIn(dot))
        eq1 = Tex("$fA = tfB + \overline{oP}$", color=Colors.pure_green.value).scale(0.8)
        eq2 = Tex("$fB = tFA$", color=Colors.pure_green.value).scale(0.8)
        eq1.move_to(UP*3)
        eq2.next_to(eq1, DOWN)
        eq1.scale(1)
        eq2.scale(1)
        self.play(Transform(dot, VGroup(eq1,eq2)))
        self.play(DrawBorderThenFill(eq1,run_time=2, rate_func=rate_functions.linear))
        self.play(DrawBorderThenFill(eq2,run_time=2, rate_func=rate_functions.linear))
        self.play(Indicate(eq1),Indicate(eq2))
        target_feedback = Text('Target \nFeedback', color=BLUE, stroke_width=0.1).scale(0.3)
        last_output = Text('Last \nOutput', color=BLUE, stroke_width=0.1).scale(0.3)
        wanted_top_feedback = Text('Wanted Top \nFeedback', color=BLUE, stroke_width=0.1).scale(0.3)
        Truth_Table = Table([['0','0','1'],['0','1','1'],['1','0','1'],['1','1','0']],col_labels =[Tex("A"),Tex("B"),Tex("A\:\\tiny NAND\:\\normalsize  B")], h_buff=0.5, v_buff=0.23,line_config={"stroke_width": 2, "color": YELLOW}, include_outer_lines=True)
        Truth_Table.remove(*Truth_Table.get_vertical_lines())
        target_feedback.next_to([-2.3,2,0])
        last_output.next_to([-1.2,2,0])
        wanted_top_feedback.next_to([0.2,2,0])
        lines = Truth_Table.get_horizontal_lines()
        Truth_Table.remove(*[lines[i] for i in range(2, len(lines))])
        Table_with_headers = VGroup(target_feedback, last_output, wanted_top_feedback ,Truth_Table)
        for_surrounding_rect = VGroup(last_output, wanted_top_feedback,Truth_Table.get_columns()[1:])
        
        last_output_wanted_top_feedback_table = Table([['0','0'],['0','1'],['1','0'],['1','1']], col_labels=[Tex("$\overline{oP}$"), Tex('tfA')], h_buff=0.5,v_buff=0.5,line_config={"stroke_width": 2, "color": YELLOW}, include_outer_lines=True)
        Table_with_headers.scale(0.8).move_to(RIGHT*5)
        last_output1 = Text('Last \nOutput', color=BLUE, stroke_width=0.1).scale(0.35)
        wanted_top_feedback1 = Text('Wanted Top \nFeedback', color=BLUE, stroke_width=0.1).scale(0.35)
        last_output1.next_to([-1.6,2.4,0])
        wanted_top_feedback1.next_to([-0.2,2.4,0])
        last_output_wanted_top_feedback_table = Table([['0','0'],['0','1'],['1','0'],['1','1']], col_labels=[Tex("$\overline{oP}$",color=Colors.pure_green.value), Tex('tfA',color=Colors.pure_green.value)], h_buff=1.3,v_buff=0.35,line_config={"stroke_width": 2, "color": YELLOW}, include_outer_lines=True)
        last_output_wanted_top_feedback_table.remove(*last_output_wanted_top_feedback_table.get_vertical_lines())
        lines1 = last_output_wanted_top_feedback_table.get_horizontal_lines()
        last_output_wanted_top_feedback_table.remove(*[lines1[i] for i in range(2, len(lines1))])
        last_output_wanted_top_feedback_table_with_headers = VGroup(last_output1, wanted_top_feedback1, last_output_wanted_top_feedback_table)
        self.play(GrowFromCenter(Table_with_headers), color=YELLOW, run_time=1, rate_func=rate_functions.linear)
        self.wait(1)
        self.play(FadeOut(SurroundingRectangle(for_surrounding_rect, buff=0.1), run_time=2))
        self.play(GrowFromPoint(last_output_wanted_top_feedback_table_with_headers.scale(0.7).move_to(LEFT*5), Truth_Table.get_columns()[1:], color=YELLOW),run_time=1, rate_func=rate_functions.linear)
        self.wait(1)
        target_feedback1 = Text('Target \nFeedback', color=BLUE, stroke_width=0.1).scale(0.4)
        fa_fb_table = Table([['1', '0'],['1', '1'],['1','0'],['0','1']], col_labels=[Tex("$fA = tfB + \overline{oP}$"),Tex("$fB = tFA$")], include_outer_lines = True, h_buff=0.5,v_buff=0.45,line_config={"stroke_width": 2, "color": YELLOW})
        target_feedback1.next_to([-1,2.75,0])
        fa_fb_table.remove(*fa_fb_table.get_vertical_lines())
        lines2 = fa_fb_table.get_horizontal_lines()
        fa_fb_table.remove(*[lines2[i] for i in range(2, len(lines2))])
        fa_fb_table_with_headers = VGroup(target_feedback1, fa_fb_table)
        for_surrounding_rect1 = VGroup(target_feedback,Truth_Table.get_columns()[0])
        self.play(FadeOut(SurroundingRectangle(for_surrounding_rect1, buff=0.1), run_time=3))
        self.play(GrowFromPoint(fa_fb_table_with_headers.scale(0.6).move_to(LEFT*1), Truth_Table.get_columns()[0], color=YELLOW),run_time=1, rate_func=rate_functions.linear)
        self.wait(1)
        
        anim1 = SurroundingRectangle(Truth_Table.get_cell(pos=(3,1)), buff=0, color=Colors.pure_green.value)
        anim2 = SurroundingRectangle(Truth_Table.get_rows()[2][1:],buff=0.12, color=Colors.pure_blue.value)
        self.play(FadeIn(anim1, run_time=2), FadeIn(anim2, run_time=2))
        # self.play(FadeOut(anim1, run_time=2), FadeOut(anim2, run_time=2))
        anim3 = SurroundingRectangle(last_output_wanted_top_feedback_table.get_rows()[-1], color=Colors.pure_blue.value, buff=0.15)
        self.play(FadeIn(anim3),run_time=2)
        # self.play(FadeOut(anim3), run_time=2)
        anim4 = SurroundingRectangle(fa_fb_table.get_rows()[-1], color=Colors.pure_green.value, buff=0.15)
        self.play(FadeIn(anim4),run_time=2)
        # self.play(FadeOut(anim4), run_time=2)
        self.play(FadeOut(anim1, run_time=3), FadeOut(anim2, run_time=3),FadeOut(anim3, run_time=3),FadeOut(anim4, run_time=3))
        self.wait(0.5)
        
        anim5 = SurroundingRectangle(Truth_Table.get_cell(pos=(5,1)), buff=0, color=Colors.pure_green.value)
        anim6 = SurroundingRectangle(Truth_Table.get_rows()[4][1:],buff=0.12, color=Colors.pure_blue.value)
        self.play(FadeIn(anim5, run_time=2), FadeIn(anim6, run_time=2))
        #self.play(FadeOut(anim5, run_time=2), FadeOut(anim6, run_time=2))
        anim7 = SurroundingRectangle(last_output_wanted_top_feedback_table.get_rows()[-2], color=Colors.pure_blue.value,buff=0.15)
        self.play(FadeIn(anim7),run_time=2)
        #self.play(FadeOut(anim7), run_time=2)
        anim8 = SurroundingRectangle(fa_fb_table.get_rows()[-2], color=Colors.pure_green.value,buff=0.15)
        self.play(FadeIn(anim8),run_time=2)
        self.play(FadeOut(anim5, run_time=3),FadeOut(anim6, run_time=3), FadeOut(anim7, run_time=3),FadeOut(anim8,run_time=3))
        self.wait(0.5)
        
        anim9 = SurroundingRectangle(Truth_Table.get_cell(pos=(2,1)), buff=0, color=Colors.pure_green.value)
        anim10 = SurroundingRectangle(Truth_Table.get_rows()[1][1:],buff=0.12, color=Colors.pure_blue.value)
        anim11 = SurroundingRectangle(Truth_Table.get_cell(pos=(4,1)), buff=0, color=Colors.pure_green.value)
        anim12 = SurroundingRectangle(Truth_Table.get_rows()[3][1:],buff=0.12, color=Colors.pure_blue.value)
        self.play(FadeIn(anim9, run_time=2), FadeIn(anim10, run_time=2), FadeIn(anim11, run_time=2),FadeIn(anim12, run_time=2))
        #self.play(FadeOut(anim9, run_time=2), FadeOut(anim10, run_time=2),FadeOut(anim11, run_time=2),FadeOut(anim12, run_time=2))
        anim13 = SurroundingRectangle(last_output_wanted_top_feedback_table.get_rows()[2], color=Colors.pure_blue.value,buff=0.15)
        self.play(FadeIn(anim13),run_time=2)
        #self.play(FadeOut(anim13), run_time=2)
        anim14 = SurroundingRectangle(fa_fb_table.get_rows()[2], color=Colors.pure_green.value,buff=0.15)
        self.play(FadeIn(anim14),run_time=2)
        self.play(FadeOut(anim9, run_time=3),FadeOut(anim10, run_time=3), FadeOut(anim11, run_time=3), FadeOut(anim12, run_time=3),FadeOut(anim13, run_time=3),
                FadeOut(anim14, run_time=3))
        self.wait(0.5)
        
        anim15 = SurroundingRectangle(Truth_Table.get_cell(pos=(5,1)), buff=0, color=Colors.pure_green.value)
        anim16 = SurroundingRectangle(Truth_Table.get_rows()[4][1:],buff=0.12, color=Colors.pure_red.value)
        tick_anim = Dot(radius=0.03,color=Colors.pure_red.value).next_to(Truth_Table.get_cell(pos=(5,2)).get_center(), DOWN*0.5 + RIGHT*0.5)
        self.play(FadeIn(anim15, run_time=2), FadeIn(anim16, run_time=2), FadeIn(tick_anim, run_time=2))
        #self.play(FadeOut(anim15, run_time=2), FadeOut(anim16, run_time=2), Flash(tick_anim, color=Colors.pure_red.value))
        self.play(Flash(tick_anim, color=Colors.pure_red.value))
        self.play(FadeOut(tick_anim))
        anim17 = SurroundingRectangle(last_output_wanted_top_feedback_table.get_rows()[1], color=Colors.pure_red.value,buff=0.15)
        self.play(FadeIn(anim17),run_time=2)
        #self.play(FadeOut(anim17), run_time=2)
        anim18 = SurroundingRectangle(fa_fb_table.get_rows()[1], color=Colors.pure_green.value,buff=0.15)
        self.play(FadeIn(anim18),run_time=2)
        self.play(FadeOut(anim15, run_time=3),FadeOut(anim16, run_time=3), FadeOut(anim17, run_time=3),FadeOut(anim18, run_time=3))
        self.wait(10)