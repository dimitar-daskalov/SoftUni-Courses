countries = input().split(", ")
capitals = input().split(", ")

countries_capitals = zip(countries, capitals)
print('\n'.join([f"{el[0]} -> {el[1]}" for el in countries_capitals]))