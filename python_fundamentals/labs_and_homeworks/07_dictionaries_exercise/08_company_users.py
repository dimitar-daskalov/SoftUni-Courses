command = input()

companies_employees = {}
while not command == "End":
    company_name, user_id = command.split(" -> ")
    if company_name not in companies_employees:
        user_id = [user_id]
        companies_employees[company_name] = user_id
    else:
        if user_id not in companies_employees[company_name]:
            companies_employees[company_name].append(user_id)
    command = input()

ordered_companies = dict(sorted(companies_employees.items(), key=lambda x: x[0]))

for key in ordered_companies:
    print(f"{key}")
    for el in ordered_companies[key]:
        print(f"-- {el}")