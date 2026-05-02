def add_two_numbers() -> int:
    string_nums = input()
    string_list = string_nums.split(",")
    num1 = int(string_list[0])
    num2 = int(string_list[1])
    return num1 + num2



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
