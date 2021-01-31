import os


def create_file(name_of_the_file):
    with open(name_of_the_file, "w"):
        pass


def add_content(name_of_the_file, file_content):
    with open(name_of_the_file, "a") as file:
        file.write(file_content + "\n")


def replace_content(name_of_the_file, old_content, new_content):
    try:
        with open(name_of_the_file, "r+") as file:
            text = "".join(file.readlines())
            file.seek(0)
            file.write(text.replace(old_content, new_content))
    except FileNotFoundError:
        print("An error occurred")


def delete_file(name_of_the_file):
    if os.path.exists(name_of_the_file):
        os.remove(name_of_the_file)
    else:
        print("An error occurred")


mapper = {
    "Create": create_file,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file,
}

command = input().split("-")
while not command[0] == "End":
    action, command_arguments = command[0], command[1:]
    mapper[action](*command_arguments)
    command = input().split("-")