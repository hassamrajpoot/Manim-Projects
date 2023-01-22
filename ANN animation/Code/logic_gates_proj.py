from manim import *
from manim.utils.color import Colors
class NandGate(VMobject):
    def __init__(self, *args, **kwargs):
        self.top_arc = Arc(radius=1, start_angle=0, angle=PI)
        self.left_line = Line(start=[-1,0,0], end=[-1,-2,0])
        self.right_line = Line(start=[1,0,0], end=[1,-2,0])
        self.bottom_line = Line(start=[-1,-2,0], end=[1,-2,0])
        self.top_circle = Circle(radius=0.2, color=WHITE)
        self.top_circle.next_to(self.top_arc, UP,buff=0)
        self.left_nand_conn = Line(start=[-0.5,-2,0], end=[-0.5,-4,0])
        self.right_nand_conn = Line(start=[0.5,-2,0], end=[0.5,-4,0])
        super().__init__(*args, **kwargs)
        self.add(self.top_arc, self.top_circle, self.left_line, self.right_line, self.bottom_line, self.left_nand_conn, self.right_nand_conn)
    def left_nand_connection(self):
        return self.left_nand_conn
    def right_nand_connection(self):
        return self.right_nand_conn
    def top_circle_conn(self):
        return self.top_circle
class NandGateWithConnections(VMobject):
    def __init__(self, *args, **kwargs):
        self.top_arc = Arc(radius=1, start_angle=0, angle=PI)
        self.left_line = Line(start=[-1,0,0], end=[-1,-2,0])
        self.right_line = Line(start=[1,0,0], end=[1,-2,0])
        self.bottom_line = Line(start=[-1,-2,0], end=[1,-2,0])
        self.top_circle = Circle(radius=0.2, color=WHITE)
        self.top_circle.next_to(self.top_arc, UP,buff=0)
        self.left_connection = VMobject().set_points_as_corners([[-0.5,-2,0],[-0.5, -4, 0], [-4,-4,0],[-4, -7, 0]])
        self.right_connection = VMobject().set_points_as_corners([[0.5,-2,0],[0.5, -4, 0], [4,-4,0],[4, -7, 0]])
        super().__init__(*args, **kwargs)
        self.add(self.top_arc, self.top_circle, self.left_line, self.right_line, self.bottom_line, self.left_connection, self.right_connection)
    def left_nand_connection(self):
        return self.left_connection
    def right_nand_connection(self):
        return self.right_connection
    def top_circle_conn(self):
        return self.top_circle
    def left_conn_end_point(self):
        return self.left_connection.get_last_point()
    def right_conn_end_point(self):
        return self.right_connection.get_last_point()
class LeftConnection(VMobject):
    def __init__(self, *args, **kwargs):
        self.left_conn_horizontal_line = Line(start=[-0.5,-4,0], end=[-4,-4,0])
        self.left_conn_verticle_line = Line(start=[-4,-4,0],end=[-4,-7,0])
        super().__init__(*args, **kwargs)
        self.add(self.left_conn_horizontal_line,self.left_conn_verticle_line)
    def left_horiz_line(self):
        return self.left_conn_horizontal_line
    def left_ver_line(self):
        return self.left_conn_verticle_line
class RightConnection(VMobject):
    def __init__(self, *args, **kwargs):
        self.right_conn_horizontal_line = Line(start=[0.5,-4,0], end=[4,-4,0])
        self.right_conn_verticle_line = Line(start=[4,-4,0],end=[4,-7,0])
        super().__init__(*args, **kwargs)
        self.add(self.right_conn_horizontal_line,self.right_conn_verticle_line)
    def right_horiz_line(self):
        return self.right_conn_horizontal_line
    def right_ver_line(self):
        return self.right_conn_verticle_line
class Arrow(VMobject):
    def __init__(self, *args,**kwargs):
        self.left_line = Line(start=[-0.4,0,0], end=[-0.4,3,0], stroke_width=2)
        self.right_line = Line(start=[0.4,0,0], end=[0.4,3,0], stroke_width=2)
        self.left_hor_line = Line(start=[-0.4,0,0], end=[-1,0,0], stroke_width=2)
        self.right_hor_line = Line(start=[0.4,0,0], end=[1,0,0], stroke_width=2)
        self.left_tilted_line = Line(start=[-1,0,0], end=[0,-2,0], stroke_width=2)
        self.right_tilted_line = Line(start=[1,0,0], end=[0,-2,0], stroke_width=2)
        super().__init__(*args,**kwargs)
        self.add(self.left_line,self.right_line,self.left_hor_line, self.right_hor_line, self.left_tilted_line, self.right_tilted_line)
class Gates(Scene):
    def construct(self):
        A = NandGate()
        B = NandGate()
        top_nand = NandGateWithConnections()
        left_connection = top_nand.left_nand_connection()
        right_connection = top_nand.right_nand_connection()
        top_line = Line(start=[0,0,0], end=[0,2,0]).next_to(top_nand.top_circle_conn(), UP, buff=0)
        A_nand_B = VGroup(top_line,top_nand, A.next_to(top_nand.left_conn_end_point(), DOWN, buff=0), B.next_to(top_nand.right_conn_end_point(),DOWN,buff=0))
        Truth_Table = Table([['0','0','1'],['0','1','1'],['1','0','1'],['1','1','0']],col_labels=[Text('A'), Text('B'), Text('A {} B'.format('ɴᴀɴᴅ'))], h_buff=0.3, v_buff=0.2,line_config={"stroke_width": 2, "color": YELLOW}, include_outer_lines=True)
        Truth_Table.remove(*Truth_Table.get_vertical_lines())
        lines = Truth_Table.get_horizontal_lines()
        Truth_Table.remove(*[lines[i] for i in range(2, len(lines))])
        A_nand_B.shift(UP*5 + LEFT*4).scale(0.3)
        self.play(FadeIn(A_nand_B), run_time=3)
        self.play(FadeIn(Truth_Table), run_time=3)
        self.play(Truth_Table.animate(rate_func =rate_functions.ease_in_out_sine).scale(0.7).shift(RIGHT*3), run_time=0.5)
        zero = Text('0').scale(0.5)
        one = Text('1').scale(0.5)
        text_A = Text('A').scale(0.5)
        text_B = Text('B').scale(0.5)
        small_part = Line(start=[-2,2,0], end=[-1,2,0])
        large_part = Line(start=[-1,2,0], end=[2,2,0])
        top_line_rec = Group(small_part, large_part)
        right_line_rec = Line(start=[2,2,0], end=[2,-2,0])
        left_line_rec = Line(start=[-2,2,0], end=[-2,-2,0])
        bottom_line_rec = Line(start=[-2,-2,0], end=[2,-2,0])
        rec = Group(top_line_rec, right_line_rec,left_line_rec,bottom_line_rec)
        rec.scale(0.6)
        rec.z_index = 0
        self.play(FadeIn(text_A.copy().next_to(A, DOWN*2)),FadeIn(text_B.copy().next_to(B, DOWN*2)))
        self.play(FadeIn(Text('A ɴᴀɴᴅ B ').scale(0.5).next_to(top_nand, RIGHT*4)))
        self.wait(3)
        z1 = zero.copy()
        z2 = zero.copy()
        o1 = one.copy()
        o2 = one.copy()
        
        rect1 = SurroundingRectangle(Truth_Table.get_rows()[2],stroke_width=2).copy().set_color(BLUE_C)
        self.play(FadeIn(rect1, run_time=2))
        self.play(ShowPassingFlash(A.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(A.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.left_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        FadeIn(z1.next_to(A, LEFT)), FadeIn(o1.next_to(B, RIGHT)))
        self.play(ShowPassingFlash(left_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(right_connection.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)) ,
                ShowPassingFlash(top_line.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100),
                FadeIn(o2.next_to(top_nand,RIGHT+UP))
                )
        self.play(FadeIn(rec.set_color(YELLOW_C).move_to(A.get_center())), run_time=3)
        a1 = Arrow().scale(0.1).set_color([YELLOW, Colors.pure_green.value])
        a2 = Arrow().scale(0.1).set_color([YELLOW, Colors.pure_green.value])
        a3 = Arrow().scale(0.1).set_color([YELLOW, Colors.pure_green.value])
        self.play(FadeIn(a1.next_to(z1, UP),run_time=2), FadeIn(a2.rotate(PI).next_to(o1, UP),run_time=2),FadeIn(a3.next_to(o2, DOWN),run_time=2))
        self.wait(2)
        self.play(FadeOut(z1), FadeOut(o1), FadeOut(o2), FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(rect1))
        self.wait(2)
        
        rect2 = SurroundingRectangle(Truth_Table.get_rows()[4],stroke_width=2).copy().set_color(BLUE_C)
        self.play(FadeIn(rect2), run_time=2)
        self.play(ShowPassingFlash(A.left_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(A.right_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.left_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.right_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        FadeIn(o1.next_to(A, LEFT)), FadeIn(o2.next_to(B, RIGHT)))
        self.play(ShowPassingFlash(left_connection.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(right_connection.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)) ,
                ShowPassingFlash(top_line.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100),
                FadeIn(z1.next_to(top_nand,RIGHT+UP))
                )
        self.play(FadeIn(a1.next_to(z1, DOWN),run_time=2), FadeIn(a2.rotate(PI).next_to(o1, UP),run_time=2),FadeIn(a3.rotate(PI).next_to(o2, UP),run_time=2))
        self.wait(2)
        self.play(FadeOut(z1), FadeOut(o1), FadeOut(o2), FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(rect2))
        self.wait(2)
        
        rect3 = SurroundingRectangle(Truth_Table.get_rows()[1],stroke_width=2).copy().set_color(ORANGE)
        self.play(FadeIn(rect3, run_time=2))
        self.play(ShowPassingFlash(A.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(A.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        FadeIn(z1.next_to(A, LEFT)), FadeIn(z2.next_to(B, RIGHT)))
        self.play(ShowPassingFlash(left_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(right_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)) ,
                ShowPassingFlash(top_line.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100),
                FadeIn(o1.next_to(top_nand,RIGHT+UP))
                )
        self.play(FadeIn(a1.next_to(z1, UP),run_time=2), FadeIn(a2.rotate(PI).next_to(z2, UP),run_time=2),FadeIn(a3.rotate(PI).next_to(o1, DOWN),run_time=2))
        self.wait(2)
        self.play(FadeOut(z1), FadeOut(z2), FadeOut(o1), FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(rect3))
        self.wait(2)
        
        rect4 = SurroundingRectangle(Truth_Table.get_rows()[3],stroke_width=2).copy().set_color(ORANGE)
        self.play(FadeIn(rect4, run_time=2))
        self.play(ShowPassingFlash(A.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(A.right_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        FadeIn(o1.next_to(A, LEFT)), FadeIn(z1.next_to(B, RIGHT)))
        self.play(ShowPassingFlash(left_connection.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(right_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)) ,
                ShowPassingFlash(top_line.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100),
                FadeIn(o2.next_to(top_nand,RIGHT+UP))
                )
        self.play(FadeIn(a1.next_to(o1, UP),run_time=2), FadeIn(a2.next_to(z1, UP),run_time=2),FadeIn(a3.next_to(o2, DOWN),run_time=2))
        self.wait(2)
        self.play(FadeOut(o1), FadeOut(o2), FadeOut(z1), FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(rect4))
        self.wait(2)
        
        
        oneorzero = Text('1/0').scale(0.5)
        o_or_z  = oneorzero.copy()
        rect5 = SurroundingRectangle(Truth_Table.get_rows()[1],stroke_width=2).copy().set_color(ORANGE)
        rect6 = SurroundingRectangle(Truth_Table.get_rows()[3],stroke_width=2).copy().set_color(ORANGE)
        self.play(FadeIn(rect5, run_time=2),
                FadeIn(rect6, run_time=2))
        self.play(ShowPassingFlash(A.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(A.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        FadeIn(z1.next_to(A, LEFT)), FadeIn(z2.next_to(B, RIGHT)))
        self.play(ShowPassingFlash(A.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(A.right_nand_connection().copy().set_color(Colors.pure_green.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.left_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        ShowPassingFlash(B.right_nand_connection().copy().set_color(Colors.pure_red.value), run_time=2, time_width=100, rate_func=lambda t: smooth(1-t)),
        z1.animate.become(o1))
        self.remove(z1)
        self.play(ShowPassingFlash(left_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(right_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)) ,
                ShowPassingFlash(top_line.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100),
                FadeIn(o2.next_to(top_nand,RIGHT+UP)),
                FadeIn(o_or_z.next_to(A, LEFT)))
        self.play(ShowPassingFlash(left_connection.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(right_connection.copy().set_color(Colors.pure_green.value), run_time=4, time_width=100, rate_func=lambda t: smooth(1-t)),
                ShowPassingFlash(top_line.copy().set_color(Colors.pure_red.value), run_time=4, time_width=100))
        self.play(FadeIn(a1.next_to(o_or_z, UP),run_time=2), FadeIn(a2.next_to(z2, UP),run_time=2),FadeIn(a3.next_to(o2, DOWN),run_time=2))
        self.wait(2)
        self.play(FadeOut(o_or_z), FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(o2),FadeOut(z2), FadeOut(rect5), FadeOut(rect6))
        self.wait(2)
        anims = []
        for obj in self.mobjects:
            anims.append(obj.animate.scale(0).move_to([0,0,0]))
        self.play(*anims)
        dot = Dot(color=YELLOW).move_to([0,0,0])
        self.play(FadeIn(dot))
        eq1 = Tex("$fA = tfB + \overline{oP}$", color=Colors.pure_green.value).scale(0.8)
        eq2 = Tex("$fB = tFA$", color=Colors.pure_green.value).scale(0.8)
        eq1.move_to(UP*3)
        eq2.next_to(eq1, DOWN)
        eq1.scale(1)
        eq2.scale(1)
        self.play(Transform(dot, VGroup(eq1,eq2)))
        self.play(DrawBorderThenFill(eq1,run_time=2, rate_func=rate_functions.ease_in_out_sine))
        self.play(DrawBorderThenFill(eq2,run_time=2, rate_func=rate_functions.ease_in_out_sine))
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
        self.play(GrowFromCenter(Table_with_headers), color=YELLOW, run_time=1, rate_func=rate_functions.ease_in_out_sine)
        self.wait(1)
        self.play(FadeOut(SurroundingRectangle(for_surrounding_rect, buff=0.1), run_time=2))
        self.play(GrowFromPoint(last_output_wanted_top_feedback_table_with_headers.scale(0.7).move_to(LEFT*5), Truth_Table.get_columns()[1:], color=YELLOW),run_time=1, rate_func=rate_functions.ease_in_out_sine)
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
        self.play(GrowFromPoint(fa_fb_table_with_headers.scale(0.6).move_to(LEFT*1), Truth_Table.get_columns()[0], color=YELLOW),run_time=1, rate_func=rate_functions.ease_in_out_sine)
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
        