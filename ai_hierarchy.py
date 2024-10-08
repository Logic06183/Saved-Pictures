from manim import *

class NLPTransformerVisualization(Scene):
    def construct(self):
        # Title
        title = Text("How NLP Works: Embeddings & Transformers", color=YELLOW).scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Section 1: Embeddings (Word to Vector)
        embedding_title = Text("Word Embeddings", color=GREEN).scale(0.6).to_edge(LEFT + UP)
        self.play(Write(embedding_title))
        
        # Example words
        words = ["apple", "fruit", "car", "drive"]
        word_texts = VGroup(*[Text(word, color=WHITE).scale(0.6) for word in words]).arrange(DOWN, buff=0.8).shift(LEFT * 5)
        self.play(FadeIn(word_texts))

        # Vectors for each word
        vectors = VGroup(
            *[Text(f"[0.5, 0.1, 0.9, 0.7]", color=BLUE).scale(0.5) for _ in words]
        ).arrange(DOWN, buff=0.8).shift(LEFT * 2)

        # Arrows from words to vectors
        arrows = VGroup(*[Arrow(word.get_right(), vec.get_left(), buff=0.2) for word, vec in zip(word_texts, vectors)])
        self.play(Create(arrows), FadeIn(vectors))

        # Explain Embeddings
        embedding_explanation = Text(
            "Words are converted into\nhigh-dimensional vectors\nfor machine learning models.",
            color=WHITE
        ).scale(0.5).shift(DOWN * 3)
        self.play(Write(embedding_explanation))
        self.wait(2)

        # Section 2: Transformer Architecture
        transformer_title = Text("Transformer Architecture", color=GREEN).scale(0.6).to_edge(LEFT + UP)
        self.play(Transform(embedding_title, transformer_title))

        # Transformer block structure
        encoder_block = Rectangle(width=2.5, height=4, color=PURPLE).shift(RIGHT * 1 + UP * 1)
        decoder_block = Rectangle(width=2.5, height=4, color=ORANGE).shift(RIGHT * 5 + UP * 1)
        
        encoder_text = Text("Encoder", color=WHITE).scale(0.5).move_to(encoder_block.get_top() + DOWN * 0.4)
        decoder_text = Text("Decoder", color=WHITE).scale(0.5).move_to(decoder_block.get_top() + DOWN * 0.4)

        # Self-attention inside encoder
        attention_mechanism = Text("Self-Attention", color=BLUE).scale(0.5).move_to(encoder_block.get_center())

        # Arrows between encoder and decoder
        arrow_enc_dec = Arrow(encoder_block.get_right(), decoder_block.get_left(), buff=0.2)
        self.play(FadeIn(encoder_block), FadeIn(decoder_block))
        self.play(Write(encoder_text), Write(decoder_text))
        self.play(Write(attention_mechanism), Create(arrow_enc_dec))

        # Display attention mechanism explanation
        attention_detail = Text(
            "Self-attention helps the model focus\non important parts of the input sequence.",
            color=WHITE
        ).scale(0.5).move_to(attention_mechanism.get_bottom() + DOWN * 1.2)
        self.play(Write(attention_detail))
        self.wait(2)

        # Section 3: How ChatGPT Works (Full Transformer Flow)
        full_flow_title = Text("How ChatGPT Works", color=GREEN).scale(0.6).to_edge(LEFT + UP)
        self.play(Transform(embedding_title, full_flow_title))

        # Input to model
        input_text = Text("Input: 'How does AI work?'", color=WHITE).scale(0.5).move_to(LEFT * 4 + DOWN * 1)
        output_text = Text("Output: 'AI works by learning patterns...'", color=WHITE).scale(0.5).move_to(RIGHT * 4 + DOWN * 1)
        input_arrow = Arrow(input_text.get_right(), encoder_block.get_left(), buff=0.2)
        output_arrow = Arrow(decoder_block.get_right(), output_text.get_left(), buff=0.2)

        self.play(FadeIn(input_text), Create(input_arrow))
        self.play(FadeIn(output_text), Create(output_arrow))

        # Summary of GPT-3/ChatGPT
        chatgpt_summary = Text(
            "GPT-3/ChatGPT processes the input\nsequence using transformer layers,\nand generates a human-like response.",
            color=WHITE
        ).scale(0.5).shift(DOWN * 3)
        self.play(Write(chatgpt_summary))
        self.wait(3)
