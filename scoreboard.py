from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f'Score = {self.score}  High Score = {self.high_score}', align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset_score(self):
        self.high_score = max(self.score, self.high_score)
        self.score = 0
        self.update_score_board()
