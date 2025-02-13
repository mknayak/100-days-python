from turtle import Screen

class PongScreen(Screen):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.bgcolor("black")
        self.tracer(0)
        self.setup(1200, 700)