def expressions(nums_received, current_sum=0, expression=""):
    if not nums_received:
        return [(expression, current_sum)]

    result_plus = expressions(nums_received[1:], current_sum+nums_received[0], f"{expression}+{nums_received[0]}")
    result_minus = expressions(nums_received[1:], current_sum-nums_received[0], f"{expression}-{nums_received[0]}")
    return result_plus + result_minus


nums = [int(el) for el in input().split(", ")]
print(*[f"{el[0]}={el[1]}" for el in expressions(nums)], sep="\n")