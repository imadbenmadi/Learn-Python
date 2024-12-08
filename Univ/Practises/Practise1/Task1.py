try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    result = (a + b > c) and (a + c > b) and (b + c > a)
    messages = [
        "The three given numbers are not valid sides of a triangle using the triangle inequality theorem.",
        "The three given numbers are valid sides of a triangle using the triangle inequality theorem."
    ]

    print(messages[result])

except ValueError:
    print("Please enter valid numbers " )
