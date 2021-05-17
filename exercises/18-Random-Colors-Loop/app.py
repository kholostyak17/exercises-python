import random


def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher = {
        0: 'red',
        1: 'yellow',
        2: 'blue',
        3: 'green',
        4: 'black'
    }
    return switcher.get(color_number, "Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = [None for i in range(10)]
    # your loop here
    for i in range(10):
        students_array[i] = get_color(random.randint(1, 4))
    return students_array


print(get_allStudentColors())
