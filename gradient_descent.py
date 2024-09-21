from manim import *

class GradientDescent(Scene):
    def construct(self):
        # Axes setup
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 16, 4],
            axis_config={"color": WHITE},
            x_length=8,
            y_length=6
        ).to_edge(DOWN)

        # Labels for axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("Cost(x)")
        
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Defining the quadratic function: y = x^2
        def cost_function(x):
            return x**2

        # Graph of the function
        graph = axes.plot(cost_function, color=BLUE, x_range=[-4, 4])
        graph_label = axes.get_graph_label(graph, label="x^2", x_val=3, direction=UP)

        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # Initial point for Gradient Descent
        initial_x = 3  # Starting point for gradient descent
        learning_rate = 0.2  # Learning rate
        point = Dot(axes.c2p(initial_x, cost_function(initial_x)), color=RED)
        self.play(FadeIn(point))
        
        # Number of iterations for gradient descent
        iterations = 20
        for _ in range(iterations):
            # Calculate gradient: derivative of x^2 is 2x
            grad = 2 * initial_x
            
            # Update x using gradient descent formula: x = x - learning_rate * grad
            new_x = initial_x - learning_rate * grad
            
            # Animate the movement of the point to the new position
            self.play(point.animate.move_to(axes.c2p(new_x, cost_function(new_x))), run_time=0.5)
            initial_x = new_x

        # Show final position
        final_label = Text("Converged to Minimum", font_size=24, color=YELLOW).next_to(point, RIGHT)
        self.play(Write(final_label))
        self.wait(2)

        # Clean up
        self.play(FadeOut(point), FadeOut(graph), FadeOut(graph_label), FadeOut(final_label), FadeOut(axes), FadeOut(x_label), FadeOut(y_label))
