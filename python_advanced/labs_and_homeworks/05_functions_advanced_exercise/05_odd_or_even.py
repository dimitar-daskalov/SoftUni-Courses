def commands(received_command, nums):
    commands_mapper = {
        "Odd": filter(lambda x: x % 2 != 0, nums),
        "Even": filter(lambda x: x % 2 == 0, nums),
    }
    return sum(commands_mapper[received_command]) * len(nums)


command = input()
numbers = [int(el) for el in input().split()]
print(commands(command, numbers))


