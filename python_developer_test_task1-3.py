# 1. Write a function that takes as a parameters number1(int), number2(int) and number3. (e.g. handle_numbers(number1, number2, number3))
# Function need to return the count of integers that are divisible by number3 in range [number1, number2]
# Example:
# number1 = 1
# number2 = 10
# number3 = 2
#
# Result:
# 5, because 2, 4, 6, 8, 10 are divisible by 2

def handle_numbers(number1, number2, number3):
    arr = []
    for i in range(number1, number2 + 1):
        arr.append(i) if i % number3 == 0 else None
    return print(str(len(arr)) + ", " + "because " +  str(arr)[1:-1] + " are divisible by " + str(number3))

# handle_numbers(1, 10, 2)

##############################################

# 2. Write a function that takes sentense as a parameter (e.g. handle_string(value)) and count number of letters and digits.
# Example:
# value = "Hello world! 123!"
#
# Result:
# Letters -  10
# Digits -  3

def handle_string(value):
    Letters, Digits = 0, 0

    for x in value:
        if x.isalpha():
            Letters += 1
        elif x.isdigit():
            Digits += 1
        else:
            pass
    return print("Letters -  " + str(Letters) + "\n" + "Digits -  " + str(Digits))

# handle_string("Hello world! 123!")

##############################################

# 3. Write a function that takes list of tuples (e.g. handle_list_of_tuples(list)) and sort it based on the next rules:
# name / age / height / weight
# Example:
list = [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
    ]
#
# Result:
# [
#     ("John", "27", "190", "87"),
#     ("Jony", "24", "191", "98"),
#     ("Jony", "24", "180", "69"),
#     ("Json", "21", "185", "75"),
#     ("Tom", "19", "167", "54"),
# ]

def handle_list_of_tuples(list):
    list_new = sorted(list, key=lambda list_s: (list_s[:][1], list_s[:][1], list_s[:][2], list_s[:][3]), reverse=True)
    return print(list_new)

handle_list_of_tuples(list)