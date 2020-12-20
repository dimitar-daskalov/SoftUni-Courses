string_received = input().split("\\")

last_element = string_received[-1]
file_name, file_extension = last_element.split(".")

print(f"File name: {file_name}", f"File extension: {file_extension}", sep="\n")