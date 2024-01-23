import turtle


def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)


def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")

    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    size = 400

    turtle.penup()
    turtle.goto(-size / 2, size / 2)
    turtle.pendown()

    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

    turtle.done()


if __name__ == "__main__":
    main()
