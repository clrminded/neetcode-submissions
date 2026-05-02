from typing import List

def read_integers() -> List[int]:
    input_string = input()
    string_list = input_string.split(",")
    my_list = []
    for string in string_list:
        my_list.append(int(string))
    return my_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
