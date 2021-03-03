# def transform_roman_to_int(value):
#     value = value.upper()
#     ROMAN_NUMS = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#     summed_values = 0
#     for i in range(len(value)):
#         current_value = ROMAN_NUMS[value[i]]
#         if i + 1 < len(value) and ROMAN_NUMS[value[i + 1]] > current_value:
#             summed_values -= current_value
#         else:
#             summed_values += current_value
#     return summed_values

from roman import fromRoman


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        if not isinstance(value, float):
            return "value is not a float"

        value = int(value)
        return cls(value)

    @classmethod
    def from_roman(cls, value: str):
        # value = transform_roman_to_int(value)
        value = fromRoman(value)
        return cls(value)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"

        value = int(value)
        return cls(value)

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"

        result = self.value + integer.value
        return result

    def __str__(self):
        return str(self.value)


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))

