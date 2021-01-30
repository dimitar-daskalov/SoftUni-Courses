def possible_combinations(names, chairs_num, combs=[]):
    if len(combs) == chairs:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        possible_combinations(names[i + 1:], chairs_num, combs)
        combs.pop()


received_names = input().split(", ")
chairs = int(input())

possible_combinations(received_names, chairs)