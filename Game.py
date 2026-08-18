import turtle
import time
import random

# -----------------------------
# Screen Setup
# -----------------------------
screen = turtle.Screen()
screen.title("🐍 Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# -----------------------------
# Snake Head
# -----------------------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# -----------------------------
# Food
# -----------------------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# -----------------------------
# Snake Body
# -----------------------------
segments = []

# -----------------------------
# Score
# -----------------------------
score = 0
high_score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

score_display.write(
    "Score: 0    High Score: 0",
    align="center",
    font=("Arial", 18, "bold")
)

# -----------------------------
# Game Over Message
# -----------------------------
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()

# -----------------------------
# Movement Functions
# -----------------------------
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    elif head.direction == "down":
        head.sety(head.ycor() - 20)

    elif head.direction == "left":
        head.setx(head.xcor() - 20)

    elif head.direction == "right":
        head.setx(head.xcor() + 20)


# -----------------------------
# Restart Game
# -----------------------------
def restart_game():
    global score

    # Remove old snake body
    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    # Reset snake
    head.goto(0, 0)
    head.direction = "stop"

    # Reset score
    score = 0

    # Remove game over message
    game_over_display.clear()

    # Update score
    score_display.clear()
    score_display.write(
        "Score: 0    High Score: " + str(high_score),
        align="center",
        font=("Arial", 18, "bold")
    )


# -----------------------------
# Exit Game
# -----------------------------
def exit_game():
    screen.bye()


# -----------------------------
# Keyboard Controls
# -----------------------------
screen.listen()

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# WASD Controls
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Restart and Exit
screen.onkeypress(restart_game, "r")
screen.onkeypress(exit_game, "q")


# -----------------------------
# Main Game Loop
# -----------------------------
while True:

    screen.update()

    # -------------------------
    # Boundary Collision
    # -------------------------
    if (
        head.xcor() > 290
