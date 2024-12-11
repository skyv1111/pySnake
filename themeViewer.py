import turtle
import colorThemes

def display_theme(colors, themeName):
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.title(f"Theme: {themeName}")
    screenWidth = 600
    screenHeight = 400
    turtle.setup(width=screenWidth, height=screenHeight)
    num_colors = len(colors)
    width_per_color = screenWidth // num_colors
    turtle.colormode(255)
    height = screenHeight
    for i, color in enumerate(colors):
        turtle.penup()
        turtle.goto(i * width_per_color - screenWidth // 2, screenHeight // 2)
        turtle.pendown()
        turtle.begin_fill()
        turtle.color(color)
        turtle.setheading(0)
        turtle.forward(width_per_color)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width_per_color)
        turtle.right(90)
        turtle.forward(height)
        turtle.end_fill()
        turtle.tracer(0)
    turtle.done()

themesDictionary = {
    "Rainbow": colorThemes.rainbow,
}

def chooseTheme():
    print("Available Themes:")
    for i, theme in enumerate(themesDictionary.keys(), start=1):
        print(f"{i}. {theme}")
    
    while True:
        try:
            choice = int(input("Enter the number of the theme you want to view: "))
            if 1 <= choice <= len(themesDictionary):
                themeName = list(themesDictionary.keys())[choice - 1]
                themeColors = themesDictionary[themeName]
                display_theme(themeColors, themeName)
                break
            else:
                print(f"Invalid input! Please choose a number between 1 and {len(themesDictionary)}.")
        except ValueError:
            print("Please enter a valid number.")

chooseTheme()
