key = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {key}")
        break
    if command[0] == "Slice":
        key = key[:int(command[1])] + key[int(command[2]):]
        print(key)
    elif command[0] == "Flip":
        if command[1] == "Upper":
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].upper() + key[int(command[3]):]
        else:
            key = key[:int(command[2])] + key[int(command[2]):int(command[3])].lower() + key[int(command[3]):]
        print(key)
    elif command[0] == "Contains":
        if command[1] in key:
            print(f"{key} contains {command[1]}")
        else:
            print(f"Substring not found!")