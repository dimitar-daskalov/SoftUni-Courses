class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")

command = input()
while not command == "End":
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    email_name, email_site_domain = command.split("@")
    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if "." not in email_site_domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    email_site, domain = email_site_domain.split(".")
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    command = input()

