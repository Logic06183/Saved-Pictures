from manim import *

class TestScene(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(radius=1, color=BLUE)
        
        # Display the circle on screen
        self.play(Create(circle))
        self.wait(1)

        # Animate the circle growing
        self.play(circle.animate.scale(2))
        self.wait(1)

        # Animate the circle shrinking
        self.play(circle.animate.scale(0.5))
        self.wait(1)

        # Fade out the circle
        self.play(FadeOut(circle))
