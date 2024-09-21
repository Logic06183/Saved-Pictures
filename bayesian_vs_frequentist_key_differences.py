from manim import *

class BayesianVsFrequentistDetailed(Scene):
    def construct(self):
        # Title
        title = Text("Bayesian vs Frequentist Statistics", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create four segments for each of the key points
        segments = VGroup(
            Text("1. Prior Beliefs and Updating", font_size=30).to_edge(LEFT).shift(UP * 2.5),
            Text("2. Interpretation of Probability", font_size=30).to_edge(RIGHT).shift(UP * 2.5),
            Text("3. Hypothesis Testing", font_size=30).to_edge(LEFT).shift(DOWN * 1.5),
            Text("4. Sample Size and Inference", font_size=30).to_edge(RIGHT).shift(DOWN * 1.5)
        )
        
        self.play(FadeIn(segments[0]), FadeIn(segments[1]), FadeIn(segments[2]), FadeIn(segments[3]))
        self.wait(2)

        # Explaining the first segment: Prior Beliefs and Updating
        self.play(segments[0].animate.scale(1.2).set_color(RED))
        prior_belief_text = Text(
            "Bayesian: Incorporates prior beliefs\nand updates with data.",
            font_size=24
        ).next_to(segments[0], DOWN, buff=0.5).align_to(segments[0], LEFT)
        
        self.play(Write(prior_belief_text))
        
        prior_curve = Axes(
            x_range=[0, 10, 1], 
            y_range=[0, 0.5, 0.1], 
            axis_config={"color": WHITE},
            x_length=4,
            y_length=3
        ).shift(DOWN * 1)
        prior_curve_graph = prior_curve.plot(lambda x: 0.3 * (1 / (1 + (x - 5)**2)), color=BLUE)
        posterior_curve_graph = prior_curve.plot(lambda x: 0.3 * (1 / (1 + (x - 6)**2)), color=RED)
        
        self.play(Create(prior_curve), Create(prior_curve_graph))
        self.wait(1)
        self.play(Transform(prior_curve_graph, posterior_curve_graph))
        
        bayesian_update = Text(
            "Updating beliefs: Prior to Posterior",
            font_size=20, color=RED
        ).next_to(prior_curve, DOWN)
        self.play(Write(bayesian_update))
        self.wait(3)

        # Clear prior beliefs visualization
        self.play(FadeOut(prior_curve), FadeOut(prior_curve_graph), FadeOut(bayesian_update), FadeOut(prior_belief_text))
        self.play(segments[0].animate.scale(1/1.2).set_color(WHITE))
        
        # Explaining the second segment: Interpretation of Probability
        self.play(segments[1].animate.scale(1.2).set_color(GREEN))
        interpretation_text = Text(
            "Frequentist: Probability = long-run frequency\nBayesian: Probability = degree of belief",
            font_size=24
        ).next_to(segments[1], DOWN, buff=0.5).align_to(segments[1], LEFT)
        
        self.play(Write(interpretation_text))
        self.wait(3)
        self.play(FadeOut(interpretation_text))
        self.play(segments[1].animate.scale(1/1.2).set_color(WHITE))

        # Explaining the third segment: Hypothesis Testing
        self.play(segments[2].animate.scale(1.2).set_color(PURPLE))
        hypothesis_text = Text(
            "Frequentist: P-values to reject or accept null\nBayesian: Probability of hypothesis given data",
            font_size=24
        ).next_to(segments[2], DOWN, buff=0.5).align_to(segments[2], LEFT)
        
        self.play(Write(hypothesis_text))
        freq_graph = Axes(
            x_range=[0, 5, 1], 
            y_range=[0, 0.4, 0.1], 
            axis_config={"color": WHITE},
            x_length=4,
            y_length=2
        ).shift(DOWN * 1)
        ci = freq_graph.plot(lambda x: 0.35 * (x > 1) * (x < 4), color=GREEN)
        
        self.play(Create(freq_graph), Create(ci))
        self.play(Write(Text("95% CI", font_size=20).next_to(ci, UP)))

        self.wait(3)
        self.play(FadeOut(hypothesis_text), FadeOut(freq_graph), FadeOut(ci))
        self.play(segments[2].animate.scale(1/1.2).set_color(WHITE))

        # Explaining the fourth segment: Sample Size and Inference
        self.play(segments[3].animate.scale(1.2).set_color(YELLOW))
        sample_text = Text(
            "Frequentist: Large sample sizes needed for accuracy\nBayesian: Works with smaller samples using priors",
            font_size=24
        ).next_to(segments[3], DOWN, buff=0.5).align_to(segments[3], LEFT)
        
        self.play(Write(sample_text))
        self.wait(3)
        self.play(FadeOut(sample_text))
        self.play(segments[3].animate.scale(1/1.2).set_color(WHITE))

        # Final summary
        summary = Text("Bayesian vs Frequentist:\nDifferent interpretations and methodologies.", font_size=30, color=WHITE)
        self.play(FadeOut(segments), Write(summary))
        self.wait(3)
        self.play(FadeOut(summary), FadeOut(title))
