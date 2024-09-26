from manim import *

class AIDiagram(Scene):
    def construct(self):
        # Set the background color
        self.camera.background_color = "#F0F8FF"  # Light blue background

        # Colors for the boxes and text
        box_color = "#E5E5E5"  # Light grey fill for the boxes
        text_color = BLACK     # Text color

        # Creating the boxes and texts
        ai_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        ai_text = Text("Artificial Intelligence", color=text_color).scale(0.6)
        ai_group = VGroup(ai_box, ai_text).move_to(LEFT * 4 + UP * 3.5)  # Moved up further

        asi_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        asi_text = Text("Artificial Super Intelligence", color=text_color).scale(0.5)
        asi_group = VGroup(asi_box, asi_text).next_to(ai_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        agi_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        agi_text = Text("Artificial General Intelligence", color=text_color).scale(0.5)
        agi_group = VGroup(agi_box, agi_text).next_to(asi_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        ani_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        ani_text = Text("Artificial Narrow Intelligence", color=text_color).scale(0.5)
        ani_group = VGroup(ani_box, ani_text).next_to(agi_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        ml_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        ml_text = Text("Machine Learning", color=text_color).scale(0.6)
        ml_group = VGroup(ml_box, ml_text).next_to(ani_group, RIGHT, buff=0.8)  # Reduced horizontal spacing

        supervised_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        supervised_text = Text("Supervised Learning", color=text_color).scale(0.5)
        supervised_group = VGroup(supervised_box, supervised_text).next_to(ml_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        semi_supervised_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        semi_supervised_text = Text("Semi-supervised Learning", color=text_color).scale(0.5)
        semi_supervised_group = VGroup(semi_supervised_box, semi_supervised_text).next_to(supervised_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        unsupervised_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        unsupervised_text = Text("Unsupervised Learning", color=text_color).scale(0.5)
        unsupervised_group = VGroup(unsupervised_box, unsupervised_text).next_to(semi_supervised_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        reinforcement_box = RoundedRectangle(corner_radius=0.2, width=4, height=1.2, color=text_color, fill_color=box_color, fill_opacity=1)
        reinforcement_text = Text("Reinforcement Learning", color=text_color).scale(0.5)
        reinforcement_group = VGroup(reinforcement_box, reinforcement_text).next_to(unsupervised_group, DOWN, buff=0.2, aligned_edge=LEFT)  # Reduced buff

        # Creating all the lines
        lines = VGroup(
            Line(ai_group.get_bottom(), asi_group.get_top(), color=text_color),
            Line(asi_group.get_bottom(), agi_group.get_top(), color=text_color),
            Line(agi_group.get_bottom(), ani_group.get_top(), color=text_color),
            Line(ani_group.get_right(), ml_group.get_left(), color=text_color),
            Line(ml_group.get_bottom(), supervised_group.get_top(), color=text_color),
            Line(supervised_group.get_bottom(), semi_supervised_group.get_top(), color=text_color),
            Line(semi_supervised_group.get_bottom(), unsupervised_group.get_top(), color=text_color),
            Line(unsupervised_group.get_bottom(), reinforcement_group.get_top(), color=text_color),
        )
        
        # Grouping all elements for easy animation
        all_elements = [
            ai_group,
            asi_group,
            agi_group,
            ani_group,
            ml_group,
            supervised_group,
            semi_supervised_group,
            unsupervised_group,
            reinforcement_group
        ]

        # Displaying elements one by one over 30 seconds
        duration_per_element = 30 / len(all_elements)
        
        for element in all_elements:
            self.play(FadeIn(element), run_time=duration_per_element)
        
        # Display lines
        self.play(Create(lines), run_time=5)

        self.wait(2)
