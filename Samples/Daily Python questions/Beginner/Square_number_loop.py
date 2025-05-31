# This project continually asks for a number, it then gives the square of the number given

phrase = "Give me a number!: "

while True:
        requested_number = input(phrase)
        number = float(requested_number)  # Convert input to a float to handle decimals
        square = number ** 2
        print(f"The square of {number} is: {square}")
    








