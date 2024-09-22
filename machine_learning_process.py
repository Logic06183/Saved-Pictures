from manim import *

class MachineLearningProcess(Scene):
    def construct(self):
        # Positions for elements
        raw_data_pos = LEFT * 6
        preprocessing_pos = LEFT * 3
        training_data_pos = ORIGIN
        model_pos = RIGHT * 3
        evaluation_pos = RIGHT * 6

        # Raw Data representation
        raw_data_points = [Square(side_length=0.2, color=RED).move_to(raw_data_pos + UP * i * 0.3) for i in range(-7, 8)]
        raw_data_group = VGroup(*raw_data_points)
        raw_data_label = Text("Raw Data", color=RED).scale(0.5).next_to(raw_data_group, DOWN)

        # Preprocessing representation
        preprocessing_box = Rectangle(width=2, height=2, color=PURPLE).move_to(preprocessing_pos)
        preprocessing_text = Text("Preprocessing", color=PURPLE).scale(0.6).move_to(preprocessing_box.get_center())

        # Training Data representation
        data_points = [Dot(point=training_data_pos + UP * i * 0.4, color=BLUE) for i in range(-5, 6)]
        data_group = VGroup(*data_points)
        data_label = Text("Training Data", color=BLUE).scale(0.5).next_to(data_group, DOWN)

        # Model representation
        model_rect = Rectangle(width=2, height=2, color=GREEN).move_to(model_pos)
        model_text = Text("ML Model", color=GREEN).scale(0.7).move_to(model_rect.get_center())

        # Evaluation representation
        evaluation_box = Rectangle(width=2, height=2, color=ORANGE).move_to(evaluation_pos)
        evaluation_text = Text("Evaluation", color=ORANGE).scale(0.6).move_to(evaluation_box.get_center())

        # Performance metrics
        metrics_text = Text("Accuracy: 85%", color=ORANGE).scale(0.5).next_to(evaluation_box, DOWN)

        # Arrows between elements
        arrow1 = Arrow(raw_data_group.get_right(), preprocessing_box.get_left(), buff=0.1)
        arrow2 = Arrow(preprocessing_box.get_right(), data_group.get_left(), buff=0.1)
        arrow3 = Arrow(data_group.get_right(), model_rect.get_left(), buff=0.1)
        arrow4 = Arrow(model_rect.get_right(), evaluation_box.get_left(), buff=0.1)
        feedback_arrow = CurvedArrow(evaluation_box.get_top(), model_rect.get_top(), angle=PI/2, color=YELLOW)

        # Animations
        self.play(FadeIn(raw_data_group), FadeIn(raw_data_label))
        self.wait(1)
        self.play(Create(arrow1))
        self.play(FadeIn(preprocessing_box), FadeIn(preprocessing_text))
        self.wait(1)
        self.play(Create(arrow2))
        self.play(FadeIn(data_group), FadeIn(data_label))
        self.wait(1)
        self.play(Create(arrow3))
        self.play(FadeIn(model_rect), FadeIn(model_text))
        self.wait(1)
        
        # Simulate training iterations
        training_epochs = 3
        for epoch in range(training_epochs):
            self.play(Indicate(model_rect, color=GREEN, scale_factor=1.05))
            self.wait(0.5)

        self.play(Create(arrow4))
        self.play(FadeIn(evaluation_box), FadeIn(evaluation_text))
        self.wait(1)
        self.play(FadeIn(metrics_text))
        self.wait(1)
        
        # Feedback loop
        self.play(Create(feedback_arrow))
        self.wait(1)
        self.play(Indicate(model_rect, color=GREEN, scale_factor=1.05))
        new_metrics_text = Text("Accuracy: 90%", color=ORANGE).scale(0.5).next_to(evaluation_box, DOWN)
        self.play(Transform(metrics_text, new_metrics_text))
        self.wait(2)



