def sum_numbers(first, second):
    return first + second

def subtract(sum, third):
    return sum - third

def add_and_subtract(first, second, third):
    sum_of_first_and_second_integers = sum_numbers(first, second)
    result = subtract(sum_of_first_and_second_integers, third)
    return result

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
#print(*result, set = " ") - 2ри начин за отпечатване