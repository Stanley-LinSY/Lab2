def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    string_numbers = input("Enter the numbers: ")
    x = string_numbers.split(", ")
    # print(x)
    out = []

    for numbers in x:
        out.append(float(numbers))
    return out


def find_min_max(user_entered):
    maximum = max(user_entered)
    minimum = min(user_entered)
    list_of_min_max = [int(minimum), int(maximum)]
    return list_of_min_max


def calc_average(user_entered):
    sum_of_input = sum(user_entered)
    length_of_input = len(user_entered)

    average = sum_of_input / length_of_input
    return average


display_main_menu()
user_input = get_user_input()
print("\nThe average is ", calc_average(user_input))
print("\nThe min and max are: ", find_min_max(user_input))
