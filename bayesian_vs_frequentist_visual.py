from manim import *

class BayesianVsFrequentist(Scene):
    def construct(self):
        # Title
        title = Text("Bayesian vs Frequentist Statistics", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Frequentist Approach Visualization
        freq_title = Text("Frequentist Approach", font_size=36, color=BLUE).to_edge(LEFT).shift(UP * 2.5)
        freq_def = Text(
            "Probability is the long-run frequency of events.\nAssumes fixed but unknown parameters.",
            font_size=24
        ).next_to(freq_title, DOWN).align_to(freq_title, LEFT)

        self.play(Write(freq_title), Write(freq_def))
        self.wait(2)

        # Showing the confidence interval (95% CI)
        freq_interval = Line(start=LEFT, end=RIGHT, color=GREEN).scale(2).shift(UP * 0.5 + RIGHT * 0.5)
        freq_point = Dot(freq_interval.get_center(), color=RED, radius=0.1)
        ci_text = Text("Confidence Interval", font_size=24, color=GREEN).next_to(freq_interval, DOWN)

        self.play(Create(freq_interval), FadeIn(freq_point), Write(ci_text))
        self.wait(2)

        freq_explanation = Text(
            "Frequentist: Estimates fixed parameter values\n(e.g., proportion of heads in coin toss)", 
            font_size=20
        ).next_to(ci_text, DOWN, buff=0.3)
        self.play(Write(freq_explanation))
        self.wait(3)

        # Clear Frequentist elements
        self.play(FadeOut(freq_title), FadeOut(freq_def), FadeOut(freq_interval), FadeOut(freq_point), FadeOut(ci_text), FadeOut(freq_explanation))

        # Bayesian Approach Visualization
        bayes_title = Text("Bayesian Approach", font_size=36, color=GREEN).to_edge(RIGHT).shift(UP * 2.5)
        bayes_def = Text(
            "Probability is a measure of belief or certainty.\nParameters are updated as data is observed.",
            font_size=24
        ).next_to(bayes_title, DOWN).align_to(bayes_title, LEFT)

        self.play(Write(bayes_title), Write(bayes_def))
        self.wait(2)

        # Visualizing Bayesian Prior
        prior_distribution = axes = Axes(
            x_range=[0, 10, 1], 
            y_range=[0, 0.5, 0.1], 
            axis_config={"color": WHITE},
            x_length=4,
            y_length=3
        ).shift(LEFT * 3 + DOWN)
        prior_curve = prior_distribution.plot(lambda x: 0.3 * (1 / (1 + (x - 5)**2)), color=BLUE)
        prior_label = Text("Prior Belief", font_size=24, color=BLUE).next_to(prior_distribution, UP)

        self.play(Create(prior_distribution), Create(prior_curve), Write(prior_label))
        self.wait(2)

        # Visualizing Bayesian Posterior after observing data
        posterior_distribution = Axes(
            x_range=[0, 10, 1], 
            y_range=[0, 0.5, 0.1], 
            axis_config={"color": WHITE},
            x_length=4,
            y_length=3
        ).shift(RIGHT * 3 + DOWN)
        posterior_curve = posterior_distribution.plot(lambda x: 0.3 * (1 / (1 + (x - 6)**2)), color=RED)
        posterior_label = Text("Posterior Belief", font_size=24, color=RED).next_to(posterior_distribution, UP)

        self.play(Create(posterior_distribution), Create(posterior_curve), Write(posterior_label))
        self.wait(2)

        bayes_explanation = Text(
            "Bayesian: Updates beliefs using prior\nknowledge and observed data",
            font_size=20
        ).to_edge(DOWN)
        self.play(Write(bayes_explanation))
        self.wait(3)

        # Clear Bayesian elements
        self.play(FadeOut(bayes_title), FadeOut(bayes_def), FadeOut(prior_distribution), FadeOut(prior_curve), FadeOut(prior_label), 
                  FadeOut(posterior_distribution), FadeOut(posterior_curve), FadeOut(posterior_label), FadeOut(bayes_explanation))

        # Comparison Visualization
        comparison_title = Text("Comparison", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(comparison_title))

        comparison_text = Text(
            "Frequentist:\n- Fixed parameters\n- Probability = long-run frequency\n\n"
            "Bayesian:\n- Parameters are random\n- Probability = degree of belief",
            font_size=24
        ).next_to(comparison_title, DOWN)

        self.play(Write(comparison_text))
        self.wait(4)

        # Clean up scene
        self.play(FadeOut(title), FadeOut(comparison_title), FadeOut(comparison_text))
