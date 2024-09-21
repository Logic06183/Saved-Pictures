from manim import *

class MachineLearningIntro(Scene):
    def construct(self):
        # Title
        title = Text("How Machine Learning Works", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Axes setup
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 5],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4,
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label("Feature (X)", edge=RIGHT, direction=DOWN, buff=0.4)
        y_label = axes.get_y_axis_label("Target (Y)", edge=UP, direction=LEFT, buff=0.4)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(1)

        # Sample data points
        data_points = [
            axes.c2p(1, 3), axes.c2p(2, 4), axes.c2p(3, 6), axes.c2p(4, 8),
            axes.c2p(5, 10), axes.c2p(6, 11), axes.c2p(7, 14), axes.c2p(8, 15),
            axes.c2p(9, 17)
        ]
        dots = VGroup(*[Dot(point, color=BLUE) for point in data_points])
        self.play(FadeIn(dots))
        self.wait(1)

        # Introduce a line and explain linear regression
        initial_line = axes.plot(lambda x: 1 * x + 1, x_range=[0, 10], color=RED)
        line_label = MathTex("Y = WX + b", font_size=36).next_to(initial_line, UP)
        self.play(Create(initial_line), Write(line_label))
        self.wait(2)

        # Explain the process of training (gradient descent) to minimize error
        training_text = Text("Training: Adjusting W and b to fit the line", font_size=24).to_edge(DOWN)
        self.play(Write(training_text))

        # Simulate the line gradually fitting the data points
        updated_line = axes.plot(lambda x: 1.7 * x + 0.5, x_range=[0, 10], color=GREEN)
        self.play(Transform(initial_line, updated_line), run_time=3)
        self.wait(1)

        # Show the final best-fit line
        best_fit_line = axes.plot(lambda x: 1.9 * x + 0.1, x_range=[0, 10], color=YELLOW)
        final_label = Text("Best-Fit Line", font_size=24).next_to(best_fit_line, UP)
        self.play(Transform(initial_line, best_fit_line), FadeOut(line_label), Write(final_label))
        self.wait(2)

        # Highlight the idea of minimizing error
        error_label = Text("Minimizing Error", font_size=36, color=RED).to_edge(DOWN)
        self.play(Write(error_label))
        self.wait(2)

        # Clean up the scene
        self.play(FadeOut(title), FadeOut(training_text), FadeOut(dots), FadeOut(initial_line), FadeOut(final_label), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(error_label))

        # End message
        end_text = Text("This is the core of Machine Learning!", font_size=40, color=YELLOW)
        self.play(Write(end_text))
        self.wait(3)
