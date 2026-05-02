def divide_numbers(a: int, b: int) -> None:
    try:
        result = a / b
    except:
        print("An error occurred!")
    if b >= 1 or b < 0:
        print(result)



# do not modify below this line
divide_numbers(10, 2)
divide_numbers(12, 3)
divide_numbers(2, 0)
