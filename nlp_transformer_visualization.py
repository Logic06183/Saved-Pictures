from manim import *

class NLPTransformerVisualization(Scene):
    def construct(self):
        # Title
        title = Text("How NLP Works: Embeddings & Transformers", color=YELLOW).scale(0.8).to_edge(UP)
        self.play(Write(title))

        # Section 1: Embeddings (Word to Vector)
        embedding_title = Text("Word Embeddings", color=GREEN).scale(0.6).to_edge(UP)
        self.play(Write(embedding_title))
        
        # Example words
        words = ["apple", "fruit", "car", "drive"]
        word_texts = VGroup(*[Text(word, color=WHITE).scale(0.6) for word in words]).arrange(DOWN, buff=0.8).shift(LEFT * 4)
        self.play(FadeIn(word_texts))

        # Vectors for each word
        vectors = VGroup(
            *[Text(f"[0.5, 0.1, 0.9, 0.7]", color=BLUE).scale(0.5) for _ in words]
        ).arrange(DOWN, buff=0.8).shift(RIGHT * 1)

        # Arrows from words to vectors
        arrows = VGroup(*[Arrow(word.get_right(), vec.get_left(), buff=0.2) for word, vec in zip(word_texts, vectors)])
        self.play(Create(arrows), FadeIn(vectors))

        # Explain Embeddings
        embedding_explanation = Text(
            "Words are converted into\nhigh-dimensional vectors\nfor machine learning models.",
            color=WHITE
        ).scale(0.5).shift(DOWN * 2.5)
        self.play(Write(embedding_explanation))
        self.wait(2)
        
        # Clear embeddings frame
        self.play(FadeOut(word_texts), FadeOut(arrows), FadeOut(vectors), FadeOut(embedding_title), FadeOut(embedding_explanation))
        
        # Section 2: Transformer Architecture
        transformer_title = Text("Transformer Architecture", color=GREEN).scale(0.6).to_edge(UP)
        self.play(Write(transformer_title))

        # Transformer block structure
        encoder_block = Rectangle(width=2.5, height=4, color=PURPLE).shift(LEFT * 2)
        decoder_block = Rectangle(width=2.5, height=4, color=ORANGE).shift(RIGHT * 2)
        
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
        ).scale(0.5).move_to(DOWN * 2.5)
        self.play(Write(attention_detail))
        self.wait(2)

        # Clear transformer frame
        self.play(FadeOut(transformer_title), FadeOut(encoder_block), FadeOut(decoder_block), FadeOut(encoder_text), 
                  FadeOut(decoder_text), FadeOut(attention_mechanism), FadeOut(arrow_enc_dec), FadeOut(attention_detail))

        # Section 3: How ChatGPT Works
        chatgpt_title = Text("How ChatGPT Works", color=GREEN).scale(0.6).to_edge(UP)
        self.play(Write(chatgpt_title))

        # Input and output demonstration
        input_text = Text("Input: 'How does AI work?'", color=WHITE).scale(0.5).shift(LEFT * 3 + UP * 1)
        output_text = Text("Output: 'AI works by learning patterns...'", color=WHITE).scale(0.5).shift(RIGHT * 3 + UP * 1)
        input_arrow = Arrow(input_text.get_right(), output_text.get_left(), buff=0.2)

        self.play(FadeIn(input_text))
        self.play(Create(input_arrow), FadeIn(output_text))

        # Summary of GPT-3/ChatGPT
        chatgpt_summary = Text(
            "GPT-3/ChatGPT processes the input\nsequence using transformer layers,\nand generates a human-like response.",
            color=WHITE
        ).scale(0.5).shift(DOWN * 2.5)
        self.play(Write(chatgpt_summary))
        self.wait(3)
        
        # Clear the final frame
        self.play(FadeOut(chatgpt_title), FadeOut(input_text), FadeOut(output_text), FadeOut(input_arrow), FadeOut(chatgpt_summary))
