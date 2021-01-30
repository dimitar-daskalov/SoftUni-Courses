def age_assignment(*names, **kwargs):
    names_with_years = {}
    for name in names:
        for key, value in kwargs.items():
            if name.startswith(key):
                names_with_years[name] = value
    return names_with_years

