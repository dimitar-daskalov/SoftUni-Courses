number = float(input())
input_numeric_text = input()
output_numeric_text = input()

if input_numeric_text == "mm" and output_numeric_text == "m":
    print(f"{number / 1000:.3f}")
elif input_numeric_text == "mm" and output_numeric_text == "cm":
    print(f"{number / 10:.3f}")
elif input_numeric_text == "m" and output_numeric_text == "mm":
    print(f"{number * 1000:.3f}")
elif input_numeric_text == "m" and output_numeric_text == "cm":
    print(f"{number * 100:.3f}")
elif input_numeric_text == "cm" and output_numeric_text == "m":
    print(f"{number / 100:.3f}")
elif input_numeric_text == "cm" and output_numeric_text == "mm":
    print(f"{number * 10:.3f}")