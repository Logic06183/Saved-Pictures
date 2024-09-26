from manim import *
import numpy as np

class MachineLearningProcess(Scene):
    def construct(self):
        # Positions for elements
        raw_data_pos = LEFT * 6
        preprocessing_pos = LEFT * 2.5
        training_data_pos = ORIGIN
        model_pos = RIGHT * 2.25
        evaluation_pos = RIGHT * 5.5

        # 1. Raw Data Representation (Features and Targets)
        raw_data_points = [
            VGroup(
                Square(side_length=0.2, color=RED).move_to(raw_data_pos + UP * i * 0.3 + LEFT * 0.2),
                Square(side_length=0.2, color=BLUE).move_to(raw_data_pos + UP * i * 0.3 + RIGHT * 0.2)
            )
            for i in range(-7, 8)
        ]
        raw_data_group = VGroup(*raw_data_points)
        raw_data_label = Text("Raw Data", color=WHITE).scale(0.4).next_to(raw_data_group, DOWN)

        # 2. Preprocessing Representation
        preprocessing_box = Rectangle(width=2, height=1.5, color=PURPLE).move_to(preprocessing_pos)
        preprocessing_text = Text("Preprocessing", color=PURPLE).scale(0.4).next_to(preprocessing_box, UP)  # Label positioned at the top

        # 3. Training and Validation Data Representation
        training_data_points = [
            Dot(point=training_data_pos + UP * i * 0.3 + LEFT * 0.2, color=GREEN)
            for i in range(-5, 6)
        ]
        validation_data_points = [
            Dot(point=training_data_pos + UP * i * 0.3 + RIGHT * 0.2, color=ORANGE)
            for i in range(-5, 6)
        ]
        training_data_group = VGroup(*training_data_points)
        validation_data_group = VGroup(*validation_data_points)

        # Adjust label positions to be at the top and bottom
        data_label = Text("Training Data", color=GREEN).scale(0.4).next_to(training_data_group, DOWN)  # Positioned below
        validation_label = Text("Validation Data", color=ORANGE).scale(0.4).next_to(validation_data_group, UP)  # Positioned above

        # 4. Model Representation (Linear Regression)
        model_rect = Rectangle(width=2, height=1.5, color=BLUE).move_to(model_pos)
        model_text = Text("Linear Regression Model", color=BLUE).scale(0.4).next_to(model_rect, UP)  # Positioned at the top

        # 5. Evaluation Representation
        evaluation_box = Rectangle(width=2, height=1.5, color=YELLOW).move_to(evaluation_pos)
        evaluation_text = Text("Evaluation", color=YELLOW).scale(0.4).next_to(evaluation_box, UP)  # Positioned at the top
        metrics_text = Text("MSE: ?", color=YELLOW).scale(0.4).next_to(evaluation_box, DOWN)

        # 6. Arrows Between Elements (Create later)
        arrow1 = Arrow(raw_data_group.get_right(), preprocessing_box.get_left(), buff=0.1)
        arrow2 = Arrow(preprocessing_box.get_right(), training_data_group.get_left(), buff=0.1)
        arrow3 = Arrow(validation_data_group.get_right(), model_rect.get_left(), buff=0.1)
        arrow4 = Arrow(model_rect.get_right(), evaluation_box.get_left(), buff=0.1)
        feedback_arrow = CurvedArrow(evaluation_box.get_top(), model_rect.get_top(), angle=PI/2, color=YELLOW)

        # 7. Coordinate Axes for Linear Regression Visualization
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=2,  # Smaller length to fit the graph within the frame
            y_length=2,  # Smaller height to fit the graph within the frame
            axis_config={"include_numbers": False},
        ).shift(DOWN * 3 + RIGHT * 3)  # Adjust position to fit within the screen

        # Adjust the axes labels, making "Feature" into two lines and scaling down the text
        axes_labels = axes.get_axis_labels(x_label="Feature\nValue", y_label="Target").scale(0.6)

        # Sample data points
        sample_points = [
            Dot(axes.coords_to_point(x, 0.5 * x + 1 + (np.random.rand() - 0.5)), color=GREEN)
            for x in np.linspace(1, 9, 8)
        ]
        sample_data_group = VGroup(*sample_points)

        # Line of poor fit (initial)
        initial_line = axes.plot(lambda x: 0.1 * x + 5, color=RED)  # Poor fit initially

        # Line of best fit (after training)
        trained_line = axes.plot(lambda x: 0.5 * x + 1, color=RED)  # Improved fit after training

        # Animations

        # Step 1: Raw Data
        self.play(FadeIn(raw_data_group), Write(raw_data_label))
        self.wait(1)
        self.play(FadeOut(raw_data_group), FadeOut(raw_data_label))

        # Step 2: Preprocessing
        self.play(FadeIn(preprocessing_box), Write(preprocessing_text))
        self.wait(1)
        self.play(FadeOut(preprocessing_box), FadeOut(preprocessing_text))

        # Step 3: Training and Validation Data
        self.play(FadeIn(training_data_group), Write(data_label))
        self.play(FadeIn(validation_data_group), Write(validation_label))
        self.wait(1)
        self.play(FadeOut(training_data_group), FadeOut(data_label))
        self.play(FadeOut(validation_data_group), FadeOut(validation_label))

        # Step 4: Model Training Visualization
        self.play(FadeIn(model_rect), Write(model_text))
        self.wait(1)
        self.play(FadeOut(model_rect), FadeOut(model_text))

        # Step 5: Evaluation
        self.play(FadeIn(evaluation_box), Write(evaluation_text))
        self.wait(1)
        self.play(FadeOut(evaluation_box), FadeOut(evaluation_text))

        # Step 6: Show Full Diagram with Arrows
        # Re-display all elements
        self.play(
            FadeIn(raw_data_group), FadeIn(raw_data_label),
            FadeIn(preprocessing_box), FadeIn(preprocessing_text),
            FadeIn(training_data_group), FadeIn(data_label),
            FadeIn(validation_data_group), FadeIn(validation_label),
            FadeIn(model_rect), FadeIn(model_text),
            FadeIn(evaluation_box), FadeIn(evaluation_text),
            FadeIn(metrics_text)
        )

        # Create arrows
        self.play(Create(arrow1), Create(arrow2), Create(arrow3), Create(arrow4))
        self.play(Create(feedback_arrow))

        # Show sample data and initial line after showing the full diagram
        self.wait(2)  # Wait before showing the graph
        self.play(Write(axes), Write(axes_labels))
        self.play(FadeIn(sample_data_group))
        self.play(Create(initial_line))
        self.wait(1)

        # Simulate training iterations
        training_epochs = 2
        for epoch in range(training_epochs):
            # Indicate model training
            self.play(Indicate(model_rect, color=BLUE, scale_factor=1.05))
            # Update line to simulate learning
            self.play(Transform(initial_line, trained_line))
            self.wait(0.5)

        # Update metrics
        mse_value = Text("MSE: 0.15", color=YELLOW).scale(0.4).next_to(evaluation_box, DOWN)
        self.play(Transform(metrics_text, mse_value))
        self.wait(1)

        # Feedback Loop
        self.play(Indicate(evaluation_box, color=YELLOW, scale_factor=1.05))
        self.play(Indicate(model_rect, color=BLUE, scale_factor=1.05))
        improved_mse_value = Text("MSE: 0.05", color=YELLOW).scale(0.4).next_to(evaluation_box, DOWN)
        self.play(Transform(metrics_text, improved_mse_value))
        self.wait(2)
