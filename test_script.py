from manim import *

class ComplexScene(Scene):
    def construct(self):
        # Create a title
        title = Text("Manim Animation Test", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create some shapes
        square = Square(side_length=2, color=BLUE).shift(LEFT * 3)
        circle = Circle(radius=1, color=GREEN)
        triangle = Triangle(color=RED).shift(RIGHT * 3)

        # Display shapes on screen
        self.play(Create(square), Create(circle), Create(triangle))
        self.wait(1)

        # Animate transformations between shapes
        self.play(Transform(square, circle), Transform(triangle, square))
        self.wait(1)

        # Create and show some text
        explanation = Text("Transformations in Manim", font_size=36).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(1)

        # Apply color change and rotation
        self.play(square.animate.set_color(ORANGE), triangle.animate.rotate(PI / 2))
        self.wait(1)

        # Show scaling animation
        self.play(circle.animate.scale(1.5), triangle.animate.scale(0.5))
        self.wait(1)

        # Create a fading out animation for all elements
        self.play(FadeOut(square), FadeOut(circle), FadeOut(triangle), FadeOut(title), FadeOut(explanation))
