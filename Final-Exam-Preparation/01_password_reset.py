def take_odd(raw_pass):
    result = ""
    for index in range(1, len(raw_pass), 2):
        result += raw_pass[index]
    print(result)
    return result


def cut(raw_pass, i, length):
    result = raw_pass[:i] + raw_pass[i + length:]
    print(result)
    return result


def substitute(raw_pass, sub_str, repl):
    result = raw_pass.replace(sub_str, repl)
    if result == raw_pass:
        print("Nothing to replace!")
    else:
        print(result)
    return result


password = input()

line = input()

while not line == "Done":
    data = line.split(' ')
    command = data[0]
    if command == "TakeOdd":
        password = take_odd(password)
    elif command == "Cut":
        index, length = [int(el) for el in data[1:]]
        password = cut(password, index, length)
    elif command == "Substitute":
        sub_str, replacement = data[1:]
        password = substitute(password, sub_str, replacement)
    line = input()

print(f"Your password is: {password}")

#Втори начин:
# def password_reset():
#     data = input()
#
#     while True:
#         command = input().split(' ')
# 
#         current_command = command[0]
#
#         if current_command == 'Done':
#             print(f'Your password is: {data}')
#             break
#
#         elif current_command == 'TakeOdd':
#             data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
#             print(data)
#
#         elif current_command == 'Cut':
#             index = int(command[1])
#             length = int(command[2])
#             data = ''.join([data[i] for i in range(len(data)) if i < index or i >= index + length])
#             print(data)
#
#         elif current_command == 'Substitute':
#             substring = command[1]
#             substitute = command[2]
#
#             if substring in data:
#                 data = data.replace(substring, substitute)
#                 print(data)
#             else:
#                 print("Nothing to replace!")
#
#
# password_reset()