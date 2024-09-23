from manim import *

class AIHistoryTimeline(Scene):
    def construct(self):
        # Title
        title = Text("The Evolution of AI and Machine Learning", color=YELLOW).scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Timeline Base Line
        timeline = Line(LEFT * 6, RIGHT * 6, color=WHITE)
        self.play(Create(timeline))

        # Major Milestones
        milestones = [
            {"year": "1956", "event": "Birth of AI\n(Dartmouth Conference)", "pos": LEFT * 5, "details": "AI was coined as a field of study."},
            {"year": "1960s", "event": "Expert Systems", "pos": LEFT * 3, "details": "Development of systems like DENDRAL and MYCIN."},
            {"year": "1980s", "event": "Machine Learning Algorithms", "pos": LEFT, "details": "Emergence of neural networks and ML."},
            {"year": "1997", "event": "Deep Blue Beats Kasparov", "pos": RIGHT * 2, "details": "IBM's Deep Blue defeats Garry Kasparov."},
            {"year": "2010s", "event": "Deep Learning Revolution", "pos": RIGHT * 4, "details": "AlexNet, ResNet, and CNNs took center stage."},
            {"year": "2020s", "event": "Foundation Models\n(GPT-3, BERT)", "pos": RIGHT * 6, "details": "Massive language models emerge."},
        ]

        # Display each milestone in separate frames
        for milestone in milestones:
            # Show dot, year, and event for each milestone
            dot = Dot(point=milestone["pos"], color=BLUE)
            year_text = Text(milestone["year"]).scale(0.5).next_to(dot, UP)
            event_text = Text(milestone["event"]).scale(0.4).next_to(dot, DOWN)
            
            # Display milestone
            self.play(FadeIn(dot), Write(year_text))
            self.play(FadeIn(event_text))
            self.wait(1)  # Pause for a moment

            # Show details in a separate frame
            detail_box = Rectangle(width=6, height=2.5, color=WHITE).move_to(DOWN * 2.5)
            detail_text = Text(milestone["details"], color=WHITE).scale(0.4).move_to(detail_box.get_center())
            
            self.play(FadeIn(detail_box), Write(detail_text))
            self.wait(3)  # Allow time for explanation
            
            # Clear the frame before moving to the next milestone
            self.play(FadeOut(dot), FadeOut(year_text), FadeOut(event_text), FadeOut(detail_box), FadeOut(detail_text))
        
        self.wait(2)
