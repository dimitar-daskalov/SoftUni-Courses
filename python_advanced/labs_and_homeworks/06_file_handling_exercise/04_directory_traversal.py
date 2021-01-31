import os

dir_content = os.listdir("exercises_test_files")

extracted_files = [file for file in dir_content if "." in file]

report_information = {}
for file in extracted_files:
    file_name, file_extension = os.path.splitext(file)
    if file_extension not in report_information:
        report_information[file_extension] = []
    report_information[file_extension].append(file_name)

result_received = ""
for file_extensions, file_names in sorted(report_information.items()):
    result_received += f"{file_extensions}\n"
    for file_n in file_names:
        result_received += f"- - - {file_n}{file_extensions}\n"

file_name = "report.txt"
path_to_desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
directory = os.path.join(path_to_desktop, file_name)

with open(directory, "w") as file:
    file.write(result_received)
