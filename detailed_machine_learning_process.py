from manim import *

class MachineLearningProcess(Scene):
    def construct(self):
        # Positions for elements
        raw_data_pos = LEFT * 6
        preprocessing_pos = LEFT * 3
        training_data_pos = ORIGIN
        model_pos = RIGHT * 3
        evaluation_pos = RIGHT * 6

        # 1. Raw Data Representation (Feature and Target)
        raw_data_points = [
            VGroup(
                Square(side_length=0.2, color=RED).move_to(raw_data_pos + UP * i * 0.3 + LEFT * 0.2),
                Square(side_length=0.2, color=BLUE).move_to(raw_data_pos + UP * i * 0.3 + RIGHT * 0.2)
            )
            for i in range(-7, 8)
        ]
        raw_data_group = VGroup(*[VGroup(point[0], point[1]) for point in raw_data_points])
        raw_data_label = Text("Raw Data (Features & Targets)", color=WHITE).scale(0.5).next_to(raw_data_group, DOWN)

        # 2. Preprocessing Representation
        preprocessing_box = Rectangle(width=2, height=2, color=PURPLE).move_to(preprocessing_pos)
        preprocessing_text = Text("Preprocessing", color=PURPLE).scale(0.6).move_to(preprocessing_box.get_center())

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
        data_label = Text("Training Data", color=GREEN).scale(0.5).next_to(training_data_group, DOWN)
        validation_label = Text("Validation Data", color=ORANGE).scale(0.5).next_to(validation_data_group, DOWN)

        # 4. Model Representation (Linear Regression)
        model_rect = Rectangle(width=2, height=2, color=BLUE).move_to(model_pos)
        model_text = Text("Linear Regression Model", color=BLUE).scale(0.6).move_to(model_rect.get_center())

        # 5. Evaluation Representation
        evaluation_box = Rectangle(width=2, height=2, color=YELLOW).move_to(evaluation_pos)
        evaluation_text = Text("Evaluation", color=YELLOW).scale(0.6).move_to(evaluation_box.get_center())
        metrics_text = Text("MSE: ?", color=YELLOW).scale(0.5).next_to(evaluation_box, DOWN)

        # 6. Arrows Between Elements
        arrow1 = Arrow(raw_data_group.get_right(), preprocessing_box.get_left(), buff=0.1)
        arrow2 = Arrow(preprocessing_box.get_right(), training_data_group.get_left(), buff=0.1)
        arrow3 = Arrow(training_data_group.get_right(), model_rect.get_left(), buff=0.1)
        arrow4 = Arrow(model_rect.get_right(), evaluation_box.get_left(), buff=0.1)
        feedback_arrow = CurvedArrow(evaluation_box.get_top(), model_rect.get_top(), angle=PI/2, color=YELLOW)

        # 7. Coordinate Axes for Linear Regression Visualization
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_numbers": False},
        ).shift(DOWN * 2 + RIGHT * 3)

        axes_labels = axes.get_axis_labels(x_label="Feature", y_label="Target")

        # Sample data points
        sample_points = [
            Dot(axes.coords_to_point(x, 0.5 * x + 1 + (np.random.rand() - 0.5)), color=GREEN)
            for x in np.linspace(1, 9, 8)
        ]
        sample_data_group = VGroup(*sample_points)

        # Line of best fit (initial)
        initial_line = axes.get_graph(lambda x: 0.5 * x + 1, color=RED)

        # Line of best fit (after training)
        trained_line = axes.get_graph(lambda x: x + 0.5, color=RED)

        # Animations
        # Step 1: Raw Data
        self.play(FadeIn(raw_data_group), Write(raw_data_label))
        self.wait(1)

        # Step 2: Preprocessing
        self.play(Create(arrow1))
        self.play(FadeIn(preprocessing_box), Write(preprocessing_text))
        self.wait(1)

        # Step 3: Training and Validation Data
        self.play(Create(arrow2))
        self.play(FadeIn(training_data_group), FadeIn(validation_data_group))
        self.play(Write(data_label), Write(validation_label))
        self.wait(1)

        # Step 4: Model Training Visualization
        self.play(Create(arrow3))
        self.play(FadeIn(model_rect), Write(model_text))
        self.wait(1)

        # Show sample data and initial line
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

        # Step 5: Evaluation
        self.play(Create(arrow4))
        self.play(FadeIn(evaluation_box), Write(evaluation_text))
        self.wait(1)

        # Calculate and display metrics (simulated)
        mse_value = Text("MSE: 0.15", color=YELLOW).scale(0.5).next_to(evaluation_box, DOWN)
        self.play(Transform(metrics_text, mse_value))
        self.wait(1)

        # Step 6: Feedback Loop
        self.play(Create(feedback_arrow))
        self.play(Indicate(model_rect, color=BLUE, scale_factor=1.05))
        improved_mse_value = Text("MSE: 0.05", color=YELLOW).scale(0.5).next_to(evaluation_box, DOWN)
        self.play(Transform(metrics_text, improved_mse_value))
        self.wait(2)
