from turtle import Turtle

class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.l_score = 0
		self.r_score = 0
		self.update_scoreboard()
		
	def update_scoreboard(self):
		self.clear()
		self.goto(0, 200)
		result_text = f"{self.l_score}  :  {self.r_score}"
		self.write(result_text, align="center", font=("Courier", 60, "normal"))
	def l_point(self):
		self.l_score += 1
		self.update_scoreboard()
		
	def r_point(self):
		self.r_score += 1
		self.update_scoreboard()
		