from manim import *

class AITimeline(Scene):
    def construct(self):
        # Timeline base
        timeline = Line(LEFT * 6, RIGHT * 6)

        # Milestone data
        milestones = [
            {"year": "1956", "event": "AI Term Coined", "pos": LEFT * 5},
            {"year": "1997", "event": "Deep Blue", "pos": LEFT * 2},
            {"year": "2011", "event": "Siri Launch", "pos": RIGHT * 1},
            {"year": "2020", "event": "GPT-3 Released", "pos": RIGHT * 4},
        ]

        # Draw timeline
        self.play(Create(timeline))
        self.wait(1)

        # Add milestones
        for milestone in milestones:
            dot = Dot(point=milestone["pos"])
            year = Text(milestone["year"]).scale(0.6).next_to(dot, DOWN)
            event = Text(milestone["event"]).scale(0.5).next_to(year, DOWN)
            self.play(FadeIn(dot), Write(year), Write(event))
            self.wait(1)

        self.wait(2)
