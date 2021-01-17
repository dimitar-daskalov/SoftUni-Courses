person_info = input()

phonebook_dict = {}

while not person_info.isdigit():
    name, phone_number = person_info.split("-")
    phonebook_dict[name] = phone_number
    person_info = input()

for _ in range(int(person_info)):
    name_received = input()
    if name_received in phonebook_dict:
        print(f"{name_received} -> {phonebook_dict[name_received]}")
    else:
        print(f"Contact {name_received} does not exist.")