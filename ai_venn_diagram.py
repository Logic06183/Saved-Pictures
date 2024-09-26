from manim import *

class AIVennDiagram(Scene):
    def construct(self):
        # Define colors for each type of AI
        asi_color = BLUE_E  # Color for ASI
        agi_color = GREEN_E  # Color for AGI
        ani_color = RED_E  # Color for ANI
        
        # Create the circles with different radii to represent the nested structure
        asi_circle = Circle(radius=3, color=asi_color, fill_opacity=0.2, fill_color=asi_color).shift(LEFT * 2.5 + UP * 1.5)
        agi_circle = Circle(radius=2, color=agi_color, fill_opacity=0.2, fill_color=agi_color).shift(LEFT * 2 + UP * 0.5)
        ani_circle = Circle(radius=1, color=ani_color, fill_opacity=0.2, fill_color=ani_color).shift(LEFT * 1.5)

        # Add text labels for each AI type
        asi_label = Text("Artificial Super Intelligence (ASI)", color=asi_color).scale(0.4).next_to(asi_circle, UP)
        agi_label = Text("Artificial General Intelligence (AGI)", color=agi_color).scale(0.4).next_to(agi_circle, RIGHT)
        ani_label = Text("Artificial Narrow Intelligence (ANI)", color=ani_color).scale(0.4).next_to(ani_circle, DOWN)

        # Grouping all elements to make manipulation easier
        venn_diagram = VGroup(asi_circle, agi_circle, ani_circle, asi_label, agi_label, ani_label)
        
        # Animating the creation of the Venn diagram
        self.play(Create(asi_circle), Write(asi_label), run_time=2)
        self.play(Create(agi_circle), Write(agi_label), run_time=2)
        self.play(Create(ani_circle), Write(ani_label), run_time=2)

        self.wait(2)
