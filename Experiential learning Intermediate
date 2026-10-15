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
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

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
# Update Score
# -----------------------------
def update_score():
    score_display.clear()
    score_display.write(
        "Score: {}    High Score: {}".format(score, high_score),
        align="center",
        font=("Arial", 18, "bold")
    )


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

    # Reset food
    food.goto(
        random.randrange(-280, 281, 20),
        random.randrange(-240, 241, 20)
    )

    # Reset score
    score = 0

    # Remove game-over message
    game_over_display.clear()

    # Update score
    update_score()


# -----------------------------
# Exit Game
# -----------------------------
def exit_game():
    screen.bye()


# -----------------------------
# Game Over
# -----------------------------
def game_over():
    global score, high_score

    # Update high score
    if score > high_score:
        high_score = score

    head.direction = "stop"

    game_over_display.clear()
    game_over_display.write(
        "GAME OVER!\n\n"
        "Score: {}\n"
        "High Score: {}\n\n"
        "Press R to Restart\n"
        "Press Q to Exit".format(score, high_score),
        align="center",
        font=("Arial", 18, "bold")
    )

    update_score()


# -----------------------------
# Keyboard Controls
# -----------------------------
screen.listen()

# Arrow Keys
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
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        game_over()

        # Wait until restart or exit
        while head.direction == "stop":
            screen.update()
            time.sleep(0.1)

    # -------------------------
    # Food Collision
    # -------------------------
    if head.distance(food) < 20:

        # Move food to random position
        food.goto(
            random.randrange(-280, 281, 20),
            random.randrange(-240, 241, 20)
        )

        # Create new body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()

        segments.append(new_segment)

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        update_score()

    # -------------------------
    # Move Snake Body
    # -------------------------
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()

        segments[index].goto(x, y)

    # First body segment follows head
    if len(segments) > 0:
        segments[0].goto(
            head.xcor(),
            head.ycor()
        )

    # -------------------------
    # Move Snake Head
    # -------------------------
    move()

    # -------------------------
    # Body Collision
    # -------------------------
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()

            while head.direction == "stop":
                screen.update()
                time.sleep(0.1)

    # -------------------------
    # Game Speed
    # -------------------------
    time.sleep(0.1)

