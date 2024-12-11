# import required modules
import turtle
import time
import random

# Import the color themes from the colorThemes.py file
import colorThemes

themesDictionary = {
    "Rainbow": colorThemes.rainbow,
}

# Randomly select a theme (name and color array)
selectedTheme, colorArray = random.choice(list(themesDictionary.items()))
print(f"Selected Theme: {selectedTheme}")

# Initialize difficulty settings
def selectDifficulty():
    difficultyMap = {
        "E": 0.13,
        "M": 0.1,
        "H": 0.07,
        "I": 0.04
    }
    while True:
        difficulty = input("\n(E) Easy\n(M) Medium\n(H) Hard\n(I) Impossible\n\nSelect your difficulty: ").upper()
        if difficulty in difficultyMap:
            print(f"\nDifficulty {difficulty} selected.")
            return difficultyMap[difficulty]
        print("\nInvalid input.")

movementDelay = selectDifficulty()

currentScore = 0

with open("snakeInfo.txt", "r") as file:
    highScore = int(file.readline())

# Initialize turtle settings
turtle.colormode(255)
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor(10, 20, 10)
wn.setup(width=600, height=800)
wn.tracer(0)

snakeHead = turtle.Turtle()
snakeHead.shape("square")
snakeHead.color("white")
snakeHead.penup()
snakeHead.goto(0, 0)
snakeHead.direction = "Stop"

food = turtle.Turtle()
food.speed(0)
food.shape(random.choice(["circle"]))
food.color(colorArray[0])
food.penup()
food.goto(0, 100)

scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.shape("square")
scorePen.color("white")
scorePen.penup()
scorePen.hideturtle()
scorePen.goto(0, 250)
scorePen.write(f"Score : 0  High Score : {highScore}", align="center", font=("arial", 24, "bold"))

snakeSegments = []
snakeLength = 1

# Movement functions
def moveUp():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"

def moveDown():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"

def moveLeft():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"

def moveRight():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"

def move():
    x, y = snakeHead.xcor(), snakeHead.ycor()
    if snakeHead.direction == "up":
        snakeHead.sety(y + 20)
    elif snakeHead.direction == "down":
        snakeHead.sety(y - 20)
    elif snakeHead.direction == "left":
        snakeHead.setx(x - 20)
    elif snakeHead.direction == "right":
        snakeHead.setx(x + 20)

wn.listen()
wn.onkeypress(moveUp, "w")
wn.onkeypress(moveDown, "s")
wn.onkeypress(moveLeft, "a")
wn.onkeypress(moveRight, "d")

# Helper functions
def resetGame():
    global currentScore, movementDelay, snakeLength
    time.sleep(1)
    snakeHead.goto(0, 0)
    snakeHead.direction = "Stop"
    for segment in snakeSegments:
        segment.goto(1000, 1000)
    snakeSegments.clear()
    currentScore = 0
    snakeLength = 1
    food.color(colorArray[0])
    scorePen.clear()
    scorePen.write(f"Score : {currentScore} High Score : {highScore}", align="center", font=("arial", 24, "bold"))

def updateScore():
    scorePen.clear()
    scorePen.write(f"Score : {currentScore} High Score : {highScore}", align="center", font=("arial", 24, "bold"))

def addSegment():
    newSegment = turtle.Turtle()
    newSegment.speed(0)
    newSegment.shape("square")
    newSegment.color(colorArray[snakeLength % len(colorArray)])  
    newSegment.penup()
    snakeSegments.append(newSegment)

def checkCollision():
    for segment in snakeSegments:
        if segment.distance(snakeHead) < 20:
            resetGame()

# Main Gameplay Loop
while True:
    wn.update()

    # Check boundary collision
    if abs(snakeHead.xcor()) > 280 or abs(snakeHead.ycor()) > 380:
        resetGame()

    if snakeHead.distance(food) < 20:
        x, y = random.randint(-14, 14) * 20, random.randint(-19, 19) * 20
        food.color(colorArray[(snakeLength + 1) % len(colorArray)])  # Change the food color
        food.goto(x, y)
        addSegment()  # Add a new segment to the snake
        snakeLength += 1
        currentScore += 10
        if currentScore > highScore:
            highScore = currentScore
        updateScore()

    # Move snake body
    for index in range(len(snakeSegments) - 1, 0, -1):
        x, y = snakeSegments[index - 1].xcor(), snakeSegments[index - 1].ycor()
        snakeSegments[index].goto(x, y)
    if snakeSegments:
        snakeSegments[0].goto(snakeHead.xcor(), snakeHead.ycor())

    move()
    checkCollision()
    time.sleep(movementDelay)

    # Save high score
    with open("snakeInfo.txt", "w") as f:
        f.write(str(highScore))

wn.mainloop()
