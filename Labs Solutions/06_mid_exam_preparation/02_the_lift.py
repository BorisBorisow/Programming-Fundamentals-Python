def lift_func(waiting_people, current_state_of_the_lift):
    for i in range(len(current_state_of_the_lift)):
        if waiting_people > 3:
            current_number_of_people = abs(4 - int(current_state_of_the_lift[i]))
            waiting_people -= current_number_of_people
            current_state_of_the_lift[i] += current_number_of_people
        else:
            current_state_of_the_lift[i] += waiting_people
            waiting_people = 0

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
        print(f"The lift has empty spots!")

    print(' '.join([str(num) for num in current_state_of_the_lift]))


number_of_people = int(input())
lift_condition = list(map(int, input().split(' ')))
lift_func(number_of_people, lift_condition)

# people = int(input())
# lift = list(map(int, input().split(' ')))
#
# for i in range(len(lift)):
#     can_load = min(4 - lift[i], people)
#     lift[i] += can_load
#     people -= can_load
#
# if people > 0:
#     print(f"There isn't enough space! {people} people in a queue!")
# elif len([cart for cart in lift if cart < 4]) > 0:
#     print("The lift has empty spots!")
#
# print(" ".join([str(cart) for cart in lift]))

